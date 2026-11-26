# Lia Studio — consolidação da pesquisa existente

| Campo | Valor |
|---|---|
| Repositório de origem | `BloomRX/Lia-Studio` |
| Branch padrão | `main` @ `0e7b9949` (2026-11-26T09:20:01Z, **115 commits**) — antes `ba70d22` (2026-10-30, 4) |
| Branch mais avançada | **a `main`**: `arena/01a0f4ab-lia-gamedev` @ `b099c4a` (2026-11-16, 90 commits) foi integrada pelo PR #1 (`12dccf06`) e removida |
| Branches remotas | **1** (`main`) — eram 9 em 2026-11-17; oito removidas após o merge |
| Arquivos na `main` | 226 entradas (210 blobs, 83 `.md`, 88 em `docs/**`) |
| Arquivos | 1.019 · **109 documentos, todos de autoria Lia** |
| Skills | **0** com payload próprio na `main` (só `.agents/skills/README.md`); o inventário de 2026-11-17 contava 16 — a autoria migrou para o Agent Hub |
| Licença | **MIT** em `LICENSE` (1.539 B, "Copyright (c) 2026 BloomRX e colaboradores da Lia Studio") — não constava do inventário anterior |
| Data do inventário | 2026-11-17 |

---

## 1. O que este projeto é

Ambiente de criação de jogos: engine (Godot), gameplay, editor, skills de gamedev e
design system próprio. É o projeto com a **maior densidade de Skills** por documento
(16 em 109 documentos).

## 2. Situação do conhecimento

Como no Forge, `main` tem 4 commits e não contém a pesquisa: os 15 documentos de
`docs/research/` existem apenas em branches de sessão. A auditoria de integração
Studio↔Forge (`STUDIO-FORGE-INTEGRATION-AUDIT.md`, **179 KB**) é o maior documento
individual de todo o inventário.

## 3. Pesquisa existente (15 documentos em `docs/research/`)

| Documento | Tamanho | Tema |
|---|---:|---|
| `STUDIO-FORGE-INTEGRATION-AUDIT.md` | 179 KB | fronteira Studio↔Forge (maior documento do inventário) |
| `ARENA-ENGINE-INTEGRATION-AUDIT.md` | 79 KB | integração de engines |
| `ARENA-SKILLS-MCP-AGENT-TOOLS-RESEARCH.md` | 68 KB | skills, MCP e ferramentas de agente |
| `ARENA-UIUX-AUDIT.md` | 50 KB | UI/UX |
| `AGENT-ARCHITECTURE-RESEARCH.md` | 42 KB | arquitetura de agentes |
| `ARENA-RUNTIME-SECURITY-AUDIT.md` | 42 KB | segurança de runtime de agente (21× `ADAPTAR`, 1 `ADOTAR`) |
| `ARENA-GAMEPLAY-QA-AUDIT.md` | 35 KB | gameplay e QA |
| `BRANCH-ARQUITETURA-ANTIGA-2026-10-18.md` | 32 KB | registro histórico de arquitetura anterior |
| `MANUS-METODO-PARA-LIA-STUDIO-2026-09-30.md` | 11 KB | método observável do Manus |
| `ARENA-SESSION-REPORT-AGENT6.md` | 10 KB | relatório de sessão |
| `PACOTE-AGENTES-INTEGRACAO-2026-10-17.md` | 6,8 KB | pacote de agentes + DevKit |
| `CORE-LOOP-MAGMADEV.md` | 3,5 KB | loop de gameplay |
| `GAMEDEV-SKILLS-FONTES-2026-10-17.md` | 3,3 KB | fontes de skills de gamedev |
| `STEFAN-WORKSPACE-NOTES-2026-10-12.md` | 3,2 KB | notas de workspace local |
| `OPENBOT-OPENDOTS-TRIAGEM.md` | 2,7 KB | triagem de OpenBot/OpenDots (`PENDENTE`) |

## 4. Fontes de terceiros já mapeadas pelo Studio

| Fonte | Licença | Estado no Studio |
|---|---|---|
| `Donchitos/Claude-Code-Game-Studios` | MIT | 7 skills adaptadas; texto preservado em `docs/licenses/` |
| `witnesstodark/mr-mak-workspace` | MIT (+ `img2threejs` Apache-2.0) | 5 skills adaptadas + ZIP de 9,9 MB versionado — upstream auditado em `LR-STUDIO-012` |
| `CopilotKit/OpenDots` | a verificar | triagem `PENDENTE` |
| `nightly-labs/openbot` | a verificar | triagem `PENDENTE` |
| `gamedev-skills/awesome-gamedev-agent-skills` | lista | fonte de referência |
| `anthropics/skills` | a verificar | referência |

## 5. Skills do projeto (16) — nenhuma com licença no payload

`ai-design` · `game-design` · `godot-*` · `level-design` · `narrative` · `qa-*` ·
`ui-ux` · `devkit` (conjunto de 16 pastas, ver `LIA-SKILLS-INVENTORY.md`).
Doze têm seção `## Origem` apontando o commit upstream — boa prática de proveniência
que **não resolve** a obrigação, porque o aviso MIT não viaja no payload.

## 6. Duplicação e conflito

| Item | Situação |
|---|---|
| `planejamento/*` com 2 versões de 3 documentos | `CONFLICTING` de tamanho |
| `docs/INDICE-DOCUMENTOS.md` em 2 versões | índices divergentes |
| `STUDIO-FORGE-INTEGRATION-AUDIT.md` (179 KB) vs Forge `STUDIO-FORGE-CONSISTENCY-ARCHITECTURE.md` (29 KB) | dois documentos sobre a mesma fronteira, em dois repositórios |

---

**Pesquisa desta base que toca este projeto agora** · 2026-11-26 — o gate de promoção por item do Animama é vizinho do problema dos 43 pacotes em versões divergentes do censo: a matriz em [`comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md`](../../comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md) §4.3.
