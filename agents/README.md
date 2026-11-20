# agents/ — instruções dos agentes de pesquisa

| Campo | Valor |
|---|---|
| Natureza | instrução operacional de agente, não política de produto |
| Limite | nenhum agente desta pasta aprova adoção de tecnologia |
| Canônico em | `MISSION.md` §3 e §5 |

| Documento | Para quem | O que faz |
|---|---|---|
| `agents/RESEARCH-ORCHESTRATOR.md` | agente orquestrador de pesquisa | recebe demanda, investiga, delega, testa, busca evidência externa, consolida, publica, mantém catálogo e histórico |
| `agents/SPECIALIST-ROLES.md` | especialistas por domínio | define quem cobre segurança, licença, modelo, MCP, UI, hardware, memória |
| `agents/SKILLS-OPERATING-SET.md` | qualquer agente do Research | fixa o conjunto mínimo de Skills do ecossistema Lia aplicado ao Research, os gatilhos de cada uma e as rejeitadas com motivo |

Ambos herdam a proibição central: **recomendar sim, decidir adoção não**. Se um agente
se pegar escrevendo "aprovado para integração", o texto está errado — o vocabulário
fechado está em `catalog/CATALOG-SCHEMA.md` §4.

Formulários de entrada ficam em `.github/ISSUE_TEMPLATE/`: `pesquisa.md` (novo objeto),
`lacuna.md` (lacuna de evidência), `decisao.md` (pedido de decisão ao proprietário).

Voltar: `README.md`
