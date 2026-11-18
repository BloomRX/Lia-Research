# Licenças prontas para uso — o que cada projeto pode fazer, sem pesquisar de novo

| Campo | Valor |
|---|---|
| ID | `LR-LIC-005` |
| Categoria | licensing |
| Projetos beneficiados | todos os cinco (camada comum de licença) |
| Fontes | §9 de cada um dos 18 relatórios em `repositories/*/REPORT.md` (licença lida no arquivo, no commit pinado); `data/inventory/license-matrix.tsv` |
| Data | 2026-11-17 |
| Status | CURRENT — **não é parecer jurídico**; é o que o arquivo diz, com obrigação traduzida em ação |
| Confiança | Alta para o texto das licenças lidas; média para fronteiras de caso limite (marcadas) |

---

## 1. A regra em três perguntas

Para qualquer código, asset ou documento de terceiro, o projeto só precisa responder:

1. **Posso usar?** (integrar, consumir como serviço, copiar trecho)
2. **Posso modificar/forkar?** (e o que acontece com o meu código depois?)
3. **O que tenho de colar junto?** (aviso, NOTICE, atribuição)

Se o repositório **não tem arquivo de licença**, a resposta a (1) e (2) é **não** —
"sem arquivo, sem permissão". Está tabulado em `data/inventory/license-matrix.tsv`
(18 linhas, uma por objeto, com colunas `usar_como`, `fork`, `modificar`, `comercial`,
`redistribuir`, `atribuicao`, `copyleft`, `patente`, `notice_obrigatorio`).

## 2. Tabela-mestra (o resumo que evita a pesquisa)

| ID | Objeto | Uso liberado | Fork/derivar | O que colar |
|---|---|---|---|---|
| `LR-MCP-001` | HA-MCP | **consumir como servidor externo** | sim | copyright + MIT |
| `LR-AGENT-003` | Meldwork | adaptar código | sim | NOTICE + Apache |
| `LR-UI-002` | Plannotator | adaptar código | sim | NOTICE + Apache |
| `LR-STUDIO-002` | Claude-Code-Game-Studios | adaptar Skills | sim | MIT **junto do payload** |
| `LR-UI-003` | ai-design-skills | adaptar Skills | sim | copyright + MIT |
| `LR-AGENT-002` | claude-trading-skills | só o padrão de manifesto | sim | copyright + MIT |
| `LR-UI-001` | Vercel UI | código em beta | sim | NOTICE + **ler Beta Terms** |
| `LR-FORGE-004` | pixelfx | adaptar efeitos | sim | `NOTICE.md` viajando; fontes fora |
| `LR-FORGE-003` | ManimGX | código MIT | sim | NOTICE por componente |
| `LR-SEC-006` | Claude-BugHunter | só referência | sim | TASL (CC BY 4.0) |
| `LR-STUDIO-004` | ArtCraft | padrões (Rust não portável) | sim | NOTICE + Apache |
| `LR-AGENT-001` | OpenJarvis | padrões | sim | NOTICE + Apache |
| `LR-STUDIO-001` | OpenIDEA | padrões | sim | NOTICE + Apache |
| `LR-FORGE-001` | Mister Download Manager | **processo separado** (GPL) | vira GPL | fonte + avisos |
| `LR-FORGE-002` | SculptForge | **app externo** (GPL) | vira GPL | fonte + avisos |
| `LR-STUDIO-003` | ReScript | ferramenta externa | LGPL no `compiler/` | avisos por diretório |
| `LR-AGENT-004` | unslop | **nada** (sem licença) | não | — |
| `LR-PROV-001` | RouterHub | **nada** | não | — |

## 3. Quatro modelos prontos para colar

### 3.1 MIT (HA-MCP, Claude-Code-Game-Studios, ai-design-skills, pixelfx, ManimGX, claude-trading-skills)

Coloque em `THIRD-PARTY-NOTICES.md` **do pacote que contém o código**, não só na raiz do repo:

```text
This product includes software developed by <AUTOR> (<URL do repositório>),
licensed under the MIT License. Copyright (c) <ANO> <AUTOR>.
The full MIT license text is reproduced in this file / in licenses/MIT.txt.
```

