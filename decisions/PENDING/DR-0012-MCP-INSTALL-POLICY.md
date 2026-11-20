# DR-0012 — Política de instalação de servidor MCP de terceiro

| Campo | Valor |
|---|---|
| ID | DR-0012 |
| Alcance | **GOVERNANCA** — decisão administrativa; não aprova adoção de tecnologia |
| Estado | **PENDING** |
| Dono | proprietário |
| Data | 2026-11-17 |
| Pesquisa | `LR-MCP-002` |

## Política proposta (a aprovar)
1. Instalação **nunca** automática; sempre ação explícita do usuário.
2. Tela de instalação mostra: licença, tools, risco máximo, egress, credenciais.
3. Servidor instalado começa **desabilitado** e em modo restrito (read-only quando disponível).
4. Atualização de servidor é ação do usuário, com diff de tools visível.
5. Servidor sem licença declarada não é instalável.
