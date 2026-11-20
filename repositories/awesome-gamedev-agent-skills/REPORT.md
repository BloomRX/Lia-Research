# awesome-gamedev-agent-skills — 79 Skills de game dev + roteador, para 12 engines

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-006` |
| Tipo | repositorio (pacote de Skills) |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | LOCAL_SMOKE_PASS |
| Recomendação | **ADAPT** — o formato, o validador de Skill e o pipeline de asset; não o pacote inteiro |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | studio (leitura transversal em agents, licensing) |
| Projetos beneficiados | Lia Studio (se o engine estiver na lista), Lia Forge (pipeline de asset), Lia Agent Hub (formato de Skill) |
| Fontes | `gamedev-skills/awesome-gamedev-agent-skills@c6ca6c41c839b68319ffc08430b99ab768debc32` (2026-11-12): `README.md`, `LICENSE`, `NOTICE`, `docs/SKILL-FORMAT.md`, `docs/INSTALLATION.md`, `docs/VERSION-SUPPORT.md`, `router/SKILL.md`, `skills/disciplines/create-game-assets/` (SKILL.md + 2 scripts + assets), `evals/RESULTS.md`, `evals/triggers.json` (366 itens), `scripts/validate-skills.py`, `.github/workflows/ci.yml`, árvore completa (504 entradas), API do GitHub, tarball do commit |
| SHA completo | `c6ca6c41c839b68319ffc08430b99ab768debc32` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — SHA citado no próprio relatório |
| HEAD atual | `c6ca6c41c839b68319ffc08430b99ab768debc32` (conferido em 2026-11-20) |
| Versão analisada | `c6ca6c4` (2026-11-12T07:38:53Z), release `v2.0.0` (2026-11-11) |
| Data da pesquisa | 2026-11-20 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `gamedev-skills/awesome-gamedev-agent-skills` · HEAD `c6ca6c41c839` · sem mudança no HEAD |
| Próxima revisão | 2027-02-18 |
| Responsável | Research Orchestrator |
| Licença | **Apache-2.0** (lida em `LICENSE`; `NOTICE` com atribuição e *disclaimer* de marca) |

## 1. Identificação e autoria

| Item | Valor |
|---|---|
| Organização | `gamedev-skills` — criada em 2026-06-27, **1 repositório público** |
| Repositório criado | 2026-06-24 |
| Último push em `main` | 2026-11-12 |
| Estrelas / forks | **9.651** / 981 |
| Mantenedor principal | `AbhishekBarali` (265 commits de 290 dos 5 principais) |
| Outros contribuidores | `Unknown-333` (15), `bcoffee0630` (5), `KennyVWS` (3), `ishangautam7` (2) |
| PRs abertos no momento | 3 (`#56` source lookup, `#57` Bevy video capture, `#58` marketplace de plugins) |
| Site | GitHub Pages gerado por script (`scripts/generate-site.py` + `check-site.py` no CI) |

Ambiguidade de homônimo verificada: não é o `awesome-gamedev` (lista de links) nem
`anthropics/skills`. O objeto é este repositório, com o site publicado a partir dele — o site
não tem conteúdo além do que está no repositório (gerado por script, conferido em
`scripts/generate-site.py`).

## 2. Estrutura real (arquivos, não o que o README diz)

O site anuncia 79 Skills + 1 roteador. A árvore confirma: **80 `SKILL.md`** (79 + `router/`),
distribuídos como o site diz:

