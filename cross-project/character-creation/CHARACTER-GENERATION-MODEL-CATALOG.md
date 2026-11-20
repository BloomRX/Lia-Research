# Catálogo de modelos e ferramentas de geração visual

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-007` |
| Categoria | model |
| Projetos | Lia Forge 2.0, Lia Studio |
| Fontes | `gh api` (licença, atividade, releases) e API de modelos do Hugging Face (licença de pesos, SHA, contagem de parâmetros), lidos em 2026-11-20; READMEs oficiais para requisitos de hardware |
| Data | 2026-11-20 |
| Revisão | 2026-11-20 (UTC) — 7.1: licença, hardware, vídeo e contagens; 7.3: conciliação Tripo/Meshy/Flow/ROCm |
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
6. **Datas — convenção deste conjunto:** todas as datas de consulta e revisão são **UTC**. O
   ambiente e os commits registram UTC; o horário local de referência (São Paulo) é **UTC−3**,
   de modo que `2026-11-20T20:04Z` = `2026-11-20 17:04` em São Paulo. Datas sem hora indicam o
   dia em UTC. Nenhuma fonte externa citada neste catálogo tem data posterior a 2026-11-20.
7. **A matriz de evidências passou a ter evidência por dimensão** (`evidencia_licenca`,
   `evidencia_hardware`, `evidencia_atividade`, `evidencia_desempenho`), mantendo
   `nivel_evidencia` como resumo. Motivo: uma licença lida em arquivo oficial, um requisito de
   hardware lido em documentação e um tempo relatado por terceiro são evidências de naturezas
   diferentes — resumi-las numa célula apagava a diferença. A taxonomia global do Research **não**
   foi alterada.
8. **Qualificador adicional, declarado:** `CONFLICTING` marca o caso em que **duas fontes
   oficiais do mesmo fornecedor** dizem coisas incompatíveis (hoje: Tripo, §6.1). Ele não
   substitui nenhum dos 8 rótulos — acompanha `OFFICIAL_LICENSE` e sempre vem junto de
   `REQUIRES_LEGAL_REVIEW`.

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
| ComfyUI (`comfyanonymous/ComfyUI`) | GPL-3.0 | grafo de nós, padrão de fato para experimentos | README cita "AMD ROCm on Linux and Windows"; **vale para as GPUs suportadas pela AMD (hoje gfx1150/gfx1151 em Windows), não para gfx803** |
| `stable-diffusion.cpp` (`leejet`) | MIT | inferência C/C++ sobre ggml; backends **CUDA, Vulkan, Metal**; build Windows | único caminho GPU plausível; **não validado** na RX 580 |
| ComfyUI-Zluda (`patientx`) | GPL-3.0 | CUDA em AMD via ZLUDA, comunitário | `COMMUNITY_REPORTED`; camada não oficial |
| ZLUDA (`vosen/ZLUDA`) | Apache-2.0 | tradução CUDA→AMD | `COMMUNITY_REPORTED` |

### 5.0. AMD no Windows: o que é oficial hoje (ROCm 7.2.1 + Ryzen AI)

Fontes: `rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityryz/windows/windows_compatibility.html`
e `.../install/installryz/windows/install-pytorch.html`, lidas em 2026-11-20 (UTC).

| Item | O que a documentação oficial diz | Classificação |
|---|---|---|
| SO | **Windows 11** | `OFFICIAL_DOCUMENTATION` |
| Arquiteturas | **gfx1150** e **gfx1151** (APUs Ryzen AI) | `OFFICIAL_DOCUMENTATION` |
| SKUs listados | Ryzen AI Max+ 395, Max 390, Max 385, AI 9 HX 375/370/365, AI 9 HX 475/470/465 | `OFFICIAL_DOCUMENTATION` |
| Stack | **ROCm 7.2.1**, **PyTorch 2.9.1**, **Python 3.12**, FP16 | `OFFICIAL_DOCUMENTATION` |
| Instalação | wheels oficiais em `repo.radeon.com/rocm/windows/rocm-rel-7.2.1/` (`rocm_sdk_*`, `torch-2.9.1+rocm7.2.1`), driver gráfico 26.2.2 | `OFFICIAL_DOCUMENTATION` |
| Escopo | nota da própria AMD: *"PyTorch on Windows includes ROCm 7.2 components; however, the entire ROCm stack is not yet supported on Windows"* | `OFFICIAL_DOCUMENTATION` |
| **Radeon RX 580 / gfx803** | **não aparece** em nenhuma matriz Windows | ausência de evidência |
| **Ryzen 5 5500** (hardware de referência) | **não é APU Ryzen AI** e não está na lista | ausência de evidência |

**Correção de classificação:** na rodada anterior o suporte Ryzen AI no Windows aparecia como
`UNVALIDATED` por eu não ter encontrado wheel oficial no seletor do PyTorch. **Estava
desatualizado**: a AMD distribui wheels próprios no `repo.radeon.com`, fora do seletor do
PyTorch. Passa a `OFFICIAL_DOCUMENTATION`.

**O que isso NÃO muda:** a conclusão sobre o equipamento de referência (Ryzen 5 5500 + RX 580,
gfx803) permanece — nenhuma das matrizes oficiais, nem a do ROCm Linux nem a do Windows/Ryzen
AI, contempla gfx803. E "PyTorch no Windows com componentes ROCm 7.2" **não** equivale a "o
stack ROCm completo no Windows".

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

### 6.1. Tripo (`tripo3d.ai`) — preço e termo **discordam** sobre o plano gratuito

Fontes lidas em **2026-11-20 (UTC)**: `https://www.tripo3d.ai/pricing` (tabela de planos) e
`https://www.tripo3d.ai/terms` ("Last updated: November 13, 2026"; §5.2, §5.2.1, §5.2.2,
§5.2.3 e §12.9).

