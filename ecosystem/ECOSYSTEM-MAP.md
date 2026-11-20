# Mapa do ecossistema Lia

Medido em 2026-11-17 via GitHub API (metadados, branches, trees). Números de
documentos são contagens de arquivos, não de conclusões.


Documentos irmãos desta pasta: [`SHARED-TECHNOLOGY-MAP.md`](SHARED-TECHNOLOGY-MAP.md) (stack e hardware que atravessam projetos) · [`PROJECT-OWNERSHIP.md`](PROJECT-OWNERSHIP.md) · [`CROSS-PROJECT-CAPABILITIES.md`](CROSS-PROJECT-CAPABILITIES.md).

---

## 1. Os cinco projetos da ordem de serviço

| Projeto | Repositório real | Branch padrão | Tipos de pesquisa | Observação |
|---|---|---|---|---|
| Lia-Project | `BloomRX/Lia-Project` | `main` @ `9c7ac18` (2026-10-30) | voz, providers, arquitetura desktop, segurança, UI/UX | 12 branches remotas; `main` está **349 commits** atrás da branch de sessão mais recente (577) |
| Lia Forge | `BloomRX/Lia-Forge` | `main` @ `6bd9a5a` (2026-11-13) | 3D, Blender, animação, pipelines de asset, MCP | `main` tem **4 commits**; 13 documentos de pesquisa vivem em branches |
| Lia Studio | `BloomRX/Lia-Studio` | `main` @ `ba70d22` (2026-10-30) | engine de jogo, gameplay, UX de editor, skills de gamedev | `main` tem **4 commits**; 15 documentos em `docs/research/` fora de `main` |
| Lia Agent Hub | `BloomRX/Lia-AgentHub` ⚠️ | `main` @ `34a27f4` (2026-11-14) | skills, catálogo, licença, segurança, arquitetura | **O nome não é `Lia-Agent-Hub`.** O caminho da OS não resolve (404) |
| Lia Model Lab | `BloomRX/Lia-Model-Lab` | `main` @ `3ec4313` (2026-11-02) | modelos locais, hardware Windows/AMD, LFM3, governança de experimento | 8 ADRs; `docs/SOURCES.md` com 26 KB de fontes |

⚠️ **Correção de nome confirmada**: `BloomRX/Lia-Agent-Hub` retorna
`Could not resolve to a Repository`. O repositório existente é `BloomRX/Lia-AgentHub`
(criado 2026-11-15, 3 MB, 5 branches). Qualquer automação que use o nome com hífens
falha silenciosamente.

## 2. Repositórios adjacentes (fora dos cinco, mas parte do ecossistema)

| Repositório | Tamanho | Papel aparente |
|---|---|---|
| `BloomRX/Lia-Go` | 10 MB | variante leve? (não investigado nesta fundação) |
| `BloomRX/LiaVoiceStudio` | 5,6 MB | estudo de voz (citado indiretamente na pesquisa de voz) |
| `BloomRX/3d-create` | 567 MB | referência de pipeline 3D (citado em auditoria de consolidação do Forge) |
| `BloomRX/3d-sprite` | 1 MB | referência de sprites |
| `BloomRX/ChibiCreate` | 10 MB | referência de personagem |
| `BloomRX/ComfyUI_Colab` | 110 MB | notebook de geração |
| `BloomRX/SilksongREA` | 430 KB | fora do escopo Lia |
| `BloomRX/animations-free` | 82 KB | assets |

Todos os 14 repositórios do usuário estão com visibilidade **pública** em 2026-11-17.
Isso é relevante para a política de segurança: ver `archive/historical/LIA-RESEARCH-FOUNDATION-REPORT.md` §2.

## 3. Fluxo de conhecimento observado

```text
        [sessão de agente]
                │
                ▼
   branch arena/* ou codex/*        ← 43 branches nos cinco projetos
                │
     (nem sempre integrada)
                │
                ▼
          main do projeto           ← em 4 dos 5 projetos, muito atrás
```

Consequência medida: **511 dos 1.620 documentos distintos existem apenas fora de
`main`**. Leitura direta de `main` em qualquer um dos cinco projetos entrega uma
fração do conhecimento real.

## 4. Volume de documentação por projeto

| Projeto | Arquivos totais (todas as branches) | Documentos distintos | De autoria Lia | Vendorizado |
|---|---:|---:|---:|---:|
| Lia-Project | 55.177 | 1.236 | 261 | 975 (`airi/` e afins) |
| Lia Forge | 1.345 | 128 | 128 | 0 |
| Lia Studio | 1.019 | 109 | 109 | 0 |
| Lia AgentHub | 250 | 57 | 57 | 0 |
| Lia Model-Lab | 687 | 90 | 90 | 0 |
| **Total** | **58.478** | **1.620** | **645** | **975** |

## 5. Onde está o risco de perda

| Risco | Evidência | Impacto |
|---|---|---|
| Pesquisa só em branch de sessão | 511 documentos | branch apagada = conhecimento apagado |
| `main` desatualizada | Lia-Project `main` 349 commits atrás | agente que lê `main` recebe estado antigo |
| Vendorização sem isolamento | 975 arquivos de doc upstream dentro do Lia-Project | confusão de proveniência e licença |
| Duplicação de Skill | `lia-brand-check` ≈ `lia-brand-consistency-review`; 3 skills de orquestração | manutenção divergente |
| Nome de repositório errado em documento | `Lia-Agent-Hub` | automação quebrada |

## 6. O que este mapa não cobre

- `Lia-Go`, `LiaVoiceStudio` e os repositórios de asset não foram inventariados
  documento a documento (`NOT RUN`, prioridade menor).
- Commits anteriores a 2026-09 não foram analisados.
- Branches locais não remotas não são visíveis por API e não foram consideradas.
