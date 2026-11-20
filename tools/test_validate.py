#!/usr/bin/env python3
"""Testes do validador. Rodar: python3 tools/test_validate.py

Sem dependências: usa `unittest` da biblioteca padrão. Cobre o que o validador
promete distinguir: relatório correto que passa, erro que bloqueia, aviso de
conteúdo, e pendência externa legítima que **não** é erro.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate as v  # noqa: E402


class TestHeader(unittest.TestCase):
    def test_le_campos_do_cabecalho(self):
        text = (
            "# T\n\n| Campo | Valor |\n|---|---|\n"
            "| ID | `LR-MCP-001` |\n| Estado da pesquisa | DOCUMENTED |\n"
            "\n## seção\n| ID | `LR-OUTRO-001` |\n"
        )
        f = v.header_block(text)
        self.assertEqual(f["ID"], "`LR-MCP-001`")
        self.assertEqual(f["Estado da pesquisa"], "DOCUMENTED")

    def test_para_no_primeiro_bloco(self):
        text = "| A | 1 |\n\ntexto\n\n| B | 2 |\n"
        self.assertNotIn("B", v.header_block(text))

    def test_ignora_linha_separadora(self):
        f = v.header_block("| Campo | Valor |\n|---|---|\n| ID | x |\n")
        self.assertNotIn("---", f)


class TestVocabulario(unittest.TestCase):
    def test_recomendacoes_sao_fechadas(self):
        self.assertEqual(len(v.RECS), 7)
        self.assertIn("ADAPT", v.RECS)
        self.assertIn("REFERENCE_ONLY", v.RECS)
        self.assertNotIn("ADAPTAR", v.RECS)
        self.assertNotIn("ADOTAR", v.RECS)

    def test_estados_e_resultados_nao_se_misturam(self):
        # `BLOCKED` é a única palavra que existe nos dois vocabulários: bloqueio de
        # pesquisa (falta fonte) e bloqueio de execução (falta hardware/autorização).
        self.assertEqual(v.STATES & v.EXEC, {"BLOCKED"})
        self.assertNotIn("TESTED", v.EXEC)
        self.assertNotIn("LOCAL_TESTS_PASS", v.STATES)

    def test_bloqueado_e_pendencia_legitima(self):
        # BLOCKED existe nos dois vocabulários e não é erro por si só
        self.assertIn("BLOCKED", v.STATES)
        self.assertIn("NOT_RUN", v.EXEC)


class TestRegrasDeArquivo(unittest.TestCase):
    def test_detecta_segredo(self):
        achou = any(p.search("token: ghp_" + "a" * 30) for p in v.SECRETS)
        self.assertTrue(achou)

    def test_nao_marca_texto_inocente(self):
        self.assertFalse(any(p.search("a chave fica no cofre do sistema") for p in v.SECRETS))

    def test_detecta_chave_privada(self):
        achou = any(p.search("-----BEGIN RSA PRIVATE KEY-----") for p in v.SECRETS)
        self.assertTrue(achou)

    def test_real_relatorio_do_repo_passa_no_cabecalho(self):
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        p = os.path.join(raiz, "repositories/ha-mcp/REPORT.md")
        f = v.header_block(open(p, encoding="utf-8").read())
        rec = f["Recomendação"]
        self.assertTrue(any(t in rec for t in v.RECS), rec)
        self.assertIn(f["Estado da pesquisa"].split()[0], v.STATES)
        self.assertIn(f["Resultado de execução"].split()[0], v.EXEC)


if __name__ == "__main__":
    unittest.main(verbosity=2)
