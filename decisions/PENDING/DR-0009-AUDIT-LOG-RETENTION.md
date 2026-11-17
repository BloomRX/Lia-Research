# DR-0009 — Retenção de log de auditoria de automação

| Campo | Valor |
|---|---|
| ID | DR-0009 |
| Estado | **PENDING** |
| Dono | proprietário |
| Data | 2026-11-17 |
| Pesquisa | `LR-MCP-001-B` |

## Questão
Por quanto tempo guardar o log de ações residenciais (intenção, parâmetro, resultado,
identidade), e onde.

## Trade-off
| Retenção | Prós | Contras |
|---|---|---|
| 7 dias | privacidade | não cobre "o que aconteceu semana passada" |
| 30 dias (proposta) | cobre investigação típica | acumula rotina da casa |
| 1 ano | auditoria forte | vira perfil de rotina — risco de privacidade |

## Recomendação de pesquisa
30 dias, local, com exportação manual e exclusão a pedido. Log **não** sai da máquina.
