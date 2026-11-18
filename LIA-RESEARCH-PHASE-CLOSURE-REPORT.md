# LIA-RESEARCH — Relatório de encerramento da fase Research

| Campo | Valor |
|---|---|
| Data | 2026-11-17 (2ª rodada) |
| Branch | `arena/7cf9c65e-lia-research` |
| Commits | `cac9644` (fundação) · `f8ac9d1` (2ª rodada) |
| Estado do repositório | **público por decisão do proprietário** (`main@c9e6e97`); branch de pesquisa é a coleção completa |
| Veredito sobre encerrar a fase | **SIM para a coleta de pesquisa · NÃO para a validação** (ver §6) |

---

## 1. Trabalhos concluídos nesta rodada

| # | Trabalho | Entrega | Status honesto |
|---|---|---|---|
| 1 | **M-3** matriz Capability × Provider | `LR-MODEL-005` | **PASS** — evidência primária (54 definições lidas) |
| 2 | **L-4** Skills AIRI + Alethe | `LR-LIC-003` | **PASS** — parecer por Skill, 50 `SKILL.md` lidos |
| 3 | **A-3** manifesto de workflow | `LR-AGENT-009` | **PASS como proposta** — não implementado, não testado |
| 4 | **L-2** proveniência de asset | `LR-LIC-004` | **PASS como proposta** — schema v3 sobre o v2 real do Forge |
| 5 | **A-4** permissões por execução | `LR-SEC-005` | **PASS como proposta** — testes F1–F6 não executados |
| 6 | **U-3** ADR de interface | `LR-UI-005` | **PASS como procedimento** — nenhum ADR escrito em projeto |
| 7 | Correção de visibilidade | `DR-0006` → `ACCEPTED` | **PASS** — 5 documentos corrigidos |
| 8 | Revisão de exposição pública | `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md` | **PASS** — 3 achados, 2 tratados, 0 pendentes |
| 9 | Reconciliação de contagens | este relatório §4 | **PASS** — 5 divergências corrigidas com justificativa |
| 10 | Avaliação de R-1 a R-5 | `RESEARCH-ROADMAP.md` Trilha R | **PASS** — 2 `NOT RUN`, 3 `SKIP`, **0 documentos vazios** |

`PASS como proposta` **não** é `PASS` de resultado: o documento existe, a tecnologia não
foi exercitada. É a distinção que a ordem de serviço exige.

## 2. O que a 2ª rodada descobriu (e ninguém tinha registrado)

1. **Embedding existe no código e não existe no catálogo.** `lm-studio` monta provider de
   embedding via `merge(chat, embed, model)`, mas **nenhum** dos 54 providers declara
   `tasks: ['embed']`. A capability é invisível para catálogo, seletor e teste.
2. **Anthropic é a única das 10 curadas em que "suportado" pode ser falso.** A Lia fala
   `/v1/chat/completions`; a superfície nativa é `/v1/messages`, e o próprio documento de
   origem diz que não foi verificado contra a API real.
3. **A atribuição viaja, a licença não.** 8 das 28 Skills AIRI declaram autor no
   frontmatter; **nenhuma** declara licença; só 5 têm `LICENSE` no payload.
4. **`web-design-guidelines` é o maior risco individual de licença:** autor `vercel`,
   sem fonte, sem licença, dentro de um payload que o produto pretende exportar.
5. **`lia-eventa-ipc` é a única Skill Lia com licença** (`MIT`) — as outras 20 não têm.
   Hoje é impossível dizer "a política das Skills Lia é X".
6. **O `alethe` é o único payload de terceiro bem documentado do ecossistema**: licença,
   versão, commit comparado e patches no mesmo lugar (`UPSTREAM.md`). É o modelo a copiar.
7. **Branches são podadas.** 6 das 12 branches `arena/*` do Lia-Project desapareceram
   entre as duas rodadas do mesmo dia. O snapshot em `data/` deixou de ser conveniência e
   passou a ser a única cópia de 236 documentos.

## 3. Pesquisas que já existiam e foram reaproveitadas (não refeitas)

