# Esquema do catálogo — campos, estados, resultados e recomendações

| Campo | Valor |
|---|---|
| Documento | Padrão único de registro de tecnologia |
| Versão | 1.1 — 2026-11-20 (proveniência + reauditoria) |
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

Proveniência (obrigatório desde 1.1): `SHA completo` (40 caracteres, quando existir) ·
`Proveniência do SHA` · `HEAD atual`. Vocabulário fechado de `Proveniência do SHA`:

| Valor | Significado |
|---|---|
| `INFORMADO_NO_RELATORIO` | o relatório já citava SHA/tag e ele foi conferido |
| `RECUPERADO_POR_ESTABILIDADE` | não havia SHA; o upstream não recebe push desde a data analisada, então o HEAD atual é a árvore lida |
| `CANDIDATO_POR_DATA` | não havia SHA; existe um commit cuja data casa com a leitura, mas não é prova |
| `INCOMPLETA_ORGANIZACAO` | o objeto é organização/serviço: não existe commit único |

Regra: **não inventar SHA**. Quando a versão não é determinável, o campo diz qual dos
rótulos incompletos se aplica e o relatório explica por quê. Versão analisada histórica
**nunca** é reescrita com o SHA recuperado — o recuperado vai no campo de proveniência.

Conferência de upstream (opcional, recomendado): `Upstream conferido` — data + HEAD atual +
se mudou desde a versão analisada. Confirmar que o repositório existe **não** é reler o
conteúdo: `Upstream conferido` não promove estado nem zera `Próxima revisão`.

## 3. Estados da pesquisa

`DISCOVERED` · `TRIAGED` · `INVESTIGATING` · `DOCUMENTED` · `TESTED` ·
`PARTIALLY_TESTED` · `NOT_TESTED` · `BLOCKED` · `STALE` · `SUPERSEDED` · `CONFLICTING`

Regra: `DOCUMENTED` exige >1 fonte lida. `TESTED` exige linha no `data/testing/test-log.tsv`.
`STALE` é automático quando `Próxima revisão` < hoje.

`TESTED` exige linha de execução **com resultado de teste** no log (`LOCAL_TESTS_PASS`,
`LOCAL_TESTS_FAIL`, `LOCAL_SMOKE_PASS`, `PARTIAL`); linha `BLOCKED` documenta a tentativa e
**não** promove o estado. `PARTIALLY_TESTED` cobre execução real com cobertura incompleta.

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

## 5.1. Reauditoria (obrigatório quando `Última verificação` > `Data da pesquisa`)

Cada relatório reavaliado carrega uma seção `Reauditoria AAAA-MM-DD` com **oito** campos:

`Versão anteriormente analisada` · `Versão novamente examinada` · `Método` ·
`Mudanças encontradas` · `Evidências novas` · `Testes próprios` · `Testes independentes` ·
`Conclusão` · `Próxima revisão`.

A `Conclusão` precisa dizer se a recomendação foi **mantida** ou **alterada**. Se mantida,
diz o motivo atual; se o motivo mudou (ex.: `sculptforge`, onde o GPL deixou de bloquear
script), o relatório registra o antes e o depois em vez de repetir a justificativa antiga.
Reescrever histórico é erro; declarar "reavaliado" sem mudança é permitido, desde que a
evidência lida esteja nomeada.

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
