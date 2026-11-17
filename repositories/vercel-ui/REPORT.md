# Vercel UI SDK — biblioteca de comportamentos de interface

| Campo | Valor |
|---|---|
| ID | `LR-UI-001` |
| Categoria | ui |
| Projetos beneficiados | Lia-Project (Stage Vue), Lia Forge, Lia Agent Hub |
| Fontes | `vercel-labs/ui@10b3b6c0eccfd176a6d60ce4efaccf0d1584da08:README.md`, `packages/*`, tree |
| Versão/commit analisado | `10b3b6c` (2026-11-17), release `@ui-sdk/web@0.1.0-beta.7` |
| Data | 2026-11-17 |
| Próxima revisão | 2027-01-17 (60 dias — beta ativo) |
| Status | CURRENT |
| Recomendação | **ADAPTAR** (avaliar protótipo isolado; não adicionar dependência agora) |
| Licença | Apache-2.0 + Vercel Beta Terms |
| Confiança | **Alta** para estrutura/licença; **Média** para maturidade de API |

---

## 1. Identificação

- **Nome:** UI SDK (`@ui-sdk/core`, `@ui-sdk/react|vue|svelte|solid|web`)
- **URL:** https://github.com/vercel-labs/ui · docs https://ui-sdk.dev
- **Organização:** `vercel-labs` (laboratório da Vercel)
- **Licença:** Apache-2.0 no repositório; **uso sujeito aos Vercel beta terms** (`CONFIRMED` no README §Beta terms)
- **Commit:** `10b3b6c` (2026-11-17T12:01:12Z)
- **Métricas:** ★5.468 · 178 forks · 146 issues · criado 2026-10-26 (≈3 semanas) · 7.900 arquivos · **1.306 arquivos de teste** · 5 workflows · 100 changesets
- **Posição declarada:** "UI SDK is in beta" (`CONFIRMED`)

## 2. Resumo executivo

O UI SDK não é uma biblioteca de componentes visuais: é uma biblioteca de
**comportamentos** *headless* — navegação por teclado, foco, seleção, dismissal,
popups, drag-and-drop e o ARIA correspondente — com adaptadores para React, **Vue**,
Svelte, Solid e Web Components. Você compõe primitivas (`definePrimitive`) com
comportamentos (`createPopup`, `createSelection`, `createFocusRecovery`,
`createTypeahead`, `createShortcuts`).

Para a Lia isso é diretamente relevante por dois motivos: o Stage é Vue, e a maior
fonte de dívida de UX em desktop Electron é justamente **foco, teclado, popup e
dismissal**. O pacote `packages/vue` existe, com módulo Nuxt
(`packages/vue/nuxt/module.ts`) e 713 arquivos `.vue` no repositório — não é um
adaptador de fachada (`CONFIRMED`).

O problema é o calendário: o projeto tem **três semanas** de vida, 146 issues abertas,
versão `0.1.0-beta.7` e termos beta próprios. Adicionar isso ao produto agora seria
trocar dívida de UX por dívida de dependência instável.

## 3. O que resolve

| Problema real | Como resolve |
|---|---|
| Foco se perde ao fechar popup | `createFocusRecovery({ fallback })` |
| Cada menu reimplementa teclado/ARIA | comportamentos compartilhados em `@ui-sdk/core` |
| Seleção múltipla com teclado inconsistente | `createSelection` |
| Dismissal (Esc, clique fora, blur) divergente | comportamento de popup |
| Agente precisa construir UI sem inventar acessibilidade | SDK + skill para agente (`npx skills add vercel-labs/ui --skill ui-sdk`) |

## 4. Arquitetura

```text
packages/core        comportamentos puros + ARIA (sem framework)
  └─ createPopup, createSelection, createFocusRecovery,
     createTypeahead, createShortcuts, definePrimitive
packages/react|vue|svelte|solid|web   adaptadores finos
apps/docs            documentação (MDX)
apps/playground      ambiente de teste
examples (3.217 arq.) demonstrações extensas
.changeset (100)     versionamento independente por pacote
```

