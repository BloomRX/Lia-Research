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
| `witnesstodark/mr-mak-workspace` | MIT © 2026 (+ `img2threejs` Apache-2.0, lido na origem) | 5 skills no Studio + ZIP 9,9 MB | `ADAPT_ALLOWED` / `RESEARCH_ONLY` | subprojeto ok (sem `NOTICE` no upstream); ZIP: registrar tag + hash em vez de removê-lo por desconhecimento |

> Atualizado 2026-11-22: a licença do subprojeto foi lida na origem, junto do pacote de
> 20 Skills do autor (`repositories/mr-mak-workspace/REPORT.md`, `LR-STUDIO-012`). Duas coisas mudam
> aqui: (a) o autor **declara `license:` no frontmatter de cada `SKILL.md`** — o mecanismo de custo
> mínimo que a §3 deste documento propõe já existe em produção, com `MIT` no `last30days-skill` e
> `Apache-2.0` no `img2threejs`; (b) o pack publicado deles traz `manifest.json` com SHA-256 por
> arquivo, `LICENSE` e `THIRD_PARTY_NOTICES.md` dentro do ZIP — o nosso ZIP não tem nada disso.
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

### 4.1 A instrução da Skill é material licenciado (medido em 2026-11-25)

`nanocle/Charakuru` (`LR-FORGE-020`, dossiê em `repositories/charakuru/REPORT.md`) é o primeiro caso
lido nesta base em que a licença **declara as Skills como parte do material coberto**: *"Covered
Materials means the original application code, scripts, **Skills (including their instructions and
reference text)**, and documentation"*. E o §10 do mesmo arquivo escreve a incerteza dentro do
disclaimer: *"SKILLS AND AI-ASSISTED WORKFLOWS MAY BE EXPERIMENTAL AND MAY REQUIRE MANUAL
CORRECTION."*

Três consequências para o Hub, como pergunta, não como tarefa:

| Fato medido lá | O que ele pergunta aqui |
|---|---|
| o texto da instrução tem dono e termos próprios, separados do código | as 48 records do conjunto operacional e as Skills `lia-*` têm algum registro de que o **texto** é da Lia, e sob que termos ele circula quando um agente o copia para outro projeto? |
| redistribuir Skill fora do pacote exige autorização, mesmo com fork permitido | um Skill exportado por runtime para outro app é "cópia privada" ou "distribuição"? A §2 do modelo deles separa os dois com uma frase; a nossa `DR-0001` ainda não tem essa frase |
| o disclaimer de garantia nomeia as Skills, não só o software | se o Hub declara "as instruções podem exigir correção manual" em algum lugar, isso é política de produto; aqui é uma linha de licença |

Nada disto foi aplicado ao Hub pela Research. É precedente externo, com texto verificável, para a
pergunta que a `DR-0001` já tem em aberto.

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
5. Registrar tag + `sha256` do pacote do Studio no aviso de terceiros deles e decidir quando reempacotar (`DR-0004`). **A medição já foi feita pela Research em 2026-11-25, sem tocar no Studio**: o arquivo `docs/Mr-Mak-Skills-Free.zip` (3.352.656 B comprimidos; 9.940.122 B extraídos, 764 entradas) tem `sha256` idêntico ao asset `Mr-Mak-Skills-0.4.14.zip` publicado na release `v0.4.14` do upstream. Sobra o registro e a decisão de reempacotar — ver §14 de `repositories/mr-mak-workspace/REPORT.md`;
