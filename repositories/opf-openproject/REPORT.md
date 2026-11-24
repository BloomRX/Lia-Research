# opf (OpenProject) — 123 repositórios medidos, e o cluster de IA que admite ser perigoso

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-016` |
| Nome | `opf` (GitHub org) — OpenProject + 122 repositórios, incluído o cluster de agentes/Skills/evals |
| Tipo | repositório (inventário completo do org; 123 objetos) |
| Fonte oficial | https://github.com/opf |
| Responsável | OpenProject GmbH |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN |
| Recomendação | **ADAPT** — levar três artefatos de política/verificação (declaração de envolvimento de IA, o bloco de WARNING das Skills, o `threat_model.md` versionado); nenhum código |
| Decisão de adoção | — nenhuma registrada |
| Categoria | inventário de org + política de agente |
| Projetos beneficiados | Lia Project (permissão por execução, declaração de autoria), Lia Forge (CI de release + `THIRD_PARTY.md`), Lia Studio (pack de Skills com validação), Lia Agent Hub (formato de SKILL.md mínimo), Lia Model Lab (harness de evals com promptfoo) |
| Versão analisada | HEAD medido em 2026-11-24 (UTC); `opf/openproject` release `v17.8.3` de 2026-11-19; `recense` v0.2.3 de 2026-11-09 |
| Proveniência do conteúdo | **medido por nós** (API do GitHub + clone raso de `opf/openproject-agent-skills`); o `opf/openproject` foi lido por árvore e arquivo, não clonado (a árvore tem 34.051 entradas) |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · `gh api orgs/opf/repos` páginas 1 e 2 → 123 repositórios |
| Upstream conferido | 2026-11-24 · árvore recursiva de `opf/openproject` com `truncated: false` (27.141 blobs, 34.051 entradas) |
| Próxima revisão | 2027-02-24 |
| Licença | `opf/openproject` = **GPL-3.0** lido no arquivo, **sem `ee/`, `premium/` ou `enterprise/` no topo da árvore (0 blobs)**; cluster de IA: `openproject-agent-skills` **MIT**, `recense` **MIT**, `opilot` GPL-3.0, `openproject-llm-evals` GPL-3.0, `openproject-cli` GPL-3.0. Census de licença dos 77 não-fork: **nenhuma 45 · GPL-3.0 19 · MIT 8 · NOASSERTION 3 · Apache-2.0 2** |
| Confiança | Alta para censo, licenças e conteúdo lido; média para "o que o `openproject` faz", que não foi executado |

---

## 1. Por que este objeto entrou na base

O dono apontou a organização e pediu "veja todos os repos desse". Para `opf` a pergunta tem uma
resposta não óbvia: **96 dos 123 repositórios são cauda ou forks de terceiros**, e o sinal real está
em um punhado de repositórios de 0 a 4 estrelas que a empresa abriu em volta do produto durante 2026:
`openproject-agent-skills`, `opilot`, `openproject-llm-evals`, `recense`, `openproject-open_desk`. É
a fotografia mais nítida que encontrei, em todo o GitHub medido até aqui, de **uma empresa de software
livre documentando honestamente o estado do próprio trabalho com agentes**. Isso tem valor de política
para a Lia, que está exatamente nesse ponto.

## 2. O censo (123 repositórios, medidos 2026-11-24)

| Corte | Medida |
|---|---|
| Total | **123** |
| Não-fork | **77** |
| Forks (espelhos de `rails`, `devise`, `angularjs`, `redmine` etc.) | **46** |
| Arquivados (total) | **39** |
| Arquivados entre os não-fork | **32** |
| Licença dos não-fork | nenhuma **45** · GPL-3.0 **19** · MIT **8** · NOASSERTION **3** · Apache-2.0 **2** |
| Idioma dos não-fork | Ruby **31** · nenhum **24** · TypeScript **9** · CSS **3** · Shell **3** · JavaScript **3** · Go **2** · Nix **1** |

Os 24 repositórios sem idioma declarado são, em sua maioria, espelhos de plugins históricos
(`openproject-backlogs`, `openproject-costs`, `openproject-meeting`, `openproject-github_integration`,
`openproject-pdf_export`, `openproject-global_roles` …) todos arquivados em 2018-2019 — o rastro do
modelo antigo de plugins separados.

Top dos não-fork por estrelas:

| Repositório | ★ | Idioma | Licença | Arquivado | Último push |
|---|---|---|---|---|---|
| `openproject` | 17.672 | Ruby | GPL-3.0 | não | **2026-11-24** |
| `openproject-docker-compose` | 354 | Shell | nenhuma | não | 2026-11-19 |
| `openproject-ce` | 97 | Ruby | nenhuma | sim | 2019-06-05 |
| `OpenProjectExcel` | 90 | — | MIT | não | 2024-05-13 |
| `openproject-cli` | 44 | Go | GPL-3.0 | não | 2026-08-18 |
| `typed_dag` | 30 | Ruby | MIT | sim | 2021-04-08 |
| `openproject-proto_plugin` | 28 | Ruby | nenhuma | não | 2025-11-04 |
| `openproject-backlogs` | 21 | — | nenhuma | sim | 2019-01-08 |
| `helm-charts` | 21 | Ruby | GPL-3.0 | não | 2026-11-20 |
| `openproject-translations` | 16 | Ruby | nenhuma | não | 2022-02-21 |
| `openproject-costs` | 12 | — | nenhuma | sim | 2018-11-15 |
| `redmine-to-openproject` | 12 | Ruby | nenhuma | sim | 2023-10-18 |
| `md-to-pdf` | 11 | Ruby | GPL-3.0 | não | 2026-10-08 |
| `commonmark-ckeditor-build` | 5 | TypeScript | NOASSERTION | não | 2026-11-23 |
| `openproject-agent-skills` | 4 | TypeScript | **MIT** | não | 2026-11-19 |
| `openproject-open_desk` | 4 | TypeScript | GPL-3.0 | não | 2026-11-19 |
| `opilot` | 3 | Ruby | GPL-3.0 | não | 2026-11-19 |
| `recense` | 0 | Go | **MIT** | não | 2026-11-09 |
| `openproject-llm-evals` | 0 | Ruby | GPL-3.0 | não | 2026-11-19 |

Os seis non-fork com push mais recente: `openproject` (11-24), `integration-qa-helmfile` (11-23),
`commonmark-ckeditor-build` (11-23), `helm-charts` (11-20), `openproject-docker-compose` (11-19),
`openproject-open_desk` (11-19) — o cluster de IA inteiro está no bolo dos últimos 30 dias.

## 3. `opf/openproject`: o carro-chefe e a fronteira "sem ee/"

Medido por árvore recursiva (`truncated: false`) e por arquivo:

- **27.141 blobs** em 34.051 entradas; licença = **GPL-3.0** (o texto do LICENSE é a GPL-3.0, não a
  AGPL), com LICENSEs também em módulos e na fonte de ícones;
- **0 (zero)** blobs casando com diretório de topo `ee/`, `premium/` ou `enterprise/`;
- 39 workflows, entre elas: `ai-involvement-check.yml`, `cla.yml`, `actions.lock`,
  `brakeman-scan-core.yml`, `codeql-scan-core.yml`, `continuous-delivery.yml`,
  `core-docker-release.yml`, `blocknote-extensions-test.yml`, `crowdin.yml`,
  `create-merge-from-previous-release-branch-pr.yml`;
- na raiz: `SECURITY.md`, `.env.example`, `docker-compose.yml`, `AGENTS.md`, `CONTRIBUTING.md`,
  `docs/`, `.oss-scanner/`; em `/.github/`: `CODEOWNERS`, `actionlint.yaml`, `zizmor.yml`,
  `dependabot.yml`, `codeql/`, `copilot-instructions.md`, `dangerfiles`,
  `flaky-spec-copilot-comment.md`, `pull_request_template.md`;
- release mais recente `v17.8.3` (2026-11-19); idioma 75,6 % Ruby · 17,0 % TypeScript · 5,9 % HTML.

**Divergência registrada**: a descrição pública do OpenProject é de um produto "Community Edition +
Enterprise Edition". No GitHub medido, **a separação não existe como diretório** — o que existe é o
`openproject-ce` arquivado (2019) e a licença GPL-3.0 lisa. Isso significa que a fronteira
comercial do OpenProject não está marcada no repositório principal da mesma forma que em `chatwoot`
(com `enterprise/` próprio `LICENSE`) e em `cal.diy` (com `packages/ee`); é a diferença entre
open-core de árvore e open-core de distribuição. Método e tabela em `LR-LIC-006`.

O `AGENTS.md` do repositório (lido) declara: monorepo de ~840 MB e >1 M de linhas, Rails + PostgreSQL,
front-end Hotwire (Turbo + Stimulus) com Primer via ViewComponent, Angular em migração para fora, e
— o detalhe transplantável — **convida o agente a criar `AGENTS.local.md` / `CLAUDE.local.md`
ignorados pelo git** para preferências de cada desenvolvedor, em vez de poluir o arquivo versionado.

## 4. O gate de envolvimento de IA (o artefato mais valioso desta leva)

`.github/workflows/ai-involvement-check.yml` + `script/ci/ai_involvement_check.sh` (129 linhas,
texto lido) + a seção "AI involvement" do `pull_request_template.md`. Transcrição da seção do
template, exatamente como está no arquivo:

```
## AI involvement
<!-- Self-assess how much AI drove this PR. Uncomment the one line below that fits. -->

