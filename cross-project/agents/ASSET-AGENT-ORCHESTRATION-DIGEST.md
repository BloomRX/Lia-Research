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
