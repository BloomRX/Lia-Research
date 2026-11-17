# Comparação — servidor MCP para automação residencial

| Campo | Valor |
|---|---|
| ID | `LR-CMP-002` |
| Pergunta | existe servidor MCP para Home Assistant que sirva à Lia? |
| Data | 2026-11-17 |
| Evidência | `CONFIRMED` para licença/tools/transporte; sem execução |

## 1. Comparação

| Critério | `homeassistant-ai/ha-mcp` | MCP nativo do Home Assistant | servidor próprio |
|---|---|---|---|
| Licença | MIT | Apache-2.0 | do proprietário |
| Tools | **86**, 12 categorias | ~15 (`REPORTED`) | o que se escrever |
| Transporte | stdio · HTTP · Docker · **in-process via webhook** | HTTP do HA | livre |
| Funciona offline na LAN | sim | sim | sim |
| Read-only por conexão | **sim** (`/readonly`) | não | a implementar |
| Catálogo por URL | **sim** (`/catalog/*`) | não | — |
| OAuth | beta, com 2 GHSAs conhecidos | nativo do HA | — |
| Maturidade | 7.934★, releases frequentes, HA ≥ 2026.8 | oficial | zero |
| Risco de segurança | superfície grande (86 tools); SSRF/XSS em beta | menor | depende |
| Custo de adoção | baixo (config) | baixo | alto |
| Custo de manutenção | de terceiro | de terceiro | **seu** |

## 2. Conclusão

Nenhum dos três é adequado como dependência direta do Core. O `ha-mcp` é o único com
cobertura funcional suficiente **e** mecanismo de redução de poder (readonly + catálogo),
e por isso é o candidato — atrás de broker próprio, opcional, desligado por padrão.

O servidor próprio só se justifica se o broker precisar de garantias que o `ha-mcp` não
dá (ex.: assinatura de política por ação). Não é o caso hoje.

## 3. O que não foi testado

Execução real, latência, comportamento de reconexão, estabilidade com 2 servidores no
mesmo cliente (armadilha documentada). Ver `repositories/ha-mcp/REPORT.md` §16.
