# Charakuru — o repositório é só documentação: o kit está num ZIP cuja licença cobra por faturamento, e a política de navegador do agente não existe em inglês

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-020` |
| Nome | `nanocle/Charakuru` (きゃらくる) — kit de modelagem de personagem: uma ilustração → avatar VRM 1.0, com app local + 9 Skills para agente |
| Tipo | repositório (app distribuído por release, não por Git) |
| Fonte oficial | https://github.com/nanocle/Charakuru · sem site próprio (`homepage: null`) · Discord do patrocinador Tripo |
| Responsável | Nano (`nanocle`), autor único dos 10 commits públicos; licença em nome de "Chara Kit contributors"; patrocínio Tripo (a empresa **não** é a licenciante — §1 do LICENSE diz isso expressamente) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED |
| Recomendação | **REFERENCE_ONLY** — sugestão ao dono: reaproveitar o *padrão* de checkpoint (app emite o pedido, agente nunca avança sozinho), a escada de reuso de navegador sem fallback silencioso, e o par "hash do asset publicado via API, sem download"; o texto das Skills não é copiável |
| Decisão de adoção | — nenhuma registrada |
| Categoria | pipeline de avatar + engenharia de Skills + licença source-available com limiar financeiro |
| Projetos beneficiados | Lia Studio (empacotamento de Skills, aviso de terceiros), Lia Agent Hub (frontmatter e termos por Skill), Lia Forge (política de release e de tradução), qualquer app que controle navegador/sessão em nome do usuário |
| Versão analisada | `main` = `8eb22f6` (2026-10-23) · release mais recente `v1.1.1` (publicada 2026-11-02) · criado em 2026-10-06 |
| Proveniência do conteúdo | **medido por nós** (`gh api` + `git clone` + leitura integral do LICENSE e dos 24 `.md`) mais o que o README deles afirma — o que é afirmação deles está marcado no texto; nada veio de blog post |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api repos/nanocle/Charakuru` + `git/trees/HEAD?recursive=1` (`truncated: false`, 106 entradas) + `releases` (8) + clone completo |
| Upstream conferido | 1792 ★ · 150 forks · 5 issues abertas · 10 watchers · `size` da API = 9.444 KB (a árvore inteira somada dá 3,4 MB, quase tudo imagem) |
| Próxima revisão | 2027-02-25 (o kit muda por release, não por tag de código — conferir `releases` antes de qualquer citação) |
| Licença | **`Charakuru Source-Available License and Terms of Use`, versão 1.2, 2026-10-07** — licença própria, 287 linhas, 11 seções; a API reporta `NOASSERTION` porque não reconhece o arquivo; "not an OSI-approved open-source license and not the MIT License" (texto do próprio arquivo) |
| Confiança | Alta no que está no repositório (tudo lido por mim, com contagens); **baixa quanto ao comportamento do kit** — o código das Skills não está na árvore pública e o ZIP não é alcançável deste sandbox |

---

## 1. Por que este objeto entrou, e por que saiu em par com o HairDeck

O dono mandou os dois links na mesma mensagem. São **concorrentes no resultado** (ilustração → avatar
VRM pronto para animar) e **opostos em tudo o mais**: um distribui o artefato por release ZIP com licença
propória e não aceita PR; o outro é código de artigo, Apache-2.0, sem release alguma. Foi essa
complementaridade — e não o domínio em comum — que decidiu o formato: dois dossiês que se citam, em vez
um digest único, porque a parte útil de cada um é justamente a que falta no outro.

Não havia registro anterior dos dois na base (`grep` no `RESEARCH-INDEX.md` e no catálogo: zero
ocorrências de `Charakuru`).

## 2. O que o repositório contém (medido na árvore, não no marketing)

