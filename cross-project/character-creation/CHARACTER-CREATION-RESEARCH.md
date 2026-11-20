# Criação de personagens — visão geral, reutilização e conclusões

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-007` |
| Categoria | studio / forge |
| Projetos | Lia Forge 2.0 (consumidor), Lia Studio |
| Fontes | 46 linhas na matriz de evidências (repositórios, páginas oficiais e serviços; ver `CHARACTER-CREATION-EVIDENCE-MATRIX.tsv`), mais a pesquisa interna listada em §2 |
| Data | 2026-11-20 |
| Status | CURRENT |
| Confiança | Média — catálogo de ferramentas verificado em fonte primária; **nenhum modelo foi executado** no hardware de referência |
| Natureza | pesquisa e documentação; **não autoriza implementação** no Forge |

---

## 1. A pergunta desta pesquisa

O pedido do Forge 2.0 define um princípio: **a identidade visual e a silhueta do personagem
têm de ser resolvidas antes de começar a construção definitiva em 3D.** O vídeo citado no
pedido (`youtube.com/watch?v=lKDVvJcSB14`) é referência de processo, não fonte técnica.

**Não assisti ao vídeo.** Não há transcrição nem acesso a conteúdo audiovisual nesta sessão;
portanto ele aparece aqui apenas como o processo que o solicitante descreveu (exploração →
ficha → 3D → jogo), e **nenhuma afirmação deste conjunto de documentos depende dele**. Se o
vídeo contiver técnica específica, ela não está coberta por esta pesquisa.

Esta rodada responde a cinco perguntas, nesta ordem de importância:

1. O princípio "silhueta primeiro" tem base metodológica documentada — e como se avalia
   uma silhueta de forma útil sem transformar nota de IA em verdade? (§4 e
   `SILHOUETTE-FIRST-DESIGN-RESEARCH.md`)
2. Que ferramentas de geração de imagem e de 3D existem, com que licença, com que hardware,
   e quais **não rodam** no hardware de referência (Windows + RX 580 8 GB)? (§5 e
   `CHARACTER-GENERATION-MODEL-CATALOG.md`)
3. É possível manter um personagem consistente entre vistas, e o que quebra nesse caminho?
   (`CHARACTER-SHEET-CONSISTENCY.md`)
4. Qual é a distância real entre "imagem bonita" e "malha pronta para jogo"?
   (`CHARACTER-2D-TO-3D-PIPELINES.md`)
5. Como isso se encaixa no Forge sem inventar contrato que eu não li?
   (`CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md`)

## 2. Reutilização: o que já existia no Lia Research

Nada aqui substitui o que já estava pesquisado. A regra do repositório é ampliar e conectar.

| Recurso existente | O que cobre | Classificação nesta rodada |
|---|---|---|
| `repositories/sculptforge/REPORT.md` (`LR-FORGE-002`) | escultura 3D, exceção de scripting, disciplina de benchmark | **reutilizável** — e a exceção de licença de 2026-11-20 importa para qualquer script de personagem |
| `repositories/artcraft/REPORT.md` (`LR-STUDIO-004`) | 17 apps criativos em Rust, barramento de comandos, formatos | **reutilizável** como arquitetura de app, não como gerador |
| `repositories/pixelfx/REPORT.md` (`LR-FORGE-004`) | VFX 2D / pixel art | **reutilizável** para pós-processamento, fora do escopo de personagem |
| `cross-project/agents/BLENDER-MCP-DIGEST.md` (`LR-FORGE-005`) | automação Blender via MCP, GPL como processo externo | **reutilizável** — é a base da etapa 6–8 do pipeline |
| `cross-project/licensing/ASSET-PROVENANCE.md` (`LR-LIC-002`) | proveniência de asset | **reutilizável** — é o que torna "Style Lock" auditável |
| `cross-project/licensing/READY-TO-USE-LICENSES.md` (`LR-LIC-005`) | avisos, GPL como processo, CC-BY-SA | **reutilizável** — usado aqui para pesos e conteúdo gerado |
| `repositories/brutal/REPORT.md` (`LR-STUDIO-005`) | framework C#/Vulkan, licenças por pacote | **reutilizável** como referência de disciplina de licença |
| Pesquisa do próprio Forge (`docs/EXTERNAL-REPOSITORY-RESEARCH.md`, 120 KB, em branch) | 40+ repositórios já triados | **precisa de atualização**, e vive fora de `main` |
| `docs/CHARACTER-HAIR-MOTION-BACKENDS-AUDIT-3D.md` (58 KB, em branch do Forge) | cabelo e motion | **requer validação** — não li o conteúdo; existe e não foi copiado |
| Documentos de pipeline do Forge (`3D-CHARACTER-PRODUCTION-PIPELINE.md`) | pipeline declarado pelo projeto | **requer validação** — pertence ao projeto, não foi duplicado aqui |

**Acesso negado, registrado:** o repositório `BloomRX/Lia-Forge` não está acessível pela API
nesta sessão (`404`). Portanto **não li** os documentos do Forge citados no índice
(`LR-FORGE-INDEX`); usei apenas os digests que já existem no Lia Research. Qualquer
recomendação de arquitetura neste conjunto de documentos é feita **sem ter lido os
contratos do Forge**, e isso está dito de novo em
`CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md` §1.

### 2.1. Matriz pesquisa anterior × necessidade nova × lacuna

| Necessidade nova (pedido) | Já existe? | Onde | Lacuna que esta rodada abre |
|---|---|---|---|
| Silhueta em preto sólido como método | **não** | — | método e critérios: `LR-STUDIO-008` |
| Avaliação automática de silhueta | **não** | — | proposta com métricas e limites: `LR-STUDIO-008` §6 |
| Geração de imagem com controle (pose, referência) | **parcial** (artcraft como app; nenhum catálogo de modelos) | `LR-STUDIO-004` | catálogo: `LR-MODEL-007` |
| Consistência entre vistas / character sheet | **não** | — | `LR-STUDIO-009` |
| Image-to-3D, text-to-3D | **menção** (`hunyuan3d`, Forge index; `LR-FORGE-005`) | Forge (fora de `main`) | comparação: `LR-FORGE-007` |
| Retopologia, UV, textura, rigging | **parcial** (Blender/MCP) | `LR-FORGE-005` | `LR-FORGE-008` |
| Pipeline completo 2D→3D→jogo | **não** | — | `LR-FORGE-009` |
| Encaixe no Forge 2.0 | **não** | — | `LR-FORGE-010` |
| Skills candidatas | **parcial** (49 capacidades no Forge, 1 skill) | Forge index | `LR-AGENT-012` |

Nenhum item acima foi "pesquisado de novo" a partir do zero: os quatro primeiros reutilizam
método, licença e arquitetura já registrados; só o conteúdo técnico é novo.

## 3. O que foi verificado, e como

| Nível de evidência | O que usei nesta rodada |
|---|---|
| **Documentação oficial / metadados primários** | `gh api` para licença, atividade, releases e README de 44 projetos; API de modelos do Hugging Face para licença de **pesos**, SHA do repo de pesos, gate e contagem de parâmetros |
| **Texto oficial de licença** | lido diretamente para os casos ambíguos (`NOASSERTION`): Hunyuan (Image 3.0 e 3D 2.0), PhotoMaker, Blender, MPFB2, Instant Meshes, ArmorPaint |
| **Documentação de hardware** | matriz de compatibilidade do ROCm 10.2 e requisitos do HIP SDK para Windows; página de instalação do PyTorch; README de cada modelo 3D com requisito de VRAM declarado |
| **Benchmark independente** | **nenhum** usado |
| **Teste próprio** | **nenhum** — não há GPU AMD no sandbox desta sessão, e baixar pesos de 12–70 GB não estava autorizado |
| **Relato de comunidade** | usado só como pista, nunca como prova (ex.: ZLUDA) |

Consequência direta: **nada aqui foi medido no hardware do usuário**. Toda afirmação de
desempenho, qualidade visual e compatibilidade com RX 580 é marcada como
`NÃO VALIDADO` quando não estiver na documentação do fabricante.

## 4. Conclusão da frente de silhueta (resumo)

O princípio "silhueta primeiro" não é preferência estética: é prática profissional
convergente em design de personagem — preencher silhuetas em preto, testar em miniatura,
diferenciar o elenco pela forma. A convergência aparece em fontes de prática
(orientações de estúdio e material didático de design), não em literatura experimental
controlada; portanto trate como **método consolidado por prática**, não como lei científica.
Detalhe e citações em `SILHOUETTE-FIRST-DESIGN-RESEARCH.md`.

O ponto mais útil para o Forge: **a avaliação automática deve ordenar candidatos, não
aprovar**. Métricas geométricas conhecidas (IoU, Chamfer, EMD) têm correlação fraca com
julgamento humano — o estudo Pix3D mediu Spearman de 0,32 (IoU), 0,43 (EMD) e 0,49
(Chamfer) contra nota humana. Um pipeline que use IoU como "aprovação" está medindo a
coisa errada com confiança alta.

## 5. Conclusão da frente de hardware (a mais dura)

O hardware de referência é Windows + **RX 580 8 GB** (gfx803, Polaris) + Ryzen 5 5500 + 16 GB.

| Fato verificado | Fonte | Consequência |
|---|---|---|
| A matriz do ROCm 10.2 lista GPUs Radeon de gfx1030 para cima; **gfx803 não aparece** | `rocm.docs.amd.com` — matriz de compatibilidade | ROCm não é caminho para a RX 580, em nenhum sistema |
| O HIP SDK para Windows 7.2 não lista a RX 580 e marca até RDNA2 (gfx1030) como **não suportado** | `rocm.docs.amd.com/projects/install-on-windows` — requisitos de sistema | "instalar ROCm no Windows" não resolve |
| O PyTorch oficial oferece ROCm apenas para Linux; Windows vem com CUDA ou CPU | `pytorch.org/get-started/locally` | `diffusers` + GPU AMD no Windows não é caminho oficial |
| `stable-diffusion.cpp` (MIT) tem backend **Vulkan**, build para Windows, e suporta SDXL, FLUX, Qwen-Image e modelos de edição | README do projeto | **é o único caminho local plausível em Vulkan** — e é CPU/GPU via ggml, não PyTorch |
| Todos os image-to-3D relevantes exigem CUDA: TRELLIS (16 GB, CUDA toolkit), TRELLIS.2 (24 GB), Hunyuan3D-2.1 (29 GB total), TripoSG (8 GB CUDA), InstantMesh (CUDA ≥ 12.1), SF3D (CUDA ou MPS; no Windows exige VS 2022) | READMEs oficiais de cada um | **2D→3D local na RX 580: inviável como caminho principal**; resta CPU (não validado) ou nuvem |

Isto não é opinião: são quatro documentos de fabricante. O que é opinião — e está marcado
como tal — é o **quanto** isso custa em tempo.

## 6. Conclusão da frente 3D (resumo)

Os modelos de image-to-3D de 2024–2026 produzem **objeto**, não **personagem de jogo**.
Nenhum deles entrega, sozinho: topologia em quadros, separação de peças de roupa, UV
limpo, rig com pesos pintados e blendshapes. O que entregam é malha visualmente
convincente, frequentemente com topologia irregular, simetria aproximada e textura
"assada" em atlas.

A comparação completa — 12 critérios, três pipelines — está em
`CHARACTER-2D-TO-3D-PIPELINES.md`. A conclusão curta: **o orçamento de tempo do Forge deve
assumir que a maior parte do trabalho está depois do modelo de IA, não antes.**

## 7. As três propostas de pipeline (uma linha cada)

| Pipeline | Ideia | Onde faz sentido | Custo dominante |
|---|---|---|---|
| 1 — Local e econômico | `stable-diffusion.cpp` (Vulkan) para conceito e vistas; corte e avaliação determinísticos; blockout manual no Blender; IA apenas como referência | hardware de referência, sem conta em serviço | **tempo humano** e qualidade limitada de vista múltipla |
| 2 — Híbrido | conceito local + image-to-3D em nuvem (Tripo/Meshy) + retopo/rig no Blender | uso regular, previsível | assinatura mensal + revisão humana |
| 3 — Alta qualidade | conceito em modelo de fronteira (Qwen-Image-Edit/FLUX Kontext), vistas com adapter multi-view, reconstrução em GPU alugada, produção manual | personagem de vitrine | GPU/hora + artista |

Nenhuma delas é "a escolha". A comparação item a item está em `CHARACTER-2D-TO-3D-PIPELINES.md` §4.

## 8. Ferramentas que eu recomendo — e as que eu não recomendo

**Recomendadas para avaliação (não para adoção automática):**

| Ferramenta | Por quê | Licença (código / pesos) |
|---|---|---|
| `stable-diffusion.cpp` | único runtime de difusão com Vulkan e build Windows; cobre SDXL, FLUX, Qwen-Image e edição | MIT / depende do modelo carregado |
| SDXL base 1.0 | base aberta, ecossistema de ControlNet/IP-Adapter mais maduro, 2,57 B parâmetros | MIT (código) / OpenRAIL++ |
| Qwen-Image e Qwen-Image-Edit-2509 | Apache-2.0 nos pesos, edição com múltiplas imagens de referência | Apache-2.0 / Apache-2.0 |
| ControlNet (SDXL) + IP-Adapter | controle de pose/silhueta e referência de personagem, ambos abertos | Apache-2.0 / Apache-2.0 |
| MV-Adapter | adapter multi-view em SDXL: ataca diretamente o problema de turnaround | Apache-2.0 / Apache-2.0 |
| Blender | mais completo, GPL-2.0+, automação por processo externo | GPL-2.0-or-later |
| Instant Meshes / xatlas | retopologia e UV determinísticos, sem nuvem | BSD-3 / MIT |
| TripoSR (CPU, a validar) | único image-to-3D com menção explícita a fallback CPU | MIT / MIT |

**Não recomendadas (com motivo):**

| Ferramenta | Motivo |
|---|---|
| TRELLIS e TRELLIS.2 | 16 GB e 24 GB de VRAM NVIDIA + CUDA toolkit + renderer CUDA próprio |
| Hunyuan3D-2.1 | 29 GB no total, e a licença **exclui UE, Reino Unido e Coreia do Sul** |
| HunyuanImage-3.0 | mesma exclusão territorial na licença comunitária |
| ACE++ | **não tem arquivo de licença** no repositório — não é utilizável por padrão |
| FLUX.1-dev | pesos sob licença **não comercial** |
| ControlNet original (lllyasviel) | parado desde 2024-02; era SD1.5 — hoje é legado |
| Instant Meshes como dependência de produto | última atividade em 2022-01; usar como ferramenta pontual, não como biblioteca |
| ZLUDA / ComfyUI-Zluda | camada não oficial, sem suporte do fornecedor; serve para experimento, não para produto |

## 8-bis. Revisão cruzada deste conjunto

Feita antes de fechar, com quatro verificações:

| Verificação | Resultado |
|---|---|
| Duplicação | a tabela de critérios de silhueta está só em `LR-STUDIO-008`; `LR-AGENT-012` aponta para ela em vez de repetir. O gate técnico de exportação está só em `LR-FORGE-007` §6; `LR-FORGE-008` §5 aponta para ele |
| Contradição | o catálogo (`LR-MODEL-007`) e os pipelines (`LR-FORGE-007`) dizem a mesma coisa sobre a RX 580: nenhum image-to-3D roda nela. Nenhuma nota de pipeline contradiz o veredito documental do catálogo |
| Recomendação sem evidência | todas as recomendações de §8 citam licença lida, requisito de hardware documentado ou ausência de licença. As que dependem de julgamento (qualidade relativa, "melhor pipeline") estão marcadas como inferência |
| Número inventado | os únicos números são: contagens de metadados (stars, parâmetros, VRAM documentada, datas), preços lidos nas páginas, Spearman do Pix3D e aritmética de memória — todos com origem declarada |

O que permanece **inferido**, e não medido: a ordem de eficácia das técnicas de sheet
(`LR-STUDIO-009` §4.1), as notas 1–5 dos 12 critérios (`LR-FORGE-007` §3) e a própria
arquitetura (`LR-FORGE-010`).

## 9. Itens não validados (declarados, não escondidos)

| Item | Por que não validei |
|---|---|
| Desempenho de qualquer modelo na RX 580 | sem GPU AMD nesta sessão; nenhum peso baixado |
| Se `stable-diffusion.cpp` + Vulkan roda SDXL em 8 GB com qualidade aceitável | exige execução; documentação não promete |
| Qualidade visual comparada de Tripo/Meshy/Rodin | exigiria conta paga e julgamento humano; preços lidos, qualidade não |
| Se TripoSR roda em CPU em tempo utilizável | README menciona fallback CPU, não dá tempo |
| Licença dos pesos de FLUX.2 e de CharacterGen | não lidas nesta rodada |
| Conteúdo dos documentos do Forge sobre personagem/cabelo | repositório inacessível (404) |
| Automação Blender headless no Windows do usuário | já era `NOT RUN` em `LR-FORGE-005`; continua |
| Conteúdo do vídeo de referência | não há acesso a vídeo nesta sessão |

## 10. Decisões que dependem do proprietário

1. **Aceitar ou não depender de nuvem** para image-to-3D. Sem isso, a meta "personagem 3D a
   partir de conceito" no hardware atual fica limitada a blockout manual.
2. **Orçamento mensal** tolerável em serviço de 3D (Tripo Pro: US$ 20/mês; Meshy Pro:
   US$ 20/mês, ambos lidos em 2026-11-20).
3. **Licença de pesos**: aceitar termos não comerciais em fase de estudo e só depois decidir
   o que entra em produto; Hunyuan exclui territórios e isso afeta distribuição.
4. **Aprovação humana obrigatória** em qual ponto: proposta é silhueta e sheet; o resto pode
   ser assistido.
5. **Onde o Style Lock mora**: no Forge (produto) ou no Research (referência)? A resposta
   muda o contrato.

## 11. Documentos deste conjunto

| Documento | Conteúdo |
|---|---|
| `SILHOUETTE-FIRST-DESIGN-RESEARCH.md` | método, linguagem de forma, critérios e automação da avaliação |
| `CHARACTER-GENERATION-MODEL-CATALOG.md` | modelos e ferramentas de imagem, licença de código × pesos, hardware |
| `CHARACTER-SHEET-CONSISTENCY.md` | vistas, turnaround, por que quebra e como reduzir |
| `CHARACTER-2D-TO-3D-PIPELINES.md` | 12 critérios, três pipelines, o que é "pronto para jogo" |
| `CHARACTER-PRODUCTION-TOOLS-ASSESSMENT.md` | blockout a exportação, automação por IA × ferramenta tradicional |
| `CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md` | encaixe no Forge 2.0, aprovações, retornos |
| `CHARACTER-CREATION-SKILLS-ANALYSIS.md` | 7 competências candidatas, entradas/saídas/critérios |
| `CHARACTER-CREATION-EVIDENCE-MATRIX.tsv` | 44 linhas: licença, hardware, nível de evidência |

Voltar: `README.md` · `projects/lia-forge/INDEX.md` · `RESEARCH-INDEX.md`
