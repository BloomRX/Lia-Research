# Declaração de envolvimento de IA: o gate do OpenProject, comparado com os outros sete, e o que a Lia pode fazer com isso

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-014` |
| Categoria | agents |
| Objetos cobertos | `opf/openproject` (gate completo), `capsoftware/cap` (AGENTS.md de 125 linhas), `calcom/cal.diy` (layout `agents/` + symlinks), `debpalash/VoiceStudio` (`.gitleaks` + `commit-identity` + CLA), `chatwoot/chatwoot` (AGENTS.md + labeler), `every-app/open-seo` (28 Skills + teste de deriva), `AppFlowy-IO/appflowy-ai-plugins` (regras de escrita em `SKILL.md`), `OpenWhispr/openwhispr` (`CLAUDE.md`) |
| Projetos beneficiados | todos os cinco; e o processo desta casa (`RESEARCH-CHANGELOG.md`, `governance/INVESTIGATION-PROTOCOL.md`, `agents/`) |
| Fontes | arquivos lidos na árvore de cada repositório via `gh api` em 2026-11-24 (workflow, script de 129 linhas, `pull_request_template.md`, `AGENTS.md`, `CLAUDE.md`); nenhum depoimento de terceiros |
| Estado | DOCUMENTED — nenhum item implementado |
| Recomendação | **ADAPT** (proposta de formato; decisão é do dono) |
| Decisão de adoção | — nenhuma registrada |
| Data | 2026-11-24 |
| Status | CURRENT |
| Confiança | Alta: cada frase transcrita foi lida no arquivo; nenhuma inferência sobre o efeito do gate em PRs reais |

---

## 1. A pergunta que este documento responde

Nenhuma das oito coisas que o dono mandou nesta leva é sobre IA no título — e ainda assim **sete dos oito
têm instruções para agentes versionadas no repositório**, e um deles tem um gate de CI que obriga o autor
do PR a declarar *quanto do trabalho foi do modelo*. Isso responde a uma pergunta que a casa vem
adiando: a declaração de autoria por IA é folklore de comunidade ou já é engenharia de processo?

Resposta medida: no fim de 2026, em software livre de porte industrial, o padrão é **três camadas** — (a)
instruções de escrita por repositório, (b) verificação automática do que as instruções dizem, (c)
declaração do autor cobrada antes do merge. O OpenProject implementa as três; Cap e open-seo implementam
(a)+(b); a maioria implementa só (a).

## 2. A camada (c): o gate do OpenProject, desmontado

### 2.1 O que o autor vê

Na seção "AI involvement" do `.github/pull_request_template.md` (transcrita em `LR-FORGE-016` §4): quatro
níveis, todos **dentro de comentários HTML**, e a instrução "Uncomment the one line below that fits". As
definições são de autoavaliação de *compreensão*, não de volume de código:

| Nível | O que o autor afirma (texto deles) |
|---|---|
| `None/Assisted` | "No AI assistance used OR only autocomplete/pasted snippets. I effectively wrote and understand all the code." |
| `Collaborative` | "AI generated a substantial part of the code; **I reviewed and understand every line**." |
| `Directed` | "I specified the requirements and AI implemented most of it; I validated via testing rather than a full line-by-line review." |
| `Autonomous` | "AI worked with little supervision; I mainly smoke-tested the result or no human was involved at all." |

Repare na régua: o que separa `Collaborative` de `Directed` não é quanto a IA escreveu, é **se o humano
linha a linha ou só por teste**. É a única escala dos quatro que um revisor consegue auditar de fora, e é
por isso que ela funciona.

### 2.2 O que a máquina faz com isso

`script/ci/ai_involvement_check.sh`, 129 linhas, lidas na íntegra:

- `LEVELS='None/Assisted|None|Assisted|Collaborative|Directed|Autonomous'` — cinco tokens aceitos, sendo
  dois sinônimos normalizados: `sed -E 's#^(None|Assisted)$#None/Assisted#'`;
- `strip_html_comments()` implementado em **awk com estado**, com o motivo escrito: "Comments can span
  multiple lines, so they cannot be stripped line by line";
- recorte da seção pelo cabeçalho: `sed -n '/^#{1,6}[[:space:]]*AI involvement/,/^#{1,6}[[:space:]]/p'`;
- para aceitar explicação depois do nível ("Collaborative – AI generated …"), corta em `–|—|-|:` e
  exige que a parte restante **seja só níveis**: `grep -E "^([[:space:]/,]*(\$LEVELS))+[[:space:]/,]*$"` —
  com o comentário explicando o porquê: "so that several levels on one line ('Collaborative / Directed')
  are rejected while an explanation that happens to mention another level is not. That part must consist
  of levels alone, as prose can start with a level word too ('None of this was AI-written')";
- quatro saídas possíveis, cada uma com `::error::` **e** `status=` no `$GITHUB_OUTPUT`: `section_missing`,
  `level_missing`, `multiple_levels`, `ok` + `level=`;
- **`exit 0` em todos os ramos**, com a justificativa na workflow: "A failure here must not skip the
  comment below, nor turn the check red on pull requests it is not enforced on."

E a workflow, `ai-involvement-check.yml`: `pull_request_target` com **justificativa de segurança escrita
no próprio arquivo** — "Nothing from the pull request is ever checked out or executed: the checkout below
takes the base branch, and the description is passed from the event payload via an environment variable" —
`permissions: contents: read` + `pull-requests: write`, `persist-credentials: false`, sparse-checkout de
um único script, `concurrency` por número de PR, e `# zizmor: ignore[dangerous-triggers]` dentro de um repo
que tem `zizmor.yml`. O resultado vira **rótulo** (`ai:*`) sincronizado com `continue-on-error: true`.

