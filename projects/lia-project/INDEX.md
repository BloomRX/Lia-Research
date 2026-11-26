# Índice — Lia-Project

Pesquisa consolidada deste projeto. Cada linha aponta para o **relatório principal**;
quando o relatório vive em `repositories/` ou `cross-project/`, o ponteiro está indicado.

---


> **Reauditoria de 2026-11-20.** Todo relatório externo listado aqui foi reavaliado
> nesta data (versão anterior, versão atual, mudanças, testes e conclusão). O detalhe
> está na seção `Reauditoria 2026-11-20` de cada `repositories/*/REPORT.md`;
> resumo por objeto em `audits/REAUDIT-2026-11-20.md`.

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem no projeto |
|---|---|---|---|
| `LR-LIC-005` | Licenças prontas para cada dependência de terceiro (sem reabrir relatório) | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 18 relatórios |
| `LR-SEC-007` | Checklist de auditoria com classe **desktop/IPC** e achado validado por schema | `repositories/cloudflare-security-audit-skill/REPORT.md` | pesquisa externa (novo) |
| `LR-MODEL-001` | Catálogo de modelos, providers e runtimes | `cross-project/model-routing/MODEL-CATALOG-DIGEST.md` | `docs/research/LIA-MODEL-PROVIDER-CATALOG.md` |
| `LR-MODEL-002` | Arquitetura neutra de providers | `cross-project/model-routing/PROVIDER-ARCHITECTURE-DIGEST.md` | `docs/research/LIA-MODEL-PROVIDER-ARCHITECTURE.md` |
| `LR-HW-001` | Windows 11 + AMD RX 580 | `cross-project/hardware/WINDOWS-AMD-COMPATIBILITY.md` | `docs/research/LIA-WINDOWS-AMD-MODEL-COMPATIBILITY.md` |
| `LR-MODEL-003` | LFM3 (avaliação) | `cross-project/ai-models/LFM3-EVALUATION.md` | `docs/research/LIA-LFM3-EVALUATION.md` + Model-Lab `docs/17-LFM3-RESEARCH.md` |
| `LR-HW-002` | Recursos em desktop sempre ativo | `cross-project/hardware/RUNTIME-RESOURCE-RESEARCH.md` | `docs/research/2026-11-14-runtime-resource-research.md` |
| `LR-MODEL-004` | Catálogo de capacidades (44 registros, 0 validados) | `cross-project/ai-models/CAPABILITY-CATALOG-DIGEST.md` | `docs/research/lia-capability-catalog/` |
| `LR-SEC-001` | Credenciais e fronteira de confiança | `cross-project/security/CREDENTIAL-AUDIT-DIGEST.md` | `docs/architecture/LIA-CREDENTIAL-OWNER.md`, `LIA-BETA-CREDENTIAL-AUDIT-2026-11-08.md` |
| `LR-VOICE-001` | Voz PT-BR (STT/TTS/transcrição nativa) | `cross-project/voice/VOICE-STACK-DIGEST.md` | `docs/product/M1-*`, `LIA-NATIVE-TRANSCRIPTION.md`, `LIA-NATIVE-SPEECH-PREVIEW.md` |
| `LR-UI-001` | Componentes de UI (Vercel UI SDK) | `repositories/vercel-ui/REPORT.md` | pesquisa externa (novo) |
| `LR-MCP-001` | Automação residencial (HA-MCP) | `repositories/ha-mcp/REPORT.md` | pesquisa externa (novo) |
| `LR-AGENT-001` | Padrões de agente local (OpenJarvis) | `repositories/openjarvis/REPORT.md` | pesquisa externa (novo) |

## 2. Pesquisa existente que permanece **apenas na origem** (não consolidada)

Documentos de alto valor que este repositório referencia mas não reproduz:

| Documento | Bytes | Branch | Por que não foi copiado |
|---|---:|---|---|
| `docs/reports/LIA-DESKTOP-ARCHITECTURE-AUDIT-2026-11-16.md` | 66 KB | `arena/7fa837f0` | auditoria específica de código; muda com o código |
| `docs/reports/LIA-UI-UX-AUDIT-2026-11-14.md` | 49 KB | sessão | idem |
| `docs/reports/LIA-VALIDATION-MATRIX-5EC464E-2026-11-14.md` | 55 KB | sessão | matriz de SHA específico |
| `docs/architecture/LIA-NATIVE-PROVIDER-COVERAGE.md` | 100 KB | sessão | dados por provider, vence rápido |
| `docs/architecture/LIA-STAGE-DEPENDENCY-MAP-2026-10-28.md` | 77 KB | sessão | mapa de dependência de código |
| `docs/architecture/LIA-NEXT-DECOUPLING-PLAN.md` | 51 KB | sessão | plano de execução do projeto |
| `docs/reports/LIA-GLOBAL-BRANCH-RECONCILIATION-2026-11-16.md` | 27 KB | sessão | estado de branches, vence rápido |
| `docs/reports/LIA-BETA-READINESS-PLAN-2026-11-14.md` | 54 KB | sessão | plano |
| `docs/architecture/decisions/DECISION-RECORD-2026-11-16.md` | 23 KB | sessão | decisão do projeto (é do projeto, não da base) |
| `docs/reports/LIA-STT-SECURITY-AUDIT-2026-11-14.md` | 17 KB | sessão | resumido em `LR-SEC-001` |

Regra aplicada: relatório que descreve **estado de código** pertence ao projeto; o
Lia-Research registra a conclusão durável e o ponteiro.

## 3. Skills do projeto (22)

| Skill | Função | Licença no payload | Observação |
|---|---|---|---|
| `lia-agent-evaluation` | avaliação de agente | ❌ ausente | |
| `lia-agent-orchestration` | orquestração | ❌ | sobrepõe `multi-agent-orchestration` (Model-Lab) |
| `lia-ai-sdk-integration` | integração AI SDK | ❌ | |
| `lia-browser-automation` | automação de navegador | ❌ | risco de egress; o padrão que resolve metade do problema está auditado em `LR-FORGE-014` §4 (lista local + cache de veredito de 6 h + payload cortado em 140 caracteres, sem ler conteúdo nem teclas) |
| `lia-electron-cdp-debugging` | depuração CDP | ❌ | |
| `lia-eventa-ipc` | IPC | ❌ | |
| `lia-pnpm-workspaces` | monorepo | ❌ | |
| `lia-regression-investigation` | investigação de regressão | ❌ | |
| `lia-release-gate` | gate de release | ❌ | candidato a ter manifesto de workflow |
| `lia-safe-change` | mudança segura | ❌ | |
| `lia-security-review` | revisão de segurança | ❌ | desenho mínimo de fila de triagem medido em `LR-SEC-009` (Chatwoot: 211 linhas de Python, `state=triage` → issue com prioridade por severidade) e inventário leve em `LR-FORGE-016` §5 (`opf/recense`: Syft + Grype sem servidor, MIT) |
| `lia-test-discipline` | disciplina de teste | ❌ | |
| `lia-ui-quality-review` | qualidade de UI | ❌ | poderia usar molde de `ai-design-skills` |
| `lia-unocss-ui` | estilo | ❌ | |
| `lia-visual-evidence` | evidência visual | ❌ | |
| `lia-voice-diagnostics` | diagnóstico de voz | ❌ | |
| `lia-vue-development` | Vue | ❌ | |
| `lia-vue-testing` | teste Vue | ❌ | |
| `lia-windows-electron-validation` | validação Windows | ❌ | |
| `stage-runtime-debugging` | runtime do Stage | ❌ | |
| `airi-upstream-integration` | integração AIRI | ❌ | |
| `alethe` | orquestração (terceiro vendorizado) | ✅ próprio | `FORK_CANDIDATE`; requer auditoria de patches |

Fonte: `LIA-SKILLS-INVENTORY.md` (`Lia-AgentHub@bd4bfbb`, 2026-11-15), verificada
contra a árvore do Lia-Project em 2026-11-17.

