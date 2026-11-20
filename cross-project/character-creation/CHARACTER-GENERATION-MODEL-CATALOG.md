# Catálogo de modelos e ferramentas de geração visual

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-007` |
| Categoria | model |
| Projetos | Lia Forge 2.0, Lia Studio |
| Fontes | `gh api` (licença, atividade, releases) e API de modelos do Hugging Face (licença de pesos, SHA, contagem de parâmetros), lidos em 2026-11-20; READMEs oficiais para requisitos de hardware |
| Data | 2026-11-20 |
| Revisão | 2026-11-21 (rodada 7.1: correções de licença, hardware, vídeo e contagens) |
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
5. **Vocabulário de evidência desta série** (pedido da rodada 7.1):
   `OFFICIAL_LICENSE` (texto de licença lido), `OFFICIAL_DOCUMENTATION` (README/doc oficial),
   `PAPER_OR_RESEARCH`, `COMMUNITY_REPORTED`, `TESTED` (executado por nós),
   `INFERRED`, `UNVALIDATED`, `BLOCKED`. Equivalência com o vocabulário do repositório
   (`catalog/CATALOG-SCHEMA.md` §6): `OFFICIAL_*` → `CONFIRMED`; `PAPER_OR_RESEARCH` →
   `REPORTED`; `COMMUNITY_REPORTED` → `REPORTED`; `UNVALIDATED` → `UNVERIFIED`.
   **`TESTED` não aparece em nenhuma linha deste catálogo** — nada foi executado.

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
- SDXL (2,57 B ≈ 5,1 GB em fp16) é o **candidato de menor porte** da lista. Não afirmo que
  "cabe confortavelmente": pesos não são o consumo total. Somam-se VAE, text encoders
  (dois no SDXL), ativações, resolução e overhead do driver. Medição real: `UNVALIDATED`.
- Para a RX 580, `stable-diffusion.cpp` oferece quantização GGUF, *offload* de pesos para
  disco/RAM (`--params-backend disk`) e teto por dispositivo (`--max-vram`) — ou seja, existem
  **mecanismos** para caber. Existir mecanismo não é caber com desempenho aceitável:
  `UNVALIDATED`, e com 16 GB de RAM o offload para RAM é limitado.
- Qwen-Image/Edit (≈20,4 B) e FLUX (≈11,9 B): quantizar reduz o consumo, mas não garante
  velocidade. Não trate "quantizado" como "utilizável".

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

1. **Os candidatos com requisito de hardware documentado exigem CUDA** — TRELLIS, TRELLIS.2,
   Hunyuan3D-2/2.1, TripoSG, InstantMesh e SF3D (este admite MPS, mas no Windows pede CUDA +
   VS 2022). A exceção declarada é **TripoSR**, que menciona fallback CPU via `torchmcubes`
   (`COMMUNITY_REPORTED`/`OFFICIAL_DOCUMENTATION`; desempenho `UNVALIDATED`).
   **Não afirmo que "todo image-to-3D depende de CUDA"**: Hunyuan3D-Omni não teve requisito
   de hardware lido (`UNVALIDATED`), e há modelos fora deste catálogo não avaliados.
2. **Gaussian Splatting não resolve** o problema do Forge: splat não é malha com topologia,
   não tem rig, e a conversão para malha reintroduz o problema de retopo.
3. **Hunyuan3D-2 é o único com 6 GB declarados**, mas em CUDA — portanto o número de VRAM
   não ajuda na RX 580.

## 5. Runtimes e interfaces — e o que "suporta AMD" quer dizer

| Runtime | Licença | Papel | Situação na RX 580 |
|---|---|---|---|
| ComfyUI (`comfyanonymous/ComfyUI`) | GPL-3.0 | grafo de nós, padrão de fato para experimentos | README cita "AMD ROCm on Linux and Windows"; **isso vale para GPUs suportadas, não para gfx803** |
| `stable-diffusion.cpp` (`leejet`) | MIT | inferência C/C++ sobre ggml; backends **CUDA, Vulkan, Metal**; build Windows | único caminho GPU plausível; **não validado** na RX 580 |
| ComfyUI-Zluda (`patientx`) | GPL-3.0 | CUDA em AMD via ZLUDA, comunitário | `COMMUNITY_REPORTED`; camada não oficial |
| ZLUDA (`vosen/ZLUDA`) | Apache-2.0 | tradução CUDA→AMD | `COMMUNITY_REPORTED` |

### 5.1. `stable-diffusion.cpp`: separar as quatro afirmações

| Afirmação | Situação | Evidência |
|---|---|---|
| Modelos declarados | SD1.x/2.x, SDXL, SD3/3.5, FLUX.1, FLUX.2, Qwen-Image, Qwen-Image-Edit, Z-Image, Chroma, PixArt e outros (lista extensa no README) | `OFFICIAL_DOCUMENTATION` |
| Backends implementados | **CUDA, Vulkan, Metal**. **Não encontrei OpenCL nem DirectML** na documentação do projeto | `OFFICIAL_DOCUMENTATION` (README + `docs/guides/backend.md`) |
| Sistemas suportados | Linux e Windows (README traz comandos PowerShell e caminho `bin/Release`) | `OFFICIAL_DOCUMENTATION` |
| Combinações testadas | o README **não** publica matriz de "modelo × backend × placa" testada | ausência de evidência |
| Resultado na RX 580 | um relato comunitário (abaixo) | `COMMUNITY_REPORTED` |

O projeto permite atribuição de backend **por módulo** (`--backend te=cpu,vae=cuda0,diffusion=vulkan0`),
`--params-backend disk` para manter pesos fora da VRAM e `--max-vram` por dispositivo. É a
base técnica do *offload*; continua sem garantia de velocidade.

### 5.2. Relato comunitário na RX 580 (`COMMUNITY_REPORTED`)

| Cenário | Tempo reportado | Observação |
|---|---|---|
| SD 1.5, 512×512, 20 passos | ≈ 72 s | mesma faixa de hardware (Polaris 8 GB) |
| FLUX.1-schnell, 1024×1024, CPU+GPU | ≈ 14 min | combinação CPU+GPU, não GPU pura |

Classificação: **`COMMUNITY_REPORTED`**, não benchmark independente e não medição do Lia
Research. Não generalizo para outras versões do runtime, para outro build Vulkan ou para
outros modelos. Serve para calibrar expectativa de ordem de grandeza: **minutos, não segundos**,
e FLUX na casa de dezenas de minutos.

### 5.3. DirectML e OpenCL

| Caminho | Situação | Classificação |
|---|---|---|
| DirectML (`torch-directml`) | o repositório `microsoft/torch-directml` **não foi encontrado** na API (404) nesta sessão | `BLOCKED` — não é possível afirmar suporte atual |
| OpenCL | não é backend documentado em `stable-diffusion.cpp`; nenhum dos modelos do catálogo declara caminho OpenCL | `UNVALIDATED` |

Nenhum dos dois entra como recomendação. Ficam como linha de investigação futura, não como
alternativa disponível.

## 6. Serviços comerciais — direitos, créditos e preços

Todos os dados abaixo foram lidos em **2026-11-20**, nas URLs indicadas. Não são parecer
jurídico; onde o texto é ambíguo, marco `REQUIRES_LEGAL_REVIEW`.

### 6.1. Tripo (`tripo3d.ai`) — Free, Pro, Max, Team

Preços lidos em `https://www.tripo3d.ai/pricing` e direitos em `https://www.tripo3d.ai/terms`
(termos com "Last updated: November 13, 2026").

