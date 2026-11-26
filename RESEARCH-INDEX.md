# RESEARCH-INDEX

Índice canônico de tudo que esta base pesquisa. Uma linha por item, com ID estável,
veredito e caminho. **Este arquivo é a fonte de verdade dos IDs**: se um ID aparece em
outro documento e não aqui, o outro documento está errado.

- **Data de referência:** 2026-11-26 (3 objetos auditados nesta data — o produto Animama, o conversor de avatares e o serviço PerfectVector, o primeiro `Tipo: serviço` do catálogo — e 1 matriz de recomendação; a rodada anterior, de 2026-11-25, trouxe 10 objetos e 1 digest de comparação; reauditoria técnica dos 22 objetos anteriores segue em `data/inventory/upstream-reaudit-2026-11-20.tsv`)
- **Itens:** 59 objetos externos (63 linhas com sub-documentos) + 5 dossiês internos + 34 digests transversais + **6 comparações** + 18 registros de governança + **8 documentos de criação de personagens e 1 matriz de execução** + 10 relatórios de 2026-11-17 (na seção própria)
- **Pouco foi executado.** Existem **43 linhas** em `data/testing/test-log.tsv` (2026-11-26):
  24 execuções locais com resultado positivo (14 suítes completas + 10 smokes de script), 6 execuções parciais
  (`PARTIAL`) e 11 tentativas bloqueadas com motivo. Nas criações de personagem e em tudo que exige GPU AMD,
  **nada foi executado** — não há GPU nesta sessão e nenhum peso foi baixado. Nas duas últimas rodadas entraram
  6 linhas: os dois validadores de Skill abertos (**346 análises + 177 validações**) executados sobre corpus
  próprio, em `LR-CMP-004`, `LR-AGENT-016`, `LR-AGENT-017` e `LR-AGENT-018`; e os dois gates de licença/
  empacotamento do Animama e do conversor (**12 testes + `check_source.py`** e **46 testes + `check.mjs`**),
  em `LR-UI-006` e `LR-FORGE-024`. Nenhum dos dois executou o produto.

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

## 1. Tecnologia externa — auditoria (59 objetos)

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
| `LR-AGENT-015` | `aaif-goose/goose` (o antigo `block/goose`) — framework de agente em Rust; governança por issue Ready e abandono do diretório próprio de MCP | Apache-2.0 (1 `LICENSE`, 0 `NOTICE`) | DOCUMENTED | **ADAPT** | — nenhuma | Alta no texto; execução `BLOCKED` (sem cargo) | `repositories/goose/REPORT.md` |
| `LR-AGENT-016` | `bytedance/deer-flow` — SuperAgent harness; **auditoria de Skill como contrato** (4 schemas, waiver com `file_sha256` + `expires_on`, CI de review) | MIT no código; marca e Skills fora do LICENSE | DOCUMENTED | **ADAPT** | — nenhuma | Alta nos arquivos; analisador **executado** aqui (346 análises) | `repositories/deer-flow/REPORT.md` |
| `LR-AGENT-017` | `anthropics/skills` + `anthropics/claude-plugins-official` + tópico `skill-creator` — onde mora a licença de uma Skill, e o que o validador deles rejeita | raiz **sem licença** + 18 `LICENSE.txt` por Skill; plugins Apache-2.0 | DOCUMENTED | **ADAPT** | — nenhuma | Alta no censo; validador **executado** aqui (177 arquivos) | `repositories/anthropics-skills/REPORT.md` |
| `LR-AGENT-018` | `obra/superpowers` — 15 Skills de processo, 12 manifests de runtime sincronizados por `.version-bump.json`, política de PR contra agente | MIT (1.070 B na raiz; 0 por Skill) | DOCUMENTED | **ADAPT** | — nenhuma | Alta nos arquivos; gates executados | `repositories/superpowers/REPORT.md` |
| `LR-VOICE-005` | `pipecat-ai/pipecat` — framework de voz que mantém 12 Skills de manutenção, `LICENSE-shadcn.md` por componente e `license-check.yaml` no CI | BSD-2-Clause | DOCUMENTED | **ADAPT** | — nenhuma | Alta no texto; nada executado | `repositories/pipecat/REPORT.md` |
| `LR-DATA-001` | `D4Vinci/Scrapling` — a biblioteca que publica a própria Skill (`agent-skill/` com `LICENSE.txt`, ZIP na `main`, `requires.bins`) | BSD-3-Clause + licença por Skill | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta no pacote; execução `BLOCKED` | `repositories/scrapling/REPORT.md` |
| `LR-FORGE-022` | `johannesjo/parallel-code` — agentes em worktrees (Electron/SolidJS); o **gate de IPC** que o Studio não tem (manifesto + allowlist + teste) | MIT (1 `LICENSE`; `package.json` sem campo) | DOCUMENTED | **ADAPT** | — nenhuma | Alta no `AGENTS.md`; `NOT_RUN` | `repositories/parallel-code/REPORT.md` |
| `LR-FORGE-023` | `dyad-sh` (org, 8 repositórios) + `dyad` — split Apache-2.0 + `src/pro/` sob FSL-1.1-ALv2; workflow que apaga release não autorizada | **NOASSERTION** = split com futuro Apache-2.0 | DOCUMENTED | **ADAPT** | — nenhuma | Alta nos arquivos de licença | `repositories/dyad/REPORT.md` |
| `LR-RAG-001` | `infiniflow/ragflow` — motor de RAG (3.549 `.go`); `AGENTS.md` que trata legado como passivo; 2 pointer-skills | Apache-2.0 (`license.go` é código, não licença) | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta no `AGENTS.md`; `NOT_RUN` | `repositories/ragflow/REPORT.md` |
| `LR-PROV-002` | `daytonaio/daytona` — 71.271 ★ e uma árvore de 3 arquivos: código para um lugar privado, licença só na tag | AGPL-3.0 **apenas em `v0.190.0`**; `main` sem `LICENSE` | DOCUMENTED | **REJECT** | — nenhuma | Alta (3 arquivos, todos lidos) | `repositories/daytona/REPORT.md` |