<!-- None/Assisted – No AI assistance used OR only autocomplete/pasted snippets. I effectively wrote and understand all the code. -->
<!-- Collaborative – AI generated a substantial part of the code; I reviewed and understand every line. -->
<!-- Directed – I specified the requirements and AI implemented most of it; I validated via testing rather than a full line-by-line review. -->
<!-- Autonomous – AI worked with little supervision; I mainly smoke-tested the result or no human was involved at all. -->
```

O script: `LEVELS='None/Assisted|None|Assisted|Collaborative|Directed|Autonomous'`, remove
comentários HTML com awk (porque podem atravessar linhas), recorta a seção pelo cabeçalho, aceita
explicação após um travessão e **rejeita dois níveis na mesma linha**; sempre sai com `exit 0` e
escreve `status=…`/`level=…` no `$GITHUB_OUTPUT`, e o workflow transforma isso em comentário e
sincroniza o rótulo `ai:*`. A workflow é `pull_request_target` **com justificativa escrita no próprio
arquivo** — "Nothing from the pull request is ever checked out or executed: the checkout below takes
the base branch, and the description is passed from the event payload via an environment variable" —
com `permissions: contents: read` + `pull-requests: write`, `persist-credentials: false`,
sparse-checkout de um único script, concurrency por número de PR e um
`# zizmor: ignore[dangerous-triggers]` justificado, num repositório que tem `zizmor.yml`.

