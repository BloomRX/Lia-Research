# Claude-BugHunter — bundle de Skills ofensivas com engenharia de qualidade rara

| Campo | Valor |
|---|---|
| ID | `LR-SEC-006` |
| Categoria | security |
| Projetos beneficiados | Lia Agent Hub (primário), Lia-Project, Lia Studio, Lia Forge, Lia Model Lab — **pela engenharia, não pelo conteúdo** |
| Fontes | `elementalsouls/Claude-BugHunter@b63ae349afad88772e6d854a277ae9965fd4c369` (2026-11-18): `README.md` (23 KB, 346 linhas), `plugin.json`, `marketplace.json`, `LICENSE`, `LICENSE-CONTENT`, `NOTICE`, `docs/credits.md`, `eval/README.md`, `eval/BASELINE.md`, `.github/workflows/{leak-guard,skill-lint,doc-count-check}.yml`, `scripts/scan_identifiers.py`, `skills/hunt-xss/SKILL.md`, árvore completa (341 blobs) |
| Data | 2026-11-17 (coleta) · commit do repo é de 2026-11-18 UTC |
| Próxima revisão | 2027-02-17 |
| Status | CURRENT |
| Recomendação | **REFERÊNCIA** — instalar não; copiar seis mecanismos de engenharia, sim |
| Licença | **Dupla**: código MIT + conteúdo CC BY 4.0 (`CONFIRMED`) |
| Confiança | **Alta** para estrutura, licença e CI (arquivos lidos); **nula** para eficácia das Skills (não executado; o próprio repo mede delta 0 no que mediu) |

---

## 1. Identificação

- **Nome:** `claude-bughunter` · autor **Sachin Sharma** (`elementalsouls`), GenAI Security Research
- **URL:** https://github.com/elementalsouls/Claude-BugHunter · site https://elementalsouls.github.io/Claude-BugHunter
- **Commit analisado:** `b63ae349` (2026-11-18T13:09Z) — branch `main`
- **Métricas:** ★ **11.020** · 1.491 forks · 13 issues abertas · criado 2025-05-05 · **341 arquivos** · 3,6 MB
- **Versão declarada:** `2.1.0` em `.claude-plugin/plugin.json` e `marketplace.json`
- **Conteúdo:** **83 Skills** (58 `hunt-*` + 10 plataforma empresarial + 6 relatoria/validação + 5 recon/OSINT + 4 metodologia), **15 slash commands**, 32 arquivos de engine Python, 18 de teste, 16 de eval
- **Linguagem:** Python (engine + eval + scripts), Markdown (conteúdo)
- **Classificação:** bundle de Skills para pentest/bug bounty externo; **ofensivo por natureza**, com postura de autorização explícita

## 2. Resumo executivo

É o maior bundle público de Skills para Claude Code que esta base já leu, e o único do
gênero que trata **qualidade como problema de engenharia**: lint de Skill, guarda de
vazamento de identificador, checagem de contagem em documentação, índice de Skills com
detecção de drift, e um **harness de avaliação com ablação** (skills ligadas × desligadas)
que publica um baseline **negativo** — delta **+0%** de resolução, custo +US$ 0,076.

Para a Lia, o valor **não** é o conteúdo ofensivo (fora de escopo em todos os cinco
projetos). É o conjunto de mecanismos que a Lia não tem e vem resolvendo à mão:

1. **avaliação de Skill com ablação e oráculo auto-avaliado** — a Lia tem 48 Skills e
   **zero** medidas (`LR-LIC-001`, `LR-AGENT-009` V6);
2. **`leak-guard` com denylist hasheada e falha fechada** — a Lia expôs caminho de usuário
   e IDs de sessão no próprio snapshot e descobriu por varredura manual;
3. **`doc-count-check`** — a Lia tinha 5 contagens divergentes na fundação, corrigidas à mão;
4. **`skill-lint` + auto-checagem de roteamento** — Skill adicionada sem mapeamento falha
   o CI em vez de ficar inalcançável;