| `LR-UI-006` | `raymond-van/animama` — companion de mesa (Electron + FastAPI) com avatar VRM/Three.js, 24 emoções persistentes, memória Markdown versionada, formato de animação próprio (`animaPoseClip/2.0`) e inventário de licença por arquivo com gate no CI | **AGPL-3.0-only** no original; 5.953 arquivos com licença própria (ativos **não** são AGPL) | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta no que foi lido em código/doc/issue; **nula** em desempenho (nada do produto executado) | `repositories/animama/REPORT.md` |
| `LR-MCP-005` | `bitbonsai/mcpvault` — MCP local de vault Markdown: 18 ferramentas medidas (11 em `--read-only`), denylist, `patch_note` com contagem prévia, **446/446 testes**, zero chamada de rede no build | MIT | TESTED | **ADAPT** | — nenhuma | Alta | `repositories/mcpvault/REPORT.md` |
| `LR-AGENT-019` | `MemPalace/mempalace` (3.12.0) — memória textual com busca vetorial: arquitetura de palace global + extração por agente, **PT-BR real no produto** (47/47 chaves); mineração e busca não executáveis offline neste ambiente | MIT | PARTIALLY_TESTED | **REFERENCE_ONLY** | — nenhuma | Média | `repositories/mempalace/REPORT.md` |
| `LR-FORGE-024` | `raymond-van/animama-avatar-converter` — invólucro de qualidade em volta do conversor Mochiya (VRChat→VRM 1.0): validador de pré-requisitos, reparo de esqueleto, CLI que dirige o Unity sem `-nographics`, e uma checagem estática que prova que não há código de rede | **MIT** (1.068 B); UniVRM `v0.131.2` e Mochiya em commit fixo, ambos MIT; pacote npm com **zero** dependências | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta na estrutura e nos dois verificadores (executados aqui: 46 testes + `check.mjs`); nenhuma em conversão real (`BLOCKED` — exige Unity) | `repositories/animama-avatar-converter/REPORT.md` |
| `LR-VEC-001` | `perfectvector.com` (Rastrix Inc.) — **serviço** de vetorização PNG/JPEG/WebP→SVG com API em beta (`https://api.perfectvector.com/v1`, **sem CORS**, 1 conversão live simultânea, resultado expira em 24 h) e MCP por OAuth Google cobrando o saldo do site; packs USD 0,08–0,40/conversão; **o §10 do Terms proíbe usar entrada, saída ou preview em avaliação, benchmark ou validação de concorrente** | sem licença de código: só contrato (Terms 2026-11-25 · API Terms v1.1 · MCP Terms v1.3 · API Privacy Notice v1.1) | DOCUMENTED | **REFERENCE_ONLY** | — nenhuma | Alta em contrato, limites e preços (12 páginas oficiais lidas na fonte); **nula** em fidelidade relativa — não medido, e medir está proibido pelo fornecedor | `repositories/perfectvector/REPORT.md` |
## 2. Projetos do ecossistema — dossiês internos (5)

