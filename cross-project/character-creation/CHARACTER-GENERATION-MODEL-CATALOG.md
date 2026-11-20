# Catálogo de modelos e ferramentas de geração visual

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-007` |
| Categoria | model |
| Projetos | Lia Forge 2.0, Lia Studio |
| Fontes | `gh api` (licença, atividade, releases) e API de modelos do Hugging Face (licença de pesos, SHA, contagem de parâmetros), lidos em 2026-11-20; READMEs oficiais para requisitos de hardware |
| Data | 2026-11-20 |
| Status | CURRENT |
| Confiança | Média-alta em licença e metadados; **baixa em desempenho** — nada foi executado |
| Natureza | pesquisa e documentação; não autoriza download de pesos nem integração |

---

## 1. Regras de leitura deste catálogo

1. **Licença de código ≠ licença de pesos.** As duas colunas existem porque quase todo erro
   de avaliação nasce de confundir uma com a outra (o código do FLUX é Apache-2.0; os pesos
   do `FLUX.1-dev` são **não comerciais**).
2. **SHA é do repositório de pesos**, não do site. Quando não li o repositório de pesos, o
   campo fica vazio em vez de ser preenchido por inferência.
3. **"Roda na RX 580?" é veredito documental**, não medição. Três valores:
   `NÃO` (exige CUDA), `VULKAN` (há caminho ggml/Vulkan, não validado no hardware),
   `NUVEM` (serviço), `?` (não determinado).
4. Nenhum peso foi baixado nesta rodada. O maior arquivo citado tem 69 GB de storage.

## 2. Modelos de imagem (text-to-image e edição)

| Modelo | Repositório oficial | Licença do código | Licença dos pesos | Pesos (SHA HF) | Parâmetros | RX 580 |
|---|---|---|---|---|---|---|
| SDXL base 1.0 | `Stability-AI/generative-models` (MIT, 27,3k★) | MIT | **OpenRAIL++** | `46216598…` | 2,57 B | `VULKAN` |
| FLUX.1-schnell | `black-forest-labs/flux` (Apache-2.0) | Apache-2.0 | **Apache-2.0** | `169573f5…` | 11,89 B | `VULKAN` |
| FLUX.1-dev | idem | Apache-2.0 | **não comercial** (`flux-1-dev-non-commercial-license`, gated) | `45d95c49…` | 11,90 B | `VULKAN` (licença limita uso) |
| FLUX.2 | `black-forest-labs/flux2` (Apache-2.0, 2,9k★) | Apache-2.0 | **não lida** nesta rodada | — | — | `?` |
| Qwen-Image | `QwenLM/Qwen-Image` (Apache-2.0) | Apache-2.0 | **Apache-2.0** | `75e0b4be…` | 20,43 B | `VULKAN` |
| Qwen-Image-Edit-2509 | `QwenLM/Qwen-Image` + HF | Apache-2.0 | **Apache-2.0** | `d3968ef9…` | 20,43 B | `VULKAN` |
| HunyuanImage-3.0 | `Tencent-Hunyuan/HunyuanImage-3.0` | **licença comunitária Tencent** (`NOASSERTION` no GitHub) | idem | — | — | `?` |

### 2.1. O que os números de parâmetros implicam (aritmética, não benchmark)

- 11,9 B em fp16 ≈ **23,8 GB** só de pesos; 20,4 B ≈ **40,8 GB**. Em 8 GB de VRAM, isso
  exige quantização (GGUF) ou offload — não é "instalar e rodar".
- SDXL (2,57 B ≈ 5,1 GB em fp16) é o único da lista que cabe confortavelmente em 8 GB.
- O caminho realista para a RX 580 é `stable-diffusion.cpp` com modelo quantizado. Isso está
  na documentação do runtime; **a qualidade resultante é `UNVERIFIED`**.

### 2.2. Licenças que mudam a decisão

| Caso | Fato | Efeito prático |
|---|---|---|
| `FLUX.1-dev` | pesos sob licença não comercial, acesso com gate | serve para estudo; não para asset de produto |
| `FLUX.1-schnell` | pesos Apache-2.0 | é a variante utilizável do FLUX |
| `HunyuanImage-3.0` | texto da licença: **não se aplica à UE, Reino Unido e Coreia do Sul** | distribuição para esses territórios fica fora dos termos |
| `Hunyuan3D-2` / `2.1` | mesma cláusula; HF marca `extra_gated_eu_disallowed: true` | idem, e o gate bloqueia download na UE |

Isso é leitura do texto, não parecer jurídico. Quem decide uso comercial é o proprietário,
com apoio jurídico se necessário.

## 3. Controle, referência e consistência (o que faz "mesmo personagem")

| Ferramenta | O que resolve | Repositório | Licença | Última atividade | RX 580 |
|---|---|---|---|---|---|
| ControlNet (SD1.5) | pose/silhueta por mapa de controle | `lllyasviel/ControlNet` | Apache-2.0 | 2024-02-25 (**parado**) | `VULKAN` |
| ControlNet++ / Union | controle unificado para SDXL | `xinsir6/ControlNetPlus` | Apache-2.0 | 2024-09-30 | `VULKAN` |
| IP-Adapter | referência de imagem (rosto, estilo) | `tencent-ailab/IP-Adapter` | Apache-2.0 | 2024-06-28 | `VULKAN` |
| InstantID | identidade facial com 1 foto | `instantX-research/InstantID` | Apache-2.0 | 2024-07-18 | `VULKAN` |
| PuLID | identidade com menos fine-tuning | `ToTheBeginning/PuLID` | Apache-2.0 | 2025-07-31 | `VULKAN` |
| PhotoMaker | identidade por empilhamento de fotos | `TencentARC/PhotoMaker` | Apache-2.0 **exceto componentes de terceiros** | 2024-10-31 | `VULKAN` |
| DreamO | edição/consistência por referência múltipla | `bytedance/DreamO` | Apache-2.0 | 2025-08-14 | `?` |
| UNO | consistência com referência (FLUX) | `bytedance/UNO` | Apache-2.0 | 2025-09-12 | `?` |
| InfiniteYou | identidade (FLUX) | `bytedance/InfiniteYou` | Apache-2.0 | 2025-08-22 | `?` |
| OmniGen2 | geração/edição unificada | `VectorSpaceLab/OmniGen2` | Apache-2.0 | 2026-03-20 | `?` |
| MV-Adapter | **multi-view** a partir de uma imagem (SDXL) | `huanngzh/MV-Adapter` | Apache-2.0 | 2025-06-26 | `?` |
| StoryDiffusion | consistência entre várias imagens | `HVision-NKU/StoryDiffusion` | Apache-2.0 | 2024-09-26 | `?` |
| ACE++ | edição por referência | `ali-vilab/ACE_plus` | **sem arquivo de licença** | 2025-04-21 | — |
| CharacterGen | imagem única → personagem 3D em A-pose | `zjp-shadow/CharacterGen` | Apache-2.0 (código) | 2025-04-11 | `NÃO` |

**Observações que valem mais que a tabela:**

- A maior parte das ferramentas de identidade (InstantID, PuLID, IP-Adapter) foi construída
  para **rosto**, não para personagem inteiro. Elas resolvem "é a mesma pessoa?" e falham em
  "é o mesmo casaco, com o mesmo fecho e o mesmo bolso".
- `ACE++` sem licença é um caso de exclusão imediata: código público não é licença.
- Vários projetos com `?` são FLUX-based: herdam o custo de 12 B e a licença dos pesos que
  carregam, então o veredito da RX 580 depende do modelo-base, não do repositório.

## 4. Image-to-3D e text-to-3D

| Modelo | Licença do código | Licença dos pesos | Hardware declarado (README) | Saída | RX 580 |
|---|---|---|---|---|---|
| TRELLIS | MIT | **MIT** (`microsoft/TRELLIS-image-large`) | **NVIDIA ≥ 16 GB**, CUDA toolkit, renderer CUDA (`diffoctreerast`) | malha com material | `NÃO` |
| TRELLIS.2 | MIT | MIT | **NVIDIA ≥ 24 GB**, CUDA 12.4, flash-attn | malha + UV/remesh CUDA | `NÃO` |
| Hunyuan3D-2 | licença comunitária Tencent | idem | **6 GB** (forma) / **16 GB** (forma+textura), `--low_vram_mode` | malha + textura | `NÃO` (CUDA) |
| Hunyuan3D-2.1 | licença comunitária Tencent | idem (`extra_gated_eu_disallowed`) | **10 GB** forma / **21 GB** textura / **29 GB** total | malha + PBR | `NÃO` |
| Hunyuan3D-Omni | licença comunitária Tencent | idem | não lida | malha | `NÃO` |
| TripoSR | MIT | MIT | **~6 GB**, menção a fallback CPU via `torchmcubes` | malha | `?` (CPU, a validar) |
| TripoSG | MIT | MIT (`VAST-AI/TripoSG`) | **CUDA, ≥ 8 GB** | malha | `NÃO` |
| InstantMesh | Apache-2.0 | Apache-2.0 (`TencentARC/InstantMesh`) | **CUDA ≥ 12.1**, Python ≥ 3.10 | malha multi-view | `NÃO` |
| Stable Fast 3D | sem `LICENSE` na raiz do GitHub | **Stability Community** (gated) | CUDA ou MPS; no Windows exige **VS 2022** + CUDA | malha + textura assada | `NÃO` |
| LGM | MIT | — | CUDA (Gaussian splatting) | splats → malha | `NÃO` |
| stable-dreamfusion | Apache-2.0 | — | CUDA | SDS, legado | `NÃO` |

### 4.1. O que isso significa para a decisão

1. **Não existe image-to-3D de qualidade em 8 GB AMD no Windows hoje**, com base na
   documentação oficial de todos os candidatos relevantes. O único com caminho não-CUDA
   declarado é TripoSR (CPU), e CPU para 3D é lento por definição — tempo não medido.
2. **Gaussian Splatting não resolve** o problema do Forge: splat não é malha com topologia,
   não tem rig, e a conversão para malha reintroduz o problema de retopo.
3. **Hunyuan3D-2 é o único com 6 GB declarados**, mas em CUDA — portanto o número de VRAM
   não ajuda na RX 580.

## 5. Runtimes e interfaces

| Runtime | Licença | Papel | RX 580 |
|---|---|---|---|
| ComfyUI (`comfyanonymous/ComfyUI`) | GPL-3.0 | grafo de nós, padrão de fato para experimentos | depende do backend; README cita AMD ROCm em Linux e Windows |
| `stable-diffusion.cpp` (`leejet`) | MIT | inferência em C/C++ sobre ggml, **backend Vulkan**, build Windows, SDXL/FLUX/Qwen-Image/edição | **único caminho GPU plausível** |
| ComfyUI-Zluda (`patientx`) | GPL-3.0 | CUDA em GPU AMD via ZLUDA, comunitário | `?` — camada não oficial |
| ZLUDA (`vosen/ZLUDA`) | Apache-2.0 | tradução CUDA→AMD | `?` |

Sobre ComfyUI em AMD: o README cita ROCm em Linux **e Windows**, mas a matriz do HIP SDK
para Windows não lista a RX 580 (gfx803) — e marca até RDNA2 como não suportado. Ou seja:
"ComfyUI suporta AMD no Windows" é verdade para GPUs suportadas, **não para esta**.

## 6. Serviços comerciais (lidos nas páginas de preço, 2026-11-20)

| Serviço | Preço de entrada | Licença do asset no plano gratuito | Observação |
|---|---|---|---|
| Tripo | Free (200 créditos ≈ 13 modelos); Pro US$ 20/mês | free = **modelos públicos, uso não comercial** | Pro dá modelos privados + uso comercial; tem DCC bridge (Blender, Unity, Godot…) |
| Meshy | Free (100 créditos, ~10 assets); Pro US$ 20/mês | free = **CC BY 4.0** (comercial com atribuição) | Pro = "private & customer owned" |
| Rodin / Hyper3D | **não verificado** | — | página não consultada nesta rodada |

Preço não é qualidade: **não avaliei a qualidade de nenhum dos dois**. O que dá para afirmar
é o custo de entrada e a diferença de licença entre free e pago — que é justamente onde
times erram.

## 7. Recomendação de leitura (não de compra)

| Ordem | O que avaliar primeiro | Por quê |
|---|---|---|
| 1 | `stable-diffusion.cpp` + SDXL quantizado | único caminho local real no hardware; risco é qualidade, não licença |
| 2 | Qwen-Image-Edit (nuvem ou GPU alugada) | Apache-2.0 nos pesos e edição multi-referência — resolve "manter o casaco" |
| 3 | ControlNet + IP-Adapter sobre SDXL | controle barato e maduro para silhueta/pose |
| 4 | Tripo/Meshy (assinatura mínima) | image-to-3D utilizável sem GPU; base para comparar com o caminho manual |
| 5 | TRELLIS.2 / Hunyuan3D-2.1 em GPU alugada | melhor qualidade aberta, só se o orçamento justificar |

Ordem inversa ao "mais bonito": começa pelo que já cabe no hardware e no orçamento.

## 8. Não validado

`FLUX.2` (pesos), `CharacterGen` (pesos), `Hunyuan3D-Omni` (hardware), qualidade de
Tripo/Meshy, tempo de CPU no TripoSR, qualquer número de desempenho na RX 580, e a
afirmação de que quantização GGUF preserva qualidade suficiente para personagem.

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-SHEET-CONSISTENCY.md` · `CHARACTER-2D-TO-3D-PIPELINES.md`