Regra que o ecossistema Lia já errou: **o aviso precisa viajar com o payload.** Skill
exportada sozinha sem o aviso não cumpre a obrigação (`LR-LIC-003`, `LR-FORGE-004`).

### 3.2 Apache-2.0 (Meldwork, Plannotator, OpenJarvis, OpenIDEA, Vercel UI, ArtCraft, ManimGX parcial)

```text
This product includes software developed by <AUTOR> (<URL>), licensed under the
Apache License, Version 2.0. A copy of the license is in licenses/Apache-2.0.txt.
Modifications: <o que foi alterado, em uma linha>.
```

Três obrigações que a Apache-2.0 acrescenta ao MIT: manter `NOTICE` quando existir,
**indicar arquivos modificados** e respeitar a cláusula de patente. Em troca, ela
**concede** licença de patente — por isso, entre MIT e Apache, prefira Apache quando
o projeto oferece escolha (caso do ArtCraft: `MIT OR Apache-2.0` → escolha Apache).

### 3.3 CC BY 4.0 (conteúdo do Claude-BugHunter: `*.md`, wordlists, rubricas)

Formato TASL — **T**ítulo, **A**utor, **S**ource, **L**icense:

```text
"<título do material>" by Sachin Sharma, from Claude-BugHunter
(https://github.com/elementalsouls/Claude-BugHunter), licensed under CC BY 4.0
(https://creativecommons.org/licenses/by/4.0/). Changes: <se houver>.
```

CC BY **exige atribuição e link mesmo em uso comercial**, e permite obra derivada.
Se o produto não pode mostrar crédito visível, o conteúdo não pode ser embutido.

### 3.4 GPL-3.0 / LGPL (Mister Download Manager, SculptForge, ReScript `compiler/`)

```text
Regra de fronteira: GPL só como PROGRAMA SEPARADO (processo próprio, comunicação
por MCP/stdio/IPC). Nunca linkar, nunca copiar crate/módulo para dentro do app.
Redistribuir binário exige oferecer o código-fonte correspondente.
```

Isso é `INFERRED` (interpretação usual), **não** parecer jurídico — a fronteira de
"programa separado" tem critérios técnicos e merece avaliação se virar produto.

## 4. Fichas de uso (o que o projeto precisa saber, sem abrir o relatório)

**`LR-MCP-001` HA-MCP — MIT.** Use como servidor externo; pode forkar. Não exibe
marca "Home Assistant" sem seguir a política do HA. `NOTICE` com copyright + MIT.

**`LR-AGENT-003` Meldwork — Apache-2.0 + `COMMERCIAL_USE.md`.** Melhor modelo de
documentação comercial do corpus: copie o arquivo, não só a licença.

**`LR-UI-002` Plannotator — Apache-2.0.** Adapte o padrão de revisão humana; nomes de
integrações (Claude, Codex, Copilot) são marcas de terceiros.

**`LR-STUDIO-002` Claude-Code-Game-Studios — MIT.** Adapte as Skills, mas **mova o
aviso para dentro do payload**. "Claude" é marca da Anthropic; não use no nome do
produto derivado.

**`LR-UI-003` ai-design-skills — MIT.** Adapte; "Figma" é marca da Figma Inc. — uso
descritivo é aceitável, parceria implícita não.

**`LR-AGENT-002` claude-trading-skills — MIT.** Só o **padrão de manifesto** serve;
dados de mercado têm licença do provedor, fora da MIT.

**`LR-UI-001` Vercel UI — Apache-2.0 + Vercel Beta Terms.** Código adaptável, mas o
Beta Terms é contrato de uso, não licença: ler antes de embarcar em produto.

**`LR-FORGE-004` pixelfx — MIT + `NOTICE.md` por efeito.** Adapte os efeitos **com o
NOTICE junto**; a fonte em `gallery/fonts` **não** é MIT — leia antes de usar.

