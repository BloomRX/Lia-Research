# Permissões por execução — escopo, delegação, revogação, isolamento e auditoria

| Campo | Valor |
|---|---|
| ID | `LR-SEC-005` |
| Categoria | security |
| Projetos beneficiados | Lia Agent Hub (modelo), Lia-Project (broker), Lia Studio (agente de código), Lia Forge (workflows) |
| Fontes | `open-jarvis/OpenJarvis@6656b7fe` (`GuardrailsEngine`, `SecretScanner`/`PIIScanner` WARN/REDACT/BLOCK, `AuditLogger` SQLite, `SandboxedAgent` Docker/Podman + mount security) → `LR-AGENT-001`; `Ryder-Sun/Meldwork@db9b6c84` (*scoped permissions*, *evidence-aware runs*, *human-in-the-loop*) → `LR-AGENT-003`; `homeassistant-ai/ha-mcp@3dd26d45` (conexão `/readonly`, aprovação de tool) → `LR-MCP-001`; `alethe v19` (workers limitados, `maxCalls`, reserva atômica de orçamento, cancelamento de árvore de processos) → `LR-LIC-003` §6; `Lia-Project` (`LIA-CREDENTIAL-OWNER.md`, correção de sandbox do Stage) → `LR-SEC-001` |
| Data | 2026-11-17 |
| Status | **PROPOSTA** — nada implementado, nada executado |
| Confiança | Alta para os padrões observados nas fontes; média para o modelo proposto |

---

## 1. Pergunta

Como uma execução de agente recebe **poder temporário e limitado**, de forma que seja
possível provar (a) o que foi autorizado, (b) por quem, (c) por quanto tempo, (d) que
foi revogado, e (e) o que de fato aconteceu — sem colocar essa garantia dentro do modelo?

## 2. Evidência: quem já resolveu parte disto

| Fonte | O que faz | Rótulo |
|---|---|---|
| OpenJarvis | segurança como **decorator** de engine (substituível, testável); `SecretScanner`/`PIIScanner` com 3 modos; `AuditLogger` em SQLite; `SandboxedAgent` com Docker/Podman e mount restrito | `CONFIRMED` (código) |
| Meldwork | permissões com escopo **por rodada**; execução com evidência; decisão humana explícita | `REPORTED` (README) |
| HA-MCP | conexão **read-only** separada da elevada; aprovação de tool; catálogo por URL | `CONFIRMED` (doc + código) |
| alethe | workers limitados (`maxCalls`), **reserva atômica** de orçamento antes de iniciar, cancelamento de árvore de processos | `CONFIRMED` (`SKILL.md` + `UPSTREAM.md`) |
| Lia-Project | dono único da credencial; sandbox do Stage com correção registrada | `REPORTED` (arquitetura) |

Nenhuma das cinco publica um **modelo de lease** completo. Cada uma tem um pedaço:
tempo (Meldwork), fronteira (OpenJarvis/HA-MCP), orçamento (alethe), credencial (Lia).
O que falta é a composição.

## 3. Vocabulário

| Termo | Definição operacional |
|---|---|
| **Principal** | quem age: usuário, agente, workflow, processo |
| **Grant** | permissão declarada por um principal com autoridade (ex.: usuário) |
| **Lease** | instância temporária de um grant, emitida para **uma** execução |
| **Scope** | tripla (`capability`, `target`, `action`) + classe de risco `R0`–`R3` |
| **Delegação** | transferência de um **subconjunto** de um lease para outro principal |
| **Revogação** | invalidação de lease com efeito imediato e falha fechada |
| **Isolamento** | fronteira física/lógica que limita o dano mesmo com permissão válida |
| **Registro** | prova de intenção + resultado, com identidade e tempo |

## 4. Modelo proposto: quatro objetos

### 4.1 `Grant` (declarado, persistente)

```yaml
grant_id: g-7f2a
principal: user:owner
scope:
  capability: home.set_power
  target: home.room.quarto
  action: "on|off"
risk: R1
consent: once_per_session      # none | once | once_per_session | always_ask
max_uses: null
expires_at: null
```

