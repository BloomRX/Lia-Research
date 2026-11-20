# ManimGX — engine de animação 3D para agentes (Manim-compatible)

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-003` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | forge |
| Projetos beneficiados | Lia Forge, Lia Studio (referência de render programático) |
| Fontes | `academa-labs/manimgx@1fb4dd7327bf5ed7d0c40d022c05cb816455ae1d:README.md`, tree, `LICENSE`, `LICENSES/`, releases |
| Versão/commit | `1fb4dd7` (commit HEAD 2026-10-24; repositório recebeu push em 2026-11-16), release `v0.1.1` (2026-10-07) |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `academa-labs/manimgx` · HEAD `1fb4dd7327bf` · sem mudança no HEAD |
| Próxima revisão | 2027-02-17 |
| Recomendação | **REFERENCE_ONLY** |
| Licença | MIT + múltiplas (`LICENSES/`: Apache-2.0, CC-BY-SA-4.0, ISC, LLVM-exception, MIT, OFL-1.1) |
| Confiança | Alta para licença/estrutura; Baixa para desempenho |

---

## 1. Identificação

- **Nome:** ManimGX
- **URL:** https://github.com/academa-labs/manimgx · site manimgx.academa.ai
- **Organização:** `academa-labs`
- **Licença:** MIT no repositório, com árvore `LICENSES/` contendo 6 licenças —
  conformidade estilo REUSE (`CONFIRMED`)
- **Commit:** `1fb4dd7` (2026-10-24T06:15:32Z — HEAD da branch padrão no momento da coleta)
- **Métricas:** ★2.784 · 198 forks · 38 issues · criado 2026-10-05 · 4.532 arquivos · 1.106 `.py` + 42 `.rs` · **4.063 arquivos em `tests/`** (dos quais 845 fixtures `.mkv` e 844 `.sha256`) · 159 `docs/` · 78 `rust/` · 24 `benchmarks/` · 8 workflows

## 2. Resumo executivo

ManimGX é uma engine de animação 3D com **a API do Manim CE** (Python) apoiada em um
núcleo Rust + wgpu, com execução no navegador. O posicionamento é "the animation
engine for agents": animação programática confiável, instalável por prompt ou pip.

Para o Forge e a Studio, é uma referência de nicho: render programático de vídeo
explicativo/técnico não é o core do pipeline de assets, mas pode servir para
documentação de produto, teasers e geração de clipes curtos a partir de dados.

O que este repositório tem de mais valioso **não é a engine**: é a **disciplina de
proveniência de licença** (árvore `LICENSES/` com 6 licenças e fixtures com hash
`.sha256`). É o exemplo mais limpo de governança de licença entre os 16 repositórios
pesquisados, e é diretamente aplicável ao problema de licença das Skills Lia.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Animação matemática/técnica programática | API Manim CE em Python |
| Desempenho de render | núcleo Rust + wgpu |
| Rodar sem instalar stack pesada | execução no navegador |
| Verificação de fixtures em testes | hashes `.sha256` versionados |
| Conformidade de licença | `LICENSES/` com texto de cada licença |

## 4. Arquitetura

```text
src/ (51)        camada Python compatível com Manim
rust/ (78)       núcleo de render (wgpu)
browser/ (17)    execução no navegador
benchmarks/ (24)
docs/ (159)      documentação (site)
tests/ (4.063)   inclui fixtures de vídeo + hashes
LICENSES/ (6)    MIT, Apache-2.0, CC-BY-SA-4.0, ISC, LLVM-exception, OFL-1.1
fonts/ (32)      fontes (OFL)
examples/ (49)
```

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| API compatível com Manim CE | `REPORTED` | README |
| Render 3D em Rust/wgpu | `CONFIRMED` (código presente) | `rust/` |
| Execução no navegador | `REPORTED` | README + `browser/` |
| Instalação por `pip` e por prompt | `REPORTED` | README |
| Benchmarks | existe diretório | `CONFIRMED` (24 arquivos) |
| Integração com agente (skill/MCP) | `REPORTED` ("for agents") | não identificado artefato de skill |

## 6. Dependências

- Python (API Manim), toolchain Rust (build do núcleo), wgpu (GPU via WebGPU/Vulkan/
  Metal/DX12 — `INFERRED` de wgpu).
- Fontes com OFL (declaradas em `LICENSES/`).
- `hypothesis`/pytest provavelmente nos testes (`UNVERIFIED`).

## 7. Requisitos de hardware e sistema

- GPU via wgpu: no Windows com RX 580, wgpu pode usar DX12 ou Vulkan — **plausível**,
  não medido (`UNVERIFIED`).
- Render de vídeo é CPU/GPU-intensivo; não é workload de tempo real.
- Consumo real: `BLOCKED` (não executado).

## 8. Segurança e privacidade

- Biblioteca local de render; sem serviço obrigatório identificado.
- Execução no navegador implica WASM: superfície de sandbox do navegador (`INFERRED`).
- Nenhuma telemetria identificada (`UNVERIFIED` — não auditado a fundo).

## 9. Licença e proveniência

**Este é o ponto alto do repositório.**

| Licença | Onde | Implicação |
|---|---|---|
| MIT | núcleo do projeto | uso amplo com aviso |
| Apache-2.0 | componentes | aviso + NOTICE + indicar alterações |
| CC-BY-SA-4.0 | conteúdo (docs/assets?) | **share-alike em conteúdo** — atenção ao copiar documentação |
| ISC | componentes | permissiva |
| LLVM-exception | provavelmente em componente Rust/C++ | permissiva com exceção de linking |
| OFL-1.1 | fontes | permite uso/embed, com restrições de venda isolada da fonte |

Classe: `ADAPT_ALLOWED` para código MIT; `RESEARCH_ONLY` para conteúdo CC-BY-SA
(copiar texto com share-alike para um repositório proprietário é problema).
Marca: "Manim" é projeto da comunidade Manim; "ManimGX" é deste autor.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~6 semanas | muito jovem |
| Versão | 0.1.1 | pré-1.0 |
| Testes | 4.063 arquivos (inclui fixtures) | investimento alto em verificação |
| CI | 8 workflows | ativo |
| Documentação | 159 arquivos | boa |
| Atividade | push em 2026-11-16, HEAD analisado de 2026-10-24 | **divergência a observar** |

Nota metodológica: o HEAD da branch padrão é de 2026-10-24, enquanto o repositório
registra push em 2026-11-16. Isso indica atividade em outras branches. O commit
analisado é o que está em `main` — declarado explicitamente.

## 11. Custos e limitações

- Gratuito. Custo de adoção: build Rust + Python, dependência de GPU.
- Limitação: nicho (animação matemática), não substitui pipeline de asset de jogo.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 + AMD | provável (wgpu) | não medido |
| Integração ao Forge | baixa prioridade | domínio diferente |
| Agente como consumidor | sim (API Python) | compatível com skills |
| Uso comercial | sim (MIT), atenção ao CC-BY-SA em docs | — |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Forge | geração de vídeos explicativos/teasers de assets |
| Lia Studio | referência de render programático e de proveniência de licença |

## 14. Oportunidades de reutilização

1. **`LICENSES/` com uma licença por arquivo** — padrão REUSE. Recomendado para as
   Skills Lia e para o Lia-Research.
2. **Fixtures com `.sha256`** — verificabilidade de testes sem versionar binário grande
   (aqui há 845 `.mkv`, o que é excessivo; o padrão, não o volume).
3. **API compatível com upstream** como estratégia de adoção: reduz custo de migração
   e permite reuso de exemplos existentes.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Conteúdo CC-BY-SA-4.0 contaminar docs proprietárias | média | não copiar texto/documentação |
| Repositório jovem (0.1.x) | média | não depender |
| Build Rust + GPU | baixa | uso opcional |
| Fontes OFL com restrição de venda isolada | baixa | embutir, não vender a fonte |
| HEAD antigo com pushes recentes | baixa | sempre citar commit analisado |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | MIT + árvore `LICENSES/` com 6 licenças | CONFIRMED | `@1fb4dd7:LICENSE`, `LICENSES/*` | 2026-11-17 |
| E2 | Núcleo Rust (42 `.rs`, 78 em `rust/`) | CONFIRMED | tree | 2026-11-17 |
| E3 | Compatibilidade com API Manim CE | REPORTED | README | 2026-11-17 |
| E4 | 4.063 arquivos de teste, com fixtures `.mkv` + `.sha256` | CONFIRMED | tree (contagem) | 2026-11-17 |
| E5 | wgpu | INFERRED | README menciona wgpu | 2026-11-17 |
| E6 | Desempenho no RX 580 | UNVERIFIED | não executado | — |

## 17. Recomendação

**`REFERENCE_ONLY`** — copiar a disciplina de licença e de verificação; não adotar a engine
sem caso de uso concreto.

**Gates** (se houver adoção):

1. mitigar CC-BY-SA em conteúdo;
2. nenhuma dependência de runtime no produto antes de prova de valor;
3. build reprodutível em Windows/AMD antes de prometer.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Propor `LICENSES/` (REUSE) para as Skills Lia e para o Lia-Research | Agent Hub / Research | spec |
| 2 | Identificar caso de uso real de vídeo programático no Forge | Forge | decisão de explorar ou arquivar tema |
| 3 | Revisar em 90 dias | Research | — |
