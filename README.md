# Lia-Research

**Base de conhecimento técnico central do ecossistema Lia.**
**Público por decisão do proprietário.** Não é aplicativo, não é dependência de runtime, não é pacote.

| Campo | Valor |
|---|---|
| Repositório | `BloomRX/Lia-Research` |
| Visibilidade | **PÚBLICA** — decisão do proprietário (`DR-0006`), consumo read-only para agentes de projeto |
| Branch padrão | `main` |
| Data de fundação | 2026-11-17 |
| Responsável | Research Orchestrator (agente) / proprietário BloomRX (decisões) |
| Status | Base reorganizada em 2026-11-20 (missão, catálogo, validador). Medição em hardware: `NOT RUN`; testes de software registrados: **0** |
| Arquivos Markdown | 174 (contagem de 2026-11-20, `find -name '*.md' -not -path './.git/*'`), validados por `tools/validate.py` |
| Relatórios externos | 23 objetos, 1 relatório cada (`repositories/*/REPORT.md`) |
| Catálogo | `catalog/catalog.tsv` — 23 linhas, gerado de `tools/build_catalog.py` |
| Decisões (governança) | 1 aceita · 12 pendentes · 3 rejeitadas · 2 referência · 2 pastas vazias por desenho |

> **Aviso de escopo.** Este repositório registra *pesquisa*, não *implementação*.
> Nenhuma recomendação aqui autoriza alterar Lia-Project, Lia Forge, Lia Studio,
> Lia Agent Hub ou Lia Model Lab. Decisões de implementação pertencem ao
> responsável de cada projeto.
>
> **Identidade e limites de autoridade:** [`MISSION.md`](MISSION.md) — a fonte de verdade
> sobre o que o Research é, o que pode recomendar e o que nunca decide.
>
> `estado da pesquisa` ≠ `recomendação` ≠ `decisão de adoção`. Os três vivem em campos
> separados no cabeçalho de cada relatório (`catalog/CATALOG-SCHEMA.md`).

---

## 1. Para que serve

O ecossistema Lia tem cinco projetos independentes que faziam pesquisa em paralelo,
em branches de sessão que nunca chegavam a `main`. O resultado medido nesta
fundação (2026-11-17):

- **1.620** documentos distintos (caminho + tamanho) encontrados nas 43 branches dos
  cinco projetos, dos quais **511 existem apenas fora de `main`**;
- **645** documentos de autoria Lia após separar o vendorizado (975 arquivos, em
  sua maioria documentação upstream do AIRI dentro do Lia-Project);
- **48** Skills catalogáveis, **47** autorais/adaptadas, **0** com licença dentro do payload;
- **0** relatórios de pesquisa externa existiam sobre os 7 alvos originais (HA-MCP,
  OpenJarvis, Vercel UI, Mister Download Manager, OpenIDEA, Claude Trading Skills,
  RouterHub) e sobre os 9 alvos adicionais depois.

Depois desta fundação: **23 objetos externos auditados** (21 repositórios + 2
organizações), **5 dossiês internos**, **31 digests transversais**, **4 comparações** e
**3 decisões de não adoção** registradas com condição de reabertura.

**Cobertura declarada:** esta base é uma **camada de ponteiro**, não um espelho. São
160 documentos aqui (2026-11-20) para **1.148 Markdown em `main`** nos cinco apps (medido
em 2026-11-17), ou seja ~1:7. O critério é seletivo: entra o que muda decisão, não o que já vive no projeto.
Revisão crítica do estado da base: `archive/historical/LIA-RESEARCH-BASELINE-REVIEW-2026-11-17.md`.

O Lia-Research existe para que esses números deixem de ser redescobertos a cada
sessão. Ele oferece: um índice único, um padrão de relatório, um vocabulário de
evidência, regras de proveniência e licença, e um fluxo de publicação.

## 2. O que ele NÃO é

- Não funde repositórios nem move código dos projetos para cá.
- Não é submodule, nem dependência de build, nem dependência de runtime.
- Não copia código de terceiros: relatórios descrevem, citam e apontam.
- Não promove recomendação a decisão. `DIRECT_INTEGRATION_CANDIDATE` ≠ autorização.
- Não é distribuível: ver `LICENSE` (sem licença concedida, por decisão).

