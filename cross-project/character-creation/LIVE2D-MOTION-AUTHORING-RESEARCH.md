# Live2D: autoria de movimento só com JSON — o repositório `live2d-add-motion-sample-web-ui`

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-009` |
| Categoria | forge (ferramenta e padrão de fluxo) |
| Projetos | Lia Forge 2.0, Lia Studio |
| Fontes | `gh api repos/shinshin86/live2d-add-motion-sample-web-ui` (metadados, licença, árvore, `README.md`, `AGENTS.md`, `.gitignore`, `index.html`), lidos em 2026-11-21; `live2d.com/en/sdk/license/` (Cubism SDK Release License); `github.com/Live2D/CubismWebFramework/blob/develop/LICENSE.md` |
| Data | 2026-11-21 |
| Status | CURRENT |
| Confiança | **Alta na mecânica e nas licenças lidas**; **média no fluxo de agente** (relato do autor, não reproduzido por mim); **nula em resultado visual** — não rodei a WebUI |
| Natureza | pesquisa e documentação; não autoriza copiar código para o Forge nem adotar a tecnologia |

> Este ID estava deliberadamente livre até a rodada 7.1 (para não inventar documento só para
> fechar sequência). Passa a ser ocupado por um objeto real a partir de 2026-11-21.

---

## 1. O que é

Repositório de **Yuki Shindo** (`shinshin86`), licença **MIT** (Copyright 2026), JavaScript +
Python de biblioteca padrão. Metadados na leitura de 2026-11-21: **336 estrelas, 23 forks,
48 commits, 4 branches, 0 tags**, criado em 2026-07-13, último push em 2026-11-03 — atividade
real, não abandonado. Tópicos: `live2d`, `cubism`, `motion`, `avatar`, `face-tracking`,
`mediapipe`, `obs`, `webui`, `claude-code`, `codex`.

A tese, escrita pelo autor na primeira linha do README:

> **"Add new motions to a Live2D model by editing JSON only — no Cubism Editor required."**

O argumento é tecnicamente correto e vale registrar: um arquivo de movimento Live2D
(`.motion3.json`) é **apenas JSON** — um conjunto de curvas de keyframe por parâmetro do
modelo. Se o modelo já tem os parâmetros, dá para animá-lo sem riggar nada, sem tocar em malha
e sem abrir o Cubism Editor.

O limite está na mesma frase: **só dentro dos parâmetros que o modelo já tem**. Não cria rig,
não cria deformador, não resolve personagem sem parâmetros adequados. E o repositório é
explícito quanto a isso — o `AGENTS.md` instrui o agente a **não forçar** um movimento quando
os parâmetros não permitem, e sim propor alternativas.

## 2. O que o repositório entrega

| Componente | Conteúdo |
|---|---|
| 7 movimentos de exemplo | Happy, Wink, Nod, Thinking, Surprised, Shy, Head shake, feitos para o modelo de amostra oficial "Hiyori" |
| tools/setup_model.py | coloca o modelo (zip ou pasta), gera `model.config.json` |
| tools/analyze_model.py | lista parâmetros, faixas seguras e parâmetros **dirigidos por física** (que não devem ser animados à mão) |
| tools/gen_motions.py | gera `.motion3.json` a partir de motion-defs/<modelo>.py e registra no `model3.json` |
| tools/validate_motions.py | **validador independente**: faixas, parâmetros inexistentes, saída de física, colisões de nome, emenda de loop (valor e inclinação) |
| tools/verify_browser.sh | verificação **visual** com Chrome headless, capturando poses de pico |
| tools/serve.py | servidor local (`localhost:8765`) e relay para página de streaming |
| motion-defs/shared/ | pacotes portáteis: `gestures.py` (nod, shakehead, surprised) e `faces.py` (smile, shy, surprised, glare) |
| `AGENTS.md` / `CLAUDE.md` | documentação **escrita para agentes de código**, com regras de design, armadilhas medidas e "Definition of Done" |
| WebUI | tocar movimento, loop, lip sync (off / simulado / áudio / microfone), expressões, tracking facial (MediaPipe) e de tronco, gravação e modo streaming para OBS |

Detalhes que mostram maturidade de engenharia (todos lidos no código/README, não testados):
normalização de valores em `[-1, 0, +1]` relativa à pose base e às faixas seguras; *ledgers* de
propriedade (`.generated-motions.json`, `.generated-expressions.json`) para nunca sobrescrever
arquivo que o gerador não criou; recusa a gerar quando há colisão de nome ou valor inseguro
("falha antes de escrever"); expressões `.exp3` com blend `Add`/`Multiply`/`Overwrite`; validação
de emenda de loop por valor **e** derivada.

## 3. O que interessa ao Lia Forge: o padrão, não o código

Isto é o achado da pesquisa. O repositório não é interessante por ser Live2D — é interessante
porque **implementa, de forma pequena e auditável, exatamente o tipo de fluxo que
`LR-AGENT-012` propõe como skill**: um agente recebe um pedido em linguagem natural, executa um
pipeline com etapas verificáveis e **só termina quando a verificação passa**.

| Elemento | Como aparece no repositório | Por que importa para nós |
|---|---|---|
| Gerador determinístico | `gen_motions.py` escreve JSON a partir de definições em Python | o artefato é reproduzível e versionável; nada de "clicar até ficar bom" |
| **Validador independente** | `validate_motions.py` não confia no gerador, revalida faixas e emendas | é o antídoto para o problema que `LR-STUDIO-008` §6 discute: score que aprova sozinho |
| Verificação visual | Chrome headless + screenshot, com `&freeze=N` para fixar a pose | fecha o ciclo "o número passou, mas ficou feio" |
| **Definition of Done** explícito | 4 itens: validador 0, screenshots corretos, nada existente alterado, URL entregue ao usuário | transforma "pronto" em critério verificável — vocabulário que falta hoje nas nossas skills |
| Documentação para agente | `AGENTS.md` com regras, armadilhas e "não force: proponha alternativa" | é o formato que o Forge precisaria para qualquer skill de personagem |
| Isolamento de escopo | tudo que é por modelo é *git-ignored*; só ferramenta e doc entram no repositório | evita que dado licenciado contamine o produto |

**O relato do autor sobre autonomia** (commit de 2026-07-13, em `CLAUDE.md`): um agente novo,
recebendo **apenas** o `AGENTS.md`, completou o fluxo inteiro (setup → análise → geração →
validação → verificação no navegador); e o pipeline passou nos três modelos de amostra
(Hiyori/Mao/Haru). Isso é `COMMUNITY_REPORTED` — declaração do autor no próprio repositório,
não medição independente.

**Armadilhas que o `AGENTS.md` registra como medidas** — e que valem como conhecimento geral de
verificação headless, independente do Live2D:

- `--virtual-time-budget` **não** avança o tempo da animação: o playback fica no frame 0;
- `--dump-dom` não espera `--timeout`; é preciso checar por screenshot;
- WebGL falha com `--disable-gpu`; é preciso `--use-angle=swiftshader-webgl`;
- `PIXI.Application` precisa de `preserveDrawingBuffer: true` para o canvas não sair em branco;
- uma instância de Chrome headless por vez, e nunca `--user-data-dir` novo.

## 4. A pilha de licenças — o ponto que decide tudo

Aqui está o motivo de o repositório precisar de documento próprio: **MIT no topo da pilha não
torna a pilha MIT.**

| Camada | Licença | O que implica |
|---|---|---|
| Código do repositório | **MIT** (texto lido: "Copyright (c) 2026 Yuki Shindo") | pode copiar, modificar, redistribuir, vender, com aviso de copyright |
| `CubismWebFramework` (Live2D Cubism Components) | **Live2D Open Software License** | licença própria da Live2D Inc., não é MIT nem Apache |
| **Cubism Core** (`live2dcubismcore.min.js`) | **Live2D Proprietary Software License** | proprietária. O repositório **não** a redistribui: o `index.html` carrega de `https://cubism.live2d.com/sdk-web/cubismcore/live2dcubismcore.min.js` no runtime |
| Dados do modelo de amostra ("Hiyori Momose" ©Live2D) | termos próprios da Live2D | **não incluídos**; o `.gitignore` diz, em japonês, que modelos e assets locais ficam fora do repositório **por razão de licença** |
| `pixi.js` 6.5.10 / `pixi-live2d-display` 0.4.0 | MIT (via jsDelivr) | ok, mas a versão 0.4.0 está fixada porque web/cubism-colors.js depende da estrutura interna dela |
| vendor/mediapipe | Apache-2.0, com `POSE-LICENSE` separado | atenção: o Pose Landmarker tem termos próprios além do Apache |

