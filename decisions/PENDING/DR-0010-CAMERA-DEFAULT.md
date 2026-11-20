# DR-0010 — Câmera habilitada por padrão?

| Campo | Valor |
|---|---|
| ID | DR-0010 |
| Alcance | **GOVERNANCA** — decisão administrativa; não aprova adoção de tecnologia |
| Estado | **PENDING** |
| Dono | proprietário |
| Data | 2026-11-17 |
| Pesquisa | `LR-MCP-001` (R4) |

## Questão
`ha_get_camera_image` captura imagem da casa, incluindo terceiros (família, visitas).

## Recomendação de pesquisa
**Desabilitada por padrão**, com opt-in permanente por câmera e aviso de que a imagem é
enviada ao modelo quando usado. R2 na matriz.

## Justificativa
É a única capacidade do catálogo cujo dano principal é a terceiros que não consentiram.
