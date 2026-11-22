# Breeze TTS 2 — código Apache-2.0, pesos não comerciais, English/Chinese apenas

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-009` |
| Nome | BreezeBlue/Breeze-TTS-2 (modelo) + breezeblue-ai/breeze-tts (código de inferência) |
| Tipo | modelo |
| Fonte oficial | https://huggingface.co/BreezeBlue/Breeze-TTS-2 · https://github.com/breezeblue-ai/breeze-tts |
| Responsável | BreezeBlue (breezeblue.ai) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Recomendação | **REJECT** (para o caso de uso do Lia) |
| Decisão de adoção | — nenhuma registrada |
| Categoria | model (leitura transversal em voice, licensing, hardware) |
| Projetos beneficiados | Lia Model Lab, Lia-Project (voz), Lia Research (método de registro de peso) |
| Versão analisada | card lido em 2026-11-22; código `a43d19e718b3` (main, 2026-11-17T09:11Z) |
| SHA completo | `a43d19e718b322e1cb3b2aa66f6d37d7945f4b21` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — SHA do `main` do repositório de código lido nesta coleta; o card não expõe commit (ver §7) |
| HEAD atual | `a43d19e718b322e1cb3b2aa66f6d37d7945f4b21` |
| Data | 2026-11-22 |
| Última verificação | 2026-11-22 |
| Upstream conferido | 2026-11-22 · HEAD `a43d19e7` · sem mudança desde a análise |
| Próxima revisão | 2027-02-22 |
| Licença | **código**: Apache-2.0 (`CONFIRMED`). **pesos, modelos derivados e saídas auto-hospedadas**: BreezeBlue Research and Non-Commercial License |
| Confiança | Alta para licença e requisitos (texto lido); nenhuma para qualidade de áudio (nada executado) |

---

## 1. Por que um modelo entra nesta base, e com qual veredito

O pedido veio como link para o card do Hugging Face. É um TTS aberto bem-sucedido — 3B parâmetros,
27.062 downloads/mês, 13 fine-tunes, 20 quantizações, 4 adapters e 22 Spaces usando o checkpoint,
reivindicando 1º lugar entre os abertos no leaderboard TTS do Artificial Analysis. Para o Lia,
porém, três fatos o encerram como candidato:

1. **idiomas: inglês e chinês.** O card diz "Bilingual Support — Generates natural English and
   Chinese speech with a single model". PT-BR não é suportado nem citado. Para um produto cuja
   interface de voz é PT-BR, isso é critério de exclusão, não de ajuste;
2. **pesos não comerciais, e a nuance importa** (§3);
3. **CUDA-only com piso de 12 GB** (§4) — nada aqui foi medido, e nenhuma inferência sobre a RX 580
   é feita neste documento.

Estado de execução: `STATIC_REVIEW_ONLY` — o repositório de código de inferência foi lido (árvore,
README, `configs/fast.json`, `docker/`); nenhum teste do projeto foi executado, e peso/áudio seguem
`BLOCKED`.

Veredito: **`REJECT` para o caso de uso do Lia**, com duas coisas a aproveitar (a estrutura de licença
em duas camadas e as métricas de latência do benchmark deles). Não é um repositório ruim: é o modelo
errado para a missão, e registrá-lo assim vale mais do que ignorá-lo.

## 2. O que é

| Item | Dado (do card e do repositório de código) |
|---|---|
| Arquitetura declarada | TTS com streaming, "voice design" sem áudio de referência, "voice direction" com referência, clone de voz e eventos vocais inline (`(laugh)`, `(sigh)` em inglês; `[笑]`, `[叹气]` em chinês) |
| Tamanho | 3B parâmetros, tensores F32 e BF16, safetensors |
| Uso de memória | ~7,7 GiB em eager; ~14,4 GiB com `--fast-all`; "12 GB GPU é o mínimo recomendado"; 24 GB para o caminho rápido |
| Latência reivindicada | TTFA < 40 ms e RTF 0,32 (~3,1× tempo real) **em H100 aquecido** |
| Código | `breezeblue-ai/breeze-tts`: 155 KB, 6 módulos em `breeze_infer/` (`api`, `audio`, `batch`, `runtime`, `templates`), `configs/fast.json`, Docker, `requirements.txt` |
| API local | `python -m breeze_infer.api` → `/v1/audio/speech`, resposta PCM s16le mono 24 kHz, streaming |
| Requisitos | Linux, Python ≥3.10, GPU NVIDIA com CUDA; Docker default para sm90 (Hopper), `FLASH_ATTN_CUDA_ARCHS=80` para A100 |
| Idade | criado 2026-08-25; último push no código 2026-11-17; 7 issues abertas; ★1.793 |
| Tokenizer | "based on Qwen3-TTS by the Alibaba Qwen Team", Apache-2.0 |

## 3. A estrutura de licença — o achado mais útil deste objeto

Lido no card, com o texto integral das cláusulas relevantes:

- "Source code is licensed under Apache 2.0. Breeze TTS 2 **model weights, derivative models, and
  self-hosted outputs are for research and non-commercial use only**";
- "Model weights, checkpoints, adapters, derivative models, and self-hosted outputs are governed
  separately by the BreezeBlue Research and Non-Commercial License. **The Apache License does not
  grant rights to use the model commercially**";
- "If you have an active paid subscription, outputs you generate through BreezeBlue's hosted platform
  or API at breezeblue.ai can be used commercially, subject to our Terms of Service. **A paid
  subscription does not grant commercial rights to the open-weight model or self-hosted outputs**";
- responsabilidade do usuário por direitos sobre entradas, áudio de referência e vozes; proibição
  explícita de clonagem não autorizada, impersonação e fraude;
- "AS IS", sem garantia, e componentes de terceiros mantêm as próprias licenças.

Isso resolve três confusões recorrentes nesta base, com um vocabulário mais preciso que o nosso hoje:

| Distinção que o card faz | Onde o Lia já errou por não fazer |
|---|---|
| licença do **código** ≠ licença dos **pesos** | `LR-MODEL-007`: "licença de código × pesos" — aqui está o formato pronto |
| saída **self-hosted** ≠ saída **do serviço pago** | a discussão do Meshy/Tripo sobre "o que posso publicar" |
| assinatura paga dá direito sobre **as saídas da API**, não sobre **o modelo** | evita a inferência "paguei → posso usar o peso comercialmente" |
| modelo derivado (fine-tune, adapter, quantização) herda a restrição | 13 fine-tunes e 20 quantizações publicadas **não** limpam a restrição |

Registro explícito de limite: isto é descrição do que o texto do card afirma, com data e URL —
**não é parecer jurídico** (`REQUIRES_LEGAL_REVIEW` para qualquer consequência de produto).

## 4. Requisitos de hardware: o que se pode e o que não se pode dizer

- `CONFIRMED` (do card): exige GPU **NVIDIA com CUDA**; piso recomendado de 12 GB; 24 GB para o
  caminho rápido; números de latência/RTF valem para **H100 aquecido**.
- `NOT RUN` / `BLOCKED`: nenhuma medição nesta sessão — a sandbox não tem GPU CUDA, não há runtime de
  voz e o `huggingface.co` não é alcançável daqui (ver §7). Nada sobre tempo por frase, RTF ou
  qualidade em qualquer hardware do usuário.
- Não se transfere nada para AMD: a ausência de suporte a ROCm/CUDA **não** implica que um caminho
  ONNX/CPU exista ou não exista — **não verificado**, e não se conclui nada sobre a RX 580 a partir
  deste objeto (nem a favor, nem contra).

## 5. Os benchmarks publicados pela mesma organização

`breezeblue-ai` tem 4 repositórios: o de código (Apache-2.0) e três suítes de avaliação —
`TTS-Voice-Design-Benchmark` (★6), `TTS-Voice-Direction-Benchmark` (★7) e `TTS-Latency-Benchmark` (★0):

- o de latência mede **TTFB** (início da requisição até o primeiro chunk não vazio de áudio),
  **Initial Silence** (duração de áudio decodificada antes do primeiro ataque de voz detectado) e
  **TTFA** (quando a primeira fala audível chega ao cliente);
- o de voice design mede **Role Fit**, **Transcript Pass Rate** e **Voice Diversity** (número de
  clusters de voz via embeddings WavLM Large + ECAPA), com o conjunto de dados no Hugging Face.

Dois usos para o Lia:

1. as três métricas de latência são **exatamente** o formato que falta à lacuna `BLOCKED`
   "Latência de TTS por frase (p50/p95)" do digest de voz — separar "primeiro byte" de "primeiro
   som audível" é o que impede reportar latência boa quando há 300 ms de silêncio inicial;
2. **os três repositórios de benchmark não têm arquivo de licença** (`licenseInfo: NONE` na API). Sem
   licença, o código do gate de latência não é reutilizável por um projeto que distribui produto —
   o mesmo tipo de lacuna das Skills do Hub, agora em suítes de avaliação. Vale registrar: bons
   números publicados por um fornecedor, medidos por suíte sem licença, sem o commit do checkpoint
   pinado, **não** são evidência importável para decisão de produto.

## 6. O que este objeto diz sobre a afirmação "#1 entre os abertos"

`REPORTED` apenas. Não consultei o Artificial Analysis (fora da allowlist desta sessão) e não há
medição própria aqui. Consequência de método, e é a que vale para a base: um modelo pode ser ótimo no
leaderboard e useless para o Lia ao mesmo tempo — os critérios de exclusão (§1) são independentes do
ranking. O registro correto é "não aplicável ao caso de uso", não "pior" nem "melhor".

## 7. Limitações desta análise (declaração de alcance)

- **Nenhum byte de peso foi baixado**; nenhuma síntese executada; nenhuma conta criada; nada instalado.
- O `huggingface.co` **não é alcançável a partir do sandbox** (TLS bloqueado fora da allowlist de
  hosts): a lista de arquivos do modelo, o tamanho real do checkpoint, a data da última modificação
  do card e a **revisão/commit do repositório de pesos** não puderam ser obtidos. O conteúdo do card
  veio pelo recuperador de página, lido em 2026-11-22 (2 chunks).
- Por isso **não há SHA do peso pinado** neste registro. O repositório de pesos é citado pelo card com
  o nome em caixa diferente (`BreezeBlue/breeze-tts-2` no link do News × `BreezeBlue/Breeze-TTS-2` na
  URL do modelo) — pode ser o mesmo repo ou um duplicado; **não verificado**, e é justamente o tipo de
  ambiguidade que impede reprodutibilidade. `BLOCKED`, não resolvido por suposição.
- Os termos de serviço citados (breezeblue.ai/legal/terms) e a licença completa dos pesos (arquivo
  `LICENSE` no repositório do modelo) **não foram lidos na íntegra**: a análise para na transcrição do
  card.

## 8. Recomendação e o que levar

**`REJECT` para adoção** — idioma, licença dos pesos e CUDA-only, cada um sozinho já bastaria.

O que fica, sem código:

1. **registrar licença em duas camadas** (código × pesos/derivados/saídas) em todo objeto de modelo
   desta base, com a regra "assinatura paga ≠ direito sobre o peso" e "fine-tune herda a restrição";
2. **adotar TTFB / Initial Silence / TTFA** como as três colunas da medição de voz, em vez de
   "latência" genérica — hoje a lacuna `BLOCKED` do digest de voz nem tem métrica definida;
3. **exigir commit do checkpoint** (revisão do repositório de pesos) como campo de proveniência em
   `LR-MODEL-007` — é o que falta para "a versão que medimos" significar alguma coisa, e é o que
   este objeto não consegue fornecer sobre si mesmo.

## 9. Evidências

| Afirmativa | Rótulo | Base |
|---|---|---|
| código Apache-2.0; pesos/derivados/saídas self-hosted "research and non-commercial use only" | `CONFIRMED` (texto do card) | card lido em 2026-11-22, com citação literal |
| "Apache License does not grant rights to use the model commercially" | `CONFIRMED` | §License and Responsible Use do card |
| assinatura paga libera saídas da API hospedada, não o modelo | `CONFIRMED` | card, §License |
| idiomas: English + Chinese; PT-BR ausente do card | `CONFIRMED` | §Highlights ("Bilingual Support") |
| 12 GB mínimo; 7,7 GiB eager; 14,4 GiB com `--fast-all`; números em H100 | `CONFIRMED` (como declaração) | card |
| 3B params; 27.062 downloads/mês; 13 fine-tunes, 20 quantizações, 4 adapters, 22 Spaces | `REPORTED` | blocos de metadados exibidos na página lida |
| repo de código: ★1.793, 155 KB, 7 issues, push 2026-11-17, LICENSE Apache-2.0 | `CONFIRMED` | API do GitHub, 2026-11-22 |
| 3 benchmarks sem arquivo de licença (NONE) | `CONFIRMED` | API `orgs/breezeblue-ai/repos` |
| métricas TTFB/Initial Silence/TTFA e Role Fit/Transcript Pass Rate/Voice Diversity | `CONFIRMED` | READMEs dos dois benchmarks |
| "#1 entre abertos no Artificial Analysis" | `REPORTED` | card; leaderboard não consultado |
| qualidade de áudio, latência medida, comportamento em CPU/AMD | `BLOCKED` | nada executado; sem GPU |
| commit/revisão do repositório de pesos; tamanho real do checkpoint; data do card | `BLOCKED` | `huggingface.co` não alcançável no sandbox |
| consequência de distribuir produto com saída gerada por pesos não comerciais | `REQUIRES_LEGAL_REVIEW` | não é parecer jurídico |

## 10. Próximos passos

1. **Nenhum trabalho contínuo sobre o modelo** — encerrado por idioma e licença. Reabertura só com
   suporte a português anunciado no próprio card.
2. Levar as três métricas de latência para a lacuna `BLOCKED` de `LR-VOICE-001` como **definição de
   medição futura**, sem executar nada agora.
3. Acrescentar ao `LR-MODEL-007` a exigência de **revisão do checkpoint** (repo + commit) e de
   separação código × pesos no registro, seguindo o formato dos objetos `LR-FORGE-012`
   (catálogo pinado com sha256) e `LR-VOICE-002` (licença por artefato).

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · `cross-project/voice/VOICE-STACK-DIGEST.md` · `catalog/CATALOG-SCHEMA.md` §2 (proveniência).
