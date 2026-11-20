# Claude Trading Skills — padrões de organização de Skills e workflows

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-002` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | agents |
| Projetos beneficiados | Lia Agent Hub |
| Fontes | `tradermonty/claude-trading-skills@a627d17dd1d8fde1c8fa73b3cc69ffe83b33cb71:README.md`, tree (`skills/`, `workflows/`, `skillsets/`), `LICENSE` |
| Versão/commit | `a627d17` (2026-11-17) — sem releases/tags |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `tradermonty/claude-trading-skills` · HEAD `f95e770591b5` · mudou desde a análise (conteúdo novo não lido) |
| Próxima revisão | 2027-02-17 |
| Recomendação | **ADAPT** (apenas padrões de organização) |
| Licença | MIT (`CONFIRMED`, © 2026 TraderMonty) |
| Confiança | Alta para estrutura e licença; Média para qualidade interna das Skills |

---

## 1. Identificação

- **Nome:** Claude Trading Skills
- **URL:** https://github.com/tradermonty/claude-trading-skills · docs tradermonty.github.io/claude-trading-skills
- **Autor:** `tradermonty`
- **Licença:** MIT, `Copyright (c) 2026 TraderMonty` — `CONFIRMED`
- **Commit:** `a627d17` (2026-11-17T14:34:04Z); **sem releases** (versionamento por commit)
- **Métricas:** ★6.772 · 1.394 forks · 51 issues · criado 2025-10-19 · 2.531 arquivos · **74 diretórios de Skill** · 740 `.md` · 1.082 `.py` · 629 arquivos de teste · 10 workflows de CI · docs em inglês e japonês

## 2. Resumo executivo

Este repositório não interessa à Lia pelo domínio (trading), e sim pela **engenharia de
organização de Skills**: 74 Skills pequenas e compostas, organizadas em três camadas
explícitas — `skills/` (unidade), `skillsets/` (subconjunto por perfil), `workflows/`
(manifesto YAML que nomeia skills, *decision gates* e artefatos, em ordem).

O padrão de manifesto de workflow é o achado mais valioso: em vez de um prompt longo
que descreve o processo, existe um YAML legível por máquina que diz *quais* Skills,
em *que ordem*, com *que portões de decisão* e *que artefatos de saída*. Isso resolve
um problema real do ecossistema Lia: as 47 Skills atuais não têm contrato de composição.

Ressalva importante: o domínio é financeiro e o próprio README declara que **não é
conselho financeiro** e que não automatiza execução. A ordem de serviço é explícita —
não adicionar funcionalidade financeira por associação com este repositório.

## 3. O que resolve

| Problema | Solução |
|---|---|
| Skill isolada não compõe processo | `workflows/*.yaml` com ordem, gates e artefatos |
| Usuário não sabe por onde começar | "Recommended Starting Path" com workflow por objetivo |
| Muitas skills, contexto estourado | `skillsets/*.yaml` — subconjunto por perfil |
| Processo informal vira prompt gigante | manifesto versionado e auditável |
| Falta de rastreabilidade de decisão | *decision gates* nomeados no manifesto |

## 4. Arquitetura

```text
skills/<nome>/SKILL.md       74 unidades autocontidas
skillsets/<perfil>.yaml      7 perfis (core-portfolio, dividend-income, ...)
workflows/<fluxo>.yaml       15 manifestos (daily/weekly/monthly)
docs/en, docs/ja             documentação bilíngue (260 arquivos)
scripts/ (230)               utilitários Python das skills
examples/ (540)              uso demonstrativo
config/                      perfis de API
.skill / skill-packages (74) distribuição empacotada
```

Estrutura de um manifesto (padrão observado): nome do fluxo, skills na ordem,
*decision gates* intermediários, artefatos esperados, e "API profile" (quais
credenciais/serviços o fluxo consome).

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| 74 Skills em formato `SKILL.md` | estável | `CONFIRMED` (tree) |
| 15 manifestos de workflow YAML | estável | `CONFIRMED` (`workflows/*.yaml`) |
| 7 skillsets por perfil | estável | `CONFIRMED` (`skillsets/*.yaml`) |
| Documentação en + ja | estável | `CONFIRMED` (740 `.md`) |
| Política de privacidade e SECURITY.md | existe | `CONFIRMED` (README aponta) |
| Empacotamento `.skill` / `skill-packages` | existe | `CONFIRMED` (74 arquivos `.skill`) |
| Testes | 629 arquivos | `CONFIRMED` (contagem) |
| Integração com corretora / execução de ordens | **não existe por desenho** | `REPORTED` (README: "not a broker execution platform") |

## 6. Dependências

- Python (1.082 arquivos) para os scripts das Skills.
- APIs de dados de mercado (config em `config/`), com perfis de API declarados.
- Nenhum runtime proprietário; Skills em Markdown + scripts.

## 7. Requisitos de hardware e sistema

- Trivial: Skills são texto + Python. Nada de GPU.
- Requer acesso a provedores de dados de mercado para os fluxos funcionarem
  (dependência de rede/credencial de terceiro).

## 8. Segurança e privacidade

| Item | Rótulo | Nota |
|---|---|---|
| Credenciais de API de dados | `OBSERVED` (`config/`) | padrão de perfil de API; não inspecionado para segredos |
| Política de privacidade própria | `CONFIRMED` | `docs/en/privacy.md` |
| SECURITY.md | `CONFIRMED` | canal de reporte |
| Skills executam rede | `OBSERVED` | egress para provedores de dados |
| Sem execução de ordens | `REPORTED` | reduz risco financeiro direto |

Lição para a Lia: um repositório de Skills deve declarar **que credenciais o fluxo
consome** (o "API profile" do manifesto). Hoje as Skills Lia não declaram isso.

## 9. Licença e proveniência

- **MIT** (`CONFIRMED`). Obrigações: aviso + texto. Sem copyleft.
- Conteúdo de dados de mercado **não** é coberto pela MIT — é de cada provedor.
- Classe: `ADAPT_ALLOWED` para o **padrão** de manifesto; `RESEARCH_ONLY` para as
  Skills em si (domínio irrelevante para a Lia).
- Marca: "Claude" é marca da Anthropic; o projeto a usa descritivamente.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~13 meses | maduro para um projeto pessoal |
| Commits | diários (PR #809 no dia da análise) | muito ativo |
| Releases | nenhuma | distribuição por commit; **sem tag = sem pin fácil** |
| Testes | 629 arquivos | sério |
| CI | 10 workflows | ativo |
| Documentação | 740 `.md`, bilíngue | acima da média |
| Mantenedor | único (com contribuições) | bus factor 1 |

## 11. Custos e limitações

- Gratuito (MIT), mas os fluxos dependem de APIs de dados pagas/gratuitas com limite.
- Limitação para a Lia: **não há release**, então "versão" só existe como commit.
- O domínio não é reaproveitável; a estrutura é.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Formato Agent Skills (`SKILL.md`) | sim | mesmo padrão das 48 Skills Lia |
| Vue/Electron/Windows | irrelevante | é conteúdo |
| Sem dependência de runtime | sim | catálogo, não biblioteca |
| Domínio financeiro na Lia | **não** | fora de escopo por decisão |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Agent Hub | padrão de manifesto de workflow, skillsets e "API profile" |
| Lia-Project / Forge / Studio | indiretamente, ao compor Skills próprias com contrato |

## 14. Oportunidades de reutilização

1. **Manifesto de workflow YAML** (skills em ordem + gates + artefatos + credenciais):
   o modelo que falta às 47 Skills Lia.
2. **Skillsets por perfil** em vez de "instale todas": reduz contexto e risco.
3. **Documentação bilíngue** como prática (o ecossistema Lia é PT-BR + EN).
4. **"API profile" declarado por fluxo**: torna explícito o egress de cada Skill.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Copiar Skill de trading para a Lia | alta (escopo) | proibido por decisão; só padrões |
| Assumir que 74 skills = 74 boas skills | média | amostragem de qualidade necessária antes de elogiar |
| Sem releases → pin difícil | baixa | fixar commit |
| Bus factor 1 | média | usar padrão, não o projeto |
| Credenciais em `config/` | média | não copiar diretório |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | MIT © 2026 TraderMonty | CONFIRMED | `@a627d17:LICENSE` | 2026-11-17 |
| E2 | 74 diretórios de Skill | CONFIRMED | tree `skills/` | 2026-11-17 |
| E3 | 15 manifestos de workflow YAML | CONFIRMED | `workflows/*.yaml` | 2026-11-17 |
| E4 | 7 skillsets | CONFIRMED | `skillsets/*.yaml` | 2026-11-17 |
| E5 | Não executa ordens / não é conselho | REPORTED | `README.md` disclaimer | 2026-11-17 |
| E6 | Qualidade individual das Skills | UNVERIFIED | não avaliada em amostra | — |
| E7 | 629 arquivos de teste | CONFIRMED | tree (contagem) | 2026-11-17 |

## 17. Recomendação

**`ADAPT`** — adotar o **formato de manifesto** para compor Skills Lia; não adotar
domínio, Skills ou credenciais.

**Gates:**

1. nenhuma Skill de trading entra no catálogo Lia;
2. o manifesto Lia deve ser próprio, inspirado no formato, não cópia;
3. incluir obrigatoriamente: credenciais consumidas, gates de decisão, artefatos;
4. validar com 3 Skills Lia reais antes de propor adoção no Hub.

**Não autoriza:** adicionar funcionalidade financeira, copiar Skills, ou reestruturar
o catálogo do Hub sem decisão.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Redigir `WORKFLOW-MANIFEST.md` proposto para Skills Lia | Agent Hub | spec com 3 exemplos |
| 2 | Amostrar 5 Skills do repositório para avaliar profundidade | Research | nota de qualidade |
| 3 | Testar manifesto em uma Skill Lia real (`lia-release-gate`) | Agent Hub | prova de conceito |
| 4 | Decidir se manifesto vira requisito de catálogo | proprietário | `DR` registrado |
