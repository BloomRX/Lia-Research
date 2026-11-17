# ADR de interface — procedimento mínimo

| Campo | Valor |
|---|---|
| ID | `LR-UI-005` |
| Categoria | interfaces |
| Projetos beneficiados | Lia-Project (Stage), Lia Studio, Lia Forge, Lia Agent Hub |
| Fontes | `Lia-AgentHub:docs/DECISION-REGISTER.md` (vocabulário de estado), `docs/stitch/handoff/README.md` (estrutura de handoff, inclui `DESIGN-DECISIONS.md`), `docs/design/UI-UX-AUDIT.md`; `Lia-Project:docs/reports/LIA-UI-UX-AUDIT-2026-11-14.md`, `LIA-UIUX-RECONCILIATION.md`; `Lia-Studio:docs/UI-UX-DESIGN-SYSTEM-LIA-STUDIO.md`, `ARENA-UIUX-AUDIT.md`; `backnotprop/plannotator@b5b30778` (**63 ADRs**) → `LR-UI-002` |
| Data | 2026-11-17 |
| Status | **PROPOSTA** (procedimento; nada implementado) |
| Confiança | Alta para as fontes; média para a recomendação de processo |

---

## 1. Pergunta

Qual é o procedimento **mínimo** para registrar uma decisão de interface, de forma que ela
não vire burocracia nem duplique o que já está no design system — e que funcione nos
quatro projetos que têm UI?

## 2. O problema medido

| Sintoma | Evidência |
|---|---|
| Decisão de UI reconstruída depois | Project tem **três** documentos de reconciliação de UI/UX (`LIA-UIUX-RECONCILIATION.md` e correlatos) — reconciliação existe porque duas fontes divergiram |
| Auditoria sem decisão | `LIA-UI-UX-AUDIT-2026-11-14.md` (49 KB) aponta problemas; nenhum arquivo diz "decidimos X, em tal data, por tal motivo" |
| Handoff sem decisão preenchida | o Hub **define** `DESIGN-DECISIONS.md` no handoff, mas o conteúdo ainda é derivado de auditoria |
| Ritmo alto é possível | plannotator tem **63 ADRs** em 11 meses — prova de que registrar é viável |

O slot já existe em dois lugares (Hub: `DESIGN-DECISIONS.md` + `DECISION-REGISTER.md`).
O que falta é o **gatilho** e o **formato mínimo** — não um sistema novo.

## 3. Princípio

> Um ADR de UI responde **por que está assim**, e só isso. O que é (tokens, componentes)
> fica no design system; o como (tela, código) fica na implementação. ADR que repete
> o design system é duplicata, não registro.

## 4. Gatilhos — quando escrever

| Gatilho | Exemplo real |
|---|---|
| Escolha entre 2+ alternativas visíveis ao usuário | "painel lateral vs. modal para configuração de provider" |
| Contrato de comportamento (foco, teclado, estados) | "popup devolve foco ao gatilho ao fechar" |
| Mudança que quebra hábito do usuário | "atalho de voz muda de `Ctrl+Space` para `Ctrl+Shift+Space`" |
| Divergência entre auditoria e implementação | reconciliar UI/UX do Project |
| Aceitação consciente de limitação | "não suportamos arrastar entre janelas no Windows" |
| Dependência de UI externa | adotar Vercel UI SDK em protótipo (`LR-UI-001`) |

## 5. Não-gatilhos — quando **não** escrever

| Não escrever para | Por quê |
|---|---|
| ajuste de espaçamento/cor dentro dos tokens | é design system, não decisão |
| correção de bug de layout | é mudança, não escolha |
| preferência de implementação invisível | não é decisão de interface |
| decisão já registrada em outro documento | duplicata; linkar |
| "vamos usar o design system" | é o padrão, não uma decisão |

Regra prática: **se ninguém consegue discordar da frase, não é decisão.**

## 6. Formato mínimo (uma página, 8 campos)

```markdown
# ADR-UI-007 — Popup devolve foco ao gatilho

| Campo | Valor |
|---|---|
| Estado | proposta · aceita · substituída · rejeitada |
| Data | 2026-11-17 |
| Projeto | Lia-Project (Stage) |
| Decisor | nome ou papel |
| Superfície | componente/tela afetada |

## Contexto
O que obrigou a decidir (2–5 linhas). Link para a auditoria/issue.

## Decisão
Uma frase imperativa. Sem "talvez".

## Alternativas consideradas
| Alternativa | Por que não |
|---|---|

## Consequências
O que fica mais fácil, o que fica mais difícil, o que passa a ser proibido.

## Como verificar
O teste, a métrica ou a inspeção que prova que a decisão está de pé.

## Revisitar se
Condição concreta que reabre a decisão (ex.: "se o SDK mudar de versão maior").
```

