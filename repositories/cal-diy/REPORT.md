# Cal.diy (calcom) — o fork que removeu o comercial: MIT puro, licença stubada em `return true`, e 50 workflows

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-019` |
| Nome | `calcom/cal.diy` — plataforma de agendamento; fork comunitário do Cal.com com "todo o código enterprise/comercial removido" |
| Tipo | repositório |
| Fonte oficial | https://github.com/calcom/cal.diy — e isto foi medido: `GET repos/calcom/cal.com` responde hoje com o objeto `calcom/cal.diy` (renomeado) |
| Responsável | Cal.com, Inc. detém o copyright (`Copyright (c) 2020-present Cal.com, Inc.` no LICENSE) e a comunidade mantém o fork; o README direciona quem quer comercial para o produto original |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN |
| Recomendação | **ADAPT** — sugestão ao dono: levar o `agents/` como fonte única com symlinks por ferramenta, o `PERMISSIONS.md` mapeando checagem→string, e o `specs/_templates/` |
| Decisão de adoção | — nenhuma registrada |
| Categoria | produto concorrente + fronteira de licença + layout de instruções a agentes |
| Projetos beneficiados | Lia Project (estrutura `agents/`, spec-driven), Lia Agent Hub (symlink × cópia), Lia Forge (50 workflows, 8 ações compostas de cache), `lia-multiplatform` (o que um fork pode e não pode arrancar) |
| Versão analisada | `v6.2.0` (release 2026-03-01) · último push 2026-11-13 · criado 2021-03-22 |
| Proveniência do conteúdo | **medido por nós** (API: árvore recursiva com `truncated: false`, workflows, LICENSE, arquivos de política) — nada executado |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · 50.349★ · 15.741 forks · 214 watchers · TypeScript 95,8 % |
| Upstream conferido | 2026-11-24 · **7.712 blobs** / 10.291 entradas · `size` 1.161.986 KB · 50 workflows · 0 caminhos com `ee/` |
| Próxima revisão | 2027-02-24 |
| Licença | **MIT puro** — `LICENSE` com 21 linhas, **zero** ocorrências de "AGPL"/"Affero" (contado com `grep -ci`), sete `LICENSE` aninhados (todos MIT: `apps/api/v2/src/platform`, `packages/app-store/{hitpay,stripepayment}`, `packages/embeds/{embed-core,embed-react,embed-snippet}`) |
| Confiança | Alta para o censo, árvore e arquivos lidos; nenhuma para o comportamento do app (nada executado — 1,16 GB de árvore e Yarn 4) |

---

## 1. Por que este objeto entrou na base

É o maior repositório da leva em número de workflows e o segundo em tamanho de árvore, e entrou por uma
razão específica: ele é **o experimento natural do "open-core sem open-core"**. O Cal.com original é
open-core; o Cal.diy é o mesmo código com a parte comercial *removida* e a licença do núcleo trocada — e
dá para ver, arquivo por arquivo, o que foi preciso fazer, o que foi feito pela metade, e o que não tem
como ser feito num fork. Nada disso é opinião: está na árvore.

Para a Lia, que está decidindo o que publicar e o que não publicar (`decisions/PENDING/DR-0004-STUDIO-THIRD-PARTY-ZIP.md`
é um caso desse tipo), é o único objeto medido que mostra as duas direções: **o que se ganha** com MIT
puro e **o que se deixa de herdar** quando se corta o commercial layer.

## 2. O objeto medido

| Campo (API, 2026-11-24) | Valor |
|---|---|
| Estrelas / forks / watchers | 50.349 / 15.741 / 214 |
| Criado / último push / release | 2021-03-22 / 2026-11-13 / `v6.2.0` (2026-03-01) |
| Idioma principal | TypeScript 95,8 % |
| `size` / blobs / entradas | 1.161.986 KB / 7.712 / 10.291 |
| Workflows | **50** arquivos em `.github/workflows` |
| Ações compostas próprias | **8** (`cache-checkout`, `yarn-install`, `cache-build-key`, `cache-build`, `cache-db-key`, `cache-db`, `docker-build-and-test`, `yarn-playwright-install`) |
| `.env.example` | **465 linhas**, **165 variáveis** no formato `CHAVE=` (contado por script próprio) + `.env.appStore.example` à parte |
| Org `calcom` | 44 repositórios; **nenhum chamado `cal.com`** (o renomeio é o que faz o `GET repos/calcom/cal.com` cair aqui); `docker` 939★ arquivado, `cal-mcp` 32★ sem licença, `companion` 34★ com push 2026-11-23 |

## 3. A licença, e o que o fork fez com a máquina de chave

Frases do README, literalmente (medidas no arquivo):

- linha 5: "For any commercial and enterprise-ready scheduling infrastructure, use Cal.com, not
  Cal.diy; hosted by us or get invited to on-prem enterprise access here: cal.com/sales";
- linha 41: "the community-driven, fully open-source scheduling platform — a fork of Cal.com with all
  enterprise/commercial code removed";
- linha 43: "Cal.diy is **100% MIT-licensed with no proprietary 'Enterprise Edition' features**";
- linha 48: "**No license key required** — Everything works out of the box";
- linha 49: "The entire codebase is licensed under MIT, no 'Open Core' split".

Confirmação estrutural medida na árvore recursiva: **0** caminhos contendo `ee/`, nenhum `enterprise/`,
nenhum `premium/`. O LICENSE raiz é MIT sem ressalva (21 linhas).

E aqui vem o detalhe que só aparece se você procurar o que sobrou, não o que foi dito. Estes arquivos
continuam na árvore:

- `apps/web/lib/settings/license-key/new/getServerSideProps.tsx`
- `packages/trpc/server/routers/viewer/admin/createSelfHostedLicenseKey.handler.ts` (+ `.schema.ts`)
- `packages/trpc/server/routers/viewer/deploymentSetup/validateLicense.handler.ts` (+ `.schema.ts`)

Abri o `validateLicense.handler.ts`. A classe que valida é esta, no primeiro bloco do arquivo:

> `class LicenseKeyService {`
> `  async checkLicense() { return true; }`
> `  static async validateLicenseKey(_key?: string) { return true; }`
> `}`

com uma exceção adicional logo abaixo: "Skip validation for E2E testing — `if (process.env.NEXT_PUBLIC_IS_E2E === "1")`
→ `valid: true`".

Registro as três leituras possíveis **sem** escolher uma como fato: (a) a UI de chave existe e pergunta a
um serviço que sempre responde `true`; (b) o fork manteve a superfície para não quebrar callers e
migrações; (c) o handler admin de *criar* chave self-hosted continua exposto a quem for admin. O que é
fato medido: **o gate comercial foi neutralizado por stub, não por remoção**. Lição explícita para
qualquer política de "fork limpa o privativo" na Lia: o que define o produto é o que os endpoints ainda
aceitam, e não o que o LICENSE diz. Fica como linha na matriz (§7).

## 4. O layout `agents/` + symlinks — e o conflito com o que o open-seo faz

Medido na raiz: `AGENTS.md`, `CLAUDE.md`, `.claude/{rules,skills,settings.json}`, `.cursor/{rules,skills}`,
`.opencode/skill/…`, `agents/`, `SPEC-WORKFLOW.md`, `specs/`, `docs/`, `PERMISSIONS.md`, `.well-known/`.

A estrutura real é **uma fonte e três vistas**:

- `agents/` contém `README.md`, `commands.md` e `knowledge-base.md` mais dois diretórios, `rules/` e
  `skills/`;
- `.claude/rules`, `.claude/skills`, `.cursor/rules` e `.cursor/skills` são **symlinks** (o listing da API
  responde `type: symlink`, com os alvos `rules → e01395` e `skills → a769d4` idênticos entre as duas
  ferramentas, ou seja: apontam para os mesmos objetos git).

Compare com `LR-FORGE-017` (open-seo), que faz o **contrário**: cópia real gerada por script
(`sync-plugin-skills.mjs`) + checagem de deriva na CI, com o motivo escrito no cabeçalho do script —
"instalações de plugin copiam o diretório e pulam symlinks". Os dois projetos, no mesmo mês, na mesma
plataforma, chegaram a soluções opostas para o mesmo problema; nenhum dos dois está "errado", e a
escolha depende de *qual* instalador se quer suportar. Isso é política de casa e merece decisão, não
imitação — §8.

Dentro de `.opencode/skill/vercel-react-best-practices/` há o padrão de Skill que a nossa casa deveria
copiar no formato (não no conteúdo): `SKILL.md` com frontmatter

> `name`, `description`, `license: MIT`, `metadata: {author: vercel, version: "1.0.0"}`,

corpo dizendo "Contains **45 rules** across 8 categories, prioritized by impact", e um diretório `rules/`
com **exatamente 45 arquivos `.md`** (contado na API) — a afirmação de contagem do corpo bate com a
árvore. Uma Skill = índice + Corpus de regras pequenas, cada uma num arquivo, com o `license:` declarado
no frontmatter porque a regra é de terceiros.

## 5. `PERMISSIONS.md`: o mapa que a nossa lacuna pedia

189 linhas, **11 linhas de tabela** no formato `| team.create | Create teams | packages/trpc/…/create.handler.ts | 55-57 |`, com colunas
*Permission String · Description · File Path · Line*, e as seções: Team Permissions, Event Type
Permissions, Booking Permissions, Organization Permissions, API Key Permissions, MembershipRole Enum,
Entity Permission Level Enum, Resources Used with Entity Permission Functions.

O enunciado do documento é o que importa: "This document maps existing role-based permission checks to
the new **PBAC** (Permission-Based Access Control) system's permission strings in the format
`resource.action`". Traduzindo para a nossa casa: eles trataram a migração de RBAC→PBAC como um
**inventário com linha de código por permission string**, versionado junto do README, e não como nota de
release. É a forma mais barata que medi de documentar permissão — e é diretamente aplicável ao
`cross-project/security/PER-EXECUTION-PERMISSIONS.md`, que hoje tem seis linhas de evidência e nenhuma
tabela "ação → arquivo:linha" no produto.

## 6. A máquina de CI em uma leitura (o que 50 workflows significam)

Categorias medidas pelos nomes (`.github/workflows/`, 50 arquivos):

- **e2e por superfície** (7): `e2e.yml`, `e2e-api-v2.yml`, `e2e-app-store.yml`, `e2e-atoms.yml`,
  `e2e-embed.yml`, `e2e-embed-react.yml`, `e2e-report.yml`;
- **builds por app** (5): `api-v2-production-build.yml`, `atoms-production-build.yml`, `pr.yml`,
  `production-build-without-database.yml`, `run-ci.yml` + o gate agregador `all-checks.yml`;
- **gate de bundle**: `nextjs-bundle-analysis.yml` + `nextjs-bundle-analysis-annotation.yml` (o
  segundo escreve o resultado como *anotação* no PR);
- **gate de segurança**: `security-audit.yml`; **gate de schema**: `check-prisma-migrations.yml`,
  `setup-db.yml`; **gate de tipo**: `check-types.yml`; **gate de i18n**: `i18n.yml` com
  `i18n-unused.config.js` na raiz;
- **cron de produto** (9): `cron-bookingReminder.yml`, `cron-scheduleEmailReminders.yml`,
  `cron-scheduleSMSReminders.yml`, `cron-scheduleWhatsappReminders.yml`, `cron-changeTimeZone.yml`,
  `cron-downgradeUsers.yml`, `cron-checkSmsPrices.yml`, `cron-syncAppMeta.yml`, `cron-webhooks-triggers.yml`
  — a agenda do SaaS **dentro do repositório aberto**, o que é uma maneira de dizer "self-host significa
  isto também";
- **higiene de PR**: `semantic-pull-requests.yml`, `labeler.yml`, `pr-welcome-bot.yml`,
  `on-changes-requested.yml`, `re-draft.yml`, `merge-reports.yml`, `publish-report.yml`,
  `cleanup.yml`, `cleanup-report.yml`, `cache-clean.yml`, `stale-issue` (via `cron-stale-issue.yml`) +
  `.kodiak.toml` (merge queue);
- **release**: `draft-release.yml`, `post-release.yml`, `changesets.yml`, `release-docker.yaml`;
- **monitoramento sintético**: `checkly.config.ts` + `__checks__/` na raiz.

Os cache-* compostos (8 ações próprias) são a resposta deles ao fato de o `yarn.lock` carregar
`overrides`/`resolutions` + 5 patches em `.yarn/patches/` (incluindo `@prisma-client-npm-5.4.2` e dois
de `dayjs`) — a CI tem de ser rápida porque a resolução de dependências é não-trivial por design.

## 7. Linha para a matriz de licenças

Proposta de registro (a matriz tem 15 colunas e é alimentada por `data/inventory/license-matrix.tsv`;
escrevo o que medi, não a interpretação): objeto `LR-FORGE-019` · licença **MIT (nenhum `ee/`, nenhum
`enterprise/`)** · uso permitido **inclusive comercial** · ressalva a registrar: **a superfície de
validação de chave de licença continua presente, com o serviço stubado em `return true`**, o que
significa que "sem dependência comercial" é fato do *licenciamento*, não do *código*.

## 8. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Rodar `yarn install` / os testes / Playwright | `NOT_RUN` | árvore de 1,16 MB com Yarn 4 + Prisma + Postgres + Docker; nada disso está disponível no sandbox (medido: sem `docker`), e a pergunta do dono não pedia execução |
| O que `createSelfHostedLicenseKey.handler.ts` faz de fato (quem pode chamar, o que grava) | `NOT_RUN` | li só o `validateLicense.handler.ts`; o par admin × deploymentSetup é a linha que fecha a §3 e não foi lida |
| Se há chamadas remotas de validação de chave restantes | `UNVALIDATED` | não busquei `fetch`/`axios` para `cal.com` na árvore |
| Os 44 repositórios do org `calcom`, um a um | `NOT_RUN` | censo do org inteiro não foi pedido; medi o total e três casos extremos |
| Conteúdo de `docs/` e dos arquivos dentro de `agents/` (`README.md`, `commands.md`, `knowledge-base.md`) e de `specs/` | `NOT_RUN` | nomes medidos; leitura própria da próxima passada (é nível 1 e é o que a §4 precisa para virar recomendação de layout) |
| Autoria dos commits do fork vs upstream | `UNVALIDATED` | não medi histórico (clone não feito) |
| Cobertura real de `security-audit.yml` (o que ele roda) | `NOT_RUN` | workflow não aberta nesta passada |

## 9. Recomendação: **ADAPT** (três sugestões, todas baratas — viabilidade por conta do dono)

> **Escopo desta seção** — o que segue é recomendação técnica desta base, não instrução para nenhum app. Se vale, cabe e é possível implementar em cada projeto é decisão do dono (`MISSION.md` §3: o Research não aprova nada).

1. **Layout `agents/` + symlinks**: *sugiro* adotar *uma* fonte (`agents/{rules,skills}`) com vistas por
   ferramenta, **mas só se** o nosso caminho de distribuição aceitar symlinks; senão, o modelo
   cópia + deriva do `LR-FORGE-017` é o indicado. Registrar a escolha como decisão (é a linha 1 da §4).
2. **`PERMISSIONS.md` no formato `recurso.ação` com coluna `arquivo:linha`** para qualquer matriz de
   permissão do Lia Project — é o complemento direto do que falta em
   `cross-project/security/PER-EXECUTION-PERMISSIONS.md`.
3. **`specs/_templates/`**: o diretório de templates (`design.md`, `decisions.md`, `implementation.md`,
   `future-work.md`, `prompts.md`, `AGENTS.md`, `CLAUDE.md`, `docs/README.md`) + o `SPEC-WORKFLOW.md`
   declarando que o fluxo é **opt-in** ("Use it when explicitly requested by saying 'use spec-driven
   development'") — um modelo para `templates/` desta casa sem impor o fluxo a todo mundo.
4. **Contagem verificável em documento**: a Skill deles diz 45 regras e o diretório tem 45 arquivos. Nossa
   versão disso: qualquer digest que afirme "N objetos" deveria ser checado por `tools/validate.py` — é o
   que `check_counts` já faz para README/índice, e faltou para o corpo dos dossiês.
5. **Decisão do dono**: (a) symlink ou cópia-gerada; (b) se a ressalva da §7 entra como aviso para todo
   projeto consumido "comercial-neutro"; (c) se a casa adota spec-driven opt-in (e o `agents/` deles como
   base do nosso `agents/`, que hoje é processo interno da Research, não instruções para escrever código).

## 10. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| 50.349★ · 15.741 forks · 214 watchers · TS 95,8 % · `v6.2.0` (2026-03-01) · push 2026-11-13 · criado 2021-03-22 | `CONFIRMED` | `gh api repos/calcom/cal.diy` + `releases/latest` + `languages` |
| `GET repos/calcom/cal.com` responde com o objeto `calcom/cal.diy` (renomeio) e não há repo `cal.com` no org (44 repos) | `CONFIRMED` | API do GitHub, mesma coleta |
| 7.712 blobs / 10.291 entradas, `truncated: false`; 50 workflows; 8 ações compostas; 0 caminhos com `ee/` | `CONFIRMED` | `git/trees/HEAD?recursive=1` + `contents/.github/workflows` + filtro próprio |
| LICENSE raiz = MIT em 21 linhas, **zero** ocorrências de AGPL/Affero; 7 LICENSE aninhados, todos MIT | `CONFIRMED` | arquivos decodificados + `grep -ci` |
| README: "100% MIT-licensed", "all enterprise/commercial code removed", "No license key required", "no 'Open Core' split", e o empurrão para Cal.com comercial | `CONFIRMED` (texto) / `REPORTED` (abrangência) | `README.md` lido, linhas 5, 41, 43, 48, 49 |
| `LicenseKeyService.checkLicense()` e `validateLicenseKey()` retornam `true`; `NEXT_PUBLIC_IS_E2E` pula a validação | `CONFIRMED` | `validateLicense.handler.ts` aberto e lido |
| Os três caminhos de license-key continuam na árvore | `CONFIRMED` | filtro da árvore recursiva |
| `.claude/rules`, `.claude/skills`, `.cursor/rules`, `.cursor/skills` são symlinks para os mesmos alvos de `agents/` | `CONFIRMED` | `contents/.claude` + `contents/.cursor` (`type: symlink`) + `contents/agents` |
| Skill vendida com frontmatter `license: MIT` + `metadata.author: vercel` e 45 regras = 45 arquivos | `CONFIRMED` | `SKILL.md` lido + contagem de `rules/` |
| `.env.example` com 465 linhas e 165 variáveis `CHAVE=` | `CONFIRMED` | arquivo baixado e contado por script |
| `PERMISSIONS.md` com 189 linhas / 11 linhas de tabela `recurso.ação` e as 8 seções nomeadas | `CONFIRMED` | arquivo baixado e contado |
| O que o fork quebra/não cobre em runtime | `UNVALIDATED` | nada executado |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · método de fronteira de
licença: `cross-project/licensing/SPLIT-LICENSE-SCAN.md` · contraste de layout de Skills (cópia ×
symlink): `LR-FORGE-017` · política de permissão desta casa:
`cross-project/security/PER-EXECUTION-PERMISSIONS.md` · templates desta casa: `templates/`.
