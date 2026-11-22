# Skills e MCP vistos pelo Studio — digest

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-006` |
| Categoria | agents |
| Projetos | Lia Studio, Lia Agent Hub |
| Fontes | `Lia-Studio@…:docs/research/ARENA-SKILLS-MCP-AGENT-TOOLS-RESEARCH.md` (68 KB, 4× `PENDENTE`); `Lia-AgentHub:docs/research/THIRD-PARTY-SKILLS-CATALOG.md` (34 KB), `INTEGRATION-CANDIDATES.md` (37 KB) |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média |

## 1. O que já foi coberto

Pesquisa transversal do Studio sobre Agent Skills, MCP e ferramentas de agente —
68 KB, com quatro pendências. Cobre formatos, comparação de hosts de agente, e
integração de ferramentas.

## 2. Dedup aplicado

Antes de pesquisar qualquer repositório de Skills ou MCP, consultar:

1. `Lia-AgentHub:docs/research/THIRD-PARTY-SKILLS-CATALOG.md`
2. `Lia-AgentHub:docs/research/INTEGRATION-CANDIDATES.md`
3. `Lia-Studio:docs/research/ARENA-SKILLS-MCP-AGENT-TOOLS-RESEARCH.md`
4. `Lia-Forge:docs/T14-AGENT-ECOSYSTEM-RESEARCH.md`

Esta fundação seguiu essa regra: dos 16 repositórios externos pesquisados, nenhum
repetia um já coberto por esses quatro documentos.

## 3. O que falta (e foi endereçado parcialmente aqui)

| Lacuna | Endereçamento |
|---|---|
| Manifesto de composição de Skills | `LR-AGENT-002` (Claude Trading Skills) |
| Skillsets/perfis | idem |
| Permissão com escopo por execução | `LR-AGENT-003` (Meldwork) |
| Segurança de servidor MCP | `LR-MCP-001` + `LR-MCP-002` |
| Distribuição de Skill com licença | `LR-LIC-001` |

## 4. Padrões de autoria de Skill vindos de fora (2026-11-20)

`LR-STUDIO-006` (`gamedev-skills/awesome-gamedev-agent-skills`) é o melhor exemplo externo
que esta base já leu de **disciplina de autoria**, mesmo sendo de outro domínio:

| Prática | Por que fecha uma lacuna nossa |
|---|---|
| Frontmatter só com `name` + `description`, validado | `LR-AGENT-009` propõe manifesto, mas nada impede campo inventado |
| Descrição que **nomeia o vizinho** ("Not for X (use `y`)") | Resolve Skill que dispara na tarefa errada — o defeito mais caro de um pacote grande |
| Teto de linhas + `## Gotchas` obrigatório | Skill longa é contexto pago sem retorno |
| Índice obrigatório em referência >100 linhas | mantém o carregamento sob demanda honesto |
| Orçamento de caracteres nas descrições (56k → 29,8k) | teto prático: host trunca descrição acima de ~1% da janela |
| Roteador que carrega 2–3 Skills, com regra de propriedade | alternativa a "instalar 48 Skills e esperar" |
| Teste executável dentro da Skill | aproxima Skill de "capacidade verificada", não de texto |

O que **não** copiar: o tamanho do pacote. 79 Skills instaladas sem uso medido é exatamente o
custo que `LR-AGENT-009` tenta evitar. Adaptar as regras, não o catálogo.

### Atualização 2026-11-22 — três objetos de anatomia de Skill entraram na base

| Objeto | O que acrescenta a este landscape |
|---|---|
| `repositories/last30days-skill/REPORT.md` (`LR-STUDIO-011`) | Skill de produção com frontmatter **declarando `license`, `version` e `allowed-tools`** — o mecanismo de custo mínimo para a lacuna das 47 Skills sem licença no payload; e o par `export-ignore` (repositório × artefato instalado) |
| `repositories/skillevaluator/REPORT.md` (`LR-STUDIO-010`) | gate em 3 níveis (estático sem chave → redundância → efeito medido), com *harness check* por host: a resposta verificável para "essa Skill está disponível neste agente?" |
| `repositories/landscape-skill-noise/REPORT.md` (`LR-AGENT-013`) | triagem negativa: `github.com/skills` é **curso**, não Agent Skill — busca sem `filename:SKILL.md` devolve isso |

Nenhum deforma as regras acima; os três reforçam a última linha — adaptar formato, não catálogo.
