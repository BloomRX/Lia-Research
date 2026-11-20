# Esquema do catálogo — campos, estados, resultados e recomendações

| Campo | Valor |
|---|---|
| Documento | Padrão único de registro de tecnologia |
| Versão | 1.0 — 2026-11-20 |
| Canônico em | este arquivo |
| Gerado por | `tools/build_catalog.py` → `catalog/catalog.tsv` |

---

## 1. Quem manda em quê

| Artefato | Papel |
|---|---|
| `repositories/<slug>/REPORT.md` | **fonte principal** da investigação daquele objeto |
| `catalog/catalog.tsv` | visão de máquina, **derivada** do cabeçalho dos relatórios |
| `RESEARCH-INDEX.md` | índice humano de IDs e ponteiros |
| `projects/*/INDEX.md` | recorte por projeto beneficiado |

O catálogo **não** é digitado à mão: é gerado. Divergência entre catálogo e relatório é erro
do gerador ou do relatório — o validador aponta.

## 2. Campos obrigatórios por objeto

Identificação: `ID` · `Nome` · `Tipo` · `Fonte oficial` · `Repositório/página` ·
`Responsável` · `Versão analisada` (SHA/tag) · `Data da pesquisa` · `Última verificação` ·
`Próxima revisão` · `Licença` · `Proveniência`.

Avaliação: `Funcionalidades` · `Aplicações potenciais` · `Compatibilidade` · `Dependências` ·
`Segurança` · `Avaliações externas` · `Limitações` · `Evidências` · `Projetos beneficiados`.

Estado e decisão: `Estado da pesquisa` · `Resultado de execução` · `Recomendação` ·
`Decisão de adoção` (vazio = não existe decisão registrada).

Conferência de upstream (opcional, recomendado): `Upstream conferido` — data + HEAD atual +
se mudou desde a versão analisada. Confirmar que o repositório existe **não** é reler o
conteúdo: `Upstream conferido` não promove estado nem zera `Próxima revisão`.

## 3. Estados da pesquisa

`DISCOVERED` · `TRIAGED` · `INVESTIGATING` · `DOCUMENTED` · `TESTED` ·
`PARTIALLY_TESTED` · `NOT_TESTED` · `BLOCKED` · `STALE` · `SUPERSEDED` · `CONFLICTING`

Regra: `DOCUMENTED` exige >1 fonte lida. `TESTED` exige linha no `data/testing/test-log.tsv`.
`STALE` é automático quando `Próxima revisão` < hoje.

`STALE` **não** é disparado por commit novo no upstream. Divergência de upstream fica em
`Upstream conferido` e é motivo de revisão, não de mudança automática de estado: o relatório
continua válido para a versão que analisou, e diz qual versão foi essa.

## 4. Recomendações (vocabulário fechado)

`DIRECT_INTEGRATION_CANDIDATE` · `ADAPT` · `FORK_CANDIDATE` ·
`INDEPENDENT_REIMPLEMENTATION` · `REFERENCE_ONLY` · `REJECT` · `INSUFFICIENT_EVIDENCE`

Nenhuma delas autoriza adoção. São opinião técnica do pesquisador (`MISSION.md` §3).

### 4.1. Migração do vocabulário antigo

| Antigo | Novo | Observação |
|---|---|---|
| `ADOTAR` | `DIRECT_INTEGRATION_CANDIDATE` | não existia nenhum caso em 2026-11-20 |
| `ADAPTAR` | `ADAPT` | 8 relatórios migrados |
| `REFERÊNCIA` | `REFERENCE_ONLY` | 10 relatórios migrados |
| `REJEITAR` | `REJECT` | 4 relatórios migrados |
| `PENDENTE` | `INSUFFICIENT_EVIDENCE` | 0 casos |

A migração preservou o texto original entre parênteses quando a célula tinha dois valores
(ex.: `rescript-lang`: `REJECT` para adoção de stack, `REFERENCE_ONLY` para interop).

## 5. Resultado de execução (campo separado)

`NOT_RUN` · `STATIC_REVIEW_ONLY` · `OFFICIAL_CI_REVIEWED` · `LOCAL_SMOKE_PASS` ·
`LOCAL_TESTS_PASS` · `LOCAL_TESTS_FAIL` · `PARTIAL` · `BLOCKED`

## 6. Evidência (mantido)

`CONFIRMED` · `OBSERVED` · `REPORTED` · `INFERRED` · `UNVERIFIED` · `BLOCKED`

## 7. Cabeçalho canônico de relatório

```markdown
| Campo | Valor |
|---|---|
| ID | `LR-XXX-000` |
| Tipo | repositorio · mcp · skill · modelo · api-servico · paper · outro |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Recomendação | ADAPT |
| Decisão de adoção | — (nenhuma registrada) |
| Versão analisada | `repo@sha` (data) |
| Última verificação | 2026-11-20 |
| Próxima revisão | 2027-02-20 |
| Licença | MIT (`CONFIRMED`) |
| Evidência | CONFIRMED |
```