**Classificação do caso: `CONFLICTING` + `REQUIRES_LEGAL_REVIEW`.** `CONFLICTING` é um
qualificador pontual — duas fontes oficiais do mesmo fornecedor dizem coisas diferentes — e não
substitui a taxonomia de 8 rótulos; ele acompanha o rótulo `OFFICIAL_LICENSE` (as duas fontes
são oficiais).

#### 6.1.1. O que cada texto diz, literalmente

| Fonte | Texto | O que afirma |
|---|---|---|
| Página de preços, plano Free | *"200 Monthly Credits ≈ 13 Models"*, *"Public Models · Non-Commercial Use"*, *"Exports 15 (H2.5 only)"*, *"Limited Access"* em HD model / 8K / Smart Topology | o plano gratuito é **público** e de **uso não comercial** |
| Página de preços, Pro/Max/Team | *"Private Models · Commercial Use"* | o uso comercial aparece como **benefício do plano pago** |
| Termos §5.2.1 | Free Outputs "are public by default"; o usuário concorda, na medida permitida por lei, em **renunciar** aos direitos autorais e permitir que **"anyone, worldwide and permanently"** use, copie, modifique, distribua ou **explore comercialmente**, sem permissão, pagamento ou atribuição; onde a renúncia não é possível, concede licença pública irrevogável de mesmo escopo | o **terceiro** pode explorar comercialmente; o texto **não** diz que o próprio usuário pode |
| Termos §5.2.2 | Paid Content: direitos são do usuário; pode usar, copiar, modificar, distribuir, **inclusive para fins comerciais**, e manter privado | plano pago = comercial, coerente com a página |
| Termos §12.9 | ordem de precedência: (a) order form/contrato empresarial; (b) DPA; (c) Supplemental Terms; (d) **estes Termos**; (e) Acceptable Use Policy | **a página de preços não está na lista** |

#### 6.1.2. O que dá para concluir, sem parecer jurídico

