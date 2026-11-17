# Plano de implementação futura — integração residencial

| Campo | Valor |
|---|---|
| ID | `LR-MCP-001-D` |
| Tipo | Plano (não executado) |
| Estado | `NOT RUN` — bloqueado por `DR-0003` |
| Data | 2026-11-17 |
| Estimativa | 4–6 semanas de trabalho assistido, em 5 fatias |

> **Nada deste plano foi executado.** Ele existe para que a decisão `DR-0003` seja
> tomada com custo visível. A ordem de serviço proíbe implementar a integração nesta
> etapa.

---

## 1. Pré-condições (sem elas, não começa)

| # | Pré-condição | Estado |
|---|---|---|
| P1 | `DR-0003` = ACCEPTED | `PENDENTE` |
| P2 | `RISK-MATRIX.md` aprovada (`DR-0008`) | `PENDENTE` |
| P3 | `MCP-CONTRACT.md` v0.1 congelado | proposta pronta |
| P4 | Instância de HA de teste (não a casa real) | `NOT RUN` |
| P5 | Revisão de segurança independente | `NOT RUN` |

## 2. Fatias

### Fatia 0 — Bancada (3–4 dias)

Objetivo: provar que o HA-MCP responde, sem tocar em produto.

- HA em container com 6 entidades sintéticas: 1 light, 1 switch, 1 sensor, 1 lock,
  1 camera, 1 automation.
- HA-MCP via `uvx` stdio, versão pinada.
- Cliente MCP de teste (script), 5 comandos: ler estado, listar, ligar, desligar, ler histórico.
- **Critério de saída:** 5/5 com log de requisição e resposta; nenhuma escrita no repo do produto.

### Fatia 1 — Broker mínimo (1 semana)

- Registro de adaptador e de capabilities (sem UI).
- Gate R0/R1 em memória.
- Auditoria em arquivo local.
- **Critério:** teste que prova bloqueio de `lock.unlock` em conexão A.

### Fatia 2 — Duas conexões (3–4 dias)

- Conexão A `/readonly` permanente; conexão B elevada sob demanda com expiração.
- Teste: com B fechada, nenhuma escrita passa (incluindo via cache e search proxy).
- **Critério:** 100% das tentativas de escrita em A bloqueadas e logadas.

### Fatia 3 — UX de consentimento (1–2 semanas)

- Modal R1 (com "lembrar por dispositivo"), R2 (sem lembrar, TTL 30 s), R3 (digitar confirmação).
- Estado "aguardando confirmação" visível no Stage.
- **Critério:** teste de usabilidade com 5 fluxos; nenhum R2 executável sem modal.

### Fatia 4 — Cache de entidades e resolução de linguagem (1 semana)

- Cache `entity_id → nome, área, domínio`; resolução de "luz do quarto".
- Tratamento de ambiguidade (pergunta, não chute).
- **Critério:** 20 frases de teste, ≥ 18 resolvidas corretamente, 0 execuções erradas.

### Fatia 5 — Hardening e revisão (3–5 dias)

- Revisão de segurança independente obrigatória.
- Teste de injeção de prompt via nome de dispositivo.
- Teste offline (derrubar internet, manter LAN).
- **Critério:** parecer aprovado; nenhum achado alto aberto.

## 3. Ordem e dependências

```text
Fatia 0 ──► Fatia 1 ──┬─► Fatia 2 ──► Fatia 3 ──► Fatia 5
                      └─► Fatia 4 ──┘
```

Fatias 2 e 4 podem correr em paralelo após a 1. Fatia 3 depende de 1 e 2.

## 4. O que fica fora

- Múltiplas casas, múltiplos usuários com permissões diferentes.
- Integração com Zigbee/Z-Wave direto (sem HA).
- Automação "aprendida" (a Lia criar automações sozinha).
- Voz como gatilho de R2/R3 (exigiria autenticação de locutor — pesquisa separada).
- Distribuição da integração a usuários finais (requer `DR-0001` e auditoria de licença).

## 5. Riscos de execução

| Risco | Mitigação |
|---|---|
| HA-MCP muda contrato no meio | pin + teste de contrato na CI |
| Casa real usada em teste | proibido; só HA de bancada |
| Pressão para "só liberar a fechadura rapidinho" | matriz R2 sem exceção; exceção exige DR novo |
| Escopo crescendo para "controle total do HA" | catálogo fixo de 12 capabilities na v1 |
| Timeout em R2 gerando ação duplicada | `TIMEOUT_UNKNOWN_STATE` + consulta de estado |

## 6. Métricas de sucesso

| Métrica | Meta |
|---|---|
| Latência p95 de `home.state.read` na LAN | < 400 ms |
| Latência p95 de `home.light.set` | < 800 ms |
| Execuções R2 sem confirmação registrada | **0** |
| Ações executadas em entidade errada | **0** |
| Conversas degradadas por HA offline | 0 (mensagem clara, conversa continua) |

## 7. Estado do plano

`NOT RUN`. Próxima ação possível sem decisão: **nada** — as fatias exigem P1 e P4.
A alternativa útil agora é pesquisa complementar: comparar com o MCP nativo do HA
(~15 tools) para confirmar que ele é insuficiente, e medir a latência real na LAN do
usuário quando houver bancada.
