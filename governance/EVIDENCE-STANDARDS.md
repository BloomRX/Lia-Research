# Padrões de evidência

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


Objetivo: tornar impossível confundir "o README diz" com "foi verificado".

---

## 1. Os seis rótulos

### `CONFIRMED`
Verificado diretamente por evidência primária que o agente reproduziu ou leu
integralmente: arquivo `LICENSE`, código-fonte, saída de teste, release, advisory.

> Exemplo da fundação: "ha-mcp declara 86 tools" → `CONFIRMED` porque a tabela de
> ferramentas está versionada em `README.md` com marcadores `TOOLS_TABLE_START/END`
> e o projeto usa CI que testa E2E.

> Exemplo de licença: "misterdownloadmanager é GPL-3.0" → `CONFIRMED` porque o
> arquivo `LICENSE` na raiz, no commit `d9a9ef0`, contém o texto GPL v3.

### `OBSERVED`
Visto durante a inspeção, mas sem validação independente. O agente viu, não testou.

> "A árvore do repositório contém `crates/mcp` com `src/main.rs` e um teste stdio"
> → `OBSERVED` que existe um servidor MCP; não `CONFIRMED` de que ele funciona.

### `REPORTED`
Afirmação do próprio projeto ou de terceiro, não verificada na fonte primária.

> "Downloads 5× mais rápidos que o IDM" → `REPORTED` (badge de README, sem método).

### `INFERRED`
Conclusão técnica do agente a partir de fatos verificados, com o raciocínio exposto.

> "A licença GPL-3.0 impede incorporar `crates/mcp` em um app proprietário sem
> abrir o app" → `INFERRED` (consequência jurídica da licença, não parecer jurídico).

### `UNVERIFIED`
Não foi possível confirmar nem refutar. Diferente de `BLOCKED`: aqui houve acesso,
mas a evidência é insuficiente ou contraditória.

### `BLOCKED`
O acesso, o ambiente ou a informação impediram a investigação. Sempre acompanhado
do que faltou e de como destravar.

---

## 2. Regras de atribuição

1. **Uma afirmação, um rótulo.** Frase sem rótulo só é permitida quando é fato
   trivial e diretamente citável (nome do repositório, URL).
2. **Rótulo herda o elo mais fraco.** Se a conclusão depende de um dado `REPORTED`,
   a conclusão não pode ser `CONFIRMED`.
3. **`CONFIRMED` exige ponteiro.** Commit SHA + caminho, ou comando reproduzível.
4. **Benchmark de terceiro nunca é `CONFIRMED` de desempenho no hardware do usuário.**
   No máximo `REPORTED`, com hardware e método do terceiro explicitados.
5. **Compatibilidade não declarada sem teste.** "Suporta Vulkan" (`REPORTED` pela doc)
   ≠ "roda na RX 580 do usuário" (`UNVERIFIED` até smoke test).

---

## 3. Escala de confiança global

Cada relatório declara uma confiança global, derivada dos rótulos usados:

| Confiança | Critério |
|---|---|
| **Alta** | maioria `CONFIRMED`; nenhuma seção crítica depende de `REPORTED` |
| **Média** | `CONFIRMED` na identificação/licença, `OBSERVED`/`REPORTED` em arquitetura |
| **Baixa** | depende de `REPORTED`/`INFERRED` em pontos materiais, ou há `BLOCKED` |

Um relatório de confiança baixa pode ser útil — mas não pode sustentar uma
recomendação `ADOTAR`.

---

## 4. Tabela de evidência

Todo relatório com mais de cinco afirmações materiais inclui:

| # | Afirmação | Rótulo | Evidência (commit/caminho) | Data |
|---|---|---|---|---|
| E1 | ... | CONFIRMED | `repo@sha:path` | 2026-11-17 |

A tabela é a seção 16 do template (Evidências e fontes) e é a única parte do
relatório que um revisor precisa conferir ponto a ponto.

---

## 5. Anti-padrões vistos no ecossistema Lia

| Anti-padrão | Por que quebra a base |
|---|---|
| "Evidência classificada como EXECUTED, não VALIDATED" | dois vocabulários concorrentes; aqui existe só um |
| Relatório de 20 KB com zero commits citados | não é rastreável, não é auditável |
| Número histórico repetido sem reconferência | envelhece em silêncio (ver §6) |
| "47 skills sem licença" sem dizer onde foi verificado | afirmação correta, evidência ausente |

---

## 6. Números históricos

Número vindo de pesquisa anterior é `REPORTED` até ser remedido. Ao remedir,
registrar as duas medições e a diferença de método:

> Histórico (2026-11): 39 registros apenas em branches de sessão.
> Medição 2026-11-17: 511 documentos distintos fora de `main`.
> Diferença explicada por granularidade (registro de pesquisa × arquivo) e escopo
> (5 repositórios, 43 branches). Status: `CONFLICTING` de métrica, ambos preservados.

Nunca substituir o número antigo em silêncio, e nunca apresentar o novo como
"o mesmo número, atualizado".
