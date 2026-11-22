#!/usr/bin/env python3
"""Validador estrutural do Lia-Research.

Uso:
    python3 tools/validate.py                 # data de hoje
    python3 tools/validate.py --today 2027-03-01
    python3 tools/validate.py --quiet | --json

Três níveis:
  ERRO  — bloqueia publicação
  AVISO — conteúdo/qualidade a revisar
  NOTA  — pendência externa legítima (BLOCKED, NOT_RUN, revisão vencida)

O validador nunca escreve em documento: `STALE` é diagnóstico, não mutação.
Regras: `catalog/CATALOG-SCHEMA.md`, `agents/PUBLISHING-PROTOCOL.md`.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

# --------------------------------------------------------------- vocabulário
RECS = frozenset({"DIRECT_INTEGRATION_CANDIDATE", "ADAPT", "FORK_CANDIDATE",
                  "INDEPENDENT_REIMPLEMENTATION", "REFERENCE_ONLY", "REJECT",
                  "INSUFFICIENT_EVIDENCE"})
STATES = frozenset({"DISCOVERED", "TRIAGED", "INVESTIGATING", "DOCUMENTED", "TESTED",
                    "PARTIALLY_TESTED", "NOT_TESTED", "BLOCKED", "STALE", "SUPERSEDED",
                    "CONFLICTING"})
EXEC = frozenset({"NOT_RUN", "STATIC_REVIEW_ONLY", "OFFICIAL_CI_REVIEWED", "LOCAL_SMOKE_PASS",
                  "LOCAL_TESTS_PASS", "LOCAL_TESTS_FAIL", "PARTIAL", "BLOCKED"})
# `BLOCKED` é o único termo que existe nos dois vocabulários (bloqueio de pesquisa e de
# execução). Qualquer outra interseção é erro de vocabulário.
EXEC_OR_STATE_SHARED = frozenset({"BLOCKED"})
OLD_VOCAB = ("ADOTAR", "ADAPTAR", "REJEITAR")
REPORT_FIELDS = ("| ID |", "| Tipo |", "| Estado da pesquisa |",
                 "| Resultado de execução |", "| Recomendação |",
                 "| Decisão de adoção |", "| Licença |")
# Resultados que só podem existir com linha no test-log
EXEC_REQUIRES_LOG = frozenset({"LOCAL_SMOKE_PASS", "LOCAL_TESTS_PASS", "LOCAL_TESTS_FAIL",
                               "PARTIAL"})
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "_site",
             ".pytest_cache", ".ruff_cache", "build", "dist", ".cache"}
INTERNAL_ROOTS = ("governance/", "catalog/", "templates/", "data/", "tools/", "agents/",
                  "decisions/", "cross-project/", "repositories/", "archive/", "audits/",
                  "projects/", "comparisons/", "ecosystem/")

# ---------------------------------------------------------------- segredos
# Cada padrão é específico o suficiente para não casar com prosa. A ideia: formato
# válido do provedor, não "string grande".
SECRET_PATTERNS = [
    ("github", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("github-pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{60,}\b")),
    ("openai", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b")),
    ("anthropic", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{32,}\b")),
    ("stripe", re.compile(r"\b[sr]k_live_[A-Za-z0-9]{20,}\b")),
    ("aws-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("aws-secret", re.compile(r"(?i)aws_?secret_?access_?key\s*[:=]\s*['\"]?[A-Za-z0-9/+=]{40}")),
    ("google-api", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("slack", re.compile(r"\bxox[abposr]-[0-9A-Za-z-]{10,}\b")),
    ("slack-webhook", re.compile(r"https://hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]{20,}")),
    ("discord-webhook", re.compile(r"https://discord(?:app)?\.com/api/webhooks/\d{15,}/[A-Za-z0-9_-]{30,}")),
    ("npm", re.compile(r"\bnpm_[A-Za-z0-9]{36}\b")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    ("private-key", re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")),
    ("pgp-key", re.compile(r"-----BEGIN PGP PRIVATE KEY BLOCK-----")),
    ("connection-string", re.compile(r"(?i)\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s:@/]+:[^\s@/]{6,}@")),
    ("azure", re.compile(r"(?i)\bAccountKey=[A-Za-z0-9+/=]{40,}")),
    ("bearer", re.compile(r"(?i)\bauthorization\s*:\s*bearer\s+[A-Za-z0-9._-]{30,}")),
]
# Um token completo só deixa de ser erro se a linha disser que ele é fictício. O marcador
# tem de afirmar falsidade — "placeholder"/"redacted" sozinhos não bastam, senão qualquer
# segredo real escaparia escrevendo essas palavras na mesma linha.
SANITIZED_MARKERS = re.compile(
    r"(?i)(exemplo sanitizado|sanitizad|fixture sint|sintétic|sintetic|não é real|"
    r"not a real|fictíc|fictic|token de teste|test token|dummy token)")


MASK_RE = re.compile(r"^[Xx0*._-]{8,}$")


def looks_masked(token: str) -> bool:
    """Máscara óbvia (XXXX, 0000, ***) não é segredo: ninguém autentica com ela."""
    tail = re.split(r"[/_\-]", token.rstrip("/"))[-1] or token
    return bool(MASK_RE.fullmatch(tail)) or "REDACTED" in token.upper()


def first_token(text: str, vocab) -> str | None:
    hits = [(text.find(t), t) for t in vocab if t in text]
    return min(hits)[1] if hits else None


def header_block(text: str) -> dict[str, str]:
    """Campos do primeiro bloco de tabela do documento (não mexe no resto)."""
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


def parse_date(value: str) -> dt.date | None:
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", value or "")
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


class Validator:
    def __init__(self, root: str | os.PathLike, today: dt.date | None = None) -> None:
        self.root = Path(root).resolve()
        self.today = today or dt.date.today()
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    # ---------------------------------------------------------------- helpers
    def rel(self, p: Path) -> str:
        return str(p.relative_to(self.root)).replace(os.sep, "/")

    def md_files(self) -> list[Path]:
        out = []
        for base, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            out += [Path(base) / f for f in files if f.endswith(".md")]
        return sorted(out)

    def reports(self) -> list[Path]:
        return sorted(self.root.glob("repositories/*/REPORT.md"))

    def text(self, p: Path) -> str:
        return p.read_text(encoding="utf-8", errors="replace")

    # ---------------------------------------------------------------- checks
    def check_titles(self, files: list[Path]) -> None:
        seen: dict[str, str] = {}
        for f in files:
            r = self.rel(f)
            if r.startswith(".github/"):
                continue
            m = re.search(r"^# (.+)$", self.text(f), flags=re.M)
            if not m:
                self.errors.append(f"sem título H1: {r}")
                continue
            t = m.group(1).strip()
            if t in seen:
                self.errors.append(f"título duplicado: '{t}' em {r} e {seen[t]}")
            seen[t] = r

    def check_secrets(self, files: list[Path]) -> None:
        for f in files:
            for n, line in enumerate(self.text(f).split("\n"), 1):
                for name, pat in SECRET_PATTERNS:
                    m = pat.search(line)
                    if not m:
                        continue
                    if SANITIZED_MARKERS.search(line) or looks_masked(m.group(0)):
                        self.notes.append(
                            f"segredo '{name}' em exemplo sanitizado/mascarado: {self.rel(f)}:{n}")
                        continue
                    self.errors.append(
                        f"possível segredo ({name}) em {self.rel(f)}:{n}: {m.group(0)[:14]}…")

    def check_empty_dirs(self) -> None:
        for base, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            if Path(base) == self.root:
                continue
            if not dirs and not files:
                self.warnings.append(f"diretório vazio: {self.rel(Path(base))}")

    def check_sizes(self, files: list[Path]) -> None:
        for f in files:
            size = f.stat().st_size
            if size > 2 * 1024 * 1024:
                self.errors.append(f"documento > 2 MB: {self.rel(f)}")
            elif size > 250 * 1024:
                self.warnings.append(f"documento grande ({size // 1024} KB): {self.rel(f)}")

    def check_local_paths(self, files: list[Path]) -> None:
        """Só caminhos internos: caminho de terceiro citado é citação, não link."""
        for f in files:
            for m in re.finditer(r"`([A-Za-z0-9_./-]+\.(?:md|tsv|py|json|txt))`", self.text(f)):
                p = m.group(1)
                if p.startswith(("http", "~/")) or "*" in p or not p.startswith(INTERNAL_ROOTS):
                    continue
                if not (self.root / p).exists():
                    self.errors.append(f"caminho interno citado não existe: {p} ({self.rel(f)})")

    def check_md_links(self, files: list[Path]) -> None:
        for f in files:
            for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", self.text(f)):
                target = m.group(1).split("#")[0].strip()
                if not target or target.startswith(("http", "mailto:", "#")):
                    continue
                if not target.endswith(".md"):
                    continue
                if not (f.parent / target).exists():
                    self.errors.append(f"link .md quebrado: {target} ({self.rel(f)})")

    def check_ids(self, files: list[Path]) -> None:
        index = self.root / "RESEARCH-INDEX.md"
        registered = set()
        if index.exists():
            registered = set(re.findall(r"`(LR-[A-Z]+-\d+)`", self.text(index)))
        defined: dict[str, str] = {}
        for f in files:
            r = self.rel(f)
            if r.startswith(("templates/", "catalog/")):
                continue
            for m in re.finditer(r"^\| ID \| `(LR-[A-Z]+-?\d+)`", self.text(f), flags=re.M):
                i = m.group(1)
                if "XXX" in i or i.endswith("-000"):
                    continue
                if i in defined:
                    self.errors.append(f"ID duplicado: {i} em {r} e {defined[i]}")
                defined[i] = r
        for i in sorted(defined):
            if registered and i not in registered:
                self.errors.append(f"ID não registrado no RESEARCH-INDEX: {i} ({defined[i]})")
        for i in sorted(registered - set(defined)):
            self.notes.append(f"ID no índice sem documento com cabeçalho próprio: {i}")

    def check_report_schema(self) -> None:
        for f in self.reports():
            r = self.rel(f)
            text = self.text(f)
            head = text[:3000]
            fields = header_block(text)
            for fld in REPORT_FIELDS:
                if fld not in head:
                    self.errors.append(f"relatório sem campo obrigatório {fld.strip('| ')}: {r}")
            # Anti-fixture: a linha de ID tem de ser a PRIMEIRA do cabeçalho. O parser
            # (`header_block`) para no primeiro texto fora da tabela, então um frontmatter que
            # reordena ou aninha o campo passa na leitura humana e quebra o catálogo gerado — é o
            # defeito que a Skill upstream `img2threejs` documentou com um teste "assert against the
            # real file, never a fixture" (`LR-STUDIO-012` §6). Medido no arquivo em disco, não num exemplo.
            if not re.search(r"^\| Campo \| Valor \|\n\|[-: ]+\|[-: ]+\|\n\| ID \|", text, flags=re.M):
                self.errors.append(f"cabeçalho fora da forma canônica (tabela deve começar com `| ID |`): {r}")
            rec = fields.get("Recomendação", "")
            if not first_token(rec, RECS):
                self.errors.append(f"recomendação fora do vocabulário: {r} → '{rec[:60]}'")
            st = fields.get("Estado da pesquisa", "")
            if st and st.split()[0] not in STATES:
                self.errors.append(f"estado de pesquisa inválido em {r}: '{st[:40]}'")
            ex = fields.get("Resultado de execução", "")
            if ex and ex.split()[0] not in EXEC:
                self.errors.append(f"resultado de execução inválido em {r}: '{ex[:40]}'")
            for old in OLD_VOCAB:
                if re.search(rf"\b{old}\b", head):
                    self.warnings.append(f"vocabulário antigo no cabeçalho de {r}: {old}")
            if len(re.findall(r"^## ", text, flags=re.M)) < 10:
                self.warnings.append(f"relatório com poucas seções: {r}")
            if "Evidên" not in text:
                self.errors.append(f"relatório sem seção de evidência: {r}")
            if "| Licença |" in head and not fields.get("Licença", "").strip("— -"):
                self.errors.append(f"campo Licença vazio: {r}")

    def check_index_consistency(self) -> None:
        index = self.root / "RESEARCH-INDEX.md"
        if not index.exists():
            return
        linhas: dict[str, str] = {}
        for line in self.text(index).split("\n"):
            if line.startswith("| `LR-") and line.count("|") >= 6:
                c = [x.strip() for x in line.strip().strip("|").split("|")]
                linhas[c[0].strip("`")] = line
        for f in self.reports():
            fields = header_block(self.text(f))
            oid = fields.get("ID", "").strip("` ")
            if oid not in linhas:
                self.errors.append(f"relatório fora do índice: {oid} ({self.rel(f)})")
                continue
            linha = linhas[oid]
            rec_idx = first_token(linha, RECS)
            rec_rep = first_token(fields.get("Recomendação", ""), RECS)
            if rec_idx and rec_rep and rec_idx != rec_rep:
                self.errors.append(f"recomendação divergente em {oid}: índice={rec_idx} relatório={rec_rep}")
            st_idx = first_token(linha, STATES - {"STALE", "SUPERSEDED"})
            st_rep = fields.get("Estado da pesquisa", "").split(" ")[0]
            if st_idx and st_rep in STATES and st_idx != st_rep:
                self.errors.append(f"estado divergente em {oid}: índice={st_idx} relatório={st_rep}")

    def check_catalog_sync(self, files: list[Path]) -> None:
        """Catálogo é derivado: precisa bater byte a byte com o gerador."""
        tsv = self.root / "catalog/catalog.tsv"
        if not tsv.exists():
            self.errors.append("catalog/catalog.tsv ausente (rode tools/build_catalog.py)")
            return
        try:
            sys.path.insert(0, str(self.root / "tools"))
            sys.dont_write_bytecode = True
            import build_catalog  # noqa: PLC0415
        except Exception as exc:  # pragma: no cover - import quebrado é erro de repo
            self.errors.append(f"tools/build_catalog.py não importável: {exc}")
            return
        esperado = build_catalog.render(build_catalog.build_rows(self.root))
        if tsv.read_text(encoding="utf-8") != esperado:
            self.errors.append("catalog/catalog.tsv não corresponde ao gerado (rode tools/build_catalog.py)")
        linhas = [l for l in tsv.read_text(encoding="utf-8").split("\n")[1:] if l.strip()]
        ids_tsv = {l.split("\t")[0] for l in linhas}
        for f in self.reports():
            oid = header_block(self.text(f)).get("ID", "").strip("` ")
            if oid not in ids_tsv:
                self.errors.append(f"objeto fora do catálogo: {oid} ({self.rel(f)})")
        rel_ids = {header_block(self.text(f)).get("ID", "").strip("` ") for f in self.reports()}
        for extra in sorted(ids_tsv - rel_ids):
            self.errors.append(f"catálogo tem linha sem relatório: {extra}")
        for f in self.reports():
            if not f.with_name("REPORT.md").exists():  # pragma: no cover - glob já garante
                self.errors.append(f"relatório ausente: {self.rel(f)}")

    def check_test_claims(self) -> None:
        log = self.root / "data/testing/test-log.tsv"
        header: list[str] = []
        rows: list[list[str]] = []
        if log.exists():
            lines = [l for l in log.read_text(encoding="utf-8").split("\n") if l.strip()]
            header = lines[0].split("\t") if lines else []
            rows = [l.split("\t") for l in lines[1:]]
        esperado = ["date", "object_id", "version", "level", "environment", "procedure",
                    "result", "evidence", "not_tested", "repro"]
        if header and header != esperado:
            self.errors.append(f"test-log.tsv com cabeçalho inesperado: {header}")
        for i, row in enumerate(rows, 2):
            if len(row) != 10:
                self.errors.append(f"test-log.tsv linha {i} tem {len(row)} colunas (esperado 10)")
                continue
            if row[6] not in EXEC:
                self.errors.append(f"test-log.tsv linha {i}: resultado fora do vocabulário '{row[6]}'")
            if not parse_date(row[0]):
                self.errors.append(f"test-log.tsv linha {i}: data inválida '{row[0]}'")
        for f in self.reports():
            fields = header_block(self.text(f))
            ex = (fields.get("Resultado de execução") or "").split()
            if not ex:
                continue
            oid = fields.get("ID", "").strip("` ")
            linhas_obj = [r for r in rows if len(r) > 1 and r[1] == oid]
            if ex[0] in EXEC_REQUIRES_LOG and not linhas_obj:
                self.errors.append(f"{self.rel(f)}: declara {ex[0]} sem linha em data/testing/test-log.tsv")
            if ex[0] in ("NOT_RUN", "STATIC_REVIEW_ONLY") and linhas_obj:
                self.warnings.append(
                    f"{self.rel(f)}: tem registro de teste mas declara {ex[0]} — atualizar resultado?")
            for r in linhas_obj:
                if len(r) == 10 and r[6] not in EXEC:
                    self.errors.append(f"test-log: resultado inválido para {oid}: {r[6]}")

    def check_decisions(self, files: list[Path]) -> None:
        for f in files:
            r = self.rel(f)
            if r.startswith("decisions/") and re.match(r"decisions/\w+/DR-\d+-", r):
                text = self.text(f)
                if "| Alcance |" not in text:
                    self.warnings.append(f"DR sem campo | Alcance |: {r}")
                elif "GOVERNANCA" not in text and "GOVERNANÇA" not in text:
                    self.errors.append(f"DR cujo alcance não é GOVERNANCA: {r}")

    def check_digests(self, files: list[Path]) -> None:
        for f in files:
            r = self.rel(f)
            if r.startswith("cross-project/") and "DIGEST" in os.path.basename(r).upper():
                head = self.text(f)[:1500]
                for must in ("| ID |", "| Data |"):
                    if must not in head:
                        self.warnings.append(f"digest sem metadados ({must}): {r}")

    def check_caches(self) -> None:
        for base, dirs, files in os.walk(self.root):
            for d in list(dirs):
                if d in ("__pycache__", "node_modules", ".pytest_cache", ".venv", "venv"):
                    self.errors.append(f"diretório gerado versionado: {self.rel(Path(base) / d)}")
            for f in files:
                if f.endswith((".pyc", ".pyo")):
                    self.errors.append(f"binário gerado versionado: {self.rel(Path(base) / f)}")

    def check_counts(self, files: list[Path]) -> None:
        readme = self.root / "README.md"
        if not readme.exists():
            return
        text = self.text(readme)
        actual_md = len([f for f in files])
        m = re.search(r"\| Arquivos Markdown \| (\d+)", text)
        if m and int(m.group(1)) != actual_md:
            self.errors.append(f"README diz {m.group(1)} arquivos .md; existem {actual_md}")
        n_reports = len(self.reports())
        m2 = re.search(r"auditoria \((\d+) objetos?\)", text) or re.search(r"\| Relatórios externos \| (\d+) objetos", text)
        if m2 and int(m2.group(1)) != n_reports:
            self.errors.append(f"README diz {m2.group(1)} objetos; existem {n_reports}")
        m3 = re.search(r"\| Catálogo \| `catalog/catalog\.tsv` — (\d+) linhas", text)
        if m3 and int(m3.group(1)) != n_reports:
            self.errors.append(f"README diz catálogo com {m3.group(1)} linhas; existem {n_reports}")

    def check_licence_counts(self) -> None:
        matrix = self.root / "data/inventory/license-matrix.tsv"
        digest = self.root / "cross-project/licensing/READY-TO-USE-LICENSES.md"
        if not (matrix.exists() and digest.exists()):
            return
        ids_matrix = {l.split("\t")[0] for l in self.text(matrix).split("\n")[1:] if l.strip()}
        text = self.text(digest)
        inicio = text.find("## 2. Tabela-mestra")
        fim = text.find("## 3.", inicio)
        bloco = text[inicio:fim] if inicio > 0 and fim > inicio else ""
        ids_digest = set(re.findall(r"\| `(LR-[A-Z]+-\d+)` \|", bloco))
        if faltando := ids_matrix - ids_digest:
            self.warnings.append(f"objetos na matriz de licença e fora do digest: {sorted(faltando)}")
        if sobrando := ids_digest - ids_matrix:
            self.errors.append(f"digest de licenças cita objeto inexistente na matriz: {sorted(sobrando)}")

    def check_orphans(self, files: list[Path]) -> None:
        corpus = {self.rel(f): self.text(f) for f in files}
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
                self.warnings.append(f"documento órfão (ninguém aponta para ele): {r}")

    def check_stale(self) -> None:
        """Revisão vencida é diagnóstico. Nunca escreve `STALE` no relatório."""
        vencidas = []
        for f in self.reports():
            fields = header_block(self.text(f))
            oid = fields.get("ID", "").strip("` ")
            d = parse_date(fields.get("Próxima revisão", ""))
            if d and d < self.today:
                dias = (self.today - d).days
                vencidas.append((oid, d, dias))
        for oid, d, dias in vencidas:
            self.notes.append(f"revisão vencida desde {d} ({dias} dias) — classificar como STALE: {oid}")

    # ---------------------------------------------------------------- runner
    CHECKS = ("títulos", "segredos", "diretórios", "tamanho", "caminhos", "links", "IDs",
              "relatórios", "índice", "catálogo", "testes", "decisões", "digests", "caches",
              "contagens", "licenças", "órfãos", "vencidas")

    def run(self) -> "Validator":
        files = self.md_files()
        per_file = {"títulos": self.check_titles, "segredos": self.check_secrets,
                    "tamanho": self.check_sizes, "caminhos": self.check_local_paths,
                    "links": self.check_md_links, "IDs": self.check_ids,
                    "decisões": self.check_decisions, "digests": self.check_digests,
                    "órfãos": self.check_orphans}
        sem_args = {"diretórios": self.check_empty_dirs, "relatórios": self.check_report_schema,
                    "índice": self.check_index_consistency, "testes": self.check_test_claims,
                    "caches": self.check_caches,
                    "licenças": self.check_licence_counts, "vencidas": self.check_stale}
        for name in self.CHECKS:
            if name in per_file:
                fn = per_file[name]
                fn(self.reports() if name == "relatórios" else files)
            elif name == "catálogo":
                self.check_catalog_sync(files)
            elif name == "contagens":
                self.check_counts(files)
            elif name in sem_args:
                sem_args[name]()
        return self


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    quiet = "--quiet" in args
    as_json = "--json" in args
    root = os.environ.get("LIA_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    today = None
    if "--today" in args:
        today = dt.date.fromisoformat(args[args.index("--today") + 1])
    elif os.environ.get("LIA_TODAY"):
        today = dt.date.fromisoformat(os.environ["LIA_TODAY"])

    v = Validator(root, today).run()
    if as_json:
        print(json.dumps({"root": str(v.root), "today": v.today.isoformat(),
                          "files": len(v.md_files()), "reports": len(v.reports()),
                          "errors": v.errors, "warnings": v.warnings,
                          "notes": v.notes}, ensure_ascii=False, indent=2))
        return 1 if v.errors else 0
    for name in v.CHECKS:
        if not quiet:
            print(f"[ok] {name}")
    for label, items in (("ERRO", v.errors), ("AVISO", v.warnings), ("NOTA", v.notes)):
        for it in items:
            print(f"  {label:6}{it}")
    if not quiet:
        print(f"\narquivos .md: {len(v.md_files())} · relatórios: {len(v.reports())}")
    print(f"erros: {len(v.errors)} · avisos: {len(v.warnings)} · notas: {len(v.notes)}"
          f" · data de referência: {v.today.isoformat()}")
    return 1 if v.errors else 0


if __name__ == "__main__":
    sys.exit(main())
