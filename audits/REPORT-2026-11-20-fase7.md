# Relatório final — rodada 7 (2026-11-20)

| Campo | Valor |
|---|---|
| Pedido | correções, validação e reauditoria técnica real (7 fases) |
| Branch | `arena/7cf9c65e-lia-research` |
| Commits desta rodada | `5a9eead` (ferramentas) · `dc9973b` (pesquisa) · este commit (relatório) |
| Estado final do validador | **0 erros · 0 avisos · 7 notas** (`python3 tools/validate.py`) |
| Testes do validador | **76 · OK** (`python3 -B -m unittest tools.test_validate`) |

## 1. As 7 fases — o que ficou pronto e o que não

| Fase | Entrega | Situação |
|---|---|---|
| 1. Validador | `tools/validate.py` reescrito (classe, 18 verificações, data dinâmica, `--json`, `LIA_TODAY`), `tools/test_validate.py` com 76 testes | **feito** |
| 2. Proveniência | `audits/PROVENANCE-2026-11-20.md`, TSV de 23 linhas, 3 campos novos em todos os cabeçalhos | **feito** |
| 3. Reauditoria de upstream | `audits/REAUDIT-2026-11-20.md` + `compare` por objeto | **feito** |
| 4. Reauditoria **técnica** + testes | seção `Reauditoria 2026-11-20` nos 23 relatórios, `audits/TECHNICAL-REAUDIT-2026-11-20.md` | **feito, com lacunas declaradas** |
| 5. Reconciliação | índice, 5 índices de projeto, matriz de licenças, digest de licenças, esquema do catálogo, protocolo de teste, roadmap | **feito** |
| 6. Fila | `RESEARCH-BACKLOG.md` §7 — decisão escrita para 17 triados + 6 candidatos | **feito** |
| 7. Fechamento | validador verde, 3 commits, push nesta branch | **feito** |

## 2. Números verificáveis

| Medida | Valor | Onde conferir |
|---|---|---|
| Objetos inventariados | **23** (22 herdados + `LR-STUDIO-006`) | `catalog/catalog.tsv` (23 linhas × 18 colunas) |
| Objetos efetivamente reavaliados | **23** (22 herdados + o novo) | 23 seções `## Reauditoria 2026-11-20` |
| Upstreams com commit novo desde a análise | **10 de 22 confirmados** (+1 medido a partir do SHA candidato: `freellmapi`, 4 commits) | `audits/TECHNICAL-REAUDIT-2026-11-20.md` §2 |
| Commits somados no intervalo | **3.576** (soma dos `ahead` dos 11 objetos) | `compare` da API, por objeto |
| SHAs completos no cabeçalho | **21 de 23** | `data/inventory/provenance-2026-11-20.tsv` |
| SHAs que faltavam e continuam sem prova | **2** (`ai-memory`, `freellmapi`: candidato por data) | §2.2 do documento de proveniência |
| Organizações declaradas incompletas | **2** (`rescript-lang`, `routerhub`) | idem |
| Suítes próprias executadas | **5** | `data/testing/test-log.tsv` |
| Asserções aprovadas | 17 · 65 · 65 · 3.530 · 2.044 | idem |
| Execuções parciais | **2** (`claude-trading-skills`, `freellmapi`) | idem |
| Objetos bloqueados por toolchain | **9** | idem, `result = BLOCKED` |
| Avaliações externas usadas | CI oficial no HEAD de **11** repositórios + dados de release de **14** | §3 |
| Recomendações alteradas | **0** | `catalog/catalog.tsv` |
| Motivos de recomendação alterados | **1** (`sculptforge`) | relatório do objeto, seção Reauditoria |
| Itens de fila com decisão | **23** (17 + 6, com `uv` deduplicado) | `RESEARCH-BACKLOG.md` §7 |
| Erros do validador na entrega | **0** | §5 |

## 3. Resultado por objeto (resumo)

**Com commit novo (10):** `ha-mcp` +41 · `misterdownloadmanager` +70 · `sculptforge` +285 ·
`openjarvis` +7 · `claude-bughunter` +8 · `claude-trading-skills` +15 · `vercel-ui` +109 ·
`plannotator` +1.511 · `artcraft` +1.011 · `openidea` +515.

**Sem commit novo (11):** `ai-design-skills`, `ai-memory`, `awesome-gamedev-agent-skills`,
`brutal`, `claude-code-game-studios`, `cloudflare-security-audit-skill`, `manimgx`,
`meldwork`, `pixelfx`, `rescript-lang`, `routerhub`, `unslop`.

Nos sem-commit a reavaliação não repetiu a frase antiga: conferiu **licença no HEAD**,
**releases posteriores**, **CI no HEAD** e, quando havia como, **executou a suíte**.

