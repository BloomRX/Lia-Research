# DR-0003 — Adotar adaptador residencial (HA-MCP)?

| Campo | Valor |
|---|---|
| ID | DR-0003 |
| Alcance | **GOVERNANCA** — decisão administrativa; não aprova adoção de tecnologia |
| Estado | **PENDING** |
| Dono | proprietário + responsável do Lia-Project |
| Data | 2026-11-17 |
| Pesquisas | `LR-MCP-001`, `LR-MCP-003` |
| Bloqueia | `repositories/ha-mcp/IMPLEMENTATION-PLAN.md` |

## O que está em jogo
Habilitar controle da casa por voz/conversa, com risco R2 (fechadura, alarme, câmera) e
R3 (desligar tudo, reiniciar).

## Pré-requisitos sugeridos antes de decidir
1. protótipo isolado com 5 comandos R0/R1 (Fatia 0);
2. prova de bloqueio de `lock.unlock` na conexão read-only (Fatia 1–2);
3. UX de consentimento R2/R3 definida (Fatia 3);
4. matriz de risco aceita (`DR-0008`);
5. revisão de segurança independente.

## Opções
| Opção | Efeito |
|---|---|
| A. Adotar, desabilitado por padrão | usuário ativa conscientemente |
| B. Adotar só leitura (R0) na v1 | menor risco, casos de uso limitados |
| C. Não adotar | mantém escopo focado no desktop |
| D. Esperar MCP nativo do HA amadurecer | menos superfície, menos recursos |

## Recomendação de pesquisa
**B** como primeira entrega (leitura + R1), com caminho elevado depois, se os gates
passarem. Não é decisão: é a hipótese a testar.
