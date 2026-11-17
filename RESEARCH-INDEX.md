# RESEARCH-INDEX

Índice canônico de tudo que esta base pesquisa. Uma linha por item, com ID estável,
veredito e caminho. **Este arquivo é a fonte de verdade dos IDs**: se um ID aparece em
outro documento e não aqui, o outro documento está errado.

- **Data de referência:** 2026-11-17
- **Itens:** 16 relatórios externos + 5 dossiês internos + 26 digests/propostas transversais + 12 decisões abertas + 1 aceita
- **Nenhum item foi executado.** Todos os vereditos são sobre o *valor de pesquisa*.

## Legenda

`Veredito` — ADOTAR · ADAPTAR · REFERÊNCIA · REJEITAR · PENDENTE
`Confiança` — quão sólida é a evidência coletada (não a recomendação)
`Evidência` — CONFIRMED · OBSERVED · REPORTED · INFERRED · UNVERIFIED · BLOCKED

---

## 1. Tecnologia externa — auditoria (16)

| ID | Objeto | Licença | Veredito | Confiança | Documento |
|---|---|---|---|---|---|
| `LR-MCP-001` | `homeassistant-ai/ha-mcp` | MIT | **ADAPTAR** | Alta | `repositories/ha-mcp/REPORT.md` |
| `LR-MCP-001-A` | proposta de arquitetura residencial | — | ADAPTAR | Alta | `repositories/ha-mcp/ARCHITECTURE-PROPOSAL.md` |
| `LR-MCP-001-B` | matriz de risco R0–R3 | — | PENDENTE (DR-0008) | Alta | `repositories/ha-mcp/RISK-MATRIX.md` |
| `LR-MCP-001-C` | contrato de servidor MCP de casa | — | ADAPTAR | Alta | `repositories/ha-mcp/MCP-CONTRACT.md` |
| `LR-MCP-001-D` | plano de implementação em 8 fatias | — | PENDENTE (DR-0003) | Média | `repositories/ha-mcp/IMPLEMENTATION-PLAN.md` |
| `LR-AGENT-001` | `open-jarvis/OpenJarvis` | Apache-2.0 | **REFERÊNCIA** | Alta | `repositories/openjarvis/REPORT.md` |
| `LR-UI-001` | `vercel-labs/ui` | Apache-2.0 + beta | **ADAPTAR** | Alta | `repositories/vercel-ui/REPORT.md` |
| `LR-FORGE-001` | `anefzaoui/misterdownloadmanager` | **GPL-3.0** | **REFERÊNCIA** | Alta | `repositories/misterdownloadmanager/REPORT.md` |
| `LR-AGENT-002` | `tradermonty/claude-trading-skills` | MIT | **ADAPTAR** | Alta | `repositories/claude-trading-skills/REPORT.md` |
| `LR-STUDIO-001` | `l0ng-ai/openidea` | Apache-2.0 | **REFERÊNCIA** | Alta | `repositories/openidea/REPORT.md` |
| `LR-PROV-001` | `routerhubSI` (organização) | MIT / NOASSERTION | **REJEITAR** | Média | `repositories/routerhub/REPORT.md` |
| `LR-FORGE-002` | `islandmed/SculptForge` | **GPL-3.0** | **REFERÊNCIA** | Alta | `repositories/sculptforge/REPORT.md` |
| `LR-STUDIO-002` | `Donchitos/Claude-Code-Game-Studios` | MIT | **ADAPTAR** | Alta | `repositories/claude-code-game-studios/REPORT.md` |
| `LR-FORGE-003` | `academa-labs/manimgx` | mixed (6) | **REFERÊNCIA** | Alta | `repositories/manimgx/REPORT.md` |
| `LR-AGENT-003` | `Ryder-Sun/Meldwork` | Apache-2.0 | **REFERÊNCIA** | Alta | `repositories/meldwork/REPORT.md` |
| `LR-UI-002` | `backnotprop/plannotator` | Apache-2.0 | **REFERÊNCIA** | Alta | `repositories/plannotator/REPORT.md` |
| `LR-FORGE-004` | `patch-gg/pixelfx` | MIT + NOTICE | **ADAPTAR** | Alta | `repositories/pixelfx/REPORT.md` |
| `LR-AGENT-004` | `theclaymethod/unslop` | **nenhuma** | **REJEITAR** | Alta | `repositories/unslop/REPORT.md` |
| `LR-STUDIO-003` | `rescript-lang` (org, 39 repos) | LGPL no `compiler/` | **REJEITAR** | Alta | `repositories/rescript-lang/REPORT.md` |
| `LR-UI-003` | `elayadesign/ai-design-skills` | MIT | **ADAPTAR** | Média | `repositories/ai-design-skills/REPORT.md` |

