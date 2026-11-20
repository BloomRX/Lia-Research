# 2D → 3D: comparação de pipelines e o que é "pronto para jogo"

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-007` |
| Categoria | forge |
| Projetos | Lia Forge 2.0 |
| Fontes | `CHARACTER-GENERATION-MODEL-CATALOG.md` (licenças e hardware), READMEs oficiais, CharNeRF (arXiv 2402.17115), Pix3D (CVPR 2018) para métricas, glTF 2.0 (Khronos) para formato |
| Data | 2026-11-20 |
| Revisão | 2026-11-20 (UTC) — 7.1: licença, hardware, vídeo e contagens; 7.3: conciliação Tripo/Meshy/Flow/ROCm |
| Status | CURRENT |
| Confiança | Média — comparativo documental; nenhum pipeline foi executado ponta a ponta |
| Natureza | pesquisa e documentação; não autoriza implementação |

---

## 1. Três coisas que não são a mesma coisa

| Nível | Definição operacional | Como saber que chegou lá |
|---|---|---|
| **Visualmente convincente** | render de uma vista parece o conceito | render 3/4 aprovado por humano |
| **Geometricamente adequado** | volume fecha em 360°, sem buraco, simetria e proporção corretas | turntable sem artefato; proporção medida ≈ conceito |
| **Pronto para jogo** | topologia, UV, materiais, rig, pesos, LOD e exportação válidos | importa em engine, anima sem colapsar, cabe no orçamento de polígonos |

Um modelo de image-to-3D atual entrega, na melhor das hipóteses, o **primeiro** nível e
parte do segundo. Declarar "game-ready" porque o render é bonito é o erro que este documento
existe para evitar.

## 2. As abordagens, comparadas

| Abordagem | Como funciona | Força | Fraqueza estrutural | RX 580 |
|---|---|---|---|---|
| Image-to-3D (single image) | LRM/difusão gera geometria a partir de 1 imagem | rápido, barato | inventa o que não vê (costas) | todos os demais exigem CUDA; exceção declarada: CPU via TripoSR (`UNVALIDATED`) |
| Multi-view reconstruction | 3–5 vistas → geometria | coerente com o sheet | depende de sheet consistente | nuvem/CUDA |
| Text-to-3D | texto → geometria | zero insumo | controle baixo, difícil de dirigir | nuvem/CUDA |
| Gaussian Splatting | otimiza nuvem de gaussianas | visual excelente | **não é malha**; sem rig; retopo depois | implementações usuais em CUDA (`UNVALIDATED` para alternativas) |
| Modelagem assistida por IA | IA sugere/remenda dentro do DCC | mantém controle e topologia | exige artista; ferramenta menos madura | local viável |
| Blockout manual | primitivas + proporção | controle total, topologia limpa desde o início | tempo humano | local, custo zero de GPU |
| Híbrido | IA para conceito/base, humano para estrutura | melhor relação qualidade/custo real | disciplina de processo | misto |

## 3. Os 12 critérios, um por um

Notas de 1 a 5 são **julgamento documental**, não medição. Onde não há base, está dito.

| # | Critério | Image-to-3D aberto | Multi-view | Blockout manual | Híbrido (IA + artista) |
|---|---|---|---|---|---|
| 1 | Semelhança visual | 4 (bom em forma geral) | 4 | 2 (depende do artista) | 4 |
| 2 | Fidelidade às proporções | 3 | 4 | **5** | 4 |
| 3 | Qualidade geométrica (superfície) | 3 | 3 | **5** | 4 |
| 4 | Topologia (quadros, loops) | **1** (triângulos irregulares) | 1 | **5** | 4 (com retopo) |
| 5 | Simetria | 3 | 3 | **5** | 4 |
| 6 | Controle de anatomia | 2 | 3 | **5** | 4 |
| 7 | Separação de peças (roupa, cabelo) | 1 (malha única) | 2 | **5** | 4 |
| 8 | Cabelo e roupas | 2 (blob) | 2 | **5** | 4 |
| 9 | Texturas e materiais | 3 (atlas assado) | 3 | 4 | 4 |
| 10 | Preparação para rigging | **1** | 2 | **5** | 4 |
| 11 | Animação e deformação | 1 | 1 | **5** | 4 |
| 12 | Exportação para jogo (GLB/glTF) | 3 (exporta; pode vir pesado) | 3 | **5** | 4 |

**Leitura honesta:** a coluna "Image-to-3D aberto" ganha em velocidade e perde em tudo o que
importa para jogo. As notas 1 e 2 nos critérios 4, 7 e 10 não são exagero: malha gerada por
difusão não tem loops de deformação, não separa casaco de corpo, e não tem onde pintar pesos.

### 3.1. Onde a IA realmente ajuda no 3D

| Etapa | Ajuda real | Não substitui |
|---|---|---|
| Referência de volume | gerar base para o artista "esculpir por cima" | proporção e planos |
| Textura | projeção/geração de textura a partir do conceito | UV correto |
| Variações de detalhe | ornamento, pattern, dano | estrutura de malha |
| Rigging assistido | auto-rig por biblioteca | pesos e correções em áreas de deformação |
| Pós-processo | remesh/decimate | decisão de orçamento de polígonos |

## 4. As três propostas de pipeline

### 4.1. Pipeline 1 — Local e econômico (hardware de referência)

```
Brief → 20 silhuetas (Vulkan/CPU) → revisão humana → concept em 1 vista
→ sheet por edição (2–4 vistas) → blockout manual no Blender
→ IA só como referência de textura → retopo/UV/rig manuais → GLB
```

| Dimensão | Avaliação |
|---|---|
| Qualidade final | média (depende do artista) |
| Fidelidade visual | alta em forma, baixa em textura |
| Custo | **R$ 0** de software; tempo humano é o custo |
| Tempo | maior de todos |
| Hardware | RX 580 para imagem (Vulkan via `stable-diffusion.cpp`; **`UNVALIDATED`**) + Blender |
| Dependências externas | nenhuma conta |
| Direitos de uso | limpos se usar SDXL (OpenRAIL++) e Blender |
| Maturidade | alta (ferramentas antigas e estáveis) |

### 4.2. Pipeline 2 — Híbrido (**candidato prioritário para avaliação prática**, não padrão aprovado)

```
Brief → silhuetas locais → aprovação → concept (Qwen-Image-Edit via GPU alugada ou nuvem)
→ sheet com edição multi-referência → image-to-3D em serviço (Tripo pago ou Meshy)
→ retopo no Blender + UV (xatlas/Instant Meshes) → rig (Rigify/auto-rig) → GLB
```

| Dimensão | Avaliação |
|---|---|
| Qualidade final | alta em conceito, média-alta em malha |
| Fidelidade visual | alta (edição preserva o aprovado) |
| Custo | assinatura US$ 20–100/mês + eventual GPU/hora |
| Tempo | fração do pipeline 1 |
| Hardware | o local continua sendo o gargalo de silhueta; o passo de concept/sheet exige GPU alugada ou nuvem (RX 580/gfx803 sem caminho oficial) |
| Dependências externas | fornecedor de 3D + eventual GPU |
| Direitos de uso | depende do plano **e do canal**. **Tripo Free: `CONFLICTING`** — a página de preços diz "Public Models · Non-Commercial Use" e o termo (§5.2.1, 2026-11-13) diz que o output nasce público, o usuário renuncia a direitos e **qualquer terceiro** pode explorar comercialmente, sem atribuição; a página de preços **não** consta da ordem de precedência do §12.9; e duas **páginas de ajuda oficiais** afirmam que a Tripo retém todos os direitos de Inputs e Outputs de usuários gratuitos (citando termos de 11/07/2025). Tripo pago (Pro US$ 20/mês, 3.000 créditos): direitos do usuário, privado, comercial — coerente entre página e termo. **Meshy Web App Free: CC BY 4.0** (comercial **com atribuição**, output do usuário), com teto de **10 downloads/mês** e meshes só de 6 Lite sem textura — 6/7/T2.5 e texturizados exigem upgrade; Meshy pago: privado, comercial e download ilimitado. **Meshy API é pré-paga** e o **plano Free não tem acesso à API, mesmo comprando créditos** (Help Center oficial); os 100 créditos gratuitos são do canal Web App. Detalhe em `CHARACTER-GENERATION-MODEL-CATALOG.md` §6.1–6.2; `REQUIRES_LEGAL_REVIEW` para o Free do Tripo |
| Maturidade | média (serviços mudam rápido) |

### 4.3. Pipeline 3 — Alta qualidade

```
Brief → exploração ampla → aprovação → concept por modelo de fronteira
→ sheet multi-view (MV-Adapter/edição forte) → reconstrução em GPU alugada
(TRELLIS.2 / Hunyuan3D-2.1) ou escultura manual → retopo/UV/rig/textura em DCC
→ validação técnica (LOD, materiais, animação) → GLB/FBX para engine
```

| Dimensão | Avaliação |
|---|---|
| Qualidade final | a melhor que o orçamento permitir |
| Fidelidade visual | alta |
| Custo | GPU/hora + artista; o mais caro |
| Tempo | médio (paraleliza) |
| Hardware | nenhum local obrigatório |
| Dependências externas | fornecedor de GPU |
| Direitos de uso | atenção: Hunyuan exclui UE/UK/Coreia; FLUX-dev é não comercial |
| Maturidade | média; exige operação técnica |

## 5. Comparação lado a lado

| Critério de decisão | Pipeline 1 | Pipeline 2 | Pipeline 3 |
|---|---|---|---|
| Melhor para | aprender, volume baixo, soberania de dados | produção recorrente | personagem de vitrine |
| Pior para | prazo curto | quem exige tudo local | orçamento apertado |
| Risco principal | tempo humano | dependência de fornecedor | custo e licença |
| Reversível? | sim | parcial (dados no serviço) | parcial |
| Precisa de artista? | **sim, muito** | sim | sim, especializado |

## 6. "Pronto para jogo": critérios objetivos que o Forge pode checar

| Critério | Verificação automática | Limite aceitável (proposta, não norma) |
|---|---|---|
| Malha fechada (manifold) | contagem de bordas abertas | 0 para personagem |
| Normais coerentes | orientação consistente | 100% |
| UV sem sobreposição | checagem de ilhas | 0 sobreposição fora de espelhamento intencional |
| Contagem de polígonos | soma de triângulos | depende do alvo (definir por projeto) |
| Escala e origem | altura em metros, pés no chão | conforme Project Visual Profile |
| Rig: huesos nomeados e hierarquia | validação de esqueleto | padrão do projeto |
| Pesos: sem vértice sem influência | soma de pesos | 1.000 ± tolerância |
| Blend shapes presentes | lista | conforme briefing |
| Exportação GLB válida | validador glTF | 0 erro |
| Animação de teste | play de clipe neutro | sem colapso visual |

Nenhum desses itens é verificado pelos modelos de image-to-3D. **Todos** são verificáveis por
script — e é aí que o Forge ganha confiabilidade sem depender de IA.

## 7. Recomendação

1. **Pipeline 2 é o candidato prioritário para avaliação prática — não um padrão de produção
   aprovado.** Ele depende de fornecedor externo, de plano pago e de termos que o proprietário
   precisa aceitar; aprová-lo é decisão dele, não desta pesquisa. Pipeline 1 como modo de
   soberania/offline, Pipeline 3 como exceção orçada. Nenhum dos três está aprovado.
2. **Image-to-3D entra como gerador de base, nunca como entrega.** A saída é insumo de retopo.
3. **O gate de qualidade é técnico, não estético**: manifold, UV, rig, pesos, GLB.
4. **Não adotar splatting** no caminho de personagem de jogo enquanto não houver conversão
   com topologia utilizável.

## 8. Não validado

Tempo real de cada pipeline; qualidade de Tripo/Meshy; se TripoSR em CPU é utilizável; se
TRELLIS.2 em GPU alugada (24 GB) é economicamente melhor que escultura manual; e qualquer
número de polígonos típico de saída dos modelos abertos.

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-GENERATION-MODEL-CATALOG.md` · `CHARACTER-PRODUCTION-TOOLS-ASSESSMENT.md`
