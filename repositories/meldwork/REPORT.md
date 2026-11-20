# Meldwork — workspace local-first de colaboração entre agentes

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-003` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | agents |
| Projetos beneficiados | Lia Agent Hub |
| Fontes | `Ryder-Sun/Meldwork@db9b6c84cbb1c86f3e3facf3cbebdcd6f1f79397:README.md`, `COMMERCIAL_USE.md`, `LICENSE`, tree, releases |
| Versão/commit | `db9b6c8` (2026-11-16), release `Meldwork-V1.0.9` (Preview) |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `Ryder-Sun/Meldwork` · HEAD `db9b6c84cbb1` · sem mudança no HEAD |
| Próxima revisão | 2027-02-17 |
| Recomendação | **REFERENCE_ONLY** |
| Licença | Apache-2.0 + declaração explícita de uso comercial permitido |
| Confiança | Alta para licença/estrutura; Média para capacidades |

---

## 1. Identificação

- **Nome:** Meldwork
- **URL:** https://github.com/Ryder-Sun/Meldwork · site ryder-sun.github.io/Meldwork
- **Autor:** `Ryder-Sun`
- **Licença:** Apache-2.0, com `COMMERCIAL_USE.md` afirmando que uso comercial é
  permitido sem taxa adicional — `CONFIRMED` (texto lido: EN + 中文)
- **Commit:** `db9b6c8` (2026-11-16T05:27:11Z) · release `V1.0.9 Preview`
- **Métricas:** ★1.586 · 109 forks · **8 issues** · criado 2026-07-29 · 658 arquivos · 379 em `desktop/` · 204 em `frontend/` (26 `.vue`) · 235 arquivos de teste · 1 workflow

## 2. Resumo executivo

Meldwork é um workspace desktop **local-first** onde agentes que o usuário já usa
(Claude, Codex, etc.) são reunidos num "working group" com objetivo, contexto e
permissões definidas, discutindo em rodadas automáticas e entregando trabalho com
verificação cruzada. O vocabulário do produto — *scoped permissions*,
*evidence-aware runs*, *human-in-the-loop decisions* — descreve quase exatamente a
fronteira que o Lia Agent Hub precisa definir.

Três observações práticas: (1) o README fala em "Agent tools you already use on your
Mac" — o produto é **macOS-only**, o que o desqualifica como caminho principal no
ecossistema Windows da Lia; (2) a licença é limpa e explicitamente comercial;
(3) a arquitetura (Electron + Vue no frontend, 26 `.vue`) é a **mesma stack da Lia**,
o que torna o código um comparável direto — inclusive para avaliar decisões de UX de
orquestração multi-agente.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Vários agentes, contexto fragmentado | workspace único com contexto compartilhado |
| Agente faz o que quer | permissões com escopo por rodada |
| Resultado sem prova | "evidence-aware runs" (execuções com evidência) |
| Decisão humana ausente | *human-in-the-loop* explícito |
| Auditoria de quem fez o quê | histórico de rodadas e checkpoints |

## 4. Arquitetura

```text
desktop/ (379)      shell Electron + serviços locais (.cjs majoritário)
frontend/ (204)     UI Vue (26 .vue) + CSS
meldwork-landing/   site
assets/             imagens/logos
AGENTS.md           instruções para agentes
CATALOG.md          catálogo (de skills/agentes?)
COMMERCIAL_USE.md   declaração de licença comercial
tests (235)         frontend + desktop + ACP
```

O commit analisado menciona explicitamente "ACP crash-recovery tests", "deterministic
evaluations (6 cases, 18 results)", "desktop pack and signature verification" — ou
seja, há **avaliação determinística ética** no projeto (`CONFIRMED` pela mensagem de
commit, `REPORTED` quanto ao conteúdo).

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Workspace multi-agente local-first | 1.0.9 preview | `REPORTED` + releases |
| Permissões com escopo | estável | `REPORTED` |
| Rodadas automáticas de discussão | estável | `REPORTED` |
| Human-in-the-loop | estável | `REPORTED` |
| Evidência por execução | estável | `REPORTED` |
| Supervisão de crash (ACP) | em teste | `CONFIRMED` (commit message) |
| Windows | **não suportado** | `REPORTED` (README: "on your Mac") |

## 6. Dependências

- Electron + Node (desktop), Vue (frontend).
- Integração com CLIs de agentes externos (Claude/Codex) — o usuário precisa tê-los.
- Nenhum serviço de nuvem obrigatório (local-first declarado).

## 7. Requisitos de hardware e sistema

- **macOS** (README). Windows/Linux não anunciados.
- Consumo: não medido (`UNVERIFIED`); workspace multi-agente com vários processos
  tende a ser pesado para 16 GB (`INFERRED`).

## 8. Segurança e privacidade

| Item | Rótulo | Nota |
|---|---|---|
| Permissões com escopo por agente | `REPORTED` | modelo interessante a estudar |
| Agentes recebem contexto compartilhado | `REPORTED` | risco de vazamento entre agentes |
| Local-first (sem nuvem obrigatória) | `REPORTED` | bom para privacidade |
| Assinatura de pacote desktop | `CONFIRMED` (commit) | prática de distribuição sólida |
| Telemetria | não identificada | `UNVERIFIED` |

## 9. Licença e proveniência

- **Apache-2.0** (`CONFIRMED`) com `COMMERCIAL_USE.md` explícito: uso comercial,
  privado, modificação e redistribuição permitidos, sem taxa; obrigações de preservar
  licença/copyright/NOTICE e indicar arquivos modificados; Apache-2.0 §6 não concede
  marca.
- Terceiros mantêm suas licenças (fontes OFL, nomes/logos de agentes).
- Classe: `ADAPT_ALLOWED` (código) / `INDEPENDENT_REIMPLEMENTATION` (padrões).
- **Modelo de documentação de licença:** um arquivo dedicado respondendo à pergunta
  que todo usuário comercial tem ("posso usar comercialmente?") é uma prática que o
  Lia-Research deveria adotar no `LICENSE`.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~4 meses | jovem, mas com 1.0.x |
| Releases | V1.0.8, V1.0.9 Preview | cadência semanal |
| Issues | **8** para 1.586 estrelas | triagem muito ativa |
| Testes | 235 arquivos | bom |
| CI | 1 workflow | mínimo |
| Documentação | `architecture.md`, `AGENTS.md`, `CATALOG.md` | boa |

## 11. Custos e limitações

- Gratuito, comercial permitido.
- Limitação crítica para a Lia: **macOS-only**.
- Limitação secundária: depende de CLIs de agentes de terceiros instalados.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 | **não** | macOS no README |
| Electron + Vue | **sim** (mesma stack) | comparável direto |
| Local-first | sim | alinhado |
| Permissões multi-agente | sim (modelo) | inspiração para o Hub |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Agent Hub | modelo de permissões com escopo, evidência por execução, HITL |
| Lia-Project | referência de UX de orquestração em Electron/Vue |

## 14. Oportunidades de reutilização

1. **`COMMERCIAL_USE.md`** como padrão de clareza jurídica (copiar o hábito).
2. **Permissões com escopo por rodada** — modelo que o Hub precisa e ainda não tem.
3. **"Evidence-aware runs"** — cada execução registra o que a sustenta; é o mesmo
   princípio de `EVIDENCE-STANDARDS.md` aplicado a execução de agente.
4. **Assinatura e verificação de pacote** no pipeline de release.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| macOS-only | média (bloqueia adoção) | referência apenas |
| Contexto compartilhado entre agentes | média | isolamento por agente se replicar |
| Dependência de CLIs de terceiros | média | — |
| Projeto jovem | baixa | não depender |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | Apache-2.0 | CONFIRMED | `@db9b6c8:LICENSE` | 2026-11-17 |
| E2 | Uso comercial permitido sem taxa | CONFIRMED | `COMMERCIAL_USE.md` | 2026-11-17 |
| E3 | macOS-only | REPORTED | `README.md` ("on your Mac") | 2026-11-17 |
| E4 | Vue + Electron, 26 `.vue` | CONFIRMED | tree | 2026-11-17 |
| E5 | Testes de recuperação ACP e avaliações determinísticas | CONFIRMED (existência) / REPORTED (resultado) | mensagem do commit `db9b6c8` | 2026-11-17 |
| E6 | Consumo de recursos | UNVERIFIED | não executado | — |

## 17. Recomendação

**`REFERENCE_ONLY`** — estudar o modelo de permissões, evidência e HITL; não adotar por
indisponibilidade de plataforma.

**Não autoriza:** portar código para o produto, assumir suporte Windows, ou
redistribuir o app.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Extrair o modelo de "permissão com escopo" como spec para o Hub | Agent Hub | spec comparável |
| 2 | Adotar `COMMERCIAL_USE.md` no Lia-Research e nas Skills Lia | Research | arquivo criado |
| 3 | Verificar se há build Windows em issues/PRs | Research | `CONFIRMED`/`BLOCKED` |
| 4 | Revisar em 90 dias | Research | — |
