# DR-0013 — Parecer sobre GPL do Mister Download Manager

| Campo | Valor |
|---|---|
| ID | DR-0013 |
| Alcance | **GOVERNANCA** — decisão administrativa; não aprova adoção de tecnologia |
| Estado | **PENDING** |
| Dono | proprietário / jurídico |
| Data | 2026-11-17 |
| Pesquisa | `LR-FORGE-001` |

## Questão
A fronteira "processo separado via MCP/stdio" é suficiente para que o MDM (GPL-3.0) não
contamine os apps Lia proprietários?

## Por que o agente não decide
É questão jurídica com critérios técnicos (processo separado, comunicação por IPC,
distribuição conjunta ou não). A resposta muda conforme o MDM seja baixado pelo usuário
ou empacotado pela Lia.

## Cenários
| Cenário | Risco |
|---|---|
| Usuário instala o MDM por conta própria; Lia só fala MCP | menor |
| Lia empacota o binário no instalador | **alto** — distribuição de GPL no pacote |
| Lia inclui código em crate próprio | inaceitável |

## Alternativa sem risco
Implementar D1–D6 de `cross-project/downloads/` sem terceiros.
