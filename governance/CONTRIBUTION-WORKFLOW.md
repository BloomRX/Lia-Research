# Fluxo de contribuição

---

## 1. Quem contribui

| Perfil | Caminho |
|---|---|
| Agente de pesquisa (Arena/Codex/etc.) | branch `research/<tema>` → PR para `main` |
| Agente de outro projeto Lia | issue `research-request`; não commita direto |
| Humano responsável | qualquer caminho, com revisão registrada |

Agentes **nunca** committam em `main` diretamente. Nem neste repositório, nem —
por hipótese alguma — nos projetos de origem.

## 2. Fluxo

```text
1. Issue (ou pedido do proprietário)
2. Checar RESEARCH-INDEX → duplicata? → atualizar em vez de criar
3. Escolher template
4. Coletar evidência (commit + data + licença)
5. Redigir
6. Auto-checagem (metodologia §3) + tools/validate.py
7. PR: título "LR-XXX-000: <título>"
8. Revisão: obrigatória para alto impacto
9. Merge → atualizar RESEARCH-INDEX, INDEX do projeto, CHANGELOG
```

## 3. Convenção de branch e commit

```text
research/<categoria>-<slug>       ex.: research/mcp-ha-mcp
consolidation/<projeto>-<data>    ex.: consolidation/lia-project-2026-11
fix/<id>-<slug>                   ex.: fix/LR-MCP-001-caminho-errado
```

Commits no padrão `tipo(escopo): assunto`, tipos: `research`, `consolidation`,
`governance`, `template`, `index`, `fix`, `chore`.

Um commit por unidade lógica. Não misturar governança com pesquisa no mesmo commit.

## 4. Pull request

O corpo do PR deve conter:

- ID(s) `LR-*` afetados;
- pergunta respondida;
- fontes e commits analisados;
- rótulos de evidência predominantes;
- o que **não** foi possível determinar;
- se a recomendação muda algo que já estava publicado (e o que muda).

Checklist no template `.github/pull_request_template.md`.

## 5. Revisão

| Impacto | Revisão exigida |
|---|---|
| Baixo (referência, comparação informativa) | auto-revisão + validação automática |
| Médio (arquitetura, maturidade, custos) | segundo par de olhos (humano ou agente distinto) |
| Alto (segurança, credenciais, automação residencial, providers, licença) | revisão independente obrigatória, registrada |

Detalhes: `agents/REVIEW-PROTOCOL.md`.

## 6. Critérios de bloqueio de merge

O PR **não** entra se:

- falta cabeçalho completo ou commit analisado;
- há afirmação de desempenho sem origem;
- há credencial, token ou dado pessoal;
- há seção do template vazia ("a ver" não é resposta);
- a licença não foi lida no arquivo;
- duplica documento existente sem justificar escopo diferente;
- `tools/validate.py` falha.

## 7. Não faça

- Não copie documento de projeto de origem para cá e edite o original depois.
- Não "corrija" número histórico: registre o novo com método e data.
- Não apague arquivo em `archive/`.
- Não adicione código de terceiros, nem como exemplo executável.
- Não altere `governance/` no mesmo PR que publica pesquisa.
