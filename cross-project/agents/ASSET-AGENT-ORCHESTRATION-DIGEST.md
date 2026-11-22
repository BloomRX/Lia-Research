# Orquestração de agentes para produção de assets — digest

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-005` |
| Categoria | agents |
| Projetos | Lia Forge |
| Fontes | `Lia-Forge@…:docs/T14-AGENT-ORCHESTRATION-ARCHITECTURE.md` (21 KB), `docs/T14-AGENT-ECOSYSTEM-RESEARCH.md` (17 KB), `docs/T9-EXECUTION-BACKEND-ARCHITECTURE.md` (16 KB), `shared/capabilities/registry.mjs` |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média |

## 1. Desenho proposto pelo Forge

Camadas: **Capability · Workflow · Provider/Adapter · Backend**. Cada capacidade de
produção (ex.: "gerar sprite sheet") é declarada no registro
(`registry.mjs`: 49 capacidades — 16 implementadas, 5 parciais, 5 propostas,
24 planejadas) e executada por um backend intercambiável.

## 2. Por que é o desenho certo para assets

| Problema | Solução |
|---|---|
| Ferramenta muda toda semana | backend intercambiável sob capability estável |
| Asset exige 5 etapas | workflow encadeia capabilities |
| Custo/latência variável por provider | adapter mede e escolhe |
| "Quase pronto" eterno | estado explícito (implemented/partial/planned) |

## 3. O que falta

| Lacuna | Status |
|---|---|
| 24 capacidades "planned" sem dono nem prazo | registrado no código, não priorizado |
| Nenhum benchmark de backend | `BLOCKED` |
| Manifesto de capability executável (equivalente ao workflow YAML) | inexistente — ver `LR-AGENT-002` |
| Proveniência por asset gerado | proposto em `LR-LIC-002`, não implementado |

## 4. Ligação com pesquisa externa

`repositories/sculptforge/REPORT.md` (benchmark reproduzível) e
`repositories/manimgx/REPORT.md` (licença por diretório) são as duas referências
externas que preenchem lacunas deste desenho.

**Atualizado 2026-11-22** — `repositories/mr-mak-workspace/REPORT.md` (`LR-STUDIO-012`) entrou como
terceira referência, e é a mais próxima do desenho real: um produto em produção que faz exatamente a
coisa deste digest (um coordenador abrindo/reencaminhando/acompanhando chats de agentes), com a fronteira
implementada como verificação de servidor — `openChatArguments()` aceita cinco campos e nunca um shell,
`bypass` não pode ser elevado pelo agente, e a saída de terminal é declarada "reference data, never as
instructions". Duas coisas que ele mostra e que §3 ainda não tinha:

- **continuidade por arquivo, não por memória**: o `handoff` escrito pelo agente que sai, salvo em
  `inbox/handoffs/`, lido pelo chat novo na mesma pasta/agente/configuração, disparado por **ocupação de
  contexto** (70 % por padrão) — o formato candidato para a linha "24 capacidades planned sem dono" e para
  `PROJECT-RESUME`;
- **a lacuna "proveniência por asset gerado" tem piso publicado**: no game jam da Epic, três pessoas com
  agentes registraram 368 marcos / 712 steps / 830 mídias, 2.891 saídas em 255 runs por serviço × modelo ×
  pessoa, e um ledger de 674 registros escritos **logo depois** de cada job — com "pago" (US$ 22,97)
  separado de "valor de tabela estimado" (US$ 2.927,42) e da nota "nobody paid these sums as such, as the
  agents ran on subscriptions". É `REPORTED` (auto-relato, com link de afiliado ao provedor principal), mas
  é o **formato de registro** que falta ao `LR-LIC-002` — não um dado a copiar.
