# Lia Model Lab — consolidação da pesquisa existente

| Campo | Valor |
|---|---|
| Repositório de origem | `BloomRX/Lia-Model-Lab` |
| Branch padrão | `main` @ `3ec4313` (2026-11-02, 36 commits) |
| Branch mais avançada | `codex/qwen35-first-pilot` @ `957e33b` (2026-11-02) |
| Branches remotas | 8 |
| Arquivos | 687 · **90 documentos, todos de autoria Lia** |
| Skills | **9** — e é o **único projeto com Skills em `main`** |
| Data do inventário | 2026-11-17 |

---

## 1. O que este projeto é

Avaliação de modelos e hardware, experimentos de inferência local verificáveis e
governança de experimento. É o projeto com o **melhor registro de decisão** do
ecossistema: 8 ADRs numerados, com contexto, alternativas e consequências.

## 2. Situação do conhecimento

Diferente dos outros quatro, aqui `main` contém quase tudo: 36 commits, os 8 ADRs, as
9 skills, `docs/SOURCES.md` (26 KB de fontes) e `docs/VALIDATION.md` (24 KB). As
branches de sessão acrescentam pilotos específicos (Qwen3.5, memory adapter, launcher).

## 3. ADRs (decisões do projeto — pertencem a ele, não a esta base)

| ADR | Assunto | Status |
|---|---|---|
| `0001-CONSOLIDATION` | consolidação oficial e fundação offline | aceita |
| `0002-LOCAL-INFERENCE` | inferência local verificável antes de SFT | aceita |
| `0003-INFERENCE-HARDENING` | autorização operacional e hardening | aceita |
| `0004-WINDOWS-MEMORY` | diagnóstico de memória Windows por política | aceita |
| `0005-WINDOWS-CONTROLLED-LAUNCHER` | launcher controlado no Windows | aceita |
| `0006-QWEN35-PINNED-CPU-PILOT` | piloto Qwen3.5 em CPU com pin | aceita |

## 4. Pesquisa existente

| Documento | Tamanho | Tema |
|---|---:|---|
| `docs/17-LFM3-RESEARCH.md` | 22 KB | LFM3: pesquisa, contratos e decisão de arquitetura |
| `docs/01-AIRI-CAPABILITY-INVENTORY.md` | 17 KB | inventário de capacidades do AIRI |
| `docs/05-FOUNDATION-MODEL-COMPARISON.md` | 18 KB | comparação de modelos de fundação |
| `docs/16-REAL-INFERENCE-PILOT.md` | 22–23 KB (4 versões) | piloto real de inferência |
| `docs/SOURCES.md` | 26 KB | fontes (com versões divergentes por branch) |
| `docs/VALIDATION.md` | 24 KB | validação |
| `docs/18-FINAL-AUDIT.md` | 20 KB | auditoria final da PR #1 |
| `docs/09-BENCHMARK-STRATEGY.md` | 7,3 KB | estratégia de benchmark |
| `docs/08-HARDWARE-INFRASTRUCTURE.md` | 8,9 KB (4 versões por branch) | infraestrutura de hardware |
| `docs/12-OPEN-DECISIONS.md` | 6,2 KB | decisões abertas |
| `docs/13-GOVERNANCA-DE-EXPERIMENTOS.md` | 5,9 KB (7 versões) | governança de experimentos |
| `docs/14-ORQUESTRACAO-DE-AGENTES.md` | 4,2 KB | orquestração |
| `docs/04-MODEL-FAMILY-ARCHITECTURE.md` | 6,8 KB | arquitetura da família de modelos |
| `docs/00-PROJECT-AUDIT.md` | 4,6 KB | auditoria inicial |

## 5. Conflito de versões (o mais severo do inventário)

O Model-Lab tem documentos com **4 e 7 versões divergentes** entre branches:

| Documento | Versões | Tamanhos |
|---|---:|---|
| `docs/13-GOVERNANCA-DE-EXPERIMENTOS.md` | **7** | 5,9 KB (idênticas em 6) + variante |
| `docs/08-HARDWARE-INFRASTRUCTURE.md` | **4** | 5,9 / 7,8 / 8,9 / 9,4 KB |
| `docs/SOURCES.md` | **4** | 21 / 24 / 26 / 29 KB |
| `docs/VALIDATION.md` | 4 | 12 / 17,5 / 23,5 / 26 KB |
| `docs/16-REAL-INFERENCE-PILOT.md` | 4 | 16,6 / 19,9 / 22,4 / 23 KB |

Cada branch acrescentou conteúdo e ninguém consolidou. Este é o exemplo mais claro de
por que o Lia-Research existe: **quatro versões da mesma medição, e nenhuma canônica.**

## 6. Skills (9) — as únicas em `main`

`capability-mapping` · `dataset-governance` · `experiment-reproducibility` ·
`finetuning-plan` · `lia-brand-consistency-review` · `model-candidate-research` ·
`model-evaluation` · `model-license-release-review` · `multi-agent-orchestration`.

Observação: `model-license-release-review` é "quase um gate de licença" (avaliação do
próprio inventário) — relevante para `DR-0001`.

## 7. Ligações com o Lia-Research

- Compatibilidade Windows/AMD: `cross-project/hardware/WINDOWS-AMD-COMPATIBILITY.md`
- LFM3 (combinado com a avaliação do Lia-Project): `cross-project/ai-models/LFM3-EVALUATION.md`
- Catálogo de modelos (44 registros, 0 validados): `cross-project/ai-models/CAPABILITY-CATALOG-DIGEST.md`
- OpenJarvis (métricas de energia/FLOPs): `repositories/openjarvis/REPORT.md`

---

**Pesquisa desta base que toca este projeto agora** · 2026-11-26 — banco de modelos com teto de custo e juiz calibrado (`LR-UI-006` §7), os pesos que podem ser copiados com suas licenças (§10) e a matriz em [`comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md`](../../comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md) §4.5.