Nada disso é um detector. É um **registro com formato** — e o desenho inteiro consiste em não mentir sobre
isso, o que se vê no `exit 0` e no "not enforced on".

### 2.3 As três objeções que já antecipo

1. **auto-declaração é barata de satisfazer mal**: ninguém é pego mentindo; o que o gate garante é que a
   pergunta foi feita e que existe distribuição de níveis para olhar depois;
2. **`pull_request_target` é a escolha errada para qualquer projeto sem o cuidado do §2.2** (checkout da
   base, `persist-credentials: false`, payload só por env var). Se a Lia copiar o gate sem copiar as
   defesas, copia um vetor. Não recomendo `pull_request_target` para nós por princípio — §5;
3. **a escala é de revisão, não de risco**: `Autonomous` com um teste bom é menos arriscado que
   `Collaborative` sem teste nenhum; o nível sozinho não deveria virar política de merge sem uma segunda
   evidência (aqui é exatamente o nosso `Resultado de execução`, §5).

## 3. A camada (a): o que cada um dos oito versiona como instrução

| Objeto | Arquivos medidos na raiz | O que a instrução faz de diferente |
|---|---|---|
| `opf/openproject` | `AGENTS.md` (+ convite a `AGENTS.local.md`/`CLAUDE.local.md` ignorados), `copilot-instructions.md`, `ai-involvement-check.yml` | dimensiona o repo para o agente ("monorepo ~840 MB, >1 M LOC") e **separa o que é local do que é versionado** |
| `capsoftware/cap` | `AGENTS.md` (125 linhas, 15 seções), `CLAUDE.md`, `.agents/`, `.claude/` | invariantes **antes** da geração, checagens pós-edição por tipo de arquivo, ratchet "contagem só desce", "call out what is verified vs merely plausible" |
| `calcom/cal.diy` | `AGENTS.md`, `CLAUDE.md`, `.claude/{rules,skills,settings.json}`, `.cursor/{rules,skills}`, `.opencode/skill/`, `agents/`, `SPEC-WORKFLOW.md`, `specs/_templates/` | **uma fonte (`agents/`) e vistas por ferramenta via symlink**; estilo codificado em regras de 1 arquivo (`select` > `include`, `import type`, early return, `ErrorWithCode`); spec-driven **opt-in** |
| `every-app/open-seo` | `AGENTS.md`, `.claude/`, `.cursor/`, `.agents/skills` (28), `plugins/openseo/{.claude,.codex,.cursor}-plugin/` | Skills como artefato de produto com **teste de deriva na CI**; 12 públicas de 28 por lista explícita no script |
| `chatwoot/chatwoot` | `AGENTS.md` | instrução mínima; o peso do processo está em `.qlty/`, `.bundler-audit.yml`, `.dependabot/` e nos gates de política (§2 de `LR-SEC-009`) |
| `debpalash/VoiceStudio` | `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, `.coderabbit.yaml`, `commit-identity.yml`, `cla*.yml` | a instrução é **secundária frente à verificação**: 19 arquivos de teste só para pins, gitleaks com allowlist visível, CLA com lembrete e backfill |
| `OpenWhispr/openwhispr` | `CLAUDE.md`, `agent-skills/` (2 `SKILL.md`), `.oss-scanner/threat_model.md` | o agente é instruído a **operar o produto** via API/CLI; a Skill de terceiros vendida com `license:` no frontmatter é o caso do cal.diy, não daqui |
| `AppFlowy-IO/*` (27) | nenhum `AGENTS.md` medido na raiz dos 16 varridos; `appflowy-ai-plugins` tem `SKILL.md` com regras de escrita | o AppFlowy instrui o **modelo que usa as ferramentas**, não o **engenharia que escreve o AppFlowy** — as regras de "confirm", "read back", "don't retry in a loop" estão em `LR-MCP-004` |

Dois fatos agregados da varredura de 16 repositórios (flag `docs` do meu censo): `AGENTS.md` presente em
`opf/openproject`, `opf/opilot` (só `CLAUDE.md`), `capsoftware/cap`, `chatwoot/chatwoot`,
`every-app/open-seo`, `debpalash/VoiceStudio`, `calcom/cal.diy` — 6 dos 8 alvos com `AGENTS.md` na raiz,
7 dos 8 com pelo menos um arquivo de instrução a agente. O único dos oito que não tem é o AppFlowy como
produto.

## 4. A camada (b): verificação — o que cada um automatiza

| Mecanismo | Quem tem | Como falha o autor |
|---|---|---|
| `scripts/test-lint` com `@interfere/landmines` + allowlists congeladas por arquivo (`oxlintrc.json` 8.076 B, `test-doubles-allow.json` 2.201 B com **33 arquivos / 324 exceções**) | `capsoftware/cap` | erro de lint no teste; subir uma contagem é proibido por regra escrita |
| `pnpm ci:check` incluindo `pnpm sync-plugin-skills && test -z "$(git status --porcelain -- plugins/openseo/skills)"` | `every-app/open-seo` | CI falha se a cópia publicada divergiu do original |
| `zizmor.yml` + `actionlint.yaml` + `actions.lock` + `cla.yml` | `opf/openproject` | workflow insegura/má-formada; contribuição sem CLA |
| `tests/test_workflow_action_pins.py` (303 linhas) + `test_actions_pinned.py` + job semanal `action-pin-verify.yml` | `debpalash/VoiceStudio` | teste Python falha fora da CI; o job semanal resolve o que o teste não pode (SHA ≠ rótulo) |
| `scripts/check.py` + `scripts/annotation-table.py` determinístico | `appflowy-ai-plugins` | `note:`/`ok` com exit code; tabela gerada precisa bater |
| `ai-involvement-check.yml` | `opf/openproject` | `::error::` anotado no log + rótulo errado no PR; **nunca** exit ≠ 0 |
| `SECURITY.md` + `.well-known/security.txt` + `security-audit.yml` + `check-prisma-migrations.yml` + `i18n.yml` | `calcom/cal.diy` | gate específico por classe de deriva (schema, i18n não usado, dependência) |

A regularidade que se pode afirmar daqui: **nenhum dos sete automatiza a declaração de autoria**; todos os
que têm peso automatizam *a forma* (metadado, espelho, pin, lint, ameaça). Isso importa para a Lia porque
é o contrário do medo comum ("vamos ter de vigiar se o agente fez o código"): o que se verifica
automaticamente é o artefato, e a autoria fica como declaração com formato.

## 5. O que isto significa para o processo desta casa (proposta, não decisão)
> **Escopo desta seção** — o que segue é recomendação técnica desta base, não instrução para nenhum app. Se vale, cabe e é possível implementar em cada projeto é decisão do dono (`MISSION.md` §3: o Research não aprova nada).


A casa já tem três das quatro peças que o gate deles pressupõe:

| Peça deles | Equivalente nosso | Estado |
|---|---|---|
| seção no template de PR | campo `Resultado de execução` + rótulos `CONFIRMED`/`OBSERVED`/`REPORTED`/`UNVALIDATED` na tabela final | **existe** (`tools/validate.py` checa o vocabulário e exige linha no test-log para `LOCAL_*`) |
| o nível ser auditável por fora | `governance/TESTING-PROTOCOL.md` níveis 1/2/3 | **existe** |
| rótulo automático | `catalog/catalog.tsv` gerado por `tools/build_catalog.py` + `check_catalog_sync` | **existe, para objeto, não para método** |
| **declaração de quanto do texto foi gerado por modelo** | — | **não existe** |

Proposta concreta, na forma mínima (quatro linhas, sem CI nova, sem `pull_request_target`, sem rótulo):

um campo opcional no cabeçalho de cada relatório, `| Envolvimento de IA | … |`, com as quatro
palavras deles traduzidas — `Nenhum/Suportado`, `Colaborativo`, `Dirigido`, `Autônomo` — e a **mesma**
semântica de "só pode haver um". Por quê, se ninguém mente? Porque a régua deles é sobre *compreensão do
revisor*, e o que a Research vende para o dono é justamente compreensão: um relatório `Autônomo` tem de
carregar mais linhas em "o que não verifiquei" do que um `Nenhum/Suportado`, e hoje isso é
invisível. Também não viola a linha da casa ("pesquisa = fato") — é metadado sobre o método, não opinião.

Por que **não** recomendo a workflow: a Lia Research não tem PRs nem branch protection; o gate de CI deles
existe para *forçar o preenchimento* entre colaboradores anônimos. Aqui quem cobra é o dono, e o
`tools/validate.py` poderia, no futuro, exigir o campo (é a mesma forma do `REPORT_FIELDS` atual). Registro
a opção e deixo a escolha.

## 6. O que eu **não** recomendo copiar

1. `pull_request_target` para um gate de texto (a justificativa deles é boa, mas há alternativa: rodar no
   `pull_request` com `script` vindo da base e corpo lido pela API — não medi se isso é viável para o
   caso deles, e não vou recomendar o que não verifiquei);
2. rótulo automático como sinal de qualidade — eles mesmos usam rótulo, não checagem vermelha;
3. escala de autoria no lugar de evidência de execução: na nossa base, `AUTÔNOMO` sem linha no
   `data/testing/test-log.tsv` é exatamente o que já rejeitamos no `LR-STUDIO-012` §13;
4. copiar a **frase** de maturidade do pack deles sem o resto: o WARNING do `openproject-agent-skills`
   vem acompanhado de `validation/baseline.md` com falhas registradas. Declaração sem corpus de falhas é
   marketing (`agents/SKILLS-OPERATING-SET.md` §regras de casa trata disso).

## 7. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| Os 4 níveis comentados no template, com as definições transcritas | `CONFIRMED` | `.github/pull_request_template.md` do `opf/openproject`, decodificado |
| Script de 129 linhas: `strip_html_comments` em awk, `LEVELS` com 5 tokens, normalização de None/Assisted, rejeição de múltiplos níveis, 4 estados de saída, `exit 0` sempre | `CONFIRMED` | `script/ci/ai_involvement_check.sh` lido por inteiro (trechos §2.2) |
| Workflow com justificativa escrita, `permissions: contents: read` + `pull-requests: write`, `persist-credentials: false`, sparse-checkout único, `zizmor: ignore[dangerous-triggers]`, rótulo com `continue-on-error` | `CONFIRMED` | `.github/workflows/ai-involvement-check.yml` |
| `AGENTS.md` presente em 6 dos 8 alvos; `CLAUDE.md` em 5; nenhum no `AppFlowy` | `CONFIRMED` | censo de flags de documento sobre 16 repositórios (`docs` da varredura) + listagens de raiz |
| Cap: 15 seções no `AGENTS.md` de 125 linhas, incluindo "Pre-Generation Invariants" e o ratchet com 33 arquivos / 324 exceções congeladas | `CONFIRMED` | `AGENTS.md` lido + os dois JSONs abertos via API |
| cal.diy: `agents/{rules,skills}` como fonte e `.claude`/`.cursor` como symlinks para os mesmos blobs (`e01395`, `a769d4`) | `CONFIRMED` | `contents/.claude`, `contents/.cursor`, `contents/agents` |
| open-seo: `ci:check` com teste de deriva do espelho de Skills; 28 Skills, 12 espelhadas, 15 com `metadata.internal` | `CONFIRMED` | `LR-FORGE-017` §4, medido no clone |
| VoiceStudio: 19 de 931 arquivos de teste com "pin" no nome; 262/262 ações em SHA-40; job semanal para o que o teste não prova | `CONFIRMED` | censo próprio + `LR-VOICE-003` §4–§5 |
| AppFlowy-Cloud README afirma que o self-host AGPL não é mais construído ali | `CONFIRMED` (texto) / `REPORTED` (consequência) | `LR-FORGE-015` §4 |
| Que o gate **reduz** contribuição de IA não declarada | `UNVALIDATED` | nenhum dado de distribuição de rótulos foi medido |
| Que qualquer um desses arquivos melhora a qualidade do código | `UNVALIDATED` | fora do que esta leva sustenta |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 3) · dois dossiês com os dados brutos:
`repositories/opf-openproject/REPORT.md` e `repositories/open-seo/REPORT.md` · protocolo desta casa sobre
método: `governance/INVESTIGATION-PROTOCOL.md` · vocabulário de execução:
`governance/TESTING-PROTOCOL.md` · inventário de Skills da casa: `agents/SKILLS-OPERATING-SET.md` ·
publicação: `agents/PUBLISHING-PROTOCOL.md`.
