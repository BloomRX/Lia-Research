# Auditoria de proveniência — Skills AIRI e Alethe

| Campo | Valor |
|---|---|
| ID | `LR-LIC-003` |
| Categoria | licensing |
| Projetos beneficiados | Lia-Project (origem), Lia Agent Hub (distribuição), Lia Studio |
| Fontes | `Lia-Project@005a324` (branch `arena/7fa837f0-lia-project`): árvore de `.agents/skills/` (22) e `airi/.agents/skills/` (28); 50 `SKILL.md` lidos; 5 arquivos de licença; `alethe/UPSTREAM.md`; `moeru-ai/airi` e `Kc1t/alethe-orchestrate-skill` consultados na API |
| Coleta | 2026-11-17 · **nenhum payload copiado ou executado** |
| Status | CURRENT |
| Confiança | **Alta** (leitura direta de arquivo e de frontmatter) |
| Próxima revisão | 2027-02-17, ou quando qualquer `SKILL.md` mudar |

---

## 1. Pergunta

As Skills de terceiro que vivem no Lia-Project têm origem, autoria e licença
identificáveis, e a Lia pode redistribuí-las? O que falta, por Skill?

## 2. Método

1. Enumerar a árvore real dos dois diretórios de Skills (`git/trees`, não README).
2. Ler o frontmatter de **todos** os `SKILL.md` (22 + 28) e extrair `metadata.author`,
   `metadata.source` e `license`.
3. Localizar arquivos `LICENSE`/`NOTICE`/`COPYING` dentro de cada payload.
4. Ler o corpo da licença (não o selo) e identificar o titular.
5. Consultar o repositório upstream (`moeru-ai/airi`, `Kc1t/alethe-orchestrate-skill`)
   para confirmar licença de repositório.
6. Classificar cada Skill em uma das seis classes de `LR-LIC-001` §2.

Dados brutos: `data/inventory/skills-provenance.tsv` (50 linhas, com bytes e campos).

## 3. Inventário

| Grupo | Skills | Bytes | Com `LICENSE` no payload | Com `author` no frontmatter |
|---|---:|---:|---:|---:|
| `.agents/skills/` (raiz do Lia-Project) | **22** (21 Lia + `alethe`) | 1.502.809 | **1** (`alethe`) | 0 |
| `airi/.agents/skills/` (vendor AIRI) | **28** | 1.347.667 | **4** | **8** |
| **Total** | **50** | **2,85 MB** | **5 (10%)** | **8 (16%)** |

Correção de registro: o número "29 skills AIRI" usado na fundação contava o
`alethe` junto. O correto é **28 AIRI + 1 Alethe = 29 payloads de terceiro**.

## 4. Licença de repositório (a base legal de 19 das 28)

| Repositório | Licença | Titular | Evidência |
|---|---|---|---|
| `moeru-ai/airi` | **MIT** | Neko Ayaka (2024–presente) | `airi/LICENSE` no vendor + API do upstream `CONFIRMED` |
| `Kc1t/alethe-orchestrate-skill` | **MIT** | Kauã Miguel (2026) | `.agents/skills/alethe/LICENSE` + API `CONFIRMED` |
| `BloomRX/Lia-Project` (as 21 Skills Lia) | **nenhuma** | — | API: `.license = null`, repo **público** `CONFIRMED` |

Ponto crítico: as 21 Skills autorais vivem em repositório **público e sem licença**.
O padrão legal é "todos os direitos reservados" — visível, mas sem permissão de uso.
Isso é consistente com `DR-0001` e agora tem evidência de repositório, não só de payload.

## 5. Proveniência das 28 Skills AIRI — parecer por Skill

`LIC` = arquivo de licença dentro do payload. `AUT` = autor declarado no frontmatter.

