# Status da pesquisa e separação entre pesquisa e decisão

---

## 1. Duas coisas diferentes

| | Pesquisa (este repositório) | Decisão de implementação |
|---|---|---|
| Quem produz | Research Orchestrator | responsável do projeto beneficiado |
| Onde vive | `repositories/`, `cross-project/`, `projects/` | `decisions/` + repositório do projeto |
| O que declara | "isto parece adequado, com estes gates" | "vamos implementar, nesta ordem, com este dono" |
| Efeito | nenhum sobre código | altera roadmap, código e release |

Uma recomendação `ADOTAR` não é autorização. Uma decisão `ACCEPTED` sem relatório
de pesquisa é decisão sem evidência — permitida, mas registrada como tal.

## 2. Cinco categorias de recomendação

| Categoria | Significado exato | O que **não** significa |
|---|---|---|
| `ADOTAR` | tecnologia adequada para adoção, condicionada aos gates listados | não significa "já aprovado", nem "integrar agora" |
| `ADAPTAR` | padrões ou partes aproveitáveis com mudanças | não significa copiar código |
| `REFERÊNCIA` | útil como inspiração/conhecimento, sem integração prevista | não significa inútil |
| `REJEITAR` | benefício insuficiente ou impedimento identificado | não significa "proibido pesquisar de novo" |
| `PENDENTE` | falta evidência para concluir | não significa "provavelmente sim" |

`REJEITAR` por impedimento de licença é diferente de `REJEITAR` por mérito técnico.
O relatório deve dizer qual dos dois.

## 3. Estados de decisão (`decisions/`)

| Pasta | Significado |
|---|---|
| `ACCEPTED/` | decisão tomada, com dono, data e escopo |
| `ADAPTED/` | adotado com modificações registradas |
| `REFERENCE-ONLY/` | mantido como referência; proibido integrar |
| `REJECTED/` | descartado, com motivo e condição de reabertura |
| `PENDING/` | aguardando decisão humana; bloqueia integração dependente |

Cada arquivo de decisão contém: ID, objeto, evidência usada (IDs `LR-*`), decisão,
dono, data, escopo, o que fica fora de escopo, e condição de reversão.

## 4. Fronteira com os projetos de origem

O Lia-Research **pode**:

- apontar risco e gate;
- recomendar ordem de experimento;
- registrar que um projeto já decidiu algo (com link para o ADR de origem);
- listar o que falta para uma decisão ser possível.

O Lia-Research **não pode**:

- abrir PR de implementação;
- editar ADR de origem;
- declarar arquitetura;
- criar dependência entre projetos;
- promover pesquisa a requisito.

## 5. Rastreabilidade de decisão para evidência

```text
decisions/ACCEPTED/DR-0007-*.md
   └── referencia LR-MCP-001 (repositories/ha-mcp/)
         └── referencia homeassistant-ai/ha-mcp@3dd26d4 docs/OAUTH.md
               └── evidência E3 (CONFIRMED, 2026-11-17)
```

Qualquer elo quebrado invalida a decisão para auditoria.

## 6. Decisões que esta fundação deixa abertas

| ID | Assunto | Por que não foi decidido pelo agente |
|---|---|---|
| `DR-0001` | licenciamento das Skills `lia-*` | exige titular; agente não pode conceder licença |
| `DR-0002` | distribuição do Lia-Research a agentes dos projetos | exige política de acesso/permissões |
| `DR-0003` | adoção ou não do HA-MCP como adaptador | exige protótipo isolado + aceite de risco R2/R3 |
| `DR-0004` | destino dos 9,9 MB de ZIP de terceiros no Lia-Studio | proveniência e licença de terceiro |
| `DR-0005` | critério de "modelo validado" no catálogo de capacidades | exige bancada de medição no hardware real |
| `DR-0006` | visibilidade do Lia-Research | ação bloqueada por permissão (403) |

## 7. Revisão de status

Status de pesquisa muda por: nova versão do objeto, correção de erro, evidência
nova, ou vencimento de validade. Em todos os casos, atualizar
`última verificação` + `RESEARCH-INDEX.md` + `RESEARCH-CHANGELOG.md`.
