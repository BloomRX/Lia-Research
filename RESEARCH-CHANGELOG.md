# RESEARCH-CHANGELOG

Registro append-only do que entrou na base. Ordem inversa (mais recente primeiro).
Cada linha: data · tipo · item · efeito.

Tipos: `ADD` (pesquisa nova) · `FIX` (correção) · `CONSOLIDATE` (digest) · `DECISION` ·
`BLOCKED`.

---
---

## 2026-11-26 (UTC) — Notas Markdown do usuário: 3 objetos, a resposta em um só documento, e os índices dos produtos conferidos contra as `main` de hoje

**Duas entregas delimitadas, na ordem pedida.** Nada nos produtos foi alterado; a Research recomenda.

- **ADD** `LR-MCP-005` `bitbonsai/mcpvault` (`repositories/mcpvault/REPORT.md`) — servidor MCP de vault
  Markdown, `main` @ `5d4e6855` (tip de 2026-11-14, o merge do PR #285 `release/0.18.4`), npm **0.18.4** com `engines.node >=22.12.0` e **zero** dependências
  declaradas no pacote publicado (as 60 do `dist/node_modules` vêm do lockfile). **Executado aqui:**
  `npm install` (135 pacotes), **`npm test` = 446 testes passando em 14 arquivos** (7,26 s),
  `npm run build`, e um harness MCP próprio em stdio com **105 chamadas** em cinco cenários de notas
  sintéticas: `--read-only` expõe 11 das 18 ferramentas e recusa escrita; a denylist segura em qualquer
  profundidade (`node_modules/`, `.trash/`, qualquer segmento com ponto — inclusive
  `.obsidian-desktop/README.md`, recusado porque o nome do config alternativo do Obsidian tem que começar
  com ponto), mas `--exclude` **só some do discovery** e não bloqueia leitura direta; `patch_note` recusa
  ambiguidade com `matchCount: 90` e resolve com `replaceAll`; `delete_note` exige `confirmPath` e move
  para `.trash/` (os 94 bytes continuam lá, ilegíveis pelo MCP); `write_note` é **last-writer-wins sem
  verificação prévia**; **nenhum teto de tamanho** (1.950.034 B lidos, 3 MB escritos sem erro); busca em
  3.001 notas em **406 ms** com walk por chamada (sem índice). Grep em `src/` **e** `dist/` montado:
  **zero** chamadas de rede. Rótulos: **TESTED / LOCAL_TESTS_PASS / ADAPT**.
- **ADD** `LR-AGENT-019` `MemPalace/mempalace` (`repositories/mempalace/REPORT.md`) — `main` @ `87ae5024`,
  PyPI **3.12.0**. ID em `LR-AGENT-` e não `LR-MEM-`: a eixo de comparação é o mesmo de `LR-AGENT-011`.
  **Executado aqui:** `pip install` num venv sem rede, `mempalace init <dir> --no-llm --yes` **funciona
  offline** (grava só `mempalace.yaml`, com `wing` e salas detectadas da árvore — com dois artefatos do
  gerador visíveis: sala `"di\xE1rio"` escapada e `keywords` duplicados), `mine --dry-run` percorre o
  vault, o registro de backends lista cinco com recusa de fallback silencioso e `BackendMismatchError`
  explícito. E **a escrita e a busca não rodam offline**: `_embed_texts` → `hf_hub_download` (~300 MB) →
  `httpx.ConnectError`, inclusive forçando `sqlite_exact` num palace novo — o wrapper de embeddings vem
  antes do backend. Conferido o i18n: `pt-br.json` tem **47 de 47** chaves de `en.json`, zero faltando, e
  `docs/PRIVATE_PALACE.md:29-30` exige que o avaliador leia PT **e** EN — português é requisito de produto
  lá, e as extras `multilingual`/`dml` estão declaradas mas não instalam nada (`multilingual: []`).
  Rótulos: **PARTIALLY_TESTED / PARTIAL / REFERENCE_ONLY**.
- **ADD** `LR-CMP-006` `comparisons/MD-NOTES-INTEGRATION.md` — a resposta **única** pedida (um arquivo,
  não três). **§1** a resposta curta em cinco peças: seleção explícita por pasta guardada como allowlist do
  usuário; índice local derivado que pode ser apagado e reconstruído; proveniência em toda resposta
  (`arquivo`, `linhas`, `hash`, `lido_em`) com o texto marcado como não-confiável; escrita opt-in e
  cirúrgica (`append` num inbox ou `patch` de string única com pré-condição de hash); exclusão por
  reconciliação com `--dry-run` primeiro. **§4** é o teste que decide a régua — "ler e buscar 3.001 notas
  sem rede, sem baixar nada, sem escrever no vault" — que só o mcpvault passou. **§2** a linha de base medida em código: `lia/core/src/memory/{contracts,store,context}.ts` na
  `main` `72c44425` — JSON único com tetos 100/500/4000/2000/4, `provenance` só aceita a string `'user'`,
  busca lexical em NFD com 33 stopwords, atômico com `0o600`, `lstat` recusando symlink e &gt;400.000 B.
  **§3** a matriz com os três candidatos + a Lia na régua das cinco palavras da pergunta. **§5** a alternativa (MCP `--read-only` + ponte
  declarada) e o que ela custa por projeto. **§5** Agent Hub (só pointer no registro de candidatos; fluxo
  *integração ≠ release*), Forge (sem nada a mudar) e Model Lab (**permanece pausado**; só o fato novo de
  que MemPalace declara onnxruntime-directml como extra de Windows). **§7** o handoff: o contrato de tipo
  proposto, sete gates de aceite e a lista do que **não** fazer.
- **FIX** `audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md` (novo) + `projects/*/INDEX.md` + `projects/*/README.md`
  — os índices operacionais conferidos contra as `main` medidas hoje: **Lia-Project** `72c44425`
  (833 commits, 798 entradas, 214 `.md`, 192 em `docs/**`, **1 branch** — não 12), **Lia-AgentHub**
  `8c14ec85` (202, **1** — não 5), **Lia-Studio** `0e7b9949` (115, **1** — não 9). Classificação por linha
  em **entrega concluída / integração pendente / validação não executada**: os 9 "permanecem apenas na
  origem" do Project **estão na `main`**; os 12 do Studio idem (7 recuperados byte a byte); no Hub os
  arquivos canônicos de skills **não estão** na `main` (ponteiro quebrado, preservado por bundle e SHA);
  `LIA-VALIDATION-MATRIX-5EC464E-2026-11-14.md` é a única exceção que sobra. Fatos novos registrados: o
  Studio agora tem **`LICENSE` MIT** (1.539 B), o Hub publicou os contratos `CAPABILITY-INVENTORY-CONTRACT`
  (`inventoryVersion: 1`, `revision` = "mesmo valor e digest diferente é conflito", `complete` = "omissões
  nunca apagam registros") e `SUPERVISED-EXECUTION-V1`, skills: Project **21** com **1** `LICENSE`, Hub **0**,
  Studio **0** (eram 22/57/109/16 no inventário de 2026-11-17), e o ZIP do Mr-Mak versiona **3.352.656 B**
  (os "9,9 MB" são o extraído). Validação declarada com honestidade: Studio executou Linux (314 testes +
  8 pulados) e **falhou** nas partes 7/9/10 do checklist Windows; o Hub rodou o piloto do Project num
  checkout Windows (28 pins / 7 testes / 88 subtestes) com corte remoto pendente — **REPORTED, não
  reproduzido por nós**.
- **FIX** `cross-project/memory/MEMORY-LANDSCAPE.md` — apêndice datado preservando o texto original:
  "Memória local existe (`REPORTED`)" vira confirmada em código, e "Política de retenção — não documentada"
  vira **documentada por entrada** (tetos + `expiresAt`) e **ausente por fonte** (`provenance` é a string
  literal `'user'`). A decisão de independência (sem memória compartilhada entre produtos) continua de pé.
- **FIX** `RESEARCH-BACKLOG.md` — a pendência de licença do Obsidian verificada na fonte
  (`obsidian.md/license`, página de 2025-02-20): *"free for all purposes, including personal, commercial,
  and non-profit use"*, sem conta, dados locais, conteúdo do autor do usuário; o binário segue
  proprietário e por isso a Lia se liga à **pasta e ao formato**. Contagens da fila (3 → **5** publicados,
  15 triados), itens 04/05 de §1 marcados com relatório publicado, e o item 2 de §5 ("comparar os três num
  único digest — evitar três relatórios que dizem o mesmo") fechado com `LR-CMP-006`.
- **CONSOLIDATE** `RESEARCH-INDEX.md` (58 objetos, 62 linhas, 6 comparações, três lacunas novas em §6),
  `README.md` (217 `.md`, 58 objetos, 58 linhas de catálogo, 43 de teste), `catalog/catalog.tsv` +
  `data/inventory/license-matrix.tsv` (56 → **58**) + `data/testing/test-log.tsv` (41 → **43**, uma linha por
  objeto com resultado executado), `RESEARCH-ROADMAP.md` (nota datada nas linhas A-1/A-4/A-20, com V-1
  ainda em **44 catalogados / 0 medidos**).
- **BLOCKED** — `BloomRX/Lia-Forge` **HTTP 403** e `BloomRX/Lia-Model-Lab` **HTTP 404** para o token da
  sessão: as 28 linhas de ponteiro desses índices (17 na §2 do Forge, 11 nas §2/§3 do Model Lab) estão marcadas **NÃO VERIFICÁVEL (2026-11-26)** com o
  motivo, sem reescrever número antigo. MemPalace: escrita/busca não executáveis offline. E continuam
  abertos, com o rótulo que já tinham: `NOT RUN` em hardware (RX 580/GPU/Windows) e a trilha de Skill
  "em uso" (30 dias de notas reais + 20 tarefas), que é o que transforma esta recomendação em política.

**Não mudou:** nenhuma recomendação técnica de objeto externo foi reaberta — `repositories/ai-memory/REPORT.md`
(`LR-AGENT-011`) está byte a byte como foi publicado; o Model Lab permanece pausado; Obsidian não virou
dependência da Lia; e a decisão de manter a Research pública (`DR-0006`) saiu reforçada da conferência, com
os dois buracos de acesso dos produtos reportados em vez de escondidos.

**Portão:** `python3 -B tools/validate.py` → **0 erros · 0 avisos · 7 notas**; `python3 -B -m unittest
tools.test_validate` → **78 testes OK**; `python3 -B tools/build_catalog.py --check` → catálogo igual ao
gerado. Contas lidas do disco: 217 `.md`, 58 relatórios, 58 linhas de catálogo e de matriz, 43 de teste.

---
## 2026-11-26 (UTC) — Animama sob leitura de fonte: 2 objetos, 1 matriz por projeto, e o gate de licença que **roda**

- **ADD** `LR-UI-006` `raymond-van/animama` — companion de mesa (Electron + FastAPI, `main` @ `4ba6db1c`,
  5.953 blobs / 70 MB / 2.943 arquivos de código / 412 `.md` / 41 ADRs / 21 `SKILL.md`). Lido em fonte real
  por clone raso com sparse-checkout, não por README: formato `animaPoseClip/2.0` (ADR 0014/0016/0019/0020,
  2 MiB, decimais fixos, beats + trilhas anatômicas em graus), as 24 emoções em `0..30` com escala dupla
  estado↔representação e promover/rebaixar em par oposto, a memória Markdown versionada com projeção diária
  gerada de tabela no banco, o parser incremental de JSON que deixa o avatar falar antes de o objeto fechar,
  e o pipeline de lip-sync com avaliação própria. **Executado aqui:** `scripts/public-release/check_source.py`
  limpo + **12 testes OK** (é o `LOCAL_TESTS_PASS` de `LR-UI-006`); `pnpm`, navegador, GPU, Windows e Unity
  não existem nesta sessão, então **nada do produto rodou** e o §8 de desempenho é estimativa rotulada.
- **ADD** `LR-FORGE-024` `raymond-van/animama-avatar-converter` — MIT, 98 blobs, 26 `.cs` (3.152 linhas,
  55 `[Test]`) e um pacote npm com **zero dependências**. **Executado aqui: `npm test` = 46 testes, 46
  passando**, e `npm run check` → `OK: version 0.1.1, 82 package files and folders, 36 sources checked.`
  A checagem deles prova estaticamente a frase "uploads nothing" (`scripts/check.mjs:155-172`), e o CLI
  documenta a armadilha do `-nographics` no Unity. Nenhuma conversão executada (`BLOCKED` — exige Unity).
- **ADD** `LR-CMP-005` `comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md` — os 15 achados classificados no
  vocabulário desta base, o dicionário explícito dos seis rótulos do dono (`ADOPT`→`DIRECT_INTEGRATION_CANDIDATE`,
  `NEEDS_VALIDATION`→`INSUFFICIENT_EVIDENCE`, etc.), e a matriz por projeto (Project / Forge / Studio /
  Agent Hub / Model Lab) ordenada por impacto, esforço e risco. §5 lista o que **não** está recomendado,
  inclusive usar o Animama como dependência ou copiar qualquer linha de código (AGPL-3.0-only +
  5.953/5.953 arquivos com `review = prepared-not-release-approved`).
- **FIX** duas contagens minhas, conferidas no clone após o primeiro commit: a linha de testes do `LR-UI-006` dizia "um `.test.mjs` ao lado de cada script" — em `src/frontend/web/scripts/` são 46 scripts e 41 testes, e **29** têm homônimo (os 17 restantes são, em sua maioria, obra de build: `generate-routes`, `landing-*`, `local-page-server`, `optimize`, `verify`, `lipsync`); e a do `LR-FORGE-024` dizia 39 % (1.240 linhas) de C# de teste — medido com `find`/`wc -l`, são **1.108 linhas nos 5 `*Tests.cs` = 35 %** dos 3.152 (1.281 com o `HumanoidTestRig.cs`). Nenhum número de portão depende disso; é a diferença entre uma frase e uma medição.
- **FIX** `repositories/superpowers/REPORT.md` §7 — retificação da retificação: `skills/doc-coauthoring/SKILL.md`
  mede **15.815 B** hoje, e **nenhum** blob de `anthropics/skills` na `HEAD` atual tem 42.969 B
  (consulta `.size==42969` → 0 linhas). A atribuição "42.969 B é o `doc-coauthoring`" sai; sobrevive só a
  correção anterior (9.530 B).
- **FIX** `data/testing/test-log.tsv` — linha de 2026-11-20 que pertencia ao `manimgx` estava chaveada sob um
  `LR-UI-006` nunca registrado; movida para `LR-FORGE-003` (o `object_id` real daquele teste `BLOCKED`).
- **FIX** `data/inventory/license-matrix.tsv` — linha de `LR-FORGE-013` (`anymachine`) tinha os campos
  deslocados a partir de `copyleft` (15 colunas, conteúdo trocado); reconstruída contra o §4 do relatório.
- **ADD** dados: `license-matrix.tsv` **54 → 56** linhas (CRLF, 15 colunas), `test-log.tsv` **39 → 41**
  (LF, 10 colunas: 14 `LOCAL_TESTS_PASS` + 10 `LOCAL_SMOKE_PASS` + 6 `PARTIAL` + 11 `BLOCKED`),
  `catalog/catalog.tsv` regenerado (56), `READY-TO-USE-LICENSES.md` +2 linhas na tabela-mestra,
  `SPLIT-LICENSE-SCAN.md` §4 com +2 repositórios (27 → 29) e o Animama registrado como o **contraexemplo**
  da divisão por diretório: um repo AGPL com licença por arquivo, inventário e gate.
- **NOTA** portões: `tools/validate.py` → **0 erros · 0 avisos · 7 notas** (as 7 notas são o baseline de IDs
  internos sem cabeçalho próprio), `tools/build_catalog.py --check` em dia, `python3 -m unittest
  tools.test_validate` → **78 testes OK**. Contagens conferidas: 213 `.md`, 56 relatórios, 56 linhas de
  catálogo, 56 de matriz, 41 de test-log.

## 2026-11-25 (UTC) — a leva de 16 links: 10 objetos, 1 digest de gates, e o censo de 187 `SKILL.md`

- **ADD** `LR-AGENT-015` `aaif-goose/goose` (o antigo `block/goose`, mesmo `id` 846698999 — renomeação de
  dono, não bifurcação): governança por issue **Ready** e aposentadoria do diretório próprio de servidores
  MCP. 366 MB de árvore; execução `BLOCKED` (sem `cargo`/`rustc` aqui).
- **ADD** `LR-AGENT-016` `bytedance/deer-flow`: a auditoria de Skill como **contrato** — 4 schemas
  (`package_snapshot` → `review_facts` → `review_report` → `waiver_manifest`), waiver com `file_sha256` +
  `expires_on` + `preapproved_file_sha256s`, CI de review em PR, e a Skill `skill-reviewer` que **não pode
  ler o alvo diretamente** e tem 6 casos de eval próprios. O analisador deles **rodou aqui** (346 análises).
- **ADD** `LR-AGENT-017` `anthropics/skills` + `anthropics/claude-plugins-official` + tópico
  `skill-creator`: o acervo de 200.497 ★ **sem `LICENSE` na raiz** (18 por Skill + `THIRD_PARTY_NOTICES.md`
  de 404 linhas); o `skill-creator` é **byte-idêntico** ao do repositório de plugins
  (`sha256 dcd4803e…`); e a versão antiga dele existe como **arquivo de referência** que ainda se declara
  `name: skill-creator`.
- **ADD** `LR-AGENT-018` `obra/superpowers`: MIT na raiz, **12 manifests** de runtime sincronizados por
  `.version-bump.json` (11 pares `path`/`field`), zero CI e uma política de PR contra agente ("94 % de
  rejeição", "não aceitamos PR de agente sobre issue alheia").
- **ADD** `LR-VOICE-005` `pipecat-ai/pipecat` (12 Skills de manutenção, `disable-model-invocation: true`,
  `LICENSE-shadcn.md` dentro do componente vendorizado, `license-check.yaml` no CI), `LR-DATA-001`
  `D4Vinci/Scrapling` (a Skill da lib com `LICENSE.txt` próprio, ZIP na `main` por URL de ramo e
  `metadata.openclaw.requires.bins`), `LR-FORGE-022` `johannesjo/parallel-code` (o gate de IPC:
  `channel-manifest.json` + allowlist no `preload.cjs` + teste de divergência), `LR-FORGE-023` `dyad-sh`
  (split Apache-2.0 + `src/pro/` sob FSL-1.1-ALv2; workflow que **apaga** release fora do CI), `LR-RAG-001`
  `infiniflow/ragflow` (o `AGENTS.md` que trata legado como passivo; `internal/{dao,entity}/license.go` é
  código, não licença) e `LR-PROV-002` `daytonaio/daytona` (**árvore de 3 arquivos**: o código foi para lugar
  privado; a licença só existe nas tags, e o `README` teve um commit para fixar o link na `v0.190.0`).
- **ADD** `LR-CMP-004` `comparisons/SKILL-GATE-COMPARISON.md` — **o resultado da rodada**: os 6 links de
  autoria de Skills viram um censo de **187 `SKILL.md`** (173 pacotes materializados com recursos), passado
  por **dois validadores abertos executados aqui** (o `quick_validate.py` da Anthropic e o analisador do
  DeerFlow, 177 + 346 execuções). Resultado central: eles **discordam em 43 dos 177 pacotes** — 39 estão
  prontos para publicar no gate de segurança e são rejeitados pelo da Anthropic (53 só por chave
  desconhecida), e 5 do próprio acervo oficial estão `blocked` por `python-env-dump-exfil` no código
  distribuído junto. Licença por Skill: **19 de 178** declaram, **23 de 187** têm arquivo — 18 dos 23 no
  repositório da Anthropic, e os 4 restantes são exatamente as Skills **copiadas** de lá.
- **CONSOLIDATE** `cross-project/licensing/SPLIT-LICENSE-SCAN.md`: **formato `I`** (exceção por diretório com
  licença futura) e mais 10 linhas de censo; censo vai de 17 para 27 repositórios; §6 ganha 2 lacunas
  declaradas (`NOTICE` não entra na contagem de `LICENSE*`; diff por diretório do dyad não auditado).
- **FIX** contabilidade: índice passa a **54 objetos** (58 linhas com sub-documentos), `license-matrix.tsv`
  a **54**, `test-log.tsv` a **36** (1 linha nova: a execução dos dois gates), catálogo regenerado (54),
  `README.md` 210 `.md`; a linha de abertura do índice, que ainda dizia "34 objetos / 30 linhas", foi
  alinhada com o corpo.
- **NOTA** `decisions/ACCEPTED/DR-0019…md` continua dizendo "os 42 objetos": é afirmação datada de um
  registro aceito, não contagem corrente — não reescrevemos histórico aprovado (append-only).
- **FORA** do que a medição resolve: nenhum registro de Skill do Hub foi tocado; as perguntas de adoção
  (contrato de gate, waiver datado, `requires.bins`, gate de IPC no Studio, licença por Skill obrigatória)
  estão nos §"Onde isto poderia se aplicar" de cada dossiê, com `— nenhuma registrada` na decisão.

---

## 2026-11-25 (UTC) — `LR-FORGE-020` Charakuru + `LR-FORGE-021` HairDeck; e o `DR-0004` fecha por hash

Primeira rodada operando sob `DR-0019`: dois links do dono, sem briefing, com relação entre eles
(concorrentes no resultado, opostos em distribuição e licença) decidindo o formato da saída.

### Objetos novos (2 relatórios, nenhum template, nenhum DR novo)
- **`LR-FORGE-020`** `nanocle/Charakuru` — `DOCUMENTED` + execução `BLOCKED` (12 linhas:
  `repositories/charakuru/REPORT.md`). O repositório tem **0 arquivos de código** (106 entradas: 24 `.md`,
  imagens, 5 arquivos de licença em `public/`); o kit — `AGENTS.md`, 9 Skills, `server.mjs` — existe só no
  ZIP da release (12.024.159 B). Licença lida inteira: **`Charakuru Source-Available License v1.2`, 287
  linhas, 11 seções** — Skills são "Covered Materials"; elegibilidade por faturamento **e** captação
  (JPY 100.000.000, testados separadamente); §5 renuncia a "ideias, técnicas, workflows"; §10 escreve a
  incerteza das Skills dentro do disclaimer. PRs não aceitos; 0 workflows.
- **`LR-FORGE-021`** `hyz317/HairDeck` — `PARTIALLY_TESTED` + `PARTIAL` (12 linhas:
  `repositories/hairdeck/REPORT.md`). Executado aqui: `python3 -m unittest discover -s tests` → **38
  coletados, 28 passaram, 10 erros de importação, 0 falha de asserção** (com e sem `numpy` em venv);
  `scripts/check_environment.py` → 3 linhas `[FAIL]` e **exit 1**, com o portão "Use Python 3.12 x64 for
  the pinned release environment". Estrutura medida: 123 `.py` / 16.566 linhas / 106 `def test`;
  **0 CI, 0 tag, 0 release, 0 `NOTICE`, sem LFS**; `data/lists` com 36.440 / 36.455 chaves `vroid-hair/…`
  (proveniência por ID, sem cópia); `docs/measurements/` com 20 JSONs de primeira × morna por etapa.

### A descoberta que mudou a própria base (e não é sobre os dois objetos)
`gh api …/releases` devolve **`digest` por asset** — o SHA-256 que o GitHub calcula, sem baixar nada. O
bloqueio de release-assets deste sandbox (`302` → `release-assets.githubusercontent.com`, 0 bytes) nunca
bloqueou a **informação**, só a rota. Usado para fechar `DR-0004`: `docs/Mr-Mak-Skills-Free.zip` (4 ramos
`arena/*` do `BloomRX/Lia-Studio`, ausente de `main`) tem `sha256` **idêntico** ao asset publicado
`Mr-Mak-Skills-0.4.14.zip` (`9e4ad7fe…08ee2`; 3.352.656 B). Consequências: a faixa "v0.4.14…v0.5.0" vira
**uma** tag; o `-Free` do nome não existe no upstream; o build reprodutível e as 764 entradas /
**9.940.122 B** extraídos passam de inferência a medição no artefato real; 0 `NOTICE` reconfirmado contra o
pacote verdadeiro. Registro em `repositories/mr-mak-workspace/REPORT.md` §14 (com o texto antigo riscado,
não apagado) e em `decisions/PENDING/DR-0004-STUDIO-THIRD-PARTY-ZIP.md`.

### Retificações e consertos desta rodada
- **0,11 MB de erro meu, corrigido**: a reconstrução da §7 dava 9,83 MB extraídos; o arquivo real tem
  9.940.122 B. A contagem de entradas batia; o total, não. Fica a regra: *reconstruir o gerador prova o
  algoritmo, não o artefato*.
- quase-escribi um erro: meu primeiro grep buscava `1 億` (com espaço) e `1亿` e ia afirmar que as traduções
  JA/zh omitiam o limiar da licença do Charakuru. **Não omitem** (`1億円` sem espaço); a tabela por idioma está
  no §8 do dossiê, com o falso negativo registrado.
- `cross-project/licensing/SPLIT-LICENSE-SCAN.md`: +2 formatos (**G.** elegibilidade quantitativa do lado do
  usuário; **H.** termos no artefato montado, não no repositório) e cabeçalhos de contagem corrigidos — "Os
  três formatos medidos" (havia 6) → oito; "Tabela dos 13 repositórios" (havia 15) → 17.
- `governance/LICENSE-AND-PROVENANCE-POLICY.md` §5: artefato publicado se ancora por **(tag, asset, tamanho,
  `digest`)**, não por `fonte_commit`.
- `projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md`: novo §4.1 (instrução de Skill como material
  licenciado) e o item 5 das ações atualizado — a medição pedida ao dono foi feita pela Research.
- `repositories/mr-mak-workspace/REPORT.md`: três defeitos estruturais **pré-existentes** consertados
  (linha de tabela quebrada em duas, tabela "Área | Bytes | O que é" com linhas de 2 células, e a linha do
  `DR-0004` sem a terceira célula + com a alegação agora superada riscada).

### Contabilidade
- `.md`: 197 → **199** · relatórios: 42 → **44** · `catalog/catalog.tsv`: **44 linhas** (em dia) ·
  `data/inventory/license-matrix.tsv`: 42 → **44** linhas, 15 colunas, 0 avisos · `data/testing/test-log.tsv`:
  33 → **35** linhas · `RESEARCH-INDEX.md` §1: 44 objetos.
- `tools/validate.py`: **0 erros / 0 avisos / 7 notas** · `tools/test_validate.py`: **78 OK**.
- Nenhuma mudança fora desta base: os apps Lia receberam **zero** linha; as sugestões dos dois dossiês são
  para o dono julgar viabilidade (`DR-0019` §5, `MISSION.md` §3).
- Incidente operacional: o sandbox reapareceu **reachatado em `Initial commit`** mais uma vez (só o `README`
  versionado, 1 arquivo). Recuperado com `git fetch` + `git reset --soft fa60141` + `git reset` — nenhum
  force-push, nenhuma reescrita de histórico, nenhuma perda.
## 2026-11-24 (UTC) — `DR-0019`: protocolo contínuo de investigação de links entra como norma da base

Determinação do proprietário (§1–§8 do "LIA RESEARCH — PROTOCOLO CONTÍNUO DE INVESTIGAÇÃO DE LINKS"),
recebida logo depois da reescrita de escopo do mesmo dia. Não muda nenhuma conclusão de pesquisa:
fixa método, rótulos e autonomia.

### DECISION — `DR-0019` (aceita) · `decisions/ACCEPTED/`
- **É decisão de governança desta base**, não aprovação de adoção em app algum (§5 do próprio DR:
  "fora de escopo" lista o que ela não autoriza).
- Aceita sem alteração de substância; a parte que colidia com a base foi reconciliada, não ignorada
  (§4.3 do DR): o protocolo nomeia `UNVERIFIED`, que não existe no vocabulário do validador, e esta
  base distingue `UNVALIDATED` (sem comprovação nossa) de `NOT_RUN` (podia ser feito aqui) e de
  `BLOCKED` (limitação medida). Tradução fixada nos dois lados.

### CONSOLIDATE — `governance/INVESTIGATION-PROTOCOL.md` 1.0 → 1.1
- **Etapa 0 — entrada do link (sem briefing)**: relação entre vários links (relacionados ·
  complementares · concorrentes · independentes) decide o formato da saída; procurar o registro
  anterior antes de investigar; perguntar só o indispensável.
- **Tabela de equivalência de rótulos** (protocolo × validador) e a regra `NOT_RUN` ≠ `BLOCKED`.
- **Etapa B**: lista de profundidade proporcional + "o que não foi coberto aparece na lista de
  não verificado; lista vazia ali é suspeita".
- **Etapa D**: fronteira do experimento controlado (sandbox/`/tmp` sim; projeto Lia, peso grande,
  serviço pago, conta, crédito, dado proprietário para fora — não) e o **critério de descoberta**:
  rodada que só cadastra está incompleta, mesmo com tudo registrado.
- **Etapa E**: parcimônia documental — linha de inventário, linha de digest, retificação, dossiê,
  ou nada; "o dono mandou o link" não é critério de documento novo.
- **"Resumo de rodada (9 itens)"** como formato fixo da resposta ao dono; **"Autonomia e limites de
  execução"** (ajuste de baixo risco entra com registro no changelog, sem pedir licença caso a caso).
- Anti-padrões +3: documento por link; `BLOCKED` usado para o que era só não feito; rodada que só cadastra.
- `templates/README.md`: esclarece que o resumo de 9 itens não é template de relatório; nenhum
  template novo foi criado.

### Contabilidade
- **+1 arquivo** (196 → **197** `.md`); decisões: 1 → **2 ACCEPTED** (índice §4: "12 abertas + 6 tomadas");
  `decisions/README.md` com a linha DR-0019.
- Relatórios: 42 · `catalog/catalog.tsv`: 42 linhas · `tools/validate.py`: **0 erros / 0 avisos /
  7 notas** · `tools/test_validate.py`: **78 OK**.
- Nada foi alterado fora desta base; nenhum app Lia recebeu mudança, instalação ou integração.

## 2026-11-24 (UTC) — determinação do dono: o Research mantém só as diretrizes desta base

Determinação recebida: **"mantenha só suas diretrizes; os outros apps, vou decidir se é possível
implementar neles."** Registrada como regra de escrita, não como mudança de conclusão de pesquisa.

### FIX — vocabulário de escopo em 12 documentos + governança
- `governance/INVESTIGATION-PROTOCOL.md`: a Etapa C termina na sugestão; diretrizes que o Research aplica
  são as desta base (`tools/`, `governance/`, `templates/`, `agents/`, índice, catálogo, `data/`). Para os
  outros apps: o que a evidência sustenta **+ a pergunta de viabilidade**. Nova linha de anti-padrão:
  "escrever 'transportar X para o app Y' como se houvesse autorização".
- Relatórios e digests da leva (mais o `LR-FORGE-014`): títulos "**Mapa para os projetos da Lia (o que
  levar)**" viraram "**Onde isto poderia se aplicar (a viabilidade é do dono)**"; a coluna "O que levar"
  virou "O que sugiro considerar"; os verbos imperativos das recomendações passaram a "**Propor:**", e o
  campo `Recomendação` dos cabeçalhos ganhou "sugestão ao dono". Os rótulos do vocabulário
  (`ADAPT`/`REFERENCE_ONLY`) não mudaram — mudar recomendação exige evidência nova, e não houve.
- Cada seção de recomendação ganhou uma nota de escopo dizendo que aquilo não é instrução para nenhum app.
- **Documentos anteriores a esta data mantêm o texto** (inclusive "Custo de adoção", que é estimativa
  descritiva, não ordem); a regra de leitura está escrita no protocolo, em vez de reescrita em 180 arquivos.
- Catálogo regenerado (`catalog/catalog.tsv`, 42 linhas) porque o campo `Recomendação` é lido do
  cabeçalho. Validador: **0 erros / 0 avisos / 7 notas**; `tools/test_validate.py`: 78 testes OK.

## 2026-11-24 (UTC) — leva de 8 links: os dois orgs contados por inteiro (27 + 123 repositórios) e três objetos com verificação executada

Pedido do proprietário: pesquisar `AppFlowy-IO` ("veja todos os repos desse"), `opf` (org), `calcom/cal.diy`,
`OpenWhispr/openwhispr`, `capsoftware/cap`, `chatwoot/chatwoot`, `every-app/open-seo` e
`debpalash/voicestudio`. Nenhuma instalação em projeto Lia, nenhuma conta, nenhum gasto, nenhum peso baixado.
Medição: `gh api` (censo de org, árvore recursiva, `contents/*` decodificados), quatro clones rasos e
**execução dos verificadores internos de três fornecedores** — o resto ficou em leitura estática porque o
sandbox não tem `cargo`, `go`, `ruby`, `flutter` nem `docker` (medido com `command -v`).

### ADD — `LR-FORGE-015` · org `AppFlowy-IO` (27 repositórios) → **REFERENCE_ONLY**, com uma exceção
- **Censo completo**: 27 repos · 1 arquivado · 14 AGPL-3.0 · **6 sem nenhum `LICENSE`** · `appflowy-editor`
  **dual AGPL-3.0 + MPL-2.0** · `AppFlowy-SelfHost-Commercial` com `SELF_HOST_LICENSE_AGREEMENT.md` e
  **sem licença aberta**.
- **A assimetria documentada por eles mesmos**: `AppFlowy-Cloud` (AGPL, ★2.018) está arquivado com o aviso
  de que "no longer used to build or distribute the latest AppFlowy self-hosted server" e que features novas
  só existem em imagens Docker `appflowyinc/*`; o que continua no GitHub é o andaime de deploy sem licença.
  Nada foi puxado nem rodado (nível 3, decisão do dono).
- CI lida por nome: `AppFlowy` tem 12 arquivos incluindo `android_ci.yaml.bak` (desligado dentro da pasta
  ativa); as checagens de Rust (audit, rustlint, stress, integration) estão no repositório **arquivado**.

### ADD — `LR-FORGE-016` · org `opf` (123 repositórios) + o gate de envolvimento de IA → **ADAPT**
- **Censo**: 123 repos · 77 não-fork · 46 forks · 39 arquivados; licenças dos não-fork: 45 nenhuma ·
  19 GPL-3.0 · 8 MIT · 3 NOASSERTION · 2 Apache-2.0.
- **`opf/openproject` é GPL-3.0 puro**: árvore de 34.051 entradas (`truncated: false`) com **0** caminhos
  `ee/`, `enterprise/` ou `premium/` — a fronteira comercial do produto não existe como diretório no repo.
- **O artefato da leva**: `ai-involvement-check.yml` + `script/ci/ai_involvement_check.sh` (129 linhas) e a
  seção "AI involvement" do template com 4 níveis (`None/Assisted`, `Collaborative`, `Directed`,
  `Autonomous`) todos dentro de comentários HTML; o script nunca sai com exit ≠ 0 e o `pull_request_target`
  carrega justificativa escrita + `permissions: contents: read` + `persist-credentials: false` +
  sparse-checkout de um único arquivo. Detalhe em `LR-AGENT-014`.
- **O cluster de IA admite o que faz**: `openproject-agent-skills` (MIT) abre com WARNING de maturidade, de
  que **causa escritas sem `--dry-run`**, de flag que muda de significado por versão e de ausência de
  suporte, e mantém `validation/baseline.md` (RED) + `validation/loopholes.md` (L1–L8, com uma mudança de
  contrato que aposentou 6 flags). Contraste direto com `LR-STUDIO-012`.

### ADD — `LR-FORGE-017` · `every-app/open-seo` @ v0.1.32 (HEAD `6f68494`) → **ADAPT** · **TESTED**
- **Único da leva com suíte completa executada aqui**: `pnpm install --ignore-scripts` (24 s) →
  `pnpm run test:ci` = **299 arquivos de teste, 2.130 testes, 0 falha** em 132 s; `tsc --noEmit` limpo;
  `oxlint --type-aware` com **0 avisos e 0 erros** em 1.514 arquivos / 184 regras.
- **O padrão que faltava na casa**: 28 Skills em `.agents/skills`, **12 espelhadas** em
  `plugins/openseo/skills` por `scripts/sync-plugin-skills.mjs`, com o `ci:check` terminando em
  `test -z "$(git status --porcelain -- plugins/openseo/skills)"` — cópia real (por que instaladores pulam
  symlink) + **teste de deriva**. Cópias conferidas: byte-idênticas.
- Fronteiras medidas: 15 de 28 Skills com `metadata.internal: true`; `server.json` em **0.1.27** contra
  `package.json` 0.1.32 (deriva de manifesto, a CI deles não cobre isso); `deploy:prod` dispara workflow em
  `bensenescu/open-seo`, que responde **404**; e `retroactive-contributions.md` declara que fixes do repo
  público entraram pelo staging privado **sem o nome do autor**.
- Falso negativo meu, registrado: o primeiro `pnpm run lint` pareceu falhar por causa do pipe para `tail`;
  reexecutado com saída em arquivo, exit 0.

### ADD — `LR-VOICE-003` · `debpalash/VoiceStudio` @ v0.5.8 → **ADAPT** · **PARTIALLY_TESTED**
- **Censo próprio de fornecedura**: 35 YAML em `.github/{workflows,actions}`, **278** referências `uses:`,
  **262** remotas, **262 em SHA de 40 hex**, **0** flutuando em tag, 34 ações distintas.
- **Testes do fornecedor executados**: `pytest tests/test_workflow_action_pins.py tests/test_actions_pinned.py
  -q --noconftest` → **20 passed, 1 skipped** (o skip pede `VOICESTUDIO_VERIFY_ACTION_PINS=1`, que é a parte
  de rede); com o `conftest.py` ativo, 21 erros `No module named 'services'` — causados **pelo meu
  sparse-checkout**, não pelo projeto (registrado como limitação minha).
- **931 arquivos de teste, 19 deles só de pinos**; `LICENSE-NOTICE.md` dizendo que AGPL-3.0-only
  "**includes commercial and internal business use**" e que "Model weights, tokenizers, and other
  third-party assets **retain their own terms**"; `.gitmodules` com `omnivoice-gallery` fora do alcance da
  licença do repo.

### ADD — `LR-FORGE-018` · `capsoftware/cap` @ cap-v0.6.3 → **ADAPT** (execução `BLOCKED` por ambiente)
- Licença **dividida por família de crate**: MIT só para `cap-camera*`/`scap-*` (um único
  `licenses/LICENSE-MIT` referenciado), AGPLv3 no resto; 35 workflows, `apps/` com 9 superfícies.
- **`AGENTS.md` de 125 linhas como documento de referência da casa**: invariantes *antes* da geração
  ("Every CI failure caused by one of these rules means the agent didn't read this section"), proibição de
  editar arquivo gerado, "no fixed sleeps / no polling spies / no retries — a test that passes on rerun is a
  flake to fix", e o **ratchet**: violações congeladas por arquivo em `scripts/test-lint/*.json` —
  **33 arquivos / 324 exceções**, máx. 69 — com "Counts only go down… Never raise a count or add an entry."

### ADD — `LR-FORGE-019` · `calcom/cal.diy` @ v6.2.0 → **ADAPT**
- **MIT puro medido**: LICENSE de 21 linhas com **zero** ocorrências de AGPL/Affero, 0 caminhos `ee/`,
  7 `LICENSE` aninhados também MIT. E a fronteira que o fork **não** removeu:
  `LicenseKeyService.checkLicense()` e `validateLicenseKey()` seguem no código devolvendo `return true`, com
  bypass por `NEXT_PUBLIC_IS_E2E`.
- **`agents/` como fonte única**: `.claude/{rules,skills}` e `.cursor/{rules,skills}` são **symlinks** para os
  mesmos blobs (`e01395`, `a769d4`) — a solução oposta à do open-seo, para o mesmo problema, no mesmo mês.
- `PERMISSIONS.md` (189 linhas) mapeando checagem RBAC → string `recurso.ação` **com coluna `arquivo:linha`**;
  50 workflows (7 e2e, `security-audit.yml`, `nextjs-bundle-analysis`, 9 `cron-*` de produto);
  `.env.example` com 465 linhas e **165 variáveis**; Skill vendida (`vercel-react-best-practices`) com
  `license: MIT` no frontmatter e "45 rules" batendo com os 45 arquivos de `rules/`.
- Renomeio confirmado: `GET repos/calcom/cal.com` responde com o objeto `calcom/cal.diy`; não existe repo
  `cal.com` no org (44 repos).

### ADD — `LR-SEC-009` · `chatwoot/chatwoot` @ v4.20.1 → **ADAPT** (formato de fila, não ferramenta)
- **A fila que a Lia não tem**: `ghsa-linear-sync.yml` (30 linhas, `permissions: contents: read`) +
  `.github/scripts/ghsa_linear_sync.py` (**211 linhas**): `GET /repos/{repo}/security-advisories?state=triage`
  com paginação por `Link`, idempotência consultando o Linear pelo título `[GHSA-id]`, `priority` derivada de
  `SEVERITY_PRIORITY` com *default* medium, e Slack/Discord **só depois** da issue criada.
- Licença: MIT **exceto** `enterprise/` (759 blobs), com a cláusula condicional "**if that directory
  exists**" e `enterprise/LICENSE` proibindo produção sem assinatura; `publish_foss_docker.yml` ×
  `publish_ee_docker.yml` como a fronteira visível na CI.
- Contraste de higiene: 40 mil estrelas aceitando `actions/checkout@v4` (tag flutuante) no mesmo mês em que
  o VoiceStudio trata 262 pins como corpus de teste.

### ADD — `LR-VOICE-004` · `OpenWhispr/openwhispr` @ v1.12.0 → **ADAPT** (duas formas, zero código)
- **Peer arquitetural do `lia-voice-input`**: 19 workflows, das quais **8 são builders de helper nativo por
  plataforma** (key listener, mic listener, fast paste, system audio, text monitors, AEC de reunião) e
  `build-and-notarize.yml` separa notarizar de empacotar.
- `docs/network-allowlist.md` por host, admitindo a fraqueza do próprio desenho ("A configured HTTP proxy
  uses an unencrypted CONNECT hop… No inbound ports") — formato de divulgação melhor que o de site, e
  aplicável ao `lia-voice-input`.
- 12.132★ com **519 issues abertas** e `SECURITY.md` suportando `1.10.x` enquanto a release é `v1.12.0`:
  a tabela de versões não acompanhou o release.

### ADD — `LR-AGENT-014`, `LR-MCP-004`, `LR-LIC-006` · três digests nascidos da mesma leva
- `LR-AGENT-014` (`cross-project/agents/AI-INVOLVEMENT-DECLARATIONS.md`): as três camadas do padrão
  (instrução → verificação → declaração cobrada) aplicadas aos oito objetos; **nenhum dos sete automatiza a
  declaração de autoria**, todos automatizam a forma. Proposta de um campo `| Envolvimento de IA |` no
  cabeçalho dos relatórios, com as objeções já escritas.
- `LR-MCP-004` (`cross-project/mcp/APPFLOWY-AI-PLUGINS-GATES.md`): permissão por execução **dentro do JSON
  Schema** — `confirm` como `{"type":"boolean","const":true}` em **31 das 45** ferramentas, obrigatório em
  `required` nas 31, presente em **20/20** destrutivas e **0/14** de leitura; `tools_integrity` com
  `tool_count` dentro do hash; verificador deles executado (`check.py` → `ok`, exit 0 com 2 notas) e tabela
  de annotations determinística (duas execuções idênticas).
- `LR-LIC-006` (`cross-project/licensing/SPLIT-LICENSE-SCAN.md`): método de 5 passos para ler licença
  dividida e os **três formatos** medidos em 13 repositórios — diretório com licença própria (Chatwoot),
  família de crates (Cap), licença única + `LICENSE-NOTICE.md` (VoiceStudio) — mais dual por componente
  (appflowy-editor) e "sem licença, com acordo" (AppFlowy SelfHost Commercial).

### CONSOLIDATE — estrutura da base
- **+11 documentos** (8 relatórios novos em `repositories/*` + 3 digests): 185 → **196** arquivos `.md`;
  §1 do índice 34 → **42 objetos**; §3 31 → **34**; `catalog/catalog.tsv` regenerado;
  `data/inventory/license-matrix.tsv` 34 → **42 linhas** (uma por objeto novo, com a evidência apontando a
  seção do relatório); `cross-project/licensing/READY-TO-USE-LICENSES.md` com 8 linhas na tabela-mestra.
- **+3 linhas** em `data/testing/test-log.tsv` (30 → 33 registros): `LOCAL_TESTS_PASS` para o open-seo,
  `LOCAL_SMOKE_PASS` para os plugins AppFlowy e `PARTIAL` para os testes de pin do VoiceStudio — a primeira
  vez nesta base que um resultado `PARTIAL` documenta uma falha causada pelo **meu** método de coleta.
- **Reparação de dados na matriz de licenças** (descoberta ao escrever estas linhas, não ao ler os
  objetos): a linha `LR-FORGE-013` tinha **uma quebra de linha dentro de um campo**, o que fazia
  `check_licence_counts` enxergar um registro com `id` vazio, e o arquivo terminava sem nova linha.
  Corrigidos; o validador passou de 1 aviso para **0 avisos** nesta base (0 erros, 7 notas, todas
  antigas e conhecidas).
- **Duas referências cruzadas erradas que eu mesmo escrevi e retirei antes do commit**: comparava
  `logging_percentage_check.yml` do Chatwoot com "95 % de overhead de stdout" atribuído a um objeto
  `LR-FORGE-013` chamado jupyter-mcp-server, e mencionava o mesmo id como par do `.bak` do AppFlowy.
  `LR-FORGE-013` é **anymachine** e não existe jupyter-mcp-server nesta base — a frase foi removida, não
  reformulada, porque a comparação não tinha fonte. Vale como lembrete da regra que a casa já tem:
  índice antes de adjetivo.
- `projects/lia-project/INDEX.md`: a lacuna `lia-security-review` (ainda `❌`) passa a citar o desenho de
  fila medido em `LR-SEC-009` e o inventário leve `opf/recense` (MIT) — continua aberta; a autoridade para
  abri-la é do dono.

### O que não se mede aqui (e fica declarado)
- Compilação/execução de qualquer projeto em Rust, Go, Ruby, Flutter ou Electron nesta máquina:
  `BLOCKED_BY_ENVIRONMENT` medido por `command -v` — por isso Cap, Chatwoot, OpenProject, AppFlowy e
  OpenWhispr têm o campo de execução em `NOT_RUN`/`BLOCKED` e nenhuma afirmação de "compila/roda".
- Termos dos pesos de modelo que VoiceStudio e OpenWhispr baixam: `BLOCKED` por política (nada foi
  baixado); `nvidia/parakeet-tdt-0.6b-v3` citado como link do README deles, não como verificação.
- Nota do dono, duas linhas: (1) a escolha symlink × cópia-gerada (cal.diy × open-seo) é decisão de
  publicação do Lia Agent Hub; (2) o ratchet "contagem só desce" do Cap resolveria os avisos recorrentes
  desta base, mas mexe no `tools/validate.py` — precisaria de DR, e a Research não aprova nada.

## 2026-11-24 (UTC) — `bisqit.app`: como um app fechado faz o que o Lia Project lista como lacuna

Pedido do proprietário: pesquisar o link e "como foi feito o app", com possível utilidade para o Lia
Project. Nenhuma instalação, nenhuma conta, nenhum gasto, nenhum download de binário.

### ADD — `LR-FORGE-014` · `bisqit.app` (Bisqit) @ site verificado 2026-11-24 → **ADAPT**
- **Objeto atípico na base**: app proprietário **sem repositório, sem licença e sem changelog público**.
  O `sitemap.xml` tem 8 URLs e nenhuma página de termos, licença ou preço; `Tipo` registrado como `outro`.
- **Arquitetura extraída da própria política de privacidade** (que, ao declarar o que sai da máquina,
  descreve o sistema): app local no Mac (domínio `app.bisqit.mac`) e Windows (`%APPDATA%\Bisqit`) →
  servidor na Vercel → **OpenRouter → Gemini** para classificar `focus`/`neutral`/`drift` → **fal** gera as
  imagens e clipes do "seu cachorro" com um worker no **Railway** → **Upstash** para licenças e contadores →
  **Resend** para o link por e-mail → **Stripe** como *seller of record*. Chaves de modelo e pagamento só no
  servidor; servidor não persiste o que julga. Tudo `REPORTED` — nada verificado no binário.
- **O loop que serve ao Lia Project**: lista embutida + lista do usuário antes de qualquer rede; payload
  cortado (app, URL sem query, título em 140 caracteres, até 6 vereditos anteriores); cache de veredito de
  6 h no cliente; correção "Not a drift" persistida como lista, não como ajuste de modelo; janela de 70 s
  para interceptar a ação; **minimizar em vez de fechar**. É a resposta pronta para a lacuna
  `lia-browser-automation` ("risco de egress") do Lia Project.
- **A escolha de permissão, registrada como caso em `LR-SEC-005`**: sem extensão de navegador, e por isso
  Acessibilidade + Automação no macOS (perguntado uma vez por navegador) e UI Automation no Windows (não
  pede nada). O caso que expõe que um `Grant` precisa de dois eixos — *agir* e *observar* — porque **pausar
  o app não para o julgamento**, só a ação.
- **Modelo de negócio medido no texto deles**: sem trial, com demo que fecha um YouTube real no onboarding;
  preço por país (Brasil citado na lista de preço menor); A/B de plano decidido pelo `install ID`, declarado
  na política de privacidade; custo por chamada de IA como justificativa pública do preço.
- **Duas divergências internas do site** (úteis como exemplo de por que ler as duas páginas): "assinatura ou
  *trial* ativo" na política × "não há período de teste" na página de preço; "se você obtiver o Bisqit pela
  Microsoft Store" no presente × "esse aviso some quando estivermos na Store" no futuro.
- **`NOT_RUN` deliberado, e registrado como limite**: binário proprietário que pede permissões de
  Acessibilidade/Automação não se instala "para ver"; o sandbox também não tem macOS nem Windows. Baixar o
  `.dmg` para checar assinatura e notarização ficou `BLOCKED` (redirect para fora da allowlist). Os dois
  testes que fechariam isto estão na §13 e são do dono: `spctl -a -vv` numa Mac de teste e observar o tráfego
  com o app pausado × aberto.
- Contraste com o nicho, medido nas páginas oficiais de seis concorrentes (Furever Dock, Dumple, Desktop
  Dog, Paw-Paw, AgentPet, Desktop Pet da App Store): dois caminhos para o mesmo problema — hook/telemetria
  local sem LLM, ou geração no servidor com estágio barato antes do pagamento. Nenhum deles publica verificação
  independente; o Bisqit também não.

### FIX / CONTABILIDADE
- `catalog/catalog.tsv` **regenerado**: 33 → **34 linhas**; `data/inventory/license-matrix.tsv` 33 → **34**
  (linha `RESEARCH_ONLY`, sem licença a ler); índice §1 **34 objetos** / 38 linhas com sub-documentos;
  README (185 `.md`, 34 objetos, catálogo de 34 linhas) e `cross-project/licensing/READY-TO-USE-LICENSES.md`
  (34, com a linha nova na tabela-mestra).
- Ponteiros: `projects/lia-project/INDEX.md` (a lacuna `lia-browser-automation` agora aponta para o padrão
  auditado) e `cross-project/security/PER-EXECUTION-PERMISSIONS.md` §2 (sexta fonte de evidência; a frase de
  síntese ganhou o eixo "gradação da ação").
- `data/testing/test-log.tsv` **não** ganhou linha: nenhuma execução deste objeto — o relatório declara
  `NOT_RUN`, e a base não registra leitura de site como teste.

## 2026-11-22 (UTC) — aprofundamento em `mr-mak-workspace` (o que "trabalhar em equipe" quer dizer)

Pedido do proprietário: olhar minuciosamente o Mr. Mak, com foco em trabalho em equipe, a partir do vídeo
do game jam da Epic, do devlog no itch.io e de um post de Patreon. Nenhuma conta, nenhuma instalação em
projeto Lia, nenhum consumo pago, nenhum download de peso.

### ADD — `LR-STUDIO-012` · `witnesstodark/mr-mak-workspace` @ `f096373f` → **ADAPT**
- **Respondido direto**: **não existe colaboração multiusuário**. `SECURITY.md`: roda na máquina do
  usuário, escuta só em loopback, "não exponha por proxy público, túnel ou interface de rede"; o pareamento
  de celular é "cada dono conecta os seus dispositivos". O que existe é **um humano orquestrando N agentes**.
  O "trabalho em equipe" do jam foi **modificação de fork**: instância nova por pessoa + um único chat cuja
  tarefa era sincronizar o workspace a cada 5-10 minutos; o script de sincronização citado no devlog deles
  (tools/sync.py) **não existe** no template.
- **Executado** (Node 22.22.3, clone do commit pinado): `npm test` = **144 passed, 27 failed, 6 skipped**
  em ~43 s — e os 27 falham **todos** pela mesma causa ambiente (`pty.node` sem build nativo; o `npm rebuild
  node-pty` deu node-gyp ERR, registrado `BLOCKED_BY_ENVIRONMENT`, sem insistir). `eslint src` limpo;
  `tsc -b && vite build` exit 0; `check-template.mjs` ok (177 imagens, 8 vídeos, 20 skills);
  `sync-skills.mjs --check` = **375 arquivos idênticos** entre `.agents/` e `.claude/`; asset-delivery 9/9;
  `test-local-voice-setup.py` 4 OK.
- **Suíte do subprojeto vendorizado medida por extenso**: `img2threejs` = **1.418 testes em 139 s, 2 falhas**.
  As duas são o caso mais útil da rodada: um teste que **recusa fixture** ("Assert against the real SKILL.md,
  never a fixture… the fixture is the shape the tooling wants rather than the shape on disk") porque
  `version:` aninhado em `metadata:` é YAML válido, passa na revisão humana e derruba os dois caminhos de
  release. E a CI deles roda **só um** dos 101 arquivos de teste do skill — o gate existe fora do gate.
  Mesma classe do defeito que a `alethe` causou no parser do nosso catálogo.
- **Empacotamento copiado após execução**: rodei `scripts/package_skills.py` duas vezes — **mesmo sha256 do
  ZIP** (4.264.037 B), `manifest.json` com SHA-256 por arquivo (768), timestamp fixo em todas as entradas,
  `tempfile.TemporaryDirectory` + `verify()` **antes** de `replace()`, `LICENSE` e notices dentro do pacote,
  e `--check` para auditar um ZIP alheio.
- **Ponta solta nossa** (afirmação **retificada** no sub-bloco abaixo): o `Mr-Mak-Skills-Free.zip` de 9,9 MB /
  764 arquivos do Lia Studio **não correspondia a nada publicado** — varri os 19 releases (só 3.352.656 B em
  0.4.14 e 4.263.307 B em 0.6.0; nenhum asset entre 9,5 e 10,5 MB) e o gerador atual (769 arquivos).
  Registrado no `DR-0004` como evidência nova **sem decisão**.
- Licença: MIT com detentor **coletivo** ("Mr. Mak Workspace contributors"), `THIRD_PARTY_NOTICES.md`
  cobrindo imagens de terceiros, samples gerados por IA, marca dos provedores e o disclaimer de projeto
  comunitário independente. Pendência então apontada: **`NOTICE` ausente** no `img2threejs` vendorizado,
  contra o texto que promete "license **and notices**" → `REQUIRES_LEGAL_REVIEW` (**também retificada**).
- Do devlog do jam (auto-relato, `REPORTED`): 368 marcos / 712 steps / 830 mídias em 3 trilhas paralelas;
  2.891 saídas em 255 runs por serviço × modelo × pessoa; 411 registros de sessão, 16.338 model calls,
  6,71 B tokens; ledger de 674 registros escritos logo depois de cada job; **US$ 22,97 pagos** de verdade
  (fal.ai) contra **US$ 2.927,42** de valor de tabela estimado, com a nota "nobody paid these sums as such".
  Contrapeso registrado: o vídeo tem link de afiliado e o provedor principal é patrocinado, e a categoria
  "glass box / best devlog" do próprio concurso premia o detalhe do registro.

### FIX / CONTABILIDADE
- `tools/validate.py` continuou intocado na primeira passada; um aviso conhecido permanece (a matriz de
  licença é CRLF e o parser não normaliza, o que produz um `''` residual na comparação com o digest).
- `catalog/catalog.tsv` **regenerado**: 32 → **33 linhas**; `license-matrix.tsv` 32 → **33**;
  `data/testing/test-log.tsv` 24 → **27**; índice (sec. 1 e 3), README (184 `.md`, 33 objetos) e
  `cross-project/licensing/READY-TO-USE-LICENSES.md` (33).
- Ponteiros novos em 5 documentos que já citavam o mr-mak sem auditoria: `governance/LICENSE-AND-PROVENANCE-POLICY.md` §7,
  `cross-project/licensing/ASSET-PROVENANCE.md` §4, `projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md`,
  `projects/lia-studio/README.md`, `projects/lia-studio/INDEX.md` (2 lacunas) e `decisions/PENDING/DR-0004-STUDIO-THIRD-PARTY-ZIP.md`.
- `cross-project/agents/ASSET-AGENT-ORCHESTRATION-DIGEST.md` (`LR-AGENT-005`) §4 ganhou o objeto como
  terceira referência externa de orquestração.

### Recuperação de estado (registrada porque virou recorrente)
- A sandbox voltou em `77a6a7b` com a árvore de trabalho intacta. Restaurado com
  `git fetch origin <branch>` + `git reset --hard FETCH_HEAD` para `0b2cb24`; nenhum arquivo foi perdido
  (183 `.md`, 32 relatórios conferidos antes e depois). Nunca forcei push.

### RETIFICAÇÃO (mesma data, na segunda passada) — duas afirmações acima não aguentaram a verificação

O pedido seguinte do proprietário foi lembrar o que o Research deve fazer nas próprias diretrizes da base
(`MISSION.md` §3: pesquisa = fato, recomendação = opinião técnica, adoção = autoridade do dono; "O Research
não aprova nada") e verificar se as perguntas devolvidas a ele não eram, em parte, trabalho meu. Eram.
Fechando-as com medição:

- **O ZIP do Studio está identificado** — e eu estava errado. Reconstruir o empacotador do próprio autor no
  clone de cada tag dá **764 entradas / 9,83 MB extraídos** em `v0.4.14`, `v0.4.15`, `v0.4.16`, `v0.4.17`,
  `v0.4.19` e `v0.5.0`: o par exato que o Studio registra. Eu havia comparado 4,26 MB **comprimidos** com
  9,9 MB **extraídos**. O pacote é legítimo e publicado; o problema real é estar **defasado** (~8 semanas,
  5 arquivos e ~0,9 MB atrás do `main`, que dá 769 / 10,78 MB).
- **Não há pendência jurídica de `NOTICE`**. A árvore inteira do upstream `img2threejs/img2threejs`
  (★21.761, Apache-2.0) tem só `LICENSE` (11.337 B) — nenhum `NOTICE` para reter, cláusula 4(d) satisfeita
  por vacuidade. A `REQUIRES_LEGAL_REVIEW` que eu abri não existe. O defeito real do vendoring é outro, e é
  deles mesmos: a chave `version:` foi movida para `metadata:` e o badge apagado, e os testes de release do
  próprio projeto falham por isso — o teste anti-fixture deles pegou a edição do empacotador.
- Limite mantido: baixar os assets publicados para conferir `sha256` do `.zip` ficou `BLOCKED` (o download
  redireciona para fora da allowlist do sandbox). A identificação acima é por reconstrução de conteúdo no
  commit da tag, não por comparação de hash.
- `LR-STUDIO-012` ganhou a §13 com a tabela das quatro reavaliações (duas retratações, uma subestimação do
  empacotador, um rótulo `REFUTED`→`DIVERGENCE` na tabela de evidências), e a §7 com as cinco defesas do
  packager que eu havia resumido demais: whitelist fechada, rejeição de symlink, lista de arquivos de estado
  proibidos, verificação de espelho `.agents` ↔ `.claude` byte a byte e exclusão estrutural de
  `.cache`/`__pycache__` (o meu clone tinha um `.cache/spec-search/core_3d.json` gerado localmente, e ele não
  entrou no ZIP).
- **Padrão levado a cabo, não só recomendado**: o `tools/validate.py` ganhou a checagem de forma canônica do
  cabeçalho — a primeira linha da tabela tem de ser `| ID |` — **medida no arquivo em disco**, com um caso de
  regressão que embaralha as linhas do próprio fixture e uma medição direta nos 33 relatórios reais.
  `tools/test_validate.py`: **76 → 78 testes, OK**; `python3 tools/validate.py`: 0 erros, 1 aviso (CRLF
  conhecido), 7 notas.
- `DR-0004` reescrito com a retificação e a pergunta trocada: de "manter ou jogar fora" para **registrar
  tag + `sha256`** (a ação da B continua válida, mas por peso de repositório, não por proveniência ignorada).
- Contagens remediadas: `data/testing/test-log.tsv` 27 → **30 linhas** (11 suítes completas, 4 smokes, 4
  parciais, 11 bloqueios), README (linhas de status, de validador e de testes) e o bloco "Pouco foi executado"
  do `RESEARCH-INDEX.md` — que anunciavam 16, 20 e 24 linhas quando o arquivo já tinha 27; todas defasadas.
- O que sobra para o dono, agora, é só autoridade legítima: **adotar** qualquer coisa nos projetos Lia,
  manter ou não o ZIP no Studio, e reempacotar. Nada disso é minha alçada, e nada disso travou esta rodada.

## 2026-11-22 (UTC) — sete objetos novos, com execucao local onde o ambiente permitiu

Nove alvos indicados pelo proprietario foram abertos; tres deles eram **listagens** (org, org, topic) e
foram consolidados em **um** objeto de paisagem, em vez de fabricar veredito por item. Nada foi
instalado em projeto Lia, nenhuma conta aberta, nenhum peso baixado, nenhuma chave criada, nenhum
consumo pago.

### ADD — `LR-SEC-008` · `bookwjitchieni1986/blender-ai-mcp-addon` → **REJECT**
- Arvore medida: **7 blobs, zero arquivos de codigo** (README, LICENSE, 2 docs, 3 PNGs); 8 commits nos
  segundos iniciais da conta de 9 dias; ★2.580 em 3 dias (2.590 na re-leitura de 2026-11-22).
- O `LICENSE` e MIT com "Copyright (c) 2025 Siddharth Ahuja" — detentor do projeto legítimo
  `ahujasid/mcp-for-blender` (★35.279, fonte completa, PyPI `mcp-for-blender` 2.3.1). Produto nomeado
  "mcp-for-blender-pro" **sem nenhuma mencionao ao original** nos tres arquivos de texto do repo.
- Advisory real (`GHSA-4h8q-hh2j-755w`, `<1.6.5`, corrigida em 1.6.5) e **inalcançavel de avaliar aqui**:
  o objeto advertise "v1.0.0" e nao ha como mapear isso sobre o pacote legitimo.
- Deliberadamente **nao baixei nem abri o ZIP** de 12.849.331 bytes: registrado `BLOCKED`, nao `FALHA`.
- Subproduto: 6 criterios de intake (hash do artefato, fonte no mesmo tag, detentor de licenca coerente,
  idade+historico, estrelas com historia, origem declarada) que o formato atual do Hub nao expressa.

### ADD — `LR-VOICE-002` · `KoljaB/RealtimeTTS` → **REFERENCE_ONLY** (licenca viaja com o artefato)
- **Executado**: wheel 0.8.10 instalado, `import` ok em Python 3.11; suíte da master na forma do CI deles
  = **319 passed, 6 failed, 21 erros de coleta, 14 skipped em 5.41 s**. Os 6 falham todos por `pyaudio`
  ausente — o CI deles instala `portaudio19-dev` + `pyaudio`; eu não instalei pacote de sistema.
- Achado central: **o wheel no PyPI e MIT; a master e Apache-2.0 desde 2026-11-10** (commit de
  relicensing, PR #398), e `RealtimeTTS/_version.py` ainda diz 0.8.10. O addendum empacotado no wheel
  fala "these MIT terms"; na master fala "Apache License 2.0". Mesmo número de versão, duas licencas.
- O adendo de escopo (engines, pesos, vozes e audio de referencia **fora** da licenca) e o modelo
  correto para a lacuna das Skills sem fronteira; mas so **3 das 30 paginas de engine** tem nota de
  licenca — preenchimento parcial, registrado como tal.
- PT-BR existe como `language_router` (`pt`/`pt-br`/`pt-pt` → `portuguese`) e como prefixo Kokoro
  (`lang_code 'p'`); **nada foi sintetizado**, entao as lacunas `BLOCKED`/`NOT RUN` de
  `cross-project/voice/VOICE-STACK-DIGEST.md` seguem intactas.

### ADD — `LR-STUDIO-010` · `NVIDIA/SkillEvaluator` → **ADAPT** (padroes, nao o pacote)
- `pip install` das deps do core ok; `import skillevaluator` ok em 3.11 — mas **3 de 306 arquivos do
  `src` so compilam em 3.12+** (f-string com backslash, PEP 701), e o caminho do Tier 1 alcanca um deles
  no `import`, o que derruba CLI e `pytest tests/validators` (59 erros de coleta). `BLOCKED_BY_ENVIRONMENT`
  com causa exata, nao "falta de tentativa".
- Medidas: **541 arquivos `test_*.py`** contra 306 modulos; SPDX em **301/306** arquivos do `src`;
  `NOTICE`; CHANGELOG com entrada **pinada por assercao de teste** (`tests/changelog_entries.py`).
- Transferivel: gate em 3 niveis com nivel estatico sem chave, *harness check* por host ("description tem
  1.028 unidades UTF-16, 4 acima do teto de 1.024") e SPDX+NOTICE conferidos pelo proprio validador.

### ADD — `LR-STUDIO-011` · `mvanhorn/last30days-skill` → **ADAPT** (anatomia de Skill grande)
- Empacotamento medido nos dois caminhos: tarball `codeload` = **261 arquivos** (sem `tests/`, por
  `export-ignore` declarado e justificado) contra **787 blobs** na arvore. Registrei a diferenca como o
  par que um catalogo precisa guardar: **presente no repositorio × presente no artefato**.
- **Executado**: 153 de 155 `.py` compilam em 3.11 (2 falham por f-string multilinha); o portao
  `ensure_supported_python()` encerra a suíte com mensagem acionavel; contornando o portao, 168 erros de
  coleta — a exigência de 3.12 é real, nao cosmeticismo.
- Corregido o enquadramento que a busca inicial sugeria: a leitura de cookies e **desligada por padrao,
  consentida, filtrada por dominio+nome antes de descriptografar, copia 0600, revogavel por env e por
  `--no-browser-cookies`**. O defeito honesto a reportar e outro: Skill com `Bash, Read, Write` cuja
  seguranca depende de consentimento de setup, documentada em arquivos que a maioria dos hosts nao le.
- `robots.txt` desrespeitado na lane de vagas: `CONFIRMED` como declaracao, `UNVERIFIED` como
  comportamento, e **nao e padrao a copiar** (`REQUIRES_LEGAL_REVIEW`).

### ADD — `LR-FORGE-013` · `apekshik/anymachine` → **REFERENCE_ONLY** (o metodo, nao o software)
- `python3 -m compileall -q .` sobre 284 MB: **exit 0 nos 103 `.py`**. Rebuild de rig **`BLOCKED`**: nao
  ha `blender` no PATH. Zero releases, zero tags, zero tests.
- O que vale: `PIPELINE.md` (243 linhas, dez etapas reference-first, custo honesto — aranha com 40
  referencias, ~2.200 linhas de script, ~40 renders) e um **`check.json` numerico por peca**, com as
  falhas commitadas tambem: `laptop {steps:136, any_overlap:false, min_clearance_mm:0.319}`,
  `rolltop pass 159 estados`, `daypack pass:false max_pen_mm:6.5 / 1619 tri_overlaps`,
  `rucksack lid 11.61 mm / 179`.
- Fronteira de licenca lida em tres camadas: codigo/GLB MIT, imagens "belong to their creators", `data/`
  sem arquivo de licenca, e pesos fora do repo em `~/.anymachine/models/` sem declaracao lida.

### ADD — `LR-MODEL-009` · `BreezeBlue/Breeze-TTS-2` + org `breezeblue-ai` → **REJECT**
- Excluido por tres criterios independentes: **English + Chinese apenas**; pesos, modelos derivados e
  **saidas self-hospedadas** sob licenca research/non-commercial (assinatura paga libera saidas da API
  hospedada, **nao** o modelo); piso de 12 GB em NVIDIA com CUDA.
- Repositorio de inferencia: Apache-2.0, ★1.793, **sem `tests/`**. Os **tres** repositorios de benchmark
  da org nao tem **arquivo de licenca nenhum** — bons numeros medidos por suíte sem licenca, sem
  revisao do checkpoint, **nao sao evidencia importavel**.
- `huggingface.co` nao e alcancavel a partir do sandbox (TLS bloqueado fora da allowlist): sem lista de
  arquivos, sem tamanho real, **sem SHA do peso** — por isso o campo `SHA completo` registra o HEAD do
  repositorio de codigo e o resto fica `BLOCKED`, sem inventar.
- Heranca util: **TTFB / Initial Silence / TTFA** como definicao para a lacuna `BLOCKED` de latencia, e o
  registro de licenca em duas camadas (codigo × pesos × saidas).

### ADD — `LR-AGENT-013` · paisagem negativa (`github.com/skills` + `waifuai` + topic `stt-tts`)
- `github.com/skills` e a org de **cursos** do GitHub (53 repos, 20/20 lidos sem licenca, **zero**
  `SKILL.md`): busca por "skills" sem `filename:SKILL.md` ou `topic:agent-skills` devolve isto.
- `waifuai`: 52 repos, **52/52 sem licenca**, ★max 43, `pushedAt` agrupados (atualizacao em massa).
  unico item emprestavel: `waifu-constitution` como **formato** (constituicao separada do mecanismo).
- `topics/stt-tts`: `total_count` **11**, ★max 12. `PerIPan/OpenWhisperer` (MIT, ★9) fica registrado
  como **piso de escopo** para o conector de voz da CLI — evidencia de que a ideia e pequena, nao de que
  exista projeto para adotar.

### FIX — vocabulario, IDs e contagens
- `tools/validate.py` foi corrigido em 2026-11-20 para aceitar `LOCAL_SMOKE_PASS` no vocabulario de
  execucao; mantive os resultados dos objetos novos dentro do enum.
- IDs renumerados **antes de qualquer commit** para nao colidir com a secao 3 do indice
  (`LR-AGENT-008`, `LR-STUDIO-007/008` e `LR-MODEL-008` ja existiam): ficaram
  `LR-STUDIO-010`, `LR-STUDIO-011`, `LR-AGENT-013`.
- `catalog/catalog.tsv` **regenerado** (25 → **32 linhas**); `data/inventory/license-matrix.tsv` 25 →
  **32 linhas**; `data/testing/test-log.tsv` 20 → **24 linhas**; indice (secoes 1 e 3), README (176 →
  **183** `.md`, 25 → **32** objetos) e os tres digests (`LR-VOICE-001`, `LR-MCP-001/002`, `LR-AGENT-006`)
  apontando para os relatorios novos.
- `tools/validate.py`: **0 erros**, 1 aviso conhecido (a matriz de licenca e CRLF e o parser de
  contagem nao normaliza, o que produz um `''` residual), 7 notas de IDs internos sem cabecalho proprio.
  `python3 -B -m unittest tools.test_validate`: **76 tests, OK**.

### Sem efeito (registrado para nao repetir)
- `breeze-tts-2`: nenhum byte de peso baixado; nenhuma sintese; nenhum preco lido; nenhum espaco pago.
- `last30days-skill` e `SkillEvaluator`: sem conta, sem chave, sem navegador, sem chamada de rede.
- `blender-ai-mcp-addon`: sem download do artefato, sem issue aberta no repositorio alheio.


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
