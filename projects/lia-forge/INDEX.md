# Índice — Lia Forge

---


> **Reauditoria de 2026-11-20.** Todo relatório externo listado aqui foi reavaliado
> nesta data (versão anterior, versão atual, mudanças, testes e conclusão). O detalhe
> está na seção `Reauditoria 2026-11-20` de cada `repositories/*/REPORT.md`;
> resumo por objeto em `audits/REAUDIT-2026-11-20.md`.

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem |
|---|---|---|---|
| `LR-FORGE-001` | Gerenciador de downloads GPL (aquisição de assets/pesos) | `repositories/misterdownloadmanager/REPORT.md` | pesquisa externa (novo) |
| `LR-FORGE-002` | Escultura 3D e disciplina de benchmark | `repositories/sculptforge/REPORT.md` | pesquisa externa (novo) |
| `LR-FORGE-003` | Animação programática e proveniência de licença | `repositories/manimgx/REPORT.md` | pesquisa externa (novo) |
| `LR-FORGE-004` | 244 efeitos pixel art / VFX 2D | `repositories/pixelfx/REPORT.md` | pesquisa externa (novo) |
| `LR-FORGE-007` | 2D→3D: image-to-3D, multi-view, splatting, blockout; 12 critérios | `cross-project/character-creation/CHARACTER-2D-TO-3D-PIPELINES.md` | pedido do Forge 2.0 (2026-11-20) |
| `LR-FORGE-008` | Produção: retopo, UV, textura, rig, exportação GLB | `cross-project/character-creation/CHARACTER-PRODUCTION-TOOLS-ASSESSMENT.md` | derivado de `LR-FORGE-007` |
| `LR-FORGE-010` | Arquitetura de referência do personagem no Forge 2.0 | `cross-project/character-creation/CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md` | derivado de `LR-FORGE-007` |
| `LR-LIC-002` | Proveniência de asset (E3) | `cross-project/licensing/ASSET-PROVENANCE.md` | `docs/T11-E3-ASSET-PROVENANCE-AND-CONTENT-VALIDATION.md` |
| `LR-AGENT-005` | Orquestração de agentes de produção de assets | `cross-project/agents/ASSET-AGENT-ORCHESTRATION-DIGEST.md` | `docs/T14-AGENT-ORCHESTRATION-ARCHITECTURE.md` |
| `LR-FORGE-005` | Ecossistema Blender / MCP | `cross-project/agents/BLENDER-MCP-DIGEST.md` | `docs/BLENDER-MCP-RESEARCH.md`, `docs/ECOSYSTEM-RESEARCH-BLENDER-ADDONS.md` |
| `LR-LIC-005` | Licenças prontas: NOTICE por componente, GPL como processo separado, CC-BY-SA fora do código | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 18 relatórios |
| `LR-STUDIO-004` | Composição/geração 2D·3D e crates de formato (leitura hostil, `craft-docpath`) | `repositories/artcraft/REPORT.md` | pesquisa externa (novo) |
| `LR-AGENT-010` | Edição determinística como alternativa a geração (custo, fidelidade, privacidade) | `cross-project/agents/ARTCRAFT-SKILL-PACK.md` | derivado de `LR-STUDIO-004` |

## 2. Pesquisa existente mantida na origem

