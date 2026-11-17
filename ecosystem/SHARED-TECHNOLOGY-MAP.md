# Mapa de tecnologia compartilhada

Stack real observada nos cinco projetos, para avaliar compatibilidade sem inventar.

---

## 1. Stack base observada

| Camada | Tecnologia | Evidência |
|---|---|---|
| Runtime desktop | Electron (Lia-Project), Tauri/Rust em projetos pesquisados (OpenIDEA) | Lia-Project `docs/architecture/decisions/ADR-0001-desktop-runtime-d-plus.md`, `PLAN-shared-electron-binary-experiment.md` |
| Frontend | TypeScript + Vue (Stage), UnoCSS | Lia-Project `airi`/`lia` trees + skill `lia-unocss-ui`, `lia-vue-development` |
| Testes | suites de Stage/renderer, `Tests/` com README próprio | Lia-Project `Tests/README.md` |
| Build | pnpm workspaces, batch/PowerShell no Windows (`Lia.bat`) | skill `lia-pnpm-workspaces`, relatórios PROMPT-38/39/40 |
| Linguagens auxiliares | Python (scripts, Model-Lab, automação), GDScript/Godot (Studio), Rust (ferramentas), Nix | metadados de linguagem do GitHub por repositório |

## 2. Hardware de referência do usuário

| Item | Valor | Fonte |
|---|---|---|
| SO | Windows 11 x64 | `docs/research/LIA-WINDOWS-AMD-MODEL-COMPATIBILITY.md` |
| CPU | Ryzen 5 5500 | idem |
| GPU | AMD Radeon RX 580 8 GB (Polaris/GCN4, **gfx803**) | idem |
| RAM | 16 GB | idem |
| Backend viável | **Vulkan** (ROCm não suporta gfx803 no Windows; CUDA inexistente) | `REPORTED` de doc oficial + `CONFIRMED` da ausência de suporte ROCm |

Consequência: qualquer tecnologia que exija CUDA, ROCm recente, Apple Silicon ou
mais de 8 GB de VRAM é incompatível com o hardware alvo **como caminho principal**.

## 3. Restrições de plataforma que atravessam projetos

| Restrição | Afeta | Implicação de pesquisa |
|---|---|---|
| Windows-first | todos | macOS-only (ex.: Meldwork) não serve como caminho principal |
| GPU AMD antiga | Project, Model-Lab, Forge (render), Studio | preferir CPU/Vulkan; evitar stacks CUDA-only |
| 16 GB RAM | todos | modelo + app + navegador competem |
| Desktop sempre ativo | Project | consumo em idle importa (pesquisa de recurso de runtime 2026-11-14) |
| Offline parcial | Project, Hub | integração precisa degradar sem internet |

## 4. Tecnologias já decididas (decisões de origem, não desta base)

| Decisão | Projeto | Artefato |
|---|---|---|
| Consolidação offline como fundação | Model-Lab | `docs/adr/0001-CONSOLIDATION.md` |
| Inferência local verificável antes de SFT | Model-Lab | `docs/adr/0002-LOCAL-INFERENCE.md` |
| Hardening de inferência | Model-Lab | `docs/adr/0003-INFERENCE-HARDENING.md` |
| Memória Windows por política | Model-Lab | `docs/adr/0004-WINDOWS-MEMORY.md` |
| Launcher Windows controlado | Model-Lab | `docs/adr/0005-WINDOWS-CONTROLLED-LAUNCHER.md` |
| Qwen3.5 CPU pilot fixado | Model-Lab | `docs/adr/0006-QWEN35-PINNED-CPU-PILOT.md` |
| Desacoplamento do AIRI | Lia-Project | `docs/architecture/AIRI-DECOUPLING-PLAN-2026-10-28.md` |
| Arquitetura aprovada + gates do Forge | Lia Forge | `docs/ADR-001-LIA-FORGE-DECISIONS.md` |
| Remediação P0 autorizada | Lia Forge | `docs/ADR-002-P0-REMEDIATION-AUTHORIZATION.md` |

Estas decisões pertencem aos projetos de origem. O Lia-Research apenas as registra
como contexto; não as reinterpreta nem as revoga.

## 5. Tecnologias investigadas nesta fundação e seu encaixe

| Tecnologia | Cabe no ecossistema? | Onde | Observação |
|---|---|---|---|
| OpenJarvis | padrão sim, código não | Model-Lab, Hub | referência arquitetural; Apache-2.0 permite, mas escopo é pesquisa local-first |
| Vercel UI SDK | sim (Vue confirmado) | Project (Stage), Forge, Hub | beta; exige protótipo isolado |
| Mister Download Manager | condicionado a GPL | Forge (download de assets) | crate `mdm-mcp` é GPL-3.0: usar como processo separado, não como biblioteca |
| Claude Trading Skills | padrão sim, domínio não | Hub | organização de Skills/workflows |
| HA-MCP | sim, opcional | Project, Hub | MIT; requer HA como dependência opcional |
| OpenIDEA | padrão sim | Studio | Tauri/Rust, Apache-2.0 |
| RouterHub | com restrição severa | Project (provider opcional) | modelos uncensored/abliterated: risco de política e de licença |
| ReScript | não | — | fora da stack TS/Vue; custo de adoção alto |
| SculptForge | referência | Forge | GPL-3.0, app standalone |
| Claude Code Game Studios | padrão sim | Studio, Hub | MIT; 674 arquivos markdown de processo |
| ManimGX | referência limitada | Forge, Studio | animação matemática; MIT |
| Meldwork | referência | Hub | macOS-only no README; Apache-2.0 |
| Plannotator | padrão sim | Project, Hub | anotação de planos; Apache-2.0 |
| pixelfx | sim (assets) | Forge | MIT; 244 efeitos |
| unslop | **não** | — | sem licença: `BLOCKED` |
| AI Design Skills | sim (padrão) | Studio, Project | MIT; pequeno e direto |

Detalhe e evidência de cada linha em `repositories/<slug>/REPORT.md`.
