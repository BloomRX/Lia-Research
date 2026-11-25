# Scrapling — a biblioteca que publica a própria Skill (com `LICENSE.txt`, ZIP versionado e `requires.bins` no frontmatter)

| Campo | Valor |
|---|---|
| ID | `LR-DATA-001` |
| Nome | `D4Vinci/Scrapling` — "Maskless Fallback & Stealth Mode" — framework Python de scraping adaptativo (fetcher, stealth browser, parsing e spiders) |
| Tipo | repositório (biblioteca) + pacote de Skill de terceiros |
| Fonte oficial | https://github.com/D4Vinci/Scrapling (o link do dono usava `d4vinci` minúsculo; a API resolveu para `D4Vinci`) · docs `scrapling.readthedocs.io` |
| Responsável | `D4Vinci` (usuário individual; contribuidor nº 1 com 1.716 de 4.498 commits — projeto de autor, não de empresa) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED — `pip install scrapling` + navegadores stealth exigiriam rede fora da allowlist; nenhum script da Skill foi executado |
| Recomendação | **REFERENCE_ONLY** — sugestão ao dono: guardar o **formato** do `agent-skill/` (Skill versionada junto da lib, com ZIP e metadados de runtime) como referência para o Hub; não propomos adotar a lib |
| Decisão de adoção | — nenhuma registrada |
| Categoria | biblioteca de scraping + empacotamento de Skill de fornecedor |
| Projetos beneficiados | **Lia Agent Hub** (formato `agent-skill/` e o ZIP como artefato), **Research** (política de artefatos binários versionados — o caso é análogo ao ZIP do mr-mak em `DR-0004`) |
| Versão analisada | `main` no HEAD de 2026-11-25 (`pushed_at 2026-11-25T23:03:43Z`) · `agent-skill/Scrapling-Skill/SKILL.md` declara `version: "0.5.1"` |
| Proveniência do conteúdo | medido por nós: censo de árvore, leitura de `agent-skill/README.md`, do frontmatter do `SKILL.md`, do `LICENSE.txt` da Skill e listagem de `references/` (18 arquivos) e `examples/` (5) |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api` + `git/trees/HEAD?recursive=1` (`truncated: false`) + `search/commits` (2.293 no mês) |
| Upstream conferido | **105.781 ★** · 11.084 forks · **26 issues abertas** · Python · 841 entradas / 697 blobs / 10,8 MB · 171 `.py` · **416 `.md`** · 5 workflows · 2 caminhos `LICENSE` (raiz + Skill) |
| Próxima revisão | 2026-12-09 |
| Licença | **BSD-3-Clause** na raiz; e a Skill tem **`LICENSE.txt` próprio** ("BSD 3-Clause License / Copyright (c) 2024, Karim shoair") com `license: Complete terms in LICENSE.txt` no frontmatter — o mesmo padrão das 18 Skills da Anthropic, aplicado por um autor individual |
| Confiança | Alta no formato empacotado (lido); **zero** quanto a capacidade anti-bot — não executei nada |

---

## 1. O que o dono está olhando, e o que isto vale

O link foi dado no meio de uma leva de Skills. Scrapling **não é** um conjunto de Skills: é uma biblioteca de
scrapling que **distribui** uma Skill. Isso o torna o ponto mais útil da leva para o Hub, porque é o caso que
nos falta: **fornecedor de ferramenta publicando o manual de uso correto como pacote versionado**.

A frase do próprio `agent-skill/README.md` diz o objetivo com precisão operacional: *"so it can use the
current API instead of guessing from outdated training data"* — a Skill existe para **substituir a memória do
modelo sobre a API da lib** pela API atual. É a justificativa mais limpa que já vi para Skill de fornecedor,
e vale como argumento para o Lia Forge ter Skills oficiais próprias em vez de depender de terceiros (o
`SKILL-LICENSE-CONSOLIDATION.md` §4.1 é exatamente sobre essa fronteira).

## 2. O pacote, medido

```
agent-skill/
├── README.md                     (1.721 B — instalação em 3 caminhos)
├── Scrapling-Skill.zip           (98.463 B — o pacote pronto, versionado no git)
└── Scrapling-Skill/
    ├── SKILL.md                  frontmatter: name: scrapling-official · version: "0.5.1" · license
    ├── LICENSE.txt               (BSD-3-Clause do autor)
    ├── examples/                 4 scripts (01_fetcher_session … 04_spider) + README
    └── references/               18 arquivos (building-rag-systems.md, fetching/choosing.md, static.md …)
