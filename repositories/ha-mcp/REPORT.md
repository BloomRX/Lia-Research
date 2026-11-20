# HA-MCP — Home Assistant Model Context Protocol Server

| Campo | Valor |
|---|---|
| ID | `LR-MCP-001` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Título | HA-MCP: servidor MCP para Home Assistant — avaliação e proposta de integração residencial da Lia |
| Categoria | mcp |
| Projetos beneficiados | Lia-Project, Lia Agent Hub |
| Áreas transversais | `cross-project/smart-home/`, `cross-project/mcp/` |
| Fontes | `homeassistant-ai/ha-mcp@3dd26d45fbefa6fed999b618092a56005bb5d79c:README.md`, `docs/OAUTH.md`, `docs/oidc.md`, `docs/in-process-server.md`, `docs/FAQ.md`, `src/ha_mcp/tool_catalog.py`, `pyproject.toml` |
| Versão/commit analisado | `3dd26d4` (2026-11-17T14:49:06Z), tag `v9.3.0.dev3610` |
| Data da pesquisa | 2026-11-17 |
| Última verificação | 2026-11-17 |
| Licença | MIT (API do GitHub: `mit`, 2026-11-20; arquivo `LICENSE` não relido) |
| Upstream conferido | 2026-11-20 · `homeassistant-ai/ha-mcp` · HEAD `955af7bf42a4` · mudou desde a análise (conteúdo novo não lido) |
| Próxima revisão | 2027-02-17 (90 dias — segurança e automação residencial) |
| Responsável | Research Orchestrator |
| Recomendação | **ADAPT** (integração opcional; não adotar como dependência do Core) |
| Licença do objeto | MIT (lida em `LICENSE`, "Copyright (c) 2024 Julien") |
| Confiança das evidências | **Alta** para identificação, licença, tools, transports e auth; **Média** para desempenho e comportamento em rede local instável |

> Documentos companheiros: `ARCHITECTURE-PROPOSAL.md` (arquitetura desejada),
> `RISK-MATRIX.md` (matriz R0–R3), `MCP-CONTRACT.md` (contratos de ferramenta),
> `IMPLEMENTATION-PLAN.md` (plano futuro, não executado).

---

## 1. Identificação

- **Nome:** HA-MCP (importável como `ha-mcp`; componente `ha_mcp_tools`)
- **URL:** https://github.com/homeassistant-ai/ha-mcp
- **Organização:** `homeassistant-ai` (projeto comunitário; mantenedor citado `julienld`)
- **Licença:** MIT, `Copyright (c) 2024 Julien` — `CONFIRMED` (arquivo `LICENSE`)
- **Versão/commit:** `3dd26d4`, tag `v9.3.0.dev3610` (dev build) — `CONFIRMED`
- **Branch padrão:** `master` (não `main`) — relevante para automação
- **Data da análise:** 2026-11-17
- **Status da pesquisa:** `CURRENT`

Métricas de contexto (não de mérito): ★7.934 · 464 forks · 16 issues abertas ·
criado 2025-09-14 · 2.818 arquivos · 846 em `src/` · **1.516 arquivos de teste** ·
**46 workflows de CI**.

## 2. Resumo executivo

HA-MCP é um servidor MCP que expõe **86 ferramentas** sobre a API do Home Assistant,
com foco declarado em *administração* do sistema — não apenas controle de
dispositivos. A comparação oficial é explícita: o MCP embutido do HA tem ~15 tools e
foca controle; o HA-MCP tem 86 e cria/edita depura automações, dashboards, backups e
arquivos YAML (`REPORTED` no README; a tabela de tools é `CONFIRMED` no arquivo).

Para a Lia, o valor é óbvio: o caso de uso "Lia, desliga tudo quando eu sair" está
coberto pela combinação `ha_search` + `ha_call_service`/`ha_bulk_control`. O risco
também é óbvio, e é maior do que a maioria das integrações: **o token do Home
Assistant é um token de administrador**, e uma ferramenta genérica (`ha_call_service`)
pode abrir uma fechadura ou desativar um alarme com a mesma assinatura que acende uma
luz. O controle de risco do HA-MCP é *grosso* (read-only por endpoint, políticas de
aprovação de tool, allowlist de entidades); o controle *fino* (por domínio, por
entidade, por nível de risco) **não existe** e teria de ser construído na Lia.