| Grandeza | Medido |
|---|---|
| Entradas na árvore de `main` | 106, `truncated: false` |
| Arquivos `.md` | 24 (README em 4 idiomas + 20 documentos em `docs/`) |
| Código-fonte | **zero** — nenhum `.py`, `.mjs`, `.js`, `.json`, `package.json` na árvore |
| `public/` | só 5 arquivos, todos de licença: `vendor/THREE-LICENSE.txt`, `vendor/FFLATE-LICENSE.txt`, `vendor/three-vrm-LICENSE.txt`, `vendor/three-vrm-animation-LICENSE.txt`, `fonts/Orbitron-OFL.txt` — **os `.js` vendorizados não estão no repositório**, apenas suas licenças |
| Imagens | 51 `.jpg` + 4 `.png` + 6 `.svg`; o maior blob é o `docs/images/readme-hero.png` de 1.823.903 B |
| `.github/` | 4 templates de issue (`report.yml` 2.641 B, `report.ko.yml` 1.586 B, `report.zh-CN.yml` 1.857 B, `config.yml` 338 B) — **nenhum workflow** |
| Histórico | 10 commits, um autor, 2026-10-04 → 2026-10-23 |

O que o README descreve como o kit (`AGENTS.md` na raiz, `skills/` com nove Skills, `server.mjs`,
`scripts/`, `assets/donor/weighted-body.blend`) **não existe na árvore pública**. O próprio README avisa,
e a frase é exata: *"GitHub's automatic 'Source code' archive contains only these documents, not the
kit."* Verifiquei as três afirmações estruturais (ausência de código, ausência de `AGENTS.md`,
ausência de `skills/`) contra a árvore completa, não contra o texto.

## 3. Consequência metodológica: a árvore pública não ancora o artefato

- Última release: **`v1.1.1`**, publicada 2026-11-02, com três assets:
  `charakuru-1.1.1-2026-11-02T09-36-05-842Z.zip` (12.024.159 B),
  `charakuru-1.1.1-technical-notes.en.md` (19.744 B) e
  `charakuru-1.1.1-update-guide.en.md` (16.285 B).
- Último commit público: **2026-10-23** — ou seja, **não há commit correspondente ao `v1.1.1`**. A frase
  do `README` que manda "abra o repositório com um coding agent e aprenda o kit por ele" não pode se
  sustentar: o que está no Git é a documentação da versão anterior.
- O badge do README diz `version-1.1.0` e o passo 1 do "Getting started" manda baixar
  `charakuru-1.1.0-….zip`, um release atrás do publicado. **Não é engano de escrita**: o README foi
  atualizado em 2026-10-23 (para o v1.1.0) e o v1.1.1 saiu dois dias depois do último commit — a
  vitrine e a árvore têm cadências diferentes por construção.

O que importa para a nossa base: **número de versão em README não é âncora aqui**. A âncora honesta é o
asset. E o hash do asset está acessível sem baixá-lo — ver §4.

## 4. O que descobri sobre o GitHub e já vale para esta base: `digest` no asset de release

`gh api repos/<dono>/<repo>/releases` traz, em cada asset, o campo **`digest`** com o SHA-256
computado pelo próprio GitHub. Para o ZIP do Charakuru:

```
sha256:130efef11e087263729842b5523e67d660b33d160e8c118df1c96a9ce50faf3d
```

medido sem nenhum download, por uma API que este sandbox alcança. Consequência direta: a pendência que
a base tinha sobre o `mr-mak` (hash do `.zip` publicado impossível de conferir porque o download escapa
da allowlist) **não era bloqueio de informação, era bloqueio de rota** — e eu usei exatamente esta
descoberta para fechar `DR-0004` nesta mesma rodada (ver `repositories/mr-mak-workspace/REPORT.md` §14
e a seção de registro desta). Limitação mantida: o `digest` prova *qual* arquivo o GitHub serve, não
o que há dentro dele.

## 5. A licença, lida inteira (287 linhas) — e por que ela é o melhor objeto da leva

Não é um texto de duas páginas. É um instrumento contábil. As regras que interessam a qualquer decisão
de uso:

