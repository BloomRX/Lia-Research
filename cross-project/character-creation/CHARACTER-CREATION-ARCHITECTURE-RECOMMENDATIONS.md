# Arquitetura de referência para o Lia Forge 2.0

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-010` |
| Categoria | forge |
| Projetos | Lia Forge 2.0 |
| Fontes | pedido de pesquisa (nomes dos componentes); `LR-FORGE-005` (Blender/MCP); `LR-LIC-002` (proveniência); `LR-STUDIO-008` e `LR-STUDIO-009` (silhueta e sheet); `LR-FORGE-007` (pipelines) |
| Data | 2026-11-20 |
| Revisão | 2026-11-21 (rodada 7.1: correções de licença, hardware, vídeo e contagens) |
| Status | CURRENT |
| Confiança | Baixa-média — **não li os contratos do Forge**; a proposta é de fronteira, não de implementação |
| Natureza | recomendação arquitetural; **não é decisão** e não autoriza alteração no produto |

---

## 1. Limite de escopo, declarado antes de qualquer proposta

O repositório `BloomRX/Lia-Forge` **não está acessível** pela API nesta sessão (404). Portanto:

- Não li `Workflow Engine`, `Intelligent Orchestrator`, `Tool Provider Hub`, `Asset Pipelines`,
  `Asset Management`, `Project Visual Profile`, `Style Lock` nem `Change Impact Report`.
- Os nomes acima vêm do pedido. Uso-os como **rótulos de responsabilidade**, não como
  contratos existentes.
- Nada aqui propõe mudar interface, schema ou módulo do Forge. Propõe **onde** cada
  responsabilidade deveria morar **se** a leitura do código confirmar o que o pedido descreve.

Isso não é formalidade: uma recomendação de arquitetura feita sem ler o código é hipótese, e
hipótese que se apresenta como decisão vira dívida.

## 2. A sequência de 10 etapas — como hipótese de pesquisa

**Procedência (corrigida em 2026-11-21):** esta sequência vem da **ordem de pesquisa recebida
do proprietário** — ela não é extraída do vídeo citado no pedido, que é um teste comparativo de
modelos de linguagem para criação de jogos e não descreve processo de personagem
(`CHARACTER-CREATION-RESEARCH.md` §1.1). Trato a sequência como hipótese a validar com o
proprietário, não como prática documentada.

```
1 Character Brief
2 Silhouette Exploration  ──┐
3 Silhouette Review         │ aprovação humana (gate 1)
4 Character Concept        ─┘
5 Character Sheet           ── gate 2 (consistência + construtibilidade)
6 3D Blockout               ── gate 3 (proporção × conceito)
7 3D Refinement
8 Rigging e preparação      ── gate 4 (técnico: rig, pesos, GLB)
9 Game Integration
10 Reference Validation
```

### 2.1. Dependências reais

| Etapa | Depende de | Saída mínima |
|---|---|---|
| 2 | 1 (brief com função e elenco) | N silhuetas + eixos de variação |
| 3 | 2 | silhueta aprovada + hash |
| 4 | 3 | concept em 1 vista, coerente com a silhueta |
| 5 | 4 | vistas canônicas + inventário de detalhes |
| 6 | 5 | blockout com proporção medida |
| 7 | 6 | malha com topologia utilizável |
| 8 | 7 | rig + pesos + blendshapes |
| 9 | 8 | asset importado e animando |
| 10 | 9 | relatório de divergência vs. referência aprovada |

### 2.2. Etapas opcionais (e quando são obrigatórias)

| Etapa | Opcional quando | Obrigatória quando |
|---|---|---|
| Silhouette Exploration | personagem já tem referência canônica aprovada (variante de cor) | personagem novo ou redesign |
| Character Concept | o sheet sai direto da silhueta (raro) | precisa de material/cor antes do sheet |
| 3D Blockout | reconstrução multi-view já entrega volume correto | sempre que houver dúvida de proporção |
| Rigging | asset é cenário/prop | personagem animável |
| Reference Validation | protótipo descartável | qualquer asset que entra em jogo |

### 2.3. Pontos de aprovação e retornos

| Gate | Aprova o quê | Pode retornar para | Custo do retorno |
|---|---|---|---|
| 1 — Silhouette Review | forma e diferenciação | 1 (brief) ou 2 (exploração) | baixo |
| 2 — Sheet | consistência e construtibilidade | 4 (concept) ou 3 (silhueta) | médio |
| 3 — Blockout | proporção | 5 (sheet) ou 6 (refazer blockout) | alto |
| 4 — Técnico | rig/pesos/GLB | 7 (malha) | alto |

**Regra que a pesquisa sustenta:** quanto mais tarde o gate, mais caro o retorno — e o gate 1 é
o único barato. Isso justifica investir na etapa 2, que é onde o Forge 2.0 quer começar.

## 3. Onde cada responsabilidade deveria morar

| Responsabilidade | Componente natural | Por quê | O que **não** deve fazer |
|---|---|---|---|
| Ordenar etapas e gates | Workflow Engine | é fluxo com estados | não decide qualidade nem escolhe modelo |
| Escolher ferramenta por etapa | Tool Provider Hub | é catálogo de provedores | não guarda regra de estilo |
| Decidir *se* e *com o quê* gerar | Intelligent Orchestrator | é política | não implementa chamada de modelo |
| Executar geração/edição | Tool Provider (adaptador) | isola credencial e formato | não decide aprovação |
| Medir silhueta, sheet, malha | Asset Pipelines (QA) | é validação determinística | não "corrige" sozinho |
| Guardar versões e hashes | Asset Management + proveniência | é histórico auditável | não reescreve aprovado |
| Definir paleta/formas do mundo | Project Visual Profile | é contexto do projeto | não é prompt de modelo |
| Impedir deriva de estilo | Style Lock | é contrato de comparação | não é aprovação estética |
| Explicar impacto de mudança | Change Impact Report | é rastreio de dependências | não aprova mudança |

### 3.1. Fronteira que evita duplicação

- **Orchestrator não gera.** Se ele chama modelo diretamente, o Tool Provider Hub perde razão
  de existir e a credencial vaza para a camada de política.
- **Workflow não pontua.** Se o engine mede qualidade, o critério fica preso ao fluxo e não é
  reutilizável em outro pipeline.
- **Style Lock não aprova.** Ele compara; quem aprova é humano (gate) ou política do projeto.

## 4. Artefato de personagem — proposta de forma, não de schema

Cada etapa produz um artefato com os mesmos campos de governança que o Research já usa:

| Campo | Exemplo | Por quê |
|---|---|---|
| `id` do artefato | `char-0042-sil-07` | identidade estável |
| `etapa` | `silhouette` | permite filtrar e auditar |
| `pai` | `char-0042-brief` | linhagem, sem ambiguidade |
| `hash` | SHA-256 do arquivo | prova de "não mudou" |
| `técnica` | `vulkan-sdxl-q8` / `manual-blockout` | explica o resultado |
| `modelo` + versão | nome + SHA dos pesos | troca de modelo muda a escala |
| `medidas` | proporção, IoU vs. pai | base do QA |
| `aprovação` | humano + data + rationale | o gate fica registrado |
| `licença` | do modelo/peso usado | sem isso o asset não é distribuível |

Sem `modelo` + `hash`, o Change Impact Report não consegue responder "o que muda se eu trocar
o gerador?" — e essa pergunta é inevitável em 12 meses.

## 5. Consultas que o sistema deveria conseguir responder

Estas são o teste de utilidade da arquitetura; se não responde, não importa o diagrama.

1. "Qual silhueta foi aprovada e com que hash?"
2. "Esta malha deriva de qual sheet e de qual concept?"
3. "Quais assets usam pesos não comerciais?" (FLUX-dev, Hunyuan)
4. "Se eu trocar o gerador de imagem, quantos assets são afetados?"
5. "Quais personagens do elenco têm silhueta com IoU acima de X entre si?" (homogeneidade)
6. "Qual etapa consumiu mais tempo neste personagem?"
7. "Este GLB passou no gate técnico e quando?"

## 6. Riscos arquiteturais

| Risco | Efeito | Mitigação |
|---|---|---|
| Guardar só o resultado, não o processo | impossível reproduzir ou auditar | artefato com pai, técnica, modelo, hash |
| Deixar a IA "resolver" proporção | erro confiante | blockout medido contra o sheet |
| Style Lock virar prompt | deriva silenciosa | comparação objetiva (distância a referência) |
| Gate 1 sem registro | aprovação vira memória | aprovação como artefato |
| Pipeline único | dependência de fornecedor | três pipelines, escolha por projeto |
| Licença por último | retrabalho | licença no artefato desde a etapa 2 |

## 7. O que recomendo como próximo passo (pesquisa, não implementação)

1. **Ler o código do Forge** e comparar esta fronteira com o que existe. Sem isso, a proposta
   continua hipótese.
2. **Prototipar só o gate 1**: silhueta → métricas baratas → revisão humana, num caderno, sem
   tocar no produto.
3. **Escolher um personagem piloto** e rodar o Pipeline 2 completo, medindo tempo por etapa —
   é o único número que falta para decidir.
4. **Fixar a política de licença** antes de gerar o primeiro asset que possa ir para jogo.

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-2D-TO-3D-PIPELINES.md`
