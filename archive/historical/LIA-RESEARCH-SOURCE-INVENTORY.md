# LIA-RESEARCH — Inventário de Fontes

> **Nota de vocabulário (2026-11-20).** Este documento é inventário de fontes (histórico) e preserva o texto da
> época. O vocabulário de recomendação foi substituído em 2026-11-20 por
> `ADAPT` / `REFERENCE_ONLY` / `REJECT` / `DIRECT_INTEGRATION_CANDIDATE`
> (`catalog/CATALOG-SCHEMA.md` §4.1). Nada aqui foi promoção a aprovação de adoção.


| Campo | Valor |
|---|---|
| Data de coleta | 2026-11-17 |
| Repositórios Lia | 5 (Project, Forge, Studio, AgentHub, Model-Lab) |
| Alvos externos | 16 objetos (14 repositórios + 2 organizações) |
| Documentos do corpus lido | 236 (manifesto com SHA em `data/inventory/corpus-manifest.tsv`) |
| Arquivos inventariados | 58.478 |

---

## 1. Regra do inventário

Toda fonte entra com: **origem + branch + commit + data + tamanho + licença lida no
arquivo + modo de aproveitamento**. O que não tiver isso não é fonte; é boato.

Modos de aproveitamento (`governance/SOURCE-PRESERVATION-POLICY.md`):
`POINTER` (só caminho e SHA) · `SUMMARY` (resumo com atribuição) · `EXCERPT` (trecho
curto citado) · `SNAPSHOT` (cópia pontual, apenas material próprio da Lia).

## 2. Repositórios do ecossistema

| Repositório | `main` | Branch mais avançada | Arquivos | Documentos | Skills | Modo |
|---|---|---|---|---|---:|---:|---|
| `BloomRX/Lia-Project` | `9c7ac18` (2026-10-30, 349 commits) | `arena/005a324` (577) | ~31.000 | 261 | 22 | POINTER + SUMMARY |
| `BloomRX/Lia-Forge` | `6bd9a5a` (4 commits) | `arena/*` | ~12.000 | 128 | 1 | POINTER + SUMMARY |
| `BloomRX/Lia-Studio` | `ba70d22` (4 commits) | `arena/*` | ~9.000 | 109 | 16 | POINTER + SUMMARY |
| `BloomRX/Lia-AgentHub` | `34a27f4` (8 commits) | `arena/bd4bfbb` | ~3.000 | 57 | biblioteca | POINTER + SUMMARY |
| `BloomRX/Lia-Model-Lab` | `3ec4313` (36 commits) | `codex/qwen35-first-pilot` | 687 | 90 | 9 | POINTER + SUMMARY |

**Alerta estrutural:** 511 dos 1.620 documentos existem apenas em branches `arena/*` ou
`codex/*`. `main` de quatro dos cinco projetos está muito atrás. Um agente que lê `main`
recebe estado antigo com aparência de atualidade — por isso todo ponteiro desta base
declara branch **e** commit.

Snapshot de segurança: `data/snapshots/lia-corpus-2026-11-17.tar.gz` (1,7 MB, 236
documentos) preserva o que foi lido, caso uma branch de sessão desapareça.

## 3. Alvos externos — 14 repositórios

