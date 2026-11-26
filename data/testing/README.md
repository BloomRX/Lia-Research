# Log de testes

Uma linha por tentativa (inclusive falha). Colunas e vocabulário em
`governance/TESTING-PROTOCOL.md` §2.

**Estado em 2026-11-26: 44 linhas de dados, cobrindo 34 objetos**, com tentativas de 2026-11-20 a
2026-11-26. Níveis: **1 × 34 · 2 × 8 · 3 × 1**. Resultados: `LOCAL_TESTS_PASS` 15 · `BLOCKED` 11 ·
`LOCAL_SMOKE_PASS` 10 · `PARTIAL` 8 (a soma fecha em 44, nenhum registro órfão).

> A linha anterior deste arquivo dizia **"Hoje: 0 linhas — nenhum objeto foi executado"**, o que estava
> falso desde 2026-11-20: o texto não foi atualizado quando as primeiras execuções entraram no log.
> Corrigido nesta data por contagem direta, sem reescrever nenhuma linha do log. Reproduzir a contagem:
> `awk 'END{print NR-1}' data/testing/test-log.tsv`.

Regra que governou a última linha adicionada (`LR-VEC-001`, 2026-11-26, nível 2, `PARTIAL`): o
protocolo exige linha para **toda** tentativa, e proíbe citar no relatório uma tentativa sem as dez
colunas. Como o dossiê mediu e citou o harness local do VTracer 0.6.15, a linha entrou — chaveada no ID
do dossiê, não no da ferramenta, porque a ferramenta não tem objeto próprio no catálogo. Isso mudou o campo
`Resultado de execução` do dossiê de `NOT_RUN` para `PARTIAL`: o serviço continua sem nenhuma execução, e
dizer o contrário seria ler mal a própria tabela.
