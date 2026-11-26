# MemPalace — memória de agente com índice próprio, instalada e executada até o ponto onde ela exige um modelo

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-019` |
| Nome | `MemPalace/mempalace` — "Give your AI a memory. No API key required." |
| Tipo | repositório (Python 3.10+ com crates Rust; instala-se do PyPI; expõe CLI, MCP proxy e servidor HTTP) |
| Licença | **MIT** (`LICENSE` 1.079 B medidos; `pyproject.toml` declara MIT) |
| Categoria | agent |
| Projetos beneficiados | Lia-Project (contrato de escopo/proveniência), Research e Model Lab quando reabrir (o molde de benchmark privado com conjunto reservado), Lia Agent Hub (padrão de ingestão por hooks) |
| Fonte oficial | https://github.com/MemPalace/mempalace · http://mempalaceofficial.com · PyPI `mempalace` |
| Responsável | `mempalace` (organização); atividade alta — PR #3038 (`perf/startup-bytecode`) aceito em 2026-11-26 |
| Versão analisada | `87ae5024d8eef885536258f5cb74cc1de8dcf9fd` (2026-11-26T01:04:05-03:00) = PyPI **3.12.0** |
| Proveniência do conteúdo | medido por nós: clone do repo (891 arquivos), leitura de `pyproject.toml`, `SECURITY.md`, `README.md`, `benchmarks/PRIVATE_PALACE.md`, `mempalace/i18n/`, `mempalace/embedding.py`, `mempalace/backends/**`; **e execução real**: `pip install mempalace` em venv, `mempalace --help`, `init`, `mine --dry-run`, `mine`, `search`, `--backend` inválido e válido, contra um vault sintético de 4 notas |
| Data | 2026-11-26 |
| Última verificação | 2026-11-26 |
| Upstream conferido | 2026-11-26 via API — ★**60.717** · 7.663 forks · **844** issues abertas · `language: Python` · `size` 34.590 KB · criado 2026-04-05 · `pushed_at` 2026-11-26T04:04:06Z · `license.spdx_id` MIT |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | PARTIAL — `init` e `mine --dry-run` rodaram offline; a escrita real e a busca falharam neste ambiente por exigirem modelo de embedding (ver §5) |
| Recomendação | **REFERENCE_ONLY** — o sistema não entra na Lia; **quatro peças do contrato** sim, listadas em §10 e desenvolvidas em `LR-CMP-006` |
| Decisão de adoção | — nenhuma (fora da autoridade desta base) |
| Confiança | Alta para o que foi executado e lido; nenhuma para qualidade de recall — não medimos recall (exige o índice, que não pôde ser construído aqui) |
| Próxima revisão | 2027-01-15 |

---

## 1. Identificação e tamanho do objeto

★60.717 em ~7 meses, 844 issues abertas, push no dia desta análise. É o maior objeto do eixo
"memória de agente" já medido nesta base (o concorrente direto, `akitaonrails/ai-memory`, está em
★16.441). Python 3.10–3.14 declarados no `pyproject.toml`; `crates/` em Rust para os backends
`rust_exact`; extras opcionais: `milvus`, `pgvector`, `gpu`, `dml` (`onnxruntime-directml`), `coreml`,
`embeddinggemma2`, `multimodal`, `extract` (`markitdown` para docx/pdf/pptx/xlsx) e **`multilingual`**,
que medimos declarada **com zero dependências** — o que muda o idioma é a escolha do modelo, não um extra.

Três pontos de entrada: `mempalace` (CLI), `mempalace-mcp` e `mempalace-light-mcp`. Deps de runtime
medidas no `pyproject.toml`: `chromadb>=1.5.4,<2`, `pyyaml`, `huggingface_hub>=0.20`, `tokenizers`,
`numpy`, `python-dateutil`.

## 2. O vocabulário, em três linhas

`wing` = um projeto; `room` = uma sala dentro do projeto (detectada **a partir da estrutura de pastas**);
`drawer` = o que foi minerado; `closet` = índice derivado; `hallways` = grafo de entidades; `layers`
L0/L1 = "acordar" com 600–900 tokens. Não é metáfora decorativa: `init <dir>` escreve `mempalace.yaml`
**dentro da pasta do projeto** com `wing` + `rooms` detectados, e os nomes de sala viram chave de busca.

## 3. O que a CLI expõe, e o que importa para a pergunta da rodada

31 subcomandos (`mempalace --help`, medido). Os cinco que interessam:

| Comando | O que faz | Por que importa aqui |
|---|---|---|
| `init <dir> [--no-llm] [--lang] [--embedding-model] [--yes]` | detecta salas pela árvore e grava o config no projeto | **seleção explícita por pasta**, com escolha explícita de modelo e opt-in de LLM |
| `mine <dir> [--dry-run] [--limit] [--mode] [--no-gitignore] [--include-ignored]` | ingere arquivos no índice | `--dry-run` **como padrão** e `--limit`: ingestão é operação com plano, não efeito colateral |
| `search <query> [--wing] [--room] [--results] [--since] [--before]` | busca | escopo por projeto/sala **e janela de data** — o escopo que a Lia não tem hoje |
| `sync [--dry-run] [--apply] [--wing]` | remove drawers cujo arquivo-fonte sumiu, mudou ou está no gitignore | **é o "exclusão" da pergunta**, resolvido por reconciliação e não por delete no vault |
| `export <dir>` | escreve uma árvore Markdown do palácio | portabilidade: o índice nunca é o único lugar onde a memória mora |

## 4. O que executamos (e o que deu)

`pip install mempalace` num venv Python 3.11 → **3.12.0 instalado**; `import mempalace` ok; CLI ok.
Contra um vault sintético de 4 notas (o mesmo usado em `LR-MCP-005`, copiado para `vault-mp`):

| Etapa | Resultado |
|---|---|
| `init vault-mp --no-llm --yes` | **ok, offline**. Criou `mempalace.yaml` com `wing: vault_mp` e 4 salas (`projetos`, `diário`, `scripts`, `general`); "Config saved". Dois artefatos do gerador visíveis no arquivo: a sala saiu como `"di\xE1rio"` (escape ASCII, não UTF-8) e as `keywords` vieram duplicadas (`projetos, projetos`) |
| `mine vault-mp --mode projects --dry-run` | **ok, offline**: "Files processed: 3 · skipped (read error or too short): 3 · Drawers filed: 3", com contagem por sala |
| `mine vault-mp --mode projects` (real) | **falha**: `httpx.ConnectError: TLS/SSL connection has been closed` dentro de `mempalace/backends/embedding_wrapper.py:97` |
| `search "RX 580"` | **falha**: o mesmo `ConnectError` |
| `search --backend lexical` / `sqlite` / `fts` | erro bom: `unknown backend ...; available: ['chroma','milvus','pgvector','qdrant','rust_exact','sqlite_exact']` — o registro lista o que existe e **não escolhe fallback** |
| `--backend sqlite_exact` sobre palace existente | erro bom, de propósito: `BackendMismatchError: palace ... contains 'chroma' backend artifacts, but 'sqlite_exact' was selected. Select the matching backend or use a fresh palace directory.` |
| `mine --backend sqlite_exact` em palace novo | **mesma falha de rede** — o backend de armazenamento não elimina o embedding da escrita |

## 5. O achado central: "no API key required" é verdade; "local" não é completo

O `README.md:249` afirma que o resultado bruto de 96,6% "requires no API key, no cloud, and no LLM at
any stage". Medimos o L1 do sistema e a frase é compatível com o código — mas há um passo que a frase
não cobre: **toda escrita passa por `embedding_wrapper.upsert` → `configured_embedding_function()`**,
que constrói o modelo de embedding (o comentário em `mempalace/embedding.py:389` diz "the model
(~300 MB) downloads on first call and is cached by `huggingface_hub`"). E o docstring de
`configured_embedding_function` é explícito sobre a recusa de atalho: *"Nothing calls chromadb's default
function instead"* — com `UnavailableEmbeddingFunction` deixando leituras (contar, listar, buscar linha)
funcionarem e qualquer embed (query ou escrita) subir erro.

Consequência prática, medida: **num ambiente sem rede e sem cache de modelo não dá para construir o
palácio**. Não é um defeito de segurança — é um requisito de provisionamento que a frase de marketing
não declara. Para a Lia, cujo alvo é uma máquina de usuário final com RX 580 e 16 GB, isso é a diferença
entre "plugin" e "instalação com download de ~300 MB + Chroma".

Também medido: o palácio padrão mora em `~/.config/mempalace/palace` (XDG), **fora** do diretório do
projeto — `init` grava config no projeto, mas os dados vão para a pasta global. E uma execução falha já
deixou artefatos `chroma` lá (motivo do `BackendMismatchError` acima).

## 6. O que é a ingestão, tecnicamente

`mine` não é "importar .md": é um pipeline (`mempalace/miner.py`, `process_file` → `palace/writes.py:195
write_file_drawers`) com detecção de origem do corpus em duas camadas (`corpus_origin.py`): Tier 1 heurístico
sem API, Tier 2 **com uma chamada de LLM** ("One call, ~$0.01 cost") para confirmar plataforma e nomes de
persona. Ou seja, a classificação rica do corpus depende de um provedor de LLM — e por isso existe
`--no-llm`, `--llm-provider {ollama,openai-compat,anthropic}` e o flag explícito **`--accept-external-llm`**.
Esse trio é o desenho que a Lia deve copiar: **consentimento de saída de dados é um parâmetro, não um rodapé**.

## 7. Segurança e tráfego de dados

`SECURITY.md:40-42`: o palácio é aberto in-processo e **não escuta porta nenhuma**; se você compartilhar
o palácio entre máquinas (o comando `serve` sobe um servidor MCP HTTP de equipe), mantenha em localhost
ou rede privada. Não achamos chamada de telemetria; o tráfego de saída real é (a) download do modelo de
embedding e (b) chamadas de LLM quando habilitadas. O conteúdo do usuário **não** vai a lugar nenhum
nesses dois caminhos por construção — mas vai ao provedor de LLM se `--llm` for aceito, e isso é o que
`--accept-external-llm` existe para tornar difícil de fazer por acidente.

## 8. pt-BR — o único ponto em que este objeto é melhor que os demais do eixo

Medido nesta sessão: `mempalace/i18n/` traz **15 idiomas** incluindo `pt-br.json` com **47 chaves, as
mesmas 47 de `en.json`, zero ausentes** (6.699 B contra 7.358 B). `benchmarks/model_eval/translate_datasets.py:42`
mapeia `"pt-BR": "Brazilian Portuguese"`. E `benchmarks/PRIVATE_PALACE.md:29-30` pede explicitamente que o
conjunto de perguntas inclua "**Portuguese and English**, ambiguidade e esperas de erro". Compare com
`LR-UI-006` §12 (Animama: nenhum `pt` em lugar nenhum) — a diferença não é acidental e é o tipo de coisa
que se perde quando se lê só o README.

## 9. O molde de avaliação (o que o Research deveria roubar hoje)

`benchmarks/PRIVATE_PALACE.md` descreve um harness de busca **privado**: JSONL por caso com `query`,
`filters.wing` (escopo), `tags`, `judgments` e **`expect_no_results: true`** para "espera de erro";
mínimo 50 perguntas de desenvolvimento e 100 reservadas; `pool` de julgamento **cego** com
`--pool-depth 20`; proibição explícita de ajustar no conjunto reservado; e o README deles mesmos marca o
risco de "*teaching to the test*" (`README.md:260`). Não medimos o harness (precisa do índice). É o
formato de avaliação de memória que falta à Lia — anotar como proposta em `LR-CMP-006` §5, não como adoção.

## 10. O que a Lia leva e o que não leva

Leva (forma, não código): **(1)** `--dry-run` como padrão de ingestão e `sync` por reconciliação em vez de
delete; **(2)** escopo com nome (`wing`/`room`) aplicado na **busca**, não só na coleta; **(3)** o par
`--no-llm` / `--accept-external-llm` como porteira de saída de dados; **(4)** o harness de benchmark
privado com conjunto reservado e casos de "espera de erro". Não leva: o sistema — 31 subcomandos, ~300 MB
de modelo por baixo, 844 issues abertas, palácio em `$HOME` e um vocabulário próprio que a Lia teria que
explicar ao usuário para sempre. Recomendação `REFERENCE_ONLY` com esses quatro itens como `ADAPT` está
tratada em `comparisons/MD-NOTES-INTEGRATION.md`.

## 11. Riscos e limites deste relatório

Nada de recall foi medido — a métrica deles exige o índice que não pudemos construir (sem rede). O que
executamos foi sobre 4 notas sintéticas, não sobre um corpus real. Não instalamos os extras (`milvus`,
`pgvector`, `gpu`, `dml`), então "funciona no DirectML da RX 580?" está **NOT RUN**. E `serve` (HTTP para
equipe) não foi levantado — o único caso em que "roda local" deixa de ser evidente.

## 12. Evidências

| # | Afirmação | Rótulo | Como reproduzir |
|---|---|---|---|
| E1 | PyPI 3.12.0 instala e a CLI roda (31 subcomandos) | **TESTED** | `python3 -m venv v && v/bin/pip install mempalace && v/bin/mempalace --help` |
| E2 | `init --no-llm` funciona offline e escreve `mempalace.yaml` no projeto, com salas da árvore | **TESTED** | §4 |
| E3 | `mine --dry-run` processa 3 e pula 3 ("read error or too short") | **TESTED** | §4 |
| E4 | `mine` e `search` reais falham por rede em `embedding_wrapper.py:97` | **TESTED** | §4, stack trace completo no log da sessão |
| E5 | backends disponíveis: 6 nomes; sem fallback silencioso; mismatch de backend recusa | **TESTED** | §4 |
| E6 | `pt-br.json` com 47 chaves = 47 de `en.json`, 0 faltando | **TESTED (diff de chaves)** | `python3` sobre os dois JSON |
| E7 | deps de runtime e extras (com `multilingual: []`) | **CONFIRMED (lido)** | `pyproject.toml` |
| E8 | palácio padrão em `~/.config/mempalace/palace`; tentativa falha deixou artefatos chroma | **TESTED** | §5 |
| E9 | ★60.717 · 844 issues · push 2026-11-26T04:04Z · MIT · 34.590 KB | **CONFIRMED (API, 2026-11-26)** | `gh api repos/MemPalace/mempalace` |
| E10 | "no API key required" / 96,6% bruto / "teaching to the test" | **REPORTED** (lido no `README.md:249,260`; não medimos) | `sed -n '235,265p' README.md` |
| E11 | sem porta de rede no modo normal; `serve` exige localhost/rede privada | **REPORTED** (`SECURITY.md:40-42`) | `sed -n '35,45p' SECURITY.md` |
| E12 | Tier 2 de `corpus_origin` custa ~$0,01 de LLM por corpus | **REPORTED** (docstring do módulo) | `head -30 mempalace/corpus_origin.py` |
| E13 | recall, qualidade do índice, uso de memória, desempenho em RX 580, `serve` multiusuário | **NOT RUN / BLOCKED** | exige o índice (§4) e/ou GPU/Windows |