Conclusão: a tecnologia é sólida, bem testada e permissivamente licenciada; a
arquitetura de segurança para uso doméstico **precisa ser da Lia**, não do HA-MCP.
Recomendação `ADAPT`: usar como adaptador opcional atrás do broker de ferramentas
da Lia, com conexão read-only por padrão e caminho elevado separado.

## 3. O que resolve

| Problema | Como o HA-MCP resolve | Evidência |
|---|---|---|
| LLM não sabe o que existe na casa | `ha_get_overview`, `ha_search` (busca fuzzy de entidade), `ha_get_state` | `CONFIRMED` (README tools table) |
| Comando de linguagem natural → ação | `ha_call_service`, `ha_bulk_control` | `CONFIRMED` |
| Automação como código sem editar YAML à mão | `ha_config_set_automation`, `ha_config_get_automation`, `ha_get_automation_traces` | `CONFIRMED` |
| Diagnóstico ("por que não funcionou?") | `ha_get_logs`, `ha_get_history`, `ha_get_automation_traces`, `ha_get_system_health` | `CONFIRMED` |
| Backup antes de mexer | `ha_manage_backup`, backups automáticos de edição | `REPORTED` (README) + `OBSERVED` (módulos `backup_*.py`) |
| Descoberta de dispositivo sem listar 200 entidades no prompt | catálogo "search" por URL (`ENABLE_TOOL_SEARCH`) | `CONFIRMED` (`src/ha_mcp/tool_catalog.py`) |

## 4. Arquitetura

```text
cliente MCP (Claude Desktop / Cursor / Lia)
        │  stdio | HTTP+MCP secret path | HA webhook | /readonly
        ▼
   ha-mcp server (FastMCP *vendorizado* em src/ha_mcp/_vendor/fastmcp)
        │
        ├── tool_catalog.py      catálogo por endpoint (full | search)
        ├── read_only.py         bloqueio de escrita por conexão
        ├── transport_security.py, ipv6_lan_guard.py
        ├── redaction.py (721 linhas)  scrub de segredos em saída/backup
        ├── ha_request_queue.py  serialização de chamadas ao HA
        └── llm_exposure.py      controle de exposição ao LLM
        ▼
   Home Assistant REST/WebSocket API  (HOMEASSISTANT_URL + token LLAT)
        ▼
   dispositivos (Zigbee/Z-Wave/Matter/Wi-Fi), automações, dashboards
```

**Modos de execução** (`CONFIRMED` em `docs/in-process-server.md` e README):

| Modo | Como | Observação |
|---|---|---|
| Integração HA (`ha_mcp_tools`) | HACS/Marketplace, servidor **in-process**, exposto por webhook do HA | recomendado pelo projeto; HA ≥ 2026.8.0 |
| Add-on (app) | Supervisor, ingress, porta 9583 | HAOS/Supervised |
| Docker / `ha-mcp-web` | HTTP, porta 8086, `MCP_SECRET_PATH` padrão `/mcp` | qualquer host |
| `uvx` stdio | processo local | mais simples para desktop |
| Proxy webhook | add-on dedicado | para HA Container/Core |

Um detalhe de arquitetura que importa para a Lia: **o catálogo de tools é fixado por
URL, não negociado por requisição** — porque clientes MCP não refrescam a lista de
tools quando ela muda. Isso permite dar ao agente conversacional um catálogo pequeno
(`/catalog/search`) e a um agente administrativo o catálogo completo (`/catalog/full`).

## 5. Funcionalidades

86 tools em 30 categorias (`CONFIRMED`, tabela versionada com marcadores
`TOOLS_TABLE_START/END` no README).

