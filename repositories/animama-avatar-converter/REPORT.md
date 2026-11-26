# animama-avatar-converter — 98 blobs, MIT, zero dependências no npm: quem faz o VRChat→VRM é o Mochiya, e o valor deste repo é o invólucro (validação, reparo de ossos, CLI que dirige o Unity sem `-nographics`)

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-024` |
| Nome | `raymond-van/animama-avatar-converter` — "Export a VRChat Avatar you own to a VRM file for Animama, from Unity or the command line. Runs locally; uploads nothing." |
| Tipo | repositório (pacote UPM do Unity **e** comando npm, no mesmo repositório) |
| Licença | **MIT** (raiz, 1.068 B, e uma cópia dentro do pacote UPM). Dependências de terceiros, todas por URL Git com pin: UniVRM `v0.131.2` (MIT) para `com.vrmc.gltf`/`com.vrmc.vrm` e **Mochiya Avatar Tools no commit `0826f6e3e453ac1885d6594b831181655c4a1b5c`** (MIT). O pacote npm tem **zero dependências** (`dependencies: undefined`, 8 arquivos, 41.414 B descompactados). O avatar convertido não herda nenhuma dessas licenças: o `README` abre com "Convert only an Avatar whose licence allows it, and share the VRM only if the licence allows that too" |
| Fonte oficial | https://github.com/raymond-van/animama-avatar-converter · npm `animama-avatar-converter` · listing VPM `https://raymond-van.github.io/animama-avatar-converter/index.json` |
| Responsável | `raymond-van`, contribuidor único (32 contribuições em 32 commits) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | LOCAL_TESTS_PASS — `npm test` executado aqui: **46 testes, 46 passaram, 0 falharam** (Node v22.22.3, ~475 ms) e `npm run check` → `OK: version 0.1.1, 82 package files and folders, 36 sources checked.` **Nenhuma conversão foi executada**: exige Unity 2022.3 com projeto VRChat, GPU e Windows/macOS — nada disso existe neste sandbox (`BLOCKED`) |
| Recomendação | **REFERENCE_ONLY** para a ferramenta (não há pipeline VRChat na Lia); **ADAPT** para quatro práticas de invólucro listadas em §7 — e a licença MIT permite lê-la e reimplementar o padrão sem risco |
| Decisão de adoção | — nenhuma registrada |
| Categoria | pipeline de ativo 3D (VRChat/Unity → VRM) + empacotamento bilingue (UPM + npm) |
| Projetos beneficiados | Lia Forge (ingestão de ativos de terceiros e o padrão "valida antes de escrever"), Lia Agent Hub (empacotamento e listing com verificadores sem dependência), Research (a checagem estática de "não fala na rede") |
| Versão analisada | `main` @ `0b24f4e61f236aac9e76716520e78e428abb7e6f` (2026-11-07T20:03:50Z) = tip da branch padrão · **2 releases** (`v0.1.1` com asset de 60.924 B, 9 downloads; `v0.1.0` com 49.240 B, 3 downloads) · pacote npm `0.1.1` · `pushed_at 2026-11-25T19:36:49Z` (pushes posteriores estão em branches, não na `main`) |
| SHA completo | 0b24f4e61f236aac9e76716520e78e428abb7e6f |
| Proveniência do SHA | **medido por nós**: `gh api repos/…/commits?per_page=3` batendo com `git rev-parse HEAD` do clone de 2026-11-26 |
| HEAD atual | 0b24f4e61f23… (o analisado é o tip da `main`) |
| Proveniência do conteúdo | clone completo (`--filter=blob:none`, sem LFS), leitura direta de `README.md` (294 linhas), `RELEASING.md`, `LICENSE` (1.068 B), dos 4 `.asmdef`, dos 26 `.cs` (3.152 linhas) e dos 16 `.mjs`; censo da árvore pela API com `truncated: false`; `gh api` de releases/tags/branches/issues/contributors; `registry.npmjs.org` para metadados do pacote. **Nenhum asset de avatar, nenhum `.unitypackage`, nenhuma dependência instalada** |
| Data | 2026-11-26 |
| Última verificação | 2026-11-26 · clone + `npm test` + `npm run check` + API |
| Upstream conferido | **2 ★** · 0 forks · 1 issue aberta (`#4 feat: convert MMD (PMX) models to VRM 1.0`) · `license: MIT` · `language: C#` · `size_KB 277` · **111 entradas / 98 blobs / ~0,3 MB** · 32 commits · 12 branches (5 delas só de README: `docs/readme-per-os`, `docs/readme-numbered-steps`, `docs/readme-os-headings`, `docs/readme-humanoid-models`, `docs/readme-unity-setup`) · criado 2026-11-02 |
| Confiança | Alta em estrutura, contratos, limites declarados e no que o `check.mjs` verifica (executado). Nenhuma sobre o resultado de uma conversão real — é justamente o que só o Unity entrega |
| Próxima revisão | 2027-01-10 |

