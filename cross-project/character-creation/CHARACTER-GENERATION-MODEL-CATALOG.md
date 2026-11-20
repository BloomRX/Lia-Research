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

### 6.1. Tripo — **quatro fontes oficiais**, e elas não concordam

Fontes lidas em **2026-11-20 (UTC)**:

1. `https://www.tripo3d.ai/pricing` — página comercial.
2. `https://www.tripo3d.ai/terms` — contrato; "Last updated: November 13, 2026".
3. `https://www.tripo3d.ai/help/privacy-policy/how-to-use-tripo-models-commercially` — guia
   informativo (cita "Terms of Service (last updated July 11, 2025)").
4. `https://www.tripo3d.ai/help/privacy-policy/how-to-understand-data-privacy-and-ai-training-at-tripo`
   — guia informativo (mesma citação de termos de 11/07/2025; Privacy Policy "effective
   February 5, 2025").

**Classificação: `CONFLICTING` + `REQUIRES_LEGAL_REVIEW`.** `CONFLICTING` continua sendo
qualificador pontual, não rótulo da taxonomia: aqui ele acompanha `OFFICIAL_LICENSE` porque
**todas** as fontes são do fornecedor.

#### 6.1.1. As quatro fontes, lado a lado

| # | Fonte | Data indicada | Natureza | O que afirma, literalmente | Escopo | Quem recebe o direito | Permite / restringe / não esclarece |
|---|---|---|---|---|---|---|---|
| 1 | Página de preços | não datada | **comercial** (descrição do plano) | Free: *"Public Models · Non-Commercial Use"*; Pro/Max/Team: *"Private Models · Commercial Use"*; Free: *"Exports 15 (H2.5 only)"* | planos e limites funcionais; não distingue Inputs de Outputs | o **usuário** | **restringe** o uso comercial do Free (afirmação da página); **não esclarece** o que terceiros podem fazer |
| 2 | Termos de Serviço | 13/11/2026 | **contratual** | §5.2: "rights you lawfully hold in User Assets belong to you"; §5.2.1: Free Outputs públicos por padrão; usuário **renuncia** aos direitos e permite que "anyone, worldwide and permanently" use, copie, modifique, distribua ou **explore comercialmente** sem atribuição; onde a renúncia não é possível, licença pública irrevogável de mesmo escopo; **Inputs enviados ficam fora** da renúncia e do regime público; §5.2.2: Paid Content do usuário, uso comercial, privado; §5.3: proibição de treinar com **Paid** Inputs/Outputs + uso de informação **anonimizada** para melhorar serviço, funcionalidades e modelos (revisão do §3.1 é separada); §12.9: precedência (order form, DPA, Supplemental Terms, Termos, AUP) | Free Outputs *vs.* Inputs *vs.* Paid Content, separados | **terceiros/público** (licença) e o **usuário** (o que lhe resta) | **permite** exploração comercial por terceiros; **não concede** nem proíbe expressamente o uso comercial pelo próprio usuário; **não converte** Free Output em propriedade da Tripo |
| 3 | Guia "How to Use Tripo Models Commercially" | não datada; cita termos de 11/07/2025 | **orientação informativa** (não contratual) | "Yes, if you are on a paid plan"; **"Free Users: Under the Terms of Service (Section 5.2.1), Tripo retains all rights to Inputs and Outputs generated by Free Users, including all Intellectual Property rights"**; tabela: Free = "Commercial use: Not granted", "IP ownership: Tripo retains all rights"; pago = "You hold all rights"; "AI training: Free = no explicit restriction — Tripo may use Free User content" | **Inputs e Outputs**, Free e pago | **a Tripo** (segundo a página) | **restringe** o comercial do Free e **atribui à Tripo** a titularidade — o que **o termo não diz** |
| 4 | Guia "Data Privacy and AI Training" | não datada; cita termos de 11/07/2025 | **orientação informativa** | pago: "Tripo will **NOT** use your Inputs and Outputs as training data… (Terms of Service, Section 5.2.2)" — a cláusula existe, mas no **§5.3** (§6.1.5); Free: "The Terms of Service do not include an equivalent restriction. Under Section 5.2.1, Tripo retains all rights to Free User Inputs and Outputs… — which may include use for model training"; assets públicos podem ser retidos (cita "Terms 10.5") | Inputs e Outputs; treinamento; retenção | **a Tripo** | a proibição do pago **existe** no contrato, no §5.3 (a página cita §5.2.2); não há cláusula equivalente para Free — a página **acerta** a permissão para Free e **erra a seção** no pago |

#### 6.1.2. As divergências, nomeadas

| # | Divergência | Onde aparece | O que o contrato diz de fato |
|---|---|---|---|
| D1 | **Titularidade** — guias dizem que a Tripo "retains all rights to Inputs and Outputs" de usuários Free | fontes 3 e 4 | §5.2 diz o contrário para o que o usuário **legalmente detém** ("belong to you"), e §5.2.1 não retém titularidade: **renuncia** em favor do público. Reter e renunciar são coisas diferentes |
| D2 | **Inputs** — guias incluem Inputs na retenção de direitos | fontes 3 e 4 | §5.2.1 **exclui expressamente** os Inputs enviados da renúncia, da licença pública e do regime de publicidade padrão |
| D3 | **Treinamento** — o guia atribui a proteção do plano pago ao **§5.2.2** | fonte 4 | **a proibição existe, mas está no §5.3**, não no §5.2.2: "Company will not use Paid Users' Inputs or Paid Outputs as training data to train, fine-tune or otherwise develop any artificial intelligence model". É erro de **referência de seção** na ajuda, não ausência de cláusula (corrigido na rodada 7.5) |
| D4 | **Uso comercial do usuário Free** — página diz "non-commercial", guia diz "not granted", termo é silente quanto ao usuário e permissivo quanto a terceiros | fontes 1, 3 e 2 | não há cláusula no termo que conceda **nem** que vede o uso comercial pelo próprio usuário Free |
| D5 | **Versão dos termos citada** — os dois guias citam termos de **11/07/2025**, e o contrato vigente é de **13/11/2026** | fontes 3 e 4 | os guias descrevem uma versão **substituída** do contrato; isso não os invalida como posição oficial, mas explica parte da divergência |

#### 6.1.3. Conclusão — o que permanece indeterminado

| Pergunta | Resposta |
|---|---|
| Direito comercial do **usuário** no Free | **não resolvido**. Duas fontes oficiais dizem "não", uma é silente e uma (a contratual) concede licença a terceiros |
| Direito de **terceiros** | pelo §5.2.1, amplo: uso, cópia, distribuição e exploração comercial, sem atribuição |
| A Tripo **retém** os direitos? | o contrato **não** diz isso; os guias dizem. Divergência registrada, não resolvida |
| **Privacidade** dos Inputs | §5.2.1 mantém Inputs fora do regime público; os guias não fazem essa distinção |
| **Treinamento** | contrato proíbe treinamento com **Paid** Inputs/Outputs no **§5.3** e permite uso de informação **anonimizada**; para Free não há proibição equivalente. A ajuda dá a seção errada (§5.2.2) — ver §6.1.5 |
| **Exclusividade** | não existe em nenhuma das fontes: o mesmo output pode ser usado por qualquer pessoa |
| Qual fonte prevalece? | **a página de ajuda não é contrato** e não está na ordem de precedência (§12.9); entre página comercial e termo, o termo é o contrato — mas o termo é silente no ponto que interessa ao usuário |

**Não declaro resolvido o direito comercial do usuário gratuito.** As páginas de ajuda são
orientação oficial do fornecedor, não contrato — e são **contraditórias entre si e com o
próprio contrato** que citam, além de citarem uma versão anterior dos termos. Isso não é motivo
para descartá-las: é motivo para registrar que a posição oficial da Tripo é **ambígua**, e que
qualquer decisão de produto depende de esclarecimento formal por escrito.

#### 6.1.4. Orientação conservadora (mantida)

**Não usar Free Outputs do Tripo para personagem proprietário do Lia Forge.** O quadro piorou em
relação à rodada anterior: além do conflito preço × termo, há duas páginas oficiais afirmando
retenção de direitos e possível uso para treinamento de conteúdo gratuito. Enquanto não houver
esclarecimento formal, o plano gratuito serve para teste descartável — nunca para asset de
produto, e nunca para enviar arte própria de personagem.

#### 6.1.5. Plano pago: proibição de treinamento existe — no §5.3, não no §5.2.2

**Correção da rodada anterior.** A 7.4 registrou a proibição de treinamento no plano pago como
"afirmação de página de ajuda, não encontrada no contrato". Isso estava errado: a cláusula
existe, no **§5.3** (Service Improvement and Model Training). Texto lido em 2026-11-20 (UTC):

> "We do not use personal information to train our models. We may use information that has been
> aggregated or anonymized so that it no longer identifies you, including text prompts and
> Outputs, to improve the performance of the Service, develop features, and develop and improve
> our models, and we do not attempt to re-identify such information. We are not required to
> remove from models already trained any information used in accordance with this Section before
> you delete it. For the avoidance of doubt, **Company will not use Paid Users' Inputs or Paid
> Outputs as training data to train, fine-tune or otherwise develop any artificial intelligence
> model**. Review of Inputs and Outputs under Section 3.1 to operate, secure and troubleshoot the
> Service, and to evaluate the quality, safety and performance of the Service and its models, is
> separate from model training and is not restricted by this Section 5.3."

O que isso permite afirmar, e o que **não** permite:

| Afirmação | Situação |
|---|---|
| A página de ajuda atribui a proteção ao §5.2.2; a cláusula explícita está no **§5.3** | **fato registrado** — erro de referência da ajuda |
| Paid Inputs e Paid Outputs **não** são usados como dados de treinamento, ajuste fino ou desenvolvimento de modelo de IA | `OFFICIAL_LICENSE` (contratual, §5.3) — antes `UNVALIDATED`, agora com referência correta |
| A Tripo pode usar informação **agregada ou anonimizada** (inclusive prompts e Outputs) para melhorar serviço, funcionalidades e modelos, sem tentar reidentificar | `OFFICIAL_LICENSE` (§5.3) — **não** é treinamento com dado identificável, e não se confunde com a proibição acima |
| Revisão de Inputs e Outputs (§3.1) para operar, proteger, solucionar problemas e **avaliar qualidade, segurança e desempenho** é **separada** de treinamento e **não** é restringida pelo §5.3 | `OFFICIAL_LICENSE` (§3.1 + §5.3). **Não** se pode dizer que a Tripo nunca processa, revisa ou avalia conteúdo pago |
| Dado anonimizado já usado em modelo treinado **não** precisa ser removido do modelo após exclusão | `OFFICIAL_LICENSE` (§5.3, §10.5) |

**Distinção que fica registrada:** "não usar como dado de treinamento" ≠ "não processar, não
revisar, não avaliar" ≠ "não usar informação anonimizada". São três regimes diferentes, e a
cláusula só protege contra o primeiro. `REQUIRES_LEGAL_REVIEW` apenas se o projeto depender de
garantia de **ausência total de processamento** — que o contrato não dá.

**Restante do plano pago, sem alteração de recomendação:** página ("Private Models · Commercial
Use"), §5.2.2 (direitos do usuário, uso comercial, privacidade), §5.2.2(a) (status sobrevive ao
cancelamento) e §5.2.2(b) (Free Output **não** se converte em Paid Content ao assinar) seguem
como na 7.3. O plano pago é o **regime contratual mais favorável** descrito nas fontes lidas —
sem promessa de exclusividade absoluta nem de ausência de todo processamento.

#### 6.1.6. Divergência de visibilidade (interface × contrato)

| Fonte | Afirmação literal | O que é |
|---|---|---|
| Página de ajuda de privacidade | "Assets are only visible to you unless you explicitly set them to "public."" | descrição da **interface** e do comportamento esperado |
| Termos §4 | "Outputs generated under a free plan are **public by default** and may be viewed by other Users and the public, as described in Sections 5.2.1 and 5.2.3; paid plans may allow you to keep Outputs private" | **regime contratual** de publicidade |
| Termos §5.2.1 | "Free Outputs are public by default"; renúncia + licença pública | regime contratual e de licença |

**Divergência registrada:** a ajuda descreve visibilidade como opt-in ("só você vê até marcar
público"), enquanto o contrato define Free Outputs como **públicos por padrão**. Não presumo que
a interface resolva o conflito contratual — nem que a interface tenha o mesmo comportamento para
Free e pago.

Separação obrigatória, registrada para não repetir a confusão:

| Categoria | Regra documentada |
|---|---|
| **Inputs originais enviados** | fora da renúncia e do regime de publicidade padrão do §5.2.1; a visibilidade depende do que o usuário publicar (§3.1 cobre publicação voluntária) |
| **Free Outputs** | públicos **por padrão** (§5.2.1, §4), com renúncia e licença pública |
| **Paid Outputs** | privados quando o serviço oferecer a opção; §5.2.3 regula o que acontece se o usuário **escolher** publicar |
| **Visibilidade na interface** | controle de produto; pode divergir do regime contratual — não é fonte de direito |
| **Regime contratual de publicidade e licença** | definido nos Termos, independentemente do que a tela mostra |

#### 6.1.7. Divergência de exclusão e retenção (§10.5)

| Fonte | Afirmação | Problema |
|---|---|---|
| Ajuda de privacidade | "any Inputs and Outputs you previously made available in "public" areas … may be retained **in perpetuity** (Terms 10.5)" | cita uma **versão de 2025** dos termos e converte **persistência da licença** em **retenção perpétua do arquivo** |
| Termos atuais §10.5 | ao excluir conta, conversa ou asset, "we delete the corresponding Inputs and Outputs … **subject to legally permitted or required retention**"; cópias de conteúdo público "previously lawfully downloaded by others **cannot be recalled**"; "Free Output waivers and public licenses **remain effective**"; anonimizado retido continua sujeito ao §5.3 e "anonymization or termination does not permit training on Paid Content" | redação diferente e mais específica |

Quatro coisas que precisam ficar separadas — e que a página de ajuda funde:

| # | Objeto | Regra atual |
|---|---|---|
| 1 | **Retenção do arquivo nos servidores** | exclusão mediante solicitação, **sujeita a retenção legal ou operacional permitida**; não há promessa de retenção perpétua no §10.5 |
| 2 | **Cópias já baixadas por terceiros** | não podem ser recuperadas — fato técnico, não licença |
| 3 | **Persistência da licença/renúncia pública de Free Outputs** | permanece eficaz após exclusão (§10.5) — é **licença**, não guarda do arquivo |
| 4 | **Retenção legal ou operacional permitida** | ressalva expressa do §10.5 |

**Não converto persistência da licença em afirmação de retenção perpétua do arquivo.** O efeito
prático é parecido — o Free Output pode continuar circulando —, mas o fundamento é outro, e a
ajuda descreve o fundamento errado.

#### 6.1.8. Contradição interna da própria ajuda: arte própria é "safe" e ao mesmo tempo "Tripo retains all rights"

A página "How to Use Tripo Models Commercially" diz, na mesma página:

1. "Free Users: … **Tripo retains all rights to Inputs and Outputs** generated by Free Users,
   including all Intellectual Property rights."
2. Tabela de risco de input: "**Your own artwork / photos — Safe — Full commercial use**".

Avaliação, sem inventar interpretação jurídica:

| Leitura | Situação |
|---|---|
| Os trechos tratam de **assuntos distintos**: (a) risco de **terceiro** ter direitos sobre a imagem de entrada; (b) titularidade contratual e processamento do Input pelo serviço; (c) direito sobre o **Output** gerado | **plausível e parcialmente sustentada** pelo próprio texto: a tabela responde "meu input me expõe a reclamação de terceiro?", não "quem detém direitos sobre o arquivo depois do upload" |
| Os trechos continuam **incompatíveis** | **também plausível**: a coluna "Full commercial use" não distingue Free de pago e, lida ao pé da letra, contradiz a linha 1 |
| Uma leitura elimina a divergência | **não**. Registro as duas e não escolho uma para "resolver" o problema |

**Consequência prática (não jurídica):** a orientação conservadora continua sendo a única
defensável — não enviar arte proprietária de personagem enquanto a divergência documental não
tiver esclarecimento formal, e não usar Free Outputs em asset de produto.

#### 6.1.9. Preços e créditos (página de preços, 2026-11-20)

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
200 ÷ 15 — **uma geração HD simples**, sem rig (20) nem Smart Mesh (35).

Limites funcionais do Free (não são direito, mas restringem produção): exportações 15 (H2.5),
1 tarefa concorrente, fila padrão, histórico de edição de 1 dia, 3 retentativas, 10 modelos
armazenados; geração de imagem restrita a Nano Banana (20 grátis/dia e depois 80% de desconto).

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

**Limite de download do Free** (`help.meshy.ai/en/articles/15696428-what-is-included-on-the-free-plan`,
lido em 2026-11-20 UTC) — é um limite **separado dos créditos**:

| Item | Regra no plano Free |
|---|---|
| Downloads por mês | **10 downloads/mês**, apenas de modelos **sem textura gerados com Meshy 6 Lite**; reset em 00:00 UTC do dia 1º |
| O que **não** pode ser baixado | modelos de **Meshy 6**, **Meshy 7** ou **T2.5**; modelos **texturizados** (inclusive um 6 Lite depois de texturizar); texturas aplicadas a modelo enviado; modelos do **3D Agent** |
| Créditos comprados | "Credits … are used for generating and don't unlock downloads" — comprar crédito **não** libera download |
| Modelos de assinatura anterior | modelos gerados em Pro ou superior continuam baixáveis **ilimitadamente** após voltar ao Free |
| Campanhas | podem conceder downloads permanentes como prêmio |
| API | **não disponível no Free** (só Pro, Premium, Ultra, Studio, Enterprise) |

Consequência que precisa ficar explícita: **os 100 créditos não são 100 créditos conversíveis em
assets exportáveis.** No Free, gerar é barato (20 créditos por modelo 7.1/6) e **exportar** é o
recurso escasso (10/mês, e só 6 Lite sem textura). Um plano de produção baseado em "5 modelos por
100 créditos" está errado para o Free: o teto real de arquivos utilizáveis é o **download**, não o
crédito.

Licença (tabela de licenciamento da própria doc): Free = **CC BY 4.0**, uso comercial **com
atribuição**, e "you own the output"; Pro/Premium/Ultra/Studio/Enterprise = **privado**, uso
comercial pleno, output do usuário.

#### 6.2.2. Canal API (`docs.meshy.ai/en/api/pricing`)

API **pré-paga**: os créditos são comprados em `meshy.ai/settings/subscription` antes de enviar
requisições. E, segundo o Help Center oficial
(`help.meshy.ai/en/articles/16815622-how-many-credits-does-each-meshy-api-task-cost`):
**o plano Free não tem acesso à API, mesmo comprando créditos adicionais**; os custos são
consistentes entre os planos pagos; plugins e integrações (ex.: ComfyUI) consomem o mesmo saldo
de API, com as mesmas tarifas; tarefas que falham são estornadas.

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
- **Os 100 créditos gratuitos são do Web App, e o Free não tem API.** Não é uma questão de saldo
  insuficiente: o acesso à API **não existe** no plano gratuito, nem comprando créditos. Logo, a
  ideia de "gastar os 100 créditos gratuitos em chamadas de API" é dupla e independentemente
  errada.
- **Pool compartilhado entre Web App e API nos planos pagos:** continua `UNVALIDATED`. O Help
  Center diz que plugins "draw from the same credit balance at the same rates" — o que fala do
  saldo de **API**, não de fusão com o crédito mensal do app. Nenhum documento lido afirma pool
  único nem separação definitiva; `P-15` **não** pode ser fechado.
- **Quatro coisas diferentes, que a documentação separa e o uso coloquial funde:**

| Dimensão | Web App Free | Web App pago | API |
|---|---|---|---|
| **Geração** | sim (100 créditos/mês) | sim | **não no Free** |
| **Crédito** | 100/mês, não acumula | mensal conforme plano | carteira pré-paga |
| **Download** | **10/mês**, só 6 Lite sem textura | ilimitado | conforme plano |
| **Licença** | **CC BY 4.0** (atribuição) | privada, comercial | conforme plano |

  "Gerei" ≠ "baixei" ≠ "posso usar comercialmente". No Free, cada uma dessas etapas tem uma
  condição própria.

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

### 6.4. Google Flow — **fonte oficial acessível**: gratuito, com regras claras

Fontes oficiais lidas em **2026-11-20 (UTC)**:
`support.google.com/flow/answer/16526234?hl=pt-BR` ("Gerenciar seus créditos do Google Flow"),
`support.google.com/flow/answer/16353333?hl=en-GB` ("Get started with Google Flow") e
`flow.google.com/about`.

| Item | O que a documentação oficial diz | Classificação |
|---|---|---|
| **Acesso gratuito** | "Com ou sem assinatura, você recebe **50 créditos do Google Flow por dia**"; sem assinatura, são **só** esses 50/dia | `OFFICIAL_DOCUMENTATION` |
| Créditos por plano | Plus **+200/mês** · Pro **+1.000/mês** · Ultra US$ 100 **+10.000/mês** · Ultra US$ 200 **+25.000/mês**, sempre **além** dos 50 diários | `OFFICIAL_DOCUMENTATION` |
| Atualização diária | acionada pela **primeira geração do dia**; exemplo oficial: primeiro uso em 12/08 → próximos 50 em 13/08 | `OFFICIAL_DOCUMENTATION` |
| Não acumulação | créditos diários não usados **não passam** para o dia seguinte; créditos mensais não usados **não passam** para o mês seguinte | `OFFICIAL_DOCUMENTATION` |
| Renovação mensal | no **início do ciclo de faturamento** | `OFFICIAL_DOCUMENTATION` |
| **Limite de vídeo para não assinantes** | "Durante os horários de pico, aproximadamente das **14h às 17h UTC**, talvez não seja possível gerar vídeos sem uma assinatura"; **imagens e o agente continuam disponíveis** | `OFFICIAL_DOCUMENTATION` |
| Idade e conta | **18+ com idade verificada**, conta Google, e estar em **região suportada** (VPN não contorna) | `OFFICIAL_DOCUMENTATION` |
| Workspace | planos Workspace qualificados recebem Flow sem custo extra, com 50 créditos diários | `OFFICIAL_DOCUMENTATION` |
| Modelos | **Nano Banana** (imagem) · **Veo 3.1 Lite** · **Omni Flash 1.2** (vídeo). Em 05/12/2026 saem Veo 3.1 Fast, Veo 3.1 Quality e Omni Flash 1.1; Veo Extend saiu em 05/11/2026 | `OFFICIAL_DOCUMENTATION` |
| Custo por operação | **por segundo de vídeo**, não fixo: Omni Flash 1.2 = 1 crédito/s em 360p e 3 créditos/s em 720p; até 10 s para todos, 11–15 s só assinantes; Veo 3.1 Lite (4/6/8 s, 720p) = **10 créditos** (5 no Ultra); upscale para 4K = **50 créditos** (só Ultra) | `OFFICIAL_DOCUMENTATION` |
| Imagem | gerada por Nano Banana; a doc **não** publica custo fixo por imagem — depende do modelo/operação | `OFFICIAL_DOCUMENTATION` (função) / `UNVALIDATED` (custo unitário de imagem) |
| Marca d'água | **SynthID invisível** em tudo; marca visível opcional, automática na Índia, Coreia do Sul e Vietnã fora do Ultra 20x | `OFFICIAL_DOCUMENTATION` |
| Falha de geração | créditos devolvidos **em até 1 hora** | `OFFICIAL_DOCUMENTATION` |
| API própria do Flow | **não documentada**. A API Gemini é outro caminho | `UNVALIDATED` (não encontrada) |
| 3D | **não oferece** | `OFFICIAL_DOCUMENTATION` |

**Reconferido em 2026-11-20 (UTC)** nesta rodada: `support.google.com/flow/answer/16526234?hl=pt-BR`
(seções "Limites de geração para não assinantes", "Número de créditos", "Como os créditos são
atualizados" e a tabela de custos por modelo) e `support.google.com/flow/answer/16353333?hl=en-GB`
(quem pode usar, idade/região, navegador, devolução de créditos). A página do produto
(`flow.google.com/about`) continua sem números de crédito — o que sustenta a leitura de que a
fonte dos números é o **Help Center**, não a landing page.

Custos por operação lidos na mesma tabela (por geração, em créditos):

| Modelo | Custo | Observação |
|---|---|---|
| Veo 3.1 Lite (4/6/8 s) | **10** (5 no Ultra) | disponível a todos |
| Veo 3.1 Fast (4/6/8 s) | 20 (10 no Ultra) | **desativado em 2026-12-05** |
| Veo 3.1 Quality (8 s) | 100 | **desativado em 2026-12-05** |
| Omni Flash 1.1 (720p) | 7 / 10 / 12 / 15 por 4/6/8/10 s | **desativado em 2026-12-05** |
| Omni Flash 1.1 (360p) | 4 / 5 / 6 / 7 por 4/6/8/10 s | idem |
| Omni Flash 1.1 (edição de vídeo) | 40 | idem |
| Upscale 1080p | 0 para Plus/Pro/Ultra; **indisponível** sem assinatura | — |
| Upscale 4K | 50, só Ultra | — |

Continua valendo: **não existe custo fixo de imagem publicado** nem equivalência crédito→imagem;
a API do produto não é documentada; e o Flow não faz 3D.

**Correção desta rodada:** a rodada 7.3 registrou os 50 créditos/dia como `COMMUNITY_REPORTED`
porque não conseguiu abrir o artigo de ajuda. O artigo **está acessível** e confirma o valor e as
regras; portanto a classificação sobe para **`OFFICIAL_DOCUMENTATION`** e a ressalva antiga é
removida. O que **continua** valendo: não existe equivalência fixa "crédito = N imagens" — o
custo é por operação, por modelo e, no vídeo, por segundo.

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
