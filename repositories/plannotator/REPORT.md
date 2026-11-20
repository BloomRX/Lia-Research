# Plannotator — workspace de anotação e revisão de planos de agente

| Campo | Valor |
|---|---|
| ID | `LR-UI-002` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | ui |
| Projetos beneficiados | Lia-Project, Lia Agent Hub |
| Fontes | `backnotprop/plannotator@b5b3077838a1758960198dc404ee98e2a57acf6d:README.md`, tree, `LICENSE`, releases |
| Versão/commit | `b5b3077` (2026-11-17), release `v0.28.67` (2026-11-17) |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `backnotprop/plannotator` · HEAD `589d4230a6d2` · mudou desde a análise (conteúdo novo não lido) |
| Próxima revisão | 2027-02-17 |
| Recomendação | **REFERENCE_ONLY** (avaliar como ponte de revisão humana; não adotar agora) |
| Licença | Apache-2.0 (`CONFIRMED`) |
| Confiança | Alta para estrutura/licença; Média para integrações |

---

## 1. Identificação

- **Nome:** Plannotator
- **URL:** https://github.com/backnotprop/plannotator · site plannotator.ai
- **Autor:** `backnotprop`
- **Licença:** Apache-2.0 (`CONFIRMED`)
- **Commit:** `b5b3077` (2026-11-17T14:46:54Z) · release `v0.28.67`
- **Métricas:** ★**12.935** · 1.298 forks · **192 issues** · criado 2025-12-28 · **7.080 arquivos** · 5.084 em `packages/` · 1.139 em `apps/` · 691 em `tests/` · **63 em `adr/`** · 14 workflows · 281 `.md` · 64 `.yaml`

## 2. Resumo executivo

Plannotator é o "lugar onde o humano fica no loop": anota planos, specs, markdown e
artefatos HTML de agentes, revisa diffs e PRs, e devolve o feedback ao agente com um
clique. Integra com Claude Code, Codex, Copilot, Amp, opencode e pi-mono. Tem ainda
integração com Obsidian (tópico).

O padrão que interessa à Lia é o **contrato de revisão**: o agente produz um artefato
(plano/spec/diff), o humano anota em uma superfície dedicada, e o feedback volta
estruturado — não como "achei bom". É exatamente o que falta no fluxo Lia hoje, em que
relatórios são revisados em texto corrido e decisões viram mensagens soltas.

Contra: 192 issues abertas, projeto pré-1.0 (`v0.28.x`, release quase diária) e
superfície de aplicação grande. É referência, não dependência.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Feedback de agente em texto corrido se perde | superfície de anotação dedicada |
| Revisão de plano acontece depois do código | revisão na fase de plano ("plan mode") |
| Revisão de diff/PR fragmentada | code review integrado |
| Feedback não estruturado | retorno ao agente com um clique |
| Contexto espalhado | "Inbox Surface" unificada |

## 4. Arquitetura

```text
packages/ (5.084)   bibliotecas compartilhadas (TS)
apps/ (1.139)       aplicações (web/desktop/CLI)
tests/ (691)        suíte ampla
adr/ (63)           ★ 63 ADRs versionados
spec/ (6)           especificações
.product/ (21)      docs de produto
.agents/ (6)        configuração de agentes
.github/ (45)       CI, templates
```

Destaque: **63 ADRs** em um projeto de 11 meses. É a prática de registro de decisão
mais consistente entre os 16 repositórios pesquisados — e o Lia-Research prega isso
com um diretório `decisions/` ainda quase vazio. Vale copiar o hábito.

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Anotação de planos/specs/markdown/HTML | estável (0.28.x) | `REPORTED` README |
| Code review de diffs/PRs | estável | `REPORTED` |
| Envio de feedback ao agente em 1 clique | estável | `REPORTED` |
| Integração Claude Code / Codex / Copilot / Amp / opencode / pi-mono | existe | `CONFIRMED` (ícones e descrição) |
| Integração Obsidian | existe | `CONFIRMED` (topic) |
| ADRs versionados | prática | `CONFIRMED` (63 arquivos) |
| API/CLI pública | `UNVERIFIED` | não lida a fundo |

