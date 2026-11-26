# Conferência dos índices operacionais com as `main` atuais — 2026-11-26

| Campo | Valor |
|---|---|
| Objeto | `projects/*/INDEX.md` e `projects/*/README.md` desta base (os "índices operacionais"), contra as `main` reais de `BloomRX/Lia-Project`, `BloomRX/Lia-AgentHub`, `BloomRX/Lia-Studio` e `BloomRX/Lia-Forge` |
| Tipo | auditoria de ponteiros, não pesquisa nova |
| Data | 2026-11-26 |
| Método | `gh api` (repositório, `git/trees/HEAD?recursive=1`, `contents/<path>`, `commits?per_page=1` com paginação, `branches?per_page=100`, `search/code`) lido **nesta sessão**; sem clone dos projetos; nenhuma escrita fora desta base |
| Escopo declarado | conferir contratos publicados; separar **entrega concluída** × **integração pendente** × **validação não executada**; corrigir ponteiros/resumos; preservar os relatórios históricos |
| Não verificável | `BloomRX/Lia-Forge` (`403 Resource not accessible by integration`) e `BloomRX/Lia-Model-Lab` (`404`) — ver §5 |
| Recomendação | ADAPT (as correções de ponteiro já aplicadas; nenhuma recomendação técnica foi alterada) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN (nada executamos nos projetos; só leitura de API) |

---

## 1. O que mudou no mundo desde que os índices foram escritos

Os cinco dossiês de projeto foram escritos em 2026-11-17 e revisados em 2026-11-20, quando o estado
era "cada produto tem uma `main` documental e uma ou mais branches de sessão com o código". Em
**2026-11-26** os três produtos visíveis fizeram, cada um, uma consolidação que **removeu as branches**:

| Projeto | HEAD da `main` medido hoje | Data | Commits | Branches no remoto | Entradas na árvore | Blobs | `.md` | `docs/**` |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `Lia-Project` | `72c44425` | 2026-11-26T07:20:39Z | 833 | **1** | 798 | 674 | 214 | 192 |
| `Lia-AgentHub` | `8c14ec85` | 2026-11-26T08:57:25Z | 202 | **1** | 199 | 165 | 50 | 78 |
| `Lia-Studio` | `0e7b9949` | 2026-11-26T09:20:01Z | 115 | **1** | 226 | 210 | 83 | 88 |

Cabeçalho do commit do Project: *"Aplica a Foundation V1.1 ao desktop e registra a validação
integrada"*; do Hub: *"docs: record completed branch cleanup and verified history backup"*; do Studio:
*"docs: registra integração e encerramento da branch do Studio"*. Três documentos de registro, lidos
inteiros nesta sessão:

- `Lia-AgentHub@main:docs/operations/BRANCH-CONSOLIDATION-2026-11-26.md` — `main` avançou
  `34a27f4 → c81d850` por fast-forward, quatro branches `arena/*` removidas, snapshot
  2026-11-26T08:37:35Z, ZIP de backup 13.462.694 B (`sha256 a4d33b5d…`), bundle 3.542.500 B, `fsck` e
  restauração verificados.
- `Lia-Studio@main:docs/BRANCH-CLEANUP-2026-11-26.md` — PR #1 **merged** em `12dccf06` (pais
  `d97a8bc5` + `8b17dffd`), árvore publicada `4d136f43` igual à candidata validada, **oito** branches
  removidas, mesmo ZIP de backup e `Lia-Studio.bundle` (`0cf03783…`), e **sete pesquisas históricas
  recuperadas** para `docs/research/` com os bytes originais preservados.
- `Lia-AgentHub@main:docs/BRANCH-AND-RELEASE-FLOW.md` — novo contrato de fluxo: `main` contém código
  **e** documentação canônica; branches Arena são **temporárias**; Codex é o integrador; antes de remover
  branch, registrar SHA e destino da entrega e preservar conteúdo exclusivo em arquivo histórico
  verificável. O documento diz explicitamente que **substitui a regra inicial de "Arena permanente e
  `main` apenas documental"** — que era exatamente o pressuposto em que os nossos índices foram escritos.

Consequência estrutural: quando a branch some, o ponteiro "está na branch X" deixa de ser um endereço
e passa a ser ou uma integração concluída ou uma perda coberta só pelo backup. É por isso que este
documento classifica linha por linha.

## 2. Classificação por projeto

