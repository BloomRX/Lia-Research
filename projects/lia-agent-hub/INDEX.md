# Índice — Lia Agent Hub

---


> **Reauditoria de 2026-11-20.** Todo relatório externo listado aqui foi reavaliado
> nesta data (versão anterior, versão atual, mudanças, testes e conclusão). O detalhe
> está na seção `Reauditoria 2026-11-20` de cada `repositories/*/REPORT.md`;
> resumo por objeto em `audits/REAUDIT-2026-11-20.md`.

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem |
|---|---|---|---|
| `LR-LIC-001` | Licença e proveniência de Skills (consolidação) | `projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md` | `SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` |
| `LR-AGENT-002` | Manifestos de workflow e skillsets | `repositories/claude-trading-skills/REPORT.md` | externo (novo) |
| `LR-AGENT-003` | Permissões com escopo, evidência por execução | `repositories/meldwork/REPORT.md` | externo (novo) |
| `LR-AGENT-004` | (rejeitado por licença) | `repositories/unslop/REPORT.md` | externo (novo) |
| `LR-AGENT-001` | Contrato de engine e guardrails | `repositories/openjarvis/REPORT.md` | externo (novo) |
| `LR-MCP-001` | Servidor MCP residencial | `repositories/ha-mcp/REPORT.md` | externo (novo) |
| `LR-FORGE-001` | Gerenciador de downloads com MCP | `repositories/misterdownloadmanager/REPORT.md` | externo (novo) |
| `LR-UI-002` | Contrato de revisão humana | `repositories/plannotator/REPORT.md` | externo (novo) |
| `LR-AGENT-006` | Catálogo de Skills/MCP (pesquisa do Studio) | `cross-project/agents/SKILLS-MCP-LANDSCAPE.md` | `ARENA-SKILLS-MCP-AGENT-TOOLS-RESEARCH.md` |
| `LR-LIC-005` | Licenças prontas: TASL (CC BY), Apache com NOTICE, `license:` no payload da Skill | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 18 relatórios |
| `LR-STUDIO-004` | Superfície de agente por app: roots, token, consentimento, MCP stdio (precedente real) | `repositories/artcraft/REPORT.md` | pesquisa externa (novo) |
| `LR-AGENT-010` | Pacote de 8 Skills de edição (ArtCraft) — opção adicional, habilitada pelo usuário | `cross-project/agents/ARTCRAFT-SKILL-PACK.md` | derivado de `LR-STUDIO-004` |
| `LR-AGENT-011` | Memória compartilhada e handoff com dono/reivindicação única | `repositories/ai-memory/REPORT.md` | pesquisa externa (novo) |
| `LR-MODEL-006` | Orçamento por chave + failover para adapters de provider | `repositories/freellmapi/REPORT.md` | pesquisa externa (novo) |

## 2. Documentos do Hub que permanecem na origem (fonte canônica)

| Documento | Bytes | Por que não foi copiado |
|---|---:|---|
| `docs/review/ARCHITECTURE-SECURITY-CROSS-REVIEW.md` | 96 KB | revisão do projeto; pertence a ele |
| `docs/architecture/SECURITY-AND-TRUST-MODEL.md` | 40–42 KB | modelo de segurança do Hub (2 versões) |
| `docs/architecture/PRODUCT-BOUNDARIES-AND-ARCHITECTURE.md` | 36–37 KB | fronteiras (2 versões) |
| `docs/architecture/DATA-STORAGE-AND-PORTABILITY.md` | 25 KB | storage e portabilidade |
| `docs/architecture/CAPABILITY-HOST-AND-DISTRIBUTION-CONTRACT.md` | 25 KB | contrato de distribuição |
| `docs/product/PLATFORM-AND-TECHNOLOGY-DECISION.md` | 26 KB | decisão de stack (1 `ACCEPTED`, 1 `REJECTED`, 1 `DEFERRED`) |
| `docs/DECISION-REGISTER.md` | 4–36 KB | registro de decisões (2 versões divergentes!) |
| `docs/operations/WINDOWS-VALIDATION-AND-BUILD-PLAN.md` | 56 KB | plano |
| `docs/research/LIA-SKILLS-INVENTORY.md` | 37 KB | **fonte canônica das 48 skills** |
| `docs/research/SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` | 36 KB | **fonte canônica de licença** |
| `docs/research/THIRD-PARTY-SKILLS-CATALOG.md` | 34 KB | catálogo de terceiros |
| `docs/research/INTEGRATION-CANDIDATES.md` | 37 KB | candidatos |

## 3. Skills e licença — resumo

Ver `skills/SKILL-LICENSE-CONSOLIDATION.md`. Em uma linha: **47 Skills autorais, 0 com
licença no payload, 5 grupos de terceiros já consumidos com cumprimento parcial**.

## 4. Referências externas já catalogadas pelo Hub

