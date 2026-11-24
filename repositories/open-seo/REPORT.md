# open-seo (EveryApp) — o único objeto desta leva em que rodei a suíte inteira: 299 arquivos, 2.130 testes, 0 falha

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-017` |
| Nome | `every-app/open-seo` (OpenSEO) — alternativa open source ao Semrush/Ahrefs, com servidor MCP e 12 Skills |
| Tipo | repositório |
| Fonte oficial | https://github.com/every-app/open-seo · site `openseo.so` |
| Responsável | Ben Senescu (`bensenescu`); empresa EveryApp; licença `Copyright (c) 2026 Ben Senescu` |
| Estado da pesquisa | TESTED |
| Resultado de execução | LOCAL_TESTS_PASS |
| Recomendação | **ADAPT** — transportar o `sync-plugin-skills.mjs` com checagem de deriva na CI, o par "protocolo × consumidor" da Skill `verify-local-mcp`, e a política de publicação de Skills (12 públicas de 28) |
| Decisão de adoção | — nenhuma registrada |
| Categoria | produto concorrente + engenharia de Skills/MCP |
| Projetos beneficiados | Lia Project (Skills + MCP), Lia Forge (CI enxuta, release automatizada, `ci:check` de deriva), Lia Agent Hub (frontmatter e publicação seletiva de Skills), Lia Studio (espelho de pacotes que não é symlink) |
| Versão analisada | `v0.1.32` (release 2026-11-23) · HEAD do clone `6f68494` · criado em 2026-02-27 |
| Proveniência do conteúdo | **medido por nós**: clone raso + execução das checagens do próprio repositório no sandbox; nenhuma afirmação tirada de blog post |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · `gh api repos/every-app/open-seo` + `git/trees/HEAD?recursive=1` (`truncated: false`) + clone `--depth 1` |
| Upstream conferido | 2026-11-24 · 2.504 blobs em 2.837 entradas de árvore; 2.489 arquivos no working tree do clone (66 MB com `.git`) |
| Próxima revisão | 2027-02-24 |
| Licença | **MIT** — `LICENSE` lido na raiz: "MIT License Copyright (c) 2026 Ben Senescu"; nenhuma outra licença em subdiretório (nenhum `ee/`, nenhum `LICENSE` adicional na árvore) |
| Confiança | Alta: os números de teste vêm de execução nesta máquina; as afirmações sobre o serviço hospedado são do README deles e estão marcadas como tal |

---

## 1. Por que este objeto entrou na base

O dono mandou o link numa leva de oito. Dos oito, este é o **único** em que eu pude executar a
verificação completa do próprio projeto — TypeScript + pnpm é o que este sandbox tem (medido: `node
v22.22.3`, `npm 10.9.8`; `cargo`, `go`, `ruby`, `flutter`, `docker` ausentes). Então ele entrou como
objeto *testado*, e serve de régua para os outros sete, que ficaram em leitura estática.

Interesse prático além da régua: é um projeto de **9 meses** (criado 2026-02-27), 41 MB de árvore,
seis workflows, MIT, 28.739 estrelas, 59 issues abertas, que entrega a mesma coisa que o Lia Project
pretende entregar para um domínio diferente: **uma ferramenta web + um servidor MCP + um conjunto de
Skills instaláveis em três lojas de agentes**.

## 2. O que é (medido no repositório, não no marketing)

Do README (texto lido): "Open source alternative to Semrush and Ahrefs", "SEO tool for the people",
"pay-as-you-go alternative", "Bring your own DataForSEO API key and pay only for what you use",
"hosted subscription is $10/month", "Fork and vibe code your own custom tool".

Pilha medida em `package.json`: 54 dependências · 34 devDependencies · `packageManager:
pnpm@10.30.1` · **58 scripts** · Vite 8.3.4 + Vitest 5.0.4 + `@playwright/test` + `oxlint 1.50.0` com
`oxlint-tsgolint` (lint type-aware) + `wrangler 4.151.0` + Drizzle ORM com **duas** famílias de
migração (`drizzle/sqlite.config.ts` para Cloudflare D1 e `drizzle/pg.config.ts` para Postgres) +
TanStack Start/Router/Query/Form/Table + AI SDK (`ai`, `@ai-sdk/react`, `@openrouter/ai-sdk-provider`)
+ `disposable-email-domains-js`. Deploy-alvo: Cloudflare Workers (`wrangler.jsonc`,
`wrangler.standalone.json`, `cloudflare.config.ts`) **e** Docker (`compose.yaml`), com
`build:standalone` empacotado por um script próprio em `scripts/celld/`.

Números do objeto (medidos na API em 2026-11-24): 28.739★ · 4.077 forks · 59 issues abertas · TypeScript
94,1 % · `size` 41.301 KB · 6 workflows · release mais recente `v0.1.32` (2026-11-23).

## 3. O que eu executei aqui, e o que saiu

Ambiente: sandbox Linux, Debian, `python3` 3.11.2, `node` v22.22.3; `pnpm` instalado pelo npm global
nesta sessão; diretório temporário `/tmp/r19/os`, fora da base Lia; nenhum arquivo do projeto Lia foi
tocado; `pnpm install --ignore-scripts` (sem scripts de postinstalação) levou 24 s e resolveu sem erro.

| Comando (do próprio repositório) | Resultado |
|---|---|
| `pnpm run test:ci` (`vitest run --reporter=dot`) | **299 arquivos de teste passaram · 2.130 testes passaram** · 132,00 s · exit 0 |
| `pnpm run types:check` (`tsc --noEmit`) | sem saída, exit 0 |
| `pnpm run lint` (`oxlint . --type-aware`) | "Found 0 warnings and 0 errors. Finished in 17.6s on 1514 files with 184 rules using 2 threads", exit 0 |

Um registro metodológico, porque quase me enganou: na primeira vez, o `lint` *pareceu* falhar
(`ELIFECYCLE Command failed`) — era o pipe para `tail` fechando a saída cedo. Reexecutado com saída em
arquivo: exit 0. Lição que vale para a casa: **um sinal de falha atravessando pipe não é resultado de
teste**; só conto o exit code coletado sem pipe, como está na tabela acima.

Durante a suíte, um teste imprime um `502` num caminho de API de terceiros e um erro de leitura de R2
tratado como "cache miss" — o que indica que há testes que exercitam caminhos de falha de provedor;
se chamam a rede de verdade ou se é fetch mockado, **não verifiquei** (§10).

## 4. O achado principal: Skills como arquivo versionado, com teste de deriva

O repositório tem **28 Skills** em os 28 arquivos `.agents/skills/*/SKILL.md`. Dessas, **12** são copiadas para
`plugins/openseo/skills/` por um script de 39 linhas cujo comentário de abertura diz tudo:

> "Codex plugin installs copy the plugin directory and skip symlinks, so plugins/openseo/skills/* must
> be real files, not symlinks to .agents/skills/*. Run this after editing any of the skills listed
> below. `pnpm ci:check` runs this and diffs the result, so a stale copy fails CI instead of shipping."

E o `ci:check` (medido no `package.json`, literal): `prettier --check . && knip && tsc --noEmit && tsc
--noEmit -p tests/badseo/tsconfig.json && tsc --noEmit -p tsconfig.report-widgets.json && oxlint .
--type-aware && pnpm sync-plugin-skills && test -z "$(git status --porcelain -- plugins/openseo/skills)"`.

Medi as duas árvores: as 12 cópias existem e são **byte-idênticas** aos originais (comparei
`keyword-research/SKILL.md` com `diff -q` → idênticas). E as **16 restantes** estão só em
`.agents/skills/`, das quais **15 declaram `metadata: internal: true`** no frontmatter.

É, literalmente, a resposta ao problema que o `LR-STUDIO-012` encontrou do outro lado: um pacote de
Skills publicado como *cópia de arquivos* sem verificador de deriva, com conteúdo vendorizado sem
NOTICE. Aqui o espelho é gerado por script, a lista do que é público é um array no código, e a CI
falha se alguém editar o original sem regerar a cópia. Confirmei também que **uma** Skill interna
(`simple-issue-description`) está fora do espelho mas **sem** a flag `internal: true` — a convenção
delas tem uma exceção de um item; ou seja, o que garante a fronteira é o array do script, não o
metadado. Registro isso porque é exatamente o tipo de detalhe que se perde quando se cita o projeto
pelo enunciado do README.

## 5. Formato de SKILL.md (o contraste com o nosso conjunto operacional)

- frontmatter das 12 públicas: `name` e `description`, nada mais;
- `competitive-landscape` tem uma chave extra `Answer:` no frontmatter — a forma não é uniforme no
  próprio repo (medido: 1 de 28 com chave fora de `name`/`description`);
- as internas carregam `metadata.internal` (15 de 28);
- a Skill mais interessante é interna: `verify-local-mcp`, que define **duas camadas de verificação**
  e nomeia os bugs que cada uma pegou: "protocol testing found DataForSEO quirks (zoom-dependent empty
  SERPs), the consumer probe found ergonomics failures (9KB provider rows overflowing client token
  budgets, fractional inputs rejected upstream with raw provider errors). Do both."

A segunda camada — um *agente que nunca viu o código* tentando usar as ferramentas, medindo
descrições, schemas, tamanho de saída, erros e fluxos assíncronos — é o teste que falta no nosso
`agents/SKILLS-OPERATING-SET.md` (48 registros). Não é um teste de contrato, é um teste de usabilidade
do contrato, com orçamento de tokens como critério.

## 6. Empacotamento para três lojas a partir de uma fonte

`plugins/openseo/` contém `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.mcp.json`,
`README.md`, `assets/` e `skills/`. Na raiz, `server.json` é o registro MCP:

> `"$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"`,
> `"name": "com.everyapp/openseo"`, `"description": "Keyword research, site audits, rank tracking and
> AI visibility for your AI agent."`, `"remotes": [{ "type": "streamable-http", … }]`

**Achado medido**: `server.json` declara `"version": "0.1.27"` enquanto `package.json` e a release
pública estão em `0.1.32` — cinco versões de atraso no manifesto do registro MCP. A CI deles cobre
deriva de *Skills* (item 4) e tipos, mas não cobre deriva de *versão entre manifestos*. É o tipo de
achado que só aparece quando se lê os dois arquivos no mesmo minuto, e é o tipo de checagem que o
`tools/validate.py` desta casa faz por design (contagem, catálogo, licenças).

## 7. A fronteira público × staging, e o arquivo de retificação

`package.json` → `"deploy:prod": "gh workflow run deploy-production.yml --repo bensenescu/open-seo
--ref main"` (idem `deploy:web`). Ou seja: o gatilho de produção mira **outro repositório**.
Medi `gh api repos/bensenescu/open-seo` → **HTTP 404** (privado ou inexistente para leitura anônima),
então o que existe na conta pública é o espelho, não a fonte.

E o repositório público tem um arquivo chamado `retroactive-contributions.md` que começa assim:

> "These people sent fixes to the public repo that shipped through our private staging repo without
> their name on the commit. Each entry links their PR to the commit that shipped it."

Com uma tabela `| Contributor | Their PR |`. O README, na seção Contributing, pede: "Creating clear
issues is the best way to contribute."

Duas coisas para a Lia researcharem como política, não como fofoca: (a) fluxo `public issue → staging
privado → commit autor` **apaga autoria**, e isso é um risco de proveniência para *qualquer* base que
consume esse projeto — a licença é MIT, mas a cadeia de autoria não está no arquivo que se baixa; (b)
eles publicaram a retificação. É o mesmo movimento do nosso §13 do `LR-STUDIO-012` (retratação
visível), feito pelo fornecedor, antes de ser pego por fora. Para `lia-multiplatform` e para o
`data/inventory/`, a regra prática é: se `deploy:*` aponta para outro repo, o que se audita é o
repositório que produz o binário, não o que aparece no Google.

## 8. Segurança e operação do lado do self-host (medido nos arquivos)

- `.env.example` com **466 linhas / 165 variáveis** é o número do `cal.diy` (outro objeto); aqui a
  superfície de config é menor — não medi arquivo por arquivo nesta passada;
- `docs/` cobre `DATAFORSEO_API_KEY.md`, `GOOGLE_MAPS_SETUP.md`, `LOCAL_DEVELOPMENT.md`,
  `LOCAL_POSTGRES.md`, `SELF_HOSTING_CLOUDFLARE.md` (+ `_LEGACY` + `_OPERATIONS`),
  `SELF_HOSTING_DOCKER.md` (+ `_LEGACY`), `SELF_HOSTING_GOOGLE_ANALYTICS.md`,
  `SELF_HOSTING_GOOGLE_SEARCH_CONSOLE.md` — três variantes de self-host e a marca de LEGACY nas
  antigas;
- `docs/maintainers/` guarda `FREE_TOOLS_PROTECTION.md`, `account-deletion.md`,
  `billing-lifecycle-emails.md`, `SITE_AUDIT_RENDERING.md`, `every-app.md` e `every-app-learnings.md`,
  cujo cabeçalho é literalmente "Things to add to EveryApp skill files later" com itens como "db.batch()
  is required for multi-row inserts — D1 has a 100 bind param limit per statement". Um *caderno de
  limitações* que alimenta as Skills por fora do código — padrão que a nossa base deveria copiar
  (§11);
- há `.oss-scanner/` na raiz (mesmo bloco que `opf/openproject` e `OpenWhispr/openwhispr` têm: scanner
  + `threat_model.md`), `SECURITY.md`, `.oxlintrc.json`, `.gitattributes`, `.npmrc`, e a Suíte de
  `tests/badseo/` como **subprojeto próprio** (com `package.json`, `pnpm-workspace.yaml`,
  `vite.config.ts`, `wrangler.jsonc`) que o `ci:check` type-checa separadamente — um corpus de
  "código ruim" mantido vivo dentro do repo.

## 9. Comparação com os outros sete da mesma leva (o que só o open-seo tem)

| Objeto | Testes executados aqui? | Tamanho da árvore | Licença | Nota |
|---|---|---|---|---|
| `open-seo` | **sim — 2.130 testes, 0 falha** | 2.504 blobs | MIT | único 100 % rodável neste sandbox |
| `appflowy-ai-plugins` | sim — o verificador deles (`check.py`) → `ok` | 37 arquivos | AGPL-3.0-only | `LR-MCP-004` |
| `opf/openproject-agent-skills` | não (sem runtime de agente aqui) | 12 arquivos | MIT | `LR-FORGE-016` |
| `debpalash/VoiceStudio` | **parcial** — 20 passed, 1 skipped nos testes de pin | `size` 219.996 KB | AGPL-3.0-only | `LR-VOICE-003` |
| `opf/openproject` | não (sem Ruby) | 27.141 blobs | GPL-3.0 | `LR-FORGE-016` |
| `capsoftware/cap` | não (sem Rust) | 6.154 blobs | MIT só para crates de câmera | `LR-FORGE-018` |
| `chatwoot/chatwoot` | não (sem Ruby) | 10.117 blobs | MIT + `enterprise/` | `LR-SEC-009` |
| `calcom/cal.diy` | não (1,16 GB de árvore; sem tempo/rede) | 7.712 blobs | MIT | `LR-FORGE-019` |

## 10. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| `pnpm build` completo (Vite + `tsc` + report-widgets) | `NOT_RUN` | o `test:ci` + `types:check` + `lint` cobrem o que a pergunta pedia; build de Worker não altera a conclusão sobre Skills/licença |
| Rodar o servidor MCP contra DataForSEO real | `BLOCKED` | exige chave de API paga; nenhuma conta criada, nenhuma chamada faturável |
| Se os testes fazem chamadas de rede | `UNVALIDATED` | vi `502` e mensagens de provedor em stderr, sem auditar o mock |
| O serviço hospedado (`openseo.so`, US$ 10/mês) | `NOT_RUN` | fora do escopo; nada foi assinado nem testado com conta |
| `bensenescu/open-seo` | `BLOCKED` | 404 anônimo; não vou tentar acessar repo privado de terceiro |
| Os 46 arquivos de migração em `drizzle/`, o `tests/badseo` a fundo, os `plugins/*/README` | `NOT_RUN` | leitura seletiva; o que cito foi o que li |
| Autoria real dos commits (quem escreveu o quê) | `UNVALIDATED` | clone raso de 1 commit; `retroactive-contributions.md` sugere fluxo não óbvio, não prova |

## 11. Recomendação: **ADAPT**

1. **Transportar** o mecanismo de deriva da §4 para o Lia Agent Hub: uma Skill pública = arquivo
   gerado + lista de exportação no código + `test -z "$(git status --porcelain -- <dir>)"` na CI. É
   39 linhas e resolve o modo de falha documentado em `LR-STUDIO-012` e `DR-0004`.
2. **Transportar** a Skill `verify-local-mcp` como modelo de teste de usabilidade de ferramentas para
   qualquer MCP nosso: camada de protocolo + camada de "agente que nunca viu o código", com limite de
   tamanho de saída como critério explícito.
3. **Transportar** a separação de frontmatter: `name` + `description` no que é público, flag `internal`
   no que não é, e **a lista de exportação como fonte de verdade** (o metadado sozinho não garante —
   item medido de §4).
4. **Não levar**: a dependência estrutural de um provedor de dados pago (DataForSEO) — custo por
   chamada é decisão do dono, não da Research, e nenhum objeto desta base autoriza gastar; nem
   Cloudflare D1 como alvo de banco para a Lia (o
   `lia-multiplatform` precisa funcionar offline; o padrão interessante deles é ter *dois* alvos com
   schemas separados, não o alvo específico).
5. **Decisão do dono**: (a) se o Lia Project publica Skills em `.claude-plugin`/`.codex-plugin`/
   `.cursor-plugin` com o mesmo gerador; (b) se uma regra tipo "deploy só a partir do repo público" é
   exigência nossa (a §7 mostra o custo do contrário); (c) se o caderno `docs/maintainers/every-app-
   learnings.md` vira formato na nossa base (eu recomendo — é a diferença entre saber e registrar).

## 12. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| MIT, `Copyright (c) 2026 Ben Senescu`, único LICENSE na árvore | `CONFIRMED` | `LICENSE` lido + `git/trees/HEAD?recursive=1` filtrado por `LICENSE` |
| 28.739★ · 4.077 forks · 59 issues · TS 94,1 % · release v0.1.32 (2026-11-23) · criado 2026-02-27 · 6 workflows · `size` 41.301 KB | `CONFIRMED` | `gh api repos/every-app/open-seo` + `releases/latest` + `contents/.github/workflows` |
| Árvore 2.504 blobs / 2.837 entradas, `truncated: false`; working tree do clone 2.489 arquivos, 66 MB | `CONFIRMED` | API + `du -sh`/`find` no clone `--depth 1` HEAD `6f68494` |
| `pnpm install --ignore-scripts` em 24 s; `test:ci` → 299 arquivos e 2.130 testes passando, exit 0; `tsc --noEmit` limpo; `oxlint --type-aware` 0/0 em 1.514 arquivos com 184 regras | `OBSERVED` | saída coletada em arquivo no sandbox (nível 1, `governance/TESTING-PROTOCOL.md`) |
| 28 Skills em `.agents/skills`, 12 espelhadas em `plugins/openseo/skills`, cópias byte-idênticas (diff -q), 15 com `metadata: internal: true`, `simple-issue-description` sem a flag | `CONFIRMED` | `glob` + leitura de frontmatter no clone |
| `ci:check` contém `pnpm sync-plugin-skills && test -z "$(git status --porcelain -- plugins/openseo/skills)"` | `CONFIRMED` | `package.json` decodificado no clone |
| `server.json` `0.1.27` × `package.json` `0.1.32` | `CONFIRMED` (deriva medida) / `UNVALIDATED` (se é intencional) | leitura dos dois arquivos |
| `deploy:prod`/`deploy:web` disparam workflow em `bensenescu/open-seo`, que responde 404 | `CONFIRMED` | `package.json` + `gh api repos/bensenescu/open-seo` |
| `retroactive-contributions.md` com a frase sobre fixes que entraram pelo staging privado sem o nome do autor | `CONFIRMED` (texto) / `REPORTED` (abrangência) | arquivo lido no clone |
| `docs/maintainers/every-app-learnings.md` com "Things to add to EveryApp skill files later" e limites de D1 | `CONFIRMED` | arquivo lido no clone |
| `tests/badseo/` é subprojeto com workspace próprio, type-checado no `ci:check` | `CONFIRMED` | `ls` + `tsconfig.json` + script |
| Comportamento real do servidor MCP e do app hospedado | `UNVALIDATED` | exigiria chave paga e conta |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · registro de execução:
`data/testing/test-log.tsv` (linha `LR-FORGE-017`) · conjunto de Skills da casa:
`agents/SKILLS-OPERATING-SET.md` · caso de deriva de pacote sem verificador: `LR-STUDIO-012` ·
formato de licença por diretório: `cross-project/licensing/SPLIT-LICENSE-SCAN.md`.