Categorias, fixadas assim neste documento:
**ENTREGA CONCLUÍDA** = o artefato está na `main` e bate com o que a base descreve;
**INTEGRAÇÃO PENDENTE** = a base produziu/apontou, e a `main` não tem (ou tem em versão diversa);
**VALIDAÇÃO NÃO EXECUTADA** = está na `main`, mas sem evidência de execução do que ele afirma.

### 2.1 Lia-Project

| Item | Classe | Evidência medida hoje |
|---|---|---|
| `docs/research/LIA-WINDOWS-AMD-MODEL-COMPATIBILITY.md` (14.133 B), `LIA-LFM3-EVALUATION.md` (17.809 B), `2026-11-14-runtime-resource-research.md` (32.301 B), `LIA-ORNITH-WEIGHTS-RESEARCH.md` (9.427 B) | **ENTREGA CONCLUÍDA** | presentes na `main`; o `docs/reports/LIA-RESEARCH-TRANSFER-RECONCILIATION.md` deles (10.452 B, lido) classifica os quatro como **`Research reference`**, cópia byte a byte, "nenhum documento classificado como Canonical nesta rodada" |
| `docs/reports/LIA-RESEARCH-TRANSFER-RECONCILIATION.md` e `LIA-RESEARCH-DOCUMENT-TRANSFER-REVIEW.md` (10.452 / 10.868 B) indexados em `docs/README.md` | **ENTREGA CONCLUÍDA** (é o contrato de transferência publicado) | `docs/README.md:42` lista a reconciliação como linha de índice |
| `docs/research/LIA-MODEL-PROVIDER-CATALOG.md` (29.719 B), `LIA-MODEL-PROVIDER-ARCHITECTURE.md` (19.456 B), `LIA-MODEL-PROVIDER-RECOMMENDATIONS.md` (14.842 B) | **INTEGRAÇÃO PENDENTE** — os três foram marcados `Pending transfer` pelo próprio Project e **estão na `main` sem terem sido reconciliados com `lia-capability-catalog/`** | presentes na árvore; reconciliação deles pede "extrair delta", não "manter os dois catálogos" |
| `docs/reports/LIA-VALIDATION-MATRIX-5EC464E-2026-11-14.md` | **INTEGRAÇÃO PENDENTE** — único documento da nossa lista §2 que **não** está na `main` | busca na árvore: ausente |
| `docs/architecture/LIA-NATIVE-PROVIDER-COVERAGE.md` (101.866 B), `LIA-STAGE-DEPENDENCY-MAP-2026-10-28.md` (79.050 B), `LIA-NEXT-DECOUPLING-PLAN.md` (52.322 B), `docs/reports/LIA-DESKTOP-ARCHITECTURE-AUDIT-2026-11-16.md` (70.526 B), `LIA-UI-UX-AUDIT-2026-11-14.md` (50.886 B), `LIA-BETA-READINESS-PLAN-2026-11-14.md` (54.515 B), `LIA-GLOBAL-BRANCH-RECONCILIATION-2026-11-16.md` (28.268 B), `docs/architecture/decisions/DECISION-RECORD-2026-11-16.md` (23.078 B), `docs/reports/LIA-STT-SECURITY-AUDIT-2026-11-14.md` (17.986 B) | **ENTREGA CONCLUÍDA** — os nove "permanecem apenas na origem" do nosso índice **estão na `main`** hoje, alguns maiores do que registramos (66→70,5 KB; 100→101,9 KB) | medidos na árvore; our §2 corrigido em `projects/lia-project/INDEX.md` |
| Skills: 21 `SKILL.md` em `.agents/skills/`, **1** com `LICENSE` (`alethe/LICENSE`, 1.069 B) | **VALIDAÇÃO NÃO EXECUTADA** quanto ao gate de licença: a exceção da `alethe` existe mas nada valida o payload; e a nossa frase "22/22 sem licença" está **errada** | contagem na árvore |
| `lia/core/src/memory/{contracts,store,context}.ts` (1.355 / 8.791 / 2.132 B) + `lia/core/test/memory-store.test.ts` (6.811 B) | lido como código-fonte na `main` hoje; base do `LR-CMP-006` §2 | não executamos o teste deles (sem `pnpm`/Node build aqui) → **VALIDAÇÃO NÃO EXECUTADA** por nós |

### 2.2 Lia-AgentHub

