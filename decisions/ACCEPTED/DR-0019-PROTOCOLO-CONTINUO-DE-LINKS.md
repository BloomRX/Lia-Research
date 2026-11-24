# DR-0019 — Protocolo contínuo de investigação de links (determinação do proprietário)

| Campo | Valor |
|---|---|
| ID | DR-0019 |
| Estado | **ACCEPTED** (determinação do proprietário, 2026-11-24) |
| Decisor | proprietário BloomRX |
| Data da decisão | 2026-11-24 (mensagem "LIA RESEARCH — PROTOCOLO CONTÍNUO DE INVESTIGAÇÃO DE LINKS", §1–§8) |
| Alcance | **GOVERNANCA** — método e escopo de autoridade do Research; **não** aprova adoção de tecnologia em nenhum app |
| Pesquisas relacionadas | todos os 42 objetos de `repositories/*/REPORT.md`; em especial `LR-FORGE-017`, `LR-VOICE-003`, `LR-MCP-004` (leva do mesmo dia, que já seguiu este formato) |
| Onde é aplicado | `governance/INVESTIGATION-PROTOCOL.md` (operação) · `MISSION.md` §3 (limite de autoridade, já vigente) · `templates/` (formatos existentes, sem criação de novo template) |
| Reversível? | sim — é protocolo de método; reverter não invalida relatórios nem evidências já registrados |

---

## 1. Contexto

A determinação foi enviada logo depois da leva de oito links (27 + 123 repositórios contados +
seis repositórios), e de uma instrução anterior do mesmo dia: *"mantenha só suas diretrizes; os
outros apps, vou decidir se é possível implementar neles"*. O protocolo formaliza a segunda frase
como regra permanente e acrescenta exigências que a base já vinha praticando sem ter escrito:
entrada de link sem briefing, profundidade proporcional, separação explícita entre documentado ×
testado × incerto × bloqueado, vedação de documento por link, e o formato de resumo de rodada em
nove itens.

## 2. Evidência considerada

| Fonte | Conclusão usada | Confiança |
|---|---|---|
| Mensagem do proprietário, §1–§8 (2026-11-24) | o texto do protocolo é a norma; este DR registra, não reescreve | Alta |
| `MISSION.md` §3 | "O Research não aprova nada" já era canônico; o §3 do protocolo o reafirma e amplia para "recomendação não é autorização de implementação" | Alta |
| `governance/INVESTIGATION-PROTOCOL.md` (prévio) | Etapas A–E + anti-padrões; faltava a Etapa 0 (entrada), o formato de resumo e a fronteira de experimentação | Alta |
| Vocabulário em `tools/validate.py:20-37` | `STATES`/`EXEC` da casa não contêm `UNVERIFIED`; contêm `UNVALIDATED` (nos rótulos de evidência) e `NOT_RUN`/`BLOCKED` (no resultado de execução) → exigiu reconciliação, §4.3 abaixo | Alta (medido no código) |
| Vocabulário em `governance/TESTING-PROTOCOL.md` | níveis 1/2/3 de teste, com o nível 3 exigindo autorização específica — é o mecanismo que implementa o §4 e o §6 do protocolo do dono | Alta |

## 3. Alternativas consideradas

| Alternativa | Por que não |
|---|---|
| Copiar o protocolo inteiro como documento novo em `governance/` | duplicaria a Etapa A–E e criaria duas normas para o mesmo ato; o §5 do próprio protocolo manda usar a estrutura existente |
| Reescrever `MISSION.md` com o texto | a missão é curta e estável; método pertence ao protocolo de investigação |
| Ignorar, porque "já fazemos isso" | três pontos **não** estavam escritos: formato de resumo de 9 itens, vedação de criar documento por link, e a reconciliação de rótulos (`UNVERIFIED` vs `UNVALIDATED`) — que é exatamente onde relatório e validador divergiriam |

## 4. Decisão

**O protocolo do proprietário entra em vigor como método permanente da base, aplicado
automaticamente a todo link futuro, sem nova solicitação.** Detalhamento do escopo exato:

### 4.1 Entrada (§1)
Nenhum briefing é exigido. Um link, vários links, ou só o nome de uma tecnologia bastam. A
identificação (projeto, versão, commit) vem antes de qualquer julgamento; com vários links, o
relatório diz se são relacionados, complementares, concorrentes ou independentes. Pergunta ao dono
só quando a informação for indispensável e a medição não resolver.

### 4.2 Profundidade proporcional (§2)
Não há piso obrigatório de itens por objeto, mas há tetos de honestidade: capacidade documentada
nunca aparece como testada; requisito de hardware, custo, dependência externa, licença e risco são
declarados ou marcados como não verificados.

### 4.3 Rótulos — equivalência adotada
O §2 do protocolo nomeia cinco estados. Nesta base o vocabulário já existe e é verificado por
máquina, então a tradução fica fixada aqui:

| Termo do protocolo | Forma canônica nesta base |
|---|---|
| `DOCUMENTED` | `Estado da pesquisa = DOCUMENTED` (e rótulo de evidência `CONFIRMED`/`REPORTED` conforme a fonte) |
| `TESTED` | `Estado = TESTED` + `Resultado de execução = LOCAL_TESTS_PASS`/`LOCAL_SMOKE_PASS` + **linha obrigatória** em `data/testing/test-log.tsv` |
| `PARTIALLY_TESTED` | `Estado = PARTIALLY_TESTED` + `Resultado = PARTIAL` + linha no test-log dizendo **o que não foi** testado |
| `UNVERIFIED` | rótulo de evidência `UNVALIDATED` (afirmação sem comprovação nossa); se a verificação era possível e não foi feita, `NOT_RUN` |
| `BLOCKED` | `Resultado de execução = BLOCKED` (ou `Estado = BLOCKED` quando o impedimento é de acesso) com a **limitação nomeada** — sem limitação medida, não se usa `BLOCKED` |

