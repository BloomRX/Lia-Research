# VoiceStudio (debpalash) — 931 arquivos de teste, 262/262 ações pinadas por SHA, e o aviso de que pesos não são AGPL

| Campo | Valor |
|---|---|
| ID | `LR-VOICE-003` |
| Nome | `debpalash/VoiceStudio` — "AI voice studio. On your device." (clone, design, dub, dictate, transcribe, narrate) |
| Tipo | repositório |
| Fonte oficial | https://github.com/debpalash/VoiceStudio · site `voicestudio.sh` · `app.voicestudio.sh` (Cloud) |
| Responsável | `debpalash` (indivíduo); tiers Pro e Cloud anunciados no README; `SPONSORS.md` na raiz |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | PARTIAL |
| Recomendação | **ADAPT** — sugestão ao dono: levar o conjunto de higiene de fornecedura (testes que provam pinos, verificador semanal que resolve o SHA pela API, `LICENSE-NOTICE.md` explícito) |
| Decisão de adoção | — nenhuma registrada |
| Categoria | produto concorrente de voz + política de supply chain |
| Projetos beneficiados | Lia Voice Input (o concorrente direto mais próximo), Lia Studio (empacotamento e assets de modelo), Lia Forge (CI de release multi-plataforma + AUR + Play), Lia Model Lab (pin de revisão de pesos), Lia Research (o LICENSE-NOTICE como formato) |
| Versão analisada | `v0.5.8` (release 2026-11-12) · criado em 2026-04-09 |
| Proveniência do conteúdo | **medido por nós** (API + clone raso filtrado por sparse-checkout + execução de dois arquivos de teste do fornecedor); o comportamento do app não foi observado |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · `gh api repos/debpalash/VoiceStudio` + `contents/.github/workflows` + clone `--depth 1 --filter=blob:none --sparse` |
| Upstream conferido | 2026-11-24 · 35 arquivos YAML entre `.github/workflows` e `.github/actions`; censo próprio de `uses:` (ver §4) |
| Próxima revisão | 2027-02-24 |
| Licença | **AGPL-3.0-only**, com `LICENSE-NOTICE.md` dizendo que isso **inclui uso comercial e interno** da aplicação, e que **pesos de modelo, tokenizers e outros assets de terceiros retêm seus próprios termos** (`CONFIRMED` pela leitura dos dois arquivos) |
| Confiança | Alta para os arquivos de CI/licença lidos e para a execução parcial da suíte; nenhuma para qualidade de áudio/TTS, que não testei |

---

## 1. Por que este objeto entrou na base

É o projeto mais estrelado da leva inteira (117.344★, 13.086 forks) e, ao mesmo tempo, o que tem
**menos issues abertas por estrela** (22 issues para 117 mil estrelas — medido no mesmo instante que os
outros sete). Para o `lia-voice-input` ele é três coisas: um concorrente direto com o mesmo posicionamento
("on your device"), um exemplo de como se empacota TTS/ASR local para desktop **e** celular sem perder a
licença aberta, e — o que mais interessa à Research — **a demonstração de que higiene de fornecedura pode
ser um corpo de testes**, não uma política em PDF.

## 2. O objeto medido

| Campo (API) | Valor |
|---|---|
| Estrelas / forks / issues abertas | 117.344 / 13.086 / **22** |
| Criado / último push / release | 2026-04-09 / ativo em 2026-11-24 / `v0.5.8` (2026-11-12) |
| `size` | 219.996 KB |
| Idiomas | Python 55,3 % · TypeScript 25,5 % · Swift 6,0 % · Kotlin 5,9 % |
| Workflows | **34** arquivos em `.github/workflows` |
| Arquivos em `tests/` | **939** entradas, das quais **931** `.py` |
| Arquivos com "pin" no nome, em `tests/` | **19** |
| Raiz | .agents/, .claude/, .coderabbit.yaml, .dagger/, .gitattributes, .github/, .gitleaks.toml, .gitleaksignore, .gitmodules, .nvmrc, .python-version, AGENTS.md, CHANGELOG.md, CLAUDE.md, LICENSE, LICENSE-NOTICE.md, Makefile, README.md, SPONSORS.md, alembic.ini, bun.lock |
| Submódulo | `.gitmodules` → `omnivoice-gallery` apontando para `github.com/debpalash/omnivoice-gallery` |
| README | 20 traduções linkadas (EN + 19, incluindo `README_PT.md`) sob marcadores `README_LANGUAGES_START/END`; tiers `VoiceStudio Pro` e `VoiceStudio Cloud` |

