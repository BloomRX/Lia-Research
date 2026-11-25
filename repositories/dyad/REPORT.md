# dyad — a organização do dono, um `LICENSE` que divide o repositório em dois, e um workflow que apaga release não autorizada

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-023` |
| Nome | `dyad-sh/dyad` — "AI app builder": construtor de aplicações com agente, desktop + web; a org `dyad-sh` é o que o dono pediu (o link veio duplicado na mensagem, tratado como **um** objeto com nota sobre a org) |
| Tipo | organização (8 repositórios) + repositório principal |
| Fonte oficial | https://github.com/dyad-sh/dyad · https://dyad.sh |
| Responsável | org `dyad-sh` — **usuário, não organização verificada** com 8 repositórios públicos; contribuidor nº 1 `wwwillchen` (1.429) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED (aplicativo Electron/TS exige `pnpm install`; não instalado) |
| Recomendação | **ADAPT** — sugestão ao dono: o `LICENSE` com **exceção por diretório** (§3) e o workflow de release-guarda (§4) são os dois itens aproveitáveis como padrão; nada indica adoção do produto |
| Decisão de adoção | — nenhuma registrada |
| Categoria | construtor de apps + prática de licenciamento split + higiene de release |
| Projetos beneficiados | Research (`SPLIT-LICENSE-SCAN.md` ganha um formato novo), **Lia Agent Hub** (o `remove-unauthorized-release.yml` como padrão de proteção de release) |
| Versão analisada | `main` no HEAD de 2026-11-25 (`pushed_at 2026-11-24T17:57:09Z`) · releases: **`v1.25.0-beta.1` (2026-11-24)**, `v1.24.0` (2026-11-23) — cadência de beta diária com **12 assets por release** · criado 2025-04-11 |
| Proveniência do conteúdo | medido por nós: metadados da API, censo da árvore recursiva, leitura do `LICENSE` raiz (via API), de `src/pro/LICENSE` (lido no clone) e de `.github/workflows/remove-unauthorized-release.yml` |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api` + `git/trees/HEAD?recursive=1` (`truncated: false`) + `search/commits` (80 no mês) |
| Upstream conferido | **22.452 ★** · 2.852 forks · 373 issues abertas · 4.442 entradas / 4.110 blobs / **39,4 MB de árvore** · 2.286 `.ts`, 768 `.tsx`, **322 `.md`** · **24 `SKILL.md`** · 5 caminhos `LICENSE` · 23 workflows |
| Próxima revisão | 2026-12-09 |
| Licença | **`NOASSERTION` na API — e é o caso mais limpo de split que já medimos**: o `LICENSE` raiz (11.694 B) abre com *"Portions of this software are licensed as follows: • All content that resides under the `src/pro/` directory … is licensed under the license defined in `src/pro/LICENSE`. • Content outside of the above mentioned directories … is available under the Apache 2 license as defined below."* — e o `src/pro/LICENSE` (3.746 B) é **FSL-1.1-ALv2** ("Functional Source License, Version 1.1, ALv2 Future License", `Copyright 2025 Dyad Tech, Inc.`) com seção **"Grant of Future License"** |
| Confiança | Alta no que está nos arquivos; **zero** sobre o produto em execução |

---

## 1. O que o link duplicado significava

O dono colou `https://github.com/dyad-sh` duas vezes. Li como **um** pedido sobre a organização, e a
org é mesmo o dado interessante: dos **8 repositórios públicos**, 3 são forks (`sandpack-bundler`,
`supabase-management-js`, `ollama-ai-provider-v2`), 3 são templates (`nextjs-template` 26 ★,
`portal-mini-store-template` 30 ★, `tanstack-start-template` 0) e 1 é utilitário interno
(`react-vite-nitro` 0 ★). **Um repositório sustenta a org: `dyad` (22.452 ★)** — não é ecossistema de
bibliotecas abertas; é o produto publicado num lugar onde também moram os templates que ele gera. Para o
nosso registro isso muda o verbo: cataloga-se o `dyad`, e a org entra como contexto, não como "projeto com
N componentes".

## 2. O que a árvore diz

4.442 entradas / 4.110 blobs / 39,4 MB. Composição por extensão: 2.286 `.ts`, 768 `.tsx`, 322 `.md`,
208 `.json`, 100 `.yml`, 97 `.txt`. **24 `SKILL.md` em `.claude/skills/`**, 23 workflows, 5 caminhos `LICENSE`
(`LICENSE`, `src/pro/LICENSE`, 2 em `packages/@dyad-sh/*` e 1 em `benchmarks/app-builder/template/nextjs/`).
Traduzindo: as Skills da casa vivem no diretório do host Claude (`LR-CMP-004` §5), os templates que o produto
gera trazem a licença do template alheio junto, e os pacotes internos têm `LICENSE` próprio — os três níveis
do split.