---

## 1. O que é, em uma linha e meia

Não é um conversor. É um **invólucro de qualidade** em volta do `MochiyaConverter` (Mochiya Avatar Tools), com três peças próprias ao redor: um verificador de pré-requisitos (`Requirements.cs`, 231 linhas), um **reparador de esqueleto** (`HumanoidBoneRepair.cs`, 352 linhas) e um **orquestrador de linha de comando** (`cli/*.mjs`, 10 arquivos) que sabe achar o editor Unity certo, abrir o projeto em batch mode e interpretar o resultado. Quem faz o glTF/VRM de verdade é o Mochiya; quem decide se o resultado é confiável é este repo.

Isso importa para a classificação: adotar *este* repositório seria adotar o invólucro e ter de comprar Unity 2022.3 + VCC + lilToon + um projeto VRChat. Adotar o *padrão* custa algumas horas.

## 2. Números que falam sozinhos

| Medida | Valor |
|---|---|
| blobs / bytes totais | 98 / ~0,3 MB |
| distribuição por extensão | 41 `.meta` · **26 `.cs`** · **16 `.mjs`** · 4 `.md` · 4 `.asmdef` · 2 `.yml` · 2 `.json` · 3 sem extensão |
| bytes por área | `Packages` 159.333 · `cli` 62.684 · `scripts` 15.774 · `README.md` 10.311 · `.github` 4.858 · `LICENSE` 1.068 |
| linhas de C# | **3.152** em 26 arquivos |
| testes C# (EditMode/NUnit) | 5 arquivos, **55 métodos `[Test]`** (AvatarExporter 17 · ExportWindowLogic 14 · HumanoidBoneRepair 13 · Requirements 11) — **39 % das linhas de C# são teste** (1.240 de 3.152) |
| testes JS | 6 arquivos `*.test.mjs` cobrindo args/main/prefabs/project/unity + listing; **46 testes, todos passando** (executado aqui) |
| dependências do pacote npm | **zero** |
| assets publicados | 1 zip por release (60.924 B no `v0.1.1`), 9 downloads |
| verificação estática própria | 82 arquivos/pastas do pacote e 36 fontes vistoriados por `scripts/check.mjs`, exit 0 |

## 3. Como funciona, do clique ao `.vrm`

Do texto XML-documentado em `Editor/Export/AvatarExporter.cs:16-21`, lido integralmente:

> "Each run instantiates the prefab in a temporary scene, strips EditorOnly objects **as a VRChat build does**, maps humanoid bones that move nothing to the bones the mesh follows (`HumanoidBoneRepair`), poses the humanoid T-pose (unless `ExportOptions.KeepPose`), then runs Mochiya's Detect, Validate and Export. The source prefab and the user's scenes are left unchanged. The VRM is written beside the target **under a temporary name and moved into place only when complete**; an existing file is never overwritten. Nothing is uploaded."

Detalhes que só aparecem lendo:

- `MoveAttempts = 5` / `MoveRetryMilliseconds = 200` — o "move into place" tem retry, porque o VRM recém-escrito ainda pode estar com handle aberto (Windows).
- `ExportBlockers.Find(...)` devolve a lista **ordenada** de motivos pelos quais o botão está desabilitado ("Fix the requirements above first.", "Exit Play Mode first.", o problema da fonte, Modular Avatar, caminho de saída inválido) — a UI e o batch mostram o mesmo texto, não há duas explicações.
- `ModularAvatar.FindComponent` detecta pelo **namespace** `nadena.dev.modular_avatar` varrendo `GetComponentsInChildren<MonoBehaviour>(true)` e lendo `GetType()`, para que o pacote não precise referenciar Modular Avatar: quem precisa de build step é **recusado**, não convertido pela metade.
- `MochiyaConverter` (43 linhas) diz no docstring: "Mochiya Avatar Tools' local Detect, Validate and Export. **Never calls its upload workflow.**" — a API do Mochiya tem upload, e o invólucro não a expõe.
- `Requirements` tem três estados (`Met` / `Missing` / `Unsupported`) — "versão errada" não é "ausente", o que muda a mensagem.
- `HumanoidBoneRepair` resolve um defeito real do ecossistema VRChat: avatares que mapeiam ossos humanoides para *dummy bones* sem skin (`Thumb1Dummy`–`Thumb3Dummy`) enquanto a malha segue `Thumb1`–`Thumb3`; o reparo remapeia e **lista no relatório** o que remapeou, e se não houver osso-alvo, **nomeia os ossos cujo movimento não vai aparecer**. É o oposto de corrigir em silêncio.