E, acima de tudo, o **Cubism SDK Release License** (a "Publication License Agreement"), cujo
texto oficial foi lido em `live2d.com/en/sdk/license/`:

| Regra | Texto | Efeito |
|---|---|---|
| Quem precisa | usuários de negócio, definidos por **faturamento anual ≥ 10 milhões de JPY** no último exercício | abaixo disso ("General Users"/Small-Scale) não há release license |
| Faixas | Small < 10 M JPY · Middle 10–100 M JPY · Large ≥ 100 M JPY (controladas por outra empresa: conta o faturamento dela) | define a tabela de taxas |
| "Publish" | distribuir, transmitir, exibir, anunciar, compartilhar — **"internamente, comercialmente, não comercialmente ou de qualquer outra forma"**, com a Live2D decidindo "a seu exclusivo critério" se um ato é publicação | publicar um jogo com personagem Live2D aciona o regime |
| "Expandable Application" | obra derivada com grande expansibilidade: **avatares, apps de streaming, geradores de vídeo**, ou título que dá acesso a várias obras | **este é o caso do Lia Forge se ele gerar personagens Live2D em série** |
| "Redistributable Code" | só o que estiver listado em `RedistributableFiles.txt` | define o que pode ser embarcado |

**Consequência, dita sem rodeio:** se o Lia Forge vier a **produzir ou publicar** personagens
Live2D como parte de um produto, a pergunta não é "o repo é MIT?" — é "quem é o cliente, qual o
faturamento dele e isso é uma Expandable Application?". **Não li a tabela de taxas** (`BLOCKED`)
e **não emito parecer**. `REQUIRES_LEGAL_REVIEW`.

