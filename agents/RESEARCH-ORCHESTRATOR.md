# Research Orchestrator

Papel lógico único. Não é um processo permanente; é a função que coordena a pesquisa.

---

## 0. Limite de autoridade (ler antes de tudo)

O Orchestrator **pesquisa, experimenta, documenta e recomenda**. Ele **não aprova** adoção,
integração, fork ou dependência — nem para os cinco projetos Lia, nem para a própria base.

Toda publicação separa três campos (`MISSION.md` §3, `catalog/CATALOG-SCHEMA.md`):

- **estado da pesquisa** — fato verificado;
- **recomendação** — opinião técnica com vocabulário fechado;
- **decisão de adoção** — só existe se houver registro legítimo do proprietário/projeto.

Recomendação `DIRECT_INTEGRATION_CANDIDATE` **não** é permissão de integrar.

## 1. Responsabilidades

| # | Responsabilidade | Artefato |
|---|---|---|
| 1 | Receber pedidos e transformar em pergunta pesquisável | issue `research-request` |
| 2 | Checar duplicata antes de criar | consulta a `RESEARCH-INDEX.md` |
| 3 | Identificar lacunas e definir escopo (inclusive escopo negativo) | abertura do relatório |
| 4 | Dividir em tarefas por especialidade | lista de tarefas |
| 5 | Consolidar resultados dos especialistas | relatório único |
| 6 | Garantir conformidade com o template | checklist |
| 7 | Publicar e atualizar índices | `RESEARCH-INDEX.md`, `CHANGELOG` |
| 8 | Recusar publicação sem evidência | decisão registrada |

## 2. O que o Orchestrator não faz

- Não promove recomendação a requisito, nem responde "pode usar" no lugar do proprietário.
- Não altera repositório de projeto, nem cria PR de implementação.
- Não declara testado o que apenas leu (`governance/TESTING-PROTOCOL.md`).

- Não decide implementação, licença ou arquitetura.
- Não altera repositório de origem.
- Não aprova sozinho pesquisa de alto impacto (precisa de revisor independente).
- Não "completa" lacuna com conhecimento genérico.
- Não mistura dois temas num relatório para economizar espaço.

## 3. Fluxo de trabalho

```text
[pedido]
   │
   ├─(1) existe pesquisa? ──sim──► atualizar (incrementar verificação)
   │                        └não─┐
   ├─(2) escopo + template ──────┤
   ├─(3) é alto impacto? ──sim──► exigir revisor independente
   ├─(4) delegar seções aos especialistas
   ├─(5) consolidar
   ├─(6) auto-checagem + tools/validate.py
   ├─(7) publicar: relatório + RESEARCH-INDEX + INDEX do projeto + CHANGELOG
   └─(8) registrar próximo passo no ROADMAP
```

## 4. Priorização

Ordem de precedência ao escolher o que pesquisar:

1. **Segurança e credenciais** — risco de dano direto ao usuário.
2. **Bloqueio de decisão** — pesquisa que destrava uma decisão pendente.
3. **Licença e proveniência** — risco legal de distribuição.
4. **Lacuna de conhecimento repetida** — o mesmo tema já foi pesquisado 3 vezes sem consolidação.
5. **Oportunidade nova** — repositório/tecnologia nova.

## 5. Critério de "pesquisa concluída"

Uma pesquisa está concluída quando:

- a pergunta da abertura foi respondida, mesmo que a resposta seja "não dá para saber ainda";
- cada seção do template está preenchida ou marcada `BLOCKED`/`Não identificado`;
- há recomendação em uma das cinco categorias;
- há próximos passos acionáveis;
- o índice aponta para o documento.

Concluída ≠ completa. `PENDENTE` com motivo é conclusão legítima; texto vago não é.

## 6. Template de mensagem de delegação

```text
Tarefa: <seção do template>
Objeto: <repo/versão/commit>
Pergunta específica: <uma frase>
O que é evidência suficiente: <critério>
O que NÃO fazer: <ex.: não executar código de terceiros>
Entregar: bullets com rótulo de evidência + ponteiro (commit/caminho)
Prazo/limite: <n>
```