## 3. O formato de licença que faltava no nosso censo

`SPLIT-LICENSE-SCAN.md` tinha 8 formatos; o do dyad é um **novo** (registro lá, não aqui):

| Elemento | O que o arquivo faz |
|---|---|
| Raiz `LICENSE` (Apache-2.0, 11.694 B) | **começa com um preâmbulo de exceção** antes do texto da licença: 2 *bullets* que movem `src/pro/` para outro regime |
| `src/pro/LICENSE` (3.746 B) | FSL-1.1-ALv2: licença funcional com **permissão para uso não competitivo** e a seção **"Grant of Future License"** — o `ALv2` do nome significa que a versão futura do código migra para Apache-2.0 |
| `packages/@dyad-sh/*/LICENSE`, `benchmarks/.../nextjs/LICENSE` | licença de terceiro carregada junto do pacote vendorizado, como deve ser |

Duas coisas que isto resolve para esta base:

1. `NOASSERTION` **com dois arquivos** é diferente de `NOASSERTION` com um acordo comercial: o GitHub não
   consegue classificar, mas a leitura leva dois minutos e o resultado é determinístico. Nosso método já diz
   isso (`SPLIT-LICENSE-SCAN.md` §1); o dyad é o caso mais didático da coleção, porque o preâmbulo está na
   primeira linha do `LICENSE`;
2. FSL + "future license" é o meio-termo que nem o Charakuru (`LR-FORGE-020`, licença por faturamento) nem a
   OpenProject (`LR-FORGE-016`, `ee/` privado) têm: o código restrito **vira Apache-2.0 no prazo**. É a
   resposta curta para "dá para publicar feature comercial sem fechar o repositório?" — sim, com data de
   virada escrita no arquivo.

Não confundir com "o dyad é AGPL/MIT/X": a pergunta "o que podemos copiar daqui" tem resposta diferente por
diretório, e é o preâmbulo que diz qual.

## 4. O workflow que apaga release que não saiu do CI

`.github/workflows/remove-unauthorized-release.yml` (lido no clone):

- gatilho: `on: release: types: [published]`, com `permissions: {}` no topo e `contents: write` só no job;
- **condição**: `if: github.event.release.author.login != 'github-actions[bot]'` — se o autor da release não é
  o robô do CI, ela não é autorizada;
- passo 1 "Record unauthorized release": escreve no sumário do job **tag e autor** (`$RELEASE_TAG`,
  `$RELEASE_AUTHOR`);
- passo 2 "Delete release": `gh api --method DELETE "repos/$REPOSITORY/releases/$RELEASE_ID"`;
- job separado `send-email` com `if: always() && …` para alertar;
- ações pinas por SHA (`actions/checkout@93cb6efe…# v5`, `actions/setup-node@a0853c24…# v5`) — não por tag.

Isto é uma **política de integridade de artefato** executada em minutos, e é o espelho do nosso problema de
`DR-0004` e da regra §5 da `governance/LICENSE-AND-PROVENANCE-POLICY.md`: lá, a pergunta foi "o ZIP no `docs/`
é o artefato publicado?"; aqui a pergunta é "esta release veio do pipeline?". O dyad resolve a segunda com
autoria + deleção + registro público. Nada a importar (nós não publicamos releases por GitHub Actions com
bot), mas é o melhor argumento que vi para **registrar autor + tag no sumário do job** quando um projeto Lia
publicar um pacote — inclusive o `SKILLS-OPERATING-SET` desta base, que hoje publica por commit.

## 5. As 24 Skills internas, medidas no censo do `LR-CMP-004`

O `dyad` é o maior contribuinte de Skills depois dos repositórios especializados: **24 `SKILL.md`** em
`.claude/skills/`, com **0** arquivos de licença por Skill e **0** chaves `license:`. No gate da Anthropic, o
pacote `deep-review` tem **YAML inválido no frontmatter** (1 de apenas 2 casos em 178 arquivos — o outro é do
pipecat) e **21 dos 23** pacotes medidos ficaram em `revise` (1 `publish_candidate`, 1 `blocked`). É o perfil típico de Skill interna: texto de
processo, sem envelope de licença, nem sempre com frontmatter limpo — e é também o perfil que o Hub teria de
engolir se importasse Skills de produto sem exigir nada. Registro sem juízo: isto não torna o dyad pior;
mostra que "publicar dentro de casa" não segue as regras de "publicar para fora".

## 6. O que não verifiquei, e por quê

- **nada do produto rodou**: exige `pnpm install` + Electron; não instalei (política da base) e não abri o
  `src/pro/` além do `LICENSE`;