| Plano | Preço | Créditos | Uso comercial | Privacidade do resultado |
|---|---|---|---|---|
| Free | US$ 0 | 200 créditos/mês | **sim, mas com waiver** (ver abaixo) | **público por padrão** |
| Pro | US$ 20/mês (anual US$ 240) | 3.000/mês | sim, direitos do usuário | privado |
| Max | US$ 90/mês (anual US$ 1.080) | 25.000/mês | idem | privado |
| Team | US$ 55/assento/mês (anual) | 90.000/mês | idem | privado |

**O que o termo diz sobre o plano gratuito** (§5.2.1, texto lido): *Free Outputs* são públicos
por padrão; o usuário **renuncia** aos direitos autorais sobre eles e permite que qualquer
pessoa, no mundo, os use, copie, modifique, distribua ou **explore comercialmente, sem
atribuição**. Onde a renúncia não é possível juridicamente, concede licença pública
irrevogável e gratuita com o mesmo escopo. Outputs pagos (§5.2.2) pertencem ao usuário, podem
ser privados e usados comercialmente.

Consequência prática: **não é "free = não comercial"** — é "free = você também não controla o
que acontece com o resultado, e ele nasce público". Para personagem de jogo, isso é
inaceitável na prática, independentemente de o uso comercial ser permitido.
`REQUIRES_LEGAL_REVIEW` apenas para o caso de a empresa querer explorar comercialmente um
output gratuito e depender de exclusividade.

**Créditos por operação** (página de preços, tabela "Feature/Credits"): HD Generate **15** ·
Smart Mesh **35** · Segmentation **5** · Retopology **5** · Texture Gen **10** · Auto Rig
**20**; add-ons: Ultra +15, Generate in Parts +30, HD Texture +10, Quad +5, Style Reference +5,
PBR +5. Ou seja: 200 créditos gratuitos ≈ **13 gerações simples** ou **5 gerações com rig**
(15 + 20).

