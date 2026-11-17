# Proposta de arquitetura — Lia + Home Assistant (opcional)

| Campo | Valor |
|---|---|
| ID | `LR-MCP-001-A` |
| Tipo | Proposta arquitetural (**não** implementação) |
| Estado | `PENDENTE` — aguarda `DR-0003` |
| Data | 2026-11-17 |
| Base | `LR-MCP-001` |

> Esta proposta descreve o que seria construído **se** a decisão `DR-0003` for
> `ACCEPTED`. Nada aqui foi implementado. Nenhuma dependência foi adicionada.

---

## 1. Princípio central

O Core da Lia **não conhece** Home Assistant. Conhece o broker de ferramentas, que
conhece adaptadores, dos quais um é o HA-MCP. Desligar a integração não deve alterar
nenhuma linha do Core.

```text
┌──────────────────────────────────────────────────────────────┐
│  Lia-Project — experiência conversacional                    │
│  intenção → capability → consentimento → feedback            │
└───────────────────────┬──────────────────────────────────────┘
                        │ capability request (não "call tool")
                        ▼
┌──────────────────────────────────────────────────────────────┐
│  Lia — Tool Broker  (já existe embrionário: autorização de   │
│  tools por capability)                                       │
│  ├─ política de risco (R0–R3)                                │
│  ├─ consentimento (modal / regra persistida)                 │
│  ├─ auditoria (quem, o quê, intenção, resultado)             │
│  └─ adaptadores registrados                                  │
└───────────────────────┬──────────────────────────────────────┘
                        │ MCP (stdio ou HTTP/readonly)
                        ▼
┌──────────────────────────────────────────────────────────────┐
│  Adapter: home-assistant                                     │
│  ├─ conexão A: /readonly   (consultas, R0)                   │
│  └─ conexão B: elevada     (R1–R3, criada sob demanda)       │
└───────────────────────┬──────────────────────────────────────┘
                        ▼
┌──────────────────────────────────────────────────────────────┐
│  HA-MCP server (externo, MIT, versionado)                    │
└───────────────────────┬──────────────────────────────────────┘
                        ▼
              Home Assistant (dispositivos, automações)
```

Responsabilidades, conforme a ordem de serviço:

| Camada | Responsável por | Não é responsável por |
|---|---|---|
| Lia-Project | experiência, consentimento, interface, feedback | protocolo MCP, política de dispositivo |
| Tool Broker (Lia) | risco, permissão, auditoria, descoberta | transporte MCP |
| Lia Agent Hub | registro/descoberta/catálogo do servidor MCP, versionamento de contrato | execução, consentimento |
| HA-MCP | tradução MCP ↔ API do HA | política de risco, identidade do usuário Lia |
| Home Assistant | estado dos dispositivos, automações, histórico | conversa |

## 2. Por que duas conexões

O HA-MCP oferece `readonly` por URL (`CONFIRMED`). Duas conexões resolvem o problema
central — "consultar é barato, agir é caro" — sem construir um proxy:

| Conexão | Endpoint | Catálogo | Uso |
|---|---|---|---|
| A — consulta | `<base>/<secret>/readonly` (ou `/catalog/search/readonly`) | tools de leitura | padrão do assistente; sempre ativa |
| B — ação | `<base>/<secret>` | tools completas | criada quando o usuário autoriza uma ação; expira |

Ganho: o catálogo que o LLM vê por padrão **não contém** `ha_call_service`. Uma
alucinação não tem ferramenta para executar. Isso é mais forte do que instruir o
modelo a "pedir permissão".

Limite honesto: `/readonly` protege contra escrita, não contra **leitura sensível**
(`ha_get_camera_image`, `ha_get_logs`). Essas precisam de controle próprio (§4).

## 3. Contrato de capability (não de tool)

A Lia não deve expor `ha_call_service` ao modelo. Deve expor capabilities com
semântica de produto:

```yaml
capability: home.light.set
params: { area: string, state: on|off, brightness?: 0..100 }
maps_to: ha_call_service(domain=light, service=turn_on|turn_off, target.area_id)
risk: R1
consent: configurable (lembrar por área/dispositivo)
```

```yaml
capability: home.climate.read
params: { area: string }
maps_to: ha_get_state / ha_search
risk: R0
consent: none
```

Vantagens: o modelo escolhe entre 8–12 capabilities em vez de 86 tools; a política de
risco fica na capability; o adaptador pode mudar sem tocar no produto.