| Seção | O que fixa |
|---|---|
| §1 | "Covered Materials" = código, scripts, **Skills (incluindo suas instruções e texto de referência)** e documentação. Os ativos do kit ficam fora, em regime próprio (§8) |
| §1 | "Revenue" e "Funding" com definição de exercício social, o que entra, o que não entra, agrupamento de entidades sob controle comum e cláusula anti-fração: "Splitting a business into projects or controlled entities does not create separate free allowances" |
| §1 | limiar **JPY 100.000.000**; "Revenue and Funding are tested separately, not added together: reaching either threshold is sufficient" |
| §2 | uso gratuito se (a) pessoal, fora de Business Use, **ou** (b) ambos abaixo do limiar — inclui "use with AI agents and Blender" e operar serviço hospedado em infraestrutura sua |
| §2 | mas: "Making Kit code available to customers, **including delivering the application to their browsers**, is redistribution" — o caso exato de um app web self-hosted |
| §4 | fork no GitHub, issues, patches e PRs são sempre permitidos, sem olhar faturamento; e o fork **não** autoriza publicar pacote, download ou app hospedado a partir dele, "including through GitHub Releases or GitHub Pages" |
| §5 | "This License does not claim ownership of general ideas, techniques, workflows, or independently written implementations" — **o padrão é reimplementável; a expressão não é copiável** |
| §6 | Outputs (modelos, texturas, animações, dados de projeto) sem royalty, sem atribuição obrigatória, sem restrição de redistribuição por terem sido feitos com o kit |
| §8 | ativo doador com pesos: carregável e modificável **localmente** só para ajuste e transferência de pesos; proibido tirar do kit |
| §9 | 30 dias para curar quebre; reincidência do mesmo tipo não cura automaticamente |
| §10 | o disclaimer de garantia **nomeia as Skills**: "SKILLS AND AI-ASSISTED WORKFLOWS MAY BE EXPERIMENTAL AND MAY REQUIRE MANUAL CORRECTION" |
| §11 | inglês autoritativo; as explicações em outros idiomas "não adicionam nem removem permissão"; contato comercial é um Gmail pessoal (`divedesign.info@gmail.com`) |

Duas coisas raras aqui, e são elas que fazem o objeto valer a visita: é a **primeira licença medida nesta
base que trata instrução de agente como material licenciado**, e a primeira cujo teste de elegibilidade
é **quantitativo e do lado do usuário**, não do lado do artefato (nada no ZIP muda se você fatura 10 mi
ou 200 mi; muda o que você pode fazer com ele). Isso muda o vocabulário da auditoria de dependência: "que
licença tem este pacote?" é insuficiente; precisa de "qual é o meu próprio número, e quando ele é
reavaliado?"

## 6. O protocolo de checkpoint (a capacidade transferível mais clara)

O app local é uma máquina de estados com cinco pontos de decisão humanos: importar a ilustração → revisar
as 8 imagens → escolher candidatos 3D → ajustar proporção → revisar movimento. A troca com o agente é:

1. o app mostra um botão *continue* que **copia um pedido pronto**;
2. o usuário cola no chat e envia;
3. o agente trabalha e o app reabre sozinho no novo estado e **para no próximo checkpoint**.

Regras que o README enuncia e que não dependem de VRM nenhuma: "The agent never moves past a checkpoint
on your own, and you are the one who picks the candidates"; "no exporting, importing or re-saving files by
hand"; e o pedido vencido — se o usuário recarregar o tab, o pedido antigo **não** deve ser usado, é para
copiar um novo. O comando de abertura é `agent-session.mjs begin`, e o motivo é um caso real de política
de execução: o Codex no Windows confundia o argumento `start` com uma URL e bloqueava; a solução foi um
verbo próprio, documentado com passo de recuperação (`docs/tutorial.md` tem a seção).

O ponto para nós: o gate de aprovação está **no estado do app**, não na boa vontade do modelo. É a mesma
direção que `LR-MCP-004` mediu no `appflowy-ai-plugins` (`"confirm": {"const": true}` em 31 das 45 tools
e dentro de `required`), mas aqui com uma diferença: o pedido tem validade, e o app é o que sabe disso.

## 7. A escada de navegador — e o fato de que ela não existe em inglês

`docs/browser-use.md` é uma política de cinco degraus para o agente que precisa de navegador:

1. usar o browser/aba que o usuário indicou; senão, inspecionar o que já está aberto e preferir o browser
   logado no serviço ou já mostrando o app;
2. se a aba do alvo existe, **usar aquela** — sem abrir outra do mesmo app, sem recarregar "para operar";
3. se não existe, adicionar aba **no mesmo window/profile**; nunca substituir conteúdo de aba do usuário;
4. abrir um browser novo **somente depois de confirmar que nenhum está aberto**, sem criar profile de
   automação nem browser headless "para o trabalho";
