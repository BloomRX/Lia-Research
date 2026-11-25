# pipecat — framework de voz em tempo real que mantém 12 Skills de manutenção interna, com um scanner de licenças no CI

| Campo | Valor |
|---|---|
| ID | `LR-VOICE-005` |
| Nome | `pipecat-ai/pipecat` — "Open source framework for building voice agents and real-time multimodal conversational AI" |
| Tipo | repositório (framework Python) |
| Fonte oficial | https://github.com/pipecat-ai/pipecat · https://www.pipecat.ai |
| Responsável | org `pipecat-ai`; contribuidor nº 1 `markbackman` (4.972 contribuições) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN (nada instalado; nenhum script executado) |
| Recomendação | **ADAPT** — sugestão ao dono: as três práticas de higiene abaixo (Skills de manutenção, `LICENSE-shadcn.md` por componente vendorizado, `license-check.yaml` no CI) |
| Decisão de adoção | — nenhuma registrada |
| Categoria | framework de voz + práticas de manutenção com agentes |
| Projetos beneficiados | **Research** (a regra de licença por arquivo vendorizado resolve metade do nosso formato `G` do `SPLIT-LICENSE-SCAN.md`), Lia Forge (`scripts/reports`), **Lia Studio** (só como referência de formato de pacote de Skills internas) |
| Versão analisada | `main` no HEAD de 2026-11-25 (`pushed_at 2026-11-25T23:07:00Z`, o mesmo minuto da coleta) |
| Proveniência do conteúdo | medido por nós: censo de árvore, leitura de `AGENTS.md` (257 linhas), do `CLAUDE.md`, dos 12 `SKILL.md` (tamanhos) e do `provider-research/SKILL.md` (8.160 B) por inteiro |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api` + `git/trees/HEAD?recursive=1` (`truncated: false`) |
| Upstream conferido | **17.439 ★** · 3.185 forks · 587 issues abertas · Python · 2.616 entradas / 2.256 blobs / **53,0 MB** · 1.781 `.py` · **68 `.md`** · 12 `SKILL.md` · **12 workflows** (1 deles `license-check.yaml`) · **3 caminhos `LICENSE`** |
| Próxima revisão | 2026-12-09 |
| Licença | **BSD-2-Clause** na raiz (`LICENSE`); mais um `LICENSE-shadcn.md` dentro de `src/pipecat/cli/templates/client/_pipecat_ui/src/components/ui/` — ou seja, **a licença do componente de terceiro vendorizado no template do CLI mora ao lado do componente**, não no `README` |
| Confiança | Alta no que foi lido; **zero** quanto ao comportamento de voz/tempo real, que não tem como ser medido aqui |

---

## 1. Por que um framework de voz entrou nesta leva

O dono mandou o link sem briefing. Duas razões apareceram na medição, e nenhuma delas é "voz":
(i) o projeto mantém **12 Skills dentro de `.claude/skills/`, todas de manutenção de repositório** — é o
melhor exemplo medido de "Skills como infraestrutura interna", que é o que a `DR-0020`/`SKILL-WORKFLOW-MANIFEST`
desta base discute; (ii) tem um **workflow de verificação de licença no CI** e uma licença de componente
arquivada ao lado do componente — prática que resolve um caso concreto do nosso
`SPLIT-LICENSE-SCAN.md` (formato `G`/`H`).

## 2. O inventário das 12 Skills, medido

| Skill | bytes | o que é |
|---|---|---|
| `update-docs` | **19.096** | manter a documentação coerente com o código |
| `update-rtvi` | 11.501 | atualizar o protocolo RTVI |
| `pr-description` | 8.326 | escrever a descrição do PR |
| `provider-research` | 8.160 | varredura de modelos por fornecedor (§3) |
| `cleanup` | 7.911 | limpeza de branches/estado |
| `docstring` | 7.782 | docstrings |
| `code-review` | 6.942 | revisão de PR |
| `prose-review` | 4.566 | revisão de prosa |
| `provider-research-digest` | 3.367 | consolidar os relatórios da varredura |
| `changelog` | 3.137 | fragmentos de changelog (towncrier) |
| `squash-commits` | 2.730 | esmagar commits |
| `pr-submit` | **1.381** | submeter o PR |

Total **84.899 B** de instruções para 12 operações de manutenção. Nenhuma é "capacidade de produto": todas
são **processo de engenharia** (PR, changelog, docs, limpeza). O par `pr-description` (8.326 B) ×
`pr-submit` (1.381 B) é a forma mais explícita disso: eles separaram *escrever* de *publicar*, e deram ao
passo de publicar **um sexto** do texto — o de risco irreversível é o mais enxuto e o mais vinculado a um
comando. Nada no nosso `agents/SKILLS-OPERATING-SET.md` (48 entradas) tem essa separação documentada.

## 3. A Skill de varredura de fornecedores (o desenho que mais vale)

`provider-research/SKILL.md` (8.160 B) declara no frontmatter `disable-model-invocation: true` +
`argument-hint: "[--only a,b] [--date YYYY-MM-DD] [--limit N] [--concurrency N]"` — **não é invocável pelo
modelo por iniciativa própria**, só pelo humano com argumentos. O corpo:

- orquestra **um subagente por unidade de pesquisa** (`provider-watch-researcher`), definido **duas vezes**
  — `.claude/agents/provider-watch-researcher.md` e `.codex/agents/provider-watch-researcher.toml` — e fecha
  com "in an agent without subagents, do the researcher's work yourself … the agent definitions are thin
  shims over that guide": **a definição de subagente é xerox; o guia (`RESEARCH_GUIDE.md`) é a fonte**;
- **recusa agir sem pré-requisito**: "Stop with a clear error if `uv run python scripts/provider-watch/inventory.py --md` fails";
- **fora do repositório**: o diretório de trabalho é `mktemp -d -t provider-research` ("Everything transient —
  payloads, `run.jsonl`, worktrees — lives there"), e os relatórios vão para um repositório separado
  (`pipecat-ai/provider-watch-reports`) clonado em `_reports`, **gitignorado**; se o clone falhar, `git init`
  e segue "with no history";
- **memória = issue**: as decisões do time são comments nas issues de digest, coletadas para
  `digest-comments.md` com `gh issue list --search "Provider watch in:title sort:created-desc"`; se o repo ou
  `gh` falharem, "write an empty file" e continua;
- **idempotência declarada**: "separate runs over disjoint `--only` slices with the same date compose into
  one sweep"; e `--limit N` "For test runs".

As três primeiras são as que valem para esta base (nós usamos `/tmp/rNN` exatamente assim). A quarta —
**usar issue como banco de decisões de pesquisa** — é o espelho exato do `decisions/PENDING` desta casa, só
que público e pesquisável por `gh`. Vale perguntar ao dono: as DRs desta base ganham algo se forem espelhadas
em issues no repositório (busca, comentário, histórico) — ou o `decisions/` é melhor justamente por ser
revisável em diff?

## 4. Higiene de licença: dois mecanismos copiáveis

| Mecanismo | Medida | Por que nos interessa |
|---|---|---|
| `LICENSE-shadcn.md` dentro de `src/pipecat/cli/templates/client/_pipecat_ui/src/components/ui/` | caminho lido na árvore (1 arquivo por componente vendorizado, no diretório do componente) | é o formato `H` do `SPLIT-LICENSE-SCAN.md` resolvido sem tabela central nem nota de rodapé: **a licença viaja com o arquivo** |
| `.github/workflows/license-check.yaml` | 1 dos 12 workflows; nome medido, conteúdo não lido linha a linha | a verificação de cabeçalho/licença é **CI**, não revisão humana; nossos `tools/validate.py` checam documento, não código |

`AGENTS.md` (257 linhas) fecha o conjunto com as obrigações de release: `uv run towncrier build --draft`
para prévia do changelog e checagem de nome de fragmento no CI de todo PR; e o `CLAUDE.md` é **uma linha**:
`@AGENTS.md` (import por referência, mesmo princípio dos symlinks do `cal.diy` em `LR-FORGE-019` — um dono,
dois leitores).

## 5. Onde isto poderia se aplicar (a viabilidade é do dono)

> **Escopo desta seção** — sugestão do que a evidência sustenta, mais a pergunta de viabilidade; não é
> instrução para nenhum app (`MISSION.md` §3, `DR-0019` §5).

| App | O que sugiro considerar | O que custaria no app |
|---|---|---|
| Research (esta base) | `LICENSE-<origem>.md` ao lado de todo trecho vendorizado (o `PUBLISHING-PROTOCOL.md` pede atribuição; isto torna a atribuição local e verificável) | zero de código: é convenção de escrita |
| Lia Agent Hub | Skills de manutenção interna com `disable-model-invocation: true` para as operações irreversíveis (publicar, marcar obsoleta, remover) | decisão de produto; o campo já existe no corpus medido (8 dos 178) |
| Lia Studio / Forge | separar "escrever descrição" de "submeter" em duas Skills com pesos diferentes | escopo de produto |

## 6. O que não verifiquei, e por quê

- **nada do produto**: exige `uv` + dezenas de SDKs de fornecedor + microfone/playback; não instalei, não
  rodei um pipeline, não chamei nenhum modelo (custo e tráfego — política desta base);
- o `license-check.yaml` foi identificado, não lido passo a passo; não verifiquei **o que** ele checagem
  (cabeçalho SPDX? dependências?);
- dos 12 `SKILL.md`, li integralmente o `provider-research`; os outros onze foram medidos por tamanho e
  frontmatter no censo dos 178 (perfil `revise` de 2 pacotes + 1 `blocked` pelo nosso scanner — o `blocked`
  é o YAML inválido do `squash-commits`, ver `LR-CMP-004` §2);
- `RESEARCH_GUIDE.md`, `inventory.py`, `publish.py`, `probe.py` não foram lidos por inteiro (2.169 linhas nos
  cinco scripts de `scripts/provider-watch/`);
- as dependências de tempo real (audioop removido no Python 3.13, `evals/`, `scripts/provider-watch`) não
  foram executadas; o `docs/` (29 arquivos em `docs/`, além de 68 `.md` no total) não foi lido.

## 7. Recomendação: **ADAPT**

Não como framework de voz — a Lia não tem caso de uso de voz medido nesta base que exija `pipecat`. Como
**três práticas de manutenção**: Skills de processo com `disable-model-invocation` nos passos irreversíveis,
licença de componente vendorizado viajando com o componente, e verificação de licença no CI (não na revisão).
Isto é `ADAPT` no sentido estrito da nossa escala: copiar o desenho, não o software.

## 8. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 17.439 ★ · 3.185 forks · 587 issues · Python · BSD-2-Clause · homepage pipecat.ai | `OBSERVED` | `gh api repos/pipecat-ai/pipecat` |
| 2.616 entradas / 2.256 blobs / 53,0 MB; 1.781 `.py`; 12 `SKILL.md`; 12 workflows; 3 caminhos `LICENSE`; 68 `.md` | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio |
| as 12 Skills estão em `.claude/skills/`, com tamanhos de 1.381 a 19.096 B (84.899 B no total) | `OBSERVED` | `wc -c` nos arquivos materializados |
| `provider-research` com `disable-model-invocation: true`, subagente duplicado em `.claude` e `.codex`, scratch fora do repo, memória por issue, `--limit` para teste | `OBSERVED` (texto) | `.claude/skills/provider-research/SKILL.md` lido por inteiro |
| `LICENSE-shadcn.md` ao lado dos componentes vendorizados; `license-check.yaml` no CI | `OBSERVED` (caminhos) | árvore recursiva |
| `CLAUDE.md` = `@AGENTS.md` (1 linha) e `AGENTS.md` com towncrier/fragmentos | `OBSERVED` (texto) | arquivos materializados e lidos |
| 12 Skills passaram pelos dois gates do `LR-CMP-004`: 8 `publish_candidate`, 2 `revise`, 1 `blocked` + 1 sem pacote | `LOCAL_SMOKE_PASS` (parcial) | analisador DeerFlow + validador Anthropic executados neste sandbox sobre o corpus materializado |
| o que o `license-check.yaml` faz exatamente | `NOT_RUN` | workflow identificado por nome, não lido passo a passo |
| comportamento de voz em tempo real, latência, qualidade | `NOT_RUN` | sem ambiente de áudio nem chaves de API; fora de escopo por política |

## 9. Ponteiras para a próxima rodada

1. ler `scripts/provider-watch/publish.py` (510 linhas): é o único lugar do corpus medido onde uma Skill
   delega **a publicação** a um script com passos explícitos — o padrão que a `DR-0020` discute para o Hub;
2. checar se `license-check.yaml` cobre cabeçalho SPDX por arquivo ou só dependências (1 leitura de ~40
   linhas, e define se a prática é copiável para `tools/validate.py`);
3. medir quantos dos 12 `SKILL.md` têm `references/` ao lado (o censo dos 178 não materializou o pipecat por
   completo: 11 de 12 entraram).

## 10. Como isto se liga à base

Nosso `agents/SKILLS-OPERATING-SET.md` mantém 48 registros de Skills sem nenhuma regra sobre **quando usá-las
e quando não podem ser usadas sozinhas**. O pipecat tem isso resolvido por campo de manifesto
(`disable-model-invocation: true` nas operações com consequência externa) — é o elo que falta na nossa
discussão de `DR-0020`, e custa uma linha de frontmatter por Skill, não um framework.
