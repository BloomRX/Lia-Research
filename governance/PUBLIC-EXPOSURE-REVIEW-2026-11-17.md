# Revisão de exposição pública

| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| Motivo | o proprietário declarou o repositório **público por decisão** (`main` README, commit `c9e6e97`) |
| Escopo | todo o conteúdo versionado nesta branch: 124 arquivos Markdown, 4 TSV, 1 snapshot, 3 scripts Python, 4 templates GitHub |
| Método | varredura por padrão (11 classes) + inspeção manual dos achados + inspeção do conteúdo do snapshot |
| Resultado | **3 achados, todos no snapshot do corpus. 2 tratados nesta rodada. 0 pendentes na base.** |

---

## 1. O que mudou

| Antes | Agora |
|---|---|
| Política: "repositório deve ser privado; se público, nada sensível pode ser commitado" | Política: "repositório é público **por decisão do proprietário**; nada sensível pode ser commitado" |
| `DR-0006` = bloqueio de privacidade | `DR-0006` = decisão **aceita** (público), registrada em `decisions/ACCEPTED/` |

A regra de conteúdo **não** relaxou. Mudou o motivo: antes era "até ficar privado";
agora é permanente.

## 2. Varredura — resultado por classe

### 2.1 Documentos da base (meus)

| Padrão | Ocorrências |
|---|---|
| token GitHub (`ghp_`, `gho_`, …) | 0 |
| chave de API (`sk-`) | 0 |
| credencial AWS (`AKIA…`) | 0 |
| bloco de chave privada (`BEGIN … PRIVATE KEY`) | 0 |
| JWT | 0 |
| `senha=` / `password=` com valor | 0 |
| IP de LAN real (`192.168.x.x`) | 0 |
| caminho de usuário Windows (`C:/Users/<nome>`) | 0 |
| home de usuário POSIX (`/Users/<nome>/`) | 0 |
| e-mail de terceiro | 0 |
| CPF | 0 |

`LIMPO`. Confirmado também por `tools/validate.py` (checagem 2), que roda em cada commit.

### 2.2 Snapshot do corpus (`data/snapshots/lia-corpus-2026-11-17.tar.gz`)

O snapshot preserva 236 documentos lidos dos cinco projetos, coletados de branches
`arena/*`. A varredura encontrou **3 achados**, todos em documentos de projeto — não em
texto produzido por esta base.

| # | Achado | Arquivo de origem | Gravidade |
|---|---|---|---|
| A1 | **Dados de sessão privada**: nome de usuário do sistema (`C:/Users/lucas/`), caminhos de rollout (`.codex/sessions/…jsonl`), contagens de token, IDs de thread | `Lia-Project:docs/architecture/LIA-AGENT-CONSUMPTION-AUDIT.local.md` | **alta** |
| A2 | **3 e-mails pessoais de autores de add-ons** (`@gmail`, `@hotmail`) extraídos de metadados (`bl_info`, `blender_manifest.toml`) | `Lia-Forge:docs/ECOSYSTEM-RESEARCH-BLENDER-ADDONS.md` | média |
| A3 | Caminho de usuário do autor upstream (`/Users/neko/`) em documentação do AIRI | `Lia-Project:docs/architecture/AGENT-SKILLS-AUDIT-AIRI.md` | baixa (dado público de terceiro, já publicado no upstream) |

## 3. Tratamento aplicado

| Achado | Ação | Justificativa |
|---|---|---|
| A1 | **arquivo excluído do snapshot** | é dump de sessão pessoal com identificador de máquina. O nome `.local.md` já indicava que não deveria ser versionado. Preservar não vale o risco; o ponteiro (repositório + caminho + branch) permanece |
| A2 | **3 e-mails substituídos** por `[e-mail do autor removido na sanitização]` | e-mail de terceiro é dado pessoal; o valor de pesquisa é a licença e a origem do add-on, não o contato |
| A3 | **mantido** | é caminho do autor do AIRI em documento público do próprio AIRI; remover destruiria evidência de origem sem ganho de privacidade |

O snapshot foi regerado (235 arquivos) e o manifesto atualizado com cabeçalho de
sanitização (`data/inventory/corpus-manifest.tsv`). Os hashes de A2 mudaram — o que é
correto: o conteúdo mudou.

## 4. Registro de sanitização (diff)

```text
data/snapshots/lia-corpus-2026-11-17.tar.gz
  236 arquivos → 235
  − Lia-Project/docs/architecture/LIA-AGENT-CONSUMPTION-AUDIT.local.md
  ~ Lia-Forge/docs/ECOSYSTEM-RESEARCH-BLENDER-ADDONS.md   (3 e-mails redigidos)
  manifest: sha256 recomputado; cabeçalho declara a transformação
```

Nenhum documento da base cita o conteúdo removido; a remoção não quebra nenhuma
afirmação de relatório (a auditoria de consumo não é fonte de nenhum ID publicado).

## 5. O que continua exposto de propósito

| Conteúdo | Por que é aceitável |
|---|---|
| Nomes de repositório e URLs | já públicos no GitHub |
| SHA de commit de repositórios públicos | já públicos |
| Advisory IDs (`GHSA-…`) e issue IDs | informação pública de segurança |
| Caminho de segredo do HA-MCP (`/mcp`, porta 8086) | documentado no README do próprio projeto; sem host real nem token |
| Descrição de vulnerabilidade em beta | já pública em advisory; aqui só é citada |
| Números de estrelas, licenças, metadados | públicos |
| `data/external/pinned-targets.tsv` | metadados públicos |

Nenhum destes revela um alvo concreto explorável: não há host real, credencial, nem
instalação identificável.

## 6. Achados fora da minha alçada (para o proprietário)

| Item | Onde | Por que importa |
|---|---|---|
| `LIA-AGENT-CONSUMPTION-AUDIT.local.md` continua versionado em `BloomRX/Lia-Project` (**público**) | repositório de produto | contém caminho de usuário, IDs de sessão e contagem de tokens; se não for intencional, deve sair do histórico por decisão do dono |
| Os cinco repositórios Lia são públicos e **sem licença** | API do GitHub | visibilidade sem licença é "todos os direitos reservados" na prática; ver `LR-LIC-003` §7.5 |
| 21 Skills autorais sem licença no payload | `Lia-Project/.agents/skills/` | `LR-LIC-001`, `DR-0001` |

Não alterei nada em repositório de produto: a base é read-only para os cinco projetos.

## 7. Conclusão

A base pode permanecer pública **sem ressalva de conteúdo**: nenhum segredo, credencial,
dado pessoal ou dump de sessão está versionado nela depois da sanitização.

Risco residual: baixo, e concentrado em repositórios de produto — não nesta base.

## 8. Revisão periódica

| Gatilho | Ação |
|---|---|
| Novo snapshot de corpus | repetir §2.2 antes de commitar |
| Qualquer documento citando sessão, credencial ou host | inspeção manual obrigatória |
| Trimestral | repetir a varredura completa (11 classes) |
