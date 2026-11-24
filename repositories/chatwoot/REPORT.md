# Chatwoot — 211 linhas de Python que fazem a triagem de advisory: MIT fora de `enterprise/`, e a fila que a Lia não tem

| Campo | Valor |
|---|---|
| ID | `LR-SEC-009` |
| Nome | `chatwoot/chatwoot` — plataforma de atendimento; objeto aqui é a **automação de triagem de GHSA** e a fronteira `enterprise/` |
| Tipo | repositório |
| Fonte oficial | https://github.com/chatwoot/chatwoot |
| Responsável | Chatwoot Inc. ("Copyright (c) 2017-2026 Chatwoot Inc." no LICENSE) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN |
| Recomendação | **ADAPT** — levar o desenho do `ghsa-linear-sync` (advisory em triage → issue com prioridade por severidade → canal humano), adaptado ao formato desta casa |
| Decisão de adoção | — nenhuma registrada |
| Categoria | segurança (triagem de aconselhamento) + fronteira de licença |
| Projetos beneficiados | `lia-security-review` (a lacuna `❌` em `projects/lia-project/INDEX.md`), Lia Forge, Lia Research (fila de triagem), Lia Project |
| Versão analisada | `v4.20.1` (release 2026-11-20) · branch padrão **`develop`** (não `main`/`master`) |
| Proveniência do conteúdo | **medido por nós** via API (LICENSE, `enterprise/LICENSE`, workflow e script de sincronização lidos por inteiro, árvore recursiva `truncated: false`) |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · 40.449★ · 9.850 forks · 17 workflows + `.circleci/` |
| Upstream conferido | 2026-11-24 · 10.117 blobs / 11.952 entradas · `enterprise/` = **759 blobs** (7,5 % da árvore) |
| Próxima revisão | 2027-02-24 |
| Licença | **MIT (Expat) exceto o que estiver sob `enterprise/`**, que tem licença própria. O LICENSE raiz é condicional: *"All content that resides under the 'enterprise/' directory of this repository, **if that directory exists**, is licensed under the license defined in 'enterprise/LICENSE'"*. O `enterprise/LICENSE` restringe uso em produção a quem tem "Chatwoot Subscription Terms of Service" (`CONFIRMED` lendo os dois) |
| Confiança | Alta para os arquivos lidos; nenhuma para o que a automação produz hoje no tracker deles (não tenho acesso a Linear) |

---

## 1. Por que este objeto está no inventário de segurança, e não como benchmark de produto

O dono pediu a leva de oito links; o Chatwoot estava lá. Dos aspectos todos (produto de atendimento
multi-canal, Rails 52 % + Vue 24 % + JS 21 %), **um** interessa à Lia agora, porque toca uma lacuna
declarada nossa: o repositório tem uma workflow de 30 linhas e um script de **211 linhas** que fazem a
triagem periódica de *security advisories* do próprio repositório — criar issue no tracker com prioridade
derivada da severidade, postar no Slack e no Discord, e pular o que já foi criado. Nós não temos fila de
triagem nenhuma: `RUSTSEC-2024-0429` está aberto em `src-tauri/Cargo.lock:1404` desde a rodada anterior
sem nenhum lugar onde "alguém viu isto" signifique alguma coisa (o `lia-security-review` está `❌` em
`projects/lia-project/INDEX.md`). Este arquivo existe para mostrar o tamanho mínimo de uma solução.

## 2. O objeto, medido

| Campo | Valor |
|---|---|
| Estrelas / forks | 40.449 / 9.850 |
| Branch padrão | `develop` |
| Release | `v4.20.1` (2026-11-20) |
| Idiomas | Ruby 52,1 % · Vue 24,0 % · JavaScript 21,3 % |
| Árvore | 10.117 blobs; `enterprise/` com 759 blobs |
| CI | 17 workflows em `.github/workflows` **+ `.circleci/`** (dois sistemas de CI no mesmo repo) |
| Higiene na raiz | `.bundler-audit.yml`, `.dependabot/`, `.devcontainer/`, `.qlty/`, `.env.example`, `.eslintrc.js`, `.all-contributorsrc`, `.annotaterb.yml`, `.husky/`, `AGENTS.md`, `SECURITY.md` |
| Licença | `NOASSERTION` na API (composta); MIT + `enterprise/LICENSE` |

Nomes de workflow medidos (13 dos 17): `auto-assign-pr.yml`, `deploy_check.yml`, `frontend-fe.yml`,
`ghsa-linear-sync.yml`, `lint_pr.yml`, `lock.yml`, `logging_percentage_check.yml`,
`migration_version_check.yml`, `nightly_installer.yml`, `publish_codespace_image.yml`,
`publish_ee_docker.yml`, `publish_foss_docker.yml`.