| Pergunta | Resposta documentada |
|---|---|
| O que o usuário pode fazer com os **seus próprios** Free Outputs? | **Não está resolvido.** A página diz "non-commercial"; o termo não concede nem proíbe explicitamente o uso comercial do próprio usuário — ele **renuncia** aos direitos. Um terceiro poder explorar comercialmente **não autoriza** o usuário a fazer o mesmo: são sujeitos e cláusulas diferentes |
| O que **terceiros** podem fazer? | Pelo §5.2.1, usar, copiar, modificar, distribuir e **explorar comercialmente**, sem atribuição, no mundo todo e permanentemente. Isso é o efeito literal da renúncia |
| A página de preços cria restrição **adicional** ao usuário? | É o que ela afirma ("Non-Commercial Use"), mas ela **não está** na ordem de precedência do §12.9 (que lista order form, DPA, Supplemental Terms, Termos e AUP). Se a descrição do plano vale como *order form* na contratação paga, é discussão contratual em aberto |
| Visibilidade, PI, direitos comerciais e exclusividade são a mesma coisa? | **Não, e é aí que a confusão nasce.** (1) *Visibilidade*: público por padrão; (2) *PI*: o usuário renuncia ao que tinha; (3) *direito comercial do usuário*: restringido pela página, ausente no termo; (4) *exclusividade*: não existe — qualquer pessoa pode usar o mesmo output, inclusive concorrentes |
| Qual texto prevalece quando são incompatíveis? | **Não é possível afirmar.** O termo é o contrato e tem cláusula de precedência que não menciona a página; a página é a descrição do plano que o usuário contrata. `REQUIRES_LEGAL_REVIEW` |

#### 6.1.3. Orientação conservadora (mantida e reforçada)

**Não usar Free Outputs do Tripo para personagem proprietário do Lia Forge.** O motivo não é
"falta de licença comercial" — é pior: o output nasce público, o usuário renuncia ao que tinha,
qualquer terceiro pode explorá-lo comercialmente, e existe uma afirmação oficial em contrário
sobre o uso do próprio usuário que não se consegue resolver lendo as fontes. Enquanto o conflito
não for esclarecido por escrito pelo fornecedor (ou por advogado), o plano gratuito serve para
teste descartável, não para asset de produto.

#### 6.1.4. Plano pago: consistente entre preço e termo?

| Verificação | Resultado |
|---|---|
| Página: "Private Models · Commercial Use" | sim, Pro/Max/Team |
| Termo §5.2.2: direitos do usuário, uso comercial, privacidade quando o serviço oferecer | **coerente** |
| Termo §5.2.2(a): Paid Content mantém status após expirar/cancelar/rebaixar | acrescenta garantia que a página não dá |
| Termo §5.2.2(b): Free Outputs **não** se tornam Paid Content ao assinar | restrição relevante: assinar depois não "limpa" o output gratuito |
| Termo §5.2.3: tornar Paid Content público dá à Tripo licença promocional não exclusiva, com atribuição, aviso prévio e incentivo, **sem** autorizar treino de modelo | mais restrito que a página sugere; `REQUIRES_LEGAL_REVIEW` só se o plano for publicar assets |

Conclusão do item: **plano pago é consistente**. O conflito é exclusivo do plano gratuito.

#### 6.1.5. Preços e créditos (página de preços, 2026-11-20)

| Plano | Preço | Créditos/mês | Saída estimada pela própria página | Modelos |
|---|---|---|---|---|
| Free | US$ 0 | 200 | ≈ 13 modelos | público, "non-commercial" |
| Pro | US$ 20/mês (US$ 240/ano) | 3.000 | ≈ 200 modelos (US$ 0,16/modelo) | privado, comercial |
| Max | US$ 90/mês (US$ 1.080/ano) | 25.000 | ≈ 1.660 modelos | privado, comercial |
| Team | US$ 55/assento/mês (US$ 110 mensal) | 90.000 | ≈ 6.000 modelos | privado, comercial |

