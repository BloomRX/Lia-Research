# Automação — fronteiras

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-008` |
| Categoria | automation |
| Projetos | Lia Agent Hub, Lia-Project, Lia Forge |
| Fontes | `repositories/ha-mcp/RISK-MATRIX.md`, `Lia-AgentHub:docs/architecture/CAPABILITY-HOST-AND-DISTRIBUTION-CONTRACT.md`, `Lia-Project:*.agents/skills/lia-browser-automation` (skill) |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média |

## 1. Três tipos de automação no ecossistema

| Tipo | Exemplo | Risco dominante |
|---|---|---|
| Automação de dispositivo (casa) | desligar luzes | ação física (R1–R3) |
| Automação de navegador | skill `lia-browser-automation` | egress de dados, sessão autenticada |
| Automação de máquina | launcher, processos, builds | alteração de ambiente |

Cada tipo precisa de política própria; tratar tudo como "tool" mistura riscos
incomparáveis.

## 2. Regras propostas

1. **Confirmação fora do LLM** para qualquer ação R2+ (ver `RISK_MATRIX`).
2. **Allowlist de domínio** para automação de navegador; nunca sessão de banco.
3. **Quota de recurso** (disco, rede, CPU) para qualquer automação que consuma.
4. **Log de intenção**: o que o usuário pediu, não só o que foi executado.
5. **Automação de terceiro nunca instala nada sozinha** (regra do MCP).

## 3. Lacuna

Não existe política unificada de automação no ecossistema. As regras acima são
proposta; a aprovação é decisão do proprietário (`DR-0008` cobre a parte residencial).