Três coisas aqui são policy-checks, não builds: `migration_version_check.yml` (migrações com número
certo — evita colisão de versão entre branches), `logging_percentage_check.yml` (o nome anuncia um
orçamento de log, isto é, volume de log tratado como grandeza a verificar em CI — **não abri o arquivo**,
então digo o que o nome e a existência dele significam, não o que a workflow checa), e `lock.yml`
(feitar issue antiga em vez de deixar acumular). Os três são o padrão que falta nesta casa: política
escrita como checagem barata, e não como recomendação em documento.

E a fronteira comercial visível na CI: **`publish_ee_docker.yml` e `publish_foss_docker.yml` são duas
imagens construídas por duas workflows**, exatamente o par que a licença em dois arquivos descreve. É
mais transparente que o padrão AppFlowy (servidor só como imagem, §`LR-FORGE-015`): aqui o FOSS tem
artefato próprio e nome próprio.

## 3. A sincronização de GHSA (o artefato a copiar)

`.github/workflows/ghsa-linear-sync.yml`, 30 linhas, lido por inteiro:

- gatilho: `schedule: cron '0 4 * * *'` com o comentário `# daily at 09:30 IST` (as duas coisas batem:
  04:00 UTC = 09:30 IST) **e** `workflow_dispatch: {}` — corrida diária manual-com-um-clique;
- `permissions: contents: read` — **nenhum escrivamento no GitHub**; o que ele escreve vai para fora;
- passos: `actions/checkout@v4` → `actions/setup-python@v5` com `python-version: '3.11'` →
  `pip install requests==2.32.3` → `python3 .github/scripts/ghsa_linear_sync.py`;
- segredos injetados por env: `GHSA_READ_TOKEN`, `LINEAR_API_KEY`, `LINEAR_TEAM_ID`,
  `LINEAR_PROJECT_ID`, `LINEAR_LABEL_ID`, e `DISCORD_WEBHOOK_URL` / `SLACK_WEBHOOK_URL` opcionais.

`.github/scripts/ghsa_linear_sync.py`, 211 linhas de Python tipado com `list[dict[str, Any]]`, lido por
inteiro. O algoritmo, na ordem em que está no arquivo:

1. `fetch_triage_advisories`: `GET https://api.github.com/repos/{repo}/security-advisories` com
   `params={"state": "triage", "per_page": 100}`, header `X-GitHub-Api-Version: 2022-11-28`, e **paginação
   pelo `Link`** (`r.links.get("next")`) até esgotar;
2. para cada advisory: `linear_issue_exists(ghsa_id)` — query GraphQL filtrando por `title contains
   [GHSA-id]` com `first: 1` → **idempotência pelo identificador no título**, sem estado local, sem
   banco;
3. `linear_create_issue` com `title = "[{ghsa_id}] {summary}"`, descrição construída em
   `build_description` (GHSA id, resumo, `Severity … (CVSS …)`), `teamId`/`projectId`/`labelIds` e
   `priority` por `SEVERITY_PRIORITY = {"critical": 1, "high": 2, "medium": 3, "low": 4}` — com
   *default* 3 (medium) quando a severidade vem como `unknown`;
4. `post_slack` e `post_discord` só **depois** de criar a issue, mencionando o identificador retornado
   (`Linear: {identifier} · Severity: … (CVSS …) · <html_url|advisory>`) e a cor por severidade em
   `SEVERITY_COLOR`;
5. contadores `created/skipped/failed` impressos, `requests.RequestException` capturado por item (uma
   falha não derruba a varredura), e o `print(f"Fetched {len(advisories)} triage advisories")` como
   primeira linha de diagnóstico.

O que eu acho transplantável, em ordem de valor: (a) **a fila é o estado do GitHub** — eles não criaram
planilha nem banco, usam o `security-advisories?state=triage`, que é onde o aviso entra quando alguém o
reporta; (b) **idempotência por consulta ao destino**, não por arquivo de estado; (c) a severidade vira
**prioridade numérica** automaticamente, mas o humano decide no tracker, não no log; (d) o alerta humano
é o passo final, condicionado ao sucesso da criação da issue; (e) `permissions: contents: read`.

O que eles **não** fazem, e que nós precisamos decidir se queremos: nada de remediação automática. Nenhuma
PR é aberta, nenhum `cargo update`/`bundler update` é tentado, nenhum SLA é medido. E há uma escolha
explícita que vale registrar: `state=triage` só pega advisory **dentro do fluxo de advisories do
repositório** — dependências de terceiros divulgadas por `cargo audit`/`bundler-audit` entram por outro
caminho (o `.bundler-audit.yml` + `.qlty/`), não por este script. Ou seja, é uma fila de **triagem de
divulgações**, não um scanner.

## 4. A fronteira `enterprise/`, lida nos dois arquivos