Créditos por operação (FAQ da mesma página): HD Generate **15** · Smart Mesh **35** · Segmentation
**5** · Retopology **5** · Texture Gen **10** · Auto Rig **20**; add-ons: Ultra +15, Generate in
Parts +30, Texture Gen +10, HD Texture +10, Quad +5, Style Reference +5, PBR +5; Smart Mesh P2.0
+65, Part Completion +5/parte, Smart Lowpoly +30. O "≈ 13 modelos" do Free corresponde a
200 ÷ 15, ou seja **uma geração HD simples** — não inclui rig (20) nem Smart Mesh (35).

Observações funcionais do Free que não são de direito, mas limitam produção: exportações
limitadas a 15 (H2.5), 1 tarefa concorrente, fila padrão, histórico de edição de 1 dia, 3
retentativas e 10 modelos armazenados; geração de imagem restrita a Nano Banana (20 grátis/dia
e depois 80% de desconto).

### 6.2. Meshy — **Web App** e **API** são dois canais com tarifas diferentes

Fontes lidas em **2026-11-20 (UTC)**: `https://docs.meshy.ai/en/webapp/pricing`,
`https://docs.meshy.ai/en/api/pricing` e `https://www.meshy.ai/pricing`.

A versão anterior deste catálogo misturava as duas tabelas — dizia "rigging 5" e "100 créditos =
10 modelos" numa seção que também descrevia o app. **Corrigido: são canais distintos, com preços
distintos, e a API é pré-paga.**

#### 6.2.1. Canal Web App (`docs.meshy.ai/en/webapp/pricing`)

| Ação | Créditos | Nota |
|---|---|---|
| Image to 3D | **20** (Meshy 7.1 ou Meshy 6) · **25** (Ultra 2K/4K) · **10** (Meshy 6 Lite) | em planos pagos, exceto Enterprise, o Meshy 7.1 começa em Ultra 2K → padrão 25 |
| Smart Topology | **15** (Meshy T2.5/T2) | por geração |
| Texture ou Split na geração | **+10** cada | soma ao custo da geração |
| AI Texturing | **10** (2K) · **15** (8K) | 8K no modelo de textura Meshy 7 |
| Model Edit | **20** | por edição |
| Relief | **20** | por modelo |
| **Remesh** | **0** | por modelo |
| **Rigging** | **0** | por modelo |
| **Animate** | **0** | por clipe; clipes além do conjunto gratuito exigem plano pago; Text to Motion consome créditos |

Plano Free do Web App: **100 créditos/mês**, sem cartão. Créditos mensais renovam **00:00 UTC do
primeiro dia do mês**; créditos permanentes e comprados não expiram. Geração falha não consome
crédito; tarefa cancelada é estornada.

Licença (tabela de licenciamento da própria doc): Free = **CC BY 4.0**, uso comercial **com
atribuição**, e "you own the output"; Pro/Premium/Ultra/Studio/Enterprise = **privado**, uso
comercial pleno, output do usuário.

#### 6.2.2. Canal API (`docs.meshy.ai/en/api/pricing`)

API **pré-paga**: os créditos são comprados em `meshy.ai/settings/subscription` antes de enviar
requisições.

| API | Mesh apenas | +2K | +4K | +8K |
|---|---|---|---|---|
| Image to 3D / Text to 3D (Preview) — `meshy-7.1`, `meshy-6` | **20** | **30** | **30** | **35** |
| idem — `meshy-6-lite`, `meshy-t2`, `meshy-t2.5` | **5** | 15 | 15 (lite: não suportado) | 20 |
| Multi-Image to 3D — `meshy-7.1`, `meshy-6` | 20 | 30 | 30 | 35 |
| Ultra geometry (`2k`/`4k`) | **+5** | +5 | +5 | +5 |

