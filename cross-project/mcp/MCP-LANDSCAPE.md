# Panorama MCP no ecossistema Lia

| Campo | Valor |
|---|---|
| ID | `LR-MCP-002` |
| Categoria | mcp |
| Projetos | Lia Agent Hub, Lia-Project, Lia Forge |
| Fontes | `Lia-Forge:scripts/spriteforge-mcp.mjs` (10 tools), `Lia-Studio@…:docs/research/ARENA-SKILLS-MCP-AGENT-TOOLS-RESEARCH.md` (68 KB), `Lia-AgentHub:docs/research/*`, pesquisa externa desta fundação |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Alta para o inventário interno; Média para o externo |

## 1. O que a Lia já tem

| Item | Estado | Evidência |
|---|---|---|
| Servidor MCP implementado no Forge (`lia-forge`) | 10 tools | `CONFIRMED` (`spriteforge-mcp.mjs`) |
| Broker de tools no produto (autorização por capability) | existe | `REPORTED` (arquitetura do Project) |
| Catálogo de servidores MCP no Hub | **não existe** | lacuna E-2/E-6 do inventário |
| Validação de segurança de servidor MCP | **não existe** | lacuna |

## 2. Servidores MCP externos pesquisados nesta fundação

| Servidor | Licença | Tools | Transporte | Veredito |
|---|---|---:|---|---|
| `homeassistant-ai/ha-mcp` | MIT | **86** | stdio, HTTP, webhook, in-process | `ADAPTAR` (opcional, atrás de broker) |
| `anefzaoui/misterdownloadmanager` (`mdm-mcp`) | **GPL-3.0** | não contado | stdio + IPC | processo externo apenas |
| MCP nativo do Home Assistant | Apache-2.0 (HA Core) | ~15 | — | insuficiente hoje (`REPORTED`) |

## 3. Padrões que valem ser copiados (de HA-MCP)

1. **Catálogo por URL** (`/catalog/full`, `/catalog/search`): resolve contexto pequeno
   vs catálogo grande sem duplicar servidor.
2. **Read-only por conexão** (`/readonly`): dois níveis de poder, uma instalação.
3. **Redaction como módulo** dedicado (721 linhas): segredo tratado como requisito
   transversal.
4. **Fix de vulnerabilidade documentado com o ID do advisory** no próprio doc.

## 4. O que o ecossistema precisa decidir

| Decisão | Dono | Registro |
|---|---|---|
| Modelo de registro de servidor MCP no Hub (campos, versionamento de contrato) | Agent Hub | `DR-0011` (proposto) |
| Política de instalação de servidor MCP de terceiro (nunca automática) | proprietário | `DR-0012` (proposto) |
| Gate de risco por domínio/serviço antes de qualquer servidor de automação | Lia-Project | `DR-0003` / `DR-0008` |

## 5. Regra permanente

> A Lia **não instala** servidor MCP automaticamente. Todo servidor é escolha explícita
> do usuário, com licença e escopo visíveis.
