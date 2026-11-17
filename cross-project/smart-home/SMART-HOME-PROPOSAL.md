# Automação residencial — proposta consolidada

| Campo | Valor |
|---|---|
| ID | `LR-MCP-003` |
| Categoria | smart-home |
| Projetos | Lia-Project, Lia Agent Hub |
| Fontes | `LR-MCP-001` + `ARCHITECTURE-PROPOSAL.md` + `RISK-MATRIX.md` + `MCP-CONTRACT.md` em `repositories/ha-mcp/` |
| Data | 2026-11-17 |
| Status | PENDENTE (aguarda `DR-0003`) |
| Confiança | Alta para o desenho; nula para desempenho (nada executado) |

## 1. Casos de uso alvo

"Lia, liga a luz do quarto" · "apaga todas as luzes" · "liga o ventilador" ·
"qual é a temperatura da sala?" · "quais dispositivos estão ligados?" ·
"desliga tudo quando eu sair".

Todos são cobertos pelas 86 tools do HA-MCP (`CONFIRMED` na tabela do README).

## 2. Arquitetura (resumo)

```text
Lia-Project (experiência, consentimento)
   └─ Tool Broker (risco R0–R3, auditoria, allowlist)
        └─ Adapter home-assistant
             ├─ conexão A /readonly  (consultas)
             └─ conexão B elevada    (ações, sob demanda, com expiração)
                  └─ HA-MCP → Home Assistant → dispositivos
```

O Core da Lia **não depende** do Home Assistant. Sem HA configurado, nada muda.

## 3. Matriz de risco (resumo — completa em `repositories/ha-mcp/RISK-MATRIX.md`)

| Nível | Exemplo | Gate |
|---|---|---|
| R0 | temperatura, estado de lâmpada | nenhum |
| R1 | ligar/desligar luz, ventilador | confirmação configurável |
| R2 | fechadura, alarme, câmera, automação | autorização explícita por ação |
| R3 | desligar tudo, reiniciar, YAML, arquivos | dupla confirmação + backup + log |

**Achado central:** o risco está no par (domínio, serviço), não no nome da tool. Um gate
por nome de ferramenta é contornável por `ha_call_service(domain="lock")`.

## 4. Offline

| Cenário | Comportamento |
|---|---|
| LAN ok, internet cai | **funciona** (HA-MCP local + HA na LAN) |
| LAN cai | integração indisponível; conversa continua |
| HA reiniciando | fila + timeout + retry único |

## 5. O que falta para decidir

1. Protótipo isolado com 5 comandos R0/R1.
2. Prova de bloqueio de R2 no caminho de consulta.
3. UX de consentimento R2/R3.
4. Decisão `DR-0003` + aceite de `DR-0008` (matriz de risco).

Ver `repositories/ha-mcp/IMPLEMENTATION-PLAN.md` (não executado).