Dossiê próprio (com a proposta de adaptação ao nosso protocolo):
`cross-project/agents/AI-INVOLVEMENT-DECLARATIONS.md` = `LR-AGENT-014`.

## 5. O cluster de IA lido arquivo por arquivo

**`opf/openproject-agent-skills`** — 4★, MIT, 12 arquivos, 216 KB, uma workflow (`release.yml` com
`.changeset/` e `bun.lock`). Um pacote de Skills chamado `openproject-workpackage-crud/` cujo
README abre com um bloco de WARNING em quatro partes (texto lido): **maturidade** — desenvolvido com
assistência de IA, "not … secure or stable enough for general usage"; **causa escritas** — não há
`--dry-run`, e a instrução é apontar para uma instância de teste primeiro; **alvo móvel** — a versão
do CLI pode mudar o significado de uma flag silenciosamente; **sem suporte**. O `SKILL.md` tem
frontmatter com **só `name` e `description`** e a regra: leituras podem rodar automaticamente,
confirme a intenção antes de qualquer escrita, e verifique com um `inspect` de follow-up; proíbe
inventar títulos de workflow actions. Em `validation/`: `baseline.md` (estado **RED**, com as
falhas do agente ingênuo documentadas) e `loopholes.md` (L1–L8), onde está registrada uma **mudança
de contrato que aposentou `--set`, `--status`, `--dry-run`, `--children`, `--json`, `--parent`**.
É o único pack de Skills que medimos nesta base que documenta as próprias falhas como linha de
base — contraste direto com o pack de 20 Skills do `LR-STUDIO-012`, onde a ausência disso foi o
problema.

