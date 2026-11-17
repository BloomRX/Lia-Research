# DR-0001 — Licenciamento e distribuição das Skills `lia-*`

| Campo | Valor |
|---|---|
| ID | DR-0001 |
| Estado | **PENDING** |
| Dono | proprietário BloomRX (exige titular) |
| Data de abertura | 2026-11-17 |
| Pesquisas | `LR-LIC-001` |
| Bloqueia | distribuição de qualquer Skill a usuário final |

## Situação
47 Skills autorais/adaptadas; **0 com licença no payload**. Declaração de autoria do
proprietário existe; licença de distribuição não existe.

## O que precisa ser decidido
1. Licença das Skills Lia (ou ausência explícita de licença).
2. Se adaptações de terceiros (MIT) mantêm MIT apenas no trecho adaptado.
3. Se Skills são distribuídas como payload exportável ou apenas usadas internamente.
4. Se `alethe` (vendorizada, com patches) e as 29 AIRI entram no catálogo.

## Opções
| Opção | Efeito |
|---|---|
| A. Sem licença (uso interno) | simples; bloqueia distribuição e contribuição externa |
| B. MIT para Skills Lia | máxima compatibilidade; permite uso por terceiros |
| C. Apache-2.0 | idem + patente explícita; mais formal |
| D. Licença própria | controle; incompatível com ecossistema de skills |

## Recomendação de pesquisa
Opção C ou B, com `NOTICE` por Skill e `LICENSES/` estilo REUSE (`LR-FORGE-003`).
A escolha é jurídica e do titular: **o agente não decide**.

## Critério de conclusão
Arquivo de licença por Skill + política escrita + registro neste DR.