Das 34 workflows medidos pelo nome, quatro não são de build e sim de política: `action-contracts.yml`,
`action-pin-verify.yml`, `cancel-closed-pr-runs.yml`, `commit-identity.yml`, mais três de CLA
(`cla.yml`, `cla-backfill.yml`, `cla-reminders.yml`). O resto cobre o produto: `aur-package.yml` (Arch),
`android-play-internal.yml`, `android-repository.yml`, `build-omnivoice-tts.yml`, `ci.yml`.

## 3. A licença, lida nos dois arquivos

`LICENSE` é a AGPL-3.0 padrão (cabeçalho lido: "GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November
2007"). O `LICENSE-NOTICE.md` é o que importa, e ele resolve as duas perguntas que sempre aparecem em
produto de IA:

1. **uso comercial**: "That **includes commercial and internal business use** of the application itself."
2. **assets**: "Model weights, tokenizers, and other third-party assets **retain their own terms**."
3. e a obrigação AGPL de rede, explicitada para quem instala o servidor.

Isso é o oposto do `LR-MODEL-009` (Breeze TTS 2: código Apache-2.0 × pesos não comerciais sem texto
próprio) e do `AppFlowy-SelfHost-Commercial` (sem LICENSE algum). É o formato que eu recomendo para o
Lia Studio no `decisions/PENDING/` que trata de assets: **um arquivo curto ao lado do LICENSE dizendo
onde termina o código e começam os pesos**, em vez de deixar o leitor adivinhar.

## 4. O corpo de testes de pinos (o achado)

O que medimos por conta própria, sem acreditar em nenhum README — censo de `uses:` em todos os YAML de
`.github/workflows` + `.github/actions`:

| Medida | Valor |
|---|---|
| Arquivos YAML varridos | 35 |
| Referências `uses:` encontradas | 278 |
| Referências a ações remotas (`owner/repo@…`) | **262** |
| Delas, terminando em SHA de 40 hex | **262 (100 %)** |
| Referências flutuando em tag (`@v4`, `@main`) | **0** |
| Ações distintas | 34 |
| Mais usadas | `actions/checkout` 66 · `actions/upload-artifact` 29 · `actions/setup-node` 17 · `astral-sh/setup-uv` 15 · `actions/cache/save` 15 |

E executei os dois arquivos de teste que provem isso. Ambiente: venv Python 3.11.2 com `pytest` +
`pyyaml`, clone raso com sparse-checkout de `tests/`, `.github/`, `scripts/` (sem o código da aplicação —
o que importa para o resultado):

```
python3 -m pytest tests/test_workflow_action_pins.py tests/test_actions_pinned.py -q --noconftest
→ 20 passed, 1 skipped in 2.83s
SKIPPED [1] tests/test_workflow_action_pins.py:291: set VOICESTUDIO_VERIFY_ACTION_PINS=1 to resolve pins over the network
```

Com o `conftest.py` do projeto ativo, a coleta quebra com `ModuleNotFoundError: No module named
'services'` — é consequência **do meu sparse-checkout**, não do projeto: o `tests/conftest.py`
(linha 716 lida) importa o pacote da aplicação para montar fixtures compartilhadas. Registro as duas
coisas separadamente porque a primeira é um resultado e a segunda é uma limitação minha. Quando acrescentei
os outros quatro arquivos de pin (`test_verify_action_pins.py`, `test_node_version_pin.py`,
`test_bun_toolchain_pins.py`, `test_omnivoice_revision_pin.py`), obtive 29 passed / 5 failed / 6 errors,
e **todas** as falhas e erros são o mesmo `No module named 'services'` — nenhuma falha de conteúdo.
Resultado total: **os 20 testes que não precisam da aplicação passam**.

## 5. Por que esses testes existem (docstring transcrita, é o argumento todo)

De `tests/test_workflow_action_pins.py` (303 linhas, texto lido):

> "The workflows are copied from each other, so a bump applied to one file left the rest on the old pin:
> `actions/checkout` ran at v7.0.1 in 61 places and at v4.4.0 or v5.0.0 in four, `actions/setup-python`
> at v7.1.0 everywhere except the recipe job (v5.6.0), and `astral-sh/setup-uv` at v6.8.0 in ten places
> and v3.2.4 in seven. **A pin that only some jobs get is a pin nobody can reason about.**"
>
> "References are found by **parsing the YAML** of every workflow and composite action and collecting each
> value under a `uses` key (aliases resolve), not by scanning text, so quoting, flow style, anchors and
> `uses : x` spacing cannot hide one and a `run:` script that mentions `uses:` is never mistaken for one."

E o que o teste *não* consegue provar, declarado no cabeçalho de `action-pin-verify.yml`:

> "The pin tests … prove every `uses:` is a full SHA and carries a version label. They **cannot prove the
> SHA _is_ the commit that label names** — that needs the GitHub API, which PR CI must not depend on — so a
> pin swapped for a well-formed SHA of a different commit would pass review. This weekly run resolves each
> distinct action/label pair…"

Três decisões de projeto dignas de cópia, todas medidas: (a) o teste é **estático sobre YAML**, roda em
qualquer máquina, sem rede; (b) a verificação que **precisa** de rede é um job semanal separado, não um
gate de PR; (c) a limitação do método está escrito junto do método.

## 6. Os outros 15 "pin tests" (o que o conjunto cobre)

Pelos nomes medidos em `tests/`: `test_download_dns_pinning.py` (fixar resolução DNS no download de
assets), `test_published_image_path_is_pinned.py` (a imagem publicada aponta para um digest),
`test_omnivoice_revision_pin.py` (revisão de modelo curada), `test_rocm_torch_pins_match_pyproject.py` e
`test_windows_rocm_recipe_pin.py` (o pin do torch por plataforma tem de bater com o `pyproject.toml`),
`test_node_version_pin.py`, `test_bun_toolchain_pins.py`, `test_gallery_pin.py`, `test_share_pin_guard.py`,
`test_beartype_claw_pinned.py`, `test_pedalboard_sigill_pin.py` (workaround de crash de sinal por versão),
`test_verify_action_pins.py`, `test_workflow_action_pins.py`, `test_actions_pinned.py`,
`test_failure_ansi_stripping.py` e `test_ffmpeg_banner_stripping.py` (saída de ferramenta normalizada
antes de virar log).

O `test_omnivoice_revision_pin.py` tem a melhor docstring para o problema do Lia Model Lab:

> "Backward compatibility: a user who already has an OmniVoice snapshot (recorded in `refs/main` by an
> older install) keeps loading it offline, with no multi-GB re-download to the curated pin."

