# parallel-code — Electron + SolidJS, 33 releases, e o gate de IPC que a Lia Studio não tem (manifesto + allowlist + teste)

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-022` |
| Nome | `johannesjo/parallel-code` — "Run coding agents from any vendor in their own worktrees": app desktop para rodar Claude Code, Codex, OpenCode, Copilot e Antigravity em paralelo, cada tarefa em seu próprio `git worktree` |
| Tipo | repositório (produto desktop + web) |
| Fonte oficial | https://github.com/johannesjo/parallel-code |
| Responsável | `johannesjo` (usuário individual; contribuidor nº 1 com 1.733) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN — não instalei nem buildo o app (Electron + `node-pty` + `npm install` fora da allowlist) |
| Recomendação | **ADAPT** — sugestão ao dono: **somente** o padrão de gate de superfície (`channel-manifest.json` + allowlist no preload + teste que obriga os três a mudarem juntos) |
| Decisão de adoção | — nenhuma registrada |
| Categoria | orquestrador de agentes + disciplina de superfície IPC |
| Projetos beneficiados | **Lia Studio** (é o destino direto do gate de IPC), Lia Forge (CI com regras estáticas + fixtures), Research (nada novo) |
| Versão analisada | `main` no HEAD de 2026-11-25 (`pushed_at 2026-11-25T15:01:41Z`) · `package.json` **5.1.0** · release mais recente **`v5.1.0` (2026-10-29)** · criado 2026-02-18 |
| Proveniência do conteúdo | medido por nós: censo de árvore, `package.json`, `README.md`, `AGENTS.md` (60 linhas, lido por inteiro), `docker/Dockerfile`, `docs/`, `.github/workflows/` |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api` × 3 (repo, releases, `commits?path=docs/self-hosting.md`) + `git/trees/HEAD?recursive=1` (`truncated: false`) |
| Upstream conferido | **1.106 ★** · 152 forks · 64 issues abertas · 2.085 entradas / 2.000 blobs / **39,5 MB de árvore** · 1.124 `.ts`, 552 `.tsx`, 89 `.kt` (Android) · **0 `SKILL.md`**, 1 `AGENTS.md`, **3 workflows** (`ci.yml`, `release.yml`, `android.yml`) · **33 releases** na página única da API |
| Próxima revisão | 2026-12-09 |
| Licença | **MIT** — `LICENSE` na raiz, `license: null` no `package.json` (medido nas 19 chaves); nenhum `LICENSE` aninhado no censo de 2.085 entradas; **0 `NOTICE`** |
| Confiança | Alta na estrutura e na disciplina de engenharia (texto lido); **zero** quanto ao comportamento (nada executado) |

---

## 1. Correções de premissa, feitas antes de qualquer conclusão

Três coisas que **eu tinha anotado sobre este repositório e que a medição de hoje negou**. Registro porque a
base inteira depende de não repetir premissa herdada:

| Anotação anterior | O que a medição mostra |
|---|---|
| "Tauri 2 + webview + SolidJS; `deploy/Dockerfile`; **242 releases** publicados; `docs/self-hosting.md` com as frases 'no host-OS isolation' e 'not a general access-control boundary'" | **Electron** (42.11.18) + `electron-builder` + SolidJS + Vite; o arquivo é **`docker/Dockerfile`**; releases = **33**; `docs/self-hosting.md` **não existe** — e não há histórico de commit para aquele caminho (`commits?path=docs/self-hosting.md` devolve lista vazia), então não foi removido: nunca existiu neste repositório |

Consequência: as afirmações deste dossiê sobre isolamento vêm **só** do `README.md` e do `docker/Dockerfile`
que li, e de nada que eu tenha "lembrado" de rodada anterior. É também o motivo de o `próxima revisão` estar
a 14 dias: um projeto com este ritmo muda o que ele mesmo diz sobre si.

## 2. O gate de IPC: três arquivos que têm de mudar juntos, e um teste que obriga

Do `AGENTS.md`, seção "### IPC changes" (linhas 52-58, na íntegra):

> Named channels originate in `electron/ipc/channel-manifest.json`; `electron/ipc/channels.ts` exports the
> manifest and its type. When adding a named channel, update the manifest and the inline allowlist in
> `electron/preload.cjs`, plus the handler and frontend call site as needed. […] Run
> `npm run test:unit -- electron/preload-allowlist.test.ts` after changing named channels or the preload allowlist.

Quatro artefatos acoplados — **manifesto → tipo → allowlist do preload → call sites** — com um teste dedicado
que só existe para impedir que o manifesto e o allowlist divirjam. Comparado com o que medimos na Lia
(`LR-STUDIO-005` §"camada 1": **63 strings de canal, zero gate**), isto é exatamente o elo ausente, e é
`ADAPT` no sentido estrito: copiar o **padrão** (fonte única de nomes + teste de divergência), não o código
Electron.

