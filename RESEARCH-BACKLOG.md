# Triagem de entrada — 20 itens recebidos (2026-11-17)

| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| Origem | lista do proprietário (11 repositórios + 9 sites/serviços) + 6 candidatos adicionais |
| Natureza | **triagem, não relatório**. Nada aqui foi executado; cada linha diz o que falta |
| Regra usada | repo → relatório com pin de SHA; site/serviço → análise de função e de como usar/reimplementar |
| Estado desta fila | 20 recebidos: **3 publicados** (`LR-AGENT-011`, `LR-SEC-007`, `LR-MODEL-006`), **17 triados** |
| Natureza do registro | linha de triagem **não** é pesquisa: nenhum item aqui é `DOCUMENTED` só por estar na tabela |

> **Como ler.** `INTAKE-nn` é o número da triagem, **não** é ID de pesquisa. ID (`LR-...`)
> só existe quando o relatório é publicado — a tabela diz quais já saíram.
> Prioridade: **A** = serve a decisão agora · **B** = serve, mas depois · **C** = não serve
> ao ecossistema (registrado para não voltar à mesa).

## 1. Os 11 repositórios

| # | Repositório | O que é | Licença | ★ | Prioridade | Situação |
|---|---|---|---|---:|---|---|
| 01 | `akitaonrails/ai-memory` | memória de longo prazo multi-harness para agentes de código, com *handoff* tipado entre Claude Code/Codex/etc. (Rust) | MIT | 16.172 | **A** | **PUBLICADO** — `LR-AGENT-011` |
| 02 | `cloudflare/security-audit-skill` | Skill de auditoria de segurança em fases, com achados verificáveis; tem arquivo específico de **desktop/Electron/IPC** e **AI/LLM** | MIT | 75.939 | **A** | **PUBLICADO** — `LR-SEC-007` |
| 03 | `tashfeenahmed/freellmapi` | agrega 87 free tiers num `/v1` compatível com OpenAI; roteamento, failover, chaves cifradas, orçamento por chave | MIT | 55.337 | **A** | **PUBLICADO** — `LR-MODEL-006` |
| 04 | `bitbonsai/mcpvault` | servidor MCP para acesso seguro a um vault Obsidian (TypeScript) | MIT | 1.726 | B | triado — relatório pendente |
| 05 | `mempalace/mempalace` | sistema de memória para IA com ChromaDB, MCP, "best-benchmarked" (Python) | MIT | 60.634 | B | triado — concorre com `ai-memory`; comparar antes |
| 06 | `getsentry/skills` | Skills que o time do Sentry usa no desenvolvimento (Python, 1,3 MB) | Apache-2.0 | 1.187 | B | triado — padrão de autoria de Skill |
| 07 | `briiirussell/cybersecurity-skills` | Skills de segurança para agentes de código (JS, 2 MB) | MIT | 526 | B | triado — sobrepõe `LR-SEC-007`; comparar |
| 08 | `chenxiachan/textfold` | "dobra" papers/páginas/arquivos em 5 níveis de detalhe, com zoom semântico (Python) | Apache-2.0 | 1.286 | B | triado — ideia útil para leitura longa |
| 09 | `erkamyaman/rust-anything` | migra app para Rust peça por peça, conferindo comportamento gravado a cada passo (Rust) | MIT | 5.540 | B | triado — técnica de verificação diferencial |
| 10 | `Bodila51/gtavi-claudecode` | plugin que transforma lives de GTA 6 em cortes verticais para redes (Python) | MIT | 1.001 | C | triado — domínio fora do escopo; pipeline de corte é a única parte reaproveitável |
| 11 | `net-merge/net-merge` | agrega várias conexões de internet ao mesmo tempo (Go, WAN/TUN) | MIT | 3.431 | C | triado — não há requisito de rede nos apps |

## 2. Os 9 sites e serviços

