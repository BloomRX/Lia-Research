# Índice — Lia Studio

---


> **Reauditoria de 2026-11-20.** Todo relatório externo listado aqui foi reavaliado
> nesta data (versão anterior, versão atual, mudanças, testes e conclusão). O detalhe
> está na seção `Reauditoria 2026-11-20` de cada `repositories/*/REPORT.md`;
> resumo por objeto em `audits/REAUDIT-2026-11-20.md`.

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem |
|---|---|---|---|
| `LR-STUDIO-001` | IDE Rust/Tauri como referência | `repositories/openidea/REPORT.md` | pesquisa externa (novo) |
| `LR-STUDIO-002` | 49 agentes / 75 skills de gamedev, escada de design | `repositories/claude-code-game-studios/REPORT.md` | pesquisa externa (novo) |
| `LR-STUDIO-003` | ReScript (avaliação de stack) | `repositories/rescript-lang/REPORT.md` | pesquisa externa (novo) |
| `LR-LIC-005` | Licenças prontas: aviso MIT dentro do payload de Skill, marca de terceiros | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 18 relatórios |
| `LR-STUDIO-004` | 17 apps criativos em Rust: barramento único de comandos e superfície de agente | `repositories/artcraft/REPORT.md` | pesquisa externa (novo) |
| `LR-STUDIO-005` | Framework C#/Vulkan (BRUTAL): “framework, não engine”, `LICENSES/` por pacote, política de IA em PR | `repositories/brutal/REPORT.md` | pesquisa externa (novo) |
| `LR-SEC-007` | Checklist de auditoria para app desktop e IPC local | `repositories/cloudflare-security-audit-skill/REPORT.md` | pesquisa externa (novo) |
| `LR-AGENT-010` | Skills de edição de foto/PDF sem gerador de imagem | `cross-project/agents/ARTCRAFT-SKILL-PACK.md` | derivado de `LR-STUDIO-004` |
| `LR-FORGE-004` | VFX 2D / animação pixel art | `repositories/pixelfx/REPORT.md` | pesquisa externa (novo) |
| `LR-STUDIO-006` | 79 Skills de game dev + roteador; regras de autoria e pipeline de asset | `repositories/awesome-gamedev-agent-skills/REPORT.md` | pesquisa externa (novo, 2026-11-20) |
| `LR-STUDIO-007` | Criação de personagens: silhueta antes do 3D (visão geral) | `cross-project/character-creation/CHARACTER-CREATION-RESEARCH.md` | pedido do Forge 2.0 (2026-11-20) |
| `LR-STUDIO-008` | Silhueta, linguagem de forma e avaliação | `cross-project/character-creation/SILHOUETTE-FIRST-DESIGN-RESEARCH.md` | derivado de `LR-STUDIO-007` |
| `LR-STUDIO-009` | Character sheet e consistência entre vistas | `cross-project/character-creation/CHARACTER-SHEET-CONSISTENCY.md` | derivado de `LR-STUDIO-007` |
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
| ZIP de 9,9 MB de terceiros versionado | proveniência **estabelecida** por reconstrução: é o pacote das tags v0.4.14→v0.5.0 (764 arquivos). Resta gravar tag + `sha256` no aviso de terceiros e decidir quando reempacotar (`DR-0004`, `LR-STUDIO-012` §7) |
| coordenação de vários agentes no Studio | o formato de handoff por arquivo (objetivo, estado, decisões e motivos, arquivos, passos) está auditado em `LR-STUDIO-012` §2 — ainda sem implementação |
| `img2threejs` (Apache-2.0) | lido na origem em 2026-11-22: `LICENSE` presente, nenhum `NOTICE` no upstream; o vendoring do mr-mak rompeu o campo `version:` (`LR-STUDIO-012` §13) |
| Triagem OpenDots/OpenBot nunca concluída | `PENDENTE` desde 2026-10-17 |
| 16 skills sem licença | bloqueia distribuição |
| Fronteira Studio↔Forge com dois documentos concorrentes | `CONFLICTING` |

---

## 6. Conferência de ponteiros — 2026-11-26

Medição desta sessão (`gh api` na `main`; `audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md` §2.3).
O texto acima é o registro de 2026-11-17/2026-11-20.

| Afirmação anterior | Estado hoje |
|---|---|
| §2 "12 documentos mantidos na origem" | **ENTREGA CONCLUÍDA**: os 12 estão na `main`; sete deles **recuperados** exatamente para os caminhos originais sem alterar os bytes dos blobs (`docs/BRANCH-CLEANUP-2026-11-26.md`) |
| "`docs/INDICE-DOCUMENTOS.md` … 2 versões divergentes"; "`planejamento/*` `CONFLICTING` de tamanho" | **fechados**: um `docs/INDICE-DOCUMENTOS.md` (3.730 B) e cinco arquivos em `docs/planejamento/`, cada um uma vez |
| "Sem `LICENSE` no payload do Studio" | **superada**: `LICENSE` na raiz = **MIT**, "Copyright (c) 2026 BloomRX e colaboradores da Lia Studio", 1.539 B |
| "16 skills no payload" | **0** `SKILL.md` na `main` (só `.agents/skills/README.md`); a autoria migrou para o Agent Hub — `docs/windows-evidence/HUB-SKILLS-FOLLOWUP.md`: "O Studio não restaura a autoria dessas Skills: o Agent Hub as gerencia" |
| "`docs/MULTI-AGENT`, fronteira com o Forge" | o registro de limpeza **deixa de afirmar** que o contrato Forge não foi publicado; a limitação atual é "a integração ainda não validada do editor com esse contrato e com o runtime Lia" → contrato: **entregue**; integração: **VALIDAÇÃO NÃO EXECUTADA** |
| ZIP de terceiros | tamanho versionado real: `docs/Mr-Mak-Skills-Free.zip` **3.352.656 B** (`docs/pacote-agentes.zip` 15.652 B); o "9,9 MB" dos nossos textos é o **extraído**, unidade que `DR-0004` já explicita junto de tag + `sha256` |
| validação da integração | **executada pelo Studio, não por nós**: Linux 2026-11-26 com `verify_alpha.py --part 1..10` verdes (314 testes + 8 pulados), `test_project_cli.py -q` 21, `test_creation.py -q` 23, servidor em `127.0.0.1` com 4 HTTP 200. Os 8 pulados são 7 de Windows Job Objects + 1 de Godot real no Windows |
| evidência Windows | **VALIDAÇÃO ABERTA**: `docs/windows-evidence/windows-check-20261126T004322Z-a4f81556.json` com partes 1-6 e 8 PASS e **7, 9 e 10 FAIL** (`godot/unreal/unity_on_path: false`; 7 chaves `not_tested`; sem logs brutos; sem dados de projeto). O run anterior (`09ce703d`) tinha FAIL em 3, 6, 7, 9, 10. Causa de FAIL **não** é atribuível pelo código de saída, e "nenhum resultado Linux substitui reteste Windows" |
