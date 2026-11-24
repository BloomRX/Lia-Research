# Cap (capsoftware) — gravação de tela open source: MIT só para as crates de câmera, AGPLv3 no resto, e um AGENTS.md que a CI cobra

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-018` |
| Nome | `CapSoftware/Cap` — gravador de tela (web + desktop + mobile + render farm) |
| Tipo | repositório |
| Fonte oficial | https://github.com/CapSoftware/Cap (o campo `name` da API é `capsoftware/cap`, minúsculo) |
| Responsável | Cap Software, Inc. (copyright "2023-present Cap Software, Inc." no LICENSE) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED |
| Recomendação | **ADAPT** — o `AGENTS.md` deles (125 linhas) é o documento de instruções a agentes mais executável que medi até aqui; nada de código |
| Decisão de adoção | — nenhuma registrada |
| Categoria | produto concorrente + política de agente + fronteira de licença |
| Projetos beneficiados | Lia Forge (empacotamento Rust multi-plataforma, ratchet de violações de teste), Lia Project (padrão de `AGENTS.md`), Lia Studio (media/render como separação de serviços), Lia Agent Hub (política de comentário e de arquivo gerado) |
| Versão analisada | `cap-v0.6.3` (release 2026-11-11) |
| Proveniência do conteúdo | **medido por nós** na API (árvore recursiva `truncated: false`, workflows, LICENSE integral, AGENTS.md integral); **nenhum código executado** |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · 25.499★ · 2.424 forks · Rust 57,0 / TypeScript 36,4 / Swift 1,8 |
| Upstream conferido | 2026-11-24 · 6.154 blobs em 7.239 entradas · `size` 1.022.103 KB · 35 arquivos de workflow |
| Próxima revisão | 2027-02-24 |
| Licença | **dividida no próprio arquivo** (`NOASSERTION` na API é consequência disso): "All code residing in the `cap-camera*` and `scap-*` families of crates is licensed under the MIT License (see licenses/LICENSE-MIT)" · "All third party components … original license" · "All other content not mentioned above is available under the **AGPLv3**". O diretório `licenses/` contém **só** `LICENSE-MIT` |
| Confiança | Alta para o que está nos arquivos; nenhuma para comportamento de captura/hardware — nada foi compilado |

---

## 1. Por que este objeto entrou na base

O dono pediu a leva de oito links; o Cap estava entre eles. Entrou no inventário por três motivos que
servem à Lia, e nenhum é a popularidade:

1. é o **segundo precedente de licença dividida** da leva (o primeiro é o Chatwoot, `LR-SEC-009`), e o
   corte aqui não é "diretório comercial" e sim **famílias de crates de hardware** — a pergunta exata
   que o `lia-multiplatform` vai ter de responder quando o Tauri/Rust tocar câmera e microfone;
2. o `AGENTS.md` deles tem um mecanismo que não vi em nenhum outro objeto medido até hoje: as violações
   de qualidade de teste **congeladas por arquivo com contagem decrescente obrigatória** (§4);
3. é um monorepo Rust+TS+Swift com 35 workflows que **não roda neste sandbox** — o que faz dele o
   exemplo concreto de quando um relatório precisa dizer `BLOCKED` em vez de "parece bom".

## 2. O objeto medido (API, 2026-11-24)

| Campo | Valor |
|---|---|
| Estrelas / forks | 25.499 / 2.424 |
| Licença declarada pela API | `NOASSERTION` (por ser arquivo composto) |
| Idiomas | Rust 57,0 % · TypeScript 36,4 % · Swift 1,8 % |
| `size` | 1.022.103 KB · 6.154 blobs / 7.239 entradas de árvore |
| Release mais recente | `cap-v0.6.3` (2026-11-11) |
| Workflows | 35 arquivos |
| Wiki | `has_wiki: true` (raro; os outros sete da leva têm `false`) |
| Apps na raiz | chrome-extension · cli · desktop-gpui · discord-bot · media-server · mobile-ios · render-farm · status · web |
| Raiz | .agents/, .claude/, .config/, .git-blame-ignore-revs, .gitattributes, .mailmap, .vscode/, AGENTS.md, CLAUDE.md, CONTRIBUTING.md, Cargo.lock, biome.json, docker-compose, bun |

Nomes de workflow que valem registro (medidos na listagem, 12 primeiros): `arch-package.yml`,
`baseline-diff.yml`, `ci.yml`, `database-profile-reliability.yml`, `desktop-release.yml`,
`docker-build-media-server.yml`, `docker-build-web.yml`, `engine-verify-label.yml`,
`engine-verify-os.yml`, `engine-verify.yml`, `glass-probe.yml`, `gpui-app-bench.yml`.

Três dessas são o tipo de gate que a Lia não tem e que não é sobre "compilar":
`baseline-diff.yml` (comparação com uma linha de base), `gpui-app-bench.yml` (micro-bench do app
nativo), `engine-verify-os.yml` + `engine-verify-label.yml` (verificação do motor de captura
*por sistema operacional*, disparada também por rótulo de PR). `glass-probe.yml` é a mesma ideia para o
compositor do macOS.

## 3. A fronteira MIT × AGPLv3, lida no arquivo

O texto do `LICENSE` é a AGPL-3.0 inteira precedida de três bullets; o primeiro é o que define tudo:

> "All code residing in the `cap-camera*` and `scap-*` families of crates is licensed under the MIT
> License (see licenses/LICENSE-MIT)."

Consequências medidas (árvore + `licenses/`):

- o MIT não está "em cada crate": está em **um** arquivo (`licenses/LICENSE-MIT`) referenciado pelo
  LICENSE raiz — quem redistribui tem de carregar os dois arquivos, não um só;
- `scap-*` é o motor de captura (o nome aparece em `engine-verify*` na CI); `cap-camera*` é a
  superfície de hardware. **A fronteira foi desenhada em volta do que precisa ser licitamente
  vinculável a driver/firmware e utilizável por integrações**, não em volta do "que é comercial";
- o resto — servidor, web, render farm, desktop — é AGPLv3. Nada de diretório `ee/`.

Isso contrasta com Chatwoot (MIT exceto `enterprise/`) e com OpenProject (GPL-3.0 puro sem fronteira na
árvore): três formas de responder à mesma pergunta, todas com o texto no arquivo da raiz. Comparação e
método em `cross-project/licensing/SPLIT-LICENSE-SCAN.md`.

## 4. O `AGENTS.md` de 125 linhas (o motivo real deste dossiê)

Estrutura medida (títulos lidos): "Pre-Generation Invariants (read BEFORE writing any code)" com
"Zero-tolerance rules", "Post-edit checks (run before you say 'done')", "Rust — write the clippy-clean
form the FIRST time", "TypeScript / JavaScript — write the Biome-clean form the FIRST time", "Tests:
wait on signals, not time", "TypeScript — strictness"; depois "Project Structure & Modules", "Build,
Test, Develop", "Coding Style & Naming", "Testing", "Commits & PRs", "Agent-Specific Practices", "Deep
Investigation Default", "Effect Usage", "Code Formatting & Lint Checks".

Os quatro pontos que eu levaria para os arquivos `agents/` desta casa, transcritos:

1. **Posição das regras**: "These rules are enforced by CI (`cargo clippy -D warnings`, Biome). Fixing
   them afterwards is wasted effort — emit code in the correct shape the FIRST time. Every CI failure
   caused by one of these rules means the agent didn't read this section." — a instrução é escrita como
   *pré-geração*, não como revisão.
2. **Política de comentário com casos proibidos nomeados**: "Default to no code comments. Add a comment
   only after solving a bug … Bad cases that remain banned: narrating what the code does, restating
   types, JSDoc that paraphrases parameter names, 'TODO: refactor' … When in doubt, prefer better
   naming/types over a comment. Applies to every language: Rust, TS, JS, Python, shell, SQL, TOML, etc."
3. **Arquivo gerado é sagrado**: "Never hand-edit generated files … These stay committed because CI and
   fresh clones depend on them … Generating and committing these artifacts is required; modifying
   generated output by hand is prohibited."
4. **O ratchet anti-regressão** (o achado): as violações existentes dos linters de teste ficam
   congeladas **por arquivo** em `scripts/test-lint/oxlintrc.json` (sleeps, polls, timeouts) e
   `scripts/test-lint/test-doubles-allow.json` (doubles), e a regra de convivência é: "Counts only go
   down: when you fix one, lower the entry (delete it at 0). **Never raise a count or add an entry.**"
   Medidos na API: `scripts/test-lint/oxlintrc.json` (8.076 bytes, uma `overrides` com
   `landmines-testing/no-test-doubles: error`) e `scripts/test-lint/test-doubles-allow.json`
   (2.201 bytes) mapeando **33 arquivos** a **324 exceções** congeladas, a maior delas 69 em
   `packages/recorder-core/__tests__/instant-recording-uploader.test.ts` — é esse o tamanho real
   do débito que alguém decidiu não deixar crescer.

   É exatamente o tipo de débito que esta casa carregava: o `data/inventory/license-matrix.tsv` tinha
   um campo com quebra de linha embutida (a linha do anymachine, que fazia um leitor por linha ver um
   registro com `id` vazio) e a última linha sem nova linha — os dois sumiram nesta rodada porque
   alguém olhou, e não porque algo impedisse o terceiro caso. O ratchet é isso: a contagem escrita, que
   torna "adicionar uma exceção nova" um ato visível.

E a política de teste propriamente dita, porque é a mais severa que medi em qualquer objeto: "No fixed
sleeps … No polling spies or request recorders with `expect.poll` / `vi.waitFor` … No retries or raised
per-test timeouts. **A test that passes on rerun is a flake to fix.**" mais "No test doubles in
`apps/media-server`, `apps/render-farm`, `apps/discord-bot`, `apps/status`, `packages/*` and
`scripts/*`: no `spyOn(...).mockReturnValue`, `vi.mock`, or replaced `fetch`. Use the real
implementation and a real local server. `apps/web` and `apps/chrome-extension` are exempt until they
have a real database and browser harness." — proibição de mock com **exceções declaradas e
condicionadas a existir infraestrutura**.

Por fim, o "Deep Investigation Default": "identify the real root cause, not only the symptom … compare
old vs new behavior when reviewing a diff … **call out what is verified vs merely plausible** … verify
the actual user-visible outcome where practical, not only compile/lint success." É, em outra
vocabulário, a regra da nossa casa que separa `CONFIRMED`/`OBSERVED` de `REPORTED` — e está escrita para
o agente, não para o revisor humano.

## 5. O que este objeto não é (e por que o relatório para aqui)

Nada do Cap foi executado. Medido no sandbox: `cargo`, `rustc` ausentes (também `go`, `ruby`,
`flutter`, `docker`), portanto o `ci.yml`/`engine-verify*.yml` não têm como rodar, e o `Result` do
cabeçalho é `BLOCKED` por ambiente — não `NOT_RUN` por preguiça: a pergunta que o dono fez (o que é,
como está organizado, o que a licença permite) é inteiramente respondível por leitura, e foi.

## 6. Mapa para os projetos da Lia

| Destino | O que levar | Seção |
|---|---|---|
| Lia Forge | o ratchet "contagem só desce" para débitos técnicos de estilo/segurança; `baseline-diff.yml` como gate de regressão de tamanho/perf de binário | §4 |
| Lia Project | o formato do `AGENTS.md`: invariantes *antes* da geração, checks pós-edição por tipo de arquivo, e exceções nomeadas | §4 |
| Lia Studio | "a test that passes on rerun is a flake to fix" como política de teste de pipeline de mídia | §4 |
| Lia Agent Hub | política de comentário com casos proibidos + "nunca editar arquivo gerado" | §4 |
| Todos | a fronteira de licença desenhada por **família de crate de hardware**, com um único `LICENSE-MIT` referenciado | §3 |
| `lia-voice-input` | `apps/desktop-gpui` + os helpers de captura como precedent de app nativo Rust com CI por SO | §2 |

## 7. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Compilar `scap-*`/`cap-camera*`, rodar `engine-verify.yml` | `BLOCKED` | sem Rust neste sandbox (medido); e a verificação exige macOS/Linux com periféricos de captura |
| As 23 workflows que não abri | `NOT_RUN` | listei 35 nomes; abri as quatro relevantes para as afirmações §2 |
| Licenças efetivas por crate (o `Cargo.toml` de cada uma) | `NOT_RUN` | a fronteira foi lida do LICENSE raiz; conferir crate a crate é outra passada e é o que o `LR-LIC-006` recomenda como método |
| `apps/render-farm` e `media-server`: o que rodam, que hardware exigem | `UNVALIDATED` | não abri o código |
| O serviço hospedado cap.so (preço, termos) | `NOT_RUN` | fora da pergunta |
| Wiki habilitada: o que contém | `NOT_RUN` | `has_wiki: true` medido; conteúdo não lido |
| Se as 35 workflows passam hoje na upstream | `NOT_RUN` | dá para medir por API (`actions/runs`) na próxima passada; não fiz |

## 8. Recomendação: **ADAPT** (nada de código)

1. **Adaptar o ratchet** (§4 item 4) para o `tools/validate.py`: um JSON de contagens por arquivo para
   os débitos que hoje geram `aviso`, com a regra de que só pode diminuir. É a única sugestão desta leva
   que eu implementaria na infraestrutura da própria casa, e não custa dependência nova.
2. **Adaptar o `AGENTS.md`-como-pre-generação** para os arquivos em `agents/`: mover as regras que hoje
   estão redigidas como "ao revisar" para "antes de escrever", com os comandos pós-edição por tipo de
   arquivo.
3. **Adaptar o modelo de fronteira de licença por família de crate** para a decisão do
   `lia-multiplatform`, se e quando câmera/microfone entrarem — registrado em `LR-LIC-006` §comparação.
4. **Não levar**: o Effect/Next.js deles como arquitetura (decisão do Lia Project, não desta leva), nem
   o `bun` como runtime (não está no sandbox e não há motivo para mudar o `tools/`).
5. **Decisão do dono**: (a) implementar o ratchet no validador agora ou abrir DR; (b) se a casa adota a
   política "zero mocks fora de UI" — ela conflita com o que fazemos em testes de `tools/`; (c) se vale
   uma passada medindo saúde de CI do Cap (linha `NOT_RUN` §7) antes de citar o projeto em qualquer
   recomendação externa.

## 9. Pendências que a Research pode fechar sem autorização nova

Nenhuma delas exige máquina que não temos, nem conta, nem gasto — estão listadas para que a próxima
passada as execute em vez de redescobri-las:

1. ler os `Cargo.toml` das crates `cap-camera*` e `scap-*` e confirmar que cada uma declara (ou não) a
   licença MIT no manifesto: é o que transforma a §3 de "declaração do LICENSE raiz" em "verificado
   crate a crate";
2. abrir `.github/workflows/security-audit.yml`? — não existe aqui; o que existe e não foi lido é
   `baseline-diff.yml`, `engine-verify.yml` e `database-profile-reliability.yml`, e é neles que a
   recomendação da §8 item 2 se apoia (citar sem ler seria o erro que a casa já retificou em
   `LR-STUDIO-012` §13);
3. medir a saúde atual da CI (execuções recentes de `ci.yml`) — dá para fazer por API e diria se os
   gates citados estão verdes ou decorativos;
4. conferir se `scripts/test-lint/` tem teste próprio (eles congelam contagens; seria irônico não testar
   o congelador).

## 10. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| 25.499★ · 2.424 forks · Rust 57,0/TS 36,4/Swift 1,8 · `cap-v0.6.3` (2026-11-11) · `has_wiki: true` · `size` 1.022.103 KB | `CONFIRMED` | `gh api repos/capsoftware/cap` + `releases/latest` + `languages` |
| 6.154 blobs / 7.239 entradas, `truncated: false`; 35 arquivos de workflow; 9 apps na raiz | `CONFIRMED` | `git/trees/HEAD?recursive=1` + `contents/.github/workflows` + `contents/apps` |
| Licença: MIT apenas para `cap-camera*`/`scap-*`, AGPLv3 para o resto, `licenses/` com um único `LICENSE-MIT`, nenhum `ee/` | `CONFIRMED` | `LICENSE` lido integralmente + listagem de `licenses/` |
| `AGENTS.md` tem 125 linhas com os títulos e frases transcritas em §4, inclusive "Counts only go down … Never raise a count or add an entry." | `CONFIRMED` | arquivo decodificado na integra nesta data |
| `scripts/test-lint/oxlintrc.json` e `test-doubles-allow.json` como listas de exceção por arquivo | `CONFIRMED` | os dois arquivos abertos via API nesta data: 8.076 e 2.201 bytes; `test-doubles-allow.json` = 33 arquivos / 324 exceções / máximo 69 |
| Ausência de toolchain para qualquer execução do projeto | `CONFIRMED` | `command -v cargo rustc` sem saída no sandbox |
| Qualidade de captura, desempenho do motor, cobertura de SO | `UNVALIDATED` | nada executado |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · método de licença por
diretório: `cross-project/licensing/SPLIT-LICENSE-SCAN.md` · outro objeto da mesma leva com fronteira
comercial na árvore: `repositories/chatwoot/REPORT.md` · arquivos de instrução a agentes desta casa:
`agents/AGENT-WORKFLOW.md` · débitos que o ratchet resolveria: `RESEARCH-CHANGELOG.md` (avisos CRLF
recorrentes).