## 2. Projetos do ecossistema — dossiês internos (5)

| ID | Projeto | Documentos | Skills | Documento |
|---|---|---:|---:|---|
| `LR-PROJ-001` | Lia-Project | 261 | 22 | `projects/lia-project/INDEX.md` |
| `LR-PROJ-002` | Lia-Forge | 128 | 1 + 49 capabilities | `projects/lia-forge/INDEX.md` |
| `LR-PROJ-003` | Lia-Studio | 109 | 16 | `projects/lia-studio/INDEX.md` |
| `LR-PROJ-004` | Lia-AgentHub | 57 | biblioteca (48 no ecossistema) | `projects/lia-agent-hub/INDEX.md` |
| `LR-PROJ-005` | Lia-Model-Lab | 90 | 9 (únicos em `main`) | `projects/lia-model-lab/INDEX.md` |

## 3. Digests transversais (17)

| ID | Tema | Documento |
|---|---|---|
| `LR-HW-001` | Windows 11 + RX 580 (gfx803) | `cross-project/hardware/WINDOWS-AMD-COMPATIBILITY.md` |
| `LR-HW-002` | consumo em desktop sempre ativo | `cross-project/hardware/RUNTIME-RESOURCE-RESEARCH.md` |
| `LR-MODEL-001` | catálogo de modelos e providers | `cross-project/model-routing/MODEL-CATALOG-DIGEST.md` |
| `LR-MODEL-002` | arquitetura neutra de provider | `cross-project/model-routing/PROVIDER-ARCHITECTURE-DIGEST.md` |
| `LR-MODEL-003` | LFM3 (duas avaliações) | `cross-project/ai-models/LFM3-EVALUATION.md` |
| `LR-MODEL-004` | catálogo de capacidades (44/131/0) | `cross-project/ai-models/CAPABILITY-CATALOG-DIGEST.md` |
| `LR-MODEL-005` | **matriz capability × provider** (54 providers lidos) | `cross-project/model-routing/CAPABILITY-PROVIDER-MATRIX.md` |
| `LR-VOICE-001` | stack de voz PT-BR | `cross-project/voice/VOICE-STACK-DIGEST.md` |
| `LR-SEC-001` | credenciais e fronteira de confiança | `cross-project/security/CREDENTIAL-AUDIT-DIGEST.md` |
| `LR-SEC-002` | segurança de runtime de agente | `cross-project/agents/AGENT-RUNTIME-SECURITY.md` |
| `LR-SEC-004` | armazenamento e portabilidade | `cross-project/storage/DATA-PORTABILITY.md` |
| `LR-UI-004` | comportamentos de interface | `cross-project/interfaces/UI-BEHAVIORS.md` |
| `LR-AGENT-005` | orquestração de agentes de asset | `cross-project/agents/ASSET-AGENT-ORCHESTRATION-DIGEST.md` |
| `LR-AGENT-006` | Skills e MCP vistos pelo Studio | `cross-project/agents/SKILLS-MCP-LANDSCAPE.md` |
| `LR-AGENT-007` | memória | `cross-project/memory/MEMORY-LANDSCAPE.md` |
| `LR-AGENT-008` | fronteiras de automação | `cross-project/automation/AUTOMATION-BOUNDARIES.md` |
| `LR-AGENT-009` | **manifesto de workflow para Skills** (proposta) | `cross-project/agents/SKILL-WORKFLOW-MANIFEST.md` |
| `LR-SEC-005` | **permissões por execução** (proposta) | `cross-project/security/PER-EXECUTION-PERMISSIONS.md` |
| `LR-UI-005` | **ADR de interface** (procedimento) | `cross-project/interfaces/UI-DECISION-ADR.md` |
| `LR-LIC-004` | **registro de proveniência de asset** (proposta) | `cross-project/licensing/ASSET-PROVENANCE-REGISTRY.md` |
| `LR-MCP-002` | panorama MCP no ecossistema | `cross-project/mcp/MCP-LANDSCAPE.md` |
| `LR-MCP-003` | automação residencial consolidada | `cross-project/smart-home/SMART-HOME-PROPOSAL.md` |
| `LR-FORGE-005` | Blender e MCP | `cross-project/agents/BLENDER-MCP-DIGEST.md` |
| `LR-FORGE-006` | aquisição de arquivos grandes | `cross-project/downloads/LARGE-FILE-ACQUISITION.md` |
| `LR-LIC-001` | licença e proveniência de Skills | `projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md` |
| `LR-LIC-002` | proveniência de assets | `cross-project/licensing/ASSET-PROVENANCE.md` |
| `LR-BENCH-001` | disciplina de benchmark reproduzível | `repositories/sculptforge/REPORT.md`, `repositories/manimgx/REPORT.md` |
| `LR-SEC-003` | auditoria de segurança de STT | `cross-project/voice/VOICE-STACK-DIGEST.md` §2 |
| `LR-LIC-003` | **auditoria das 28 skills AIRI + `alethe`** (parecer por Skill) | `projects/lia-agent-hub/skills/AIRI-AND-ALETHE-PROVENANCE.md` |

