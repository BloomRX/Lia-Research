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

Voltar: `README.md` · `catalog/README.md`
