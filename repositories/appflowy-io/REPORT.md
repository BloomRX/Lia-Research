# AppFlowy-IO — os 27 repositórios do org medidos um a um, e o que a licença de cada um permite

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-015` |
| Nome | `AppFlowy-IO` (GitHub org) — AppFlowy + editor + cloud + self-host comercial + 23 repositórios menores |
| Tipo | repositório (inventário completo do org; 27 objetos) |
| Fonte oficial | https://github.com/AppFlowy-IO |
| Responsável | AppFlowy Pte. Ltd. (Singapura); o acordo comercial nomeia a pessoa jurídica explicitamente |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN |
| Recomendação | **REFERENCE_ONLY** para o org no todo; **ADAPT** para o objeto único dentro dele — ver `LR-MCP-004` |
| Decisão de adoção | — nenhuma registrada |
| Categoria | inventário de org (licença, atividade, empacotamento de plugins) |
| Projetos beneficiados | Lia Forge (empacotamento AGPL × binário), Lia Project (front-end Flutter de notas), Lia Model Lab (o que fazer com um servidor que o upstream parou de publicar) |
| Versão analisada | árvore de HEAD medida em 2026-11-24 (UTC) via API; `AppFlowy` release `0.15.1` de 2026-11-15; `appflowy-editor` 6.1.0 de 2025-12-08; `AppFlowy-SelfHost-Commercial` 0.9.159 de 2025-11-20 |
| Proveniência do conteúdo | **medido por nós** (API do GitHub + clone raso do `appflowy-ai-plugins`); nada aqui vem de post de blog nem de material de marketing |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · `gh api orgs/AppFlowy-IO/repos?per_page=100` (página 2 vazia → 27 é o total) |
| Upstream conferido | 2026-11-24 · nenhum fork nosso; leitura direta da árvore e do arquivo LICENSE de cada repositório |
| Próxima revisão | 2027-02-24 |
| Licença | **AGPL-3.0 na maioria** (AppFlowy, AppFlowy-Cloud, AppFlowy-Collab, AppFlowy-LAI, AppFlowy-Web, AppFlowy-Web-Clipper, appflowy-ai-plugins, AppFlowy-Supabase, AppFlowy-Chat, AppFlowy-Theme, AppFlowy-Cloud-Billing-Client, template Supabase); `appflowy-editor` **dual AGPL-3.0 + MPL-2.0**; **`AppFlowy-SelfHost-Commercial` não tem arquivo LICENSE** — só o `SELF_HOST_LICENSE_AGREEMENT.md`; `AppFlowy-Website`, `AppFlowy-Builder`, `AppFlowy-Web-Editor`, `AppFlowy-CI`, `AppFlowy-Gotrue`, `AppFlowy-Docker-CI` sem licença; `auth` MIT; `supabase` e `AppFlowy-with-AppFlowy-Cloud-Build` Apache-2.0 (`CONFIRMED` pela leitura de cada arquivo) |
| Confiança | Alta para o censo e para as licenças (lidas no arquivo); média para "o que o binário distribui" — nada foi compilado aqui |

---

## 1. Por que este objeto entrou na base

O dono mandou uma leva de oito links e pediu, para os dois que são organizações, "veja todos os
repos desse". Este arquivo é o resultado para `AppFlowy-IO`: os 27 repositórios contados, com
estrelas, arquivamento, idioma, licença lida no arquivo e data do último push — não uma amostra, o
conjunto inteiro.

Ele vale para a Lia por três razões concretas, e nenhuma delas é "é open source e tem 79 mil
estrelas":

1. é o **precedente vivo** do problema do Lia Forge: um produto desktop cujo núcleo é AGPL, cujo
   editor é dual, e cuja oferta self-host *comercial* é publicada sem arquivo de licença — o
   exatamente o formato que uma empresa adota quando quer distribuir binário sem abrir o servidor;
2. é o **único objeto desta leva** cujo verificador interno eu consegui executar de ponta a ponta
   (`appflowy-ai-plugins`); isso está em `LR-MCP-004`, não aqui;
3. é um caso raro de **assimetria de manutenção documentada no próprio repositório**: o servidor que
   todos usam para self-host foi arquivado, e o aviso sobre isso está escrito no README dele — o
   tipo de fato que some quando se cita o projeto só pelas estrelas.

## 2. O censo (27 repositórios, medidos 2026-11-24)

Nenhum dos 27 é fork do nosso ponto de vista do org — `supabase`, `auth` e `y-crdt` são forks do
upstream de terceiros e estão incluídos no censo porque aparecem em `orgs/AppFlowy-IO/repos`.

| Repositório | ★ | Forks | Idioma | Licença (lida no arquivo) | Arquivado | Último push |
|---|---|---|---|---|---|---|
| `AppFlowy` | 79.454 | 6.357 | Dart | AGPL-3.0 | não | 2026-11-15 |
| `AppFlowy-Cloud` | 2.018 | 600 | Rust | AGPL-3.0 | **sim** | 2026-09-11 |
| `appflowy-editor` | 695 | 354 | Dart | dual AGPL-3.0 + MPL-2.0 | não | 2026-08-06 |
| `AppFlowy-Web` | 361 | 189 | TypeScript | AGPL-3.0 | não | 2026-11-21 |
| `AppFlowy-Docs` | 116 | 109 | — | sem SPDX (NOASSERTION) | não | 2025-10-07 |
| `appflowy-board` | 115 | 77 | Dart | sem SPDX (NOASSERTION) | não | 2026-01-04 |
| `AppFlowy-Collab` | 90 | 51 | Rust | AGPL-3.0 | não | 2026-02-18 |
| `AppFlowy-Website` | 61 | 31 | JavaScript | **nenhuma** | não | 2026-10-27 |
| `AppFlowy-Plugins` | 37 | 31 | Dart | sem SPDX (NOASSERTION) | não | 2026-01-19 |
| `AppFlowy-with-AppFlowy-Cloud-Build` | 36 | 29 | — | Apache-2.0 | não | 2024-01-07 |
| `AppFlowy-SelfHost-Commercial` | 26 | 14 | Python | **nenhum arquivo LICENSE** | não | 2026-11-21 |
| `AppFlowy-LAI` | 24 | 6 | Rust | AGPL-3.0 | não | 2025-04-17 |
| `AppFlowy-Web-Clipper` | 22 | 8 | TypeScript | AGPL-3.0 | não | 2024-12-17 |
| `AppFlowy-Builder` | 14 | 22 | Python | **nenhuma** | não | 2026-11-18 |
| `AppFlowy-Web-Editor` | 11 | 9 | TypeScript | **nenhuma** | não | 2025-07-01 |
| `AppFlowy-Supabase` | 10 | 11 | Rust | AGPL-3.0 | não | 2024-01-10 |
| `AppFlowy-App-Supabase-Template` | 8 | 57 | — | AGPL-3.0 | não | 2023-11-21 |
| `AppFlowy-Theme` | 5 | 4 | — | AGPL-3.0 | não | 2023-09-15 |
| `AppFlowy-Chat` | 5 | 11 | TypeScript | AGPL-3.0 | não | 2025-07-28 |
| `AppFlowy-CI` | 3 | 6 | Python | **nenhuma** | não | 2026-11-23 |
| `supabase` | 2 | 2 | — | Apache-2.0 | não | 2023-08-29 |
| `AppFlowy-Cloud-Billing-Client` | 2 | 5 | Rust | AGPL-3.0 | não | 2024-06-12 |
| `AppFlowy-Gotrue` | 1 | 0 | — | **nenhuma** | não | 2025-04-16 |
| `auth` | 1 | 14 | Go | MIT | não | 2026-09-10 |
| `AppFlowy-Docker-CI` | 1 | 2 | — | **nenhuma** | não | 2026-11-13 |
| `appflowy-ai-plugins` | 1 | 1 | Python | AGPL-3.0 | não | 2026-11-05 |
| `y-crdt` | 0 | 3 | Rust | sem SPDX (NOASSERTION) | não | 2023-04-03 |

Contas do censo: **27** repositórios · **1** arquivado (`AppFlowy-Cloud`) · **14** AGPL-3.0 ·
**6** sem nenhum arquivo de licença na raiz (`AppFlowy-Website`, `AppFlowy-Builder`,
`AppFlowy-Web-Editor`, `AppFlowy-CI`, `AppFlowy-Gotrue`, `AppFlowy-Docker-CI`) · **1** com acordo
privado no lugar da licença (`AppFlowy-SelfHost-Commercial`) · **5** sem SPDX identificável apesar de
terem arquivo LICENSE (`AppFlowy-Docs`, `appflowy-board`, `AppFlowy-Plugins`, `AppFlowy-SelfHost-Commercial`,
`y-crdt`).

## 3. AppFlowy (o carro-chefe): o que está na raiz e o que roda em CI

Árvore medida: `93.941` KB no campo `size` da API (que é KiB de objetos, não bytes descompactados —
número citado como grandeza, não como tamanho de download).

Conteúdo da raiz (14 primeiras entradas): .dockerignore, .githooks/, .github/, .gitignore,
CHANGELOG.md, CODE_OF_CONDUCT.md, LICENSE, README.md, ROADMAP.md, codemagic.yaml,
commitlint.config.js, doc/, frontend/, install.sh.

As 12 workflows medidas em `AppFlowy-IO/AppFlowy/.github/workflows`: android_ci.yaml.bak,
build_command.yml, commit_lint.yml, docker_ci.yml, flutter_ci.yaml, ios_ci.yaml, mobile_ci.yml,
ninja_i18n.yml, release.yml, rust_ci.yaml, rust_coverage.yml, translation_notify.yml.

Dois detalhes valem o registro:

- **android_ci.yaml.bak** está no diretório de workflows com sufixo `.bak`. O GitHub só lê arquivos
  com extensão `.yml`/`.yaml`, então um `.yaml.bak` não roda — é um trabalho desligado *dentro* da
  pasta ativa. Anoto porque a alternativa usual (apagar o arquivo) destruiria a informação de que a CI
  de Android existiu e de que foi desligada de propósito; aqui o estado "desligado, não morto" fica
  legível para quem chega.
- a CI cobre as quatro superfícies (flutter, rust, ios, android-desligado) mais três checagens
  sociais (commit_lint, ninja_i18n para tradução, translation_notify). Não há workflow de auditoria
  de dependências *neste* repositório — as que eu procurava (audit.yml, rustlint.yml,
  stress_test.yml, integration_test.yml, client_api_check.yml) estão no `AppFlowy-Cloud`, o
  repositório arquivado. Registrar isso importa porque é a parte do Rust que ficou sem o verificador
  quando o servidor foi movido para imagens Docker pré-construídas.

## 4. AppFlowy-Cloud arquivado × AppFlowy-SelfHost-Commercial sem licença

Este é o achado do objeto, e ele é uma *política*, não um código.

**O que o README do `AppFlowy-Cloud` diz** (frase lida no arquivo, 2026-11-24): o repositório está
"archived and is no longer used to build or distribute the latest AppFlowy self-hosted server", e que
"New server features are only available in the official prebuilt Docker images" (hub.docker.com,
prefixo `appflowyinc/appflowy_cloud`), com a observação de que versões mais novas dos clientes web e
desktop podem exigir o servidor comercial.

**O que o `AppFlowy-SelfHost-Commercial` contém**: release 0.9.159 (2025-11-20), sete workflows
(backup-test.yml, cancel-merged-pr-runs.yml, classify-changes.yml, deployment-test.yml,
release-docker-build.yml, self-host-upgrade-check.yml, update-release-images.yml),
docker-compose.yml, docker-compose.backup.yml, docker/, docker-swarm/, helm/, scripts/, docs/, e o
`SELF_HOST_LICENSE_AGREEMENT.md` — **sem nenhum `LICENSE`**.

**O que o acordo diz na cláusula 1** (texto lido): "APPFLOWY PTE. LTD. SOFTWARE LICENSE AGREEMENT …
grants you a non-exclusive, non-transferable license to use the Software for your internal" (o
trecho que li termina em "internal"; a cláusula continua). Um acordo de uso interno, não-transferível,
em repositório público sem licença aberta.

Ler os dois juntos é o quadro honesto: o self-host AGPL "de verdade" virou imagem de container
pré-construída sem fonte correspondente no org, e o que se mantém no GitHub é o andaime de deploy com
licença proprietária. **Nada aqui é acusação** — é o formato da fronteira. O que importa para a Lia é
o desenho: *o código de empacotamento pode ser público mesmo quando o binário e o serviço não são*, e
o `self-host-upgrade-check.yml` + `deployment-test.yml` + `backup-test.yml` existem justamente para
que a fronteira pública continue funcional.

Consequência prática que eu **não** verifiquei (e não vou verificar sem autorização): puxar as
imagens `appflowyinc/*` e rodar. Isso é nível 3 em `governance/TESTING-PROTOCOL.md` — download de
imagem de terceiros com comportamento de servidor. Fica como teste do lado do dono, §10.

## 5. appflowy-editor: dual AGPL-3.0 + MPL-2.0, e por que isso é a parte transplantável

O arquivo LICENSE começa, literalmente: "All code contributed to the AppFlowy Editor project is
dual-licensed, and released under b…" (a frase continua com as duas licenças). Release 6.1.0 de
2025-12-08, duas workflows (commit_lint.yml, test.yml), `.fvmrc` fixando o toolchain Flutter.

O que um dual-license "contribuído sob AGPL **ou** MPL" significa é uma escolha do licensor, não do
usuário: quem consome pode optar pela MPL-2.0 (permiscível com código proprietário, só exige que os
arquivos MPL em si permaneçam sob MPL), enquanto a AGPL fica obrigando o servidor. Para o
`lia-multiplatform`, que hoje está marcado AGPL-3.0-or-later na matriz, a lição não é "copiar o
AppFlowy" — é que *o componente de editor* é exatamente o lugar onde uma dual-license reduz atrito
sem ceder o produto. Registro em `LR-LIC-006`, que trata do método.

## 6. appflowy-ai-plugins: o objeto que justifica o inventário

Um repositório de **1 estrela**, 37 arquivos, 849 KB, Python, AGPL-3.0-only, push 2026-11-05. É o
repositório mais novo em sinal real do org (o `AppFlowy-CI`, com 3, é infraestrutura) e o único da
leva inteira cujo verificador interno eu executei: `python3 scripts/check.py` → `ok`, exit 0, com
duas notas; e `python3 scripts/annotation-table.py` duas vezes → saída idêntica, 48 linhas,
`sha256 09133d787d55fcd8…`.

O motivo de ele existir no org com uma estrela: é o **par de plugins MCP** (Claude e Codex, versões
cloud e self-hosted) do AppFlowy, com `tools.json` do catálogo deles, com 45 ferramentas + um bloco de
integridade declarando `sha-256` do catálogo, e `confirm: true` obrigatório em toda ferramenta que
escreve. Dossiê completo em `LR-MCP-004`; é o único item desta leva que eu recomendo transportar.

## 7. O resto do org em uma linha cada (medido, sem dossiê)

- `AppFlowy-Web` (361★, TS, AGPL) — ativo 2026-11-21; é o cliente web que o aviso do Cloud menciona.
- `AppFlowy-Docs` (116★) e `AppFlowy-Website` (61★, sem licença) — conteúdo, não código.
- `appflowy-board` (115★, NOASSERTION) e `AppFlowy-Collab` (90★, AGPL) — o protocolo de colaboração;
  se um dia o Lia Project precisar de CRDT próprio, aqui está o ponto de partida, mas **não** foi
  lido nesta rodada.
- `AppFlowy-Plugins` (37★) — o mecanismo antigo de extensibilidade em Dart, anterior ao par MCP.
- `AppFlowy-LAI` (24★, Rust, AGPL) — inference: só existe como objeto de interesse do Lia Model Lab,
  não foi lido; sem release pública medida.
- `AppFlowy-Builder`, `AppFlowy-CI`, `AppFlowy-Docker-CI` — três repositórios de infraestrutura sem
  licença; `AppFlowy-CI` com push 2026-11-23 é o mais ativo de todo o org depois do `AppFlowy-Web`.
- `AppFlowy-Web-Clipper`, `AppFlowy-Theme`, `AppFlowy-Chat`, `AppFlowy-Supabase`,
  `AppFlowy-App-Supabase-Template`, `AppFlowy-Cloud-Billing-Client`, `AppFlowy-Gotrue`, `auth`,
  `supabase`, `y-crdt`, `AppFlowy-with-AppFlowy-Cloud-Build` — cauda; somados, 91 estrelas.

## 8. O que o org faz de diferente (e por que a Lia deveria olhar para isso)

1. **Licença por componente, não por org.** Quatro regimes convivendo: AGPL no produto, dual no
   editor, Apache em dois repositórios, nenhuma licença em seis repositórios de infraestrutura. É
   caro de auditar para quem consome — e é precisamente por isso que a matriz de licenças da Lia
   existe.
2. **CI com teste de upgrade do self-host.** `self-host-upgrade-check.yml` existe porque o produto é
   uma instalação de longa duração do usuário, não um serviço deles. O Lia Forge tem o mesmo problema
   (empacotar binário que o usuário sobe sozinho) e não tem nada parecido.
3. **`.bak` em vez de apagar.** A CI de Android desligada fica no lugar, com nome que avisa.
4. **Verificador de metadados dentro do repositório** (`scripts/check.py`,
   `scripts/annotation-table.py`) — item §6; é o padrão "a declaração é uma fixture, e há um teste
   para ela".
5. **Aviso de arquivamento escrito no README**, não escondido no banner do GitHub.

## 9. Mapa para os projetos da Lia

| Destino | O que levar | Seção |
|---|---|---|
| Lia Forge | `self-host-upgrade-check.yml` + `deployment-test.yml` + `backup-test.yml` como o conjunto de CI que uma distribuição self-host precisa; `.fvmrc`/toolchain pin | §3, §4, §8 |
| Lia Project | nada de código: Flutter/Cargo fora do ambiente daqui; ler `AppFlowy-Collab` se CRDT entrar em pauta | §7 |
| Lia Model Lab | `AppFlowy-LAI` como ponto de partida não lido; **não** cite como disponível | §7 |
| Lia Agent Hub | `appflowy-ai-plugins` (o par de plugins + `tools.json` com digest) | §6, `LR-MCP-004` |
| Lia Research | o censo de 27 com licença lida no arquivo é o formato; o par `AppFlowy-Cloud` × `AppFlowy-SelfHost-Commercial` é o exemplo de como um "open source" muda de fronteira sem mudar de slogan | §4 |

## 10. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Compilar `AppFlowy` (Flutter) ou `AppFlowy-Collab`/`Cloud` (Rust) | `BLOCKED` | sem `flutter`, `cargo`, `rustc` neste sandbox (medido: `command -v` vazio para os três) |
| Rodar as imagens `appflowyinc/appflowy_cloud` | `NOT_RUN` | nível 3 — exige autorização do dono; nenhum container aqui |
| Ler `AppFlowy-Collab`, `AppFlowy-LAI`, `AppFlowy-Plugins`, `AppFlowy-Docs` | `NOT_RUN` | fora do escopo que a pergunta sustentava; registrado como pendência §11 |
| Quem mantém o `AppFlowy-SelfHost-Commercial` e sob que contrato | `UNVALIDATED` | o acordo não define partes além da licensora; sem página de preço lida nesta rodada |
| Número de contribuidores por repositório | `BLOCKED` | o cabeçalho `Link` da API não veio nesta coleta (mesma limitação do `LR-*` anterior); nada citado como medido |
| Se o `AppFlowy-Web` consome o servidor comercial (o README do Cloud sugere) | `REPORTED` | está escrito no aviso; não abri o `AppFlowy-Web` |
| Licença dos assets (ícones, fontes, imagens) dos 27 | `NOT_RUN` | só o LICENSE da raiz foi lido por repositório |

## 11. Recomendação: **REFERENCE_ONLY** (com uma exceção, em outro objeto)

1. **Não adotar** nada deste org como dependência; o AGPL no núcleo é uma decisão que o dono toma, não
   eu.
2. **Usar o §4 como material de decisão do Lia Forge**: quando o Forge decidir "abrir o código, fechar
   o binário/serviço", `AppFlowy-IO` é um exemplo medido do formato — inclusive do custo (seis
   repositórios sem licença, um servidor arquivado).
3. **Transportar uma coisa só**: o par `appflowy-ai-plugins` → `LR-MCP-004`.
4. **Decisão do dono (nenhuma é minha)**: (a) autorizar ou não o teste de nível 3 com as imagens
   `appflowyinc/*`; (b) se o Lia Forge adota o modelo "acordo próprio em vez de licença aberta" para o
   self-host, o que isso implica com a matriz atual em `data/inventory/license-matrix.tsv`; (c) se
   `AppFlowy-Collab` merece dossiê próprio (aí sim, com leitura de CRDT, que eu não fiz).
5. **Pendência registrada**: recontar o org em 2027-02-24 — `AppFlowy-CI` e `AppFlowy-Builder` estão
   mais ativos que o produto hoje, o que costuma anteceder mudança de política de licença.

## 12. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| O org tem 27 repositórios; 1 arquivado; 14 AGPL-3.0 | `CONFIRMED` | `gh api orgs/AppFlowy-IO/repos?per_page=100` (página 2 = 2 bytes, vazia) + campo `license.spdx_id` por repositório |
| Seis repositórios sem arquivo LICENSE na raiz; `AppFlowy-SelfHost-Commercial` idem | `CONFIRMED` | `git/trees/HEAD` da raiz por repositório (16 varridos por script; os demais pelo campo `license`) |
| `AppFlowy` release 0.15.1 (2026-11-15), 12 arquivos de workflow, `.bak` na pasta ativa | `CONFIRMED` | `releases/latest` + `contents/.github/workflows` + listagem da raiz |
| `AppFlowy-Cloud` arquivado com aviso de que features novas só existem em imagens Docker oficiais | `CONFIRMED` | README lido via `contents/README.md` (frase exata transcrita no §4) |
| `AppFlowy-SelfHost-Commercial`: 0.9.159, 7 workflows, `SELF_HOST_LICENSE_AGREEMENT.md`, licença concedida "for your internal" uso, sem LICENSE | `CONFIRMED` (texto) / `REPORTED` (efeito prático) | árvore + primeiras 600 caracteres do acordo decodificados |
| `appflowy-editor` é dual AGPL-3.0 + MPL-2.0; release 6.1.0; `.fvmrc` presente | `CONFIRMED` | LICENSE lido na raiz + `releases/latest` + listagem da raiz |
| `appflowy-ai-plugins`: 37 arquivos, 849 KB, 1★, push 2026-11-05, `check.py` → `ok` exit 0 | `CONFIRMED` + `OBSERVED` | clone `--depth 1` (HEAD `318a8c8`) e execução do script no sandbox |
| Compilação de Flutter/Rust não é possível neste ambiente | `CONFIRMED` | `command -v cargo rustc flutter go ruby docker` sem saída |
| `AppFlowy-Web` consome o servidor comercial | `REPORTED` | só o aviso do README do Cloud diz; o `AppFlowy-Web` não foi aberto |
| Número de contribuidores, cobertura de testes, tamanho real de download | `UNVALIDATED` | nada medido |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · método de leitura de
licença por diretório: `cross-project/licensing/SPLIT-LICENSE-SCAN.md` · objeto transportável:
`cross-project/mcp/APPFLOWY-AI-PLUGINS-GATES.md` · org comparado na mesma leva:
`repositories/opf-openproject/REPORT.md`.