| Categoria | Tools | Relevância para a Lia |
|---|---|---|
| Search & Discovery | `ha_get_overview`, `ha_get_state`, `ha_search` | **essencial** (R0) |
| Service & Device Control | `ha_bulk_control`, `ha_call_event`, `ha_call_service`, `ha_get_operation_status`, `ha_list_services` | **essencial** (R1/R2 conforme parâmetro) |
| Automations | `ha_config_{get,set,remove}_automation` | alta (R2) |
| Scenes / Scripts | `ha_config_*_scene`, `ha_config_*_script` | alta (R1/R2) |
| History & Statistics | `ha_get_history`, `ha_get_logs`, `ha_get_automation_traces` | alta (R0) |
| Camera | `ha_get_camera_image` | **sensível** (privacidade) |
| System | `ha_restart`, `ha_reload_core`, `ha_manage_backup`, `ha_manage_updates`, `ha_manage_security_policy`, `ha_manage_theme`, `ha_config_{get,set}_yaml` (beta) | **R3** |
| Files (beta) | `ha_list_files`, `ha_read_file`, `ha_write_file`, `ha_delete_file` | **R3** |
| Entity/Device registry | `ha_get_entity`, `ha_set_entity`, `ha_remove_entity`, `ha_get_device`, `ha_set_device`, `ha_remove_device` | R2/R3 |
| Dashboards | 6 tools + screenshot (beta) | R1 |
| Helpers, Labels, Areas, Zones, Groups, Calendar, Todo, Blueprints, HACS, Energy, Matter/radio, Apps, Assist pipeline, Developer | ver tabela do README | varia |

Estados: tools marcadas *(beta)* são `ha_config_set_yaml`, `ha_get_dashboard_screenshot`,
`ha_manage_custom_tool`, e as quatro de arquivo. Beta = superfície instável, não
colocar no caminho principal do usuário.

## 6. Dependências

| Dependência | Natureza | Licença | Observação |
|---|---|---|---|
| FastMCP | **vendorizado** em `src/ha_mcp/_vendor/fastmcp` | MIT (upstream) | vendoring reduz risco de supply chain, aumenta dívida de atualização |
| Home Assistant | serviço obrigatório (o alvo) | Apache-2.0 (HA Core) | HA ≥ 2026.8.0 para a integração |
| Python | `>=3.11` (`pyproject.toml`) | PSF | `uvx --python 3.14` no exemplo oficial |
| `rmcp`-like stack | — | — | não aplicável (é Python) |
| Cliente MCP | Claude Desktop, Claude Code, Cursor, Windsurf, Codex, 15+ | — | Codex tem bug conhecido de inicialização HTTP (reportado no FAQ) |
| `npx mcp-remote` | para clientes que não falam HTTP | MIT | só para o modo add-on |

Não há dependência de nuvem obrigatória para operação local (`CONFIRMED` pela
arquitetura de transports; a nuvem só aparece no caminho remoto opcional).

## 7. Requisitos de hardware e sistema

- Servidor: roda em HA (in-process), em container, ou como processo Python local.
  Consumo não medido nesta pesquisa — `UNVERIFIED` (não foi executado).
- Cliente: qualquer cliente MCP; para a Lia, o processo conversacional no Windows 11
  + RX 580 / 16 GB precisa apenas falar MCP, não inferir nada aqui.
- Rede: HA na LAN; para acesso remoto, webhook do HA (funciona com Nabu Casa) ou
  túnel/reverse proxy com HTTPS.
- Windows: `uvx` documentado (`docs/Windows-uv-guide.md`) — `REPORTED`.

## 8. Segurança e privacidade

**Modelos de autenticação** (`CONFIRMED` em `docs/OAUTH.md`, `docs/oidc.md`, README):

| Modo | Credencial | Multi-usuário | Risco principal |
|---|---|---|---|
| Secret path na URL | segredo na URL | não | segredo em log/histórico/referrer; HTTP claro se não houver TLS |
| OAuth (beta) | LLAT por usuário via consent form | sim | gestão de clientes OAuth; exige HTTPS |
| OIDC | gate de identidade; **token único compartilhado** | autentica, não isola | todos veem a mesma casa com o mesmo poder |
| `ha_auth` (integração) | login de conta HA | sim | depende do HA |

**Vulnerabilidades históricas** (`CONFIRMED` por advisory citado na documentação):

- `GHSA-fmfg-9g7c-3vq7` — **SSRF** no campo de URL do formulário OAuth; corrigido
  removendo o campo (v7.0.0, `HOMEASSISTANT_URL` agora é variável do servidor).
- `GHSA-pf93-j98v-25pv` — **XSS** no consent form; corrigido com escaping.

