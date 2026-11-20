# templates/ — modelo por tipo de objeto

| Campo | Valor |
|---|---|
| Natureza | modelos de relatório, não relatórios |
| Regra | um modelo por **tipo de objeto** pesquisado |
| Placeholder de ID | `LR-XXX-000` — nunca publicar assim; trocar por ID livre do `RESEARCH-INDEX.md` |

Escolher o modelo pelo que o objeto **é**, não pelo nome do repositório. Um objeto
ambíguo (ex.: repositório que é também servidor MCP) usa o modelo do tipo principal e
cita o secundário na seção de aplicações.

| Modelo | Tipo de objeto | Quando usar | Prefixo de ID |
|---|---|---|---|
| `templates/repository-research.md` | repositório de código | biblioteca, app, framework, coleção de scripts | `LR-REPO` |
| `templates/skill-research.md` | Skill / agente empacotado | `SKILL.md`, prompt pack, plugin de agente | `LR-AGENT` |
| `templates/mcp-research.md` | servidor MCP | ferramenta exposta por Model Context Protocol | `LR-MCP` |
| `templates/model-research.md` | modelo + pesos | LLM, difusão, voz, visão, embeddings | `LR-MODEL` |
| `templates/api-service-research.md` | API / SaaS | serviço remoto, endpoint, plataforma paga | `LR-API` |
| `templates/paper-research.md` | paper / benchmark | artigo, leaderboard, avaliação publicada | `LR-PAPER` |
| `templates/technology-evaluation.md` | avaliação ampla | comparação de abordagem, não de objeto único | `LR-CMP` |
| `templates/security-audit.md` | auditoria de segurança | revisão de postura, permissões, superfície | `LR-SEC` |
| `templates/license-audit.md` | auditoria de licença | dúvida de licença/proveniência | `LR-LIC` |
| `templates/benchmark-report.md` | execução de teste | medição própria (Nível 0–3) | `LR-BENCH` |
| `templates/comparative-analysis.md` | comparação | dois ou mais objetos lado a lado | `LR-CMP` |
| `templates/architecture-analysis.md` | arquitetura | desenho interno de um sistema | `LR-ARCH` |
| `templates/source-inventory.md` | inventário | levantamento de fontes, não avaliação | `LR-INV` |
| `templates/decision-record.md` | decisão | decisão de **governança** (`decisions/`) | `DR` |

Obrigatório em qualquer modelo: os três campos separados — `Estado da pesquisa`,
`Resultado de execução`, `Recomendação` — e `Decisão de adoção` vazio quando não existe
decisão registrada (`catalog/CATALOG-SCHEMA.md` §1).

Voltar: `README.md` · `MISSION.md`
