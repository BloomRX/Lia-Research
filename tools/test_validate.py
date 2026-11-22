#!/usr/bin/env python3
"""Testes do validador e do gerador de catálogo.

    python3 tools/test_validate.py            # 60+ testes, sem rede, sem dependência

Cada teste monta um repositório mínimo em diretório temporário, aplica **uma** mutação
e verifica o diagnóstico. O fixture base passa limpo: se ele quebrar, o teste falha —
é o que impede "verde" por validador frouxo.
"""
from __future__ import annotations

import datetime as dt
import os
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True

import build_catalog  # noqa: E402
import validate as v  # noqa: E402

TODAY = dt.date(2026, 11, 20)

REPORT = """# Objeto de teste — relatório

| Campo | Valor |
|---|---|
| ID | `{id}` |
| Tipo | repositorio |
| Estado da pesquisa | {state} |
| Resultado de execução | {exec} |
| Recomendação | **{rec}** |
| Decisão de adoção | — (nenhuma registrada) |
| Licença | MIT (lida em `LICENSE`) |
| Data da pesquisa | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Próxima revisão | {next_review} |
| Upstream conferido | 2026-11-20 · `org/repo` · HEAD `abc1234` · sem mudança no HEAD |

{secoes}

## Evidências

| Afirmação | Rótulo |
|---|---|
| existe | CONFIRMED |
"""

SECOES = "\n".join(f"## {i}. Seção {i}\n\ntexto\n" for i in range(1, 11))


def make_repo(tmp: Path, *, report_id: str = "LR-REPO-001", state: str = "DOCUMENTED",
              exec_: str = "STATIC_REVIEW_ONLY", rec: str = "ADAPT",
              next_review: str = "2027-02-17", extra_files: dict[str, str] | None = None,
              md_count_override: int | None = None, lic_id: str = "LR-REPO-001") -> Path:
    (tmp / "catalog").mkdir(parents=True, exist_ok=True)
    (tmp / "repositories/foo").mkdir(parents=True, exist_ok=True)
    (tmp / "data/testing").mkdir(parents=True, exist_ok=True)
    (tmp / "data/inventory").mkdir(parents=True, exist_ok=True)
    (tmp / "cross-project/licensing").mkdir(parents=True, exist_ok=True)
    (tmp / "templates").mkdir(parents=True, exist_ok=True)
    (tmp / "decisions/PENDING").mkdir(parents=True, exist_ok=True)
    (tmp / "decisions/PENDING/DR-0001-TESTE.md").write_text(
        "# DR-0001 — teste\n\n| Campo | Valor |\n|---|---|\n| ID | DR-0001 |\n"
        "| Alcance | **GOVERNANCA** |\n", encoding="utf-8")

    (tmp / "repositories/foo/REPORT.md").write_text(
        REPORT.format(id=report_id, state=state, exec=exec_, rec=rec,
                      next_review=next_review, secoes=SECOES), encoding="utf-8")
    (tmp / "MISSION.md").write_text("# MISSION\n\nlimites.\n", encoding="utf-8")
    (tmp / "RESEARCH-INDEX.md").write_text(
        "# RESEARCH-INDEX\n\n| ID | Objeto | Licença | Estado | Recomendação | Decisão de adoção | Confiança | Documento |\n"
        "|---|---|---|---|---|---|---|---|\n"
        f"| `{report_id}` | `org/repo` | MIT | {state} | **{rec}** | — nenhuma | Alta | `repositories/foo/REPORT.md` |\n",
        encoding="utf-8")
    (tmp / "templates/x.md").write_text("# Template X\n\nmodelo.\n", encoding="utf-8")
    (tmp / "cross-project/licensing/READY-TO-USE-LICENSES.md").write_text(
        "# Licenças\n\n## 2. Tabela-mestra\n\n| ID | Objeto | Uso | Fork | Colar |\n|---|---|---|---|---|\n"
        f"| `{lic_id}` | foo | usar | sim | MIT |\n\n## 3. Modelos\n", encoding="utf-8")
    (tmp / "data/inventory/license-matrix.tsv").write_text(
        "id\tobjeto\tspdx\tlido_em\tusar_como\tfork\tmodificar\tcomercial\tredistribuir\t"
        "atribuicao\tcopyleft\tpatente\tnotice_obrigatorio\tclasse\tevidencia\n"
        f"{lic_id}\torg/repo\tMIT\tLICENSE\tusar\tsim\tsim\tsim\tsim\tsim\tnao\tnao\tMIT\t"
        "USE_AS_IS\trepositories/foo/REPORT.md\n", encoding="utf-8")
    (tmp / "data/testing/test-log.tsv").write_text(
        "date\tobject_id\tversion\tlevel\tenvironment\tprocedure\tresult\tevidence\tnot_tested\trepro\n",
        encoding="utf-8")
    (tmp / "catalog/catalog.tsv").write_text(
        build_catalog.render(build_catalog.build_rows(tmp)), encoding="utf-8")
    if extra_files:
        for rel, content in extra_files.items():
            p = tmp / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
    n_md = len(list(tmp.rglob("*.md"))) + 1  # o próprio README
    (tmp / "README.md").write_text(
        "# R\n\n| Campo | Valor |\n|---|---|\n"
        f"| Arquivos Markdown | {md_count_override if md_count_override is not None else n_md} |\n"
        "| Relatórios externos | 1 objetos |\n"
        "| Catálogo | `catalog/catalog.tsv` — 1 linhas |\n\n"
        "Ver `RESEARCH-INDEX.md`, `templates/x.md`, "
        "`cross-project/licensing/READY-TO-USE-LICENSES.md` e "
        "`decisions/PENDING/DR-0001-TESTE.md`.\n", encoding="utf-8")
    return tmp


