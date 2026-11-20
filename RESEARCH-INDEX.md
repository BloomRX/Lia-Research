# RESEARCH-INDEX

Índice canônico de tudo que esta base pesquisa. Uma linha por item, com ID estável,
veredito e caminho. **Este arquivo é a fonte de verdade dos IDs**: se um ID aparece em
outro documento e não aqui, o outro documento está errado.

- **Data de referência:** 2026-11-20
- **Itens:** 22 objetos externos (26 linhas com sub-documentos) + 5 dossiês internos + 31 digests transversais + 3 comparações + 18 registros de governança
- **Nenhum item foi executado.** Não existe linha em `data/testing/test-log.tsv`: todo
  `Resultado de execução` desta base é `STATIC_REVIEW_ONLY` ou `NOT_RUN`.

## Legenda

`Estado` — DISCOVERED · TRIAGED · INVESTIGATING · DOCUMENTED · TESTED · PARTIALLY_TESTED ·
NOT_TESTED · BLOCKED · STALE · SUPERSEDED · CONFLICTING
`Recomendação` — DIRECT_INTEGRATION_CANDIDATE · ADAPT · FORK_CANDIDATE ·
INDEPENDENT_REIMPLEMENTATION · REFERENCE_ONLY · REJECT · INSUFFICIENT_EVIDENCE
`Decisão de adoção` — só existe se um projeto decidiu; **pesquisa não preenche este campo**
`Confiança` — quão sólida é a evidência coletada (não a recomendação)
`Evidência` — CONFIRMED · OBSERVED · REPORTED · INFERRED · UNVERIFIED · BLOCKED

Definições: `catalog/CATALOG-SCHEMA.md`. Máquina: `catalog/catalog.tsv`.

---

## 1. Tecnologia externa — auditoria (22 objetos)

Colunas separadas por exigência de `MISSION.md` §3: **estado** (quanto já se sabe),
**recomendação** (opinião técnica) e **decisão de adoção** (não existe, e esta base não
tem autoridade para criar).

