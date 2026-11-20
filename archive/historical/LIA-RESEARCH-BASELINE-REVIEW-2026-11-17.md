# Revisão de base — o que já temos aqui e o que já existe nos apps

> **Nota de vocabulário (2026-11-20).** Este documento é revisão de base de 2026-11-17 (histórico) e preserva o texto da
> época. O vocabulário de recomendação foi substituído em 2026-11-20 por
> `ADAPT` / `REFERENCE_ONLY` / `REJECT` / `DIRECT_INTEGRATION_CANDIDATE`
> (`catalog/CATALOG-SCHEMA.md` §4.1). Nada aqui foi promoção a aprovação de adoção.


| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| Escopo | re-leitura da base + verificação do estado real dos repositórios do usuário |
| Método | contagem por comando (`find`, `gh api`), leitura dos índices, sem herdar números de documentos anteriores |
| Status | CURRENT |
| Consequência | 4 correções aplicadas nesta mesma data (D1–D4, §6) |

---

## 1. Por que esta revisão existe

Pedido do proprietário, depois de dois ajustes de rumo: (a) os apps da ArtCraft são uma
**opção**, não regra de produto; (b) a base é **pública** e isso precisa estar escrito de
forma inequívoca. Com o escopo alinhado, faltava responder: *o que já foi feito e o que já
existe nos outros repositórios?*

Este documento é uma **re-leitura crítica**, não um resumo elogioso. Ele mede de novo em
vez de repetir números antigos — e por isso encontrou quatro erros, três deles meus.

## 2. Números medidos hoje (não herdados)

| Métrica | Valor | Como foi medido |
|---|---:|---|
| Arquivos Markdown nesta base | 136 | `find -name '*.md'` |
| Tamanho do repositório | 8,0 MB | `du -sh` |
| Objetos externos auditados | 18 | `repositories/*/REPORT.md` |
| Vereditos | **7 ADAPTAR · 8 REFERÊNCIA · 3 REJEITAR · 0 ADOTAR** | cabeçalho de cada relatório |
| Digests/propostas transversais | 30 | linhas de `RESEARCH-INDEX.md` §3 |
| Registros de decisão | 18 (12 abertas · 1 aceita · 3 rejeitadas · 2 referência) | `decisions/*/DR-*.md` |
| Repositórios públicos na conta | **14** | `gh api users/BloomRX/repos` |
| Branches nos 5 repositórios principais | **43** (12·10·9·5·7) | `gh api …/branches` |
| Markdown em `main` dos 5 | **1.148** (1.050·37·8·6·47) | Trees API, `truncated=false` |

## 3. O que está sólido (e por quê)

| # | Ativo | Evidência de que funciona |
|---|---|---|
| S1 | **Índice único com ID estável** (59 IDs) | toda pesquisa nova cai em um lugar só; nenhuma duplicata desde a fundação |
| S2 | **Evidência rotulada + pin por SHA** | 18 relatórios com commit fixo, data e rótulo (`CONFIRMED`…`UNVERIFIED`) |
| S3 | **Licença lida no arquivo, nunca no badge** | 3 casos em que o metadado do GitHub mentiu (dual MIT/Apache, plugin MIT × conteúdo CC BY, GPL embutido) |
| S4 | **Rejeição com condição de reabertura** | 3 `REJEITAR` com o que precisaria mudar para voltar à mesa |
| S5 | **Validador com 11 checagens** | 136 arquivos, 0 erros, 0 avisos — quebrou 0 vezes desde a fundação |

## 4. O que está frágil (autocrítica)

| # | Fragilidade | Por que importa |
|---|---|---|
| F1 | **0 ADOTAR em 18 objetos** | pode ser critério bom — ou viés. Nunca adotamos nada; vale testar a hipótese "estamos rejeitando demais" |
| F2 | **5 propostas, 0 execução** (`LR-AGENT-009`, `LR-AGENT-010`, `LR-SEC-005`, `LR-UI-005`, `LR-LIC-004`) | documento de proposta é barato; prova é caro. A base está pesada do lado barato |
| F3 | **Meta-documentação crescendo** — 6 relatórios sobre a própria base (fundação, consolidação, auditoria, encerramento, exposição, esta revisão) contra 18 de pesquisa | risco de a base virar assunto de si mesma |
| F4 | **Números divergindo entre documentos** | 2 achados hoje: índice dizia "(17)" com 30 linhas e "(13 abertas)" com 12. Corrigidos |
| F5 | **Regressão minha, hoje** | escrevi que os 5 repositórios de produto seriam privados. São **públicos** — e o `ecosystem/ECOSYSTEM-MAP.md` já dizia isso. Corrigido |
| F6 | **Cobertura não declarada** | 136 documentos aqui contra 1.148 em `main` nos 5 apps. A base é **camada de ponteiro**, não espelho — e isso não estava dito com clareza |

