# Compatibilidade Windows 11 + AMD RX 580

| Campo | Valor |
|---|---|
| ID | `LR-HW-001` |
| Categoria | hardware |
| Projetos | Lia-Project, Lia Model Lab, Lia Forge |
| Fontes | `Lia-Project@005a324:docs/research/LIA-WINDOWS-AMD-MODEL-COMPATIBILITY.md` (14/11/2026), `Lia-Model-Lab@3ec4313:docs/08-HARDWARE-INFRASTRUCTURE.md`, ADR-0004/0005 |
| Data | 2026-11-17 |
| Status | CURRENT |
| Próxima revisão | 2027-05-17 |
| Confiança | **Alta** para o que é documentação oficial; **Baixa** para desempenho (nada medido) |

## 1. Hardware alvo

Windows 11 x64 · **AMD Radeon RX 580 8 GB (Polaris/GCN4, gfx803)** · Ryzen 5 5500 · 16 GB RAM.

## 2. Veredito por backend

| Backend | Situação | Evidência | Recomendação |
|---|---|---|---|
| CPU x86-64 quantizado | compatível | inferência de software geral | **baseline obrigatório** |
| llama.cpp **CPU** | sim | projeto documenta build | primeira escolha para LLM pequeno |
| llama.cpp **Vulkan** | build Windows documentado; RX 580 = relato de comunidade | doc oficial + relato | **P0 para benchmark** |
| llama.cpp HIP/ROCm | **não suportado** para gfx803 no Windows | matriz oficial AMD omite RX 580 | não depender |
| ONNX Runtime + DirectML | DirectML cobre GCN1+ por DX12, mas EP em *sustained engineering* | doc oficial | só ONNX validado, execução serial |
| Windows ML | suportado no Win11, seleciona EP | doc Microsoft | considerar para ONNX auxiliar |
| PyTorch CUDA | impossível (sem NVIDIA) | fato | não usar |
| PyTorch ROCm | matriz oficial não inclui RX 580 Windows | doc AMD | descartar |
| OpenVINO | otimizado para Intel | doc do projeto | ignorar para GPU AMD |
| MLX | Apple Silicon | doc Apple | não aplicável |
| vLLM / SGLang | stacks CUDA/HIP de servidor | doc dos projetos | fora do alvo |

## 3. Regra de ouro

> "Detectou o dispositivo" **não** é "executou rápido". Enumeração Vulkan prova
> enumeração; não prova kernels corretos, `fp16`, dot product inteiro, alocação de
> memória, estabilidade de shader cache nem ausência de reset de driver.

## 4. Armadilhas documentadas

1. `HSA_OVERRIDE_GFX_VERSION` e containers ROCm são **experimentais** — nunca no fluxo de instalação do usuário.
2. DirentML desabilita *memory pattern*, exige execução sequencial e não permite `Run()` concorrente na mesma sessão.
3. Referência gfx803 em MI6/MI8 (aceleradores) **não** valida RX 580 de consumidor.
4. Tamanho do arquivo quantizado ≠ pico de memória de trabalho (KV cache, vision/audio assets, buffers de shader, Stage).

## 5. Implicação para o ecossistema

Qualquer tecnologia pesquisada que exija CUDA, ROCm recente, Apple Silicon ou >8 GB
VRAM útil é incompatível **como caminho principal**. Isso afeta diretamente:
OpenJarvis (`nvidia-ml-py`), stacks de inferência rápida, e qualquer promessa de modelo
"grande" local.

## 6. O que falta (lacuna registrada)

| Lacuna | Status |
|---|---|
| Benchmark real de `llama.cpp Vulkan` na RX 580 | `BLOCKED` — exige execução |
| Pico de VRAM com Stage ativo | `BLOCKED` |
| WER/latência de STT PT-BR no Ryzen 5 5500 | `BLOCKED` |

Ver `RESEARCH-ROADMAP.md` item H-1.