- não li os outros 4 `LICENSE`/`LICENSE.txt` do repositório (só confirmei caminhos); não verifiquei se as
  mudanças em `src/pro/` estão de fato restritas a esse diretório — o que medi é o **texto do preâmbulo**;
- não abri as 24 Skills uma por uma (censo + o caso `deep-review`);
- não li os 23 workflows além do `remove-unauthorized-release.yml`;
- não verifiquei os 12 assets das releases (nome/tamanho/digest) — é o próximo passo natural se o dono
  quiser o padrão de artefato do dyad comparado com o nosso (`LR-FORGE-012`);
- o produto comercial (dyad.sh, planos, telemetria) não foi visitado — fora do escopo desta base.

## 7. Recomendação: **WATCH**

`ADAPT` pelo formato de licença (split com exceção por diretório + futura Apache) e pela higiene de release;
e serve também porque o `NOASSERTION` do dyad, do OpenProject e do Charakuru agora formam uma coleção de três
comportamentos distintos que a API não distingue — e que nós distinguimos em `SPLIT-LICENSE-SCAN.md`.
Não recomendo nada do produto: a Lia não tem caso de uso de "construtor de apps" medido nesta base.

## 8. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| org `dyad-sh` = usuário com 8 repositórios públicos (3 forks, 3 templates, 1 utilitário, 1 produto) | `OBSERVED` | `gh api orgs/dyad-sh/repos` + `users/dyad-sh` |
| 22.452 ★ · 2.852 forks · 373 issues · TypeScript · `NOASSERTION` · criado 2025-04-11 | `OBSERVED` | `gh api repos/dyad-sh/dyad` |
| 4.442 entradas / 4.110 blobs / 39,4 MB; 2.286 `.ts`; 322 `.md`; **24 `SKILL.md`**; 5 `LICENSE*`; 23 workflows | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio |
| preâmbulo do `LICENSE` raiz (11.694 B) movendo `src/pro/` para `src/pro/LICENSE` e o resto para Apache-2.0 | `OBSERVED` (texto) | `gh api repos/dyad-sh/dyad/contents/LICENSE` decodificado (`head -12`) |
| `src/pro/LICENSE` = FSL-1.1-ALv2, 3.746 B, 104 linhas, "Copyright 2025 Dyad Tech, Inc.", com "Grant of Future License" e a definição de *Competing Use* | `OBSERVED` (texto) | arquivo lido no clone com filtro de blob + `grep` de seções |
| release guarda: autor ≠ `github-actions[bot]` → registrar no sumário e `DELETE` via `gh api`, com `send-email` em `always()` e ações pinadas por SHA | `OBSERVED` (código de workflow) | `.github/workflows/remove-unauthorized-release.yml` lido no clone |
| 24 Skills com 0 licença e 0 `allowed-tools`; `deep-review` com YAML inválido | `OBSERVED` | censo dos 187 + corpus de 178 materializados (`/tmp/r25/corpus_final.json`) |
| releases `v1.25.0-beta.1` (2026-11-24) e `v1.24.0` (2026-11-23) com 12 assets cada | `OBSERVED` | `releases?per_page=3` |
| 80 commits nos últimos 30 dias | `OBSERVED` | `search/commits?q=repo:dyad-sh/dyad+committer-date:>2026-10-25` |
| o construtor gera apps, qualidade de output, telemetria | `NOT_RUN` | nada instalado nem executado |
| se as mudanças em `src/pro/` respeitam o preâmbulo de licença | `NOT_RUN` | o diff por diretório não foi auditado |

## 9. Ponteiras para a próxima rodada

1. `sha256` dos 12 assets de `v1.24.0` vs. `git ls-remote` da tag — é o parâmetro que usaríamos para
   "publicação íntegra" no Hub (e o teste da ideia do §4);
2. ler os outros 4 arquivos `LICENSE` (2 pacotes internos, 1 template de benchmark) para ver se herdaram
   Apache ou levaram licença própria;
3. contar quantas das 24 Skills internas têm `references/` ou `scripts/` ao lado (o censo de 178 mediu 0
   `allowed-tools` no `dyad`; falta o resto do perfil).

## 10. Como isto se liga à base

O `NOASSERTION` do dyad é o quarto caso da coleção desta casa — OpenProject (`ee/` privado),
Charakuru (licença por faturamento), AppFlowy Cloud (acordo de self-host) e agora **exceção por diretório com
virada futura**. A regularidade que os quatro ensinam e que o `SPLIT-LICENSE-SCAN.md` agora registra é: o
campo SPDX da API só diz que **o robô desistiu**; a decisão está sempre no arquivo, quase nunca no
repositório inteiro.
