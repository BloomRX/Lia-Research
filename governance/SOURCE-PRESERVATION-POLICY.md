# Política de preservação das fontes

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


Princípio: **o Lia-Research consolida conhecimento; não reorganiza os projetos de origem.**

---

## 1. O que nunca é feito nas fontes

Proibido sem autorização explícita e por escrito do proprietário:

- Excluir branch, tag ou repositório.
- `git reset`, `git clean`, `git rebase`, `git push --force`.
- Fazer merge de branches de outros projetos.
- Sobrescrever documento original.
- Alterar histórico Git de projeto de origem.
- Descartar alterações locais de terceiros.
- Remover arquivo considerado duplicado.
- Criar commit em repositório de origem em nome da pesquisa.
- Tornar público repositório ou documento privado.

Na fundação de 2026-11-17, a coleta foi **somente leitura**: `gh api` (metadados,
trees, contents, commits, branches, releases) e clones parciais em `/tmp` sem
checkout destrutivo. Nenhum comando de escrita foi executado contra os cinco
projetos.

## 2. Modos de consolidação

| Modo | Quando usar | O que fica no Lia-Research |
|---|---|---|
| `referenciado` | caso padrão | metadados + ponteiro permanente para a origem |
| `resumido` | documento longo cujo valor está na conclusão | digest de 1–3 páginas com ponteiros por seção |
| `citado` | trecho específico é a evidência | citação curta, atribuída, com commit |
| `copiado-integral` | documento pequeno, estável, cuja íntegra importa para auditoria | cópia + cabeçalho de proveniência + licença |

Padrão: `referenciado`/`resumido`. `copiado-integral` exige justificativa escrita.
Nunca copiar o mesmo relatório em quatro lugares — o relatório principal fica no
diretório da tecnologia e os índices apontam.

## 3. Ponteiro permanente (nunca `main`)

Errado:

```text
https://github.com/BloomRX/Lia-Project/blob/main/docs/research/LIA-MODEL-PROVIDER-CATALOG.md
```

Certo (commit fixo, branch explícita quando o arquivo não está em `main`):

```text
https://github.com/BloomRX/Lia-Project/blob/005a324/docs/research/LIA-MODEL-PROVIDER-CATALOG.md
```

Motivo medido: **511 dos 1.620 documentos** encontrados existem apenas em branches
de sessão. Um link para `main` aponta para um 404.

## 4. Risco conhecido: branch de sessão é volátil

Branches `arena/*` e `codex/*` podem ser apagadas por quem as criou. Consequência:
o conhecimento que só existe lá pode desaparecer sem estar "errado".

Mitigação adotada nesta fundação:

1. Inventário registra `repo + path + branch + commit` de cada documento.
2. Documentos materiais foram **resumidos** aqui, com os fatos-chave preservados.
3. `RESEARCH-ROADMAP.md` inclui a ação "promover pesquisa de branch de sessão para
   `main` do projeto de origem" — que é decisão do dono do projeto, **não** desta base.

O que o Lia-Research **não** faz: criar a branch, abrir o PR de integração ou mover
o documento. Isso alteraria a arquitetura dos projetos.

## 5. Conflito entre fonte e consolidação

Se o digest divergir do original, o original ganha. O digest deve ser corrigido e a
correção registrada em `RESEARCH-CHANGELOG.md`. Nunca "corrigir" o original.

## 6. Diretório de arquivo

`archive/` preserva o que não é mais a melhor fonte:

| Subdiretório | Conteúdo |
|---|---|
| `superseded/` | versões substituídas, mantidas para entender a evolução |
| `historical/` | decisões e números de contexto que explicam o presente |
| `incomplete/` | pesquisa interrompida, registrada para não ser reinventada |

Nada em `archive/` é apagado. Se um item se torna irrelevante, marca-se
`HISTORICAL` e mantém-se.

## 7. Verificação de preservação

Antes de encerrar uma rodada de consolidação, confirmar:

- [ ] `git -C <origem> status` limpo nos clones temporários (somente leitura).
- [ ] Nenhuma operação de escrita em `BloomRX/*` além do próprio Lia-Research.
- [ ] Todo documento consolidado tem origem + branch + commit + data.
- [ ] Nenhum documento original foi alterado ou removido.
- [ ] Avisos de copyright e licenças foram preservados nas citações.

## 8. Nunca substituir o número antigo (regra de 2026-11-20)

Atualizar pesquisa **não** é sobrescrever pesquisa. Ao revisar um objeto:

| Campo | Regra |
|---|---|
| `Data da pesquisa` | fica a data em que a análise foi feita; revisão ganha data própria |
| `Versão analisada` | o SHA antigo não desaparece: a nova versão entra ao lado, com data |
| Conclusão que mudou | escrever "antes: X, em `<data>`, na versão `<sha>`; agora: Y, porque Z" |
| Número medido | nunca arredondar para bater com o texto novo |

Arquivo substituído vai para `archive/superseded/` com `Substitui:` no cabeçalho. Relatório
que muda de conclusão sem registrar a anterior perde exatamente o que o torna confiável.