`Grant` é o que o usuário configura. Ele **não** autoriza execução sozinho.

### 4.2 `Lease` (emitido, efêmero)

```yaml
lease_id: l-9c31
grant_id: g-7f2a
issued_to: execution:plan-42/step-3
issued_at: 2026-11-17T22:31:04Z
expires_at: 2026-11-17T22:36:04Z     # TTL curto por padrão (5 min)
uses_remaining: 1
delegable: false
evidence_required: true
```

Regras do lease:

1. **Sempre temporário.** Sem TTL, não é lease — é permissão permanente disfarçada.
2. **Emitido por execução**, não por agente. Agente novo = lease novo.
3. **`uses_remaining` finito** para `R1`+; `R0` pode ser ilimitado.
4. **`R2`/`R3` nunca delega** e nunca tem `uses_remaining > 1` sem confirmação por uso.
5. **`evidence_required: true`** para `R1`+: a execução precisa anexar prova (o que foi
   feito) para ser considerada concluída.

### 4.3 `ExecutionContext`

Identidade da execução: `execution_id`, `plan_id`, `step`, `principal` original,
cadeia de delegação (`parent_lease`), orçamento (`max_calls`, `deadline`), e o
`SandboxProfile` (quais caminhos, quais domínios de rede, quais processos).

### 4.4 `AuditRecord` (append-only)

| Campo | Regra |
|---|---|
| `intent` | o que o principal pediu, em texto, **antes** da ação |
| `scope_used` | tripla efetivamente exercida |
| `lease_id` / `grant_id` | rastreabilidade |
| `result` | `ok` \| `denied` \| `error` \| `timeout` \| `revoked` |
| `side_effects` | lista de efeitos observados (arquivo escrito, mensagem publicada) |
| `evidence` | hash/ponteiro da prova |
| `decided_by` | humano ou política automática, com versão da política |

Sem `intent`, o log responde "o que aconteceu" e nunca "o que foi pedido" — e é
impossível distinguir uso legítimo de desvio.

## 5. Máquina de estados do lease

```text
        ┌──────────┐  emitir   ┌────────┐  usar   ┌────────┐
        │ declared │──────────►│ active │────────►│ spent  │
        └──────────┘           └────────┘         └────────┘
                                  │  ▲
                     expirar /    │  │ revalidar (falha fechada
                     revogar      ▼  │ se revogado)
                                ┌──────────┐
                                │ revoked  │
                                └──────────┘
```

Regras:

1. `active → spent` só com `AuditRecord` anexado.
2. `expires_at` é verificado **na hora do uso**, não na emissão.
3. Revogação durante uso **não mata** o efeito já produzido: registra e bloqueia o
   próximo. Fingir que cancela é o erro mais caro deste modelo.
4. Qualquer ambiguidade de estado = `revoked` (falha fechada).

## 6. Delegação

| Regra | Motivo |
|---|---|
| Subconjunto apenas: `scope ⊆ parent.scope` | impedir escalada por delegação |
| `expires_at` do filho ≤ do pai | impedir extensão de prazo |
| `risk` do filho ≤ do pai | impedir elevação |
| `delegable: false` para `R2`+ | risco de feitiçaria: um agente "empresta" poder |
| Cadeia registrada (`parent_lease`) | permite reconstruir quem autorizou quem |

Exemplo real do ecossistema: o `alethe` orquestra workers CLI. Se um worker puder
delegar a outro sem limite, `maxCalls` deixa de significar algo. O lease corta isso
na raiz.

## 7. Revogação

Três gatilhos:

| Gatilho | Efeito |
|---|---|
| Usuário revoga | todos os leases do grant passam a `revoked`; próxima tentativa falha |
| Política revoga (ex.: alvo saiu do allowlist) | leases ativos invalidados no próximo uso |
| Falha de integridade (hash de política mudou, credencial trocada) | lease inválido imediatamente |

Propriedades exigidas: revogação é **local e imediata** (sem depender de rede),
**idempotente** e **registrada**. Não existe "revogação eventual".

## 8. Isolamento (o que limita o dano mesmo com permissão válida)