O padrão arquitetural é o que importa: **lógica de comportamento fora da camada de
render**, com adaptador por framework. Isso permite que a Lia use os mesmos
comportamentos em Vue (Stage) e no futuro em outras superfícies.

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Navegação por teclado | beta | `CONFIRMED` README |
| Gestão de foco (recovery) | beta | `CONFIRMED` (API `createFocusRecovery`) |
| Seleção (single/multi) | beta | `CONFIRMED` |
| Popups/overlays | beta | `CONFIRMED` (doc fala de popover nativo do browser) |
| Dismissal | beta | `CONFIRMED` |
| Typeahead | beta | `CONFIRMED` |
| Drag and drop | beta | `CONFIRMED` |
| ARIA/acessibilidade | beta | `CONFIRMED` (descrita como responsabilidade do core) |
| Adaptador Vue | beta | `CONFIRMED` (`packages/vue`, 713 `.vue`) |
| Módulo Nuxt | existe | `CONFIRMED` (`packages/vue/nuxt/module.ts`) |
| Web Components | beta | `CONFIRMED` (`packages/web`) |
| Skill para agente | existe | `CONFIRMED` (`npx skills add`) |
| WebMCP (agente controlando a UI) | experimental | `CONFIRMED` (doc `agents/connect-an-agent/webmcp.mdx`) |
| Suporte a Electron | não documentado | `UNVERIFIED` |

## 6. Dependências

- Pacotes publicados por framework, sem dependência cruzada obrigatória entre eles.
- `apps/docs` e `apps/playground` trazem stack de documentação (não vai para o produto).
- Versões: beta (`0.1.0-beta.x`), versionadas por changesets.
- **Não verificado**: tamanho de bundle de `@ui-sdk/vue`, dependências transitivas
  exatas → `UNVERIFIED` (requer inspeção de `package.json` publicada no npm; não feito
  para não instalar nada).

## 7. Requisitos de hardware e sistema

- É biblioteca de front-end: sem requisito de hardware. Roda onde o Vue roda —
  incluindo Electron no Windows 11 do usuário.
- Node 22+ provavelmente necessário para o playground (não confirmado no README lido).

## 8. Segurança e privacidade

- Biblioteca de UI: sem coleta de dados própria, sem servidor, sem telemetria
  identificada na leitura (`OBSERVED`: nenhuma dependência de analytics nos pacotes).
- Risco real: **supply chain de pacote npm em beta** e a superfície de WebMCP (permitir
  que um agente dirija a interface do usuário). WebMCP é experimental e deve ser
  tratado como recurso de laboratório, não caminho de produção.
- Nenhum advisory identificado nesta leitura (`UNVERIFIED` — não foi consultado o
  histórico de advisories).

## 9. Licença e proveniência

- **Apache-2.0** no repositório (`CONFIRMED`).
- **Vercel Beta Terms** aplicáveis ao uso durante o beta — é um termo adicional de
  *serviço/uso*, não uma licença de código. Ler antes de qualquer integração de
  produto; pode impor condições de uso, suporte e continuidade.
- Classe: `ADAPT_ALLOWED` para código; `INDEPENDENT_REIMPLEMENTATION` para os padrões
  (comportamentos são ideias implementáveis de forma independente).
- Marca: "Vercel" e o nome "UI SDK" não são licenciados.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~3 semanas | **muito imaturo** |
| Versão | 0.1.0-beta.7 | API em movimento |
| Issues abertas | 146 | alto para a idade |
| Testes | 1.306 arquivos | investimento sério em qualidade |
| CI | 5 workflows | ok |
| Backing | Vercel Labs | provável continuidade; mas labs = experimental |
| Changesets | 100 | releases frequentes por pacote |

## 11. Custos e limitações

- Custo de integração: médio — exige repensar componentes do Stage em torno de
  primitivas, não apenas trocar imports.
- Custo de manutenção: alto enquanto beta (breaking changes prováveis).
- Limitações: sem garantia de estabilidade; termos beta; sem evidência de uso em
  Electron; documentação em movimento.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Vue (Stage) | **sim** | pacote real + 713 `.vue` |
