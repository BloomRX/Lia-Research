# pixelfx — 244 efeitos de pixel art como código

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-004` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | forge |
| Projetos beneficiados | Lia Forge (assets/VFX), Lia Studio (jogos 2D) |
| Fontes | `patch-gg/pixelfx@5294518ce7c72e48b6100a744596e0acf57f2826:README.md`, `NOTICE.md`, tree, `LICENSE` |
| Versão/commit | `5294518` (2026-11-12) — sem releases/tags |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `patch-gg/pixelfx` · HEAD `5294518ce7c7` · sem mudança no HEAD |
| Próxima revisão | 2027-02-17 |
| Recomendação | **ADAPT** (uso de catálogo/efeitos com atribuição correta) |
| Licença | MIT **com atribuições específicas** em `NOTICE.md` |
| Confiança | Alta para licença; Média para qualidade dos efeitos |

---

## 1. Identificação

- **Nome:** pixelfx
- **URL:** https://github.com/patch-gg/pixelfx · galeria patch-gg.github.io/pixelfx
- **Autor:** `patch-gg` (Patch)
- **Licença:** MIT + `NOTICE.md` com atribuições obrigatórias — `CONFIRMED`
- **Commit:** `5294518` (2026-11-12T08:42:34Z); **sem releases**
- **Métricas:** ★7.932 · 1.038 forks · 14 issues · criado 2026-10-30 · 313 arquivos · 282 `.js` · 4 `.md` · 13 `.mjs` em `tools/` · **0 testes** · 1 workflow · `.claude-plugin/` presente

## 2. Resumo executivo

pixelfx entrega **244 efeitos e animações de pixel art, cada um um pequeno trecho de
código** (canvas/JS), com galeria navegável, recolor e mirror, uso em jogo de browser
e export para sprite sheet. Inclui uma **skill de Claude Code** que cria novos efeitos
no estilo de um pixel artist exigente (draft → render → look → refine). Doze
"movimentos" encadeiam efeitos em ataques com wind-up, impacto e recovery.

Para o Lia Forge é um catálogo de assets com licença permissiva e uma dependência
zero (é código, não binário). Para a Studio, é referência de animação 2D expressiva com
poucos recursos.

O ponto de atenção é de proveniência: o `NOTICE.md` declara que parte dos efeitos
**adapta** o VFX open-source do Sprite Fusion (MIT, © Hugo Duprez) e o comportamento
de skills do Hollow Crown (MIT, © rehan-remade), e que **a fonte da galeria não é
coberta pela MIT**. Ou seja: MIT no topo, obrigações específicas dentro.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Falta de VFX 2D para jogo indie | 244 efeitos prontos, parametrizáveis |
| Integração com engine | export sprite sheet + uso direto em canvas |
| Criar efeito novo com qualidade | skill de agente com fluxo draft/render/look/refine |
| Recolorir/espelhar sem refazer | parâmetros no player |

## 4. Arquitetura

```text
src/ (281 .js)      efeitos individuais + core (sim.js, act.js)
gallery/ (5)        player/gallery (fonte própria, licença separada)
tools/ (13 .mjs)    export sprite sheet, validação
docs/ (4)           CATALOG.md e afins
.claude-plugin/     empacotamento como plugin/skill
NOTICE.md           atribuições de terceiros
```

Cada efeito é um módulo pequeno e independente — desenho que facilita cópia seletiva
(e, portanto, exige disciplina de atribuição).

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| 244 efeitos | estável | `CONFIRMED` (contador no README + `docs/CATALOG.md`) |
| 12 movimentos encadeados ("acting") | estável | `CONFIRMED` |
| Export sprite sheet | estável | `CONFIRMED` (`tools/`) |
| Recolor / mirror | estável | `REPORTED` |
| Skill de Claude Code para criar efeitos | existe | `CONFIRMED` (`.claude-plugin/`) |
| Testes automatizados | **ausentes** | `CONFIRMED` (0 arquivos de teste) |

## 6. Dependências

- JavaScript puro (navegador/canvas); sem framework obrigatório.
- Node apenas para `tools/` (export).
- Nenhuma dependência de runtime pesada.

## 7. Requisitos de hardware e sistema

- Trivial: canvas 2D em navegador. Compatível com qualquer máquina.
- Export de sprite sheet: CPU, sem GPU.

## 8. Segurança e privacidade

- Código local, sem rede, sem telemetria identificada (`OBSERVED`: nenhuma dependência
  de rede nos módulos).
- Risco baixo. O único vetor é executar JS de terceiro no produto sem revisão —
  desnecessário, já que os efeitos são pequenos e auditáveis.

## 9. Licença e proveniência

| Camada | Licença | Obrigação |
|---|---|---|
| Código dos efeitos | MIT | aviso + texto |
| Efeitos que adaptam Sprite Fusion | MIT, © 2026 Hugo Duprez | atribuir, citar origem |
| `src/core/act.js` (adapta Hollow Crown) | MIT, © 2026 rehan-remade | atribuir |
| Fonte em `gallery/fonts` | **não coberta pela MIT** | ver `gallery/fonts/NOTICE.md`; **não usar a fonte** sem ler |

Classe: `ADAPT_ALLOWED`, **condicionada** a manter o `NOTICE.md` junto dos efeitos
derivados. Este é o exemplo canônico do erro que o ecossistema Lia comete com Skills:
aviso na raiz, payload sem aviso.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~2,5 semanas | muito jovem |
| Releases | nenhuma | sem versionamento |
| Issues | 14 | baixo |
| Testes | 0 | lacuna |
| CI | 1 workflow | mínimo |
| Escopo | 244 efeitos | grande para a idade; muitos podem ser simples variantes |

## 11. Custos e limitações

- Gratuito. Integração barata (JS puro).
- Limitações: sem testes; sem versão; qualidade heterogênea provável; fonte própria
  fora da licença.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 | sim | JS/canvas |
| Forge (asset pipeline) | sim como catálogo de referência | export sheet |
| Studio (Godot 2D) | sim | sprite sheets |
| Sem GPL | sim | MIT |
| Testes/estabilidade | não | sem testes |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Forge | catálogo de VFX 2D, export de sprite sheets |
| Lia Studio | referência de animação 2D e de encadeamento de efeitos |

## 14. Oportunidades de reutilização

1. **Efeito como módulo pequeno e auditável** em vez de pacote grande.
2. **Skill de agente que produz assets com revisão visual** (draft → render → look →
   refine): padrão diretamente aplicável à Studio.
3. **`NOTICE.md` por camada**: modelo correto de atribuição em repositório com
   contribuições derivadas.

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| Usar efeitos sem levar o `NOTICE.md` | **alta** (legal) | empacotar NOTICE junto |
| Usar a fonte da galeria | média | fora da MIT; não usar |
| Sem testes/versão | média | copiar efeito individual, não o pacote |
| Qualidade heterogênea | baixa | curadoria |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | MIT no repositório | CONFIRMED | `@5294518:LICENSE` | 2026-11-17 |
| E2 | Atribuições a Sprite Fusion e Hollow Crown (MIT) | CONFIRMED | `NOTICE.md` | 2026-11-17 |
| E3 | Fonte da galeria fora da MIT | CONFIRMED | `NOTICE.md` → `gallery/fonts/NOTICE.md` | 2026-11-17 |
| E4 | 244 efeitos | CONFIRMED | contador marcado no README + `docs/CATALOG.md` | 2026-11-17 |
| E5 | 0 testes | CONFIRMED | tree (nenhum diretório/arquivo de teste) | 2026-11-17 |
| E6 | Qualidade individual dos efeitos | UNVERIFIED | não avaliada visualmente | — |

## 17. Recomendação

**`ADAPT`** — usar como catálogo de referência/asset com atribuição completa;
não integrar o pacote inteiro como dependência.

**Gates:**

1. `NOTICE.md` viaja junto de qualquer efeito copiado;
2. fonte da galeria não é usada;
3. curadoria por efeito (sem testes, a qualidade não é garantida);
4. nenhum efeito entra no app sem revisão visual.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Selecionar 10 efeitos candidatos e revisar visualmente | Forge | lista curada |
| 2 | Definir política de NOTICE dentro de pacote de asset | Forge/Agent Hub | spec |
| 3 | Avaliar a skill de criação de efeito como padrão para a Studio | Studio | proposta |