5. **licença dupla com fronteira por tipo de arquivo** (código MIT × conteúdo CC BY 4.0) +
   `NOTICE` + `credits.md` — exatamente a lacuna "0 de 48 payloads com licença";
6. **manifesto de plugin** que declara versão, autor, licença, **credencial (`sensitive: true`)**
   e servidor MCP com `env` mapeado — valida e completa a proposta `LR-AGENT-009`.

Ao mesmo tempo, o repositório tem **duas inconsistências de licença** internas (README/
NOTICE × `credits.md`; `plugin.json` diz só "MIT") que servem de aviso: metadado de licença
sem verificação automática diverge — inclusive num repo de segurança com CI exemplar.

## 3. O que resolve

| Problema | Solução no repo |
|---|---|
| Skill de segurança genérica demais ("um prompt grande") ou fragmentada (30 links) | 83 Skills por classe, com gatilho por descrição |
| Claims sem prova ("nossas skills ajudam") | harness de avaliação com ablação e baseline publicado (mesmo quando o resultado é nulo) |
| Vazamento de identificador de cliente em README/testes | `scan_identifiers.py` repo-wide, denylist hasheada, **fail-closed** |
| Números de documentação envelhecem | `check_doc_counts.py` no CI |
| Skill órfã (não roteada) | `engine/skill_map.py` auto-checagem que falha o build |
| Instalação em 5 harnesses diferentes | `install.sh`/`install.ps1` com `--all`, manifesto de instalação, `--uninstall` que preserva Skill de outro bundle |
| Bundle enorme sem catálogo | `gen_skill_index.py --check` + `docs/skills.md` |

## 4. Arquitetura

```text
.claude-plugin/{plugin.json, marketplace.json}   manifesto + catálogo de marketplace
skills/<83>/SKILL.md                              conteúdo (CC BY 4.0)
commands/<15>.md                                  slash commands (Claude Code only)
engine/  (Python)  scope.py · recon.py · skill_map.py · memory.py · closure.py · engine.py
                  routing determinístico: achado → Skill que o trata
eval/    run_eval.py · run_eval_ps*.py · oracle_portswigger.py · run_fp.py · BASELINE.md
research/reports/  harvest_h1/bugcrowd/intigriti → classify → draft_patterns → coverage
scripts/  install.sh/.ps1 · scan_identifiers.py · lint_skills.py · check_doc_counts.py
          gen_skill_index.py · refresh-cve-index.py · hunt.sh/.ps1
mcp/hackerone/  server.py (19 KB) + README
.github/workflows/  8 workflows
```

**Fronteira declarada:** a camada de *conhecimento* (Skills) porta para 5 harnesses
(`~/.claude/skills`, `~/.agents/skills`, `~/.hermes/skills`, `~/.gemini/config/skills`);
slash commands e engine ficam Claude-Code-only **por desenho**. `CONFIRMED` no README.

## 5. Funcionalidades

| Grupo | N | Exemplos |
|---|---:|---|
| `hunt-*` classes web/API | 58 | `hunt-xss`, `hunt-sqli`, `hunt-ssrf`, `hunt-idor`, `hunt-jwt-crypto`, `hunt-llm-ai`, `hunt-rag-vector`, `hunt-k8s` |
| Plataforma empresarial | 10 | `m365-entra-attack`, `okta-attack`, `vmware-vcenter-attack`, `enterprise-vpn-attack`, `apk-redteam-pipeline` |
| Relatoria e validação | 6 | `triage-validation` (7-Question Gate), `evidence-hygiene`, `report-writing`, `bugcrowd-reporting` |
| Recon e OSINT | 5 | `web2-recon`, `offensive-osint`, `recon-scope-triage` |
| Metodologia | 4 | `bb-methodology`, `redteam-mindset`, `mid-engagement-ir-detection` |

