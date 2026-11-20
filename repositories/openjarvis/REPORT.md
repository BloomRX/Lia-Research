# OpenJarvis — framework de IA pessoal local-first

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-001` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | agents |
| Projetos beneficiados | Lia Agent Hub, Lia-Project, Lia Model Lab |
| Fontes | `open-jarvis/OpenJarvis@6656b7fed28e2ff1efa4e77987cf351f2d71eec0:README.md`, `docs/architecture/overview.md`, `docs/architecture/security.md`, `pyproject.toml`, tree |
| Versão/commit analisado | `6656b7f` (2026-11-17), release `desktop-v1.0.5` (2026-11-11) |
| Data da pesquisa | 2026-11-17 |
| Upstream conferido | 2026-11-20 · `open-jarvis/OpenJarvis` · HEAD `a9e59e8770f9` · mudou desde a análise (conteúdo novo não lido) |
| Próxima revisão | 2027-02-17 |
| Recomendação | **REFERENCE_ONLY** (padrões sim; código não) |
| Licença | Apache-2.0 (`CONFIRMED`) |
| Confiança | **Alta** para arquitetura, licença e dependências; **Baixa** para desempenho/energia (não medido aqui) |

---

## 1. Identificação

- **Nome:** OpenJarvis (`pip install OpenJarvis`; CLI `jarvis`)
- **URL:** https://github.com/open-jarvis/OpenJarvis · site https://openjarvis.stanford.edu/
- **Organização:** `open-jarvis` (origem acadêmica Stanford; paper arXiv 2605.17172)
- **Licença:** Apache-2.0 — `CONFIRMED` no arquivo
- **Commit:** `6656b7f` (2026-11-17T06:11:34Z)
- **Métricas:** ★16.276 · 3.930 forks · 85 issues · criado 2026-02-15 · Python 2.228 arquivos (957 `src`, **752 testes**) · 146 em `rust/` · 141 `frontend/` · 99 `docs/` · 14 workflows de CI
- **Classificação interna do projeto:** `Development Status :: 3 - Alpha` (`CONFIRMED` no `pyproject.toml`)

## 2. Resumo executivo

OpenJarvis é uma pilha de IA pessoal *local-first* construída sobre cinco primitivas
(Intelligence, Engine, Agentic Logic, Memory, Learning) com um argumento central
medido pelo próprio grupo: modelos locais já resolvem 88,7% das consultas de turno
único, e a eficiência de inteligência melhorou 5,3× entre 2023 e 2025 (`REPORTED`,
paper). É a referência mais próxima do que a Lia quer ser — assistente pessoal que
roda na máquina do usuário e só chama a nuvem quando necessário.

Para a Lia, o valor **não** é adotar o framework: é copiar o desenho. Três padrões se
destacam: (a) a separação Intelligence/Engine/Agents que permite trocar runtime sem
tocar em agente; (b) o `InferenceEngine` ABC como contrato único para Ollama, vLLM,
SGLang, llama.cpp e nuvem; (c) `GuardrailsEngine` como **decorator** de engine, que
transforma segurança em camada substituível em vez de código espalhado.

Riscos: é alpha, maduro em pesquisa e imaturo em produto; tem telemetria (`posthog`
como dependência); e o caminho de hardware é GPU/NVIDIA-oriented, o que **não** casa
com a RX 580 do usuário.

## 3. O que resolve

| Problema | Solução no OpenJarvis |
|---|---|
| Cada runtime de modelo tem API diferente | `InferenceEngine` ABC: `generate()`, `stream()`, `list_models()`, `health()` |
| Escolher modelo exige saber VRAM/contexto | catálogo `BUILTIN_MODELS` com params, contexto, VRAM, engines suportados |
| Agente não sabe o que existe | descoberta de modelos em runtime, merge no `ModelRegistry` |
| Segurança é retrabalho por integração | `GuardrailsEngine` envolve qualquer engine |
| Custo/energia invisível | Learning & Traces: energia, FLOPs, latência e dólar como métricas de primeira classe (`REPORTED`) |

## 4. Arquitetura

```text
Intelligence (catálogo de modelo + config)
      │
      ▼
Engine (InferenceEngine ABC): Ollama | vLLM | SGLang | llama.cpp | Cloud
      │  ← GuardrailsEngine (SecretScanner, PIIScanner, WARN/REDACT/BLOCK, AuditLogger SQLite)
      ▼
Agentic Logic: 9 tipos de agente + SandboxedAgent (Docker/Podman, mount security)
      │
      ▼
Memory: SQLite/FTS5 | FAISS | ColBERTv2 | BM25 | Hybrid (RRF)
      │
      ▼
