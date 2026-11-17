# DR-0002 — Acesso de agentes ao Lia-Research

| Campo | Valor |
|---|---|
| ID | DR-0002 |
| Estado | **PENDING** |
| Dono | proprietário |
| Data | 2026-11-17 |
| Bloqueia | uso da base pelos agentes dos cinco projetos |

## Perguntas a decidir
1. Quem **pode ler** (agentes de quais projetos, com qual token/deploy key)?
2. Quem **pode publicar** (só o Orchestrator? agentes de projeto via PR?).
3. Quem **pode revisar** pesquisa de alto impacto?
4. Cópia local de leitura é permitida? Com qual política de sincronização?
5. Logs de acesso são necessários?

## Opções de acesso (propostas)
| Opção | Prós | Contras |
|---|---|---|
| A. Deploy key read-only por projeto | simples, auditável | uma chave por repositório |
| B. GitHub App com permissão de leitura | granularidade | configuração maior |
| C. Clone manual + cópia local | zero infraestrutura | desatualiza |
| D. Submodule | — | **proibido** pela ordem de serviço |

## Fora de escopo
Não autoriza tornar o repositório público nem conceder permissão ampla automática.