## 4. Catálogo inicial proposto (12 capabilities)

| Capability | Mapeia para | Risco | Consentimento |
|---|---|---|---|
| `home.state.read` | `ha_get_state`, `ha_search` | R0 | nenhum |
| `home.overview` | `ha_get_overview` | R0 | nenhum |
| `home.history.read` | `ha_get_history` | R0 | nenhum (janela limitada) |
| `home.light.set` | `ha_call_service` light | R1 | configurável |
| `home.switch.set` | `ha_call_service` switch | R1 | configurável |
| `home.climate.set` | `ha_call_service` climate | R1 | configurável |
| `home.scene.activate` | `ha_config_*_scene` / `ha_call_service` scene | R1 | configurável |
| `home.all.off` | `ha_bulk_control` | R3 | dupla confirmação |
| `home.automation.manage` | `ha_config_set_automation` | R2 | explícito |
| `home.lock.set` | `ha_call_service` lock | **R2** | explícito por ação |
| `home.alarm.set` | `ha_call_service` alarm_control_panel | **R2** | explícito por ação |
| `home.camera.snapshot` | `ha_get_camera_image` | **R2 (privacidade)** | opt-in permanente |

Fora do catálogo por padrão: arquivos, YAML, restart, security policy, dev tools,
registry de entidade/dispositivo, HACS, backups. São operações de administrador, não
de assistente pessoal; um "modo manutenção" separado pode expô-las com R3.

## 5. Descoberta de dispositivos sem poluir o prompt

`ha_search` com busca fuzzy devolve entidades por nome de ambiente. A Lia deve:

1. manter um **cache de entidades** local (id, nome, área, domínio) atualizado sob
   demanda;
2reolver "a luz do quarto" no cache da Lia, não enviando 200 entidades ao modelo;
3. enviar ao HA apenas o comando resolvido.

Custo: um cache a invalidar. Benefício: prompt pequeno, latência baixa, menos
alucinação de `entity_id`.

## 6. Offline / LAN sem internet

| Cenário | Comportamento |
|---|---|
| LAN ok, internet ok | normal (conexão A) |
| LAN ok, **internet cai** | **funciona**: HA-MCP em LAN/stdio não precisa de internet; UI mostra "modo local" |
| LAN cai, internet ok | integração indisponível; Lia continua funcionando para o resto; mensagem clara |
| HA reiniciando | fila + timeout + retry único; nunca bloquear a conversa |

Regra de produto: perder a automação residencial **nunca** pode degradar a conversa.

## 7. O que esta arquitetura recusa de propósito

| Recusa | Motivo |
|---|---|
| Embutir HA-MCP como biblioteca | MIT permite, mas cria dependência de runtime no Core |
| Expor as 86 tools ao modelo | custo de contexto + superfície de risco |
| Deixar o HA-MCP decidir risco | ele não conhece o usuário Lia nem a política do produto |
| Fazer da Lia um front-end do HA | a Lia é assistente pessoal; HA é um dos domínios |
| Instalar servidor MCP automaticamente | ordem de serviço: não auto-instalar servidor de terceiro |

## 8. Alternativas consideradas

| Alternativa | Prós | Contras | Veredito |
|---|---|---|---|
| **A. HA-MCP atrás do broker** (proposta) | 86 tools, MIT, ativo, read-only por conexão | dependência externa, breaking changes | **preferida** |
| B. MCP nativo do HA (~15 tools) | sem terceiro, suporte oficial | sem automações/dashboards/diagnóstico | insuficiente hoje |
| C. Cliente REST próprio da Lia | controle total de risco | reimplementa 86 tools; manutenção eterna | rejeitada |
| D. HACS integration in-process | instalação mais simples para o usuário | acopla ao HA; servidor dentro do HA | opção de deployment, não de arquitetura |

A escolha entre A e D é de **deployment**, não de arquitetura: o broker funciona com
qualquer um dos dois transports.

## 9. Pré-requisitos antes de qualquer código

1. `DR-0003` decidido.
2. `RISK-MATRIX.md` aprovada.
3. `MCP-CONTRACT.md` congelado (versão 0.1).
4. Protótipo isolado validado (5 comandos, ver `IMPLEMENTATION-PLAN.md`).
5. Política de log/auditoria definida (o que é gravado, por quanto tempo, onde).
