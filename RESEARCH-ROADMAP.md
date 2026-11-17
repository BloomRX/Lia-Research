# RESEARCH-ROADMAP

O que falta pesquisar, na ordem em que faz diferença. Cada item tem dono sugerido,
pré-requisito, critério de conclusão e o que **não** fazer.

Regra: item só sai daqui quando existe documento com evidência, não quando "já sabemos".

---

## Trilha 0 — Correções de base (fazer antes de qualquer coisa nova)

| # | Item | Por quê | Critério de conclusão |
|---|---|---|---|
| 0-1 | ~~Tornar o repositório privado~~ | **resolvido**: o proprietário decidiu mantê-lo público (`c9e6e97`) | revisão de exposição: `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md` |
| 0-2 | ~~Persistir inventário~~ | **feito** 2026-11-17: `data/` com TSVs + snapshot | `data/README.md` |
| 0-3 | ~~Unificar a contagem de commits do Lia-Project~~ | **feito**: 349 nas duas menções | `ecosystem/ECOSYSTEM-MAP.md` §1 e §5 |

## Trilha H — Hardware (bloqueia toda decisão de modelo)

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| H-1 | Benchmark `llama.cpp Vulkan` vs CPU na RX 580 | máquina do usuário | BLOCKED |
| H-2 | Consumo em idle e durante jogo (3 configurações) | H-1 | BLOCKED |
| H-3 | Pico de VRAM com Stage ativo | H-1 | BLOCKED |
| H-4 | STT PT-BR (whisper.cpp vs sherpa-onnx): WER + latência | máquina + 1 h de áudio | BLOCKED |

**Não fazer:** prometer "roda em 8 GB" sem H-3; tratar ROCm como opção de usuário.

## Trilha M — Modelos

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| M-1 | Eleger **um** catálogo canônico e reconciliar LFM3 | decisão dos 2 projetos | PENDING |
| M-2 | Executar a bancada em 3 modelos (LFM3-1.7B, Qwen pequeno, 1 embedding) | H-1 | BLOCKED |
| M-3 | Matriz de conformidade de capability × provider | nenhum | **PASS** — `LR-MODEL-005` (54 providers lidos) |
| M-4 | Definir critério de "modelo validado" (`DR-0014`) | nenhum | PENDING |

## Trilha L — Licença e proveniência (bloqueia distribuição)

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| L-1 | Resolver `DR-0001` (licença das Skills `lia-*`) | proprietário | PENDING |
| L-2 | Registro de proveniência de asset executável | `LR-LIC-002` | **PASS (proposta)** — `LR-LIC-004` |
| L-3 | Política de retenção/exclusão de dados do usuário | produto | PENDING |
| L-4 | Auditar as 28 skills AIRI e o `alethe` | nenhum | **PASS** — `LR-LIC-003` (19 de 28 seguem `RESEARCH_ONLY`) |

## Trilha A — Agente e automação

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| A-1 | Protótipo isolado HA-MCP com 5 comandos R0/R1 | `DR-0008` | PENDING |
| A-2 | Prova de bloqueio R2 no caminho de leitura | A-1 | PENDING |
| A-3 | Manifesto de workflow para Skills | `DR-0001` | **PASS (proposta)** — `LR-AGENT-009` |
| A-4 | Permissão com escopo por execução | `LR-AGENT-003` | **PASS (proposta)** — `LR-SEC-005` |
| A-5 | Teste de injeção de prompt via conteúdo de ferramenta | A-4 | NOT RUN |

## Trilha UI — Interface

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| U-1 | Protótipo de 1 tela com Vercel UI SDK (foco/popup/DnD) | leitura dos beta terms | PENDING |
| U-2 | Comparar com a implementação atual (bundle, acessibilidade) | U-1 | PENDING |
| U-3 | Hábito de ADR de UI | nenhum | **PASS (procedimento)** — `LR-UI-005` |

## Trilha R — Avaliação das lacunas declaradas (2026-11-17)

Avaliadas nesta data. Regra aplicada: só abre pesquisa quem tem **fonte identificada** e
**pergunta concreta**. Sem fonte, o status é `SKIP` com motivo — nunca documento vazio.

| # | Tema | Fonte existe? | Pergunta concreta | Status |
|---|---|---|---|---|
| R-1 | Distribuição, instalador, update, assinatura | **sim, parcial**: `OpenJarvis` (installers `install.sh`/`install.ps1`, artefatos desktop), `Meldwork` (assinatura de pacote `CONFIRMED` em commit), `Lia-Project:docs/product/RELEASE-WINDOWS-*` | "como publicar um app Electron assinado no Windows sem alerta de SmartScreen e sem serviço obrigatório?" | `NOT RUN` — abrir em T2 |
| R-2 | Observabilidade e telemetria local | **insuficiente**: `LR-HW-002` pede métricas; nenhum alvo pesquisado implementa telemetria local auditável | "que métricas registrar sem virar perfil de comportamento?" | `SKIP` — fonte rasa; abriria relatório especulativo |
| R-3 | Backup e restauração de estado | **parcial**: `Lia-AgentHub:DATA-STORAGE-AND-PORTABILITY.md` (`LR-SEC-004`) | "exportar/restaurar memória e configuração é o mesmo que portabilidade?" | `SKIP` — já coberto no essencial por `LR-SEC-004`; abrir só se virar requisito de produto |
| R-4 | Visão e multimodal | **não**: nenhum projeto tem pesquisa dedicada; catálogo não tem modelo multimodal (`LR-MODEL-005` §7) | "vale ter visão local na RX 580?" | `SKIP` — pergunta depende de H-1/H-3 (`BLOCKED` por hardware) |
| R-5 | Acessibilidade (WCAG) | **parcial**: `LR-UI-001` (comportamentos ARIA do Vercel UI), `LR-UI-004`, `LR-UI-005` | "qual nível de WCAG a Lia assume, e como é verificado?" | `NOT RUN` — abrir junto com U-1/U-2 |

Nenhum diretório `cross-project/vision/`, `observability/` ou `distribution/` foi criado:
criar pasta para "marcar presença" é o oposto de pesquisa honesta.

---

## Ordem recomendada dos próximos 5 trabalhos

As cinco primeiras desta lista estão **feitas** na 2ª rodada de 2026-11-17:
`LR-MODEL-005` (M-3), `LR-LIC-003` (L-4), `LR-AGENT-009` (A-3), `LR-UI-005` (U-3),
`LR-LIC-004` (L-2) e `LR-SEC-005` (A-4). A nova ordem:

1. **L-4b** — origem individual das 19 Skills `RESEARCH_ONLY` (`LR-LIC-003` §5 diz quais).
2. **M-5** — tool calling por provider: nenhum declara tools; provar ou documentar como
   limitação (`LR-MODEL-005` §5.1).
3. **R-1** — distribuição e assinatura no Windows (fonte parcial já identificada).
4. **U-1/U-2** — protótipo Vercel UI + comparação medida (antes: ler os beta terms).
5. **H-1** — quando a máquina estiver disponível; nada acima depende dela.