| Fronteira | Mecanismo | Fonte |
|---|---|---|
| Processo | workers separados, cancelamento de árvore | alethe `CONFIRMED` |
| Sistema de arquivos | mount restrito / raiz de workspace | OpenJarvis `SandboxedAgent` `CONFIRMED` |
| Rede | allowlist de domínio + egress declarado | `LR-MCP-002` (proposta de catálogo) |
| Renderer × main | credencial só no main; sandbox do Stage | Lia-Project `REPORTED` |

Regra: **isolamento não substitui permissão, e permissão não substitui isolamento.**
Um `rm -rf` autorizado continua sendo um `rm -rf`.

## 9. Aplicação aos quatro casos do ecossistema

| Caso | Lease | Risco | Observação |
|---|---|---|---|
| Chat com tools | por turno, TTL minutos | R0–R1 | 1 lease por turno, não por sessão |
| MCP de casa | por comando, `uses_remaining: 1` | R1–R3 | `R2`+ exige confirmação por uso; read-only separado (`LR-MCP-003`) |
| Workflow do Forge | por passo, com `evidence_required` | R1–R2 | gate humano em passo de publicação |
| Execução de código (Studio) | por execução, TTL curto, sem delegação | **R3** | isolamento obrigatório; nunca no host sem sandbox |

## 10. O que **não** é permissão

| Não é | Por quê |
|---|---|
| Instrução no prompt ("peça permissão antes de apagar") | é sugestão ao modelo, não controle |
| Allowlist por **nome** de ferramenta | contornável por parâmetro (`domain="lock"`) — `LR-MCP-001-B` |
| "O agente é confiável" | confiança não é mecanismo |
| Log sem intenção (§4.4) | prova efeito, não autorização |
| Sandbox sem política de lease | impede alguns danos, não autoriza nada |

## 11. Plano de verificação (a executar por quem implementar)

| # | Teste | Aprovação |
|---|---|---|
| F1 | lease expirado é recusado no uso | falha fechada |
| F2 | delegação com scope maior é recusada | escalada impossível |
| F3 | `R2` com `delegable: true` é recusado na emissão | política inviolável |
| F4 | revogação durante execução bloqueia o próximo uso e registra o anterior | sem efeito retroativo falso |
| F5 | todo `spent` tem `AuditRecord` com `intent` | auditoria completa |
| F6 | tentativa de uso sem lease gera `denied` auditado, não exceção silenciosa | observável |

Nenhum destes testes foi executado. **A proposta não é verificada até F1–F6 passarem.**

## 12. Riscos da proposta

| Risco | Mitigação |
|---|---|
| Burocracia: usuário aprova cada ação e desiste | `consent: once_per_session` para `R1`; só `R2`+ pede sempre |
| TTL curto quebra fluxo longo | renovação explícita, com registro (não renovação silenciosa) |
| Lease virar teatro (emitido e nunca verificado) | F1/F6 no CI de quem implementar |
| Auditoria virar perfil de comportamento | retenção limitada (`DR-0009`), local, exportável |
| Modelo complexo demais para adotar | implementar só `Grant`+`Lease`+`AuditRecord` primeiro |

## 13. Limitações e pendências

| Item | Rótulo |
|---|---|
| Nenhum lease emitido ou testado | `NOT RUN` |
| Meldwork: modelo de escopo lido só no README | `REPORTED` |
| Isolamento no Windows (job objects, AppContainer) não pesquisado | `UNVERIFIED` |
| Não avaliado custo de UX de confirmação por uso | `NOT RUN` |
| Revogação distribuída (múltiplos processos) sem desenho | `NOT RUN` |

## 14. Encaminhamento

| Ação | Dono | Gate |
|---|---|---|
| Aceitar vocabulário Grant/Lease/AuditRecord | Agent Hub + Project | `DR-0022` (proposto) |
| Implementar `Grant`+`Lease` antes de expandir tools | Lia-Project | `DR-0008` (matriz de risco) |
| Rodar F1–F6 em protótipo isolado | quem implementar | antes de qualquer tool `R2` |
| Definir retenção do registro | proprietário | `DR-0009` |