CLI (`cli/*.mjs`, lido o essencial de `project.mjs` e `unity.mjs`):

| Mecanismo | Evidência |
|---|---|
| Pins das dependências por URL Git + tag/commit | `cli/project.mjs:15-22` — `UNIVRM_VERSION = "0.131.2"`, `MOCHIYA_COMMIT = "0826f6e3e453…"`, e o próprio pacote por `…animama-avatar-converter.git?path=/Packages/com.animama.avatar-converter#v${version}` (`:25-27`) |
| Detecção de conflito antes de mexer no `manifest.json` | `:42-46` aceita apenas a versão/commit exatos; `:128-132` calcula `added` e `conflicts`, e "An installed UniVRM for VRM 0.x must move to UniGLTF's version too" |
| Tolerância ao jeito errado de instalar | `:49-51` conhece os `.asmdef` que uma cópia manual do `.unitypackage` deixa em `Assets/` (UniGLTF.asmdef, …) e os trata como o problema que são |
| Batch mode com códigos de saída tipados | `cli/unity.mjs:9-13`: `CANNOT_CONVERT = 2`, `NOT_READY = 3`, e os métodos `-executeMethod Animama.AvatarConverter.BatchExport.Validate\|Export` com `-animamaPrefab/-animamaOut/…` (`BatchExport.cs:4-12`) |
| **A armadilha do `-nographics`** | `cli/unity.mjs:1-4`: "Unity runs **with graphics, never `-nographics`**: the exporter reads compressed textures back through the GPU and writes flat grey placeholders without one." |
| Log do Unity preservado | README: "Unity's log is saved beside the VRM as `<Avatar name>.export.log`" |

## 4. O que preserva e o que não preserva (pergunta explícita do dono)

Do `README.md:204-224`, na ordem em que eles listam, com o comentário técnico que cabe em cada um:

| Item | Situação | Leitura técnica |
|---|---|---|
| Esqueleto humanoide | preservado, com reparo | o remapeamento de dummy bones (§3) é exatamente o que faltaria em avatares de terceiros |
| Forma facial (blendshapes) | **preservada por nome** | o `README` não promete; quem consome é o Animama: ADR 0032 diz que "morph target names survive a VRM conversion unchanged" e o runtime detecta ARKit pelos nomes. É por isso que o conversor pode ignorar expressões VRM preset |
| Expressões VRM / ARKit | não gera | "Other Unity humanoid models convert too, but **without a VRChat avatar descriptor the VRM has no lip sync, blinking or eye movement**" — a origem do dado é o `VRCAvatarDescriptor`, não o modelo |
| Toggles e gesture expressions do Animator | **não passam** | "Animama drives the face itself" — decisão de produto a montante, não limitação técnica |
| PhysBones → VRM springs | aproximados | "hair and clothes still move, but can't be grabbed or stretched" |
| Materiais lilToon | exportados com texturas divididas em cor/dado | o lado Animama documenta que as extensões `MOCHIYA_avatar_composition` e `MOCHIYA_materials_liltoon` **sobrevivem apontando para nada no binário** e são aceitas pelo otimizador porque sabe disso (`docs/frontend/runtime/vrm-optimization.md`) |
| Shaders que não são lilToon (Poiyomi etc.) | achados empobrecidos | "keep only their main texture and colour… toon shading, outlines, emission and matcaps are lost" |
| Vertex colors | **perdidos** | consequência declarada: "some lilToon outlines look slightly heavier" |
| Jaw-bone lip sync | não | coerente com o §7 do Animama (o lábios vêm do áudio, não do osso) |
| Avatares que exigem Modular Avatar build | recusados | §3 |
| qualquer `.vrm` existente | nunca sobrescrito | escrita em nome temporário + move |

## 5. Licença e proveniência — separando as três camadas