15 comandos: `/hunt`, `/recon`, `/scope`, `/surface`, `/triage`, `/validate`, `/report`,
`/chain`, `/intel`, `/token-scan`, `/autopilot`, `/web3-audit`, `/remember`, `/pickup`,
`/memory-gc`.

## 6. Dependências

| Dependência | Papel | Observação |
|---|---|---|
| Claude Code CLI (`claude -p`) | engine de execução do eval | `CONFIRMED` |
| Burp Suite + MCP server | "mãos" HTTP do agente | opcional; `--burp-mcp` |
| Docker | alvo auto-avaliado (Juice Shop) | `CONFIRMED` |
| subfinder · dnsx · httpx · katana · nuclei | recon | `REPORTED` (inventário no README) |
| SecLists / wordlists Assetnote | payloads | `REPORTED` |
| Python 3.12 stdlib | lint, scan, contagem, índice | `CONFIRMED` (CI sem pip) |
| Playwright | lançador headless do tier v1.1 | declarado como futuro |

## 7. Requisitos de hardware e sistema

CLI + Docker + Burp rodando localmente; nada exige GPU. **Compatível** com Windows
(41 KB de PowerShell: `install.ps1`, `hunt.ps1`, `install-community-skills.ps1`), o que é
raro entre os 17 objetos já auditados por esta base — e é o único ponto em que a stack do
repo encontra a stack da Lia (Windows 11 + RX 580) sem atrito.

## 8. Segurança e privacidade

Este é o objeto mais sensível já auditado aqui. Postura declarada:

| Item | Evidência |
|---|---|
| Autorização explícita exigida | `SECURITY.md` + seção "Authorization" do README `CONFIRMED` |
| Gate de escopo em código | `triage-validation` 7-Question Gate (Q2 impacto aceito, Q3 em escopo); `engine/scope.py` (8,7 KB) `CONFIRMED` |
| Fora de escopo declarado | AD interno, C2, pós-exploração, evasão, iOS/hardware, binário — lista explícita, chamada de "decisão de desenho" `CONFIRMED` |
| Guarda de identificador de cliente | `scan_identifiers.py` + denylist hasheada + `leak-guard.yml` em todo push, **fail-closed** `CONFIRMED` |
| Segredos | lint com varredura de segredo; `userConfig.sensitive: true` para token H1 `CONFIRMED` |
| Redação de PII em evidência | skill `evidence-hygiene`; problema real citado: "screenshots leaked cookies and victim PII" `REPORTED` |
| Safeguards do runtime | README documenta que Anthropic bloqueia/redireciona pedidos ofensivos e recomenda o Cyber Verification Program (CVP) `REPORTED` |

**Risco para a Lia:** instalar este bundle em runtime de produto traz capacidade ofensiva
para dentro de um app de consumo. Não é o perfil de ameaça do produto, e pode acionar
comportamento de recusa/fallback de modelo em fluxos de voz e chat — que é exatamente o
efeito que o próprio README descreve ("model switched mid-session"). `INFERRED` a partir
de `CONFIRMED` (documentação do fornecedor do modelo).

## 9. Licença e proveniência

**Dupla licença, com fronteira explícita por tipo de arquivo** (`CONFIRMED`):

| Conteúdo | Licença | Arquivo |
|---|---|---|
| `*.py`, `*.sh`, código | **MIT** © 2026 Sachin Sharma | `LICENSE` (1.070 B) |
| `*.md`, wordlists, catálogos de regex, rubricas, docs | **CC BY 4.0** | `LICENSE-CONTENT` (18.657 B, texto integral CC BY 4.0) |
| Skills de terceiros vendorizadas (8) | MIT de `shuvonsec/claude-bug-bounty` | `NOTICE` + `docs/credits.md` |

Composição declarada em `docs/credits.md`: **55 originais + 20 da comunidade + 8
vendorizadas = 83**; **12 dos 15 comandos** são vendorizados.