**`opf/opilot`** — 3★, GPL-3.0, Ruby 87,7 %, README abrindo com "⚠️ EXPERIMENTAL PROOF OF CONCEPT —
use at your own risk!", descrito como "standalone 'OpenProject copilot' que usa o `pi` agent harness +
LLM à escolha". Arquitetura medida na raiz: `Dockerfile.harness`, `Dockerfile.inference-gw`,
`Dockerfile.mcp-gw`, `Dockerfile.runner`, `compose.yml`, `repos.json`, `CLAUDE.md`, `.env.example`,
`Gemfile`, `Rakefile`, `TODO.md` — **quatro contêineres para um experimento** (harness, gateway de
inferência, gateway MCP, runner), e **uma** workflow (`test.yml`). É o oposto do `AppFlowy-Cloud`: aqui
a empresa mantém o servidor de agente em código aberto e com fronteira de contêineres explícita.

**`opf/openproject-llm-evals`** — 0★, GPL-3.0, zero workflows. `promptfoo` com `default_judge.yml`,
`providers.yml`, dois evals (`proofread/`, `refine-ticket/`), `Makefile`, e a chave `OPENROUTER_API_KEY`
vinda por `.env` (README). Ou seja: **eval de LLM mantido fora da CI** — deliberadamente, porque
rodar modelo custa dinheiro. Isso é um precedente útil para a decisão do Lia Model Lab sobre o que
pode ou não entrar em CI (item do dono, §9).

**`opf/recense`** — 0★, **MIT**, Go, v0.2.3 (2026-11-09), `THIRD_PARTY.md`, `charts/`, `install.sh`,
`Dockerfile`, `cmd/`, `internal/`, `deploy/`, duas workflows (`ci.yaml`, `release.yaml`). README:
"Know which machines and containers you have, what software they contain, and which known
vulnerabilities affect them … uses Syft for complete software inventory and Grype for vulnerability
matching. No database, dashboard, or central Recense server is required" — um agente que escreve JSON
estruturado no pipeline OpenTelemetry existente. É **o modelo de inventário de segurança mais leve que
vi em toda a base**, e MIT. Relevante para `lia-security-review` (ainda `❌` vazia em
`projects/lia-project/INDEX.md`) e para o `data/inventory/` desta própria casa.

**`opf/openproject-cli`** — 44★, Go, GPL-3.0, push 2026-08-18: é o CLI que o pack de Skills invoca —
a "flag que muda de significado" do §5 é a superfície deste repositório. Não lido nesta rodada.

## 6. Padrões do org que a Lia deveria copiar (todos medidos, nenhum adotado)

1. **Declaração de envolvimento de IA com gate de CI e rótulo automático** (§4) — o custo de
   implementado é ~1 script + 1 template; o nosso `RESEARCH-CHANGELOG.md` e os relatórios já têm a
   matéria-prima.
2. **`zizmor.yml` + `actionlint.yaml` + `actions.lock` + `cla.yml`** na mesma pasta `.github/`:
   fornecedura de CI tratada como código, com CLA. Comparar com as 262/262 pins do `VoiceStudio`
   (`LR-VOICE-003`) — dois jeitos de chegar lá, um por ferramenta, outro por teste próprio.
