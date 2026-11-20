#!/usr/bin/env python3
"""Normaliza o cabeçalho dos relatórios existentes ao esquema do catálogo.

Uso:
    python3 tools/migrate_reports.py --dry-run
    python3 tools/migrate_reports.py

Regras (catalog/CATALOG-SCHEMA.md):
- vocabulário antigo de recomendação é traduzido, nunca promovido;
- estado da pesquisa e resultado de execução passam a ser campos próprios;
- `decisao_de_adocao` fica vazio quando não há decisão registrada.
"""
import glob
import re
import sys

MAP_REC = {
    "ADOTAR": "DIRECT_INTEGRATION_CANDIDATE",
    "ADAPTAR": "ADAPT",
    "REFERÊNCIA": "REFERENCE_ONLY",
    "REFERENCIA": "REFERENCE_ONLY",
    "REJEITAR": "REJECT",
}
ESTADOS = {"DISCOVERED", "TRIAGED", "INVESTIGATING", "DOCUMENTED", "TESTED",
           "PARTIALLY_TESTED", "NOT_TESTED", "BLOCKED", "STALE",
           "SUPERSEDED", "CONFLICTING"}


def rows(lines):
    return [l for l in lines if l.startswith("|")]


def get(rows_, field):
    for r in rows_:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if cells and cells[0] == field:
            return cells[1] if len(cells) > 1 else ""
    return None


def set_row(block, field, value):
    """Substitui a linha do campo ou devolve None se não existir."""
    for i, r in enumerate(block):
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if cells and cells[0] == field:
            block[i] = f"| {field} | {value} |"
            return True
    return False


def insert_after(block, after, field, value):
    for i, r in enumerate(block):
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if cells and cells[0] == after:
            block.insert(i + 1, f"| {field} | {value} |")
            return True
    return False


def migrate(path, dry=False):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    # localiza o bloco de tabela do cabeçalho (primeiro bloco de linhas '|')
    start = next((i for i, l in enumerate(lines) if l.startswith("|")), None)
    if start is None:
        return "sem tabela de cabeçalho"
    end = start
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    block = lines[start:end]

    if get(block, "Estado da pesquisa") is not None:
        return "já migrado"

    old_status = get(block, "Status") or ""
    old_rec = get(block, "Recomendação") or ""
    changed = []

    # 1. traduz TODAS as recomendações citadas, preservando o texto original
    def translate(t):
        for k, v in MAP_REC.items():
            t = re.sub(rf"\b{re.escape(k)}\b", v, t)
        return t

    new_rec = translate(old_rec) if old_rec else "INSUFFICIENT_EVIDENCE"
    set_row(block, "Recomendação", new_rec)
    changed.append(f"recomendação: {old_rec.split()[0] if old_rec else '-'} → {new_rec.split()[0]}")

    # 2. estado da pesquisa a partir do Status antigo
    estado = "DOCUMENTED"
    if "HISTORICAL" in old_status:
        estado = "STALE"
    elif "SUPERSEDED" in old_status:
        estado = "SUPERSEDED"
    elif "CONFLICTING" in old_status:
        estado = "CONFLICTING"

    # 3. insere campos novos na ordem canônica
    if get(block, "Tipo") is None:
        insert_after(block, "ID", "Tipo", "repositorio")
    insert_after(block, "Tipo", "Estado da pesquisa", estado)
    insert_after(block, "Estado da pesquisa", "Resultado de execução", "STATIC_REVIEW_ONLY")
    # move Recomendação para logo após Resultado? mantém onde está (após projetos) se existir
    insert_after(block, "Resultado de execução", "Decisão de adoção", "— (nenhuma registrada)")
    if get(block, "Última verificação") is None:
        insert_after(block, "Data", "Última verificação", "2026-11-20")
    # remove Status (substituído por Estado da pesquisa)
    block = [r for r in block if not r.strip().startswith("| Status |")]

    new_lines = lines[:start] + block + lines[end:]
    # 2. corpo: 'VEREDITO: `X`' passa a 'Recomendação: `NOVO`' (mantém sentido, tira o tom de veredito)
    body = "\n".join(new_lines)
    body = re.sub(r"\*\*VEREDITO: (`?)\*?\*?\s*", "**Recomendação (opinião técnica, não é aprovação): ** ", body)
    body = translate(body)
    out = body
    if not dry:
        open(path, "w", encoding="utf-8").write(out)
    return "; ".join(changed) or "sem mudança"


def main():
    dry = "--dry-run" in sys.argv
    n = 0
    for p in sorted(glob.glob("repositories/*/REPORT.md")):
        msg = migrate(p, dry)
        print(f"{p}: {msg}")
        n += 1
    print(f"\n{n} relatórios processados{' (dry-run)' if dry else ''}")


if __name__ == "__main__":
    main()