| # | Skill | AUT | Origem declarada | LIC | Classe | Pendência |
|---|---|---|:--:|:--:|---|---|
| 1 | `agent-browser` | — | — | — | `RESEARCH_ONLY` | autor e origem desconhecidos |
| 2 | `agent-browser-electron` | — | — | — | `RESEARCH_ONLY` | idem |
| 3 | `create-pr` | — | — | — | `RESEARCH_ONLY` | idem |
| 4 | `enforce-rules-for-unocss` | — | — | — | `RESEARCH_ONLY` | idem |
| 5 | `enforce-rules-for-vitest` | — | — | — | `RESEARCH_ONLY` | idem |
| 6 | `eventa` | **moeru-ai** | — | — | `ADAPT_ALLOWED` | autor é o dono do AIRI (MIT) |
| 7 | `pinia` | **Anthony Fu** | gerado de `vuejs/pinia` via `antfu/skills` | — | `ADAPT_ALLOWED` | MIT do repo cobre; atribuição preservada |
| 8 | `pnpm` | **Anthony Fu** | gerado de `pnpm/pnpm` via `antfu/skills` | — | `ADAPT_ALLOWED` | idem |
| 9 | `release-note-writer` | — | — | — | `RESEARCH_ONLY` | autor desconhecido |
| 10 | `simple-english` | — | — | — | `RESEARCH_ONLY` | 18 KB, autor desconhecido |
| 11 | `stage-tamagotchi-godot-csharp` | — | — | — | `RESEARCH_ONLY` | específico do AIRI |
| 12 | `tsdown` | — | VoidZero + sxzz | **MIT** | `USE_AS_IS` | licença própria presente |
| 13 | `unocss` | **Anthony Fu** | gerado de `unocss/unocss` | — | `ADAPT_ALLOWED` | idem |
| 14 | `upload-github-attachment` | — | — | — | `RESEARCH_ONLY` | autor desconhecido |
| 15–22 | `use-agent-browser-*` (2), `use-vishot*` (6) | — | — | — | `RESEARCH_ONLY` | família de ferramentas proprietárias; autor desconhecido |
| 23 | `vue` | **Anthony Fu** | gerado de `vuejs/docs` | — | `ADAPT_ALLOWED` | idem |
| 24 | `vue-best-practices` | **vuejs-ai** | — | **MIT** | `USE_AS_IS` | © 2025 hyf0, SerKo |
| 25 | `vue-testing-best-practices` | **vuejs-ai** | — | **MIT** | `USE_AS_IS` | mesmo titular |
| 26 | `vueuse-functions` | **SerKo** | — | **MIT** | `USE_AS_IS` | © 2026 SerKo |
| 27 | `web-design-guidelines` | **vercel** | Web Interface Guidelines | — | `RESEARCH_ONLY` | **declara autor mas não licença nem fonte** |
| 28 | `xsai` | — | — | — | `RESEARCH_ONLY` | autor desconhecido |

Resumo: 4 `USE_AS_IS` · 5 `ADAPT_ALLOWED` · **19 `RESEARCH_ONLY`**.

## 6. Alethe — o único caso bem documentado do ecossistema

| Item | Valor |
|---|---|
| Upstream | `Kc1t/alethe-orchestrate-skill` (MIT, 154★, ativo) |
| Versão | 19 (2026-10-23), comparada com `c36c341c…` |
| Payload | 24 arquivos, ~900 KB (inclui 2 PNG em base64 de 484 KB e 313 KB, `report.html` 66 KB, `editor.html` 180 KB, `orchestrate.py` 251 KB) |
| Licença no payload | `LICENSE` MIT © 2026 Kauã Miguel — **presente** |
| Proveniência | `UPSTREAM.md` com origem, versão, commit comparado, licença, fonte consultada e tutorial |
| Patches locais | **sim** — SKILL.md tem seção "Local audit constraints (Lia, 2026-10-28)" (editor com `textContent` + filtro de URL; reserva atômica de estimativas); registrados em `UPSTREAM.md` e em `docs/architecture/ALETHE-HARDENING-2026-10-28.md` |
| Classe | `FORK_CANDIDATE` (patch próprio sobre base MIT) |
| Pendência | patches não são commit upstream; atualizar exige diff manual |

**Este é o padrão a generalizar.** É o único payload de terceiro no ecossistema em que
licença, versão, commit comparado, patches e limites de escopo estão no mesmo lugar —
dentro do payload, não num documento distante.

## 7. Achados

### 7.1 Atribuição viaja; licença não
8 das 28 Skills declaram `metadata.author` (e algumas, o `source` de geração). Isso é
atribuição real e vale como evidência de origem — mas **nenhuma** declara `license` no
frontmatter. Obrigação MIT exige o texto da licença junto da cópia; um campo `author`
não substitui o `LICENSE`.

