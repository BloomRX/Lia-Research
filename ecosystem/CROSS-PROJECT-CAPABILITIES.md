# Capacidades transversais

Capacidades que aparecem em mais de um projeto. O objetivo é evitar que cada projeto
resolva o mesmo problema de forma incompatível — sem criar obrigação de adoção.

---

## 1. Inventário de capacidades compartilhadas

| Capacidade | Onde já existe | Onde falta | Fonte única de pesquisa |
|---|---|---|---|
| Catálogo de provedores de modelo | Lia-Project (`docs/research/LIA-MODEL-PROVIDER-CATALOG.md`), Model-Lab (`docs/05-FOUNDATION-MODEL-COMPARISON.md`) | Forge, Studio | `cross-project/model-routing/` |
| Roteamento por capability | Lia-Project (research de arquitetura de provider neutro) | todos | `cross-project/model-routing/` |
| Skills (Agent Skills) | Studio 16, Project 22, Model-Lab 9, Forge 1 | Hub só cataloga, não tem payload | `projects/lia-agent-hub/skills/` |
| Servidor/consumo MCP | Forge (`spriteforge-mcp.mjs`, 10 tools), Project (broker de tools) | Hub (descoberta), Studio | `cross-project/mcp/` |
| Voz (STT/TTS/VAD) | Lia-Project (voz supervisionada, Kokoro) | Forge, Studio | `cross-project/voice/` |
| Memória | Lia-Project (memória local + autorização de tools) | todos | `cross-project/memory/` |
| Build/validação Windows | Project, Forge, Model-Lab (ADRs 0004/0005) | Studio | `cross-project/hardware/` |
| Auditoria de licença de terceiros | Agent Hub (`SKILL-LICENSE-AND-PROVENANCE-AUDIT`) | Forge, Studio, Project | `cross-project/licensing/` |
| Design system / UI | Studio (`UI-UX-DESIGN-SYSTEM`), Project (UI/UX audit), Hub (Stitch briefs) | Forge parcial | `cross-project/interfaces/` |
| Aquisição de arquivos grandes | ninguém (download manual) | todos | `cross-project/downloads/` |
| Automação residencial | ninguém | Project + Hub | `cross-project/smart-home/` |

## 2. Capacidades já implementadas em código (não são Skills)

Medido no inventário do Agent Hub (`2026-11-15`, `arena/db625478`):

| Item | Quantidade | Onde | Natureza |
|---|---:|---|---|
| Capacidades de produção registradas | 49 | Forge `shared/capabilities/registry.mjs` | 16 implemented · 5 partial · 5 proposed · 24 planned |
| Ferramentas MCP implementadas | 10 | Forge `scripts/spriteforge-mcp.mjs` (servidor `lia-forge`) | `CONFIRMED` por código |
| Registros de catálogo de modelos | 44 catalogados · ~131 descobertos · **0 validados** | Project `docs/research/lia-capability-catalog/` | `CONFIRMED` por documento |

"0 validados" é o dado mais importante desta tabela: existe um catálogo de 44
registros e nenhum modelo foi medido no hardware de referência.

## 3. Duplicações que custam manutenção

| Duplicata | Tipo | Consequência |
|---|---|---|
| `lia-brand-check` (Forge) ≈ `lia-brand-consistency-review` (Model-Lab) | mesma função | duas regras de marca divergindo |
| `lia-agent-orchestration` (Project) ≈ `multi-agent-orchestration` (Model-Lab) ≈ `alethe` (terceiro) | mesma função | três contratos concorrentes |
| Catálogo de modelos em Project **e** Model-Lab | dados | dois números de "melhor modelo" |
| Documentação de arquitetura em Forge (`PRODUCT-ARCHITECTURE`) e Studio (`LIA-STUDIO-ARCHITECTURE-DECISIONS`) sobre a fronteira Forge↔Studio | arquitetura | risco de decisões contraditórias |

Registro de conflito: `decisions/PENDING/DR-0007-CONSOLIDACAO-SKILLS-DUPLICADAS.md`.

## 4. Regra de compartilhamento

```text
Pesquisa compartilhada  →  sim (este repositório)
Componente compartilhado →  só por decisão explícita dos donos
Dependência compartilhada → não
```

Um relatório pode dizer "os dois projetos precisam disto". Não pode dizer "os dois
projetos vão usar o mesmo módulo".
