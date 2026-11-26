# Lia Forge — consolidação da pesquisa existente

| Campo | Valor |
|---|---|
| Repositório de origem | `BloomRX/Lia-Forge` |
| Branch padrão | `main` @ `6bd9a5a` (2026-11-13, **apenas 4 commits**) |
| Branch mais avançada | `codex/windows-stability-fixes` @ `f94d8b1` (2026-11-15) |
| Branches remotas | 10 |
| Arquivos (todas as branches) | 1.345 |
| Documentos distintos | 128 — **todos de autoria Lia** |
| Skills | 1 (`lia-brand-check`) |
| Data do inventário | 2026-11-17 |

---

## 1. O que este projeto é

Estúdio de produção de assets de jogo: pipeline 2D/3D, integração Blender, geração,
sprites, animação, e um registro de 49 capacidades em código
(`shared/capabilities/registry.mjs`: 16 implementadas, 5 parciais, 5 propostas,
24 planejadas).

## 2. Situação do conhecimento

O Forge é o caso mais extremo de descolamento entre `main` e trabalho real:
**`main` tem 4 commits**, enquanto branches de sessão têm até 94. Praticamente toda a
pesquisa (10 dos 13 documentos de pesquisa) existe só em branches.

Isto é o oposto do Lia-Project: lá `main` é antiga mas tem conteúdo; aqui `main` é
quase um esqueleto.

## 3. Pesquisa existente (13 documentos de pesquisa + 9 relatórios + 7 de arquitetura)

| Documento | Tamanho | Tema |
|---|---:|---|
| `docs/EXTERNAL-REPOSITORY-RESEARCH.md` | 120 KB | pesquisa individual de fontes externas de pipeline |
| `docs/INTEGRATED-RESEARCH-AND-ARCHITECTURE-REVIEW-2026-11-14.md` | 104–114 KB (2 versões) | integração das quatro pesquisas contra o código |
| `docs/LIA-FORGE-CONSOLIDATED-ARCHITECTURE-PROPOSAL.md` | 143 KB | proposta arquitetural consolidada |
| `docs/INDEPENDENT-ARCHITECTURE-REVIEW.md` | 79 KB | revisão independente |
| `docs/T9-HYBRID-EXECUTION-AND-ASSET-PRODUCTION-RESEARCH.md` | 79 KB | execução híbrida e produção 2D/3D |
| `docs/ECOSYSTEM-RESEARCH-BLENDER-ADDONS.md` | 45 KB | ecossistema de add-ons Blender |
| `docs/3D-RENDERING-TOOLS-RESEARCH.md` | 16 KB | motores e renderização |
| `docs/ANIMATION-TOOLS-RESEARCH.md` | 21 KB | animação |
| `docs/ASSET-PIPELINE-TOOLS-RESEARCH.md` | 17 KB | formatos e conversões |
| `docs/BLENDER-MCP-RESEARCH.md` | 16 KB | automação MCP com Blender |
| `docs/COLIBRI-TECHNICAL-RESEARCH.md` | 16 KB | avaliação de `JustVugg/colibri` |
| `docs/T11-2D-SKELETAL-ANIMATION-AND-AI-RESEARCH.md` | 17 KB | animação esquelética 2D |
| `docs/T14-AGENT-ECOSYSTEM-RESEARCH.md` | 17 KB | ecossistema de agentes para assets |

**Isto é o segundo maior corpus de pesquisa do ecossistema**, atrás apenas do
Lia-Project — e o menos acessível, por estar fora de `main`.

## 4. Duplicação detectada

| Par de documentos | Situação |
|---|---|
| `INTEGRATED-RESEARCH-AND-ARCHITECTURE-REVIEW-2026-11-14.md` (104 KB e 114 KB) | **duas versões na mesma branch** com tamanhos diferentes |
| `WINDOWS-VALIDATION-PLAN-CATALOG-RECONCILIATION-COMPARISON.md` (61 KB e 67 KB) | duas versões |
| `docs/README.md` e `docs/INDEX` implícito | índice documental de 25 KB pode estar defasado |

## 5. Tema crítico: licença de assets

`docs/T11-E3-ASSET-PROVENANCE-AND-CONTENT-VALIDATION.md` trata proveniência de assets
para o primeiro render E3 — o único documento do ecossistema que endereça proveniência
de **conteúdo** (não de código). É diretamente relevante para a política de licença
do Lia-Research.

## 6. Onde está a pesquisa que importa

Ver `INDEX.md`. Destaque: as quatro pesquisas de ferramentas (3D, animação, pipeline,
Blender-MCP) são as mais reutilizáveis; a proposta consolidada de 143 KB é a mais
densa e a mais arriscada de citar sem leitura (documento grande, fácil de
sobre-interpretar).

---

**Pesquisa desta base que toca este projeto agora** · 2026-11-26 — clip `animaPoseClip/2.0`, a gate de promoção por item e o matcher de nomes de morph no avatar VRM (`LR-UI-006` §3/§4), o invólucro do conversor (`LR-FORGE-024` §4/§6) e a matriz em [`comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md`](../../comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md) §4.2.