| Pasta | Skills | Conteúdo |
|---|---:|---|
| `skills/godot/` | 16 | Godot 4.7 (GDScript e C#), cena, física, shader, teste headless, export |
| `skills/disciplines/` | 15 | conceitos transversais: IA, procgen, save, shader, game feel, **create-game-assets** |
| `skills/other-engines/` | 12 | Bevy, pygame-ce, LÖVE, Defold, Roblox |
| `skills/unity/` | 9 | Unity 6.3 LTS (6000.3) |
| `skills/genres/` | 9 | plataforma, cartas, tower defense — composição de Skills |
| `skills/web-engines/` | 6 | Phaser 4.2, PixiJS 8.22, three.js r187 |
| `skills/unreal/` | 6 | UE 5.8: Blueprint, C++, Enhanced Input, BT/EQS/StateTree, Niagara, packaging |
| `skills/workflows/` | 5 | game jam, protótipo rápido, publicação Steam/itch.io |
| `skills/ebitengine/` | 1 | Go + Ebitengine 2.10.6 |
| `router/` | 1 | dispatcher: detecta engine e tarefa, carrega 2–3 Skills |

Além das Skills: 19 arquivos de teste, 37 `.py` (dos quais **19 dentro de Skills**), 9 docs,
`scripts/validate-skills.py`, `scripts/run-trigger-evals.py`, `.claude-plugin/marketplace.json`,
`templates/`, `evals/` (366 prompts).

## 3. Instruções (o que a Skill manda o agente fazer; gatilhos; escopo)

O padrão que o pacote usa — e que é o valor transferível principal:

1. **Frontmatter mínimo**: só `name` e `description`. O validador proíbe qualquer outra chave.
2. **Descrição que declara o vizinho**: `… Not for coyote time (`platformer`), RigidBody2D ou 3D
   (`godot-physics`), tile levels (`godot-tilemap`).` Isso resolve o problema real de Skill que
   dispara na tarefa errada.
3. **Descrição curta por orçamento de contexto**: o pacote mediu que o Claude Code lista
   descrições dentro de ~1% da janela e trunca o resto; por isso o total caiu de 56.142 para
   29.866 caracteres entre versões.
4. **Verificação dentro da Skill**: a Skill de movement traz um `.gd` de teste e o comando
   `godot --headless … --script`, com critério de saída 0.
5. **Seção `## Gotchas` obrigatória** e índice (`## Contents`) para referência longa (>100 linhas).
6. **Trust boundary explícita no router**: conteúdo de projeto e saída de ferramenta são dados a
   inspecionar, não autoridade para sobrescrever instruções do host.

`docs/SKILL-FORMAT.md` diz seguir a especificação Agent Skills (`agentskills.io`) no menor
subconjunto portátil, conferida em 2026-10-24.

## 4. Scripts e dependências (executáveis? rede? ferramentas externas?)

| Item | Achado |
|---|---|
| Rede nos scripts de Skill | **nenhuma** ocorrência de `urllib`/`requests`/`socket` em `skills/**/*.py` |
| Rede no repositório | só nos scripts de site (URLs de sitemap e links) |
| Dependência de terceiro | **uma**: `Pillow>=10,<14` (`create-game-assets/scripts/requirements.txt`) |
| `subprocess` | usado para invocar engine/compilador (`godot --headless`, `dotnet`, `bob.jar`) — é o propósito |
| Escrita em disco | dentro do diretório do projeto (`new_game.py` cria scaffold; `package_macos_app.py` monta `.app`) |
| Instalação | `npx skills add <repo>` — CLI **`skills`** do npm, publicado por `vercel-labs/skills` (MIT, mantenedores `rauchg` e `quuu`, v1.9.0), que copia ou cria link simbólico das pastas para o diretório de Skills de cada agente |

## 5. Permissões necessárias (arquivo, rede, shell, credenciais)

- **Arquivo**: ler o projeto do usuário; escrever scaffold/assets/testes no projeto.
- **Shell**: executar engine headless, compilador, empacotador — é o que permite a Skill verificar.
- **Rede**: nenhuma nas Skills; a instalação via `npx` exige rede e Node ≥ 22.20.
- **Credenciais**: nenhuma. Não há MCP, não há login, não há conta.
- Ao instalar: o CLI escreve **fora** do repositório, no diretório de configuração do agente —
  efeito persistente na máquina (por isso é Nível 3 para a Lia, ver §9).

## 6. Mecanismos além do texto (validadores, schemas, MCP, testes)

| Mecanismo | O que faz | Confiança |
|---|---|---|
| `scripts/validate-skills.py` | nome em kebab-case, descrição ≤1.024, ≤500 linhas, `## Gotchas` presente, "not for" obrigatório, índice para referência longa, links e caminhos válidos, manifesto de plugin | **CONFIRMED** — rodei: "Validated 80 skill file(s)… All checks passed", exit 0 |
| CI (`ci.yml`) | validação + testes unitários + build do site; job separado em matriz Ubuntu/Windows/macOS com Python 3.10 | **CONFIRMED** no código; último run em `main` = `success` em `c6ca6c4` |
| `tests/` (19 arquivos) | testes dos scripts empacotados (Godot headless, Defold, build report, asset tools) | REPORTED pelo `evals/RESULTS.md`; CI verde sustenta |
| `evals/triggers.json` (366 prompts) | 3 should-trigger + 1 near-miss por Skill, 30 combos, 20 que não precisam de Skill | CONFIRMED o arquivo existe e tem 366 entradas; **a medição** é deles |
| `evals/RESULTS.md` | precisão 0,945–0,984 · recall 0,963–0,979 · near-miss 91,1%→96,2% (Haiku) | REPORTED — julgaram modelos, **uma execução por célula**, não é estudo com usuários |
| `.claude-plugin/marketplace.json` | manifesto de marketplace de plugin | CONFIRMED presente; ampliação é o PR #58 |

## 7. Licença e atribuição (o aviso viaja com o payload?)

- `LICENSE` = **Apache-2.0** (texto lido, primeira linha e cabeçalho).
- `NOTICE`: "All skills in this repository are original works… authored from primary
  documentation… no text or code was copied" — declaração do autor, não verificável por nós.
- Marcas (Godot, Unity, Unreal, Phaser, PixiJS, three.js, Bevy, LÖVE, MonoGame…) declaradas
  como uso descritivo, sem afiliação.
- Consequência prática de reusar conteúdo: Apache-2.0 exige manter `LICENSE` + `NOTICE` e
  indicar mudanças; concede patente. **Não é parecer jurídico** — é o que o arquivo diz.
- O `NOTICE` **não viaja automaticamente** quando se copia uma pasta de Skill: a cópia leva só
  `SKILL.md` + `scripts/`. Quem copia tem de levar `LICENSE`/`NOTICE` junto.

## 8. Riscos (injeção, comando destrutivo, exfiltração)

| Risco | Avaliação |
|---|---|
| Injeção de instrução via Skill | Médio por natureza (Skill é instrução executável pelo agente). Aqui há mitigação incomum: seção de *trust boundary* no router e descrições que dizem o que **não** fazer |
| Injeção via conteúdo de projeto | Declarada como dado, não instrução — texto correto, mas nada impede o modelo de obedecer; a defesa real é do host |
| Comando destrutivo | Não encontrado nos scripts lidos; `generate-site.py` usa `shutil.rmtree` só em diretório de saída próprio |
| Exfiltração / rede | Nenhuma chamada de rede nas Skills |
| Cadeia de suprimentos na instalação | `npx` executa pacote do npm e altera diretório de configuração do agente; padrão de risco conhecido, mitigado por pacote de organização conhecida, não auditado por nós |
| Interesse comercial | README tem patrocinador com link de afiliado (`infistar.cc…?aff=…`) e slot pago; o texto afirma que patrocínio não afeta o roteamento — afirmação não verificável |
| Claims de validação | "Checked on the real engines" é do autor; o próprio `evals/RESULTS.md` declara o que **não** rodou: Unity Editor, Unreal Editor, Roblox Studio e builds C# do Godot |

## 9. Teste com entrada sintética (Nível 1) e o que ficou fora

**Nível 1 — local, isolado, sem rede depois do download, sem credencial.**

| Passo | Resultado |
|---|---|
| Baixar tarball do commit `c6ca6c4` e extrair em `/tmp` | 5,2 MB, 37 `.py` |
| Rodar o validador deles no próprio repositório | `Validated 80 skill file(s)… All checks passed` (exit 0) |
| Criar venv isolada e instalar `Pillow>=10,<14` | Pillow 13.0.0 |
| `asset_report.py` com PNG RGBA **todo opaco** + `--require-alpha` | exit **1**, problema: `alpha channel is fully opaque; no pixel is transparent` — pega "transparência falsa" |
| `asset_report.py` com PNG realmente transparente | exit **0**, `transparent_pixels: 4096` |
| `asset_report.py` com 32x48 e muitas cores | exit **1**, dois problemas: tamanho e contagem de cores |
| `build_preview_sheet.py` com os 3 PNGs | `Wrote sheet.png (3 assets, 4 columns)` (exit 0) |

Registro completo em `data/testing/test-log.tsv` (linhas de 2026-11-20).

**Não executado, e por quê:**

- Godot, Unity, Unreal, Defold, Roblox Studio: exigem instalar engine (GBs) e, no caso de
  Unity/Roblox, conta e licença — Nível 3, fora de escopo sem autorização.
- `scripts/run-trigger-evals.py`: precisa de um modelo juiz (API e cota); a medição de 98,7%
  continua sendo alegação do autor, com método declarado e reproduzível por quem tiver juiz.
- Instalação via `npx skills add`: escreve na configuração de agente do host (Nível 3).

## 10. Aplicação: usar, adaptar, reimplementar ou referenciar

**O que serve à Lia, em ordem de valor:**

1. **Regras de autoria de Skill** (`docs/SKILL-FORMAT.md` + `validate-skills.py`): descrição que
   nomeia vizinhos, teto de linhas, `## Gotchas` obrigatório, índice para referência longa,
   orçamento de caracteres das descrições. Isso responde direto ao problema registrado em
   `LR-AGENT-009` (manifesto de Skill) e `LR-AGENT-010` (pacote ArtCraft).
2. **Pipeline de asset com porte de qualidade** (`create-game-assets`): brief de direção de arte →
   manifesto por asset (fonte, licença, aprovação, `technical_checks_passed`) → normalização
   determinística → QA de raster (alfa falso, tamanho, cores) → validação dentro do jogo. Casa com
   `cross-project/licensing/ASSET-PROVENANCE-REGISTRY.md`.
3. **Roteador de Skills**: detectar engine/contexto e carregar 2–3 Skills, com regra de
   propriedade quando duas Skills reivindicam o mesmo pedido.
4. **Método de teste**: teste headless dentro da Skill (o agente prova o que escreveu) e eval de
   disparo com *near-misses* — o mesmo desenho do nosso `governance/TESTING-PROTOCOL.md`.
5. **As 79 Skills em si**: só fazem sentido se o Lia Studio usar um dos 12 engines. Não há
   pesquisa nesta base que diga qual engine o Studio usa; importar o pacote por precaução seria
   inflar contexto sem uso (ver `LR-AGENT-009` sobre custo de Skills não usadas).

## 11. Evidências

| Afirmação | Rótulo | Ponteiro |
|---|---|---|
| Repositório existe, `main` em `c6ca6c4`, 9.651★, Apache-2.0 na API | CONFIRMED | `gh api repos/gamedev-skills/awesome-gamedev-agent-skills` (2026-11-20) |
| `LICENSE` é Apache-2.0 e há `NOTICE` com atribuição | CONFIRMED | `repo@c6ca6c4:LICENSE`, `:NOTICE` |
| 80 `SKILL.md`, distribuição 16/15/12/9/9/6/6/5/1 | CONFIRMED | árvore do commit (`git/trees?recursive=1`) |
| Validador do próprio repo passa | CONFIRMED (execução nossa, Nível 1) | `python3 scripts/validate-skills.py` → exit 0 |
| `asset_report.py` detecta transparência falsa, tamanho e cores | CONFIRMED (execução nossa, Nível 1) | `data/testing/test-log.tsv`, 2026-11-20 |
| Scripts de Skill não fazem chamada de rede | CONFIRMED | varredura `skills/**/*.py` no tarball |
| Versões pinadas são releases reais (Godot 4.7.2, Ebiten 2.10.6, Bevy 0.20.1, Phaser 4.2.1, three r187, Defold 1.14.1, Luau 0.746) | CONFIRMED | `gh api repos/<org>/<repo>/releases/tags/<tag>` (2026-11-20) |
| "Checked on the real engines" para 10 de 12 | REPORTED | `evals/RESULTS.md` §3, com a lista do que não rodou |
| 98,7% de disparo correto em 366 prompts | REPORTED (medição do autor, modelo juiz, 1 execução por célula) | `evals/RESULTS.md` §1 |
| CI verde no `main` | CONFIRMED (API de runs) | `actions/runs` → `c6ca6c4` `push main success` |
| Patrocínio não afeta roteamento | UNVERIFIED | README §Sponsors |
| Skills são obra original, sem cópia de terceiros | REPORTED | `NOTICE` |

## 12. Recomendação (opinião técnica)

**`ADAPT`.** Adaptar quatro coisas: (a) as regras de autoria e o validador de Skill; (b) o
pipeline de asset com manifesto e QA de raster; (c) o padrão de roteador com regra de
propriedade; (d) o hábito de teste headless dentro da Skill.

Não adotar o pacote inteiro: 79 Skills de 12 engines são contexto pago antes de haver uso, e
nesta base não existe evidência de qual engine o Lia Studio vai usar. Copiar as Skills agora
seria inflar o agente para resolver um problema hipotético.

Licença permite o reuso (Apache-2.0 + NOTICE). Isso **não** é autorização de adoção: quem
decide se o Studio usa um desses engines, e se o pipeline entra no Forge, é o proprietário e o
responsável do projeto.

## 13. Próximos passos

1. Rodar `validate-skills.py` contra as Skills `lia-*` reais (exige cópia read-only das 5 pastas
   de Skills dos projetos; hoje não estão nesta base) e medir quantas regras falhariam —
   insumo direto para `LR-AGENT-009`.
2. Testar `create-game-assets` com um asset real do Forge: manifesto + `asset_report.py` +
   contact sheet, e comparar com o registro de proveniência que já existe.
3. Se o Studio escolher Godot 4.7 ou Unity 6.3, reavaliar o subconjunto de Skills daquele
   engine e só então estudar instalação — em diretório isolado, nunca na configuração do agente.
4. Revisar em 2027-02-20: Skills de engine envelhecem junto com o engine, e o repositório tem
   3 PRs abertos que mudam estrutura (marketplace de plugins).

## Reauditoria 2026-11-20

| Campo | Valor |
|---|---|
| Versão anteriormente analisada | `— (primeira análise em 2026-11-20)` |
| Versão novamente examinada | ``c6ca6c41c839`` (2026-11-20) |
| Método | `compare` da API do GitHub (commits + arquivos), leitura de arquivos materiais no HEAD, estado de CI no HEAD, releases |
| Mudanças encontradas | Não é reauditoria: o objeto entrou nesta rodada (`LR-STUDIO-006`) e já nasceu com SHA, teste próprio e conferência de versões. |
| Evidências novas | Duas execuções Nível 1 registradas no log (validador do repo e `asset_report.py`). |
| Testes próprios | **Executado**: validador (80 Skills, exit 0) e QA de raster (3 casos). |
| Testes independentes | CI no HEAD: *success* em `c6ca6c4`. |
| Conclusão | Recomendação `ADAPT` definida hoje; sem reavaliação anterior. |
| Próxima revisão | 90 dias. |


Voltar: `RESEARCH-INDEX.md` · `catalog/catalog.tsv` · `cross-project/licensing/ASSET-PROVENANCE-REGISTRY.md`
