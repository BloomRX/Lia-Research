# Licenças prontas para uso — o que cada projeto pode fazer, sem pesquisar de novo

| Campo | Valor |
|---|---|
| ID | `LR-LIC-005` |
| Categoria | licensing |
| Projetos beneficiados | todos os cinco (camada comum de licença) |
| Fontes | seção de evidências de cada um dos **59** relatórios em `repositories/*/REPORT.md` (licença lida no arquivo, na ref pinada); `data/inventory/license-matrix.tsv` |
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
"sem arquivo, sem permissão".

**Selo ≠ licença.** A API do GitHub informa **uma** licença por repositório. Em
`storytold/photocraft` (pasta `artcraft`) ela diz `Apache-2.0`, mas o repositório oferece
`LICENSE-MIT` **e** `LICENSE-APACHE` — o consumidor escolhe. Quem lê o selo perde uma
opção de uso. Conferido em 2026-11-20 (`audits/REAUDIT-2026-11-20.md`). Está tabulado em `data/inventory/license-matrix.tsv`
(42 linhas, uma por objeto, com colunas `usar_como`, `fork`, `modificar`, `comercial`,
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
| `LR-STUDIO-005` | BRUTAL (C#/Vulkan) | só referência | sim | créditos + **logo na abertura** + `NOTICE.txt` |
| `LR-AGENT-001` | OpenJarvis | padrões | sim | NOTICE + Apache |
| `LR-STUDIO-001` | OpenIDEA | padrões | sim | NOTICE + Apache |
| `LR-FORGE-001` | Mister Download Manager | **processo separado** (GPL) | vira GPL | fonte + avisos |
| `LR-FORGE-002` | SculptForge | **app externo** (GPL-3.0) — desde 2026-11-20 tem **exceção de scripting**: script que use API/CLI/MCP/SDK pode ter qualquer licença | o app vira GPL; o script não | fonte + avisos + `LICENSE-EXCEPTION.md` |
| `LR-STUDIO-003` | ReScript | ferramenta externa | LGPL no `compiler/` | avisos por diretório |
| `LR-AGENT-004` | unslop | **nada** (sem licença) | não | — |
| `LR-FORGE-012` | jena-image-render | padrões e código | sim | copyright + MIT; **imagem do pod é GPL-3.0** (ComfyUI) |
| `LR-FORGE-011` | image-render-generative | referência de proveniência | sim | `NOTICE` + Apache + indicar alterações |
| `LR-STUDIO-010` | NVIDIA/SkillEvaluator | padrões e CI | sim | `NOTICE` + Apache + indicar alterações |
| `LR-STUDIO-011` | last30days-skill | padrões de metadado | sim | copyright + MIT (cookies/robots: não imitar) |
| `LR-VOICE-002` | RealtimeTTS | referência de adendo de escopo | sim | **licença por artefato**: MIT no wheel, Apache-2.0 na master |
| `LR-MODEL-009` | Breeze TTS 2 | **nada** (pesos não comerciais) | não | Apache no código não alcança os pesos |
| `LR-SEC-008` | blender-ai-mcp-addon | **nada** (licença alheia + binário opaco) | não | — |
| `LR-FORGE-014` | Bisqit | **nada** (sem fonte, sem licença publicada) | não | nenhum aviso a colar: o problema aqui é o contrário — o app pede permissões largas e não distribui nada |
| `LR-FORGE-013` | anymachine | método de verificação por peça | sim | MIT; imagens e `data/` à parte; pesos sem declaração lida |
| `LR-AGENT-013` | `github.com/skills` + `waifuai` + topic `stt-tts` | **nada** (triagem negativa) | não | sem arquivo de licença não há permissão de uso |
| `LR-STUDIO-012` | mr-mak-workspace | padrões de workspace, handoff e empacotamento | sim | MIT coletivo + `THIRD_PARTY_NOTICES.md`; `NOTICE` do subprojeto Apache ausente → revisar |
| `LR-PROV-001` | RouterHub | **nada** | não | — |
| `LR-AGENT-011` | ai-memory | adaptar o protocolo de *handoff* | sim | copyright + MIT |
| `LR-SEC-007` | security-audit-skill | check-list de auditoria | sim | copyright + MIT |
| `LR-MODEL-006` | freellmapi | software MIT; o *serviço* é instantâneo de 30 dias | sim (auto-hospedar) | copyright + MIT |
| `LR-STUDIO-006` | gamedev agent skills | adaptar formato e pipeline de asset | sim | `NOTICE` + `LICENSE` + indicar alterações |
| `LR-FORGE-015` | AppFlowy-IO (27 repos) | padrões de CI de self-host; o par de plugins MCP | sim | AGPL por componente; dual no editor; 6 sem licença; o Commercial é acordo, não licença aberta |
| `LR-FORGE-016` | opf / OpenProject (123) | gate de envolvimento de IA, pack de Skills com validação, `THIRD_PARTY.md` | sim | GPL-3.0 no produto **sem** `ee/`; MIT no pack de Skills e no `recense` |
| `LR-FORGE-017` | open-seo | Skills com teste de deriva; verificação em duas camadas | sim | MIT puro; autoria passa por staging privado (proveniência, não licença) |
| `LR-FORGE-018` | Cap | AGENTS.md com ratchet anti-regressão | sim (com cuidado) | MIT **só** nas crates de câmera; AGPLv3 no resto; redistribuir = carregar os dois arquivos |
| `LR-FORGE-019` | cal.diy | `agents/`+symlinks, `PERMISSIONS.md`, `specs/_templates` | sim | MIT puro; a máquina de license-key sobrevive stubada |
| `LR-SEC-009` | Chatwoot | fila de triagem de advisory (211 linhas de Python) | sim, fora de `enterprise/` | MIT com cláusula condicional; `enterprise/` proíbe produção sem assinatura |
| `LR-VOICE-003` | VoiceStudio | censo de pins + testes de pin; o `LICENSE-NOTICE.md` | sim | AGPL-3.0-only declarando uso comercial ok e pesos com termos próprios; submódulo à parte |
| `LR-VOICE-004` | OpenWhispr | allowlist de rede; `Supported Versions` | sim | MIT; termos dos pesos linkados não foram lidos |
| `LR-FORGE-020` | Charakuru | **nada a colar**: a licença proíbe redistribuir e extrair os ativos; vale como modelo de *texto* de licença com limiar financeiro | sim (fork no GitHub) | reter o `LICENSE` próprio + os 5 avisos de terceiros; nada de Skills nem assets fora do pacote |
| `LR-FORGE-021` | HairDeck | o `download_weights.py`: peso + `LICENSE` do modelo + `sha256` esperado, com `local_get` e `HF_ENDPOINT` | sim | Apache-2.0; **nenhum `NOTICE` no repo** — os termos dos modelos gated chegam no workspace, não no Git |
| `LR-AGENT-015` | goose (ex-`block/goose`) | Apache-2.0: usar, modificar, comercializar | sim | copyright + texto; **não há `NOTICE`** (0 na árvore de 3.130 entradas) |
| `LR-AGENT-016` | deer-flow | MIT **no código**; nome, logos e Skills fora do LICENSE | sim | copyright + texto; ler a seção "Product Trademarks" antes de usar marca |
| `LR-AGENT-017` | `anthropics/skills` + diretório de plugins | por Skill: 18 `LICENSE.txt` (a raiz **não tem** licença) | sim, Skill a Skill | o `LICENSE.txt` do pacote + o `THIRD_PARTY_NOTICES.md` (404 linhas) se houver terceiro |
| `LR-AGENT-018` | superpowers | MIT simples (1.070 B) | sim | copyright + texto; as 15 Skills não trazem licença própria |
| `LR-VOICE-005` | pipecat | BSD-2-Clause | sim | copyright + texto + **o `LICENSE-shadcn.md`** se copiar o template vendorizado |
| `LR-DATA-001` | Scrapling | BSD-3-Clause, lib e Skill com `LICENSE.txt` separado | sim | copyright + texto (3 cláusulas: manter aviso) |
| `LR-FORGE-022` | parallel-code | MIT | sim | copyright + texto |
| `LR-RAG-001` | ragflow | Apache-2.0 | sim | NOTICE é obrigatório por Apache; nenhum no repo (0) — criar se redistribuir |
| `LR-PROV-002` | daytona (público) | AGPL-3.0 **só nas tags**; a `main` não tem `LICENSE` | sim (o que foi publicado) | a tag lida + AGPL inteira; **sem suporte e sem garantia** |
| `LR-FORGE-023` | dyad | split: Apache-2.0 fora de `src/pro/`; FSL-1.1-ALv2 dentro (sem uso competitivo) | sim, exceto `src/pro/` | preâmbulo de exceção do `LICENSE` + os 4 arquivos por diretório |
| `LR-UI-006` | raymond-van/animama | **AGPL-3.0-only** no trabalho original; **os ativos não são AGPL** — 10 valores no inventário por arquivo (`LicenseRef-pixiv-VRoidPreset` 128, CC0 32, MIT+AGPL 25, Apache-2.0+AGPL 17, FunASR Model License 1.1 5, marca não licenciada 11) | **não** como dependência nem como código copiado | `LICENSE` (34.020 B) + `licenses/source-review.json` (5.953 entradas, uma por arquivo rastreado) + `licenses/third-party/*` por camada; `review = prepared-not-release-approved` em todas |
| `LR-FORGE-024` | raymond-van/animama-avatar-converter | MIT (1.068 B); UniVRM `v0.131.2` e Mochiya `0826f6e3` por URL Git pinada, ambos MIT; pacote npm com zero dependências | sim (o padrão de invólucro), sem usar a ferramenta | reter o aviso MIT se copiar; **o `.vrm` de saída carrega a licença do prefab de entrada**, e o `README` avisa disso antes do primeiro clique |
| `LR-MCP-005` | bitbonsai/mcpvault | MIT no repositório (1.071 B) e no `package.json` publicado; **zero** dependências declaradas no pacote npm (as 60 são do lockfile da instalação) | sim, e o padrão de `pathfilter`/`frontmatter`/`trash` vale mais copiado do que dependido | `@modelcontextprotocol/server` é **Apache-2.0 sem `NOTICE`** (12.227 B) → ao redistribuir o servidor, levar o texto Apache e verificar a política de marca do MCP; `gray-matter` MIT, `yaml` ISC, `trash` MIT |
| `LR-AGENT-019` | MemPalace/mempalace | MIT (1.079 B) no repositório; o **sdist do PyPI 3.12.0 não traz `LICENSE` nem `README`** (15 arquivos) | sim, como contrato de busca/escopo; o instalador não deve ser usado como dependência da Lia | aviso MIT + verificar a licença do **modelo de embedding** baixado em runtime (~300 MB) e das extras (`chromadb`, `onnxruntime`, `torch`) — a licença do código não as cobre |
| `LR-VEC-001` | PerfectVector (Rastrix Inc.) — **serviço**, não repositório: **nenhuma licença de código existe**; o que rege é contrato (Terms 2026-11-25 · API Terms v1.1 · MCP Terms v1.3 · API Privacy Notice v1.1) | **nada** de código; do lado do resultado, o §8.1 libera: "We claim no ownership of your inputs or of the SVG outputs" | **não** — não há código para usar; e o caminho de prova está fechado: o §10 veda usar entrada, saída, preview, thumbnail ou metadado em treinamento, **avaliação, benchmark**, red-teaming ou dataset, e em qualquer sistema que compita com ou replique o serviço | nada a anexar de licença; o que tem de viajar é o **contrato do uso**: §9 dos API Terms é o consentimento escrito para oferecer o recurso aos nossos usuários, com termos próprios pelo menos tão protetores e **sem repassar a chave** |

Os quatro últimos entraram em 2026-11-20 (antes o digest cobria 19 objetos, a matriz já tinha
22). Contagem conferida contra `data/inventory/license-matrix.tsv` — hoje **59** (+1 em 2026-11-26: `LR-VEC-001`, o primeiro objeto que é **serviço** e não repositório — sem `LICENSE` para ler, com contrato para ler; +2 ainda em 2026-11-26: `LR-UI-006` e `LR-FORGE-024`, a rodada Animama; +10 em 2026-11-25: a leva dos 16 links — `LR-AGENT-015`…`018`, `LR-VOICE-005`, `LR-DATA-001`, `LR-FORGE-022`/`023`, `LR-RAG-001`, `LR-PROV-002`; antes, +2 no mesmo dia com `LR-FORGE-020` Charakuru e `LR-FORGE-021` HairDeck). Os oito seguintes entraram em 2026-11-24 (a leva `AppFlowy-IO`/`opf` + seis repositórios); o método de leitura de licença dividida está em `cross-project/licensing/SPLIT-LICENSE-SCAN.md`.

Cuidado com Apache-2.0 em pacote de Skills: copiar **uma pasta** de Skill leva só `SKILL.md` e
`scripts/`; o `NOTICE` e o `LICENSE` têm de ser copiados junto, ou o reuso fica sem atribuição.

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

### 3.5 Licença com atribuição gráfica (BRUTAL License v1.0)

Existe uma quarta família que não é MIT nem copyleft: **permissiva com obrigação de
exibir logo**. `LR-STUDIO-005` é o exemplo lido.

```text
Produto que usa BRUTAL deve:
  1. incluir o copyright na tela de créditos;
  2. exibir o logo BRUTAL antes do gameplay/função principal, não menos proeminente
     que outros logos (dispensa: permissão escrita, projeto sem fins lucrativos,
     ou quando exibir o logo prejudica o propósito do produto);
  3. distribuir NOTICE.txt junto do produto.
```

Consequência para a Lia: **é decisão de produto, não de engenharia.** Se um app Lia
adotar uma dependência assim, o logo de terceiro entra na abertura do app. Antes de
adotar, responder: "aceitamos um logo de terceiro na abertura?" Se não, a alternativa é
licença comercial (o BRUTAL oferece) ou não usar.

Regra de leitura: **"open source" no README não é tipo de licença.** O BRUTAL é
permissivo, permite uso comercial, e ainda assim **não é OSI** — o próprio README diz
que não foi submetido. Sempre ler o `LICENSE`.

### 3.4 GPL-3.0 / LGPL (Mister Download Manager, SculptForge, ReScript `compiler/`)

> **Atualização de 2026-11-20 (SculptForge).** O repositório passou a trazer
> `LICENSE-EXCEPTION.md` — *SculptForge Scripting Exception 1.0*, permissão adicional do §7
> da GPLv3: programa que use o app apenas pela API pública Python, CLI, servidor MCP ou SDK
> de plugin **pode ter qualquer licença**. Isso muda a resposta para "posso escrever script
> em volta?" (antes: vira GPL; agora: não vira). O app continua GPL-3.0. Fonte: commit
> `30bc117`, arquivo lido em `repositories/sculptforge/REPORT.md` §Reauditoria.

```text
Regra de fronteira: GPL só como PROGRAMA SEPARADO (processo próprio, comunicação
por MCP/stdio/IPC). Nunca linkar, nunca copiar crate/módulo para dentro do app.
Redistribuir binário exige oferecer o código-fonte correspondente.
```

Isso é `INFERRED` (interpretação usual), **não** parecer jurídico — a fronteira de
"programa separado" tem critérios técnicos e merece avaliação se virar produto.

## 4. Fichas de uso (o que o projeto precisa saber, sem abrir o relatório)

**`LR-AGENT-011` ai-memory — MIT.** Adapte o protocolo de *handoff*; o servidor recebe só
identidade de sessão, nunca o corpo do transcript — copiar essa fronteira é o valor.
**MIT exige o aviso junto do código derivado.**

**`LR-SEC-007` security-audit-skill — MIT.** Use como check-list de auditoria (11 classes
de risco, `report-schema.json`); reimplementar o fluxo é mais útil que instalar.

**`LR-MODEL-006` freellmapi — MIT no software.** O catálogo de free tiers é uma foto de
30 dias atrás; o serviço pago é outro produto. Auto-hospedar o código é permitido, usar a
lista como verdade não é.

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

**`LR-STUDIO-005` BRUTAL — licença própria (base MIT + atribuição gráfica).** Se um dia
for usado, exige créditos, **logo antes da função principal** e `NOTICE.txt`. Não é OSI.
O padrão a copiar dele é estrutural: `LICENSES/` **dentro de cada pacote** que redistribui
terceiros, e um `NOTICE.txt` de três linhas.

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
