# RESEARCH-CHANGELOG

Registro append-only do que entrou na base. Ordem inversa (mais recente primeiro).
Cada linha: data · tipo · item · efeito.

Tipos: `ADD` (pesquisa nova) · `FIX` (correção) · `CONSOLIDATE` (digest) · `DECISION` ·
`BLOCKED`.

---

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
- 10 objetos com commit novo (**3.917 commits** no total), 11 sem commit novo.
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