| Item | Classe | Evidência |
|---|---|---|
| **Contratos publicados na `main`**: `docs/architecture/CAPABILITY-INVENTORY-CONTRACT.md` (`inventoryVersion: 1`; `revision` = "mesmo valor e digest diferente é conflito"; `complete` = "omissões nunca apagam registros"), `docs/architecture/SUPERVISED-EXECUTION-V1.md` + `docs/schemas/supervised-execution-v1.schema.json`, `docs/examples/**` (incl. `intake/demo-conflict-same-revision.json`), `docs/operations/INVENTORY-INTAKE.md`, `CENTRAL-CAPABILITY-GOVERNANCE.md` | **ENTREGA CONCLUÍDA** — e é a primeira vez que a base vê esses contratos: nenhum dos nossos índices os lista | cabeçalho e tabela de envelope lidos por API nesta sessão |
| `LIA-SKILLS-INVENTORY.md`, `SKILL-LICENSE-AND-PROVENANCE-AUDIT.md`, `THIRD-PARTY-SKILLS-CATALOG.md` e `LIA-SKILLS-ROADMAP.md` (os quatro em `docs/research/`), os `.records.json` e o `sources.json` de `catalog/`, e `Lia-AgentHub:tools/build-catalog-records.py` (caminhos do Hub, não desta base) | **INTEGRAÇÃO PENDENTE — com dois ponteiros quebrados, e não um**: os quatro documentos estão alcançáveis por SHA no commit `bd4bfbb9ed8065be1e571940926d293689985682` (a ponta da `arena/1a7ed773-lia-agenthub`, removida em 2026-11-26), medidos hoje em 37.825 / 37.125 / 34.294 / 21.216 B. `catalog/` inteiro e `Lia-AgentHub:tools/build-catalog-records.py` **não estão na `main` (404) nem nesse commit** (a árvore dele tem 26 blobs e nenhum `catalog/`) — esse ponteiro já estava quebrado antes da limpeza, e a única via de recuperação declarada é o ZIP/bundle do registro de consolidação | `gh api git/trees/bd4bfbb9…?recursive=1` e `contents/<path>?ref=main`, os dois lidos nesta sessão; `docs/operations/BRANCH-CONSOLIDATION-2026-11-26.md` para o backup |
| `docs/DECISION-REGISTER.md` (38.258 B) | **ENTREGA CONCLUÍDA** — a "versão dupla divergente" que registrávamos deixou de existir: um arquivo só, e a seção *Referências* cita `INTEGRATION-CANDIDATES.md` nomeando **MCPVault e ai-memory** como evidência externa do próprio Hub | lido por API; §3 `grep` na árvore |
| Skills no payload do Hub | **NENHUMA**: `0` `SKILL.md`, `0` `LICENSE`, sem `.agents/` na `main` — o Hub é registro/contrato, e a autoria de Skills foi movida para lá do Studio (`docs/windows-evidence/HUB-SKILLS-FOLLOWUP.md`: "O Studio não restaura a autoria dessas Skills: o Agent Hub as gerencia") | contagem na árvore |
| Piloto do Lia-Project no Hub (`docs/operations/LIA-PROJECT-PILOT-HANDOFF.md`) | **VALIDAÇÃO PARCIAL EXECUTADA POR ELES, NÃO POR NÓS**: 28 Skills materializadas, verificador recusando Skill sem `SKILL.md`, 28 pins / 7 testes / 88 subtestes passando em checkout Windows `J:/Lia/migration/agent-hub/project-pilot-3153c8b` @ `807c0b1`; **corte remoto pendente**; 23 de 51 Skills fora do corte (20 por origem/licença, `alethe` com componentes pendentes, `upload-github-attachment` com modo executável, `minecraft-debug-mcp` sem prova de carregamento) | documento lido inteiro nesta sessão |
| CI | três checks do commit `c81d850` aprovados (pytest Ubuntu, pytest Windows, verificação do pacote Windows) — `REPORTED` pelo registro deles, **não** conferimos o run | idem |

### 2.3 Lia-Studio