Campos que **não** entram: mockup (link), token (design system), código (PR).

## 7. Onde mora (um dono por decisão)

| Projeto | Caminho | Papel |
|---|---|---|
| Lia-Project | `docs/adr/ui/NNNN-*.md` | decisões do Stage |
| Lia Studio | `docs/adr/ui/NNNN-*.md` | decisões do editor |
| Lia Forge | `docs/adr/ui/NNNN-*.md` | decisões de ferramenta |
| Lia Agent Hub | `docs/design/DESIGN-DECISIONS.md` (já definido no handoff) | decisões do handoff Stitch |
| Lia-Research | `cross-project/interfaces/` | **só lições transversais**, nunca cópia da decisão |

Regra anti-duplicação: a decisão vive no projeto que a executa. O Hub registra a
decisão **de design**; o projeto registra a **de implementação**; se forem a mesma,
uma referencia a outra e não repete o texto.

## 8. Como o Stitch entra

O Stitch produz tela, não decisão. A ligação é por referência:

```text
stitch/screens/<tela>.md      → id do projeto Stitch + versão
stitch/prompts/<tela>.md      → prompt versionado
DESIGN-DECISIONS.md / ADR-UI  → POR QUE a tela é assim
approved/<tela>.md            → QUAL versão foi implementada
```

Nenhum ADR copia o HTML exportado. Se a decisão só existe no prompt, ela não existe:
prompt é entrada, não registro.

## 9. Ciclo de vida

| Estado | Significa | Quem muda |
|---|---|---|
| `proposta` | escrita, sem efeito | qualquer agente |
| `aceita` | vale para implementação | decisor humano (regra do Hub §DECISION-REGISTER: "Arena pode recomendar; aceite é humano") |
| `substituída` | nova decisão referenciou esta | autor da nova |
| `rejeitada` | registrada para não voltar | decisor |

ADR **nunca é apagado**. Rejeitada é mais útil que inexistente: impede a mesma discussão
duas vezes.

## 10. Custo esperado (para não virar teatro)

| Métrica | Meta saudável | Sinal de burocracia |
|---|---|---|
| ADRs de UI por trimestre | **3 a 8** por projeto | > 20 |
| Tempo para escrever um | 10–20 min | > 1 h |
| ADRs que alguém relê | > 30% em 6 meses | 0% |
| ADRs substituídos | alguns | nenhum (decisão boa não é eterna) |

Se um ADR leva uma hora, o problema não é o processo: é a decisão ainda não estar tomada.

## 11. Piloto sugerido (3 decisões reais)

| # | Decisão | Projeto | Por que serve de piloto |
|---|---|---|---|
| 1 | Nome e posicionamento do Hub (`D-01` do registro) | Agent Hub | já tem alternativas e recomendação registradas |
| 2 | Contrato de foco em popup/overlay | Project (Stage) | comportamento verificável, toca acessibilidade |
| 3 | Tokens do design system: fonte única | Studio | evita divergência entre editor e produto |

Nenhum destes foi escrito por esta base: a decisão é do projeto.

## 12. Limitações e pendências

| Item | Rótulo |
|---|---|
| Nenhum ADR de UI existe hoje em nenhum dos cinco projetos | `UNVERIFIED` (não encontrado na varredura; pode haver em branch podada) |
| Não avaliado se o formato cabe em documento de 1 página no Notion/Drive | `NOT RUN` |
| Impacto de 63 ADRs do plannotator em navegação não medido | `NOT RUN` |
| Acessibilidade: procedimento não cobre WCAG; é tema próprio (`R-5`) | declarado |

## 13. Encaminhamento

| Ação | Dono | Gate |
|---|---|---|
| Adotar formato de 8 campos no Hub (substitui nada, preenche o slot) | Agent Hub | decisão do produto |
| Escrever os 3 ADRs piloto | cada projeto | `DR-0023` (proposto) |
| Reconciliar UI/UX do Project registrando as decisões (não só os problemas) | Project | após aceite |
