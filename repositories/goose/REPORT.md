# goose — o agente Rust que governa por issue no quadro, e que decidiu **não** manter diretório próprio de servidores MCP

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-015` |
| Nome | `aaif-goose/goose` — framework de agente em Rust com CLI e desktop Electron; "install, execute, edit, and test with any LLM" |
| Tipo | repositório (produto + framework) |
| Fonte oficial | https://github.com/aaif-goose/goose · docs `goose-docs.ai` |
| Responsável | org `aaif-goose` (nome exibido "goose", criada 2026-03-25, blog goose-docs.ai, 7 repositórios). **`block/goose` é o mesmo repositório**: os dois endpoints devolvem `id=846698999` — é migração de dono, não bifurcação |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED |
| Recomendação | **ADAPT** — sugestão ao dono: o gate de contribuição ("só issue **Ready** vira PR, e o PR explica como o plano de verificação foi executado") e a decisão de delegar descoberta de servidores MCP ao registro oficial |
| Decisão de adoção | — nenhuma registrada |
| Categoria | runtime de agente + governança de contribuição + diretório MCP |
| Projetos beneficiados | Lia Forge (fluxo de contribuição e release), Lia Agent Hub (política de descoberta de MCP), Research (registro de decisão por issue) |
| Versão analisada | `main` no HEAD de 2026-11-25 (o `pushed_at` da API é o mesmo minuto da coleta) · criado em 2024-08-23 |
| Proveniência do conteúdo | medido por nós (`gh api` + clone com filtro de blob + leitura de `AGENTS.md`, da árvore e do `SKILL.md`); nada veio de post de terceiros |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api repos/aaif-goose/goose` + `git/trees/HEAD?recursive=1` (`truncated: false`) + `search/commits` |
| Upstream conferido | 56.994 ★ · 523 issues abertas · **3.130 entradas / 2.618 blobs / 366.028.698 B de árvore** · 641 `.rs`, 363 `.md`, 346 `.tsx`, 272 `.ts` · **39 workflows** · **254 commits nos últimos 30 dias** · contributor nº 1 = `dependabot[bot]` (376 contribuições) |
| Próxima revisão | 2026-12-09 |
| Licença | **Apache-2.0** — `LICENSE` único na raiz; nenhum `NOTICE` na árvore; nenhuma licença aninhada (medido no censo de 3.130 entradas) |
| Confiança | Alta na estrutura e na governança (arquivos lidos); **zero** no comportamento — zero execução: não há `cargo`/`rustc` neste sandbox e nada foi compilado; o que foi medido em execução aqui é o censo de árvore, o censo de frontmatter e os dois gates do `LR-CMP-004` aplicados ao corpus onde o goose entra só como contagem |

---

## 1. Por que este objeto entrou

O dono mandou o link de um repositório cujo dono **mudou de nome**: o URL aponta para `aaif-goose`, e a
empresa que criou o projeto (Block) ainda existe no GitHub com 147 repositórios públicos. Identificar isso
veio antes de qualquer julgamento sobre "seria um fork?". Não é: `block/goose` e `aaif-goose/goose` são o
mesmo `id` numérico, então a API confirma transferência de posse, não cópia.

## 2. O que é, medido na árvore

Framework de agente em Rust (641 arquivos `.rs`) com front-end desktop em Electron/React (346 `.tsx`,
272 `.ts`), 39 workflows de CI e uma árvore de 366 MB — a maior desta leva de 16 links. Não tem `NOTICE`,
tem um `SKILL.md` (em `evals/harbor/.agents/skills/compare-tasks/`) e dois `AGENTS.md`.

## 3. O achado de governança: o `AGENTS.md` como contrato de contribuição

257 linhas? Não — o `AGENTS.md` do goose é curto e inteiro operacional. As regras, na ordem em que estão
no arquivo:

- **"The issue is the source of truth for work intended for an upstream pull request."** O quadro
  (`github.com/orgs/aaif-goose/projects/1`) é o estado canônico.
- antes de implementar, confirmar que a issue está com Status **Ready**; **não** implementar issues em
  **Inbox**, **Needs info** ou **Accepted / design** — nesses estados a tarefa é resolver a discussão;