**`LR-FORGE-003` ManimGX — licença mista.** Código MIT: ok. Conteúdo CC-BY-SA:
copiar para repositório proprietário cria obrigação share-alike — **não copie docs**.
Fontes OFL: uso ok, venda isolada da fonte não.

**`LR-SEC-006` Claude-BugHunter — MIT + CC BY 4.0.** Código dos scripts é MIT; o
conteúdo é CC BY. Uso prático: referência e TASL. Nunca embutir as 83 Skills.

**`LR-STUDIO-004` ArtCraft — `MIT OR Apache-2.0`.** Escolha Apache (patente). O código
Rust não é portável para Electron/Vue: use o **desenho** (`LR-STUDIO-004` §14).

**`LR-AGENT-001` OpenJarvis / `LR-STUDIO-001` OpenIDEA — Apache-2.0.** Padrões
reimplementáveis; código não é alvo de fork.

**`LR-FORGE-001` Mister Download Manager / `LR-FORGE-002` SculptForge — GPL-3.0.**
Fora do app. Se um dia integrar, processo separado + fonte disponível.

**`LR-STUDIO-003` ReScript — LGPL no `compiler/`, MIT no resto.** O `LICENSE` declara o
mapa **por diretório** — é o modelo a imitar. Compilador como ferramenta: ok.

**`LR-AGENT-004` unslop — sem licença.** Nenhuma cópia. A ideia (rewrite gates) pode ser
reimplementada de forma independente.

**`LR-PROV-001` RouterHub — bloqueado.** MIT só nos repositórios de marketing; o serviço
e os modelos modificados não têm licença verificável.

## 5. O caso Lia: cinco repositórios públicos sem `LICENSE`

Hoje os cinco repositórios dos apps **não têm arquivo de licença** (`CONFIRMED`:
`.license = null` em todos). Consequência técnica: **todos os direitos reservados** —
nada é concedido a terceiros. Isso **não** impede o dono de usar o próprio código,
mas impede qualquer distribuição externa e deixa ambíguo o uso por terceiros.

Isso importa mais agora que se sabe que **os cinco são públicos**: há 48 Skills sem
licença legível por qualquer pessoa, e um colaborador não tem permissão formal para
reutilizar nada.

`DR-0001` está aberto. Para o proprietário **só escolher**, três opções e consequências:

| Opção | Concede | Custo | Combina com |
|---|---|---|---|
| **A. MIT** | uso, modificação, distribuição, comercial; aviso | perde controle sobre forks; sem cláusula de patente | Skills e utilitários |
| **B. Apache-2.0** | idem + patente + NOTICE | mais obrigações de documentação | apps e bibliotecas |
| **C. Manter sem licença** | nada a terceiros | impede colaboração e distribuição; risco de terceiro achar que pode usar | nada — só faz sentido se o repo for privado |

Recomendação desta base (`INFERRED`, decisão é do dono): **B para código, A para
conteúdo curto**, e — o mais importante — **declarar a licença dentro de cada Skill**
(`license:` no payload), que é o erro já registrado em `LR-LIC-001`/`LR-LIC-003`.

## 6. Como um projeto consome isto em 3 passos

1. **Ache a linha** do objeto em `data/inventory/license-matrix.tsv` (ou a ficha em §4).
2. **Cole o `NOTICE`/atribuição** do §3 no **pacote que contém o material** — não na raiz
   do repositório, se o material sai sozinho (Skill, efeito, asset).
3. **Registre** em `docs/licenses/` do projeto + cite o ID (`LR-...`) no commit que
   introduziu o material.

## 7. Limites deste documento

- **Não é parecer jurídico.** Traduz o que os arquivos de licença dizem.
- **Não concede licença de terceiros** — só repete o que já foi concedido pelo autor.
- **Não decide a licença da Lia** (`DR-0001`, proprietário).
- **Não cobre** marcas, trade dress, patentes de terceiros, termos de serviço de API
  (Vercel Beta Terms, HackerOne, provedores de modelo) nem jurisdição.
- **Não substitui** leitura do arquivo quando o caso for fronteira (GPL × programa
  separado, CC-BY-SA × conteúdo proprietário).