1. **Este repositório: MIT** (1.068 B, raiz + cópia dentro do pacote). Zero dependências npm. Logo: o *padrão* pode ser reimplementado em qualquer produto Lia sem obrigação recíproca; partes copiadas exigiriam apenas reter o aviso.
2. **As dependências Unity: MIT também**, mas obtidas por URL Git com pin de tag/commit (`v0.131.2` do UniVRM e o commit do Mochiya). Nada é *redistribuído* neste repo — o `manifest.json` do usuário passa a apontar para lá. Isso é o que permite ao pacote ter 41 KB de zip.
3. **O ativo convertido: não é licenciado por nenhuma das duas.** A instrução "convert only an Avatar whose licence allows it" está no topo, repetida como aceite no fluxo (`LicenceNotice.cs`, 48 linhas, na pasta `Export/`), e a licença do VRM de saída é a do prefab de entrada. A ADR 0032 do Animama fecha o raciocínio: "Conversion quality bounds what the app receives… Avatar files that cannot be converted to VRM remain unsupported".

Emitir um `.vrm` **não** limpa termos de BOOTH/VRoid; este dossiê não registra nenhuma hipótese contrária.

## 6. Maturidade

Verdadeira, e pequena: 32 commits, 2 releases, 9 downloads no asset mais recente, 2 estrelas, 1 issue, um mantenedor. Três sinais de que nonetheless não é um experimento abandono: (a) CI matricial **ubuntu + windows** rodando `npm test`, com actions fixadas por SHA de commit (`actions/checkout@08c6903…#v5.0.0`); (b) um job separado que roda `check.mjs`, `pack.mjs` e `build-listing.mjs` "as a release would, without publishing"; (c) 5 branches abertas só para reescrever o README por sistema operacional. O `RELEASING.md` (986 B) existe, o `CHANGELOG.md` do pacote é mantido, e a `check.mjs` **valida a coerência tag ↔ versão ↔ CHANGELOG** (`--tag v0.1.0`). O que falta: teste de conversão sobre um avatar real em CI (impossível sem licença Unity), e qualquer histórico de suporte a casos esquisitos além do que os 55 testes de unidade cobrem.

## 7. O que leva a Lia (mecanismos, não código)

