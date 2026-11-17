# Matriz de conformidade — Capability × Provider

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-005` |
| Categoria | model-routing |
| Projetos beneficiados | Lia-Project (primário), Lia Agent Hub, Lia Model Lab |
| Fontes | `Lia-Project@005a324:airi/packages/stage-ui/src/libs/providers/providers/*/index.ts` (54 provedores lidos), `.../providers/types.ts` (schema de `tasks`/`capabilities`), `docs/architecture/LIA-NATIVE-PROVIDER-COVERAGE.md` (101 KB, registro do Corte B), `docs/research/LIA-MODEL-PROVIDER-CATALOG.md`, `lia-capability-catalog/0{2,3,4}`, `LIA-MODEL-PROVIDER-RECOMMENDATIONS.md` |
| Data | 2026-11-17 · coleta por leitura de código + documento interno; **nada executado** |
| Status | CURRENT |
| Confiança | **Alta** para o que foi lido no código; **nula** para comportamento em runtime |
| Próxima revisão | 2027-02-17 (ou quando `provider-catalog.ts` mudar) |

---

## 1. Pergunta de pesquisa

Quais *capabilities* de produto a Lia pode oferecer hoje, quais provedores as sustentam,
com que grau de suporte — e onde a diferença entre "declarado" e "implementado" cria
risco de prometer o que não existe?

## 2. Método

1. Inventariar todas as definições de provider do Stage (54 diretórios) e extrair
   `tasks` e blocos `capabilities` declarados.
2. Cruzar com o registro do Corte B (quais executam no processo main, com testes).
3. Classificar cada célula em quatro níveis:
   - **NATIVO** — declarado na definição **e** com caminho de código exercitado/testado;
   - **PARCIAL** — caminho existe, mas declaração incompleta, endpoint não verificado ou
     só um adaptador cobre;
   - **EXTERNO** — exige serviço/ferramenta fora do app (não é capability própria);
   - **AUSENTE** — nenhum caminho de código;
   - **N/V** — não verificado (declaração não extraível), nunca contado como suporte.
4. Não usar README de provedor como evidência de suporte da Lia.

Dados brutos desta matriz: `data/inventory/provider-tasks.tsv` (54 linhas, com origem e
método no cabeçalho).

## 3. O schema real de capability (evidência)

`ProviderDefinition` declara `tasks: string[]` e, opcionalmente:

```ts
capabilities?: {
  chat?: { reasoning?: ChatReasoningCapability }
  transcription?: { protocol: 'websocket'|'http'|'native'
                    generateOutput: boolean; streamOutput: boolean; streamInput: boolean }
  speech?: { transport: 'rest' | 'bidirectional-ws' }
}
```

`CONFIRMED` em `providers/types.ts` (linhas 158–270). Consequência: **o schema declara
três dimensões de capacidade** (chat+reasoning, transcrição, transporte de fala) e **não
declara** embeddings, tool calling, vision ou structured output. Quem precisa dessas
dimensões as descobre lendo o código de cada provider.

## 4. Distribuição de `tasks` (dado primário)

| `tasks` declaradas | Provedores | Observação |
|---|---:|---|
| `chat` | **33** | 10 são "curados" e executam no main (Corte B) |
| `text-generation` | 1 | `official` — declaração atípica |
| `text-to-speech` (+`tts`) | **13** | inclui `kokoro-local` (local, keyless) |
| `speech-to-text` (+`asr`,`stt`,`streaming-transcription`) | **3** | `aliyun-nls`, `apple-speech`, `browser-web-speech-api` |
| nenhum `tasks` extraível | 4 | `byteplus`, `byteplus-coding-plan`, `voicevox`, `volcengine-coding-plan` → **N/V** |
| `embed` | **0** | ver §6 |

## 5. Matriz — capabilities de produto × provedores

Legenda: **N** nativo · **P** parcial · **E** externo · **—** ausente · **N/V** não verificado

### 5.1 Chat e conversa

| Capability | Curated 10 (main) | Outros 23 chat | Evidência |
|---|:--:|:--:|---|
| Chat (request/response) | **N** | N/V por provider | 10 curados: código + 643 testes (`COVERAGE` §8) `CONFIRMED` |
| Streaming + cancelamento | **N** | N/V | `COVERAGE` §6 "streaming (chunks + fim), cancelamento (`cancel`+abort)" `CONFIRMED` (testes), runtime `NOT RUN` |
| Concorrência entre conversas | **N** | N/V | jobs com dono e teto — §6 `REPORTED` (documento), sem teste citado |
| Toggle de raciocínio (`reasoning`) | **P** (5 de 10) | — | declarado só em `openai`, `groq`, `cerebras-ai`, `openrouter-ai`, `ollama` `CONFIRMED` |
| Tool calling (function calling) | **P** | N/V | plataforma tem `tool-schema.ts` com adaptador de `anyOf`; nenhum provider **declara** tools `CONFIRMED` (ausência de declaração) + `INFERRED` (pass-through OpenAI-shaped) |
| Structured output / JSON mode | **N/V** | N/V | não declarado; sem teste localizado |
| Visão (imagem de entrada) | **N/V** | N/V | não declarado em `tasks`/`capabilities`; multimodal depende do modelo |
| Listagem de modelos (`listModels`) | **P** | P | continua no caminho legado (`voice-editor.ts`) — `COVERAGE` §6.5 `CONFIRMED` |
| Modelos locais keyless | **N** (2 de 10) | — | `ollama`, `lm-studio` com validação de config `CONFIRMED` |

### 5.2 Voz

| Capability | Provedores | Nível | Evidência |
|---|---|:--:|---|
| TTS remoto | `elevenlabs`, `openai-audio`, `unspeech`(deepgram), `openrouter-audio-speech`, `google-gemini-audio-speech`, `minimax-speech`, `player2-speech`, `mimo-audio`, `index-tts-vllm` | **N** (declarado) | `tasks: ['text-to-speech']` lido em cada `index.ts` `CONFIRMED` |
| TTS local | `kokoro-local`, `local-audio`, `voicevox` | **N** | `kokoro-local` declarado + runtime supervisionado existe no produto (`LR-VOICE-001`) `REPORTED` |
| TTS com streaming bidirecional | — | **E** | `capabilities.speech.transport: 'bidirectional-ws'` existe no schema; nenhum provider lido o declara `CONFIRMED` (ausência) |
| STT (nuvem/LAN) | `aliyun-nls` | **N** | `streaming-transcription` declarado `CONFIRMED` |
| STT local/nativo | `apple-speech` (macOS), `browser-web-speech-api` (Chromium) | **P no Windows** | `apple-speech` é específico de Apple; Web Speech API no Electron depende do build `INFERRED` |
| STT com streaming de entrada | schema permite `streamInput` | **N/V** | nenhum provider lido declara o trio completo |
| Full-duplex (barge-in) | — | **—** | não existe caminho; pesquisa aberta (`LR-VOICE-001` §4) |

### 5.3 Conhecimento e ferramentas

| Capability | Nível | Evidência |
|---|:--:|---|
| Embeddings | **P** | `lm-studio/index.ts` importa `createEmbedProvider` e faz `merge(chat, embed, model)` — caminho existe; **nenhum** provider declara `tasks: ['embed']` e nenhum modelo de embedding está no catálogo curado → capability sem declaração nem catálogo `CONFIRMED` |
| Reranking | **—** | nenhum caminho |
| Memória (recuperação local) | **N** (fora do provider) | implementada no produto, não no provider (`LR-AGENT-007`) `REPORTED` |
| Tools/permissões | **N** (fora do provider) | arquitetura de tools/autorização do produto, por capability (`LR-SEC-002`) `REPORTED` |
| MCP | **P** | broker existe; 1 servidor implementado no Forge (`LR-MCP-002`) `CONFIRMED` |
| Busca web | **E** | nenhum provider nativo; exige ferramenta externa |

### 5.4 Mídia

| Capability | Nível | Evidência |
|---|:--:|---|
| Imagem (geração/edição) | **E** | `stable-diffusion.cpp`/ComfyUI por API — `LIA-MODEL-PROVIDER-RECOMMENDATIONS.md` §imagem `REPORTED` |
| Vídeo | **E** (hosted) ou **—** (RX 580) | `Wan2.2` só high-end; local inviável no alvo `REPORTED` |

## 6. Os quatro desvios que a matriz expõe

### 6.1 Embedding implementado e não catalogado
`lm-studio` monta provider de embedding, mas `tasks` declara só `chat`. Não existe
`tasks: ['embed']` em nenhum dos 54. Resultado: a capability existe no código e é
**invisível** para catálogo, para o seletor de modelo e para o teste de conformidade.
Risco concreto: escolher embedding sem que ele apareça no catálogo de capacidades
(`LR-MODEL-004`: 44 registros, 0 validados).

### 6.2 Anthropic declarada como OpenAI-shaped
`anthropic/index.ts` declara `tasks: ['chat']` e a Lia reproduz `POST /v1/chat/completions`,
enquanto a superfície nativa é `/v1/messages`. `COVERAGE` §6.2 diz explicitamente que **não
foi verificado contra a API real**. É a única das dez onde "suportado" pode ser falso em
runtime. `P`, não `N`.

### 6.3 `listModels` no caminho legado
A descoberta de modelos não migrou com o resto. Consequência para a matriz: a coluna
"modelos disponíveis" é carregada por um caminho que o Corte B não auditou. `P`.

### 6.4 Declaração incompleta é regra, não exceção
Quatro providers não têm `tasks` extraível; `official` declara `text-generation` (fora do
vocabulário dos outros); `lm-studio` esconde embedding. **Quem lê `tasks` como fonte de
verdade subestima ou superestima o produto.** O único jeito de afirmar suporte é ler o
caminho de execução — que é o que este documento fez para 10 curados e não fez para 44.

## 7. Cobertura por modelo (não por provider)

Providers mudam a forma; o modelo decide a capacidade real. Da evidência disponível:

| Capacidade | Depende de | Situação |
|---|---|---|
| Texto PT-BR | modelo de chat | 44 catalogados, **0 medidos** (`LR-MODEL-004`) |
| Visão | modelo multimodal | nenhum modelo multimodal no catálogo curado `CONFIRMED` (ausência) |
| Áudio (ASR+TTS num modelo) | LFM3-Audio-2B | voice chat **inglês-only** na ficha `REPORTED` → PT-BR `UNVERIFIED` |
| Embedding | modelo + provider | nenhum catalogado (§6.1) |
| Raciocínio | modelo com reasoning | 5 providers declaram toggle; modelo não verificado |

## 8. Licença e riscos

| Item | Situação |
|---|---|
| Licença dos providers | não é do provider: é do **modelo** e dos termos do serviço |
| Termos de serviço | nenhum foi auditado em profundidade; RouterHub foi rejeitado por isso (`LR-PROV-001`) |
| Credencial | 10 curados resolvem no main; **`groq` ainda é legível no renderer** por causa da transcrição (`COVERAGE` §9.1) `CONFIRMED` |
| Endpoint não verificado | Anthropic (§6.2) |
| Modelo local | licença do peso é independente (LFM Open tem limite de receita) |

## 9. Conclusão

A Lia tem **uma** capability madura — chat com streaming e cancelamento, em 10 providers,
executando no processo main. Tudo o mais é parcial, externo ou inexistente. A matriz não
recomenda adicionar provider: recomenda **fechar as declarações** antes de expandir.

Em ordem de custo/benefício:

1. Declarar `embed` (ou removê-lo do código morto) — 1 linha, elimina §6.1.
2. Corrigir a assinatura de `tasks` dos 4 sem declaração — 4 linhas, elimina §6.4.
3. Migrar `listModels` — dívida já reconhecida no projeto.
4. Decidir Anthropic: adapter `/v1/messages` ou documentar como limitação conhecida.
5. Corrigir a exceção `groq` (transcrição no renderer) — é risco de credencial, não de
   capability.

## 10. Limitações e pendências

| Limitação | Rótulo |
|---|---|
| Nenhum provider exercitado em runtime nesta pesquisa | `NOT RUN` |
| 44 providers não auditados no caminho de execução (só declaração) | `UNVERIFIED` |
| Tool calling: nenhuma evidência de teste por provider | `UNVERIFIED` |
| Vision: nenhuma evidência de suporte no catálogo | `UNVERIFIED` |
| Streaming bidirecional de TTS: schema existe, provider não | `CONFIRMED` (ausência) |
| Contagem de providers depende da branch `005a324`; branches `arena/*` foram podadas em 2026-11-17 | `CONFIRMED` |

## 11. Encaminhamento

| Ação | Dono | Registro |
|---|---|---|
| Declarar `embed` e corrigir `tasks` | Lia-Project | proposta, não decisão |
| Matriz de conformidade virar gate de CI do projeto | Lia-Project | `DR-0019` (proposto) |
| Auditar tool calling por provider | Lia-Project | `RESEARCH-ROADMAP.md` M-5 |
| Fechar `groq` no renderer | Lia-Project | já é §10 do documento de origem |