| Pesquisa existente | Como foi usada nesta rodada |
|---|---|
| `LIA-NATIVE-PROVIDER-COVERAGE.md` (101 KB) | base do registro do Corte B na matriz M-3 |
| `LIA-MODEL-PROVIDER-ARCHITECTURE.md`, `RECOMMENDATIONS.md` | camadas capability→adapter→provider |
| `lia-capability-catalog/0{2,3,4}` | 44 registros / 0 validados |
| `LIA-SKILLS-INVENTORY.md`, `SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` | base de `LR-LIC-001`; L-4 estendeu, não repetiu |
| `T11-E3-ASSET-PROVENANCE…` + manifesto v2 do Forge | base de `LR-LIC-004` (não inventei schema) |
| `DECISION-REGISTER.md` e `stitch/handoff/README.md` do Hub | base de `LR-UI-005` (o slot já existia) |
| `T14-AGENT-ORCHESTRATION-ARCHITECTURE.md` + `registry.mjs` | 49 capacidades usadas em `LR-AGENT-009` |
| Ports externos já auditados (OpenJarvis, Meldwork, HA-MCP, plannotator) | evidência de `LR-SEC-005` e `LR-UI-005` |

Nenhum relatório de pesquisa externa foi refeito. Nenhum documento de projeto foi alterado.

## 4. Reconciliação de contagens

| Item | Antes | Agora | Método / motivo |
|---|---|---|---|
| Commits de atraso da `main` do Lia-Project | 349 (§1) × 228 (§5) | **349** | contagem verificada; §5 corrigida |
| Skills AIRI | "29" | **28 AIRI + 1 Alethe** | a contagem agregava o `alethe` ao vendor AIRI |
| Skills com licença no payload | "0/48" (payloads Lia) | 0/48 Lia **e** 5/50 payloads totais | 4 AIRI + alethe têm licença própria |
| Decisões abertas | 13 | **12** (+1 aceita) | `DR-0006` encerrado por decisão |
| Arquivos Markdown | 113 / 118 / 124 | **131** | contagem de 2026-11-17 |
| Documentos no snapshot | 236 | **235** | sanitização (1 exclusão, 3 redações) |
| Providers com `tasks` ≠ `chat` | não medido | 13 TTS · 3 STT · 1 `text-generation` · 4 sem declaração | leitura de 54 `index.ts` |

Contagens históricas preservadas com data e método: inventário de 2026-11-17
(58.478 arquivos · 1.620 documentos · 511 fora de `main` · 975 vendorizados · 645 Lia) em
`data/README.md` §4 e `ecosystem/ECOSYSTEM-MAP.md`.

## 5. Situação da revisão de segurança pública

| Aspecto | Resultado |
|---|---|
| Documentos da base | **limpos** — 11 classes de padrão, 0 ocorrências em 131 Markdown |
| Snapshot do corpus | **3 achados**: 1 excluído (sessão privada), 3 e-mails redigidos, 1 mantido com justificativa |
| Segredos, tokens, credenciais | **0** |
| Dado pessoal | **0** após sanitização |
| Alvos potencialmente exploráveis | **0** — advisories são públicos, sem host real |
| Documento de registro | `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md` |

**Risco residual: baixo, e fora desta base.** O arquivo
`LIA-AGENT-CONSUMPTION-AUDIT.local.md` continua público em `BloomRX/Lia-Project` — contém
caminho de usuário, IDs de sessão e contagem de tokens. Não é meu escopo alterar
repositório de produto; está registrado para o proprietário.

## 6. A fase Research pode ser encerrada?

**Resposta em duas partes, porque a pergunta tem duas.**

### 6.1 Coleta de pesquisa — **SIM**

Não há mais pesquisa que possa ser feita **sem** hardware, sem decisão do proprietário ou
sem acesso a termos de serviço. Todo tema aberto hoje cai em uma destas três categorias:

| Categoria | Itens | Por que para aqui |
|---|---|---|
| Depende de execução (Windows/RX 580) | H-1…H-4, M-2, A-1, U-1/U-2, F1–F6, M-5 | exige a máquina do usuário |
| Depende de decisão do proprietário | 12 DRs abertos | exige autoridade que o agente não tem |
| Depende de terceiro publicar | ToS do RouterHub, licença do `web-design-guidelines`, versão vendorizada do AIRI | `BLOCKED` fora do controle |

### 6.2 Validação da pesquisa — **NÃO**

