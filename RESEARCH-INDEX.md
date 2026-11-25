# RESEARCH-INDEX

Índice canônico de tudo que esta base pesquisa. Uma linha por item, com ID estável,
veredito e caminho. **Este arquivo é a fonte de verdade dos IDs**: se um ID aparece em
outro documento e não aqui, o outro documento está errado.

- **Data de referência:** 2026-11-21 (dois objetos novos auditorados nesta data; reauditoria técnica dos 22 objetos concluída em 2026-11-20)
- **Itens:** 34 objetos externos (38 linhas com sub-documentos) + 5 dossiês internos + 31 digests transversais + 3 comparações + 18 registros de governança + **8 documentos de criação de personagens e 1 matriz de evidências** (2026-11-20, revisado em 2026-11-24)
- **Pouco foi executado.** Existem **30 linhas** em `data/testing/test-log.tsv` (2026-11-22):
  15 execuções locais com resultado positivo (11 suítes completas + 4 smokes de script), 4 execuções parciais e
  11 tentativas bloqueadas com motivo. Na
  criação de personagens, **nada foi executado** — não há GPU AMD nesta sessão e nenhum peso
  foi baixado.

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

## 1. Tecnologia externa — auditoria (44 objetos)

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
| `LR-AGENT-002` | `tradermonty/claude-trading-skills` | MIT | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Alta | `repositories/claude-trading-skills/REPORT.md` |
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
| `LR-UI-003` | `elayadesign/ai-design-skills` | MIT | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Média | `repositories/ai-design-skills/REPORT.md` |
| `LR-SEC-006` | `elementalsouls/Claude-BugHunter` | MIT + CC BY 4.0 | PARTIALLY_TESTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/claude-bughunter/REPORT.md` |
| `LR-STUDIO-004` | `storytold` (ArtCraft, 17 apps + 186 crates) | MIT OR Apache-2.0 | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/artcraft/REPORT.md` |
| `LR-STUDIO-005` | `ahwootech/BRUTAL` (framework C#/Vulkan) | BRUTAL License v1.0 (não OSI) | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/brutal/REPORT.md` |
| `LR-STUDIO-006` | `gamedev-skills/awesome-gamedev-agent-skills` (79 Skills + roteador, 12 engines) | Apache-2.0 | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Alta | `repositories/awesome-gamedev-agent-skills/REPORT.md` |
| `LR-AGENT-011` | `akitaonrails/ai-memory` (memória multi-harness) | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/ai-memory/REPORT.md` |
| `LR-SEC-007` | `cloudflare/security-audit-skill` | MIT | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Média | `repositories/cloudflare-security-audit-skill/REPORT.md` |
| `LR-MODEL-006` | `tashfeenahmed/freellmapi` (free tiers agregados) | MIT (software) | PARTIALLY_TESTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/freellmapi/REPORT.md` |
| `LR-FORGE-011` | `boschresearch/image-render-generative` | Apache-2.0 | PARTIALLY_TESTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/image-render-generative/REPORT.md` |
| `LR-FORGE-012` | `jenalab-com/jena-image-render` (+7 repos da org) | MIT | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Alta | `repositories/jena-image-render/REPORT.md` |
| `LR-SEC-008` | `bookwjitchieni1986/blender-ai-mcp-addon` ("mcp-for-blender-pro") | MIT com copyright de terceiro | DOCUMENTED | **REJECT** | — nenhuma | Alta | `repositories/blender-ai-mcp-addon/REPORT.md` |
| `LR-FORGE-013` | `apekshik/anymachine` (Blender procedural + `check.json`) | MIT | PARTIALLY_TESTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/anymachine/REPORT.md` |
| `LR-STUDIO-010` | `NVIDIA/SkillEvaluator` (gate de Skills em 3 níveis) | Apache-2.0 | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Alta | `repositories/skillevaluator/REPORT.md` |
| `LR-STUDIO-011` | `mvanhorn/last30days-skill` (anatomia de Skill grande) | MIT | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Alta | `repositories/last30days-skill/REPORT.md` |
| `LR-VOICE-002` | `KoljaB/RealtimeTTS` (wrapper de engines + fronteira de licença) | MIT no wheel 0.8.10 / Apache-2.0 na master | PARTIALLY_TESTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/realtimetts/REPORT.md` |
| `LR-MODEL-009` | `BreezeBlue/Breeze-TTS-2` + org `breezeblue-ai` | Apache-2.0 (código) × não comercial (pesos/saídas) | DOCUMENTED | **REJECT** | — nenhuma | Alta | `repositories/breeze-tts-2/REPORT.md` |
| `LR-AGENT-013` | `github.com/skills` + org `waifuai` + topic `stt-tts` | ausente na maioria | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta | `repositories/landscape-skill-noise/REPORT.md` |
| `LR-STUDIO-012` | `witnesstodark/mr-mak-workspace` (workspace local de vários agentes + pack de 20 Skills) | MIT (+ `img2threejs` Apache-2.0) | TESTED | **ADAPT** | — nenhuma | Alta | `repositories/mr-mak-workspace/REPORT.md` |
| `LR-FORGE-014` | `bisqit.app` — Bisqit, app fechado de desktop que fecha abas (o que ele lê, o que sai da máquina, o pipeline de foto → cachorro animado, preço por país) | **nenhuma** (proprietário fechado) | DOCUMENTED | **ADAPT** | — nenhuma | Alta para o que eles afirmam; nenhuma para o binário | `repositories/bisqit/REPORT.md` |
| `LR-FORGE-015` | `AppFlowy-IO` (org — 27 repositórios contados um a um) | AGPL-3.0 no produto; dual no editor; **nenhuma** licença em 6; SelfHost-Commercial sem LICENSE | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta para censo e licenças; média para o binário | `repositories/appflowy-io/REPORT.md` |
| `LR-FORGE-016` | `opf` (org OpenProject — 123 repositórios) + o cluster de IA | GPL-3.0 no produto (sem `ee/` na árvore); MIT no pack de Skills e no `recense` | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/opf-openproject/REPORT.md` |
| `LR-FORGE-017` | `every-app/open-seo` (OpenSEO) — MCP + 12 Skills + suíte executada aqui | **MIT** (um único LICENSE na árvore) | TESTED | **ADAPT** | — nenhuma | Alta (2.130 testes executados) | `repositories/open-seo/REPORT.md` |
| `LR-FORGE-018` | `capsoftware/cap` — gravação de tela; AGENTS.md de 125 linhas com ratchet | MIT só em `cap-camera*`/`scap-*`; **AGPLv3** no resto | DOCUMENTED | **ADAPT** | — nenhuma | Alta nos arquivos; nenhuma execução | `repositories/cap/REPORT.md` |
| `LR-FORGE-019` | `calcom/cal.diy` — fork com o comercial removido; `agents/` + symlinks | **MIT puro** (zero AGPL); licença stubada em `return true` | DOCUMENTED | **ADAPT** | — nenhuma | Alta | `repositories/cal-diy/REPORT.md` |
| `LR-SEC-009` | `chatwoot/chatwoot` — a fila de triagem de GHSA (211 linhas) e `enterprise/` | MIT exceto `enterprise/` (759 blobs, cláusula condicional) | DOCUMENTED | **ADAPT** | — nenhuma | Alta no que foi lido | `repositories/chatwoot/REPORT.md` |
| `LR-VOICE-003` | `debpalash/VoiceStudio` — 931 testes, 262/262 pins em SHA, NOTICE de assets | AGPL-3.0-only + `LICENSE-NOTICE.md` (comercial ok; pesos à parte) | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Alta (20 testes do fornecedor executados) | `repositories/voicestudio/REPORT.md` |
| `LR-VOICE-004` | `OpenWhispr/openwhispr` — transcrição local com allowlist de rede e 2 Skills | MIT | DOCUMENTED | **ADAPT** | — nenhuma | Alta nos arquivos; nenhuma em PT-BR | `repositories/openwhispr/REPORT.md` |
| `LR-FORGE-020` | `nanocle/Charakuru` — o repo é só documentação; o kit está no ZIP, e a licença cobra por faturamento | **sem SPDX**: `Charakuru Source-Available License v1.2`, 287 linhas; Skills são material coberto | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta no que está no repo (tudo lido), baixa no comportamento do kit (ZIP inacessível) | `repositories/charakuru/REPORT.md` |
| `LR-FORGE-021` | `hyz317/HairDeck` — código de artigo: 106 testes, 28 rodam sem GPU; peso chega com `sha256` e licença ao lado | **Apache-2.0** (código e checkpoints); termos de SAM 3 / DINOv3 não lidos | PARTIALLY_TESTED | **ADAPT** | — nenhuma | Alta no que executei aqui; média nos números de desempenho (deles, não reproduzidos) | `repositories/hairdeck/REPORT.md` |

## 2. Projetos do ecossistema — dossiês internos (5)

| ID | Projeto | Documentos | Skills | Documento |
|---|---|---:|---:|---|
| `LR-PROJ-001` | Lia-Project | 261 | 22 | `projects/lia-project/INDEX.md` |
| `LR-PROJ-002` | Lia-Forge | 128 | 1 + 49 capabilities | `projects/lia-forge/INDEX.md` |
| `LR-PROJ-003` | Lia-Studio | 109 | 16 | `projects/lia-studio/INDEX.md` |
| `LR-PROJ-004` | Lia-AgentHub | 57 | biblioteca (48 no ecossistema) | `projects/lia-agent-hub/INDEX.md` |
| `LR-PROJ-005` | Lia-Model-Lab | 90 | 9 (únicos em `main`) | `projects/lia-model-lab/INDEX.md` |

## 3. Digests transversais (34)

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
| `LR-AGENT-014` | declaração de envolvimento de IA: o gate do OpenProject (script de 129 linhas) comparado com os outros sete | `cross-project/agents/AI-INVOLVEMENT-DECLARATIONS.md` |
| `LR-MCP-004` | `confirm: true` como JSON Schema e `tools_integrity` — o par de plugins MCP do AppFlowy (verificador executado) | `cross-project/mcp/APPFLOWY-AI-PLUGINS-GATES.md` |
| `LR-LIC-006` | como se lê uma licença dividida: método em 5 passos e os 3 formatos medidos em 13 repositórios | `cross-project/licensing/SPLIT-LICENSE-SCAN.md` |

## 3-bis. Comparações

| ID | Pergunta | Documento |
|---|---|---|
| `LR-CMP-001` | como expressar licença em projeto com terceiros e assets | `comparisons/LICENSE-MODEL-COMPARISON.md` |
| `LR-CMP-002` | qual servidor MCP de casa usar, se algum | `comparisons/MCP-SERVER-COMPARISON.md` |
| `LR-CMP-003` | como medir modelo/hardware sem virar fé | `comparisons/BENCHMARK-APPROACH-COMPARISON.md` |

## 3-ter. Criação de personagens — silhueta primeiro (2026-11-20, ampliada e conciliada em 2026-11-20 UTC)

Pesquisa pedida pelo Lia Forge 2.0. **10 IDs e 10 documentos Markdown**, mais 1 matriz de 51
registros em 16 colunas; nenhum deles autoriza implementação.

Histórico das rodadas, em ordem cronológica (todas em 2026-11-20 UTC):

1. **Rodada 7.1** — correção factual: vídeo de referência reclassificado, contagens, licenças
   Tripo/Meshy, hardware AMD, regra de componente conexo por arquétipo.
2. **Rodada 7.2** — dois objetos novos: `LR-MODEL-008` (AetherAI) e `LR-FORGE-009` (Live2D).
3. **Rodada 7.3** — conciliação: Tripo `CONFLICTING`, Meshy por canal (Web App × API), acesso
   gratuito do Flow, ROCm 7.2.1/Ryzen AI oficial, evidência por dimensão na matriz.
4. **Rodada 7.4** — fechamento: quatro fontes oficiais do Tripo (incluindo as páginas de ajuda),
   Flow promovido a `OFFICIAL_DOCUMENTATION`, restrição de API no Free do Meshy e correções de
   contagem/ordenação.
5. **Rodada 7.5** — correção de fonte: proibição de treinamento do plano pago localizada no
   **§5.3** dos Termos (a ajuda citava §5.2.2), divergências de **visibilidade** e de
   **exclusão/retenção** registradas como itens próprios, e limite de **10 downloads/mês** do
   Meshy Free separado dos créditos.

| ID | Tema | Documento | Natureza |
|---|---|---|---|
| `LR-STUDIO-007` | visão geral, reutilização e conclusões | `cross-project/character-creation/CHARACTER-CREATION-RESEARCH.md` | síntese |
| `LR-STUDIO-008` | silhueta, linguagem de forma e avaliação automática | `cross-project/character-creation/SILHOUETTE-FIRST-DESIGN-RESEARCH.md` | método |
| `LR-STUDIO-009` | character sheet e consistência entre vistas | `cross-project/character-creation/CHARACTER-SHEET-CONSISTENCY.md` | técnica |
| `LR-MODEL-007` | modelos de imagem, controle e 3D; licença de código × pesos | `cross-project/character-creation/CHARACTER-GENERATION-MODEL-CATALOG.md` | catálogo |
| `LR-FORGE-007` | 2D→3D: 12 critérios e "pronto para jogo" | `cross-project/character-creation/CHARACTER-2D-TO-3D-PIPELINES.md` | comparação |
| `LR-FORGE-008` | produção: blockout a exportação | `cross-project/character-creation/CHARACTER-PRODUCTION-TOOLS-ASSESSMENT.md` | ferramentas |
| `LR-FORGE-010` | arquitetura de referência para o Forge 2.0 | `cross-project/character-creation/CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md` | recomendação |
| `LR-AGENT-012` | competências candidatas a skill | `cross-project/character-creation/CHARACTER-CREATION-SKILLS-ANALYSIS.md` | análise |
| `LR-FORGE-009` | Live2D: movimento só com JSON, padrão gerador+validador+verificação, licenças da pilha | `cross-project/character-creation/LIVE2D-MOTION-AUTHORING-RESEARCH.md` | ferramenta |
| `LR-MODEL-008` | AetherAI: serviço de assets 2D (pixel art, sprite animation), direitos e tokens | `cross-project/character-creation/AETHERAI-GAME-ASSET-SERVICE-RESEARCH.md` | serviço |
| — | matriz de evidências (**51 registros** = 46 da 7.0 + 3 da 7.1 + 2 da 7.2; 52 linhas com o cabeçalho) | `cross-project/character-creation/CHARACTER-CREATION-EVIDENCE-MATRIX.tsv` | dado |

Os três pipelines completos estão em `CHARACTER-2D-TO-3D-PIPELINES.md` §4 (IDs de pipeline
não recebem LR próprio: são propostas, não objetos auditáveis).

## 4. Decisões (12 abertas + 6 tomadas)

| Estado | IDs | Pasta |
|---|---|---|
| ACCEPTED (2) | DR-0006 (repositório público) · DR-0019 (protocolo contínuo de links) | `decisions/ACCEPTED/` |
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
