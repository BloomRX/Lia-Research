# RESEARCH-ROADMAP

| Campo | Valor |
|---|---|
| Natureza | roadmap operacional **e** estratégico |
| Parte A | o que falta pesquisar, item a item, com critério de conclusão |
| Parte B | sequência de 12 meses, dependências e critério de parada |
| Regra | item só sai daqui quando existe documento com evidência |
| Fonte de verdade da missão | `MISSION.md` |


> **Nota de 2026-11-26.** Este roadmap continua descrevendo o plano de 2026-11-17; o que mudou foi o
> estado de três linhas, e ele está medido, não previsto.
>
> | Linha | O que aconteceu |
> |---|---|
> | **A-1** (modelos/rotas) | o catálogo de providers tem três documentos correspondentes na `main` do Lia-Project (`docs/research/LIA-MODEL-PROVIDER-{CATALOG,ARCHITECTURE,RECOMMENDATIONS}.md`), classificados **por eles** como `Pending transfer` — os nossos `LR-MODEL-001`/`LR-MODEL-002` valem como consulta, e o canônico continua `lia-capability-catalog/`. Nenhum modelo foi medido: **V-1 continua 44 catalogados / 0 medidos** |
> | **A-4** (memória e contexto por usuário) | o bloco que faltava saiu: `LR-CMP-006` (recomendação mínima, alternativa e handoff ao Project, com sete gates) + `LR-MCP-005` (mcpvault, ensaio executado, 446/446 testes) + `LR-AGENT-019` (MemPalace, não executável offline). **A-14 permanece**: o ensaio de memória nunca rodou sobre notas reais — o nosso ensaio é com notas sintéticas e a limitação está declarada nos três documentos |
> | **A-20** (índices dos 5 produtos) | **executada para Project, Hub e Studio** em 2026-11-26, com correção de ponteiros e classificação por linha em `audits/RECONCILIACAO-OPERACIONAL-2026-11-26.md`. Ficam não verificáveis as **28** linhas de `Lia-Forge` (HTTP 403) e `Lia-Model-Lab` (HTTP 404) — e o Model Lab continua **pausado por decisão do dono**, então a pendência é de acesso |
>
> A pergunta que abriu a rodada — "qual é a integração mínima para a Lia aproveitar notas Markdown,
> inclusive de um vault do usuário?" — está respondida em `LR-CMP-006`; ela não dependia do PC com
> Radeon RX 580, e **não esperou** por ele. O hardware continua bloqueando V-1, V-7, A-9 e A-19, com
> rótulo `NOT RUN`.

## Parte A — o que falta pesquisar

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

## Trilha C — Confiabilidade da base (2026-11-20)

