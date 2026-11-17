# LIA-RESEARCH — Acesso e Fluxo de Trabalho de Agentes

| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| Modelo | leitura por ponteiro, sem submodule, sem dependência de runtime |
| Decisão de acesso | aberta em `DR-0002` (proprietário) |
| Estado | proposta operacional; **não** é requisito de nenhum projeto |

---

## 1. Princípio

> A base serve os cinco projetos. **Nenhum** dos cinco depende dela para funcionar.

Se o `Lia-Research` desaparecer, os apps continuam compilando, instalando e rodando.
Consequência prática: proibido submodule, proibido import em build, proibido `git clone`
no instalador, proibido token de build.

## 2. Modelo de consulta (3 camadas)

```text
camada 1 — índice       RESEARCH-INDEX.md            (1 arquivo, sempre atualizado)
camada 2 — decisão      decisions/*/DR-*.md          (o que já foi decidido e por quê)
camada 3 — evidência    repositories/*/REPORT.md     (o que foi verificado, com fonte)
                        cross-project/**, projects/**
```

Um agente nunca começa pela camada 3. Começa pela 1: é o que evita pesquisa duplicada.

## 3. Fluxo de trabalho do agente (7 passos)

| # | Passo | Saída | Falha típica que evita |
|---|---|---|---|
| 1 | Consultar `RESEARCH-INDEX.md` pelo tema | ID existente ou "não existe" | refazer pesquisa de 30 KB |
| 2 | Consultar a pesquisa interna do projeto (§2 de `AGENT-WORKFLOW.md`) | se já está coberto | duplicar doc de 68 KB |
| 3 | Abrir o relatório de origem, não o digest | evidência com SHA | citar resumo de resumo |
| 4 | Coletar com pin (repo@sha:caminho + data + licença lida) | linha de evidência | "segundo o README" |
| 5 | Classificar cada afirmação | rótulo de evidência | opinião virando fato |
| 6 | Publicar em caminho único, com IDs no índice | relatório + entrada no índice | 3 documentos sobre o mesmo tema |
| 7 | Rodar `tools/validate.py` | 0 erros | link quebrado, ID órfão, segredo |

## 4. Protocolo de leitura em repositório de origem

```bash
# 1. qual é o estado real?
gh api repos/BloomRX/Lia-Project/branches --jq '.[].name'
# 2. em qual branch está o documento? (não existe em main na maioria dos casos)
gh api "repos/BloomRX/Lia-Project/contents/<path>?ref=<branch>" --jq '.sha'
# 3. ler o conteúdo em raw (nunca com .content + base64: vira mojibake)
gh api -H "Accept: application/vnd.github.raw" "repos/BloomRX/Lia-Project/contents/<path>?ref=<branch>"
```

Regras derivadas de falhas reais:
- `?ref=main` dá 404 para a maioria dos docs → resolver branch antes;
- clone blobless + enumeração ingênua pendura >10 min → usar Trees API;
- SHA curto em comparação de conjunto gera falso "não existe" → comparar SHA completo.

## 5. Permissões por papel

| Papel | Ler | Escrever | Publicar | Revisar |
|---|---|---|---|---|
| Orchestrator | tudo | sim | sim (com checklist) | sim |
| Especialista de projeto | tudo | só no seu escopo | via PR | não |
| Agente de produto (Project/Forge/Studio/AgentHub) | tudo | **não** | **não** | não |
| Humano proprietário | tudo | tudo | sim | sim (final) |

O agente de produto é **consumidor**. Isso é deliberado: quem está implementando não
deve alterar a base que justifica a implementação.

## 6. O que um agente **não** pode fazer aqui

| Proibido | Motivo |
|---|---|
| Editar ADR de projeto de origem | decisão do projeto |
| Declarar arquitetura ou requisito | pesquisa não promove a requisito |
| Criar dependência entre projetos | viola independência |
| Conceder licença | exige titular |
| Copiar código de terceiro | só ponteiro + SHA |
| Apagar/arquivar pesquisa publicada | vai para `archive/`, com motivo |
| Marcar item como concluído porque o arquivo existe | o critério é conteúdo verificado |

## 7. Cenários de uso (o teste real deste documento)

### Cenário A — "queremos voz melhor no PT-BR"
1. índice → `LR-VOICE-001` → `cross-project/voice/VOICE-STACK-DIGEST.md`;
2. digest diz: 3 lacunas `BLOCKED`, regra "medir o Kokoro existente antes de adicionar";
3. agente **não** pesquisa modelo novo: aponta H-4 e a regra;
4. resultado: nenhuma semana perdida, nenhuma dependência adicionada.

### Cenário B — "podemos usar o serviço X de modelos?"
1. índice → `LR-PROV-001` → relatório → **REJEITAR** com 4 condições;
2. agente lê as condições, verifica se alguma foi cumprida, e responde "não, e aqui está
   o que precisa acontecer";
3. resultado: recusa rastreável, não opinião.

### Cenário C — "por que não usamos ReScript?"
1. índice → `LR-STUDIO-003` → **REJEITAR** + condição de reabertura;
2. `decisions/REJECTED/DR-0016`;
3. resultado: a pergunta não volta a cada trimestre.

### Cenário D — "preciso implementar o HA-MCP"
1. `LR-MCP-001-D` (plano) → 8 fatias com gates;
2. `DR-0003` **PENDING** → agente **não** implementa; apresenta o plano e a pendência;
3. resultado: o agente não decide o que é do proprietário.

## 8. Sincronização e atualização

| Pergunta | Resposta |
|---|---|
| Com que frequência revisar? | por documento (`Próxima revisão`); trimestral para CURRENT |
| O que fazer quando o original muda? | atualizar o digest e registrar em `RESEARCH-CHANGELOG.md` |
| Cópia local permitida? | sim, de leitura; sem escrita, sem PR automático |
| Precisa de token no projeto? | **não** — isso criaria dependência de runtime |
| E se a branch de origem sumir? | `data/snapshots/` prova o que existia na data |

## 9. Critério de aceitação deste modelo

Um agente novo, recebendo apenas o link do repositório e uma pergunta de produto,
deve: (a) encontrar o documento certo em ≤2 consultas; (b) não repetir pesquisa
existente; (c) não ultrapassar seus limites de decisão; (d) deixar rastro de onde leu.

Foi testado nos 4 cenários acima, com o corpus real desta base.