```

Dois detalhes que não vi em nenhum dos outros 186 `SKILL.md` que censei:

1. **`name: scrapling-official` ≠ nome do diretório** (`Scrapling-Skill`) — um dos 29 casos do censo; o
   `name` escolhido é deliberadamente "official" (a Skill se apresenta como a versão canônica, distinguindo-se
   de cópias comunitárias);
2. **`metadata.openclaw.requires.bins: [python3]` + `anyBins: [pip, pip3]`** — declaração de **pré-requisito
   de runtime** no frontmatter, mais `emoji`. É o único caso no corpus com um contrato de "o que precisa estar
   instalado para esta Skill funcionar" — no nosso vocabulário: a coluna de ambiente do
   `check_environment.py` do HairDeck (`LR-FORGE-021`) expressa em 4 linhas de YAML.

## 3. O ZIP versionado no `main` — um caso de proveniência, não de gosto

`agent-skill/README.md`: *"You can use this **direct URL** to download the ZIP file of the skill directly"* →
`https://github.com/D4Vinci/Scrapling/raw/refs/heads/main/agent-skill/Scrapling-Skill.zip`. Consequências
medidas e declaráveis:

- o artefato binário está **no histórico** (blob de 98.463 B). A Skill e o ZIP convivem na mesma árvore, então
  quem instala pelo ZIP recebe o que o autor empacotou naquele commit, **não** o estado atual da Skill — se há
  defasagem, só a comparação do `sha256` do blob com os arquivos responde, e isso eu não fiz (§6);
- a URL é **por ramo** (`refs/heads/main`), não por tag — o mesmo endereço muda de bytes a cada push. É
  a forma mais exposta do problema que a `governance/LICENSE-AND-PROVENANCE-POLICY.md` §5 fixou para a Lia:
  artefato precisa de **tag + digest**;
- há um terceiro caminho: **ClawHub** (`docs.openclaw.ai/tools/clawhub`) como registro de instalação do
  formato — o `agent-skill/README.md` documenta `Clawhub`, Claude Code e OpenClaw como consumidores do mesmo
  pacote, citando a especificação `agentskills.io/specification`.

Comparação direta com `DR-0004` (o ZIP do mr-mak): lá o ZIP estava **fora** da árvore, num `docs/` de app, e
o problema foi prová-lo (resolvido por `assets[].digest`); aqui o ZIP está **dentro** do repositório de código
com URL de ramo. A Lição para o Hub é a mesma dos dois casos: **ou se distribui por registro com digest, ou
se distribui por tag com digest; distribuir por URL de ramo é distribuir um artefato que ninguém consegue
nomear**.

## 4. A biblioteca em si: o que a árvore diz (e o que eu não abri)

416 arquivos `.md` contra 171 `.py` — Scrapling é um projeto **documentado acima da média** (a proporção é o
inverso do `deer-flow`, 363 `.md` para 2.715 `.py`). 26 issues abertas com 105.781 estrelas e 11.084 forks, e
2.293 commits no último mês, indicam um mantenedor que fecha fila. **Não abri a documentação de uso nem o
código de scraping** — o assunto deste dossiê é o empacotamento; a viabilidade técnica de `Scrapling` como
ferramenta de dados da Lia é uma pergunta diferente, com `NOT_RUN` explícito abaixo.

## 5. Onde isto poderia se aplicar (a viabilidade é do dono)

> **Escopo desta seção** — sugestão do que a evidência sustenta, mais a pergunta de viabilidade; não é
> instrução para nenhum app (`MISSION.md` §3, `DR-0019` §5).

| App | O que sugiro considerar | O que custaria no app |
|---|---|---|
| **Lia Agent Hub** | o formato `agent-skill/` (Skill + ZIP + `LICENSE.txt` + `references/`) como layout canônico de pacote publicado; e a exigência de **tag** para o artefato | decisão de formato; nenhuma dependência do Scrapling é necessária |
| **Lia Agent Hub** | frontmatter com pré-requisitos de runtime (`requires.bins`) como campo de manifesto — hoje o ecossistema quase não declara nada (0 de 187 declaram ambiente além deste caso) | pequeno: um campo no schema de Skill |
| **Lia Forge** | a frase de propósito da Skill de fornecedor ("usar a API atual em vez de chutar com base em treino velho") é o argumento para `scripts/reports`/Skills de produto terem **dono e versão** | texto de política |

## 6. O que não verifiquei, e por quê