| Falta | Consequência |
|---|---|
| Nenhuma medição de desempenho | 44 modelos catalogados, **0 validados** |
| Nenhum protótipo executado | 6 pesquisas são propostas, não resultados |
| Revisão humana independente | 5 relatórios de alto impacto sem parecer (`agents/REVIEW-PROTOCOL.md`) |
| Testes F1–F6 do modelo de permissão | proposta não verificada |
| Manifesto de workflow não testado em nenhuma Skill | forma sem prova |

Declarar a fase Research "concluída" hoje significaria dizer que existe conhecimento
verificado sobre desempenho. **Não existe.** O correto é: *coleta encerrada, validação
pendente de hardware*.

## 7. Pendências por responsável

### 7.1 Dependem do proprietário (12 decisões)

| ID | Decisão | Destrava |
|---|---|---|
| `DR-0001` | licença das Skills `lia-*` (+ resolver `lia-eventa-ipc`) | exportação de Skill, `LR-AGENT-009` |
| `DR-0002` | publicação/revisão na base (leitura é pública) | escrita na base |
| `DR-0004` | destino do ZIP de 9,9 MB no Studio | proveniência limpa |
| `DR-0007` | consolidação de Skills duplicadas | catálogo sem sobreposição |
| `DR-0008` | aceitar matriz de risco R0–R3 | `DR-0003`, `LR-SEC-005` |
| `DR-0009`/`DR-0010` | retenção de log · câmera por padrão | integração residencial |
| `DR-0011`/`DR-0012` | registro e instalação de MCP | catálogo do Hub |
| `DR-0013` | parecer GPL do MDM | aquisição de arquivos grandes |
| `DR-0014` | critério de "modelo validado" | catálogo honesto |
| `DR-0003` | adotar adaptador residencial | implementação do HA-MCP |
| + `DR-0019`…`DR-0023` | 5 propostas de pesquisa (CI da matriz, manifesto, schema v3, permissões, ADR piloto) | adoção por projeto |

### 7.2 Dependem de teste no Windows (bloqueados, não "concluídos")

| Item | O que falta | Status |
|---|---|---|
| H-1 | `llama.cpp` Vulkan × CPU na RX 580 | `BLOCKED` |
| H-2 / H-3 | consumo em idle/jogo · pico de VRAM com Stage | `BLOCKED` |
| H-4 | WER + latência de STT PT-BR | `BLOCKED` |
| M-2 | 3 modelos validados na bancada | `BLOCKED` |
| A-1 / A-2 | protótipo HA-MCP R0/R1 e bloqueio de R2 | `BLOCKED` |
| U-1 / U-2 | protótipo Vercel UI + medição de bundle | `BLOCKED` |
| R-1 | assinatura/instalador no Windows | `NOT RUN` |

### 7.3 Dependem de revisão humana

5 relatórios de alto impacto (HA-MCP, MDM, pixelfx, rescript-lang, RouterHub) e as 4
propostas desta rodada precisam de parecer independente antes de qualquer adoção.

## 8. Estado final da base

| Métrica | Valor |
|---|---|
| Arquivos Markdown | **131** |
| IDs de pesquisa no índice | **57** |
| Relatórios externos | 16 objetos / 20 documentos |
| Dossiês de projeto | 5 |
| Documentos transversais | 25 (`cross-project/`) |
| Comparações | 4 |
| Decisões | 12 `PENDING` · 3 `REJECTED` · 2 `REFERENCE-ONLY` · **1 `ACCEPTED`** · 5 propostas |
| Dados versionados | 2,4 MB (`data/`: inventário, manifesto, 14 alvos pinados, snapshot sanitizado) |
| Tamanho total | 5,5 MB |
| Validação | `tools/validate.py`: 131 arquivos, **0 erros, 0 avisos** |

## 9. Recomendação

1. **Encerrar a coleta** e registrar a base como "pronta para consulta, pendente de
   validação".
2. **Abrir a fase de decisão** com as 12 pendências — três delas (`DR-0001`, `DR-0008`,
   `DR-0014`) destravam a maior parte das outras.
3. **Executar H-1 na primeira janela com a máquina disponível**: sem ele, nenhuma
   afirmação de desempenho desta base pode virar `CONFIRMED`.
4. **Não promover nenhuma proposta desta rodada a padrão** antes de testada em um caso real.

A base não está completa. Está **honesta sobre o que falta** — que é o único estado em que
uma base de pesquisa serve para decidir.