## 6. Dependências

- TypeScript/Node; monorepo com packages internos.
- Integração via CLIs de agentes de terceiros (acoplamento a formatos deles).
- Algumas integrações exigem serviços externos (ex.: repositório Git remoto) — `INFERRED`.

## 7. Requisitos de hardware e sistema

- Web/desktop/CLI; provavelmente Windows/macOS/Linux (`UNVERIFIED` para Windows).
- Sem requisito de GPU.

## 8. Segurança e privacidade

| Item | Rótulo | Nota |
|---|---|---|
| Conteúdo de planos/diffs trafega para agentes | `OBSERVED` | planos podem conter dados sensíveis |
| Integração com múltiplas CLIs | `CONFIRMED` | cada integração é uma superfície |
| Servidor local? | `UNVERIFIED` | verificar bind antes de uso |
| Telemetria | não identificada | `UNVERIFIED` |

## 9. Licença e proveniência

- **Apache-2.0** (`CONFIRMED`). Obrigações: aviso, texto, NOTICE, indicar alterações.
- Classe: `ADAPT_ALLOWED` (código) / `INDEPENDENT_REIMPLEMENTATION` (padrão de revisão).
- Marca: nomes das integrações (Claude, Codex, Copilot) são marcas de terceiros.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~11 meses | razoável |
| Versão | 0.28.67, releases quase diárias | **muito volátil** |
| Issues | 192 | alto |
| Testes | 691 arquivos | sério |
| CI | 14 workflows | forte |
| ADRs | 63 | excelente prática |

## 11. Custos e limitações

- Gratuito. Custo de integração: médio-alto (é uma aplicação, não uma lib).
- Limitação: velocidade de release indica API instável; acoplamento a formatos de
  agentes de terceiros.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 | `UNVERIFIED` | não declarado explicitamente na leitura |
| Electron/Vue | não é a stack | TS genérico |
| Integração com os agentes usados pela Lia | sim | Claude Code/Codex são usados no ecossistema |
| Uso como ferramenta interna de revisão | sim | cenário mais realista |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Agent Hub | padrão de revisão humana estruturada |
| Lia-Project | possível ferramenta interna para revisar planos de sessão |

## 14. Oportunidades de reutilização

1. **Contrato de revisão**: artefato → anotação → feedback estruturado → agente.
2. **`adr/` com 63 decisões**: prova de que registrar decisão é viável em ritmo alto.
3. **Revisão na fase de plano** (antes do código): reduz retrabalho — princípio que o
   Lia-Research aplica a si mesmo com `REVIEW-PROTOCOL.md`.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Adotar app pré-1.0 com release diário | média | usar como ferramenta, não dependência |
| Conteúdo sensível em planos revisados | média | política de dados antes de uso |
| Windows não verificado | baixa | testar antes |
| Acoplamento a formatos de terceiros | baixa | — |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | Apache-2.0 | CONFIRMED | `@b5b3077:LICENSE` | 2026-11-17 |
| E2 | 63 ADRs versionados | CONFIRMED | tree `adr/` | 2026-11-17 |
| E3 | Integrações com Claude Code/Codex/Copilot/Amp/opencode/pi-mono | CONFIRMED | README + assets | 2026-11-17 |
| E4 | 192 issues, v0.28.67 | CONFIRMED | API + releases | 2026-11-17 |
| E5 | Suporte Windows | UNVERIFIED | não confirmado | — |

## 17. Recomendação

**`REFERENCE_ONLY`** — o valor está no padrão de revisão e no hábito de ADR; a ferramenta
em si é opcional e instável.

**Não autoriza:** integrar ao produto, depender do app, ou redirecionar conteúdo
sensível de planos para ele sem política.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Propor "contrato de revisão" no fluxo de pesquisa (artefato → anotação → decisão) | Research | spec |
| 2 | Popular `decisions/` do Lia-Research (hoje com poucos registros) | Research | ≥ 10 DRs |
| 3 | Testar como ferramenta interna de revisão de planos | proprietário | decisão de uso |
