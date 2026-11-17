# DR-0014 — Critério de "modelo validado"

| Campo | Valor |
|---|---|
| ID | DR-0014 |
| Estado | **PENDING** |
| Dono | Lia Model Lab |
| Data | 2026-11-17 |
| Pesquisa | `LR-MODEL-004` |

## Situação
44 modelos catalogados, ~131 descobertos, **0 validados**. Sem critério, "validado"
significa "alguém gostou".

## Critério proposto
Um modelo é `VALIDATED` quando, no hardware de referência, existe medição registrada de:

| Métrica | Obrigatória |
|---|---|
| pico de RAM/VRAM com o app ativo | sim |
| tokens/s (prefill e decode) | sim |
| latência p95 do primeiro token | sim |
| qualidade em 5 prompts fixos PT-BR | sim |
| licença lida por modelo | sim |
| hash do arquivo de peso | sim |

Sem os seis, o registro permanece `CATALOGED`.