O LICENSE raiz é o modelo "MIT condicional sobre um diretório": três bullets, sendo o primeiro
"… **if that directory exists**, is licensed under the license defined in 'enterprise/LICENSE'". Medido:
o diretório **existe** no monorepo, com 759 blobs, e tem `LICENSE` próprio cujo começo é:

> "The Chatwoot Enterprise license (the 'Enterprise License') Copyright (c) 2017-2026 Chatwoot Inc …
> This software and associated documentation files (the 'Software') may only be used in production, if
> you (and any entity that you represent) have agreed to, and are in compliance with, the Chatwoot
> Subscription Terms of Service …"

Duas consequências práticas, que valem para qualquer consumo nosso de código com essa forma:

1. **`git clone` do Chatwoot não dá direito de uso em produção da parte enterprise**, e a cláusula é
   por *entidade representada*, não por instalação — o que torna "rodar o `enterprise/` para ver o que
   faz" um ato juridicamente distinto de ler o código;
2. a formulação "if that directory exists" é o truque que permite à empresa **remover o diretório de uma
   cópia** e redistribuir tudo como MIT — é por isso que o `publish_foss_docker.yml` existe.

Registro isso na tabela de `cross-project/licensing/SPLIT-LICENSE-SCAN.md`, onde comparo os três formatos
(diretório com licença própria × crates com licença própria × nada na árvore) e o que cada um implica para
o `lia-multiplatform`.

## 5. Comparação de higiene de fornecedura (na mesma leva, dois extremos)

| | Chatwoot (medido) | VoiceStudio (`LR-VOICE-003`) |
|---|---|---|
| Ações de terceiros na CI | `actions/checkout@v4`, `actions/setup-python@v5` — **tags flutuantes** | 262/262 em SHA-40, 0 flutuantes |
| Pin de dependência de ferramenta | `pip install requests==2.32.3` (a versão da lib é pinada; a action, não) | toolchains pinados por `.nvmrc`, `.python-version`, `bun.lock` + testes próprios |
| Auditoria | `.bundler-audit.yml` + `.qlty/` + `.dependabot/` + CodeQL em `.github/codeql`? (não verifiquei aqui) | `action-contracts.yml` + `action-pin-verify.yml` semanais + gitleaks |
| Fila de triagem | **existe**: o §3 | não medi |
| Segurança declarada | `SECURITY.md`: "We use Github to track the security issues that affect our project" | `SECURITY.md` presente (não lido nesta passada) |

Não é uma lição de "quem é melhor": é a observação de que **um projeto de 40 mil estrelas aceita tag
flutuante em action de CI** enquanto um projeto de um ano trata pinos como corpus de teste. Para a Lia,
a fila deles é o que falta; o pino deles é o que já temos planejado.

## 6. Mapa para os projetos da Lia

| Destino | O que levar | Seção |
|---|---|---|
| `lia-security-review` (lacuna `❌`) | o desenho de fila do §3, com o tracker substituído por um arquivo nesta base (`data/inventory/` ou `decisions/PENDING/`) | §3 |
| Lia Research | o mecanismo de idempotência: "o estado mora no destino, consultado por chave estável" — versão nossa: `grep` do id no catálogo antes de abrir novo objeto | §3 |
| Lia Forge | `publish_ee_docker.yml` × `publish_foss_docker.yml` como forma de ter duas distribuições a partir de uma árvore | §2 |
| Lia Project | `migration_version_check.yml` e `logging_percentage_check.yml` como exemplos de *política* virando checagem barata | §2 |
| `cross-project/licensing` | a cláusula condicional "if that directory exists" | §4, `LR-LIC-006` |
| Dono | decisão sobre prioridade por severidade: o mapa `critical→1 … low→4` com default medium é uma política editorial que a casa tem de escrever, não importar | §3 |

## 7. Proposta concreta (executável aqui, sem conta nova)

Um arquivo novo em `data/inventory/`, chamado aqui de advisory-triage.tsv, com colunas `date · source · id · crate · severity ·
state · action · evidence`, e uma checagem no `tools/validate.py` que reclama se uma linha tem
`state=open` há mais de N dias sem `action`. Para o `RUSTSEC-2024-0429` (que está no `Cargo.lock` do
Lia Forge desde a rodada passada e hoje mora em lugar nenhum), o `state` inicial seria `open` e a
`action` seria a triagem propriamente dita. Nada de webhook, nada de Linear: a lição do Chatwoot é o
formato da fila, não o fornecedor.

Não implementei — **é mudança de infraestrutura da casa, e o padrão da casa é que isso entra por
decisão do dono** (`governance/RESEARCH-GOVERNANCE.md`). Registro a sugestão, não a ação.