5. **se a conexão falhar, isso não autoriza concluir que "não há browser aberto"**, nem migrar
   sozinha para o browser embutido do Codex — que tem estado diferente do browser normal do usuário.

O degrau 5 é o que vale fora do domínio: **falha de conexão com um contexto existente não é licença para
trocar de contexto silenciosamente**. É o análogo, no lado do agente, do "sem fallback mudo" que a base
já trata em permissão por execução.

Medida de cobertura que ninguém anunciou: esse arquivo, que pela convenção do repositório seria o
`<nome>.md` em inglês (README, `docs/license.md`, `docs/getting-started.md`, `docs/tutorial.md` seguem essa
convenção), tem **664 caracteres kana e 110 latinos** — é japonês, e não existe `browser-use.ja.md`. O que
existe em inglês é só o `README`; a política de navegador do agente está em JA/KO/zh-CN e **nunca em
inglês**. `docs/preview-user.md` idem, ao contrário: as três traduções existem (`.ja`, `.ko`, `.zh-CN`) e
o arquivo em inglês não existe. `docs/expression-authoring.ja.md` só existe em japonês, e é para lá que o
README em inglês aponta. `docs/getting-started.ko.md` não existe e o link coreano do arquivo de
getting-started aponta para `tutorial.ko.md` — alvo válido, conteúdo trocado.

## 8. Tradução × alegação de licença (medido por padrão, não por impressão)

| Arquivo | limiar ¥100 mi | "qualquer um dos dois basta" | período de exercício | "não anualizar" | reavaliar financiamento | "acordo escrito" |
|---|---|---|---|---|---|---|
| `README.md` (EN) | SIM | SIM | SIM | SIM | SIM | SIM |
| `README.ja.md` | SIM | SIM | SIM | SIM | SIM | SIM |
| `README.ko.md` | SIM | **não encontrado** | SIM | **não encontrado** | SIM | SIM |
| `README.zh-CN.md` | SIM | SIM | SIM | SIM | SIM | SIM |
| `docs/license.md` (EN) | SIM | — | — | — | — | — |
| `docs/license.ja.md` | SIM | — | — | — | SIM | — |
| `docs/license.ko.md` | SIM | — | SIM | — | SIM | SIM |
| `docs/license.zh-CN.md` | SIM | SIM | SIM | SIM | SIM | SIM |

Leitura honesta da tabela: as **explicações** em inglês e japonês (848 e 920 bytes) dizem "ambos abaixo de
¥100 mi" e param aí; as versões coreana e chinesa (1.712 e 1.778 bytes) acrescentam a regra de contagem —
exercício social, janela de 12 meses, proibição de anualizar, reavaliação no recebimento. Quem decidir
uso comercial pela página "explicada" no seu idioma tem menos instrução do que quem a lê em chinês, ainda
que o LICENSE (287 linhas, que tem tudo isso) seja o texto autoritativo e esteja a um clique.

Registro do meu erro de método, porque ele quase virou conclusão: minha primeira varredura buscava
`1 億` (com espaço) e `1亿`; o japonês real é `1億円` sem espaço. Eu ia escrever que "as traduções JA e
zh omitem o limiar" — **omitem nada**: os quatro READMEs e os quatro `docs/license.*` declaram o número.
Refiz a contagem com um padrão por idioma e a tabela acima é o resultado.

## 9. Governança do projeto, medida

`CONTRIBUTING.md`: **"Pull requests are not accepted."** Desenvolvimento e registro de verificação ficam
privados ("Development history and internal verification records remain in private development"). O
template de issue para problema de Skill pede **o agente/modelo usado e a etapa em que falhou** — e proíbe
anexar conversa inteira, credenciais, caminhos pessoais e material não público. Quatro idiomas de
template. Zero workflow de CI (as 4 entradas de `.github/` são templates de issue).

Sinal, não sentença: é o desenho inverso do `open-seo` (`LR-FORGE-017`, que aceita PR, roda 2.130 testes
na CI e mesmo assim publica sem crédito em parte do histórico) — aqui nada é automatizado no GitHub
porque quase nada está no GitHub. A superfície de auditoria externa é a documentação; o artefato é caixa
preta para quem não abre o ZIP.

## 10. O que rodei aqui e o que não pude rodar