Obrigação prática do CC BY 4.0: **atribuir Sachin Sharma / Claude-BugHunter e linkar o
repositório**, inclusive em uso comercial. Isso é compatível com um README de pesquisa;
é **incompatível** com um produto que embuta o conteúdo sem crédito visível.

### 9.1 Duas inconsistências que o CI não pega

| Inconsistência | Evidência | Gravidade |
|---|---|---|
| `NOTICE` diz que o repo "does NOT redistribute upstream community skills directly", mas `credits.md` diz que "skills and commands are **vendored directly** into `skills/` e `commands/`" e a árvore confirma 83 `SKILL.md` presentes | `NOTICE` × `credits.md` × árvore | média — a redação de `NOTICE` provavelmente se refere às *outras* Skills referenciadas (instaladas por bootstrap), mas lida isolada contradiz o resto |
| `plugin.json` declara `"license": "MIT"` — o conteúdo é CC BY 4.0 | `plugin.json` | média — quem consome pelo marketplace vê só MIT |

Lição direta para a Lia: **manifesto de pacote é lugar de declarar licença por classe de
conteúdo**, e licença declarada sem checagem automática diverge — mesmo com 8 workflows.

VERDICT `REFERÊNCIA`, classe `USE_AS_IS` **apenas** para estudo dos mecanismos; **nenhum
payload copiado** (proibido, e desnecessário: o valor está nos scripts de higiene).

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Estrelas / forks | 11.020 / 1.491 | adoção alta |
| Último push | 2026-11-18 | ativo (commit no mesmo dia da coleta) |
| Versão | 2.1.0 | semver no manifesto |
| CI | **8 workflows** | acima da média do ecossistema Lia (0 a 2) |
| Testes | 18 arquivos (engine + harness + scanner self-test) | testa o *instrumento*, não só o produto |
| CODEOWNERS + 4 issue templates | presente | manutenção organizada |
| Changelog | `CHANGELOG.md` 11 KB | histórico escrito |
| Roadmap | público, com itens abertos e fechados | transparência |

## 11. Custos e limitações

| Item | Custo/limite | Evidência |
|---|---|---|
| Tokens de contexto | 83 Skills carregadas por descrição; o eval mediu **+1 turno e +US$ 0,076** no caso Juice Shop | `BASELINE.md` `CONFIRMED` |
| Docker + Burp + licença Burp Pro | setup pesado para o eval completo | `REPORTED` |
| Eval v0 é fraco por desenho | Juice Shop está memorizado → **delta 0%**, ceiling effect | `BASELINE.md` `CONFIRMED` |
| Eval v1 (PortSwigger) semi-bloqueado | exige conta + lançamento manual por CSRF | `eval/README.md` `CONFIRMED` |
| Fronteira de harness | commands/engine só Claude Code | `CONFIRMED` |
| Conteúdo ofensivo | inutilizável para produto de consumo | julgamento de escopo |

## 12. Compatibilidade com o ecossistema Lia

| Dimensão | Situação |
|---|---|
| Windows 11 | **sim** — PowerShell de primeira classe (`install.ps1`, `hunt.ps1`) `CONFIRMED` |
| RX 580 / GPU | irrelevante — não usa inferência local |
| Electron/Vue | nenhuma relação |
| Python | compatível (stdlib + scripts) |
| Skill format | `SKILL.md` com frontmatter — **mesmo formato** das 50 Skills da Lia `CONFIRMED` |
| Licença CC BY 4.0 no conteúdo | exige atribuição; incompatível com embutir sem crédito |
| Segurança | conteúdo ofensivo: **incompatível** com o runtime de produto |

## 13. Projetos beneficiados

