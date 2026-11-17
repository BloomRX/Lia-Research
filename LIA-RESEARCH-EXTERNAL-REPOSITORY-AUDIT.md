# LIA-RESEARCH — Auditoria de Repositórios Externos

| Campo | Valor |
|---|---|
| Data | 2026-11-17 |
| Objetos | 16 (14 repositórios + 2 organizações) |
| Executado | nada — nenhum clone, instalação, build ou teste |
| Vereditos | ADAPTAR 6 · REFERÊNCIA 6 · REJEITAR 4 |

---

## 1. Tabela mestra

| # | Objeto | SHA | Licença | ★ | Veredito | Valor principal | Bloqueio |
|---|---|---|---|---:|---|---|---|
| 1 | `ha-mcp` | `3dd26d45` | MIT | 7.934 | **ADAPTAR** | 86 tools + read-only + catálogo + in-process | 2 GHSAs em beta; 2 servidores/cliente travam |
| 2 | `OpenJarvis` | `6656b7fe` | Apache-2.0 | 16.276 | **REFERÊNCIA** | contrato `InferenceEngine`, guardrails como decorator, energia/FLOPs | alpha; NVIDIA; telemetria |
| 3 | `vercel-labs/ui` | `10b3b6c0` | Apache-2.0 + beta | 5.468 | **ADAPTAR** | comportamentos headless + adaptador Vue real | beta terms; nenhum dado de bundle |
| 4 | `misterdownloadmanager` | `d9a9ef06` | **GPL-3.0** | 11.806 | **REFERÊNCIA** | fila/retomada de download | copyleft; projeto de 3 semanas |
| 5 | `claude-trading-skills` | `a627d17d` | MIT | 6.772 | **ADAPTAR** | manifesto de workflow + skillsets | domínio financeiro proibido |
| 6 | `openidea` | `18228564` | Apache-2.0 | 9.279 | **REFERÊNCIA** | divisão em crates; plugin SDK | Studio não é IDE |
| 7 | `routerhubSI` | n/a (org) | MIT/NOASSERTION | 413–351 | **REJEITAR** | — | sem backend; sem ToS |
| 8 | `SculptForge` | `363e2b86` | **GPL-3.0** | 722 | **REFERÊNCIA** | benchmark pack com hardware declarado | copyleft |
| 9 | `cc-game-studios` | `abc0de79` | MIT | 39.886 | **ADAPTAR** | 582 arquivos de fluxo de estúdio de jogo | 0 CI; material muito grande |
| 10 | `manimgx` | `1fb4dd73` | mista (6) | 2.784 | **REFERÊNCIA** | árvore `LICENSES/` (REUSE) + fixtures com hash | CC-BY-SA em parte |
| 11 | `meldwork` | `db9b6c84` | Apache-2.0 | 1.586 | **REFERÊNCIA** | permissão com escopo por execução | macOS-only |
| 12 | `plannotator` | `b5b30778` | Apache-2.0 | 12.935 | **REFERÊNCIA** | contrato de revisão humana + 63 ADRs | sem relação direta com produto |
| 13 | `pixelfx` | `5294518c` | MIT + NOTICE | 7.932 | **ADAPTAR** | NOTICE por camada de conteúdo | 0 testes; fonte fora da licença |
| 14 | `unslop` | `0f4a07f5` | **nenhuma** | 1.132 | **REJEITAR** | vocabulário de avaliação | sem licença = sem direito |
| 15 | `rescript-lang` | n/a (org) | LGPL no `compiler/` | 7.486 | **REJEITAR** | `LICENSE` com mapa por diretório | incompatível com Vue; LGPL |
| 16 | `ai-design-skills` | `456d9e0d` | MIT | 15.818 | **ADAPTAR** | molde de skill de design | só 9 arquivos — pouco corpo |

## 2. Distribuição de vereditos e o que significa