| ID | Objeto | Licença | Estado | Recomendação | Decisão de adoção | Confiança | Documento |
|---|---|---|---|---|---|---|---|
| `LR-MCP-001` | `homeassistant-ai/ha-mcp` | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/ha-mcp/REPORT.md` |
| `LR-MCP-001-A` | proposta de arquitetura residencial | — | proposta derivada de `LR-MCP-001` | **ADAPT** | — nenhuma | Alta | `repositories/ha-mcp/ARCHITECTURE-PROPOSAL.md` |
| `LR-MCP-001-B` | matriz de risco R0–R3 | — | proposta derivada de `LR-MCP-001` | **ADAPT** | pendente (decisão do projeto) | Alta | `repositories/ha-mcp/RISK-MATRIX.md` |
| `LR-MCP-001-C` | contrato de servidor MCP de casa | — | proposta derivada de `LR-MCP-001` | **ADAPT** | — nenhuma | Alta | `repositories/ha-mcp/MCP-CONTRACT.md` |
| `LR-MCP-001-D` | plano de implementação em 8 fatias | — | proposta derivada de `LR-MCP-001` | **ADAPT** | pendente (decisão do projeto) | Média | `repositories/ha-mcp/IMPLEMENTATION-PLAN.md` |
| `LR-AGENT-001` | `open-jarvis/OpenJarvis` | Apache-2.0 | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/openjarvis/REPORT.md` |
| `LR-UI-001` | `vercel-labs/ui` | Apache-2.0 + beta | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/vercel-ui/REPORT.md` |
| `LR-FORGE-001` | `anefzaoui/misterdownloadmanager` | **GPL-3.0** | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/misterdownloadmanager/REPORT.md` |
| `LR-AGENT-002` | `tradermonty/claude-trading-skills` | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/claude-trading-skills/REPORT.md` |
| `LR-STUDIO-001` | `l0ng-ai/openidea` | Apache-2.0 | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/openidea/REPORT.md` |
| `LR-PROV-001` | `routerhubSI` (organização) | MIT / NOASSERTION | DOCUMENTED | **REJECT** | — nenhuma | Média | `repositories/routerhub/REPORT.md` |
| `LR-FORGE-002` | `islandmed/SculptForge` | **GPL-3.0** | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/sculptforge/REPORT.md` |
| `LR-STUDIO-002` | `Donchitos/Claude-Code-Game-Studios` | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/claude-code-game-studios/REPORT.md` |
| `LR-FORGE-003` | `academa-labs/manimgx` | mixed (6) | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/manimgx/REPORT.md` |
| `LR-AGENT-003` | `Ryder-Sun/Meldwork` | Apache-2.0 | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/meldwork/REPORT.md` |
| `LR-UI-002` | `backnotprop/plannotator` | Apache-2.0 | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/plannotator/REPORT.md` |
| `LR-FORGE-004` | `patch-gg/pixelfx` | MIT + NOTICE | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/pixelfx/REPORT.md` |
| `LR-AGENT-004` | `theclaymethod/unslop` | **nenhuma** | DOCUMENTED | **REJECT** | — nenhuma | Alta | `repositories/unslop/REPORT.md` |
| `LR-STUDIO-003` | `rescript-lang` (org, 39 repos) | LGPL no `compiler/` | DOCUMENTED | **REJECT** | — nenhuma | Alta | `repositories/rescript-lang/REPORT.md` |
| `LR-UI-003` | `elayadesign/ai-design-skills` | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Média | `repositories/ai-design-skills/REPORT.md` |
| `LR-SEC-006` | `elementalsouls/Claude-BugHunter` | MIT + CC BY 4.0 | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/claude-bughunter/REPORT.md` |
| `LR-STUDIO-004` | `storytold` (ArtCraft, 17 apps + 186 crates) | MIT OR Apache-2.0 | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/artcraft/REPORT.md` |
| `LR-STUDIO-005` | `ahwootech/BRUTAL` (framework C#/Vulkan) | BRUTAL License v1.0 (não OSI) | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/brutal/REPORT.md` |
| `LR-AGENT-011` | `akitaonrails/ai-memory` (memória multi-harness) | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/ai-memory/REPORT.md` |
| `LR-SEC-007` | `cloudflare/security-audit-skill` | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Média | `repositories/cloudflare-security-audit-skill/REPORT.md` |
| `LR-MODEL-006` | `tashfeenahmed/freellmapi` (free tiers agregados) | MIT (software) | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/freellmapi/REPORT.md` |

## 2. Projetos do ecossistema — dossiês internos (5)

| ID | Projeto | Documentos | Skills | Documento |
|---|---|---:|---:|---|
| `LR-PROJ-001` | Lia-Project | 261 | 22 | `projects/lia-project/INDEX.md` |
| `LR-PROJ-002` | Lia-Forge | 128 | 1 + 49 capabilities | `projects/lia-forge/INDEX.md` |
| `LR-PROJ-003` | Lia-Studio | 109 | 16 | `projects/lia-studio/INDEX.md` |
| `LR-PROJ-004` | Lia-AgentHub | 57 | biblioteca (48 no ecossistema) | `projects/lia-agent-hub/INDEX.md` |
| `LR-PROJ-005` | Lia-Model-Lab | 90 | 9 (únicos em `main`) | `projects/lia-model-lab/INDEX.md` |

## 3. Digests transversais (31)

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
| `LR-AGENT-010` | **pacote de Skills de edição** (ArtCraft como opção do usuário) | `cross-project/agents/ARTCRAFT-SKILL-PACK.md` |
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
| `LR-LIC-005` | **licenças prontas para uso** (18 objetos, obrigação em ação) | `cross-project/licensing/READY-TO-USE-LICENSES.md` |

## 3-bis. Comparações

| ID | Pergunta | Documento |
|---|---|---|
| `LR-CMP-001` | como expressar licença em projeto com terceiros e assets | `comparisons/LICENSE-MODEL-COMPARISON.md` |
| `LR-CMP-002` | qual servidor MCP de casa usar, se algum | `comparisons/MCP-SERVER-COMPARISON.md` |
| `LR-CMP-003` | como medir modelo/hardware sem virar fé | `comparisons/BENCHMARK-APPROACH-COMPARISON.md` |

## 4. Decisões (12 abertas + 5 tomadas)

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

17 repositórios com SHA no cabeçalho: `data/external/pinned-targets.tsv`; conferência de
2026-11-20 em `data/inventory/upstream-reaudit-2026-11-20.tsv`.
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
