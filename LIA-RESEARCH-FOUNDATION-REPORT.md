# LIA-RESEARCH — Relatório de Fundação

| Campo | Valor |
|---|---|
| Versão | 1.0 |
| Data | 2026-11-17 |
| Repositório | `BloomRX/Lia-Research` — branch `arena/7cf9c65e-lia-research` |
| Autor | Research Orchestrator (agente), sob ordem de serviço do proprietário |
| Escopo | fases 0–3 da ordem de serviço (§14) |
| Status global | **PASS com 1 bloqueio** (visibilidade privada) e 6 lacunas declaradas |

---

## 1. Sumário

Esta base existe para uma pergunta só: **quando alguém — humano ou agente — precisar
decidir algo sobre a Lia, existe um lugar onde a evidência já foi reunida, datada,
classificada e ligada à origem?**

Hoje: sim, para 16 tecnologias externas, 5 projetos internos e 21 temas transversais.
Não, para desempenho: **nada foi executado, nenhum modelo foi medido, nenhuma
compatibilidade de hardware foi provada**.

O achado mais consequente da fundação não é sobre tecnologia de terceiro. É interno:

> **48 Skills catalogáveis no ecossistema, 0 com licença dentro do payload.** E 44
> modelos catalogados, 0 validados no hardware real.

Duas afirmações que qualquer catálogo faria automaticamente e que, hoje, seriam falsas.

## 2. O que foi entregue

| Área | Entrega | Volume |
|---|---|---:|
| Governança | 8 documentos (método, evidência, licença, segurança, preservação, status, contribuição) | 8 |
| Templates | 9 modelos, incluindo avaliação em 18 seções | 9 |
| Agentes | orquestrador, especialistas, workflow, publicação, revisão | 5 |
| Ecossistema | mapa, propriedade, capacidades, tecnologia compartilhada | 4 |
| Projetos | 5 dossiês (`README` + `INDEX`) | 10 |
| Pesquisa externa | 16 relatórios + 4 derivados do HA-MCP | 20 |
| Transversal | digests com dedup e ponteiro para origem | 21 |
| Comparações | licença, MCP, benchmark | 4 |
| Decisões | 13 abertas, 3 rejeições, 2 referência, 2 pastas vazias por desenho | 18 |
| Dados | inventário, manifesto com hash, alvos pinados, snapshot | 7 |
| Ferramentas | `tools/validate.py` + 3 scripts de coleta | 4 |
| GitHub | PR template + 3 issue templates | 4 |

Total: **113 arquivos Markdown** verificados por `tools/validate.py`, 0 erros.

## 3. Método em uma página

1. **Varredura do ecossistema** por Trees API (não por clone: clone blobless pendura).
   58.478 arquivos, 43 branches, 1.620 documentos distintos.
2. **Dedup obrigatório** antes de qualquer pesquisa nova: consultar a pesquisa interna
   de cada projeto (§2 de `agents/AGENT-WORKFLOW.md`). Dos 16 alvos externos, nenhum
   repetia tema já coberto.
3. **Coleta com pin**: SHA do commit, data, licença lida **no arquivo** (nunca no badge),
   tamanho do repo, maturidade.
4. **Classificação de evidência** por afirmação: CONFIRMED / OBSERVED / REPORTED /
   INFERRED / UNVERIFIED / BLOCKED.
5. **Veredito de pesquisa**, não de adoção: ADOTAR / ADAPTAR / REFERÊNCIA / REJEITAR /
   PENDENTE — sempre sobre "vale como conhecimento", nunca "vamos implementar".
6. **Publicação de dono único**: cada conhecimento mora em um caminho. O resto aponta.
7. **Validação automática**: títulos, segredos, diretórios vazios, caminhos, IDs,
   estrutura de relatório, listagem de decisões.

## 4. Status por fase (§14 da ordem de serviço)

| Fase | Objetivo | Status | Evidência |
|---|---|---|---|
| 0 | Estrutura e governança | **PASS** | 9 pastas, 8 docs de governança, 9 templates |
| 1 | Inventário dos 5 projetos | **PASS** | 58.478 arquivos, 1.620 docs, 645 Lia, 975 vendorizados |
| 2 | Auditoria dos 16 alvos externos | **PASS** | 16 relatórios com SHA pinado e licença lida |
| 3 | Consolidação transversal | **PASS** | 21 digests, 4 comparações, 3 decisões tomadas |
| 4 | Medição e validação | **NOT RUN** | exige execução na máquina do usuário |
| 5 | Revisão e entrega | **PASS parcial** | falta revisão humana (`agents/REVIEW-PROTOCOL.md`) |
| — | Visibilidade privada | **BLOCKED** | `403` na API; ver `DR-0006` |