| Documento | Bytes | Branch | Motivo |
|---|---:|---|---|
| `docs/LIA-FORGE-CONSOLIDATED-ARCHITECTURE-PROPOSAL.md` | 143 KB | sessão | proposta do projeto; pertence ao projeto |
| `docs/EXTERNAL-REPOSITORY-RESEARCH.md` | 120 KB | sessão | 40+ repositórios; indexado em `LR-FORGE-INDEX` abaixo |
| `docs/INTEGRATED-RESEARCH-AND-ARCHITECTURE-REVIEW-2026-11-14.md` | 104/114 KB | sessão | revisão contra código específico |
| `docs/INDEPENDENT-ARCHITECTURE-REVIEW.md` | 79 KB | sessão | revisão independente do projeto |
| `docs/T9-HYBRID-EXECUTION-AND-ASSET-PRODUCTION-RESEARCH.md` | 79 KB | sessão | pesquisa longa, ainda não destilada |
| `docs/ECOSYSTEM-RESEARCH-BLENDER-ADDONS.md` | 45 KB | sessão | catálogo de add-ons, vence rápido |
| `docs/CHARACTER-HAIR-MOTION-BACKENDS-AUDIT-3D.md` | 58 KB | sessão | auditoria técnica |
| `docs/PHASE-0-REPORT.md` | 55 KB | sessão | relatório de fase |
| `docs/IMPLEMENTATION-AUDIT.md` | 35 KB | sessão | auditoria de código |
| `docs/MODULE-CONSOLIDATION-AUDIT-3D.md` | 41 KB | sessão | consolidação Forge×3d-sprite×3d-create |
| `docs/UIUX-AUDIT-AND-IMPLEMENTATION-ROADMAP.md` | 38 KB | sessão | UX |
| `docs/WINDOWS-STABILITY-INTEGRATION-PLAN-2026-11-16.md` | 59 KB | sessão | plano |
| `docs/T12-ARCHITECTURE-AND-TOOLCHAIN-CONSOLIDATION.md` | 40 KB | sessão | consolidação de toolchain |
| `docs/T8-ARCHITECTURAL-DECISIONS-REVIEW.md` | 18 KB | sessão | revisão de decisões |
| `docs/DECISIONS-AND-OPEN-QUESTIONS.md` | 20 KB | sessão | decisões abertas do projeto |
| `docs/ADR-001-LIA-FORGE-DECISIONS.md` | 3,7 KB | `main` | decisão do projeto — **está em `main`** |
| `docs/ADR-002-P0-REMEDIATION-AUTHORIZATION.md` | 16 KB | sessão | autorização de remediação P0 |

## 3. Índice dos repositórios externos já pesquisados pelo projeto

O `EXTERNAL-REPOSITORY-RESEARCH.md` cobre (nomes extraídos do corpus):
`ggml-org/llama.cpp`, `hyz317/HairDeck`, `luminik-io/alfred`, `heygen-com/hyperframes`,
`neilsonnn/image-blaster`, `link-ding/doll-studio`, `Blizaine/Maestro`,
`legioncodeinc/honeycomb`, `aldegad/sprite-gen`, `leigest519/OpenGame`,
`arjun988/blender-skills`, `ahujasid/mcp-for-blender`, `SifuInTheShell/Effigy`,
`nanocle/Charakuru`, `MaxLiu22/Motion2MixamoRig`, `storytold/artcraft`,
`pixelartistry/PixelArtistry-Animated-Characters`, `chongdashu/ai-game-spritesheets`,
`jamesvovos/ai-game-asset-creator`, `hunyuan3d/hunyuan3d`, `yiboz2001/UltraTex`,
`zju3dv/GVHMR`, `vchoutas/smplx`, `nv-tlabs/kimodo`, `localai-org/kimodo.cpp`,
`wizzli/agents` (referências parciais).

**Regra de dedup:** antes de pesquisar qualquer um destes, consultar o documento do
Forge. Nenhum deles foi re-pesquisado nesta fundação — e não deve ser, sem motivo novo.

## 4. Skills do projeto (1)

| Skill | Função | Licença | Observação |
|---|---|---|---|
| `lia-brand-check` | revisão de marca | ❌ ausente no payload | duplica `lia-brand-consistency-review` (Model-Lab) |

## 4-bis. Criação de personagens (2026-11-20)

Pesquisa pedida pelo Forge 2.0 sobre "silhueta antes do 3D": **8 IDs, 8 documentos Markdown e 1 matriz com 49 registros** (46 da rodada 7.0 + 3 candidatos acrescentados na correção 7.1) em
`cross-project/character-creation/`. Três pipelines propostos (local, híbrido, alta
qualidade), catálogo de 49 registros com licença de código × pesos, e a conclusão dura:
**image-to-3D de qualidade não roda em RX 580 8 GB** (todos os candidatos exigem CUDA).
O modelo de linguagem (`LR-MODEL-007`) e as skills candidatas (`LR-AGENT-012`) completam o
conjunto. Nada disso foi implementado ou aprovado.

## 5. Lacunas

| Lacuna | Situação |
|---|---|
| 10 de 13 documentos de pesquisa fora de `main` | risco de perda |
| Duas versões do mesmo documento de revisão integrada | `CONFLICTING` |
| 24 capacidades "planned" nunca implementadas | estado registrado em código, não validado |
| Nenhum benchmark de render no hardware do usuário | `BLOCKED` |
