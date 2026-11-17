# DR-0018 — OpenIDEA, SculptForge, ManimGX e pixelfx como referência

| Campo | Valor |
|---|---|
| ID | DR-0018 |
| Estado | **REFERENCE-ONLY** |
| Data | 2026-11-17 |
| Pesquisas | `LR-STUDIO-001`, `LR-FORGE-002`, `LR-FORGE-003`, `LR-FORGE-004` |
| Reversível? | sim |

## Decisão
Nenhum destes entra como dependência. Aproveitamento limitado a padrões:

| Fonte | Padrão |
|---|---|
| OpenIDEA | divisão em crates por responsabilidade; plugin SDK com exemplos oficiais |
| SculptForge | benchmark pack com hardware declarado e resultados públicos |
| ManimGX | árvore `LICENSES/` (REUSE) e fixtures com hash |
| pixelfx | `NOTICE.md` por camada de conteúdo |

## Fora de escopo
Não autoriza copiar código, redistribuir binários, nem introduzir Rust/Tauri no produto.
SculptForge e pixelfx também não autorizam incorporar código GPL/MIT sem auditoria de
NOTICE.
