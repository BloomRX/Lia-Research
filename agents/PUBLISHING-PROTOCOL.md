# Protocolo de publicação

Publicar não é criar arquivo. É tornar o conhecimento descobrível, rastreável e
auditável. Um documento sem índice é conhecimento perdido com aparência de salvo.

---

## 1. Checklist de publicação (ordem obrigatória)

| # | Passo | Verificação |
|---|---|---|
| 1 | Cabeçalho completo | ID, commit, datas, status, recomendação, licença, confiança |
| 2 | 18 seções (ou template aplicável completo) | nenhuma ausente |
| 3 | Tabela de evidências preenchida | cada afirmação material tem rótulo + ponteiro |
| 4 | Caminho correto | `repositories/<slug>/` para tecnologia; `cross-project/<área>/` para tema transversal |
| 5 | Ponteiro para a origem | URL com commit fixo, nunca `main` |
| 6 | Linha em `RESEARCH-INDEX.md` | ID, título, categoria, projeto, status, revisão, caminho |
| 7 | Ponteiro no `INDEX.md` do projeto | uma linha, não cópia |
| 8 | Entrada em `RESEARCH-CHANGELOG.md` | data, ID, o que mudou |
| 9 | Atualização do `RESEARCH-ROADMAP.md` | se abriu ou fechou tema |
| 10 | `python3 tools/validate.py` | sem erro |

## 2. Onde o documento mora (regra do relatório principal)

Um relatório tem **um** endereço principal:

| Tipo de objeto | Caminho principal |
|---|---|
| Repositório/tecnologia externa | `repositories/<slug>/REPORT.md` |
| Módulo interno de projeto | `projects/<projeto>/<área>/` |
| Tema transversal (voz, memória, MCP) | `cross-project/<área>/` |
| Comparação entre alternativas | `comparisons/<tema>/` |
| Decisão | `decisions/<estado>/DR-XXXX-*.md` |

Exemplo aplicado:

```text
HA-MCP  →  repositories/ha-mcp/REPORT.md          (principal)
        ─► projects/lia-project/integrations/     (aponta)
        ─► projects/lia-agent-hub/mcp/            (aponta)
        ─► cross-project/smart-home/              (aponta)
        ─► cross-project/mcp/                     (aponta)
```

Quatro apontamentos, uma cópia. Nunca o contrário.

## 3. IDs

Formato: `LR-<CATEGORIA>-<NNN>`.

| Categoria | Prefixo | Escopo |
|---|---|---|
| Agentes | `LR-AGENT` | orquestração, memória, frameworks de agente |
| MCP | `LR-MCP` | protocolo, servidores, integração |
| Voz | `LR-VOICE` | STT, TTS, VAD, full-duplex |
| Modelos | `LR-MODEL` | catálogo, avaliação, pesos, licenças de modelo |
| Segurança | `LR-SEC` | auditorias, credenciais, autenticação |
| Interface | `LR-UI` | componentes, acessibilidade, interação |
| Forge | `LR-FORGE` | assets, pipelines, 3D |
| Studio | `LR-STUDIO` | engine, gameplay, tooling de jogos |
| Hardware | `LR-HW` | compatibilidade, desempenho |
| Licença | `LR-LIC` | auditoria de licença/proveniência |
| Provedor | `LR-PROV` | providers e roteadores comerciais |
| Repositório | `LR-REPO` | auditoria de repositório inteiro |

Regras:
- ID é imutável. Mover arquivo não muda ID.
- ID não é reaproveitado. Pesquisa rejeitada mantém o ID, marcada `REJEITAR`.
- Próximo número = maior existente no índice + 1. Nunca preencher buraco.
- Um ID = um documento. Uma família de documentos pode ter `LR-MCP-001` … `-004`
  com sufixo `PARTE`.

## 4. Metadados e o índice

`RESEARCH-INDEX.md` é a **única** fonte de descoberta. Ele não duplica conteúdo:
uma linha por pesquisa. Se o índice e o documento divergem, o documento é a verdade
sobre o conteúdo e o índice deve ser corrigido imediatamente.

## 5. Atualização de pesquisa existente

Atualizar (não criar) quando: nova versão do objeto, correção de erro, evidência
nova que muda a conclusão. Ao atualizar:

1. manter o ID;
2. atualizar `Última verificação` e `Próxima revisão`;
3. registrar no changelog o que mudou e por quê;
4. se a conclusão mudou, escrever `## Mudança de conclusão` explicando antes/depois;
5. se houve versão anterior relevante, preservá-la em `archive/historical/`.

## 6. Retirada

Documento nunca é apagado. Estado `SUPERSEDED` + cabeçalho apontando o substituto.
`REJEITAR` também não apaga: a pesquisa que rejeita é evidência da decisão.

## 7. Pós-publicação

- Verificar que o link resolve (commit existe, caminho existe).
- Verificar que o ID aparece em exatamente um lugar do índice.
- Verificar que o projeto beneficiado tem o ponteiro.
- Rodar a validação uma última vez depois do commit.
