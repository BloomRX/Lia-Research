# Conjunto operacional de Skills do ecossistema aplicado ao Lia Research

| Campo | Valor |
|---|---|
| Natureza | instrução operacional de agente, não política de produto |
| Versão | 1.0 — 2026-11-20 (UTC) |
| Fontes | catálogo do Lia Agent Hub (`docs/research/`, branch `arena/db625478`) + `SKILL.md` lidos nos repositórios de origem |
| Limite | nenhuma Skill aqui adota tecnologia, aprova integração ou altera governança |
| Estado de execução | **APPLIED (manual)** — lido e aplicado como procedimento; **não** carregado por runtime |

---

## 0. Por que este documento existe

O Research é departamento permanente de inteligência tecnológica, não mantenedor de
catálogo. As rodadas 7.x mostraram três desvios recorrentes: rodada aberta para corrigir
detalhe secundário, auditoria repetida sem justificativa nova e conclusão registrada sem
refutação. Este documento fixa **qual instrução do ecossistema Lia** impede cada um — e
qual foi deliberadamente **não** adotada.

Ele não substitui `governance/RESEARCH-METHODOLOGY.md`, `governance/INVESTIGATION-PROTOCOL.md`
nem `governance/TESTING-PROTOCOL.md`. Onde houver conflito, vale o protocolo do repositório:
a Skill é método importado, não autoridade.

## 1. Onde está o catálogo (e o que ele não é)

| Objeto | Localização | O que é |
|---|---|---|
| Catálogo de Skills (48 registros) | `Lia-AgentHub`, branch `arena/db625478-lia-agenthub`, `docs/research/catalog/` | 4 arquivos `*.records.json` + `sources.json`, no formato `schemaVersion: 1` do Hub |
| Inventário canônico | mesma branch, `docs/research/LIA-SKILLS-INVENTORY.md` (37 KB) | 48 Skills, 16 Studio, 22 Project, 9 Model-Lab, 1 Forge, com commit por repositório |
| Relatório de importação | mesma branch, `docs/research/SKILL-CATALOG-IMPORT-REPORT.md` | limites dos registros e roteiro de conferência |
| Roadmap de Skills | mesma branch, `docs/research/LIA-SKILLS-ROADMAP.md` | 8 Skills **propostas** (não existem) |
| Payload real de cada Skill | `SKILL.md` no repositório de origem, no commit citado | a instrução que se aplica |

Três limites que precisam ficar explícitos:

1. **O catálogo não é a biblioteca.** A biblioteca real vive na máquina do usuário e não é
   acessível daqui. O que existe neste ambiente é o **registro** e o **arquivo de origem**.
2. **Todos os 48 registros estão `trust: unreviewed` e `lifecycle: quarantined`.** Estar no
   catálogo não é aprovação, nem sinal de que a Skill roda.
3. **A Skill de pesquisa que o Research precisaria não existe.**
   `lia-research-evidence` é a **proposta nº 7** do roadmap, marcada como planejada — não
   implementada em nenhum repositório. Não criei nem instalei nada; o conjunto abaixo é
   composto só do que já existe.

## 2. O que foi lido nesta atividade

Lido por inteiro, no commit indicado, em 2026-11-20 (UTC):

| Skill | Repositório e commit | Bytes | sha256 (16 primeiros) |
|---|---|---:|---|
| `lia-agent-orchestration` | `Lia-Project` @ `0093de09` (branch `arena/c6b02f64-lia-project`) | 3.105 | `ff131e2512e55c71` |
| `lia-regression-investigation` | `Lia-Project` @ `0093de09` | 4.632 | `ef7bfc74c585847f` |
| `lia-test-discipline` | `Lia-Project` @ `0093de09` | 2.800 | — (não adotada) |
| `lia-agent-evaluation` | `Lia-Project` @ `0093de09` | 4.974 | — (não adotada) |
| `lia-safe-change` | `Lia-Project` @ `0093de09` | 2.759 | — (não adotada) |
| `lia-game-test-evidence-review` | `Lia-Studio` @ `203b60f` (branch `arena/01a0f4ab-lia-gamedev`) | 1.814 | `1a3cb983f9361ec9` |
| `lia-game-design-review` | `Lia-Studio` @ `203b60f` | 1.826 | — (não adotada) |
| `lia-project-resume` | `Lia-Studio` @ `203b60f` | 2.313 | `d259d2010b231632` |
| `lia-task-handoff` | `Lia-Studio` @ `203b60f` | 2.521 | — (não adotada) |
| `lia-module-planning` | `Lia-Studio` @ `203b60f` | 2.627 | — (não adotada) |