### 6.2. Meshy (`meshy.ai`) — planos e custo por modalidade

Preço lido em `https://www.meshy.ai/pricing`; créditos por requisição em
`https://docs.meshy.ai/en/api/pricing` (2026-11-20).

| Plano | Preço | Créditos/mês | Licença do asset |
|---|---|---|---|
| Free | US$ 0 | 100 | **CC BY 4.0** (comercial **com atribuição**) |
| Pro | US$ 20/mês | 1.000 | "private & customer owned" |
| Premium | US$ 40/mês | 3.000 | idem |
| Ultra | US$ 100/mês | 8.000 | idem |
| Studio | US$ 70/mês (5.500 compartilhados) | — | idem |

**Custo real por geração — a modalidade importa** (créditos por requisição):

| API | Mesh apenas | +textura 2K | +textura 4K | +textura 8K |
|---|---|---|---|---|
| Image to 3D (`meshy-7.1`, `meshy-6`) | **20** | 30 | 30 | 35 |
| Image to 3D (`meshy-6-lite`, `meshy-t2`, `meshy-t2.5`) | **5** | 15 | 15 (lite: não suportado) | 20 |
| Multi-image to 3D | 20 | 30 | 30 | 35 |
| Ultra geometry (surcharge) | +5 | +5 | +5 | +5 |

Outros custos: **rigging 5** por requisição · **animation 3** por ação · **UV unwrap 5** ·
**remesh 5** · retexture 10 (2K/4K) ou 15 (8K).

Portanto: **"100 créditos = 10 modelos" está errado**. Com 100 créditos gratuitos: **5** imagens
para 3D sem textura (20 cada), **3** com textura 2K (30 cada), ou **20** no modo lite sem
textura (5 cada). A frase anterior deste catálogo generalizava; fica corrigida.

### 6.3. GPT Image (OpenAI) — geração e edição de imagem, sem 3D

Fontes: `developers.openai.com/api/docs/guides/image-generation` e
`developers.openai.com/api/docs/pricing` (2026-11-20).

| Item | Situação | Classificação |
|---|---|---|
| Modalidade | text-to-image **e** edição dentro da Responses API; `action: generate / edit / auto`; edição multi-turno via `previous_response_id` | `OFFICIAL_DOCUMENTATION` |
| Modelos citados | `gpt-image-2.5-sunburst` (exemplos), `gpt-image-2.6-sunburst` / `-flare` (tabela de preços) | `OFFICIAL_DOCUMENTATION` |
| Preço | por token: imagem de entrada US$ 8/1M, saída US$ 30/1M (Standard); Batch pela metade | `OFFICIAL_DOCUMENTATION` |
| Character sheet / consistência | **não há garantia documentada** de consistência entre vistas; multi-turno preserva contexto, não identidade | `UNVALIDATED` |
| 3D | **não oferece** reconstrução 3D | `OFFICIAL_DOCUMENTATION` |
| Direitos e retenção | termos e política de dados da OpenAI — **não lidos nesta rodada** | `UNVALIDATED` |

### 6.4. Google Flow (`flow.google.com`) — estúdio web por assinatura

Fonte: `flow.google.com/about` e `support.google.com/flow` (2026-11-20).

| Item | Situação | Classificação |
|---|---|---|
| Natureza | **aplicação web** de criação (imagem + vídeo + ferramentas), modelos Google (Nano Banana para imagem, Veo 3.1 para vídeo, Gemini Omni) | `OFFICIAL_DOCUMENTATION` |
| Acesso | por **assinatura Google AI**; recursos variam por nível, plataforma e região; 18+ | `OFFICIAL_DOCUMENTATION` |
| API | a página do Flow **não** documenta API do produto; há API Gemini para modelos de imagem, que é outro caminho | `UNVALIDATED` para Flow-como-API |
| Character sheet / consistência | Nano Banana é descrito como forte em "subject consistency"; **sem garantia de turnaround multi-vista** | `OFFICIAL_DOCUMENTATION` (marketing) / `UNVALIDATED` (resultado) |
| Direitos | termos do Google AI/Flow — **não lidos nesta rodada** | `UNVALIDATED` |
| 3D | **não oferece** reconstrução 3D | `OFFICIAL_DOCUMENTATION` |

Nenhum dos dois é solução de 3D. Ambos são candidatos de **conceito e edição**; a comparação
de qualidade exige teste visual, que esta rodada não fez.

### 6.5. Rodin / Hyper3D

Preço e termos **não verificados** nesta rodada. Continua `BLOCKED` como lacuna.

## 6-bis. Reallusion Character Creator 5.2 (novo candidato)

Fonte principal: `reallusion.com/character-creator/ai-character-creator.html` e
`reallusion.com/character-creator/` (2026-11-20).