Ou seja: pinar a revisão do peso **e** manter o cache antigo válido — as duas metades que a maioria dos
projetos implementa só pela primeira.

## 7. O que mais foi lido e vale registro

- `.gitleaks.toml` + `.gitleaksignore`: segredo em diff é verificação, com arquivo de exceções **visível**;
- `.coderabbit.yaml`: revisão de IA configurada por arquivo versionado;
- `.dagger/`: pipeline de build como código Dagger, dentro do repo;
- `commit-identity.yml` + `cla.yml` + `cla-backfill.yml` + `cla-reminders.yml`: identidade de commit e CLA
  com *lembretes* e *backfill* — CLA tratado como processo contínuo, não como botão;
- `cancel-closed-pr-runs.yml`: fechar PR cancela os jobs — política de custo/energia na CI;
- `alembic.ini` + `Makefile` + `bun.lock` + `.python-version` + `.nvmrc`: dois toolchains (Python e
  Node/Bun) fixados por arquivo, cada um no lugar canônico;
- o badge `trendshift.io/repositories/28176` no topo do README é a única coisa no README que **não** é
  auto-elogio mensurável por nós: não verifiquei o ranking (§9).

## 8. Comparação direta com o `lia-voice-input` e com o `OpenWhispr`

| Aspecto | VoiceStudio (medido) | OpenWhispr (medido, `LR-VOICE-004`) | Lia hoje |
|---|---|---|---|
| Licença | AGPL-3.0-only + NOTICE de assets | MIT | ver `data/inventory/license-matrix.tsv` |
| Escopo | clone/dub/dictate/transcribe/narrate, "646 languages" | transcrição local com Whisper/Parakeet/Orukeet + nuvem | voz local PT-BR (digestão em `cross-project/voice/VOICE-STACK-DIGEST.md`) |
| Plataformas | desktop, servidor, **celular/tablet** (Swift + Kotlin) | desktop (Electron + JS/TS/Swift) | desktop (Tauri) |
| Testes | 931 arquivos Python | não medido arquivo por arquivo | 33 execuções nossas registradas em `data/testing/test-log.tsv` (2026-11-24) |
| Pins de CI | 262/262 em SHA + verificador semanal | workflows por plataforma + `lockfile-lint.yml` + `codeql.yml` | nenhuma checagem de pin hoje |
| Assets de modelo | revisão pinada + cache retrocompatível | modelos locais (Whisper, Parakeet tdt-0.6b-v3) | decisão pendente no Model Lab |

