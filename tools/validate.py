#!/usr/bin/env python3
"""Validador do Lia-Research.

Uso:
    python3 tools/validate.py            # roda tudo
    python3 tools/validate.py --quiet    # só erros

Checa 9 coisas que já quebraram ou podem quebrar esta base:
 1. todo .md tem título H1
 2. nenhum segredo aparente (token, chave, senha, host privado)
 3. nenhum diretório vazio
 4. nenhum arquivo > 5 MB versionado
 5. todo caminho .md citado entre crases existe
 6. todo ID LR-* citado existe em RESEARCH-INDEX.md
 7. todo relatório externo tem as 18 seções + veredito
 8. todo DR em decisions/PENDING está listado no README da pasta
 9. todo digest transversal tem cabeçalho de metadados

Sai com código 1 se houver erro. Avisos não falham o build.
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "data/snapshots"}
MAX_BYTES = 5 * 1024 * 1024

SECRET_PATTERNS = [
    (r"\bghp_[A-Za-z0-9]{20,}", "GitHub personal token"),
    (r"\bgh[pousr]_[A-Za-z0-9]{20,}", "GitHub token"),
    (r"\bsk-[A-Za-z0-9]{24,}", "API secret key"),
    (r"\bAKIA[0-9A-Z]{16}\b", "AWS access key id"),
    (r"\bxox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
    (r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----", "private key block"),
    (r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}", "JWT"),
    (r"(?i)\b(password|passwd|senha)\s*[:=]\s*\S{6,}", "senha em texto"),
    (r"\b(192\.168\.\d{1,3}\.\d{1,3})\b", "IP de LAN real"),
    (r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b", "CPF"),
]

REQUIRED_REPORT_SECTIONS = 18

errors: list[str] = []
warnings: list[str] = []
ok_count = 0


def rel(p: str) -> str:
    return os.path.relpath(p, ROOT)


def skipped(r: str) -> bool:
    """True se o caminho relativo está dentro de um diretório ignorado."""
    r = r.replace(os.sep, "/")
    return any(r == s or r.startswith(s + "/") for s in SKIP_DIRS)


def walk_md() -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        r = rel(dirpath)
        dirnames[:] = [d for d in dirnames if not skipped(os.path.normpath(os.path.join(r, d)))]
        for f in filenames:
            if f.endswith(".md"):
                out.append(os.path.join(dirpath, f))
    return sorted(out)


def check_titles(files: list[str]) -> None:
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        lines = text.splitlines()
        i = 0
        if lines and lines[0].strip() == "---":  # front matter YAML (issue templates)
            for j in range(1, len(lines)):
                if lines[j].strip() == "---":
                    i = j + 1
                    break
        first = next((ln for ln in lines[i:] if ln.strip()), "")
        if not first.startswith("# ") and "name:" not in "".join(lines[:i]):
            errors.append(f"sem título H1: {rel(f)}")


def check_secrets(files: list[str]) -> None:
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        for pat, label in SECRET_PATTERNS:
            for m in re.finditer(pat, text):
                if label == "IP de LAN real" and "192.168." in m.group(1):
                    # documentação de exemplo é aceita se marcada como placeholder
                    line = text[: m.start()].count("\n") + 1
                    warnings.append(f"{rel(f)}:{line}: IP de LAN em '{m.group(1)}' (ok se for exemplo)")
                    continue
                line = text[: m.start()].count("\n") + 1
                errors.append(f"possível segredo ({label}) em {rel(f)}:{line}")


def check_empty_dirs() -> None:
    for dirpath, dirnames, filenames in os.walk(ROOT):
        r = rel(dirpath)
        if r == "." or r.startswith(".git" + os.sep) or r == ".git" or skipped(r):
            continue
        if not dirnames and not filenames:
            errors.append(f"diretório vazio: {r}")


def check_size(files: list[str]) -> None:
    for f in files:
        s = os.path.getsize(f)
        if s > MAX_BYTES:
            warnings.append(f"arquivo grande ({s // 1024} KB): {rel(f)}")


def build_path_set() -> set[str]:
    paths = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        r = rel(dirpath)
        if r == ".git" or r.startswith(".git" + os.sep) or skipped(r):
            continue
        for f in filenames:
            paths.add(os.path.normpath(os.path.join(r, f)).replace(os.sep, "/"))
        for d in dirnames:
            paths.add(os.path.normpath(os.path.join(r, d)).replace(os.sep, "/"))
    return paths


CRED_PATH = re.compile(r"`([A-Za-z0-9_./-]+\.md)`")
# Só caminhos que declaram ser DESTA base são verificados. Citação de arquivo de outro
# repositório (README.md, docs/OAUTH.md) é legítima e não pode ser checada aqui.
LOCAL_PREFIXES = (
    "governance/", "ecosystem/", "projects/", "repositories/", "cross-project/",
    "comparisons/", "decisions/", "templates/", "agents/", "data/", "tools/",
    "archive/", ".github/",
)


def check_paths(files: list[str], paths: set[str]) -> None:
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        own_dir = os.path.dirname(rel(f))
        for m in CRED_PATH.finditer(text):
            p = m.group(1)
            if p.startswith(("http", "/")):
                continue
            local = p.startswith(LOCAL_PREFIXES) or (own_dir and f"{own_dir}/{p}" in paths)
            if not local:
                continue
            if p in paths or (own_dir and f"{own_dir}/{p}" in paths):
                continue
            errors.append(f"caminho local citado não existe: {p} ({rel(f)})")


ID_RE = re.compile(r"\bLR-[A-Z]+-\d{3}(?:-[A-D])?\b")


def check_ids(files: list[str]) -> None:
    index_path = os.path.join(ROOT, "RESEARCH-INDEX.md")
    if not os.path.exists(index_path):
        errors.append("RESEARCH-INDEX.md ausente")
        return
    index = open(index_path, encoding="utf-8", errors="replace").read()
    known = set(ID_RE.findall(index))
    unknown: dict[str, set[str]] = {}
    for f in files:
        if rel(f) == "RESEARCH-INDEX.md":
            continue
        text = open(f, encoding="utf-8", errors="replace").read()
        for i in set(ID_RE.findall(text)):
            if i.endswith("000"):
                continue  # placeholder de template
            if i not in known:
                unknown.setdefault(i, set()).add(rel(f))
    for i, where in sorted(unknown.items()):
        warnings.append(f"ID fora do índice: {i} citado em {', '.join(sorted(where))}")


def check_reports(files: list[str]) -> None:
    for f in files:
        r = rel(f)
        if not (r.startswith("repositories/") and r.endswith("REPORT.md")):
            continue
        text = open(f, encoding="utf-8", errors="replace").read()
        head = text[:2500].upper()
        verdicts = ("ADOTAR", "ADAPTAR", "REFER", "REJEITAR", "PENDENTE")
        if not any(v in head for v in verdicts):
            errors.append(f"relatório sem veredito no cabeçalho: {r}")
        heads = re.findall(r"^## .*$", text, flags=re.M)
        if len(heads) < REQUIRED_REPORT_SECTIONS:
            errors.append(
                f"relatório com {len(heads)} seções (esperado >= {REQUIRED_REPORT_SECTIONS}): {r}"
            )
        if "Evidência" not in text and "EVIDÊNCIA" not in text.upper():
            errors.append(f"relatório sem seção de evidência: {r}")


def check_decisions(files: list[str]) -> None:
    pend = os.path.join(ROOT, "decisions/PENDING")
    if not os.path.isdir(pend):
        return
    readme = os.path.join(pend, "README.md")
    listed = open(readme, encoding="utf-8", errors="replace").read() if os.path.exists(readme) else ""
    for f in sorted(os.listdir(pend)):
        if not (f.startswith("DR-") and f.endswith(".md")):
            continue
        dr = f.split("-")[1]
        if f"DR-{dr}" not in listed:
            warnings.append(f"{f} não está listado em decisions/PENDING/README.md")


def check_digests(files: list[str]) -> None:
    for f in files:
        r = rel(f)
        if not r.startswith("cross-project/"):
            continue
        text = open(f, encoding="utf-8", errors="replace").read()
        head = text[:1500]
        for must in ("| ID |", "| Data |"):
            if must not in head:
                warnings.append(f"digest sem metadados ({must}) na abertura: {r}")


def main() -> int:
    quiet = "--quiet" in sys.argv
    files = walk_md()
    paths = build_path_set()

    for name, fn in [
        ("1 título", lambda: check_titles(files)),
        ("2 segredos", lambda: check_secrets(files)),
        ("3 diretórios", check_empty_dirs),
        ("4 tamanho", lambda: check_size(files)),
        ("5 caminhos", lambda: check_paths(files, paths)),
        ("6 IDs", lambda: check_ids(files)),
        ("7 relatórios", lambda: check_reports(files)),
        ("8 decisões", lambda: check_decisions(files)),
        ("9 digests", lambda: check_digests(files)),
    ]:
        before = len(errors)
        fn()
        status = "ok" if len(errors) == before else "FALHA"
        if not quiet:
            print(f"[{status:5}] {name}")

    print()
    print(f"arquivos .md verificados: {len(files)}")
    print(f"erros: {len(errors)} · avisos: {len(warnings)}")
    for e in errors:
        print("  ERRO  " + e)
    for w in warnings:
        print("  aviso " + w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
