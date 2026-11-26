# MCPVault — um servidor MCP que lê e escreve um vault de notas Markdown, medido de ponta a ponta

| Campo | Valor |
|---|---|
| ID | `LR-MCP-005` |
| Nome | `bitbonsai/mcpvault` — "A local MCP server that lets compatible clients read, search, and edit notes in an Obsidian vault" |
| Tipo | repositório (servidor MCP em TypeScript, distribuído como pacote npm `@bitbonsai/mcpvault`) |
| Licença | **MIT** (`LICENSE` de 1.071 B medidos). Camada de terceiros: `@modelcontextprotocol/server` e `@modelcontextprotocol/core` **Apache-2.0** (`LICENSE` 12.227 B, **nenhum `NOTICE`** no pacote), `gray-matter` MIT, `yaml` ISC, `trash` MIT |
| Categoria | mcp |
| Projetos beneficiados | **Lia-Project** (consumo de notas do usuário), Lia Agent Hub (superfície de tool para agente), Research (método de ensaio executado) |
| Fonte oficial | https://github.com/bitbonsai/mcpvault · https://mcpvault.org · npm `@bitbonsai/mcpvault` |
| Responsável | `bitbonsai` (Fabio K. Stanzani, conhecido por `bitbonsai/test-guard`; o projeto é mantido por uma pessoa com 137 forks) |
| Versão analisada | `5d4e68550e9fe27fc24b9e16d96b8ff5b39355d7` (2026-11-14, merge do PR #285 `release/0.18.4`) = npm **0.18.4** |
| Proveniência do conteúdo | medido por nós nesta sessão: clone do repo, `npm install`, `npm test`, `npm run build`, e **quatro scripts de ensaio MCP sobre stdio** contra quatro vaults sintéticos — 13 servidores iniciados, com **92 chamadas de ferramenta registradas em JSON** (`trial/resultado.json`: 4 cenários, 75 chamadas; `resultado2.json`: 1 cenário, 17) e dois ensaios de conferência com saída impressa (`trial-lia3.mjs` frontmatter, `trial-lia4.mjs` pasta de config renomeada); leitura de `src/*.ts` (21 arquivos, **7.529 linhas** por `wc -l`; são 25 arquivos `.ts` em `src/**`, com 7.776 linhas) e `dist/server.js` |
| Data | 2026-11-26 |
| Última verificação | 2026-11-26 |
| Upstream conferido | 2026-11-26 via API — ★**1.733** · 137 forks · **23** issues abertas · `language: TypeScript` · `size` 5.451 KB · criado 2025-09-21 · `pushed_at` 2026-11-23T12:06:56Z (o `main` que clonamos está em `5d4e6855` de 2026-11-14 — os 9 dias de diferença são atividade fora da `main`: branches de release e issues; foi o `5d4e6855` que instalamos, testamos e medimos, não o `pushed_at`) · `license.spdx_id` MIT · npm latest **0.18.4**, `engines.node >=22.12.0`, `unpackedSize` 172.093 B, 4 dependências de runtime |
| Estado da pesquisa | TESTED |
| Resultado de execução | LOCAL_TESTS_PASS — suíte deles executada aqui (446 testes) + 4 cenários de execução real do servidor |
| Recomendação | **ADAPT** — a superfície de ferramentas e as quatro defesas de caminho são portáveis; o pacote **não** deve entrar como dependência da Lia |
| Decisão de adoção | — nenhuma (fora da autoridade desta base) |
| Confiança | Alta para tudo que foi executado e lido no código; média para o comportamento em Windows (ver §12 — duas issues abertas específicas, não reproduzidas aqui) |
| Próxima revisão | 2026-12-24 |

---

## 1. O que é, em uma linha

Um processo local, lançado por stdio, que expõe **18 ferramentas** sobre uma pasta de notas no disco
e se recusa a tocar em qualquer coisa fora dela. Não tem banco, não tem índice persistente, não tem
conta, não tem telemetria, não abre porta e não faz chamada de rede — verificado, não presumido (§9).
É o objeto mais próximo do que a pergunta da rodada pede ("Lia lê as notas do usuário, com seleção
explícita, proveniência, escopo, correção e exclusão"), e por isso ele foi executado aqui.

## 2. A superfície (contagem medida na sessão real)

`tools/list` devolve **18** ferramentas:
`read_note`, `read_note_lines`, `read_multiple_notes`, `get_note_outline`, `get_notes_info`,
`get_frontmatter`, `update_frontmatter`, `list_directory`, `list_all_tags`, `get_vault_stats`,
`search_notes`, `wiki_link`, `manage_tags`, `write_note`, `patch_note`, `move_note`, `move_file`,
`delete_note`.

Com `--read-only` a lista encolhe para **11** (`write_note`, `patch_note`, `move_note`, `move_file`,
`update_frontmatter`, `manage_tags`, `delete_note` somem de `tools/list`) **e** a chamada ainda é
recusada com mensagem própria: `write_note is disabled because MCPVault is running in read-only mode.`
Isso é o desenho correto — o cliente descobre a incapacidade pelo contrato, não por tentativa e erro.
Medido: `trial/resultado.json` cenário `C_read-only`.

## 3. O que executamos aqui (nada disto é inferido de README)

| Ensaio | Comando | Resultado |
|---|---|---|
| Suíte do projeto | `npm install` (135 pacotes, 5 s) · `npm test` | **446 testes passando em 14 arquivos**, 7,26 s, Node v22.22.3, vitest 5.1.0. Distribuição: `filesystem` 208 · `pathfilter` 52 · `frontmatter` 48 · `release` 34 · `atomic-write` 26 · `search` 25 · `createServer` 13 · `wikilink` 15 · `integration` 5 · `cli` 7 · `uri` 7 · `protocol-version` 2 · `shutdown` 2 · `system-trash` 2 |
| Compilação | `npm run build` (`tsc --project tsconfig.build.json`) | exit 0, `dist/server.js` 3.194 B + `dist/src/**` |
| Banco de notas sintético | 3 vaults criados por script (4, 3.001 e 5 arquivos) | `A_leitura` 22 chamadas · `B_escrita` 15 · `C_read-only` 4 · `D_exclusao` 3 · ensaio 2 com 3.001 notas · ensaio 3 de round-trip · ensaio 4 de pasta de configuração renomeada |

Todo o conteúdo era inventado por nós (`nota-rig.md`, `decisoes.md`, `Diário/2026-11-26.md`, 3.000 notas
`n0000..n2999` com a agulha em `n2517`). **Nenhuma nota real do usuário foi lida.**

## 4. Leitura e escrita: o que a ferramenta devolve de verdade

- `read_note` devolve `{fm, content}` — o frontmatter sai **separado** do corpo, não como texto cru.
- `get_note_outline` devolve títulos com nível e **número da linha** (`[{"level":1,"text":"Rig de teste","line":7}]`);
  `read_note_lines` recorta por faixa de linhas. Para um agente que vai **reescrever** uma nota, esse par
  é mais útil que a leitura inteira, e é o que a Lia deveria expor.
- `patch_note` exige unicidade: `oldString: 'palavra'` numa nota com 90 ocorrências devolve
  `{"success": false, "message": "Found 90 occurrences... Use replaceAll=true...", "matchCount": 90}`.
  Com `replaceAll: true`, as 90 foram trocadas e o resto do arquivo permaneceu.
  **É a primitive de correção certa**: ambiguidade é recusa, não "primeiro achado".
- `write_note` aceita `mode: overwrite | append | prepend`. O append **não garante linha em branco**
  (aberto como issue #273; nosso ensaio mascarou o efeito porque passamos `\n` explícito).
- **Não há limite de tamanho de leitura nem de escrita.** `read_note` sobre uma nota de 2 MB devolveu
  **1.950.034 bytes** em uma resposta (91 ms); `write_note` gravou 3 MB sem objeção. Para uma Lia que
  injeta contexto em modelo pequeno, isso é o primeiro buraco a fechar — o store atual do Project tem
  tetos (`400_000` bytes no documento, 500 caracteres por entrada: `lia/core/src/memory/store.ts`, lido
  hoje na `main`) e a ponte com notas do usuário precisa dos mesmos tetos.

## 5. Busca: lexical, sem índice, com escopo

`search_notes` caminha a árvore e casa substring — não há FTS nem índice persistente no repo.
Medido com 3.001 notas / 4,28 MB: busca da agulha **406 ms**, busca de termo comum (`limit: 20`)
**409 ms**, `get_vault_stats` **147 ms** — i.e. o custo é o walk completo, por chamada. O resultado
traz `path`, `title`, `excerpt`, `matchCount`, `line` e `uri`, o que chega para *atribuir* a fonte de
um trecho, mas **não traz relevância calculada**: a ordenação é por contagem de ocorrências
(`mc: 90` no nosso caso), não por BM25. Escopo funciona: `pathPrefix: "Projetos"` restringe,
`excludePaths: ["Projetos"]` subtrai, e `searchFrontmatter: true` acha `decisao` **só** no frontmatter.
Consequência para a Lia: com vault de centenas de notas isso é aceitável; com dezenas de milhares,
ou se busca roda a cada turno, o walk precisa virar índice — e aí o candidato de índice é o
`SQLite/FTS5` que `LR-HW-001`/`LR-AGENT-001` já recomendam, não um banco vetorial.

## 6. Limites de diretório e contenção — a parte que vale o estudo

Quatro defesas, todas medidas, cada uma com o arquivo-fonte:

| Defesa | Como funciona no código | O que medimos |
|---|---|---|
| Segmentos restritos **em qualquer profundidade** | `src/pathfilter.ts:9-19` (`RESTRICTED_SEGMENTS`: `.obsidian`, `.git`, `node_modules`, `.DS_Store`, `Thumbs.db`, comparados em minúsculo por segmento) + `.trash` nos `ignoredPatterns` | busca **não** achou `keyword-nested` em `<vault>/tools/cli/node_modules/pacote/index.md`, nem `keyword-lixo` em `.trash/velho.md`; `list_directory /` não listou `.obsidian` nem `.trash` |
| Lista de extensões, aplicada na **leitura** | `allowedExtensions = [.md, .markdown, .txt, .base, .canvas]` (`src/pathfilter.ts:29-36`) | `.png` e `.json` recusados com `Access denied`; `.txt` lido |
| Travessia de caminho | normalização + verificação de pertencimento | `../fora-do-vault.md` → `Path traversal not allowed`; caminho absoluto fora → recusado |
| **Symlink** | resolve o destino e exige que esteja dentro do vault | `link-para-fora.md` → `Symlink target is outside vault`; e o ensaio de disco confirmou `nada escrito fora do vault` nos 4 cenários |

Um teste que **não** virou achado, e vale registrar como teste bem-sucedido: o Obsidian permite
renomear a pasta de configuração (`help.obsidian.md` — "Override config folder", por exemplo
`.obsidian-desktop`). Esperávamos que a lista literal `.obsidian` deixasse a pasta renomeada passar.
Medido: `.obsidian-desktop/README.md` foi **recusado** — a regra de recusa é por *ponto inicial* do
segmento (o texto da mensagem diz "dotfiles are not accessible"), não pelo nome exato. A defesa é
mais forte que a lista sugere.

Efeito colateral real, este confirmado: **qualquer pasta de plugin é "nota"**. `plugins/meu-plugin/README.md`
entrou na busca e na leitura (e o `get_vault_stats` contou 2 notas num vault de 5 arquivos, porque só conta
extensões permitidas). Ou seja: "o vault" ≠ "as notas do usuário". A seleção explícita que a Lia precisa
não é um detalhe de UX — é uma fronteira de escopo, e o vault do Obsidian contém código de terceiros.

## 7. Proveniência: o que existe e o que falta

Existe: `get_notes_info` devolve `size`, `modified` (epoch ms), `hasFrontmatter` e **`obsidianUri`**
(`obsidian:////<caminho>`), que é um deep-link para a pessoa abrir a nota no app — a peça que falta
para "a Lia citar de onde veio" ser acionável pelo usuário. Não existe: nenhum carimbo de
*quando a Lia leu*, nenhum digest do conteúdo, nenhuma noção de "esta nota mudou desde que você a
indexou". O modelo de proveniência da Lia precisa acrescentar `sha256` + `lido_em` + escopo, e o
único lugar sensato para isso é o **índice derivado**, nunca o arquivo do usuário (escrever no vault
para registrar proveniência é a decisão errada — §8).

## 8. Conflitos e concorrência: aqui o pacote não serve de modelo

- Escrita é **last-writer-wins**: não há pré-condição do tipo "só escreva se o arquivo ainda tiver o
  hash que você leu". `write_note` sobre `notas/n0002.md` existentes simplesmente sobrescreveu.
- O round-trip do frontmatter é *preservante mas não idêntico*: medimos comentário à mão e ordem das
  chaves **sobrevivendo** a `update_frontmatter` (`filesystem.ts:308,946,1061` usam `preserveStringify`),
  mas `tags: [lia]` virou `tags: [ lia ]` — exatamente o que a issue aberta **#288** descreve, e o
  **#289** complementa ("re-sorts keys and omits the blank line"). O `#` disso é o preço de usar
  `gray-matter` como invólucro; eles mitigam a parte perigosa trocando o motor de parsing pelo `yaml`
  (`src/frontmatter.ts:5-15`, com o motivo: js-yaml 3.x tem DoS quadrático por merge-key aliases,
  **CVE-2023-44270**, e o motor `javascript` do gray-matter é desabilitado para não avaliar YAML como JS).
- `move_note` renomeia o arquivo mas **não conserta** `[[wikilinks]]` apontando para o nome antigo
  (issue **#274**, aberta — não reproduzimos de propósito, para não depender de bug alheio).
- `get_notes_info` **descarta silenciosamente** caminhos inexistentes ou recusados (issue **#290**).
  Para um contrato de proveniência, "silencioso" é o defeito: a Lia precisa de `missing` explícito —
  que é justamente o que `LiaMemoryResult` já faz hoje (`code: 'missing'`).
- Sem *watchdog*: `#166` pede timeout por chamada porque uma operação pendurada **trava a sessão MCP**
  (e `#167` mostra um caso real com `EISDIR` em `move_note`).

## 9. Tráfego de dados: verificado, não afirmado

Grep em `src/` e `dist/` por `fetch(`, `http.request`, `https.request`, `WebSocket`, `axios`,
`XMLHttpRequest`: **zero ocorrências fora dos testes**. As 4 dependências de runtime são o SDK MCP
(transporte stdio), `gray-matter`, `yaml` e `trash` (que chama utilitários do sistema operacional para
mover ao cesto local). `package.json` não declara `postinstall` nem telemetria. Não abrimos firewall
nem rodamos com `http_proxy` envenenado — o que temos é a ausência de sítio de chamada, que é mais
forte que "não vimos tráfego" e mais fraco que "rede bloqueada com sucesso": registrado como está.
Dado sensível em trânsito: **nenhum**, desde que o cliente MCP seja local — o modelo lê o texto que a
ferramenta devolve, então o egresso real é o prompt do modelo, não o servidor.

## 10. Segurança: postura do projeto e o que não confere

`SECURITY.md` pede *private vulnerability reporting* no GitHub e promete resposta em 72 h.
A issue aberta **#287** afirma que o PVR está desabilitado (`404`) — **não medimos** (a API de
disponibilidade de PVR não é legível por token de integração), então fica como `REPORTED`, com o
ponto indicado. Há também uma auditoria estática de terceiro aberta como **#221**
("nothing exploitable, one filename edge case"), que citamos como contexto, não como prova.

## 11. Licença e o que ela permite aqui

MIT no `LICENSE` (1.071 B). O que o MIT cobre é o código do servidor — **não** as notas do usuário,
que continuam sendo do usuário (e o Obsidian declara isso: "You retain ownership of all content you
create in Obsidian. We do not claim any rights to it" — `obsidian.md/license`, página consultada em
2026-11-26, atualizada em 2025-02-20). Se a Lia copiar qualquer trecho, o aviso MIT vai junto.
A camada Apache-2.0 do SDK MCP pede `NOTICE` se redistribuído; o pacote não traz `NOTICE` nenhum
(medido: 4 arquivos em `node_modules/@modelcontextprotocol/server`), o que é o padrão que
`LR-LIC-005` já registra como "criar se redistribuir".

## 12. Compatibilidade com o ambiente da Lia

| Dimensão | Situação | Fonte |
|---|---|---|
| Node | precisa de `>=22.12.0`; rodou em v22.22.3 | medido |
| Windows | duas issues abertas específicas de raiz de unidade: **#283** (`obsidianUri` dobra o separador quando o vault está na raiz) e **#281** (`patch_note`/`update_frontmatter` falham e caminhos de busca perdem um caractere quando o vault é raiz de unidade/compartimento, 0.18.2+). A máquina de referência da Lia é Windows: **se o vault do usuário for `D:\`, isso é caso de teste, não suposição** | `REPORTED` (títulos das issues; não reproduzido — sem Windows aqui) |
| GPU / modelo | nenhum uso | medido (grep) |
| Banco vetorial | nenhum | medido (`src/` inteiro) |
| Latência por busca em vault grande | 406 ms para 3.001 notas, por chamada, sem cache | medido |
| Escrita concorrente com o editor do usuário | não detecta; last-writer-wins | medido |

## 13. O que portar (forma) e o que não usar

Portar, sem importar o pacote: (1) as **quatro recusas de caminho** de §6, com a mesma semântica de
"falhar é o resultado"; (2) `--read-only` **refletido em `tools/list`**, não só na execução; (3) o par
`get_note_outline` + `read_note_lines` como via de edição cirúrgica; (4) `patch_note` com recusa por
ambiguidade; (5) `delete_note` com `confirmPath` igual a `path` e `trashMode: local` movendo para
`.trash/<caminho-relativo>` (medido: 94 B intactos em `.trash/Projetos/Lia/nova.md`) — reversível para a
pessoa; (6) lista de extensões **positiva** em vez de lista de nomes a negar.

Não usar: o pacote como dependência da Lia (são 18 ferramentas e um contrato de texto que a Lia não
precisa inteiro; o custo de superfície é do produto), o `search_notes` sem teto como fonte de contexto,
a ausência de pré-condição de escrita, e `manage_tags`/`update_frontmatter` como via de escrita no vault
do usuário (é o caminho que produz diff semântico em arquivo alheio).

## 14. Riscos e limites deste relatório

O ensaio usou **notas sintéticas**: nada aqui mede o comportamento sobre um vault real com 20 mil notas,
CRLF misturado, attachments binários e plugins que escrevem no vault enquanto o agente lê. Não rodamos
em Windows (§12). Não medimos o `--exclude` como fronteira de segurança — medimos o contrário: com
`--exclude Projetos/Lia` a busca ficou vazia, mas `read_note` **direto no excluído continuou funcionando**
(cenário `D_exclusao`), exatamente como o `--help` documenta. **`--exclude` é discrição, não controle de
acesso**, e a recomendação da base não pode tratá-lo como isolamento.

## 15. Como isto se liga à base

Alimenta `LR-CMP-006` (`comparisons/MD-NOTES-INTEGRATION.md`) com o candidato leve da comparação e com
a lista de tetos/defesas que a Lia tem que ter; confirma por medição a regra de `LR-AGENT-007`
("léxico antes de vetor") — o único objeto com ★1.733 que resolve o problema sem banco vetorial **e**
tem testes; e dá a `LR-LIC-005` mais um caso de "Apache sem `NOTICE`, criar se redistribuir". Não
contradiz nenhum relatório anterior. Não reabre a auditoria de fornecedores: é um objeto novo, pedido
explícito desta rodada.

## 16. Evidências

| # | Afirmação | Rótulo | Como reproduzir |
|---|---|---|---|
| E1 | 446 testes passando em 14 arquivos, vitest 5.1.0 | **TESTED** | `git clone --filter=blob:none https://github.com/bitbonsai/mcpvault && cd mcpvault && npm i && npm test` |
| E2 | 18 ferramentas; 11 com `--read-only` | **TESTED** | ensaio 1, `tools/list` nos cenários `A` e `C` |
| E3 | `patch_note` recusa ambiguidade (90 ocorrências) | **TESTED** | ensaio 2, `P1`/`P2` |
| E4 | `read_note` de 2 MB devolve 1.950.034 B; `write_note` de 3 MB passa | **TESTED** | ensaio 2, `S4`/`W3` |
| E5 | busca em 3.001 notas = 406 ms; `stats` = 147 ms | **TESTED** | ensaio 2, `S1`/`S3` |
| E6 | `node_modules` aninhado e `.trash` fora da busca; `.png`/`.json` recusados; symlink para fora recusado; `../` recusado | **TESTED** | ensaio 1, `A_leitura` 08/09/14/15/16/17/18 |
| E7 | `.obsidian-desktop` (config renomeada) **também** recusado | **TESTED** | ensaio 4 |
| E8 | frontmatter: comentário e ordem sobrevivem; fluxo re-emitido (`[lia]`→`[ lia ]`); corpo intacto | **TESTED** | ensaio 3, diff ANTES/DEPOIS |
| E9 | escrita é last-writer-wins (sem pré-condição) | **TESTED** | ensaio 2, `W1` sobre `notas/n0002.md` existente |
| E10 | zero chamadas de rede em `src/`+`dist/` | **TESTED (grep)** | `grep -rnE "fetch\(|https?\.request|WebSocket|axios\|XMLHttpRequest" src dist` |
| E11 | `--exclude` não bloqueia leitura direta | **TESTED** | ensaio 1, `D_exclusao` 03 |
| E12 | ★1.733, 23 issues, npm 0.18.4, `engines.node >=22.12.0`, `unpackedSize` 172.093 B, 4 deps | **CONFIRMED (API/registry, 2026-11-26)** | `gh api repos/bitbonsai/mcpvault`; `curl registry.npmjs.org/@bitbonsai/mcpvault` |
| E13 | issues #273/#274/#281/#283/#287/#288/#289/#290/#166/#167/#221 | **REPORTED** (títulos lidos na API; não reproduzimos) | `gh api repos/bitbonsai/mcpvault/issues?state=open` |
| E14 | `LICENSE` MIT 1.071 B; SDK Apache-2.0 12.227 B sem `NOTICE`; `gray-matter` MIT, `yaml` ISC, `trash` MIT | **CONFIRMED (arquivos lidos)** | `wc -c`; `package.json` de cada dependência |
| E15 | comportamento em Windows com vault em raiz de unidade | **NOT RUN** | sem Windows neste ambiente |
| E16 | vault real do usuário (20 mil notas, CRLF, plugins escrevendo) | **NOT RUN** | não usamos dados do usuário |
