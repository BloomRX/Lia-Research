# Animama — o que um companion de mesa em VRM/Three.js resolve: formato de animação próprio, 41 ADRs e um inventário de licença por arquivo que roda como gate

| Campo | Valor |
|---|---|
| ID | `LR-UI-006` |
| Nome | `raymond-van/animama` — "The AI companion missing from your life": companheiro de desktop (Electron) com avatar VRM, 24 emoções persistentes, memória em Markdown versionado e ferramentas de criação de gesto |
| Tipo | repositório (produto completo: backend FastAPI em Python + app React/Electron em TypeScript) |
| Licença | **AGPL-3.0-only** para o trabalho original (raiz `LICENSE`, 34.020 B medidos; `pyproject.toml` declara `license = "AGPL-3.0-only"` + `license-files` com 4 textos de terceiros) — **e explicitamente não-AGPL para os assets**: `licenses/source-review.json` tem 5.953 entradas, uma por arquivo rastreado, com 10 valores distintos (AGPL-3.0-only 5.635 · `LicenseRef-pixiv-VRoidPreset` 128 · texto de aviso preservado 55 · CC0-1.0 32 · MIT+AGPL 25 · Apache-2.0+AGPL 17 · MIT do runtime Hey API 12 · marca registrada não licenciada 11 · AGPL com retratos sob termos VRoid 10 · **FunASR Model License 1.1** 5). Ver §9 |
| Fonte oficial | https://github.com/raymond-van/animama · https://animama.ai · https://docs.animama.ai (não lida aqui) · vídeo de walkthrough `youtu.be/sWw4bSrriDE` |
| Responsável | `raymond-van` (2.348 contribuições) + `claude` (4) — um mantenedor humano, trabalho assistido por agente, declarado por ele |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | LOCAL_TESTS_PASS — executamos **duas** checagens estáticas do próprio repositório no clone de `4ba6db1c`: `python3 scripts/public-release/check_source.py` (sai limpo) e as 12 unidades de `scripts/public-release/test_check_source.py` (OK em 0,139 s). **Nada do produto foi executado**: sem `pnpm install`, sem Node build, sem navegador, sem GPU, sem Windows, sem Unity |
| Recomendação | **REFERENCE_ONLY** para o produto e para o código (AGPL-3.0-only ⇒ não entra como dependência nem como base); **ADAPT** para seis mecanismos descritos em §11, que são de método e não de código |
| Decisão de adoção | — nenhuma registrada |
| Categoria | presença de desktop + avatar 3D + emoção/comportamento + memória de companion + governança de licença |
| Projetos beneficiados | Lia-Project (presença, voz, PiP, credenciais no Windows), Lia Forge (formato de animação + validadores + CLI de autoria), Lia Studio (skills de autoria com gate de promoção), Lia Agent Hub (os 21 `SKILL.md` e o symlink `.claude/skills`), Lia Model Lab (harness de benchmark de modelo com teto de custo e ensaio gratuito), Research (inventário de licença por arquivo) |
| Versão analisada | `main` @ `4ba6db1c5eb385b4cfb23b3595df2e3c89ebb6e5` (commit de 2026-11-25T20:18:31Z, igual ao `pushed_at`) · **0 releases e 1 tag** (`repo-split/initial-2026-09-08`) · instaladores publicados fora do GitHub: macOS 0.1.5, Windows 0.1.6 · backend `pyproject.toml` diz `version = "0.3.0"` |
| SHA completo | 4ba6db1c5eb385b4cfb23b3595df2e3c89ebb6e5 |
| Proveniência do SHA | **medido por nós**: `gh api repos/raymond-van/animama/commits?per_page=1` em 2026-11-26, e confirmado por `git rev-parse HEAD` no clone raso do mesmo dia |
| HEAD atual | 4ba6db1c5eb3… (o analisado é o tip) |
| Proveniência do conteúdo | medido por nós: árvore recursiva via API (`truncated: false`), **clone raso real** (`git clone --filter=blob:none` + `sparse-checkout`), leitura de `README.md`, `AGENTS.md`, `SPECS.md`, `SDLC.md` (parcial), `PLANS.md`, `GLOSSARY.md`, `pyproject.toml`, `contracts/versions.json`, `.env.example` (via API), 41 títulos de ADR, 12 ADRs lidos, `licenses/source-review.json` (5.953 entradas) e os 27 arquivos de `licenses/`, além de ~40 arquivos de `src/` e `docs/`. Nada foi baixado de `downloads.animama.ai`, nada de peso de modelo, nada de Git LFS (os `.vrm` do repositório são ponteiros de 132–133 B) |
| Data | 2026-11-26 |
| Última verificação | 2026-11-26 · `gh api` + clone + `node`/`python3` de execução local |
| Upstream conferido | **119 ★** · 13 forks · 16 issues abertas · `license: AGPL-3.0` · `language: TypeScript` · `size_KB 49.642` · criado 2026-09-08 · `pushed_at 2026-11-25T20:18:31Z` · `archived: false` · homepage `https://animama.ai` · **2.353 commits no histórico público**, sendo os dois primeiros "Repo Split" de 2026-09-08 (o histórico anterior é privado) · cadência: 53 commits em 2026-11-24 e 42 em 2026-11-25 |
| Confiança | **Alta** no que foi lido no repositório (código, docs, contratos, licenças, histórico). **Nenhuma** em comportamento: nada do app foi executado; desempenho, voz, render e Windows são `DOCUMENTED` ou `BLOCKED` |
| Próxima revisão | 2026-12-10 (repositório com ~45 commits/dia na coleta; vence rápido de propósito) |

---

## 1. O que o dono pediu, e como este dossiê foi feito

O pedido tinha oito áreas e uma condição: ler fonte real, não README. Este documento foi escrito assim:

| Etapa | O que foi feito | O que rendeu |
|---|---|---|
| 1 | Censo da árvore pela API, recursivo, `truncated: false` | 7.125 entradas · 5.953 blobs · 70,0 MB descomprimidos · 1.172 diretórios |
| 2 | `git clone --filter=blob:none` + `sparse-checkout` do **próprio repositório**, depois `git checkout` | 28 MB de material local para ler arquivos reais, sem baixar `node_modules`, pesos nem LFS |
| 3 | Leitura direta de `README.md` (230 linhas), `AGENTS.md` (391), `SPECS.md` (157), `PLANS.md` (157), `GLOSSARY.md` (378), `SDLC.md` (428, lido em partes), `pyproject.toml`, `contracts/`, `.env.example` | vocabulário do domínio e o contrato de processo |
| 4 | 41 ADRs listados por nome; 12 lidos (§4–§9 citam os números) | as decisões com data, donos e evidência |
| 5 | Leitura de código em `src/frontend/web/src/lib/{avatar,lipsync,emotion,speech,…}`, `src/backend/animama/app/`, `src/frontend/desktop/src/main-process/` | mecanismo, não descrição |
| 6 | `licenses/source-review.json` + `licenses/third-party/*.md` + `scripts/public-release/` | §9, e as duas execuções do cabeçalho |
| 7 | `animama.ai` e a página do vídeo (metadados + transcrição automática + comentários) | §12, marcado `DOCUMENTED` |
| 8 | `gh api` de issues/PRs do repositório (16 abertas; #928, #901, #782, #660, #712 lidos por inteiro) | §8, que é a única parte com números de desempenho reais |

O que **não** foi feito, de propósito: instalar dependências, rodar o app, rodar Playwright, baixar modelos, abrir `docs.animama.ai`, tocar em `downloads.animama.ai`. Nada disso é necessário para o que foi classificado abaixo, e tudo isso é o que separa `DOCUMENTED` de `TESTED` nesta base.

## 2. Números que falam sozinhos

Medidos nesta rodada, no commit `4ba6db1c` — todos por comando, nenhum por memória:

| Medida | Valor |
|---|---|
| blobs na árvore recursiva | **5.953** em 70,0 MB |
| arquivos de código em `src/` (`.ts/.tsx/.py/.mjs`) | **2.943**, 24,28 MB |
| `.ts` / `.tsx` / `.py` / `.mjs` / `.json` / `.md` no repositório | 1.526 / 588 / 1.060 / 229 / 1.243 / **412** |
| bytes por diretório de topo | `src` 34.699.757 · `docs` 16.640.194 · `content` 6.392.187 · `tests` 5.100.273 · `licenses` 2.593.575 · `scripts` 1.671.401 · `.agents` 1.431.905 · `uv.lock` 984.894 · `models` 59.747 |
| arquivos `.md` | 412 (9,62 MB) — **28 % dos bytes de texto do repositório são documentação** |
| ADRs | **41** (numerados, com status, data, "decision basis" e evidência) |
| `SKILL.md` em `.agents/skills/` | **21** (11 de produto: animação, VRM, quatro sabores de VFX, UI, stacks locais, release desktop, benchmark de modelo, assets de efeito · 10 de processo: `to-spec`, `to-execplan`, `implement`, `tdd`, `code-review`, `docs-sync`, `git-workflow`, `merge-n-clean`, `workspace-setup`, `intent-discovery`, `setup-ray-skills`) |
| testes | **795** arquivos `*.test.*` no total · 344 `.py` em `tests/` · 686 `.test.ts(x)` só em `src/frontend/web` · em `src/frontend/web/scripts/`, **46 scripts `.mjs`** e **41 arquivos de teste** (15 deles `.browser.test.mjs`) — só **29 dos 46** têm `.test.mjs` de mesmo nome ao lado; os 17 sem são, em sua maioria, de obra (`generate-routes.mjs`, `landing-*.mjs`, `local-page-server.mjs`, `optimize.mjs`, `verify.mjs`, `lipsync.mjs`, `animation.mjs`, `effect-save/promote.mjs`) |
| conteúdo incluído | **152 gestos + 168 reações + 26 poses**; VFX em três classes com 273 / 220 / 139 blobs (`particle` / `avatar` / `scene`) |
| tamanho de um clip de gesto | `wave-hello.json` = 6.852 B; **mediana 1.692 B**, máximo 55.855 B; uma reação = 988 B |
| contrato de versão | `contracts/versions.json`: `runtime-owner` 1.0.0 e `local-http` **25.0.0** (OpenAPI gerado offline) |
| dependências do web app | 64 de runtime / 23 de desenvolvimento · **42 scripts npm** · pnpm 10.33.0 |
| `pyproject.toml` | 37 dependências principais · extras `documents`(5) `voice`(1) `encrypt`(1) `viz`(0) `realtime`(0) · grupos `dev`(17) `desktop-build`(1) · mypy/ruff/pytest/coverage configurados no mesmo arquivo |
| atividade | 2.353 commits públicos; **53 no dia 2026-11-24 e 42 em 2026-11-25** |

Leitura honesta desses números: **152 + 168 = 320** gestos e reações, o que confere com o "over 300" do `README` e do site. E a mediana de 1,7 KB por animação é o efeito do formato descrito em §5 — é o número que diz se a ideia funciona, e funciona.

## 3. Avatar e renderização (área 1)

**A decisão estruturante está em ADR 0032, lido inteiro:** o avatar *é* um arquivo VRM (0.x ou 1.0) e sempre será — "VRM stays the Avatar container; ARKit shapes are a face capability". O motivo é técnico, não estético: *todos* os subsistemas montam sobre `three-vrm` — "humanoid motion, Gestures, poses and VRMA retargeting, spring bones, look-at, expressions, VFX anchors and portraits" — e um FBX nativo não carrega o mapeamento humanoid do Unity, nem os PhysBones, nem os ajustes de material lilToon. Aceitar glTF/FBX direto implicaria manter **uma segunda implementação** de esqueleto e molas. Eles optaram por pagar o custo na conversão (aí entra o `animama-avatar-converter`, dossiê `LR-FORGE-024`) e não no runtime.

Medido em `src/frontend/web/package.json` (via `gh api contents`, porque o arquivo não estava no meu sparse inicial): `three ^0.182.0`, `@pixiv/three-vrm ^3.5.5`, `@pixiv/three-vrm-animation ^3.5.5`, `three.quarks ^0.17.1` (partículas), `@mochiya/three-liltoon 0.1.9` e `three-stdlib 2.36.1` **fixos por exatidão**, `onnxruntime-web ^1.24.1` com um alias `onnxruntime-web-assets: npm:onnxruntime-web@1.24.2` — ou seja, a versão do runtime de inferência é pinada duas vezes, uma para o tipo e outra para o asset. React 19 + `@react-three/fiber ^9.8.2` + drei, Zustand 5, TanStack Router/Query, i18next 26.4.2, TypeScript **6.0.3**, Playwright 1.58.2, knip 6.43.0.

Rosto e olhos, em código lido:

- `lib/avatar/arkitFaceCapability.ts` — os 52 blendshapes ARKit são **detectados pelo nome do morph target**, não por material nem por preset: cada nome é reduzido a um conjunto de tokens minúsculos sem o token de lado e comparado com os nomes canônicos, o que casa `MouthSmile_L`, `mouthsmileleft`, o `Mouth_Smile_Left` do SRanipal e o `MouthCornerPullLeft` do Unified Expressions. Depois registra tudo sob o nome canônico (`registerArkitExpressions`), e "features usam esses nomes diretamente em avatares que os têm e caem no comportamento existente nos que não têm".
- `lib/avatar/spring-bone/` — física de cabelo/roupa **não é só a mola do three-vrm**: há um `SpringBoneSemanticClassifier` que classifica as molas por semântica (inclusive com tokens japoneses `前髪/横髪/後髪/髪`) e aplica `UNPROFILED_SPRING_BONE_INTENSITY_SCALE` às que não entraram em perfil, com limiar de confiança 0,5, aviso limitado a 5 e a extensão `VRMC_springBone` (VRM 1.0) tratada separadamente da `VRM` 0.x. É o oposto de "confia no que o arquivo traz": o arquivo é suspeito até ser classificado.
- `lib/avatar/Avatar.ts` começa importando `measureAvatarProportions`, `bodyFramingScale`, `headFramingCenter`, `headFramingScale`, `setAvatarFaceSize` — o enquadramento do corpo/cabeça é calculado por avatar, porque a mesma cena tem de servir a janela grande e o PiP de 210×280 (§8).
- Lip-sync em §7.
- Presença de desktop: `main-process/pip/pip-window-manager.ts` — janela frameless, `transparent: true`, sempre no topo, sem sombra, sem entrada na barra de tarefas, 210×280 inicial, limites 116×154–1200×896 (`:508`, `:107`), clique atravessado por `window.setIgnoreMouseEvents(true, { forward: true })` (`:995`), e o `quick-chat` liga `backgroundThrottling: false` (`:455`) justamente porque um renderer estrangulado quebra a presença. Multi-monitor não é tratado como "tela principal": o PiP "reopens where the owner last left it on this machine". Não há, no repositório, qualquer menção a transparência por chave de cor nem a "janela por monitor" — o modelo é uma janela de topo por instância.

## 4. Emoções e comportamento (área 2)

Isto é o que há de mais transferível no projeto, e a fonte é o tripé `docs/frontend/runtime/avatar-emotion.md` (668 linhas, lido em partes) + `src/backend/animama/domain/emotions.py` + `app/primary_emotion_update.py` (157 linhas, **lido inteiro**), com o vocabulário em `GLOSSARY.md`.

O estado é **por emoção, não por grupo**, e o grupo é derivado:

- 24 emoções persistentes = 8 grupos × 3 (`affection: admiration|caring|love`, `esteem: respect|confidence|gratitude`, `delight`, `drive`, `alarm`, `rejection`, `revulsion`, `gloom`), com `neutral` **não persistido** ("can appear only as metadata on no-op `emotion.update` events").
- Cada valor vive em `0..30`; novos Animas começam todos em `0`. Budgets explícitos no domínio: `EMOTION_PROMOTION_BUDGET = 5`, `EMOTION_DEMOTION_BUDGET = 3`, `EMOTION_PROMOTION_LIMIT = 3`, `EMOTION_DEMOTION_LIMIT = 2`.
- O modelo não escreve estado: escreve **`emotional_tone` (um tom vocal, ex. `impressed`) e `emotional_intensity` de 1 a 10**. O backend faz o resto, e a escala é dupla e deliberada: `1-3 → desloca 1`, `4-6 → 2`, `7-10 → 3` para o **estado**; e `1-2 → nenhuma Reação`, `3-4 → Mild`, `5-6 → Moderate`, `7-8 → Strong`, `9-10 → Intense` para a **representação**. As duas escalas têm limiares diferentes de propósito: "a turn at 1-2 still shifts the emotion state" sem gesticular.
- O `primary_emotion_update.py` faz o resto em 30 linhas legíveis: se o tom é não-neutro e reconhecido, promove a emoção canônica mapeada **e rebaixa uma emoção do grupo oposto**, sorteada (`_default_opposing_emotion_chooser` = `random.choice`), com o grupo oposto vindo de `OPPOSING_EMOTION_GROUPS` (`affection↔rejection`, `delight↔gloom`, `drive↔alarm`, …); se não houver candidato, a Reação vai a zero. Tudo clampado a `0..30`.
- Persistência: `anima.emotional_state` é um objeto completo de 24 chaves; o SSE é `emotion.update` **full-state**, e o `EmotionGroup` "não é persistido nem emitido". Bandas de intensidade derivadas: `0-4 → 0`, `5-15 → 1`, `16-25 → 2`, `26-30 → 3`.
- Representação visual, medida no doc: o manifesto de animação só tem 6 faixas — `neutral/joy/fear/angry/disgust/sad` — e os 8 grupos são **reduzidos** a elas (`affection→neutral`, `esteem→neutral`, `delight→joy`, `drive→joy`, `alarm→fear`, `rejection→angry`, `revulsion→disgust`, `gloom→sad`). Ou seja: a vida interior tem 24 dimensões e o corpo tem 6 faixas. Essa assimetria é a decisão, não um defeito.
- **Não há decaimento.** Procurei por `decay|drift` no documento e no domínio: o valor persiste até o próximo turno ou uma edição; `Reflection`/`Automatic episode processing` mexem com memória, não com emoção. "shift and evolve during your time together", do site, é verdade no sentido de *acumular*, não de *esfriar*.
- Reações = 24 emoções × 4 intensidades = **96 células**, cada uma com até 4 Reações; "para cada evento emocional o chat toca um membro da célula ao acaso, nunca o que tocou antes quando a célula tem ≥2"; célula vazia **não** cai em outra célula ("never falls back"). 168 itens medidos em `content/included/reactions/`, exatamente 7 por emoção.
- Idle = um pool por Anima, semeado na criação: pool Default + uma célula por (emoção, intensidade); "cada idle é um gesto Default metade do tempo e, na outra metade, um gesto das células da emoção atual com intensidade ≤ a corrente"; e **"Idle Gestures are never AI-callable"** — o modelo escolhe gesto *ativo*, nunca o fundo. O conjunto de avaliação de seleção de gesto usa um loadout de **140 gestos** (`docs/benchmarks/inputs/loadout-starter-v1.json`, contado por mim).

O autor explica a ascendência conceitual no próprio vídeo (§12): a roda de Plutchik com pares opostos, reetiquetada com as 27 classes do **GoEmotions** do Google, rotuladas para conversa. A base do repositório confirma o resultado, não a narrativa: os grupos opostos e os nomes são exatamente uma recorte conversacional.

## 5. Animação e ferramentas: `animaPoseClip/2.0` (área 3)

O formato é a contribuição mais concreta do projeto para qualquer pipeline de personagem. Contrato lido em três camadas:

- `src/backend/animama/app/services/clip_format.py:19` — `ANIMA_POSE_CLIP_SCHEMA = "animaPoseClip/2.0"`, com a frase do cabeçalho dizendo que é **o único** formato e que o 1.0 aposentado é **rejeitado com uma mensagem clara, nunca convertido** (ADR 0016). A mensagem é a mesma no frontend (`parseClip.ts`) e no import de pacote, e há um cuidado explícito: "The HTTP boundary never echoes submitted data" — o schema estranho citado vem de `repr` curto, imprimível e ≤64 caracteres, porque "diagnostics are persisted and shown".
- `src/frontend/web/src/lib/avatar/poses/animaPoseClip/clipVocabulary.ts` — `MAX_ANIMA_POSE_CLIP_BYTES = 2 * 1024 * 1024` e `ANIMA_POSE_CLIP_DECIMALS = { transform: 5, time: 4, expressionWeight: 3, other: 5 }`, com a justificativa no comentário: cinco decimais seguram rotação a milésimos de grau; quatro seguram tempo a 0,1 ms; três seguram peso de expressão; "coarser rotations would drift down bone chains and turn slow motion into visible steps".
- ADR 0014 — o porquê: com `1.0`, gestos escritos por agentes eram curvas por osso assadas em keyframes densos: **"about 100 times the size of their curves, about 8 s of busy motion within the 2 MiB clip limit, and 60–250 keyframes that cannot be edited in the Gesture creator"**, e a intenção de autoria se perdia. A resposta foi o formato por trilhas agrupadas em **beats** (`start/raise/wave/lower/settle`, vistos no arquivo real), com dois tipos de trilha de rotação — **anatômica**, em graus nos componentes nomeados do modelo de articulação (vocabulário `animamaMotion/1` + auxiliares que completam os 3 eixos), e **quaternion por osso com slerp**, esta para poses feitas à mão e clips 1.0 convertidos — um osso usa um tipo só. Interpolação "chega" na chave: `smooth` (cúbica monotônica), `linear`, `hold` ou um easing 1.0, por chave ou por beat. Mãos usam **presets do Hands tool com Curl/Spread** e pés plantados são resolvidos pelo rig do próprio avatar (`plantFeet`), o que é o que permite re-posing num avatar com proporção diferente.

Um clip de verdade, lido em `content/included/gestures/wave-hello/wave-hello.json` (6.852 B): `schema`, `id`, `name`, `duration: 2.6`, `basePose: "relaxedRest"`, `fadeIn/fadeOut` com durações, `mutedProceduralLayers: [sway, bounce, headNod, headSideTilt, cursorLookAt, emotionPosture]`, `plantFeet: true`, `beats[5]` com `id/label/time`, e `joints.rightShoulder…`. Uma Reação (`admiration-1.json`, 988 B) acrescenta `role: "reaction"` e `playback.lifetime.kind = "whileInteractionPhase"` com `phases: ["talking"]` e `scope: "activeRun"` — a animação sabe sozinha quando morrer. E ao lado de cada item, um `*.meta.json` com `content_type`, `content_id` (`builtin:gesture:wave-hello`), `semantic_key`, `ai_description` — **a descrição que o modelo lê para escolher o gesto é um campo do conteúdo, não um comentário no código**.

Ferramenta de autoria, lida no CLI e no skill:

| Comando | O que faz |
|---|---|
| `pnpm -s animation joints` / `animation base` | consulta de juntas/limites e valores-base, para o agente não inventar ângulo |
| `animation validate <clip>` | estrutura + valores fora de limite anatômico com **JSON paths**, e o tamanho serializado contra os 2 MB que o app carrega |
| `animation check <clip>` | `range`, `smoothness`, `intersections`, `feet`; mede cada contato no seu `point` (um contato resolvido vale ≤1,5 cm); avisa quando um braço resolvido está longe do alvo ou a palma não aponta para o `facing`; acha dedo atravessando dedo/palma/outra mão; e **avisa em oscilação rápida (junção oscilando acima de ~4 Hz por 3 ciclos)** |
| `animation:preview <clip>` | reprodução ao vivo nos dois avatares incluídos, iluminada como a tela de chat, com camadas procedurais vivas, marcadores de beat e presets de câmera; recarrega ao editar |
| `animation:render --times --side left --view hands` | folhas de contato em stills e close-up de uma mão em quatro ângulos |
| `animation resolve` / sidecar de revisão | cada nota humana do dono fica registrada e é resolvida uma a uma (`preview/reviewNotes.ts`) |
| `animation:save <items.json>` | salva **pelo creator** (novo Local item ou revisão do mesmo Selector ID), nunca escrevendo `content/local/` na mão |
| `animation promote <items.json> --dry-run` | passo 9 do skill, só com aprovação explícita do dono por item **e por entrada de licença** |

Existe uma segunda peça importante: `src/backend/animama/app/services/idle_clip_validation.py` diz, no docstring, "**Mirrors** the frontend `validateAnimaPoseClipV2`" — a validação estrutural existe **duas vezes**, em Python e em TypeScript, comparando tempos em ticks de 0,1 ms. É robusto para o usuário (o backend não confia no que chegou) e é um custo de manutenção real (§10).

O que **não** tem equivalente no repositório: qualquer editor visual com timeline que rode fora do app, qualquer importador de FBX/BVH/Mixamo no lado do produto (há `scripts/mixamo-motion/` e `docs/frontend/runtime/mixamo-acquisition.md` para *aquisição*, e o pacote Mixamo entra como conteúdo "non-portable", ADR 0018), e qualquer ferramenta de captura de vídeo.

## 6. Inteligência e memória (área 4) — comparação conceitual, sem hierarquia

Fontes: `docs/backend/features/memory.md` (868 linhas, lido em partes + todos os títulos), `docs/backend/features/memory-manager-and-episodic-memory.md` (1.423 linhas, títulos + §178-347), ADRs 0004/0009/0024/0034, e o vocabulário do `GLOSSARY.md`.

O desenho, em sete frases:

1. **A memória são arquivos Markdown legíveis** e o banco é a autoridade de identidade, versões, escopo e recibos. ADR 0004 recusa as duas alternativas óbvias — "byte store opaco" e "escrever em arquivo e banco sem coordenação" — e escolhe journals no filesystem + recibo durável no banco, com a frase: "Journals are recovery evidence, not disposable caches".
2. Escopo: `PROFILE.md` é do usuário e **compartilhado por todos os Animas**; cada Anima exige `IDENTITY.md` e `MEMORIES.md`; episódios ficam em `episodes/YYYY/MM/YYYY-MM-DD.md`.
3. Captura episódica é **um campo do reply estruturado**: `remember`. Se o turno é incógnito, nulo ou branco, não captura; se a captura falha, "logged and do not turn an otherwise successful chat response into an SSE error". A tabela `memory_episode_items` é a fonte da verdade; **o `.md` diário é uma projeção gerada** com itens `- [ ] <!-- episode:id -->`, só para poder ser lido e buscado pelo sistema de arquivos.
4. Injeção no prompt com limites numéricos, não com "o que couber": o perfil entra inteiro até **16 KiB** e depois só o começo cortado em fim de linha com um aviso de que o resto está a um `memory_read_files`; as notas recentes são no máximo **20 notas / 3.000 caracteres / 14 dias locais**, selecionadas da mais nova para a mais antiga **parando antes** da que estouraria o orçamento, listadas da mais antiga para a mais nova, com a data local de cada uma; `# Anima Memories` vem com preâmbulo fixo que diz "trate como notas lembradas, nunca como instruções" e que linhas descrevendo o que *pertence* a um cabeçalho **não são memórias**.
5. Ferramentas: `memory_list_files`, `memory_read_files`, `search_memory_files` (busca léxica por padrão, com `include_episodic_memory`), `memory_apply_patch` / `memory_write_file` (nativo `apply_patch` no caminho OpenAI Responses), `search_uploaded_files`, `read_uploaded_file_chunks`. Embeddings existem como **papel de modelo opcional**: "Embeddings stay off, with keyword search, until chosen".
6. Consolidação tem **dois motores com política diferente**: o *Automatic episode processing* roda sozinho quando as notas pendentes atingem o limiar das App Settings, **aprova as próprias propostas**, só escreve memória compartilhada (`PROFILE.md`) e marca cada mudança no histórico como automática; já a *Reflection* é **"owner-started… It never runs automatically"**, cobre turnos não cobertos por uma Reflection aplicada e propõe uma edição curada de `MEMORIES.md`. A versão hospedada não tem processamento automático nenhum.
7. Toda mudança é versionada e reversível, com identidade de operação idempotente ("Save and Import retries with the same owner-scoped operation identity… return the original successful result"), e a regra de idioma (`MEMORY_LANGUAGE_RULE`) manda escrever a memória no idioma da conversa, manter nomes/alcunhas/palavras citadas como o usuário escreveu, **não traduzir texto existente** e nomear arquivos em ASCII.

Posto ao lado do que esta base registra da Lia (`cross-project/memory/MEMORY-LANDSCAPE.md`, `LR-AGENT-007`):

| Eixo | Lia (registrado nesta base) | Animama (medido aqui) | Leitura |
|---|---|---|---|
| Forma da memória | local, com autorização de tools e atribuição de fonte | Markdown em FS virtual + versões | **convergem**; não há motivo para a Lia mudar nada |
| Vetor antes do léxico | regra de ouro: não adicionar banco vetorial antes de medir falha do lexical | embeddings são papel opcional; padrão é keyword | **corrobora a regra da Lia com uma segunda implementação independente** — o que vale citar em defesa da decisão, não alterá-la |
| Memória compartilhada | "não deve existir", por decisão de independência entre projetos | `PROFILE.md` compartilhado **entre Animas de uma mesma instalação**; nada compartilhado entre composições | eixos diferentes (projeto × companion). Não é contradição nem precedente |
| Métrica | "não há métrica pública de recall"; lacuna `NOT RUN` | harness de benchmark com **braços de memória episódica** e um `Memory Manager` como área própria | é aqui que a Lia tem lacuna e o Animama tem instrumento (§11, item F8) |
| Retenção | política "não documentada" | 14 dias / 20 notas / 3.000 caracteres só para a **injeção**; os itens ficam no banco | o recorte útil é separar *retenção* de *janela de injeção* |

Duas coisas que a Lia **não** tem e que merecem existir como pergunta (não como instrução): (a) o campo `remember` dentro do mesmo reply estruturado que já produz a fala — custo marginal zero de ida ao modelo, e a resposta do app pode mostrar "Memory updated" porque `message_data.memory` grava o que o turno lembrou; (b) o cue persistido por mensagem, que é o que torna a memória auditável na conversa em vez de num log.

## 7. Modelos, voz e infraestrutura (área 5)

`GLOSSARY.md` define o vocabulário e o código cumpre: **Model connection** (base URL + credencial + opções de compatibilidade, falando OpenAI Responses, OpenAI Chat Completions ou Anthropic Messages), **Model role** (chat padrão, `Utility` para títulos e compactação, `Memory Manager`, `Embeddings`), **Account-listed models** (a lista que o plano ChatGPT mostra, guardada como linhas somente-leitura e "retired at sign-out"; ADR 0039), e "Keys and sign-in tokens never enter the database".

Saída estruturada e streaming, lidos em `app/main_structured_response.py` (500 linhas):

- o reply principal é **um único objeto JSON** com `emotional_tone`, `emotional_intensity`, `gesture`, `speech`, `display`, `remember`; o schema é Pydantic (`create_model`, `field_validator`) e "strict JSON schema" é literal no docstring.
- para não esperar o objeto fechar, há um **parser incremental de JSON escrito em campo por campo**: `_skip_json_ws`, `_decode_json_string_prefix`, `_scan_top_level_string_field`, `_scan_top_level_value_field` — scanners próprios, com estado `complete`/`invalid` — e a classe `MainStructuredJsonStreamParser`, que explica a política no docstring: "Early streaming follows that order: it waits for tone + intensity together, waits until gesture is complete, and only then emits speech sentence chunks. The final full JSON parse remains authoritative for validation and persistence."
- `gesture` passa por `normalize_gesture_id` + `GestureValidationResult(raw, normalized, gesture, dropped_reason)`: o que o modelo inventou é **descartado com motivo registrado**, não repassado nem corrigido em silêncio. O `scripts/evals/gesture_selection.py` mede exatamente isso, rodando "the same system prompt (and turn context, when there is any), equipped Gesture list, structured reply schema, structured repair and salvage, and Gesture validation as `chat:sse`", com repositórios substituídos por stand-ins em memória e turnos `store=False`.
- **`Pre-send compaction`**: resumir o histórico com o papel `Utility` *antes* de mandar, "so a model without native compaction never receives a prompt larger than its context window"; se o resumo falha, "the oldest messages are left out of that request instead". Compactação pós-resposta continua sendo o caminho normal.
- **Layout de prompt para cache** é documento de projeto (`docs/backend/runtime/prompt-caching.md`, 264 linhas) com harness opt-in `tests/live/test_prompt_cache_layout.py` que roda um chat scriptado de 6 turnos e mede a fatia de tokens de entrada servidos do cache em **cada caminho de provedor** — e a regra: "A layout change must not lower the share on any path."

Voz (lida em `docs/backend/integrations/voice-and-speech.md`, nos `models/*/manifest.json` e em `lib/speech`): STT offline no cliente (Parakeet para inglês, SenseVoice-Small para ja/ko/zh), MicVAD e "Smart Turn" de fim de turno; TTS ElevenLabs (realtime), Gemini, OpenAI e **Pocket TTS rodando no computador**. O pipeline de lábios é §7-below. `emotional_tone` vira *duas* coisas distintas conforme o provedor: tags de áudio curtas (`[laughs]`, `<long pause>`) **só quando a voz do turno é Gemini ou ElevenLabs** — "Pocket TTS, browser speech and chat bubbles receive none" — e, no Gemini, uma frase de estilo ("Speak in a very happy tone."). Para o Pocket, existe um mecanismo próprio: `docs/frontend/features/emotional-voice-catalog.md` descreve catálogos binários privados de embeddings de voz por (emoção, intensidade).

**pt-BR (pergunta explícita do dono).** Medido, não inferido:

- `src/backend/animama/domain/settings.py:15` — `UiLocale = Literal["en", "ja", "ko", "zh-Hans", "zh-Hant"]`. **Não existe `pt`**, e a ADR 0024 faz do Locale o idioma da conversa (instrui o modelo e fixa o código de fala).
- `docs/backend/integrations/voice-and-speech.md:38-41` — o `language_code` enviado ao ElevenLabs/Gemini só assume `ja`, `ko`, `zh` (inglês deixa o padrão); e `:70` "Speech is sent as written, in any language, without its emoji". Ou seja: texto em português passa, **mas nada é ajustado para ele**.
- STT: Parakeet é inglês, SenseVoice é ja/ko/zh — nenhum cobre português; Pocket TTS "works only in English and show[s] a warning under other locales".
- Lip-sync: `lib/lipsync/eval/clip.ts:15` `EvalLanguage = "en" | "ja" | "ko" | "zh" | "es"` — **há avaliação para espanhol e nenhuma para português**; `docs/plans/lipsync-upgrade/lipsync-research.md:308` lista "French, German, **Portuguese** | not prototyped". O dicionário é CMUdict+SCOWL (inglês). O único lugar onde o português aparece como regra é o fallback genérico `latinUnits` (`converters.ts:206-211`: "Letter rules for Latin-script words other than English, such as Spanish or Portuguese"), usado quando ainda não existe definição de idioma por Anima.

Conclusão honesta: para um produto **pt-BR-first**, o Animama não traz nada que esteja pronto; traz o desenho onde uma língua nova entra (converter + `EvalLanguage` + grupo de pontuação + referência de vogais + setting de idioma de fala por Anima, que a ADR/lista menciona como pré-requisito #385).

## 7-bis. Lip-sync, porque é o subsistema que a Lia mais provavelmente vai querer

`docs/frontend/runtime/avatar-lipsync.md` + `lib/lipsync/planner.ts` lidos por inteiro na parte relevante:

1. Cada provedor de voz encaixa um **tap neutro** (`lib/speech/speech-pcm-tap.ts`): ElevenLabs/Gemini/Pocket entregam todo chunk de PCM que mandam tocar, "with silence for any gap they schedule"; o chunk que abre uma parte leva o texto; jogadores reportam onde a reprodução retomou depois de underrun; e a fala do navegador, **cujo áudio não pode ser capturado**, reporta início/fim e palavra por palavra onde a voz diz. Isso é a abstração certa: o plano é do áudio que *saiu*, não do que o provedor prometeu.
2. O planejador roda em **worker off-main-thread**, é **progressivo** ("units placed well behind the newest audio (two seconds) are kept, and each call re-aligns only the audio after them"), e eles publicam o custo: "about 2 ms a call for a two-minute part, in Node".
3. O que o bridge faz com o plano: um segmento `vowel5` no relógio de reprodução, **amostrado por `AudioContext.currentTime`** no `ExpressionController` — não por `requestAnimationFrame`, o que é a diferença entre lip-sync e gaguejo quando o render escorrega.
4. Troca de provedor no meio de um turno (ElevenLabs caindo para o Pocket) **reinicia o planejamento** em vez de costurar.
5. Textos sem nada dizível ou não alinháveis: "the mouth follows the audio alone, and the plan says why" — degradação declarada.
6. Há avaliação offline com métricas nomeadas (`lib/lipsync/eval/metrics.ts`): `vowelOpen`, `openInSilence`, `nonspeechOpen`, `corr`/`lagMs` (melhor lag em ±250 ms), `vowelMatch` (ja/ko/zh/es) e `tagIous`, com fixtures congelados (`testset.json`, linhas `heldOut: true` reportadas à parte) e referência vinda de forced alignment (`reference.ts`), tudo a **60 FPS**. Os números deles, marcados `(M)` no plano: *vowel match 48 %*, *open in silence 0 % (inglês) / 4 % / 8 %*, *4 de 8 tags posicionadas*, *conversores < 0,01 ms por segundo de áudio*, *alinhamento ~3 ms por segundo de áudio* (2,8 ms em 4 s, 4,3 ms em 11–13 s). **Medidos por eles, em Node, não aqui.**

## 8. Desempenho na máquina da Lia (área 6): estimativas rotuladas, jamais medidas

**O que não pode ser afirmado:** nada executado aqui. Este sandbox não tem Windows, não tem GPU, não tem `pnpm install`, não tem Chromium com WebGL2 e não tem Unity. As perguntas "roda na RX 580?", "e junto com um jogo?" ficam `BLOCKED`, e o hardware da Lia está registrado em `cross-project/hardware/WINDOWS-AMD-COMPATIBILITY.md` (`LR-HW-001`: Windows 11 x64 · RX 580 8 GB Polaris/gfx803 · Ryzen 5 5500 · 16 GB) e `cross-project/hardware/RUNTIME-RESOURCE-RESEARCH.md` (`LR-HW-002`).

O que o repositório entrega de útil são **números deles + o instrumento**. A tabela abaixo é a base mais sólida que existe hoje para responder a pergunta — e cada linha diz de onde vem:

| Fato medido *por eles* | Valor | Por que importa na Lia |
|---|---|---|
| Custo de MSAA em canvas de avatar (issue #660, Apple M5, Chromium headless, ANGLE Metal, `footprint` do processo de GPU, avatar Annie carregado) | 1440×900 @DPR 2: **523 MB com MSAA / 362 MB sem** · 1440×900 @1×: 313/264 · PiP 210×280 @DPR 2: 250/238. Canvas vazio economiza os mesmos 161 MB → a economia **é o buffer de multisample** e cresce com a área. Loop síncrono render+readback: 3,0 → **2,1 ms/quadro** | a regra "pedir `antialias` só abaixo de DPR 2" cabe em qualquer canvas. Na Lia, um PiP pequeno paga pouco; um Stage 1080p com MSAA ligado é o que dói — **numa placa de 8 GB compartilhando com um jogo, o peso relativo é maior que num M5 de 192 GB unificados, e isso é aritmética, não medida** |
| Custo de decodificar thumbnail em servidor (issue #712, Pillow 12, macOS, um processo novo por decodificação) | crescimento de pico: 12 MP JPEG **95 MiB** · 40 MP JPEG 306 · 4096×4096 RGBA PNG 194 · 16 MP RGBA WebP 309 · 40 MP RGBA PNG **448 MiB**; e o motivo: `ImageOps.exif_transpose` faz uma segunda cópia em tamanho cheio antes de reduzir | numa máquina de 16 GB, um backend que decodifica N imagens concorrentes em worker threads pode estourar só com isso. A correção (limitar a memória do decode) entrou como `perf:` |
| STT "recomendado = GPU" tem custo de peso | `models/parakeet-tdt-0.6b-v2-webgpu/manifest.json`: **1 arquivo de 1.238.962.105 B (1.181,6 MiB) em FP16**, contra o conjunto CPU de 7 arquivos somando **661.332.409 B (630,7 MiB)** INT8; SenseVoice: CPU 239.563.552 B (228,5 MiB) INT8 vs WebGPU 937.619.109 B (**894,2 MiB** FP32) | "WebGPU recomendado" significa pedir ~1,2 GiB de VRAM. Em gfx803 com `fp16` não verificado (`LR-HW-001` §2-3, regra "detectou ≠ rodou rápido"), o caminho GPU do Animama é exatamente o que a Lia não deve prometer a si mesma. **Eles não mediram em Radeon; nós também não** |
| TTS local no navegador | `docs/…/voice-and-speech.md` + issue #901: Pocket roda **em uma thread WASM** porque "the app is not cross-origin isolated (#128)"; a estratégia `adaptive` decide no 2º chunk e, se a síntese for mais lenta que o tempo real, **troca para `buffer_all` e não toca nada até gerar a resposta inteira**; relato de usuário: "Pocket TTS takes 20–30 seconds before it starts speaking"; reproduzido confinando o renderer a efficiency cores (taskpolicy) | é o cenário de pior caso da Lia: CPU de 6 núcleos + jogo rodando = síntese abaixo de tempo real → silêncio proporcional ao tamanho da resposta. Estimativa *nossa*, explicitamente não medida: uma resposta de ~60 palavras ≈ 30 s de áudio; se a síntese ficar a 1,5× o tempo real, o primeiro som sai ~45 s depois — **aritmética sobre o mecanismo documentado, com o fator 1,5 escolhido por nós; não é benchmark** |
| Custo de bundle de runtime | issue #782: uma visita a um Anima inicial move **~52,5 MB** | o número que define o piso de cache HTTP local. Detalhe valioso: a investigação concluiu que **não havia defeito de produto** — o cache de um contexto Playwright off-the-record são 2 % da RAM, máx. 50 MB, com LRU, então as respostas mais antigas evapunham antes da próxima visita |
| Orçamento de distribuição | `src/frontend/desktop/runtime/size-budgets.json`: core **786.432.000 B** de download e **1.610.612.736 B** instalado; pack `expanded-included-content` 524.288.000 B instalado; regressão > **5 %** é exceção; `size-exceptions.json` e `size-approvals.json` **ambos vazios** ("no exception is granted") | é um teto de *bytes de instalação*, não de FPS. Serve como forma de escrever "quanto esta presença pode pesar" com número e aprovação por exceção |

Suspensão/ociosidade, o que foi lido: o documento `docs/frontend/desktop/picture-in-picture.md` afirma que, com o PiP nativo ativo, "the main window keeps the app shell and runtime producer mounted but **suspends its own scene render**. This avoids drawing the avatar twice"; o `quick-chat` liga `backgroundThrottling: false`; e o app aceita `--disable-gpu` como diagnóstico (`troubleshooting.md:76`), com a consequência escrita: "the app works, but the avatar needs WebGL and does not render". **Não encontrei** política de FPS máximo, `powerSaveBlocker`, corte por foco de janela nem modo "economia" — procurei por `maxFps|frameRate|powerSave|throttle|occlusion|suspend` no código do main process e não há. O que existe de economia é: render suspenso quando o PiP assume, URL de conteúdo imutável por digest para não revalidar (ADR 0033), e o cache de prompt por layout (§7).

Limites conhecidos, declarados por eles (não por nós): Intel Mac, universal Mac, Windows ARM e Linux não têm release autocontido (`docs/frontend/desktop/installation.md`); "PCs limited to Windows 10 often have older graphics hardware, where Avatar rendering can be slow; performance there is best effort"; o app empacotado atual do Windows 0.1.6 **só instala em Windows 11 build ≥ 22000** (builds a partir do código atual voltam a aceitar 10 22H2); a #928 (aberta) é um furo de primeira instalação em Windows; a #922/#920/#906 pedem Linux sem resposta de release; e um comentário no vídeo do autor: "performance is terrible, needs some optimizations" (4 curtidas), ao qual o mantenedor responde perguntando se era o demo web ou o app, nuvem ou modelo local — **isso é relato, não evidência, e registro aqui para não parecer omitido**.

## 9. Licenças por componente (área 8) — e o motivo de isto ser o achado mais forte

Três camadas que **não devem ser confundidas**, todas medidas:

1. **O produto é AGPL-3.0-only** (`LICENSE` de 34.020 B na raiz; `pyproject.toml` `license = "AGPL-3.0-only"`), com CLA explícito (`.github/CLA.md`, ADR 0037) para que contribuições externas entrem sob o mesmo termo. Consequência para a Lia, escrita sem ambiguidade: **nada daqui entra como dependência de um produto Lia nem como código copiado** sem acionar as obrigações do copyleft de rede. É um motivo suficiente para a classificação `REJECT` na incorporação e `REFERENCE_ONLY` no resto — é uma decisão sobre o *que a Lia faz com o código*, e a Licença da própria Lia não muda por causa disto.
2. **Os ativos não são AGPL, e eles dizem isso no texto.** `licenses/third-party/code-and-models.md:17` fecha o parágrafo do Pocket TTS com "These assets are not AGPL"; a linha do SenseVoice repete; `pyproject.toml` carrega `license-files` com os textos de Letta (Apache-2.0) e do OpenAI Agents SDK (MIT) **dentro da wheel**; e há termos que nem licença de código são: `LicenseRef-pixiv-VRoidPreset` em 128 arquivos, FunASR Model License 1.1 em 5 (uso/modificação/compartilhamento exigem atribuir fonte, autor e manter o nome do modelo), CC BY 4.0 nos pesos, "MIT (unmodified upstream mark); the provider's trademark rights are not licensed" em 11, e o pacote de motions Mixamo como conteúdo **non-portable** (ADR 0018: toca, pré-visualiza, equipa; não sai do app, não é exportável, e "identical bytes stored anywhere are restricted too"). O retrato Lapwing citado no `README` vem de um item de BOOTH (©kuji), com review do dono registrado em `licenses/third-party/art-vroid-review.json`.
3. **O inventário é por arquivo e é um gate de CI.** `licenses/source-review.json` (schema `animama-source-license-review/1`, `reviewed_on 2026-11-03`) tem **5.953 entradas** — exatamente o número de blobs da árvore — com os campos `path`, `candidate_license`, `basis`, `copyright`, `review`; `basis` menciona a atestação do autor em 4.478 entradas e algo diferente (origem terceira mapeada) em 1.475; e **as 5.953 entradas têm `review = "prepared-not-release-approved"`**. `scripts/public-release/check_source.py` falha se um arquivo rastreado não tiver exatamente uma entrada, se uma entrada apontar para arquivo morto, se faltar campo, se uma licença estiver `pending` ou se um caminho de estado privado estiver rastreado. `licenses/README.md` avisa, na cara: "they are not forensic certification that no external influence exists".

Executado por nós (é o `LOCAL_TESTS_PASS` do cabeçalho): `python3 scripts/public-release/check_source.py` → `licenses/source-review.json covers every tracked file exactly once.` e `python3 -m unittest discover -s scripts/public-release` → **12 testes, OK, 0,139 s**. Duas notas de método que saíram da execução: (a) o script é puro `git ls-files` + JSON, sem dependências, por isso roda em qualquer lugar — um gate que precisa de `uv sync` não é um gate, é um trabalho; (b) ele usa `git ls-files` **sem** o `--sparse`, portanto funciona em checkout esparso, o que é raro e vale anotar.

A camada de **bibliotecas** é uma quarta coisa, separada das três acima: `three ^0.182.0`, `@pixiv/three-vrm ^3.5.5`, `three.quarks ^0.17.1`, `@mochiya/three-liltoon 0.1.9`, `onnxruntime-web 1.24.2` etc. são MIT/Apache do upstream delas; o fato de o Animama ser AGPL não contamina nada disso, e o inverso também é verdade. Nosso próprio `cross-project/licensing/SPLIT-LICENSE-SCAN.md` (formato I) trata exatamente desse caso.

## 10. Limitações e dívidas que a leitura mostrou

- **Duas validações do mesmo formato** (Python e TypeScript), assumidas no docstring como "Mirrors" — risco clássico de derivação, e o custo de mudar o formato é 2×.
- **Histórico público começa num repo split**: `repo-split/initial-2026-09-08` é a única tag, os dois primeiros commits são "Repo Split", 0 releases no GitHub. Toda prova de origem precisa de ref/commit (que é o que este dossiê faz) e, para os instaladores, de `downloads.animama.ai` com checksums — que **não** verificamos.
- `review: prepared-not-release-approved` em 5.953/5.953 entradas: **nenhum arquivo está aprovado para publicação**; a própria licença do repo é "publicado como está" (#823, D2).
- O `local-http` é `25.0.0` gerado offline (`contracts/versions.json`): o contrato HTTP existe e é versionado, mas não é assinado publicamente — quem consome a API gera o cliente (`pnpm openapi-ts`) e a regeneração é instruída no documento.
- **Nada de multiusuário por design** (ADR 0002: um principal de instalação gerado no schema; "Accountless does not mean requests can select an owner"; expor para outra máquina exige o operador trazer TLS+auth). Se a Lia quisesse a mesma presença em mais de um usuário, essa é a decisão que ela teria de refazer.
- A seleção de gesto depende do modelo acertar um `selector` entre 140; o repositório mede isso em avaliação, mas **não** há queda-para-"sem-gesto" aprendível: gesto inválido é descartado com motivo.
- A base de usuários medida em números duros é pequena: 119 ★ / 13 forks / 16 issues (duas de release, várias de plataforma) — maturidade de código alta, maturidade de comunidade baixa.

## 11. O que serve para a Lia, por mecanismo (não por código)

Classificação no padrão desta base. `ADAPT` = vale levar o mecanismo, escrito pela Lia; `REFERENCE_ONLY` = guardar como precedente documentado; `INDEPENDENT_REIMPLEMENTATION` = a peça é pequena, fechada e vale fazer do zero; `REJECT` = não incorporar.

| # | Achado | Fonte primária | Maturidade | Classificação | Produto |
|---|---|---|---|---|---|
| F1 | `animaPoseClip/2.0`: beats + trilhas anatômicas em graus, 2 MiB, decimais fixos, mãos por preset, pés resolvidos no rig | `clip_format.py:19`, `clipVocabulary.ts:35-52`, ADR 0014/0016/0019/0020, `wave-hello.json` | aceita e única; 1.0 rejeitado; 320 itens produzidos com ela | **ADAPT** (o formato em si é deles; a ideia de "curva por junção em graus, agrupada em beats nomeados, com `generated detail`" é o que se leva) | Forge, Studio |
| F2 | CLI de autoria com verificação determinística (range/interseção/contato ≤1,5 cm/oscilação >4 Hz) e promoção a conteúdo incluído só com aprovação por item **e** por licença | `motion-authoring/cli.ts`, `checks.ts`, `.agents/skills/animama-animation/SKILL.md` passos 3–4 e 9 | 21 skills, cada script com `.test.mjs` ao lado | **ADAPT** | Forge, Studio, Agent Hub |
| F3 | VRM como contêiner + capacidade facial detectada por nome de morph target (tolerante a ARKit/SRanipal/Unified Expressions) + classificador semântico de spring bones | ADR 0032, `arkitFaceCapability.ts`, `spring-bone/SpringBoneSemanticClassifier.ts` | decisão com data e dono (2026-10-24, #687) | **ADAPT** para a detecção por nome; **REFERENCE_ONLY** para a decisão de contêiner | Forge, Studio |
| F4 | Otimizador VRM caseiro que **recusa** extensões desconhecidas e documenta "what it must never do"; paridade lilToon por render (`liltoon-parity.mjs`) | `docs/frontend/runtime/vrm-optimization.md` (112 linhas), scripts `vrm:optimize`, `avatar:parity-render` | usado para gerar o conteúdo incluído e toda conversão VRChat | **ADAPT** (o padrão: otimizador próprio + lista do que é proibido + verificação por PSNR `--min-psnr 45`) | Forge |
| F5 | Instrumento de custo de quadro em GPU (`EXT_disjoint_timer_query_webgl2`) com varredura de DPR/materiais, e a regra MSAA-abaixo-de-DPR-2 | `web/scripts/effect-bench.mjs`, issue #660 (medida em M5) | no repo, com CLI e JSON de saída | **ADAPT** como método; **NEEDS_VALIDATION** para qualquer número na RX 580 → nesta base `INSUFFICIENT_EVIDENCE` | Project, Model Lab |
| F6 | Emoção: estado persistente por canal 0–30, grupo derivado, escala dupla (estado vs representação), promover/rebaixar em par oposto | `domain/emotions.py`, `primary_emotion_update.py`, `avatar-emotion.md` | invariante declarado e com regras de edição (§4 do doc) | **REFERENCE_ONLY** (a Lia não tem estado emocional; isto é um precedente, não uma recomendação de design) | Project |
| F7 | Memória: `remember` dentro do reply estruturado, projeção diária Markdown gerada de tabela no banco, limites de injeção numéricos, Reflexão só com disparo humano, versões + recebimento idempotente | `memory.md`, `memory-manager-and-episodic-memory.md`, ADR 0004/0009/0034 | em produção nos dois backends; hosted sem automação | **ADAPT** como pergunta de viabilidade para o Project (não como instrução) | Project, Agent Hub |
| F8 | Banco de modelos com **teto de gasto** (`--max-calls --max-usd`), ensaio grátis contra mock (`ANIMAMA_LLM_SKIP=1`) + juiz stand-in, juiz humano-cego com calibração (`export/import/pilot/waive`), `plan` como dry-run de tokens/custo/tempo, e `cleanup` | `docs/benchmarks/README.md`, `scripts/evals/` | documentado como fluxo completo, com issue-mãe #470 | **ADAPT** | Model Lab |
| F9 | Layout de prompt por provedor **para cache**, com harness que proíbe piorar a taxa de cache em qualquer caminho | `docs/backend/runtime/prompt-caching.md:1-34`, `tests/live/test_prompt_cache_layout.py` | opt-in, mas existe e é obrigatório em mudança de layout | **ADAPT** | Project, Model Lab |
| F10 | Parser incremental de JSON de campo único que permite **falar antes de o objeto fechar**, com parse final autoritativo e descarte justificado de gesto inválido | `main_structured_response.py:159-500` | em uso no caminho quente de chat | **INDEPENDENT_REIMPLEMENTATION** (peça pequena e fechada; fazer do zero evita qualquer leitura de licença) | Project, Studio |
| F11 | Vault de credenciais no desktop com a armadilha do Windows resolvida: esperar a chave do Chromium aparecer em `Local State` antes de criar o cofre (senão o cofre fica ilegível) | `desktop/src/main-process/runtime/vault.ts:24-49` + `recovery.ts:169` | comentado com o motivo e com `safeStorage` assíncrono (Electron 45 depreca o síncrono, 46 o remove) | **ADAPT** (a armadilha vale como nota de plataforma mesmo que a Lia use outro mecanismo) | Project |
| F12 | Inventário de licença por arquivo + gate de cobertura no CI + "assets are not AGPL" + `license-files` na wheel + conteúdo non-portable com regra no inventário | `licenses/README.md`, `source-review.json` (5.953 entradas, 10 valores), `check_source.py`, ADR 0018 | roda, passa, e falha fechando | **ADAPT** | Research, Agent Hub |
| F13 | Processo SPECS/PLANS/SDLC/AGENTS/GLOSSARY com 41 ADRs, revisão por tier de risco (ADR 0027), CI "Portable product validation" com checkout sem hidratar ativos e dependências congeladas | `SPECS.md`, `PLANS.md`, `SDLC.md`, `docs/adr/0006/0027`, `.github/workflows/validate-public.yml` | o processo é o produto mais maduro do repositório | **ADAPT** para esta base (a `RESEARCH-*` já faz uma parte); REFERENCE_ONLY para os demais | Research |
| F14 | Incorporar código, ativos ou pesos do Animama em qualquer projeto Lia | §9 (AGPL-3.0-only + ativos não-AGPL + `prepared-not-release-approved` em 5.953/5.953) | — | **REJECT** (como incorporação; não como leitura) | todos |

Nenhuma linha acima é autorização de implementação: é recomendação de pesquisa, e a decisão é do dono de cada projeto.

## 12. Evidências

**Executado por nós** (o único trecho `TESTED` deste dossiê):

| Comando | Onde | Saída |
|---|---|---|
| `python3 -B scripts/public-release/check_source.py` | clone em `4ba6db1c` | `licenses/source-review.json covers every tracked file exactly once.` · exit 0 |
| `python3 -B -m unittest discover -s scripts/public-release -p "test_*.py" -v` | idem | **Ran 12 tests — OK — 0,139 s** |
| `gh api repos/raymond-van/animama/git/trees/HEAD?recursive=1` | API | 7.125 entradas, `truncated: false` |
| `git log --oneline \| wc -l` / `git log --format="%an" \| sort \| uniq -c` | clone | 2.353 commits · Raymond Van 2.021 + Ray 313 + Raymond 14 + Claude 4 + split 1 |
| `gh api repos/raymond-van/animama/{releases,tags,contributors}` | API | 0 releases · 1 tag `repo-split/initial-2026-09-08` · `raymond-van:2348`, `claude:4` |
| `gh api "…/contents/src/frontend/web/package.json?ref=4ba6db1c…"` | API | versão exata das dependências de render |

**Trechos literais que sustentam as afirmações fortes** (arquivo:path medido no clone):

- `src/backend/animama/domain/emotions.py:13-19` — `EMOTION_MIN_VALUE = 0`, `EMOTION_MAX_VALUE = 30`, `EMOTION_PROMOTION_BUDGET = 5`, `EMOTION_DEMOTION_BUDGET = 3`, `EMOTION_PROMOTION_LIMIT = 3`, `EMOTION_DEMOTION_LIMIT = 2`.
- `src/backend/animama/app/primary_emotion_update.py:44-69` — as duas escalas de intensidade, com as docstrings "1-3 shifts by 1, 4-6 by 2 and 7-10 by 3" e "1-2 plays none, then 3-4, 5-6, 7-8 and 9-10 select intensities 1-4 (Mild, Moderate, Strong, Intense)".
- `src/backend/animama/app/services/clip_format.py:1-33` — formato único, rejeição sem conversão, e a frase do comentário "Fixed package-import reason: the HTTP boundary never echoes submitted data".
- `src/backend/animama/app/main_structured_response.py:469-478` — a ordem de campos e por que a fala só sai depois do gesto estar completo.
- `src/backend/animama/app/services/idle_clip_validation.py:440-446` — "Mirrors the frontend `validateAnimaPoseClipV2`… Times are compared in the 0.1 ms ticks a saved file holds".
- `src/frontend/web/src/lib/lipsync/planner.ts:1-17` — planejamento progressivo, limite de 2 s, custo "about 2 ms a call for a two-minute part, in Node".
- `src/frontend/web/src/lib/lipsync/eval/metrics.ts:1-16` — as métricas e "These follow the research brief's scoring (`docs/plans/lipsync-upgrade/`)".
- `src/frontend/web/src/lib/avatar/arkitFaceCapability.ts:3-14` — a normalização de nomes de morph target.
- `src/frontend/desktop/src/main-process/runtime/vault.ts:24-49` — `awaitDurableEncryptionKey`, o `Local State`/`os_crypt` escrito ~10 s depois do start, timeout 30 s, espera de 250 ms.
- `src/frontend/desktop/src/main-process/pip/pip-window-manager.ts:508,995` — `transparent: true` e `setIgnoreMouseEvents(true, { forward: true })`.
- `docs/adr/0014-track-based-anima-pose-clips.md:20-26` — "about 100 times the size of their curves, about 8 s of busy motion within the 2 MiB clip limit, and 60–250 keyframes that cannot be edited".
- `docs/adr/0032-vrm-container-with-arkit-face-shapes.md:12-19` — "Every Avatar subsystem sits on three-vrm… An FBX export holds none of the Unity humanoid mapping, PhysBones or lilToon material settings".
- `docs/adr/0004-filesystem-content-and-recoverable-mutations.md:22-33` — "Filesystem and database changes do not share a literal transaction… Journals are recovery evidence, not disposable caches".
- `docs/frontend/desktop/size-decisions.md:1-19` — tetos + `size-exceptions.json`/`size-approvals.json` + "Missing or malformed approval evidence fails closed".
- `docs/backend/features/memory.md:38-49` — os limites de injeção (`16 KiB`, `20 notas`, `3.000 caracteres`, `14 dias`) e a regra de parar antes da nota que estouraria o orçamento.
- `docs/frontend/desktop/installation.md:24-29` e `troubleshooting.md:71-78` — melhor esforço em GPU antiga e `--disable-gpu`.
- `.env.example` (via API, `?ref=4ba6db1c`) — credenciais em arquivo externo ao checkout; `dev-tools` desligado por padrão, "Bind addresses are fixed at 127.0.0.1", "never publish these tools through a public tunnel/proxy".

**`DOCUMENTED` — dito por eles, não verificado por nós:** as capacidades do `README.md`/site, todo o `docs/animama.ai` (não aberto), as transcrições do vídeo, os números de #660/#712/#901/#782 (medições relatadas em issue, em hardware deles), e os 41 ADRs cujos textos completos não foram lidos um a um (12 foram).

`BLOCKED` / não executado: qualquer coisa que exija Node build, navegador com WebGL2, GPU, Windows, Unity, PostgreSQL/Docker, ou baixar 1,2 GiB de pesos. `Evidência` correspondente: `OBSERVED` para o que li em arquivo, `REPORTED` para issue/docs, `BLOCKED` para execução.

## 13. Ponteiras para a próxima rodada

1. Rodar `pnpm -s effects:bench` **na máquina da Lia** é a única coisa que transforma §8 em medida; o instrumento já existe e tem `--json`. Sem isso, nada aqui sai de `DOCUMENTED`.
2. `docs.animama.ai` tem as páginas que o repo não tem (`/self-host`, `/emotions`, `/behaviors`, `/voice`, `/effects`, `/configuration`) — ainda não lidas; são o lugar onde "24 emoções" e "300 gestos" viram contrato de produto.
3. Verificar os checksums publicados em `downloads.animama.ai` e amarrar `0.1.5`/`0.1.6` a um commit (hoje não há release no GitHub; é a mesma regra `§5` da nossa política de proveniência).
4. Ler `SDLC.md` por inteiro (428 linhas; li 4 em 7 blocos) e `docs/adr/0027` + `0006` para tirar a política de revisão por tier sem inventar.
5. Contar o corpus de skills do Animama **no** censo de `LR-CMP-004` (187 `SKILL.md` contados em 2026-11-25 em outro conjunto; os 21 daqui são `AGPL-3.0-only` e mudam a resposta de "quantos skills têm licença ao lado do arquivo": aqui são 0, pois a licença está no inventário por arquivo).
6. Ver se `pocket-tts-attribution.txt` lista mesmo todas as vozes e se os 4 nomes CC0 sobrevivem — é o único caso no repositório em que um **dado derivado de voz humana** tem cadeia de licença própria.

## 14. Como isto se liga à base

- **Não duplica** o que já existia: os dossiês vizinhos são `repositories/charakuru/REPORT.md` e `repositories/hairdeck/REPORT.md` (ativos VRM/cabelo, sem companion, sem memória, sem formato de animação) e `cross-project/character-creation/LIVE2D-MOTION-AUTHORING-RESEARCH.md` (2D; a lição "o padrão, não o código" é a mesma que F1/F2 reforçam em 3D).
- **Alimenta** `LR-HW-002` com o instrumento e com a pergunta certa (custo de render não é só do modelo), e confirma `LR-HW-001` no ponto "fp16/WebGPU não é caminho principal": o caminho GPU do STT deles pede 1,2 GiB de pesos.
- **Corrobora** a regra de ouro de `LR-AGENT-007` (léxico antes de vetor) com uma implementação independente que levou embeddings a papel opcional; registrar isto não altera nenhuma decisão da Lia.
- Entra em `comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md` (`LR-CMP-005`) com a matriz de 5 projetos, o dicionário dos seis rótulos do dono e as classificações por achado.
- A camada de licença (F12/F14) é material direto para `cross-project/licensing/SPLIT-LICENSE-SCAN.md` e `READY-TO-USE-LICENSES.md`, já atualizados com esta rodada.
