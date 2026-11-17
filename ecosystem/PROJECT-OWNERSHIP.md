# Propriedade dos projetos

Quem decide o quê. Usado para saber a quem uma pesquisa deve ser endereçada e quem
pode transformar recomendação em decisão.

---

## 1. Fronteiras declaradas

| Projeto | Responsabilidade | Não é responsável por |
|---|---|---|
| **Lia-Project** | experiência conversacional, Stage, voz no produto, providers, consentimento do usuário, desktop runtime | catálogo de capacidades de terceiros, produção de assets, treinar modelos |
| **Lia Forge** | produção de assets (2D/3D), pipelines, integração Blender, geração | experiência conversacional do usuário final |
| **Lia Studio** | engine de jogo, gameplay, editor, experiência de criação de jogos | runtime de assistente pessoal |
| **Lia Agent Hub** | catálogo, descoberta, empacotamento e orquestração de Skills/MCP | executar a experiência do usuário; hospedar modelos |
| **Lia Model Lab** | avaliação de modelos e hardware, experimentos de inferência local, governança de experimento | servir produção; decidir catálogo do produto |
| **Lia-Research** (este) | pesquisa, consolidação, proveniência, índice | implementar, decidir, alterar os demais |

## 2. Regra de não-dependência

Nenhum projeto pode **exigir** outro para funcionar. Consequências práticas:

- Lia-Project não pode depender de Lia Agent Hub estar rodando.
- Lia Agent Hub não pode depender de Lia Model Lab.
- Nenhum pode depender de Lia-Research em runtime (clone de leitura é permitido;
  import em build, não).
- Uma tecnologia pesquisada pode beneficiar vários projetos; isso não obriga adoção
  conjunta nem simultânea.

## 3. Quem aprova o quê

| Tipo de decisão | Aprovador | Artefato |
|---|---|---|
| Implementar tecnologia nova em um projeto | responsável daquele projeto | `decisions/ACCEPTED/DR-*` + ADR no projeto |
| Licença de conteúdo Lia | proprietário BloomRX | `DR-0001` |
| Distribuição de Skill a usuário final | proprietário + auditoria de licença | `DR-0001` + `LR-LIC-*` |
| Integração de automação residencial (R2/R3) | proprietário, com matriz de risco aceita | `DR-0003` |
| Acesso de agentes ao Lia-Research | proprietário | `DR-0002` |
| Visibilidade do repositório | proprietário (ação bloqueada para o agente: 403) | `DR-0006` |
| Mudança de governança | proprietário | PR com label `governance` |

## 4. Sobreposições conhecidas (não resolvidas aqui)

| Sobreposição | Projetos | Quem deveria decidir |
|---|---|---|
| Skill de revisão de marca (`lia-brand-check` × `lia-brand-consistency-review`) | Forge × Model-Lab | produto, com apoio do Hub |
| Orquestração de agentes (`lia-agent-orchestration` × `multi-agent-orchestration` × `alethe`) | Project × Model-Lab × terceiro | arquitetura, com Hub |
| Produção 3D (Forge) × engine de jogo (Studio) | Forge × Studio | fronteira de produto |
| Catálogo de modelos (Model Lab) × catálogo de providers (Project) | Model-Lab × Project | produto |

O Lia-Research registra a sobreposição e as evidências. **Não** decide a fusão:
consolidar Skills é decisão de produto, e a ordem de serviço proíbe promover
recomendação a decisão.

## 5. Contato e responsável humano

A ordem de serviço nomeia "Agente Research / Research Orchestrator" como responsável
de execução e o usuário (`BloomRX`) como autoridade. Não há, nos documentos
inventariados, registro de outros mantenedores humanos por projeto. Se houver, este
arquivo deve ser atualizado pela pessoa responsável.
