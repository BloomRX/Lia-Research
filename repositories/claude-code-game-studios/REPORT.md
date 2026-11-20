# Claude Code Game Studios — 49 agentes e 75 skills de processo de gamedev

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-002` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | studio |
| Projetos beneficiados | Lia Studio, Lia Agent Hub |
| Fontes | `Donchitos/Claude-Code-Game-Studios@abc0de79d6ceb0b5d7aa693945849b3937afbe6a:README.md`, tree (`.claude/`, `studio-tests/`, `docs/`), `LICENSE`, releases |
| Versão/commit | `abc0de7` (2026-11-09), release `v1.3.0` |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `Donchitos/Claude-Code-Game-Studios` · HEAD `abc0de79d6ce` · sem mudança no HEAD |
| Próxima revisão | 2027-02-17 |
| Recomendação | **ADAPT** (padrões de processo e hierarquia) |
| Licença | MIT (`CONFIRMED`, © 2026 Donchitos) |
| Confiança | Alta para estrutura/licença; Média para eficácia do processo |

---

## 1. Identificação

- **Nome:** Claude Code Game Studios
- **URL:** https://github.com/Donchitos/Claude-Code-Game-Studios
- **Autor:** `Donchitos`
- **Licença:** MIT, `Copyright (c) 2026 Donchitos` — `CONFIRMED`; cópia do texto já
  preservada pelo Lia-Studio em `docs/licenses/CLAUDE-CODE-GAME-STUDIOS-MIT.txt`
- **Commit:** `abc0de7` (2026-11-09T12:39:37Z) · releases `v1.3.0`, `v1.2.0`
- **Métricas:** ★**39.886** · 5.212 forks · 95 issues · criado 2026-02-12 · 794 arquivos · **582 em `.claude/`** · 674 `.md` · 68 `.sh` · 130 em `studio-tests/` · 60 em `docs/` · **0 workflows de CI**

## 2. Resumo executivo

Este é o upstream mais influente do ecossistema Lia na área de gamedev: o Agent Hub
já auditou 7 Skills adaptadas dele para o Lia Studio, e o Studio mantém o texto MIT em
`docs/licenses/`. O que o repositório oferece é, essencialmente, **um organograma de
estúdio transformado em agentes e processo**: 49 agentes, 75 skills de workflow,
pipelines de equipe, escada de documentos de design, e — na v1.3.0 — "web como engine"
e "studio mode".

O valor para a Lia Studio não é a implementação: é o **modelo de coordenação**
(hierarquia, handoff entre especialistas, documentos de design em degraus) e o
**modelo de distribuição de conhecimento para agentes** (582 arquivos em `.claude/`).

Ressalva importante: apesar de 39,9k estrelas, o repositório **não tem CI** e seus
testes vivem em `studio-tests/` como scripts. Popularidade alta não é validação do
método — é adoção.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Agente único não cobre todas as disciplinas | 49 agentes especializados com hierarquia |
| Falta de processo entre ideação e entrega | 75 skills de workflow + pipelines por "equipe" |
| Documento de design incompleto | "design-document ladder" em degraus |
| Onboarding de agente em projeto grande | `CLAUDE.md` + `.claude/` estruturado |
| Do brief ao jogo jogável | `/prototype` → brief de uma página → jogo web → verificação |

## 4. Arquitetura

```text
.claude/ (582)      agentes, skills, comandos, regras — o "cérebro"
studio-tests/ (130) testes do próprio framework de agentes
docs/ (60)          documentação de processo
design/ (2)         templates de documento de design
production/ (2)     templates de produção
src/ (2)            projeto de exemplo
CHANGELOG.md, CLAUDE.md, UPGRADING.md
```

Não há código de produto: o artefato é **conhecimento estruturado** + automação de
processo. Isso o torna diretamente comparável ao que o Lia Agent Hub precisa ser.

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| 49 agentes especializados | estável | `REPORTED` (descrição) + `.claude/` (582 arquivos) |
| 75 skills de workflow | estável | `REPORTED` |
| `/prototype` gera jogo web a partir de brief | v1.3.0 | `CONFIRMED` (release notes no commit) |
| Pipelines de equipe / "studio mode" | v1.3.0 | `CONFIRMED` |
| Escada de documentos de design | estável | `REPORTED` |
| Guia de upgrade entre versões | existe | `UPGRADING.md` |
| CI | **ausente** | `CONFIRMED` (0 workflows) |

## 6. Dependências

- Claude Code (ou agente compatível que leia `.claude/` e markdown de regras).
- Shell (68 `.sh`) para automação de pipeline.
- Nenhuma dependência de runtime de jogo.

## 7. Requisitos de hardware e sistema

- Irrelevante para o conhecimento; o "jogo web" gerado roda em navegador.
- Requer um agente com janela de contexto grande: 582 arquivos de instrução competem
  por contexto (`INFERRED` — este é um limite prático real).

## 8. Segurança e privacidade

| Item | Rótulo | Nota |
|---|---|---|
| Scripts shell executáveis no repo | `CONFIRMED` (68) | revisar antes de executar |
| Agentes com permissão de escrita em projeto | `INFERRED` | risco de alteração ampla |
| Sem CI → sem validação automática de contribuição | `CONFIRMED` | supply chain de conteúdo menos controlada |
| Telemetria | não identificada | — |

## 9. Licença e proveniência

- **MIT** (`CONFIRMED`). Obrigações: aviso + texto da licença.
- **Problema já identificado no ecossistema:** o Studio adaptou 7 Skills com seção
  `## Origem` apontando o commit upstream, mas **o aviso MIT vive na raiz do
  repositório, fora do payload da Skill**. Se a Skill for exportada sozinha, a
  obrigação não é cumprida.
