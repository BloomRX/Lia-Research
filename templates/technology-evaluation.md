# Technology evaluation — `<NOME>`

> Template oficial. Todas as 18 seções são obrigatórias.
> Se não houver dado para uma seção, escrever `Não identificado` — nunca remover a seção.
> Preencher o cabeçalho antes de começar a redigir.

| Campo | Valor |
|---|---|
| ID | `LR-<CAT>-000` |
| Título | |
| Categoria | agents / mcp / voice / models / ui / security / forge / studio / hardware / licensing |
| Projetos beneficiados | |
| Fontes | `org/repo@sha:path` |
| Versão/commit analisado | |
| Data da pesquisa | |
| Última verificação | |
| Próxima revisão | |
| Responsável | |
| Status | CURRENT / HISTORICAL / SUPERSEDED / INCOMPLETE / UNVERIFIED / CONFLICTING / NOT-RECOVERED |
| Recomendação | ADOTAR / ADAPTAR / REFERÊNCIA / REJEITAR / PENDENTE |
| Licença do objeto pesquisado | SPDX ou `não identificada` |
| Confiança das evidências | alta / média / baixa |

## 1. Identificação

- Nome:
- URL:
- Organização:
- Licença (lida no arquivo, commit):
- Versão/tag:
- Commit analisado:
- Data da análise:
- Status da pesquisa:

## 2. Resumo executivo

Cinco a dez linhas. O que é, para que serve, se serve para a Lia, e o que decide a
recomendação. Quem ler só esta seção deve poder decidir se continua lendo.

## 3. O que resolve

Problema do usuário/projeto. Não confundir com "features que tem".

## 4. Arquitetura

Componentes, fluxo de dados, protocolos, pontos de extensão. Onde está o acoplamento.

## 5. Funcionalidades

Tabela: funcionalidade · estado (estável/beta/ausente) · evidência.

## 6. Dependências

Runtime, bibliotecas, serviços externos, binários opcionais. Licença das principais.

## 7. Requisitos de hardware e sistema

SO suportado, arquitetura, GPU, RAM, disco. Marcar o que é `REPORTED` vs medido.

## 8. Segurança e privacidade

Autenticação, autorização, exposição de rede, armazenamento de dados, telemetria,
advisories conhecidos, superfície de ataque.

## 9. Licença e proveniência

Licença lida no arquivo, obrigações, compatibilidade com distribuição dos apps Lia,
classe de aproveitamento (`USE_AS_IS`…`BLOCKED`), camadas separadas (código/conteúdo/pesos/marca).

## 10. Maturidade e manutenção

Idade, cadência de commits, releases, issues abertas, CI, testes, número de
mantenedores, bus factor.

## 11. Custos e limitações

Dinheiro, tokens, tempo de integração, limites técnicos declarados.

## 12. Compatibilidade com o ecossistema Lia

Stack real dos projetos (Electron/Vue/TypeScript, Windows 11, RX 580 8 GB, Ryzen 5 5500,
16 GB RAM), contratos existentes que seriam afetados.

## 13. Projetos beneficiados

Tabela: projeto · como usaria · pré-requisito.

## 14. Oportunidades de reutilização

O que aproveitar: padrão, comportamento, contrato — e por qual via legal.

## 15. Riscos e incompatibilidades

Tabela: risco · severidade · probabilidade · mitigação · decisão necessária.

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência (commit/caminho) | Data |
|---|---|---|---|---|
| E1 | | | | |

## 17. Recomendação

Uma das cinco categorias + 3–6 linhas de justificativa + gates explícitos.
Declarar o que a recomendação **não** autoriza.

## 18. Próximos passos

Numerados, com dono sugerido e critério de conclusão. Ações que dependem de decisão
humana são marcadas `AGUARDA DECISÃO`.