A distinção operacional, que o protocolo pede e o validador cobra: `NOT_RUN` = "poderia ter sido
feito aqui e não foi" (dívida desta base, assumida em texto); `BLOCKED` = "há uma limitação
medida que impede" (falta de ferramenta, 404, custo, conta, ambiente).

### 4.4 Descoberta antes de cadastro (§4)
"Não transformar toda investigação em simples cadastro de catálogo" passa a critério de
qualidade da rodada: uma rodada sem capacidade nova identificada, sem alternativa melhor para um
problema conhecido, ou sem experimento viável indicado, está incompleta — mesmo que tenha
registrado todos os links.

### 4.5 Fronteira de experimentação (§4, §6)
Experimento controlado é permitido e desejado, dentro destes limites, que nesta base já são prática
medida: nada de instalar dependência em projeto Lia; nada de baixar peso grande; nada de serviço
pago, crédito, conta ou envio de dado proprietário. Ferramentas auxiliares de medição podem ser
instaladas **no sandbox de pesquisa**, em diretório temporário, quando o teste é do próprio objeto
(precedente desta data: `pnpm 10.30.1` global no sandbox e um `venv` com `pytest`+`pyyaml` em
`/tmp` para executar os verificadores internos de `open-seo` e do `VoiceStudio`). Cada execução
assim entra no test-log com ambiente e procedimento descritos, para ser reproduzível.

### 4.6 parcimônia documental (§5)
Não se cria documento por link. Um link pode resultar em: uma linha de inventário, uma linha nova
num digest existente, uma retificação num relatório antigo, ou nada registrado — o critério é se
há evidência que mude o que a base sabe. Se o objeto já foi investigado, recupera-se o registro e
procura-se **novidade ou lacuna relevante**, sem repetir o trabalho.

### 4.7 Resumo de rodada em nove itens (§7)
Identificação · Descoberta · Capacidades · Evidências · Relevância para Lia (sem determinar adoção)
· Limitações · Resultado · Registro · Continuidade (uma única próxima ação útil; sem etapas
artificiais). Este é o formato padrão da resposta ao dono ao fim de cada leva, e está escrito em
`governance/INVESTIGATION-PROTOCOL.md` para não depender da memória da conversa.

### 4.8 Autonomia interna (§6)
Ajustes de baixo risco na própria base — vocabulário do validador, formato de índice, catálogo,
templates, `agents/`, governança — são aplicados sem interromper o dono para pedir permissão caso a
caso, com registro no `RESEARCH-CHANGELOG.md`. O que ultrapassa a fronteira (mexer em outro repo,
publicar, integrar, gastar, sobrescrever trabalho alheio, reescrever histórico) é registrado como
oportunidade + decisão pendente, e para aí.

## 5. Fora de escopo

Esta decisão **não** autoriza o Research a: adotar, integrar, instalar, forkear ou modificar
qualquer outro app do ecossistema; decidir se uma capacidade é viável em Lia Project, Lia Forge,
Lia Studio, Lia Agent Hub ou Lia Model Lab; assumir custo, conta ou obrigação legal; alterar
branches, commits ou histórico de terceiros. Ela também **não** reabre nenhuma recomendação
existente: os rótulos `ADAPT`/`REFERENCE_ONLY`/`REJECT` dos 42 objetos continuam válidos como
opinião técnica, e muda-lhes o conteúdo exige evidência nova.

## 6. Consequências

- **Positivas**: o método deixa de depender do texto de uma conversa; o validador passa a ter
  correspondência oficial com os rótulos do dono; a exigência de descoberta impede rodada de
  puro-cadastro; a autonomia interna elimina idas-e-vindas por ajuste trivial.
- **Negativas**: um resumo de nove itens por rodada é mais longo que o parágrafo que o dono às vezes
  queria; a fronteira de experimentação exige escrever o ambiente de cada execução (mais uma coluna
  mental no test-log).
- **Dívida criada**: os 42 relatórios anteriores não foram reescritos para o formato de nove itens —
  o formato é de *resumo de rodada*, não de relatório, então não há retrabalho; e `templates/` ganha
  por ora apenas um lembrete no `README.md` da pasta, não um template novo.

## 7. Condição de reversão

Revisão se o dono: (a) passar a querer briefing estruturado por link; (b) decidir que resumo de
rodada deve ser uma ou duas linhas; (c) transferir para o Research a decisão de viabilidade em algum
app específico; (d) autorizar permanentemente experimentos que hoje exigem pedido (por exemplo, baixar
peso médio em `/tmp` para medir). Nada disso está vedado — só não é escolha desta base.

## 8. Gates de implementação

| Gate | Critério de aprovação | Dono |
|---|---|---|
| Escrita do protocolo na Etapa 0 + seções novas | `governance/INVESTIGATION-PROTOCOL.md` lido e coerente com `MISSION.md` §3; validador 0 erros | Research (esta base) |
| Equivalência de rótulos sem quebrar o validador | `tools/test_validate.py` (78) OK e `validate.py` com 0 erros/0 avisos no repositório real | Research |
| Adoção do resumo em 9 itens | a partir da próxima rodada; esta já usa | Research |
| Experimentos com dependência no sandbox | nível 1/2 conforme `governance/TESTING-PROTOCOL.md`, com ambiente declarado no test-log | Research (dentro do §4.5) |
| Qualquer efeito em outro app | decisão + implementação do responsável do app | **proprietário** |
