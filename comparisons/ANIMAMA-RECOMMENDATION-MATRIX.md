# Matriz Animama → 5 projetos: o que a Lia leva são sete mecanismos, e nenhum linha de código

| Campo | Valor |
|---|---|
| ID | `LR-CMP-005` |
| Tipo | comparação/digest de recomendação entre objetos pesquisados na mesma rodada |
| Objetos cobertos | `LR-UI-006` (Animama), `LR-FORGE-024` (animama-avatar-converter) — e as bases internas `LR-HW-001`, `LR-HW-002`, `LR-AGENT-007`, `LR-CMP-004`, `LR-STUDIO-012` |
| Data | 2026-11-26 |
| Última verificação | 2026-11-26 · tudo que este documento afirma vem dos dois dossiês da rodada, que citam commit, caminho e comando |
| Estado da pesquisa | DOCUMENTED — com duas execuções locais nos dossiês (12 + 46 testes) e **nenhuma execução do produto** |
| Recomendação | ver §4; **nenhuma linha deste documento autoriza implementação** |
| Decisão de adoção | — nenhuma registrada |
| Licença | irrelevante para este documento (não incorpora nada); o estado por camada está em `LR-UI-006` §9 e `LR-FORGE-024` §5 |
| Confiança | Alta no que foi lido em código/doc/issue dos dois repositórios; **nula em desempenho na máquina da Lia** (sem GPU, sem Windows, sem Unity neste sandbox) |
| Próxima revisão | 2027-01-10 |

---

## 1. Por que este documento existe separadamente

A rodada pediu duas coisas que um dossiê por repositório não responde: **(a)** classificar cada achado em seis rótulos que o dono usa (`ADOPT`/`ADAPT`/`REIMPLEMENT`/`REFERENCE_ONLY`/`REJECT`/`NEEDS_VALIDATION`) e **(b)** dizer, por projeto, o que fazer com isso, ordenado por impacto, esforço, risco e prioridade. O §2 resolve a tradução de rótulos; o §4 é a matriz; o §5 é o que deliberadamente **não** está recomendado.

## 2. Dicionário de rótulos (pedidos × desta base)

Os seis rótulos do pedido não existem todos no vocabulário desta base (`tools/validate.py` → `RECS`), e o catálogo é gerado por casamento de substring. Para nada se perder na tradução:

| Rótulo do dono | Vocabulário desta base | Regra de uso nesta rodada |
|---|---|---|
| `ADOPT` | `DIRECT_INTEGRATION_CANDIDATE` | só com prova de licença **e** prova de execução. **Nenhum achado da rodada chegou aqui** — a licença do Animama (AGPL-3.0-only) barra por si |
| `ADAPT` | `ADAPT` | o mecanismo é levável sem o código; escrito do zero pela Lia |
| `REIMPLEMENT` | `INDEPENDENT_REIMPLEMENTATION` | peça pequena e fechada o bastante para valer refazer; usado uma vez (F10) |
| `REFERENCE_ONLY` | `REFERENCE_ONLY` | precedente documentado; não gera trabalho |
| `REJECT` | `REJECT` | não incorporar, com motivo (licença, plataforma ou ausência de caso de uso) |
| `NEEDS_VALIDATION` | `INSUFFICIENT_EVIDENCE` | o que exige execução que ainda não houve. Toda linha de desempenho deste documento está aqui, não em `ADAPT` |

## 3. Os 15 achados, com o que cada um exige para virar outra coisa

