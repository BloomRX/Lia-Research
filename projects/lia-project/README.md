# Lia-Project — consolidação da pesquisa existente

| Campo | Valor |
|---|---|
| Repositório de origem | `BloomRX/Lia-Project` |
| Branch padrão | `main` @ `9c7ac18` (2026-10-30, 349 commits) |
| Branch mais avançada | `arena/7fa837f0-lia-project` @ `005a324` (2026-11-17, **577 commits**) |
| Branches remotas | 12 |
| Arquivos (todas as branches) | 55.177 |
| Documentos distintos | 1.236 |
| De autoria Lia | 261 |
| Vendorizado | 975 (principalmente `airi/`) |
| Data do inventário | 2026-11-17 |

---

## 1. O que este projeto é

O produto principal do ecossistema: assistente pessoal desktop (Electron + TypeScript
+ Vue no Stage), com voz, providers de modelo, memória local, autorização de tools e
uma arquitetura desktop que passou por reavaliação recente.

## 2. Aviso de leitura obrigatório

**`main` não é o estado atual.** A branch padrão tem 349 commits; a branch de sessão
mais recente tem 577. Um agente que leia `main` recebe um estado de 2026-10-30 e perde
todo o trabalho de novembro. Este é o achado mais importante do inventário.

Segundo aviso: **975 dos 1.236 documentos não são da Lia.** São documentação upstream
do AIRI (`airi/docs/`, `airi/.agents/`), vendorizada dentro do repositório. Contar
esses arquivos como "pesquisa Lia" infla qualquer métrica em ~4×.

## 3. Mapa da documentação de autoria Lia (261 documentos)

| Área | Documentos | Onde |
|---|---:|---|
| Pesquisa (`docs/research/`) | 18 | catálogo de providers, hardware AMD, LFM3, recursos de runtime, catálogo de capacidades |
| Relatórios (`docs/reports/`) | 62 | auditorias de desktop, UI/UX, segurança, STT, validação Windows, matrizes de validação |
| Arquitetura (`docs/architecture/`) | 30 | arquitetura Lia, Stage, providers, AIRI (análise, comparação, desacoplamento), decisões |
| Decisões | 10 | `docs/architecture/decisions/` (ADR-0001 runtime desktop, benchmark C0–C8, specs) |
| Produto | ~20 | M1 voz (fases 1–5), planos de finalização, auditorias de instalação |
| Skills (`.agents/skills/`) | 35 arquivos / **22 skills** | `lia-*` e `alethe` (vendorizada) |
| Licenças | 4 | `docs/licenses/` |
| Outros | ~112 | guias, glossário, planos, benchmarks |

## 4. Temas de pesquisa consolidados

1. **Providers de modelo e arquitetura neutra** — `LIA-MODEL-PROVIDER-CATALOG.md` (29 KB),
   `LIA-MODEL-PROVIDER-ARCHITECTURE.md` (19 KB), `LIA-MODEL-PROVIDER-RECOMMENDATIONS.md` (15 KB).
2. **Hardware Windows + AMD RX 580** — `LIA-WINDOWS-AMD-MODEL-COMPATIBILITY.md`.
3. **Modelo local LFM3** — `LIA-LFM3-EVALUATION.md` (+ `LIA-Model-LaB` tem pesquisa paralela).
4. **Recursos em desktop sempre ativo** — `2026-11-14-runtime-resource-research.md`.
5. **Catálogo de capacidades** — `lia-capability-catalog/` (8 documentos): 44 registros
   catalogados, ~131 descobertos, **0 validados**.
6. **Arquitetura desktop e runtime** — `LIA-DESKTOP-ARCHITECTURE-AUDIT-2026-11-16.md` (66 KB),
   `LIA-DESKTOP-RUNTIME-ARCHITECTURE-DECISION.md`.
7. **AIRI: análise, comparação e desacoplamento** — 5 documentos.
8. **Segurança** — auditorias de credenciais, STT, reconciliação de segurança, sandbox do Stage.

## 5. Divergências e conflitos detectados

| Item | Situação |
|---|---|
| Pesquisa de provider em Lia-Project **e** Model-Lab | dois catálogos de modelo concorrentes; numeração e conclusões diferentes → `CONFLICTING` |
| LFM3 avaliado em dois projetos | avaliações com datas e critérios distintos → complementares, não idênticas |
| 6 versões do `README.md` em branches diferentes | nenhuma é canônica |
| `docs/DECISIONS.md` com 1,2 KB vs `DECISION-RECORD-2026-11-16.md` com 23 KB | o índice de decisões não reflete as decisões reais |

## 6. Onde está a pesquisa que importa

Ver `INDEX.md` nesta pasta. Resumo: 80% do valor está em `docs/research/`,
`docs/reports/` e `docs/architecture/`, e **quase tudo apenas em branches de sessão**.

## 7. Recomendação de preservação

O Lia-Research **não** move nem integra nada. A ação recomendada ao dono do projeto
(registrada em `RESEARCH-ROADMAP.md`) é promover para `main` os documentos de
`docs/research/` — hoje inacessíveis a quem lê a branch padrão.

---

**Pesquisa desta base que toca este projeto agora** · 2026-11-26 — layout de cache de prompt por fornecedor (`LR-UI-006` §7), parser de JSON parcial (`LR-UI-006` §5), Vault no Windows (`LR-UI-006` §10) e a matriz completa em [`comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md`](../../comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md) §4.1.