`NOT RUN` e `BLOCKED` **não** são PASS. A fase 4 é a razão pela qual nenhuma
recomendação desta base passa de `ADAPTAR`/`REFERÊNCIA`.

## 5. Cinco achados que mudam decisão

### 5.1 Zero licença em 48 Skills
Nenhum payload de Skill do ecossistema contém licença. Declarar autoria não concede
direito de distribuição. O importador do Hub detecta licença só na raiz do payload:
as 47 entrariam como `licenseKnown: false`. Não é bug, é ausência de decisão (`DR-0001`).

### 5.2 Zero modelo validado
44 registros de modelo, ~131 descobertos, 0 medidos. Toda escolha de modelo hoje é
ficha técnica de terceiro. A bancada existe (`tools/desktop-benchmark`) e não rodou.

### 5.3 O risco residencial não está no nome da tool
Um gate por nome de ferramenta é contornável: `ha_call_service(domain="lock")` executa
qualquer serviço. O risco mora no par (domínio, serviço) — daí a matriz R0–R3 por
domínio, e não uma lista de tools proibidas.

### 5.4 Automação de casa e desktop são riscos incomparáveis
Desligar uma luz e apagar um arquivo não pertencem à mesma escala. Tratar tudo como
"tool com permissão" achata o risco e produz política que não protege nada.

### 5.5 Dois catálogos de modelo, duas avaliações de LFM3, nenhum dono
O ecossistema tem autoridade duplicada sobre "qual modelo". Não é contradição de fato;
é ausência de dono. Registrado como `CONFLICTING` e endereçado em `M-1`, não resolvido.

## 6. O que esta fundação **não** fez (e por quê)

| Não feito | Motivo | Onde está registrado |
|---|---|---|
| Implementar qualquer tecnologia pesquisada | proibido pela ordem de serviço | `governance/RESEARCH-GOVERNANCE.md` |
| Medir desempenho | exige a máquina do usuário | fases 4, `RESEARCH-ROADMAP.md` H-1 |
| Conceder licença às Skills | exige titular | `DR-0001` |
| Tornar o repositório privado | bloqueado por permissão (403) | `DR-0006` |
| Consolidar versões divergentes de docs de projeto | decisão e trabalho do projeto | `projects/lia-model-lab/README.md` §5 |
| Pesquisar visão/multimodal como tema | sem fonte e sem espaço para pesquisa real | `RESEARCH-ROADMAP.md` R-4 |
| Copiar código de terceiro | proibido; só ponteiro + SHA | `governance/SOURCE-PRESERVATION-POLICY.md` |

## 7. Riscos da própria base

| Risco | Severidade | Mitigação |
|---|---|---|
| Repositório público com conteúdo que se pretendia privado | **alta** | nada sensível foi commitado; validado por `tools/validate.py`; `DR-0006` aberto |
| Base desatualiza e passa a mentir com confiança | alta | campo `Próxima revisão` por documento; `RESEARCH-CHANGELOG.md` |
| Vira dependência de runtime dos projetos | média | regra de independência em `ecosystem/PROJECT-OWNERSHIP.md` |
| Digest virar fonte e divergir do original | média | cada digest aponta origem + commit; original é canônico |
| Snapshot antigo ser citado como estado atual | média | `data/README.md` §2 declara o snapshot como prova do passado, não fonte |
| Crescer com pesquisa rasa para "cobrir tema" | alta | lacuna declarada é aceita; `archive/incomplete/` existe para isso |

## 8. Recomendação final

A base está pronta para uso como **referência de decisão**, não como especificação de
implementação. O próximo trabalho de maior alavancagem não é pesquisar mais: é
**decidir as 13 pendências** — três delas (DR-0001, DR-0006, DR-0008) destravam quase
todo o resto.

## 9. Auditoria deste documento

| Verificação | Resultado |
|---|---|
| Todo número citado existe em documento desta base | sim (ver `RESEARCH-INDEX.md`) |
| Nenhuma conclusão apresentada como medida | sim — 0 medições no repositório |
| Nenhum veredito de adoção | sim — 0 `ACCEPTED`, 0 `ADAPTED` |
| `python3 tools/validate.py` | 0 erros, 0 avisos |