| Item | O que a documentação oficial informa | Classificação |
|---|---|---|
| AI 3D Generator | geração de personagem/prop por texto ou imagem, com motores **AI Mesh**, **Tripo** e **Tencent Hunyuan** integrados | `OFFICIAL_DOCUMENTATION` |
| Entrada por imagens | image-to-3D com imagem de referência; a página mostra "reference image and target images" (1–4 imagens **não** é número que eu tenha lido explicitamente) | `OFFICIAL_DOCUMENTATION` parcial |
| CC Wrap | converte modelo humanoide (inclusive gerado por IA) em **CC Base** com topologia de personagem, por 3 passos: detectar pontos → alinhar → refinar | `OFFICIAL_DOCUMENTATION` |
| Presets anatômicos | dedos (0–5), dedos do pé, orelha/nariz — pensado para estilizado e criatura | `OFFICIAL_DOCUMENTATION` |
| Roupas | "AI Clothing to 3D": quad remesh, redução de polígonos, transferência automática de pesos | `OFFICIAL_DOCUMENTATION` |
| Rigging | AccuRIG integrado (humanoide, hard-surface, ajuste de pesos) | `OFFICIAL_DOCUMENTATION` |
| Interoperabilidade | iClone, Maya, Blender, Unreal, Unity e "qualquer outra ferramenta 3D" | `OFFICIAL_DOCUMENTATION` |
| Requisito de hardware | Windows 10/11 64-bit; **8 GB VRAM**; GPU "NVIDIA GTX 10 Series / **AMD Radeon RX5500 XT**"; 16 GB RAM; 30 GB de instalação + **200 GB de cache DDS**; recomendado 64 GB RAM e SSD | `OFFICIAL_DOCUMENTATION` (manual e KB da Reallusion) |
| **RX 580** | **não é a placa citada**. Ter 8 GB de VRAM não iguala a RX 5500 XT (RDNA1, gfx1012) à RX 580 (Polaris, gfx803) | `INFERRED` a partir do requisito publicado |
| Custos de IA | consumo por créditos/serviço dos provedores integrados (Tripo/Hunyuan) — **valores por operação não lidos** | `UNVALIDATED` |
| Licença dos resultados | EULA da Reallusion — **não lido nesta rodada** | `BLOCKED` |
| Preço do software | há teste gratuito de 30 dias; preços de licença **não coletados** | `BLOCKED` |

**Parecer de pesquisa (não recomendação):** CC5.2 é o único candidato do catálogo que ataca
explicitamente o elo "malha de IA → topologia de personagem com rig", que é justamente o que
falta nos image-to-3D abertos. Ao mesmo tempo, ele **não roda na RX 580** segundo o requisito
publicado, exige 200 GB de disco para cache e depende dos provedores de IA integrados (com as
licenças deles). Vale como **opção comercial/híbrida a avaliar em máquina compatível**, não
como caminho local no hardware de referência.

## 7. Recomendação de leitura (não de compra)

| Ordem | O que avaliar primeiro | Por quê |
|---|---|---|
| 1 | `stable-diffusion.cpp` + SDXL quantizado | único caminho local real no hardware; risco é qualidade, não licença |
| 2 | Qwen-Image-Edit (nuvem ou GPU alugada) | Apache-2.0 nos pesos e edição multi-referência — resolve "manter o casaco" |
| 3 | ControlNet + IP-Adapter sobre SDXL | controle barato e maduro para silhueta/pose |
| 4 | Tripo/Meshy (plano **pago** mínimo) | image-to-3D utilizável sem GPU; **no plano gratuito o resultado é público** (Tripo) ou exige atribuição (Meshy) |
| 5 | TRELLIS.2 / Hunyuan3D-2.1 em GPU alugada | melhor qualidade aberta, só se o orçamento justificar |

Ordem inversa ao "mais bonito": começa pelo que já cabe no hardware e no orçamento.

**Correção de 2026-11-21:** a recomendação anterior tratava Tripo/Meshy como "US$ 20/mês" sem
distinguir o que o plano gratuito concede. Com os termos lidos, o plano gratuito do Tripo
torna o output **público com renúncia de direitos** (§6.1) — para personagem de jogo, o piso
realista é o **plano pago**. No Meshy, o gratuito é CC BY 4.0 (atribuição obrigatória).

## 8. Não validado

`FLUX.2` (pesos), `CharacterGen` (pesos), `Hunyuan3D-Omni` (hardware), qualidade de
Tripo/Meshy, tempo de CPU no TripoSR, qualquer número de desempenho na RX 580, e a
afirmação de que quantização GGUF preserva qualidade suficiente para personagem.

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-SHEET-CONSISTENCY.md` · `CHARACTER-2D-TO-3D-PIPELINES.md`