| Projeto | Como (por mecanismo, não por conteúdo) |
|---|---|
| **Lia Agent Hub** | eval de Skill com ablação; manifesto de plugin com `userConfig.sensitive`; instalador multi-harness com posse e `--uninstall`; `skill-lint` + índice com drift |
| **Lia-Project** | `leak-guard` (denylist hasheada, fail-closed) para o repo público; `evidence-hygiene` para auditorias de segurança |
| **Lia Studio** | `check_doc_counts` + `skill-lint` no CI; disciplina de catálogo |
| **Lia Forge** | padrão de eval com oráculo auto-avaliado para pipeline de asset (equivalente ao benchmark que falta) |
| **Lia Model Lab** | harness de avaliação com condição de controle — o desenho que falta em `LR-MODEL-004` (44 catalogados, 0 validados) |
| **Lia-Research** | denylist hasheada + falha fechada no `tools/validate.py`; `doc-count-check` para as contagens do `README`/`ECOSYSTEM-MAP` |
| **Política compartilhada** | modelo de licença dupla com fronteira por tipo de arquivo (`LR-LIC-001`) |

## 14. Oportunidades de reutilização (as seis que valem)

| # | Mecanismo | O que copiar | Onde aplica | Custo |
|---|---|---|---|---|
| R1 | **Eval com ablação** | mesma tarefa/agente/oráculo, com e sem Skill; publicar delta mesmo se 0; conjunto de falsos positivos (`fp_cases.json`) | Agent Hub, Model Lab, Forge | médio (exige oráculo) |
| R2 | **Denylist hasheada fail-closed** | shingles de 1–2 palavras hasheados; denylist nunca em texto claro; `exit 2` se faltar; modo `--staged` | Lia-Research + 5 repos públicos | baixo |
| R3 | **`doc-count-check`** | contagem de Skills/comandos verificada contra o disco no CI | Lia-Research, Studio, Hub | baixo |
| R4 | **`skill-lint` + auto-checagem de roteamento** | Skill nova sem mapeamento quebra o build; índice gerado com `--check` | Agent Hub | baixo |
| R5 | **Licença dupla por tipo de arquivo** | MIT para código, CC BY 4.0 (ou outra) para conteúdo, `NOTICE` + `credits.md` com contagem por origem | `DR-0001`, `LR-LIC-001`, `LR-LIC-003` | baixo |
| R6 | **Manifesto de plugin** | versão semver + autor + **licença por classe** + `userConfig` com `sensitive: true` + `mcpServers` com `env` — sem auto-instalar servidor | `LR-AGENT-009`, `LR-MCP-002` | baixo |

Bônus (R7): **pipeline de citação com teste de identidade** (`research/reports/` +
`test_citation_identity.py`) — o repo afirma "433 padrões individualmente citados e
auditáveis" e testa isso. A Lia-Research cita manualmente; este é o desenho automatizável.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Nota |
|---|---|---|
| Instalar bundle ofensivo no runtime do produto | **alta** | capacidade sem uso de produto; risco legal e de reputação |
| Acionar recusa/fallback de modelo em fluxos normais | média | documentado pelo próprio repo (`INFERRED`) |
| Atribuição CC BY 4.0 não cumprida em conteúdo embutido | média | obriga crédito e link |
| `NOTICE` × `credits.md` divergentes | baixa | ambiguidade de escopo de redistribuição |
| `plugin.json` subdeclara licença (MIT só) | baixa | consumidor de marketplace é mal informado |
| Payloads/wordlists em contexto de agente | média | conteúdo tóxico para uso indevido; dependem de gate humano |
| Cópia de scripts sem adaptação | baixa | `scan_identifiers.py` assume layout `scripts/` do repo |

## 16. Evidências e fontes