| # | Achado | Onde está a evidência | Classificação | O que falta para subir |
|---|---|---|---|---|
| F1 | `animaPoseClip/2.0` — beats nomeados + trilhas anatômicas em graus + `generated detail`; 2 MiB; decimais fixados por tipo de grandeza | `LR-UI-006` §5 (`clip_format.py:19`, `clipVocabulary.ts:35-52`, ADR 0014/0016, `wave-hello.json` de 6.852 B) | **ADAPT** | uma especificação escrita por nós, com o 1.0 deles como banco de teste de formato |
| F2 | CLI de autoria com verificação determinística + promoção a conteúdo incluído condicionada a aprovação por item **e** por licença | `LR-UI-006` §5 (tabela de comandos; `motion-authoring/checks.ts`; skill passos 3–4 e 9) | **ADAPT** | decidir se o Forge aceita "o validador manda, o agente obedece" |
| F3 | Capacidade facial detectada por nome de morph target (ARKit/SRanipal/Unified Expressions) e molas classificadas por semântica | `LR-UI-006` §3 (`arkitFaceCapability.ts`, `spring-bone/SpringBoneSemanticClassifier.ts`) | **ADAPT** | amostra de VRM reais para testar o casador de nomes |
| F4 | Otimizador de ativo caseiro que recusa o que não conhece + lista do que "nunca deve fazer" + verificação por PSNR | `LR-UI-006` §3 (docs de `vrm:optimize`, `--min-psnr 45`) | **ADAPT** (o padrão) | definir quais extensões o Forge conhece o bastante para aceitar |
| F5 | Instrumento de custo de quadro em GPU (`EXT_disjoint_timer_query_webgl2`) | `LR-UI-006` §8 (`effect-bench.mjs`, issue #660) | **INSUFFICIENT_EVIDENCE** para número; **ADAPT** para método | rodar na RX 580; sem isso nada aqui vira medida |
| F6 | Estado emocional persistente por canal (24 × `0..30`), grupo derivado, escala dupla estado↔representação, promover/rebaixar em par oposto | `LR-UI-006` §4 (`domain/emotions.py`, `primary_emotion_update.py`, `avatar-emotion.md`) | **REFERENCE_ONLY** | nada: a Lia não tem estado emocional, e esta base não propõe criar um |
| F7 | `remember` dentro do mesmo reply estruturado + projeção diária `.md` gerada de tabela no banco + limites numéricos de injeção + Reflection só com disparo humano + versões reversíveis | `LR-UI-006` §6 | **ADAPT** como **pergunta de viabilidade** ao Project | resposta do dono do Project sobre aceitar escrita de memória no turno |
| F8 | Banco de modelos com teto de custo, ensaio gratuito contra mock, juiz humano-cego com calibração e `plan` como dry-run de tokens/custo/tempo | `LR-UI-006` §7/§11 (docs de `benchmarks/README.md`, `scripts/evals/`) | **ADAPT** | portar a **forma** dos comandos para o Model Lab, não o código |
| F9 | Layout de prompt por provedor para cache, com harness que proíbe piorar a taxa de cache em qualquer caminho | `LR-UI-006` §7 (`prompt-caching.md:1-34`) | **ADAPT** | medir a taxa de cache da Lia hoje (ainda não medida) |
| F10 | Parser incremental de JSON campo-a-campo para falar antes de o objeto fechar, com parse final autoritativo | `LR-UI-006` §7 (`main_structured_response.py:159-500`) | **INDEPENDENT_REIMPLEMENTATION** | especificar a ordem de campos do schema da Lia; a peça é ~200 linhas |
| F11 | Armadilha do cofre no Windows: esperar a chave do Chromium em `Local State` antes de criar o cofre | `LR-UI-006` §11/F11 (`vault.ts:24-49`) | **ADAPT** (como nota de plataforma) | confirmar qual mecanismo de cofre o Project usa hoje |
| F12 | Inventário de licença **por arquivo** cobrindo os 5.953 blobs, com gate que falha se faltar entrada | `LR-UI-006` §9 (executado: `check_source.py` limpo + 12 testes OK) | **ADAPT** — imediato, é da própria Research | nada; é formato de documento nosso |
| F13 | Processo SPECS/PLANS/SDLC/GLOSSARY/AGENTS com 41 ADRs e revisão por tier de risco | `LR-UI-006` §11/F13 | **REFERENCE_ONLY** para os produtos, **ADAPT** parcial para a Research | decidir se algum ADR nosso ganha "decision basis" como campo |
| F14 | Qualquer linha de código/asset/peso do Animama dentro de um projeto Lia | `LR-UI-006` §9 | **REJECT** (AGPL-3.0-only + 5.953/5.953 `prepared-not-release-approved`) | nada. Reverter isto é decisão de licença do produto, não de pesquisa |
| C1–C6 | Práticas do conversor (checagem estática de "não usa rede", escrita atômica, recusar em vez de degradar, empacotamento duplo, `-nographics`, uso direto) | `LR-FORGE-024` §7 | **ADAPT** (C1–C4), **REFERENCE_ONLY** (C5), **REJECT** (C6) | C1 é a única com custo abaixo de uma tarde |

## 4. Matriz por projeto

Escopo declarado pelo dono: *a Lia pode se beneficiar disto em quê?* A coluna **Prioridade** ordena dentro do projeto; **Risco** é o risco de *agir* sobre a recomendação, não de ler.

### 4.1 Lia-Project

| Prioridade | Recomendação | Impacto | Esforço | Risco | Base |
|---|---|---|---|---|---|
| P1 | **F9** — medir a taxa de cache de prompt por provedor antes de mexer no layout de instruções; a regra deles ("uma mudança de layout não pode piorar a taxa em nenhum caminho") é a parte barata | alto (custo e latência de todo turno) | médio | baixo — é medição, não mudança | `LR-UI-006` §7 |
| P2 | **F10** — reply estruturado streaming com ordem de campos fixada, para o avatar falar antes de o JSON fechar | alto (é a latência percebida da voz) | médio | médio — mexe no contrato de saída | `LR-UI-006` §7 |
| P3 | **F11** — registrar a armadilha do cofre no Windows como nota de plataforma, independentemente do mecanismo escolhido | médio (evita um bug de perda de credencial) | baixo | baixo | `LR-UI-006` §11 |
| P4 | **F7** — a pergunta `remember` no mesmo turno: viável? desejável? o Project decide | médio-alto | alto | médio — toca política de memória existente | `LR-UI-006` §6 |
| P5 | **F5** — a pergunta "quanto custa a presença durante um jogo" tem instrumento análogo ao deles; rodar na RX 580 é o que fecha a lacuna H-2 | alto para a resposta, nenhum para o produto | alto (exige a máquina) | **nenhum** se for só medição | `LR-HW-002`, `LR-UI-006` §8 |
| — | **F6** | — | — | REFERENCE_ONLY: não gera trabalho | §4 |

### 4.2 Lia Forge

| Prioridade | Recomendação | Impacto | Esforço | Risco | Base |
|---|---|---|---|---|---|
| P1 | **F1+F2** — um formato de animação por trilhas agrupadas em beats, com verificação mecânica (limites, interseção, contato, oscilação) antes de salvar; é o que separa "agente gera animação" de "agente gera animação revisável" | alto | alto | médio — é especificação nova, não código deles | `LR-UI-006` §5 |
| P2 | **C1** — checagem estática de promessas do tipo "roda local, não envia nada" | médio | **baixo** | baixo | `LR-FORGE-024` §7 |
| P3 | **C2/C3** — saída atômica com retry e "recusar em vez de degradar em silêncio" nos exportadores | médio | baixo | baixo | `LR-FORGE-024` §3 |
| P4 | **F4** — otimizador de ativo que recusa extensões desconhecidas + lista explícita do que nunca deve fazer | médio | médio | médio — pode recusar ativos que hoje passam | `LR-UI-006` §3 |
| P5 | **F3** — casador de nomes de morph target, se o Forge algum dia aceitar VRM de terceiros | baixo hoje | médio | baixo | `LR-UI-006` §3 |
| — | **C6** | — | — | REJECT: não há caso de uso VRChat/Unity | `LR-FORGE-024` §7 |

### 4.3 Lia Studio

| Prioridade | Recomendação | Impacto | Esforço | Risco | Base |
|---|---|---|---|---|---|
| P1 | **F2** — o padrão "skill de autoria com validador + gate de promoção por item e por licença" encaixa no que o Studio já tem de skills e no censo de `LR-CMP-004` (43 pacotes em que dois validadores discordam) | alto | médio | médio — exige decidir o que o gate bloqueia | `LR-UI-006` §5, `LR-CMP-004` |
| P2 | **F1** — o mesmo formato de clip serve a animação 2D/espinha de sprite? pergunta aberta, não conclusão | médio | alto | médio | §3 |
| P3 | **C3** — recusar em vez de degradar, nos ferramentas de criação | médio | baixo | baixo | `LR-FORGE-024` §3 |
| — | **F10** | — | — | só se o Studio emitir fala estruturada; hoje não | §3 |

### 4.4 Lia Agent Hub

| Prioridade | Recomendação | Impacto | Esforço | Risco | Base |
|---|---|---|---|---|---|
| P1 | **F12** — inventário de licença por arquivo com gate de cobertura: são 5.953 entradas para 5.953 blobs, e o verificador precisa só de `git ls-files` + stdlib. É exatamente o formato `G`/`I` que o Hub e o `SPLIT-LICENSE-SCAN` procuram | alto | **baixo** | baixo | `LR-UI-006` §9 |
| P2 | **F2 (skills)** — 21 `SKILL.md` no Animama, **nenhum** com arquivo de licença ao lado: a licença vive no inventário por arquivo. É o terceiro modelo de licenciamento de skill que esta base cataloga (Anthropic: arquivo lateral; DeerFlow: nada; Animama: inventário central) | alto para o censo | baixo | baixo | `LR-CMP-004` |
| P3 | **C4** — empacotar o mesmo conteúdo para dois hospedeiros (aqui `.agents/skills/` + symlink `.claude/skills` + `agents/openai.yaml` por skill) | médio | médio | baixo | `LR-UI-006` §2, `LR-FORGE-024` §7 |
| P4 | **F7** — memória como arquivos versionados com recibos idempotentes: só o desenho, sem tocar na independência entre projetos (decisão preservada) | baixo-médio | alto | médio | `LR-UI-006` §6 |

### 4.5 Lia Model Lab

| Prioridade | Recomendação | Impacto | Esforço | Risco | Base |
|---|---|---|---|---|---|
| P1 | **F8** — forma do banco: `plan` (dry-run de tokens/custo/tempo antes de gastar), tetos `--max-calls`/`--max-usd` obrigatórios, ensaio gratuito contra mock + juiz stand-in, juiz cego com calibração (`export/import/pilot/waive`) e `cleanup` de bancos órfãos | alto | médio | baixo — é governança de experimento, e o Lab já é o projeto com o melhor registro de decisão | `LR-UI-006` §11/F8 |
| P2 | **F5** — rodar `effects:bench` na RX 580 é a única linha desta rodada que vira medida; sem rodar, fica `INSUFFICIENT_EVIDENCE` | alto para a dúvida do dono | alto | baixo | `LR-UI-006` §8 |
| P3 | **F9** — harness de cache de prompt com "não pode piorar em nenhum caminho" | médio-alto | médio | baixo | §4.1 P1 |
| P4 | **A tabela de pesos de STT/TTS** como insumo de orçamento: CPU Parakeet 630,7 MiB / GPU 1.181,6 MiB; SenseVoice CPU 228,5 / GPU 894,2; Pocket 194,4 + vozes 227,1 + clonagem 37,9 — todos com SHA-256 por arquivo e licença por arquivo | alto (é o piso de RAM/VRAM de qualquer "voz local") | **zero** (é leitura) | baixo | `LR-UI-006` §8 |
| — | **F6** | — | — | não compete com nada que o Lab meça hoje | — |

### 4.6 Research (esta base)

| Prioridade | Recomendação | Esforço |
|---|---|---|
| P1 | **F12** — adotar o formato "inventário por arquivo + verificador que só precisa de `git ls-files`" como meta para `data/inventory/license-matrix.tsv` | baixo |
| P2 | **F13** — o campo `Decision basis:` nos ADRs deles é o que falta nos nossos DR quando a evidência é um registro de conversa | baixo |
| P3 | **A regra que esta rodada confirma**: capacidade descrita (site, vídeo, docs, issue) nunca entra como testada — o Animama é o caso mais fácil de errar, porque o repositório é aberto, enorme e bem documentado, e ainda assim **nada** do que ele faz foi medido aqui | — |

## 5. O que não está recomendado, e por quê escrito

1. **Não adicionar o Animama como dependência** de nada. Além da licença, a superfície é a de um produto: FastAPI + PostgreSQL + Electron + React 19 + Three + onnxruntime-web + 1,4 GiB de pesos possíveis. O `Dockerfile`/`docker-compose.yml` existem, e nada disso foi construído aqui.
2. **Não copiar código nem assets.** Com AGPL-3.0-only no original e 5.953/5.953 arquivos marcados `prepared-not-release-approved`, "copiar" nem é a discussão: a licença do produto Lia não é essa.
3. **Não tratar como superior a arquitetura cognitiva.** O §6 de `LR-UI-006` compara eixos: o ponto em que o Animama **corrobora** a regra da Lia (léxico antes de vetor) é o mesmo em que ele mostra o que a Lia não tem (instrumento de medida de recall). Nada disso move uma decisão de arquitetura oficial da Lia, e não move porque não foi pedido a esta base.
4. **Não usar os números de desempenho deles como se fossem da Lia.** As tabelas de #660/#712 e a estimativa de latência de TTS no §8 são *(a) medidas em hardware Apple, e (b) uma extrapolação aritmética feita por nós com um fator inventado e declarado*. As duas coisas estão rotuladas no dossiê e é assim que precisam ser citadas adiante.
5. **Não abrir pesquisa genérica sobre os vizinhos** que o `README` menciona (`pocket-tts`, `smart-turn`, `three.quarks`, `unity-avatar-tools`, `VRM-Addon-for-Blender`). Foram citados aqui só onde explicam o Animama; cada um é uma rodada própria, se o dono quiser.

## 6. Evidências deste documento

Nenhuma medição nova: cada linha remete a uma seção de `repositories/animama/REPORT.md` ou `repositories/animama-avatar-converter/REPORT.md`, onde estão os caminhos de arquivo, os números de commit (`4ba6db1c…` e `0b24f4e6…`) e os comandos executados (12 testes no gate de licença do Animama, 46 testes + 1 verificação de repositório no conversor). Fontes externas usadas só como `DOCUMENTED`: `https://animama.ai/` e a página do vídeo `https://www.youtube.com/watch?v=sWw4bSrriDE` (título "I Built An AI Companion That Actually Feels Alive. Here's How.", canal Raymond Van, 2026-11-18, 12:36, 41.392 visualizações, 1.155 curtidas, 14 capítulos, transcrição automática lida em parte, comentários lidos) — mais a API do GitHub para releases/tags/branches/issues/contributors dos dois repositórios.

## 7. Como isto se liga à base

Novos objetos: `LR-UI-006`, `LR-FORGE-024`, este `LR-CMP-005`. Atualizados por consequência: `RESEARCH-INDEX.md` (§1 +2 linhas, §3-bis +1), `README.md` (contagens), `catalog/catalog.tsv` (gerado), `data/inventory/license-matrix.tsv` (+2), `data/testing/test-log.tsv` (+2), `cross-project/licensing/READY-TO-USE-LICENSES.md` (+2 linhas na tabela-mestra) e `cross-project/licensing/SPLIT-LICENSE-SCAN.md` (objetos cobertos), além da entrada de `RESEARCH-CHANGELOG.md`.