Lidos apenas como **descrição** (inventário, sem abrir o `SKILL.md`): as 9 de
`Lia-Model-Lab`, a `lia-brand-check` de `Lia-Forge`, as 28+1 vendadas do AIRI e as 20 do
pacote Mr. Mak. Registro isso porque a diferença importa: descrição no inventário não é
instrução lida.

## 3. O que é realmente utilizável no Arena

Critério aplicado, nesta ordem: (a) o arquivo é legível daqui; (b) o método não exige
runtime, sistema operacional, CLI, credencial ou permissão; (c) o Research tem o que a
Skill consome (documentos, commits, suíte de teste).

| Situação | Skills | Consequência |
|---|---|---|
| **Utilizável como procedimento lido** | 4 adotadas + 6 lidas e rejeitadas por redundância ou escopo | aplico a instrução manualmente; sem runtime |
| **Inacessível daqui** | 9 de `Lia-Model-Lab`, 1 de `Lia-Forge` | os repositórios retornam `404` para o token atual; só a descrição do inventário está ao alcance |
| **Inexistente** | 8 propostas do roadmap, incl. `lia-research-evidence` | não se pode usar o que não foi implementado |
| **Bloqueada por dependência** | `lia-agent-evaluation` (credencial de provedor), `lia-visual-evidence` (Vishot), `lia-browser-automation` (agent-browser + CDP), `alethe` (CLI instalada), `lia-release-gate` e `stage-runtime-debugging` (Windows + checkout) | no Arena ficam `BLOCKED`, não `FALHA` |

**Ponto que não pode ser maquiado:** o Arena não expõe runtime de Skills nesta sessão —
nenhuma Skill é descoberta ou carregada automaticamente. O que fiz foi **ler o `SKILL.md`
e aplicar o procedimento**. Chamar isso de "Skill executada" seria falso; o rótulo correto
é `APPLIED (manual)`, e é o que está no cabeçalho deste documento.

## 4. Conjunto mínimo adotado — 1 principal + 3 especialistas

### 4.1 Principal: `lia-agent-orchestration`

Base de tudo o que o Research faz por rodada. Os cinco elementos que passam a valer:

| Regra da Skill | Como entra no Research |
|---|---|
| Brief de 8 campos (objetivo verificável, contexto, caminhos **leitura/escrita**, restrições, critério de conclusão, comando de teste, formato de retorno, faixa de capacidade) | abertura de toda rodada; o pedido do proprietário é convertido nesses campos antes de qualquer leitura |
| Retorno de 6 campos (o que investigou, arquivos, decisões, testes comando→resultado→código, limites, próximo passo) | formato do relatório final; `NÃO EXECUTADO` com motivo é resposta válida |
| Um escritor por caminho, por rodada | evita edição concorrente entre especialistas e retrabalho de índice |
| Capacidade por evidência | rodada pequena não vira pesquisa ampla: a faixa alta exige causa identificada, ambiguidade cara ou risco de perda |
| "Quem precisa sair do próprio conjunto **para e reporta**" | **a regra de parada de escopo** que faltava explicitamente no Research |

### 4.2 Especialista: `lia-regression-investigation` — quando uma conclusão precisa ser provada

Acionada quando: uma rodada anterior será corrigida, duas fontes oficiais divergem, ou uma
conclusão "parece certa". Contribuições diretas ao erro da rodada 7.4 (que concluiu ausência
de cláusula lendo só o §5.2.2):

- reproduzir antes de concluir: achar a **cláusula**, não a paráfrase da página de ajuda;
- testar a própria hipótese ao contrário: procurar onde a cláusula **estaria** se existisse,
  antes de afirmar que não existe;