| Operação | Créditos |
|---|---|
| Retexture / Text to 3D Refine | 10 (2K/4K) · 15 (8K) |
| **Auto-Rigging** | **5 por requisição** |
| **Animation** | **3 por ação** (até 10 ações por requisição) |
| Text to Motion | 10 (`prime`) · 3 (`swift`) |
| **Remesh** | **5** |
| **UV Unwrap** | **5** |
| Convert / Resize | 1 |
| Text/Image to Image | 3–12 conforme modelo (nano-banana 3 … GPT Image 12) |
| Analyze Printability | grátis |

#### 6.2.3. Por que a distinção importa

- **O mesmo nome custa diferente em cada canal**: rigging é **0** no Web App e **5** na API;
  remesh é **0** no Web App e **5** na API; Meshy 6 Lite é **10** no Web App e **5** na API.
  Qualquer frase do tipo "rigging custa 5" sem canal está errada.
- **Os 100 créditos gratuitos são do Web App.** A API é pré-paga; **não há documento lido que
  diga que o crédito gratuito do app pode ser gasto com tarifas de API**. Pool compartilhado:
  `UNVALIDATED` (não documentado nas páginas lidas).
- **Estimativas separadas por canal (100 créditos):**

| Canal / configuração | Modelos que 100 créditos compram |
|---|---|
| Web App, Meshy 7.1/6 sem textura (20) | **5** |
| Web App, com textura (+10 = 30) | **3** |
| Web App, Ultra 2K/4K (25) | **4** |
| Web App, Meshy 6 Lite (10) | **10** |
| API, `meshy-7.1` mesh apenas (20) | 5 — **só se esses créditos existirem na carteira de API** |
| API, com textura 2K (30) | 3 — idem |
| API, `meshy-6-lite` mesh apenas (5) | 20 — idem |

A linha anterior deste catálogo dizia "20 no modo lite (5)" sem canal; o número **5 é de API**, e
no Web App o lite custa **10**. Fica corrigido, com os dois números no lugar certo.

### 6.3. GPT Image (OpenAI) — geração e edição de imagem, sem 3D

Fontes: `developers.openai.com/api/docs/guides/image-generation` e
`developers.openai.com/api/docs/pricing` (2026-11-20, UTC).

| Item | Situação | Classificação |
|---|---|---|
| Modalidade | text-to-image **e** edição na Responses API; `action: generate / edit / auto`; edição multi-turno via `previous_response_id` | `OFFICIAL_DOCUMENTATION` |
| Modelos citados | `gpt-image-2.5-sunburst` (exemplos), `gpt-image-2.6-sunburst` / `-flare` (tabela de preços) | `OFFICIAL_DOCUMENTATION` |
| Preço | por token: imagem de entrada US$ 8/1M, saída US$ 30/1M (Standard); Batch pela metade | `OFFICIAL_DOCUMENTATION` |
| Character sheet / consistência | **não há garantia documentada** de consistência entre vistas; multi-turno preserva contexto, não identidade | `UNVALIDATED` |
| 3D | **não oferece** | `OFFICIAL_DOCUMENTATION` |
| Direitos e retenção | termos e política de dados da OpenAI — **não lidos** | `UNVALIDATED` |

### 6.4. Google Flow — **acesso gratuito existe**, e não é só assinatura

Fontes: `flow.google.com/about` (para onde `labs.google/fx/tools/flow` redireciona),
`support.google.com/flow` (índice, sem os artigos) — lidas em 2026-11-20 (UTC).