- **nada da lib foi executado**: instalar `scrapling` e os navegadores stealth pede pip fora da allowlist e
  centenas de MB; nenhum script dos `examples/` rodou. Logo, "a Skill faz o agente usar a API certa" é a
  alegação do autor, não minha conclusão;
- não comparei byte a byte o conteúdo do ZIP com o diretório `Scrapling-Skill/` — **dá para fazer** (`sha256`
  do blob vs. arquivos), e fica como próximo passo se o dono quiser saber se o artefato está defasado;
- não abri os 18 `references/*.md` individualmente, nem o `docs/` da lib;
- não verifiquei quantas Skills comunitárias de Scrapling existem fora do repositório (o `name:
  scrapling-official` sugere que sim — contagem não feita);
- ClawHub não foi consultado (fora da allowlist).

## 7. Recomendação: **REFERENCE_ONLY**

`REFERENCE_ONLY` porque o objeto que nos serve é o **pacote**, não a biblioteca: se o Hub for definir layout de Skill
publicável, este é um dos poucos casos reais em que um autor individual empacotou direito (licença própria,
versão no frontmatter, exemplos, referências, artefato). E `WATCH` também para a pergunta de defasagem
ZIP × diretório, que é barata de responder e da qual já temos precedente interno (`DR-0004`).

**Propor** ao dono, sem aplicar: (i) registrar no `SPLIT-LICENSE-SCAN.md` o formato "licença no
frontmatter apontando para `LICENSE.txt` da Skill" como variante do formato `G` (agora com dois
precedentes: Anthropic e um autor individual); (ii) abrir pergunta de Hub: "Skill de fornecedor deve poder
declarar pré-requisitos de runtime (`requires.bins`) no manifesto?".

## 8. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 105.781 ★ · 11.084 forks · 26 issues · Python · BSD-3-Clause · `D4Vinci/Scrapling` (o `d4vinci` do dono redireciona) | `OBSERVED` | `gh api repos/D4Vinci/Scrapling` |
| 841 entradas / 697 blobs / 10,8 MB; 416 `.md`; 171 `.py`; 5 workflows; 2 caminhos `LICENSE` | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio |
| estrutura de `agent-skill/` (README + ZIP de 98.463 B + `SKILL.md` + `LICENSE.txt` + 18 `references/` + 5 `examples/`) | `OBSERVED` | sparse-checkout do diretório + `find`/`ls -la` |
| `name: scrapling-official`, `version: "0.5.1"`, `license: Complete terms in LICENSE.txt`, `metadata.openclaw.requires.bins/anyBins` | `OBSERVED` (texto) | `sed -n 1,22p` do `SKILL.md` materializado |
| ZIP distribuído por URL de `refs/heads/main`; instalação também por ClawHub; alegação "instead of guessing from outdated training data" | `OBSERVED` (texto) | `agent-skill/README.md` lido |
| 2.293 commits no último mês; `D4Vinci` com 1.716 de 4.498 contribuições | `OBSERVED` | `search/commits?q=repo:…+committer-date:>2026-10-25` + `contributors` |
| o ZIP corresponde ao diretório atual | `NOT_RUN` | `sha256` do blob vs. arquivos — factível, não executado nesta rodada |
| a Skill melhora o uso da API pelo agente; anti-bot, stealth, performance | `NOT_RUN` | exigiria instalar a lib e rodar contra sites; não medido |

## 9. Ponteiras para a próxima rodada

1. `sha256` do blob `agent-skill/Scrapling-Skill.zip` vs. o `sha256` reconstruído do diretório — fecha a
   pergunta de defasagem (§6) com um comando, e é o teste de "artefato versionado no código envelhece?";
2. contar quantos dos 18 `references/*.md` têm caminho citado no `SKILL.md` (o gate do deer-flow achou
   14 referências órfãs no corpus; o Scrapling é o caso em que isso é verificação barata);
3. ver se há Skills comunitárias de Scrapling fora do repositório (o `name: scrapling-official` sugere
   duplicação) — busca por tópico/nome, sem instalar nada.

## 10. Como isto se liga à base

O ZIP na `main` com URL de ramo é o espelho exato do `DR-0004` desta casa, só que **sem a defesa**: lá, o
pacote do mr-mak foi identificado porque a release publicava `digest`; aqui não há tag nem digest, e o objeto
é mantido por um autor individual. É o argumento mais curto que existe para a regra da
`governance/LICENSE-AND-PROVENANCE-POLICY.md` §5: artefato sem âncora nomeável envelhece em silêncio, e o
custo de percebê-lo cresce com o número de consumidores.
