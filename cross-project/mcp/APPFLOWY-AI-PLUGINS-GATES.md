# `confirm: true` como JSON Schema: o AppFlowy colocou a permissão por execução dentro do manifesto de ferramentas

| Campo | Valor |
|---|---|
| ID | `LR-MCP-004` |
| Categoria | mcp |
| Objeto | `AppFlowy-IO/appflowy-ai-plugins` (AGPL-3.0-only, Python, 1★, 37 arquivos, HEAD `318a8c8`, push 2026-11-05) |
| Projetos beneficiados | Lia Project (política de execução), Lia Agent Hub (formato de plugin/manifesto), Lia Forge (empacotamento para Claude e Codex), Lia Security (escopo read/write/admin), Lia Model Lab (nada) |
| Fontes | clone `--depth 1` do repositório lido arquivo por arquivo; execução do verificador interno (`scripts/check.py`) e do gerador determinístico (`scripts/annotation-table.py`); `gh api` para licença/release/idiomas |
| Resultado de execução | **LOCAL_SMOKE_PASS** — os dois scripts do próprio repositório foram executados neste sandbox (linha em `data/testing/test-log.tsv`) |
| Recomendação | **ADAPT** — o mecanismo `confirm` no `inputSchema` e o bloco `tools_integrity`; nenhum código |
| Decisão de adoção | — nenhuma registrada |
| Data | 2026-11-24 |
| Status | CURRENT — documento de evidência e proposta; nenhuma mudança foi feita em projeto Lia |
| Confiança | Alta: todas as contagens abaixo foram medidas nos arquivos, não no README |

---

## 1. O que é o objeto, em uma frase

Quatro plugins MCP do AppFlowy — `claude/appflowy`, `claude/appflowy-self-hosted`, `codex/appflowy`,
`codex/appflowy-self-hosted` — mais dois `marketplace.json` (`.claude-plugin/` e `.agents/plugins/`) e um
catálogo canônico que as quatro variantes descrevem — `tools.json`, dentro do diretório `catalog/` do repositório deles. Um repositório de **uma
estrela**, o objeto menos popular desta leva de oito links, e o único cujo verificador interno deu para
executar de ponta a ponta.

## 2. O número que importa: 31 de 45 ferramentas exigem `confirm`

Medido direto no `tools.json` do catálogo (repo deles) com um script próprio (não com `grep`):

| Medida | Valor |
|---|---|
| Ferramentas no catálogo | **45** |
| Com propriedade `confirm` no `inputSchema.properties` | **31** |
| Dessas, com `confirm` também em `inputSchema.required` | **31 (100 %)** |
| Ferramentas com `destructiveHint: true` | **20** |
| Destrutivas **sem** `confirm` | **0** |
| Ferramentas com `readOnlyHint: true` | **14** — e **nenhuma** delas tem `confirm` |
| `idempotentHint: true` | 20 · `openWorldHint: true` | **0** (todas `false`) |

A definição da propriedade, literal do arquivo:

> `"confirm": { "const": true, "description": "Set true only when the user's request or approval authorizes
> this specific change. Existing authorization need not be requested again.", "type": "boolean" }`

Três decisões embutidas nisto, todas diferentes do que se vê em MCPs por aí:

1. a autorização é **`const: true` num schema JSON** — não uma convenção de prompt, não uma checagem no
   servidor. Uma chamada sem `confirm: true` é *malformada*, então o modelo precisa produzir o token de
   autorização como parte do argumento;
2. a frase "Existing authorization need not be requested again" trata do pior efeito colateral de gates
   assim (perguntar a mesma coisa 12 vezes numa tarefa); eles a escreveram no schema, onde o modelo lê;
3. os 11 itens da diferença (31 − 20) mostram que a régua **não é** "é destrutiva?" e sim "muda alguma
   coisa?": ferramentas não-destrutivas que alteram estado também exigem o token, e as 14 de leitura não
   exigem nada. É a mesma forma da nossa `cross-project/security/PER-EXECUTION-PERMISSIONS.md`, com
   implementação.

