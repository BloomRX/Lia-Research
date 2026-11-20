# DR-0004 — Destino do ZIP de terceiros no Lia-Studio

| Campo | Valor |
|---|---|
| ID | DR-0004 |
| Alcance | **GOVERNANCA** — decisão administrativa; não aprova adoção de tecnologia |
| Estado | **PENDING** |
| Dono | proprietário + responsável do Studio |
| Data | 2026-11-17 |
| Pesquisa | `LR-LIC-001` |

## Situação
`Lia-Studio:docs/Mr-Mak-Skills-Free.zip` — 9,9 MB, 764 arquivos, 20 skills de terceiros,
**não importadas**. O `THIRD_PARTY_NOTICES.md` do Studio registra que o ZIP não foi
comparado arquivo a arquivo com a fonte pública.

## Opções
| Opção | Efeito |
|---|---|
| A. Manter versionado | conveniência; 9,9 MB de terceiros com proveniência não verificada |
| B. Remover do Git e registrar hash + URL | proveniência clara, sem binário no repo |
| C. Auditar e importar skills selecionadas | requer licença por skill + NOTICE |
| D. Manter e auditar depois | dívida crescente |

## Recomendação de pesquisa
**B** (remover do versionamento mantendo registro de hash/URL), com C apenas após
auditoria. A remoção exige autorização do responsável do Studio — não é ação do agente.
