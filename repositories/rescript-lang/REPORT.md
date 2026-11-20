# ReScript — linguagem tipada que compila para JavaScript (organização)

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-003` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | studio (linguagem/stack) |
| Projetos beneficiados | (nenhum diretamente — avaliação de stack) |
| Fontes | `api.github.com/orgs/rescript-lang/repos` (39 repos, 2026-11-17); `rescript-lang/rescript` (`LICENSE` com texto por diretório) |
| Versão/commit | não fixado — análise de **organização**; o compilador é `rescript-lang/rescript` (★7.486) |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `rescript-lang/rescript` · HEAD `b2df86941d6e` · sem SHA analisado registrado |
| Próxima revisão | 2027-11-17 (tema estável) |
| Recomendação | **REJECT** (adoção de stack) / **REFERENCE_ONLY** (interop e compilação) |
| Licença | **múltipla**: `compiler/` **LGPL-3.0-or-later**; `compiler/syntax/`, `runtime/`, `belt/`, `rewatch/` **MIT** |
| Confiança | Alta para licença e organização; Média para ecossistema |

---

## 1. Identificação

- **Nome:** ReScript (organização `rescript-lang`)
- **URL:** https://github.com/rescript-lang (organização; **o link da ordem de serviço
  é uma organização, não um repositório** — 39 repositórios públicos)
- **Licença:** `rescript` é multi-licença (`CONFIRMED` no arquivo `LICENSE`, que declara
  o mapa por diretório: `compiler/` LGPL-3.0-or-later; `compiler/syntax/` MIT;
  `packages/@rescript/runtime/` MIT; `packages/@rescript/belt/` MIT; `rewatch/` MIT);
  o site (`rescript-lang.org`), `rescript-react`, `rescript-vscode`, `reanalyze`,
  `syntax`, `rescript-core`, `vim-rescript` são MIT; o GitHub reporta `NOASSERTION`
  para o compilador justamente por ser multi-licença.
- **Data:** 2026-11-17

## 2. Resumo executivo

ReScript é uma linguagem funcional robustamente tipada que compila para JavaScript
legível e eficiente. A organização tem 39 repositórios, com um ecossistema coerente:
compilador, sintaxe standalone, biblioteca padrão (`rescript-core`), bindings para
React, extensão de VSCode, `reanalyze` (análise de código morto) e um build system
alternativo (`rewatch`).

A avaliação para a Lia é simples e negativa: a stack dos cinco projetos é
**TypeScript + Vue + Electron** (com Godot na Studio e Python/Rust em ferramentas).
ReScript não interopera com Vue de forma nativa (bindings oficiais existem para
**React**, não Vue), exige toolchain própria (bsconfig/ninja), e adotá-la significaria
reescrever o Stage. Não há benefício que justifique — e a ordem de serviço pede
explicitamente para não alterar arquitetura por associação com repositório pesquisado.

Duas coisas merecem registro: (a) o **modelo de licença por diretório** é exemplar e
resolve o `NOASSERTION` do GitHub com clareza; (b) o `reanalyze` (detecção de código
morto) é uma ferramenta que poderia beneficiar a Lia independentemente da linguagem —
embora seja específica de ReScript/OCaml.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| JS sem garantias de tipo em runtime | compilação estrita, sem `any` implícito |
| Output difícil de ler | compila para JS legível |
| Migração incremental | interoperável com JS/TS existente (`INFERRED` do desenho da linguagem) |
| Análise de código morto | `reanalyze` |
| Build mais rápido | `rewatch` |

## 4. Arquitetura da organização

| Repositório | ★ | Licença | Papel |
|---|---:|---|---|
| `rescript` | 7.486 | LGPL-3.0-or-later + MIT (por diretório) | compilador |
| `rescript-lang.org` | 1.853 | MIT | site de documentação |
| `rescript-react` | 517 | MIT | bindings React |
| `rescript-vscode` | 357 | MIT | extensão de editor |
| `reanalyze` | 281 | MIT | análise estática (dead code) |
| `syntax` | 253 | MIT | gramática standalone |
| `awesome-rescript` | 205 | — | lista curada |
| `rescript-core` | 170 | MIT | biblioteca padrão |
| `vim-rescript` | 164 | MIT | plugin |
| `rewatch` | 130 | — | build system alternativo |

(Outros 29 repositórios menores; `bucklescript.github.io` é legado.)

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Compilador estável | sim | releases contínuas |
| Bindings oficiais para **React** | sim | `rescript-react` |
| Bindings oficiais para **Vue** | **não** | ausente na organização |
| Extensão de VSCode | sim | `rescript-vscode` |
| Análise de código morto | sim | `reanalyze` |
| Build alternativo | experimental | `rewatch` |

## 6. Dependências

- Toolchain Node + binário de compilador; `ninja`/`rewatch` para build.
- Interop com npm.

## 7. Requisitos de hardware e sistema

- Trivial para desenvolvimento. Sem impacto em runtime além do JS gerado.

## 8. Segurança e privacidade

- Linguagem/compilador: risco de supply chain de toolchain (binários por plataforma).
- Nenhuma telemetria conhecida (`UNVERIFIED`).

## 9. Licença e proveniência

| Componente | Licença | Implicação |
|---|---|---|
| `compiler/` | **LGPL-3.0-or-later** | usar o compilador é permitido; modificar e distribuir o compilador exige liberar as modificações sob LGPL. **O código que ele gera não herda a licença** (`INFERRED`, comportamento típico de compilador). |
| `syntax/`, `runtime/`, `belt/`, `rewatch/` | MIT | permissivas |
| Site/docs | MIT | — |

Ponto de qualidade: o arquivo `LICENSE` **declara o mapa por diretório**, o que
transforma um `NOASSERTION` do GitHub em informação auditável. É o segundo melhor
exemplo de governança de licença entre os 16 repositórios (atrás do `LICENSES/` do
ManimGX).

Classe: `RESEARCH_ONLY` para o ecossistema como um todo (não há intenção de adotar);
`USE_AS_IS` se algum dia usar o compilador como ferramenta.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Compilador | ★7.486, ativo | maduro |
| Governança | organização com múltiplos mantenedores | saudável |
| Documentação | site próprio + awesome list | boa |
| Adoção | nicho, estável | não cresce como TS |

## 11. Custos e limitações

- Custo de adoção na Lia: **muito alto** (reescrever Stage/TS; sem bindings Vue).
- Ganho esperado: tipos melhores e output menor — insuficiente para justificar.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Vue (Stage) | **não** nativamente | sem bindings oficiais |
| Electron | possível (gera JS) | mas sem ganho claro |
| TypeScript existente | interop com JS, não com tipos TS | migração trabalhosa |
| Godot (Studio) | irrelevante | — |
| Custo de manutenção da equipe | alto | nova linguagem |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| (nenhum) | — |
| Lia Studio | apenas como referência de design de linguagem/tooling |

## 14. Oportunidades de reutilização

1. **`LICENSE` com mapa por diretório** — solução direta para o problema de licença
   mista que as Skills Lia vão enfrentar (código próprio + adaptações MIT + assets).
2. **`reanalyze`** como conceito: análise de código morto em projeto grande; a Lia tem
   duplicação conhecida (skills repetidas) que uma ferramenta equivalente detectaria.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Adotar a linguagem por entusiasmo técnico | **alta** | rejeitada; decisão registrada |
| Fragmentar a stack (TS + ReScript) | alta | não fazer |
| LGPL mal interpretada no compilador | baixa | não modificar o compilador |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | 39 repositórios na organização | CONFIRMED | `GET /orgs/rescript-lang/repos` | 2026-11-17 |
| E2 | `compiler/` LGPL-3.0-or-later; runtime/belt/syntax/rewatch MIT | CONFIRMED | `rescript-lang/rescript:LICENSE` (texto por diretório) | 2026-11-17 |
| E3 | Bindings oficiais para React, não para Vue | CONFIRMED | lista de repos da organização | 2026-11-17 |
| E4 | Compilador com ★7.486 | CONFIRMED | API | 2026-11-17 |
| E5 | Output JS não herda LGPL do compilador | INFERRED | comportamento típico de compilador; confirmar com jurídico se necessário | — |

## 17. Recomendação

**`REJECT`** para adoção de stack; **`REFERENCE_ONLY`** para o modelo de licença e para
a ideia de análise estática.

Justificativa: incompatibilidade com a stack real (Vue), custo de migração altíssimo,
ganho não demonstrado para o caso de uso, e nenhum projeto Lia precisa de uma segunda
linguagem de aplicação.

**Não autoriza:** introduzir ReScript em qualquer projeto, nem traduzir código atual.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Registrar `REJECTED` com motivo e condição de reabertura (aparecimento de bindings Vue maduros + ganho medido) | Research | `DR` registrado |
| 2 | Adotar o padrão "LICENSE com mapa por diretório" no Lia-Research | Research | arquivo atualizado |
| 3 | Revisar em 12 meses (tema estável) | Research | — |
