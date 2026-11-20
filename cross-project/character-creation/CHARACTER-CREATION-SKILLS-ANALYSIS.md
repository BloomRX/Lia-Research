# Competências candidatas a skill (análise, não criação)

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-012` |
| Categoria | agent |
| Projetos | Lia Forge 2.0, Lia AgentHub |
| Fontes | `LR-FORGE-010` (fronteira de componentes), `LR-STUDIO-008` (critérios de silhueta), `LR-STUDIO-009` (QA de sheet), `LR-FORGE-007` (gate técnico) |
| Data | 2026-11-20 |
| Revisão | 2026-11-21 (rodada 7.1: correções de licença, hardware, vídeo e contagens) |
| Status | CURRENT |
| Confiança | Média — análise de responsabilidades; **nenhuma skill foi escrita** |
| Natureza | análise; o pedido proíbe criar skills definitivas nesta etapa |

---

## 1. Regra de desenho

Uma skill é **competência com critério de aceitação**, não um passo do fluxo. Se a competência
é "executar etapa 3", ela é do Workflow Engine. Se é "decidir com qual modelo", é do
Orchestrator. A skill existe quando há **julgamento técnico reutilizável** com entrada e saída
verificáveis.

Teste de três perguntas antes de propor qualquer skill:

1. Tem entrada e saída **tipadas** (não "um personagem")?
2. Tem critério de qualidade que **outro agente** consegue verificar?
3. Sobrevive à troca de ferramenta (funciona com SDXL, Qwen ou Blockout manual)?

Se falha em qualquer uma, não é skill — é etapa.

## 2. As sete competências propostas

### 2.1. Character Concept Design

| Campo | Definição |
|---|---|
| Entrada | brief estruturado (função, temperamento, escala, elenco, restrições de estilo) |
| Saída | 3 conceitos em uma vista + justificativa de cada decisão de forma |
| Ferramentas | provedor de imagem (via Tool Provider Hub), Style Lock para referência |
| Critério de aceitação | cada conceito cita a forma dominante e a proporção declarada; nenhum contradiz o brief |
| Não faz | aprovar; gerar sheet; definir preço de fornecedor |
| Risco | virar "prompt bonito" sem rastreio de decisão |

### 2.2. Silhouette Exploration

| Campo | Definição |
|---|---|
| Entrada | brief + elenco existente (para diferenciação) |
| Saída | 12–20 silhuetas preenchidas, normalizadas, com eixo de variação declarado por lote |
| Ferramentas | gerador de imagem; segmentação/remoção de fundo; métricas de §6.1 do `LR-STUDIO-008` |
| Critério de aceitação | reconhecível em 32 px; **contagem de componentes compatível com o inventário do arquétipo** (não "componente único": asas, caudas, armas e elementos flutuantes são legítimos); IoU entre variantes do mesmo lote abaixo de limite **a calibrar** |
| Não faz | escolher a vencedora; julgar originalidade |
| Risco | produzir 20 variações de ruído em vez de 20 decisões; e aplicar regra de humanoide a criatura/robô |

### 2.3. Character Sheet Generation

| Campo | Definição |
|---|---|
| Entrada | silhueta aprovada (hash) + concept aprovado + inventário de detalhes |
| Saída | vistas canônicas (frente/perfil/costas + 3/4 opcional) + manifesto |
| Ferramentas | edição multi-referência (Qwen-Image-Edit), adapter multi-view, ControlNet |
| Critério de aceitação | todas as vistas presentes; altura normalizada; inventário presente em todas; cor de roupa consistente |
| Não faz | aprovar consistência; modelar |
| Risco | sheet bonito com personagens diferentes (o erro clássico) |

### 2.4. Character Consistency Review

| Campo | Definição |
|---|---|
| Entrada | sheet + silhueta aprovada + inventário |
| Saída | relatório de divergências por item, com evidência (recorte/medida) |
| Ferramentas | IoU de silhueta, histograma por região, contagem de acessórios, similaridade de embedding como apoio |
| Critério de aceitação | cada divergência aponta dois arquivos e uma medida; nenhum veredito sem medida |
| Não faz | corrigir automaticamente; aprovar |
| Risco | confundir "diferente" com "errado" em estilo expressivo |

### 2.5. 2D-to-3D Reconstruction

| Campo | Definição |
|---|---|
| Entrada | sheet aprovado + escolha de pipeline (1/2/3) |
| Saída | malha base + relatório de origem (técnica, modelo, hash, tempo) |
| Ferramentas | image-to-3D (nuvem ou GPU), Blender headless, validador de malha |
| Critério de aceitação | malha abre no DCC; escala correta; relatório de proveniência completo |
| Não faz | declarar game-ready; fazer retopo fino |
| Risco | entregar malha que "parece" e não serve — por isso o critério é técnico |

### 2.6. 3D Quality Assessment

| Campo | Definição |
|---|---|
| Entrada | malha + sheet de referência |
| Saída | nota por critério do gate técnico (manifold, UV, polígonos, normais) + comparação de silhueta 2D×3D |
| Ferramentas | validador de malha, render ortográfico, IoU silhueta 3D×2D |
| Critério de aceitação | todo critério tem número; nenhum "parece bom" |
| Não faz | corrigir; aprovar estética |
| Risco | medir só o que é fácil e ignorar deformação |

### 2.7. Game-Ready Character Validation

| Campo | Definição |
|---|---|
| Entrada | asset com rig + animação de teste + alvo (engine, orçamento de polígonos) |
| Saída | checklist do §6 de `LR-FORGE-007` com resultado por item + GLB validado |
| Ferramentas | validador glTF, inspeção de `skins`/pesos, play de clipe neutro |
| Critério de aceitação | todos os itens verificados; falha explícita quando não verificável |
| Não faz | aprovar entrada no jogo; decidir LOD ideal |
| Risco | "passou no GLB" ser confundido com "está bom" |

## 3. O que **não** deve virar skill

| Candidato tentador | Por que não |
|---|---|
| "Gerar personagem completo" | é pipeline, não competência; duplica Workflow |
| "Escolher modelo de imagem" | é política do Orchestrator/Tool Hub |
| "Aprovar personagem" | é decisão humana, não competência de agente |
| "Aplicar Style Lock" | é comparação determinística de pipeline, não julgamento |
| "Otimizar custo de GPU" | é operação de infraestrutura |
| "Escrever prompt" | é detalhe de implementação dentro de 2.1/2.2 |

## 4. Dependências entre skills

```
2.2 Silhouette Exploration ──► 2.3 Sheet Generation ──► 2.4 Consistency Review
        ▲                                                        │
        │                                                        ▼
   2.1 Concept Design ◄────────────────────────────── 2.5 Reconstruction
                                                                 │
                                                    2.6 Quality Assessment
                                                                 │
                                                    2.7 Game-Ready Validation