O `INTEGRATION-CANDIDATES.md` e o `THIRD-PARTY-SKILLS-CATALOG.md` já cobrem fontes de
Skills. Antes de pesquisar um repositório de Skills novo, consultar estes dois
documentos (regra de dedup de `governance/RESEARCH-GOVERNANCE.md` §6).

## 5. Gaps E-1…E-9 (estado herdado)

| Gap | Área | Estado em 2026-11-17 |
|---|---|---|
| E-1 | detecção de licença apenas por arquivo na raiz | **aberto** — afeta 47 skills |
| E-2 | perfil de agente Codex não é tipo do modelo | aberto |
| E-3 | skillsets/perfis não modelados | aberto |
| E-4 | manifesto de workflow inexistente | aberto — proposta em `LR-AGENT-002` |
| E-5 | duplicação de Skill não resolvida | aberto — `DR-0007` |
| E-6 | Skills fora de `main` não detectadas pelo catálogo | aberto |
| E-7 | sem validação de segurança de Skill importada | aberto |
| E-8 | proveniência de asset dentro de Skill não modelada | aberto |
| E-9 | ausência de versionamento semântico de Skill | aberto |

Os nove gaps permanecem. Nenhum foi fechado por esta fundação — e não deveriam ser:
fechá-los é implementação no Hub, fora do escopo da ordem de serviço.

---

## 6. Conferência de ponteiros — 2026-11-26

Medição desta sessão (`gh api` na `main`; `audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md` §2.2).
O texto acima é o registro de 2026-11-17.

| Afirmação anterior | Estado hoje |
|---|---|
| "Branches `arena/*` permanecem como registro histórico" | **superada**: `main` @ `8c14ec85` com **202 commits**, **1** branch remota. `docs/BRANCH-AND-RELEASE-FLOW.md` agora exige integração na `main` e **substitui** a regra inicial de "`main` apenas documental"; as quatro `arena/*` foram removidas após `BRANCH-CLEANUP`/snapshot (`docs/operations/BRANCH-CONSOLIDATION-2026-11-26.md`, ZIP 13.462.694 B + bundle, `fsck` e restauração verificados) |
| §2 "13 documentos que permanecem na origem" (`LIA-SKILLS-INVENTORY.md`, `SKILL-LICENSE-AND-PROVENANCE-AUDIT.md`, `THIRD-PARTY-SKILLS-CATALOG.md`, `LIA-SKILLS-ROADMAP.md`, `catalog/*.records.json` (5), `Lia-AgentHub:catalog/sources.json` e `Lia-AgentHub:tools/build-catalog-records.py` (caminhos do Hub, não desta base)) | **INTEGRAÇÃO PENDENTE, com ponteiro a corrigir**: nenhum deles está na `main`; o próprio registro de limpeza os lista como "13 arquivos de pesquisa ausentes da base", preservados no bundle e alcançáveis por SHA (`b4e63eae`). Quem precisar do payload usa o link por commit, não a branch |
| "`DECISION-REGISTER.md` … versão dupla divergente" | **ENTREGA CONCLUÍDA**: `docs/DECISION-REGISTER.md` (38.258 B) existe uma única vez na `main` |
| "o payload de skills não está no Hub" | confirmado por contagem: **0** `SKILL.md`, **0** `LICENSE` na `main` |
| (novo) contratos publicados | a `main` traz `docs/architecture/CAPABILITY-INVENTORY-CONTRACT.md` (`inventoryVersion: 1`; `revision` = "mesmo valor e digest diferente é conflito"; `complete` = "omissões nunca apagam registros"), `SUPERVISED-EXECUTION-V1.md` + `docs/schemas/supervised-execution-v1.schema.json`, `docs/examples/**` (incl. `intake/demo-conflict-same-revision.json`), `INVENTORY-INTAKE.md`, `CENTRAL-CAPABILITY-GOVERNANCE.md`. **Leitura pendente da base**: nada aqui foi comparado com `LR-MCP-004`/`LR-AGENT-019` ainda |
| `docs/DECISION-REGISTER.md` e o registro de integração | a seção *Referências* do registro cita `docs/research/INTEGRATION-CANDIDATES.md` nomeando **MCPVault e ai-memory** como evidência externa do Hub — e registra "Nenhuma decisão foi promovida nesta rodada". É o gancho do `LR-CMP-006` §5.1, não uma recomendação desta base |
| piloto do Project no Hub | **VALIDAÇÃO EXECUTADA POR ELES, NÃO POR NÓS**: 28 Skills materializadas, verificador recusando Skill sem `SKILL.md`, 28 pins / 7 testes / 88 subtestes verdes em checkout Windows `J:/Lia/migration/agent-hub/project-pilot-3153c8b` @ `807c0b1`; corte remoto pendente; 23 de 51 Skills fora do corte por origem/licença/escopo (`docs/operations/LIA-PROJECT-PILOT-HANDOFF.md`) |