| # | Evidência | Rótulo | Fonte | Data |
|---|---|---|---|---|
| E1 | Repo ativo, MIT + CC BY 4.0 dupla, 11.020★ | CONFIRMED | API + `LICENSE` + `LICENSE-CONTENT` | 2026-11-17 |
| E2 | 83 `SKILL.md`, 15 comandos, 341 arquivos | CONFIRMED | Trees API | 2026-11-17 |
| E3 | 58 `hunt-*`; 24 classes originais | CONFIRMED | árvore + `docs/credits.md` | 2026-11-17 |
| E4 | Manifesto de plugin com `userConfig.sensitive` e `mcpServers` | CONFIRMED | `.claude-plugin/plugin.json` | 2026-11-17 |
| E5 | Eval com ablação; baseline **delta +0%**, +US$ 0,076, ceiling effect declarado | CONFIRMED | `eval/BASELINE.md` | 2026-11-17 |
| E6 | 8 workflows, incluindo `leak-guard`, `skill-lint`, `doc-count-check`, `eval-harness` | CONFIRMED | `.github/workflows/` | 2026-11-17 |
| E7 | Denylist hasheada, fail-closed (`exit 2`), `--staged`, self-test do scanner | CONFIRMED | `scripts/scan_identifiers.py` | 2026-11-17 |
| E8 | 55 originais + 20 comunidade + 8 vendorizadas; 12/15 comandos vendorizados | CONFIRMED | `docs/credits.md` | 2026-11-17 |
| E9 | `NOTICE` afirma não redistribuir; `credits.md` afirma vendorizar | CONFIRMED (contradição) | `NOTICE` × `credits.md` | 2026-11-17 |
| E10 | `plugin.json` declara só `MIT` | CONFIRMED | `plugin.json` | 2026-11-17 |
| E11 | Safeguards/fallback de modelo documentados pelo autor | REPORTED | README "Authorization" | 2026-11-17 |
| E12 | Eficácia das Skills em alvo não memorizado | **UNVERIFIED** | eval v1 semi-bloqueado | 2026-11-17 |
| E13 | Qualidade dos payloads/wordlists | **UNVERIFIED** | não executado, não avaliado | 2026-11-17 |
| E14 | Conformidade legal de uso ofensivo por terceiros | **BLOCKED** | fora do escopo desta base | 2026-11-17 |

## 17. Recomendação

**VEREDITO: `REFERÊNCIA`.**

Não instalar, não embutir, não distribuir. O bundle é excelente no que faz e irrelevante
para o produto da Lia — nenhum dos cinco projetos precisa de capacidade ofensiva.

O que **deve** ser adaptado são seis mecanismos de engenharia (§14, R1–R6), que resolvem
lacunas já registradas nesta base com nome e número:

- `LR-LIC-001`/`LR-LIC-003` (0 de 48 payloads com licença) → **R5**;
- `LR-AGENT-009` V6 (nenhuma Skill provada) → **R1**;
- `LIA-RESEARCH` contagens divergentes → **R3**;
- exposição pública encontrada à mão → **R2**;
- catálogo de Skill do Hub sem gate → **R4**;
- proposta de manifesto sem precedente real → **R6**.

Sobre "vai servir para todos": **serve a todos como padrão de higiene, a nenhum como
conteúdo.** É a distinção que separa aproveitar engenharia de importar risco.

## 18. Próximos passos

| # | Ação | Dono | Gate |
|---|---|---|---|
| 1 | Adaptar **R2** (denylist hasheada fail-closed) para `tools/validate.py` desta base | Lia-Research | nenhum |
| 2 | Adaptar **R3** (`doc-count-check`) para contagens de README/ECOSYSTEM-MAP | Lia-Research | nenhum |
| 3 | Propor **R1** (eval com ablação) ao Agent Hub como pré-requisito de `publish` de Skill | Agent Hub | `DR-0020` |
| 4 | Usar **R5** como insumo de `DR-0001` (licença por tipo de arquivo) | proprietário | `DR-0001` |
| 5 | Incorporar **R6** ao schema de `LR-AGENT-009` (licença por classe + `sensitive`) | Agent Hub | `DR-0020` |
| 6 | Avaliar **R7** (pipeline de citação) para `SOURCE-PRESERVATION-POLICY` | Lia-Research | `L-5` |
| 7 | Revisar em 2027-02-17 (repo ativo: pode mudar de versão) | Lia-Research | — |
