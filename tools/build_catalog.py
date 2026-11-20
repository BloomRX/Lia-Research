#!/usr/bin/env python3
"""Gera `catalog/catalog.tsv` a partir dos cabeçalhos de `repositories/*/REPORT.md`.

    python3 tools/build_catalog.py           # escreve catalog/catalog.tsv
    python3 tools/build_catalog.py --check    # só compara, sai 1 se divergir

O TSV é derivado, nunca editado à mão: a fonte de verdade é o cabeçalho de
cada REPORT.md (`catalog/CATALOG-SCHEMA.md`).
"""
from __future__ import annotations

import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "catalog/catalog.tsv")
COLS = ["id", "objeto", "caminho", "tipo", "estado_pesquisa", "resultado_execucao",
        "recomendacao", "licenca", "categoria", "data", "ultima_verificacao",
        "proxima_revisao", "upstream_conferido", "divergencia_upstream"]


def header(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    started = False
    for line in text.split("\n"):
        if line.startswith("|"):
            started = True
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] != "Campo" and not set(cells[0]) <= {"-", ":"}:
                fields.setdefault(cells[0], cells[1])
        elif started:
            break
    return fields


def clean(v: str) -> str:
    v = v.replace("\t", " ").strip()
    return v.replace("**", "").replace("`", "").strip()


def rows() -> list[list[str]]:
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "repositories/*/REPORT.md"))):
        text = open(path, encoding="utf-8").read()
        f = header(text)
        slug = os.path.basename(os.path.dirname(path))
        rec = clean(f.get("Recomendação", ""))
        found = [(rec.find(t), t) for t in ("DIRECT_INTEGRATION_CANDIDATE", "ADAPT",
                 "FORK_CANDIDATE", "INDEPENDENT_REIMPLEMENTATION", "REFERENCE_ONLY",
                 "REJECT", "INSUFFICIENT_EVIDENCE") if t in rec]
        token = min(found)[1] if found else "INSUFFICIENT_EVIDENCE"
        out.append([
            clean(f.get("ID", "")), slug, f"repositories/{slug}/REPORT.md",
            clean(f.get("Tipo", "repositorio")),
            clean(f.get("Estado da pesquisa", "")).split(" ")[0],
            clean(f.get("Resultado de execução", "")).split(" ")[0],
            token,
            clean(f.get("Licença", ""))[:80],
            clean(f.get("Categoria", "")),
            clean(f.get("Data", "")),
            clean(f.get("Última verificação", "")),
            clean(f.get("Próxima revisão", "")),
            clean(f.get("Upstream conferido", "")).split("·")[0].strip(),
            "SIM" if "mudou desde a análise" in f.get("Upstream conferido", "") else "nao",
        ])
    return out


def render(data: list[list[str]]) -> str:
    lines = ["\t".join(COLS)]
    lines += ["\t".join(r) for r in data]
    return "\n".join(lines) + "\n"


def main() -> int:
    data = rows()
    text = render(data)
    if "--check" in sys.argv:
        current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if current != text:
            print("catalog.tsv desatualizado: rode python3 tools/build_catalog.py")
            return 1
        print(f"catalog.tsv em dia ({len(data)} linhas)")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(text)
    print(f"catalog/catalog.tsv: {len(data)} objetos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
