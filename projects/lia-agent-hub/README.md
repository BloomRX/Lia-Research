# Lia Agent Hub — consolidação da pesquisa existente

| Campo | Valor |
|---|---|
| Repositório de origem | `BloomRX/Lia-AgentHub` ⚠️ **não** `Lia-Agent-Hub` |
| Branch padrão | `main` @ `8c14ec85` (2026-11-26T08:57:25Z, **202 commits**) — antes `34a27f4` (2026-11-14, 8) |
| Branch mais avançada | **a `main`**: as quatro `arena/*` (incl. `arena/1a7ed773-lia-agenthub` @ `bd4bfbb`) foram consolidadas e removidas em 2026-11-26 |
| Branches remotas | **1** (`main`) — eram 5 em 2026-11-17 |
| Arquivos na `main` | 199 entradas (165 blobs, 50 `.md`, 78 em `docs/**`) · **0** `SKILL.md` e **0** `LICENSE` no payload |
| Arquivos | 250 · **57 documentos, todos de autoria Lia** |
| Data do inventário | 2026-11-17 |

---

## 1. Correção de nome (importante)

A ordem de serviço usa `BloomRX/Lia-Agent-Hub`. Esse caminho **não existe**
(`Could not resolve to a Repository`). O repositório real é `BloomRX/Lia-AgentHub`,
criado em 2026-11-15. Qualquer automação, link ou índice que use o nome com hífens
falha silenciosamente.

## 2. O que este projeto é

Catálogo, descoberta, empacotamento e orquestração de Skills e capacidades. É o
projeto com a documentação de **governança de licença mais avançada** do ecossistema —
e o único com auditoria de proveniência de Skills concluída.

## 3. Pesquisa existente (13 documentos em `docs/research/`)

| Documento | Tamanho | Tema | Status |
|---|---:|---|---|
| `ARCHITECTURE-SECURITY-CROSS-REVIEW.md` (`docs/review/`) | 96 KB | revisão cruzada de arquitetura e segurança | `CURRENT` |
| `PHASE-0-1-CONSISTENCY-REVIEW.md` | 54 KB | revisão de consistência (6× `REJEITAR`) | `HISTORICAL` (fase concluída) |
| `LIA-SKILLS-INVENTORY.md` | 37 KB | inventário de Skills | **`CURRENT` — fonte canônica** |
| `SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` | 36 KB | auditoria de licença/proveniência | **`CURRENT` — fonte canônica** |
| `THIRD-PARTY-SKILLS-CATALOG.md` | 34 KB | catálogo de Skills de terceiros | vigente |
| `INTEGRATION-CANDIDATES.md` | 37 KB | candidatos de integração | vigente |
| `REPOSITORY-AND-BRANCH-AUDIT.md` | 30 KB | auditoria de repos e branches | `HISTORICAL` (vence rápido) |
| `LIA-SKILLS-ROADMAP.md` | 21 KB | roadmap de skills próprias | vigente |
| `SKILL-CATALOG-IMPORT-REPORT.md` | 21 KB | relatório de importação | vigente |
| `PHASE-0-1-1-FINAL-CONSISTENCY-FIXES.md` | 21 KB | correções de consistência | `HISTORICAL` |
| `PHASE-0-1-2-PRECISION-FIXES.md` | 15 KB | ajustes de precisão Unicode | `HISTORICAL` |
| `README.md` (research) | 7,7 KB | índice do agente de pesquisa | vigente |
| `catalog/README.md` | 3,3 KB | formato de registro de catálogo | vigente |

Arquitetura (8) e segurança (`SECURITY-AND-TRUST-MODEL.md`, 40 KB) são os documentos
mais densos e mais úteis para o resto do ecossistema.

## 4. Achados que atravessam todo o ecossistema

Extraídos de `LIA-SKILLS-INVENTORY.md` (2026-11-15, `arena/db625478`) e reconferidos
na árvore em 2026-11-17:

| Achado | Número | Rótulo |
|---|---:|---|
| Skills catalogáveis (formato `SKILL.md`) | **48** (Studio 16 · Project 22 · Model-Lab 9 · Forge 1) | `CONFIRMED` |
| Autorais/adaptadas pela Lia | **47** | `CONFIRMED` |
| Terceiro vendorizado com patches | 1 (`alethe`) | `CONFIRMED` |
| Skills do AIRI vendorizadas dentro do Lia-Project | **29** | `CONFIRMED` |
| Skills de terceiros em ZIP guardado no Studio (não importado) | 20 | `CONFIRMED` |
| Perfis de agente Codex (não são Skills) | 7 | `CONFIRMED` |
| Capacidades registradas em código (Forge) | 49 | `CONFIRMED` |
| Ferramentas MCP implementadas num produto Lia | 10 | `CONFIRMED` |
| Registros de catálogo de modelo | 44 catalogados · ~131 descobertos · **0 validados** | `CONFIRMED` |
| Skills em `main` de qualquer repositório Lia | **9** (só Model-Lab) | `CONFIRMED` |

**As três conclusões do inventário, preservadas:**

1. O ecossistema tem 47 capacidades em formato Agent Skills — o Hub não nasce vazio.
   Mas quase nada está em `main`; existência em branch não é presença em `main`.
2. Nenhuma das 47 pastas carrega licença no payload. O importador detecta licença
   apenas por arquivo na raiz (`adapters/importer.py::_detect_license`), portanto as 47
   entrariam como `licenseKnown: false`.
3. Há duplicação real e não decidida: `lia-brand-check` ≈
   `lia-brand-consistency-review`; três skills de orquestração se sobrepõem.

## 5. Estado da evidência (correção de vocabulário)

O histórico do projeto registra evidência classificada como **"EXECUTED", não
"VALIDATED"**. O Lia-Research não adota esse vocabulário duplo: usa os seis rótulos de
`governance/EVIDENCE-STANDARDS.md`. O mapeamento é:

| Vocabulário do Hub | Equivalente aqui |
|---|---|
| `EXECUTED` | `OBSERVED` (foi executado, sem validação independente) |
| `VALIDATED` | `CONFIRMED` |
| `BLOCKED` / inexistente | `BLOCKED` |

Registrado como `CONFLICTING` de vocabulário, com os dois preservados.

## 6. Gaps E-1…E-9

O inventário histórico identificou nove lacunas (E-1 a E-9) no modelo de catálogo.
Elas **não foram reescritas aqui** — o documento de origem é a fonte. A consolidação
de Skills e licença está em `skills/SKILL-LICENSE-CONSOLIDATION.md`; a lista de lacunas
com status está em `INDEX.md` §5.

---

**Pesquisa desta base que toca este projeto agora** · 2026-11-26 — o terceiro modelo de licença de Skill (inventário por arquivo com gate, `LR-UI-006` §9) e o censo dos 21 `SKILL.md` sem `LICENSE.txt` lateral; matriz em [`comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md`](../../comparisons/ANIMAMA-RECOMMENDATION-MATRIX.md) §4.4.
