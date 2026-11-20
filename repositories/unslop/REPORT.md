# unslop — skill de agente para "des-IA-izar" texto

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-004` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | agents |
| Projetos beneficiados | (nenhum — bloqueado por licença) |
| Fontes | `theclaymethod/unslop@0f4a07f5ca8bb400b4d4450b00d67c6e4a30b85a:README.md`, tree, `api.github.com` (metadados de licença) |
| Versão/commit | `0f4a07f` (2026-11-14) — sem releases |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `theclaymethod/unslop` · HEAD `0f4a07f5ca8b` · sem mudança no HEAD |
| Próxima revisão | 2027-05-17 (baixa prioridade) |
| Recomendação | **REJECT** (por ausência de licença) |
| Licença | **Nenhuma** — todos os direitos reservados (`CONFIRMED`) |
| Confiança | Alta (licença e estrutura verificadas diretamente) |

---

## 1. Identificação

- **Nome:** unslop
- **URL:** https://github.com/theclaymethod/unslop
- **Autor:** `theclaymethod`
- **Licença:** **ausente**. `GET /repos/.../unslop` → `license: null`;
  `GET /contents/LICENSE` → **404**. Logo: todos os direitos reservados (`CONFIRMED`)
- **Commit:** `0f4a07f` (2026-11-14T18:34:06Z)
- **Métricas:** ★1.132 · 63 forks · 10 issues · criado 2026-02-08 · 439 arquivos · 167 `.md` · 152 `.txt` · 71 `.py` · **355 arquivos em `evals/`** · 25 em `references/` · 21 scripts · 4 presets · **2 docs**

## 2. Resumo executivo

unslop encontra escrita formuláica ("tells" de IA) e faz edições pontuais preservando
significado e voz. Quatro comandos: `teach` (constrói uma voz a partir das suas
amostras), `cleanup` (aponta tells como sugestões, não altera), `rewrite` (diagnostica
e reconstrói sob guardas), `mimic` (escreve na voz ensinada). Tem scanners Python
standalone e uma infraestrutura de avaliação notavelmente grande (355 arquivos em
`evals/`).

O problema é único e definitivo: **não há arquivo de licença**. Repositório público
sem licença significa todos os direitos reservados — o autor não concedeu permissão
de uso, cópia, modificação ou redistribuição. Qualquer adoção exigiria autorização
explícita do autor.

Isso é uma oportunidade de decisão, não uma falha do projeto: basta o autor adicionar
uma licença. Até lá, `RESEARCH_ONLY` estrito, sem cópia.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Texto gerado por IA soa genérico | detecção de padrões ("tells") com sugestões |
| Reescrever sem perder a voz | `teach` constrói perfil de voz a partir de amostras |
| Reescrever sem perder significado | "rewrite gates" de preservação |
| Falta de avaliação objetiva | 355 arquivos de avaliação |

Honestidade documental notável: o README diz que "nem um scan limpo nem uma frase
familiar provam quem escreveu o texto, e os checks não garantem que todo defeito
sumiu". Isso é o tipo de ressalva que o `EVIDENCE-STANDARDS.md` exige.

## 4. Arquitetura

```text
SKILL.md (implícito pelo formato)  comandos /unslop teach|cleanup|rewrite|mimic
scripts/ (21 .py)                  scanners standalone
references/ (25)                   referências de padrões
presets/ (4)                       configurações
evals/ (355)                       infraestrutura de avaliação
plans/ (18)                        planos de trabalho
AGENTS.md, CLAUDE.md, CONTRIBUTING.md
```

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| 4 comandos (teach/cleanup/rewrite/mimic) | estável | `CONFIRMED` README |
| Scanners Python standalone | estável | `CONFIRMED` (`scripts/`) |
| Avaliações | existe (355 arquivos) | `CONFIRMED` |
| Presets | existe (4) | `CONFIRMED` |
| Licença | **ausente** | `CONFIRMED` |

## 6. Dependências

- Python para scanners; agente que leia `SKILL.md`/`AGENTS.md`.
- Nenhuma dependência de serviço.

## 7. Requisitos de hardware e sistema

- Trivial (texto + Python).

## 8. Segurança e privacidade

- Scanners processam texto do usuário; se o agente for remoto, o texto vai ao
  provider — consideração normal de qualquer skill, não específica deste projeto.
- Sem rede própria identificada.

## 9. Licença e proveniência

- **Sem licença.** `CONFIRMED` por dois caminhos independentes (metadados `null` e 404
  no arquivo). Consequência: **nenhuma permissão concedida**.
- Classe: `BLOCKED`. Nem `RESEARCH_ONLY` com cópia; apenas leitura para aprendizado.
- Aprendizado legítimo (não protegido): a *ideia* de "rewrite gates" e de separar
  detecção de reescrita é um padrão, e padrões podem ser reimplementados
  independentemente (`INDEPENDENT_REIMPLEMENTATION`).

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~9 meses | razoável |
| Releases | nenhuma | distribuição por commit |
| Issues | 10 | baixo |
| Evals | 355 arquivos | investimento alto |
| Licença | ausente | **bloqueio** |
| Docs | 2 | mínimo |

## 11. Custos e limitações

- Gratuito **apenas para leitura**. Uso exige autorização.
- Limitação adicional: documentação mínima (2 arquivos), então mesmo com licença
  haveria custo de entendimento.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Licença para uso | **não** | bloqueio absoluto |
| Formato skill | provavelmente sim | compatível por natureza |
| Windows | sim | Python |
| Utilidade para a Lia | possível (qualidade de texto de produto/docs) | secundária |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| (nenhum até haver licença) | — |

Potencial futuro: revisão de texto de UI e documentação (todos os projetos).

## 14. Oportunidades de reutilização

1. **"Rewrite gates"** — separar *detecção* de *ação* e verificar preservação: padrão
   aplicável a qualquer skill que edite conteúdo.
2. **Ressalva epistêmica explícita** ("clean scan não prova autoria"): modelo de como
   documentar limite de um detector.

Ambas são ideias; nenhuma linha de código pode ser copiada.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Uso sem licença = violação de copyright | **alta** | não copiar, não integrar |
| Autor pode licenciar depois | — | reavaliar se publicar licença |
| Documentação mínima | baixa | — |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | Sem licença | CONFIRMED | `GET /repos/theclaymethod/unslop` → `license: null`; `GET /contents/LICENSE` → 404 | 2026-11-17 |
| E2 | 4 comandos | CONFIRMED | `README.md` | 2026-11-17 |
| E3 | 355 arquivos de avaliação | CONFIRMED | tree | 2026-11-17 |
| E4 | Qualidade dos scanners | UNVERIFIED | não executado (e não executável sem licença) | — |

## 17. Recomendação

**`REJECT`** — enquanto não houver licença, nenhum uso é possível.

**Condição de reabertura:** o autor adicionar uma licença (MIT/Apache-2.0 serviriam).
Então reabrir como `ADAPT` após leitura da licença.

**Não autoriza:** copiar texto do skill, executar scripts, ou reimplementar a partir
do texto do repositório (só a partir do conceito).

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Registrar decisão `REJECTED` com condição de reabertura | Research | `DR` registrado |
| 2 | Se útil, pedir licença ao autor (opcional, cortesia) | proprietário | licença publicada |
| 3 | Extrair apenas o conceito de "rewrite gates" como padrão Lia | Agent Hub | nota de padrão |
| 4 | Revisar em 6 meses | Research | — |