## 3-bis. Comparações

| ID | Pergunta | Documento |
|---|---|---|
| `LR-CMP-001` | como expressar licença em projeto com terceiros e assets | `comparisons/LICENSE-MODEL-COMPARISON.md` |
| `LR-CMP-002` | qual servidor MCP de casa usar, se algum | `comparisons/MCP-SERVER-COMPARISON.md` |
| `LR-CMP-003` | como medir modelo/hardware sem virar fé | `comparisons/BENCHMARK-APPROACH-COMPARISON.md` |

## 4. Decisões (13 abertas + 5 tomadas)

| Estado | IDs | Pasta |
|---|---|---|
| ACCEPTED (1) | DR-0006 (repositório público) | `decisions/ACCEPTED/` |
| PENDING (12) | DR-0001…DR-0004, DR-0007…DR-0014 | `decisions/PENDING/` |
| REJECTED (3) | DR-0005, DR-0015, DR-0016 | `decisions/REJECTED/` |
| REFERENCE-ONLY (2) | DR-0017, DR-0018 | `decisions/REFERENCE-ONLY/` |
| ADAPTED (0) | — | `decisions/ADAPTED/` |

## 4-bis. Decisões propostas nas pesquisas de 2026-11-17 (2ª rodada)

Ainda **não** abriram arquivo em `decisions/`: são propostas de pesquisa que só viram DR
quando um projeto decide levá-las adiante. Citadas com o número `(proposto)` nos
documentos, para não perder a referência.

| ID proposto | Decisão | Descrita em | Dono |
|---|---|---|---|
| `DR-0019` | matriz capability × provider como gate de CI | `LR-MODEL-005` §11 | Lia-Project |
| `DR-0020` | adotar manifesto de workflow de Skill | `LR-AGENT-009` §11 | Hub |
| `DR-0021` | adotar `schemaVersion: 3` de proveniência de asset | `LR-LIC-004` §10 | Forge |
| `DR-0022` | aceitar vocabulário Grant/Lease/AuditRecord | `LR-SEC-005` §14 | Hub + Project |
| `DR-0023` | escrever os 3 ADRs de UI piloto | `LR-UI-005` §13 | cada projeto |

## 5. Fontes externas pinadas

14 repositórios com SHA: `data/external/pinned-targets.tsv`.
Organizações (sem SHA de conteúdo): `routerhubSI` (11 repos), `rescript-lang` (39 repos).

## 6. Lacunas declaradas

| Lacuna | Rótulo | Onde está registrada |
|---|---|---|
| Nenhum modelo validado (44 catalogados, 0 medidos) | CONFIRMED | `LR-MODEL-004` |
| Benchmarks de GPU na RX 580 | BLOCKED | `LR-HW-001` §6 |
| WER/latência de voz PT-BR | BLOCKED | `LR-VOICE-001` §4 |
| Termos/retention do RouterHub | BLOCKED | `LR-PROV-001` |
| Visão/multimodal como tema próprio | NOT RUN | `RESEARCH-ROADMAP.md` R-4 |
| Repositório público (deveria ser privado) | BLOCKED (403) | `DR-0006` |
