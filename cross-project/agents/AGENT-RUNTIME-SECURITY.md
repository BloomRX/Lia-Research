# Segurança de runtime de agente — digest

| Campo | Valor |
|---|---|
| ID | `LR-SEC-002` |
| Categoria | security |
| Projetos | Lia Studio, Lia Agent Hub, Lia-Project |
| Fontes | `Lia-Studio@…:docs/research/ARENA-RUNTIME-SECURITY-AUDIT.md` (41 KB, 3× `PENDENTE`), `AGENT-ARCHITECTURE-RESEARCH.md` (42 KB, 21× `ADAPTAR`, 1× `ADOTAR`), `Lia-AgentHub:docs/architecture/SECURITY-AND-TRUST-MODEL.md` (40 KB) |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média-Alta |

## 1. Escopo do documento original

Auditoria de runtime de agente e segurança no Studio: como o agente executa, com que
permissão, e onde a sandbox pode falhar. Três itens ficaram `PENDENTE` no original —
não resolvidos aqui, por serem do projeto.

## 2. Padrões de segurança para agente (consolidados)

| Padrão | Fonte | Aplicação |
|---|---|---|
| Segurança como camada (decorator), não espalhada | OpenJarvis `GuardrailsEngine` | contrato de engine |
| Sandbox com montagem restrita | OpenJarvis `SandboxedAgent` | execução de código |
| Permissão com escopo por rodada | Meldwork | orquestração multi-agente |
| Read-only por conexão | HA-MCP | tools de risco |
| Aprovação humana de tool | HA-MCP | tools destrutivas |
| Scan de segredo/PII com 3 modos (WARN/REDACT/BLOCK) | OpenJarvis | entrada/saída de modelo |
| Auditoria em log próprio | OpenJarvis (`AuditLogger`), Meldwork | rastreabilidade |

## 3. Regra derivada

> Agente não pode ter, por padrão, mais poder do que a tarefa exige — e o mecanismo
> para garantir isso tem de estar **fora** do modelo, não no prompt.

Um prompt dizendo "peça permissão antes de apagar" não é controle; é sugestão.

## 4. Lacunas

| Lacuna | Status |
|---|---|
| Modelo de permissão de plugin/skill executável no ecossistema | inexistente |
| Teste de injeção de prompt via conteúdo de ferramenta | inexistente |
| Auditoria de execução de agente com intenção declarada | inexistente |
