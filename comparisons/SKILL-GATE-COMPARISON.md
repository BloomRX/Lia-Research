# Comparação — o que um gate de Skill verifica, e o que ele não vê

| Campo | Valor |
|---|---|
| ID | `LR-CMP-004` |
| Pergunta | se a Lia for exigir "Skill válida" antes de publicar, **qual** validação é essa — e o que escapa dela? |
| Data | 2026-11-25 |
| Evidência | **executada aqui**: 178 `SKILL.md` materializados de 10 repositórios, passados por dois validadores open-source independentes (o da Anthropic e o analisador do DeerFlow); nada foi afirmado por impressão |
| Objetos cobertos | `anthropics/skills` (raiz + `skill-creator`), `anthropics/claude-plugins-official` (`skill-creator` de plugin), `obra/superpowers` (`systematic-debugging`), `parallel-web/parallel-agent-skills`, `JCodesMore/ai-website-cloner-template`, `bytedance/deer-flow`, `pipecat-ai/pipecat`, `dyad-sh/dyad`, `infiniflow/ragflow`, `aaif-goose/goose`, `D4Vinci/Scrapling` + o tópico `skill-creator` |

---

## 1. Como este documento nasceu

O dono mandou 16 links numa mensagem. Onze deles são o mesmo objeto visto de ângulos diferentes: **pacote
de Skills de agente** — dois caminhos do repositório oficial da Anthropic, o `skill-creator` do diretório
de plugins, uma Skill específica do `superpowers`, um repositório de Skills de fornecedor de API, um
template de clonagem, e quatro repositórios de produto que também publicam Skills dentro. Fazer um dossiê
por link seria mentira com o conteúdo: o que há de novo aqui só aparece **cruzando** os corpos.

Então: os dossiês dos produtos ficaram em `repositories/*` (`LR-AGENT-015`…`018`, `LR-FORGE-022`/`023`,
`LR-MODEL-010`, `LR-VOICE-005`, `LR-SEC-010`) e a comparação de *gates* é este documento.

## 2. O corpus, medido

**187 `SKILL.md`** no censo dos 13 repositórios (árvore recursiva via API, `truncated: false` em todos):
`claude-plugins-official` 62 · `deer-flow` 33 · `dyad` 24 · `anthropics/skills` 20 ·
`parallel-agent-skills` 16 · `superpowers` 15 · `pipecat` 12 · `ragflow` 2 · `goose` 1 · `Scrapling` 1 ·
`ai-website-cloner-template` 1 · `daytonaio/daytona` 0 · `parallel-code` 0.

Depois de materializar **cada diretório de Skill com todos os seus arquivos** (sparse-checkout dirigido
pelas árvores), **178** dos 187 arquivos ficaram disponíveis por completo para os dois validadores — os 9
restantes (1 do Scrapling, 1 do diretório de plugins, 4 do `deer-flow`, 1 da Anthropic, 1 do
`parallel-agent-skills`, 1 do ragflow) não caíram nos padrões de checkout e **saem das contagens de
frontmatter**, entrando só no censo de árvore. O conjunto virou **173 pacotes** (algumas Skills compartilham
diretório de pacote).

| Medida do corpus | Valor |
|---|---|
| frontmatter YAML parseável | **176 de 178**; 2 com YAML inválido (`dyad/.claude/skills/deep-review`, `pipecat/.claude/skills/squash-commits`) |
| chave `name` | 176 · `description` 175 |
| `name` ≠ nome do diretório | **29 de 178** (16 %) |
| `allowed-tools` | 26 arquivos; **19 concedem `Bash`**, mas **17 usam escopo parametrizado** (`Bash(gh:*)`, `Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/ledger.py *)`) em vez de liberar o shell inteiro |
| `disallowed-tools` | 6 · `disable-model-invocation` 8 · `user-invocable` 17 · `argument-hint` 22 · `compatibility` 26 |
| `license:` na frente | **19 de 178** (10,7 %) — 17 deles estão no mesmo repositório (`anthropics/skills`) |
| `version:` | 13 · `metadata:` 14 · `required-secrets` 1 · `hooks` 1 · `agent`/`context` 2 |
| corpo referencia `scripts/…` | 57 · referencia `references/…` | 28 |
| `description` | mediana 248 caracteres, p90 771, máximo **1.068**, 1 arquivo acima do limite de 1024 |
| `LICENSE` ao lado do `SKILL.md` (por árvore, nos 187) | **23** — e **18** dos 23 são do `anthropics/skills` |