Executado neste sandbox (medição própria, sem instalar nada):

- `gh api repos/…/git/trees/HEAD?recursive=1` → 106 entradas, `truncated: false`; censo por extensão e
  diretório; `public/` listado arquivo por arquivo.
- `gh api repos/…/releases` → 8 releases, 12 assets, tamanho e `digest` de cada um; contagem de
  downloads do ZIP do `v1.1.1`: **7.447**.
- `git clone` completo → 10 commits, 1 autor, datas acima.
- Verificação de integridade de link relativo nos 24 `.md`: **176 links**, 63 externos, **113 internos,
  0 quebrados** (script próprio, mesma checagem que o `tools/validate.py` desta base faz).
- Leitura integral de `LICENSE` (287 linhas), `THIRD_PARTY_NOTICES.md`, `CONTRIBUTING.md`,
  `docs/browser-use.md`, `docs/getting-started.md`, `docs/license.md` e `.ja`/`.ko`/`.zh-CN` de license.
- Verificação das cinco notas de terceiros: MIT (Arjun Barrett 2023, `fflate`), MIT (`three.js authors`),
  MIT × 2 (pixiv, `three-vrm` e `three-vrm-animation`), SIL OFL 1.1 (`Orbitron`) — **todas as cinco
  conferem com o texto citado**. O §8 do LICENSE nomeia só duas (Three.js e Orbitron) e delega as demais
  em "Other identified third-party licenses also prevail"; a tabela de `THIRD_PARTY_NOTICES.md` lista as
  cinco. Divergência de enumeração entre os dois arquivos, não de substância.

Não executável aqui, com a limitação medida (é `BLOCKED`, não `NOT_RUN`):

- baixar o ZIP para inspecionar `AGENTS.md`, as nove Skills e o `server.mjs`: `curl` do asset devolve
  `302` para `release-assets.githubusercontent.com` e morre em `SSL_ERROR_SYSCALL`, **0 bytes
  recebidos** — o mesmo host bloqueado que já travava o `mr-mak`. Os `.md` de 19 KB e 16 KB da mesma
  release estão no mesmo host: mesmo resultado.
- rodar o app ou qualquer Skill: exigiria Node 22 (há: `v22.22.3`), navegador desktop, conta Tripo e
  Blender 5.2 — três dos quatro fora do que a base pode fazer sem criar conta, pagar ou instalar.

## 11. Onde isto poderia se aplicar (a viabilidade é do dono)

> **Escopo desta seção** — isto é sugestão a partir do que a evidência sustenta, mais a pergunta de
> viabilidade de cada app. Não é instrução para nenhum app, e nada aqui foi aplicado fora desta base
> (`MISSION.md` §3: o Research não aprova nada; `DR-0019` §5).

| App | O que sugiro considerar | O que custaria no app |
|---|---|---|
| Research (esta base) | usar `digest` de asset de release como âncora de proveniência onde o download é bloqueado; adicionar coluna de `first` × `warm` ao `data/testing/test-log.tsv` | zero código: é uma linha a mais por registro; a checagem já foi feita nesta rodada |
| Lia Studio | separar "documentação pública" de "artefato distribuído" na hora de citar um projeto de terceiros — aqui a versão do README não corresponde a nenhuma versão do app | só disciplina de citação: âncora = tag do release + hash do asset |
| qualquer app que controle navegador | os cinco degraus do §7, em especial o 5 (falha de conexão ≠ trocar de contexto) | precisa decidir o que é "contexto existente" no seu runtime; o resto é política escrita, não código |
| Lia Agent Hub | tratar texto de Skill como material licenciável, com termos próprios — o Charakuru faz isso e o §5 diz até onde vai | depende de quem detém os direitos das Skills do Hub; é pergunta, não tarefa |

## 12. O que não verifiquei, e por quê

- **Não li uma linha do kit.** As nove Skills, o `AGENTS.md`, o `server.mjs` e o `project.charakit` estão
  só no ZIP, inacessível daqui (§10). Toda afirmação sobre como as Skills são escritas é DOCUMENTED, não
  observada.
- Não abri o `docs/tutorial.md` (17.784 B) nem o `.ja` (21.868 B) por inteiro — usei para checar a
  existência da seção de recuperação do `begin`; o resto do tutorial não foi lido, e é nele que estão os
  detalhes operacionais que o README promete.
