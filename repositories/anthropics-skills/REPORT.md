# `anthropics/skills` + o diretório oficial de plugins — onde mora a licença de uma Skill, e o que o validador deles rejeita

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-017` |
| Nome | `anthropics/skills` (19 Skills em `skills/` + o `template/` na raiz; inclui as duas que o dono apontou: `algorithmic-art` e `skill-creator`) + `anthropics/claude-plugins-official` (o diretório de plugins, 43 plugins) + o tópico `skill-creator` |
| Tipo | repositórios (acervo de Skills + diretório de plugins) e tópico como objeto de censo |
| Fonte oficial | https://github.com/anthropics/skills · https://github.com/anthropics/claude-plugins-official · https://github.com/topics/skill-creator |
| Responsável | org `anthropics` (`id` 58798950); no `anthropics/skills` o contribuidor nº 1 é `rlancemartin` (17) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | LOCAL_SMOKE_PASS (parcial) — o `quick_validate.py` deles foi **executado** por mim sobre 177 pacotes de 10 repositórios; nada dos produtos foi instalado nem executado |
| Recomendação | **ADAPT** — sugestão ao dono: o `skill-creator` é o documento canônico sobre como escrever e validar Skills; o empacotamento de licença deles (por Skill, com `THIRD_PARTY_NOTICES.md` e **sem** `LICENSE` na raiz) é o formato a imitar no Hub |
| Decisão de adoção | — nenhuma registrada |
| Categoria | formato de Skill + validação + licenciamento por pacote |
| Projetos beneficiados | **Lia Agent Hub** (formato de pacote e de licença), **Lia Forge** (`agents/SKILLS-OPERATING-SET.md` desta base), Research (a regra "documento que não é relatório" — §5 abaixo vale também para nós) |
| Versão analisada | `HEAD` de cada repositório em 2026-11-25 (`gh api … /git/trees/HEAD?recursive=1`) |
| Proveniência do conteúdo | medido por nós: censo de árvore dos dois repositórios, leitura direta de `README.md`, `THIRD_PARTY_NOTICES.md`, `spec/agent-skills-spec.md`, `template/SKILL.md`, `skills/{algorithmic-art,skill-creator,doc-coauthoring}/SKILL.md`, `skills/skill-creator/{SKILL.md,agents/*,scripts/*}`, `plugins/skill-creator/**` e `plugins/plugin-dev/skills/skill-development/**`; os 4 links do dono viraram **um** censo de 187 `SKILL.md` |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 |
| Upstream conferido | `anthropics/skills`: **200.497 ★** · 544 entradas / 448 blobs / 12,1 MB · 20 `SKILL.md` · **0 `LICENSE` na raiz** · 18 `LICENSE.txt` · `THIRD_PARTY_NOTICES.md` com 404 linhas · 0 workflows · criado 2025-03-06 · `license: null` na API. `anthropics/claude-plugins-official`: **48.219 ★** · **Apache-2.0** · 1.273 entradas · **62 `SKILL.md` em 21 plugins (43 plugins no total)** · 50 caminhos com `LICENSE` · 7 workflows |
| Próxima revisão | 2026-12-09 |
| Licença | `anthropics/skills`: **sem licença de repositório**; 18 `LICENSE.txt` um-por-Skill, e as duas Skills apontadas pelo dono estão em situações diferentes — `skill-creator` tem, `algorithmic-art` tem (com `templates/`), e `doc-coauthoring`/`template` não. `claude-plugins-official`: Apache-2.0 de plugin **mais** `LICENSE.txt` por Skill |
| Confiança | Alta para contagens e para o texto lido; o julgamento de "qual licença serve ao Hub" é opinião técnica, não fato |

---

## 1. O fato mais incômodo: 53 dos 80 "inválidos" são rejeitados pelo validador da própria Anthropic

Rodei `skills/skill-creator/scripts/quick_validate.py` (168 linhas) sobre os **177** `SKILL.md` que materializei
com todos os recursos, de 10 repositórios: **97 válidos, 80 inválidos**. Agregando os motivos dos 80:

| motivo | casos |
|---|---|
| **só por chaves desconhecidas no frontmatter** | **53** |
| `name` (maiúsculas/pontuação/divergência com o diretório) | 22 |
| `description` (vazia/longa) | 2 |
| YAML inválido no frontmatter | 2 |
| `compatibility` veio dicionário, e não string | 1 |

A lista de chaves aceitas é literal: `allowed-tools, compatibility, description, license, metadata, name,
product, version`… — e o validador **rejeita qualquer chave fora dela**. Só que `argument-hint` (22 usos),
`user-invocable` (17), `disable-model-invocation` (8), `disallowed-tools` (6) e `tools` (2) são chaves em uso
corrente no ecossistema, inclusive em produtos de fornecedor. Consequência para nós: **um gate que rejeita
chave desconhecida vira o gate do medo — as pessoas param de declarar metadados úteis** para passar no
validador. O `LR-CMP-004` §4 mostra o outro lado da moeda (o gate permissivo deixa passar 5 pacotes que um
scanner de código bloqueia).

## 2. O repositório que ensina o empacotamento de licença: 18 arquivos, nenhuma raiz

`anthropics/skills` tem **200 mil estrelas e nenhum `LICENSE` na raiz**. O que ele tem:

- **um `LICENSE.txt` dentro de cada pasta de Skill** (18), citado no frontmatter como
  `license: Complete terms in LICENSE.txt`;
- um **`THIRD_PARTY_NOTICES.md` de 404 linhas** no raiz, com blocos por licença e componente
  (`BSD 2-Clause License … imageio 2.37.0, Copyright (c) 2014-2022, imageio developers`);
- um `template/SKILL.md` na raiz de 140 bytes que é só `name: template-skill` + `description:` +
  `# Insert instructions below` (e o `name` **não** bate com o diretório `template/` — um dos 29 casos);
- um `.claude-plugin/` — ou seja, o acervo **se apresenta como marketplace de plugins**, não como repositório
  de exemplos;
- um `spec/agent-skills-spec.md` de **87 bytes / 3 linhas**, que não especifica nada: é um aviso apontando
  para `agentskills.io` como dono do padrão.

É o caso extremo do formato `B`/`G` do nosso `SPLIT-LICENSE-SCAN.md`: split declarado em dois níveis (por
Skill + terceiros), com o repositório nu. Comparação direta com nossos quatro casos (`LR-FORGE-016` OpenProject,
`LR-FORGE-017` open-seo, `LR-FORGE-019` cal.diy, `LR-FORGE-020` Charakuru) — este é o único em que **a ausência
na raiz é intencional**: eles não querem que uma licença de repositório seja lida como licença das Skills.

## 3. O `skill-creator` é uma peça de engenharia, não um prompt

33.168 bytes de `SKILL.md` + **1.897 linhas de Python em 8 scripts**:

O pacote tem quatro subpastas, e cada uma tem nome e tamanho (medidos): em `scripts/`, os **8 scripts de
Python** (`quick_validate.py`, `package_skill.py`, `run_eval.py`, `run_loop.py`, `aggregate_benchmark.py`,
`improve_description.py`, `generate_report.py`, `utils.py`); na subpasta de definição de subagentes,
**`analyzer.md`, `comparator.md`, `grader.md`**; em `eval-viewer/`, `generate_review.py` + `viewer.html`; em
`assets/`, `eval_review.html`; e `schemas.md` na subpasta de referências.

Lê-se daí: (i) empacotar tem script (`package_skill.py`); (ii) validar tem script (**sem** executar o
conteúdo); (iii) avaliar tem script com **loop** (`run_loop.py`) e **agregação de benchmark**
(`aggregate_benchmark.py`) e um **grader** em `skills/skill-creator/agents/grader.md` com **comparador pareado cego**
(`…/agents/comparator.md` — a mesma ideia do `--model-a/--model-b` do open-seo, `LR-FORGE-017`); (iv) a
**descrição** tem um otimizador próprio (`improve_description.py`), porque é ela que faz o disparo;
(v) há um visualizador de HTML para revisão humana dos runs.

É a resposta material à pergunta que esta base vem enrolando desde `LR-AGENT-009` (manifesto de workflow) e
`DR-0020`: Skill publicada precisa de *ferramenta de verificação*, e a ferramenta tem um nome e um tamanho.
Não propomos adotar o `skill-creator` — propomos **medir a nossa distância dele**: nós temos o
`tools/validate.py` (catálogo) e nenhum `run_eval.py` (comportamento).

## 4. A Skill que virou arquivo de referência: a `claude-plugins-official` tem dois `skill-creator`

`plugins/skill-creator/skills/skill-creator/SKILL.md` é **byte-idêntico** ao do `anthropics/skills` —
confirmei com `sha256sum` dos dois arquivos materializados: `dcd4803e61e913e6…3e7b3c2bcf` nos dois. Espelho
entre repositórios mantido por cópia (não há script de sincronização na árvore; 43 plugins, 62 `SKILL.md`).

E o `plugins/plugin-dev/skills/skill-development/references/skill-creator-original.md` é a **versão anterior**
do mesmo texto, agora rebaixada a arquivo de referência — **mantendo o frontmatter de Skill** (`name:
skill-creator`, `description: Guide for creating effective skills…`). Duas consequências medidas: (a) dentro
de um mesmo repositório há dois arquivos que se declaram `skill-creator`; (b) um arquivo em `references/`
com frontmatter de Skill é um falso-positivo pronto para qualquer censador que conte `name:` — o meu censo
dos 178 evitou isso só porque procurei por nome de arquivo (`SKILL.md`), não por presença de frontmatter.
É um ângulo novo para a DR-0004 (inventário do Studio): **contar Skills por frontmatter e por caminho dá
números diferentes**; a auditoria do mr-mak usou caminho (`40 SKILL.md` no ZIP), e está correta, mas o critério
precisa ficar escrito.

## 5. O gênero "criador de Skills", medido no tópico

`topic:skill-creator` = **81 repositórios**, cabeça por estrelas: `rpamis/comet` 3.316 (MIT),
`joeseesun/qiaomu-meta-skill` 393 (MIT), `AGI-comming/functional-skill-creator` 257 (MIT),
`antongulin/opencode-skill-creator` 199 (Apache-2.0), `oil-oil/oil-skill-creator` 103 (MIT), cauda em 9–23 ★.
Licenças: MIT domina, **2 sem licença** (`jalaalrd/video-to-skill`, `youngfreeFJS/skill-test-skill`) e 1
`NOASSERTION` (`ceresOPA/Alicization-Town`). Dois deles são concorrentes diretos do gate do §1
("tests and scores any Agent Skill against the official…") — ficam como fila, não abri.

Leitura que a evidência permite: "criar Skills" já é **gênero de repositório** com tópico próprio, 81 entradas
e uma cauda de ~10 ★ por projeto. Isso não é mercado; é o comportamento esperado de um formato novo sem
registro: cada um publica o seu gerador/avaliador. Se o Hub quer ser o registro, a barreira não é técnica —
é existir um lugar canônico onde um `skill-creator` é encontrado.

## 6. `algorithmic-art`, o link específico do dono

`SKILL.md` de 19.769 bytes de instruções + `templates/generator_template.js` + `templates/viewer.html` +
`LICENSE.txt` — **zero executável obrigatório**: é uma Skill que produz arte generativa escrevendo código para
o usuário rodar, com um visualizador HTML ao lado. Compara com `webapp-testing` (que precisa de Playwright) e
com o `Scrapling-Skill` (`LR-DATA-002`): três pontos no espectro "Skill como texto" → "Skill com scripts" →
"Skill com dependência de ferramenta". Nosso `agents/SKILLS-OPERATING-SET.md` (48 entradas) fica no primeiro
ponto — e é o que o `SKILL-LICENSE-CONSOLIDATION.md` já descreve como "instrução pura, custo de adaptação baixo".

## 7. O que não verifiquei, e por quê

- **nada foi instalado nem executado**: o `run_eval.py`/`run_loop.py` exigem agente + API de modelo (custo e
  tráfego de API — a política da base proíbe gastos e chaves), e o `package_skill.py` só empacota; rodei o
  `quick_validate.py` como biblioteca, não como CLI de CI;
- não abri os 43 plugins um por um; os números são censo de árvore + leitura do `skill-creator` e do
  `plugin-dev/skill-development`;
- não baixei nem inspecionei os `.zip`/marketplace de `anthropics/skills` (0 releases publicadas — medi
  `releases` vazio em rodadas anteriores; não reconfirmei nesta);
- não entrei em `agentskills.io` nem em `skills.sh` (o README referencia ambos; fora do escopo de links do dono
  e fora do que dá para verificar aqui);
- o conteúdo dos 18 `LICENSE.txt` por Skill não foi lido um por um — contei presença e li o do
  `skill-creator`; a afirmação "cada Skill tem o seu" é censo, não leitura integral.

## 8. Recomendação: **ADAPT** (duas práticas, um aviso)

**Adaptar:** (1) o empacotamento de licença por Skill + `THIRD_PARTY_NOTICES.md` na raiz — é o formato que o
nosso `SKILL-LICENSE-CONSOLIDATION.md` propõe para o Hub, com um precedente de 200 mil estrelas; (2) a
existência de scripts de validação/empacotamento **junto** da Skill, como parte do pacote (não do repositório
 hospedeiro).
**Avisar:** a rigidez do `quick_validate.py` (rejeitar chave desconhecida) é um erro que podemos não repetir —
o `deer-flow` mostra o caminho do meio (chaves próprias registradas + waiver com hash e expiração,
`LR-AGENT-016` §5).

## 9. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 200.497 ★; `license: null`; 544 entradas; 20 `SKILL.md`; **0 `LICENSE` na raiz**; 18 `LICENSE.txt`; `THIRD_PARTY_NOTICES.md` 404 linhas | `OBSERVED` | `gh api repos/anthropics/skills` + `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio + leitura do arquivo |
| `spec/agent-skills-spec.md` tem 87 B e só aponta para `agentskills.io`; `template/SKILL.md` tem 140 B com `name: template-skill`; `.claude-plugin/marketplace.json` existe | `OBSERVED` | arquivo materializado por sparse-checkout e lido |
| `claude-plugins-official`: 48.219 ★, Apache-2.0, 1.273 entradas, 62 `SKILL.md` em 21 plugins, 43 plugins, 50 caminhos `LICENSE` | `OBSERVED` | API + censo de árvore (`truncated: false`) |
| `plugins/skill-creator/skills/skill-creator/SKILL.md` e `anthropics/skills/skills/skill-creator/SKILL.md` têm o mesmo `sha256` `dcd4803e…` | `OBSERVED` | `sha256sum` nos dois arquivos materializados neste sandbox |
| `skill-creator-original.md` em `references/` mantém frontmatter com `name: skill-creator` | `OBSERVED` | leitura do arquivo (`head -14`) |
| 177 validações com o `quick_validate.py` da Anthropic: 97 válidos / 80 inválidos; 53 inválidos só por chave desconhecida | `LOCAL_SMOKE_PASS` (parcial) | `importlib` sobre o script deles, corpus = 10 repositórios materializados (`/tmp/r25/anthropic_validate.json`, agregação em `/tmp/r25/cross_validate.py`) |
| chaves em uso no corpus: `allowed-tools` 26, `compatibility` 26, `argument-hint` 22, `license` 19, `user-invocable` 17, `version` 13, `disable-model-invocation` 8, `disallowed-tools` 6, `tools` 2 | `OBSERVED` | parse de frontmatter dos 178 arquivos (`/tmp/r25/corpus_final.json`) |
| `topic:skill-creator` = 81 repositórios; distribuição de licenças da cabeça | `OBSERVED` | `gh api "search/repositories?q=topic:skill-creator"` (`total_count` + itens) |
| o `skill-creator` roda de ponta a ponta (eval, loop, grader) | `NOT_RUN` | exige agente + API de modelo com custo; nada foi chamado |
| os 18 `LICENSE.txt` são todos iguais entre si | `NOT_RUN` | li o do `skill-creator`; a comparação byte a byte dos 18 não foi feita |

## 10. Ponteiras para a próxima rodada

1. comparar byte a byte os 18 `LICENSE.txt` de `anthropics/skills` (dá 1 comando: `sha256sum`); se forem
   idênticos, a licença por Skill é cerimonial e o Hub pode tratá-la como **herdada do acervo**, não negocial;
2. abrir `youngfreeFJS/skill-test-skill` e `jalaalrd/video-to-skill` (sem licença, 11 e 14 ★): são os dois
   concorrentes diretos dos gates deste dossiê;
3. medir quantos dos 173 pacotes têm `scripts/` **executáveis sem dependência** (o `quick_validate.py` deles
   usa PyYAML, que não é stdlib — um gate de Skill que precisa de dependência externa já é uma decisão de
   plataforma).

## 11. Como isto se liga à base

O censo dos 187 é o mesmo número que o `agents/SKILLS-OPERATING-SET.md` desta casa usa para si (48 registros
nossos): a comparação que importa não é "quantos", é **que um acervo de 200 mil estrelas não tem licença na
raiz e tem 18 envelopes de licença dentro**, enquanto nós temos 1 `LICENSE` na raiz e 0 por Skill. Nosso
formato é o do repositório; o deles é o do pacote. Se o Hub um dia publicar Skills de terceiros, o modelo
deles é o que sobrevive à extração.
