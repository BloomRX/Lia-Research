# Índice — Lia Agent Hub

---

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
| `LR-STUDIO-004` | Superfície de agente por app: roots, token, consentimento, MCP stdio (precedente real) | `repositories/artcraft/REPORT.md` | pesquisa externa (novo) |
| `LR-AGENT-010` | Pacote de 8 Skills de edição (ArtCraft) — opção adicional, habilitada pelo usuário | `cross-project/agents/ARTCRAFT-SKILL-PACK.md` | derivado de `LR-STUDIO-004` |

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