3. **`.oss-scanner/` com `threat_model.md` versionado** (openproject, OpenWhispr e `open-seo` têm —
   medido nos três). Um modelo de ameaça dentro do repositório, com Dockerfile para o scanner.
4. **WARNING de maturidade no topo do README de um pack de Skills** (§5) — custo zero, e resolve
   exatamente a classe de problema que o `DR-0004` tratou do lado do consumo.
5. **`AGENTS.local.md` ignorado pelo git** (§3 fim) — preferências por máquina sem contaminar o
   arquivo versionado; nossa versão disso seria um `AGENTS.local.md` no sandbox de pesquisa.
6. **`THIRD_PARTY.md` + `charts/` + `install.sh` num projeto de 0 estrelas** (`recense`) — higiene de
   proveniência independentemente de popularidade.

## 7. Mapa para os projetos da Lia

| Destino | O que levar | Seção |
|---|---|---|
| Lia Project | o formato "leitura roda sozinha, escrita pede confirmação, e escrita é verificada com inspect de follow-up" — é literalmente o `PER-EXECUTION-PERMISSIONS.md` com implementação externa | §5 |
| Lia Project / Research | o gate de declaração de envolvimento de IA | §4, `LR-AGENT-014` |
| Lia Forge | `actions.lock` + `actionlint` + `zizmor` + `cla.yml` como conjunto de CI; `THIRD_PARTY.md` do `recense` | §6 |
| Lia Studio | o pack MIT com `validation/baseline.md` + `validation/loopholes.md` como o formato que faltou no caso do `LR-STUDIO-012` | §5 |
| Lia Agent Hub | `SKILL.md` com frontmatter mínimo (name + description) e regras no corpo | §5 |
| Lia Model Lab | `openproject-llm-evals`: promptfoo + judge em YAML + provedores separados, mantido fora da CI | §5 |
| `lia-security-review` (lacuna) | `recense`: agente Go + Syft + Grype sem servidor central, MIT | §5 |

## 8. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Rodar `openproject` (Rails + PostgreSQL) ou o `opilot` | `BLOCKED` | sem `ruby` nem `docker` neste sandbox (medido); nenhuma imagem puxada |
| Executar o `script/ci/ai_involvement_check.sh` contra um corpo de PR real | `NOT_RUN` | dava para fazer localmente com um arquivo; **ficou para a próxima passada** — é nível 1 e eu não o fiz, registro como falha minha, não como bloqueio |
| As outras 104 workflows do `openproject` | `NOT_RUN` | só a lista de nomes foi varrida; as de interesse para nós foram lidas |
| Onde fica o código da Enterprise Edition | `UNVALIDATED` | não está no org; procurar fora disso seria especulação |
| `openproject-cli` (a superfície que o WARNING do §5 cita) | `NOT_RUN` | fora do escopo da pergunta; é a leitura que falta para fechar a loopholes L1–L8 |
| Estado de segurança (`recense` com Syft/Grype) | `NOT_RUN` | binário não baixado nem executado |
| Os 46 forks e os 32 não-fork arquivados, um a um | `NOT_RUN` | o corte agregado foi medido (censo §2); os individuais são cauda |

## 9. Recomendação: **ADAPT**

1. **Adaptar (proposta, não decisão)**: o gate de §4 no fluxo da Research, como bloco opcional de
   auto-declaração nos relatórios; e o WARNING de §5 como modelo para qualquer pack de Skills que a
   Lia publique. Detalhamento e as três objeções que já antecipo em `LR-AGENT-014` §5–§6.
2. **Não adotar**: nenhum código deste org; GPL-3.0 no produto e o fato de o `openproject-cli` ser
   GPL-3.0 tornam "usar o CLI no Lia" uma decisão de licença do dono, não da Research.
