# RealtimeTTS (KoljaB) — streaming de TTS por engine, com uma lição de fronteira de licença

| Campo | Valor |
|---|---|
| ID | `LR-VOICE-002` |
| Nome | KoljaB/RealtimeTTS |
| Tipo | repositorio |
| Fonte oficial | https://github.com/KoljaB/RealtimeTTS · PyPI `realtimetts` |
| Responsável | Kolja Beigel e colaboradores |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | LOCAL_TESTS_PASS |
| Recomendação | **REFERENCE_ONLY** |
| Decisão de adoção | — nenhuma registrada |
| Categoria | voice |
| Projetos beneficiados | Lia-Project (voz PT-BR), Lia Model Lab (fronteira engine × pesos) |
| Versão analisada | commit `7443092f11bb52b71f85b11075472024ae894924` (master, 2026-11-10T16:43Z) · PyPI `0.8.10` (2026-09-27) |
| SHA completo | `7443092f11bb52b71f85b11075472024ae894924` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — HEAD de `master` na coleta |
| HEAD atual | `7443092f11bb52b71f85b11075472024ae894924` |
| Data | 2026-11-22 |
| Última verificação | 2026-11-22 |
| Upstream conferido | 2026-11-22 · HEAD `7443092f` em `master` · `pushed_at` do repositório é de branch de feature, não da master |
| Próxima revisão | 2027-02-20 |
| Licença | **duas, conforme o artefato**: MIT no wheel 0.8.10 do PyPI; Apache-2.0 no `LICENSE` da master desde 2026-11-10 (`CONFIRMED` nos dois) |
| Confiança | Alta para execução e licença; Alta para a fronteira engine × pesos |

---

## 1. O que é, e por que entrou nesta base

Biblioteca que transforma texto em áudio **em streaming**, delegando a síntese a um conjunto de
engines: 37 arquivos em `RealtimeTTS/engines/` e 30 páginas em `docs/engines/` (Azure, ElevenLabs,
OpenAI, Coqui, Kokoro, Piper, Edge, gTTS, Chatterbox, Higgs, Orpheus, Parler, Qwen, LuxTTS, PocketTTS
e mais). ★4.059 · 420 forks · 132 issues · criado 2023-08-26.

É diretamente o assunto do Lia-Project: o digest `cross-project/voice/VOICE-STACK-DIGEST.md` registra
que existe runtime supervisionado de TTS local com Kokoro, que a latência por frase está `BLOCKED` e
que "Comparação Kokoro existente × alternativas" está `NOT RUN` com a regra *medir antes de
adicionar*. Este relatório não adiciona engine: registra o que o wrapper faz com a fronteira de
licença — que é a parte transferível.

## 2. Executado nesta sessão (nada de rede, nenhuma chave, nenhuma fatura)

Ambiente: sandbox Linux, CPython 3.11.2.

| Etapa | Resultado |
|---|---|
| `pip install "RealtimeTTS==0.8.10"` | sucesso; core **mínimo**: `pydub`, `resampy`, `stream2sentence` apenas |
| `import RealtimeTTS` | **ok** em Python 3.11; `__version__ = 0.8.10` |
| metadado do wheel | `License: MIT`, sem classifier de licença; `dist-info/licenses/` traz `LICENSE` (**MIT License**) e `LICENSING_ADDENDUM.md` |
| suíte de testes da master, com os **mesmos** passos de dependência do CI deles (`pytest`, `setuptools>=68`, `numpy`, `requests`, `fastapi`, `httpx`, `soundfile`) | **319 passed**, 6 failed, 21 erros de coleta, 14 skipped, 5.41 s |
| triagem dos 6 failures | todos terminam em `ModuleNotFoundError: No module named 'pyaudio'` / `ImportError: RealtimeTTS local playback requires PyAudio. Install 'realtimetts[playback]' and, on Linux/macOS, install PortAudio first` |
| por que o CI deles está verde | o `ci.yml` roda `sudo apt-get install portaudio19-dev` + `pip install pyaudio` + `pip install -e ".[openai]"`. **Não instalei PortAudio nem PyAudio** (sem apt/sudo: é instalação de ferramenta de sistema, fora do escopo) |

