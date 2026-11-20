# Fluxo do agente de pesquisa

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


Sequência operacional para qualquer agente (Arena, Codex, ou humano) que produz
pesquisa para o Lia-Research.

---

## 0. Pré-voo (2 minutos, evita retrabalho de horas)

```bash
# 1. Estado do repositório
git -C <lia-research> status --short
git -C <lia-research> log --oneline -3

# 2. Autenticação GitHub (sem pedir credencial ao usuário)
gh auth status

# 3. Já existe pesquisa sobre o tema?
grep -i "<tema>" RESEARCH-INDEX.md
```

Se `gh auth status` falhar: **parar** e informar que a conexão GitHub precisa de
atenção. Nunca pedir senha, PAT ou código 2FA ao usuário.

## 1. Enquadramento

- Frase da pergunta.
- Projeto(s) beneficiado(s).
- Template escolhido.
- Escopo negativo.
- Critério de evidência suficiente.

## 2. Coleta

Ver `governance/RESEARCH-METHODOLOGY.md` §2. Regra de ouro:

> **Resolver caminho → branch antes de baixar.** Em ecossistema com 43 branches,
> metade dos documentos não está em `main`.

## 3. Verificação

Para cada afirmação material: existe arquivo? qual commit? qual rótulo?
Se não houver evidência, o rótulo é `UNVERIFIED` — e o texto não pode afirmar.

## 4. Redação

Template completo. Toda seção presente. Sem generalidade de enchimento.

## 5. Validação automática

```bash
python3 tools/validate.py
```

Verifica: cabeçalho, ID único, seções obrigatórias, links para commit fixo,
ausência de padrões de segredo, entrada no índice.

## 6. Publicação

1. Mover/criar arquivo no caminho definitivo.
2. Adicionar linha em `RESEARCH-INDEX.md`.
3. Adicionar ponteiro no `INDEX.md` do projeto beneficiado.
4. Entrada em `RESEARCH-CHANGELOG.md`.
5. Registro em `RESEARCH-ROADMAP.md` se abriu novo tema.
6. Commit e PR.

## 7. Encerramento

Responder explicitamente:

- o que foi confirmado;
- o que ficou `PENDENTE`/`BLOCKED` e por quê;
- o que o usuário precisa decidir;
- qual o próximo passo mais útil.

---

## Uso de ferramentas: limites

| Ferramenta | Permitido | Proibido |
|---|---|---|
| `gh api` leitura | sim | `PATCH`/`DELETE` em repositório de origem |
| clone | sim, em `/tmp`, `--filter=blob:none` | clone dentro do Lia-Research |
| execução de código de terceiro | não (sem autorização) | rodar instalador, MCP server, skill |
| download de pesos de modelo | não | baixar GB "para testar" |
| edição | só neste repositório | qualquer `BloomRX/*` |

## Memória entre sessões

O Lia-Research **é** a memória. Não manter estado em branch de sessão: se a
conclusão não está publicada aqui com ID e índice, ela não existe para a próxima
sessão — e essa foi exatamente a falha estrutural medida em 2026-11.