Isso é um sinal de maturidade razoável (corrigiram e documentaram a causa), e um
alerta: a superfície de auth desse projeto já teve falha de rede interna.

**Controles existentes:**

| Controle | Como funciona | Evidência |
|---|---|---|
| Read-only por conexão | sufixo `/readonly` no endpoint esconde write tools e bloqueia chamadas de escrita, inclusive via cache/search proxy | `CONFIRMED` (README) |
| Read Only Mode global | toggle de servidor | `REPORTED` |
| Políticas de segurança de tool | aprovação de usuário por tool; `ha_manage_security_policy` | `REPORTED` (README) + `OBSERVED` (tool existe) |
| Enable/disable/pin de tool | UI de settings | `REPORTED` |
| Entity Visibility | restringe entidades visíveis, aplica na chamada seguinte | `REPORTED` |
| Backups automáticos de edição | antes de alterar helper/integração/YAML | `REPORTED` |
| Redaction | `redaction.py` (721 linhas) remove segredos de saída e backup | `OBSERVED` |
| Guarda de LAN IPv6 | `ipv6_lan_guard.py` | `OBSERVED` |
| Segurança de transporte | `transport_security.py` | `OBSERVED` |

**Privacidade:** roda local, sem telemetria hoje; coleta de estatística anônima é
"planejada", condicionada à configuração de analytics do HA, com aviso prévio de um
mês; bug reports só com aprovação explícita (`REPORTED`, seção Privacy do README).
Há política própria em `PRIVACY.md`.

**O que não existe (e a Lia precisa construir):**

