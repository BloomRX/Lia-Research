# blender-ai-mcp-addon — repositório sem código-fonte que distribui ZIP binário com licença e identidade de outro projeto

| Campo | Valor |
|---|---|
| ID | `LR-SEC-008` |
| Nome | bookwjitchieni1986/blender-ai-mcp-addon |
| Tipo | repositorio |
| Fonte oficial | https://github.com/bookwjitchieni1986/blender-ai-mcp-addon |
| Responsável | conta `bookwjitchieni1986` (identidade não verificada) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED |
| Recomendação | **REJECT** |
| Decisão de adoção | — nenhuma registrada |
| Categoria | security (leitura transversal em forge, mcp) |
| Projetos beneficiados | Lia Forge (Blender/MCP), Lia Agent Hub (intake de terceiros), Lia Project |
| Versão analisada | `v1.0.0` · commit `7a235a5c0245bc3ef2e5296d4ea4a8eec3aed986` (main) |
| SHA completo | `7a235a5c0245bc3ef2e5296d4ea4a8eec3aed986` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — confirmado por duas vias independentes na re-leitura de 2026-11-22: `refs/tags/v1.0.0` aponta para o objeto de commit `7a235a5c…`, e `commits/main` devolve o mesmo SHA (mensagem "Add docs/images/studio-settings.png", 2026-11-19T14:43:48Z). O tag é `type: commit`, não `type: tag` — não há objeto anotado com data de release |
| HEAD atual | `7a235a5c0245` (conferido em 2026-11-22) |
| Data | 2026-11-22 |
| Última verificação | 2026-11-22 |
| Upstream conferido | 2026-11-22 · HEAD `7a235a5c` · sem mudança desde a análise |
| Próxima revisão | 2027-02-20 |
| Licença | MIT no arquivo, com "Copyright (c) 2025 Siddharth Ahuja" — **não é o detentor do conteúdo deste repositório** |
| Confiança | Alta para todos os fatos estruturais; nenhuma para o conteúdo do ZIP (não baixado) |

---

## 1. Resumo executivo

Este repositório **não contém o software que anuncia**. A árvore tem 7 arquivos e 2 diretórios:
`LICENSE`, `README.md`, `docs/QUICKSTART.md`, `docs/CONNECTIONS.md` e três PNGs de interface —
**nenhum `.py`, nenhum `addon.py`, nenhum `src/`**. A distribuição é feita por um artefato binário
de **12,8 MB** anexado a uma release, descrito como contendo "Portable Python 3.13 runtime bundled".

Três fatos tornam o objeto uma questão de **segurança do ecossistema**, não de tecnologia:

1. o `LICENSE` é MIT com copyright **de outra pessoa** — "Siddharth Ahuja, 2025" — que é exatamente
   o detentor do projeto legítimo `ahujasid/mcp-for-blender` (★35.279, MIT, PyPI `mcp-for-blender`
   2.3.1, antigamente `blender-mcp`);
2. o nome do produto no README é **"mcp-for-blender-pro"**, colado sobre a marca do projeto que ele
   imita — e os três arquivos de texto do repositório (README, `docs/CONNECTIONS.md`,
   `docs/QUICKSTART.md`) **não mencionam o projeto original em nenhum momento**: a busca por
   `ahujasid`, `blender-mcp`, `upstream`, `formerly` e `original` só devolve uma frase sobre tradução
   ("remain in their original language"). Não há aviso de não-afiliação, nem crédito, nem ponte.
3. a conta autora tem **9 dias** (criada 2026-11-13), **um** repositório, 0 seguidores, e o repositório
   foi criado e teve todos os 8 commits **no mesmo minuto** (2026-11-19 14:43 UTC), com push final
   61 segundos depois — mas já tinha ★2.578 e 35 forks no momento da coleta (2.580 na verificação
   seguinte).

Nada aqui é acusação de malware: o ZIP não foi baixado nem analisado, e não há competência técnica
nesta sessão para afirmar o que ele faz. O que é `CONFIRMED` é a estrutura: **binário opaco, sem
código-fonte, licença alheia, identidade colada, métricas sem história**. Isso basta para `REJECT`.

## 2. Estrutura medida (não é descrição do README)

