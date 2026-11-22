# last30days-skill — Skill de pesquisa multi-fonte: o que uma Skill grande precisa carregar

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-011` |
| Nome | mvanhorn/last30days-skill |
| Tipo | repositorio (pacote de Skills) |
| Fonte oficial | https://github.com/mvanhorn/last30days-skill |
| Responsável | `mvanhorn` |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | PARTIAL |
| Recomendação | **ADAPT** |
| Decisão de adoção | — nenhuma registrada |
| Categoria | studio (leitura transversal em agents, security, licensing) |
| Projetos beneficiados | Lia Agent Hub (formato de Skill e de empacotamento), Lia Research (método de síntese), Lia Studio |
| Versão analisada | `e63f8e8732f1` (main, 2026-11-21T21:44Z) · tag `v4.5.0` |
| SHA completo | `e63f8e8732f1` (12 caracteres, lidos da API de commits; `v4.5.0` na mesma linha) |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — conferido contra o HEAD de `main` na coleta |
| HEAD atual | `e63f8e8732f1` |
| Data | 2026-11-22 |
| Última verificação | 2026-11-22 |
| Upstream conferido | 2026-11-22 · HEAD `e63f8e87` · sem mudança desde a análise |
| Próxima revisão | 2027-02-20 |
| Licença | MIT (`CONFIRMED` em `LICENSE`, © 2026 Matt Van Horn; também declarada no frontmatter da Skill) |
| Confiança | Alta para estrutura, empacotamento e segurança declarada; média para comportamento de rede (não exercitado) |

---

## 1. O que é, e por que está nesta base

Uma **Skill de agente** — não um app — que pesquisa o que as pessoas disseram sobre um tema nos
últimos 30 dias (Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, web) e sintetiza com
pontuação por engajamento. ★72.092 · 6.387 forks · 18 issues abertas · criado 2026-01-23 · ativo no
dia da análise. É o caso mais completo que existe, publicamente, de **"Skill que virou produto"**:
versão 4.5.0, 10 idiomas de README (incluindo `README.pt-BR.md`), instaladores para Claude Code,
Codex, Cursor, Copilot, Gemini CLI e "50+ hosts de Agent Skills", extensão MCP com engine Go
vendorizada.

Para o Lia Agent Hub o valor não é a Skill — é o **conjunto de decisões de engenharia em torno de uma
Skill**: metadado, empacotamento, permissões, consentimento, testes de rede e fronteira de licença de
terceiros. O Hub está desenhando exatamente essas coisas agora.

## 2. Anatomia da Skill (medida no commit)

| Camada | Conteúdo |
|---|---|
| Árvore | 787 blobs no repositório; 435 arquivos em `tests/`; 201 em `skills/`; 543 `.py` |
| `SKILL.md` frontmatter | `name`, `version: "4.5.0"`, `description`, `argument-hint`, **`allowed-tools: Bash, Read, Write, AskUserQuestion, WebSearch`**, `homepage`, `repository`, `author: mvanhorn`, **`license: MIT`**, `user-invocable: true`, `metadata.openclaw.{emoji, requires.env, requires.optionalEnv (15 chaves), bins: [node, python3], primaryEnv, files, homepage}` |
| Runtime da Skill | `SKILL.md` + `references/` (19 md) + `scripts/` (155 `.py`) + `.skillignore` + `agents/openai.yaml` |
| Empacotamento | `.gitattributes` com `export-ignore` + `scripts/build-skill.sh` gerando o `.skill` de upload |
| Manifestos por host | `.claude-plugin/`, `.codex-plugin/`, `.grok-plugin/`, `gemini-extension.json`, `mcp/` (Go) |

O ponto que resolve uma dúvida real desta base: **a licença declarada dentro do frontmatter**. É o
mecanismo mais leve que vi para a lacuna "47 de 48 Skills sem licença no payload" — um campo, não um
arquivo novo. E o bloco `metadata.openclaw.requires` é o mesmo tipo de declaração que a `alethe` do
Hub tentou com `metadata:` aninhado e que quebrou o parser do catálogo.

## 3. Empacotamento: a decisão mais interessante do objeto

`.gitattributes` abre com o motivo: *"Exclude non-runtime files from `git archive` output"*. Estão
`export-ignore`: `__pycache__/`, `node_modules/`, `*.pyc`, `.DS_Store`, `evals/`, `tests/`, `docs/`,
`fixtures/`, `assets/`, `SPEC.md`, `TASKS.md`, `CONTRIBUTORS.md`, `HERMES_SETUP.md`, `CHANGELOG.md`.
Há um comentário que vale como regra de projeto:

> `skills/` e `.claude-plugin/` **não** são export-ignorados porque o `/plugin install` do Claude
> Code busca exatamente esse tarball git. Removê-los do arquivo (como a v3.0.1 fez) quebra instalações
> silenciosamente.

Medido nesta sessão, nos dois caminhos de download:

| Artefato | Arquivos | `tests/`? |
|---|---|---|
| tarball `codeload` do commit (= o que um instalador de host recebe) | **261** | não |
| API `git/trees?recursive=1` do mesmo commit | **787** | sim (383 em `tests/`) |

Ou seja: **a suíte de testes não viaja no artefato de instalação, por escolha documentada**. O custo é
o que esta análise experimentou — a partir do tarball não há como rodar os testes. Um catálogo que
registre só "tem `tests/`" estaria errado; o que precisa de registro é **"presente no repositório ×
presente no artefato"**.

## 4. O que foi executado e o que bloqueou

| Etapa | Resultado |
|---|---|
| baixar o tarball do commit | 12.800.146 bytes |
| `python3 -m compileall -q skills/last30days/scripts` (Python 3.11.2) | **153 de 155 compilam**; 2 falham (`scripts/lib/hackernews.py`, `scripts/lib/render.py`) por f-string multilinha — sintaxe de 3.12 |
| rodar a suíte a partir do tarball | impossível por construção: `tests/` não está no artefato |
| `clone --depth 1` + `pytest tests` | bloqueado pelo portão do próprio projeto: `ensure_supported_python()` imprime "last30days v4 requires Python 3.12+. Detected Python 3.11.2." com instruções por sistema e `raise SystemExit(1)` |
| contornar o portão (patch local de `MIN_PYTHON`) e re-coletar | 168 erros de coleta pela mesma causa de sintaxe — **o portão é verdadeiro, não cosmeticismo** |

Nenhuma requisição de rede, nenhuma chave, nenhuma extração de cookie, nenhuma instalação no sistema.
O `--preflight` documentado — que "mostra a fonte de config, o plano de cookies do navegador, as
escritas planejadas… sem ler cookies nem escrever arquivos" — **não foi executado**: bloqueia antes,
no Python. Registro como `BLOCKED` com o motivo exato, não como `FALHA`.

## 5. Segurança: o que o SECURITY.md declara × o que o código mostra

Declarações lidas em `SECURITY.md` (102 linhas) e `CONFIGURATION.md` (1.048 linhas):

- leitura de cookies do navegador é **desligada por padrão e exige consentimento no setup**; revogável
  com `BROWSER_CONSENT=false` ou `FROM_BROWSER=off`; `--no-browser-cookies` desliga incondicionalmente
  para a execução;
- escopo declarado: só `auth_token` e `ct0` de `.x.com`, e `_session_id` de `.truthsocial.com`,
  filtrando por domínio e nome **antes** de descriptografar;
- o banco do navegador é lido de uma **cópia** escrita com modo `0600` e apagada depois;
- chaves ficam no Keychain do macOS (`last30days-<KEY>`) ou no `pass`, nunca em relatório;
- reranking local garantido: sem as quatro famílias de chave nada vai a provedor; evidência de
  `--corpus` local "nunca é enviada a provedor";
- `private_files.py` existe para publicar texto atomicamente com permissão dono-e-apenas-dono e
  preparar modos antes de o SQLite criar arquivos a partir do modo do banco.

No código, a mesma intenção com alcance mais largo que a frase do SECURITY.md: `chrome_cookies.py`
declara cobrir **toda a família Chromium no macOS** (Chrome, Brave, Edge, Vivaldi, Opera, Arc, Dia,
Chromium), todos com o mesmo algoritmo v10 (AES-128-CBC com chave no Keychain), mudando só diretório
de perfil e nome do serviço. O filtro por nome é o que limita; **o mecanismo é geral**. Consequência
para quem registra: a promessa é verdadeira por construção de filtro, não por limitação técnica. Um
catálogo que dissesse "lê 3 cookies" seria mais fraco que a realidade; um que dissesse
"descriptografa a chave do Keychain" seria mais forte. Precisa das duas camadas: **o que o código pode
× o que a política restringe**.

Exceção declarada, com honestidade rara: na *jobs lane*, "por decisão do autor, a lane lê a listagem de
vagas mesmo onde o robots.txt desallows aquele caminho" (cita o Google), com
`LAST30DAYS_JOBS_RESPECT_ROBOTS=1` para desligar, e a lista do que **não** fazem: sem spoofing de
fingerprint, sem resolver challenge, sem browser headless. `CONFIRMED` como declaração, `UNVERIFIED`
como comportamento — e **não é padrão a copiar**: desrespeitar robots.txt é risco jurídico, registrado
como `REQUIRES_LEGAL_REVIEW`.

## 6. Padrões aproveitáveis

1. **frontmatter com `license` + `version` + `allowed-tools`** — três campos que respondem 80% do que o
   Hub não sabe hoje sobre as 48 Skills.
2. **`export-ignore` declarado com motivo e com a exceção comentada** — a fronteira "repositório ×
   artefato instalado" tem de ser decisão escrita, não efeito colateral do git.
3. **portão de versão com mensagem acionável** (o que faltou, o que fazer por sistema, o que
   reexecutar). Contraste direto com o objeto da mesma rodada: a ferramenta da NVIDIA falhou em
   3.11 com `SyntaxError` em profundidade — mistério; aqui, três linhas e um exit code — diagnóstico.
4. **`tests/network_guard.py`**: fixture `autouse` que intercepta `bind`/`connect` e faz o teste
   **falhar** ao tentar rede, inclusive quando a exceção é engolida. É o mecanismo que a regra desta
   base — "nenhuma conta, nenhum consumo" — precisa para virar asserção de CI em vez de promessa.
5. **10 idiomas de README no mesmo commit**, pt-BR incluído: se o Hub quer adoção, o texto de entrada é
   custo real de manutenção, e aqui está provado que cabe.
6. **`.skillignore` com justificativa** — mas ver a limitação abaixo.

**Limitação do padrão 6:** o `.skillignore` retira do *scan* de segurança do instalador exatamente os
artefatos de desenvolvimento e avaliação (`build-skill.sh`, `compare.sh`, `evaluate_search_quality.py`,
`reddit_canary.py`, `test_device_auth.py`, `verify_v3.sh`…). O comentário justifica ("não-runtime") e,
sendo arquivos do próprio autor, o risco aqui é baixo — mas **o formato permite esconder do gate
justamente o que o gate deveria ler**. Se o Hub adotar algo assim: o que está ignorado continua
contabilizado no inventário, e ignorar tem de ser declarado, não silencioso.

## 7. Custos e dependências

- `pyproject`: `requires-python = ">=3.12"` e **`dependencies = []`** — o pacote não puxa nada; o
  runtime da Skill exige `python3` + `node` e aceita até 15 variáveis de chave **opcionais**
  (ScrapeCreators como `primaryEnv`, OpenAI, xAI, bearer do X, OpenRouter, Perplexity, Parallel,
  Brave, Apify, Bluesky, Truth Social, Xiaohongshu…).
- Sem chave, o projeto declara degradação para modo "só web" — **não verificado aqui**.
- O custo de uso é de terceiros (API do X, ScrapeCreators, Brightdata…). **Nenhum preço foi lido**;
  qualquer valor unitário está `UNVERIFIED` e não deve ser repetido por nenhum projeto Lia com base
  neste relatório.

## 8. Compatibilidade com o ecossistema Lia

| Alvo | Encaixe |
|---|---|
| Lia Agent Hub | alto, como **referência de formato**: frontmatter com licença/versão/ferramentas, manifesto por host, empacotamento com `export-ignore`, `.skillignore` com regra contábil |
| Lia Research | o pipeline de síntese (fontes → cluster → rerank local → brief com trilha de evidência) é análogo ao fluxo desta base; **não** copiar a coleta por cookies nem o atropelamento de robots.txt |
| Lia Studio / Project | sem uso direto: depende de navegadores, contas pessoais e 3.12 |
| Lia Forge / Model Lab | nenhum |

**Não usar como dependência.** `ADAPT` aqui é sobre metadado e disciplina de gate.

## 9. Evidências

| Afirmativa | Rótulo | Base |
|---|---|---|
| 261 arquivos no tarball do commit; 155 `.py` na Skill; 153 compilam em 3.11 | `OBSERVED` | download + `compileall` nesta sessão |
| portão de Python com mensagem e `SystemExit(1)`; 168 erros de coleta com o portão removido | `OBSERVED` | clone + `pytest` nesta sessão |
| frontmatter com `license: MIT`, `allowed-tools`, `metadata.openclaw.requires` | `CONFIRMED` | `skills/last30days/SKILL.md` no commit |
| `export-ignore` de `tests/`, `docs/`, `fixtures/`, `assets/` + exceção de `skills/` comentada | `CONFIRMED` | `.gitattributes` |
| `dependencies = []` e `requires-python >=3.12` | `CONFIRMED` | `pyproject.toml` |
| cookies off por padrão, escopo de 3 nomes, snapshot `0600`, `--no-browser-cookies` | `CONFIRMED` (declaração) | `SECURITY.md`, `CONFIGURATION.md`, `chrome_cookies.py` |
| o mecanismo de leitura não é restrito a 3 nomes por construção | `OBSERVED` | docstring e corpo de `chrome_cookies.py` |
| `tests/network_guard.py` com fixture autouse de socket | `CONFIRMED` | arquivo lido no clone |
| ★72.092 · 6.387 forks · 18 issues · v4.5.0 · push 2026-11-21 | `CONFIRMED` | API do GitHub, 2026-11-22 |
| comportamento de rede, qualidade da síntese, custo por execução | `BLOCKED` | nada exercitado; sem contas nem chaves |
| robots.txt desrespeitado na prática | `UNVERIFIED` | declarado no SECURITY.md; nenhuma requisição feita |
| "funciona em 50+ hosts" | `REPORTED` | README; nenhum host de agente disponível nesta sessão |

## 10. Recomendação e próximos passos

**`ADAPT`** — quatro decisões concretas, sem tocar em código: frontmatter com
`license`/`version`/`allowed-tools`; registro "presente no repositório × presente no artefato"; portão
de versão com mensagem de correção; e *network guard* como teste, para que "nenhuma conta, nenhum
consumo" deixe de ser promessa e passe a ser asserção verificável.

1. Levar o formato de frontmatter para `projects/lia-agent-hub/skills/SKILL-LICENSE-CONSOLIDATION.md`
   como alternativa de custo mínimo à licença por arquivo.
2. Revisão em 2027-02-20: projeto ativo (push no dia da análise), hosts e extras mudam rápido.
3. Não reabrir sem um gatilho: Python 3.12+ na sessão, ou autorização explícita para exercitar
   `--preflight` contra uma Skill do Hub.

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · contexto em `cross-project/agents/SKILLS-MCP-LANDSCAPE.md`.