| # | Item | Status | Evidência |
|---|---|---|---|
| C-1 | Validador com data injetável e testes próprios | **feito** | `tools/validate.py` (18 verificações), `tools/test_validate.py` (78 testes) |
| C-2 | Proveniência de SHA por objeto | **feito** | `audits/PROVENANCE-2026-11-20.md`; 21/23 com SHA de 40 caracteres, 2 organizações incompletas por desenho |
| C-3 | Reauditoria de upstream (existência + movimento) | **feito** | `audits/REAUDIT-2026-11-20.md`; 10 de 22 com commit novo |
| C-4 | Reauditoria **técnica** (conteúdo) | **feito, com lacunas declaradas** | `audits/TECHNICAL-REAUDIT-2026-11-20.md`; 22 relatórios com seção `Reauditoria` |
| C-5 | Execução real de suítes | **parcial** | 5 suítes executadas; 8 objetos bloqueados por toolchain; 9 tentativas registradas |
| C-6 | Fila de pesquisa com decisão escrita | **feito** | `RESEARCH-BACKLOG.md` §7 (17 triados + 6 candidatos) |
| C-7 | Teste de Skill com entrada sintética (fecha "0 Skills medidas") | **pendente** | depende de `promptfoo`/`deepeval` (fila §7.1 #12 e #13) |
| C-8 | Rodar as suítes Rust/C++/.NET num ambiente com toolchain | **pendente** | bloqueio de ambiente, não de pesquisa |

> C-4 é "feito" no sentido de que **cada** objeto tem seção com evidência nova; não significa
> que todo objeto foi executado. A diferença está escrita na seção 5 do documento de
> reauditoria técnica.

## Trilha P — Criação de personagens (pedido do Forge 2.0, 2026-11-20; corrigida em 2026-11-20)

| # | Item | Status | Evidência / próximo passo |
|---|---|---|---|
| P-1 | Silhueta como primeiro gate, com critérios | **feito (método)** | `LR-STUDIO-008`; falta calibrar as métricas |
| P-2 | Catálogo de modelos com licença de código × pesos | **feito (revisado)** | `LR-MODEL-007` + matriz de 51 registros (46 + 3 + 2), com evidência por dimensão |
| P-3 | Consistência entre vistas / character sheet | **feito (análise)** | `LR-STUDIO-009`; nenhuma técnica executada |
| P-4 | 12 critérios 2D→3D e definição de "pronto para jogo" | **feito** | `LR-FORGE-007` §3 e §6 |
| P-5 | Três pipelines comparados | **feito** | `LR-FORGE-007` §4–5 |
| P-6 | Arquitetura para o Forge 2.0 | **feito como hipótese** | `LR-FORGE-010`; **requer leitura do código do Forge** |
| P-7 | Skills candidatas | **feito (análise)** | `LR-AGENT-012`; nenhuma skill escrita |
| P-8 | Rodar `stable-diffusion.cpp` + SDXL na RX 580 | **BLOCKED** | exige a máquina do usuário; único dado é `COMMUNITY_REPORTED` (SD1.5 ≈ 72 s) |
| P-9 | Comparar qualidade Tripo × Meshy × manual | **BLOCKED** | exige conta paga; lembrar que Free do Tripo torna o output público |
| P-11 | Decidir sobre CC5.2 / GPT Image / Flow como candidatos | **PENDING** | novos em 2026-11-20; exigem avaliação em máquina compatível e leitura de EULA |
| P-12 | Descobrir custo real por operação da AetherAI (`LR-MODEL-008`) | **BLOCKED** | a página de preços exige sessão/JavaScript; 70 tokens = US$ 3,99 é o único número obtido. Exige decisão de abrir conta |
| P-13 | Spike de movimento 2D com `LR-FORGE-009` (Live2D) | **BLOCKED** | exige modelo Live2D licenciado e Chrome; **e** decisão sobre o Cubism SDK Release License (faixa de faturamento) |
| P-14 | Esclarecer por escrito o Free do Tripo (`CONFLICTING`) | **BLOCKED** (piorou na 7.4) | agora são quatro fontes oficiais divergentes, duas delas afirmando retenção de direitos; depende de consulta ao fornecedor/advogado; Free segue vetado para asset proprietário |
| P-15 | Descobrir se créditos de Web App e API do Meshy são o mesmo pool | **UNVALIDATED** (não fecha) | a 7.4 confirmou que o **Free não tem API**; para planos pagos, nenhum documento lido afirma pool único nem separação definitiva |
| P-10 | Piloto de um personagem com medição de tempo por etapa | **PENDING** | decisão do proprietário |

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
| L-4b | Origem individual das 19 Skills `RESEARCH_ONLY` | `LR-LIC-003` §5 | `NOT RUN` |
| L-5 | Pipeline de citação com teste de identidade (hoje: citação manual) | `LR-SEC-006` R7 | `NOT RUN` — desenho existe em repo externo |
| L-6 | **Licenças prontas por objeto** (o projeto não precisa reabrir o relatório) | `LR-LIC-005` | **PASS** — matriz + fichas + 4 modelos de NOTICE |
| L-7 | Rodar o passo 3 do §6 em cada projeto (NOTICE no payload + registro em `docs/licenses/`) | L-6 | `NOT RUN` — depende dos projetos |

## Trilha A — Agente e automação

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| A-1 | Protótipo isolado HA-MCP com 5 comandos R0/R1 | `DR-0008` | PENDING |
| A-2 | Prova de bloqueio R2 no caminho de leitura | A-1 | PENDING |
| A-3 | Manifesto de workflow para Skills | `DR-0001` | **PASS (proposta)** — `LR-AGENT-009` |
| A-4 | Permissão com escopo por execução | `LR-AGENT-003` | **PASS (proposta)** — `LR-SEC-005` |
| A-5 | Teste de injeção de prompt via conteúdo de ferramenta | A-4 | NOT RUN |
| A-6 | Pacote de Skills de edição (ArtCraft) — 8 Skills propostas | `LR-STUDIO-004` | **PASS (proposta)** — `LR-AGENT-010` |
| A-7 | Executar V6 do pacote (editar foto real via MCP) | A-6 + app instalado | `NOT RUN` |
| A-8 | **Política de contribuição assistida por IA** (declarar, testar, explicar) | `LR-STUDIO-005` B1 | `NOT RUN` — texto-modelo existe |
| A-9 | Protocolo de **handoff entre agentes** (dono + reivindicação única) | `LR-AGENT-011` M1 | `NOT RUN` |
| A-10 | **Schema de achado + validador** para auditorias (forma, não verdade) | `LR-SEC-007` S1/S3 | `NOT RUN` |
| M-6 | **Orçamento por chave + failover com motivo registrado** | `LR-MODEL-006` F1/F2 | `NOT RUN` |

## Trilha UI — Interface

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| U-1 | Protótipo de 1 tela com Vercel UI SDK (foco/popup/DnD) | leitura dos beta terms | PENDING |
| U-2 | Comparar com a implementação atual (bundle, acessibilidade) | U-1 | PENDING |
| U-3 | Hábito de ADR de UI | nenhum | **PASS (procedimento)** — `LR-UI-005` |
| U-4 | Piloto de **barramento único de comandos** (UI/CLI/IPC/MCP) no Studio | `LR-STUDIO-004` A1 | `NOT RUN` |
| U-5 | Roots de leitura/escrita por sessão de agente + consentimento global | `LR-STUDIO-004` A2/A3 | `NOT RUN` |

## Trilha D — Ativos de design e vetorização (aberta em 2026-11-26)

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| D-1 | Ler a **Privacy Policy do site** e a **MCP Privacy Notice** do PerfectVector: a retenção do editor on-line (≈3 meses) e a do site (≈30 dias) estão `REPORTED`, não `CONFIRMED` | nenhum | `NOT RUN` — abre na próxima conferência; revisão marcada 2027-01-15 |
| D-2 | Medir a alternativa aberta **em escala local** (VTracer 0.6.15 + Inkscape 1.4.4/Potrace 1.16) sobre a mesma bateria de 4 casos sintéticos, com verificação automática de `fill` contra a paleta e varredura de 16/24/32/64/512 px | sandbox com os binários instalados | `PARTIAL` — VTracer medido em 4 casos (`LR-VEC-001` §8); `inkscape`/`potrace`/`autotrace` ausentes ⇒ `BLOCKED: FALTA_DEPENDENCIA` |
| D-3 | Decidir **no produto** se a Lia quer um modo raster→SVG local no Studio (VTracer embutido, MIT) — a pesquisa entrega a régua, não a decisão | D-2 | `SKIP` — fora da autoridade desta base |
| D-4 | Re-conferir os termos do fornecedor antes de **qualquer** uso: o site avisa mudanças materiais com 30 dias (§14), a **API pode mudar de preço sem aviso** (§4.2 dos API Terms), e o contrato inteiro está em `early access` (§2) | D-1 | `PENDENTE` |

Aberta por `LR-VEC-001` (`repositories/perfectvector/REPORT.md`), o primeiro objeto do catálogo cujo
`Tipo` é **serviço**: sem `LICENSE` para ler, com contrato para ler. Handoff por produto em
`projects/lia-forge/INDEX.md` §6, `projects/lia-studio/INDEX.md` §7 e `projects/lia-design-foundation/INDEX.md`.

---

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

---

# Parte B — visão de 12 meses

Origem: `archive/superseded/LIA-RESEARCH-ROADMAP.md` (documento de 2026-11-17, fundido
aqui em 2026-11-20 para acabar com dois arquivos chamados "roadmap" na raiz).
Continua sendo **sequência e critério de parada**; o detalhe item a item está na Parte A.

---

### 1. Diagnóstico que ordena o roadmap

A base tem **profundidade documental** e **ausência de medição**. Portanto o roadmap não
é "pesquisar mais temas": é converter conhecimento em decisão e decisão em número.

```text
documento  →  decisão  →  protótipo  →  medição  →  status CONFIRMED
   (feito)     (falta)      (falta)      (falta)        (zero hoje)
```

Tudo que não avança nessa cadeia é vaidade bibliográfica.

### 2. Trimestre 1 (nov–jan) — Decidir e desbloquear

| Item | Entrega | Depende de | Status |
|---|---|---|---|
| Privacidade do repositório | `"private": true` | proprietário | BLOCKED (403) |
| `DR-0001` licença das Skills | arquivo de licença por Skill | titular | PENDING |
| `DR-0008` matriz de risco | política aceita | proprietário | PENDING |
| `DR-0002` acesso de agentes | política de **publicação/revisão** — leitura já é pública (`DR-0006`) | proprietário | PENDING (parcial) |
| `M-3` matriz capability × provider | documento novo | nenhum | **pronto** |
| `L-4` auditoria das 29 skills AIRI + `alethe` | relatório `LR-LIC-003` | nenhum | **pronto** |
| `A-3` spec de manifesto de workflow | draft de spec | `DR-0001` | pronto para escrever |

**Critério de saída do trimestre:** três DRs fechados e nenhuma Skill `lia-*` sem
situação de licença declarada.

### 3. Trimestre 2 (fev–abr) — Medir

| Item | Entrega | Depende de |
|---|---|---|
| `H-1` benchmark Vulkan × CPU na RX 580 | primeira tabela de desempenho real | máquina |
| `M-2` bancada em 3 modelos | 3 registros `VALIDATED` | `H-1`, `DR-0014` |
| `H-3` pico de VRAM com Stage | o número que decide "cabe" | `H-1` |
| `U-1`/`U-2` protótipo Vercel UI + comparação | decisão de UI baseada em medição | beta terms lidos |
| `A-1` protótipo HA-MCP com 5 comandos R0/R1 | prova de conceito isolada | `DR-0008` |

**Critério de saída:** existir pelo menos **um** número de desempenho `CONFIRMED` na
base. Hoje não existe nenhum.

### 4. Trimestre 3 (mai–jul) — Decidir com número

| Item | Entrega |
|---|---|
| `M-1` catálogo canônico de modelo | um dono, uma tabela, decisão datada |
| `DR-0003` adaptador residencial | decisão com base em `A-1` |
| `L-2` registro de proveniência de asset | proposta executável para o Forge |
| `A-4` permissão com escopo por execução | spec + protótipo |
| `U-3` hábito de ADR de UI | primeiros 3 ADRs do produto |

### 5. Trimestre 4 (ago–out) — Consolidar e podar

| Item | Entrega |
|---|---|
| Revisão trimestral de todos os documentos `CURRENT` | status atualizado ou `STALE` |
| Auditoria de peso da base | o que ninguém citou em 6 meses → `archive/superseded` |
| `DR-0007` Skills duplicadas resolvidas | catálogo sem sobreposição |
| Revisão de licença de todos os artefatos distribuíveis | 0 payload sem NOTICE |
| Retrospectiva: a base evitou trabalho? | métrica de uso, não de volume |

### 6. Dependências (o que destrava o quê)

```text
DR-0006 (privado) ──► política de segurança plena
DR-0001 (licença)  ──► A-3 (manifesto) ──► distribuição de Skill no Hub
DR-0008 (risco)    ──► A-1 (protótipo) ──► DR-0003 (decisão residencial)
H-1 (benchmark)    ──► M-2 (modelos validados) ──► DR-0014 (critério) ──► M-1 (catálogo)
L-4 (AIRI)         ──► DR-0001 (escopo do que é Lia)
```

### 7. O que este roadmap exclui de propósito

| Excluído | Por quê |
|---|---|
| Pesquisar mais 16 repositórios | profundidade já excede a capacidade de decisão |
| Criar `cross-project/vision/` | sem fonte e sem espaço para pesquisa real (`R-4`) |
| Escrever especificação de produto | a base não declara arquitetura |
| Implementar qualquer coisa | proibido pela ordem de serviço |
| Migrar para outra ferramenta de documentação | o problema não é a ferramenta |

### 8. Métrica de sucesso da base (não é volume)

| Métrica | Hoje | Meta T4 |
|---|---|---|
| Perguntas respondidas em ≤2 consultas | estimado 80% | ≥95% |
| Pesquisas duplicadas criadas | 0 (dedup aplicado) | 0 |
| Afirmações de desempenho sem medição publicadas | 0 | 0 |
| Decisões abertas | 13 | ≤4 |
| Skills com licença declarada | 0/48 | 48/48 |
| Modelos validados | 0/44 | ≥3 |
| Artefatos distribuíveis sem NOTICE | 17 estimados | 0 |

### 9. Condição de parada

A base **não** deve crescer indefinidamente. Sinais de que deve parar de pesquisar e
começar a executar:

1. a mesma pergunta é respondida pelo índice há 3 meses sem novo dado;
2. existe documento citando outro documento desta base, sem fonte externa nova;
3. uma decisão está aberta há mais de um trimestre e ninguém a bloqueou tecnicamente.

Nesses casos, o próximo passo não é pesquisa: é decisão.