| # | Endereço | O que é | Relevância | Prioridade | Situação |
|---|---|---|---|---|---|
| 12 | `canirunai.kc1t.com` | calculadora de compatibilidade hardware↔modelo (116 modelos), detecção por WebGL e `npx can-i-run-ai` | **alta** — ataca direto o `LR-HW-001` (RX 580) e o "44 catalogados / 0 validados" | **A** | triado — usar como **pré-filtro**, nunca como medição |
| 13 | `docs.astral.sh/uv` | gerenciador de pacotes/projetos Python em Rust (`astral-sh/uv`, Apache-2.0, ★92.434) | média — tooling dos scripts Python da Lia | B | triado |
| 14 | `graphify.com` | SaaS (YC) de grafo de código consultável por MCP, com motor open source; afirma ★150.753 e 15,2 M repos indexados | média — reduz tokens ao dar grafo em vez de repo ao agente | B | triado — **licença do motor não verificada** |
| 15 | `obsidian.md` | app de notas local-first; **proprietário** (gratuito para uso pessoal, pago para uso comercial) | média — memória/documentos do usuário | B | triado — ⚠️ verificar termos comerciais antes de integrar |
| 16 | `kc1t.com/…/memoria-para-suas-ias` | artigo sobre memória para IAs (mesmo autor do CanIRunAI) | baixa — conteúdo, não ferramenta | C | triado — ler só se for escrever sobre memória |
| 17 | `lousa-ia.vercel.app` | "lousa" (quadro) com IA na web | baixa — depende do que faz na prática; não inspecionado a fundo | C | triado — `UNVERIFIED` |
| 18 | `owasp.org/projects/top-ten` | OWASP Top 10 (padrão de referência de risco web) | **alta** — vocabulário comum para as auditorias de segurança | **A** | triado — adotar como *checklist* citada, não como ferramenta |
| 19 | `sentry.io/welcome` | plataforma de observabilidade de erro (SaaS, com SDK open source) | média — é a lacuna `R-2` (observabilidade nunca pesquisada) | B | triado — o *padrão* de captura de erro importa mais que o produto |
| 20 | `github.com/topics/ai-qa` | **lista** de repositórios de QA com IA | média — fonte para a próxima rodada (ver §3) | B | triado — lista, não objeto |

## 3. Candidatos adicionais (para a próxima fila, medidos por API)

**Estado honesto: `TRIAGED`.** Estes seis foram medidos por API do GitHub (nome, licença,
estrelas, descrição). Nenhum README foi lido, nenhuma licença foi aberta no arquivo. Não
existe relatório e não existe ID — dizer "avaliado" aqui seria mentira.

| Repositório | O que é | Licença | ★ | Por que entra na fila |
|---|---|---|---:|---|
| `promptfoo/promptfoo` | teste/red-team de prompt, agente e RAG | MIT | 27.477 | responde direto ao "0 Skills medidas" (`LR-AGENT-009` V6) |
| `confident-ai/deepeval` | framework de avaliação de LLM | Apache-2.0 | 19.570 | métricas de avaliação sem depender de SaaS |
| `langfuse/langfuse` | observabilidade de LLM (self-host) | NOASSERTION | 37.649 | preenche a lacuna de observabilidade `R-2` |
| `BerriAI/litellm` | gateway/proxy para 100+ provedores | NOASSERTION | 63.580 | é o **upstream** do gateway rejeitado em `LR-PROV-001`; avaliar a origem, não o fork |
| `modelcontextprotocol/servers` | servidores MCP de referência | NOASSERTION | 92.121 | base para o `LR-MCP-002` |
| `astral-sh/uv` | gerenciador Python em Rust | Apache-2.0 | 92.434 | já nesta lista (item 13) |

## 4. O que a triagem já permite concluir