**Achados materiais:**

1. `sculptforge` ganhou `LICENSE-EXCEPTION.md` — permissão adicional do §7 da GPLv3 para
   script via API/CLI/MCP. A recomendação continua `REFERENCE_ONLY`, mas o motivo mudou:
   o bloqueio jurídico para script deixou de existir. O app continua GPL-3.0.
2. `ha-mcp` passou a exigir **Python `>=3.14,<3.15`** — condição de contorno nova.
3. `plannotator` tem **1 check vermelho no HEAD** e virou família de plugins (Cline,
   opencode, pi) — o relatório o descrevia como app único.
4. `openidea` no HEAD só apresenta checks *skipped*: **não há evidência de CI verde**.
5. `misterdownloadmanager` passou a rodar ClusterFuzzLite, CodeQL e Scorecard.

## 4. Testes — o que foi executado de verdade

| Objeto | Comando | Resultado |
|---|---|---|
| `ai-design-skills` | `python -m unittest discover -s tests` | **17/17 OK** |
| `claude-bughunter` | `python -m unittest discover -s tests` | **65/65 OK** |
| `cloudflare-security-audit-skill` | `node validate-findings.test.cjs` + `validate-coverage-ledger.test.cjs` | **34/34 + 31/31 OK** |
| `claude-trading-skills` | `pytest examples/…/tests` · `pytest scripts/tests` | 24 passam/8 pulam · **3.506 passam, 88 falham, 73 erro de coleta** |
| `freellmapi` | `npm test` | **2.044 passam, 1.796 falham, 1.656 pulam** (749 por `better-sqlite3` ausente) |

As duas últimas são `PARTIAL`: falha de ambiente não vira falha do projeto, e suíte que não
conclui não vira `TESTED`. **Nenhum objeto Rust/C#/C++/Blender foi executado** — `cargo`,
`dotnet`, CMake e Blender não existem no sandbox. Ficou registrado como `BLOCKED`, com a
evidência do bloqueio, não como "testado por inspeção".

## 5. Validação

```
$ python3 tools/validate.py
erros: 0 · avisos: 0 · notas: 7 · data de referência: 2026-11-20
$ python3 tools/validate.py --today 2027-06-01
erros: 0 · avisos: 0 · notas: 27   # os STALE aparecem como diagnóstico, sem reescrever nada
$ python3 -B -m unittest tools.test_validate
Ran 76 tests — OK
$ python3 tools/build_catalog.py --check
catalog.tsv em dia (23 linhas)
```

As 7 notas são IDs que vivem no índice e em digests sem cabeçalho próprio
(`LR-BENCH-001`, `LR-PROJ-001..005`, `LR-SEC-003`) — declarado, não escondido.

**Incidente de push (registrado porque aconteceu):** o GitHub bloqueou o primeiro push por
*secret scanning* — as fixtures de webhook do Slack em `tools/test_validate.py` eram
literais, ainda que inventadas. Correção: as fixtures passaram a ser montadas em runtime.
Não houve tentativa de liberar o segredo no painel do GitHub.

## 6. O que esta rodada **não** fez

- Não executou nenhuma suíte Rust/C++/.NET: 9 objetos seguem `BLOCKED` por ambiente.
- Não testou Skill com entrada sintética — é a lacuna mais antiga da base ("0 Skills
  medidas") e virou a prioridade 1 da fila (`promptfoo`, `deepeval`).
- Não usou benchmark independente; usou CI oficial e releases (evidência `REPORTED`/`OBSERVED`).
- Não tocou em Nível 3: nenhuma conta, nenhuma API autenticada, nenhum hardware.
- Não reescreveu versão analisada histórica de nenhum relatório.
- Não alterou nenhuma recomendação de rótulo, e não converteu nenhuma em decisão de adoção:
  as 18 DRs continuam `GOVERNANCA`, com **0 decisões de adoção**.

## 7. Pendências

| # | Pendência | Por que ficou |
|---|---|---|
| 1 | Rodar as suítes dos 9 bloqueados | precisa de toolchain (`cargo`, `dotnet`, CMake, Blender, Python 3.14) |
| 2 | Medir uma Skill com entrada sintética | depende de `promptfoo`/`deepeval` (fila, prioridade 1–2) |
| 3 | Triar as 88 falhas de `claude-trading-skills` uma a uma | tempo; causa observada já registrada |
| 4 | Confirmar a árvore lida de `ai-memory` e `freellmapi` | não há registro de SHA na leitura original |
| 5 | Rever termos do `routerhub` | exige abrir contrato no site; `BLOCKED` declarado |

Voltar: `audits/README.md` · `RESEARCH-CHANGELOG.md`