- Não verifiquei se os termos do **Tripo** ou do **Blender MCP** permitem o que o fluxo deles faz
  (login do usuário operado por agente). Serviços de terceiros, contas próprias; nada disso está no
  repositório.
- Não sei quanto custa o Tripo nem o que o patrocínio implica na prática; o README não diz preço e eu não
  fui ao site.
- O `docs/images/` não foi comparado com o texto (não verifiquei se os prints correspondem ao `v1.1.1`).
- Não contei contributors além do autor (API de contributors com `-i` não traz paginação aqui; é a mesma
  limitação medida na leva anterior: `gh api -i` não devolve o cabeçalho `Link`, e sem ele não há contagem
  de contribuidores).

## 13. Recomendação: **REFERENCE_ONLY**

`REFERENCE_ONLY` por três motivos que se somam, e nenhum deles é "o projeto é ruim":

1. **não há fonte para auditar** o que ele faz de mais interessante — o comportamento está num artefato
   que a licença deles define como coberto e que eu não pude abrir;
2. **o que é copiável não precisa ser copiado**: o §5 renuncia a ideias, técnicas, workflows e
   implementações independentes, então o valor (checkpoint com pedido válido, escada de navegador,
   elegibilidade quantitativa) entra como *padrão reimplementado por nós*, e não como transporte de código
   ou de texto de Skill;
3. o transporte de texto seria justamente o que a licença proíbe (redistribuição, extração de ativos), e
   a nossa base tem política de "todo registro de terceiros com licença lida" — aqui a licença lida diz
   "não".

**Propor** ao dono, sem aplicar: (i) fixar no protocolo que citação de projeto distribuído por release usa
tag + `digest` do asset, com `BLOCKED` explícito quando o asset não é alcançável; (ii) levar a escada de
navegador do §7 como rascunho de política para qualquer app Lia que controle navegador; (iii) se algum dia
houver interesse comercial no kit, a pergunta a fazer não é "que licença é", é "em que faixa de faturamento
o uso se enquadra e quando isso é reavaliado".

## 14. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| O repositório contém só documentação (0 arquivos de código) | `OBSERVED` | `git/trees/HEAD?recursive=1` com `truncated: false` + censo por extensão no clone |
| 9 Skills / `AGENTS.md` / `server.mjs` descritos no README e ausentes da árvore | `DOCUMENTED` (existência do artefato: `UNVALIDATED`) | README × árvore; o artefato está fora do alcance da allowlist |
| Licença = source-available v1.2, 287 linhas, limiar JPY 100 mi, Skills cobertas, §5 não reivindica workflow | `OBSERVED` (texto lido) | `LICENSE` inteiro lido no clone; §8 conferido contra os 5 arquivos de licença |
| ZIP do v1.1.1 = 12.024.159 B, sha256 `130efef1…faf3d`, 7.447 downloads | `OBSERVED` | `gh api repos/nanocle/Charakuru/releases/latest` campo `digest` e `size` |
| Conteúdo do ZIP | `BLOCKED` | `curl` → `302` para `release-assets.githubusercontent.com`, `SSL_ERROR_SYSCALL`, 0 bytes |
| `docs/browser-use.md` é japonês; não há versão EN nem `.ja` separado | `OBSERVED` | contagem de kana (664) × latinos (110) no corpo sem código; ausência confirmada na árvore |
| EN e JA das "explicações de licença" omitem a regra contábil que KO e zh têm | `OBSERVED` | tabela de §8, por padrão de busca por idioma, com o falso negativo do primeiro grep registrado |
| 113 links internos, 0 quebrados | `OBSERVED` | script próprio de checagem de link relativo nos 24 `.md` |
| PRs não aceitos; sem CI | `OBSERVED` | `CONTRIBUTING.md` lido; `.github/` contém só `ISSUE_TEMPLATE/` |
| Comportamento do app, qualidade das Skills, custo Tripo | `NOT_RUN` | dá para medir (abrir o ZIP, rodar o app) — não é bloqueio de ferramenta, é escolha de escopo: exige conta e instalação; vira `DR` pendente se o dono quiser |