## 8. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Executar o `ghsa_linear_sync.py` | `BLOCKED` | exige `GHSA_READ_TOKEN` + chaves de Linear/Slack/Discord; nenhuma conta foi criada nem buscada (regra permanente) |
| O que a automação produz hoje | `NOT_RUN` | o Linear deles é privado |
| As 4 workflows que não listei, e o conteúdo do `.circleci/config.yml` | `NOT_RUN` | nomes medidos, arquivos não abertos |
| Licença de cada arquivo dentro de `enterprise/` | `NOT_RUN` | li o `enterprise/LICENSE`; não verifiquei cabeçalhos por arquivo |
| Se `railties`/`rubocop`/CodeQL estão habilitados (`.github/codeql/` existe no OpenProject; no Chatwoot não confirmei) | `UNVALIDATED` | não listei `.github/` inteiro aqui |
| Comportamento de segurança real do app | `UNVALIDATED` | nada foi instalado nem executado (sem Ruby no ambiente, medido) |
| `SECURITY.md` por extenso, programa de bug bounty | `NOT_RUN` | só as duas primeiras frases lidas |

## 9. Recomendação: **ADAPT** (formato, não ferramenta)

1. **Adaptar**: a fila de triagem como arquivo versionado nesta base (§7), com severidade→prioridade e
   idempotência por chave; e o comentário explícito de `permissions: contents: read` em qualquer
   workflow que a Lia venha a ter com token de leitura.
2. **Adaptar**: a clausula condicional de licença ("if that directory exists") **não** — é uma forma que
   favorece quem distribui, não quem consome; registrar que ela existe, e que nenhuma licença da Lia
   deveria depender de um diretório poder ser removido.
3. **Não adotar** o Chatwoot como dependência nem como modelo de produto; nada na pergunta do dono
   pedia isso, e Vue 2/Rails é uma arquitetura que a casa não avalia agora.
4. **Fecho dos `NOT_RUN` que dependem de mim**: listar `.github/` inteiro do Chatwoot e abrir o
   `SECURITY.md` — é nível 1, dá para fazer, e fica pendido para a próxima passada junto com o par
   `briiirussell/cybersecurity-skills` × `cloudflare/security-audit-skill` que já está na backlog como
   **07** em `RESEARCH-BACKLOG.md`.
5. **Decisão do dono**: (a) aprovar ou não o `advisory-triage.tsv` + checagem no validador; (b) se a
   casa adota prioridade por severidade com default `medium` igual ao deles; (c) qual `N` de dias sem
   ação deve gerar `erro` (contra `aviso`).

## 10. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| 40.449★ · 9.850 forks · Ruby 52,1/Vue 24,0/JS 21,3 · branch padrão `develop` · `v4.20.1` (2026-11-20) | `CONFIRMED` | `gh api repos/chatwoot/chatwoot` + `releases/latest` + `languages` |
| 10.117 blobs; `enterprise/` com 759 blobs; 17 workflows + `.circleci/` | `CONFIRMED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + `contents/.github/workflows` |
| LICENSE raiz = "MIT Expat" exceto `enterprise/`, com a cláusula condicional "if that directory exists" | `CONFIRMED` | `LICENSE` decodificado (14 primeiras linhas transcritas) |
| `enterprise/LICENSE` restringe uso em produção a assinantes dos Chatwoot Subscription Terms | `CONFIRMED` | `enterprise/LICENSE` decodificado |
| Workflow de 30 linhas: cron `0 4 * * *` (comentário 09:30 IST coerente), `workflow_dispatch`, `permissions: contents: read`, `requests==2.32.3`, 7 segredos | `CONFIRMED` | arquivo lido na íntegra nesta data |
| Script de 211 linhas: endpoint `security-advisories?state=triage`, paginação por `Link`, idempotência por título no Linear, prioridade por severidade, Slack/Discord depois da criação | `CONFIRMED` | `.github/scripts/ghsa_linear_sync.py` lido (trechos de `fetch_triage_advisories` e `main` transcritos) |
| `publish_ee_docker.yml` e `publish_foss_docker.yml` convivem | `CONFIRMED` | listagem de workflows |
| O app roda como FOSS de produção com a mesma segurança | `UNVALIDATED` | nada executado; sem Ruby no ambiente |
| Existência de `.github/codeql/` no Chatwoot | `UNVALIDATED` | não listado nesta passada (diferente do OpenProject, onde foi listado) |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · política de permissão por
execução que este objeto corrobora: `cross-project/security/PER-EXECUTION-PERMISSIONS.md` · auditoria de
credenciais desta casa: `cross-project/security/CREDENTIAL-AUDIT-DIGEST.md` · objeto da lacuna
`lia-security-review`: `projects/lia-project/INDEX.md` · pendência relacionada: `RESEARCH-BACKLOG.md`
item 07.
