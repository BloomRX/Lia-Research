# Stack de voz PT-BR — digest

| Campo | Valor |
|---|---|
| ID | `LR-VOICE-001` |
| Categoria | voice |
| Projetos | Lia-Project |
| Fontes | `Lia-Project@005a324:docs/product/M1-PERSONAL-VOICE-ARCHITECTURE.md`, `M1-*VOICE*REPORT.md` (fases 3, 4, 5, 4E2, round 4), `docs/architecture/LIA-NATIVE-TRANSCRIPTION.md` (20 KB), `LIA-NATIVE-SPEECH-PREVIEW.md` (12 KB), `docs/reports/LIA-MULTI-PROVIDER-VOICE-ARCHITECTURE.md` (18 KB), `LIA-AUDIO-QA-MATRIX.md` (38 KB), `LIA-STT-SECURITY-AUDIT-2026-11-14.md` |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média — muito material de QA, mas sem medição consolidada |

## 1. Estado das capacidades

| Capacidade | Estado | Evidência |
|---|---|---|
| TTS local (Kokoro) | runtime supervisionado existe | `REPORTED` (arquitetura + relatórios de fase) |
| TTS multi-provider | arquitetura definida | `REPORTED` |
| STT nativo (transcrição) | implementado, com auditoria de segurança | `REPORTED` + `LR-SEC-003` |
| VAD | Silero candidato | `REPORTED` |
| Full-duplex | não implementado | pesquisa aberta |
| PT-BR de qualidade | **não provado** com métrica | `UNVERIFIED` |

## 2. Auditoria de segurança de STT (resumo)

Existe auditoria dedicada (`LIA-STT-SECURITY-AUDIT-2026-11-14.md`, 17–18 KB) sobre
credenciais de STT e ensaio de voz. É o único subsistema de voz com revisão de
segurança formal. Conclusões específicas permanecem na origem (documento de projeto).

## 3. Matriz de QA de áudio

`LIA-AUDIO-QA-MATRIX.md` (38 KB) + `LIA-AUDIO-EVIDENCE-RECONCILIATION.md` (29 KB) +
`LIA-AUDIO-QA-RECONCILIATION.md` (13 KB): três documentos de reconciliação indicam
histórico de divergência entre evidência e declaração — bom sinal de rigor, mau sinal
de estabilidade.

## 4. Lacunas

| Lacuna | Status |
|---|---|
| WER de STT PT-BR no Ryzen 5 5500 | `BLOCKED` |
| Latência de TTS por frase (p50/p95) | `BLOCKED` |
| Barge-in / eco | `BLOCKED` |
| Comparação Kokoro existente × alternativas | `NOT RUN` — regra do projeto: medir antes de adicionar |

## 5. Objetos externos auditados nesta frente (2026-11-22)

Dois relatórios entraram na base sobre esta frente e **não alteram** nenhuma linha de §4:
`repositories/realtimetts/REPORT.md` (`LR-VOICE-002`, wrapper de engines: licença por **artefato**,
adendo de escopo engine × peso, e 319 testes passando em Python 3.11 sem gerar áudio) e
`repositories/breeze-tts-2/REPORT.md` (`LR-MODEL-009`, pesos não comerciais, English/Chinese,
CUDA-only → `REJECT` para o caso de uso do Lia). O que eles trazem de concreto para as lacunas acima é
a **definição de métrica** — TTFB, Initial Silence e TTFA separados — e não um dado novo: as três
linhas `BLOCKED` continuam `BLOCKED`, e "medir antes de adicionar" continua valendo.

## 5. Referência externa útil

`ggml-org/whisper.cpp` e `k2-fsa/sherpa-onnx` já aparecem no corpus interno; nenhum
foi re-pesquisado aqui (dedup aplicado). `hexgrad/kokoro` citado.