| Veredito | N | Leitura |
|---|---:|---|
| ADAPTAR | 6 | há padrão ou componente que vale em escopo restrito, com gate |
| REFERÊNCIA | 6 | conhecimento útil; integração proibida |
| REJEITAR | 4 | nem como referência técnica: sem licença, incompatível, ou sem substância |
| ADOTAR | **0** | nenhum objeto mereceu adoção direta — e essa é a conclusão, não um erro |

**Zero `ADOTAR` é resultado, não omissão.** Adoção exige execução, e a ordem de serviço
proíbe implementar durante a pesquisa.

## 3. Padrões que a Lia deveria copiar (independente do repositório)

| Padrão | Origem | Onde aplicar | Custo |
|---|---|---|---|
| Licença declarada dentro do artefato distribuível | pixelfx, manimgx | toda Skill exportável | baixo |
| Contrato único de engine (`generate/stream/list_models/health`) | OpenJarvis | provider da Lia | baixo |
| Segurança como decorator, não espalhada | OpenJarvis | broker de tools | médio |
| Read-only por conexão | HA-MCP | tools de risco | baixo |
| Catálogo por URL (cheio × busca) | HA-MCP | catálogo de Skills/MCP | médio |
| Permissão com escopo por execução | Meldwork | orquestração multi-agente | alto |
| Benchmark com hardware declarado | SculptForge | bancada de modelo | baixo |
| Fixture com hash | ManimGX | testes de render | baixo |
| Revisão humana como contrato (anotar → devolver) | Plannotator | revisão de artefato gerado | médio |
| ADR por decisão datada (63 no repo) | Plannotator | toda decisão de UI/produto | quase zero |

## 4. Armadilhas encontradas (evidência, não opinião)

| Armadilha | Objeto | Rótulo |
|---|---|---|
| Badge de licença mente nos dois sentidos | `rescript` mostra "Other" mas é LGPL+MIT por pasta; `unslop` sem badge **não** tem licença | CONFIRMED |
| "Peer-reviewed / acadêmico" não é validação no hardware do usuário | OpenJarvis | CONFIRMED |
| Beta com termos separados da licença | vercel-labs/ui | CONFIRMED |
| Dois servidores MCP no mesmo cliente travam | HA-MCP | REPORTED |
| Docker `--rm` perde estado de auth | HA-MCP | CONFIRMED (doc) |
| Cliente com bug em HTTP MCP | Codex (`#11284`) | CONFIRMED (issue) |
| Org de "API de modelo" sem backend publicado | routerhubSI | CONFIRMED (11 repos, nenhum backend) |
| Repositório grande com 0 CI | cc-game-studios (582 arquivos, 0 workflow) | CONFIRMED |
| Projeto com 355 arquivos de avaliação e nenhuma licença | unslop | CONFIRMED |

## 5. O que não foi verificado (e não pode ser citado como fato)

| Item | Rótulo | Por quê |
|---|---|---|
| Qualquer número de desempenho de qualquer objeto | `UNVERIFIED` | nada executado |
| Compatibilidade de qualquer objeto com RX 580 | `UNVERIFIED` | nada executado |
| Estabilidade de 86 tools do HA-MCP em uso real | `UNVERIFIED` | só documentação |
| Qualidade de saída de `ai-design-skills` | `UNVERIFIED` | 9 arquivos, sem uso |
| Retenção/ToS do RouterHub | `BLOCKED` | não publicado |
| Licença das 28 skills AIRI | **resolvido em 2026-11-17** | `LR-LIC-003`: 4 `USE_AS_IS`, 5 `ADAPT_ALLOWED`, 19 `RESEARCH_ONLY` |

## 6. Recomendação

Nenhum dos 16 objetos justifica mudança de arquitetura hoje. Seis justificam um
protótipo isolado **depois** de decisão do projeto. Dois exigem parecer jurídico antes de
qualquer contato com código (MDM, SculptForge — ambos GPL).

O item de maior valor imediato não é código: é **copiar os hábitos de registro**
(ADR datado, NOTICE por camada, licença dentro do artefato). Custo quase zero, e resolve
os dois maiores passivos internos.
