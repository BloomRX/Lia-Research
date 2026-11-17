# Auditoria de qualidade — auto-revisão da fundação

| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| Escopo | toda a base, no estado da fundação |
| Método | conferência item a item **com evidência**, não por existência de arquivo |
| Resultado | 24 itens: **20 PASS · 2 PARCIAL · 2 FAIL declarado** |

> Regra desta auditoria: "o arquivo existe" não aprova nada. Cada linha exige o que foi
> verificado e onde. Item que não pode ser verificado é `PARCIAL` ou `FAIL`, nunca PASS
> por ausência de erro encontrado.

---

## 1. Checklist de auto-revisão de relatório (`governance/RESEARCH-METHODOLOGY.md` §3)

| # | Item | Status | Evidência |
|---|---|---|---|
| 1 | Cabeçalho completo com commit e data | PASS | 20 relatórios verificados; `tools/validate.py` checa veredito no cabeçalho |
| 2 | Todas as seções do template | PASS | validador exige ≥18 seções `##` em `repositories/*/REPORT.md`; 0 falhas |
| 3 | Afirmação não trivial com rótulo de confiança | PASS | cada relatório tem seção de evidências com E1..En rotulados |
| 4 | Licença lida no arquivo, não no selo | PASS | 4 selos contraditos: `rescript` (Other→LGPL+MIT), `unslop` (none→404), `misterdl` (GPL confirmado no corpo), `manimgx` (mixed) |
| 5 | Nenhuma credencial ou dado pessoal | PASS | 10 padrões de segredo varridos em 123 arquivos; 0 ocorrências |
| 6 | Nenhuma afirmação de desempenho sem origem | PASS | 0 números de desempenho próprio na base; os citados são `REPORTED` de terceiro |
| 7 | Recomendação é uma das cinco categorias | PASS | ADAPTAR 6 · REFERÊNCIA 6 · REJEITAR 4 · ADOTAR 0 · PENDENTE 3 derivados |
| 8 | "Próximos passos" acionável | PASS | cada relatório fecha com item, dono sugerido e gate |
| 9 | Link usa commit fixo, não `main` | **PARCIAL** | 14 alvos externos com SHA completo; documentos internos usam SHA curto (`005a324`, `3ec4313`) por legibilidade — resolve, mas é abreviado |
| 10 | Nenhum documento de origem alterado | PASS | nenhuma escrita em repositório de origem; nenhuma branch criada/apagada/rebaseada |

## 2. Checklist de publicação (`agents/PUBLISHING-PROTOCOL.md`)

| # | Item | Status | Evidência |
|---|---|---|---|
| 11 | Documento em caminho único | PASS | validador checa caminhos locais citados; 0 quebrados |
| 12 | ID estável no `RESEARCH-INDEX.md` | PASS | 0 IDs órfãos após correção (`LR-BENCH-001`, `LR-SEC-003`, `LR-LIC-003`, `LR-CMP-00x`) |
| 13 | Projeto e área atualizados | PASS | 5 `INDEX.md` + `RESEARCH-INDEX.md` + `RESEARCH-CHANGELOG.md` |
| 14 | Entrada no changelog | PASS | seção 2026-11-17 com 7 tipos de evento |
| 15 | Revisão obrigatória aplicada | **FAIL** | revisão humana não ocorreu; é a pendência declarada da fase 5 |

## 3. GATES da ordem de serviço

| # | Gate | Status | Evidência |
|---|---|---|---|
| 16 | Visibilidade do repositório | **PASS (reauditado)** | proprietário declarou público por decisão (`c9e6e97`); registrado em `decisions/ACCEPTED/DR-0006`; exposição revisada em `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md` |
| 17 | Estrutura completa (§3) | PASS | todas as pastas com conteúdo, exceto 3 declaradas em `README.md` §8 |
| 18 | 9 templates | PASS | `ls templates/` → 9 arquivos |
| 19 | Governança (§9) | PASS | 8 documentos |
| 20 | IDs estáveis + metadados (§8) | PASS | `RESEARCH-INDEX.md` §1–§4 |
| 21 | Tiers de evidência (§2.3) | PASS | 6 rótulos definidos e usados; `BLOCKED` usado 6× |
| 22 | 18 seções + 5 vereditos (§7) | PASS | validador automatizado |
| 23 | Papéis e protocolo de revisão (§10) | PASS | `agents/` com 5 documentos |
| 24 | Sem submodule / sem dependência de runtime (§11) | PASS | zero `.gitmodules`, zero import, zero token nos cinco projetos |

## 4. Os dois FAIL, explicados

### 4.1 Visibilidade (item 16) — reauditado e resolvido
Originalmente `FAIL / BLOCKED`: a tentativa de tornar privado retornou `403` por duas
rotas, porque o token da integração não tem permissão de administração.

**Resolução (2026-11-17):** o proprietário publicou, na `main`
(`c9e6e97`), o README que declara o repositório público **por decisão** e define o modo
de consumo read-only para agentes de projeto. A pendência deixa de ser bloqueio e passa
a ser decisão registrada em `decisions/ACCEPTED/DR-0006-REPOSITORY-PUBLIC.md`.

O gate correspondente mudou de pergunta: não é mais "está privado?", e sim **"a
exposição pública foi revisada?"** — resposta em
`governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md`: 3 achados, 2 tratados, 0 pendentes
na base.

### 4.2 Revisão humana (item 15)
A fundação foi produzida por um agente. O protocolo exige revisor independente para
pesquisa de alto impacto — e 5 relatórios são alto impacto (HA-MCP, MDM, pixelfx,
rescript, RouterHub). Sem isso, o status correto é `PARCIAL`, não `PASS`.

## 5. Itens PARCIAL, explicados

### 5.1 SHA abreviado em documentos internos
Ponteiro para documento interno usa `Lia-Project@005a324:docs/...` em vez do SHA de 40
caracteres. É reconstruível (o prefixo é único no repositório) mas não é o padrão duro
de commit pinado. Recomendação: o índice de fontes (`data/inventory/corpus-manifest.tsv`)
tem os hashes de conteúdo; o SHA completo pode ser resolvido quando necessário.

## 6. O que esta auditoria **não** cobre

| Fora de escopo | Por quê |
|---|---|
| Correção técnica das análises | exige revisor humano com domínio |
| Desempenho de qualquer tecnologia | nada foi executado |
| Licença das 28 skills AIRI e `alethe` | **auditado** em `LR-LIC-003` (2ª rodada) |
| Qualidade dos documentos de origem | não é papel desta base |

## 7. Conclusão

A base está consistente internamente e honesta sobre o que não sabe. O que impede
`PASS` pleno não é trabalho faltando na base — são duas ações de terceiros:
**permissão de visibilidade** e **revisão humana**. Ambas estão registradas com o que
precisa acontecer, por quem.
