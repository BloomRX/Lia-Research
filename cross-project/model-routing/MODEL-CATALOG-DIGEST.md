# Catálogo de modelos e providers — digest combinado

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-001` |
| Categoria | models |
| Projetos | Lia-Project, Lia Model Lab |
| Fontes | `Lia-Project@005a324:docs/research/LIA-MODEL-PROVIDER-CATALOG.md` (29,5 KB); `docs/research/LIA-MODEL-PROVIDER-RECOMMENDATIONS.md` (14,7 KB); `Lia-Model-Lab@3ec4313:docs/05-FOUNDATION-MODEL-COMPARISON.md` (18 KB) |
| Data | 2026-11-17 |
| Status | **CONFLICTING** (dois catálogos concorrentes) |
| Confiança | Alta para estrutura e licenças citadas; nula para desempenho |

## 1. Conflito declarado

O ecossistema tem **dois catálogos de modelo** que não se citam:

| | Lia-Project | Lia Model Lab |
|---|---|---|
| Documento | `LIA-MODEL-PROVIDER-CATALOG.md` | `05-FOUNDATION-MODEL-COMPARISON.md` |
| Escopo | providers + modelos + runtimes para produto | modelos de fundação para treino/avaliação |
| Registros | 44 (no catálogo de capacidades) | comparação por família |
| Conclusão | poucos modelos testados, opções simples local/free/paid | família Lia + candidatos |

Não é contradição de fato; é **duplicação de autoridade**. Dois lugares decidem "qual
modelo", com critérios diferentes, e nenhum é o dono.

## 2. Recomendações de provider preservadas (Lia-Project, 14/11)

| Capability | Primeiros candidatos | Classe | Observação |
|---|---|---|---|
| Conversa local/tool-use | llama.cpp + LFM3-1.7B GGUF Q4; Qwen pequeno | A | Vulkan/CPU; licença LFM com limite de receita |
| Conversa remota | Gemini/OpenAI/Anthropic/Groq como adapters opcionais | A/B | nenhum default forçado |
| STT pt-BR local | whisper.cpp vs sherpa-onnx | A | benchmark necessário |
| VAD | Silero VAD | A | MIT, pequeno |
| TTS pt-BR | runtime Kokoro existente vs Kokoro/ONNX; opcional Cartesia/ElevenLabs | A/B | **não adicionar concorrente antes de medir o existente** |
| Áudio único (ASR+TTS) | LFM3-Audio-2B | B | inglês-only no voice chat |
| Visão/tela | crop + OCR (PaddleOCR/Tesseract), depois LFM3-VL/Qwen VLM | B | opt-in, frames pequenos |
| Embeddings | Qwen3-Embedding-0.6B / BGE-M3 | B | só quando recall lexical falhar |
| Reranking | BGE/Qwen reranker | C | exige ganho mensurável |
| Full-duplex | VAD/STT/router/TTS modular + comparação com realtime de OpenAI/Gemini | B/C | medir barge-in, eco, latência |
| Geração de imagem | stable-diffusion.cpp Vulkan / ComfyUI + API | C | não é serviço sempre ativo |
| Geração de vídeo | Wan2.2 apenas high-end / hosted | **D para RX 580** | inviável localmente |
| Orquestrador | arquitetura de tools/permissões existente | A | LangGraph só se estado durável |
| Interop de plugin | adaptador MCP atrás de broker próprio | B | não auto-instalar servidor |

## 3. Licenças não triviais registradas

LFM Open License (limite de receita) · Piper GPL + voz individual · XTTS CPML
(non-commercial) · VoiceStudio AGPL · pesos de modelo e assets com licenças
independentes.

## 4. Regra preservada

> "Não fazer catálogo indiscriminado. Oferecer poucos modelos testados, opções simples
> local/free/paid e uma tela avançada com critérios/termos."

## 5. Encaminhamento

`RESEARCH-ROADMAP.md` item M-1: eleger **um** catálogo canônico (proposta: o do
Project, por ser de produto) e transformar o do Model-Lab em insumo de avaliação.
Decisão de produto, não desta base.