| Item | Medido via API em 2026-11-22 |
|---|---|
| Árvore | 7 blobs + 2 trees, `truncated: false` — `LICENSE` (1.072 B), `README.md` (7.219 B), `docs/QUICKSTART.md` (1.432 B), `docs/CONNECTIONS.md` (2.691 B), 3 PNG (112 KB, 108 KB, 137 KB) |
| Commits | 8, todos com data `2026-11-19T14:43`; o primeiro é literalmente "Initial commit" |
| Autor | `bookwjitchieni1986` — 1 repositório, 8 contribuições, criada 2026-11-13, 0 seguidores |
| Release | `v1.0.0`, publicada `2026-11-19T14:44:11Z`, um único asset `blender-ai-mcp-addon-v1.0.0.zip`, 12.849.331 bytes, **2.192 downloads** |
| Anúncio | "The release bundle targets **Windows x64** with Blender 4.2 or later" |
| Métricas | ★2.578 → ★2.580 → **★2.590** (releitura em 2026-11-22) · 35 forks · 56 issues · 345 KB · `language: null` · `license: MIT` |
| Links externos | o README aponta para `github.com/.../releases/latest` e para os dois `docs/*.md`; em `docs/CONNECTIONS.md` os únicos `http` presentes são `127.0.0.1:9876/mcp`, `localhost:11434` e `your-service.example/v1` — **nenhum link para o projeto original** |

## 3. Os issues não falam deste repositório

Amostra de 12 issues abertos (2026-11-21/22) contém pedidos de suporte para **arquivos que não
existem aqui**: "Can not activate **addon.py** in Blender", "Which one is server? addon in Blender
or **src/blender_mcp/server.py**?". Um deles é um relatório de vulnerabilidade —
**#65 "Arbitrary File Read via generate_hunyuan3d_model"**, descrevendo `open()` em caminho
controlado pelo usuário, sem validação, com o arquivo lido sendo enviado base64 a uma API externa.

Dois modos de leitura, e os dois são problema:

- **a.** alguém instalou um projeto homônimo (o `blender-mcp`/`mcp-for-blender` legítimo, que tem
  `addon.py` e `src/blender_mcp/server.py`) e veio pedir suporte aqui por engano; ou
- **b.** o ZIP deste repositório é uma cópia/remistura daquele código — hipótese compatível com o
  `LICENSE` copiado do mesmo autor, e **impossível de confirmar sem abrir o ZIP**.

Em qualquer caso, o repositório funciona como **ponto de captura de tráfego de suporte** de outro
projeto, com um binário próprio na frente. Para o Lia Agent Hub, que vai expor um catálogo de
terceiros, isso é um caso de escola: o registro precisa de campos que tornem este padrão visível
(§6).

## 4. A vulnerabilidade citada existe — no outro projeto

Conferido na API de advisories do GitHub em 2026-11-22: **GHSA-4h8q-hh2j-755w**, *BlenderMCP path
traversal in `download_polyhaven_asset` allows arbitrary file writes*, severidade **medium**,
CVSS **5.3**, publicado **2026-07-24**, pacote `blender-mcp`, afetando `< 1.6.5`, corrigido em
**1.6.5**. O PyPI de `mcp-for-blender` está em **2.3.1**.

O relevo para o Lia: a versão anunciada aqui é **1.0.0**, numerada antes da linha 1.6.5, mas sem
qualquer meio de mapear esse número às versões do projeto legítimo. Comprar um binário por
"versão 1.0.0" é exatamente o caso em que **não se consegue responder "estou vulnerável?"**. Isso
é um critério de intake, não um comentário sobre este repositório em particular.

## 5. O que não foi feito, e por quê

- **Não baixei, descompactei, instalei ou executei o ZIP.** Baixar um executável de fonte
  não verificada é uma ação com consequência para a máquina do usuário; o pedido desta base é
  pesquisa documental e execução **isolada de código-fonte aberto**. Registro como `BLOCKED` —
  não como `FALHA`.
- **Não abri conta, não instalei nada em projeto Lia, não editei o repositório** (é de terceiro;
  nem abrir issue: isso alimentaria o tráfego que se está descrevendo).
- Não há análise forense aqui. Se o proprietário quiser evidência de conteúdo, o passo é **análise
  estática do ZIP em ambiente isolado, deliberada e autorizada** — fora do escopo de pesquisa.

## 6. Consequências práticas para o ecossistema Lia (proposta de prática)

| Critério de intake sugerido | Como este objeto falharia |
|---|---|
| **Hash publicado e verificável do artefato binário** | o ZIP não tem checksum publicado; 12,8 MB sem integridade declarada |
| **Código-fonte do que é distribuído, no mesmo repositório ou tag** | zero arquivos de código |
| **Licença com detentor coerente com o conteúdo** | MIT em nome de terceiro, que nunca publicou este repositório |
| **Idade mínima + histórico** | 9 dias de conta, 8 commits em 1 minuto |
| **Estrelas não bastam; exigem história** | ★2.590 em 3 dias, sem nenhuma release anterior nem CHANGELOG |
| **Nome e URL do projeto de origem declarados** | "mcp-for-blender-pro" sobre "mcp-for-blender", sem link para o original |

