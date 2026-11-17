# RESEARCH-CHANGELOG

Registro append-only do que entrou na base. Ordem inversa (mais recente primeiro).
Cada linha: data · tipo · item · efeito.

Tipos: `ADD` (pesquisa nova) · `FIX` (correção) · `CONSOLIDATE` (digest) · `DECISION` ·
`BLOCKED`.

---

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
