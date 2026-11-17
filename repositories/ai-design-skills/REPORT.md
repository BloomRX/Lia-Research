# AI Design Skills — coleção pequena de skills de design

| Campo | Valor |
|---|---|
| ID | `LR-UI-003` |
| Categoria | ui |
| Projetos beneficiados | Lia Studio, Lia-Project (design system/UX) |
| Fontes | `elayadesign/ai-design-skills@456d9e0d3e2d84c748bb143c6ca3d90c45e16213:README.md`, tree, `LICENSE` |
| Versão/commit | `456d9e0` (2026-11-01) — sem releases |
| Data | 2026-11-17 |
| Próxima revisão | 2027-02-17 |
| Status | CURRENT |
| Recomendação | **ADAPTAR** (por padrão, não por conteúdo) |
| Licença | MIT (`CONFIRMED`) |
| Confiança | Alta para licença/estrutura; Média para profundidade (só 2 skills) |

---

## 1. Identificação

- **Nome:** AI Design Skills
- **URL:** https://github.com/elayadesign/ai-design-skills
- **Autor:** `elayadesign`
- **Licença:** MIT (`CONFIRMED` — arquivo presente na raiz)
- **Commit:** `456d9e0` (2026-11-01T23:24:09Z)
- **Métricas:** ★**15.818** · 1.223 forks · 7 issues · criado 2026-07-29 · **apenas 9 arquivos** · 3 `.md` · 2 `.py` · 1 CI · 1 diretório de teste

## 2. Resumo executivo

Uma coleção deliberadamente mínima: **duas skills** (`landing-page-design`,
`figma-designer`), cada uma uma pasta autocontida com `SKILL.md`, mais um script e um
teste. O autor mantém um repositório separado para o skill de redesign, porque ele
precede a coleção.

O dado mais interessante é a proporção: **15,8 mil estrelas para 9 arquivos**. Isso
diz menos sobre profundidade e mais sobre demanda: existe fome por skills de design
pequenas, instaláveis e autocontidas (`npx skills add`). Para o Lia Studio, que tem
design system próprio em evolução, o padrão de "skill autocontida com intake
questions + sistema visual + critérios" é aproveitável.

Não é uma fonte de conhecimento de design profundo — é um formato que funciona.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Agente gera landing page genérica | skill com intake questions + estrutura + copy de conversão + sistema visual |
| Design no Figma sem estrutura | skill que exige variáveis de espaçamento/cor, estilos de texto nomeados, auto layout, componentes com estados |
| Instalação difícil de "regras" | pasta autocontida + `npx skills add` |

## 4. Arquitetura

```text
skills/landing-page-design/SKILL.md
skills/figma-designer/SKILL.md
scripts/ (1 .py)
tests/ (1)
assets/ (1 .png)
.github/ (1 workflow)
LICENSE, README.md, .gitignore
```

Zero infraestrutura. O artefato é o texto da skill.

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Skill de landing page | estável | `CONFIRMED` (README tabela + caminho) |
| Skill de Figma com estrutura real | estável | `CONFIRMED` |
| Instalação via `npx skills add` | estável | `CONFIRMED` |
| Testes | 1 arquivo | `CONFIRMED` |
| Muitas skills | **não** — apenas 2 | `CONFIRMED` |

## 6. Dependências

- Nenhuma além do agente que lê markdown e (opcionalmente) Python para o script.

## 7. Requisitos de hardware e sistema

- Trivial.

## 8. Segurança e privacidade

- Conteúdo estático. Sem execução de rede. Risco mínimo.
- Cautela padrão: instruções de agente podem conter comandos; revisar antes de rodar.

## 9. Licença e proveniência

- **MIT** (`CONFIRMED`). Aviso + texto.
- Classe: `ADAPT_ALLOWED`.
- Marca: "Figma" é marca da Figma Inc.; a skill ensina a usar a ferramenta, o que é
  uso descritivo, mas um produto Lia não deve implicar parceria.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~4 meses | novo |
| Estrelas | 15.818 | demanda alta, escopo pequeno |
| Commits | último é ajuste de README | atividade baixa |
| Issues | 7 | baixo |
| Releases | nenhuma | — |

Projeto de baixa manutenção e alto alcance: bom para copiar formato, ruim para
depender de evolução.

## 11. Custos e limitações

- Gratuito; integração trivial.
- Limitação: 2 skills, profundidade limitada. Não é referência de design system.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Formato Agent Skills | sim | mesmo padrão das 48 Lia |
| Windows | sim | conteúdo |
| Aplicável ao design system da Studio | parcialmente | padrão de intake + sistema visual |
| Não introduz dependência | sim | — |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Studio | padrão de skill de design com intake e sistema visual |
| Lia-Project | referência para UI/UX de Stage (hierarquia, espaçamento, estados) |

## 14. Oportunidades de reutilização

1. **Anatomia da skill de design**: intake questions → estrutura → copy → sistema
   visual → critérios de verificação. É um bom molde para uma futura skill
   `lia-ui-quality-review` evoluída.
2. **Autocontenção**: uma pasta, um `SKILL.md`, zero infraestrutura. O oposto do
   repositório de 582 arquivos.
3. **Exigir estrutura real na ferramenta** (variáveis, estilos nomeados, auto layout)
   em vez de "desenhe algo bonito".

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Confundir popularidade com profundidade | média | usar como molde, não como fonte |
| Projeto de baixa manutenção | baixa | não depender |
| Marca Figma | baixa | uso descritivo |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | MIT | CONFIRMED | `@456d9e0:LICENSE` | 2026-11-17 |
| E2 | 2 skills em 9 arquivos | CONFIRMED | tree + README | 2026-11-17 |
| E3 | 15.818 estrelas | CONFIRMED | API | 2026-11-17 |
| E4 | Qualidade das instruções | UNVERIFIED | não avaliadas em uso | — |

## 17. Recomendação

**`ADAPTAR`** — copiar a anatomia e a autocontenção na evolução das skills de UI Lia.

**Não autoriza:** substituir o design system da Studio, ou instalar as skills como
dependência de produto.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Comparar a anatomia com `lia-ui-quality-review` atual | Studio | lista de lacunas |
| 2 | Propor molde de skill de design para o catálogo Lia | Agent Hub | spec |
| 3 | Revisar em 90 dias | Research | — |