## 3. Escopo no login, não na ferramenta

As linhas 16–23 do `SKILL.md` (lidas):

> "Which tools you see depends on what the user allowed at sign-in. Reading needs `read`. … sharing forms
> need `write`. Editing or deleting other existing content (page names, icons and … replacement, any
> deletion) and revoking or rotating a form's sharing link need `admin`. If a … workspace or server
> administrator has to change that. **Do not retry in a loop.**"

Mais três regras do mesmo arquivo, na seção "Reading"/"Writing": paginação explícita com
`start_cursor`/`next_cursor`; concorrência otimizada — "pass them back as `expected_version` /
`expected_block_hash`, so an edit made by someone else in [the meantime is detected]"; "Every tool that
changes something requires `confirm: true`"; "Deleting (blocks, rows, properties, comments, reminders)
cannot be undone from here. **Confirm the exact items with the user, and name them in your confirmation
question**"; e "After a change, read back what matters and report it with the page's name".

É a escada completa em quatro degraus, e cada degrau tem um mecanismo diferente — o que vale para nós
mais do que qualquer uma das decisões isoladas:

| Degrau | Mecanismo | Onde mora |
|---|---|---|
| ver ou não uma ferramenta | escopo no consentimento de login (`read`/`write`/`admin`) | servidor OAuth |
| poder chamar uma ferramenta que escreve | `confirm` obrigatório no schema | o `tools.json` do catálogo deles |
| não corromper edição alheia | `expected_version` / `expected_block_hash` | entrada de cada ferramenta |
| não repetir a pergunta | frase sobre autorização existente + "Do not retry in a loop" | descrição e `SKILL.md` |
| conferir depois | "read back what matters and report it" | `SKILL.md` |