Resultado honesto: **a biblioteca funciona e importa no ambiente**; o que falhou é um extra de
playback local que exige pacote de sistema. Os 21 erros de coleta são testes de engines com extras
ausentes (`azure_test.py`, `coqui_test.py` etc.). `tests/` tem 121 entradas: **55** `test_*.py` — o que a
config deles coleta, dado `python_files = [test_*.py]` —, **30** `*_test.py`, que são scripts manuais de
demonstração com credenciais e que o próprio pytest do projeto **não** coleta, 15 outros `.py` e 21
arquivos de dados (wav/json).

## 3. A descoberta central: **a licença viaja com o artefato, não com o repositório**

| Artefato | Licença | Evidência |
|---|---|---|
| wheel/sdist `realtimetts 0.8.10` (PyPI, 2026-09-27) | **MIT** | `LICENSE` dentro de `dist-info/licenses/` abre com "MIT License"; metadado `License: MIT` |
| `LICENSE` na `master` @ `7443092f` (2026-11-10) | **Apache-2.0** | texto Apache; commit "Relicense RealtimeTTS under Apache-2.0" (PR #398) |
| README, seção License | os dois | "RealtimeTTS's own source code is licensed under the Apache License 2.0… **Releases up to and including 0.8.10 were published under the MIT License**" |

Detalhe fino que só aparece abrindo os arquivos: o `LICENSING_ADDENDUM.md` na master já diz *"The
'Software' licensed under the Apache License 2.0…"*, enquanto o mesmo arquivo **dentro do wheel** diz
*"…under these MIT terms…"*. Ou seja, os dois textos coexistem corretamente por versão — e **a versão
no repositório não foi bumpada**: `_version.py` continua `0.8.10` na master. Um auditor que consultar
`main`+PyPI sem ler o texto vai errar em uma das duas direções.

Consequência operacional para o Lia: o registro de licença de qualquer dependência precisa de
**três** coordenadas — artefato (wheel × repositório), versão e data — com URL. "MIT" sozinho, como
campo de catálogo, é insuficiente mesmo em projeto bem-intencionado e bem documentado.

## 4. O `LICENSING_ADDENDUM.md`: o mecanismo que a Skill do Hub precisa copiar

Texto lido (curto e literal): a licença cobre **só o código da biblioteca**; as engines, pesos,
vozes, latentes de voz, áudio de referência, datasets e APIs hospedadas **não** são parte do
"Software", **não** são distribuídos com ele e continuam sob as próprias licenças e termos — e o
Apache/MIT "does not extend to, nor release you from checking and complying with" esses termos. Lista
duas obrigações do usuário: entender as restrições de cada engine (uso comercial, atribuição,
share-alike) e obter licenças/permissões diretamente dos provedores. Fecha com: "That information is
for guidance only and does not constitute legal advice… verify the upstream terms for the exact
package, model and revision you ship."

É **exatamente** a lacuna do ecossistema Lia, resolvida em um arquivo de 1,1 KB:

| Situação Lia | Situação RealtimeTTS |
|---|---|
| 47 de 48 Skills sem licença no payload; marca "alethe" com assets fora da licença MIT | adendum explícito dizendo o que a licença **não** cobre |
| pesos/vozes de TTS usados pelo Lia-Project sem registro de fronteira | lista por engine em `docs/engines/` |
| catálogo do Hub com `license.status: unknown` | README com o aviso e o pointer por arquivo |

Contrapeso medido, para não idealizar: **só 3 das 30 páginas de engine** (`higgs.md`, `inflect.md`,
`qwen.md`) contêm a palavra "license". Piper, Kokoro, Coqui, Edge e as demais **não** têm nota de
licença na própria página — a promessa do adendo ("start with `docs/engines/`") está à frente da
cobertura real. Padrão certo, preenchimento parcial: 3/30.

## 5. Português (BR): o que dá para afirmar do que foi lido

- `RealtimeTTS/language_router.py` normaliza `"pt"`, `"pt-br"`, `"pt-pt"` e `"portuguese"` para a
  chave `portuguese` — lido no **wheel instalado**, linhas 102–106;
- `engines/kokoro_engine.py` trata português brasileiro explicitamente (`return "p"  # Brazilian
  Portuguese` em três pontos, incluindo a seleção de voz por `lang_code='p'`);
- `docs/engines/kokoro.md`: "plus Spanish, French, Hindi, Italian, and **Brazilian Portuguese**
  prefixes"; `docs/engines/modelslab.md` menciona Portuguese;
- o README declara docs em 10 idiomas humanos, incluindo `docs/pt/index.md`.

O que **não** está aqui: qualidade de PT-BR, latência, e qual engine entrega o quê. Nada foi
sintetizado — sem áudio, sem GPU, sem chaves. O digest da base mantém `PT-BR de qualidade: não
provado com métrica` (`UNVERIFIED`) e `Latência de TTS por frase (p50/p95): BLOCKED`, e este relatório
**não altera** nenhum dos dois.

## 6. Padrões aproveitáveis

1. **Adendume de escopo de licença** (§4) — um arquivo curto dizendo o que a licença não cobre, com
   pointer por componente. Aplicável ao Hub e a qualquer Skill que chame serviço pago.
2. **o verificador de release do projeto (2.074 linhas) testado por 3 suítes** (`test_release_guard.py`,
   `test_release_guard_cli.py`, `test_release_guard_cpu_macos.py`, `test_public_cpu_release_profile.py`):
   cada perfil de engine declara `service_required`, `required_dependencies` com **versão fixada**
   (ex.: `realtimetts-qwen-native-cpu: 0.4.1`), `required_wheel_platforms` e
   `required_native_library_groups` — e a publicação falha se o artefato não bate. Isso é o análogo
   exato do que falta ao `agents/PUBLISHING-PROTOCOL.md` desta base: **gate de publicação como
   asserção de versão por artefato**.
3. **Extras por engine** (`pip install "realtimetts[kokoro]"`, `[playback]`, `[openai]`): o core
   instala 3 dependências em vez das 497 linhas de `requires_dist` completas do metadado —
   fronteira de instalação declarada, não prometida.
4. **Matriz de CI em 5 versões de Python** (3.10–3.14) com `fail-fast: false`: um ambiente velho ou
   novo demais é sinal, não bloqueio.
5. **Contrapeso**: o CI do projeto lista 41 arquivos de teste nominalmente, dos 55 `test_*.py`
   existentes — 14 ficaram fora (`test_callbacks.py`, `test_piper_engine.py`,
   `test_incremental_text_feed.py`, `test_qwen_cpu_topology.py`…). Lista explícita dá controle; também
   cria o modo de falha "teste escrito, nunca executado".

## 7. Limitações e riscos

- **Sem áudio gerado nesta sessão.** Nenhuma engine foi executada — as que precisam de chave estão
  `BLOCKED`, as locais precisam de pesos/PortAudio ausentes. Nada aqui mede qualidade, latência ou
  custo.
- **AMD/RX 580: nada afirmado.** As engines locais têm requisitos próprios (Coqui/XTTS exigem
  PyTorch/CUDA; Kokoro tem caminho CPU/ONNX). Nenhum requisito foi testado contra o hardware do
  usuário, e **não** se transfere requisito de uma engine para a biblioteca.
- A migração MIT → Apache-2.0 **sem bump de versão** (§3) é um risco de suprimento real para quem
  fixa "0.8.10": o mesmo número pode significar duas licenças diferentes conforme a origem.
- `pyaudio`/PortAudio como dependência de sistema no caminho local: em sandbox restrito isso é
  barreira de ambiente, não defeito — mas é a razão pela qual a suíte não roda verde fora do CI deles.

## 8. Recomendação

**`REFERENCE_ONLY`** — referência de **prática de fronteira de licença** e de **gate de publicação**;
nenhuma adoção de dependência por este relatório. O motivo de não ser `ADAPT`: o Lia-Project já tem
runtime de TTS próprio documentado, e a regra da base é medir antes de adicionar — não há medição
nova aqui que justifique trocar ou acrescentar engine. O que vale levar não é o pacote, são os dois
artefatos dele: o adendo (§4) e o release guard (§6.2).

Se um dia o Lia distribuir um produto que empacote engines de TTS, a obrigação de verificar licença de
cada engine/peso/voz revisada **é do projeto que publica**, não desta pesquisa — e o texto do adendo
deve ser lido como alerta de escopo, não como modelo de cláusula (`REQUIRES_LEGAL_REVIEW`).

## 9. Evidências

| Afirmativa | Rótulo | Base |
|---|---|---|
| install do wheel ok; import ok em 3.11; core = 3 dependências | `OBSERVED` | venv desta sessão |
| 319 passed / 6 failed / 21 erros / 14 skipped em 5.41 s, na forma do CI deles | `OBSERVED` | `pytest` no clone da master, sem PortAudio/PyAudio |
| os 6 falham por `pyaudio` ausente | `OBSERVED` | traceback das duas suítes |
| CI deles instala `portaudio19-dev` + `pyaudio` + `.[openai]` e lista 41 arquivos nominalmente | `CONFIRMED` | `.github/workflows/ci.yml` na master |
| wheel 0.8.10 é MIT; master é Apache-2.0; `_version.py` ainda 0.8.10 | `CONFIRMED` | `dist-info/licenses/LICENSE` × `LICENSE` do repo × `RealtimeTTS/_version.py` |
| addendum no wheel fala "these MIT terms", na master fala "Apache License 2.0" | `CONFIRMED` | os dois textos, lado a lado |
| adendo de escopo (engines, pesos, vozes fora da licença) | `CONFIRMED` | `LICENSING_ADDENDUM.md` lido |
| `pt`/`pt-br`/`pt-pt` normalizados no roteador de idioma | `CONFIRMED` | `language_router.py:102-106` no wheel |
| Kokoro com `lang_code 'p'` = Brazilian Portuguese | `CONFIRMED` | `engines/kokoro_engine.py`, três pontos |
| nota de licença em só 3 das 30 páginas de engine | `CONFIRMED` | busca por `licen` em `docs/engines/` |
| release guard com versões fixadas por perfil | `CONFIRMED` | arquivo de verificação de release no repositório upstream (2.074 linhas) |
| qualidade/latência de PT-BR; custo por engine | `BLOCKED` | nenhum áudio gerado, nenhuma chave |
| comportamento em AMD/RX 580 | `UNVALIDATED` | nada testado neste hardware |
| run verde na master `7443092f` (2 runs, success) | `CONFIRMED` | API `actions/runs?branch=master`, 2026-11-22 |

## 10. Próximos passos

1. Copiar o **formato** do adendo para o Hub (arquivo curto declarando o que a licença da Skill não
   cobre: modelos, vozes, marcas, assets) e para `projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md`.
2. Registrar no catálogo que **licença é por artefato**: nenhuma linha de `catalog/catalog.tsv` deve
   dizer só "MIT"/"Apache-2.0" sem versão+data+URL — é a regra que este objeto obriga.
3. Para o Lia-Project: nada muda na stack de voz por este relatório. A lacuna "Kokoro × alternativas"
   continua `NOT RUN` e exige medição, não leitura.
4. Revisão em 2027-02-20, gatilho objetivo: saída de `0.9.x` (existem `v0.9.0rc1…rc7` como branches
   de release no histórico de CI), o que deve coincidir com o Apache-2.0 publicado.

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · `cross-project/voice/VOICE-STACK-DIGEST.md` · `catalog/CATALOG-SCHEMA.md`.