Learning & Traces → melhora roteamento e modelo com dados locais
```

Agentes identificados (`CONFIRMED` em `docs/architecture/overview.md`):
`SimpleAgent`, `OrchestratorAgent`, `NativeReActAgent`, `NativeOpenHandsAgent`,
`RLMAgent`, `OpenHandsAgent`, `ClaudeCodeAgent`, `OperativeAgent`,
`MonitorOperativeAgent`.

Há `rust/crates` com extensão nativa (o instalador baixa "the Rust extension" em
segundo plano) — `CONFIRMED` pela árvore e pelo README.

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Múltiplos engines de inferência | estável | `CONFIRMED` doc/arquitetura |
| Catálogo de 5 backends de memória | estável | `CONFIRMED` |
| 9 tipos de agente, incluindo CodeAct e ReAct | estável (alpha) | `CONFIRMED` |
| Sandbox de agente (Docker/Podman) | estável | `CONFIRMED` |
| Guardrails com PII/secret scanning | estável | `CONFIRMED` |
| Desktop GUI (.exe/.dmg/.deb/.rpm/.AppImage) | release 1.0.5 | `CONFIRMED` release |
| Instalador Windows nativo (PowerShell) | disponível | `CONFIRMED` README |
| Canais (Telegram) | dependência presente | `REPORTED` (`python-telegram-bot`) |
| Leaderboard/evals de energia | existe no projeto | `REPORTED` (link no README) |
| Integração com MCP | não identificado na leitura | `UNVERIFIED` |

## 6. Dependências

| Dependência | Papel | Observação |
|---|---|---|
| `openai` | cliente de API | também usado para endpoints compatíveis |
| `aiohttp`, `httpx`, `requests`, `urllib3` | HTTP | versões com *security floors* declarados |
| `datasets`, `fsspec`, `filelock` | dados | `datasets` puxa numpy/pandas |
| `psutil` | processo/recursos | limpeza de descendentes no Windows |
| `nvidia-ml-py` | métricas de GPU | **NVIDIA-only** |
| `posthog` | **telemetria/analytics** | revisar antes de qualquer adoção |
| `ddgs` | busca web | egress de rede |
| `python-telegram-bot` | canal | bot externo |
| Runtime Rust | extensão nativa | build/download |
| Python | `>=3.11,<3.14` | pin justificado por wheel de numpy |

## 7. Requisitos de hardware e sistema

- macOS, Linux, WSL2 e **Windows nativo** (`CONFIRMED`, README).
- Windows: instalador PowerShell + tarefa agendada; GUI desktop com release `.exe`.
- GPU: `nvidia-ml-py` sugere foco NVIDIA/CUDA. **Nenhuma evidência de suporte a
  Vulkan/AMD gfx803** nesta pesquisa → no hardware do usuário (RX 580), o caminho
  realista é CPU ou Ollama com backends suportados, sem a camada de medição de energia.
- RAM: 16 GB é o mínimo prático para modelos pequenos quantizados; não há requisito
  declarado no README → `UNVERIFIED`.
- Consumo real: **não medido** (`BLOCKED`: exigiria instalar e executar).

## 8. Segurança e privacidade

**Positivo:** segurança como decorator (`GuardrailsEngine`) implementando a mesma ABC
do engine — qualquer backend pode ser protegido sem modificação; três modos de
redação (WARN/REDACT/BLOCK); `AuditLogger` em SQLite; sandbox de agente com
"mount-security enforcement". Desenho exemplar para a Lia copiar como **padrão**.

**Atenção:**

| Item | Rótulo | Implicação |
|---|---|---|
| Dependência `posthog` | `CONFIRMED` | capacidade de analytics/telemetria; política exata não lida à fundo (`UNVERIFIED`) |
| `ddgs` (busca web) | `CONFIRMED` | egress de conteúdo de prompt para terceiro se usado |
| Agente com execução de código (`NativeOpenHandsAgent`) | `CONFIRMED` | superfície de execução local; sandbox é opcional |
| Sandbox depende de Docker/Podman | `CONFIRMED` | sem container, execução roda no host |
| Telegram bot | `CONFIRMED` | canal externo; vazamento de contexto se mal configurado |

Recomendação de leitura obrigatória antes de qualquer uso: `docs/architecture/security.md`
e a política de telemetria. Não foi possível validar o comportamento em runtime.

## 9. Licença e proveniência

- Apache-2.0, `CONFIRMED`. Obrigações: aviso, texto, **NOTICE** se existir, indicar
  alterações. Sem copyleft.
- Classe: `INDEPENDENT_REIMPLEMENTATION` para os **padrões**; `RESEARCH_ONLY` para
  código (não há previsão de fork).
- Marca: "OpenJarvis", "Stanford" não são licenciados pelo Apache-2.0.
- Pesos de modelo usados por ele: licença própria de cada modelo (fora do escopo do
  Apache do framework).

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | 9 meses (criado 2026-02) | jovem |
| Classificação | Alpha | API pode mudar |
| Testes | 752 arquivos | forte para pesquisa |
| CI | 14 workflows | ativo |
| Commits | diários; último inclui bot de tráfego | atividade real + ruído de bot |
| Governança | institucional (Stanford) | menos risco de abandono, mais risco de prioridade acadêmica |
| Issues | 85 abertas para 16k estrelas | proporção aceitável |

## 11. Custos e limitações

- Financeiro: zero (Apache-2.0), mas modelos locais custam hardware.
- Integração: alta — o framework tem opinião forte sobre arquitetura; adotá-lo
  significaria reorganizar a Lia em torno de primitivas dele.
- Limitações: alpha; GPU-oriented; Python pesado; telemetria presente; sem evidência
  de suporte AMD/Windows-Vulkan.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 | sim | instalador nativo `CONFIRMED` |
| AMD RX 580 / Vulkan | **não demonstrado** | `nvidia-ml-py`; sem evidência Vulkan |
| 16 GB RAM | apertado | modelos pequenos apenas |
| Electron/Vue | não é frontend | tem GUI própria (TSX) |
| Não depender de nuvem | sim, por desenho | local-first declarado |
| Offline | sim | exceto canais/busca web |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Model Lab | modelo mental de avaliação (energia/FLOPs/latência/custo) e de catálogo de modelos |
| Lia Agent Hub | padrão de contrato de engine e de registro de agente |
| Lia-Project | padrão de guardrails como camada; desenho de política de memória |

## 14. Oportunidades de reutilização

1. **`InferenceEngine` ABC** com `generate/stream/list_models/health`: contrato mínimo
   que já resolveria a fragmentação de providers observada na Lia.
2. **Guardrails como decorator**: segurança substituível, testável, sem tocar no engine.
3. **Catálogo de modelo com metadados de VRAM/contexto**: base para o catálogo Lia,
   hoje com 44 registros e 0 validados.
4. **Três modos de redação** (WARN/REDACT/BLOCK): política gradual em vez de binária.
5. **Métricas de primeira classe** (energia/FLOPs/latência/dólar): muda a pergunta de
   "qual modelo é melhor" para "melhor por watt e por dólar".

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Adotar o framework e herdar sua arquitetura | alta | usar como referência, não como dependência |
| Telemetria (`posthog`) | média | não adotar sem revisar política |
| Alpha com API instável | média | nenhuma integração de produto |
| GPU NVIDIA-oriented vs AMD do usuário | alta | não prometer desempenho no RX 580 |
| Python 3.14 sem wheel (numpy) | baixa | pin `>=3.11,<3.14` já resolvido no projeto |
| Execução de código por agente | alta | se algum dia usar, sandbox obrigatório |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | Apache-2.0 | CONFIRMED | `@6656b7f:LICENSE` + `pyproject.toml` | 2026-11-17 |
| E2 | 5 primitivas | CONFIRMED | `docs/architecture/overview.md` | 2026-11-17 |
| E3 | Engines Ollama/vLLM/SGLang/llama.cpp/Cloud | CONFIRMED | idem | 2026-11-17 |
| E4 | 9 tipos de agente | CONFIRMED | idem | 2026-11-17 |
| E5 | 5 backends de memória | CONFIRMED | idem | 2026-11-17 |
| E6 | Guardrails como decorator + 3 modos | CONFIRMED | `docs/architecture/security.md` | 2026-11-17 |
| E7 | Instalador Windows nativo | CONFIRMED | `README.md` | 2026-11-17 |
| E8 | 88,7% das consultas locais; 5,3× eficiência | REPORTED | README citando paper arXiv 2605.17172 | 2026-11-17 |
| E9 | Dependência de telemetria | CONFIRMED | `pyproject.toml` (`posthog`) | 2026-11-17 |
| E10 | Suporte AMD/Vulkan | UNVERIFIED | não há evidência; não testado | — |

## 17. Recomendação

**`REFERENCE_ONLY`** — estudar e copiar padrões; não adotar como dependência.

Justificativa: a arquitetura responde exatamente às perguntas que a Lia enfrenta hoje
(contrato de engine, catálogo com metadados, guardrails substituíveis), mas adotá-la
significaria reorganizar o ecossistema em torno de um framework alpha, orientado a
GPU NVIDIA, com telemetria — três coisas incompatíveis com o hardware e a política
do usuário.

**Gates** (se algum dia houver adoção parcial):

1. nenhum componente entra como dependência de runtime;
2. reimplementação independente de padrões, com registro de origem;
3. revisão da política de telemetria;
4. prova de funcionamento em Windows + AMD antes de qualquer promessa.

**Não autoriza:** instalar OpenJarvis, importar código, ou trocar o runtime de modelo
da Lia.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Extrair o desenho do `InferenceEngine` para um doc de contrato da Lia | Model-Lab | spec comparável |
| 2 | Comparar `GuardrailsEngine` com a política de credenciais já existente na Lia | Project | decisão de adoção de padrão |
| 3 | Ler `docs/architecture/learning.md` e avaliar métricas de energia para a bancada | Model-Lab | proposta de bancada |
| 4 | Verificar suporte real a backend Vulkan/CPU em Windows AMD | Model-Lab | `CONFIRMED` ou `BLOCKED` documentado |
| 5 | Revisar em 90 dias (projeto alpha, muda rápido) | Research | novo commit analisado |