A mesma seção manda que o renderer **não** importe código de backend (*"Renderer imports of backend code are
restricted"*, linha 35) e separa transporte: desktop por IPC, UI de celular por HTTP/WebSocket.

## 3. Regras estáticas com teste, e a admissão honesta do que elas não fazem

Linha 23 do `AGENTS.md`: *"CI tests that Semgrep rules work on fixtures; **it does not scan the repository
with Semgrep**. `npm run lint:security` and `npm run lint:secrets` run …"*. Ou seja: as regras de segurança
estão versionadas e têm fixture, mas **a varredura não é obrigatória no CI** — e isso está escrito, não
descoberto. É o par exato do argumento que o `tools/test_validate.py` desta base sustenta: checagem sem teste
é arbitrariedade; teste sem checagem não protege nada. E o `AGENTS.md:46` fixa até animação em tokens
(`--duration-*`), o que é o mesmo princípio de "não deixar o agente reinventar" aplicado a CSS.

## 4. Isolamento: o que o README realmente promete

| Afirmação (linha) | Texto medido | Como ler |
|---|---|---|
| `README.md:12/17` | *"Run coding agents from any vendor in their own worktrees"* · *"Every change isolated in its own git worktree · Free, open source, no extra platform"* | o isolamento prometido é **de versão** (branch + worktree), não de execução |
| `README.md:66` | *"each task gets its own branch and worktree, **and optionally its own Docker container**"* | container é **opcional**; o padrão é worktree |
| `README.md:123` | *"per-project Docker sandboxes **(not for Antigravity)**, direct mode w/o docker"* | a matriz de suporte é desigual por agente, e isso está dito |
| `docker/Dockerfile:1-5` | *"Pre-installs common dev tools so agents don't waste time on setup. Build: `docker build -t parallel-code-agent:latest docker/` — Size target: ~600 MB (multi-stage not needed; one fat layer is fine for a dev image)"* | a imagem existe para **conveniência de setup**, não como fronteira de segurança — nada de `--network none`, `read_only`, `cap_drop` no cabeçalho nem no comando documentado |

É `DOCUMENTED` e não acusação: eles nunca vendem sandbox de segurança no que li. Mas a diferença entre
"isolamento de versão" e "isolamento de execução" é justamente o ponto que o `LR-STUDIO-005` discute para a
Lia (worktree é fronteira de *git*, não de *filesystem de usuário*) — e aqui há um dado novo e útil para o
dono: um projeto com **89 arquivos Kotlin** (Android) e **3 workflows** trata o container como *opcional*, e
o `desktop` como padrão.

## 5. `docs/` como acervo de decisão, medido

12+ arquivos de plano no diretório, com nomes que denotam estágio: `agent-coordination-plan.md`,
`agent-handoff-plan.md`, `guided-understanding-plan.md`, `investigation-spike.md`, `acp-chat-spike.md`,
`design-doc.md`, `features.md`, `custom-agents.md`, `cards.md`, `document-workspaces.md`,
`architecture-overview.html`, `browser-preview.md`. Dois padrões que nos interessam: sufixo **`-spike`**
(como nosso `NOTES-spike.md` do RouterHub, `LR-PROV-001`) e **`architecture-overview.html`** — uma visão
renderizável do sistema versionada junto do código (nosso `build_replay_html.py`, `LR-CMP-001`, é o
parente próximo). Não li o conteúdo de cada um: contagem e nomes são censo de árvore.

## 6. O que a árvore diz sobre o resto do produto (censo, sem leitura)

2.000 blobs / 39,5 MB em `main`; 1.124 `.ts` + 552 `.tsx` (frontend SolidJS + Electron), 89 `.kt` (Android
nativo, com workflow próprio `android.yml`), **36 `.md`** no total (o `README.md` é o principal; `AGENTS.md`
tem 60 linhas e o `CLAUDE.md` o importa, medido em `AGENTS.md:8`: *"Shared project guidance lives here;
`CLAUDE.md` imports this file"* — o mesmo `@`-import do pipecat, §4 do `LR-AGENT-017`);
`scripts/bench/` com `chat-stream.spec.ts`, `reliability.spec.ts`, `reliability-probes.ts`,
`profile-summary.ts`, `trace-summary.ts` (Playwright como banco de confiabilidade — nome medido, conteúdo
não lido); `scripts/fake-agent.mjs` (harness que finge um agente, para os testes).

## 7. O que não verifiquei, e por quê

- **nada executado**: nem o app, nem os testes unitários, nem o `test:unit -- electron/preload-allowlist.test.ts`,
  nem `npm run lint:security`/`lint:secrets`. Ler o `AGENTS.md` e não rodar o teste que ele manda rodar é
  exatamente a distância que esta base rotula — por isso o estado é `DOCUMENTED` e não `PARTIALLY_TESTED`;
- não abri `electron/ipc/channel-manifest.json` nem `electron/preload.cjs`: **a existência do gate é
  afirmação do `AGENTS.md`** (`DOCUMENTED`); para virar `OBSERVED` basta abrir os dois arquivos e o teste
  (fica como próximo passo barato, e é o que daria ao Studio a forma concreta do manifesto);
- não li os 12 documentos de `docs/` (só nomes e contagem);
- não verifiquei a matriz de suporte por agente (Cline/Cursor/Gemini/Qoder/CoStrict/Antigravity/CodeAlive!)
  nem as permissões que cada CLI deles pede;
- o `web/` (frontend de celular) não foi aberto, só contado nos `.tsx`/`.ts`.

## 8. Recomendação: **ADAPT** (uma prática)

`ADAPT` no sentido estreito e único: **o padrão manifesto + allowlist + teste de divergência** (e, de
brinde, o "CI test rules on fixtures, and say so when it doesn't scan"). Não é "usar parallel-code": a Lia
não tem caso de uso medido para um orquestrador de agentes concorrentes — a decisão de ter algo assim é do
dono do Forge/Studio, e este dossiê não recomenda nada nesse terreno.

## 9. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 1.106 ★ · 152 forks · 64 issues · MIT · TypeScript · criado 2026-02-18 | `OBSERVED` | `gh api repos/johannesjo/parallel-code` |
| **33** releases; mais recente `v5.1.0` (2026-10-29); `package.json` versão 5.1.0 | `OBSERVED` | `releases?per_page=100` (33 itens, 1 página) + `releases/latest` + `package.json` lido |
| 2.085 entradas / 2.000 blobs / 39,5 MB; 1.124 `.ts`; 89 `.kt`; 0 `SKILL.md`; 3 workflows; 1 `LICENSE`; 0 `NOTICE` | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio |
| Electron 42.11.18 + `electron-builder` 26.15.3 + SolidJS 1.9.18; 33 dependências, 30 de desenvolvimento; `license: null` no `package.json` | `OBSERVED` | `package.json` materializado e parseado |
| gate de IPC: `channel-manifest.json` → `channels.ts` → allowlist em `preload.cjs` → teste `electron/preload-allowlist.test.ts`; renderer não importa backend | `DOCUMENTED` (instrução lida; arquivos não abertos) | `AGENTS.md:35,52-58` |
| Semgrep com fixtures no CI e **sem** varredura do repositório; `lint:security`/`lint:secrets` manuais | `DOCUMENTED` | `AGENTS.md:23` |
| worktree é a fronteira padrão; Docker é opcional e "not for Antigravity"; imagem de ~600 MB para conveniência | `DOCUMENTED` (texto) + `OBSERVED` (arquivo) | `README.md:12,17,66,123` + `docker/Dockerfile` (cabeçalho e `FROM ubuntu:22.04`) |
| `docs/` com 12+ planos (`*-plan.md`, `*-spike.md`, `architecture-overview.html`) | `OBSERVED` (nomes) | listagem da árvore |
| a premissa anterior sobre `docs/self-hosting.md` | **retirada** | `commits?path=docs/self-hosting.md` → lista vazia; `contents/…?ref=main` → 404 |
| o app roda, os testes passam, o gate de IPC está íntegro hoje | `NOT_RUN` | nada foi executado nem aberto além dos arquivos citados |

## 10. Ponteiras para a próxima rodada

1. abrir `electron/ipc/channel-manifest.json`, `electron/preload.cjs` e `electron/preload-allowlist.test.ts`
   (3 arquivos, ~200 linhas) — transforma a política citada em `OBSERVED` e dá ao Studio a forma concreta do
   manifesto;
2. ler `scripts/fake-agent.mjs` (o agente falso que os testes usam): é o padrão de "testar orquestração sem
   modelo", o que falta a quase tudo que catalogamos;
3. verificar se `ci.yml` roda `lint:security`/`lint:secrets` (o `AGENTS.md:23` diz que as regras têm fixture,
   mas não afirma se a varredura roda) — 1 leitura de 60 linhas fecha a pergunta.

## 11. Como isto se liga à base

O `LR-STUDIO-005` registrou que a superfície IPC do Studio é 63 strings sem gate. Este objeto é a evidência
externa de que o gate cabível não é biblioteca nem framework: é **um arquivo de manifesto, uma allowlist e um
teste que os compara**. É também o motivo de o `parallel-code` entrar no índice com `ADAPT` de *uma* prática e
não com recomendação de produto: a Lia não precisa de um orquestrador concorrente, mas o Studio precisa de um
teste de divergência.