- uma variável por vez: separar "treinamento" de "revisão", "anonimização" e "retenção" — foi
  exatamente a fusão dessas variáveis que produziu o erro;
- modelo reduzido não prova o sistema: trecho lido isolado não autoriza afirmar o regime
  inteiro do contrato;
- registrar cada sintoma como `aberto`, `causa provada`, `corrigido` ou `refutado`.

### 4.3 Especialista: `lia-game-test-evidence-review` — antes de fechar qualquer rodada

Acionada antes de consolidar o relatório. Contribuições:

- cada critério de conclusão ligado a **teste, artefato, comando, ambiente e data**;
- ausência vira `NÃO AVALIADO`, nunca aprovação silenciosa;
- classificação por critério `ADEQUADA`, `INCOMPLETA`, `AUSENTE` ou `NÃO AVALIADA`;
- mock, leitura, hash e execução real são evidências de classes diferentes.

O nome é de jogo, o método é geral; o mapeamento para os rótulos do Research
(`CONFIRMED`, `OBSERVED`, `REPORTED`, `INFERRED`, `UNVERIFIED`, `BLOCKED`, em
`governance/EVIDENCE-STANDARDS.md`) fica assim: `ADEQUADA` exige `CONFIRMED` ou `OBSERVED`
com artefato; `INCOMPLETA` corresponde a `INFERRED`; `AUSENTE` e `NÃO AVALIADA` nunca
sobem para `CONFIRMED`.

### 4.4 Especialista: `lia-project-resume` — abertura de rodada

Acionada ao retomar o trabalho (toda sessão nova, porque o estado local de git não persiste).
Contribuições:

- reconstruir estado a partir de **artefato persistido**, não de memória de conversa;
- separar estado da tarefa, execução, validação e aprovação — quatro coisas que o Research
  já registra separadas e que se fundem quando a rodada é longa;
- listar verificado, não executado e inconclusivo com referência à evidência;
- não reescrever documento como verdade sem confirmação.

Mapeamento de arquivos: `PROJECT_BRIEF.md` → `MISSION.md`; `MODULE_INDEX.md` →
`RESEARCH-ROADMAP.md` e `RESEARCH-INDEX.md`; `DECISIONS.md` → `decisions/`; `JOURNAL.md`
→ `RESEARCH-CHANGELOG.md`; `HANDOFF.md` → não existe, e não será criado.

## 5. Quando cada uma é acionada

| Momento | Skill | Gatilho objetivo |
|---|---|---|
| 1. Receber o objetivo | `lia-agent-orchestration` | todo pedido novo |
| 2. Identificar a necessidade | `lia-agent-orchestration` + `lia-project-resume` | necessidade não é a mesma coisa que o pedido literal |
| 3. Escopo, exclusões, critério de conclusão | `lia-agent-orchestration` | rodada sem critério de conclusão não abre |
| 4. Dividir em tarefas | `lia-agent-orchestration` | só quando há mais de um caminho de escrita ou mais de uma etapa |
| 5. Investigar e reunir evidência | `governance/INVESTIGATION-PROTOCOL.md` (A–E) | protocolo do repositório prevalece |
| 6. Avaliar alternativas e limites | `lia-regression-investigation` | divergência entre fontes ou correção de rodada anterior |
| 7. Consolidar e recomendar | `lia-game-test-evidence-review` | antes de publicar qualquer conclusão |
| 8. Registrar conhecimento reutilizável | `RESEARCH-CHANGELOG.md` + índice | conhecimento, não contagem de linhas |
| 9. Encerrar | `lia-agent-orchestration` | critério de conclusão atingido, ou parada por escopo |

## 6. O que cada desvio recorrente passa a ter como barreira