Nenhum desses campos existe hoje nos registros `*.records.json` do Hub — é lacuna de
**formato**, endereçável sem criar nada novo: são colunas, não Skills.

## 7. Recomendação

**`REJECT`** — não baixar, não instalar, não listar como candidato de integração e não citar como
evidência de que "existe um MCP de Blender com N estrelas". O caminho legítimo para o mesmo objetivo
(Blender controlado por agente) é o projeto `ahujasid/mcp-for-blender`, MIT, com `addon.py`, `src/`,
`tests/`, `Dockerfile`, distribuição por PyPI e advisory pública com versão corrigida — objeto já
registrado nesta base em `cross-project/agents/BLENDER-MCP-DIGEST.md`, e não reaberto aqui
(dedup `RESEARCH-GOVERNANCE.md` §6: este relatório é sobre o **imitador**, não sobre o upstream).

## 8. Contexto: o que o Lia já tem, e por que este objeto não acrescenta nada (caso de teste de política)
| Necessidade | Onde já está registrada | O que este objeto mudaria |
|---|---|---|
| Blender controlado por agente | `cross-project/agents/BLENDER-MCP-DIGEST.md` (`LR-FORGE-005`), sobre o upstream legítimo | nada — o upstream continua sendo a fonte |
| aprovação explícita de tool call, shell e escrita de arquivo | `cross-project/mcp/MCP-LANDSCAPE.md` (`LR-MCP-001`/`LR-MCP-002`) | reforça a regra: é o mecanismo que teria parado o `generate_hunyuan3d_model` do issue #65 |
| intake de terceiros no catálogo | `projects/lia-agent-hub/INDEX.md` + §6 acima | é aqui que este objeto tem valor, como **caso de teste de política** |
| licença por artefato (binário sem fonte) | `cross-project/licensing/READY-TO-USE-LICENSES.md` | caso extremo: licença de terceiro sobre artefato opaco |

Leitura útil do contraste: os três projetos de MCP de Blender que aparecem em buscas (o legítimo, este
e variantes de marca) **não se distinguem por funcionalidade no que é público** — a descrição do
servidor local na porta 9876 e do backend Ollama na 11434 é a mesma. A única diferença visível sem
executar é o **grau de exposição do código**. Isso é o que torna o formato de registro (`has_source`,
hash do artefato, detentor da licença, idade do histórico) uma peça de segurança, e não burocracia: é
a única coisa que um adotante pode checar antes de rodar.

## 9. Evidências

| Afirmativa | Rótulo | Fonte (todas em 2026-11-22, UTC) |
|---|---|---|
| 7 blobs / 2 trees, sem código-fonte | `CONFIRMED` | API `git/trees/HEAD?recursive=1` |
| 8 commits no mesmo minuto; asset 12.849.331 B com 2.192 downloads | `CONFIRMED` | API `commits`, `releases` |
| conta com 1 repositório, criada 2026-11-13, 0 seguidores | `CONFIRMED` | API `users/...`, `repo list` |
| MIT com copyright "Siddharth Ahuja" ≠ autor do repositório | `CONFIRMED` | `LICENSE` lido, comparado a `ahujasid/mcp-for-blender/README.md` |
| nenhuma menção ao projeto original em README nem docs | `CONFIRMED` | busca por 5 termos nos 3 arquivos de texto |
| issues pedindo suporte a `addon.py` / `src/blender_mcp/server.py` | `CONFIRMED` | API `issues` (#76, #64) |
| issue #65 descreve arbitrary file read | `CONFIRMED` | corpo da issue lido |
| GHSA-4h8q-hh2j-755w, medium/CVSS 5.3, `< 1.6.5`, patch em 1.6.5 | `CONFIRMED` | API `advisories` |
| ★2.578→2.580→2.590, 35 forks, 56 issues | `CONFIRMED` | três leituras da API (duas 8 min apartadas, uma no ciclo seguinte) |
| "o ZIP contém código malicioso" | — | **não afirmado**; nenhum byte foi aberto |
| "o ZIP é cópia do blender-mcp" | `UNVERIFIED` | hipótese (b) do §3, não testável sem o arquivo |
| comportamento em execução, VRAM, qualidade | `BLOCKED` | nada executado |

## 10. Gatilho de reabertura

Reabrir apenas se: (a) o repositório passar a publicar código-fonte com licença própria;
(b) aparecer denúncia formal ou remoção pela plataforma; ou (c) o proprietário autorizar análise
forense do ZIP em ambiente isolado. Sem um desses, este objeto não entra em nova rodada — e este
relatório é a razão para que nenhum projeto Lia o cite como dependência.

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · esquema `catalog/CATALOG-SCHEMA.md` · contexto em `cross-project/agents/BLENDER-MCP-DIGEST.md`.