```

Nenhuma skill chama outra diretamente: o encadeamento é do Workflow Engine, e a passagem é
por artefato (não por memória de conversa). Isso é o que permite trocar a skill 2.3 por um
provedor diferente sem quebrar o resto.

## 5. Contratos mínimos que cada skill precisa respeitar

| Contrato | Conteúdo |
|---|---|
| Entrada versionada | toda entrada é artefato com hash; não existe "a imagem que eu mandei antes" |
| Saída com proveniência | técnica, modelo, versão, licença, tempo |
| Falha explícita | quando não dá para verificar, a saída diz `NÃO VERIFICADO`, não inventa |
| Sem efeito colateral | skill não sobrescreve artefato aprovado |
| Custo declarado | tokens/GPU/créditos por execução, quando aplicável |
| Nenhuma credencial no payload | chamada de modelo é do Tool Provider |

## 6. Riscos de desenho de skill

| Risco | Efeito |
|---|---|
| Skill que "sabe" o modelo | fica obsoleta em meses |
| Skill que aprova | remove o humano do único ponto que importa |
| Skill que mede só o fácil | falsa confiança |
| Skill com prompt embutido | não reutilizável, não auditável |
| Muitas skills pequenas | orquestração vira o problema |

## 7. Recomendação

Começar por **duas** skills, não sete: `Silhouette Exploration` e `Character Consistency
Review`. São as que têm critério objetivo, não dependem de modelo específico e atacam
exatamente o princípio do pedido. As demais só depois de um piloto real medido.

## 8. Não validado

Nenhuma skill foi escrita, executada ou avaliada. Os critérios de aceitação são propostas
derivadas de `LR-STUDIO-008`/`009`/`007`, não resultados de teste. A fronteira com Workflow
Engine e Orchestrator é hipótese, porque os contratos do Forge não foram lidos.

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md`