## 3. Navegação por quatro dimensões

Uma mesma pesquisa é localizada de quatro formas. O relatório principal existe em
**um** lugar; os índices apenas apontam para ele.

| Dimensão | Onde | Pergunta que responde |
|---|---|---|
| Projeto beneficiado | `projects/<projeto>/INDEX.md` | "O que a Lia Forge pode usar?" |
| Área tecnológica | `cross-project/<área>/` | "O que sabemos sobre voz, memória, MCP?" |
| Repositório/tecnologia | `repositories/<slug>/` | "O que já foi apurado sobre o HA-MCP?" |
| Decisão | `decisions/<estado>/` | "Isso foi aceito, adaptado, rejeitado?" |

Entrada principal: **[`RESEARCH-INDEX.md`](RESEARCH-INDEX.md)** — tabela com ID,
categoria, projeto, tecnologia, status, data de revisão e caminho.

## 4. Mapa do repositório

Na raiz ficam só navegação, licença, índice, roadmap, changelog e política essencial.
Documento de entrega não fica na raiz: vai para `archive/`.

```text
Lia-Research/
├── MISSION.md                 identidade, limites de autoridade, os três conceitos
├── README.md                  entrada e mapa
├── RESEARCH-INDEX.md          índice mestre (fonte de descoberta)
├── RESEARCH-ROADMAP.md        Parte A: o que pesquisar · Parte B: 12 meses
├── RESEARCH-BACKLOG.md        fila de triagem (20 recebidos, 3 publicados)
├── RESEARCH-CHANGELOG.md      histórico de publicações, revisões e migrações
├── catalog/                   CATALOG-SCHEMA.md + catalog.tsv (gerado) + README
├── governance/                investigação, teste, evidência, licença, segurança, preservação
├── agents/                    orquestrador, papéis de especialista, revisão, publicação
├── templates/                 um modelo por tipo de objeto (14 modelos)
├── decisions/                 registros de governança (nunca aprovação de adoção)
├── repositories/              um diretório por objeto externo (23 relatórios)
├── cross-project/             15 áreas tecnológicas transversais (inclui `character-creation/`)
├── projects/                  consolidação por projeto Lia
├── comparisons/               comparações entre alternativas
├── ecosystem/                 mapa do ecossistema e capacidades compartilhadas
├── audits/                    conferência periódica de upstream
├── data/                      inventário, manifesto, test-log, snapshots
├── archive/                   historical/ · superseded/ · incomplete/ (nunca descartado)
├── templates, tools/          modelos e validate.py / build_catalog.py / check_upstream.py
└── .github/                   PR template + 3 issue templates
```

Mapa dos documentos que não são relatório:

| Precisa de… | Vai em |
|---|---|
| saber o que o Research pode e não pode | `MISSION.md` |
| pesquisar um objeto novo | `governance/INVESTIGATION-PROTOCOL.md` + modelo em `templates/README.md` |
| testar com segurança | `governance/TESTING-PROTOCOL.md` |
| registrar o resultado de um teste | `data/testing/test-log.tsv` |
| saber o estado de um objeto | `catalog/catalog.tsv` + `catalog/CATALOG-SCHEMA.md` |
| contribuir sem quebrar a base | `governance/CONTRIBUTION-WORKFLOW.md` |
| conferir auditoria de qualidade | `governance/QUALITY-AUDIT-2026-11-17.md` |
| ver o que já foi conferido no upstream | `audits/REAUDIT-2026-11-20.md` |
| entender quem faz o quê | `agents/RESEARCH-ORCHESTRATOR.md` + `agents/SPECIALIST-ROLES.md` |
| criar personagem com IA (silhueta → 3D) | `cross-project/character-creation/CHARACTER-CREATION-RESEARCH.md` |
| publicar | `agents/PUBLISHING-PROTOCOL.md` |

## 5. Vocabulário obrigatório

**Confiança de evidência** (definições completas em `governance/EVIDENCE-STANDARDS.md`):

