# DR-0015 — unslop rejeitado por ausência de licença

| Campo | Valor |
|---|---|
| ID | DR-0015 |
| Estado | **REJECTED** |
| Data | 2026-11-17 |
| Pesquisa | `LR-AGENT-004` |
| Reversível? | sim, se o autor publicar licença |

## Evidência
Metadados da API: `license: null`. Requisição a `contents/LICENSE`: **404**.
Repositório público sem licença = todos os direitos reservados (`CONFIRMED`).

## Decisão
Nenhum uso, cópia, execução ou integração. Apenas leitura para aprendizado de conceito
(não de texto).

## Condição de reabertura
Publicação de licença permissiva (MIT/Apache-2.0) pelo autor. Reavaliar então com
`templates/license-audit.md`.
