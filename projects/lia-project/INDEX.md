# Índice — Lia-Project

Pesquisa consolidada deste projeto. Cada linha aponta para o **relatório principal**;
quando o relatório vive em `repositories/` ou `cross-project/`, o ponteiro está indicado.

---

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem no projeto |
|---|---|---|---|
| `LR-LIC-005` | Licenças prontas para cada dependência de terceiro (sem reabrir relatório) | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 18 relatórios |
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
| `lia-browser-automation` | automação de navegador | ❌ | risco de egress |
| `lia-electron-cdp-debugging` | depuração CDP | ❌ | |
| `lia-eventa-ipc` | IPC | ❌ | |
| `lia-pnpm-workspaces` | monorepo | ❌ | |
| `lia-regression-investigation` | investigação de regressão | ❌ | |
| `lia-release-gate` | gate de release | ❌ | candidato a ter manifesto de workflow |
| `lia-safe-change` | mudança segura | ❌ | |
| `lia-security-review` | revisão de segurança | ❌ | |
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