| Item | Situação | Classificação |
|---|---|---|
| Natureza | estúdio de criação (imagem + vídeo) com modelos Google | `OFFICIAL_DOCUMENTATION` |
| **Acesso gratuito** | **existe**: contas sem assinatura Google AI usam o Flow com **50 créditos por dia** | `COMMUNITY_REPORTED` — ver ressalva abaixo |
| Créditos diários | 50/dia; não acumulam; renovam no primeiro uso do dia (relato de terceiros) | `COMMUNITY_REPORTED` |
| Planos pagos | Google AI Plus / Pro / Ultra acrescentam créditos mensais (200 / 1.000 / 10.000 ou 25.000) **além** dos 50 diários; preços não lidos na fonte oficial nesta rodada | `COMMUNITY_REPORTED` para os números de crédito; `BLOCKED` para preços |
| Modelos | **Nano Banana** (imagem) · **Veo 3.1** e **Gemini Omni** (vídeo) | `OFFICIAL_DOCUMENTATION` |
| Imagem × vídeo | Nano Banana = imagem/edição; Veo 3.1 e Omni = vídeo; o custo em créditos é **por operação e por modelo**, não fixo por imagem | `OFFICIAL_DOCUMENTATION` (função) / `UNVALIDATED` (tabela de custos por operação) |
| Disponibilidade | "features may vary by Google AI subscription tier, platform (web vs. mobile), and region" | `OFFICIAL_DOCUMENTATION` |
| Idade e conta | **18+**; login em conta Google | `OFFICIAL_DOCUMENTATION` |
| API própria do Flow | **não documentada**. A API Gemini para modelos de imagem/vídeo é **outro** caminho | `UNVALIDATED` (não encontrada; não é prova de inexistência) |
| 3D | **não oferece** | `OFFICIAL_DOCUMENTATION` |

**Ressalva de rastreabilidade, e ela é importante:** a página oficial do produto **não exibe**
créditos, planos nem o número 50. Ela diz que o Flow integra as assinaturas Google AI, que os
recursos variam por nível/plataforma/região e que é 18+. O valor de **50 créditos/dia sem
assinatura** aparece em **páginas de ajuda do Google** citadas por várias fontes terciárias
convergentes (2026-08 a 2026-11), mas **não consegui abrir o artigo de ajuda diretamente** nesta
sessão (`support.google.com/flow/answer/...` falhou; o índice devolveu apenas tópicos).
Por isso o número está como `COMMUNITY_REPORTED`, com a fonte oficial citada por terceiros, e
**não** como `OFFICIAL_DOCUMENTATION`. O que muda em relação à rodada anterior: **o Flow não é
tratado como exclusivamente pago** — o acesso gratuito é registrado, com a ressalva de rastreio.
**Nenhuma equivalência entre crédito e quantidade de imagens/vídeos é afirmada aqui.**

### 6.5. Rodin / Hyper3D

Preço e termos **não verificados**. Continua `BLOCKED` como lacuna.

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
| 4 | Tripo/Meshy (plano **pago** mínimo) | image-to-3D utilizável sem GPU; no gratuito, Tripo é **`CONFLICTING`** (público + renúncia, com "non-commercial" na página de preços) e Meshy é CC BY 4.0 (atribuição) |
| 5 | TRELLIS.2 / Hunyuan3D-2.1 em GPU alugada | melhor qualidade aberta, só se o orçamento justificar |

Ordem inversa ao "mais bonito": começa pelo que já cabe no hardware e no orçamento.

**Correção de 2026-11-20 (reforçada na conciliação):** a recomendação anterior tratava
Tripo/Meshy como "US$ 20/mês" sem distinguir o que o plano gratuito concede. No Tripo o quadro é
**`CONFLICTING`**: output público, renúncia de direitos, licença pública que permite exploração
comercial por terceiros, e uma página de preços que diz "Non-Commercial Use" para o próprio
usuário, sem estar na ordem de precedência do termo (§6.1.2). Para personagem de jogo, o piso
realista é o **plano pago** — e, no caso do Tripo Free, nem isso resolve sem esclarecimento por
escrito. No Meshy, o gratuito (Web App) é CC BY 4.0, com atribuição obrigatória.

## 8. Não validado

`FLUX.2` (pesos), `CharacterGen` (pesos), `Hunyuan3D-Omni` (hardware), qualidade de
Tripo/Meshy, tempo de CPU no TripoSR, qualquer número de desempenho na RX 580, e a
afirmação de que quantização GGUF preserva qualidade suficiente para personagem.

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-SHEET-CONSISTENCY.md` · `CHARACTER-2D-TO-3D-PIPELINES.md`
