# `obra/superpowers` — 15 Skills, 12 manifests de runtime sincronizados por um arquivo de bump, e uma taxa de rejeição de PR de 94 % declarada no README

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-018` |
| Nome | `obra/superpowers` — "An agentic skill framework for Claude Code, Codex, and friends": conjunto de Skills de processo (brainstorming → plano → TDD → debugging → review → branch) empacotado como plugin para doze superfícies de agente |
| Tipo | repositório (plugin multi-runtime de Skills) |
| Fonte oficial | https://github.com/obra/superpowers · link que o dono mandou: `skills/systematic-debugging/` |
| Responsável | **Jesse Vincent** (`obra`, user `id 64052`; org `prime-radiant` = a empresa dele). Não é projeto de fornecedor de modelo |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | LOCAL_SMOKE_PASS (parcial) — os 15 pacotes passaram pelos dois validadores de `LR-CMP-004` neste sandbox; nenhum hook foi executado |
| Recomendação | **ADAPT** — sugestão ao dono: (i) o `.version-bump.json` como mecanismo de sincronização multi-manifesto; (ii) o `systematic-debugging` como forma de escrever instrução de processo com evidências e contra-exemplo |
| Decisão de adoção | — nenhuma registrada |
| Categoria | conjunto de Skills de processo + empacotamento multi-runtime + governança de contribuição em era de PRs de agente |
| Projetos beneficiados | **Research** (`tools/` e a disciplina anti-deriva desta base), **Lia Agent Hub** (publishing em vários mercados), **Lia Forge** (política de PR de agente) |
| Versão analisada | `main` no HEAD de 2026-11-25 (`pushed_at 2026-11-24T23:59:04Z`) · `RELEASE-NOTES.md` abre em **v7.0.2 (2026-11-03)** · criado 2025-10-09 |
| Proveniência do conteúdo | medido por nós: censo de árvore (308 entradas), leitura de `AGENTS.md` (9.911 B), `README.md` (14.847 B), `.version-bump.json`, `hooks/session-start`, `.github/PULL_REQUEST_TEMPLATE.md`, `RELEASE-NOTES.md`, `skills/using-superpowers/SKILL.md`, `skills/writing-skills/SKILL.md` e `skills/systematic-debugging/*` |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api repos/obra/superpowers` + `repos/…/license` + `git/trees/HEAD?recursive=1` (`truncated: false`) |
| Upstream conferido | **326.586 ★** · 28.979 forks · 372 issues abertas · `language: Shell` · 236 blobs / **1,6 MB de árvore** · 15 `SKILL.md` · 13 `.md` por Skill em média (53 no total) · 20 `.sh` + 2 `.py` · **0 arquivos de licença fora do `LICENSE` da raiz** · **0 workflows em `.github/workflows/`** |
| Próxima revisão | 2026-12-09 |
| Licença | **MIT** — `LICENSE` de 1.070 B na raiz, "Copyright (c) 2025 Jesse Vincent"; API concorda (`spdx_id: MIT`). Correção de premissa desta sessão: o campo não era `null` — ver §7 |
| Confiança | Alta em estrutura, licenças e política (tudo lido); zero em eficácia pedagógica — não rodei o agente com as Skills |

---

## 1. Por que este objeto interessa mais como **engenharia de distribuição** que como conteúdo

Quem vê `superpowers` por fora vê "um monte de prompts bons". O que a árvore mostra é outra coisa: é um
projeto de **uma pessoa** (Shell, 1,6 MB, 15 Skills, zero CI) que mantém **doze empacotamentos** de um mesmo
conteúdo e **uma política de contribuição antifraude** escrita para o agente ler. As duas coisas são o que
falta aqui na Lia.

## 2. O problema dos doze espelhos, e a solução de 20 linhas

`superpowers` mantém, no mesmo repositório:

```
.antigravity-plugin/  .claude-plugin/  .codex-plugin/  .cursor-plugin/  .devin-plugin/
.hermes-plugin/       .kimi-plugin/    .muse-plugin/   .opencode/       .pi/
.agents/plugins/marketplace.json       gemini-extension.json
```

Onze formatos de manifesto para onze hosts. Em vez de script de sincronização com `git status` (o modelo do
open-seo, `LR-FORGE-017`) ou de symlink (o `cal.diy`, `LR-FORGE-019`), eles têm **`.version-bump.json`** —
um arquivo de dados que declara o acoplamento:

```
"files": [ { "path": "package.json", "field": "version" },
           { "path": ".hermes-plugin/plugin.yaml", "field": "version" },
           { "path": ".claude-plugin/marketplace.json", "field": "plugins.0.version" }, … 11 entradas ]
"audit": { "exclude": [ "CHANGELOG.md", … ] }
```

Cada entrada é `path` + `field` (inclusive caminho dentro de JSON: `plugins.0.version`), e há uma lista de
`audit.exclude`. Resultado: **a fonte da verdade sobre "o que precisa mudar junto" é um arquivo versionado no
próprio repositório** — e não uma convenção na cabeça do mantenedor. É o formato exato que a nossa `DR-0021`
(busca de Skills órfãs) e o `SKILL-LICENSE-CONSOLIDATION.md` §4.1 precisam para "arquivos por superfície".

## 3. Zero CI, e uma política de PR que substitui o CI

Medido: **nenhum arquivo em `.github/workflows/`** num repositório de 326.586 estrelas. Em vez de
verificação automatizada, `.github/PULL_REQUEST_TEMPLATE.md` + `AGENTS.md` carregam a disciplina, com números
e frases que o próprio autor escreveu:

| Item | O que está escrito (traduzido) |
|---|---|
| Rejeição | *"This repo has a 94 % PR rejection rate. Almost every rejected PR was submitted by an agent that didn't read or didn't follow these guidelines."* |
| Endurecimento | PRs com seções em branco, múltiplas mudanças não relacionadas, **ou sem evidência de envolvimento humano** são fechadas sem revisão |
| Ramo alvo | *"MUST target the `dev` branch, not `main`"* — `main` é o ramo liberado |
| Anti-caçador-de-issue | *"This project does not accept agent-written PRs that fix issues filed by someone else… you are wasting your tokens: the PR will be closed. Add your report to that issue instead."* |
| Seção obrigatória | *"Who is submitting this PR? (required)"* — qual agente, onde rodou, o que o humano pediu; *"We weigh contributions by what produced them: content reasoned from documentation is held to a different bar than work grounded in a real session."* |

A última linha é a que vale para esta base: eles **ponderam a evidência pela procedência** (documentação ×
sessão real). Nosso formato de rótulos (`OBSERVED` / `DOCUMENTED` / `LOCAL_*` / `BLOCKED` / `NOT_RUN`) faz a
mesma separação por tipo de medição; a diferença é que eles pesam, nós só rotulamos. Vale registrar a pergunta
para o dono do Forge: um `AGENTS.md` de projeto Lia deveria dizer ao agente o que **não** fazer (PR não
solicitada) com a mesma crudeza?

## 4. `systematic-debugging`, o arquivo que o dono apontou

`skills/systematic-debugging/` = **5 arquivos**: `SKILL.md` de **9.530 B**, `root-cause-tracing.md`,
`condition-based-waiting.md`, `condition-based-waiting-example.ts` e `find-polluter.sh`. O frontmatter tem só
`name` + `description` (sem `version`, sem `license`, sem `allowed-tools`) e o corpo abre com:

> *Use when encountering any bug, test failure, or unexpected behavior, **before proposing fixes***
> **Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.
> **Violating the letter of this process is violating the spirit of debugging.**

O formato que importa para nós: a Skill **declara o momento de disparo como restrição de sequenciamento**
("antes de propor correções"), e não como descrição de capacidade. É a mesma estrutura das nossas regras de
rótulo ("a instrução que um agente segue vem junto da medição que a justifica") e da regra das 5 fontes do
`AGENTS.md` deles: *find* → *prove* → *fix*.

## 5. A Skill que invoca as outras: `using-superpowers`

Abre com blocos delimitados (`<SUBAGENT-STOP>`, `<EXTREMELY-IMPORTANT>`) e a regra: *"If you think there is
even a 1 % chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill… This is not
negotiable. You cannot rationalize your way out of this."* Duas leituras possíveis, e registro as duas:

- **a favor**: é o mecanismo de disparo que falta ao nosso conjunto de Skills — nós registramos 48 Skills
  sem nenhuma regra de "quando és obrigado a usar";
- **contra**: é instrução de compliance endereçada à racionalização do modelo, escrita como proibição moral.
  Não há medida de eficácia no repositório; e `hooks/session-start` + o manifesto de plugin são o que fazem o
  texto chegar à sessão, não a ênfase.

A parte copiável sem discussão é a segunda: **a Skill precisa de um gancho de sessão**, e eles têm
`hooks/hooks.json`, `hooks/hooks-cursor.json`, `hooks/run-hook.cmd`, `hooks/session-start` — um gancho por
host, com o mesmo conteúdo.

## 6. Um gancho de 30 linhas que carrega a engenharia toda

`hooks/session-start` (bash, `set -euo pipefail`) tem dois comentários que valem mais que muitos frameworks:

- *"Determine plugin root directory. Splits `$0` … **This avoids `dirname`** because a `SessionStart:startup`
  hook can run with a broken/empty PATH (`anthropics/claude-code#43127`) before any PATH-repairing sibling
  hook in the same startup batch takes effect."* — a decisão de código ligada a um bug upstream **numerado**;
- *"No command substitution or pipe runs in this script: each one forks, and a fork costs tens of
  milliseconds under Git Bash on Windows."* — restrição de desempenho do host explicitada no script.

É o nosso critério de "anotar a razão, não só o fato", aplicado a um hook de plugin. (Nota: o comentário diz
"two lines"; o arquivo tem mais — não medi linha a linha.)

## 7. Correções de premissa desta sessão, feitas em lugar

Durante a medição desta rodada descobri que **duas notas que eu tinha em rascunho estavam erradas** sobre
este repositório, e corrijo aqui, não em segredo:

1. ~~"o campo `license` da API é `null`; nenhum `LICENSE` fora da raiz"~~ → a API devolve
   **`spdx_id: MIT`** com `LICENSE` de **1.070 B** na raiz. O que a medição confirma é o outro lado:
   **15 `SKILL.md` sem licença por Skill e 0 `NOTICE`** — um pacote MIT de uma peça só, exatamente o formato
   que o `SPLIT-LICENSE-SCAN.md` chama de simples e que o Hub não pode assumir para conteúdo de terceiros;
2. ~~"`systematic-debugging/SKILL.md` tem 42.969 B"~~ → tem **9.530 B** (42.969 B é o `doc-coauthoring` do
   `anthropics/skills`, medido por mim no censo dos 178). O erro vinha de anotação de censo não reconfirmada.
   **Retificação da retificação (2026-11-26):** a atribuição entre parênteses também estava errada. Medido
   hoje, `skills/doc-coauthoring/SKILL.md` tem **15.815 B**, e **nenhum blob** de `anthropics/skills` na `HEAD`
   atual tem 42.969 B — `gh api "repos/anthropics/skills/git/trees/HEAD?recursive=1"` filtrando `.size==42969`
   devolve **0 linhas** (o maior `.md` do repositório é `skills/claude-api/shared/model-migration.md`, 346.255 B).
   Ou seja: o número 42.969 não pertencia a nenhum arquivo que saibamos reidentificar, e a explicação "era o
   `doc-coauthoring`" é retirada. O que sobrevive é só a primeira correção: 9.530 B.

As duas correções mudam a recomendação: o `superpowers` não é "licença ausente" (é MIT claro), e as Skills
deles não são longas (são 4× menores que a média do corpus: 9.530 B contra 7.843 B de mediana do total de
187 — a comparação real é que **o texto deles é curto e o dos fornecedores é longo**).

## 8. Como o pacote deles se comporta nos dois gates (§4 do `LR-CMP-004`)

Foi o corpus **mais limpo dos dez**: 13 dos 14 pacotes que entraram na varredura (de 15 `SKILL.md`), com 1 `revise` e **0 `blocked`** no
analisador do DeerFlow; e nenhum dos 15 foi rejeitado por chaves desconhecidas (só `name` + `description`).
Comparação direta: `anthropics/skills` tem 5 pacotes `blocked` pelo scanner de código, `dyad` tem 1 de 23
prontos. O que explica? O `superpowers` distribui **texto e um shell script de procedimento** — quase nada de
código executável por Skill. É a evidência quantitativa de uma hipótese que estava no nosso
`SKILL-LICENSE-CONSOLIDATION.md`: *Skill com script embutido multiplica a auditoria; Skill de processo não*.

## 9. O que não verifiquei, e por quê

- **não instalei nem executei** o plugin em nenhum dos doze hosts: não há Claude Code, Codex nem Cursor aqui,
  e instalar um plugin de terceiros nesses runtimes é fora de escopo por política desta base;
- o gancho `session-start` não foi executado (não tem harness de hook neste sandbox);
- a **taxa de 94 %** é afirmação do `AGENTS.md`, não medição minha — não contei PRs fechadas vs. aceitas
  (dá para contar via API; fica como fila se o dono quiser o número real);
- não li as outras 13 Skills uma por uma; o censo (15 pacotes, 53 `.md`, tamanhos) é por árvore;
- a lista de releases da API **não foi reconfirmada nesta rodada**; citei o topo do `RELEASE-NOTES.md`
  (v7.0.2, 2026-11-03), que é o que está no repositório — e não confunda com `v6.0.3`, número que circula em
  anotações antigas desta sessão e que não verifiquei;
- a eficácia pedagógica (as Skills melhoram o resultado do agente?) não tem medição deles nem minha. É a
  pergunta que a `LR-CMP-004` §6 mostra que nenhum dos dois gates responde.

## 10. Recomendação: **ADAPT** (duas peças)

**Adaptar:** (1) um arquivo `.version-bump.json`-like na nossa base — uma tabela declarativa de
"caminho + campo que precisam mudar juntos" para o `agents/SKILLS-OPERATING-SET.md` e os registros de plugin
do Hub, em vez de confiar na memória do revisor (isto é texto de política, não código, e resolve metade da
`DR-0021`); (2) o `AGENTS.md`-de-terceiro como modelo de política escrita *para o agente ler*, com a seção
"quem está submetendo este PR" (a nossa base já faz isso no formulário do `PUBLISHING-PROTOCOL.md`; o deles
tem dente: "PR sem essa seção é fechada").

**Não adaptar:** o `<EXTREMELY-IMPORTANT>` de compliance — é estilo retórico que não verificamos funcionar, e
a nossa casa documenta decisão em tabela, não em ênfase.

**Propor** ao dono, sem aplicar nada: (i) levar o padrão de manifesto de bump para o Hub como resposta a
"um Skill, N hosts"; (ii) testar a forma de "quem submeteu este PR" no `PUBLISHING-PROTOCOL.md` desta base.

## 11. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 326.586 ★ · 28.979 forks · 372 issues · `language: Shell` · MIT · criado 2025-10-09 | `OBSERVED` | `gh api repos/obra/superpowers` |
| `LICENSE` na raiz: MIT, 1.070 B, "Copyright (c) 2025 Jesse Vincent"; API `spdx_id: MIT` | `OBSERVED` | `gh api repos/obra/superpowers/license` + `git show HEAD:LICENSE` no clone com filtro de blob |
| 308 entradas / 236 blobs / 1,6 MB; 15 `SKILL.md`; 0 `LICENSE` aninhados; **0 workflows**; 20 `.sh` + 2 `.py`; 53 `.md` em `skills/` | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio |
| doze superfícies empacotadas (`.antigravity-plugin` … `gemini-extension.json`) | `OBSERVED` | lista de caminhos de primeiro nível da árvore |
| `.version-bump.json` com 11 pares `path`/`field` e `audit.exclude` | `OBSERVED` | arquivo lido no HEAD via `git show` |
| política de PR: 94 % de rejeição, alvo `dev`, "does not accept agent-written PRs that fix issues filed by someone else", seção obrigatória "Who is submitting this PR?" | `OBSERVED` (texto) | `.github/PULL_REQUEST_TEMPLATE.md` + `AGENTS.md` lidos |
| `hooks/session-start` com workaround de PATH vazio citado a issue `anthropics/claude-code#43127` e nota de custo de `fork` no Git Bash | `OBSERVED` (código + comentário) | `git show HEAD:hooks/session-start` |
| `systematic-debugging/SKILL.md` = 9.530 B com 4 arquivos irmãos (`root-cause-tracing.md`, `condition-based-waiting.md`, `…-example.ts`, `find-polluter.sh`) | `OBSERVED` | `wc -c` + `ls` no diretório materializado |
| `using-superpowers` exige invocação antes de "qualquer resposta, inclusive perguntas de esclarecimento" | `OBSERVED` (texto) | `head -22 skills/using-superpowers/SKILL.md` |
| 13/14 `publish_candidate`, 1 `revise`, 0 `blocked`; nenhuma rejeição do validador da Anthropic | `LOCAL_SMOKE_PASS` (parcial) | os dois gates executados neste sandbox, tabela completa em `comparisons/SKILL-GATE-COMPARISON.md` §4 |
| a taxa de rejeição de 94 % | `DOCUMENTED` (alegação do autor, não contada) | `AGENTS.md`; contagem de PRs fechadas não foi feita |
| as Skills melhoram a taxa de sucesso do agente | `NOT_RUN` | exigiria rodar os runtimes com modelo real; nenhum foi chamado |
