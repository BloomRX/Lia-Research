# RESEARCH-ROADMAP

O que falta pesquisar, na ordem em que faz diferença. Cada item tem dono sugerido,
pré-requisito, critério de conclusão e o que **não** fazer.

Regra: item só sai daqui quando existe documento com evidência, não quando "já sabemos".

---

## Trilha 0 — Correções de base (fazer antes de qualquer coisa nova)

| # | Item | Por quê | Critério de conclusão |
|---|---|---|---|
| 0-1 | Tornar o repositório privado | requisito explícito da ordem de serviço; hoje público | `"private": true` na API |
| 0-2 | ~~Persistir inventário~~ | **feito** 2026-11-17: `data/` com TSVs + snapshot | `data/README.md` |
| 0-3 | Unificar a contagem de commits do Lia-Project em `ECOSYSTEM-MAP.md` | 349 vs 228 no mesmo documento | um número, verificado |

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
| M-3 | Matriz de conformidade de capability × provider | nenhum | **pronto para fazer** |
| M-4 | Definir critério de "modelo validado" (`DR-0014`) | nenhum | PENDING |

## Trilha L — Licença e proveniência (bloqueia distribuição)

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| L-1 | Resolver `DR-0001` (licença das Skills `lia-*`) | proprietário | PENDING |
| L-2 | Propor registro de proveniência de asset executável | `LR-LIC-002` | **pronto para fazer** |
| L-3 | Política de retenção/exclusão de dados do usuário | produto | PENDING |
| L-4 | Auditar as 29 skills AIRI e o `alethe` | nenhum | **pronto para fazer** |

## Trilha A — Agente e automação

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| A-1 | Protótipo isolado HA-MCP com 5 comandos R0/R1 | `DR-0008` | PENDING |
| A-2 | Prova de bloqueio R2 no caminho de leitura | A-1 | PENDING |
| A-3 | Especificação de manifesto de workflow para Skills | `DR-0001` | **pronto para fazer** |
| A-4 | Modelo de permissão com escopo por execução | `LR-AGENT-003` | pronto para escrever |
| A-5 | Teste de injeção de prompt via conteúdo de ferramenta | A-4 | NOT RUN |

## Trilha UI — Interface

| # | Item | Pré-requisito | Status |
|---|---|---|---|
| U-1 | Protótipo de 1 tela com Vercel UI SDK (foco/popup/DnD) | leitura dos beta terms | PENDING |
| U-2 | Comparar com a implementação atual (bundle, acessibilidade) | U-1 | PENDING |
| U-3 | ADR habit: começar a registrar decisão de UI com data | nenhum | **pronto para fazer** |

## Trilha R — Pesquisa não iniciada (lacunas declaradas)

| # | Tema | Por que está aqui | Nota |
|---|---|---|---|
| R-1 | Distribuição e empacotamento (instalador, update, assinatura) | nenhum projeto documenta | fora dos 16 alvos |
| R-2 | Observabilidade/telemetria local (métricas sem enviar dados) | `LR-HW-002` pede, nada cobre | fora dos 16 alvos |
| R-3 | Backup/restore de estado do app | `LR-SEC-004` tangencia | fora dos 16 alvos |
| R-4 | Visão/multimodal como tema próprio | não existe pesquisa dedicada | **não criar diretório vazio**; criar quando houver fonte |
| R-5 | Acessibilidade (WCAG) no produto | auditorias citam, sem norma | fora dos 16 alvos |

---

## Ordem recomendada dos próximos 5 trabalhos

1. **M-3** — matriz de conformidade capability × provider (não depende de hardware).
2. **L-4** — auditoria das 29 skills AIRI + `alethe` (dívida de licença real).
3. **A-3** — spec do manifesto de workflow (destrava Hub e Forge).
4. **U-3** — hábito de ADR de UI (custo quase zero, ganho permanente).
5. **H-1** — quando a máquina estiver disponível; nada acima depende dela.