| Item | Classe | Evidência |
|---|---|---|
| As 12 pesquisas da nossa §2 ("mantidas na origem", branch `sessão`) | **ENTREGA CONCLUÍDA** — todas as 12 estão na `main` hoje, sete delas *recuperadas* exatamente para os caminhos originais sem alterar bytes dos blobs | árvore + `docs/BRANCH-CLEANUP-2026-11-26.md` |
| `docs/INDICE-DOCUMENTOS.md` e `planejamento/*` (nossos "2 versões divergentes"/"`CONFLICTING` de tamanho") | **ENTREGA CONCLUÍDA** — um arquivo de índice (3.730 B) e 5 arquivos em `planejamento/`, cada um uma vez | árvore |
| `docs/MULTI-AGENT`, fronteira Forge: o README deles **deixa de afirmar** que o contrato Forge não foi publicado; a limitação atual é "a integração ainda não validada do editor com esse contrato e com o runtime Lia" | **ENTREGA CONCLUÍDA** para o contrato; **VALIDAÇÃO NÃO EXECUTADA** para a integração editor × contrato | trecho lido do registro de limpeza |
| Validação da integração, executada **por eles** em Linux (Python 3.12.14, Node v24.22.3, 2026-11-26): `verify_alpha.py --part 1..10` verdes com **314 testes Python + 8 pulados**, `test_project_cli.py -q` 21, `test_creation.py -q` 23, servidor em `127.0.0.1` com HTTP 200 em `/`, `/api/health`, `/api/projects`, `/static/animation.html` | **VALIDAÇÃO EXECUTADA, MAS NÃO POR NÓS** — e os 8 pulados são 7 testes de Windows Job Objects + 1 de Godot real no Windows | tabela no registro de limpeza |
| Evidência Windows na `main`: `docs/windows-evidence/windows-check-20261126T004322Z-a4f81556.json` (`schema lia-studio-windows-evidence-v1`) — partes 1-6 e 8 **PASS**, **7, 9 e 10 FAIL**, `godot/unreal/unity_on_path: false`, `not_tested: engine_versions, engine_projects, gameplay, agent_runtime, windows_installer, secrets_store, build_or_release`, sem logs brutos, sem dados de projeto; e `HUB-SKILLS-FOLLOWUP.md` deixando claro que "nenhum resultado Linux substitui reteste Windows" e que causa de cada FAIL **não** é atribuível pelo código de saída | **VALIDAÇÃO ABERTA** no Windows: os FAILs 7/9 seguem abertos; o run anterior (`09ce703d`) tinha FAIL em 3, 6, 7, 9, 10 | JSON e follow-up lidos nesta sessão |
| Skills do payload do Studio | **ENTREGA MOVIDA**: `0` `SKILL.md` na `main` (só `.agents/skills/README.md`); nossos índices diziam 16 (Studio) | contagem na árvore |
| Licença do repositório | **NOVIDADE não registrada pela base**: `LICENSE` na raiz = **MIT**, "Copyright (c) 2026 BloomRX e colaboradores da Lia Studio", 1.539 B medidos | `contents/LICENSE` |
| ZIP de terceiros `docs/Mr-Mak-Skills-Free.zip` | tamanho real versionado **3.352.656 B** (o "9,9 MB" dos nossos textos é o **extraído** — já corrigido em `DR-0004`, que mantém tag + `sha256` como registro correto); `docs/pacote-agentes.zip` 15.652 B | árvore |

## 3. Correções aplicadas nesta data (e o que foi preservado)

Preservação: os relatórios históricos **não** foram reescritos — `audits/*`, os `REPORT.md` de
`repositories/*` e o texto original das seções antigas dos índices ficam como estão. Onde o índice
errava, acrescentamos um bloco **Conferência 2026-11-26** com o valor medido, e só corrigimos
diretamente números que são contagem (não narrativa):

