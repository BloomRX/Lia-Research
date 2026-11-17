# DR-0011 — Modelo de registro de servidor MCP no Hub

| Campo | Valor |
|---|---|
| ID | DR-0011 |
| Estado | **PENDING** |
| Dono | Lia Agent Hub |
| Data | 2026-11-17 |
| Pesquisa | `LR-MCP-002` |

## Questão
Quais campos um servidor MCP precisa declarar para ser catalogável.

## Proposta mínima
`nome` · `transporte` (stdio/http) · `licença` · `commit/versão` · `tools expostas` ·
`classes de risco` · `credenciais exigidas` · `egress de rede` · `offline?` ·
`contrato versão`.

Sem isso, o Hub cataloga um servidor sem saber o que ele pode fazer — exatamente o
problema atual das Skills (licença desconhecida em 47/47).
