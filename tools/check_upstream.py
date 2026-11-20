#!/usr/bin/env python3
"""Re-auditoria de upstream: confere cada objeto do catálogo contra o GitHub.

    python3 tools/check_upstream.py write   # escreve data/inventory/upstream-reaudit-<data>.tsv
    python3 tools/check_upstream.py          # imprime na tela

Faz só leitura pública (`gh api`, sem credencial pessoal, sem clone). Registra
existência, branch padrão, SHA atual, licença declarada pela API, data do último
push e se o objeto mudou desde a versão analisada. Não altera nenhum relatório:
a atualização de `Última verificação` é decisão humana.
"""
from __future__ import annotations

import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-11-20"
OUT = os.path.join(ROOT, "data/inventory/upstream-reaudit-%s.tsv" % DATE)

EXTRA = {
    "ai-memory": "akitaonrails/ai-memory",
    "cloudflare-security-audit-skill": "cloudflare/security-audit-skill",
    "freellmapi": "tashfeenahmed/freellmapi",
    "rescript-lang": "rescript-lang/rescript",
    "routerhub": "routerhubSI/litellm",
}
# Onde a pasta usa outro nome que o repositório analisado.
NOTE = {"artcraft": "pasta 'artcraft', upstream storytold/photocraft"}


def gh(args: list[str]) -> str:
    try:
        return subprocess.run(["gh"] + args, capture_output=True, text=True, timeout=60).stdout
    except subprocess.TimeoutExpired:
        return ""


def objects() -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "repositories/*/REPORT.md"))):
        slug = os.path.basename(os.path.dirname(p))
        text = open(p, encoding="utf-8").read()
        m = re.search(r"`([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)@([0-9a-f]{7,40})", text)
        if m:
            out[slug] = (f"{m.group(1)}/{m.group(2)}", m.group(3))
        elif slug in EXTRA:
            out[slug] = (EXTRA[slug], "")
        else:
            out[slug] = ("?", "")
    return out


def main() -> int:
    rows = [["pasta", "upstream", "existe", "branch", "sha_analisado", "sha_atual",
             "mudou", "licenca_api", "pushed_at", "arquivado", "estrelas", "nota"]]
    for slug, (repo, sha) in objects().items():
        raw = gh(["api", f"repos/{repo}"])
        try:
            meta = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            meta = {}
        if not meta or meta.get("message"):
            rows.append([slug, repo, "NAO", "", sha[:12], "", "", "", "", "", "", "API: " + str(meta.get("message", "sem resposta"))])
            continue
        branch = meta.get("default_branch", "")
        cur = ""
        if branch:
            j = gh(["api", f"repos/{repo}/commits/{branch}", "--jq", ".sha"])
            cur = j.strip()
        lic = (meta.get("license") or {}).get("spdx_id") or "SEM_LICENCA_DETECTADA"
        mudou = "SIM" if sha and cur and not cur.startswith(sha[:7]) else ("nao" if sha else "sem-sha")
        rows.append([slug, repo, "SIM", branch, sha[:12], cur[:12], mudou, lic,
                     (meta.get("pushed_at") or "")[:10], "SIM" if meta.get("archived") else "nao",
                     str(meta.get("stargazers_count", "")), NOTE.get(slug, "")])
    text = "\n".join("\t".join(r) for r in rows) + "\n"
    if "write" in sys.argv:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        open(OUT, "w", encoding="utf-8").write(text)
        print(f"escrito: {os.path.relpath(OUT, ROOT)} ({len(rows) - 1} objetos)")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
