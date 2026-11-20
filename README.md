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
| Status | Fundação entregue (fases 0–3); fase 4 de medição `NOT RUN` |
| Arquivos Markdown | 142 (contagem de 2026-11-17, `find -name '*.md'`), validados por `tools/validate.py` |
| Relatórios externos | 22 objetos auditados, 26 documentos |
| Decisões | 13 abertas · 3 rejeições · 2 referência · 2 pastas vazias por desenho |

> **Aviso de escopo.** Este repositório registra *pesquisa*, não *implementação*.
> Nenhuma recomendação aqui autoriza alterar Lia-Project, Lia Forge, Lia Studio,
> Lia Agent Hub ou Lia Model Lab. Decisões de implementação pertencem ao
> responsável de cada projeto. Ver `governance/RESEARCH-STATUS-AND-DECISIONS.md`.

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

Depois desta fundação: **22 objetos externos auditados** (20 repositórios + 2
organizações), **5 dossiês internos**, **23 digests transversais**, **4 comparações** e
**3 decisões de não adoção** registradas com condição de reabertura.

**Cobertura declarada:** esta base é uma **camada de ponteiro**, não um espelho. São
136 documentos aqui para **1.148 Markdown em `main`** nos cinco apps (medido em 2026-11-17),
ou seja ~1:8. O critério é seletivo: entra o que muda decisão, não o que já vive no projeto.
Revisão crítica do estado da base: `LIA-RESEARCH-BASELINE-REVIEW-2026-11-17.md`.

O Lia-Research existe para que esses números deixem de ser redescobertos a cada
sessão. Ele oferece: um índice único, um padrão de relatório, um vocabulário de
evidência, regras de proveniência e licença, e um fluxo de publicação.

## 2. O que ele NÃO é

- Não funde repositórios nem move código dos projetos para cá.
- Não é submodule, nem dependência de build, nem dependência de runtime.
- Não copia código de terceiros: relatórios descrevem, citam e apontam.
- Não promove recomendação a decisão. `ADOTAR` ≠ autorização.
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

```text
Lia-Research/
├── RESEARCH-INDEX.md          índice mestre (fonte de descoberta)
├── RESEARCH-ROADMAP.md        o que pesquisar depois, e por quê
├── RESEARCH-CHANGELOG.md      histórico de publicações e revisões
├── governance/                metodologia, evidência, licença, segurança, preservação
├── ecosystem/                 mapa do ecossistema, propriedade, capacidades compartilhadas
├── projects/                  consolidação por projeto (ler a pesquisa existente)
├── cross-project/             conhecimento transversal por área tecnológica
├── repositories/              um diretório por repositório/tecnologia externa investigada
├── comparisons/               comparações entre alternativas
├── decisions/                 registros de decisão (ACCEPTED/ADAPTED/REFERENCE-ONLY/REJECTED/PENDING)
├── archive/                   material histórico, superado e incompleto (nunca descartado)
├── templates/                 modelos obrigatórios de documento
├── agents/                    papéis, fluxo, publicação e revisão
├── data/                      inventário, manifesto com hash, snapshot do corpus
├── tools/                     validate.py + scripts de coleta reproduzíveis
├── .github/                   PR template, 3 issue templates, validação
└── LIA-RESEARCH-*.md          os 6 relatórios de entrega da ordem de serviço
```

Áreas existentes em `cross-project/` (todas com conteúdo, nenhuma criada para
"completar a árvore"): `agents/` `ai-models/` `automation/` `downloads/` `hardware/`
`interfaces/` `licensing/` `mcp/` `memory/` `model-routing/` `security/` `smart-home/`
`storage/` `voice/`.

Diretórios propostos que **não** foram criados estão em §8, com justificativa.

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

**Recomendação**: `ADOTAR`, `ADAPTAR`, `REFERÊNCIA`, `REJEITAR`, `PENDENTE`.

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
`LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md` §3-bis.

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
| Links, IDs, segredos e estrutura validados | PASS — `python3 tools/validate.py`: 0 erros, 0 avisos |
| Fase 4 (medição em hardware) | **NOT RUN** — exige execução na máquina do usuário |
| Revisão humana da entrega | **PENDENTE** — protocolo em `agents/REVIEW-PROTOCOL.md` |

`NOT RUN` e `BLOCKED` **não** são `PASS`. Detalhamento, incluindo o que ficou bloqueado
e por quê: `LIA-RESEARCH-FOUNDATION-REPORT.md`.

## 10. Os seis relatórios de entrega

| Documento | O que responde |
|---|---|
| `LIA-RESEARCH-FOUNDATION-REPORT.md` | o que foi construído, com que status, e o que não foi |
| `LIA-RESEARCH-SOURCE-INVENTORY.md` | toda fonte com origem, commit, data e modo de uso |
| `LIA-RESEARCH-EXTERNAL-REPOSITORY-AUDIT.md` | os 16 objetos externos, vereditos e armadilhas |
| `LIA-RESEARCH-CONSOLIDATION-REPORT.md` | duplicatas, conflitos e o que a consolidação resolveu |
| `LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md` | como um agente consulta sem virar dependência |
| `LIA-RESEARCH-ROADMAP.md` | as 4 fases do próximo ano, com critério de parada |
| `LIA-RESEARCH-PHASE-CLOSURE-REPORT.md` | encerramento da fase Research, com pendências por responsável |

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