- ler design acordado, restrições e **não-objetivos** antes de tocar no código; manter a implementação
  dentro do escopo da issue; se a implementação revelar mudança material de design, **voltar à issue**;
- **todo PR externo precisa linkar a issue Ready que implementa e explicar como o plano de verificação foi
  executado**;
- exceções nomeadas explicitamente: trabalho dirigido por mantenedor, correção de segurança urgente,
  automação de release e mudanças locais/exploratórias não exigem issue Ready.

Duas coisas que a nossa base faz e que aqui têm forma mais dura: (i) nós registramos decisão em
`decisions/`, mas não **bloqueamos** trabalho por estado de issue; (ii) nós escrevemos "o que não
verifiquei" no fim do relatório — eles exigem "explique como o plano de verificação foi executado" como
condição de entrada do PR. A segunda é estritamente mais forte, e é texto de `AGENTS.md`, não código.

## 4. O achado de ecossistema: eles estão **desmontando** o diretório próprio de servidores MCP

Trecho do `AGENTS.md`, seção "MCP Server Directory": o projeto **aposenta** seu diretório de servidores
específico do projeto em favor do **registro oficial do MCP** (`github.com/modelcontextprotocol/registry`)
e do formato `server.json`. Consequências escritas para o agente: não adicionar servidores novos em
`documentation/static/servers.json` (contribuições assim não são mais aceitas); encaminhar autores ao
registro; tratar o diretório existente como **dados legados** enquanto descoberta e instalação via registro
são implementadas. Citam a Discussion #10830 como sede da decisão.

Isto é evidência externa de alta qualidade para `DR-0011` (modelo de registro de servidor MCP no Hub) e
`DR-0012` (política de instalação): um projeto de 57 mil estrelas decidiu que **curadoria local de
servidores MCP é passivo, não ativo** — e o `server.json` do open-seo (`LR-FORGE-017`, que aponta para o
schema `2025-12-11` do mesmo registro) ia na mesma direção. A pergunta que sobra para o dono do Hub deixa
de ser "qual diretório usamos" e passa a ser "consumimos o registro oficial, e o que fazemos com entradas
que só existem em diretórios de projeto".

## 5. Escrita para humano, não log de trabalho

Seção "GitHub Communication": comentários de issue/PR são para humanos; começar pela conclusão ou pela ação
necessária; não repetir contexto já presente no fio; um resumo claro em vez de comentários incrementais. É
a mesma política que a `DR-0019` me deu para o resumo de rodada — com a diferença de que a deles vale para
*todo* comentário público, e a minha só para o fechamento de rodada.

## 6. Ambiente, medido: por que a execução é `BLOCKED` e não `NOT_RUN`

O `AGENTS.md` manda `source bin/activate-hermit` e `cargo build` — isto é, o toolchain vem do **hermit**
(pacote por arquivo de pin, baixado no primeiro uso) e o build é Rust. Este sandbox não tem `cargo` nem
`rustc` (medido em rodadas anteriores com o mesmo resultado, e a ausência persiste) e o hermit baixaria
toolchain de host fora da allowlist. Logo: `BLOCKED` com causa medida, não escolha de escopo. O que **pude**
fazer aqui: ler `AGENTS.md`, censar a árvore, passar o único `SKILL.md` pelos dois gates do
`LR-CMP-004` — o pacote foi **censado** (1 `SKILL.md`, 98 B, frontmatter parseável) mas **não entrou no conjunto de 173 pacotes materializados** para os dois gates, porque o diretório `evals/harbor/` ficou fora dos padrões de sparse-checkout; registro a ausência em vez de arredondar.

## 7. Rastreabilidade de contribuição: um dado que engana

O `contributors` da API coloca **`dependabot[bot]` como maior contribuidor (376)**. Qualquer afirmação tipo
"projeto com N contribuidores, o principal é X" sai errada se a lista não for filtrada por bot. Registro
aqui porque a nossa base cita contributor counts em dossiês: o `search/commits` que usei para os 254 commits
em 30 dias é imune a isso, o `contributors` não é.

## 8. Onde isto poderia se aplicar (a viabilidade é do dono)