| Alvo | SHA pinado | Licença (arquivo) | ★ | Modo |
|---|---|---|---:|---|
| `open-jarvis/OpenJarvis` | `6656b7fed2` | Apache-2.0 | 16.276 | POINTER + SUMMARY |
| `vercel-labs/ui` | `10b3b6c0ec` | Apache-2.0 + beta terms | 5.468 | POINTER + SUMMARY |
| `anefzaoui/misterdownloadmanager` | `d9a9ef0621` | **GPL-3.0** | 11.806 | POINTER + SUMMARY |
| `tradermonty/claude-trading-skills` | `a627d17dd1` | MIT | 6.772 | POINTER + SUMMARY |
| `homeassistant-ai/ha-mcp` | `3dd26d45fb` | MIT | 7.934 | POINTER + SUMMARY |
| `l0ng-ai/openidea` | `182285647e` | Apache-2.0 | 9.279 | POINTER + SUMMARY |
| `islandmed/SculptForge` | `363e2b86cf` | **GPL-3.0** | 722 | POINTER + SUMMARY |
| `Donchitos/Claude-Code-Game-Studios` | `abc0de79d6` | MIT | 39.886 | POINTER + SUMMARY |
| `academa-labs/manimgx` | `1fb4dd7327` | **mista (6)** | 2.784 | POINTER + SUMMARY |
| `Ryder-Sun/Meldwork` | `db9b6c84cb` | Apache-2.0 | 1.586 | POINTER + SUMMARY |
| `backnotprop/plannotator` | `b5b3077838` | Apache-2.0 | 12.935 | POINTER + SUMMARY |
| `patch-gg/pixelfx` | `5294518ce7` | MIT + NOTICE | 7.932 | POINTER + SUMMARY |
| `theclaymethod/unslop` | `0f4a07f5ca` | **nenhuma (404)** | 1.132 | POINTER apenas |
| `elayadesign/ai-design-skills` | `456d9e0d3e` | MIT | 15.818 | POINTER + SUMMARY |

Tabela completa com datas e linguagem: `data/external/pinned-targets.tsv`.

## 4. Alvos externos — 2 organizações (sem SHA de conteúdo)

| Organização | Repos | Observação |
|---|---:|---|
| `routerhubSI` | 11 | nenhum repositório de backend; `.si` = Eslovênia (`INFERRED`) |
| `rescript-lang` | 39 | monorepo `rescript` com licença mista por diretório |

Organização não tem commit: o inventário registra a lista de repos e o SHA de cada um
que foi efetivamente lido (`rescript`, `rescript-lang.org`).

## 5. Fontes normativas externas citadas (não auditadas como repositório)

| Fonte | Uso | Rótulo |
|---|---|---|
| Lista de suporte ROCm/HIP da AMD | RX 580 fora da matriz Windows | `REPORTED` |
| Documentação DirectML / Windows ML | limites de EP e execução serial | `REPORTED` |
| GitHub Security Advisories `GHSA-fmfg-9g7c-3vq7`, `GHSA-pf93-j98v-25pv` | SSRF/XSS no HA-MCP beta | `CONFIRMED` (texto do advisory) |
| `openai/codex#11284` | bug de HTTP MCP no Codex | `CONFIRMED` (issue aberta) |
| Paper arXiv 2605.17172 (OpenJarvis) | 88,7% / 5,3× | `REPORTED` — não reproduzido |
| Licença LFM Open | limite de receita | `REPORTED` (ficha do modelo) |

## 6. O que **não** foi coletado

| Não coletado | Por quê |
|---|---|
| Código-fonte de terceiros | só ponteiro + SHA; cópia desnecessária e arriscada |
| Binários, releases, pesos de modelo | tamanho e licença |
| Dados de conta, telemetria, screenshots de sessão | política de segurança |
| Termos de serviço do RouterHub | `BLOCKED` — não publicados |
| Benchmarks próprios | exige execução (fase 4) |
| Licença das 28 skills AIRI e do `alethe` | **coletado** em 2026-11-17 (`LR-LIC-003`); origem individual de 19 delas segue `UNVERIFIED` |

## 7. Rastreabilidade

```text
relatório (repositories/*/REPORT.md)
  └─ seção 16 (Evidências e fontes)
       └─ E<n> com rótulo + data
            └─ repo@sha:caminho
                 └─ data/external/pinned-targets.tsv (metadados)
                      └─ data/inventory/corpus-manifest.tsv (hash do que foi lido)
```

Se qualquer elo faltar, a afirmação deixa de ser evidência e passa a ser opinião —
e precisa ser rebaixada a `INFERRED` no relatório.