| Conclusão | Base |
|---|---|
| O tema dominante desta lista é **memória de agente** e **Skills de segurança** | itens 01, 04, 05, 06, 07, 02 |
| Três objetos concorrem entre si — `ai-memory` × `mempalace` × `mcpvault` | 01, 05, 04 |
| Dois objetos vivem na fronteira da legalidade de termos de uso — `freellmapi` (free tiers) e `graphify`/`obsidian` (serviço/proprietário) | 03, 14, 15 |
| Só um item fala do hardware real da Lia de forma útil | 12 (`canirunai`) — e ele **estima**, não mede |
| Nenhum item, sozinho, resolve o maior buraco da base: **nada validado em execução** | `LR-AGENT-009` V6, 44/0 modelos |

## 5. Próxima fila (proposta, sem promessa de data)

| Ordem | O que | Por quê agora |
|---|---|---|
| 1 | `LR-SEC-007` §desktop/IPC aplicado ao Lia-Project | é o único material já lido que fala de **Electron/IPC local** |
| 2 | Comparar `ai-memory` × `mempalace` × `mcpvault` num único digest | evitar três relatórios que dizem o mesmo |
| 3 | `promptfoo` como resposta ao V6 (medir Skill de verdade) | fecha a lacuna mais antiga da base |
| 4 | `canirunai` como pré-filtro do catálogo de 44 modelos | dá utilidade imediata sem prometer medição |
| 5 | `langfuse` × `sentry` para a lacuna `R-2` | observabilidade nunca pesquisada |

## 6. Limites desta triagem

- Os 6 candidatos da §3 têm **licença informada pela API**, não lida no arquivo (`langfuse`
  e `litellm` aparecem como `NOASSERTION` justamente por isso).
- Nada desta fila foi executado; `Resultado de execução` de todos os itens é `NOT_RUN`.
- Triagem é ordem de fila, não conclusão técnica: item `C` aqui pode voltar se o contexto
  do ecossistema mudar.

- **Não executei** nenhum dos 11 repositórios; estrelas e tamanho vêm da API.
- **Não li** README completo de 8 dos 11 repositórios — só metadados e descrição.
- **Não verifiquei** a licença do motor open source do Graphify nem os termos comerciais
  do Obsidian; ambos estão marcados como pendência.
- `lousa-ia.vercel.app` não foi inspecionado a fundo.
- A lista `github.com/topics/ai-qa` é uma **fonte**, e o que dela saiu está no §3 por
  metadados, não por leitura.

## 7. Decisões da fila — 2026-11-20

Resultado da rodada de triagem pós-reauditoria. Cada item recebe **uma** decisão, com motivo.
Prioridade aqui é ordem de execução, não valor intrínseco.

### 7.1. Os 17 triados