### Distribuição por repositório (a mesma contagem, partida)

`n` = `SKILL.md` no censo da árvore · `arquivo LICENSE` = quantos têm `LICENSE*` no **mesmo diretório** ·
`materializados` = quantos foram baixados com todos os recursos para validação · `declara licença` e
`declara allowed-tools` = chaves no frontmatter dos materializados.

| Repositório | `SKILL.md` | com arquivo `LICENSE` ao lado | materializados | declaram `license:` | declaram `allowed-tools` |
|---|---:|---:|---:|---:|---:|
| `anthropics/claude-plugins-official` | 62 | 2 | 61 | 1 | 14 |
| `bytedance/deer-flow` | 33 | 2 | 29 | 1 | 3 |
| `dyad-sh/dyad` | 24 | 0 | 24 | 0 | 0 |
| `anthropics/skills` | 20 | 18 | 19 | 17 | 0 |
| `parallel-web/parallel-agent-skills` | 16 | 0 | 15 | 0 | 8 |
| `obra/superpowers` | 15 | 0 | 15 | 0 | 0 |
| `pipecat-ai/pipecat` | 12 | 0 | 12 | 0 | 1 |
| `infiniflow/ragflow` | 2 | 0 | 1 | 0 | 0 |
| `aaif-goose/goose` | 1 | 0 | 1 | 0 | 0 |
| `D4Vinci/Scrapling` | 1 | 1 | 0 | 0 | 0 |
| `JCodesMore/ai-website-cloner-template` | 1 | 0 | 1 | 0 | 0 |
| **total** | **187** | **23** | **178** | **19** | **26** |

O padrão não é ruído: **o único repositório do corpus que licencia por Skill é o da Anthropic** (18 de 20), e
os quatro repositórios com mais Skills depois dele — `deer-flow` (33), `dyad` (24),
`parallel-agent-skills` (16) e `superpowers` (15) — têm **0, 0, 0 e 0** arquivos de licença por Skill. E os **4** casos fora da Anthropic
(`deer-flow`: `skills/public/{skill-creator,frontend-design}` · `claude-plugins-official`:
`plugins/{skill-creator,frontend-design}/skills/…`) são exatamente **as duas Skills copiadas do acervo da
Anthropic** — o `LICENSE.txt` viajou com a cópia, e nenhuma das outras Skills desses repositórios levou
licença alguma. É a evidência mais direta que encontrei de que **a licença de uma Skill é atributo do
pacote, não do repositório que o hospeda**: quem redistribui o texto redistribui o envelope, e quem escreve
o próprio não envelopeia nada.

Três coisas nesse quadro já respondem metade da pergunta:

1. **"Skill válida" não é uma propriedade, é a decisão de qual schema você adota.** 53 dos 80 rejeitados
   abaixo foram rejeitados **só por chave desconhecida** (`version`, `argument-hint`, `user-invocable`,
   `disallowed-tools`, `tools`) — campos que o próprio ecossistema usa e o validador da Anthropic não
   reconhece;
2. quase ninguém licencia por Skill (19 declaram, 23 têm arquivo), exceto um repositório — que é o da
   Anthropic;
3. `description` estourando limite existe **no acervo oficial** (1 caso, `skills/claude-api`, 1.068 chars).

## 3. Os dois validadores, executados aqui

| | `anthropics/skills → skill-creator/scripts/quick_validate.py` | `deer-flow → deerflow/skills/review/analyzer.py` |
|---|---|---|
| o que é | 168 linhas, stdlib + PyYAML; CLI `python quick_validate.py <dir>`; exit 0/1 | 393 linhas de analisador + 410 de leitores + 242 de renderizador + 2.000 linhas de `skillscan/`; CLI próprio com `--profile`, `--fail-on {never,warning,error,blocker}` |
| o que verifica | **schema**: frontmatter existe, YAML parseia, `name` minúsculas com no máximo 64, `description` não vazia com no máximo 1024, `compatibility` string com no máximo 500, e **nenhuma chave fora da lista permitida** | **pacote e comportamento**: caminhos de recurso (`resource.missing`, `escaping-link`, `unreferenced`), endpoints (`network-cleartext-http`, `network-local-http`), segredos (`secret-env-assignment`), nomes inválidos, tamanho de descrição, e **AST dos scripts em Python** (`python-env-dump-exfil`, `python-shell-exec`, `python-subprocess`, `declaration-sensitive-capability`) |
| origem dos achados | — | `review-core` 3.456 · `skillscan` 365 (perfil `deerflow`, 173 pacotes) |
| veredicto | válido / inválido + motivo | `readiness` ∈ {`publish_candidate`, `revise`, `blocked`} + `summary{blockers,errors,warnings,infos}` |
| perfis | um | dois: `deerflow` e `agentskills` (o segundo acrescenta `agentskills.description-length`, **107 achados** que o primeiro não faz) |