## 5. O que já existe nos outros repositórios (verificado hoje)

| Repositório | Branches | `.md` em `main` | O que a base consolidou | O que continua só na origem |
|---|---:|---:|---|---|
| `Lia-Project` | 12 | 1.050 | 261 documentos Lia-own + 22 Skills indexadas (`LR-PROJ-001`) | pesquisa de provider concorrente; 511 docs fora de `main` |
| `Lia-Forge` | 10 | 37 | 128 documentos + 49 capacidades (`LR-PROJ-002`) | 16 docs de arquitetura e auditoria (grandes, do projeto) |
| `Lia-Studio` | 9 | 8 | 109 documentos + 16 Skills (`LR-PROJ-003`) | 12 docs de pesquisa e roadmap (do projeto) |
| `Lia-AgentHub` | 5 | 6 | 57 documentos + biblioteca de Skills (`LR-PROJ-004`) | gaps E-1…E-9 herdados |
| `Lia-Model-Lab` | 7 | 47 | 90 documentos + 9 Skills (`LR-PROJ-005`) | 5 versões divergentes de medição |

**Fora dos cinco:** a conta tem 14 repositórios públicos. Oito não são "projetos Lia" e
estão mapeados sem pesquisa: `Lia-Go` (10 MB), `LiaVoiceStudio` (5,6 MB), `3d-create`
(567 MB), `3d-sprite`, `ChibiCreate`, `ComfyUI_Colab`, `animations-free`, `SilksongREA`
(fora de escopo). Nenhum foi auditado — e `Lia-Go` e `LiaVoiceStudio` têm nome de produto.

**Relação de cobertura:** 136 documentos aqui para 1.148 em `main` nos cinco apps ≈ **1:8**.
Isso é saudável se a base for seletiva; é problema se alguém achar que ela espelha tudo.

## 6. Correções aplicadas nesta revisão

| # | Achado | Correção |
|---|---|---|
| D1 | `LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md` §3-bis dizia "os cinco repositórios de produto são privados" | corrigido para **públicos** (`visibility: public` verificado nos 5), com a consequência: exposição pública não é só desta base |
| D2 | `RESEARCH-INDEX.md` §3 anunciava "(17)" com **30** linhas | corrigido para (30) |
| D3 | `RESEARCH-INDEX.md` §4 anunciava "(13 abertas)" com **12** | corrigido para (12 abertas + 5 tomadas) |
| D4 | Cobertura 1:8 não declarada | declarada no `README.md` §1 e nesta revisão |

## 7. O que eu faria agora, em ordem

| # | Ação | Por quê | Gate |
|---|---|---|---|
| 1 | **Fechar `DR-0001`** (licença das Skills Lia) | 48 Skills em repositórios **públicos** sem licença declarada é o maior risco aberto | proprietário |
| 2 | **Varredura de exposição nos 5 apps públicos** | a base só auditou a si mesma; já houve precedente de arquivo `.local` público | proprietário |
| 3 | **Rodar V6 de uma Skill** (ArtCraft, edição de foto) | primeira medida real do ecossistema; hoje 0 Skills provadas | autorização |
| 4 | **Automatizar contagem** (`doc-count-check`, `LR-SEC-006` R3) | F4 já custou duas rodadas de correção manual | — |
| 5 | **Decidir se `Lia-Go` e `LiaVoiceStudio` entram no escopo** | são 15 MB de repositório e não aparecem em nenhum dossiê | proprietário |
| 6 | Só então, nova pesquisa externa | evita F3 | — |

## 8. O que esta revisão não fez

- Não pesquisou objeto externo novo.
- Não executou nenhum app nem Skill (`V6` continua `NOT RUN`).
- Não leu os 1.148 documentos dos apps — leu os índices e contou o corpus.
- Não alterou nenhum repositório de produto.
- Não julgou a qualidade do código dos apps: isso é decisão de cada projeto.

---

## 9. Conclusão em uma frase

A base está **organizada e honesta**, mas ainda é **mais opinião documentada que medição** —
e o maior risco que ela mesma revelou não está nela: são **48 Skills sem licença em cinco
repositórios públicos**.
