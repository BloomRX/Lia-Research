# Consolidação — licença e proveniência de Skills

| Campo | Valor |
|---|---|
| ID | `LR-LIC-001` |
| Categoria | licensing |
| Projetos | Lia Agent Hub (primário), Studio, Project, Model-Lab, Forge |
| Fontes | `Lia-AgentHub@bd4bfbb:docs/research/SKILL-LICENSE-AND-PROVENANCE-AUDIT.md` (36 KB, consultas de 2026-11-15), `LIA-SKILLS-INVENTORY.md` (37 KB), `Lia-Studio:docs/licenses/*`, verificação de árvore em 2026-11-17 |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | **Alta** (o original lê commits e licenças uma a uma) |

---

## 1. O número que importa

| Métrica | Valor | Rótulo |
|---|---:|---|
| Skills catalogáveis no ecossistema | 48 | CONFIRMED |
| Autorais/adaptadas pela Lia | 47 | CONFIRMED |
| **Com licença dentro do payload** | **0** | CONFIRMED |
| Terceiro vendorizado com patches | 1 (`alethe`) | CONFIRMED |
| Skills AIRI vendorizadas no Lia-Project | 29 | CONFIRMED |
| Skills de terceiros em ZIP no Studio (não importadas) | 20 | CONFIRMED |
| Skills em `main` de qualquer repositório | 9 (só Model-Lab) | CONFIRMED |

Consequência mecânica: o importador do Hub detecta licença **apenas por arquivo na raiz
do payload** (`adapters/importer.py::_detect_license`). Logo, as 47 entrariam como
`licenseKnown: false`. Isso não é bug de código; é ausência de decisão.

## 2. Classes de aproveitamento (do original, preservadas)

| Classe | Teste |
|---|---|
| `USE_AS_IS` | licença própria, permissiva, obrigações compatíveis, sem modificação |
| `ADAPT_ALLOWED` | permite derivação com condições (atribuição, aviso, às vezes mesma licença) |
| `FORK_CANDIDATE` | há motivo técnico para fork próprio, preservando avisos |
| `INDEPENDENT_REIMPLEMENTATION` | ideia/comportamento público reimplementável sem copiar material |
| `RESEARCH_ONLY` | útil para estudo, mas falta licença/clareza/autorização |
| `BLOCKED` | copyleft de rede, NC, ND, ausência de licença ou impedimento |

## 3. Terceiros já consumidos — estado real

| Upstream | Licença lida | Uso no ecossistema | Classe | Pendência |
|---|---|---|---|---|
| `Donchitos/Claude-Code-Game-Studios` | MIT © 2026 Donchitos | 7 skills no Studio (commit `05ad7c8` verificado) | `ADAPT_ALLOWED` | aviso MIT fora do payload → **violação em export** |
| `witnesstodark/mr-mak-workspace` | MIT © 2026 (+ `img2threejs` Apache-2.0) | 5 skills no Studio + ZIP 9,9 MB | `ADAPT_ALLOWED` / `RESEARCH_ONLY` | ler licença do subprojeto; decidir destino do ZIP (`DR-0004`) |
| `Kc1t/alethe-orchestrate-skill` | a verificar | 1 skill vendorizada no Project | `FORK_CANDIDATE` | registrar patches |
| AIRI (`moeru-ai/airi`) | a verificar versão vendorizada | 890 arquivos doc + 29 skills no Project | `RESEARCH_ONLY` | auditoria completa ausente |
| `anthropics/skills` | a verificar | referência | `RESEARCH_ONLY` | — |

## 4. O achado de empacotamento

12 Skills do Studio têm seção `## Origem` com link para o arquivo no commit exato do
upstream — **boa prática, rara**. Mas o texto MIT está em `docs/licenses/` na raiz do
repositório. Se uma Skill for exportada sozinha (objetivo declarado do Hub), a
obrigação de atribuição não viaja com ela.

**Correção mínima:** cada payload de Skill derivada inclui um `NOTICE` (ou o texto da
licença) dentro da própria pasta. O formato `.lia-capability` já prevê arquivos de
NOTICE — ou seja, o contêiner existe e está vazio.

## 5. O que a Lia não pode presumir

Declarar autoria (feito pelo proprietário) **não** concede licença de distribuição.
Até `DR-0001` ser decidido, toda Skill `lia-*` é "uso interno, sem redistribuição".

## 6. Referências externas que resolvem o problema

| Fonte | Prática a copiar |
|---|---|
| `ManimGX` (`LR-FORGE-003`) | árvore `LICENSES/` com uma licença por arquivo (padrão REUSE) |
| `rescript-lang/rescript` (`LR-STUDIO-003`) | `LICENSE` com mapa por diretório quando há licença mista |
| `pixelfx` (`LR-FORGE-004`) | `NOTICE.md` por camada (código, efeito adaptado, fonte excluída) |
| `Meldwork` (`LR-AGENT-003`) | `COMMERCIAL_USE.md` respondendo a pergunta comercial |
| `misterdownloadmanager` | GPL: exemplo de licença que impede incorporação |

## 7. Ações recomendadas (não executadas)

1. `DR-0001`: decidir licença das Skills `lia-*` (proprietário).
2. Adotar `NOTICE` + `LICENSES/` por Skill (padrão REUSE).
3. Corrigir as 12 Skills do Studio e as 5 do mr-mak (bloqueio legal).
4. Auditar as 29 skills AIRI e separar o que é Lia do que é upstream.
5. Decidir o destino do ZIP de 9,9 MB (`DR-0004`).
