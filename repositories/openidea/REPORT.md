# OpenIDEA — IDE em Rust/Tauri (referência para Lia Studio)

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-001` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | studio |
| Projetos beneficiados | Lia Studio (Lia Forge e Agent Hub como referência secundária) |
| Fontes | `l0ng-ai/openidea@182285647ee2a80e84c01157ae35d6b63f572d71:README.md`, tree (`crates/`, `plugins/`), `LICENSE`, releases |
| SHA completo | `182285647ee2a80e84c01157ae35d6b63f572d71` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — SHA citado no próprio relatório |
| HEAD atual | `6d157c8b711faa27ef8ca065fb04c22cd14c5f43` (conferido em 2026-11-20) |
| Versão/commit | `1822856` (2026-11-17), release `v0.1.47` + nightly `0.1.48-nightly` |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `l0ng-ai/openidea` · HEAD `e6905f288ea4` · mudou desde a análise (conteúdo novo não lido) |
| Próxima revisão | 2027-01-19 |
| Recomendação | **REFERENCE_ONLY** |
| Licença | Apache-2.0 (`CONFIRMED`) |
| Confiança | Alta para estrutura/licença; Baixa para desempenho e benchmarks |

---

## 1. Identificação

- **Nome:** OpenIDEA
- **URL:** https://github.com/l0ng-ai/openidea · site openidea.sh
- **Organização:** `l0ng-ai`
- **Licença:** Apache-2.0 — `CONFIRMED`
- **Commit:** `1822856` (2026-11-17T15:22:56Z)
- **Métricas:** ★9.279 · 854 forks · **158 issues abertas** · criado 2026-10-21 (≈4 semanas) · 6.316 arquivos · 1.022 `.rs` + 1.974 `.ts` + 726 `.tsx` · **847 arquivos de teste** · 144 e2e · 7 workflows · 45 crates

## 2. Resumo executivo

OpenIDEA é um IDE desktop escrito em Rust com frontend TypeScript (Tauri), com
keymap estilo IntelliJ, *tool windows*, *search-everywhere*, editor, LSP, DAP
(debugger), Git, terminal, cliente de banco e cliente HTTP, plugin system e mais de
60 linguagens. Em quatro semanas chegou a um escopo que normalmente leva anos — o que
é ao mesmo tempo impressionante e um sinal de alerta sobre maturidade real.

Para a Lia Studio, o interesse **não** é virar um IDE: é entender como um app Rust
organiza 45 crates (incluindo `ide-mcp`, `ide-lsp`, `ide-dap`, `ide-plugin`,
`ide-vfs`, `ide-search`) e como um plugin/skill system é estruturado — algo
diretamente análogo às necessidades de extensibilidade da Studio e do Forge.

Ressalva metodológica: o projeto **não publica benchmarks reproduzíveis** na
documentação lida. Qualquer afirmação de desempenho seria `REPORTED` ou `UNVERIFIED`.
A ordem de serviço pede benchmarks reproduzíveis — e eles não existem aqui.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| IDE Electron é pesado | app nativo Rust + Tauri |
| Fragmentação de ferramentas (editor, git, db, http) | tool windows unificadas |
| Extensibilidade | sistema de plugins com SDK (`ide-plugin`, `ide-sdk`, `plugins/official`) |
| Integração com agentes | crate `ide-mcp` + `ide-agent` (`CONFIRMED` pela árvore) |
| Múltiplas linguagens | `languages/` (86 entradas) + `ide-lsp` |

## 4. Arquitetura

```text
src-tauri/        shell Tauri (103 arquivos)
crates/ (45)      núcleo Rust
  ide-core, ide-workspace, ide-vfs, ide-text, ide-syntax, ide-index, ide-search
  ide-lsp, ide-dap, ide-run, ide-build, ide-terminal
  ide-vcs, ide-github, ide-remote, ide-ssh
  ide-db, ide-http, ide-notebook, ide-coverage, ide-profiler
  ide-plugin, ide-sdk, ide-extension, ide-mcp, ide-agent
  ide-analysis, ide-command, ide-clipboard, ide-fonts, ide-streams, ide-tools ...
