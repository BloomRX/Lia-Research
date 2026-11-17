# Comparação — como medir modelo e hardware

| Campo | Valor |
|---|---|
| ID | `LR-CMP-003` |
| Pergunta | qual abordagem de benchmark serve à Lia, dado que nada foi medido ainda |
| Data | 2026-11-17 |
| Evidência | `CONFIRMED` (métodos lidos); nenhum resultado próprio |

## 1. Quatro abordagens observadas

| Abordagem | Onde | Métrica central | Reproduzível? | Serve à Lia? |
|---|---|---|---|---|
| Paper de sistema | OpenJarvis (`LR-AGENT-001`) | energia, FLOPs, custo/USD | parcial (hardware do paper) | **como vocabulário**, não como número |
| Benchmark pack com hardware declarado | SculptForge (`LR-FORGE-002`) | fps/qualidade por GPU, enviado pela comunidade | sim, se hardware for declarado | **sim** — é o formato certo |
| Fixture com hash | ManimGX (`LR-FORGE-003`) | render idêntico ao fixture | alta | sim, para *correção*, não desempenho |
| Bancada interna | Lia-Project (`LR-MODEL-004`, doc 08) | tokens/s, VRAM, latência | sim, se executada | **sim** — é a ferramenta que falta rodar |

## 2. O que a Lia precisa

| Métrica | Por quê | Existe hoje? |
|---|---|---|
| tokens/s (prefill e decode) | viabilidade de UX | não |
| p95 do primeiro token | sensação de resposta | não |
| pico de RAM/VRAM com app + Stage | o número que decide "cabe" | não |
| consumo em idle | assistente sempre ativo | não |
| WER PT-BR | qualidade de voz | não |
| hash do peso | reprodutibilidade | sim (formato), não (execução) |

## 3. Conclusão

A Lia já tem o instrumento (`tools/desktop-benchmark`) e o plano (doc 08 do Model-Lab).
Falta **executar** e publicar com hardware declarado, no formato do SculptForge.

Regra derivada: qualquer número citado sem hardware, versão de runtime e hash do peso
é `REPORTED`, no melhor caso — e nunca entra em decisão de produto.
