# Três buscas de paisagem que não renderam candidato: `github.com/skills`, org `waifuai`, topic `stt-tts`

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-013` |
| Nome | Paisagem negativa: GitHub Skills (org) · waifuai (org) · topic `stt-tts` |
| Tipo | repositorio |
| Escopo | **três listagens de terceiros consolidadas em um único objeto** (justificativa no §1) |
| Responsável | GitHub Inc. (org `skills`) · `waifuai` (org pessoal) · comunidade que marca o topic |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN |
| Recomendação | **REFERENCE_ONLY** |
| Decisão de adoção | — nenhuma registrada |
| Categoria | agents (leitura transversal em voice, security) |
| Projetos beneficiados | Lia Agent Hub (formato de catálogo), Lia Research (política de listagem), Lia-Project (voz) |
| Fonte oficial | https://github.com/skills · https://github.com/orgs/waifuai · https://github.com/topics/stt-tts |
| Versão analisada | instantâneo de 2026-11-22 pela API do GitHub; sem pin de commit — são listagens, não artefatos |
| SHA completo | — não aplicável: nenhum código de terceiro foi baixado nem executado neste objeto |
| Proveniência do SHA | **NA_APLICAVEL** — objeto de listagem; o registro é o instantâneo da API com data |
| HEAD atual | não aplicável |
| Data | 2026-11-22 |
| Última verificação | 2026-11-22 |
| Upstream conferido | 2026-11-22 · três leituras de API no mesmo ciclo · nada a comparar por commit |
| Próxima revisão | 2027-05-22 (prazo longo: os três são ruído, não sinal vivo) |
| Licença | **majoritariamente ausente**: 20 de 20 repositórios lidos da org `skills` e 52 de 52 da org `waifuai` com `licenseInfo: NONE`; topic `stt-tts` com 3 de 11 sem licença |
| Confiança | Alta para as contagens (API); nenhuma para qualidade de qualquer item (nada foi aberto individualmente) |

---

## 1. Por que este documento existe em vez de três relatórios

Três dos pedidos desta rodada eram **listagens**, não artefatos: uma URL de organização
(`github.com/skills`), outra organização (`github.com/waifuai`) e um topic (`topics/stt-tts`). O modo
de falha fácil — e o que a maior parte das "pesquisas de ecossistema" faz — é fabricar uma linha de
veredito por item listado. Este objeto toma a decisão contrária: **uma avaliação por listagem**, com os
itens registrados em bloco, porque o que a listagem prova é sobre a listagem.

E as três conclusões são negativas, o que é resultado:

| Busca | O que se esperava | O que é |
|---|---|---|
| `github.com/skills` | o registro de Agent Skills do GitHub | **organização de cursos** do GitHub Training, 53 repositórios de aula; **zero** `SKILL.md` na busca da organização |
| `waifuai` | ecossistema de assistente de voz/anime com MCP | 52 repositórios de widgets Live2D/VRM, sem licença em nenhum, ★ máximo 43 |
| `topics/stt-tts` | candidatos de voz para o Lia-Project | 11 repositórios no total, ★ máximo 12 — topic praticamente vazio |

Nas três: **nenhum objeto adotável**. Nenhuma decisão de adoção é registrada, e nada aqui altera a
lacuna `BLOCKED` de latência de voz do digest `LR-VOICE-001`.

## 2. `github.com/skills` — o equívoco de nome é o achado

Organização "GitHub Skills", criada 2022-04-15, 53 repositórios públicos, nenhum com licença declarada
(`licenseInfo: NONE` nos 20 lidos). É a plataforma de **cursos interativos** do GitHub (`for-the-score`,
`secure-code-game` ★2.861, `skill-checkers`, cursos de Copilot ★815 e ★263). Não há `SKILL.md`: a busca
de arquivo dentro da organização retorna zero.

O valor para a base está exatamente no choque de vocabulário. Em 2026 "skill" significa, em dois
ecossistemas diferentes e com grafia idêntica, coisas sem relação:

| Sentido | Unidade | Onde o Lia está |
|---|---|---|
| *Agent Skill* | pasta com `SKILL.md` + frontmatter + scripts, carregada por um host de agente | Hub (`agents/*.records.json`), `cross-project/agents/SKILLS-MCP-LANDSCAPE.md` |
| *GitHub Skill* | curso interativo com branches e checks | nenhum projeto Lia; é material didático |

Consequência prática: **qualquer busca por "skills" no GitHub precisa do qualificador
`filename:SKILL.md` ou `topic:agent-skills`**, senão o ruído é este. Registro porque é o tipo de falso
positivo que consome um ciclo inteiro sem produzir nada.

## 3. Org `waifuai` — 52 repositórios, uma ideia emprestável, nenhuma licença

Contagem da API: 52 repositórios, organização criada 2018-09-20, **52/52 `licenseInfo: NONE`**, ★
máximo **43**, a maioria com ★0–1. Amostras:

| Repositório | O que é |
|---|---|
| `waifu-companion` | overlay de navegador com avatar Live2D + chat de voz + memória de longo prazo |
| `waifu-llm-vrm` | ponte Python ↔ Godot: o LLM dirige um avatar VRM |
| `hermes-waifu` | widget Live2D para o agente Hermes |
| `mcp-waifu-chat` / `mcp-waifu-queue` | MCP + SQLite / MCP + Redis, mesma moldura |
| `waifu-constitution` | texto declarando "behavior, autonomy and agency boundaries" |
| `biochem-framework`, `ai-benchmarks`, `llms-full-txt` | três coisas sem relação entre si |

Duas leituras:

1. **o padrão "assistente com persona local via MCP" está maduro o bastante para ser banal** — é o
   mesmo par (avatar + fila/chat em MCP) replicado seis vezes, com SQLite × Redis como único detalhe
   arquitetural distinto;
2. **os `pushedAt` agrupados** (empurrões nos mesmos dias 2026-08-15 / 08-19 / 09-10, em repositórios de
   ★0–1) é sinal de atualização em massa, não de atividade independente — o padrão que o `LR-SEC-008`
   descreve como "estrelas sem história", aqui em versão benigna.

O único item com valor para o Lia é **`waifu-constitution` como formato**: um repositório inteiro cujo
produto é declarar limites de comportamento, autonomia e agência da persona. O Lia tem a `alethe` como
*conjunto* de Skills e nenhuma constituição separada — e constituição separada do mecanismo é o que
permite auditar um sem editar o outro. Registro como **padrão a discutir no Hub**, não como conteúdo a
importar (o texto deles é sobre avatar de anime, não sobre o assistente do Lia).

Licença: **sem arquivo de licença não há permissão de uso** — qualquer reutilização é
`REQUIRES_LEGAL_REVIEW`, e é por isso que "nada a adotar" aqui não é opinião estética, é consequência do
metadado ausente.

## 4. `github.com/topics/stt-tts` — topic com 11 repositórios e ★12 de teto

`total_count: 11` na API de busca por topic. Os itens acima de ★6:

| Repositório | ★ | Licença | O que é |
|---|---|---|---|
| `habitual69/voicr` | 12 | — | voz no terminal |
| `martinpercu/Odoo-AI-Agent` | 12 | — | agente de voz dentro do Odoo |
| `PerIPan/OpenWhisperer` | 9 | **MIT** | **modo de voz para CLIs de IA — STT Whisper local + TTS Pocket** |
| `KremlevLev/Rynne` | 8 | — | — |
| `europanite/client-side-speech-ai` | 7 | Apache-2.0 | Whisper rodando no navegador |
| +6 outros | ≤5 | variados | — |

Sinal útil, mesmo em escala pequena: **`OpenWhisperer` é o formato exato que o Lia-Project conversa
como hipótese** — STT e TTS plugados dentro de uma CLI de agente, local, MIT, ★9. Ele prova três coisas
de uma vez: (a) a ideia cabe em um projeto de uma pessoa; (b) não tem tração; (c) com ★9 e MIT, não há
suporte a manter. Isso **não** o torna candidato (`NOT_RUN`, nenhum código lido além da descrição), mas
barateia a decisão de o Lia fazer o próprio conector em vez de esperar por um ecossistema.

Contra-leitura obrigatória: topic pequeno pode ser **topic novo ou mal marcado**, não necessariamente
deserto. O mesmo tema, procurado por outros marcadores, tem o `KoljaB/realtimetts` (★4.059, objeto
`LR-VOICE-002` da mesma rodada) e dezenas de projetos — o topic composto `stt-tts` é que está vazio.
Registro como `CONFIRMED` para a listagem e `UNVERIFIED` para qualquer inferência de "não existe
demanda".

## 5. O que uma listagem prova e o que ela não prova

| Pergunta | A listagem responde? |
|---|---|
| "existe um padrão consolidado neste nicho?" | sim, se os itens repetem a mesma forma (é o caso de waifuai) |
| "há licença para reuso?" | **aqui a resposta é quase sempre não** — 20/20, 52/52, 3/11 sem licença |
| "o item X é bom?" | não — nenhuma lista responde isso, e foi por isso que nenhum item foi aberto |
| "há candidato de adoção?" | não, nas três buscas |

## 6. Padrão de método que este objeto deixa para a base

**URL de organização ou topic = um objeto de paisagem com contagem e veredito da lista; só se abre
relatório individual quando um item específico passa em triagem de licença + atividade.** É o inverso do
catálogo inflado, e é o motivo pelo qual esta base tem 30 relatórios em vez de 150. A regra tem
exceção documentada: se um item da lista apresentar sinal forte isolado (licença + estrelas +
atividade + formato raro), ele sobe para relatório próprio — foi o que se fez com `waifu-constitution`
ficando aqui (sem licença) e com `OpenWhisperer` ficando aqui (★9).

## 7. Recomendação

**`REFERENCE_ONLY`** — nada a adotar, nada a rastrear como dependência. Três conclusões acionáveis:

1. **qualificador de busca obrigatório** (`filename:SKILL.md` / `topic:agent-skills`) para o Hub e para
   esta base; "skills" sem qualificador devolve cursos;
2. **constituição separada do mecanismo** (`waifu-constitution`) como item de pauta no Hub, com
   ressalva de formato, não de conteúdo;
3. **`OpenWhisperer` registrado como evidência de custo baixo** para o conector de voz da CLI do
   Lia-Project — a decisão de construir não depende de achar um projeto para adotar.

Nenhum dos três justifica revisão antes de 2027-05-22. Gatilhos de reabertura: um item do topic
`stt-tts` passar de ★500 com licença; o GitHub Skills criar organização/anotação própria de Agent
Skills; qualquer repositório `waifuai` publicar licença e ter uso real documentado.

## 8. Limites desta leitura (o que este objeto deliberadamente não faz)

- **Nenhum repositório individual foi aberto.** As conclusões vêm de metadados de API (descrição,
  estrelas, licença, datas). Isso é triagem, não revisão de conteúdo — e está rotulado como tal.
- Nenhum item das três listas foi comparado com o próprio README, com releases ou com histórico de
  commits. A comparação que daria o próximo degrau de evidência (os cursos da org `skills` têm
  `SKILL.md` em branch de exercício?) não foi feita: **fora do escopo de uma triagem de listagem**.
- Peso da fonte: o campo `description` do GitHub é escrito pelo dono do repositório. Uma lista inteira
  com `licenseInfo: null` é metadado confiável; uma lista inteira com descrições autocongratulares, não.
- ★ contados em 2026-11-22 mudam rápido em contas pequenas; **nenhum número deste documento é base para
  decisão de produto** — ele serve para a decisão de *não* abrir mais 115 relatórios.
- A API de stargazers devolve `403` nesta autenticação, então **não há leitura da origem das estrelas**;
  em `LR-SEC-008` isso seria decisivo, aqui não muda o veredito.
- `waifuai` é tratada como bloco. Se algum dos 52 repositórios se tornar relevante, exige relatório
  próprio — a consolidação não é decisão sobre os itens, é decisão sobre o custo de registrar.

## 9. Evidências

| Afirmativa | Rótulo | Base (todas em 2026-11-22, UTC) |
|---|---|---|
| `github.com/skills` é org de cursos, 53 repositórios, zero `SKILL.md` | `CONFIRMED` | `users/skills` + lista de repositórios da org + busca de arquivo |
| 20/20 repositórios lidos da org `skills` sem licença | `CONFIRMED` | campo `licenseInfo: null` |
| org `waifuai`: 52 repositórios, 52/52 sem licença, ★ máximo 43, criada 2018-09-20 | `CONFIRMED` | `orgs/waifuai` + lista de repositórios |
| `pushedAt` agrupados em 2026-08-15 / 08-19 / 09-10 | `CONFIRMED` | campo `pushed_at` da lista |
| topic `stt-tts`: `total_count: 11`, ★ máximo 12 | `CONFIRMED` | API de busca por topic |
| `OpenWhisperer` = STT Whisper + TTS Pocket em CLI de IA, MIT | `CONFIRMED` (metadado) / `NOT_RUN` (código) | resultado da busca + descrição do repositório |
| conteúdo de qualquer um dos 115 repositórios citados | `UNVERIFIED` | nada foi aberto |
| origem das estrelas de `waifuai` | `BLOCKED` | API `stargazers` devolve 403 |
| "não há demanda por voz em CLI" | `REJECTED_INFERENCIA` | topic com 11 itens não mede demanda; ver §4 |

## 10. Próximos passos

1. Nenhuma execução pendente neste objeto — a triagem é o produto.
2. Se a discussão do conector de voz do Lia-Project avançar, usar `OpenWhisperer` como **piso de
   escopo** ("isso cabe em um conector"), não como dependência.
3. Revisar em 2027-05-22 apenas se houver um dos gatilhos do §7.

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · `cross-project/agents/SKILLS-MCP-LANDSCAPE.md` · `cross-project/voice/VOICE-STACK-DIGEST.md`.
