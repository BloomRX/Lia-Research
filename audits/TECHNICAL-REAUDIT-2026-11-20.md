# Reauditoria técnica — 2026-11-20

| Campo | Valor |
|---|---|
| Data | 2026-11-20 |
| Objetos reavaliados | 22 (todos os herdados de 2026-11-17); o 23º (`LR-STUDIO-006`) nasceu hoje |
| Método | `compare` da API (commits + arquivos), leitura de arquivos materiais no HEAD, CI do upstream no HEAD, releases, testes próprios em ambiente isolado |
| O que **não** foi feito | leitura integral de código de cada objeto; nenhum objeto Rust/C#/Go/Blender foi executado (toolchain ausente) |
| Registro por objeto | seção `Reauditoria 2026-11-20` em `repositories/*/REPORT.md` |
| Registro de execução | `data/testing/test-log.tsv` (16 linhas) |

## 1. Números

| Medida | Valor |
|---|---|
| Objetos com commit novo desde a análise | **10 confirmados** + 1 (`freellmapi`) medido a partir de SHA candidato |
| Objetos sem commit novo | **11** (+1 objeto novo) |
| Commits totais no intervalo (11 objetos) | **3.576** |
| Maior movimento | `plannotator` +1.511 · `artcraft` +1.011 · `openidea` +515 · `sculptforge` +285 |
| Arquivos alterados analisados | 300 por objeto (limite da API; truncado em 6 objetos) |
| Recomendações alteradas | **0** |
| Motivos de recomendação alterados | **1** (`sculptforge`: o bloqueio de licença caiu; o rótulo ficou) |
| Testes próprios executados | **5 suítes** em 5 objetos + 2 execuções parciais + **9 tentativas bloqueadas**, todas com linha no log |
| Testes aprovados | `ai-design-skills` 17/17 · `claude-bughunter` 65/65 · `cloudflare` 65/65 (34+31) · `claude-trading-skills` 3.530 de 3.598 · `freellmapi` 2.044 de 3.840 |
| Testes falhos | `claude-trading-skills` 88 (+73 erro de coleta) · `freellmapi` 1.796 (dominados por `better-sqlite3` ausente) |
| Bloqueados | 9 objetos: Rust (5), C#/.NET (1), C++/Blender (1), Manim/LaTeX (1), Python ≥3.14 + HA (1) |
| Versões pinadas conferidas contra release real | 7 |

## 2. O que mudou de fato nos 10

| Objeto | Mudança material | Efeito na conclusão |
|---|---|---|
| `ha-mcp` | `requires-python >=3.14`, FastMCP vendorizado, addon dev 9.3.0.dev3612/3615 | nenhum na recomendação; **nova condição de contorno** (runtime) |
| `misterdownloadmanager` | ClusterFuzzLite, CodeQL, Scorecard no CI; log com fila limitada | melhora de segurança; GPL inalterada |
| `sculptforge` | **`LICENSE-EXCEPTION.md`** (scripting) + pacote Python + scripting no app | **motivo da recomendação muda**: GPL deixa de bloquear script via API/CLI/MCP |
| `openjarvis` | `Chrono` substituído; `doctor` não sonda engine remota por padrão | risco de dependência menor; nenhum motivo novo de adoção |
| `claude-bughunter` | ferramenta MCP `get_report`; UTF-8 no Windows | nenhum |
| `claude-trading-skills` | correção de sizing ATR e de retry 429 | nenhum |
| `vercel-ui` | correções de acessibilidade e controle | nenhum |
| `plannotator` | virou família de plugins (Cline/opencode/pi); **1 check vermelho no HEAD** | ressalva nova registrada |
| `artcraft` | +1.011 commits, 186 crates, v0.23.1 | nenhum; revisão encurtada para 60 dias |
| `openidea` | +515 commits, v0.1.49, **CI só com skipped no HEAD** | sem evidência de CI verde — registrado |

## 3. Objetos sem commit novo: o que foi reverificado

Não basta "o SHA é o mesmo". Para os 11, esta rodada conferiu:

1. **Licença no HEAD** (não só no commit analisado) — inclusive o caso `unslop`, onde a
   ausência de licença foi confirmada de novo em vez de herdada.
2. **Releases posteriores à análise** — `claude-code-game-studios` (v1.3.0) e `brutal`
   (v2026.10.1) têm release, mas anterior à análise; `ai-memory` tem `v3.5.1` *posterior*
   (o relatório descreve versão anterior).
3. **CI no HEAD** quando o repositório publica checks.
4. **Teste próprio** onde havia como executar (`ai-design-skills`, `cloudflare`).

## 4. Onde a reauditoria foi mais fraca — e por quê

| Objeto | Limite |
|---|---|
| `artcraft`, `openidea`, `plannotator` | 300 arquivos é teto da API; a lista é amostra grande, não o diff inteiro |
| `freellmapi` | suíte não conclui sem `better-sqlite3`; 1.796 falhas são de ambiente |
| `claude-trading-skills` | 88 falhas não triadas uma a uma; causa observada é import faltando em subprocesso |
| `rescript-lang`, `routerhub` | organização: não existe commit único; "reauditar" é rever a organização e o serviço |
| `ha-mcp` | nenhuma execução: exigiria Python 3.14 **e** instância Home Assistant |

## 5. Conclusão honesta

Os 22 objetos foram reavaliados com evidência nova por objeto. **Isso não é o mesmo que
dizer que todos foram testados**: cinco tiveram execução real, nove estão bloqueados por
toolchain, e oito só têm revisão estática de diff. Nenhuma recomendação mudou de rótulo;
uma mudou de motivo. Declarar "tudo reauditado e validado" seria exatamente o tipo de
afirmação que `governance/TESTING-PROTOCOL.md` proíbe.

Voltar: `audits/README.md` · `audits/REAUDIT-2026-11-20.md` · `audits/PROVENANCE-2026-11-20.md`