- Existe cópia do texto em `Lia-Studio:docs/licenses/` — parcialmente adequado.
- Classe: `ADAPT_ALLOWED` com correção de empacotamento.
- Marca: "Claude" é marca da Anthropic; "Claude Code Game Studios" não é licenciada
  para uso como nome de produto derivado.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~9 meses | maduro em adoção |
| Estrelas | 39.886 | o mais popular da lista |
| Releases | v1.2.0 (2026-10-19), v1.3.0 (2026-11-09) | cadência mensal |
| CI | **0** | lacuna |
| Testes | 130 arquivos em `studio-tests/` | existem, sem automação visível |
| Guias | CHANGELOG + UPGRADING | acima da média |

## 11. Custos e limitações

- Gratuito (MIT). Custo real: **contexto** — carregar 582 arquivos é caro.
- Limitação: processo opinativo e acoplado a Claude Code; portar para outro agente
  exige reescrita do carregamento.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Formato skills Markdown | sim | compatível com catálogo Lia |
| Lia Studio (Godot/TS) | parcial | processo é agnóstico, exemplos não |
| Windows | sim | shell scripts exigem Git Bash/WSL |
| Sem dependência de runtime | sim | é conteúdo |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Studio | modelo de hierarquia de agentes e escada de documentos de design |
| Lia Agent Hub | modelo de distribuição de conhecimento para agentes (`.claude/`) |

## 14. Oportunidades de reutilização

1. **Escada de documentos de design** (brief → spec → plano → verificação): resolve o
   "agente não sabe em que fase está".
2. **Hierarquia explícita de especialistas** com handoff: modelo para o Orchestrator
   do Hub.
3. **`UPGRADING.md`** para conteúdo versionado — raro e útil.
4. **Brief de uma página** como entrada canônica de protótipo.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Aviso MIT fora do payload da Skill (violação em export) | **alta** (legal) | empacotar NOTICE dentro da Skill |
| Custo de contexto (582 arquivos) | média | carregar sob demanda (skillsets) |
| Sem CI, scripts shell | média | revisar antes de executar |
| Processo opinativo vira dogma | média | adaptar, não copiar |
| Marca "Claude" | baixa | não usar em nome de produto |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | MIT © 2026 Donchitos | CONFIRMED | `@abc0de7:LICENSE` | 2026-11-17 |
| E2 | 49 agentes / 75 skills | REPORTED | descrição do repo | 2026-11-17 |
| E3 | 582 arquivos em `.claude/`, 674 `.md` | CONFIRMED | tree | 2026-11-17 |
| E4 | 0 workflows de CI | CONFIRMED | tree `.github/` | 2026-11-17 |
| E5 | v1.3.0 com `/prototype` e studio mode | CONFIRMED | release notes no commit | 2026-11-17 |
| E6 | 7 skills já adaptadas pelo Lia Studio com seção `## Origem` | CONFIRMED | auditoria do Agent Hub `SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` (A-1) | 2026-11-15 |
| E7 | Eficácia do método | UNVERIFIED | não avaliada empiricamente | — |

## 17. Recomendação

**`ADAPT`** — adotar padrões de processo e de organização de conhecimento;
corrigir o empacotamento de aviso das 7 Skills já adaptadas.

**Gates:**

1. `NOTICE`/texto MIT dentro do pacote exportado de cada Skill derivada;
2. carregamento sob demanda (não os 582 arquivos de uma vez);
3. revisão de scripts antes de qualquer execução;
4. nenhuma nova Skill derivada sem registro de commit upstream.

**Não autoriza:** copiar o repositório inteiro, executar seus scripts, ou renomear
produto usando a marca do upstream.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Corrigir empacotamento de aviso das 7 Skills (bloqueio legal) | Agent Hub / Studio | pacote com NOTICE interno |
| 2 | Avaliar a "escada de documentos" para o fluxo da Studio | Studio | proposta |
| 3 | Medir custo de contexto do carregamento atual | Studio | número |
| 4 | Revisar em 90 dias | Research | — |