1. Permissão por **entidade** no nível do token (HA LLAT é tudo-ou-nada; "Entity
   Visibility" é filtro de visibilidade, não autorização).
2. Classificação de risco por **domínio/serviço** (`lock.unlock` vs `light.turn_on`).
3. Confirmação em dois passos para R2/R3 fora do LLM.
4. Trilha de auditoria com intenção declarada ("usuário pediu X"), além do log do HA.

## 9. Licença e proveniência

- **MIT**, `Copyright (c) 2024 Julien` — `CONFIRMED` no arquivo `LICENSE` no commit analisado.
- Obrigações: manter aviso de copyright e texto da licença em cópias/derivações.
  Sem copyleft; sem obrigação de abrir código; "AS IS".
- Marca: "Home Assistant" e o logo do HA-MCP **não** são licenciados por este MIT.
  Um produto Lia que exiba a marca HA precisa seguir a política de marca do HA.
- Camadas: código MIT; documentação dentro do repo (mesma licença, presumível);
  nenhum peso de modelo envolvido.
- **Classe de aproveitamento:** `USE_AS_IS` para consumir como servidor externo
  (nenhuma cópia de código); `ADAPT_ALLOWED` se algum dia houver fork.
- Risco de distribuição: **baixo**. Não há impedimento para a Lia oferecer
  "conectar ao seu Home Assistant via HA-MCP".

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Criado | 2025-09-14 | ~14 meses de vida na data da análise |
| Último commit | 2026-11-17 (mesmo dia) | ativo |
| Cadência | vários dev builds/dia (`dev3610`) | muito ativo; dev channel ruidoso |
| Releases | tags de dev + versões estáveis (v7.x documentado, v9.3.0 em dev) | versionamento semântico com breaking changes documentados (v7.3.0 move `ha_config_set_yaml` para beta) |
| Testes | 1.516 arquivos de teste, 46 workflows, E2E badge | **forte** |
| Issues abertas | 16 com 7.9k estrelas | proporção baixa = triagem ativa |
| Bus factor | mantenedor principal único citado (`julienld`), com sponsors e contribuidores listados | risco moderado |

Breaking changes são frequentes e explícitos. Para a Lia isso significa: **pin de
versão obrigatório**, nunca `latest`, e teste de contrato a cada bump.

## 11. Custos e limitações

- **Custo financeiro:** zero (MIT, self-hosted). Sponsors opcionais.
- **Custo de integração:** moderado-alto do lado da Lia (broker de tools + política
  de risco + UX de consentimento), baixo do lado do HA (instalar integração + token).
- **Limitações declaradas:**
  - só a release estável atual do HA é oficialmente suportada (piso técnico 2026.8.0);
  - admin token é o caminho recomendado; token não-admin tem limitações e operações
    admin são recusadas;
  - OAuth ainda é **beta**;
  - Codex HTTP tem bug de inicialização conhecido (usar stdio);
  - não rodar in-process **e** add-on ao mesmo tempo ("pode deixar a conexão travada").
- **Limitação estrutural (nossa, não deles):** não há granularidade de permissão por
  entidade/risco. É o custo real de adotar.

## 12. Compatibilidade com o ecossistema Lia

| Requisito Lia | HA-MCP atende? | Observação |
|---|---|---|
| Windows 11 + Electron | sim | cliente MCP local (`uvx`) ou HTTP para HA |
| Não depender de nuvem | sim | caminho LAN local |
| Funcionar offline | **parcial** | LAN ok; acesso remoto exige webhook/túnel |
| Integração opcional e desativável | sim | é um servidor externo; desconectar = desligar |
| Core não depende de HA | sim, se atrás de broker | regra de arquitetura em `ARCHITECTURE-PROPOSAL.md` |
| Broker de tools existente na Lia | compatível | Lia-Project já tem autorização de tools por capability |
| Hub como orquestrador | compatível | Hub cataloga servidores MCP |
| Sem código GPL no produto | sim | MIT |

## 13. Projetos beneficiados

| Projeto | Como usaria | Pré-requisito |
|---|---|---|
| **Lia-Project** | experiência conversacional, consentimento, UI de confirmação, Stage | broker de tools + política R0–R3 |
| **Lia Agent Hub** | descoberta/catálogo de servidor MCP, versionamento de contrato | modelo de catálogo MCP (lacuna atual) |
| Lia Model Lab | indireto: nada | — |
| Lia Forge / Studio | nenhum uso direto | — |

## 14. Oportunidades de reutilização

1. **Padrão "catálogo por URL"** (`/catalog/full`, `/catalog/search`): resolver o
   problema de contexto pequeno vs catálogo grande sem trocar servidor. Reutilizável
   como conceito no broker da Lia.
2. **Read-only por conexão**: o mesmo servidor, dois níveis de poder, sem duplicar
   instalação. Modelo direto para "Lia consulta" vs "Lia executa".
3. **Redaction como módulo separado** com 721 linhas: bom exemplo de tratar segredo
   como requisito transversal, não como cuidado pontual.
4. **Backup antes de edição + verificação pós-edição**: padrão para qualquer ação
   destrutiva que a Lia venha a expor.
5. **Documentar a causa da vulnerabilidade no próprio doc** (SSRF/XSS): prática de
   proveniência de segurança que vale copiar como hábito.

## 15. Riscos e incompatibilidades

| # | Risco | Severidade | Probabilidade | Mitigação | Decisão |
|---|---|---|---|---|---|
| R1 | Token admin dá poder total à casa; LLM pode abrir fechadura | **alta** | média | conexão read-only por padrão; caminho elevado separado; confirmação fora do LLM | `DR-0003` |
| R2 | `ha_call_service` é genérico: risco está no parâmetro, não no nome da tool | **alta** | alta | gate por domínio/serviço na Lia, não por tool | `DR-0003` |
| R3 | Injeção de prompt via conteúdo de entidade/nome de dispositivo | média | média | tratar retorno como dados; allowlist; sem expor `ha_get_logs` cru ao LLM | proposta |
| R4 | Câmera (`ha_get_camera_image`) = imagem da casa | **alta** (privacidade) | baixa | desabilitar por padrão; exigir opt-in explícito | proposta |
| R5 | Breaking changes frequentes | média | alta | pin de versão + teste de contrato no CI da Lia | gate |
| R6 | Secret path em URL vaza em log/histórico | média | média | exigir OAuth/OIDC ou mTLS na rede local; nunca URL em log | gate |
| R7 | Bus factor (mantenedor principal) | média | baixa | pin de commit + fork de emergência sob MIT | monitorar |
| R8 | Offline: perda de internet derruba o caminho remoto | baixa | alta | caminho LAN como primário; UI diz "modo local" | proposta |
| R9 | Rodar in-process + add-on simultaneamente trava conexão | baixa | média | regra de instalação única no guia da Lia | doc |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | Licença MIT, © 2024 Julien | CONFIRMED | `ha-mcp@3dd26d4:LICENSE` | 2026-11-17 |
| E2 | 86 tools em 30 categorias | CONFIRMED | `@3dd26d4:README.md` tabela `TOOLS_TABLE_*` | 2026-11-17 |
| E3 | FastMCP vendorizado | CONFIRMED | `src/ha_mcp/tool_catalog.py` importa `ha_mcp._vendor.fastmcp` | 2026-11-17 |
| E4 | Read-only por sufixo de endpoint | CONFIRMED | `README.md` §Read-only HTTP connections | 2026-11-17 |
| E5 | SSRF e XSS corrigidos em v7.0.0 | CONFIRMED | `docs/OAUTH.md` cita GHSA-fmfg-9g7c-3vq7 e GHSA-pf93-j98v-25pv | 2026-11-17 |
| E6 | OIDC compartilha um único token HA | CONFIRMED | `docs/oidc.md` ("all requests share the same ... credentials") | 2026-11-17 |
| E7 | Modo in-process via webhook, HA ≥ 2026.8.0 | CONFIRMED | `docs/in-process-server.md` | 2026-11-17 |
| E8 | Tools de arquivo e YAML em beta | CONFIRMED | `README.md` marcas *(beta)* | 2026-11-17 |
| E9 | Sem telemetria hoje | REPORTED | `README.md` §Privacy | 2026-11-17 |
| E10 | 1.516 arquivos de teste, 46 workflows | CONFIRMED | tree `@3dd26d4` (contagem) | 2026-11-17 |
| E11 | Consumo de memória/CPU em HA real | BLOCKED | não executado; exigiria instância HA | — |

## 17. Recomendação

**`ADAPT`** — usar o HA-MCP como adaptador opcional de ferramentas, atrás do broker
de ferramentas da Lia, sem acoplar o Core ao Home Assistant.

Justificativa: a tecnologia é maturidade alta, licença permissiva e cobre os casos de
uso desejados. O que falta não é capacidade — é **granularidade de risco**, e essa
lacuna é de arquitetura da Lia.

**Gates explícitos:**

1. Conexão padrão do assistente é `/readonly`.
2. Caminho elevado é conexão separada, criada sob demanda, com expiração.
3. Gate de risco por domínio/serviço, implementado na Lia (`RISK-MATRIX.md`).
4. Versão pinada + teste de contrato a cada bump.
5. Câmera, arquivos, YAML, restart e security policy desabilitados por padrão.
6. Home Assistant permanece **opcional**: sem HA configurado, a Lia funciona igual.

**O que esta recomendação não autoriza:** implementar a integração, adicionar
dependência ao `package.json` da Lia, criar submodule, ou alterar o Core.
Isso exige `DR-0003`.

## 18. Próximos passos

| # | Ação | Dono sugerido | Conclusão |
|---|---|---|---|
| 1 | Protótipo **isolado** (fora do repo do produto): cliente MCP mínimo + HA de teste, 5 comandos R0/R1 | Lia-Project | 5/5 comandos com log auditável |
| 2 | Implementar protótipo do gate de risco por domínio/serviço | Lia-Project | matriz R0–R3 aplicada em teste |
| 3 | Medir latência LAN→HA de `ha_search`/`ha_call_service` (p50/p95) | Lia-Project | relatório de benchmark |
| 4 | Definir UX de consentimento R2/R3 (modal, timeout, "não lembrar") | Lia-Project (produto) | spec aprovada |
| 5 | Levantar modelo de catálogo MCP no Hub | Lia Agent Hub | spec de registro de servidor |
| 6 | Decidir `DR-0003` com base em 1–4 | proprietário | decisão registrada |
| 7 | Revisar esta pesquisa em 90 dias ou no próximo advisory | Research | `última verificação` atualizada |
| 8 | `AGUARDA DECISÃO`: escolher entre OAuth (per-user) e OIDC (gate) para instalação multi-cliente | proprietário | decisão de deployment |

**Não implementado nesta etapa**, conforme a ordem de serviço: nenhuma integração,
nenhuma dependência, nenhum código de terceiros incorporado.
