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
| `LR-VEC-001` | Vetorização raster→SVG como serviço externo (API beta + MCP): contrato, limites, preço e o que os termos proíbem | `repositories/perfectvector/REPORT.md` | triagem dirigida pedida pelo dono (2026-11-26) |

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

## 4-bis. Criação de personagens (2026-11-20, ampliada e conciliada em 2026-11-20 UTC)

Pesquisa pedida pelo Forge 2.0 sobre "silhueta antes do 3D": **10 IDs, 10 documentos Markdown e 1 matriz com 51 registros** (46 da rodada 7.0 + 3 da 7.1 + 2 da 7.2) em
`cross-project/character-creation/`. Três pipelines propostos (local, híbrido, alta
qualidade), catálogo de 51 registros com licença de código × pesos, e a conclusão dura:
**image-to-3D de qualidade não roda em RX 580 8 GB** (todos os candidatos exigem CUDA).
O catálogo de modelos (`LR-MODEL-007`) e as skills candidatas (`LR-AGENT-012`) completam o
conjunto. Na rodada 7.2 entraram dois objetos fora do eixo 3D: **AetherAI** (`LR-MODEL-008`),
serviço de assets 2D com o termo de direitos mais permissivo entre os lidos, e
**`live2d-add-motion-sample-web-ui`** (`LR-FORGE-009`), cujo valor é o **padrão de fluxo**
(gerador + validador independente + verificação visual headless + Definition of Done), não a
tecnologia. Nada disso foi implementado ou aprovado.

## 5. Lacunas

| Lacuna | Situação |
|---|---|
| 10 de 13 documentos de pesquisa fora de `main` | risco de perda |
| Duas versões do mesmo documento de revisão integrada | `CONFLICTING` |
| 24 capacidades "planned" nunca implementadas | estado registrado em código, não validado |
| Nenhum benchmark de render no hardware do usuário | `BLOCKED` |

---

## Conferência de ponteiros — 2026-11-26: **não verificável**

Estado deste índice: **NÃO VERIFICADO**. Em 2026-11-26 pedimos o estado real da `main` e o token desta
sessão recebeu **HTTP 403 (Resource not accessible by integration)** de `gh api repos/BloomRX/Lia-Forge`
— o repositório existe e está privado para nós. Portanto nenhuma linha acima foi conferida contra a
`main` atual: o inventário é de 2026-11-17, quando o Forge era legível, e os ponteiros "na branch
`arena/*`" deixaram de ter valor preditivo porque os outros três produtos consolidaram e removeram as
suas em 2026-11-26. Nada foi apagado nem atualizado aqui; a data de última conferência continua
2026-11-17 e as pendências continuam válidas como *perguntas*.

Risco que esta lacuna cria, e que o dono precisa decidir: se o Forge seguiu o fluxo dos irmãos
(`docs/BRANCH-AND-RELEASE-FLOW.md`: branch temporária, remoção após snapshot), os documentos que os
nossos índices citam como "na origem" podem ter sido integrados, movidos ou removidos sem que a base
saiba. A correção não é reescrever o índice — é ler o Forge quando o acesso voltar, com `git ls-tree`
na `main` e comparação por SHA.

## 6. Handoff — vetorização de ativos raster→SVG (2026-11-26)

Pesquisa: `LR-VEC-001` (`repositories/perfectvector/REPORT.md`) — serviço PerfectVector (Rastrix Inc.),
API em beta + MCP oficial. Recomendação da base: **não integrar** nada disto no Forge.

| Condição | O que a pesquisa estabeleceu |
|---|---|
| Portas existentes | só duas: a **API** (`POST /v1/vectorizations`, 1 crédito no sucesso) e o **MCP** (OAuth Google, cobra do saldo do site). O Studio do navegador não tem automação |
| Por que o MCP está fora | ele não expõe chave nenhuma: amarra o uso à **conta Google de um usuário**, cobra do **saldo do site** e proíbe copiar/reusar/repassar as credenciais que entrega ao assistente (MCP Terms §6) — ou seja, não é "mais um provedor" que se registre com uma credencial: é uma conta de terceiro dentro do app, com consumo que só existe para uma pessoa. Se o princípio de credencial do usuário estiver confirmado no produto, o conflito é estrutural, não de configuração — e esta base não mediu o modelo de provedores do Forge, o que é dito aqui vem só do contrato do MCP |
| Por que a API não entra hoje | exige back-end nosso: **sem CORS** e chave jamais entregue ao usuário (API Terms §9); a Lia não tem servidor de retransmissão, e o resultado **expira em 24 h** (`410 result_expired`) — o pipeline teria de guardar cópia própria desde o primeiro dia |
| Se um dia houver back-end | as nove condições estão em `LR-VEC-001` §10 (chave da Lia, `Idempotency-Key` derivada do hash da origem, `connect-timeout 10 s` / `total 150 s`, persistência imediata do SVG, fila de 1 conversão por conta, `201 status:failed` como falha de negócio, rejeição local de <100 px / >5 MiB / animado / não-PNG-JPEG-WebP, termos próprios ≥ protetores, nada de material oficial no fluxo) |
| O que **não** é bloqueio técnico, é contrato | o §10 do Terms proíbe usar entradas, saídas, previews ou metadados em **avaliação, benchmark** ou validação de sistema concorrente — ou seja: a Lia não pode "provar que o próprio vetorizador é melhor" com material do serviço sem consentimento escrito |
| Custo de referência | **USD 0,08–0,40 por conversão** (packs one-time de 12 meses; preço da API pode mudar **sem aviso** — o §4.2 dos API Terms suspende a regra de 30 dias) |

O trabalho que a pesquisa **autoriza** no Forge é local: a medição da alternativa aberta (VTracer, MIT)
está em `LR-VEC-001` §8, com as quatro imagens sintéticas, os 5 parâmetros que o binding aceita e o
desvio de cor medido. Isso roda sem rede, sem crédito e sem contrato de terceiro.