class Base(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        make_repo(self.root)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def run_val(self, today: dt.date = TODAY):
        return v.Validator(self.root, today).run()

    def regen(self) -> None:
        """Regenera o catálogo depois de mutar um relatório (senão o teste mede outra coisa)."""
        (self.root / "catalog/catalog.tsv").write_text(
            build_catalog.render(build_catalog.build_rows(self.root)), encoding="utf-8")

    def assertClean(self) -> None:
        val = self.run_val()
        self.assertEqual(val.errors, [], f"erros inesperados: {val.errors}")
        self.assertEqual(val.warnings, [], f"avisos inesperados: {val.warnings}")

    def assertError(self, fragment: str) -> None:
        val = self.run_val()
        self.assertTrue(any(fragment in e for e in val.errors),
                        f"esperava erro contendo {fragment!r}; obtive {val.errors}")

    def assertWarning(self, fragment: str) -> None:
        val = self.run_val()
        self.assertTrue(any(fragment in w for w in val.warnings),
                        f"esperava aviso contendo {fragment!r}; obtive {val.warnings}")

    def assertNote(self, fragment: str) -> None:
        val = self.run_val()
        self.assertTrue(any(fragment in n for n in val.notes),
                        f"esperava nota contendo {fragment!r}; obtive {val.notes}")


# ------------------------------------------------------------- anti-fixture
class TestAntiFixture(Base):
    """A regra é medida no arquivo em disco, não num exemplo construído pelo teste.

    Herdado de `LR-STUDIO-012` §6: o `SKILL.md` do `img2threejs` vendorizado aninhou `version:`
    sob `metadata:` — YAML válido, legível para humano, e os dois caminhos de release abortam.
    O teste deles declara "Assert against the real SKILL.md, never a fixture". Aqui a forma
    canônica é a mesma ideia: a primeira linha do cabeçalho tem de ser `| ID |`, porque o parser
    para no primeiro texto fora da tabela e o catálogo gerado fica mudo.
    """

    def test_regressao_no_fixture_detecta(self) -> None:
        """Se a linha de ID sair do topo, o validador acusa — medindo o arquivo real do fixture."""
        root = make_repo(self.root, report_id="LR-REPO-001")
        f = root / "repositories/foo/REPORT.md"
        lines = f.read_text(encoding="utf-8").split("\n")
        i_id = next(i for i, l in enumerate(lines) if l.startswith("| ID |"))
        i_sep = next(i for i, l in enumerate(lines) if set(l) <= set("|- ") and l.startswith("|---"))
        lines[i_id], lines[i_id + 1] = lines[i_id + 1], lines[i_id]
        f.write_text("\n".join(lines), encoding="utf-8")
        self.run_val()
        val = v.Validator(root, TODAY).run()
        self.assertTrue(any("forma canônica" in e for e in val.errors),
                        f"esperava erro de forma de cabeçalho; obtive {val.errors}")
        self.assertTrue(i_id > i_sep)

    def test_base_real_passa_na_medi_direta(self) -> None:
        """Mede a base de verdade (sem fixture): todo relatório real tem cabeçalho canônico."""
        real = Path(__file__).resolve().parents[1]
        val = v.Validator(real).run()
        forma = [e for e in val.errors if "forma canônica" in e]
        self.assertEqual(forma, [], f"cabeçalhos reais fora da forma canônica: {forma}")
        rels = sorted((real / "repositories").glob("*/REPORT.md"))
        self.assertGreaterEqual(len(rels), 30, "a medição direta precisa de corpus real para valer")


# ------------------------------------------------------------------ fixture
class TestFixtureSanidade(Base):
    def test_fixture_base_passa_limpo(self):
        self.assertClean()

    def test_relatorio_e_catalogo_sao_encontrados(self):
        val = self.run_val()
        self.assertEqual(len(val.reports()), 1)
        self.assertEqual(len(val.md_files()), 7)


# ------------------------------------------------------------------ vocabulário
class TestVocabulario(unittest.TestCase):
    def test_recomendacoes_sao_fechadas(self):
        self.assertEqual(len(v.RECS), 7)
        for t in ("ADAPT", "REFERENCE_ONLY", "REJECT", "INSUFFICIENT_EVIDENCE"):
            self.assertIn(t, v.RECS)
        for t in ("ADAPTAR", "ADOTAR", "REFERÊNCIA", "PENDENTE"):
            self.assertNotIn(t, v.RECS)

    def test_estado_e_resultado_so_compartilham_blocked(self):
        self.assertEqual(v.STATES & v.EXEC, v.EXEC_OR_STATE_SHARED)

    def test_first_token_e_deterministico(self):
        texto = "**REJECT** (stack) / **REFERENCE_ONLY** (interop)"
        self.assertEqual(v.first_token(texto, v.RECS), "REJECT")
        self.assertEqual(v.first_token("nada aqui", v.RECS), None)

    def test_parse_date(self):
        self.assertEqual(v.parse_date("2027-02-17 (90 dias)"), dt.date(2027, 2, 17))
        self.assertIsNone(v.parse_date("março"))
        self.assertIsNone(v.parse_date("2027-13-40"))


class TestHeader(unittest.TestCase):
    def test_le_primeiro_bloco(self):
        f = v.header_block("| Campo | Valor |\n|---|---|\n| ID | `LR-X-001` |\n| Estado da pesquisa | BLOCKED |\n\n## s\n| ID | outro |\n")
        self.assertEqual(f["ID"], "`LR-X-001`")
        self.assertEqual(f["Estado da pesquisa"], "BLOCKED")
        self.assertNotIn("outro", f.values())

    def test_para_no_texto(self):
        self.assertNotIn("B", v.header_block("| A | 1 |\n\ntexto\n\n| B | 2 |\n"))


# ------------------------------------------------------------------ títulos
class TestTitulos(Base):
    def test_sem_h1(self):
        (self.root / "solto.md").write_text("texto sem título\n", encoding="utf-8")
        self.assertError("sem título H1")

    def test_titulo_duplicado(self):
        (self.root / "dup.md").write_text("# MISSION\n\noutro\n", encoding="utf-8")
        self.assertError("título duplicado")

    def test_github_issue_template_isento(self):
        p = self.root / ".github/ISSUE_TEMPLATE/x.md"
        p.parent.mkdir(parents=True)
        p.write_text("---\nname: x\n---\ncorpo\n", encoding="utf-8")
        val = self.run_val()
        self.assertFalse(any("sem título H1" in e and ".github" in e for e in val.errors))


# ------------------------------------------------------------------ segredos
# Montado em runtime: fixtures de segredo não ficam literais no arquivo
# (o GitHub Push Protection bloqueia webhook do Slack mesmo quando é inventado).
_HOOK = "https://" + "hooks" + ".slack.com/services/"


class TestSegredos(Base):
    def _check(self, linha: str) -> bool:
        p = self.root / "doc.md"
        p.write_text(f"# Doc de segredo\n\n{linha}\n", encoding="utf-8")
        val = self.run_val()
        achou = any("possível segredo" in e for e in val.errors)
        p.unlink()
        return achou

    def test_github_token(self):
        self.assertTrue(self._check("token: ghp_" + "a" * 36))

    def test_openai_e_anthropic(self):
        self.assertTrue(self._check("sk-proj-" + "A" * 40))
        self.assertTrue(self._check("sk-ant-" + "B" * 40))

    def test_aws(self):
        self.assertTrue(self._check("AKIA" + "Q" * 16))

    def test_jwt(self):
        self.assertTrue(self._check(
            "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dBjftJeZ4CVPmB92K27uhbUJU1p1r_wW1gFWFOEjXk"))

    def test_slack(self):
        self.assertTrue(self._check("xoxb-123456789012-abcdefghijkl"))

    def test_slack_webhook(self):
        self.assertTrue(self._check(
            _HOOK + "T0ABCDEF1/B0ABCDEF2/9fQ2mZpL7rKd4sVn1Xy8Tb3W"))

    def test_webhook_com_xxxxx_e_exemplo(self):
        self.assertFalse(self._check(
            _HOOK + "T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"))

    def test_chave_privada(self):
        self.assertTrue(self._check("-----BEGIN RSA PRIVATE KEY-----"))

    def test_string_de_conexao(self):
        self.assertTrue(self._check("postgres://usuario:senha123456@host:5432/db"))

    def test_bearer_longo(self):
        self.assertTrue(self._check("authorization: bearer " + "z" * 40))

    def test_exemplo_sanitizado_nao_e_erro(self):
        self.assertFalse(self._check("token de exemplo sanitizado: ghp_" + "a" * 36))
        self.assertFalse(self._check("`<GITHUB_TOKEN>` vindo de variável de ambiente"))

    def test_marcador_generico_nao_escapa_token_real(self):
        # "placeholder" na mesma linha não pode servir de passe livre
        self.assertTrue(self._check("placeholder: ghp_" + "a" * 36))
        self.assertTrue(self._check("redacted: ghp_" + "a" * 36))

    def test_exemplo_sanitizado_gera_nota(self):
        (self.root / "doc.md").write_text(
            "# Doc\n\ntoken fictício de exemplo: ghp_" + "a" * 36 + "\n", encoding="utf-8")
        self.assertNote("exemplo sanitizado/mascarado")

    def test_prosa_inocente(self):
        self.assertFalse(self._check("a chave fica no cofre do sistema, nunca no repositório"))
        self.assertFalse(self._check("use `sk-...` como prefixo ilustrativo"))


# ------------------------------------------------------------------ estrutura
class TestEstrutura(Base):
    def test_diretorio_vazio(self):
        (self.root / "vazio").mkdir()
        self.assertWarning("diretório vazio")

    def test_documento_grande(self):
        (self.root / "grande.md").write_text("# Grande\n\n" + "x" * (300 * 1024), encoding="utf-8")
        self.assertWarning("documento grande")

    def test_documento_gigante_e_erro(self):
        (self.root / "gigante.md").write_text("# Gigante\n\n" + "x" * (2 * 1024 * 1024 + 10),
                                              encoding="utf-8")
        self.assertError("documento > 2 MB")

    def test_pycache_versionado(self):
        p = self.root / "tools/__pycache__/x.pyc"
        p.parent.mkdir(parents=True)
        p.write_bytes(b"x")
        val = self.run_val()
        self.assertTrue(any("diretório gerado versionado" in e for e in val.errors))
        self.assertTrue(any("binário gerado versionado" in e for e in val.errors))


class TestLinks(Base):
    def test_caminho_interno_inexistente(self):
        (self.root / "doc.md").write_text("# Doc\n\nver `governance/NAO-EXISTE.md`\n", encoding="utf-8")
        self.assertError("caminho interno citado não existe")

    def test_caminho_de_terceiro_nao_e_erro(self):
        (self.root / "doc.md").write_text("# Doc\n\no repo tem `docs/mcp.md` e `src/main.go`\n",
                                          encoding="utf-8")
        val = self.run_val()
        self.assertFalse(any("caminho interno" in e for e in val.errors))

    def test_link_md_quebrado(self):
        (self.root / "doc.md").write_text("# Doc\n\n[outro](nao-existe.md)\n", encoding="utf-8")
        self.assertError("link .md quebrado")

    def test_link_md_valido_e_ancora(self):
        (self.root / "doc.md").write_text(
            "# Doc\n\n[mission](MISSION.md) e [âncora](#secao) e [web](https://x.dev/a.md)\n",
            encoding="utf-8")
        val = self.run_val()
        self.assertFalse(any("link .md quebrado" in e for e in val.errors))


# ------------------------------------------------------------------ IDs
class TestIds(Base):
    def test_id_duplicado(self):
        (self.root / "repositories/bar").mkdir()
        (self.root / "repositories/bar/REPORT.md").write_text(
            REPORT.format(id="LR-REPO-001", state="DOCUMENTED", exec="STATIC_REVIEW_ONLY",
                          rec="ADAPT", next_review="2027-02-17", secoes=SECOES), encoding="utf-8")
        self.assertError("ID duplicado")

    def test_id_fora_do_indice(self):
        p = self.root / "repositories/foo/REPORT.md"
        s = p.read_text(encoding="utf-8").replace("LR-REPO-001", "LR-REPO-777")
        p.write_text(s, encoding="utf-8")
        self.assertError("ID não registrado no RESEARCH-INDEX")

    def test_relatorio_fora_do_indice(self):
        p = self.root / "RESEARCH-INDEX.md"
        p.write_text(p.read_text(encoding="utf-8").split("| `LR-")[0], encoding="utf-8")
        self.assertError("relatório fora do índice")

    def test_placeholder_de_template_ignorado(self):
        (self.root / "templates/y.md").write_text(
            "# Template Y\n\n| Campo | Valor |\n|---|---|\n| ID | `LR-XXX-000` |\n", encoding="utf-8")
        val = self.run_val()
        self.assertFalse(any("LR-XXX-000" in e for e in val.errors))


# ------------------------------------------------------------------ esquema
class TestEsquemaRelatorio(Base):
    def _mutate(self, old: str, new: str) -> None:
        p = self.root / "repositories/foo/REPORT.md"
        s = p.read_text(encoding="utf-8")
        self.assertIn(old, s)
        p.write_text(s.replace(old, new, 1), encoding="utf-8")

    def test_campo_obrigatorio_ausente(self):
        self._mutate("| Resultado de execução | STATIC_REVIEW_ONLY |\n", "")
        self.assertError("campo obrigatório Resultado de execução")

    def test_recomendacao_inventada(self):
        self._mutate("| Recomendação | **ADAPT** |", "| Recomendação | **TALVEZ** |")
        self.assertError("recomendação fora do vocabulário")

    def test_estado_invalido(self):
        self._mutate("| Estado da pesquisa | DOCUMENTED |", "| Estado da pesquisa | PRONTO |")
        self.assertError("estado de pesquisa inválido")

    def test_resultado_invalido(self):
        self._mutate("| Resultado de execução | STATIC_REVIEW_ONLY |",
                     "| Resultado de execução | FUNCIONOU |")
        self.assertError("resultado de execução inválido")

    def test_licenca_vazia(self):
        self._mutate("| Licença | MIT (lida em `LICENSE`) |", "| Licença | — |")
        self.assertError("campo Licença vazio")

    def test_sem_secao_de_evidencia(self):
        self._mutate("## Evidências", "## Final")
        self.assertError("sem seção de evidência")

    def test_vocabulario_antigo_e_aviso(self):
        self._mutate("| Recomendação | **ADAPT** |", "| Recomendação | **ADAPTAR** |")
        self.assertWarning("vocabulário antigo")

    def test_blocked_legitimo_nao_e_erro(self):
        self._mutate("| Estado da pesquisa | DOCUMENTED |", "| Estado da pesquisa | BLOCKED |")
        self._mutate("| Resultado de execução | STATIC_REVIEW_ONLY |",
                     "| Resultado de execução | BLOCKED |")
        idx = self.root / "RESEARCH-INDEX.md"
        idx.write_text(idx.read_text(encoding="utf-8").replace("DOCUMENTED", "BLOCKED"),
                       encoding="utf-8")
        self.regen()
        self.assertClean()

    def test_not_run_legitimo_nao_e_erro(self):
        self._mutate("| Resultado de execução | STATIC_REVIEW_ONLY |",
                     "| Resultado de execução | NOT_RUN |")
        self.regen()
        self.assertClean()


# ------------------------------------------------------------------ índice
class TestIndice(Base):
    def test_recomendacao_divergente(self):
        idx = self.root / "RESEARCH-INDEX.md"
        idx.write_text(idx.read_text(encoding="utf-8").replace("**ADAPT**", "**REJECT**"),
                       encoding="utf-8")
        self.assertError("recomendação divergente")

    def test_estado_divergente(self):
        idx = self.root / "RESEARCH-INDEX.md"
        idx.write_text(idx.read_text(encoding="utf-8").replace("| DOCUMENTED |", "| TESTED |"),
                       encoding="utf-8")
        self.assertError("estado divergente")


# ------------------------------------------------------------------ catálogo
class TestCatalogo(Base):
    def test_catalogo_ausente(self):
        (self.root / "catalog/catalog.tsv").unlink()
        self.assertError("catalog/catalog.tsv ausente")

    def test_catalogo_dessincronizado(self):
        p = self.root / "catalog/catalog.tsv"
        p.write_text(p.read_text(encoding="utf-8").replace("ADAPT", "REJECT"), encoding="utf-8")
        self.assertError("não corresponde ao gerado")

    def test_catalogo_com_linha_extra(self):
        p = self.root / "catalog/catalog.tsv"
        p.write_text(p.read_text(encoding="utf-8") + "LR-FANTASMA-001\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\n",
                     encoding="utf-8")
        val = self.run_val()
        self.assertTrue(any("linha sem relatório" in e or "não corresponde ao gerado" in e
                            for e in val.errors))

    def test_gerador_e_deterministico(self):
        a = build_catalog.render(build_catalog.build_rows(self.root))
        b = build_catalog.render(build_catalog.build_rows(self.root))
        self.assertEqual(a, b)


# ------------------------------------------------------------------ test-log
class TestRegistroDeTeste(Base):
    def _log(self, linha: str) -> None:
        (self.root / "data/testing/test-log.tsv").write_text(
            "date\tobject_id\tversion\tlevel\tenvironment\tprocedure\tresult\tevidence\tnot_tested\trepro\n"
            + linha + "\n", encoding="utf-8")

    def test_alegar_teste_sem_registro(self):
        p = self.root / "repositories/foo/REPORT.md"
        p.write_text(p.read_text(encoding="utf-8").replace("STATIC_REVIEW_ONLY", "LOCAL_TESTS_PASS"),
                     encoding="utf-8")
        self.assertError("sem linha em data/testing/test-log.tsv")

    def test_alegar_teste_com_registro_passa(self):
        self._log("2026-11-20\tLR-REPO-001\tc0ffee\t1\tsandbox\tpytest\tLOCAL_TESTS_PASS\tok\tnada\tpytest")
        p = self.root / "repositories/foo/REPORT.md"
        p.write_text(p.read_text(encoding="utf-8").replace("STATIC_REVIEW_ONLY", "LOCAL_TESTS_PASS"),
                     encoding="utf-8")
        self.regen()
        self.assertClean()

    def test_cabecalho_errado(self):
        (self.root / "data/testing/test-log.tsv").write_text("data\tobjeto\n", encoding="utf-8")
        self.assertError("cabeçalho inesperado")

    def test_linha_com_colunas_faltando(self):
        self._log("2026-11-20\tLR-REPO-001\tc0ffee\t1")
        self.assertError("colunas")

    def test_resultado_invalido_no_log(self):
        self._log("2026-11-20\tLR-REPO-001\tc0ffee\t1\tsb\tp\tDEU_BOM\tok\tnada\trepro")
        self.assertError("resultado fora do vocabulário")

    def test_data_invalida_no_log(self):
        self._log("ontem\tLR-REPO-001\tc0ffee\t1\tsb\tp\tPARTIAL\tok\tnada\trepro")
        self.assertError("data inválida")

    def test_registro_sem_alegacao_e_aviso(self):
        self._log("2026-11-20\tLR-REPO-001\tc0ffee\t1\tsb\tp\tLOCAL_SMOKE_PASS\tok\tnada\trepro")
        self.assertWarning("tem registro de teste mas declara")


# ------------------------------------------------------------------ decisões
class TestDecisoes(Base):
    def _dr(self, extra: str) -> None:
        (self.root / "decisions/PENDING/DR-0001-TESTE.md").write_text(
            "# DR-0001 — teste\n\n| Campo | Valor |\n|---|---|\n| ID | DR-0001 |\n" + extra,
            encoding="utf-8")

    def test_dr_sem_alcance(self):
        self._dr("")
        self.assertWarning("DR sem campo | Alcance |")

    def test_dr_com_alcance_governanca(self):
        self._dr("| Alcance | **GOVERNANCA** — administrativa |\n")
        val = self.run_val()
        self.assertFalse(any("Alcance" in w for w in val.warnings))

    def test_dr_com_alcance_adocao(self):
        self._dr("| Alcance | **ADOCAO** |\n")
        self.assertError("alcance não é GOVERNANCA")


class TestDigests(Base):
    def test_digest_sem_metadados(self):
        (self.root / "cross-project/x").mkdir(parents=True, exist_ok=True)
        (self.root / "cross-project/x/DIGEST.md").write_text(
            "# Digest\n\nconteúdo\n\nVer `MISSION.md`.\n", encoding="utf-8")
        self.assertWarning("digest sem metadados")


# ------------------------------------------------------------------ contagens
class TestContagens(Base):
    def test_contagem_de_md_errada(self):
        p = self.root / "README.md"
        texto = p.read_text(encoding="utf-8")
        real = len(list(self.root.rglob("*.md")))
        p.write_text(texto.replace(f"| Arquivos Markdown | {real} |",
                                   f"| Arquivos Markdown | {real - 1} |"), encoding="utf-8")
        self.assertError(f"README diz {real - 1} arquivos .md")

    def test_contagem_de_objetos_errada(self):
        p = self.root / "README.md"
        p.write_text(p.read_text(encoding="utf-8").replace("| Relatórios externos | 1 objetos |",
                                                           "| Relatórios externos | 2 objetos |"),
                     encoding="utf-8")
        self.assertError("README diz 2 objetos")

    def test_contagem_do_catalogo_errada(self):
        p = self.root / "README.md"
        p.write_text(p.read_text(encoding="utf-8").replace("— 1 linhas", "— 3 linhas"),
                     encoding="utf-8")
        self.assertError("catálogo com 3 linhas")


# ------------------------------------------------------------------ licenças
class TestLicencas(Base):
    def test_digest_cita_objeto_inexistente(self):
        p = self.root / "cross-project/licensing/READY-TO-USE-LICENSES.md"
        p.write_text(p.read_text(encoding="utf-8").replace(
            "| `LR-REPO-001` | foo |", "| `LR-REPO-999` | foo |"), encoding="utf-8")
        self.assertError("digest de licenças cita objeto inexistente")

    def test_matriz_com_objeto_fora_do_digest(self):
        m = self.root / "data/inventory/license-matrix.tsv"
        m.write_text(m.read_text(encoding="utf-8")
                     + "LR-OUTRO-001\tx\tMIT\tLICENSE\ta\tsim\tsim\tsim\tsim\tsim\tnao\tnao\tMIT\tX\tY\n",
                     encoding="utf-8")
        self.assertWarning("na matriz de licença e fora do digest")


# ------------------------------------------------------------------ órfãos
class TestOrfaos(Base):
    def test_documento_orfao(self):
        (self.root / "governance").mkdir(exist_ok=True)
        (self.root / "governance/ORFAO.md").write_text("# Órfão\n\ntexto\n", encoding="utf-8")
        self.assertWarning("documento órfão")

    def test_documento_referenciado_nao_e_orfao(self):
        (self.root / "governance").mkdir(exist_ok=True)
        (self.root / "governance/LIGADO.md").write_text("# Ligado\n\ntexto\n", encoding="utf-8")
        p = self.root / "MISSION.md"
        p.write_text("# MISSION\n\nver `governance/LIGADO.md`\n", encoding="utf-8")
        val = self.run_val()
        self.assertFalse(any("LIGADO" in w for w in val.warnings))


# ------------------------------------------------------------------ vencimento
class TestVencimento(Base):
    def test_revisao_vencida_e_nota_nao_erro(self):
        p = self.root / "repositories/foo/REPORT.md"
        p.write_text(p.read_text(encoding="utf-8").replace("2027-02-17", "2026-01-01"),
                     encoding="utf-8")
        self.regen()
        val = v.Validator(self.root, TODAY).run()
        self.assertEqual(val.errors, [])
        self.assertTrue(any("revisão vencida" in n for n in val.notes))

    def test_vencimento_nao_reescreve_relatorio(self):
        p = self.root / "repositories/foo/REPORT.md"
        antes = p.read_text(encoding="utf-8").replace("2027-02-17", "2026-01-01")
        p.write_text(antes, encoding="utf-8")
        self.regen()
        v.Validator(self.root, TODAY).run()
        self.assertEqual(p.read_text(encoding="utf-8"), antes)
        self.assertNotIn("| Estado da pesquisa | STALE |", p.read_text(encoding="utf-8"))

    def test_data_de_referencia_e_injetavel(self):
        p = self.root / "repositories/foo/REPORT.md"
        p.write_text(p.read_text(encoding="utf-8").replace("2027-02-17", "2026-12-31"),
                     encoding="utf-8")
        self.regen()
        antes = v.Validator(self.root, dt.date(2026, 11, 20)).run()
        depois = v.Validator(self.root, dt.date(2027, 1, 15)).run()
        self.assertFalse(any("vencida" in n for n in antes.notes))
        self.assertTrue(any("vencida" in n for n in depois.notes))

    def test_hoje_e_lido_do_relogio_quando_nao_injetado(self):
        val = v.Validator(self.root)
        self.assertEqual(val.today, dt.date.today())


# ------------------------------------------------------------------ integração
class TestIntegracaoRepositorioReal(unittest.TestCase):
    def test_repositorio_real_passa(self):
        raiz = Path(__file__).resolve().parent.parent
        if not (raiz / "RESEARCH-INDEX.md").exists():
            self.skipTest("não é o repositório do Lia-Research")
        val = v.Validator(raiz).run()
        self.assertEqual(val.errors, [], f"erros no repositório real: {val.errors}")
        self.assertGreaterEqual(len(val.reports()), 20)

    def test_catalogo_real_em_dia(self):
        raiz = Path(__file__).resolve().parent.parent
        if not (raiz / "catalog/catalog.tsv").exists():
            self.skipTest("sem catálogo")
        esperado = build_catalog.render(build_catalog.build_rows(raiz))
        self.assertEqual((raiz / "catalog/catalog.tsv").read_text(encoding="utf-8"), esperado)


if __name__ == "__main__":
    unittest.main(verbosity=1)