| Rótulo | Significado |
|---|---|
| `CONFIRMED` | verificado diretamente em código, licença, API ou teste reproduzível |
| `OBSERVED` | observado na inspeção, sem validação independente |
| `REPORTED` | afirmado por documentação oficial ou terceiro |
| `INFERRED` | inferência técnica fundamentada, explicitada como tal |
| `UNVERIFIED` | não foi possível confirmar |
| `BLOCKED` | impedido por acesso, ambiente ou informação |

**Estado do documento**: `CURRENT`, `HISTORICAL`, `SUPERSEDED`, `INCOMPLETE`,
`UNVERIFIED`, `CONFLICTING`, `NOT-RECOVERED`.

**Recomendação**: `DIRECT_INTEGRATION_CANDIDATE`, `ADAPT`, `REFERENCE_ONLY`, `REJECT`, `PENDENTE`.

Nenhum relatório pode usar "funciona", "é compatível" ou "é rápido" sem um dos
rótulos acima. Benchmark de terceiro não é resultado no hardware do usuário.

## 6. Como um agente consulta este repositório

1. Leia `RESEARCH-INDEX.md` e filtre por projeto/categoria/tecnologia.
2. Abra **apenas** o relatório principal indicado (não há cópias divergentes).
3. Confira o cabeçalho de identificação: commit analisado + data + status.
4. Se o status for `SUPERSEDED`/`CONFLICTING`, siga o ponteiro para o substituto.
5. Cite o ID (`LR-...`) na sua própria documentação, não o caminho do arquivo.

**Leitura não exige autenticação.** O repositório é público: qualquer sessão lê por
`https://raw.githubusercontent.com/BloomRX/Lia-Research/<branch>/<caminho>`, sem token,
deploy key ou GitHub App. `gh` só é necessário para os **cinco repositórios de produto**,
que são privados. Sempre cite a **branch** junto do ID — o conteúdo difere de `main` para
as branches de sessão.

Detalhes de acesso, permissões e sincronização de leitura:
`archive/historical/LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md` §3-bis.

## 7. Como publicar uma pesquisa

Fluxo resumido (completo em `agents/PUBLISHING-PROTOCOL.md`):

```text
pedido → checar RESEARCH-INDEX (duplicata?) → escopo → template
      → coletar evidência (commit + data) → redigir → revisão (alto impacto?)
      → publicar → atualizar RESEARCH-INDEX + INDEX do projeto + CHANGELOG
```

Regra dura: **um documento sem commit/data/status não é publicado.**

## 8. Diretórios não criados (e por quê)

| Proposto | Situação | Justificativa |
|---|---|---|
| `cross-project/vision/` | **não criado** | nenhum dos cinco projetos tem pesquisa dedicada de visão/multimodal; criar pasta sem fonte seria fingir cobertura. Lacuna registrada em `RESEARCH-ROADMAP.md` R-4 |
| `cross-project/observability/` | **não criado** | tema citado (`LR-HW-002`) mas sem nenhuma fonte pesquisada — `R-2` |
| `cross-project/distribution/` | **não criado** | empacotamento/assinatura/update não foi pesquisado em nenhum alvo — `R-1` |
| `projects/*/{architecture,security,...}/` | **não criados** | um `README` + `INDEX` por projeto aponta para a pesquisa onde ela já vive; subpastas seriam cópias |
| `comparisons/` | criado (4 arquivos) | só entrou comparação com pergunta de decisão |
| `archive/{superseded,historical,incomplete}/` | criados com `README.md` | pastas estruturais, com critério de entrada escrito |

A regra aplicada: **nenhum diretório vazio** e nenhuma pasta criada para "completar a
árvore". Lacuna declarada vale mais que diretório decorativo.

## 9. Estado desta fundação