| Desvio | Barreira |
|---|---|
| perder o objetivo em investigação longa | brief de 8 campos com objetivo em uma frase verificável, reescrito no topo do relatório |
| expandir além do escopo | escopo negativo obrigatório na abertura + regra "saiu do conjunto, para e reporta" |
| repetir auditoria já feita | abertura com `lia-project-resume` a partir do índice e do changelog; achado anterior é citado, não refeito |
| gastar esforço na manutenção do catálogo | critério de conclusão precisa declarar o **conhecimento** produzido; renumerar seção não é resultado |
| abrir rodada para corrigir detalhe secundário | capacidade por evidência: sem causa identificada, ambiguidade cara ou risco de perda, não abre rodada nova |
| documentação sem resultado útil | retorno de 6 campos com "o que mudou na decisão do proprietário"; se nada muda, a rodada foi manutenção e deve ser dita assim |

## 7. Rejeitadas — e por quê

| Skill | Motivo da rejeição |
|---|---|
| `lia-module-planning` | escrita para projeto de jogo (`GDD.md`, `MODULE_INDEX.md`, "Dev"); duplica a Fase A da metodologia |
| `lia-test-discipline` | os comandos do Research já estão fixados em `governance/TESTING-PROTOCOL.md`; as trilhas Node/pnpm/Vitest citadas não existem aqui |
| `lia-task-handoff` | pressupõe outro executor; o Research publica em changelog e índice |
| `lia-agent-evaluation` | exige credencial de provedor; no Arena seria `BLOCKED`; a regra de uma variável já está em `lia-regression-investigation` |
| `lia-safe-change` | governa alteração de código; o Research não altera código de produto |
| `lia-game-design-review` | revisa GDD; o análogo do Research já é `agents/REVIEW-PROTOCOL.md` |
| `alethe` | exige CLI instalada e autenticada; instalação proibida nesta atividade; orquestração multi-worker não é o gargalo |
| `lia-brand-check`, `lia-brand-consistency-review` | escopo de marca do produto, não de pesquisa |
| 9 de `Lia-Model-Lab` e 1 de `Lia-Forge` | repositórios inacessíveis (`404`); não se adota o que não se pode ler |

## 8. Limitações de compatibilidade

1. **Sem runtime.** Nada é carregado automaticamente; toda aplicação é leitura e adesão
   manual, verificável no relatório mas não provada por execução.
2. **Commit de branch, não de `main`.** Nenhuma das Skills existe em `main` de
   `Lia-Project` nem de `Lia-Studio`; os commits pinados acima podem desaparecer quando a
   branch for limpa. Promover as quatro a `main` é decisão dos donos desses repositórios —
   fora do escopo desta pesquisa.
3. **Instrução em português com vocabulário de jogo.** `Dev`, `Task`, `gate` e `GDD`
   precisam de tradução para o vocabulário do Research; tradução feita no §4, não no arquivo
   de origem (que não foi modificado).
4. **Rótulos diferentes.** A Skill de evidência usa `ADEQUADA/INCOMPLETA/AUSENTE/NÃO
   AVALIADA`; o Research usa seis rótulos. O mapeamento do §4.3 é a única ponte autorizada.
5. **Licença.** `Lia-Studio` e `Lia-Project` são MIT na raiz, mas 47 das 48 Skills não têm
   licença dentro do payload — a leitura aqui é de método, sem cópia de conteúdo para este
   repositório.

## 9. Como isto foi aplicado nesta atividade

| Passo | Aplicação concreta |
|---|---|
| 1–3 | objetivo virou pergunta verificável ("que Skills do Hub existem, quais são legíveis e qual conjunto mínimo serve ao Research"), com escopo negativo explícito: não criar Skill, não alterar o Hub, não reabrir as rodadas 7.x, não pesquisar tecnologia nova |
| 4 | divisão em quatro frentes: catálogo, instruções, verificação de disponibilidade, redação do protocolo |
| 5 | leitura do catálogo no branch do Hub e de 10 `SKILL.md` nos repositórios de origem, com commit e hash registrados |
| 6 | divergência entre "listada no catálogo" e "utilizável" resolvida por teste de acessibilidade por repositório, não por suposição |
| 7 | nenhuma Skill declarada utilizada sem leitura do arquivo; as 10 restantes do ecossistema ficam como descrição |
| 8 | este documento |
| 9 | encerrado sem criar Skill, sem instalar nada e sem tocar em outro projeto Lia |

Voltar: `agents/README.md` · `governance/RESEARCH-METHODOLOGY.md`
