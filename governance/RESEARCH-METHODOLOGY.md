# Metodologia de pesquisa

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


Este é o procedimento operacional. Ele foi escrito a partir do método que
realmente funcionou na fundação de 2026-11-17 (e dos erros cometidos nela).

---

## 1. Fases

### Fase A — Enquadramento (antes de coletar)

1. Formular a pergunta em uma frase, com o projeto beneficiado nomeado.
2. Consultar `RESEARCH-INDEX.md`: já existe? (ver `RESEARCH-GOVERNANCE.md` §6)
3. Definir o que seria evidência suficiente para responder — **antes** de olhar o objeto.
4. Escolher o template (`templates/`).
5. Registrar escopo negativo: o que esta pesquisa **não** vai cobrir.

Erro a evitar: começar pelo README do projeto e deixar que ele defina a pergunta.
README define o que o autor quer que você pense; a pergunta define o que você precisa saber.

### Fase B — Coleta de evidência primária

Ordem de prioridade (de mais forte para mais fraca):

1. **Licença** — arquivo `LICENSE`/`COPYING` na raiz, lido no commit analisado.
2. **Código** — estrutura, dependências declaradas, testes, CI.
3. **Metadados** — releases, commits, issues, advisories.
4. **Documentação oficial do projeto** — `docs/`, site.
5. **Documentação de terceiros** — artigos, posts, benchmarks publicados.
6. **Alegações de README** — último recurso, sempre como `REPORTED`.

Registrar para cada item: URL, commit/tag, data da consulta.

### Fase C — Verificação adversarial

Para cada afirmação que entrará no relatório, perguntar:

- Existe arquivo que prove isso, ou é o README falando?
- A licença que o GitHub mostra é a mesma do arquivo `LICENSE`? (São coisas diferentes.)
- O recurso é estável ou está atrás de flag beta?
- A versão analisada é a que o usuário vai instalar?
- Se eu não puder provar, qual rótulo uso?

### Fase D — Redação

Uma afirmação por parágrafo curto, cada uma com rótulo quando não for óbvia.
Toda seção do template é obrigatória; se não há dado, escrever "não identificado"
— nunca omitir a seção, nunca preencher com generalidade.

### Fase E — Revisão

Auto-revisão obrigatória (checklist §3) e, para alto impacto, revisão independente
(`agents/REVIEW-PROTOCOL.md`).

### Fase F — Publicação

`agents/PUBLISHING-PROTOCOL.md`: índice, projeto, changelog, validação.

---

## 2. Técnicas de coleta que funcionaram (e as que não)

### 2.1 Clone parcial para inventário de branches

```bash
git clone --filter=blob:none --no-checkout https://github.com/ORG/REPO.git repo
git branch -r
git ls-tree -r --long origin/main
```

- Funciona para listar estrutura sem baixar conteúdo.
- **Não escala** para `ls-tree -r` em muitas branches: cada árvore é buscada
  sob demanda pela rede. Na fundação, 5 repositórios × 43 branches estouraram
  600 s de timeout.

### 2.2 Trees API para inventário em escala

```bash
gh api "repos/ORG/REPO/git/trees/SHA?recursive=1"
```

- Uma requisição por branch, 43 branches em ~6 segundos.
- Devolve caminho, tipo e tamanho. É o método recomendado para inventário.

### 2.3 Contents API para leitura de arquivo

```bash
gh api -H "Accept: application/vnd.github.raw" \
  "repos/ORG/REPO/contents/PATH?ref=BRANCH"
```

- `--jq .content` devolve base64 que precisa de decodificação; usar `Accept: raw`
  é menos sujeito a erro.
- Um `404` quase sempre significa **branch errado**, não arquivo inexistente. Foi
  a causa de 35 de 45 falhas iniciais na fundação: os documentos existiam apenas em
  branches de sessão.

### 2.4 Resolver caminho → branch antes de baixar

Passo obrigatório em ecossistema com muitas branches: montar o índice
`(repo, path) → [branches]` a partir das trees, escolher a branch com commit mais
recente que contém o caminho, e só então baixar. Sem isso, metade da pesquisa
"não existe".

### 2.5 O que não confiar

| Sinal | Por que não confiar |
|---|---|
| Selo de licença do GitHub | derivado de heurística; `NOASSERTION` e `null` significam "leia o arquivo" |
| Badge "X tools" | contagem de marketing; conferir no código ou na tabela de tools |
| README "blazingly fast" | afirmação sem medição |
| Estrelas do repositório | popularidade não é qualidade nem licença |
| Idade do último commit | commit de bot (changelog, tráfego) parece atividade |
| Benchmarks em blog | hardware e método desconhecidos |

---

## 3. Checklist de auto-revisão

- [ ] Cabeçalho completo, com commit e data.
- [ ] Toda seção do template presente.
- [ ] Cada afirmação não trivial tem rótulo de confiança.
- [ ] Licença lida **no arquivo**, não no selo.
- [ ] Nenhuma credencial, token ou dado pessoal no texto.
- [ ] Nenhuma afirmação de desempenho sem origem declarada.
- [ ] Recomendação é uma das cinco categorias, não um sinônimo inventado.
- [ ] Seção "Próximos passos" é acionável (o que, quem, quando).
- [ ] Links para arquivos de origem usam commit fixo, não `main`.
- [ ] Nenhum documento de origem foi alterado.

---

## 4. Tratamento de bloqueio

Bloqueio não é fim de pesquisa; é um resultado. Procedimento:

1. Registrar o que se tentou, com comando e mensagem de erro.
2. Registrar o que **não** foi possível determinar por causa disso.
3. Marcar a seção como `BLOCKED` com o motivo.
4. Continuar os itens independentes.
5. Se a ausência inviabiliza a conclusão, a recomendação é `PENDENTE`, não `REJEITAR`.

Exemplo real da fundação: a alteração de visibilidade do repositório para privado
retornou HTTP 403 ("Resource not accessible by integration"). A fundação foi declarada
com uma pendência explícita em vez de assumir que estava privado — e, quando o
proprietário decidiu manter o repositório público, a pendência virou decisão registrada
(`decisions/ACCEPTED/DR-0006-REPOSITORY-PUBLIC.md`) em vez de desaparecer.

---

## 5. Higiene de dados

- Coletar em diretório temporário fora do repositório (`/tmp`), nunca em `docs/`.
- Versionar apenas o que é conhecimento: relatório, matriz, digest.
- **Não** versionar clone, código de terceiros, binário, peso de modelo ou release.
- Amostras de configuração devem ser sanitizadas antes de qualquer citação.

### 5.1 Exceção declarada: `data/`

`data/` é o único lugar onde material bruto entra, e por um motivo específico: os
documentos dos cinco projetos vivem majoritariamente em branches `arena/*`, que são de
sessão e podem desaparecer. Sem algum registro persistente, uma afirmação publicada aqui
deixa de ser verificável quando a branch some.

Limites da exceção:

| Regra | Valor |
|---|---|
| Material de terceiros | **proibido** — só manifesto com caminho + SHA |
| Conteúdo | apenas material próprio da Lia |
| Tamanho por artefato | ≤ 2 MB (tudo acima é comprimido) |
| Obrigatório | manifesto com hash e `README.md` explicando o que é |
| Autoridade | snapshot **não** é fonte de verdade: é prova do que existia na data |

Motivo da mudança: na fundação de 2026-11-17 o inventário existia apenas em `/tmp`,
que não é persistido. Registro que evapora não é registro.