Execução real desta rodada: **346 análises (173 pacotes × 2 perfis) e 177 validações, 0 erro de execução**.

## 4. O resultado que importa: os dois gates discordam em 1 de cada 4

| | DeerFlow: `publish_candidate` | DeerFlow: `revise` | DeerFlow: `blocked` |
|---|---|---|---|
| **Anthropic: válido** | 78 | 11 | **5** |
| **Anthropic: inválido** | **39** | 36 | 4 |

Leitura das duas células em negrito:

- **39 pacotes rejeitados pelo validador da Anthropic estão prontos para publicar** segundo o analisador do
  DeerFlow. Todos os 80 "inválidos" se explicam por schema: 53 por chaves desconhecidas, 22 por `name`
  (maiúsculas, pontuação, divergência com o diretório), 2 por YAML quebrado, 2 por `description`, 1 por
  `compatibility` virar dicionário.
- **5 pacotes aceitos pelo validador da Anthropic estão `blocked` no DeerFlow.** São do próprio acervo
  oficial: `skills/claude-api`, `skills/docx`, `skills/pptx`, `skills/xlsx`, `skills/webapp-testing` — e o
  gatilho é sempre o mesmo par de regras sobre o código distribuído junto:
  `python-env-dump-exfil` ("o Python lê o ambiente inteiro e usa um canal de saída") e
  `python-shell-exec` / `python-subprocess`, mais 3 achados de `package-python-analysis-limit` por causa de
  esquemas XSD de 1 MB dentro de `scripts/office/schemas/`.

Os cinco são, quase certamente, **falsos positivos de exfiltração**: `scripts/office/soffice.py` é o
envoltório que fala com o LibreOffice local. Isto não desqualifica o gate — qualifica o desenho: é
impossível ter um portão determinístico de Skills **sem** um mecanismo de justificativa/allowlist por
regra, porque o código legítimo de manipulação de arquivos sempre vai parecer exfiltração para um AST.

**Pronto para publicar, no outro lado:** `obra/superpowers` foi o corpus mais limpo dos dez
(**13 publish · 1 revise · 0 blocked**), seguido de `deer-flow` (27 · 1 · 1 — e o seu `blocked` é o
*fixture* `evals/fixtures/blocked`, funcionando como esperado), `parallel-agent-skills` (12 · 3 · 0),
`claude-plugins-official` (44 · 16 · 1), `anthropics/skills` (11 · 3 · 5), `ragflow` (1 · 0 · 0),
`pipecat` (8 · 2 · 1), `dyad` (**1 · 21 · 1** de 23 pacotes).

## 5. Convenções de empacotamento medidas (o "onde mora a Skill")

| Convenção | Quem usa | Efeito prático |
|---|---|---|
| `.claude/skills/<nome>/SKILL.md` | `dyad` (24), `pipecat` (12) | ligada a um runtime específico; dentro de `.claude/` há também `agents/*.md` |
| `.agents/skills/…` | `ragflow` (2), `goose` (1, em `evals/harbor/.agents/skills/`) | caminho neutro de runtime, ainda raro no corpus |
| `skills/public/<nome>/` | `deer-flow` (29 medidos de 33) | "public" vs "custom" vs "legacy" — a árvore declara a política de procedência |
| `plugins/<plugin>/skills/<nome>/` | `claude-plugins-official` (61) | a Skill é unidade do plugin, não do repositório |
| `agent-skill/<Nome>-Skill/` | `Scrapling` | biblioteca que distribui a própria Skill como subproduto versionado junto do código |
| frontmatter com `@AGENTS.md` ou `CLAUDE.md` de 1 linha | `pipecat` (`CLAUDE.md` = `@AGENTS.md`), `parallel-code` ("`CLAUDE.md` imports this file") | uma fonte, dois consumidores — mesma finalidade dos symlinks do `cal.diy` (`LR-FORGE-019`), sem depender de symlink no Windows |

