#!/usr/bin/env python3
"""Validador estrutural do Lia-Research.

    python3 tools/validate.py            # relatório completo
    python3 tools/validate.py --quiet    # só erros
    python3 tools/validate.py --json     # saída de máquina

Três níveis:
  ERRO   — bloqueia publicação
  AVISO  — conteúdo/qualidade a revisar
  NOTA   — pendência externa legítima (BLOCKED, NOT_RUN, pesquisa vencida)

Regras em `catalog/CATALOG-SCHEMA.md` e `agents/PUBLISHING-PROTOCOL.md`.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = dt.date(2026, 11, 20)
SKIP_DIRS = {".git", "node_modules", "archive/historical"}

RECS = {"DIRECT_INTEGRATION_CANDIDATE", "ADAPT", "FORK_CANDIDATE",
        "INDEPENDENT_REIMPLEMENTATION", "REFERENCE_ONLY", "REJECT",
        "INSUFFICIENT_EVIDENCE"}
STATES = {"DISCOVERED", "TRIAGED", "INVESTIGATING", "DOCUMENTED", "TESTED",
          "PARTIALLY_TESTED", "NOT_TESTED", "BLOCKED", "STALE", "SUPERSEDED",
          "CONFLICTING"}
EXEC = {"NOT_RUN", "STATIC_REVIEW_ONLY", "OFFICIAL_CI_REVIEWED", "LOCAL_SMOKE_PASS",
        "LOCAL_TESTS_PASS", "LOCAL_TESTS_FAIL", "PARTIAL", "BLOCKED"}
OLD_VOCAB = ("ADOTAR", "ADAPTAR", "REJEITAR")
REPORT_FIELDS = ("| ID |", "| Tipo |", "| Estado da pesquisa |",
                 "| Resultado de execução |", "| Recomendação |",
                 "| Decisão de adoção |", "| Licença |")
SECRETS = (
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)\bpassword\s*[:=]\s*\S{6,}"),
)

errors: list[str] = []
warnings: list[str] = []
notes: list[str] = []


def rel(p: str) -> str:
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def walk_md() -> list[str]:
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and d != ".git"]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.join(base, f))
    return sorted(out)


def header_block(text: str) -> dict[str, str]:
    """Campos do primeiro bloco de tabela do documento."""
    fields: dict[str, str] = {}
    started = False
    for line in text.split("\n"):
        if line.startswith("|"):
            started = True
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] not in ("Campo", "---") and not set(cells[0]) <= {"-", ":"}:
                fields.setdefault(cells[0], cells[1])
        elif started:
            break
    return fields


# ---------------------------------------------------------------- checks
INTERNAL_ROOTS = ("governance/", "catalog/", "templates/", "data/", "tools/",
                  "agents/", "decisions/", "cross-project/", "repositories/",
                  "archive/")


def check_titles(files: list[str]) -> None:
    seen: dict[str, str] = {}
    for f in files:
        r = rel(f)
        if r.startswith(".github/"):
            continue
        text = open(f, encoding="utf-8", errors="replace").read()
        m = re.search(r"^# (.+)$", text, flags=re.M)
        if not m:
            errors.append(f"sem título H1: {r}")
            continue
        t = m.group(1).strip()
        if t in seen:
            errors.append(f"título duplicado: '{t}' em {r} e {seen[t]}")
        seen[t] = r


def check_secrets(files: list[str]) -> None:
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        for pat in SECRETS:
            m = pat.search(text)
            if m:
                errors.append(f"possível segredo em {rel(f)}: {m.group(0)[:12]}…")


def check_empty_dirs() -> None:
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        if base == ROOT:
            continue
        if not dirs and not files:
            warnings.append(f"diretório vazio: {rel(base)}")


def check_sizes(files: list[str]) -> None:
    for f in files:
        size = os.path.getsize(f)
        if size > 2 * 1024 * 1024:
            errors.append(f"documento > 2 MB: {rel(f)}")
        elif size > 250 * 1024:
            warnings.append(f"documento grande ({size // 1024} KB): {rel(f)}")


def check_local_paths(files: list[str]) -> None:
    """Só valida caminhos internos deste repositório.

    Caminhos de terceiros (`docs/mcp.md` do repo pesquisado, por exemplo) são
    citações, não links: ficam de fora para o validador não inventar erros.
    """
    for f in files:
        r = rel(f)
        text = open(f, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"`([A-Za-z0-9_./-]+\.(?:md|tsv|py|json|txt))`", text):
            p = m.group(1)
            if p.startswith(("http", "~/")) or "*" in p:
                continue
            if not p.startswith(INTERNAL_ROOTS):
                continue
            if not os.path.exists(os.path.join(ROOT, p)):
                errors.append(f"caminho interno citado não existe: {p} ({r})")


def check_md_links(files: list[str]) -> None:
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = m.group(1).split("#")[0]
            if not target or target.startswith(("http", "mailto:", "#")):
                continue
            if not target.endswith(".md"):
                continue
            if not os.path.exists(os.path.join(os.path.dirname(f), target)):
                errors.append(f"link .md quebrado: {target} ({rel(f)})")


def check_ids(files: list[str]) -> None:
    index = open(os.path.join(ROOT, "RESEARCH-INDEX.md"), encoding="utf-8").read()
    registered = set(re.findall(r"`(LR-[A-Z]+-\d+)`", index))
    defined: dict[str, str] = {}
    for f in files:
        if rel(f).startswith("templates/"):
            continue
        text = open(f, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"^\| ID \| `(LR-[A-Z]+-\d+)`", text, flags=re.M):
            i = m.group(1)
            if "XXX" in i or i.endswith("-000"):
                continue  # placeholder de template
            if i in defined:
                errors.append(f"ID duplicado: {i} em {rel(f)} e {defined[i]}")
            defined[i] = rel(f)
    for i in sorted(defined):
        if i not in registered:
            errors.append(f"ID não registrado no RESEARCH-INDEX: {i} ({defined[i]})")
    for i in sorted(registered - set(defined)):
        notes.append(f"ID no índice sem documento com cabeçalho próprio: {i}")


def check_report_schema(files: list[str]) -> None:
    for f in files:
        r = rel(f)
        if not (r.startswith("repositories/") and r.endswith("REPORT.md")):
            continue
        text = open(f, encoding="utf-8", errors="replace").read()
        head = text[:3000]
        fields = header_block(text)
        for fld in REPORT_FIELDS:
            if fld not in head:
                errors.append(f"relatório sem campo obrigatório {fld.strip('| ')}: {r}")
        rec = fields.get("Recomendação", "")
        token = next((t for t in RECS if t in rec), None)
        if not token:
            errors.append(f"recomendação fora do vocabulário do catálogo: {r} → '{rec[:60]}'")
        st = fields.get("Estado da pesquisa", "")
        if st and st.split()[0] not in STATES:
            errors.append(f"estado de pesquisa inválido em {r}: '{st[:40]}'")
        ex = fields.get("Resultado de execução", "")
        if ex and ex.split()[0] not in EXEC:
            errors.append(f"resultado de execução inválido em {r}: '{ex[:40]}'")
        for old in OLD_VOCAB:
            if re.search(rf"\b{old}\b", head):
                warnings.append(f"vocabulário antigo no cabeçalho de {r}: {old}")
        if len(re.findall(r"^## ", text, flags=re.M)) < 10:
            warnings.append(f"relatório com poucas seções: {r}")
        if "Evidên" not in text:
            errors.append(f"relatório sem seção de evidência: {r}")


def check_test_claims(files: list[str]) -> None:
    log = os.path.join(ROOT, "data/testing/test-log.tsv")
    rows = []
    if os.path.exists(log):
        rows = [l for l in open(log, encoding="utf-8").read().split("\n")[1:] if l.strip()]
    tested = {"LOCAL_SMOKE_PASS", "LOCAL_TESTS_PASS", "LOCAL_TESTS_FAIL", "PARTIAL"}
    for f in files:
        r = rel(f)
        if not (r.startswith("repositories/") and r.endswith("REPORT.md")):
            continue
        fields = header_block(open(f, encoding="utf-8").read())
        ex = fields.get("Resultado de execução", "").split()[0] if fields.get("Resultado de execução") else ""
        if ex in tested:
            oid = fields.get("ID", "").strip("` ")
            if not any(row.split("\t")[1] == oid for row in rows if len(row.split("\t")) > 1):
                errors.append(f"{r}: declara {ex} sem linha em data/testing/test-log.tsv")


def check_decisions(files: list[str]) -> None:
    for f in files:
        r = rel(f)
        if r.startswith("decisions/") and re.match(r"decisions/\w+/DR-\d+", r):
            text = open(f, encoding="utf-8").read()
            if "| Alcance |" not in text:
                warnings.append(f"DR sem campo | Alcance |: {r}")
            elif "GOVERNANCA" not in text and "GOVERNANÇA" not in text:
                errors.append(f"DR cujo alcance não é GOVERNANCA: {r}")


def check_digests(files: list[str]) -> None:
    for f in files:
        r = rel(f)
        if r.startswith("cross-project/"):
            head = open(f, encoding="utf-8").read()[:1500]
            for must in ("| ID |", "| Data |"):
                if must not in head:
                    warnings.append(f"digest sem metadados ({must}): {r}")


def check_caches() -> None:
    for base, dirs, files in os.walk(ROOT):
        if ".git" in base:
            continue
        for d in dirs:
            if d in ("__pycache__", "node_modules", ".pytest_cache", ".venv"):
                errors.append(f"diretório gerado versionado: {rel(os.path.join(base, d))}")
        for f in files:
            if f.endswith((".pyc", ".pyo")):
                errors.append(f"binário gerado versionado: {rel(os.path.join(base, f))}")


def check_counts(files: list[str]) -> None:
    actual_md = len([f for f in files if rel(f).count("/") >= 0])
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    m = re.search(r"\| Arquivos Markdown \| (\d+)", readme)
    if m and int(m.group(1)) != actual_md:
        errors.append(f"README diz {m.group(1)} arquivos .md; existem {actual_md}")
    n_reports = len([f for f in files if rel(f).startswith("repositories/") and rel(f).endswith("REPORT.md")])
    m2 = re.search(r"auditoria \((\d+)\)", readme)
    if m2 and int(m2.group(1)) != n_reports:
        errors.append(f"README diz {m2.group(1)} objetos auditados; existem {n_reports}")


def check_orphans(files: list[str]) -> None:
    corpus = {rel(f): open(f, encoding="utf-8", errors="replace").read() for f in files}
    allowed = {"README.md", "RESEARCH-INDEX.md", "RESEARCH-CHANGELOG.md",
               "RESEARCH-ROADMAP.md", "RESEARCH-BACKLOG.md", "MISSION.md"}
    referenced: set[str] = set()
    for r, text in corpus.items():
        for m in re.finditer(r"`([A-Za-z0-9_./-]+\.md)`", text):
            t = m.group(1)
            referenced.add(os.path.normpath(t))
            referenced.add(os.path.normpath(os.path.join(os.path.dirname(r), t)))
        for m in re.finditer(r"\]\(([^)#]+\.md)", text):
            t = m.group(1)
            referenced.add(os.path.normpath(t))
            referenced.add(os.path.normpath(os.path.join(os.path.dirname(r), t)))
    for r in corpus:
        if r in allowed:
            continue
        if r not in referenced and os.path.basename(r) not in referenced:
            warnings.append(f"documento órfão (ninguém aponta para ele): {r}")


def check_stale(files: list[str]) -> None:
    for f in files:
        fields = header_block(open(f, encoding="utf-8", errors="replace").read())
        nxt = fields.get("Próxima revisão", "")
        m = re.search(r"(\d{4})-(\d{2})-(\d{2})", nxt)
        if not m:
            continue
        d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if d < TODAY:
            notes.append(f"revisão vencida ({d}) — classificar como STALE: {rel(f)}")


def main() -> int:
    quiet = "--quiet" in sys.argv
    as_json = "--json" in sys.argv
    files = walk_md()
    for name, fn in [
        ("títulos", check_titles), ("segredos", check_secrets),
        ("diretórios", check_empty_dirs), ("tamanho", check_sizes),
        ("caminhos", check_local_paths), ("links", check_md_links),
        ("IDs", check_ids), ("relatórios", check_report_schema),
        ("testes", check_test_claims), ("decisões", check_decisions),
        ("digests", check_digests), ("caches", check_caches),
        ("contagens", check_counts), ("órfãos", check_orphans),
        ("vencidas", check_stale),
    ]:
        before = (len(errors), len(warnings))
        fn(files) if name not in ("diretórios", "caches") else fn()
        status = "ok" if (len(errors), len(warnings)) == before else "nota"
        if not quiet and not as_json:
            print(f"[{status:5}] {name}")

    if as_json:
        print(json.dumps({"errors": errors, "warnings": warnings, "notes": notes,
                          "files": len(files)}, ensure_ascii=False, indent=2))
        return 1 if errors else 0

    for label, items in (("ERRO", errors), ("AVISO", warnings), ("NOTA", notes)):
        for it in items:
            print(f"  {label:6}{it}")
    print(f"\narquivos .md verificados: {len(files)}")
    print(f"erros: {len(errors)} · avisos: {len(warnings)} · notas: {len(notes)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