| # | Item | Decisão | Motivo | Ordem |
|---:|---|---|---|---|
| 01 | `bitbonsai/mcpvault` (MCP de vault Obsidian) | **investigar** | fecha duas lacunas de uma vez: memória/notes de agente e servidor MCP com dado pessoal. Superfície de leitura de arquivo sensível é o que `LR-MCP-002` não cobre | 3 |
| 02 | `docs.astral.sh/uv` | **investigar (curto)** | tooling de Python de todos os scripts desta base e dos 5 projetos; já aparece como duplicata em 3 lugares, então a investigação é de consolidação | 4 |
| 03 | `pypi`/`mcp` servers restantes | **aguardar evidência** | lista de servidores sem caso de uso concreto pedido por projeto; sem demanda, seria catálogo por catálogo | — |
| 04 | `sentry.io` | **comparar** com `langfuse` | mesma pergunta (observabilidade de erro × observabilidade de LLM); comparar antes de investigar separado | 5 |
| 05 | `obsidian.md` | **permanecer como referência** | objeto de produtividade do proprietário, não de engenharia Lia; serve ao item 01 como contexto | — |
| 06 | `lousa-ia.vercel.app` | **rejeitar** | app de terceiro sem código público, sem licença verificável, sem função que a Lia não tenha | — |
| 07 | `graphify.com` | **investigar (segurança primeiro)** | SaaS com MCP que recebe código do repositório; a pergunta não é utilidade, é o que sai da máquina. Trilha: §8 | 6 |
| 08 | `canirunai.kc1t.com` | **rejeitar como fonte de validação** | estima, não mede. Útil como pré-filtro; usado como prova viraria exatamente o erro que `LR-MODEL-004` denuncia | — |
| 09 | `akitaonrails/ai-memory` | **feito** | `LR-AGENT-011` publicado | — |
| 10 | `cloudflare/security-audit-skill` | **feito** | `LR-SEC-007` publicado | — |
| 11 | `tashfeenahmed/freellmapi` | **feito** | `LR-MODEL-006` publicado | — |
| 12 | `promptfoo/promptfoo` | **investigar — prioridade 1** | é a resposta mais direta à lacuna mais antiga da base: "0 Skills medidas". Testa prompt, agente e RAG; permite medir Skill com entrada sintética (Nível 1) | **1** |
| 13 | `confident-ai/deepeval` | **comparar** com `promptfoo` | mesma família (avaliação de LLM); investigar os dois em paralelo e comparar, não em sequência | 2 |
| 14 | `langfuse/langfuse` | **investigar (self-host)** | preenche `R-2` (observabilidade). Licença `NOASSERTION` na API: ler o arquivo antes de qualquer conclusão | 7 |
| 15 | `BerriAI/litellm` | **investigar como upstream** | `DR-0005` rejeitou o **fork**; avaliar o original é pergunta diferente e continua aberta | 8 |
| 16 | `modelcontextprotocol/servers` | **permanecer como referência** | coleção de servidores de exemplo; útil como lista, não como objeto único de relatório | — |
| 17 | `astral-sh/uv` | **não duplicar** | é o item 02 desta lista. Uma entrada só, com nota de deduplicação | — |

### 7.2. Os 6 candidatos adicionais da triagem original

| Item | Decisão | Motivo |
|---|---|---|
| `promptfoo` | **investigar (1)** | ver 7.1 #12 — resolve lacuna de teste, não só catálogo |
| `deepeval` | **comparar (2)** | par natural de `promptfoo`; comparar evita dois relatórios que dizem o mesmo |
| `langfuse` | **investigar (7)** | observabilidade; licença a confirmar no arquivo |
| `litellm` | **investigar como upstream (8)** | origem do gateway rejeitado no fork |
| `modelcontextprotocol/servers` | **referência** | coleção, não objeto |
| `astral-sh/uv` | **deduplicado** | já é o item 02; não vira linha própria |

Nenhum item recebeu prioridade "C" como desculpa: os três que saem da fila (`lousa-ia`,
`canirunai` como fonte, `sentry` isolado) saem por motivo escrito — licença ausente, método
que não mede, e pergunta já coberta por comparação.

### 7.3. Por que esta ordem

1. **`promptfoo`, 2. `deepeval`** — a base tem 23 relatórios e 14 linhas de teste, das quais
   apenas 5 são execução real. A lacuna não é "saber mais tecnologias", é **provar** o que
   já está catalogado. Ferramenta de avaliação ataca isso.
2. **`mcpvault`, 4. `uv`** — MCP é a superfície que mais cresce no ecossistema; `uv` é
   infraestrutura de todo script Python desta base.
3. **`sentry` × `langfuse`, 7. `graphify`** — observabilidade e o caso "SaaS que lê o
   repositório", que é o risco mais concreto de vazamento em 2026.
4. **`litellm` (upstream)** — só depois de saber se observabilidade e avaliação mudam a
   conclusão de `DR-0005`.

### 7.4. Regra que vale para esta fila

Item entra em investigação quando tem **pergunta respondível**, não quando é interessante.
A pergunta vai escrita no cabeçalho do relatório; se não couber em uma frase, o item volta
para a fila.

