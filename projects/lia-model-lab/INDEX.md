# Índice — Lia Model Lab

---

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem |
|---|---|---|---|
| `LR-LIC-005` | Licenças prontas: pesos de modelo têm licença própria, fora do framework | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 18 relatórios |
| `LR-MODEL-003` | LFM3 (avaliação combinada Project + Model-Lab) | `cross-project/ai-models/LFM3-EVALUATION.md` | `docs/17-LFM3-RESEARCH.md` + `LIA-LFM3-EVALUATION.md` |
| `LR-MODEL-001` | Catálogo de modelos/providers | `cross-project/model-routing/MODEL-CATALOG-DIGEST.md` | `docs/05-FOUNDATION-MODEL-COMPARISON.md` + research do Project |
| `LR-MODEL-004` | Catálogo de capacidades (44/131/0) | `cross-project/ai-models/CAPABILITY-CATALOG-DIGEST.md` | `lia-capability-catalog/` |
| `LR-HW-001` | Windows 11 + RX 580 | `cross-project/hardware/WINDOWS-AMD-COMPATIBILITY.md` | `docs/08-HARDWARE-INFRASTRUCTURE.md` + research do Project |
| `LR-HW-002` | Consumo em desktop sempre ativo | `cross-project/hardware/RUNTIME-RESOURCE-RESEARCH.md` | `2026-11-14-runtime-resource-research.md` |
| `LR-AGENT-001` | Métricas de energia/FLOPs e contrato de engine | `repositories/openjarvis/REPORT.md` | externo (novo) |
| `LR-PROV-001` | RouterHub (provider rejeitado) | `repositories/routerhub/REPORT.md` | externo (novo) |
| `LR-FORGE-001` | Download de pesos com retomada (GPL) | `repositories/misterdownloadmanager/REPORT.md` | externo (novo) |
| `LR-STUDIO-004` | Contrato tipado de capability (`Role`/`Capability`/`InputRole`) e proibição de fallback silencioso | `repositories/artcraft/REPORT.md` | pesquisa externa (novo) |
| `LR-BENCH-001` | Disciplina de benchmark reproduzível | `repositories/sculptforge/REPORT.md`, `repositories/manimgx/REPORT.md` | externo (novo) |

## 2. ADRs do projeto (fonte canônica: o próprio projeto)

| ADR | Documento | Por que não foi copiado |
|---|---|---|
| 0001 | `docs/adr/0001-CONSOLIDATION.md` | decisão do projeto |
| 0002 | `docs/adr/0002-LOCAL-INFERENCE.md` | decisão do projeto |
| 0003 | `docs/adr/0003-INFERENCE-HARDENING.md` | decisão do projeto |
| 0004 | `docs/adr/0004-WINDOWS-MEMORY.md` | decisão do projeto (2 versões) |
| 0005 | `docs/adr/0005-WINDOWS-CONTROLLED-LAUNCHER.md` | decisão do projeto |
| 0006 | `docs/adr/0006-QWEN35-PINNED-CPU-PILOT.md` | decisão do projeto |

Registrados aqui como **contexto**, não reescritos. O Lia-Research não revoga nem
reinterpreta ADR de projeto.

## 3. Documentos com múltiplas versões (atenção)

| Documento | Versões | Ação recomendada |
|---|---:|---|
| `docs/13-GOVERNANCA-DE-EXPERIMENTOS.md` | 7 | consolidar na origem |
| `docs/08-HARDWARE-INFRASTRUCTURE.md` | 4 | consolidar; a maior (9,4 KB) é a mais nova |
| `docs/SOURCES.md` | 4 | consolidar |
| `docs/VALIDATION.md` | 4 | consolidar |
| `docs/16-REAL-INFERENCE-PILOT.md` | 4 | consolidar |

Nenhuma consolidação foi feita nesta base — é decisão e trabalho do projeto.

## 4. Skills (9) — únicas em `main` em todo o ecossistema

| Skill | Função | Licença no payload |
|---|---|---|
| `capability-mapping` | mapear capacidades | ❌ |
| `dataset-governance` | governança de dataset | ❌ |
| `experiment-reproducibility` | reprodutibilidade | ❌ |
| `finetuning-plan` | plano de fine-tuning | ❌ |
| `lia-brand-consistency-review` | revisão de marca | ❌ (duplica `lia-brand-check` do Forge) |
| `model-candidate-research` | pesquisa de candidato | ❌ |
| `model-evaluation` | avaliação de modelo | ❌ |
| `model-license-release-review` | gate de licença | ❌ (candidata a `NOTICE` obrigatório) |
| `multi-agent-orchestration` | orquestração | ❌ (duplica Project + `alethe`) |

## 5. Lacunas

| Lacuna | Situação |
|---|---|
| Nenhum modelo do catálogo validado no hardware real | 44 registros, 0 medições |
| Sem pesquisa dedicada de visão/multimodal | inexistente (diretório não criado — ver README §8 do Lia-Research) |
| Versões divergentes de medição | 5 documentos, até 7 versões |
| Benchmark de energia/FLOPs | inexistente; OpenJarvis é referência |