| ID | Projeto | Documentos | Skills | Documento |
|---|---|---:|---:|---|
| `LR-PROJ-001` | Lia-Project | 261 | 22 | `projects/lia-project/INDEX.md` |
| `LR-PROJ-002` | Lia-Forge | 128 | 1 + 49 capabilities | `projects/lia-forge/INDEX.md` |
| `LR-PROJ-003` | Lia-Studio | 109 | 16 | `projects/lia-studio/INDEX.md` |
| `LR-PROJ-004` | Lia-AgentHub | 57 | biblioteca (48 no ecossistema) | `projects/lia-agent-hub/INDEX.md` |
| `LR-PROJ-005` | Lia-Model-Lab | 90 | 9 (únicos em `main`) | `projects/lia-model-lab/INDEX.md` |

Contagens da coluna **Documentos** são o inventário de 2026-11-17. Re-medidas em 2026-11-26 na `main`:
Lia-Project **214** `.md` / 674 blobs / **21** `SKILL.md` (1 com `LICENSE`); Lia-AgentHub **50** `.md` /
165 blobs / **0** skills; Lia-Studio **83** `.md` / 210 blobs / **0** skills e **`LICENSE` MIT (1.539 B)**
novo na raiz. `BloomRX/Lia-Forge` e `BloomRX/Lia-Model-Lab` **não verificáveis** hoje (403 e 404 no token
da sessão). Tabela completa e classificação por linha em `audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md`.

**Sexto diretário em `projects/`, criado em 2026-11-26:** `projects/lia-design-foundation/`
(`README.md` + `INDEX.md`). **Não é dossiê de produto** — é índice de handoff, porque nenhum repositório
do projeto é legível por esta sessão (HTTP 404 em três grafias prováveis). As três linhas acima continuam
valendo como os cinco projetos inventariados.

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
| `LR-CMP-004` | o que um gate de Skill verifica, e o que escapa dele (dois validadores executados sobre 173 pacotes) | `comparisons/SKILL-GATE-COMPARISON.md` |
| `LR-CMP-005` | o que a Lia leva do Animama: 15 achados classificados e uma matriz por projeto, com o que **não** está recomendado | `comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md` |
| `LR-CMP-006` | qual é a integração mínima para a Lia ler notas Markdown de um vault do usuário, com seleção explícita, proveniência, escopo, correção e exclusão — e o que o Project ainda não tem | `comparisons/MD-NOTES-INTEGRATION.md` |

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
| Repositório público (deveria ser privado) | BLOCKED (403) | `DR-0006`; a decisão de manter a base pública foi reafirmada na conferência de 2026-11-26 (`audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md` §6) |
| `BloomRX/Lia-Forge` ilegível (HTTP 403) e `BloomRX/Lia-Model-Lab` ausente (HTTP 404) para o token da sessão: **28** linhas de ponteiro não conferíveis (17 na tabela §2 do índice do Forge, 11 nas §2/§3 do do Model Lab) | NOT VERIFIABLE (2026-11-26) | `audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md` §5, `projects/lia-forge/INDEX.md`, `projects/lia-model-lab/INDEX.md` |
| Busca vetorial local para a Lia: o `sqlite_exact` do MemPalace não elimina o download do embedder (~300 MB) | BLOCKED (ambiente sem rede) | `LR-AGENT-019` §5 |
| Fidelidade relativa entre vetorização paga e os vetores abertos: **não mensurável por contrato** — o §10 do Terms do PerfectVector proíbe usar entrada, saída, preview ou metadado em “evaluation, benchmarking” ou em validação de sistema concorrente; só consentimento escrito abre essa porta | BLOCKED (cláusula do fornecedor) | `LR-VEC-001` §5.4, §9 (R10), §11 (E16) |
| Retenção do editor on-line (≈3 meses) e do site (≈30 dias) do PerfectVector, e a **MCP Privacy Notice**: nenhuma das duas foi lida no documento-mestre | NOT RUN (fica para D-1) | `LR-VEC-001` §4 (P13), §11 (E17), `RESEARCH-ROADMAP.md` trilha D |
| `Lia Design Foundation` não é projeto legível para esta sessão: HTTP 404 em `BloomRX/Lia-Design-Foundation`, `lia-design-foundation` e `Lia-Design` (2026-11-26), e **0** arquivos desta base o mencionavam antes desta rodada — o índice criado é **handoff**, não dossiê | NOT VERIFIABLE | `projects/lia-design-foundation/README.md`, `LR-VEC-001` §10 |
| Comparção local da alternativa aberta está só no VTracer: `inkscape`, `potrace`, `autotrace` e `vtracer` (CLI) não existem neste sandbox (só ImageMagick 6.9.11-60) | BLOCKED: FALTA_DEPENDENCIA | `LR-VEC-001` §8, `RESEARCH-ROADMAP.md` D-2 |