## 4. Lacunas declaradas

| Lacuna | Situação |
|---|---|
| Nenhuma Skill com licença no payload | 22/22 sem licença → bloqueia distribuição |
| Nenhum modelo do catálogo validado | 44 catalogados, 0 medidos |
| Duas pesquisas de provider concorrentes | consolidação exige decisão de produto |
| `main` sem a pesquisa de novembro | 511 documentos fora de `main` |

---

## 5. Conferência de ponteiros — 2026-11-26

Medição desta sessão (`gh api` na `main`; ver `audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md` §2.1).
Os dossiês e tabelas acima ficam como registro datado de 2026-11-17; só o que segue vale hoje.

| Afirmação anterior | Estado hoje |
|---|---|
| "Branches `arena/*` permanecem como registro histórico; o conteúdo citado nelas **não foi integrado à `main`**" | **superada** — restou **1** branch (`main`); `005a324` foi consolidada. `main` @ `72c44425` com **833 commits** |
| `docs/research/LIA-WINDOWS-AMD-MODEL-COMPATIBILITY.md`, `LIA-LFM3-EVALUATION.md`, `2026-11-14-runtime-resource-research.md`, `LIA-ORNITH-WEIGHTS-RESEARCH.md` permanecem na origem | **ENTREGA CONCLUÍDA** — os quatro estão na `main`, e o próprio `docs/reports/LIA-RESEARCH-TRANSFER-RECONCILIATION.md` (10.452 B, lido) os classifica `Research reference`, cópia byte a byte, "nenhum documento classificado como Canonical nesta rodada" |
| "`LIA-NATIVE-PROVIDER-COVERAGE.md`, `LIA-STAGE-DEPENDENCY-MAP-2026-10-28.md`, `LIA-NEXT-DECOUPLING-PLAN.md`, `LIA-DESKTOP-ARCHITECTURE-AUDIT-2026-11-16.md`, `LIA-UI-UX-AUDIT-2026-11-14.md`, `LIA-BETA-READINESS-PLAN-2026-11-14.md`, `LIA-GLOBAL-BRANCH-RECONCILIATION-2026-11-16.md`, `DECISION-RECORD-2026-11-16.md`, `LIA-STT-SECURITY-AUDIT-2026-11-14.md` permanecem apenas na origem" | **ENTREGA CONCLUÍDA** para os nove — todos na `main`, alguns maiores do que registramos (70,5 KB / 101,9 KB). O §4 deles como "leitura pendente" permanece válido: ainda não os lemos |
| gap "511 documentos fora de `main`" | **resolvido com uma exceção**: das linhas de §2 que a base citava, só `docs/reports/LIA-VALIDATION-MATRIX-5EC464E-2026-11-14.md` **não** está na `main` (busca na árvore: ausente) |
| gap "Nenhuma Skill com licença no payload" | **refinado**: 21 `SKILL.md` na `main`, **1** com `LICENSE` (`alethe/LICENSE`, 1.069 B). restam 20 sem. O bloqueio de distribuição continua, com base menor |
| `lia/core/src/memory/{contracts,store,context}.ts` + `lia/core/test/memory-store.test.ts` | presentes na `main` (1.355 / 8.791 / 2.132 / 6.811 B) e **lidos como código nesta sessão**; nenhum teste foi executado por nós → a comparação com fornecedores está em `LR-CMP-006` §2, §7 |

Novo pointer que faltava: `MODEL-CATALOG-DIGEST`/`PROVIDER-ARCHITECTURE-DIGEST`/`PROVIDER-RECOMMENDATIONS-DIGEST`
têm hoje equivalentes na `main` (`docs/research/LIA-MODEL-PROVIDER-{CATALOG,ARCHITECTURE,RECOMMENDATIONS}.md`)
classificados pelo Project como **`Pending transfer`** — ou seja, o catálogo canônico continua
`lia-capability-catalog/` e a nossa pesquisa entra como insumo a reconciliar, não como substituta.