| Verificação | Resultado |
|---|---|
| Repositório existe e está acessível | PASS |
| Visibilidade pública revisada (substitui o gate "repositório privado") | **PASS** — `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md`: 3 achados no snapshot, 2 tratados, 0 pendentes |
| Estrutura criada | PASS |
| Governança e templates | PASS |
| Inventário dos 5 projetos | PASS (58.478 arquivos, 1.620 docs, 645 Lia) |
| Inventário persistido em `data/` | PASS (7 arquivos, com hash) |
| Pesquisa externa (7 obrigatórios) | PASS |
| Pesquisa externa (9 adicionais) | PASS |
| HA-MCP análise aprofundada | PASS |
| Índices e changelog | PASS (`RESEARCH-INDEX`, `-ROADMAP`, `-CHANGELOG`) |
| Links, IDs, segredos e estrutura validados | PASS — `python3 tools/validate.py` (18 verificações): 0 erros |
| Re-auditoria de upstream (2026-11-20) | 22/22 existem · 10 com commits novos · 0 links mortos (`audits/REAUDIT-2026-11-20.md`) |
| Criação de personagens (2026-11-20, revisada em 2026-11-20 UTC) | **10 IDs, 10 documentos Markdown e 1 matriz com 51 registros** (46 da rodada 7.0 + 3 da 7.1 + 2 da 7.2), 3 pipelines propostos; **nada executado** e nenhum peso baixado (`cross-project/character-creation/CHARACTER-CREATION-RESEARCH.md`) |
| Reauditoria técnica (2026-11-20) | 22 objetos reavaliados · 3.576 commits no intervalo · 0 recomendações alteradas · 1 motivo alterado (`audits/TECHNICAL-REAUDIT-2026-11-20.md`) |
| Validador próprio | `python3 tools/validate.py` (18 verificações, data dinâmica) e `python3 tools/test_validate.py` (**76 testes**) |
| Testes de software executados | **16 linhas** em `data/testing/test-log.tsv`: 5 suítes reais (17 + 65 + 65 + 3.530 + 2.044 asserções), 2 execuções parciais e 9 tentativas bloqueadas com motivo |
| Catálogo gerado do cabeçalho dos relatórios | PASS — `tools/build_catalog.py --check` |
| Fase 4 (medição em hardware) | **NOT RUN** — exige execução na máquina do usuário |
| Revisão humana da entrega | **PENDENTE** — protocolo em `agents/REVIEW-PROTOCOL.md` |

`NOT RUN` e `BLOCKED` **não** são `PASS`. Detalhamento, incluindo o que ficou bloqueado
e por quê: `archive/historical/LIA-RESEARCH-FOUNDATION-REPORT.md`.

## 10. Relatórios de entrega (arquivados)

| Documento | O que responde |
|---|---|
| `archive/historical/LIA-RESEARCH-FOUNDATION-REPORT.md` | o que foi construído, com que status, e o que não foi |
| `archive/historical/LIA-RESEARCH-SOURCE-INVENTORY.md` | toda fonte com origem, commit, data e modo de uso |
| `archive/historical/LIA-RESEARCH-EXTERNAL-REPOSITORY-AUDIT.md` | os 16 objetos externos, vereditos e armadilhas |
| `archive/historical/LIA-RESEARCH-CONSOLIDATION-REPORT.md` | duplicatas, conflitos e o que a consolidação resolveu |
| `archive/historical/LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md` | como um agente consulta sem virar dependência |
| `archive/superseded/LIA-RESEARCH-ROADMAP.md` | as 4 fases do próximo ano, com critério de parada |
| `archive/historical/LIA-RESEARCH-PHASE-CLOSURE-REPORT.md` | encerramento da fase Research, com pendências por responsável |

## 11. Manutenção

- Toda pesquisa tem data de criação, última verificação, commit analisado e
  próxima revisão sugerida (`RESEARCH-ROADMAP.md`).
- Pesquisas sobre providers, modelos, preços e serviços comerciais vencem em 30–90
  dias; pesquisa arquitetural estável, em 6–12 meses.
- Antes de criar documento novo: consultar o índice. Duplicata é defeito.
- Alterações de conteúdo exigem entrada em `RESEARCH-CHANGELOG.md`.

---

*Fundação executada em 2026-11-17. Coleta de evidências: GitHub REST API
(metadados, trees, contents, commits, branches, releases), leitura estática de
licenças e código. Nenhum repositório de origem foi alterado; nenhuma branch foi
criada, apagada, movida ou rebaseada; nenhum código de terceiros foi incorporado.*