plugins/          plugins/official, indexing.md, themes.md, build.sh
languages/ (86)   gramáticas/queries
src/ (3.763)      frontend TS/TSX
e2e/ (144), evals/ (55), fixtures/ (113)
```

O desenho por crates é o que há de mais reutilizável como **modelo**: cada
responsabilidade (VFS, busca, LSP, DAP, VCS) é um crate independente com fronteira
explícita. É o oposto de "um binário monolítico com módulos internos".

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Editor com keymap IntelliJ | estável (0.1.x) | `REPORTED` README |
| LSP / code insight | existe | `CONFIRMED` (`ide-lsp`, `ide-analysis`) |
| Debugger DAP (+ JDWP) | existe | `CONFIRMED` (`ide-dap`, `ide-jdwp`) |
| Git | existe | `CONFIRMED` (`ide-vcs`, `ide-github`) |
| Terminal | existe | `CONFIRMED` (`ide-terminal`) |
| Cliente de banco | existe | `CONFIRMED` (`ide-db`) |
| Cliente HTTP | existe | `CONFIRMED` (`ide-http`) |
| Plugin system | existe | `CONFIRMED` (`plugins/`, `ide-plugin`, `ide-sdk`) |
| MCP / agente integrado | existe | `CONFIRMED` (`ide-mcp`, `ide-agent`) |
| 60+ linguagens | `REPORTED` | README; 86 entradas em `languages/` |
| Benchmarks reproduzíveis | **ausente** | `UNVERIFIED` |
| Consumo de memória documentado | **ausente** | `UNVERIFIED` |

## 6. Dependências

- Rust toolchain + Tauri (WebView nativo em vez de Chromium embutido — `INFERRED` pelo Tauri).
- Frontend TypeScript (build próprio).
- Não foi feita leitura completa de `Cargo.toml` do workspace → lista exata de crates
  de terceiros `UNVERIFIED`.
- Plugins oficiais distribuídos no repositório.

## 7. Requisitos de hardware e sistema

- Cross-platform (Windows/macOS/Linux; topic `cross-platform`) — `REPORTED`.
- Windows 11 + Ryzen 5 5500 + 16 GB: plausível para editor/depuração; **não medido**.
- RX 580: irrelevante para o IDE (sem requisito de GPU), mas isso não foi verificado
  com execução.
- Consumo de memória: `UNVERIFIED` — e é justamente a métrica que a ordem de serviço
  pediu. Sem execução, não há resposta.

## 8. Segurança e privacidade

| Item | Rótulo | Avaliação |
|---|---|---|
| Sistema de plugins executa código de terceiro | `CONFIRMED` (existência) | **superfície de risco principal**; modelo de permissões não verificado |
| `ide-agent` / `ide-mcp` (agente com acesso ao workspace) | `CONFIRMED` | agente pode ler/editar arquivos do projeto |
| `ide-remote`, `ide-ssh` | `CONFIRMED` | acesso remoto a hosts |
| `ide-db` guarda credenciais de banco? | `UNVERIFIED` | verificar armazenamento antes de recomendar padrão |
| Telemetria? | `UNVERIFIED` | não identificada na leitura |
| Advisories | `UNVERIFIED` | projeto jovem, sem histórico consultado |

Nada aqui indica falha; indica **superfície não avaliada**. Não é base para adoção.

## 9. Licença e proveniência

- **Apache-2.0** (`CONFIRMED`). Obrigações: aviso, texto, NOTICE, indicar alterações.
- Classe: `INDEPENDENT_REIMPLEMENTATION` (padrões) / `RESEARCH_ONLY` (código).
- Marca: "OpenIDEA", "IntelliJ IDEA" (referência de keymap) — marcas de terceiros não
  licenciadas. Um produto Lia não pode se apresentar como "IDE estilo IntelliJ" sem
  cuidado com marca.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~4 semanas | muito imaturo |
| Versão | 0.1.47 + nightly diário | pré-1.0, cadência altíssima |
| Issues abertas | 158 | alto |
| Testes | 847 + 144 e2e | investimento sério |
| Escopo | 45 crates, 60+ linguagens | escopo grande para a idade |
| Sustentabilidade | desconhecida | `UNVERIFIED` |

Escopo excepcional em tempo excepcionalmente curto é um padrão que merece cautela:
pode indicar geração massiva assistida por IA, com profundidade desigual. Não é
julgamento, é hipótese a testar (`INFERRED`).

## 11. Custos e limitações

- Gratuito (Apache-2.0). Custo de adoção de código: alto (Rust + Tauri + 45 crates).
- Limitações: pré-1.0, sem benchmarks, sem histórico, sem estabilidade de API de plugin.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 | sim (`REPORTED`) | cross-platform declarado |
| Rust no ecossistema | parcial (Forge/Studio usam Node/Godot) | custo de stack novo |
| Tauri vs Electron (Lia) | arquitetura diferente | referência, não base |
| Extensibilidade por plugin | conceito compatível | modelo mental útil |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Studio | padrão de organização em crates, plugin system, tool windows |
| Lia Forge | referência de VFS/asset browser e de cliente HTTP/DB |
| Lia Agent Hub | `ide-mcp` como exemplo de agente embutido no host |

## 14. Oportunidades de reutilização

1. **Divisão em crates por responsabilidade** (`ide-vfs`, `ide-search`, `ide-lsp`):
   fronteiras explícitas em vez de módulos acoplados.
2. **Plugin SDK + plugins oficiais no mesmo repo**: padrão de extensibilidade com
   exemplos de referência.
3. **Agente integrado ao host via MCP** (`ide-mcp`): modelo para "ferramenta que o
   agente usa" dentro de um app de criação.
4. **Tool windows / search-everywhere** como padrão de UX para apps complexos.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Adotar stack Rust/Tauri na Studio | alta | manter Godot/TS; usar só padrões |
| Plugins executando código arbitrário | alta | não replicar sem modelo de permissão |
| Projeto imaturo com escopo enorme | alta | referência, não dependência |
| Ausência de benchmarks | média | não citar desempenho |
| Marca "IntelliJ" | baixa | evitar associação em produto |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | Apache-2.0 | CONFIRMED | `@1822856:LICENSE` | 2026-11-17 |
| E2 | 45 crates, incluindo `ide-mcp`, `ide-lsp`, `ide-dap`, `ide-plugin` | CONFIRMED | tree `crates/` | 2026-11-17 |
| E3 | Plugin system com SDK e plugins oficiais | CONFIRMED | `plugins/README.md`, `ide-sdk` | 2026-11-17 |
| E4 | 847 testes + 144 e2e | CONFIRMED | tree (contagem) | 2026-11-17 |
| E5 | 60+ linguagens | REPORTED | README | 2026-11-17 |
| E6 | Benchmarks reproduzíveis | UNVERIFIED | não encontrados | — |
| E7 | Consumo de memória | BLOCKED | exigiria execução | — |
| E8 | Suporte Windows validado | UNVERIFIED | declarado, não testado | — |

## 17. Recomendação

**`REFERENCE_ONLY`** — estudar organização em crates, plugin system e integração de agente;
não adotar código nem stack.

**Gates** (se algum dia houver adoção de padrão):

1. nenhuma migração de stack da Studio (Godot/TS) por influência deste repositório;
2. padrão de plugin só com modelo de permissão definido;
3. desempenho nunca citado sem medição própria.

**Não autoriza:** transformar a Lia Studio em IDE genérica, introduzir Rust/Tauri no
produto, ou adotar plugins de terceiros.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Extrair o mapa de responsabilidades dos 45 crates como referência de modularização | Studio | doc de 1 página |
| 2 | Ler o modelo de permissão de plugins (`ide-plugin`) | Studio/Research | `CONFIRMED` ou `BLOCKED` |
| 3 | Se houver interesse em medição, executar build e medir memória em idle | Studio | benchmark próprio |
| 4 | Revisar em 90 dias | Research | novo commit |

## Reauditoria 2026-11-20

| Campo | Valor |
|---|---|
| Versão anteriormente analisada | ``182285647ee2` (2026-11-17)` |
| Versão novamente examinada | ``6d157c8` (+515 commits, release `v0.1.49`)` (2026-11-20) |
| Método | `compare` da API do GitHub (commits + arquivos), leitura de arquivos materiais no HEAD, estado de CI no HEAD, releases |
| Mudanças encontradas | 515 commits, 300 arquivos (truncado): `crates/` (293), 3 workflows, `Cargo.lock`/`Cargo.toml`. Commits: correções em bench, VCS (seleção de branch, largura de log), abrir projeto em nova aba, postcondições de operação. |
| Evidências novas | Atividade intensa num projeto ainda em `0.1.x`: a API e a estrutura mudam rápido. `LICENSE` não aparece entre os arquivos alterados. |
| Testes próprios | **Bloqueado**: Rust; `cargo` ausente. |
| Testes independentes | CI no HEAD: apenas 1 check *skipped* — **não há evidência de CI verde neste commit**; isso é um dado, não um defeito. |
| Conclusão | Recomendação **reavaliada e mantida em `REFERENCE_ONLY`**. Sem CI verificável no HEAD e com 515 commits de diferença, qualquer conclusão sobre código seria leitura de superfície. |
| Próxima revisão | 60 dias. |