| TypeScript | sim | projeto TS |
| Electron | `UNVERIFIED` | biblioteca DOM padrão, mas sem teste documentado |
| Windows 11 | sim | irrelevante para lib DOM |
| Node/pnpm workspace | sim | monorepo com pnpm-like |
| Acessibilidade exigida pela Lia | endereça exatamente | foco/teclado/ARIA |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia-Project | comportamentos de popup/foco/seleção no Stage Vue |
| Lia Forge | painéis e menus do editor de assets |
| Lia Agent Hub | UI de catálogo e revisão (Vue/React) |

## 14. Oportunidades de reutilização

1. **Modelo mental "comportamento ≠ componente"** — o aprendizado mais valioso, e ele
   não custa dependência.
2. `createFocusRecovery` como solução específica para o problema clássico de foco em
   Electron.
3. **Skill empacotada para agente** (`npx skills add ... --skill ui-sdk`): exemplo de
   como distribuir conhecimento de UI para agentes — padrão para as Skills Lia.
4. WebMCP como referência para "agente que opera a própria interface".

## 15. Riscos e incompatibilidades

| Risco | Severidade | Probabilidade | Mitigação |
|---|---|---|---|
| Beta com breaking changes | **alta** | alta | protótipo isolado; pin exato; sem adoção em produto até 1.0 |
| Termos beta da Vercel | média | certa | leitura jurídica antes de produto |
| 146 issues em 3 semanas | média | média | acompanhar taxa de correção em 60 dias |
| Reescrita do Stage em torno de primitivas | alta | média | avaliar em uma tela, não no Stage inteiro |
| WebMCP dirigindo UI do usuário | alta (segurança) | baixa | manter experimental, fora do produto |
| Supply chain npm | média | baixa | lockfile + auditoria |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | Apache-2.0 | CONFIRMED | `@10b3b6c:LICENSE` | 2026-11-17 |
| E2 | Beta com termos da Vercel | CONFIRMED | `README.md` §Beta terms | 2026-11-17 |
| E3 | Adaptador Vue real, com Nuxt | CONFIRMED | `packages/vue`, `packages/vue/nuxt/module.ts` | 2026-11-17 |
| E4 | 5 adaptadores | CONFIRMED | `packages/{core,react,solid,svelte,vue,web}` | 2026-11-17 |
| E5 | Comportamentos: popup, selection, focus, typeahead, shortcuts, DnD | CONFIRMED | README + `packages/core` | 2026-11-17 |
| E6 | 1.306 arquivos de teste | CONFIRMED | tree `@10b3b6c` | 2026-11-17 |
| E7 | Versão 0.1.0-beta.7 | CONFIRMED | release list | 2026-11-17 |
| E8 | Suporte a Electron | UNVERIFIED | não documentado, não testado | — |

## 17. Recomendação

**`ADAPTAR`** — aproveitar o modelo de comportamentos e, no máximo, `@ui-sdk/vue` em
protótipo isolado.

**Gates:**

1. protótipo em **uma** tela do Stage, fora do `main` do produto;
2. pin de versão exata (sem `^`), com renovação manual;
3. leitura dos Vercel beta terms antes de qualquer release;
4. nenhum uso de WebMCP em produto;
5. reavaliação em 60 dias: se issues abertas não caírem e a API continuar mudando,
   manter apenas o padrão.

**Não autoriza:** adicionar `@ui-sdk/vue` ao projeto agora, reescrever componentes,
ou introduzir WebMCP.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Protótipo isolado: um popup + seleção com teclado no Stage | Lia-Project | comparação com implementação atual |
| 2 | Medir o custo de bundle de `@ui-sdk/vue` | Lia-Project | número, não impressão |
| 3 | Ler os Vercel beta terms | proprietário | `AGUARDA DECISÃO` sobre viabilidade jurídica |
| 4 | Levantar issues abertas por tipo (bug × feature) | Research | indicador de estabilidade real |
| 5 | Revisar em 60 dias | Research | decisão de manter `ADAPTAR` ou rebaixar para `REFERÊNCIA` |