## 5. O que foi testado, e o que não foi

| Ação | Resultado | Rótulo |
|---|---|---|
| Clonar o repositório (clone raso) | ok | `TESTED` |
| `python3 -m py_compile tools/*.py` | **ok** (todos compilam) | `TESTED` |
| `python3 tools/gen_motions.py` sem modelo | recusa com mensagem clara: `model.config.json not found. Run setup_model.py first` | `TESTED` |
| Rodar o pipeline completo | **não**: exige modelo Live2D (licenciado, não incluído) | `BLOCKED` |
| Verificar a WebUI no navegador | **não**: o sandbox não tem Chrome/Chromium | `BLOCKED` |
| Tracking facial / MediaPipe | **não**: exige câmera e navegador | `BLOCKED` |
| Modo streaming para OBS | **não** | `BLOCKED` |

Ou seja: verifiquei que o código é sintaticamente válido, que as ferramentas têm guarda de
entrada e que o repositório **não redistribui** dado licenciado. **Não** verifiquei que a
animação funciona ou fica boa.

## 6. Onde isso entra (e onde não entra) nas frentes existentes

| Frente | Veredito |
|---|---|
| `LR-STUDIO-008` (silhueta) | não interfere. A silhueta continua sendo gate humano antes da animação |
| `LR-STUDIO-009` (sheet) | **complementa**: o sheet garante consistência entre vistas; o movimento Live2D garante que o personagem 2D se mexe com o rig que tem |
| `LR-FORGE-007` (2D→3D) | **não substitui** nenhum pipeline. Live2D é 2D por construção — não gera malha, não exporta GLB, não serve para jogo 3D |
| `LR-FORGE-008` (produção) | acrescenta uma etapa que não estava no assessment: **animação 2D sem DCC**, para personagem 2D (VTuber, jogo 2D, diálogo) |
| `LR-AGENT-012` (skills) | **é a referência mais próxima** do que uma skill do Forge deveria parecer: gerador + validador independente + verificação visual + Definition of Done + docs para agente |
| Hardware (`LR-STUDIO-007` §5) | roda em navegador com WebGL; nada de CUDA. Não resolve o gargalo de geração de imagem, mas não é bloqueado pela RX 580 — `UNVALIDATED` quanto a desempenho real |

## 7. Recomendação de pesquisa (não de adoção)

1. **Adotar o padrão de fluxo, não o código.** "Gerador + validador independente + verificação
   visual + Definition of Done" é reaproveitável em qualquer skill do Forge, inclusive nas que
   não têm nada a ver com Live2D. É o item de maior valor deste repositório.
2. **Não adotar Live2D como caminho de personagem 3D.** Não é o que a tecnologia faz.
3. **Se houver personagem 2D/VTuber no escopo**, um spike local é barato: clonar, usar o modelo
   de amostra, pedir a um agente "adicione um movimento de acenar" e comparar o resultado com o
   que um animador levaria para fazer à mão. Antes disso, resolver a questão de licença com o
   proprietário (§4).
4. **Registrar a assimetria de licença** no material do Forge: MIT no repositório, proprietário
   no Core, e um release license por faturamento. É o tipo de detalhe que vira problema tarde.

## 8. Não validado (`UNVALIDATED` / `BLOCKED`)

| Item | Estado |
|---|---|
| Qualidade visual dos 7 movimentos | `BLOCKED` (sem navegador/modelo) |
| Autonomia real de um agente no fluxo | `COMMUNITY_REPORTED` (relato do autor) |
| Desempenho em máquina modesta | `UNVALIDATED` |
| Tabela de taxas do Cubism SDK Release License | `BLOCKED` (não lida) |
| Compatibilidade da licença Live2D com o modelo de distribuição do Lia Forge | `REQUIRES_LEGAL_REVIEW` |
| Termos dos modelos de amostra (Hiyori/Haru/Mao) | `UNVALIDATED` (não lidos; o repo apenas diz que não redistribui) |
| Se `pixi-live2d-display` 0.4.0 é a versão adequada a longo prazo | `UNVALIDATED` |

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-CREATION-SKILLS-ANALYSIS.md` · `CHARACTER-PRODUCTION-TOOLS-ASSESSMENT.md`
