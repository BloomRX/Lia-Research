# daytona (público) — um repositório de 71.271 ★ que hoje tem 3 arquivos: o código foi para um lugar privado

| Campo | Valor |
|---|---|
| ID | `LR-PROV-002` |
| Nome | `daytonaio/daytona` — infraestrutura de execução para código gerado por IA ("Run AI Code. Secure and Elastic Infrastructure for Running Your AI-Generated Code") |
| Tipo | repositório (estado atual = **aviso de manutenção**, não produto) |
| Fonte oficial | https://github.com/daytonaio/daytona · org sucessora https://github.com/daytona |
| Responsável | org `daytonaio` (12 repositórios públicos) → desenvolvimento movido para a org `daytona` (32 repositórios na página 1) e para **codebase privada** |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED — não há o que executar: a `main` tem 3 arquivos (`README.md` + 2 PNG) |
| Recomendação | **REJECT** — sugestão ao dono: não tratar `daytonaio/daytona` como fonte de código nem como evidência de sanidade do produto; e **este objeto é um caso de política de registro** (§5) |
| Decisão de adoção | — nenhuma registrada |
| Categoria | proveniência de código + desaparecimento de fonte |
| Projetos beneficiados | Research (política de registro), Lia Agent Hub (o que fazer com objeto catalogado que some do ar), Lia Forge (rastreabilidade de dependência) |
| Versão analisada | `main` em 2026-11-25 (último push 2026-07-24) · **última tag `v0.190.0`** · ≥100 tags na primeira página da API |
| Proveniência do conteúdo | medido por nós: `gh api` do repositório, árvore recursiva, `contents/LICENSE` em `HEAD` e em `v0.190.0`, `orgs/daytonaio/repos`, `orgs/daytona/repos`, `repos/daytona/skills` |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api repos/daytonaio/daytona` + `git/trees/HEAD?recursive=1` (`truncated: false`) |
| Upstream conferido | **71.271 ★** · 5.637 forks · 457 issues abertas · **`archived: true`** · **`license: null`** · **`language: null`** · criado 2024-02-06 |
| Próxima revisão | 2027-02-25 (repositório arquivado: não muda sozinho) |
| Licença | **AGPL-3.0 apenas nas tags**: o `LICENSE` de `v0.190.0` tem 34.522 B e cabeçalho lido "GNU AFFERO GENERAL PUBLIC LICENSE Version 3"; **na `main` não há `LICENSE`** — `contents/LICENSE?ref=main` devolve `404 Not Found`, e o `README` avisa que o uso é livre "under the [LICENSE](…/blob/v0.190.0/LICENSE)" — **o próprio projeto linka a licença por tag, não por branch** |
| Confiança | Altíssima sobre o estado do repositório (são 3 arquivos, todos lidos); nenhuma sobre o produto privado |

---

## 1. O que o dono pediu, e o que a medição mostrou

O link veio no meio da leva de 16. Havia três hipóteses plausíveis antes de medir: projeto ativo, projeto
morto, projeto que virou empresa fechada. A medição decidiu pela terceira, com um detalhe que nenhuma das
hipóteses previa: **o repositório foi esvaziado**, não apenas arquivado.

## 2. Números que falam sozinhos

| Medida | Valor |
|---|---|
| entradas recursivas na `main` | **5** |
| blobs | **3** |
| bytes da árvore | **151.194** (≈151 KB) |
| arquivos de código | 0 |
| `LICENSE` na `main` | **ausente** (`404`) |
| workflows | 0 |
| estrelas / forks / issues | 71.271 / 5.637 / 457 |
| `archived` / `license` / `language` na API | `true` / `null` / `null` |
| o que restou no `README` | aviso + logotipos + escada de links (docs, Slack, issues) |

O texto do aviso, literal: *"**This repository is no longer maintained.** As of June 2026, Daytona's core
development has moved to a **private codebase**. This repository will receive no further updates, fixes, or
releases. It remains public and free to use, fork, and build on under the
[LICENSE](https://github.com/daytonaio/daytona/blob/v0.190.0/LICENSE), as is and without support or
warranty."* — e a referência a recursos em `github.com/daytona`.

Os commits que produziram esse estado, na ordem: `chore: sync go.sum for v0.190.0 (#5122)` (2026-06-23),
`daytona maintenance notice` (2026-06-23), `Fix license link in README` (2026-06-25). Ou seja: **a última
manutenção pública do repositório foi apontar a licença para uma tag fixa.** A `main` não tinha mais o
arquivo.

## 3. Para onde foi

| Objeto | Medido |
|---|---|
| org `daytonaio` | 12 repositórios; `daytona` arquivado; `docs` **arquivado**; `helm-charts` ativo (24 ★, `NOASSERTION`, último push 2026-11-19); `sandbox-network-whitelist` ativo (3 ★, sem licença) |
| org `daytona` (a nova) | 32 repositórios na página 1; top por estrelas: `ai-enablement-stack` 646, `content` 124, `legacy-daytona-provider-docker` 56, `sdk` 37, **`skills` 23** |
| `daytona/sdk` | 37 ★, `license: NOASSERTION` — o SDK que substitui o cliente open-source **não tem licença SPDX detectável** |
| `daytona/skills` | árvore com **1 entrada: um único `SKILL.md`** — a empresa publica Skills como arquivo solto |

Dois detalhes que valem registro para o Hub: (a) o SDK — a peça que um consumidor efetivamente usa — está
`NOASSERTION`, o que no nosso método (`SPLIT-LICENSE-SCAN.md` §1) quer dizer "leia o arquivo; há mais de uma
história"; (b) um repositório de Skills com **um arquivo e nenhuma licença ao lado** é o caso-limite que o
`SKILL-LICENSE-CONSOLIDATION.md` descreve como "instrução pura sem procedência": não é forkável com
segurança, é texto sem envelope.

## 4. O que não é, para não escrever errado depois

- **não** é "o produto morreu": o produto mudou de endereço (org nova com 32 repositórios e `helm-charts`
  em atividade até 2026-11-19) e o core virou privado;
- **não** é "licença revogada": o texto publicado continua AGPL-3.0 nas tags, e o aviso reafirma o direito de
  uso/fork/build **sobre o que foi publicado**;
- **não** confunda `daytonaio/daytona` com `daytonaio/docs`: ambos arquivados; os `helm-charts` e o
  `sandbox-network-whitelist` continuam ativos, e é neles que a superfície de operação pública ainda vive.

## 5. A regra que este objeto cria para esta base

Um registro de catálogo que aponta para `main` de um repositório **morre sem aviso** quando o dono apaga o
conteúdo. Nossa defesa atual é a coluna `Versão analisada` + `Última verificação`, que funciona; o que
falta é a **âncora por tag quando o objeto tem releases**. Daytono é o contraexemplo que prova o ponto: o
próprio maintenedor teve que mudar o link da licença de `blob/HEAD/LICENSE` para
`blob/v0.190.0/LICENSE` (commit de 2026-06-25). Se o `data/inventory/license-matrix.tsv` dissesse só
"AGPL-3.0, `LICENSE`", hoje essa linha apontaria para um arquivo inexistente.

Proposta para o dono (nada aplicado nos apps da Lia):

| App | Sugestão | Custo |
|---|---|---|
| Research (esta base) | objeto com release publicada: a linha do matrix cita **tag + digest do `LICENSE`** (padrão que já usamos em `LR-FORGE-012`); objeto `archived` vira `Próxima revisão` longa, não ciclo de 30 dias | edição de política + uma coluna de convenção; zero código |
| Lia Agent Hub | regra análoga para **fontes de Skill**: uma Skill cuja origem some do ar não pode ficar `CURRENT`; a procedência precisa ser capturada no momento da importação | decisão de produto; o mecanismo é o nosso `evidence` vazio = `UNVERIFIED` |

## 6. O que não verifiquei, e por quê

- o conteúdo das tags antigas não foi auditado (baixar 100 tags de um projeto Go não cabe aqui); abri só o
  `LICENSE` de `v0.190.0` para confirmar o texto AGPL;
- **não** afirmei nada sobre o produto atual da Daytona (preço, API, disponibilidade) — o que está fora do
  GitHub não foi medido, e a allowlist daqui não visita `daytona.io`;
- `daytona/sdk` está `NOASSERTION`: **não** abri o arquivo de licença do SDK (fica como próximo passo se o
  dono quiser avaliar o cliente);
- o `SKILL.md` único de `daytona/skills` foi contado, não lido por inteiro;
- `helm-charts` e `sandbox-network-whitelist` foram censados por metadados; nenhuma leitura de conteúdo.

## 7. Recomendação: **REJECT** (e por que mesmo assim valeu)

`REJECT` no sentido operacional: não há objeto técnico para adotar, e qualquer dependência de "o que o
repositório diz" hoje leria um aviso. O valor da entrada está em (i) fechar a pergunta "o que houve com o
Daytono?" com números lidos, (ii) produzir a regra de âncora do §5, e (iii) alimentar o nosso censo de
formatos de licença com um caso raro: **licença existente só na tag, ausente na `main`** — o que nenhum dos
17 formatos do `SPLIT-LICENSE-SCAN.md` previa.

## 8. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| `archived: true`, 71.271 ★, `license: null`, `language: null`, último push 2026-07-24 | `OBSERVED` | `gh api repos/daytonaio/daytona` |
| árvore da `main` = 5 entradas / 3 blobs / 151.194 B (2 PNG + 1 `README.md`) | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) |
| `LICENSE` ausente na `main` | `OBSERVED` | `contents/LICENSE?ref=main` → `404 Not Found` |
| `LICENSE` em `v0.190.0`: 34.522 B, cabeçalho "GNU AFFERO GENERAL PUBLIC LICENSE Version 3" | `OBSERVED` | `contents/LICENSE?ref=v0.190.0` (tamanho + primeiras linhas) |
| aviso de "moved to a private codebase" e link de licença fixado na tag | `OBSERVED` (texto) | `gh api repos/daytonaio/daytona/readme` decodificado |
| `daytona maintenance notice` (2026-06-23) e `Fix license link in README` (2026-06-25) | `OBSERVED` | `commits?per_page=3` |
| org `daytonaio`: 12 repositórios, `docs` arquivado, `helm-charts` ativo 24 ★ `NOASSERTION` | `OBSERVED` | `orgs/daytonaio/repos` |
| org `daytona`: 32 repositórios; `sdk` 37 ★ `NOASSERTION`; `skills` com 1 `SKILL.md` e nenhuma licença ao lado | `OBSERVED` | `orgs/daytona/repos` + `repos/daytona/skills/git/trees/HEAD?recursive=1` |
| sanidade/qualidade do produto atual | `NOT_RUN` | fora do GitHub; não medido |
| termos de serviço e preço do SaaS | `NOT_RUN` | domínio fora da allowlist desta sessão |

## 9. Ponteiras para a próxima rodada

1. ler o `LICENSE` do `daytona/sdk` (org nova, `NOASSERTION`) — é a pergunta "o que um consumidor da Daytona
   pode fazer hoje" e custa um `contents/`;
2. listar os 12 assets da release `v0.190.0` (`releases/tags/v0.190.0`) e checar se há `digest` publicado: é o
   teste da nossa própria regra de âncora (§5) num caso real de produto fechado;
3. verificar se `daytonaio/helm-charts` (ativo, 24 ★, `NOASSERTION`) ainda aponta para imagens do produto
   público — se sim, é a única superfície executável que restou.

## 10. Como isto se liga à base

A coluna `Próxima revisão` desta base nasceu para pegar objeto velho; este objeto pegou **desaparecimento de
conteúdo**, que é diferente: a `main` continua viva (o `pushed_at` é de julho), só que vazia. A regra prática
que extraio e proponho (§5) é que objeto com release tem de ser registrado por **tag**, e objeto sem licença
na `main` tem de citar a ref em que a licença foi lida. É a mesma disciplina que usamos no `DR-0004` com
`assets[].digest` — aqui aplicada ao que acontece **depois** que o arquivo some.
