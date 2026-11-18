# Índice — Lia Studio

---

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem |
|---|---|---|---|
| `LR-STUDIO-001` | IDE Rust/Tauri como referência | `repositories/openidea/REPORT.md` | pesquisa externa (novo) |
| `LR-STUDIO-002` | 49 agentes / 75 skills de gamedev, escada de design | `repositories/claude-code-game-studios/REPORT.md` | pesquisa externa (novo) |
| `LR-STUDIO-003` | ReScript (avaliação de stack) | `repositories/rescript-lang/REPORT.md` | pesquisa externa (novo) |
| `LR-LIC-005` | Licenças prontas: aviso MIT dentro do payload de Skill, marca de terceiros | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 18 relatórios |
| `LR-STUDIO-004` | 17 apps criativos em Rust: barramento único de comandos e superfície de agente | `repositories/artcraft/REPORT.md` | pesquisa externa (novo) |
| `LR-STUDIO-005` | Framework C#/Vulkan (BRUTAL): “framework, não engine”, `LICENSES/` por pacote, política de IA em PR | `repositories/brutal/REPORT.md` | pesquisa externa (novo) |
| `LR-AGENT-010` | Skills de edição de foto/PDF sem gerador de imagem | `cross-project/agents/ARTCRAFT-SKILL-PACK.md` | derivado de `LR-STUDIO-004` |
| `LR-FORGE-004` | VFX 2D / animação pixel art | `repositories/pixelfx/REPORT.md` | pesquisa externa (novo) |
| `LR-UI-003` | Molde de skill de design | `repositories/ai-design-skills/REPORT.md` | pesquisa externa (novo) |
| `LR-LIC-001` | Licença e proveniência de Skills | `projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md` | `SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` + `docs/licenses/` |
| `LR-SEC-002` | Segurança de runtime de agente | `cross-project/agents/AGENT-RUNTIME-SECURITY.md` | `ARENA-RUNTIME-SECURITY-AUDIT.md` |

## 2. Pesquisa existente mantida na origem

| Documento | Bytes | Branch | Motivo |
|---|---:|---|---|
| `docs/research/STUDIO-FORGE-INTEGRATION-AUDIT.md` | 179 KB | sessão | fronteira de dois projetos; pertence a eles |
| `docs/research/ARENA-ENGINE-INTEGRATION-AUDIT.md` | 79 KB | sessão | auditoria de código |
| `docs/research/ARENA-SKILLS-MCP-AGENT-TOOLS-RESEARCH.md` | 68 KB | sessão | pesquisa ampla; resumida em `LR-AGENT-006` |
| `docs/research/ARENA-UIUX-AUDIT.md` | 50 KB | sessão | UX do produto |
| `docs/research/AGENT-ARCHITECTURE-RESEARCH.md` | 42 KB | sessão | 21× `ADAPTAR`, 1× `ADOTAR` — resumido |
| `docs/research/ARENA-RUNTIME-SECURITY-AUDIT.md` | 42 KB | sessão | resumido em `LR-SEC-002` |
| `docs/research/ARENA-GAMEPLAY-QA-AUDIT.md` | 35 KB | sessão | gameplay |
| `docs/research/BRANCH-ARQUITETURA-ANTIGA-2026-10-18.md` | 32 KB | sessão | **histórico** — preservar como `HISTORICAL` |
| `docs/PLANO-TECNICO-AJUSTES-E-EVOLUCAO-LIA-STUDIO.md` | 55 KB | sessão | plano |
| `docs/architecture/LIA-STUDIO-ARCHITECTURE-DECISIONS.md` | 22 KB | sessão | decisão do projeto (C1–C10, 2 `PENDENTE`) |
| `planejamento/visao-produto-fluxo-e-plano-de-entregas.md` | 28 KB | sessão | plano de produto |
| `docs/plans/LIA-STUDIO-IMPLEMENTATION-ROADMAP.md` | 22 KB | sessão | roadmap |

## 3. Skills do projeto (16) — ver `LIA-SKILLS-INVENTORY.md`

Todas sem licença no payload. 12 com seção `## Origem` (bom), mas aviso MIT fora do pacote.

## 4. Licenças preservadas no Studio

| Arquivo | Licença |
|---|---|
| `docs/licenses/CLAUDE-CODE-GAME-STUDIOS-MIT.txt` | MIT |
| `docs/licenses/MR-MAK-WORKSPACE-MIT.txt` | MIT |

## 5. Lacunas

| Lacuna | Situação |
|---|---|
| ZIP de 9,9 MB de terceiros versionado | decisão de proveniência pendente (`DR-0004`) |
| `img2threejs` (Apache-2.0) não lido na origem | `UNVERIFIED` |
| Triagem OpenDots/OpenBot nunca concluída | `PENDENTE` desde 2026-10-17 |
| 16 skills sem licença | bloqueia distribuição |
| Fronteira Studio↔Forge com dois documentos concorrentes | `CONFLICTING` |
