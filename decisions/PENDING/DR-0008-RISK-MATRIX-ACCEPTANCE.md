# DR-0008 — Aceitar a matriz de risco R0–R3

| Campo | Valor |
|---|---|
| ID | DR-0008 |
| Estado | **PENDING** |
| Dono | proprietário |
| Data | 2026-11-17 |
| Pesquisa | `LR-MCP-001-B` (`repositories/ha-mcp/RISK-MATRIX.md`) |
| Bloqueia | `DR-0003` |

## Decisão pedida
Aceitar como política oficial a classificação R0–R3, em que o risco é determinado pelo
par (domínio, serviço) e não pelo nome da ferramenta.

## Regras que a aceitação implica
1. confirmação nunca decidida pelo LLM;
2. R2 não persistível ("lembrar para sempre" proibido);
3. domínio não classificado = R2 por default;
4. `script`/`scene` herdam o maior risco interno;
5. toda execução R1–R3 registra intenção.
