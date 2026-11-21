# RESEARCH-CHANGELOG

Registro append-only do que entrou na base. Ordem inversa (mais recente primeiro).
Cada linha: data · tipo · item · efeito.

Tipos: `ADD` (pesquisa nova) · `FIX` (correção) · `CONSOLIDATE` (digest) · `DECISION` ·
`BLOCKED`.

---

## 2026-11-21 (UTC) — dois objetos novos auditados **com execução**: Bosch image-render e jenalab

Rodada de descoberta, não de manutenção: dois alvos indicados pelo proprietário foram abertos,
analisados no commit pinado e **executados localmente** onde dava para executar. Nenhum projeto Lia
foi alterado, nenhuma conta aberta, nenhum peso baixado, nenhum GPU alugada, nenhuma chave criada.

### ADD — `LR-FORGE-012` · `jenalab-com/jena-image-render` (`3b9276fe`)
- **Executado de verdade** (venv Python 3.11.2, tarball do commit): `159 + 22 testes OK` na forma do
  CI, `181 passed + 47 subtests` via pytest (0.72 s), e os 14 exemplos em `--dry-run` nos dois alvos
  — **28 execuções, 0 falhas, sem GPU, sem ComfyUI e sem chave de RunPod**.
- Achei por sonda o que a suíte não cobre: `config.py:340` faz `steps=int(...)` sem faixa — `steps 0`
  e `steps -5` passam no plano com exit 0. A afirmação do README ("validates models, files,
  LoRA/engine matches and output paths") é **precisa e estreita**: faixa numérica não está incluída,
  e o que o ComfyUI faria com isso ficou `UNVALIDATED`.
- Padrão mais útil do objeto: `catalog.json` pinna **23 arquivos de peso** por
  `hf://org/repo@<commit>/<path>` + SHA-256 + tamanho (98,82 GB nos 13 arquivos de modelo), com tabela
  de licença por alias "**as stated on each model card at the pinned revision**". É o formato que falta
  em `LR-MODEL-007` (código × pesos) e no problema das 47 Skills sem licença no payload.
- Fronteira de licença lida no `Dockerfile` do pod: pacote MIT falando com **ComfyUI GPL-3.0 por
  HTTP**; `entrypoint.sh` recusa subir sem senha e prende o ComfyUI em `127.0.0.1`. Se o Lia um dia
  distribuir imagem com ComfyUI: `REQUIRES_LEGAL_REVIEW`.
- **Idade zero**: criado, publicado e analisado no mesmo dia (2026-11-21), 1 commit, sem releases,
  sem issues. Recomendação `ADAPT` **aos padrões**, não ao pacote; revisão em 90 dias (não 180), por
  ser software sem histórico.
- **Os outros 7 repositórios da organização** foram abertos e registrados no mesmo relatório, sem
  virar 7 linhas de catálogo: MIT em todos os 6 próprios; `SwiftTerm` é fork **0 à frente / 56 atrás**
  do upstream e `mediator` é fork **idêntico** (0/0) — snapshots sem modificação; 5 dos 6 próprios são
  apps macOS, irrelevantes como dependência para o Lia.

### ADD — `LR-FORGE-011` · `boschresearch/image-render-generative` (`ba2a9608`)
- Plugin de refinamento generativo (ControlNet multi-controle / Prompt-Free-Diffusion) do sistema de
  render sintético catharsys da Bosch Research. Execução: `pip install -e .` **ok**,
  `python -m compileall src/` **ok** (12 módulos), import **falha** com
  `ModuleNotFoundError: No module named 'anybase'`.
- Dois achados que só apareceram ao executar: (a) `setup.cfg` **sub-declara dependências** — lista só
  `pyjson5` e `tqdm`; (b) `anybase` no PyPI é hoje **1.1.0 com `Requires-Python >=3.12`** e o sandbox tem
  3.11 → o caminho de execução está bloqueado por idade do código, não por capricho do ambiente.
  `catharsys` não existe no PyPI (404) e só vem do workspace de 17 repositórios declarado em
  `image-render-setup/repos/repos-main.yaml`.
- Licença Apache-2.0 `CONFIRMED` com **cabeçalho `<LICENSE id="Apache-2.0">` em cada `.py`**,
  `NOTICE.md` de detentores e `3rd-party-licenses.md` declarando "nenhum" — disciplina de proveniência
  que o Lia deveria copiar (é a mesma lacuna das Skills do Hub). Contribuir exige DCO 1.1 + commit GPG.
- 814 dias sem push (a família inteira parou em 2025-07-31), ★0, 4 forks, sem CI, sem testes, sem
  release; `version.py` declara 1.0.4 enquanto a linha de release fixa `tags/v1.0.3`. Veredito:
  **`REFERENCE_ONLY`** — referência de disciplina e de forma de pipeline, nada de código.

### FIX — contagens e índices da base
- 25 objetos auditados (23 repositórios + 2 organizações), catálogo regenerado (25 linhas), índice com
  as duas linhas novas, `data/inventory/license-matrix.tsv` com 25 linhas e as duas linhas na
  Tabela-mestra de `LR-LIC-005`, `data/testing/test-log.tsv` com 20 linhas.
- `README.md` dizia "**0** testes de software registrados" com 16 linhas já existentes no log: passa a
  declarar as **20 linhas** (2026-11-21). Contagem de Markdown: 174 → 176.

### Validação
- `python3 tools/validate.py`: **0 erros · 0 avisos · 7 notas** (as 7 notas são as mesmas de antes —
  IDs de índice sem cabeçalho próprio).
- `python3 -m unittest tools.test_validate`: **Ran 76 tests — OK**.

---
## 2026-11-20 (UTC) — disciplina operacional: conjunto mínimo de Skills do ecossistema

Não é rodada de pesquisa: nenhum objeto novo foi investigado, nenhum ID ou documento de
tecnologia foi criado. O que entrou é **procedimento**: qual instrução já existente no
ecossistema Lia o Research aplica, quando aplica e o que rejeitou.

### ADD — `agents/SKILLS-OPERATING-SET.md`
- **Catálogo localizado:** `Lia-AgentHub`, branch `arena/db625478-lia-agenthub`,
  `docs/research/` (4 arquivos `*.records.json` com 48 registros, inventário canônico de 37 KB,
  relatório de importação e roadmap). Todos os 48 registros seguem `trust: unreviewed` e
  `lifecycle: quarantined` — catálogo não é biblioteca nem aprovação.
- **Lidas por inteiro (10 `SKILL.md`, com commit e hash):** 5 de `Lia-Project` @ `0093de09`
  e 5 de `Lia-Studio` @ `203b60f`. As 9 de `Lia-Model-Lab` e a de `Lia-Forge` **não puderam
  ser lidas**: os dois repositórios retornam `404` ao token atual → `BLOCKED`, sem adivinhação.
- **Conjunto mínimo adotado — 1 principal + 3 especialistas:** `lia-agent-orchestration`
  (brief de 8 campos, retorno de 6, um escritor por caminho, capacidade por evidência, parada
  ao sair do escopo), `lia-regression-investigation` (refutar a própria hipótese, uma variável
  por vez), `lia-game-test-evidence-review` (matriz de rastreabilidade, `NÃO AVALIADO` nunca
  vira aprovação) e `lia-project-resume` (reconstruir estado do artefato persistido).
- **Rejeitadas com motivo, uma linha cada:** `lia-module-planning`, `lia-test-discipline`,
  `lia-task-handoff`, `lia-agent-evaluation`, `lia-safe-change`, `lia-game-design-review`,
  `alethe`, `lia-brand-check`, `lia-brand-consistency-review`.
- **Achado que limita a expectativa:** a Skill de que o Research mais precisaria,
  `lia-research-evidence`, é a **proposta nº 7** do roadmap do Hub — **não implementada**.
  Nada foi criado, instalado ou copiado de outro projeto.
- **Compatibilidade:** o Arena não expõe runtime de Skills; a aplicação é leitura e adesão
  manual, registrada como `APPLIED (manual)`, nunca como execução. Nenhuma das quatro existe
  em `main` de seu repositório — os commits pinados podem desaparecer com a limpeza de branch.

### FIX — contagem de arquivos
- `README.md` passa de 173 para 174 arquivos Markdown (o validador confere a contagem).

---

## 2026-11-20 (UTC) — rodada 7.5: §5.3 do Tripo, visibilidade/retenção e downloads do Meshy Free

Rodada pequena e focada: corrigir a referência contratual do treinamento no plano pago, registrar
duas divergências ajuda × Termos e completar as limitações operacionais do Meshy Free. Nenhum
documento ou ID novo, nada implementado, nenhuma conta aberta, nenhum crédito gasto.

### FIX — Tripo §5.3 (correção de erro da própria 7.4)
- A 7.4 classificou a proibição de treinamento no plano pago como `UNVALIDATED`, por não achá-la
  no §5.2.2. **Estava errado**: a cláusula existe no **§5.3** ("Company will not use Paid Users'
  Inputs or Paid Outputs as training data to train, fine-tune or otherwise develop any artificial
  intelligence model"). A página de ajuda atribui a proteção ao §5.2.2 — **erro de referência da
  ajuda**, agora registrado como tal. Classificação com evidência contratual: `OFFICIAL_LICENSE`.
- Registradas as três coisas que o §5.3 **não** impede: uso de informação **agregada ou
  anonimizada** para melhorar serviço/funcionalidades/modelos; **revisão** de Inputs e Outputs sob
  o §3.1 para operar, proteger, solucionar problemas e avaliar qualidade/segurança/desempenho
  (expressamente separada de treinamento); retenção de dado anonimizado já usado em modelo.
  Fica vedado afirmar que a Tripo nunca processa, revisa ou avalia conteúdo pago.
- Recomendação do plano pago **sem alteração**: segue como regime contratual mais favorável, sem
  promessa de exclusividade absoluta nem de ausência de todo processamento.

### FIX — Tripo: duas divergências novas, como itens independentes
- **Visibilidade** (§6.1.6): a ajuda diz que assets "are only visible to you unless you explicitly
  set them to public"; os Termos (§4, §5.2.1) dizem que **Free Outputs são públicos por padrão**.
  Separadas cinco categorias (Inputs, Free Outputs, Paid Outputs, visibilidade de interface,
  regime contratual de publicidade/licença), com a ressalva de que a interface **não** resolve o
  conflito contratual.
- **Exclusão e retenção** (§6.1.7): a ajuda fala em retenção "in perpetuity" citando o §10.5 de
  uma versão de 2025; o §10.5 atual trata de exclusão **sujeita a retenção legal/operacional
  permitida**, de cópias já baixadas por terceiros ("cannot be recalled"), da **persistência da
  licença/renúncia** e da retenção de anonimizado. Registrado que persistência de licença **não**
  é retenção perpétua do arquivo.
- **Contradição interna da ajuda** (§6.1.8): a mesma página que afirma "Tripo retains all rights to
  Inputs and Outputs" também classifica "your own artwork / photos" como "Safe — Full commercial
  use". Registradas as duas leituras (assuntos distintos × incompatibilidade residual) e
  **nenhuma** foi escolhida para "resolver" o problema.

### FIX — Meshy: downloads do Free, separados dos créditos
- Help Center oficial: Free tem **10 downloads/mês**, apenas de modelos **sem textura do Meshy 6
  Lite**; **Meshy 6, 7, T2.5, qualquer modelo texturizado, textura aplicada a modelo enviado e
  modelos do 3D Agent exigem upgrade** para baixar; crédito comprado "doesn't unlock downloads";
  modelos de assinatura anterior continuam baixáveis sem limite.
- Catálogo passa a separar explicitamente **geração, crédito, download e licença**. Corrigida a
  leitura implícita de que "100 créditos = 5 modelos" seria "5 assets exportáveis": no Free o teto
  real é o download (10/mês, só 6 Lite sem textura).

### C — Google Flow
- Reconferido em 2026-11-20 (UTC) nos artigos `16526234` (pt-BR) e `16353333` (en-GB): 50
  créditos/dia com ou sem assinatura, extras mensais por plano, atualização na primeira geração,
  não acumulação, janela de vídeo 14h–17h UTC para não assinantes, 18+ com idade verificada e
  região suportada, aposentadoria de Veo 3.1 Fast/Quality e Omni Flash 1.1 em **05/12/2026**.
  Mantido `OFFICIAL_DOCUMENTATION`; sem custo fixo de imagem, sem API própria, sem 3D.

### DECISION — nenhuma
- Free do Tripo continua `CONFLICTING` + `REQUIRES_LEGAL_REVIEW`; direito comercial do usuário
  gratuito **não** foi declarado resolvido; segue vedado usar Free Outputs em asset proprietário
  e enviar arte proprietária enquanto a divergência documental não tiver esclarecimento formal.

---

## 2026-11-20 (UTC) — rodada 7.4: últimas fontes oficiais (Tripo, Flow, API do Meshy)

Fechamento de quatro achados de revisão independente. Nenhum documento apagado, nenhuma
recomendação convertida em adoção, nada implementado, nenhuma conta aberta, nenhum crédito gasto.

### FIX — Tripo: quatro fontes oficiais na mesma conciliação
- Somadas duas páginas de ajuda oficiais: **"How to Use Tripo Models Commercially"** e
  **"How to Understand Data Privacy and AI Training at Tripo"**. Ambas afirmam que a Tripo
  **retém todos os direitos de Inputs e Outputs** de usuários gratuitos e citam os termos de
  **11/07/2025** — versão substituída pela de 13/11/2026.
- Montada a tabela das quatro fontes (página de preços, Termos, guia comercial, guia de
  privacidade/treinamento) com data, natureza (comercial / contratual / orientação), escopo
  (Inputs × Outputs × Free × pago), titular do direito e o que cada uma permite, restringe ou
  não esclarece.
- Nomeadas cinco divergências: **D1** titularidade (guias dizem "retains all rights"; §5.2 diz
  que os direitos que o usuário detém são dele e §5.2.1 renuncia em favor do público); **D2**
  Inputs (guias incluem; §5.2.1 exclui expressamente do regime); **D3** treinamento (guia diz
  proibição para pago "nos termos 5.2.2" — o texto lido do §5.2.2 não contém essa cláusula);
  **D4** uso comercial do usuário Free (página "non-commercial", guia "not granted", termo
  silente e permissivo quanto a terceiros); **D5** versão dos termos citada pelos guias.
- Mantido **`CONFLICTING` + `REQUIRES_LEGAL_REVIEW`**. O direito comercial do usuário gratuito
  **não** foi declarado resolvido. Recomendação conservadora reforçada (não usar Free Outputs
  nem enviar arte própria de personagem). Plano pago **sem alteração** de recomendação, com a
  ressalva nova de que a "proibição de treinamento" para pago é afirmação de página de ajuda.

### FIX — Google Flow: `COMMUNITY_REPORTED` → `OFFICIAL_DOCUMENTATION`
- O artigo oficial de créditos está acessível e confirma: **50 créditos/dia com ou sem
  assinatura**; **+200/mês** no Plus, **+1.000** no Pro, **+10.000** no Ultra US$ 100 e
  **+25.000** no Ultra US$ 200; atualização diária disparada pela **primeira geração do dia**;
  diários e mensais **não acumulam**; mensais renovam no início do ciclo de faturamento;
  **vídeo pode ficar indisponível para não assinantes entre ~14h e 17h UTC**, com imagem e
  agente disponíveis; **18+ com idade verificada** e região suportada (VPN não contorna);
  Workspace qualificado recebe 50 diários; custo por **segundo/modelo** (Omni Flash 1.2: 1/s em
  360p, 3/s em 720p; Veo 3.1 Lite: 10 créditos, 5 no Ultra; 4K: 50 créditos, só Ultra);
  SynthID invisível; falha devolve créditos em até 1 hora.
- Removida a ressalva de que o artigo não teria sido acessado. Continua vedado inventar
  "crédito = N imagens/vídeos"; API própria do Flow segue não documentada (API Gemini é outro
  caminho); Flow continua sem 3D.

### FIX — Meshy: plano Free não tem API
- Help Center oficial: custos iguais entre planos pagos; **o plano Free não tem acesso à API,
  mesmo comprando créditos adicionais**; plugins e integrações consomem o mesmo saldo de API.
- Catálogo passa a separar **Free Web App (100 créditos/mês)** de **Free API (não disponível)**.
  Fica registrado que "gastar os 100 créditos gratuitos em chamadas de API" é duplamente
  errado. **P-15 continua `UNVALIDATED`**: para planos pagos, nenhum documento lido afirma pool
  único nem separação definitiva.

### FIX — relatório e índices
- Contagem real de arquivos da rodada 7.3 conferida no diff `2d46707..b7f0be7`: **16 caminhos**
  — 11 em `cross-project/character-creation/` (10 Markdown + 1 TSV) e 5 de índice/controle. O
  resumo anterior dizia "12 + 5" e estava errado; o número correto é **11 + 5**.
- `RESEARCH-INDEX.md` §3-ter passa a listar as rodadas em **ordem cronológica** (7.1 → 7.2 →
  7.3 → 7.4), com o changelog mantendo ordem inversa e horários em UTC.

### DECISION — nenhuma
- Nenhuma adoção ou integração aprovada. Pipeline 2 continua candidato a avaliação. Free do
  Tripo continua vetado para asset proprietário.

---

## 2026-11-20 (UTC) — rodada 7.3 (o pedido a chama de "7.2"): conciliação de fontes, créditos e compatibilidade

Quatro inconsistências apontadas por revisão independente. Nenhum documento apagado, nenhuma
conclusão correta revertida, nada implementado, nenhuma conta aberta, nenhum crédito gasto.

### FIX — Tripo: contradição oficial documentada como tal (`CONFLICTING`)
- Página de preços: plano Free = *"Public Models · Non-Commercial Use"*; Pro/Max/Team =
  *"Private Models · Commercial Use"*. Termos (13/11/2026) §5.2.1: Free Outputs públicos por
  padrão, com renúncia de direitos e licença pública que permite a **qualquer terceiro** usar e
  explorar comercialmente, sem atribuição. §12.9 lista a ordem de precedência (order form, DPA,
  Supplemental Terms, Termos, AUP) e **não inclui a página de preços**.
- Análise separada em quatro dimensões (visibilidade, PI, direito comercial do usuário,
  exclusividade) e registrada a conclusão: **o conflito não se resolve lendo as fontes**. Caso
  classificado `CONFLICTING` + `REQUIRES_LEGAL_REVIEW`. Mantida a orientação conservadora: Free
  do Tripo não serve para personagem proprietário, e "terceiro pode explorar comercialmente"
  **não** autoriza o usuário.
- Paid Outputs verificados: página e §5.2.2/§5.2.3 **coerentes**; §5.2.2(b) registra que Free
  Outputs não se tornam pagos ao assinar.

### FIX — Meshy: Web App e API separados
- **Web App**: 100 créditos/mês; Image to 3D 20 (7.1/6), **25** (Ultra 2K/4K), **10** (6 Lite);
  Smart Topology 15; textura/split +10; AI Texturing 10/15; Model Edit 20; **Rigging 0,
  Animate 0 (conjunto gratuito), Remesh 0**. Licença: Free = CC BY 4.0 com atribuição.
- **API** (pré-paga): 20 mesh / 30 com 2K–4K / 35 com 8K; 6-lite 5; Ultra +5; **Auto-Rigging 5**;
  **Animation 3 por ação**; UV Unwrap 5; Remesh 5; Convert/Resize 1; Retexture 10/15.
- Corrigidas as frases que misturavam canais ("rigging 5" genérico; "20 modelos no lite" usando
  tarifa de API contra crédito de Web App; **6 Lite = 10 no Web App**, não 5). Estimativas de
  quantidade refeitas **por canal**. Pool de créditos compartilhado entre canais: `UNVALIDATED`.

### FIX — Google Flow: acesso gratuito registrado
- Registrado que **existe acesso sem assinatura** e que o valor corrente é **50 créditos/dia**,
  com a ressalva de rastreabilidade: a página oficial do produto não exibe números de crédito e
  o artigo de ajuda do Google não abriu nesta sessão — logo `COMMUNITY_REPORTED`, não
  `OFFICIAL_DOCUMENTATION`. `OFFICIAL_DOCUMENTATION` fica para o que está na página: modelos
  (Nano Banana imagem; Veo 3.1 e Gemini Omni vídeo), variação por nível/plataforma/região e 18+.
- Sem equivalência crédito↔imagem/vídeo. API do Flow continua **não documentada** (a API Gemini
  é outro caminho). Não faz 3D.

### FIX — ROCm/Ryzen AI no Windows: classificação corrigida
- Documentação oficial da AMD: **Windows 11**, APUs **gfx1150/gfx1151** (Ryzen AI Max+ 395,
  Max 390, Max 385, AI 9 HX 375/370/365, HX 475/470/465), **ROCm 7.2.1**, **PyTorch 2.9.1**,
  **Python 3.12**, FP16, wheels em `repo.radeon.com`, driver 26.2.2. Nota da AMD: *"the entire
  ROCm stack is not yet supported on Windows"*.
- Suporte Ryzen AI no Windows passa de `UNVALIDATED` para **`OFFICIAL_DOCUMENTATION`**. A
  conclusão sobre o equipamento de referência (Ryzen 5 5500 + RX 580/gfx803) **não muda**: não
  está em nenhuma matriz oficial, e a RX 580 continua fora de ROCm/HIP.

### FIX — matriz: evidência por dimensão
- `nivel_evidencia` mantido como resumo; acrescentadas `evidencia_licenca`, `evidencia_hardware`,
  `evidencia_atividade`, `evidencia_desempenho`. Tempos da RX 580 ficam em
  `evidencia_desempenho` = `COMMUNITY_REPORTED`, sem contaminar licença. Taxonomia global do
  Research intocada; 51 registros preservados.

### FIX — datas
- Padronizadas em **UTC**; removidas as ocorrências de 2026-11-21 (o commit `9a03c6f` é
  `2026-11-20T20:04:23Z`). Convenção registrada no catálogo §1 e no hub §3, com a conversão para
  São Paulo (UTC−3).

### DECISION — nenhuma
- Nada foi aprovado. Pipeline 2 continua "candidato prioritário para avaliação". Tripo Free
  continua vetado para asset proprietário.

---

## 2026-11-20 20:33 UTC — rodada 7.2 (AetherAI + Live2D) — dois objetos novos: serviço de assets 2D e autoria de movimento

Pedido do proprietário a partir de duas URLs. Nenhum documento anterior apagado, nada
implementado, nenhuma conta criada, nenhum token comprado, nenhum peso baixado.

### ADD — `LR-MODEL-008` · `AETHERAI-GAME-ASSET-SERVICE-RESEARCH.md`
- AetherAI (`aetherforgeai.com`, Aether Forge Games Inc., lei coreana, termos vigentes
  2026-04-01): estúdio de imagens, pixel art 32/48 px com modelo próprio, animação de sprites a
  partir de uma imagem (`sprite-pulsar-v2`), reskin de movimento (sprite→sprite), assets
  gratuitos e modelo de IP dedicado.
- **Direitos lidos e transcritos**: a empresa não reivindica propriedade nem exclusividade, uso
  comercial livre **sem atribuição**, resultados sobrevivem ao encerramento, sem restrição
  retroativa; e, no outro lado, a existência de copyright é "determinada caso a caso" e não há
  garantia contra semelhança com terceiros. É o regime mais permissivo entre os serviços já
  catalogados (comparado com Tripo Free, Meshy Free/CC BY e GPT Image).
- **Proibições contratuais registradas** (art. 6): nada de benchmarking, análise sistemática,
  material comparativo ou scraping/automação — restringe como o serviço pode ser avaliado por
  nós. `REQUIRES_LEGAL_REVIEW`.
- Preço: 70 tokens por US$ 3,99 (1ª compra); educacional 1.000 tokens por KRW 68.900. **Custo
  por geração `BLOCKED`** — a página de planos é renderizada por JavaScript. Não repito o erro
  de inventar equivalência "X tokens = Y assets".

### ADD — `LR-FORGE-009` · `LIVE2D-MOTION-AUTHORING-RESEARCH.md`
- `shinshin86/live2d-add-motion-sample-web-ui` (MIT, 336★, 48 commits, ativo): editar
  `.motion3.json` só com JSON e um agente, sem Cubism Editor, dentro dos parâmetros que o
  modelo já tem.
- **O valor registrado é o padrão de fluxo**, não a tecnologia: gerador determinístico +
  validador independente + verificação visual em Chrome headless + "Definition of Done" +
  documentação escrita para agentes (`AGENTS.md`/`CLAUDE.md`). É a referência mais próxima do
  formato que `LR-AGENT-012` propõe para skills.
- **Pilha de licenças separada**: MIT no repositório ≠ Live2D Open Software License
  (CubismWebFramework) ≠ Live2D Proprietary Software License (Cubism Core, carregado do CDN da
  Live2D e **não** redistribuído) ≠ dados de modelo (não incluídos por licença) ≠ pixi.js /
  pixi-live2d-display (MIT) ≠ MediaPipe (Apache-2.0 + `POSE-LICENSE`). Cubism SDK Release
  License a partir de 10 M JPY de faturamento, com "Expandable Application" cobrindo geradores
  de avatar — `REQUIRES_LEGAL_REVIEW`, taxas `BLOCKED`.
- `TESTED`: clone raso ok, `py_compile` de todas as ferramentas ok, gerador recusa rodar sem
  `model.config.json` com mensagem clara. Pipeline completo, WebUI e tracking: `BLOCKED`.

### FIX — contagens e referência cruzada
- Conjunto: **10 IDs, 10 documentos Markdown e 1 matriz com 51 registros** (46 + 3 + 2), em
  `README.md`, `RESEARCH-INDEX.md` §3-ter, `projects/lia-forge/INDEX.md` §4-bis, `RESEARCH-ROADMAP.md`
  e hub `LR-STUDIO-007`. README: 171 → **173** arquivos Markdown.
- Referência quebrada no hub §2: a linha "pipeline completo 2D→3D→jogo" citava `LR-FORGE-009`
  antes de o ID existir. Passou a apontar para `LR-FORGE-007`; `LR-FORGE-009` agora é um objeto
  real, não um número reservado.

### DECISION — nenhuma
- Nenhum dos dois é recomendação de contratação ou adoção. Trilha P ganhou P-12 e P-13, ambos
  `BLOCKED` por dependência de decisão do proprietário.

---

## 2026-11-20 20:04 UTC — rodada 7.1 (correção factual) — correção factual da pesquisa de criação de personagens

Correção documental do conjunto de 2026-11-20. Nenhum documento apagado, nenhuma conclusão
removida sem justificativa registrada, nada implementado, nenhuma conta aberta, nenhum crédito
gasto, nenhum peso baixado.

### FIX — contagens
- Conjunto passa a ser declarado como **8 IDs, 8 documentos Markdown e 1 matriz** em
  `README.md`, `RESEARCH-INDEX.md` (§3-ter), `projects/lia-forge/INDEX.md`, `RESEARCH-ROADMAP.md`
  (Trilha P) e no hub `LR-STUDIO-007`. Não existe `LR-FORGE-009` e não foi inventado.
- Matriz: **46 registros originais + 3 candidatos da rodada 7.1 = 49 registros** (50 linhas com
  cabeçalho). O número mudou porque a rodada acrescentou candidatos — declarado aqui, não
  silenciado.

### FIX — vídeo de referência
- `youtube.com/watch?v=lKDVvJcSB14` é **teste comparativo de modelos de linguagem para jogos**
  (MagmaDev, 2026-11-19, 45:58), não vídeo de processo de personagem. A atribuição da sequência
  "exploração → ficha → 3D → jogo" ao vídeo foi **removida** em `LR-STUDIO-007` §1.1 e
  `LR-STUDIO-008` §1; a sequência fica atribuída à **ordem de pesquisa recebida**. Vídeo não
  assistido: `BLOCKED` para o restante do conteúdo.

### FIX — direitos, créditos e preços
- Tripo: Free Outputs **públicos por padrão**, com renúncia de direitos e licença pública que
  permite exploração comercial por terceiros sem atribuição (termos de 2026-11-13, §5.2.1);
  Paid Outputs do usuário, privados e comerciais (§5.2.2). "Free = não comercial" **eliminado**.
- Meshy: custo por modalidade (mesh 20 · 2K 30 · 8K 35 · lite 5 · rigging 5 · animação 3/ação).
  "100 créditos = 10 modelos" **eliminado**.
- Data de consulta e URL registradas no catálogo (§6), na matriz e nos pipelines.

### FIX — hardware AMD
- Separado em: ROCm Linux (sem gfx803), PyTorch oficial no Windows (CUDA/CPU), suporte restrito
  a APUs Ryzen AI (`UNVALIDATED`) e gfx803 (sem caminho em nenhum dos dois).
- `stable-diffusion.cpp`: backends CUDA/Vulkan/Metal (OpenCL e DirectML não documentados),
  modelos declarados vs. matriz de testes (não publicada) vs. relato comunitário na RX 580
  (SD1.5 ≈ 72 s; FLUX.1-schnell CPU+GPU ≈ 14 min).
- Consumo de memória re-derivado (pesos ≠ total); "cabe confortavelmente" removido.
- Hunyuan3D-Omni sem veredito (`UNVALIDATED`); TripoSR mantido como exceção CPU.

### FIX — método
- Vocabulário de evidência de 8 rótulos (`OFFICIAL_DOCUMENTATION`, `OFFICIAL_LICENSE`,
  `PAPER_OR_RESEARCH`, `COMMUNITY_REPORTED`, `TESTED`, `INFERRED`, `UNVALIDATED`, `BLOCKED`)
  no catálogo e na matriz; `CONFIRMED` retirado da matriz.
- Pix3D reescopado (reconstrução de objeto, estudo comportamental); interpretação de variância
  removida.
- Cinco fontes de prática identificadas por título/autor/URL/data, com qualidade declarada.
- Regra de "componente conexo" passou a ser **configurável por arquétipo**.
- Blender: `--background --python` roda **dentro** do processo; consequência de distribuição
  marcada `REQUIRES_LEGAL_REVIEW`.

### ADD — candidatos
- Reallusion Character Creator 5.2, GPT Image (OpenAI) e Google Flow no catálogo (§6-bis,
  §6.3, §6.4) e na matriz (3 linhas novas).

### DECISION — nenhuma
- Pipeline 2 reclassificado como **candidato prioritário para avaliação**, não padrão aprovado.
  Adoção continua decisão do proprietário.

---

## 2026-11-20 (3ª rodada) — criação de personagens: silhueta antes do 3D

Pesquisa pedida pelo Lia Forge 2.0. Nada foi implementado, nenhum peso baixado, nenhuma
ferramenta executada.

### ADD — 8 documentos Markdown (8 IDs) + 1 matriz em `cross-project/character-creation/`
- `CHARACTER-CREATION-RESEARCH.md` (`LR-STUDIO-007`): visão geral, matriz de reutilização do
  que já existia, conclusões e decisões pendentes.
- `SILHOUETTE-FIRST-DESIGN-RESEARCH.md` (`LR-STUDIO-008`): método, linguagem de forma, 8
  critérios de avaliação com nível de confiança e a fronteira automação/humano.
- `CHARACTER-SHEET-CONSISTENCY.md` (`LR-STUDIO-009`): vistas canônicas, 7 causas de
  inconsistência, técnicas por eficácia e QA automatizável.
- `CHARACTER-GENERATION-MODEL-CATALOG.md` (`LR-MODEL-007`): modelos de imagem, controle e 3D;
  **licença de código separada da licença de pesos**; veredito para a RX 580.
- `CHARACTER-2D-TO-3D-PIPELINES.md` (`LR-FORGE-007`): 12 critérios, três pipelines, e a
  distinção "visualmente convincente × geometricamente adequado × pronto para jogo".
- `CHARACTER-PRODUCTION-TOOLS-ASSESSMENT.md` (`LR-FORGE-008`): blockout → GLB, com licenças
  lidas (Blender GPL, Instant Meshes BSD, xatlas MIT, ArmorPaint zlib, MPFB2 própria).
- `CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md` (`LR-FORGE-010`): fronteira dos
  componentes, gates e retornos — **sem ter lido os contratos do Forge** (repo 404).
- `CHARACTER-CREATION-SKILLS-ANALYSIS.md` (`LR-AGENT-012`): 7 competências, 6 que não devem
  virar skill.
- `CHARACTER-CREATION-EVIDENCE-MATRIX.tsv`: 46 registros com licença, hardware, atividade e
  nível de evidência.

### Descobertas que mudam decisão
- **Windows + RX 580 não tem ROCm**: gfx803 não está na matriz do ROCm 10.2 e o HIP SDK para
  Windows não lista a RX 580 (marca até RDNA2 como não suportado).
- **Nenhum image-to-3D relevante roda sem CUDA**: TRELLIS 16 GB, TRELLIS.2 24 GB, Hunyuan3D-2.1
  29 GB, TripoSG 8 GB CUDA, InstantMesh CUDA ≥ 12.1, SF3D CUDA/MPS com VS 2022 no Windows.
- **`stable-diffusion.cpp` (MIT, Vulkan, build Windows)** é o único caminho local plausível
  para imagem — qualidade resultante não validada.
- **Licenças que excluem território**: Hunyuan Image 3.0 e Hunyuan3D 2.x não se aplicam à UE,
  Reino Unido e Coreia do Sul; o HF marca `extra_gated_eu_disallowed`.
- **`ACE++` não tem arquivo de licença** — código público não é licença.
- **Métricas geométricas não são veredito**: no Pix3D, Spearman de 0,32 (IoU), 0,43 (EMD) e
  0,49 (Chamfer) contra julgamento humano.

### NÃO validado (declarado nos documentos)
Desempenho em qualquer hardware AMD, qualidade de Tripo/Meshy/Rodin, tempo de CPU do TripoSR,
licença dos pesos de FLUX.2 e CharacterGen, contratos do Forge, e termos de Mixamo/MetaHuman.

## 2026-11-20 (2ª rodada) — validadores, proveniência e reauditoria técnica dos 22

### Validadores (FIX — sem fragilizar)
- `tools/validate.py` reescrito como classe: **data dinâmica** (`--today` / `LIA_TODAY` para
  teste reproduzível), 18 verificações, 3 níveis. `STALE` virou diagnóstico: o validador
  **nunca** reescreve relatório.
- Segredos: 18 padrões (GitHub, pat, OpenAI, Anthropic, Stripe, AWS key/secret, Google, Slack
  token e webhook, Discord, npm, **JWT**, chave privada OpenPGP/RSA, string de conexão,
  Azure, Bearer). Máscara `XXXX`/`0000` não é erro; "placeholder" na mesma linha **não**
  serve de passe livre (teste dedicado).
- Catálogo: comparação byte a byte contra o gerador → linha extra, linha faltando e célula
  editada à mão passam a ser erro.
- `tools/test_validate.py`: **76 testes** com fixtures temporárias (positivo, negativo, campo
  ausente, data vencida, `BLOCKED`/`NOT_RUN` legítimos, arquivo histórico, integração no repo
  real). Antes: 10.

### Proveniência (ADD)
- `audits/PROVENANCE-2026-11-20.md` + `data/inventory/provenance-2026-11-20.tsv`.
- Contagem corrigida: eram **5** objetos sem SHA, não 4.
- 21 de 23 com SHA de 40 caracteres no cabeçalho; `ai-memory` e `freellmapi` ficam como
  **candidato por data** (coincidem com o HEAD, mas não provam a árvore lida);
  `rescript-lang` e `routerhub` declarados **incompletos por serem organizações**.

### Reauditoria técnica (ADD)
- 22 relatórios receberam a seção `Reauditoria 2026-11-20`: versão anterior, versão
  examinada, mudanças, evidências, testes, conclusão e próxima revisão.
- 10 objetos com commit novo confirmado (**3.576 commits** no total, incluindo 4 de `freellmapi` medidos a partir do SHA candidato), 11 sem commit novo.
- **0 recomendações alteradas**; **1 motivo alterado**: `sculptforge` ganhou
  `LICENSE-EXCEPTION.md` (scripting), então o GPL deixou de bloquear script via API/CLI/MCP.
- `audits/TECHNICAL-REAUDIT-2026-11-20.md` com números, lacunas e limites do método.

### Testes próprios (ADD — 16 linhas no log)
- `ai-design-skills` 17/17 · `claude-bughunter` 65/65 · `cloudflare-security-audit-skill`
  65/65 (34+31) · `claude-trading-skills` 3.530/3.598 · `freellmapi` 2.044/3.840 (pares `PARTIAL`).
- 9 tentativas bloqueadas com motivo (`cargo`, `dotnet`, Blender, Manim, Python ≥3.14, HA), cada uma com linha no log.

### Fila (ADD)
- `RESEARCH-BACKLOG.md` §7: decisão escrita para os 17 triados e para os 6 candidatos;
  `uv` deduplicado; `promptfoo`/`deeval` no topo por atacarem a lacuna de **teste**.

## 2026-11-20 — `LR-STUDIO-006` pacote de Skills de game dev (23º objeto)

### Pesquisa nova (ADD)
- `LR-STUDIO-006` `gamedev-skills/awesome-gamedev-agent-skills@c6ca6c4` — 79 Skills + roteador,
  12 engines (Godot 4.7, Unity 6.3 LTS, Unreal 5.8, Phaser 4.2, PixiJS 8.22, three r187, Bevy
  0.20, pygame-ce, LÖVE, Defold, Roblox, Ebitengine). **ADAPT** — formato, validador de Skill e
  pipeline de asset; não o pacote inteiro. Apache-2.0 lida no arquivo, `NOTICE` com atribuição.
- Estado `PARTIALLY_TESTED`, resultado `LOCAL_SMOKE_PASS`: **primeira vez** que esta base
  registra execução de terceiro. 2 linhas em `data/testing/test-log.tsv`.
- Independência verificada: 7 versões pinadas conferidas contra as releases reais na API do
  GitHub (Godot 4.7.2, Ebiten 2.10.6, Bevy 0.20.1, Phaser 4.2.1, three r187, Defold 1.14.1,
  Luau 0.746) — todas existem.
- O que é alegação do autor, não nossa: "checked on the real engines" para 10 de 12 e 98,7% de
  disparo em 366 prompts. O próprio `evals/RESULTS.md` declara o que não rodou (Unity Editor,
  Unreal Editor, Roblox Studio, builds C# do Godot) e que julgou modelo, uma execução por célula.

### Transversal (CONSOLIDATE)
- `cross-project/agents/SKILLS-MCP-LANDSCAPE.md` §4: 7 práticas de autoria de Skill que fecham
  lacunas de `LR-AGENT-009`.
- `cross-project/licensing/ASSET-PROVENANCE-REGISTRY.md` §6-bis: manifesto + QA de raster
  (alfa falso) como duas checagens que faltam em P1–P8.
- `data/inventory/license-matrix.tsv` e `READY-TO-USE-LICENSES.md`: 22 → **23** objetos;
  alerta de que copiar uma pasta de Skill não leva `NOTICE`/`LICENSE` junto.

## 2026-11-20 — redefinição de missão, catálogo gerado e re-auditoria

Nada aqui é pesquisa nova sobre tecnologia: é a base arrumando a própria casa. Os 22
relatórios continuam com a mesma data de pesquisa (`2026-11-17`).

### Identidade e autoridade (ADD)
- `MISSION.md`: identidade permanente (departamento de P&D e avaliação técnica), limite de
  autoridade (pesquisa **recomenda**, não decide adoção) e a separação dos três conceitos.
- `agents/RESEARCH-ORCHESTRATOR.md` §0: o orquestrador não pode aprovar nada, em nenhum
  projeto, nem "só desta vez".
- Banner de limite de autoridade em 13 documentos de `governance/` e `agents/`.

### Protocolos novos (ADD)
- `governance/INVESTIGATION-PROTOCOL.md`: etapas A–E e tabela dos 6 erros que esta base
  já cometeu (triagem virando `DOCUMENTED`, etc.).
- `governance/TESTING-PROTOCOL.md`: níveis 0–3, 10 regras obrigatórias, registro de 10
  colunas em `data/testing/test-log.tsv`.
- `catalog/CATALOG-SCHEMA.md` + `catalog/catalog.tsv` (gerado por
  `tools/build_catalog.py`): 22 linhas, estado ≠ resultado ≠ recomendação ≠ decisão.
- 5 modelos novos em `templates/`: MCP, Skill, modelo, API/serviço, paper.

### Vocabulário (FIX, com migração registrada)
- 22 relatórios: `ADAPTAR`→`ADAPT`, `REFERÊNCIA`→`REFERENCE_ONLY`, `REJEITAR`→`REJECT`.
  `ADOTAR` não existia. Texto original preservado entre parênteses quando havia dois
  valores no mesmo campo (ex.: `LR-STUDIO-003` rejeita a stack e aceita referência de interop).
- `RESEARCH-INDEX.md` §1 ganhou coluna **Decisão de adoção** (vazia: pesquisa não decide) e
  passou a mostrar estado e recomendação em colunas separadas.
- `archive/superseded/RESEARCH-STATUS-AND-DECISIONS.md`: o texto antigo de 5 categorias
  foi arquivado, não reescrito.

### Reorganização (FIX)
- 7 relatórios de entrega movidos para `archive/historical/`; `LIA-RESEARCH-ROADMAP.md`
  fundido em `RESEARCH-ROADMAP.md` Partes A/B; `LIA-RESEARCH-INTAKE-2026-11-17.md` virou
  `RESEARCH-BACKLOG.md`. Raiz agora só tem entrada, missão, índice, roadmap, fila,
  changelog e licença. Todos os links corrigidos.
- `tools/__pycache__/` removido. `collect.py`, `enum2.py` e `fetch3.py` movidos para
  `archive/scripts/` (são scripts de sessão únicos, dependem de arquivos que não existem
  mais; ver README de lá).
- `archive/superseded/RESEARCH-STATUS-AND-DECISIONS.md` e demais órfãos agora linkados.

### Validador (FIX)
- `tools/validate.py` reescrito: 18 verificações em 3 níveis (ERRO bloqueia, AVISO pede
  revisão, NOTA é pendência legítima). Inclui ID↔índice, link local, órfão, cabeçalho
  completo, vocabulário fechado, teste declarado sem linha no log, catálogo dessincronizado,
  contagem de licenças e cache versionado.
- `tools/test_validate.py`: 10 testes, rodam em 5 ms (`python3 tools/test_validate.py`).

### Re-auditoria de upstream (ADD)
- `tools/check_upstream.py` + `data/inventory/upstream-reaudit-2026-11-20.tsv`:
  **22/22 objetos existem**, **10 com commits novos** desde a versão analisada, 0 links
  mortos. Cada relatório ganhou `| Upstream conferido |`.
- `audits/REAUDIT-2026-11-20.md` com a tabela completa e a lição do selo ≠ licença.

### Correções de contagem (FIX)
- `cross-project/licensing/READY-TO-USE-LICENSES.md`: 19 → **22** objetos (faltavam
  `LR-AGENT-011`, `LR-SEC-007`, `LR-MODEL-006`), conferido contra a matriz.
- `README.md`: 142 → 158 arquivos; estado da base atualizado; 0 testes declarado.

## 2026-11-17 — triagem de 20 itens + 3 relatórios publicados

### Triagem (ADD)
- `RESEARCH-BACKLOG.md`: os 20 itens recebidos classificados por prioridade
  (A/B/C), com licença, tamanho, o que é e o que falta. **Triagem não é relatório** — a
  própria tabela diz o que ainda não foi lido nem executado.
- 6 candidatos adicionais medidos por API para a próxima fila: `promptfoo`, `deepeval`,
  `langfuse`, `litellm` (upstream do gateway rejeitado em `LR-PROV-001`),
  `modelcontextprotocol/servers`, `astral-sh/uv`.

### Relatórios publicados (ADD)
- `LR-AGENT-011` `ai-memory` — memória multi-harness com **handoff que tem dono e é
  reivindicado uma única vez**, busca híbrida com vetor opcional, e privacidade decidida
  antes de armazenar (servidor recebe só harness + identidade da sessão). **ADAPTAR**.
- `LR-SEC-007` `cloudflare/security-audit-skill` — 143 KB, ★75.939: 11 classes de ataque
  (incluindo **desktop/IPC local** e **AI/LLM**) + `report-schema.json` + **dois validadores
  com teste**. Primeira Skill lida por esta base cujo resultado é verificado por código.
  **ADAPTAR**.
- `LR-MODEL-006` `freellmapi` — 87 free tiers num `/v1` com roteamento, failover e orçamento
  por chave. **REFERÊNCIA**: o desenho serve ao Model Lab; o serviço não pode virar
  dependência de produto (o repo se declara "personal experimentation only").

### Integrações
- `license-matrix.tsv`: 22 linhas.
- Roadmap: A-9 (handoff), A-10 (schema de achado), M-6 (orçamento por chave).
- Índices de Project, Studio, Hub e Model Lab apontam para os novos IDs.

## 2026-11-17 — novo objeto externo: BRUTAL (framework C#/Vulkan)

### Pesquisa nova (ADD)
- `LR-STUDIO-005` `ahwootech/BRUTAL@c4c62f55` — framework de jogo em C#/.NET 10 sobre
  Vulkan, base do motor *Waylith* (RimWorld) e da Kitten Space Agency. ★2.527.
  Veredito **REFERÊNCIA**: sem caminho técnico para a stack Lia; três práticas a adaptar.

### Achados (ADD)
- **Licença própria** `BRUTAL License v1.0`: base MIT **+ créditos + logo obrigatório
  antes do gameplay + `NOTICE.txt`**, e **não é OSI** (o README admite). "Open source" no
  README não é tipo de licença.
- **Política de contribuição assistida por IA** (B1): pode usar agente, mas responde por
  cada linha, declara no PR, e PR grande/não testado/inexplicado é fechado — cláusula que
  faltava em `agents/`.
- **`LICENSES/` por pacote publicado** (B2): o aviso viaja com o que redistribui.
- **Código não compila no repo**: 0 `.csproj`, 0 `.sln`; 5.070 de 5.644 `.cs` são gerados;
  1 único workflow (bot de boas-vindas).
- **Hardware:** exige Vulkan 1.3; suporte na RX 580 fica `UNVERIFIED` até rodar
  `vulkaninfo` (`LR-HW-001`).

### Integrações (CONSOLIDATE)
- `LR-LIC-005` §3.5: nova família de licença (permissiva com atribuição gráfica) + ficha.
- `data/inventory/license-matrix.tsv`: 19ª linha.
- `RESEARCH-ROADMAP.md`: A-8 (política de IA em contribuição).

## 2026-11-17 — licenças prontas para uso (o projeto não reabre a pesquisa)

### Pesquisa nova (ADD)
- `LR-LIC-005` `cross-project/licensing/READY-TO-USE-LICENSES.md`: os 18 objetos com
  **obrigação traduzida em ação** — pode usar / pode fork / o que colar. Quatro modelos
  de `NOTICE` prontos (MIT, Apache-2.0, CC BY 4.0 TASL, GPL como processo separado) e
  ficha de leitura rápida por objeto.
- `data/inventory/license-matrix.tsv`: 18 linhas × 15 colunas, consumível por script.

### Decisão preparada (ADD)
- `DR-0001` ganhou três opções com consequência explícita (MIT / Apache-2.0 / manter sem
  licença), para o proprietário **só escolher**. Recomendação registrada como `INFERRED`:
  Apache para código, MIT para conteúdo curto, e `license:` dentro de cada Skill.

### Achados (ADD)
- Os **cinco repositórios dos apps são públicos e sem `LICENSE`** → hoje "todos os
  direitos reservados": 48 Skills legíveis por qualquer pessoa, sem permissão formal.
- Fronteiras que exigem leitura: GPL × programa separado, CC-BY-SA no ManimGX, fontes
  fora da MIT no pixelfx, Vercel Beta Terms.

## 2026-11-17 — revisão de base (o que temos aqui × o que já existe nos apps)

### Revisão (REVIEW)
- `archive/historical/LIA-RESEARCH-BASELINE-REVIEW-2026-11-17.md`: re-leitura crítica com números **medidos
  hoje**, não herdados. Estado: 136 docs · 18 objetos (7 ADAPTAR · 8 REFERÊNCIA ·
  3 REJEITAR · **0 ADOTAR**) · 30 digests · 18 DRs · 14 repos públicos · 43 branches ·
  **1.148** Markdown em `main` nos cinco apps (cobertura ~1:8, agora declarada no README).

### Correções (FIX — achados da própria revisão)
- **D1:** o ACCESS doc afirmava que os cinco repositórios de produto eram privados.
  São **públicos** (`visibility: public` verificado nos cinco). Texto corrigido, com a
  consequência registrada: a exposição pública não é só desta base.
- **D2:** `RESEARCH-INDEX.md` §3 anunciava "(17)" com 30 linhas.
- **D3:** `RESEARCH-INDEX.md` §4 anunciava "(13 abertas)" com 12.
- **D4:** cobertura 1:8 (136 ↔ 1.148) declarada no `README.md` §1.
- **Regressão registrada:** D1 foi erro introduzido nesta sessão; o
  `ecosystem/ECOSYSTEM-MAP.md` já dizia "todos os 14 repositórios são públicos".

### Conclusão da revisão (ADD)
- Autocrítica F1/F2: **0 ADOTAR em 18 objetos** e **5 propostas sem nenhuma execução** —
  a base é hoje mais opinião documentada que medição.
- Maior risco apontado: **48 Skills sem licença em cinco repositórios públicos**
  (`DR-0001` aberto).

## 2026-11-17 — acesso público explicitado + pacote de Skills ArtCraft

### Correção (FIX)
- **A base já era pública; os documentos ainda deixavam dúvida.** `DR-0002` dizia
  "não autoriza tornar o repositório público" — vencido por `DR-0006` (ACCEPTED).
  Reescrito: leitura **aberta e sem token**; restam abertas só publicação, revisão,
  cópia local e logs. Opções de deploy key/GitHub App retiradas do caminho de leitura.
- `archive/historical/LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md`: cabeçalho corrigido (visibilidade
  `DR-0006`; publicação `DR-0002`) e nova §3-bis com **acesso sem token** — URLs raw,
  API não autenticada, clone de leitura, e a distinção entre esta base (pública) e os
  cinco repositórios de produto (privados, exigem `gh`).
- Ajustados `README.md` §6, `archive/superseded/RESEARCH-STATUS-AND-DECISIONS.md`,
  `ecosystem/PROJECT-OWNERSHIP.md`, `archive/superseded/LIA-RESEARCH-ROADMAP.md`, `decisions/PENDING/README.md`
  e `archive/historical/LIA-RESEARCH-PHASE-CLOSURE-REPORT.md` para não descrever `DR-0002` como bloqueio de leitura.

### Pesquisa nova (ADD)
- `LR-AGENT-010` — **pacote de 8 Skills de edição** sobre os apps ArtCraft
  (`cross-project/agents/ARTCRAFT-SKILL-PACK.md`). Apps da ArtCraft são **mais uma opção**:
  quem decide habilitar é o usuário.

### Correção de rumo (FIX — v1.1 de `LR-AGENT-010`)
- A v1 tratava "edição ≠ geração" como **regra dura de produto** ("é proibido cair em
  gerador"). **Justificativa da mudança:** por instrução do proprietário, usar os apps da
  ArtCraft é opção adicional e a decisão é do usuário, não da pesquisa. Pesquisa registra
  trade-offs; não promulga regra de produto.
- O que permanece como requisito **técnico**: declarar app/versão, declarar raízes,
  falhar de forma explícita (nunca silenciosa), não escrever fora da raiz, registrar
  proveniência e custo. `UNAVAILABLE` passou de "proibição de alternativa" a **estado
  informado**, com o próximo passo decidido pelo produto/usuário.
- `data/inventory/artcraft-automation-surface.tsv` — superfície de automação verificada
  de PhotoCraft, PdfCraft e VectorCraft (as outras 14 apps ficam `UNVERIFIED`).

### Achados (ADD)
- A suíte usa **as mesmas flags** de raiz em todos os apps, mas **nomes de ferramenta
  divergem** (`doc_open` × `open_file`, `command_run` × `run_command` × `invoke_menu`) →
  uma Skill por app, nunca um "contrato único" de tools.
- O launcher expõe **uma** entrada MCP (`ArtCraft`) para todos os apps instalados, com
  consentimento global desligado por padrão.
- `command_batch` não é transação e `edit.undo` não desfaz escrita em disco — a Skill
  precisa separar editar de salvar.

### Validação (ADD)
- V1–V5 por desenho; **V6 `NOT RUN`** — nenhum app ArtCraft foi instalado ou executado.
- `tools/validate.py`: 135 arquivos, 0 erros, 0 avisos.

## 2026-11-17 — novo objeto externo: ArtCraft (17 apps criativos)

### Pesquisa nova (ADD)
- `LR-STUDIO-004` `storytold` / ArtCraft — 17 apps criativos nativos em Rust, **186 crates**
  compartilhados, launcher próprio, MCP embutido por app. Veredito **ADAPTAR** (desenho, não código).

### Achados (ADD)
- **Barramento único de comandos**: UI, CLI, protocolo JSON e MCP despacham no mesmo registro.
- **Autoridade de agente por lançamento**: read/write roots explícitos, bearer token em
  arquivo privado, loopback, switch de consentimento **desligado por padrão** — e a frase
  "tool schemas are not authorization boundaries".
- **Lacuna admitida no próprio repo**: sem capability por comando; endurecimento proposto, não implementado.
- **Contrato de IA tipado** (`Role`/`Capability`/`InputRole`) com “falhar explícito, nunca
  substituir o motor silenciosamente”, consentimento, jobs e segredos fora do JSON compartilhado.
- `craft-docpath`: caminho guardado em documento só abre local ou no próprio share.
- Dual `MIT OR Apache-2.0`, mas metadado do GitHub declara só Apache (mesma classe de erro de `LR-SEC-006`).
- Vizinhos medidos: Graphite ★27.981 Apache-2.0 · Penpot ★62.523 MPL-2.0 · ComfyUI ★147.500 **GPL-3.0**.

### Integrações (CONSOLIDATE)
- `RESEARCH-ROADMAP.md`: novas linhas U-4 (comando único) e U-5 (roots/consentimento).
- Índices de Studio, Forge, Agent Hub e Model Lab apontam para `LR-STUDIO-004`.

## 2026-11-17 — novo objeto externo: Claude-BugHunter

### Pesquisa nova (ADD)
- `LR-SEC-006` `elementalsouls/Claude-BugHunter@b63ae349` — 83 Skills, 15 comandos,
  341 arquivos, ★11.020, **licença dupla MIT + CC BY 4.0**. Veredito **REFERÊNCIA**:
  o conteúdo ofensivo não serve ao produto; seis mecanismos de engenharia servem a todos
  os projetos (R1 eval com ablação · R2 denylist hasheada fail-closed · R3 doc-count-check
  · R4 skill-lint + roteamento · R5 licença por classe de arquivo · R6 manifesto de plugin).

### Achados (ADD)
- O repo publica **baseline negativo honesto**: skills ligadas × desligadas = **delta +0%**,
  custo +US$ 0,076, com "ceiling effect" declarado — raro e educativo.
- Duas inconsistências de licença internas: `NOTICE` × `credits.md` sobre redistribuição, e
  `plugin.json` declarando só `MIT` para conteúdo que é CC BY 4.0.
- `plugin.json` declara credencial com `sensitive: true` e servidor MCP com `env` — precedente
  real para `LR-AGENT-009` e `LR-MCP-002`.

### Integrações (CONSOLIDATE)
- `LR-AGENT-009` §9: V6 ganhou precedente implementado (eval + lint/roteamento).
- `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md` §7-bis: melhoria da varredura (R2).
- `governance/LICENSE-AND-PROVENANCE-POLICY.md` §2: modelo de licença por classe de arquivo.
- `RESEARCH-ROADMAP.md`: novas linhas L-4b e L-5.

## 2026-11-17 — 2ª rodada: fechamento das lacunas prioritárias

### Pesquisa nova (ADD)
- `LR-MODEL-005` **matriz capability × provider** (`cross-project/model-routing/CAPABILITY-PROVIDER-MATRIX.md`):
  54 definições de provider lidas em `Lia-Project@005a324`; 33 `chat`, 13 `text-to-speech`,
  3 `speech-to-text`, **0 `embed`** declarados. Dados brutos em `data/inventory/provider-tasks.tsv`.
- `LR-LIC-003` **auditoria das 28 Skills AIRI + Alethe**
  (`projects/lia-agent-hub/skills/AIRI-AND-ALETHE-PROVENANCE.md`): 50 `SKILL.md` lidos,
  5 licenças, parecer por Skill — 4 `USE_AS_IS`, 5 `ADAPT_ALLOWED`, **19 `RESEARCH_ONLY`**.
  Dados brutos em `data/inventory/skills-provenance.tsv`.
- `LR-AGENT-009` **manifesto de workflow** e `LR-SEC-005` **permissões por execução** e
  `LR-LIC-004` **registro de proveniência de asset** e `LR-UI-005` **ADR de interface** —
  todos marcados **PROPOSTA/PROCEDIMENTO**: nenhum implementado.

### Achados novos (ADD)
- Embedding implementado em `lm-studio` e **invisível** no catálogo de capabilities.
- Anthropic declarada OpenAI-shaped: única das 10 onde "suportado" pode ser falso em runtime.
- 8 Skills AIRI declaram autor, **nenhuma** declara licença; só 5 têm `LICENSE` no payload.
- `lia-eventa-ipc` é a **única** Skill Lia com licença (`MIT`) — as outras 20 não têm.

### Decisão do proprietário (DECISION)
- `DR-0006` movido de `PENDING` para `ACCEPTED`: repositório permanece **público**,
  consumo read-only para agentes de projeto (`Lia-Research@c9e6e97`). Documentos que diziam
  "privado" foram corrigidos: `README`, `SECURITY-AND-PRIVACY-POLICY` §6,
  `RESEARCH-METHODOLOGY`, `QUALITY-AUDIT`, `RESEARCH-STATUS-AND-DECISIONS` (arquivado em 2026-11-20).

### Segurança pública (ADD + FIX)
- `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md`: 11 classes varridas em 131 Markdown,
  4 TSV e no snapshot. 3 achados, 2 tratados, 0 pendentes.
- **Snapshot sanitizado**: `LIA-AGENT-CONSUMPTION-AUDIT.local.md` excluído (caminho de
  usuário, IDs de sessão, contagem de tokens) e 3 e-mails de autores de add-ons redigidos.
  236 → 235 arquivos; manifesto regerado com cabeçalho de sanitização.

### Correções de registro (FIX)
- "29 skills AIRI" → **28 AIRI + 1 Alethe** (a contagem anterior agregava o `alethe`).
- "13 decisões abertas" → **12 abertas + 1 aceita**.
- "118/124 arquivos Markdown" → **131** (contagem de 2026-11-17).
- `ECOSYSTEM-MAP.md` §5: 228 → **349** commits de atraso da `main` do Lia-Project.
- Trilha R do roadmap: R-1 `NOT RUN` (fonte parcial), R-2/R-3/R-4 `SKIP` com motivo,
  R-5 `NOT RUN`. Nenhum diretório vazio criado.

### Observado (não registrado como decisão)
6 das 12 branches `arena/*` do Lia-Project foram podadas entre 2026-11-17 15:00 e 22:00 —
o snapshot de `data/` deixou de ser conveniência e passou a ser a única cópia de 236
documentos. Nenhum documento desta base dependia das branches removidas.

## 2026-11-17 — Fundação inicial (fase 0–3)

### Governança e método (ADD)
- `governance/` — 8 documentos: governança, metodologia, padrões de evidência, licença e
  proveniência, segurança e privacidade, preservação de fonte, status e decisões,
  fluxo de contribuição.
- `templates/` — 9 modelos (avaliação de tecnologia em 18 seções, pesquisa de repositório,
  análise de arquitetura, auditoria de segurança, auditoria de licença, benchmark,
  comparação, registro de decisão, inventário de fonte).
- `agents/` — 5 papéis/protocolos: orquestrador, especialistas, fluxo, publicação, revisão.

### Levantamento do ecossistema (ADD)
- 58.478 arquivos, 43 branches, **1.620 documentos distintos**, 511 fora de `main`,
  975 vendorizados, 645 de autoria Lia — ver `ecosystem/ECOSYSTEM-MAP.md`.
- `ecosystem/CROSS-PROJECT-CAPABILITIES.md`: 49 capabilities no Forge, 10 tools MCP,
  44 modelos catalogados, **0 validados**.

### Pesquisa externa (ADD — 16 objetos)
- `LR-MCP-001` HA-MCP **ADAPTAR** + 4 documentos derivados (arquitetura, risco, contrato, plano).
- `LR-AGENT-001` OpenJarvis **REFERÊNCIA** · `LR-UI-001` Vercel UI **ADAPTAR** ·
  `LR-FORGE-001` MDM **REFERÊNCIA** (GPL) · `LR-AGENT-002` Trading Skills **ADAPTAR** ·
  `LR-STUDIO-001` OpenIDEA **REFERÊNCIA** · `LR-PROV-001` RouterHub **REJEITAR**.
- `LR-FORGE-002` SculptForge **REFERÊNCIA** (GPL) · `LR-STUDIO-002` Game Studios **ADAPTAR** ·
  `LR-FORGE-003` ManimGX **REFERÊNCIA** · `LR-AGENT-003` Meldwork **REFERÊNCIA** ·
  `LR-UI-002` Plannotator **REFERÊNCIA** · `LR-FORGE-004` pixelfx **ADAPTAR** ·
  `LR-AGENT-004` unslop **REJEITAR** · `LR-STUDIO-003` ReScript **REJEITAR** ·
  `LR-UI-003` AI Design Skills **ADAPTAR**.

### Dossiês internos (ADD)
- `projects/{lia-project,lia-forge,lia-studio,lia-agent-hub,lia-model-lab}/{README,INDEX}.md`.

### Consolidação transversal (CONSOLIDATE — 21 digests)
- Hardware (2) · modelos (4) · voz (1) · segurança (3) · UI (1) · agentes (4) ·
  MCP (2) · casa (1) · download (1) · licença (2) · memória (1) · storage (1) · automação (1).
- `LR-LIC-001`: 48 Skills catalogáveis, **0 com licença no payload** — o achado mais
  consequente da fundação.

### Decisões (DECISION)
- 13 registros `PENDING` abertos (DR-0001…DR-0004, DR-0006…DR-0014).
- 3 `REJECTED` (RouterHub, unslop, ReScript) e 2 `REFERENCE-ONLY` (OpenJarvis, ferramentas de criação).
- `ACCEPTED/` e `ADAPTED/` vazios **por desenho**: a ordem de serviço proíbe o agente de
  promover pesquisa a implementação.

### Dados (ADD)
- `data/` — inventário comprimido (58.478 arquivos, 1.620 docs), manifesto do corpus (236
  arquivos com SHA), 14 alvos externos pinados, snapshot do corpus (1,7 MB).

### Bloqueios (BLOCKED)
- Visibilidade privada do repositório: `403` na API. Registrado em `DR-0006`.

### Correções (FIX)
- Contagem de documentos "1.620 não estão em `main`" era bug de comparação de SHA curto;
  o correto é **511 fora de `main`**.
- `Lia-Agent-Hub` não existe: o repositório é **`Lia-AgentHub`**.
- `unslop` não tem licença (badge ausente **não** significava "verificar depois": é 404).
- `rescript` tem licença mista: `compiler/` é LGPL-3.0-or-later (badge "Other" escondia).
