# Contrato MCP proposto — adaptador residencial

| Campo | Valor |
|---|---|
| ID | `LR-MCP-001-C` |
| Versão do contrato | `0.1` (proposta, não implementada) |
| Estado | `PENDENTE` |
| Data | 2026-11-17 |

> Contrato de **integração**, não de implementação. Descreve o que a Lia espera de um
> servidor MCP residencial e o que ela promete entregar. Nenhum código foi escrito.

---

## 1. Requisitos do servidor (o que a Lia exige de um adaptador)

| # | Requisito | Motivo | HA-MCP atende? |
|---|---|---|---|
| S1 | Transporte stdio **ou** HTTP com TLS | desktop local / instalação remota | sim |
| S2 | Modo somente leitura por conexão | catálogo padrão sem escrita | sim (`/readonly`) |
| S3 | Catálogo de tools fixo por URL | cliente MCP não refresca lista | sim (`/catalog/*`) |
| S4 | Versão identificável em runtime | pin e teste de contrato | `REPORTED` (`_version.py` existe) |
| S5 | Operação em LAN sem internet | requisito de produto | sim |
| S6 | Licença que permita uso comercial interno | distribuição | sim (MIT) |
| S7 | Sem auto-instalação de dependências em runtime | segurança | **parcial** (integração HACS baixa o pacote) |
| S8 | Erros estruturados (não string livre) | tratamento de falha na UI | `UNVERIFIED` |

## 2. Capabilities expostas pela Lia ao modelo

Formato: nome, parâmetros, risco, resultado. O modelo **nunca** vê nomes de tool MCP.

```yaml
# leitura
home.state.read        { entity?: string, area?: string, query?: string } → R0
home.overview          {}                                               → R0
home.history.read      { entity: string, hours: 1..72 }                 → R0

# ação comum
home.light.set         { area|entity, state: on|off, brightness?: 0..100 } → R1
home.switch.set        { area|entity, state: on|off }                     → R1
home.climate.set       { area|entity, temperature: 16..30 }               → R1
home.scene.activate    { scene: string }                                  → R1

# sensível
home.automation.set    { automation: string, enabled: bool }              → R2
home.lock.set          { lock: string, action: lock|unlock }              → R2
home.alarm.set         { panel: string, action: arm|disarm }              → R2
home.camera.snapshot   { camera: string }                                 → R2

# sistêmico
home.all.off           { confirm_token: string }                          → R3
```

Regras:

1. Capacidade ausente = ação impossível. Não existe "tool catch-all" exposta.
2. `confirm_token` é gerado pela UI após confirmação, com TTL de 30 s, uso único.
3. Toda capability devolve `{ ok, data?, error?, audit_id }`.
4. Nenhuma capability aceita texto livre interpretado como serviço/serviço HA.

## 3. Mapeamento capability → tool MCP

| Capability | Tool HA-MCP | Parâmetros mapeados |
|---|---|---|
| `home.state.read` | `ha_search`, `ha_get_state` | `query` → search; `entity` → get_state |
| `home.overview` | `ha_get_overview` | — |
| `home.history.read` | `ha_get_history` | `entity`, janela |
| `home.light.set` | `ha_call_service` | `domain=light`, `service=turn_on/off`, `target{area_id/entity_id}`, `data{brightness}` |
| `home.switch.set` | `ha_call_service` | `domain=switch` |
| `home.climate.set` | `ha_call_service` | `domain=climate`, `service=set_temperature` |
| `home.scene.activate` | `ha_call_service` | `domain=scene`, `service=turn_on` |
| `home.automation.set` | `ha_config_set_automation` | id + enabled |
| `home.lock.set` | `ha_call_service` | `domain=lock`, `service=lock/unlock` |
| `home.alarm.set` | `ha_call_service` | `domain=alarm_control_panel` |
| `home.camera.snapshot` | `ha_get_camera_image` | camera id |
| `home.all.off` | `ha_bulk_control` | alvos filtrados por domínio R0/R1 |

Bloqueio explícito no adaptador (nunca repassar): `ha_config_set_yaml`,
`ha_write_file`, `ha_delete_file`, `ha_restart`, `ha_reload_core`,
`ha_manage_security_policy`, `ha_dev_manage_server`, `ha_remove_entity`,
`ha_remove_device`, `ha_manage_backup`.

## 4. O que a Lia promete ao adaptador

| # | Garantia | Como |
|---|---|---|
| L1 | Só chamar capability do catálogo aprovado | broker com allowlist |
| L2 | Nunca repassar texto do usuário como argumento livre de serviço | resolução de entidade no cache Lia |
| L3 | Aplicar gate de risco antes da chamada | `RISK-MATRIX.md` |
| L4 | Registrar auditoria de cada execução | log local com TTL |
| L5 | Propagar timeout e não repetir ação R2/R3 | idempotência por `audit_id` |
| L6 | Degradar sem quebrar a conversa quando HA estiver fora | fila + erro amigável |
| L7 | Não enviar dados da casa a provider de modelo por padrão | resumo local; sem dump de entidades ao LLM remoto |

## 5. Versionamento e compatibilidade

- O adaptador declara `server_version` e `contract_version`.
- Bump de tool do HA-MCP quebra o contrato → teste falha → integração desabilitada,
  não silenciosamente degradada.
- Pin de versão do HA-MCP no adaptador; nunca `latest`.
- Matriz de compatibilidade suportada: `N` e `N-1`. Terceira versão fora = aviso ao
  usuário.

## 6. Erros e estados

| Situação | Resposta da capability | UI |
|---|---|---|
| HA offline | `{ ok:false, error:"HA_UNREACHABLE" }` | "Não consigo falar com a casa agora" |
| Entidade ambígua | `{ ok:false, error:"AMBIGUOUS", candidates:[...] }` | pergunta qual |
| Permissão negada | `{ ok:false, error:"CONSENT_DENIED" }` | nada acontece |
| Token expirado | `{ ok:false, error:"AUTH_EXPIRED" }` | pede reconexão |
| Timeout em R2 | `{ ok:false, error:"TIMEOUT_UNKNOWN_STATE" }` | **não repetir**; verificar estado |
| Versão incompatível | `{ ok:false, error:"CONTRACT_MISMATCH" }` | integração desabilitada |

`TIMEOUT_UNKNOWN_STATE` é o caso mais perigoso: a ação pode ter ocorrido. A UI deve
consultar o estado antes de oferecer nova tentativa.

## 7. O que este contrato não define

- Interface visual (é do Lia-Project).
- Formato de armazenamento do catálogo (é do Hub).
- Estratégia de autenticação no HA (OAuth vs OIDC vs secret path) — decisão de
  deployment, `DR-0003`.
- Suporte a múltiplas casas. Fora de escopo da v0.1.