3. **Testes que fecham os `NOT_RUN` acima — e que a Research pode fazer sem autorização nova**: (a)
   executar o `ai_involvement_check.sh` com corpos de exemplo (bom/ruim/múltiplos níveis) no sandbox;
   (b) ler o `README.md` + `CHANGELOG` do `openproject-cli` para casar as flags aposentadas. Se o dono
   quiser, fecho isso na próxima passada.
4. **Decisão do dono**: (a) se o Lia Project adota declaração de envolvimento de IA em PR; (b) se
   `recense` (MIT) entra como candidato de inventário de segurança para as máquinas do Studio/Forge;
   (c) se evals de modelo podem ou não existir em CI (o precedente do opf é "não, por custo").

## 10. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| 123 repositórios; 77 não-fork; 46 forks; 39 arquivados (32 entre não-fork) | `CONFIRMED` | `gh api orgs/opf/repos?per_page=100` páginas 1–2, contados no arquivo JSON |
| Licenças dos não-fork: 45 nenhuma / 19 GPL-3.0 / 8 MIT / 3 NOASSERTION / 2 Apache-2.0 | `CONFIRMED` | campo `license.spdx_id` do mesmo censo |
| `openproject`: 17.672★, GPL-3.0, v17.8.3 (2026-11-19), 39 workflows, 27.141 blobs em 34.051 entradas, `truncated: false` | `CONFIRMED` | `repos/opf/openproject` + `releases/latest` + `contents/.github/workflows` + `git/trees/HEAD?recursive=1` |
| Nenhuma diretoria `ee/`, `premium/` ou `enterprise/` no topo da árvore | `CONFIRMED` | filtragem da árvore recursiva (0 coincidências) |
| `SECURITY.md`, `.env.example`, `docker-compose.yml`, `AGENTS.md`, `CONTRIBUTING.md`, `docs/`, `.oss-scanner/{Dockerfile,Dockerfile.dockerignore,database.yml,threat_model.md}` na raiz | `CONFIRMED` | listagem da raiz + `contents/.oss-scanner` |
| Template com 4 níveis de envolvimento de IA, todos dentro de comentários HTML; script com 5 níveis aceitos, saída `status=`/`level=`, `exit 0` sempre | `CONFIRMED` | `pull_request_template.md` e `script/ci/ai_involvement_check.sh` (129 linhas) decodificados |
| Workflow `pull_request_target` com justificativa escrita, `permissions` mínimas, checkout da base branch e `# zizmor: ignore[dangerous-triggers]` | `CONFIRMED` | `ai-involvement-check.yml` decodificada |
| `openproject-agent-skills`: MIT (Copyright (c) 2026 the OpenProject GmbH), 12 arquivos, 216 KB, WARNING em 4 partes, `validation/baseline.md` RED, `loopholes.md` L1–L8 com flags aposentadas | `CONFIRMED` | clone `--depth 1` + leitura de todos os arquivos |
| `opilot` é prova de conceito declarada, com 4 Dockerfiles e 1 workflow | `CONFIRMED` (arquivos) / `REPORTED` (o "use at your own risk") | listagem da raiz + README |
| `recense`: MIT, v0.2.3 (2026-11-09), Syft + Grype, sem servidor central, `THIRD_PARTY.md` | `CONFIRMED` | LICENSE + README + `releases/latest` + raiz |
| `openproject-llm-evals` roda fora da CI (0 workflows) e usa promptfoo com OpenRouter | `CONFIRMED` | listagem de workflows + README |
| O binário/serviço se comporta como os READMEs dizem | `UNVALIDATED` | nada executado; sem Ruby/Docker no ambiente |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · gate de declaração:
`cross-project/agents/AI-INVOLVEMENT-DECLARATIONS.md` · método de licença por diretório:
`cross-project/licensing/SPLIT-LICENSE-SCAN.md` · contraste de pack de Skills:
`repositories/mr-mak-workspace/REPORT.md` (`LR-STUDIO-012`) · outro org da mesma leva:
`repositories/appflowy-io/REPORT.md`.
