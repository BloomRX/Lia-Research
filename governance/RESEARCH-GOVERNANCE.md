# 1. Escopo e autoridade

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


Este documento define quem pode fazer o quê no Lia-Research. Ele deriva da ordem de
serviço de 2026-11-17 e não pode ser ampliado por conveniência de uma sessão.

| Papel | Pode | Não pode |
|---|---|---|
| Research Orchestrator (agente) | pesquisar, redigir, publicar relatório, atualizar índices, abrir issue | autorizar implementação, mudar licença, alterar projetos de origem |
| Especialista (subagente temporário) | produzir seção técnica para o Orchestrator | publicar sozinho, aprovar o próprio trabalho |
| Revisor independente | aprovar/rejeitar pesquisa de alto impacto | editar o relatório que revisa |
| Responsável de projeto (humano) | decidir implementação, decidir licença, aprovar riscos | reescrever evidência (pode contestar com evidência nova) |
| Proprietário BloomRX (humano) | tudo, inclusive criar/arquivar decisões | — |

**Regra de separação:** quem pesquisa não decide implementação; quem decide
implementação não reescreve evidência.

# 2. O que conta como "publicado"

Um documento só está publicado quando, na mesma alteração:

1. existe no caminho definido pelo template aplicável;
2. tem cabeçalho de identificação completo (§4);
3. está referenciado em `RESEARCH-INDEX.md`;
4. está referenciado no `INDEX.md` do projeto beneficiado;
5. tem entrada em `RESEARCH-CHANGELOG.md`;
6. passou pelo `tools/validate.py` sem erro.

Item ausente = documento não publicado, mesmo que o arquivo exista. Esta regra
existe porque a falha dominante do ecossistema Lia em 2026-11 era exatamente essa:
**pesquisa existindo em branch de sessão, invisível para todo mundo**.

# 3. Estados de um documento

| Estado | Definição | Ação esperada |
|---|---|---|
| `CURRENT` | válido, evidência atual | revisar na data planejada |
| `HISTORICAL` | não é a melhor fonte, mas explica decisões passadas | manter, nunca apagar |
| `SUPERSEDED` | existe substituto mais novo | cabeçalho aponta para o substituto |
| `INCOMPLETE` | pesquisa interrompida | declarar o que falta |
| `UNVERIFIED` | conteúdo coletado sem validação suficiente | não citar como fato |
| `CONFLICTING` | conclusões contraditórias entre documentos | registrar o conflito, não escolher por conta própria |
| `NOT-RECOVERED` | referência localizada, conteúdo inacessível | registrar onde se procurou |

`NOT-RECOVERED` não autoriza inventar o conteúdo. `HISTORICAL` não autoriza
apagar. `SUPERSEDED` não autoriza remover o arquivo.

# 4. Cabeçalho obrigatório (frontmatter em tabela)

Todo relatório começa com esta tabela, sem exceção:

```markdown
| Campo | Valor |
|---|---|
| ID | LR-XXX-000 |
| Título | ... |
| Categoria | agents \| mcp \| voice \| models \| ui \| security \| forge \| studio \| hardware \| licensing |
| Projetos beneficiados | Lia-Project, Lia Forge, ... |
| Fontes | repo/branch/caminho@commit |
| Versão/commit analisado | sha ou tag |
| Data da pesquisa | AAAA-MM-DD |
| Última verificação | AAAA-MM-DD |
| Próxima revisão | AAAA-MM-DD |
| Responsável | Research Orchestrator / especialista |
| Status | CURRENT \| HISTORICAL \| ... |
| Recomendação | ADOTAR \| ADAPTAR \| REFERÊNCIA \| REJEITAR \| PENDENTE |
| Licença do objeto pesquisado | SPDX ou "não identificada" |
| Confiança das evidências | alta \| média \| baixa + rótulos usados |
```

# 5. Ciclo de revisão

| Tipo de objeto | Validade da pesquisa | Motivo |
|---|---|---|
| Serviço comercial, provider, preços, catálogo de modelos | 30 dias | preço/modelo/política mudam sem aviso |
| Repositório externo ativo (commits semanais) | 60–90 dias | arquitetura muda |
| Segurança, autenticação, credenciais | 90 dias ou a cada advisory | risco muda mais rápido que o código |
| Arquitetura estável, padrões, conceitos | 6–12 meses | baixa taxa de mudança |
| Licença e proveniência | a cada release que redistribuímos | obrigação legal acompanha a versão |

Revisão atrasada não invalida o documento: marca-se `stale` no índice e a
recomendação passa a exigir reconferência antes de uso.

# 6. Duplicação e conflito

Antes de criar documento: consultar `RESEARCH-INDEX.md` por projeto, categoria e
tecnologia. Três resultados possíveis:

1. **Coberto** → atualizar o documento existente, incrementando a data de verificação.
2. **Escopo diferente** → novo documento, com referência cruzada explícita.
3. **Contraditório** → **não** sobrescrever. Abrir seção `## Conflito` no documento
   mais novo, listar as duas posições com evidência, marcar `CONFLICTING` e criar
   item em `decisions/PENDING/`.

# 7. Proibições absolutas

- Excluir branch, fazer reset/clean/rebase/force push em repositório de origem.
- Sobrescrever documento original de outro projeto.
- Remover arquivo "duplicado" de projeto de origem.
- Atribuir licença a material Lia-* sem decisão do proprietário.
- Armazenar token, chave, senha, cookie, credencial ou dado pessoal.
- Apresentar README de terceiro como resultado comprovado.
- Apresentar benchmark de terceiro como medição no hardware do usuário.

# 8. Auditoria

A cada trimestre (ou a cada 50 pesquisas publicadas), o Orchestrator executa:

1. `python3 tools/validate.py` — cabeçalhos, IDs, links, duplicatas;
2. conferência de `stale` no índice;
3. amostragem de 10% dos relatórios contra a fonte citada;
4. registro do resultado em `RESEARCH-CHANGELOG.md`.

Falha de auditoria bloqueia novas publicações até correção, exceto correções de
segurança.

# 9. Alteração desta política

Somente o proprietário BloomRX altera este arquivo. O agente pode propor mudança
via issue com label `governance`, incluindo justificativa e impacto.
