# Comportamentos de interface

| Campo | Valor |
|---|---|
| ID | `LR-UI-004` |
| Categoria | ui |
| Projetos | Lia-Project (Stage), Lia Forge, Lia Agent Hub |
| Fontes | `repositories/vercel-ui/REPORT.md`, `repositories/plannotator/REPORT.md`, `repositories/ai-design-skills/REPORT.md`, `Lia-Studio:docs/UI-UX-DESIGN-SYSTEM-LIA-STUDIO.md`, `Lia-Project:docs/reports/LIA-UI-UX-AUDIT-2026-11-14.md` (49 KB), `LIA-UIUX-RECONCILIATION.md` |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média |

## 1. Stack de UI observada

Vue + TypeScript + UnoCSS no Stage (Electron); design system próprio na Studio;
auditorias de UI/UX em Project (49 KB) e Forge (38 KB+); briefs de design no Hub
(Stitch, 15 arquivos).

## 2. Problemas recorrentes (das auditorias internas)

| Problema | Ocorrência |
|---|---|
| Foco perdido em popup/overlay | clássico de Electron |
| Navegação por teclado inconsistente | recorrente em apps com muitas superfícies |
| Estados de erro genéricos | auditorias de UI/UX apontam |
| Densidade de informação no editor | Forge e Studio |
| Reconciliação de UI/UX em 3 documentos | indica divergência entre implementação e spec |

## 3. Referências externas consolidadas

| Fonte | O que oferece | Veredito |
|---|---|---|
| Vercel UI SDK | comportamentos headless (foco, seleção, popup, DnD, ARIA), adaptador Vue real | `ADAPTAR` em protótipo isolado |
| Plannotator | contrato de revisão humana (anotar artefato → devolver ao agente) | `REFERÊNCIA` |
| AI Design Skills | molde de skill de design (intake → sistema visual → critérios) | `ADAPTAR` (formato) |

## 4. Regra

Nenhuma dependência de UI entra no produto antes de **protótipo isolado em uma tela**,
com medição de bundle e comparação com a implementação atual. A ordem de serviço é
explícita nisso.