E a origem do texto, quando é gerado: o `AGENTS.md` do `ai-website-cloner-template` começa com um bloco
delimitado por comentários `BEGIN/END:nextjs-agent-rules`, escrito **pelo `next dev`**, que diz ao agente
*quem* escreveu aquilo, onde verificar (`node_modules/next/dist/server/lib/generate-agent-files.js`) e por
que não removê-lo ("removing it from a diff only re-creates the uncommitted change"). Das cinco soluções de
anti-deriva medidas nesta base e nesta leva (symlink do cal.diy, `sync-plugin-skills.mjs` com `test -z
git status` do open-seo, espelho byte-idêntico, `@import`, e este bloco autoexplicativo), **a última é a
única que explica ao agente o motivo** — e custa zero.

## 6. O que nenhum dos dois gates vê (medido por ausência, não por opinião)

Nenhum dos validadores checa, no corpus medido:

- **se a Skill funciona**. A DeerFlow tem um `evals.json` com 6 casos e a Anthropic tem `run_eval.py`,
  `run_loop.py`, `aggregate_benchmark.py`, `improve_description.py` e um `eval-viewer/` — mas **nenhum dos
  dois gates executa** nada do que valida (o CLI deles diz "without executing it" no próprio texto). A
  distinção é a mesma da nossa coluna `level` em `data/testing/test-log.tsv`;
- **procedência do texto**: nenhum verificador olha se a Skill é cópia de terceiro; 158 dos 178 pacotes
  não têm `LICENSE` ao lado e 159 não declaram `license:`;
- **a licença do que a Skill baixa**: o `Scrapling-Skill` traz `LICENSE.txt` próprio, e as Skills do
  `anthropics/skills` também — os outros não;
- **derivade de `name` × diretório**: 29 divergem; nenhum dos dois gates trata isso como bloqueio
  (a DeerFlow só sinaliza quando o nome tem caractere inválido: 21 achados).

Reproduzi os seis casos do `evals.json` do `skill-reviewer` só com a camada **determinística**: **2 de 6
batem** com `expected_readiness` (`publish-candidate` ✓, `blocked` ✓); os outros quatro divergem porque
exigem a rubrica semântica — inclusive `zh-output`, que no manifest **não tem** `expected_readiness`
algum. É a demonstração mais nítida que encontrei de que "passar no scanner" e "estar pronta para
publicar" são afirmações diferentes, e de que um gate sem camada semântica não decide os casos difíceis.

## 7. O que a base pode fazer com isso (proposta; nada aplicado nos apps da Lia)

> **Escopo desta seção** — sugestão a partir do que a evidência sustenta, com a pergunta de viabilidade de
> cada app. Não é instrução para nenhum app e nada aqui foi aplicado fora desta base (`MISSION.md` §3,
> `DR-0019` §5).

| Destino | O que sugiro considerar | O que custaria |
|---|---|---|
| **Lia Agent Hub** | dois estágios separados: **gate de schema** (permitindo chaves próprias *por registro*, não por rejeição) e **gate de segurança de pacote** (recursos, endpoints, scripts). Publicar só de passar no primeiro, e *revisar* no segundo | o gate de schema cabe em `tools/validate.py` como checagem nova; o de segurança existe — é o analisador do DeerFlow (MIT), que podemos executar aqui sem adotar o runtime deles |
| **Lia Agent Hub** | adotar a regra de `name` × diretório (29/178 divergem hoje no ecossistema) e o limite de `description` com contagem explícita | ~30 linhas de verificação |
| **Research (esta base)** | permitir chave desconhecida **com justificativa** — o mesmo mecanismo que a célula `5 blocked` acima prova ser indispensável | é política de escrita, não código |
| **Lia Studio / Forge** | Skills de fluxo (revisar PR, descrição, changelog) já existem em `pipecat` (12) e `dyad` (24) como modelos de texto e de gradação; o `systematic-debugging` do superpowers (5 arquivos, com um `.sh` de procedimento) é o formato mais denso medido | decisão de escopo de produto, não deste digest |

## 8. O gênero "skill-creator", medido no tópic

