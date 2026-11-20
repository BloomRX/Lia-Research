# archive/scripts/ — scripts de sessão, preservados

| Script | Para que serviu | Por que saiu de `tools/` |
|---|---|---|
| `collect.py` | baixar README/LICENSE/tree dos 22 alvos via `gh api`, com lista fixa `TARGETS` | lista fixa, sem parâmetro, específico da rodada de 2026-11-17 |
| `enum2.py` | enumerar branches/trees dos 5 repositórios Lia para o inventário de 43 branches | mediu o ecossistema uma vez; repetir exige contexto que só existe no relatório |
| `fetch3.py` | baixar arquivos escolhidos a partir de um `resolve.tsv` que não existe mais | depende de arquivo temporário inexistente; não roda |

Motivo de arquivar em vez de apagar: os números do inventário (`archive/historical/LIA-RESEARCH-SOURCE-INVENTORY.md`)
saíram destes scripts. Sem eles, o número fica sem método. Em `tools/` ficam apenas
ferramentas reproduzíveis: `validate.py`, `test_validate.py`, `build_catalog.py`,
`check_upstream.py`, `migrate_reports.py`.

Voltar: `archive/README.md` · `tools/`
