# archive/

Material que **já foi publicado** aqui e deixou de ser atual, ou que nunca foi
concluído. Nada aqui é apagado: uma base de pesquisa que reescreve o passado perde
exatamente o que a torna confiável.

| Pasta | O que entra | O que **não** entra |
|---|---|---|
| `superseded/` | relatório substituído por versão mais nova | correção de erro trivial (corrige-se no lugar) |
| `historical/` | pesquisa de contexto que já cumpriu função | decisão tomada (essa vai em `decisions/`) |
| `incomplete/` | coleta interrompida, com o que se sabe e onde parou | rascunho em andamento |

## Regra de arquivamento

1. O documento arquivado mantém o ID original.
2. O substituto registra no cabeçalho: `Substitui: <ID> (arquivado em AAAA-MM-DD)`.
3. `archive/<pasta>/README.md` local lista o motivo e o substituto.
4. Nada de "arquivar" para esconder fracasso: `incomplete/` é registro honesto de
   coleta que não fechou, e é preferível a um relatório raso apresentado como completo.