| Arquivo | O que foi corrigido | Base da correção |
|---|---|---|
| `projects/lia-project/README.md` | `main` @ `72c44425` (833 commits), branches **1**, e a linha de skills 22→21 | §1, §2.1 |
| `projects/lia-project/INDEX.md` | §2 "permanecem apenas na origem" reclassificada contra a árvore da `main`: das 10 linhas, **9 presentes** e **1 ausente** — `docs/reports/LIA-VALIDATION-MATRIX-5EC464E-2026-11-14.md`; o gap "511 documentos fora de `main`" sai de "aberto" para **resolvido com uma exceção** (`LIA-VALIDATION-MATRIX-5EC464E`); "Nenhuma Skill com licença" → **20 de 21** (`alethe` tem `LICENSE`) | §2.1 |
| `projects/lia-agent-hub/README.md` | `main` @ `8c14ec85` (202 commits), branches **1** (eram as 4 `arena/*` + `main`); pointer das skills: o inventário canônico está removido da `main`, alcançável só por SHA/bundle | §1, §2.2 |
| `projects/lia-agent-hub/INDEX.md` | a tabela §2 (12 linhas) reclassificada contra a árvore da `main`: **9 presentes**, **3 ausentes** — e são justamente `docs/research/LIA-SKILLS-INVENTORY.md`, `docs/research/SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` e `docs/research/THIRD-PARTY-SKILLS-CATALOG.md`; além delas, `docs/research/LIA-SKILLS-ROADMAP.md` também está fora da `main` (os quatro sobrevivem por SHA no commit `bd4bfbb9…`), e `catalog/` + `Lia-AgentHub:tools/build-catalog-records.py` não estão nem na `main` nem nesse commit — ver §2.2; `DECISION-REGISTER.md` deixa de ser "2 versões divergentes"; novos contratos publicados entram na §1 como leitura pendente da base | §2.2 |
| `projects/lia-studio/README.md` | `main` @ `0e7b9949` (115 commits), branches **1**, **`LICENSE` MIT (1.539 B)** registrado, skills do payload 16 → **0 com payload próprio** | §1, §2.3 |
| `projects/lia-studio/INDEX.md` | §2 reclassificada como entregue; `CONFLICTING` de `INDICE-DOCUMENTOS.md`/`planejamento/*` fechado; ZIP 9,9 MB → 3.352.656 B versionado + nota de unidade; fronteira com o Forge: contrato publicado, integração não validada; evidência Windows 7/9/10 FAIL incluída como validação aberta | §2.3 |
| `projects/lia-forge/README.md`, `projects/lia-forge/INDEX.md`, `projects/lia-model-lab/README.md`, `projects/lia-model-lab/INDEX.md` | marcados **não verificáveis** a partir desta sessão, com o código HTTP medido — nenhum número antigo foi apagado, nenhum novo foi inventado | §5 |
| `RESEARCH-BACKLOG.md` | linha 15 (Obsidian, "verificar termos comerciais antes de integrar") resolvida com a fonte primária | §6 |
| `cross-project/memory/MEMORY-LANDSCAPE.md` | apêndice datado: a memória do Project é **lexical com tetos** e tem `expiresAt`; a lacuna "retenção não documentada" é estreitada para "por fonte, não por entrada" | `LR-CMP-006` §2 |

Nenhum `Recomendação` de objeto externo mudou: a reconciliação mexe em ponteiro e resumo, não em
veredito técnico. Onde o veredito dependeria do que não pudemos ler (Forge, Model Lab), dissemos isso.

## 4. Três divergências que não são nossas, mas que a base precisa parar de repetir

1. **"Catálogo canônico × catálogo de pesquisa"** — o Project mantém `lia-capability-catalog/` como
   canônico e classificou nossos três documentos de provider como `Pending transfer`. Qualquer resumo
   nosso que trate `MODEL-CATALOG-DIGEST`/`PROVIDER-ARCHITECTURE-DIGEST` como "o que vale" está fora do
   alinhamento: valem como *consulta*, com o delta a extrair. (`LR-MODEL-001`, `LR-MODEL-002`.)
2. **"`main` só documental"** — a premissa de 2026-11-17 morreu em 2026-11-26 nos três produtos. Os
   textos desta base que explicam lacunas "porque o documento está em branch e não na `main`" precisam
   da nova regra: **branch temporária, remoção com backup, entrega que precisa estar na `main` para existir**.
3. **"Sem validação em Windows"** — a frase era verdadeira para *nós* e passou a ser meia-verdade sobre
   o mundo: o Hub executou 28 pins/7 testes/88 subtestes num checkout Windows, o Studio tem dois
   relatórios Windows na `main` (um deles com 3 FAILs abertos), e nenhum dos dois foi reproduzido aqui.
   A formulação correta agora é "**nós não executamos; há evidência executada pelos projetos, com
   lacunas declaradas**" — aplicada em `WINDOWS-AMD-COMPATIBILITY` (pointer) e nos índices acima.

## 5. O que ficou não verificável (e por quê)

