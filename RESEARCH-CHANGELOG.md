# RESEARCH-CHANGELOG

Registro append-only do que entrou na base. Ordem inversa (mais recente primeiro).
Cada linha: data · tipo · item · efeito.

Tipos: `ADD` (pesquisa nova) · `FIX` (correção) · `CONSOLIDATE` (digest) · `DECISION` ·
`BLOCKED`.

---

## 2026-11-17 — revisão de base (o que temos aqui × o que já existe nos apps)

### Revisão (REVIEW)
- `LIA-RESEARCH-BASELINE-REVIEW-2026-11-17.md`: re-leitura crítica com números **medidos
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
- `LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md`: cabeçalho corrigido (visibilidade
  `DR-0006`; publicação `DR-0002`) e nova §3-bis com **acesso sem token** — URLs raw,
  API não autenticada, clone de leitura, e a distinção entre esta base (pública) e os
  cinco repositórios de produto (privados, exigem `gh`).
- Ajustados `README.md` §6, `governance/RESEARCH-STATUS-AND-DECISIONS.md`,
  `ecosystem/PROJECT-OWNERSHIP.md`, `LIA-RESEARCH-ROADMAP.md`, `decisions/PENDING/README.md`
  e `LIA-RESEARCH-PHASE-CLOSURE-REPORT.md` para não descrever `DR-0002` como bloqueio de leitura.

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
  `RESEARCH-METHODOLOGY`, `QUALITY-AUDIT`, `RESEARCH-STATUS-AND-DECISIONS`.

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
