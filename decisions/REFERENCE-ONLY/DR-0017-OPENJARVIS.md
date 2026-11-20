# DR-0017 — OpenJarvis mantido como referência

| Campo | Valor |
|---|---|
| ID | DR-0017 |
| Alcance | **GOVERNANCA** — decisão administrativa; não aprova adoção de tecnologia |
| Estado | **REFERENCE-ONLY** |
| Data | 2026-11-17 |
| Pesquisa | `LR-AGENT-001` |
| Reversível? | sim |

## Decisão
OpenJarvis não é dependência. Seus **padrões** (`InferenceEngine` ABC, `GuardrailsEngine`
como decorator, catálogo de modelo com metadados, 3 modos de redação) podem ser
reimplementados independentemente, com registro de origem.

## Fora de escopo
Não autoriza instalar, importar código, nem trocar o runtime de modelo da Lia.

## Motivo
Projeto alpha, orientado a GPU NVIDIA, com dependência de telemetria — incompatível com
o hardware (RX 580) e a política do usuário.
