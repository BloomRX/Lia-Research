# LIA-RESEARCH — Relatório de Consolidação

> **Nota de vocabulário (2026-11-20).** Este documento é relatório de entrega da consolidação (histórico) e preserva o texto da
> época. O vocabulário de recomendação foi substituído em 2026-11-20 por
> `ADAPT` / `REFERENCE_ONLY` / `REJECT` / `DIRECT_INTEGRATION_CANDIDATE`
> (`catalog/CATALOG-SCHEMA.md` §4.1). Nada aqui foi promoção a aprovação de adoção.


| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| O que consolida | 1.620 documentos de 5 projetos + 16 alvos externos |
| O que **não** consolida | nada foi movido, reescrito ou apagado em projeto de origem |
| Saída | 21 digests + 4 comparações + 5 dossiês + 3 documentos de estado |

---

## 1. O problema que a consolidação resolve

O ecossistema produz muita pesquisa e não tem onde guardá-la de forma consultável.
Consequências medidas no inventário:

| Sintoma | Medida | Evidência |
|---|---|---|
| Mesmo documento, várias versões | `13-GOVERNANCA-DE-EXPERIMENTOS.md` tem **7**; 4 com 4 versões cada | `data/inventory/lia-doc-versions.tsv.gz` |
| Pesquisa só em branch de sessão | 511 de 1.620 docs fora de `main` | `ecosystem/ECOSYSTEM-MAP.md` |
| Autoridade duplicada | 2 catálogos de modelo, 2 avaliações de LFM3, 3 reconciliações de UI/UX | `LR-MODEL-001`, `LR-MODEL-003`, `LR-UI-004` |
| Documento órfão | 4 documentos de arquitetura do Project com versões divergentes (25 KB cada) | `projects/lia-project/INDEX.md` |
| Licença ausente onde há distribuição | 0/48 Skills com licença no payload | `LR-LIC-001` |

## 2. Como a consolidação foi feita

Quatro modos, escolhidos por tipo de material:

| Modo | Quando | Exemplo |
|---|---|---|
| **Ponteiro** | documento vive e é mantido no projeto | todos os `INDEX.md` e digests |
| **Digest** | conhecimento espalhado em 3+ documentos | `cross-project/hardware/*`, `LR-MODEL-004` |
| **Comparação** | pergunta de decisão com 2+ objetos | `comparisons/*` |
| **Dossiê** | apresentação de um projeto inteiro | `projects/*/README.md` |

Regra dura: **nenhum digest substitui o original**. Todo digest declara
`repo@commit:caminho` da fonte. O original continua canônico; o digest é atalho de leitura.

## 3. Mapa da consolidação

```text
ecosystem/            → estado agregado (mapa, posse, capacidades, stack)
projects/<5>/         → onde mora cada pesquisa interna + duplicatas conhecidas
cross-project/hardware/   ← Project (research) + Model-Lab (08-HARDWARE)
cross-project/ai-models/  ← Project (capability-catalog) + Model-Lab (05, 17)
cross-project/model-routing/ ← Project (provider catalog/architecture/recommendations)
cross-project/voice/      ← Project (11 documentos de voz/áudio/QA)
cross-project/security/   ← Project (6 auditorias) + Studio (runtime) + AgentHub (trust)
projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md ← AgentHub (36 KB) + árvore
cross-project/agents/     ← Forge (T14) + Studio (ARENA-*) + AgentHub (catalog)
```

## 4. Duplicatas e conflitos — registro explícito

| Tipo | Objeto | Situação | Ação |
|---|---|---|---|
| Duplicata de conteúdo | `lia-brand-check` × `lia-brand-consistency-review` | duas Skills, mesmo propósito, projetos diferentes | `DR-0007` |
| Duplicata de conteúdo | 3 Skills de orquestração (Project, Model-Lab, `alethe`) | sobreposição | `DR-0007` |
| Conflito de autoridade | catálogo de modelo do Project × Model-Lab | nenhum é dono | `M-1` |
| Conflito de método | duas avaliações de LFM3 com critérios distintos | compatíveis, não reconciliadas | `M-1` |
| Conflito de número | commits de `main` (349 vs 228) | corrigido para **349** | feito |
| Versões divergentes | 5 documentos do Model-Lab (até 7 versões) | não consolidado | decisão do projeto |
| Conflito arquitetural | 4 documentos de arquitetura com 2 versões no Project | não consolidado | decisão do projeto |

**Não consolidei versões divergentes de propósito.** Escolher a "certa" sem o autor
presente seria inventar intenção. O que fiz: tornar o conflito visível, com tamanho e
branch de cada versão, para que ele possa ser resolvido por quem tem autoridade.

## 5. Os cinco achados da consolidação

### 5.1 A duplicação não é de texto, é de autoridade
Nenhum par de documentos diz coisas opostas. O problema é ter dois lugares que decidem.
Isso custa mais caro que uma contradição: contradição se resolve, ambiguidade de dono se
arrasta.

### 5.2 O material bom está na branch errada
Os melhores documentos (arquitetura de provider, auditoria de licença de Skill,
compatibilidade de hardware) existem em `arena/*`. Em `main`, não. Quem lê `main`
trabalha com informação de semanas atrás e não sabe.

### 5.3 O ecossistema já documenta os próprios erros — e isso é um ativo
Há `LIA-SECURITY-RECONCILIATION.md`, `LIA-UIUX-RECONCILIATION.md`,
`LIA-AUDIO-EVIDENCE-RECONCILIATION.md`, `06-ERRATA-E-REVISAO.md`. Prática rara e
valiosa: corrigir registro em vez de reescrever história. Preservada como padrão em
`governance/EVIDENCE-STANDARDS.md`.

### 5.4 A licença é o passivo mais concreto
Não é hipótese jurídica: 12 Skills do Studio têm aviso MIT fora do payload e serão
exportadas como payload independente. No dia em que a exportação existir, o produto
distribui material sem a obrigação que a licença exige.

### 5.5 O instrumento existe, a medição não
`tools/desktop-benchmark`, `docs/08-BANCADA-DE-MEDICAO.md`, matriz de QA de áudio de
38 KB. Tudo pronto, nada rodado. O gargalo não é conhecimento — é execução no hardware.

## 6. O que a consolidação deixa pendente (declarado)

| Pendência | Dono | Registro |
|---|---|---|
| ~~Auditar 28 skills AIRI + `alethe`~~ | **feito** em `LR-LIC-003` | 19 de 28 ficaram `RESEARCH_ONLY` |
| Consolidar 5 documentos com versões divergentes | Model-Lab | `projects/lia-model-lab/INDEX.md` §3 |
| Eleger catálogo canônico de modelo | Project + Model-Lab | `M-1` |
| Unificar 4 documentos de arquitetura do Project | Project | `projects/lia-project/INDEX.md` |
| Pesquisa de visão/multimodal | ninguém | `R-4` (não criar pasta vazia) |

## 7. Critério de sucesso desta consolidação

Um agente que entra hoje, sem contexto, consegue responder em **duas consultas**:

1. "o que já sabemos sobre X?" → `RESEARCH-INDEX.md` → documento;
2. "esse X vale a pena?" → documento → veredito + evidência + o que falta.

Se precisar de três, a consolidação falhou. Se a resposta for "vale", sem medição,
a base mentiu.