| Item | Estado medido | Efeito nos índices |
|---|---|---|
| `BloomRX/Lia-Forge` | `gh api repos/BloomRX/Lia-Forge` → **403 Resource not accessible by integration** (existe; ilegível para este token) | as **17** linhas de ponteiro da tabela §2 do índice do Forge (e as 13 da §1, que apontam para relatórios desta base) ficam marcadas **NÃO VERIFICADO DESDE 2026-11-17**, com o motivo. Nada foi reescrito |
| `BloomRX/Lia-Model-Lab` | `gh api repos/BloomRX/Lia-Model-Lab` → **404** (também 404 para `lia-model-lab`; busca `Model-Lab user:BloomRX` → 0 resultados) | idem para as **11** linhas dos índices do Model Lab (6 na tabela §2 de ADRs + 5 na §3 de documentos com múltiplas versões). O projeto está **pausado** por decisão do dono, então a pendência é de acesso, não de revisão vencida |
| Achei `BloomRX/Lia-VRM-Tests` (público, criado/push 2026-11-25, `size` 0 KB, árvore com **1** entrada) | repositório vazio: sem conteúdo a auditar hoje | registrado aqui para não "descobrir" isto duas vezes |
| Runs de CI dos três projetos | não abrimos `actions/runs` — os status são `REPORTED` pelos registros de consolidação | não afirmamos verde nenhum em nome deles |

## 6. Obsidian e a pergunta de visibilidade

Dois pontos desta rodada tocam `DR-0006` (a Research permanece pública) e nenhum deles a contradiz:

- **A visibilidade que mudou foi a dos projetos, não a desta base.** Forge ficou ilegível e Model Lab
  sumiu do token. A decisão do dono sobre a Research está intacta e o `audits/` continua público — mas a
  premissa operacional simétrica ("a Research lê os cinco projetos por API") agora tem dois buracos.
  Consequência prática registrada: `governance/INVESTIGATION-PROTOCOL.md` precisa de um passo para
  "fonte não verificável por visibilidade", e os índices passaram a dizer isso em vez de congelar número
  antigo. Não mudamos decisão nenhuma, apenas reportamos a lacuna.
- **A linha do Obsidian no backlog** ("⚠️ verificar termos comerciais antes de integrar") foi conferida na
  fonte: `obsidian.md/license` (página atualizada em 2025-02-20) diz *"Obsidian is free for all purposes,
  including personal, commercial, and non-profit use"*, com licenças comerciais **opcionais**, sem conta
  necessária, dados locais não enviados ao servidor deles e conteúdo do autor do usuário
  ("We do not claim any rights to it"). O app continua proprietário — o que muda é que não há trava
  comercial a verificar. A ressalva que permanece é outra: o **`obsidian://` URI** de terceiros (o
  `obsidianUri` do `LR-MCP-005` §7) depende do app instalado no cliente, e um deep-link para fora do
  navegador é superfície de UX, não de dados.

## 7. Evidências

| # | Afirmação | Rótulo |
|---|---|---|
| E1 | cabeçalhos das `main` (SHA, data, contagem de commits, 1 branch cada) | **CONFIRMED (API, 2026-11-26)** — `gh api repos/BloomRX/<repo>/{commits?per_page=1,branches?per_page=100,git/trees/HEAD?recursive=1}` |
| E2 | 674/165/210 blobs e 192/78/88 arquivos em `docs/**` | **CONFIRMED (árvore recursiva, `truncated: false`)** |
| E3 | conteúdo e datas dos três documentos de consolidação/limpeza; contrato de inventário v1 com `revision`/`complete`; tabela de validação Linux do Studio; JSON de evidência Windows com FAIL 7/9/10 | **CONFIRMED (lidos por `contents` + base64 nesta sessão)** |
| E4 | Project classifica 4 docs como `Research reference` e 3 como `Pending transfer`; "nenhum Canonical nesta rodada" | **CONFIRMED** (`docs/reports/LIA-RESEARCH-TRANSFER-RECONCILIATION.md`, 10.452 B) |
| E5 | 6 arquivos do Project citam `Lia-Research`; Hub e Studio, **0** | **CONFIRMED (search/code)** — `gh api search/code?q=repo:BloomRX/<r>+Lia-Research` |
| E6 | `Lia-Forge` 403; `Lia-Model-Lab` 404; `Lia-VRM-Tests` com 1 entrada | **CONFIRMED (API)** |
| E7 | CI dos projetos aprovado nos commits de consolidação | **REPORTED** (afirmação dos registros; runs não abertos) |
| E8 | qualquer afirmação sobre o estado de Forge/Model-Lab posterior a 2026-11-17 | **NOT VERIFIABLE** — ver §5 |
| E9 | execução dos testes do Project (`memory-store.test.ts`) ou do Studio (`verify_alpha.py`) por nós | **NOT RUN** — não instalamos nem executamos nada nos produtos; a base só lê |
