# Protocolo de revisão independente

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


Revisão independente é obrigatória quando o erro custa caro: segurança, credenciais,
licença, providers comerciais e automação residencial.

---

## 1. Quando é obrigatória

| Gatilho | Exemplo |
|---|---|
| Segurança ou autenticação | análise do modelo de token/OAuth do HA-MCP |
| Credenciais ou segredos | qualquer relatório que mencione gestão de chave |
| Licença com impacto de distribuição | GPL/AGPL, "sem licença", pesos de modelo |
| Provider comercial | preço, retenção de dados, jurisdição |
| Automação residencial | fechadura, alarme, ações R2/R3 |
| Ação irreversível recomendada | migração de runtime, troca de protocolo |

## 2. Quem revisa

- Não pode ser o autor.
- Preferencialmente um agente diferente (outro modelo/sessão) **ou** o proprietário.
- Para licença: revisão humana é obrigatória para qualquer conclusão que afete
  distribuição a usuário final.

## 3. O que o revisor faz

1. **Amostragem de evidência**: escolher as 5 afirmações mais materiais e ir até a
   fonte. O ponteiro resolve? O conteúdo diz o que o relatório diz?
2. **Checagem de rótulo**: alguma afirmação `REPORTED` está sendo usada como `CONFIRMED`?
3. **Checagem de escopo**: o relatório conclui mais do que a evidência permite?
4. **Checagem de licença**: a licença foi lida no arquivo, no commit certo?
5. **Checagem de segurança**: há credencial, host real, dado pessoal?
6. **Checagem de proibição**: alguma recomendação invade decisão de outro dono?

## 4. Formato do parecer

```markdown
## Parecer de revisão — LR-XXX-000
Revisor: <nome/agente>   Data: AAAA-MM-DD   Rodada: 1
Resultado: APROVADO | APROVADO COM RESSALVAS | REPROVADO

### Verificações
| # | Item | Resultado | Observação |
|---|---|---|---|

### Ressalvas (bloqueiam publicação?)
1. ...

### Evidência contestada
| Afirmação | Problema | Correção sugerida |
|---|---|---|

### Assinatura
```

O parecer é anexado ao relatório (seção final) ou ao PR, nunca em arquivo separado
que se perde.

## 5. Consequências

| Resultado | Efeito |
|---|---|
| APROVADO | publica |
| APROVADO COM RESSALVAS | publica com ressalvas listadas **no documento** |
| REPROVADO | não publica; volta ao autor com motivo específico |

Duas reprovações no mesmo item escalam para decisão humana: a pesquisa está mal
enquadrada, não mal escrita.

## 6. Registro

Toda revisão de alto impacto gera linha em `RESEARCH-CHANGELOG.md`:
`revisão independente de LR-XXX-000 — APROVADO — <revisor> — <data>`.
