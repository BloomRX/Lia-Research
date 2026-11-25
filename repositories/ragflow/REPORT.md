# ragflow — o `AGENTS.md` que manda tratar código legado como passivo, e as 2 Skills que apontam para um arquivo de regras

| Campo | Valor |
|---|---|
| ID | `LR-RAG-001` |
| Nome | `infiniflow/ragflow` — motor de RAG baseado em compreensão profunda de documentos ("context engine", "agentic retrieval") |
| Tipo | repositório (produto open-core) |
| Fonte oficial | https://github.com/infiniflow/ragflow · https://ragflow.io |
| Responsável | `infiniflow` (org; autor principal `Zhichang Yu` em `pyproject.toml`) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN — nada instalado nem executado (o produto exige Elasticsearch/Infinity + modelos) |
| Recomendação | **REFERENCE_ONLY** — sugestão ao dono: guardar a política de legado do `AGENTS.md` (6 princípios, §3) como referência de texto; o motor não tem caso de uso medido na Lia |
| Decisão de adoção | — nenhuma registrada |
| Categoria | motor de RAG + disciplina de refatoração para agentes |
| Projetos beneficiados | Research (política de retratação em §3), Lia Forge (regra de superfície pública), Lia Agent Hub (as 2 Skills são o caso "Skill que só aponta para uma regra") |
| Versão analisada | `main` no HEAD de 2026-11-25 (`pushed_at 2026-11-25T13:09:35Z`) · criado 2023-12-12 |
| Proveniência do conteúdo | medido por nós: censo de árvore, leitura do `AGENTS.md` (171 linhas) e dos 2 `SKILL.md` |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api` + `git/trees/HEAD?recursive=1` (`truncated: false`) |
| Upstream conferido | **94.709 ★** · 11.403 forks · **1.303 issues abertas** · `language: Go` (3.549 `.go` na árvore — o núcleo migrou de Python para Go: 167 `.py` apenas) · 7.324 entradas / 6.587 blobs / 66,6 MB · **2 `SKILL.md`** · **3 caminhos `LICENSE`** · 4 workflows · 902 commits nos últimos 30 dias |
| Próxima revisão | 2026-12-09 |
| Licença | **Apache-2.0** — `LICENSE` raiz de **11.357 B**; os outros dois caminhos `LICENSE` são **código do produto** (`internal/dao/license.go`, `internal/entity/license.go`), não arquivos de licença |
| Confiança | Alta no que foi lido; zero quanto ao motor (não executado) |

---

## 1. Por que este link está aqui

Dentro da leva, o ragflow vale por três coisas específicas, e nenhuma delas é o motor de RAG: o `AGENTS.md`
de 171 linhas com a política de legado (§3), as 2 `SKILL.md` que não ensinam nada — só apontam para um
arquivo de regras (§4), e a descoberta contábil de que um `LICENSE` no censo pode ser **código do produto**
(§5).

## 2. Estrutura medida

7.324 entradas / 6.587 blobs / 66,6 MB. A composição por extensão é o dado: **3.549 `.go`** contra 167
`.py` e 1.069 `.tsx`. É um projeto que **reescreveu o núcleo em Go** mantendo `pyproject.toml` (nome
`ragflow`, autor `Zhichang Yu`) — a API `language: Go` é consequência disso. Para um dossiê, isso significa
uma coisa: qualquer afirmação do tipo "é um projeto Python de RAG" lida de README antigo está errada hoje. É
o argumento material para a coluna `Última verificação` existir nesta base.

## 3. O `AGENTS.md`: dívida como passivo, e o resto dos 6 princípios

Seção "Core Stance", na íntegra medida:

> - **Treat legacy code as liability, not as a compatibility target.**
> - Prefer **deletion over shims**, deprecated branches, wrapper APIs, and dual-track migration notes.
> - If old and new implementations coexist, **converge to one path** unless an external contract forces compatibility.
> - **Remove dead tests, commented-out code, stale docs**, and "move later" notes instead of preserving them.
> - **Reduce public surface area** when a helper can be made private or internal.
> - Keep refactors **centered on the owning abstraction**, not on adjacent compatibility layers.

E a frase de abertura do arquivo: *"Use this file as the local operating guide for the current codebase.
**Prefer the code and the current AGENTS.md over any older convention or remembered project shape.**"* — que
é, em uma linha, a regra que esta base aplica com `retificado em `+`` e com a seção "retrações": **a fonte é o
estado atual, não a nota anterior**. O `web/AGENTS.md` (204 linhas) repete a política para o front-end.

Não estou propondo importar "preferir deletar" como política da Lia — isto é material de decisão para o dono
do Forge, que é quem decide sobre compatibilidade.

## 4. Duas Skills que não contêm nada: `go-naming` e `react-doctor`

`.agents/skills/` (caminho neutro de runtime, como no goose):

| Skill | tamanho | o que o corpo faz |
|---|---|---|
| `go-naming` | ~200 B | uma linha: *"Strictly follow the naming conventions in `rules/named.md`"* — link relativo **dentro do repositório deles**; o conteúdo está em `.agents/rules/named.md` |
| `react-doctor` | ~8 KB | fluxo de varredura/triagem de diagnósticos React **que busca o playbook canônico**: *"fetches the canonical playbook"* — nem no repositório o texto final mora; e tem `version: "1.2.0"` |

É o **formato `E`** (pointer-skill) que o `SPLIT-LICENSE-SCAN.md` já distingue dos nossos 4 casos, com a
nuance que nos é própria: se o alvo de um pointer é buscado em runtime (`react-doctor`) ou lido de um
arquivo do próprio pacote (`go-naming`), o **custo de auditoria** muda de "um arquivo" para "uma URL
externa". Para o Hub, a pergunta que isto abre (e não responde) é: uma Skill que é só um ponteiro pode ser
marcada `CURRENT`?

Dois pontos que a medição do `LR-CMP-004` acrescenta: `go-naming` é um dos casos em que o **caminho**
prometido não é verificável por um validador de esquema (ele só checa frontmatter — o pointer quebrado não
é pego; a DeerFlow pega, com o achado `resource.missing`), e o `react-doctor` tem `version` declarada, que o
validador da Anthropic **rejeita** como chave desconhecida.

## 5. Descoberta contábil que muda a nossa checagem de licença

Censo de caminhos `LICENSE` no ragflow: **3 arquivos** — `LICENSE` (11.357 B, Apache-2.0),
`internal/dao/license.go` e `internal/entity/license.go`. Os dois últimos são **a feature de licença do
produto** (o modelo gorm tem `License string` mapeado para a coluna `encrypted_data;type:longtext` e
`CreatedAt timestamp`; comentário de arquivo *"License time record model"* — ou seja, chave **criptografada
no banco**, com expiração). Um censador ingênuo — inclusive o nosso, que conta `LICENSE*` na árvore — lê
"3 arquivos de licença" como "3 licenças no repositório".

Registro como regra para esta base: **o censo de `LICENSE*` da árvore deve casar nome de arquivo
case-insensitive e excluir extensão de código** (`.go`, `.py`, `.rs`, `.ts`). Nenhum documento nosso precisa
mudar de conteúdo por isso (as contagens dos relatórios anteriores foram feitas à mão, com leitura), mas a
ferramenta de censo que eu uso em rodadas futuras sim. É um ajuste meu, não de app — aplico no método da
próxima rodada.

## 6. O que não verifiquei, e por quê

- **nada do motor**: índices, qualidade de recuperação, Infinity vs. Elasticsearch, API de agente; nada foi
  instalado nem executado (exige serviço de busca + modelos + volume de dados);
- `AGENTS.md`: li a seção "Core Stance" e a abertura; as outras ~155 linhas não foram lidas por inteiro, e
  o `web/AGENTS.md` foi só contado (204 linhas);
- não abri `.agents/rules/named.md` (o alvo real do pointer) nem o `react-doctor` por inteiro;
- não procurei `NOTICE` no ragflow — o censo que fiz foi de caminhos contendo `LICENSE`; um `NOTICE` pode
  existir sem aparecer nessa contagem (é a limitação conhecida do nosso censador, documentada em `DR-0019`);
- não verifiquei o que o produto faz com o `license.go` além do que o modelo gorm mostra: **não** afirmo que
  o ragflow "bloqueia funcionalidade por chave" — só que tem um registro de licença persistido cifrado.

## 7. Recomendação: **WATCH**

O motor não tem caso de uso medido na Lia (a base trata RAG via OpenVINO/embeddings próprios —
`LR-OV-001`, `LR-MCP-001`), e instalar um produto de busca com 66 MB de árvore aqui seria fora de escopo.
Ficam três itens de material de decisão: a política de legado do `AGENTS.md` (Forge), o formato
pointer-skill com alvo externo (Hub), e a correção do censador de licença (esta base).

**Propor** ao dono, sem aplicar: registrar no `RESEARCH-BACKLOG.md` a leitura do `AGENTS.md` completo do
ragflow e do `web/AGENTS.md` como insumo da política de refatoração do Forge, se ele quiser um texto próprio.

## 8. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 94.709 ★ · 11.403 forks · 1.303 issues · Apache-2.0 · `language: Go` · ragflow.io · criado 2023-12-12 | `OBSERVED` | `gh api repos/infiniflow/ragflow` |
| 7.324 entradas / 6.587 blobs / 66,6 MB; 3.549 `.go`; 167 `.py`; 1.069 `.tsx`; 160 `.md`; 2 `SKILL.md`; 4 workflows | `OBSERVED` | `git/trees/HEAD?recursive=1` (`truncated: false`) + censo próprio |
| os 6 princípios da "Core Stance" e a frase "prefer the code and the current AGENTS.md over any older convention or remembered project shape" | `OBSERVED` (texto) | `AGENTS.md:1-12` lidos no clone com filtro de blob |
| `web/AGENTS.md` = 204 linhas | `OBSERVED` (contagem) | `wc -l` no arquivo materializado |
| `go-naming` é 1 linha apontando para `../../rules/named.md`; `react-doctor` tem `version: "1.2.0"` e "fetches the canonical playbook" | `OBSERVED` (texto) | os dois `SKILL.md` materializados e lidos no cabeçalho |
| `internal/entity/license.go`: gorm, coluna `encrypted_data` `longtext`, *"License time record model"*; `LICENSE` raiz = 11.357 B | `OBSERVED` (código) | arquivo lido + `contents/LICENSE` (tamanho pela API) |
| 902 commits nos últimos 30 dias | `OBSERVED` | `search/commits?q=repo:infiniflow/ragflow+committer-date:>2026-10-25` (`total_count`) |
| o motor funciona, recupera bem, escala | `NOT_RUN` | nada instalado nem executado |
| se há `NOTICE` no repositório | `NOT_RUN` | o censador desta rodada só casou `LICENSE*` |

## 9. Ponteiras para a próxima rodada

1. ler `.agents/rules/named.md` (o alvo real do pointer `go-naming`) — 1 arquivo, e decide se a pointer-skill
   é auditável sozinha ou não;
2. rodar o censador de licença **corrigido** (excluir `*.go`/`*.py`/`*.rs` do match de `LICENSE*`) sobre os 54
   objetos desta base e ver se alguma linha do `license-matrix.tsv` foi inflada pelo mesmo falso positivo;
3. contar commits de `docs/` vs. `internal/` no último trimestre — o `AGENTS.md:6-12` manda deletar doc
   velho; medir se eles cumprem é a única forma de saber se o texto é política ou desejo.

## 10. Como isto se liga à base

A "Core Stance" do ragflow é a versão mais explícita que li da regra que esta casa pratica com
`retificado em §…`: **o estado atual manda sobre a nota anterior**. A diferença é que eles resolvem por
deleção e nós por registro visível — e a base tem de continuar escolhendo a segunda opção, porque nosso
produto é a memória da pesquisa. O ponto de atrito que fica para o dono do Forge é exatamente esse: apagar é
mais barato do que retificar; quem paga o custo da escolha não é quem decide.