`topic:skill-creator` = **81 repositórios**. Cabeça da lista por estrelas: `rpamis/comet` 3.316 (MIT),
`joeseesun/qiaomu-meta-skill` 393 (MIT), `AGI-comming/functional-skill-creator` 257 (MIT),
`antongulin/opencode-skill-creator` 199 (Apache-2.0), `oil-oil/oil-skill-creator` 103 (MIT),
`balancegsr/skill-creators` 23, `vignzpie/resume-agent-skills` 20, e cauda com 9–14 ★. Licença: MIT domina,
com dois **SEM LICENÇA** (`jalaalrd/video-to-skill`, `youngfreeFJS/skill-test-skill`) e um `NOASSERTION`.
Dois deles ("`skill-test-skill`": *tests and scores any Agent Skill against the official …*) são
concorrentes diretos dos gates deste documento — não abertos nesta rodada; ficam como fila.

## 9. O que não verifiquei, e por quê

- O corpus é o que **estes** repositórios distribuem. Não busquei Skills fora dos repositórios pedidos
  (a não ser o tópico do §8), então a taxa de 53/80 "inválidos por chave" pode mudar em outro recorte.
- Não rodei os validadores sobre o acervo do `lia-agent-hub` (não há `SKILL.md` nesta base; os nossos
  registros são `.md` de catálogo). A comparação "nós × eles" fica **`NOT_RUN`** — dá para fazer (escrever
  o mesmo gate em `tools/` e rodar), não é bloqueio de ferramenta.
- Não separei os 120 erros internos do scanner por causa com contagem própria além do que a string mostra:
  **118** são `ast.TypeAlias` (atributo que só existe no Python 3.12+; este sandbox tem 3.11.2) e **2** são
  `ValueError: source code string cannot contain null bytes`. Eles viraram **60 achados
  `skillscan.scanner-error`** — ou seja, o analisador *reportou a própria degradação* em vez de devolver
  "limpo", o que é a qualidade de design mais copiável que vi nesta rodada.
- Não executei `run_eval.py` nem `package_skill.py` da Anthropic, nem o `installer.py` do DeerFlow (454
  linhas de política de instalação, lido só o bastante para citar os limites que ele impõe).
- O `description-length` do perfil `agentskills` (107) não foi cruzado com o limite do Claude Code; só
  registro que os dois perfis divergem em 107 pacotes.

## 10. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 187 `SKILL.md` no corpus; distribuição por repositório | `OBSERVED` | `gh api repos/<r>/git/trees/HEAD?recursive=1` × 13, `truncated: false` em todos |
| 178 materializados com recursos completos; 173 pacotes | `OBSERVED` | `git clone --filter=blob:none` + `git sparse-checkout set --no-cone` com os diretórios de Skill derivados da árvore |
| chaves de frontmatter, `name` ≠ diretório, 2 YAML inválidos, mediana de `description` | `OBSERVED` | script próprio com `yaml.safe_load` sobre os 178 arquivos (saída integral em `/tmp/r25/corpus_final.json`) |
| 177 validações com o gate da Anthropic (97 válidos / 80 inválidos) e 346 análises com o gate do DeerFlow (117 publish / 47 revise / 9 blocked) | `LOCAL_SMOKE_PASS` | `quick_validate.validate_skill` importado por `importlib` + `analyze_skill_package`/`readiness_from_facts` executados neste sandbox, com shim de namespace para não arrastar o runtime |
| matriz de discordância 78/11/5 × 39/36/4 | `OBSERVED` | junção dos dois resultados por diretório (`/tmp/r25/anthropic_validate.json` × `/tmp/r25/final_scan.json`) |
| os 5 `blocked` da Anthropic são `python-env-dump-exfil` + `python-shell-exec` em `scripts/office/soffice.py` | `OBSERVED` | achados do analisador com `path` e mensagem por pacote |
| 2 de 6 casos do `evals.json` reproduzíveis pela camada determinística | `OBSERVED` | comparação direta com `expected_readiness` do manifest |
| 6 sintaxes PEP 695 em `deerflow_extension_api/state.py:32` quebram o import em Python 3.11, com `requires-python = ">=3.12"` declarado | `OBSERVED` | `SyntaxError` capturado + `backend/pyproject.toml:6` |
| `deer-flow` não consegue importar o analisador sem o runtime (o `__init__` de `deerflow.skills` puxa `langchain_core`; o de `config` puxa `dotenv` → `extensions` → `extension-api`) | `OBSERVED` | cadeia de `ModuleNotFoundError` capturada em três execuções sucessivas |
| `topic:skill-creator` = 81 repositórios | `OBSERVED` | `gh api search/repositories?q=topic:skill-creator` (`total_count`) |
| Skills do Hub × os dois gates | `NOT_RUN` | não há `SKILL.md` nesta base; é trabalho nosso, não limitação do ambiente |