## 9. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| A suíte completa de 931 testes | `BLOCKED` | exige o código da aplicação e o ambiente deles (uv + torch); eu quis justamente não instalar o projeto deles — clone raso filtrado e `--ignore` de nada pesado |
| Qualidade de áudio, latência, cobertura dos "646 idiomas" | `UNVALIDATED` | não executei o app; nenhum modelo baixado |
| Os `.dmg`/`.exe`/APK publicados | `NOT_RUN` | nenhum binário baixado nesta base (regra permanente) |
| Se o SHA de cada pin bate com a tag nomeada | `NOT_RUN` | é o que o job semanal deles faz; poderíamos replicar com a API, mas são 34 ações × 262 refs — fica para quando houver decisão de adotar o padrão |
| Ranking no Trendshift | `UNVALIDATED` | badge lido, página não aberta |
| `omnivoice-gallery` (submódulo) | `NOT_RUN` | é repositório de outro dono dentro do deles; não listado na matriz |
| Comportamento de rede do app Cloud/Pro | `NOT_RUN` | exige conta |

## 10. Recomendação: **ADAPT**

> **Escopo desta seção** — o que segue é recomendação técnica desta base, não instrução para nenhum app. Se vale, cabe e é possível implementar em cada projeto é decisão do dono (`MISSION.md` §3: o Research não aprova nada).

1. **Propor: transportar o padrão de teste estático de pin** (parse de YAML, contagem, rótulo de versão) para o
   Lia Forge, onde hoje não existe nenhuma checagem. Custo: um arquivo de teste, sem rede.
2. **Propor: transportar a separação PR-gate × verificação semanal** para qualquer CI que a Lia venha a ter com
   ações de terceiros — é exatamente a objeção "não chame a rede no teste de PR" respondida com design.
3. **Propor: transportar o `LICENSE-NOTICE.md`** como formato para o Lia Studio/Lia Model Lab (fronteira código ×
   pesos declarada em arquivo próprio, ao lado do LICENSE).
4. **Não recomendo adotar** o produto, o Cloud, nem o submódulo `omnivoice-gallery`; AGPL no servidor é decisão do
   dono, e o `omnivoice` em si é modelo com termos próprios que eu não li.
5. **Teste que fecha o §9 linha 4 sem nada novo**: rodar `test_verify_action_pins.py` com
   `VOICESTUDIO_VERIFY_ACTION_PINS=1` numa máquina com a árvore inteira — é nível 2, precisa de ambiente
   completo, e fica registrado como pendência, não como recomendação ao dono.

## 11. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| 117.344★ · 13.086 forks · 22 issues abertas · criado 2026-04-09 · v0.5.8 (2026-11-12) · `size` 219.996 KB · Python 55,3/TS 25,5/Swift 6,0/Kotlin 5,9 | `CONFIRMED` | `gh api repos/debpalash/VoiceStudio` + `releases/latest` + `languages` |
| 34 workflows; 35 YAML contando `.github/actions`; 939 entradas em `tests/`, 931 `.py`, 19 com "pin" no nome | `CONFIRMED` | `contents/.github/workflows` + `ls` no sparse checkout |
| Censo de pins: 278 `uses:`, 262 remotas, 262 em SHA-40, 0 em tag, 34 ações distintas | `CONFIRMED` | script próprio sobre os YAML do clone (não o teste deles) |
| `pytest` dos dois arquivos de pin: 20 passed, 1 skipped (skip = verificação por rede), exit 0 | `OBSERVED` | venv Python 3.11.2 + pytest/pyyaml no sandbox; linha em `data/testing/test-log.tsv` |
| Adicionando 4 arquivos de pin: 29 passed, 5 failed, 6 errors — todos `ModuleNotFoundError: No module named 'services'` por causa do meu sparse checkout | `OBSERVED` (o erro) / `CONFIRMED` (a causa, lida em tests/conftest.py:716) | saída do pytest no sandbox |
| `LICENSE-NOTICE.md`: uso comercial e interno incluído; pesos/tokenizers com termos próprios; obrigação AGPL de rede | `CONFIRMED` (texto) | `LICENSE-NOTICE.md` lido na raiz |
| Submódulo `omnivoice-gallery` → `debpalash/omnivoice-gallery` | `CONFIRMED` | `.gitmodules` lido |
| Docstring dos pinos ("a pin that only some jobs get…", parse de YAML) e o cabeçalho do job semanal | `CONFIRMED` | arquivos lidos no clone |
| O app faz o que o README afirma (646 idiomas, on-device) | `REPORTED` | só o README; nada executado |
| Qualidade acústica, consumo de VRAM, comportamento em PT-BR | `UNVALIDATED` | fora do que este sandbox pode medir |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · registro de execução:
`data/testing/test-log.tsv` (linha `LR-VOICE-003`) · par da mesma leva:
`repositories/openwhispr/REPORT.md` · política de credencial/segredo desta casa:
`cross-project/security/CREDENTIAL-AUDIT-DIGEST.md` · fronteira de assets:
`cross-project/licensing/SPLIT-LICENSE-SCAN.md`.
