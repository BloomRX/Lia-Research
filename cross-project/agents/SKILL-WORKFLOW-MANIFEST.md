# Manifesto de workflows para Skills — proposta neutra

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-009` |
| Categoria | agents |
| Projetos beneficiados | Lia Agent Hub (catálogo), Lia Forge (execução de asset), Lia Studio (autoria) |
| Fontes de evidência | `tradermonty/claude-trading-skills@a627d17d` (`workflows/*.yaml` 15, `skillsets/*.yaml` 7) → `LR-AGENT-002`; `Lia-Forge:shared/capabilities/registry.mjs` (49 capacidades) → `LR-AGENT-005`; `Ryder-Sun/Meldwork@db9b6c84` (permissão por execução) → `LR-AGENT-003`; `LR-LIC-001`/`LR-LIC-003`; contêiner `.lia-capability` do Agent Hub |
| Data | 2026-11-17 |
| Status | **PROPOSTA** — não é decisão, não é implementação, não é requisito de projeto |
| Confiança | Alta para os padrões citados (lidos em código); o schema aqui é síntese, não norma existente |

---

## 1. Pergunta

É possível descrever um **workflow de Skills** de forma que os três projetos o entendam
sem que nenhum dependa do outro — com entradas, saídas, permissões, ferramentas,
versionamento e validação declarados em arquivo?

## 2. O problema que existe hoje

| Sintoma | Onde | Evidência |
|---|---|---|
| Processo descrito em prosa dentro do `SKILL.md` | 21 Skills do Lia-Project | nenhum campo de entrada/saída/permissão |
| Capacidade declarada em código, não em contrato | Forge: `registry.mjs` com 49 capacidades | estado (16/5/5/23) sem schema versionado |
| Nenhuma Skill declara credencial que consome | 50 payloads auditados | `LR-LIC-003` §7.1 |
| Composição feita por prompt longo | prática observada | `LR-AGENT-002` §4 |

O padrão que resolve isso já existe e foi lido em código: o repositório de Skills
financeiras mantém `workflows/<fluxo>.yaml` — **quais** Skills, em **que ordem**, com
**quais gates** e **quais artefatos** — e `skillsets/<perfil>.yaml` — subconjunto por
perfil. Máquina-legível, versionável, auditável.

## 3. Princípios (não negociáveis)

1. **Neutro de provider e runtime.** O manifesto nunca nomeia modelo, endpoint ou
   fornecedor. Ele nomeia *capacidade*; quem executa escolhe o provider (`LR-MODEL-005`).
2. **Sem dependência entre projetos.** Nenhum manifesto importa arquivo de outro
   projeto. Um projeto consome o manifesto; não o código do vizinho.
3. **Declarativo, não executável.** O manifesto descreve; não contém script com efeito.
4. **Validável sem executar.** Um validador estático consegue dizer se está coerente.
5. **Licença e escopo dentro do pacote.** Sem `LICENSE`/`NOTICE` no payload, a Skill não
   é exportável (`LR-LIC-001`, `LR-LIC-003`).
6. **Permissão declarada pelo que a Skill toca**, não pelo que ela diz que faz
   (`LR-MCP-001-B`: risco no par alvo×ação, não no nome).

## 4. Anatomia proposta de um pacote

```text
<skill-id>/
├── SKILL.md              # instrução para o agente (formato atual, preservado)
├── manifest.yaml         # NOVO — contrato de composição
├── LICENSE               # obrigatório se a licença ≠ do repositório hospedeiro
├── NOTICE                # obrigatório se derivada de terceiro
└── UPSTREAM.md           # obrigatório se de terceiro (modelo: alethe/UPSTREAM.md)
```

`SKILL.md` continua sendo a fonte da instrução. O manifesto é o **contrato**; não
substitui o texto, não duplica o texto.

## 5. Schema proposto (`manifest.yaml`)

### 5.1 Campos obrigatórios

| Campo | Tipo | Regra |
|---|---|---|
| `schema_version` | `1` | inteiro; muda só com quebra de compatibilidade |
| `id` | string | igual ao nome do diretório; `kebab-case`; único no catálogo |
| `version` | semver | versão do **conteúdo**, não do schema |
| `title` | string | 1 linha, humano |
| `description` | string | 1–3 linhas; usada em busca |
| `purpose` | enum | `research` \| `authoring` \| `execution` \| `review` \| `release` |
| `inputs` | lista | cada item: `name`, `type`, `required`, `description` |
| `outputs` | lista | cada item: `name`, `type`, `description` |
| `capabilities.requires` | lista | capacidade **abstrata** (ex.: `text.generate`, `image.render`) |
| `permissions` | lista | cada item: `target` (domínio), `actions`, `risk` (`R0`–`R3`), `consent` |
| `license` | objeto | `spdx`, `holder`, `notice_required` (bool) |
| `validation` | objeto | `static` (lista de checagens), `runtime` (o teste que prova funcionamento) |

### 5.2 Campos opcionais

| Campo | Uso |
|---|---|
| `capabilities.provides` | quando a Skill publica capacidade para outras consumirem |
| `tools` | ferramentas concretas **opcionais**: `mcp:home-assistant`, `cli:ffmpeg` |
| `credentials` | nomes de credencial requeridas (nunca valores) |
| `runtime.hints` | preferências não vinculantes: `gpu: preferred`, `offline: required` |
| `depends_on` | outras **Skills** por id+versão (nunca outro projeto) |
| `supersedes` | id+versão que esta substitui |
| `provenance` | `origin`, `upstream_version`, `patched` (bool), `patch_note` |
| `inputs.schema` | JSON Schema quando a entrada for estruturada |

### 5.3 Campos **proibidos** (por desenho)

| Proibido | Por quê |
|---|---|
| `model`, `provider`, `endpoint`, `api_key` | quebra a neutralidade; muda por máquina |
| caminho absoluto ou `../` para outro projeto | quebra a independência |
| script inline com efeito | manifesto declara; não executa |
| segredo de qualquer tipo | política de segurança |

## 6. Exemplo mínimo (ilustrativo, sintético)

```yaml
schema_version: 1
id: sprite-sheet-compose
version: 1.2.0
title: Compor sprite sheet a partir de quadros
description: Recebe quadros PNG e produz uma folha com grade declarada e metadados.
purpose: execution

inputs:
  - name: frames
    type: image/png[]
    required: true
    description: quadros em ordem de animação
  - name: grid
    type: object
    required: false
    description: "{cols, rows}; padrão calculado do número de quadros"

outputs:
  - name: sheet
    type: image/png
    description: folha composta
  - name: metadata
    type: application/json
    description: posições, fps, nomes de quadro

capabilities:
  requires:
    - image.compose          # abstrato: sem nomear biblioteca
  provides: []

permissions:
  - target: filesystem.workspace
    actions: [read, write]
    risk: R1
    consent: once
  - target: network
    actions: []
    risk: R0
    consent: none

credentials: []

tools:
  - cli: imagemagick   # opcional; a capacidade pode ser satisfeita por outro backend

runtime:
  hints:
    offline: preferred
    gpu: none

license:
  spdx: null             # pendente de DR-0001 — declarar null é válido e visível
  holder: BloomRX
  notice_required: false

validation:
  static:
    - outputs_declared
    - permissions_classified
    - no_cross_project_path
  runtime: tools/test-sprite-sheet.sh   # o que prova que funciona

provenance:
  origin: internal
  patched: false
```

## 7. Workflow (composição), não só Skill

O manifesto de *Skill* descreve a unidade. O workflow é outro arquivo, menor:

```yaml
schema_version: 1
id: character-portrait-to-game-sprite
version: 0.3.0
purpose: execution
steps:
  - skill: character-portrait-cleanup
    version: "^1.0"
    gate: output_reviewed_by_human      # decision gate explícito
  - skill: sprite-sheet-compose
    version: "^1.2"
    when: cleanup.approved
  - skill: release-bundle
    version: "^0.1"
    gate: license_notice_present
artifacts:
  - sheet.png
  - metadata.json
  - NOTICE.txt
```

Regra derivada da fonte: **gate é declaração, não sugestão** — `output_reviewed_by_human`
precisa existir como mecanismo, senão o workflow mente.

## 8. Versionamento

| Mudança | `version` | `schema_version` |
|---|---|---|
| texto do `SKILL.md` | patch | igual |
| novo input opcional / nova capacidade | minor | igual |
| input obrigatório novo, output removido, permissão nova | **major** | igual |
| mudança de campo obrigatório do schema | major | **incrementa** |
| correção de licença/NOTICE | patch | igual |

Consumidores declaram faixa (`^1.0`); o catálogo recusa ambiguidade — **nenhuma Skill
resolve por "latest"** sem faixa explícita. É a lição de todos os relatórios desta base:
`main` desatualizada já causou leitura de estado antigo no ecossistema.

## 9. Validação proposta (5 checagens estáticas + 1 de execução)

| # | Checagem | Falha significa |
|---|---|---|
| V1 | schema válido contra `manifest.schema.json` | manifesto quebrado |
| V2 | toda `capabilities.requires` resolvível no catálogo de capacidades | workflow impossível de executar |
| V3 | toda `permissions` com `target`, `actions` e `risk` | permissão não classificada = R2 por default |
| V4 | `license` presente; se derivado, `NOTICE` e `UPSTREAM.md` presentes | exportação bloqueada |
| V5 | nenhum caminho cross-project, nenhum campo proibido | independência violada |
| V6 | `validation.runtime` existe **e** foi executado alguma vez | Skill não provada |

V1–V5 são estáticas e podem rodar em CI. V6 é a única que exige máquina — e é a que
separa "declarado" de "funciona". Nenhuma Skill do ecossistema tem V6 hoje.

**Precedente real (2026-11-17):** o bundle `claude-bughunter` implementa tanto o V6
quanto o gate estático — `eval/run_eval.py` roda a mesma tarefa com e sem as Skills
(ablação) e publica o delta **mesmo quando é zero**; `scripts/lint_skills.py` +
`engine/skill_map.py` falham o CI quando uma Skill não está roteada. Ver `LR-SEC-006`
R1 (eval) e R4 (lint + roteamento).

## 10. Como cada projeto usa sem depender do outro

| Projeto | Papel | Lê | Escreve |
|---|---|---|---|
| **Lia Agent Hub** | catálogo e importação | manifesto de qualquer origem | índice próprio; nunca o payload alheio |
| **Lia Forge** | execução de workflows de asset | manifesto de Skill + workflow | seu próprio `registry.mjs` (compatível) |
| **Lia Studio** | autoria e revisão | manifesto para montar UI de composição | nada fora do seu repo |
| **Lia-Project** | consumo em produto | manifesto para montar tela de configuração | nada |

Acoplamento zero: o **formato** é compartilhado; o **arquivo** nunca é importado de
outro repositório. Se o Hub desaparecer, Forge e Studio continuam lendo manifestos
locais. É a mesma regra da base de pesquisa (`LIA-RESEARCH-ACCESS-AND-AGENT-WORKFLOW.md` §1).

## 11. O que este documento **não** decide

- Nome final do arquivo (`manifest.yaml` vs `skill.yaml`) — decisão de implementação.
- Se o Hub passa a validar na importação — decisão do Hub (`DR-0011`).
- Se o Forge migra as 49 capacidades para manifestos — decisão do Forge.
- Licença das Skills Lia — `DR-0001` (aqui só se declara que o campo é obrigatório e
  pode ser `null` de forma explícita, para que a ausência seja visível).

## 12. Riscos da proposta

| Risco | Mitigação |
|---|---|
| Vira burocracia: 50 manifestos para manter | gerar a partir do `SKILL.md` existente; só 5 campos são realmente novos |
| Divergir do padrão de fato (`SKILL.md` do ecossistema Anthropic) | o manifesto é **aditivo**: nenhum campo do `SKILL.md` muda |
| Ser adotado como dependência entre projetos | V5 proíbe caminho cross-project; formato copiável, não importável |
| `permissions` virar lista decorativa | V3 + `risk` sem default silencioso (não classificado = R2) |
| Ninguém executar V6 | declarar V6 como requisito de `publish`, não de `draft` |

## 13. Pendências

| Pendência | Rótulo |
|---|---|
| Escrever `manifest.schema.json` real | `NOT RUN` (é implementação; proibida nesta fase) |
| Testar com 3 Skills reais do ecossistema | `NOT RUN` |
| Validar contra o formato `SKILL.md` do ecossistema Anthropic | `UNVERIFIED` (não pesquisado nesta rodada) |
| Decidir adoção | `PENDING` → `DR-0020` (proposto) |