### 7.2 19 Skills sem autor, sem fonte e sem licença própria
Sobrevivem pelo MIT do repositório AIRI (Neko Ayaka). É defensável para redistribuição
**se** o aviso MIT viajar. Não é defensável para reivindicar autoria nem para relicenciar.
Duas delas (`web-design-guidelines` de vercel, família `use-vishot`) claramente **não**
são obra do AIRI — o MIT do AIRI provavelmente não cobre terceiro que ele mesmo vendorizou.

### 7.3 `web-design-guidelines` é o maior risco individual
Declara `author: vercel`, `version: 1.0.0`, sem `source`, sem `LICENSE`. É conteúdo
institucional de terceiro dentro de um payload redistribuível. Antes de qualquer
exportação, precisa de origem e licença verificadas na fonte (Vercel Web Interface
Guidelines).

### 7.4 Uma Skill Lia já concede MIT
`lia-eventa-ipc/SKILL.md` traz `license: MIT` no frontmatter — **a única** das 21 Skills
autorais. Ou é acidente, ou é teste. Em qualquer caso, hoje existe exatamente uma Skill
`lia-*` com licença e vinte sem, o que torna impossível dizer "a política das Skills Lia
é X". Não alterei nada (repositório de produto é read-only para esta base).

### 7.5 Os cinco repositórios Lia são públicos e sem licença
`Lia-Project`, `Lia-Forge`, `Lia-Studio`, `Lia-AgentHub`, `Lia-Model-Lab`: `.license =
null`, público. Consequência: 2,85 MB de payload de Skills visíveis, 90% sem licença
dentro do payload, num repositório sem licença de projeto.

## 8. Riscos

| Risco | Severidade | Evidência |
|---|---|---|
| Exportar Skill sem o aviso MIT | **alta** — descumprimento de licença | 19 de 28 sem `LICENSE` |
| Reivindicar autoria de Skill de terceiro | média | 8 com autor declarado, 19 sem |
| Redistribuir `web-design-guidelines` sem base | **alta** | autor vercel, sem licença |
| Perder patches do `alethe` em atualização | média | `UPSTREAM.md` cobre, mas exige diff manual |
| Inconsistência de licença entre Skills Lia | média | `lia-eventa-ipc` MIT × 20 sem licença |
| Payloads pesados no repo (900 KB só no alethe) | baixa | 2,85 MB total |

## 9. Recomendações (proposta — não aplicada)

1. **`UPSTREAM.md` obrigatório** em todo payload de terceiro: origem, versão, commit
   comparado, licença, patches, data. Modelo: `.agents/skills/alethe/UPSTREAM.md`.
2. **`LICENSE` dentro do payload** sempre que a licença não for a do repositório hospedeiro.
3. **Corrigir `web-design-guidelines`**: obter licença e fonte na Vercel, ou remover do
   vendor, ou marcar `RESEARCH_ONLY` de forma explícita no catálogo.
4. **Resolver `lia-eventa-ipc`**: decisão do proprietário (`DR-0001`); até lá, registrar
   a inconsistência no catálogo em vez de silenciá-la.
5. **Não exportar nenhuma das 19 `RESEARCH_ONLY`** até auditoria individual de origem.
6. Registrar no importador do Hub: licença ausente = `BLOCKED` para exportação, não
   "desconhecida" (ausência de licença não é ausência de informação: é ausência de direito).

## 10. Limitações e pendências

| Limitação | Rótulo |
|---|---|
| Origem individual das 19 sem autor não rastreada até o autor original | `UNVERIFIED` |
| Licença do `web-design-guidelines` na fonte Vercel | `BLOCKED` (não pesquisado nesta rodada) |
| Nenhum payload foi executado | `NOT RUN` |
| Contagem depende de `005a324`; branches `arena/*` estão sendo podadas | `CONFIRMED` |
| Skills do Studio/Model-Lab/Forge não reauditadas aqui | cobertas por `LR-LIC-001` |

## 11. Encaminhamento

| Ação | Dono | Bloqueio |
|---|---|---|
| Decidir licença `lia-*` e resolver `lia-eventa-ipc` | proprietário | `DR-0001` |
| Auditar origem de `web-design-guidelines` | Research | próxima rodada |
| Tornar `UPSTREAM.md` + `LICENSE` gate de importação no Hub | Lia Agent Hub | `DR-0011` |
| Atualizar `LR-LIC-001` com a contagem corrigida (28+1) | Research | feito nesta rodada |
