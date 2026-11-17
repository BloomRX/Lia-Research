# DR-0016 — ReScript não é adotado como stack

| Campo | Valor |
|---|---|
| ID | DR-0016 |
| Estado | **REJECTED** |
| Data | 2026-11-17 |
| Pesquisa | `LR-STUDIO-003` |
| Reversível? | sim, com as condições abaixo |

## Evidência
`E3` bindings oficiais para React, **não** para Vue (`CONFIRMED` pela lista de repos).
`E2` licença mista: `compiler/` LGPL-3.0-or-later, resto MIT.
Stack real do ecossistema: TypeScript + Vue + Electron + Godot.

## Decisão
ReScript não entra em nenhum projeto. Custo de migração e incompatibilidade com Vue
superam qualquer ganho não demonstrado.

## Consequências
Nenhuma (decisão de não fazer). O padrão de `LICENSE` por diretório foi adotado como
prática — ver `governance/LICENSE-AND-PROVENANCE-POLICY.md`.

## Condição de reabertura
Bindings Vue maduros **e** ganho medido em um protótipo real.
