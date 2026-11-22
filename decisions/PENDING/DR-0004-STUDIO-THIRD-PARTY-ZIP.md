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

## Evidência nova (2026-11-22, sem decisão)

Auditoria do upstream em `repositories/mr-mak-workspace/REPORT.md` (`LR-STUDIO-012`):

- os **19 releases** publicados têm dois artefatos de Skills — 3.352.656 B (`v0.4.14`) e
  4.263.307 B (`v0.6.0`) — e **nenhum** asset entre 9,5 e 10,5 MB;
- o empacotador atual do projeto (`scripts/package_skills.py`, rodado duas vezes nesta sessão)
  produz **4.264.037 B** com `manifest.json` de **768** arquivos, e é determinístico (mesmo
  `sha256` do ZIP em builds sucessivos);
- o arquivo local do Studio tem **764** arquivos declarados: **não bate** com nenhuma release nem
  com o gerador atual.

Consequência para a decisão, registrada sem recomendar: enquanto o ZIP não for identificado por hash +
revisão de origem, ele é `RESEARCH_ONLY` por definição de `MISSION.md` (proveniência desconhecida). A
comparação que fecharia isto é barata: `sha256sum` do ZIP local × `manifest.json` de uma release pinada.

