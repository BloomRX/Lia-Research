# Criação de personagens — visão geral, reutilização e conclusões

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-007` |
| Categoria | studio / forge |
| Projetos | Lia Forge 2.0 (consumidor), Lia Studio |
| Fontes | 51 registros na matriz de evidências (46 originais + 3 da rodada 7.1 + 2 da 7.2) (repositórios, páginas oficiais e serviços; ver `CHARACTER-CREATION-EVIDENCE-MATRIX.tsv`), página pública do vídeo com transcrição parcial, e a pesquisa interna listada em §2 |
| Data | 2026-11-20 |
| Revisão | 2026-11-20 (UTC) — 7.1: licença, hardware, vídeo e contagens; 7.3: conciliação Tripo/Meshy/Flow/ROCm |
| Status | CURRENT |
| Confiança | Média — catálogo de ferramentas verificado em fonte primária; **nenhum modelo foi executado** no hardware de referência |
| Natureza | pesquisa e documentação; **não autoriza implementação** no Forge |

---

## 1. A pergunta desta pesquisa

O pedido do Forge 2.0 define um princípio: **a identidade visual e a silhueta do personagem
têm de ser resolvidas antes de começar a construção definitiva em 3D.**

### 1.1. O vídeo de referência (`youtube.com/watch?v=lKDVvJcSB14`) — corrigido

A rodada anterior dizia que não tinha conseguido assistir ao vídeo e, ao mesmo tempo, um dos
documentos atribuía a ele a sequência "exploração → ficha → 3D → jogo". **As duas coisas não
podiam estar certas.** Na rodada 7.1 obtive a página pública do vídeo com transcrição parcial.

| Campo | Valor |
|---|---|
| Título | "GPT 6.2 ASTRA é Realmente TUDO ISSO que Estão Falando?" |
| Canal | MagmaDev |
| Publicação | 2026-11-19 · duração 45:58 · 4.496 visualizações (na leitura) |
| Natureza | **teste comparativo de modelos de linguagem para desenvolvimento de jogos** (GPT 6.2 Astra/Sol vs. alternativas), com foco em custo e resultado |
| O que a parte acessível mostra | criação de um jogo de fazenda/ovelhas a partir de game design; personagem (bruxa) gerada e **refeita 3–4 vezes com técnicas e ferramentas diferentes** para comparar custo/qualidade; uso de um framework próprio de modelagem 3D ("Asset Forge 3D", Python) para gerar assets sem manipular o Blender |
| Classificação da evidência | `COMMUNITY_REPORTED` (relato de terceiro; transcrição parcial lida) |
| O que **não** encontrei no trecho acessível | qualquer método de "silhueta primeiro", ficha/turnaround canônico, vistas ortográficas ou critérios de avaliação de silhueta |

**Consequência:** o vídeo deixa de ser fonte de processo nesta série. A sequência de dez
etapas vem **da ordem de pesquisa recebida do proprietário** (e é tratada como hipótese em
`CHARACTER-CREATION-ARCHITECTURE-RECOMMENDATIONS.md`), não do conteúdo audiovisual. O vídeo
permanece útil como **relato sobre custo de modelos de fronteira** — outro assunto.
`BLOCKED` para qualquer outra afirmação: só a primeira parte da transcrição estava acessível,
e não assisti ao vídeo.

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
| Pipeline completo 2D→3D→jogo | **não** | — | `LR-FORGE-007` (três pipelines propostos; nenhum aprovado) |
| Encaixe no Forge 2.0 | **não** | — | `LR-FORGE-010` |
| Skills candidatas | **parcial** (49 capacidades no Forge, 1 skill) | Forge index | `LR-AGENT-012` |

Nenhum item acima foi "pesquisado de novo" a partir do zero: os quatro primeiros reutilizam
método, licença e arquitetura já registrados; só o conteúdo técnico é novo.

## 3. O que foi verificado, e como

**Convenção de datas:** todas as datas desta série são **UTC**. Os commits do repositório são
carimbados em UTC e o horário local de referência é São Paulo (**UTC−3**); um commit de
`2026-11-20T20:04Z` corresponde a `2026-11-20 17:04` em São Paulo. Datas sem hora indicam o dia
em UTC — foi o que corrigiu a divergência entre "revisão em 2026-11-21" nos documentos e o
carimbo `2026-11-20` do commit.

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

## 5. Conclusão da frente de hardware (revisada)

Hardware de referência: Windows · **Radeon RX 580 8 GB (Polaris, gfx803)** · Ryzen 5 5500 · 16 GB RAM.

### 5.1. O que é fato, e o que era generalização minha

| Afirmação | Situação corrigida | Evidência |
|---|---|---|
| "PyTorch com ROCm só existe no Linux" | **Errado como afirmação geral, e corrigido.** A AMD publica, em documentação própria, **PyTorch 2.9.1 + ROCm 7.2.1 + Python 3.12 para Windows 11** em APUs **Ryzen AI** de arquitetura **gfx1150/gfx1151** (Ryzen AI Max+ 395, Max 390, Max 385, AI 9 HX 375/370/365, HX 475/470/465), com wheels em `repo.radeon.com` e driver 26.2.2. Fora desse recorte, o seletor do PyTorch continua oferecendo ROCm só para Linux | `OFFICIAL_DOCUMENTATION` |
| Suporte Ryzen AI no Windows | **suporte oficial para SKUs listados** — não é "todo Ryzen", não é "toda Radeon". A própria AMD anota que "the entire ROCm stack is not yet supported on Windows" | `OFFICIAL_DOCUMENTATION` |
| "A RX 580 não é suportada pelo HIP SDK no Windows" | **continua válido**: a lista oficial de GPUs suportadas no Windows não inclui a RX 580 e marca até RDNA2 (gfx1030) como não suportada | `OFFICIAL_DOCUMENTATION` (rocm.docs.amd.com, HIP SDK 7.2) |
| "ROCm não cobre gfx803" | **continua válido**: a matriz do ROCm 10.2 lista Radeon de gfx1030 para cima, e a matriz Windows/Ryzen AI só traz gfx1150/gfx1151 | `OFFICIAL_DOCUMENTATION` |
| Ryzen 5 5500 + RX 580 (referência) | **não contemplado** por nenhuma matriz oficial: o Ryzen 5 5500 não é APU Ryzen AI e a RX 580 é gfx803 | `OFFICIAL_DOCUMENTATION` (por ausência nas listas) |
| "gfx803 não aparece em nenhum lugar" | correto para as páginas lidas; não afirmei suporte comunitário | `UNVALIDATED` para builds comunitários |

Resumo utilizável: **não existe caminho oficial de GPU AMD para esta placa, nem no Linux
(por arquitetura) nem no Windows (por lista de suporte)**. Isso não diz nada sobre builds
comunitários, que não avaliei.

### 5.2. `stable-diffusion.cpp`: o que está provado e o que não está

| Pergunta | Resposta | Classe |
|---|---|---|
| Modelos declarados | SDXL, FLUX.1/2, Qwen-Image e Qwen-Image-Edit, SD3.5, Z-Image, Chroma, PixArt, entre outros | `OFFICIAL_DOCUMENTATION` |
| Backends | **CUDA, Vulkan, Metal**. OpenCL e DirectML **não constam** na documentação do projeto | `OFFICIAL_DOCUMENTATION` |
| Windows | suportado (builds e comandos PowerShell no README) | `OFFICIAL_DOCUMENTATION` |
| Combinações testadas | **não há matriz publicada** de modelo × backend × placa | ausência de evidência |
| Na RX 580 | um relato comunitário: SD 1.5 512²/20 passos ≈ **72 s**; FLUX.1-schnell 1024² em CPU+GPU ≈ **14 min** | `COMMUNITY_REPORTED` |

**Portanto:** aparecer na mesma lista de modelos suportados **não** torna SDXL, FLUX ou
Qwen-Image "compatíveis com a RX 580". O que se pode dizer é: existe um caminho (Vulkan) e um
relato de que ele funciona em SD1.5, com FLUX na casa de dezenas de minutos. SDXL e Qwen-Image
na RX 580: `UNVALIDATED`.

### 5.3. Memória: por que "cabe" é uma afirmação enganosa

Pesos não são consumo. O total inclui VAE, text encoders (o SDXL tem dois), ativações,
resolução de saída, buffers do backend e overhead do driver. Com 8 GB de VRAM e 16 GB de RAM:

| Modelo | Pesos (fp16, aritmética) | O que é preciso para caber | Situação |
|---|---|---|---|
| SDXL (2,57 B) | ≈ 5,1 GB | sobra para VAE/encoders **se** ativações couberem | candidato de menor porte; `UNVALIDATED` |
| FLUX.1-schnell (11,9 B) | ≈ 23,8 GB | quantização agressiva + offload/tiling | `UNVALIDATED` |
| Qwen-Image / Edit (20,4 B) | ≈ 40,8 GB | quantização + offload pesado | `UNVALIDATED` |

O runtime oferece `--params-backend disk` e `--max-vram`, ou seja, **mecanismos** de offload.
Mecanismo não é desempenho: com 16 GB de RAM, mover pesos para RAM/SSD significa
processamento em CPU em boa parte do tempo. Não chamo nenhum desses casos de "utilizável"
sem medição.

### 5.4. Image-to-3D no hardware de referência

| Modelo | Requisito documentado | Veredito |
|---|---|---|
| TRELLIS | NVIDIA ≥ 16 GB + CUDA toolkit + renderer CUDA | `UNVALIDATED` para RX 580; requisito oficial incompatível |
| TRELLIS.2 | NVIDIA ≥ 24 GB + CUDA 12.4 | idem |
| Hunyuan3D-2 | 6 GB (forma) / 16 GB (total), CUDA | idem |
| Hunyuan3D-2.1 | 10 / 21 / 29 GB, CUDA | idem |
| Hunyuan3D-Omni | **requisito não lido** | **sem veredito** — antes eu havia classificado como `NÃO`; corrigido para `UNVALIDATED` |
| TripoSG | CUDA ≥ 8 GB | idem |
| InstantMesh | CUDA ≥ 12.1 | idem |
| SF3D | CUDA ou MPS; Windows exige CUDA + VS 2022 | idem |
| **TripoSR** | ≈ 6 GB; **menciona fallback CPU** (`torchmcubes` sem CUDA) | **exceção**: caminho CPU declarado, desempenho `UNVALIDATED` |

Conclusão honesta: **não há evidência de image-to-3D utilizável nesta GPU**, e o único caminho
não-CUDA declarado é CPU (TripoSR), sem número de tempo.

Nota de precisão acrescentada na rodada de conciliação: o fato de a AMD ter suporte oficial a
ROCm/PyTorch no Windows **para APUs Ryzen AI gfx1150/gfx1151** não alcança a RX 580 (gfx803)
nem o Ryzen 5 5500. São recortes de hardware diferentes; tratar um como o outro seria o mesmo
erro que esta série vem corrigindo.

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
| 2 — Híbrido | conceito local + image-to-3D em nuvem (Tripo pago ou Meshy) + retopo/rig no Blender | uso regular, previsível | assinatura mensal + revisão humana |
| 3 — Alta qualidade | conceito em modelo de fronteira (Qwen-Image-Edit/FLUX Kontext), vistas com adapter multi-view, reconstrução em GPU alugada, produção manual | personagem de vitrine | GPU/hora + artista |

Nenhuma delas é "a escolha". A comparação item a item está em `CHARACTER-2D-TO-3D-PIPELINES.md` §4.

## 8. Ferramentas que eu recomendo — e as que eu não recomendo

**Recomendadas para avaliação (não para adoção automática):**

| Ferramenta | Por quê | Licença (código / pesos) |
|---|---|---|
| `stable-diffusion.cpp` | único runtime de difusão com Vulkan e build Windows entre os que verifiquei; declara SDXL, FLUX, Qwen-Image e edição — **declarar não é rodar na RX 580** | MIT / depende do modelo carregado |
| SDXL base 1.0 | base aberta, ecossistema de ControlNet/IP-Adapter mais maduro, 2,57 B parâmetros — **candidato de menor porte**, não "cabe confortavelmente" | MIT (código) / OpenRAIL++ |
| Qwen-Image e Qwen-Image-Edit-2509 | Apache-2.0 nos pesos, edição com múltiplas imagens de referência | Apache-2.0 / Apache-2.0 |
| ControlNet (SDXL) + IP-Adapter | controle de pose/silhueta e referência de personagem, ambos abertos | Apache-2.0 / Apache-2.0 |
| MV-Adapter | adapter multi-view em SDXL: ataca diretamente o problema de turnaround | Apache-2.0 / Apache-2.0 |
| Blender | mais completo, GPL-2.0+, automação por processo externo | GPL-2.0-or-later |
| Instant Meshes / xatlas | retopologia e UV determinísticos, sem nuvem | BSD-3 / MIT |
| TripoSR (CPU, a validar) | único image-to-3D com menção explícita a fallback CPU — exceção declarada, tempo `UNVALIDATED` | MIT / MIT |
| Blender + CC Wrap (Reallusion) como referência de "IA → topologia de personagem" | mostra o elo que falta nos modelos abertos; CC5.2 exige GPU ≥ RX 5500 XT (a RX 580 não é citada) e 200 GB de cache | GPL-2.0-or-later / proprietário |
| `live2d-add-motion-sample-web-ui` (`LR-FORGE-009`) | **como padrão de fluxo**, não como tecnologia: gerador + validador independente + verificação visual headless + Definition of Done + documentação para agente | MIT no repo / **Core proprietário** e release license da Live2D |
| AetherAI (`LR-MODEL-008`) | candidato a testar **para animação de sprite 2D**, porque o termo de direitos é o mais claro entre os serviços lidos — e porque o caminho local na RX 580 não cobre isso | proprietário (SaaS) / n.a. |

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
| Plano **gratuito** do Tripo para personagem de jogo | `CONFLICTING`: a página de preços diz "Non-Commercial Use" e o termo (§5.2.1) diz que qualquer terceiro pode explorar comercialmente o output, com renúncia de direitos do usuário. Enquanto não for esclarecido, não serve para asset proprietário |
| Plano **gratuito** do Meshy como entrega final | CC BY 4.0: comercial, mas com atribuição obrigatória — decisão de produto, não técnica |
| Live2D como caminho de personagem **3D** | a tecnologia é 2D por construção: não gera malha, não exporta GLB |
| AetherAI para **3D, rig ou GLB** | o serviço não faz nada disso; a animação é por sprites |

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

## 8-ter. Revisão cruzada da rodada 7.1 — contradições encontradas e corrigidas

Releitura dos 8 documentos contra as fontes obtidas em 2026-11-20/21 (a rodada 7.2 acrescentou
mais dois documentos, revisados de forma independente). Sete contradições,
todas corrigidas na fonte, não "harmonizadas" no texto:

| # | Contradição | Onde estava | Correção |
|---|---|---|---|
| 1 | "não assisti ao vídeo" no hub vs. "o vídeo descreve esta ordem" na silhueta | §1 do hub, §1 de `LR-STUDIO-008` | vídeo identificado como teste de LLM para jogos; atribuição removida; sequência reatribuída ao pedido |
| 2 | Tripo Free descrito como "não comercial" | matriz (coluna de licença), §4.2 dos pipelines | Free = output **público** + renúncia de direitos + licença pública com uso comercial por terceiros (§6.1 do catálogo) |
| 3 | "100 créditos = 10 modelos" no Meshy | matriz, nota do catálogo | custo por modalidade: 20 / 30 / 35 créditos; 100 créditos = 3–5 modelos típicos ou 20 no modo lite |
| 4 | "ROCm/PyTorch só Linux" generalizado | §5 do hub, §5 do catálogo | separado em: ROCm Linux, oficial Windows CUDA/CPU, APU Ryzen AI (restrito, `UNVALIDATED`), gfx803 sem suporte em nenhum dos dois |
| 5 | "todos os image-to-3D exigem CUDA" com Hunyuan3D-Omni marcado como `NÃO` | §5.4, matriz | Omni sem requisito lido → `UNVALIDATED`; TripoSR (CPU) mantido como exceção |
| 6 | "SDXL cabe confortavelmente em 8 GB" | §2.1 do catálogo, tabela do hub | "candidato de menor porte", com a lista do que consome memória além dos pesos |
| 7 | `blender --background --python` tratado como "processo externo" | §2.1 de `LR-FORGE-008` | o script roda **dentro** do processo do Blender (`bpy`); distinção refeita, com `REQUIRES_LEGAL_REVIEW` |

Mais duas correções de método: a matriz passou a usar o vocabulário de evidência de 8 rótulos
(substituindo `CONFIRMED`, que sugeria mais certeza do que havia) e a regra de "componente
conexo único" virou regra **por arquétipo** — a versão anterior reprovaria robôs, criaturas e
mascotes legítimos.

## 9. Itens não validados (declarados, não escondidos)

| Item | Por que não validei |
|---|---|
| Desempenho de qualquer modelo na RX 580 | sem GPU AMD nesta sessão; nenhum peso baixado. O único dado é `COMMUNITY_REPORTED` (SD1.5 ≈ 72 s; FLUX ≈ 14 min em CPU+GPU) |
| Se `stable-diffusion.cpp` + Vulkan roda SDXL ou Qwen-Image em 8 GB | exige execução; a documentação declara suporte de modelo, não de placa |
| DirectML como caminho | repositório `microsoft/torch-directml` deu 404 na API; `BLOCKED` |
| Termos de Reallusion, OpenAI e Google Flow | não lidos nesta rodada |
| Requisito de hardware do Hunyuan3D-Omni | README não lido para esse fim |
| Qualidade visual comparada de Tripo/Meshy/Rodin | exigiria conta paga e julgamento humano; preços lidos, qualidade não |
| Se TripoSR roda em CPU em tempo utilizável | README menciona fallback CPU, não dá tempo |
| Licença dos pesos de FLUX.2 e de CharacterGen | não lidas nesta rodada |
| Conteúdo dos documentos do Forge sobre personagem/cabelo | repositório inacessível (404) |
| Automação Blender headless no Windows do usuário | já era `NOT RUN` em `LR-FORGE-005`; continua |
| Conteúdo do vídeo de referência | obtida apenas a página pública com transcrição parcial; **o vídeo não foi assistido** e o restante do conteúdo é `BLOCKED` |
| Direitos e preços de Reallusion, OpenAI e Google Flow | páginas de produto lidas; EULA/termos **não** lidos |
| `microsoft/torch-directml` (DirectML) | 404 na API nesta sessão: `BLOCKED` |
| Suporte ROCm/Windows para APUs Ryzen AI | **resolvido nesta rodada**: documentação oficial da AMD cobre Windows 11 + gfx1150/gfx1151 com PyTorch 2.9.1/ROCm 7.2.1. Fora desses SKUs, nada muda |

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
6. **Plano pago de serviço 3D**: o gratuito do Tripo é `CONFLICTING` (página diz não comercial;
   termo permite exploração comercial por terceiros) e o do Meshy exige atribuição (CC BY 4.0).
   Se o Forge produzir asset de jogo, o piso é plano pago (US$ 20–100/mês) ou caminho local.

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
| `AETHERAI-GAME-ASSET-SERVICE-RESEARCH.md` | serviço de assets 2D: funções, direitos do resultado, tokens, proibições contratuais |
| `LIVE2D-MOTION-AUTHORING-RESEARCH.md` | autoria de movimento por JSON, padrão gerador+validador+verificação, pilha de licenças |
| `CHARACTER-CREATION-EVIDENCE-MATRIX.tsv` | **51 registros** (52 linhas com o cabeçalho: 46 da rodada 7.0 + 3 da 7.1 + 2 da 7.2): licença de código × pesos, hardware, nível de evidência |

Contagem do conjunto: **10 IDs, 10 documentos Markdown e 1 matriz com 51 registros**
(46 da rodada 7.0 + 3 candidatos da 7.1 + 2 objetos da 7.2).

> `LR-FORGE-009` ficou livre nas rodadas 7.0 e 7.1 justamente para não inventar documento só
> para fechar sequência. Na rodada 7.2 ele foi ocupado por um objeto real
> (`LIVE2D-MOTION-AUTHORING-RESEARCH.md`). `LR-MODEL-008` é o serviço AetherAI.

Voltar: `README.md` · `projects/lia-forge/INDEX.md` · `RESEARCH-INDEX.md`
