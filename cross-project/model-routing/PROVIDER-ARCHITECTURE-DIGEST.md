# Arquitetura neutra de providers — digest

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-002` |
| Categoria | models |
| Projetos | Lia-Project, Lia Agent Hub |
| Fontes | `Lia-Project@005a324:docs/research/LIA-MODEL-PROVIDER-ARCHITECTURE.md` (19 KB); `docs/architecture/LIA-PROVIDER-ADAPTER-DESIGN-2026-10-29.md`; `LIA-PROVIDER-RUNTIME-2026-10-30.md` |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Alta (desenho), sem validação de runtime |

## 1. O que a Lia já tem (segundo os documentos)

- Gestão de provider no produto.
- Runtime de voz supervisionado.
- Memória local.
- Autorização de tools por capability.

## 2. O desenho proposto

Três camadas separadas — **capability → adapter → provider** — em que o produto pede
uma *capability* (`chat.stream`, `stt.transcribe`, `tts.speak`) e nunca um modelo.

| Camada | Responsabilidade | Não faz |
|---|---|---|
| capability | contrato de produto (streaming, cancelamento, tool call, erro) | não conhece HTTP |
| adapter | tradução para API do provider | não decide política |
| provider | endpoint + credencial + modelo | não conhece UX |

## 3. Convergência externa

O contrato `InferenceEngine` do OpenJarvis (`generate`, `stream`, `list_models`,
`health`) é a versão madura da mesma ideia (`LR-AGENT-001` §14). Vale como referência
de assinatura mínima — não como dependência.

## 4. Matriz de conformidade necessária (ainda não escrita)

O documento original pede uma "matriz de conformidade de capability/provider" para:
texto, streaming/cancelamento, tool call, erro, redação, seleção obsoleta, saúde de
processo e ciclo de vida. Isso **não existe** — é a lacuna mais acionável.

## 5. Encaminhamento

`RESEARCH-ROADMAP.md` item M-3: escrever a matriz de conformidade antes de adicionar
qualquer provider novo (incluindo o HA-MCP como caso de teste de adaptador externo).
