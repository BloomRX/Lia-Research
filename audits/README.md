# audits/ — conferência periódica dos objetos já pesquisados

| Campo | Valor |
|---|---|
| Natureza | verificação de existência, versão e licença no upstream |
| Não é | releitura de conteúdo, nem nova pesquisa |
| Saída bruta | `data/inventory/upstream-reaudit-2026-11-20.tsv` |

Aqui ficam os digests das rodadas de conferência: o que ainda existe, qual é o HEAD,
o que mudou desde a versão analisada, se a licença declarada pela API bate com o arquivo
do repositório. Confirmar que o objeto existe **não** promove estado de pesquisa — só
evita publicar link morto e dá gatilho de revisão.

| Rodada | Objetos | Resultado |
|---|---|---|
| `audits/REAUDIT-2026-11-20.md` | 22 | 22 existem; 10 com commits novos desde a análise; 0 links mortos |
| `audits/PROVENANCE-2026-11-20.md` | 23 | SHA analisado de cada objeto; 21 com 40 caracteres, 2 organizações incompletas por desenho |
| `audits/TECHNICAL-REAUDIT-2026-11-20.md` | 22 | reavaliação de conteúdo: 3.917 commits no intervalo, 5 suítes executadas, 8 bloqueios por toolchain |

Voltar: `README.md` · `catalog/README.md`