| # | Prática | Fonte | Classificação |
|---|---|---|---|
| C1 | **Checagem estática da alegação de privacidade**: `scripts/check.mjs:155-172` varre todos os `.cs` do pacote e todos os arquivos de `cli/` contra `UnityWebRequest\|HttpClient\|WebClient\|System\.Net\|Mochiya\w*Upload` (C#) e `\bfetch\(|["'](node:)?(https?\|http2\|net\|tls\|dgram)["']\|XMLHttpRequest\|WebSocket` (JS), e falha o build se aparecer rede. É o que torna "uploads nothing" uma **propriedade verificável** em vez de uma frase | `scripts/check.mjs`, executado aqui | **ADAPT** — Research/Agent Hub: qualquer promessa de "roda local, não envia nada" que a Lia faça sobre um produto deveria ter um verificador deste tamanho |
| C2 | Saída atômica com retry: escrever em nome temporário ao lado do destino, mover só quando completo, nunca sobrescrever | `AvatarExporter.cs:16-27` | **ADAPT** — Forge (todo exportador de ativo) |
| C3 | Recusar em vez de degradar silencioso: Modular Avatar por varredura de namespace sem referência de compilação; bloqueadores com motivo ordenado compartilhado entre UI e batch | `ModularAvatar.cs`, `ExportBlockers.cs` | **ADAPT** — Forge, Studio |
| C4 | Empacotar o mesmo código para dois hospedeiros (UPM `package.json`/`.asmdef` + `bin` npm) com **uma** fonte de verdade de versão, verificada no CI | `Packages/com.animama.avatar-converter/package.json`, `package.json`, `check.mjs:36-48` | **ADAPT** — Agent Hub |
| C5 | O fato do `-nographics` e o `CANNOT_CONVERT=2 / NOT_READY=3` | `cli/unity.mjs:1-13` | **REFERENCE_ONLY** — só vale para quem dirigir Unity |
| C6 | Usar o conversor no pipeline da Lia | — | **REJECT** (exige Unity 2022.3 + projeto VRChat + lilToon ≥ 2.3.4 + Node ≥ 22; e a Lia não consome avatares VRChat. Se um dia consumir, o objeto a reabrir é este) |

## 8. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Uma conversão real | `BLOCKED` | não há Unity, não há projeto VRChat, não há licença; seria também um download que o escopo desta base não faz |
| Que o `.vrm` de saída tem humanoid/expressions corretos | `UNVERIFIED` | só verificável com o § acima |
| Os 55 testes C# | `NOT_RUN` | exigem `UNITY_INCLUDE_TESTS` dentro do editor; **não existe** runner sem Unity |
| `release.yml` | lido só o nome | não executei nem inspecionei o fluxo de publicação |
| `index.json` do VPM publicado | não aberto | `raymond-van.github.io` fora do escopo de rede permitido aqui; a *geração* do listing foi lida no CI e no script |

## 9. Evidências

Executado nesta sessão (as duas primeiras linhas são o `LOCAL_TESTS_PASS`):

```
$ node --version
v22.22.3
$ node --test "cli/*.test.mjs" "scripts/*.test.mjs"        # = `npm test`
1..46  # tests 46  # pass 46  # fail 0  # duration_ms 504
$ npm run check
OK: version 0.1.1, 82 package files and folders, 36 sources checked.   (exit 0)
$ grep -c "\[Test\]" $(find . -name "*Tests.cs")
RequirementsTests.cs:11  AvatarExporterTests.cs:17  ExportWindowLogicTests.cs:14  HumanoidBoneRepairTests.cs:13
$ gh api repos/raymond-van/animama-avatar-converter/releases
v0.1.1: com.animama.avatar-converter-0.1.1.zip | 60924 B | downloads 9
v0.1.0: com.animama.avatar-converter-0.1.0.zip | 49240 B | downloads 3
$ curl registry.npmjs.org/animama-avatar-converter
versões: 0.0.0-stage, 0.1.0, 0.1.1 · latest 0.1.1 · license MIT · engines node>=22
deps: None · unpackedSize 41414 · fileCount 8 · maintainers: raymond-van
```

Leitura de arquivos (caminhos medidos no clone): `Editor/Export/{AvatarExporter,HumanoidBoneRepair,MochiyaConverter,ExportBlockers,BatchExport,ModularAvatar,LicenceNotice,ExportWindow,AvatarSource,ExportTypes,ReportExplanations,SceneSetupScope,IAvatarConverter}.cs`, `Editor/Bootstrap/{Requirements,DependencyInstaller,SetupWindow,RequirementsView,BatchRequirements,ExportMenu}.cs`, `cli/{args,main,prefabs,project,unity}.mjs` (+ os 5 `.test.mjs`), `scripts/{check,pack,build-listing,listing}.mjs`, os 4 `.asmdef`, `Packages/com.animama.avatar-converter/package.json`, `README.md`, `RELEASING.md`, `LICENSE`, `.github/workflows/ci.yml`.

Classificação da evidência: `OBSERVED` para o que foi lido e executado; `REPORTED` para as promessas de `README` (limites de preservação, opções do comando, troubleshooting) que só o Unity confirmaria; `BLOCKED` para a tabela do §8.

## 10. Ponteiras para a próxima rodada

1. `packages/…/CHANGELOG.md` ainda não foi lido linha a linha — é onde as decisões de preservação mudam de ideia.
2. A issue `#4` (e a branch `feat/pmx-conversion`) abrem a pergunta PMX/MMD: se a Lia algum dia ingerir ativos de BOOTH em formato MMD, **esse** é o caso de uso real do conversor, não o VRChat. Reabrir aqui, não no Animama.
3. Verificar se o Mochiya `0826f6e3` ainda é o commit suportado e se a versão mínima `[0.1.6]` do `.asmdef` bate com a `MOCHIYA_COMMIT` (a `check.mjs` garante isso no repo deles; vale reler na próxima revisão).
4. Medir o que uma conversão custa em disco/tempo **só se** um projeto Lia decidir consumir VRChat/PMX — hoje é pergunta sem dono, e não cabe a esta base respondê-la.

## 11. Como isto se liga à base

- Irmão direto do dossiê `repositories/animama/REPORT.md` (`LR-UI-006`): o §4 da ADR 0032 daquele repositório é o contrato do lado receptor — "VRChat Avatars reach the app through a VRM conversion that preserves their morph targets" — e é por isso que este conversor não precisa gerar expressões VRM.
- A prática C1 entra como candidato em `comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md` (`LR-CMP-005`) e como precedente para o formato I de `cross-project/licensing/SPLIT-LICENSE-SCAN.md`: aqui há MIT na raiz, cópia dentro do pacote e pins de terceiros por commit — três camadas nomeáveis sem nenhum documento extra.
- O resto (C2–C4) é padrão de empacotamento/exportação, não arquitetura de produto: cabe ao dono do Forge e do Hub decidir se serve. Nada aqui propõe dependência, fork ou cópia.