> **Escopo desta seção** — sugestão do que a evidência sustenta, mais a pergunta de viabilidade; não é
> instrução para nenhum app (`MISSION.md` §3, `DR-0019` §5).

| App | O que sugiro considerar | O que custaria no app |
|---|---|---|
| Lia Forge | o gate "só issue Ready vira PR; PR externa linka a issue e diz como verificou" — é texto de `AGENTS.md`, com as exceções nomeadas | escrever a política; nada de código |
| Lia Agent Hub | sair de diretório próprio de servidores MCP e consumir o registro oficial + `server.json`, tratando o que já existe como legado | depende de quanto do catálogo atual do Hub é descoberta vs registro; é a pergunta do `DR-0011` |
| Research (esta base) | exigir "como o plano de verificação foi executado" no resumo de rodada, não só a lista de não verificado | zero: é uma linha a mais no formato de 9 itens |

## 9. O que não verifiquei, e por quê

- nada de comportamento: sem `cargo` não buildo, não rodo o CLI, não rodo o desktop, não valido os 39
  workflows fora do texto (não li um por um — 39 é contagem de árvore, não leitura);
- não li o `evals/harbor/` inteiro, só o `SKILL.md` de comparação de runs; o que "harbor" mede, com que
  benchmarks e com que modelos, não verifiquei (o arquivo cita runs como `sonnet46-full`, `pi-sonnet46-full`
  — nomes de configuração, não resultados);
- os 2 `AGENTS.md` foram lidos só na raiz; o segundo (em subdiretório) não foi aberto;
- não conferi se a migração para o registro oficial está implementada ou só declarada;
- contagem total de contribuidores permanece não medida (o `-i` da API não devolve `Link` — mesma
  limitação registrada em `LR-FORGE-016`).

## 10. Recomendação: **ADAPT**

`ADAPT` no sentido estreito: não é "usar goose", é "duas práticas deles são melhores que as nossas
equivalentes e não custam código". O runtime em Rust em si não tem caso de uso na Lia medido por esta base,
e o `AGPL`/`Apache` não é obstáculo (Apache-2.0, sem `NOTICE`), mas também não há por que adotar: o que
vale é a política.

**Propor** ao dono, sem aplicar: (i) levar o gate de issue-Ready para o `agents/PUBLISHING-PROTOCOL.md`
desta base e propor o mesmo ao Forge; (ii) registrar em `cross-project/mcp/` que um projeto deste porte
aposentou o diretório próprio em favor do registro oficial — é insumo direto para `DR-0011`/`DR-0012`;
(iii) proibir na nossa escrita de pesquisa a frase "maior contribuidor" sem filtrar bot.

## 11. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| `block/goose` e `aaif-goose/goose` são o mesmo repositório | `OBSERVED` | `gh api repos/block/goose` devolve `full_name: aaif-goose/goose`, `id 846698999`, igual ao endpoint direto |
| org `aaif-goose` criada 2026-03-25, nome "goose", 7 repositórios | `OBSERVED` | `gh api orgs/aaif-goose` |
| 3.130 entradas / 2.618 blobs / 366.028.698 B; 641 `.rs`; 39 workflows; 0 `NOTICE` | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio |
| gate de issue Ready; PR externa linka issue e explica verificação; exceções nomeadas | `OBSERVED` (texto) | `AGENTS.md` lido na íntegra no clone com filtro de blob |
| aposentadoria do diretório MCP em favor do registro oficial | `DOCUMENTED` (declaração lida; implementação não verificada) | `AGENTS.md` §"MCP Server Directory" + Discussion #10830 citada |
| 254 commits em 30 dias; `dependabot[bot]` como maior contribuidor | `OBSERVED` | `search/commits?q=repo:…+committer-date:>2026-10-25` (254) e `contributors?per_page=1&anon=true` |
| compila, roda e escala | `BLOCKED` | sem `cargo`/`rustc` no sandbox; hermit baixaria toolchain de host fora da allowlist |
| qualidade do runtime como substituto de qualquer coisa da Lia | `NOT_RUN` | não medido; exigiria rodar o agente contra modelos reais com custo |
