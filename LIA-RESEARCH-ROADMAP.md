# LIA-RESEARCH — Roadmap da Base

| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| Horizonte | 12 meses (4 trimestres) |
| Fonte de verdade do detalhe | `RESEARCH-ROADMAP.md` (itens com critério de conclusão) |
| Este documento | visão de sequência, dependências e critério de parada |

---

## 1. Diagnóstico que ordena o roadmap

A base tem **profundidade documental** e **ausência de medição**. Portanto o roadmap não
é "pesquisar mais temas": é converter conhecimento em decisão e decisão em número.

```text
documento  →  decisão  →  protótipo  →  medição  →  status CONFIRMED
   (feito)     (falta)      (falta)      (falta)        (zero hoje)
```

Tudo que não avança nessa cadeia é vaidade bibliográfica.

## 2. Trimestre 1 (nov–jan) — Decidir e desbloquear

| Item | Entrega | Depende de | Status |
|---|---|---|---|
| Privacidade do repositório | `"private": true` | proprietário | BLOCKED (403) |
| `DR-0001` licença das Skills | arquivo de licença por Skill | titular | PENDING |
| `DR-0008` matriz de risco | política aceita | proprietário | PENDING |
| `DR-0002` acesso de agentes | política de leitura/escrita | proprietário | PENDING |
| `M-3` matriz capability × provider | documento novo | nenhum | **pronto** |
| `L-4` auditoria das 29 skills AIRI + `alethe` | relatório `LR-LIC-003` | nenhum | **pronto** |
| `A-3` spec de manifesto de workflow | draft de spec | `DR-0001` | pronto para escrever |

**Critério de saída do trimestre:** três DRs fechados e nenhuma Skill `lia-*` sem
situação de licença declarada.

## 3. Trimestre 2 (fev–abr) — Medir

| Item | Entrega | Depende de |
|---|---|---|
| `H-1` benchmark Vulkan × CPU na RX 580 | primeira tabela de desempenho real | máquina |
| `M-2` bancada em 3 modelos | 3 registros `VALIDATED` | `H-1`, `DR-0014` |
| `H-3` pico de VRAM com Stage | o número que decide "cabe" | `H-1` |
| `U-1`/`U-2` protótipo Vercel UI + comparação | decisão de UI baseada em medição | beta terms lidos |
| `A-1` protótipo HA-MCP com 5 comandos R0/R1 | prova de conceito isolada | `DR-0008` |

**Critério de saída:** existir pelo menos **um** número de desempenho `CONFIRMED` na
base. Hoje não existe nenhum.

## 4. Trimestre 3 (mai–jul) — Decidir com número

| Item | Entrega |
|---|---|
| `M-1` catálogo canônico de modelo | um dono, uma tabela, decisão datada |
| `DR-0003` adaptador residencial | decisão com base em `A-1` |
| `L-2` registro de proveniência de asset | proposta executável para o Forge |
| `A-4` permissão com escopo por execução | spec + protótipo |
| `U-3` hábito de ADR de UI | primeiros 3 ADRs do produto |

## 5. Trimestre 4 (ago–out) — Consolidar e podar

| Item | Entrega |
|---|---|
| Revisão trimestral de todos os documentos `CURRENT` | status atualizado ou `STALE` |
| Auditoria de peso da base | o que ninguém citou em 6 meses → `archive/superseded` |
| `DR-0007` Skills duplicadas resolvidas | catálogo sem sobreposição |
| Revisão de licença de todos os artefatos distribuíveis | 0 payload sem NOTICE |
| Retrospectiva: a base evitou trabalho? | métrica de uso, não de volume |

## 6. Dependências (o que destrava o quê)

```text
DR-0006 (privado) ──► política de segurança plena
DR-0001 (licença)  ──► A-3 (manifesto) ──► distribuição de Skill no Hub
DR-0008 (risco)    ──► A-1 (protótipo) ──► DR-0003 (decisão residencial)
H-1 (benchmark)    ──► M-2 (modelos validados) ──► DR-0014 (critério) ──► M-1 (catálogo)
L-4 (AIRI)         ──► DR-0001 (escopo do que é Lia)
```

## 7. O que este roadmap exclui de propósito

| Excluído | Por quê |
|---|---|
| Pesquisar mais 16 repositórios | profundidade já excede a capacidade de decisão |
| Criar `cross-project/vision/` | sem fonte e sem espaço para pesquisa real (`R-4`) |
| Escrever especificação de produto | a base não declara arquitetura |
| Implementar qualquer coisa | proibido pela ordem de serviço |
| Migrar para outra ferramenta de documentação | o problema não é a ferramenta |

## 8. Métrica de sucesso da base (não é volume)

| Métrica | Hoje | Meta T4 |
|---|---|---|
| Perguntas respondidas em ≤2 consultas | estimado 80% | ≥95% |
| Pesquisas duplicadas criadas | 0 (dedup aplicado) | 0 |
| Afirmações de desempenho sem medição publicadas | 0 | 0 |
| Decisões abertas | 13 | ≤4 |
| Skills com licença declarada | 0/48 | 48/48 |
| Modelos validados | 0/44 | ≥3 |
| Artefatos distribuíveis sem NOTICE | 17 estimados | 0 |

## 9. Condição de parada

A base **não** deve crescer indefinidamente. Sinais de que deve parar de pesquisar e
começar a executar:

1. a mesma pergunta é respondida pelo índice há 3 meses sem novo dado;
2. existe documento citando outro documento desta base, sem fonte externa nova;
3. uma decisão está aberta há mais de um trimestre e ninguém a bloqueou tecnicamente.

Nesses casos, o próximo passo não é pesquisa: é decisão.