A comparação que a casa já tinha: o OpenProject, no mesmo mês, disse a mesma coisa em prosa no README do
pack de Skills ("Reads can run automatically… confirm intent before any write, then verify with a
follow-up inspect") — mas **sem** nada que impeça a chamada. O `LR-FORGE-016` tem a política; o
`appflowy-ai-plugins` tem a política **e** o schema. O `openproject-agent-skills` tem ainda uma coisa que
aqui falta: `--dry-run` inexistente admitido como limitação, enquanto o AppFlowy tem o `confirm`.

## 4. `tools_integrity`: o catálogo declara o próprio hash

Do `tools.json` do catálogo:

> `"tools_integrity": { "algorithm": "sha-256", "digest": "d801992edde4b28e327e76568c864970d0e6b9836f3a9b480a997a3067b94db9", "tool_count": 45, "version": "25" }`

Repare no par `tool_count` + `digest`: o número de ferramentas está **dentro** do bloco verificado, então
"adicionei uma ferramenta e esqueci de atualizar o resto" quebra o hash. E o `version: "25"` é um contador
de revisão do catálogo, independente da versão do plugin (`plugin.json` → `0.2.0`) e da versão do pacote.

Duas outras coisas declaradas no mesmo repositório e verificáveis por mim:

- as **annotations** por ferramenta são geradas, não digitadas: `scripts/annotation-table.py` produz uma
  tabela de 48 linhas, e rodei duas vezes — **saída byte-idêntica**, `sha256 09133d787d55fcd8…`;
- os dois `marketplace.json` (`.claude-plugin/` e `.agents/plugins/`) carregam política de instalação
  explícita (`policy.installation: AVAILABLE`, `authentication: ON_INSTALL`), e os quatro `plugin.json`
  trazem `version: 0.2.0`, `license: AGPL-3.0-only` e URLs de privacidade/termos/suporte.

## 5. O que executei, e o que as duas notas significam

`python3 scripts/check.py` no clone raso, saída integral:

```
note: codex/appflowy-self-hosted points at the placeholder URL; run scripts/set-server-url.py <your AppFlowy URL> in your own copy
note: Claude Code is not installed; skipped claude plugin validate
ok
exit=0
```

Lido assim: o verificador **passa com notas** em vez de falhar, e as duas notas são exatamente as duas
coisas que um verificador decente não pode checar sozinho — (a) o `.mcp.json` self-hosted usa
`${user_config.server_url}` (placeholder, por design), enquanto a variante cloud aponta para uma URL `http`
fixa; (b) a validação específica do Claude Code depende do binário `claude` estar instalado. Um verificador
que distingue "ausência de ambiente" de "defeito" é um padrão que o nosso
`tools/validate.py` deveria copiar (ele hoje emite `aviso`/`nota`, na mesma direção — anoto o paralelismo,
não a mudança).

Registro a divergência material sobre a URL cloud, porque ela é o ponto em que este objeto **não** é um
modelo pronto: o README do repositório afirma que a URL do MCP cloud **ainda não está no ar**. Então a
variante `appflowy` (cloud) dos quatro plugins é um esqueleto funcional e não um serviço utilizável — nada
aqui deve ser lido como "o AppFlowy tem um MCP público".

## 6. `SUBMISSION.md`: o checklist de diretório que ninguém mais tem

O arquivo é uma checklist campo-a-campo de submissão a diretório de plugins, e cita os dois documentos
que mandam de verdade: a política de diretório de software da Anthropic — incluindo a reavaliação quando
há "material endpoint change" (a regra das 3 horas para re-revisão) — e a orientação da OpenAI de que
**mudar a URL de um servidor MCP existente exige falar com o suporte, e uma origem nova implica um plugin
novo**. Traduzido para a nossa casa: o endpoint é parte da identidade do artefato, tanto quanto a versão.
Nenhum dos 34 objetos anteriores desta base tinha evidência disso; a `agents/PUBLISHING-PROTOCOL.md` da Lia
não cobre troca de endpoint. É a única sugestão deste documento que é *política desta casa*, não do
produto.

## 7. Mapa para os cinco projetos

| Destino | O que levar | Seção |
|---|---|---|
| `lia-security-review` (lacuna `❌`) e `cross-project/security/PER-EXECUTION-PERMISSIONS.md` | `confirm` como `const: true` no `inputSchema` + obrigatório em `required`; escopo read/write/admin no consentimento | §2, §3 |
| Lia Agent Hub | `tools_integrity` (digest com contagem dentro) e annotations por tabela gerada determinística | §4 |
| Lia Project | as regras de comportamento: paginação explícita, read-back depois da escrita, "não retente em loop", nomear itens na pergunta de confirmação | §3 |
| Lia Forge | dois `marketplace.json` com política de instalação + `plugin.json` com `license:` e URLs legais por variante cloud/self-hosted | §4 |
| `agents/PUBLISHING-PROTOCOL.md` | §6 — a origem como parte da identidade publicável | §6 |
| Lia Model Lab | nada | — |

## 8. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Rodar um dos plugins contra um AppFlowy self-hosted real | `BLOCKED` | exige servidor AppFlowy (sem Docker aqui) e instância autenticada; nada foi instalado |
| Se o `marketplace.json` é aceito de fato pela loja | `NOT_RUN` | exige submissão — fora do escopo e da autoridade da Research |
| Que o servidor *obedece* ao `confirm` (e não só o schema) | `UNVALIDATED` | li o manifesto, não a implementação do servidor; sem código de handler no repositório |
| Os 37 arquivos, fora dos que abri (handlers, `scripts/set-server-url.py`) | `NOT_RUN` | leitura seletiva; o que cito foi o que li |
| Quais exatamente são as 14 de leitura, as 20 destrutivas e as 11 intermediárias | `CONFIRMED` (contagens) / `NOT_RUN` (classificação individual transcrita) | a tabela de 48 linhas do `annotation-table.py` existe no repo; não foi colada aqui por tamanho |
| Estado da URL cloud | `REPORTED` | só o README deles afirma; nenhuma chamada de rede foi feita |
| Comportamento do `claude plugin validate` | `NOT_RUN` | binário ausente no sandbox (o `check.py` avisou) |

## 9. Recomendação: **ADAPT** (proposta; nada foi implementado)

1. **Adaptar o `confirm` no schema** para qualquer MCP/skill que a Lia publique e que altere estado —
   `const: true` em `required`, com a frase anti-pergunta-repetida na descrição. Custo: editar o catálogo
   de ferramentas; não há dependência nova.
2. **Adaptar o `tools_integrity`** ao `catalog/catalog.tsv` desta casa: um bloco com `algorithm`,
   `digest` e `tool_count`/`row_count`, checado no `tools/validate.py`. Isso resolve um risco que já
   existe aqui: catálogo e índice divergirem sem ninguém perceber (o `check_counts` cobre README/índice,
   não o conteúdo do TSV).
3. **Adaptar a fraseologia do §3** ("name them in your confirmation question", "read back what matters")
   na política de execução da casa, em `cross-project/security/PER-EXECUTION-PERMISSIONS.md` — as seis
   linhas de evidência que já estão lá ganham um precedente com implementação.
4. **Registrar em `agents/PUBLISHING-PROTOCOL.md`** a regra da §6 (endpoint novo = artefato novo) *como
   questão para o dono*, já que hoje o arquivo não trata de mudança de origem.
5. **Não adotar**: o AppFlowy como plataforma, nem as 45 ferramentas; o objeto vale pelo desenho, e o
   próprio upstream diz que a parte cloud não está no ar.

## 10. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| 45 ferramentas; 31 com `confirm` em `properties` e as 31 com `confirm` em `required`; 20 destrutivas (todas cobertas); 14 readOnly (nenhuma com `confirm`); `openWorldHint` verdadeiro em 0 | `CONFIRMED` | script próprio sobre o `tools.json` do catálogo, no clone `318a8c8` |
| `confirm` é `{"type":"boolean","const":true}` com a descrição transcrita | `CONFIRMED` | item do `inputSchema` impresso |
| `tools_integrity` = sha-256, digest `d801992e…b94db9`, `tool_count 45`, `version "25"` | `CONFIRMED` | mesmo arquivo |
| Escopo `read`/`write`/`admin` decidido no sign-in; `expected_version`/`expected_block_hash`; "Do not retry in a loop"; read-back | `CONFIRMED` | `SKILL.md` das variantes (linhas 16–52 lidas) |
| `scripts/check.py` → duas notas + `ok`, exit 0 | `OBSERVED` | executado no sandbox (Python 3.11.2) |
| `scripts/annotation-table.py` determinístico: duas execuções, saída idêntica, 48 linhas, `sha256 09133d787d55fcd8…` | `OBSERVED` | executado duas vezes, saída comparada |
| 4 plugins (claude/codex × cloud/self-hosted), 2 `marketplace.json` com `installation: AVAILABLE` e `authentication: ON_INSTALL`, `plugin.json` `0.2.0` + `license: AGPL-3.0-only` | `CONFIRMED` | `find` da árvore + arquivos lidos |
| Repositório: 1★ · 1 fork · Python · AGPL-3.0-only · push 2026-11-05 · 37 arquivos · 849 KB | `CONFIRMED` | `gh api repos/AppFlowy-IO/appflowy-ai-plugins` + `du` no clone |
| `SUBMISSION.md` cita a política de diretório da Anthropic (re-revisão por mudança material de endpoint) e a orientação da OpenAI (URL nova ⇒ plugin novo) | `CONFIRMED` (texto) | arquivo lido no clone |
| O servidor aplica `confirm` de verdade; a URL cloud funciona | `UNVALIDATED` | nada foi chamado; o README diz que ainda não está no ar (`REPORTED`) |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 3) · inventário do org: `repositories/appflowy-io/REPORT.md` ·
política desta casa que este objeto corrobora: `cross-project/security/PER-EXECUTION-PERMISSIONS.md` ·
registrador de Skills: `agents/SKILLS-OPERATING-SET.md` · protocolo de publicação a emendar:
`agents/PUBLISHING-PROTOCOL.md` · registro de execução: `data/testing/test-log.tsv` (linha `LR-MCP-004`).
