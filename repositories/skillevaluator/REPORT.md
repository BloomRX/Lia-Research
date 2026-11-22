# NVIDIA SkillEvaluator — avaliação de Skills de agente em 3 níveis, com templates de CI reutilizáveis

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-010` |
| Nome | NVIDIA/SkillEvaluator |
| Tipo | repositorio |
| Fonte oficial | https://github.com/NVIDIA/SkillEvaluator · https://docs.nvidia.com/skills/skillevaluator/ |
| Responsável | NVIDIA Corporation & Affiliates |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | BLOCKED |
| Recomendação | **ADAPT** |
| Decisão de adoção | — nenhuma registrada |
| Categoria | studio (leitura transversal em agents, licensing, security) |
| Projetos beneficiados | Lia Agent Hub (validação de catálogo), Lia Studio, Lia Project, Lia Research |
| Versão analisada | `4964c8b301cadbc121e126c268d06e201047133c` (main, 2026-11-21T20:38Z) |
| SHA completo | `4964c8b301cadbc121e126c268d06e201047133c` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — conferido contra o HEAD de `main` na coleta |
| HEAD atual | `4964c8b301cadbc121e126c268d06e201047133c` (muito ativo: push no dia da análise) |
| Data | 2026-11-22 |
| Última verificação | 2026-11-22 |
| Upstream conferido | 2026-11-22 · HEAD `4964c8b3` · sem mudança desde a análise |
| Próxima revisão | 2027-02-20 |
| Licença | Apache-2.0 (`CONFIRMED` em `LICENSE`, `NOTICE` e SPDX em 301 de 306 arquivos do `src`) |
| Confiança | Alta para estrutura, documentação e bloqueio; média para os números de regras (não contados) |

---

## 1. O que é

Ferramenta para **avaliar Skills e plugins de agente** — não para executá-las. O recorte é o que
falta no ecossistema Lia hoje: uma Skill entra no catálogo do Hub com `trust: unreviewed` e nada a
valida. O SkillEvaluator é parte do pipeline *NVIDIA Verified Skills* e define o que "revisar"
significa, em três níveis:

| Nível | O que faz | O que exige |
|---|---|---|
| **Tier 1** | qualidade, schema, versão, PII, licença, Unicode, lint de scripts, *harness check* — e usa SkillSpector, Gitleaks, Bandit e Semgrep opcional para segurança | nenhum LLM; instaladores de scanners externos |
| **Tier 2** | deduplicação e **overlaps semânticos** entre Skills | chave gratuita do NVIDIA Build (embeddings) |
| **Tier 3** | **avaliação com agente vivo**, medindo o *lift* da Skill no resultado da tarefa | chave + Docker + dataset revisado |

Há também `skillevaluator quality-check ./minha-skill`, declarado como "sem chave, sem scanner, sem
GPU, sem Docker", produzindo nota sobre 100 com limiar padrão 70.

## 2. Por que importa para o Lia Agent Hub

O catálogo do Hub tem 48 registros, todos `trust: unreviewed` / `lifecycle: quarantined`, 47 sem
licença no payload e **zero** verificações. O roadmap do Hub propõe criar `lia-skill-intake` e
`lia-repo-audit`. Este objeto mostra que o problema já tem uma solução madura, Apache-2.0, com
**templates de CI prontos** — que é exatamente o formato que o Hub precisa para não virar
mantenedor de ferramenta de avaliação.

| Capacidade do Hub que hoje não existe | Coberta por |
|---|---|
| detectar Skills redundantes fazendo o mesmo trabalho | Tier 2 (overlaps semânticos) — é literalmente o item §Etapa 2 do pedido do proprietário |
| provar que uma Skill carrega licença e NOTICE | Tier 1 (license check) + SPDX por arquivo + `NOTICE` |
| impedir que um catálogo cresça por inércia | Tier 2 + gate de qualidade numérica por release |
| dizer se a Skill **funciona** em cada host | Tier 1 *harness check*: a saída documentada lista por host (`claude-code`, `opencode`, `hermes`, `openclaw`, `copilot-cli`…) o motivo da falha, ex.: "description is 1.028 UTF-16 units, 4 over the 1.024 limit" |
| medir efeito, não presença | Tier 3 com e sem Skill |

O *harness check* é o ponto mais subestimado: o limite de `description` **contado em unidades
UTF-16** por host é o tipo de regra que um catálogo próprio nunca vai descobrir sozinho, e é o que
explica por que uma Skill "listada" não é uma Skill "utilizável" — a mesma distinção que esta base
precisou fazer na mão ao avaliar as Skills do Hub.

## 3. O que foi executado aqui (e o que bloqueou, com causa exata)

Ambiente: sandbox Linux, CPython **3.11.2**, tarball do commit pinado, venv isolado. Nenhuma chave,
nenhum Docker, nenhum download fora do PyPI.

| Etapa | Resultado |
|---|---|
| `pip install` das 10 dependências declaradas no core | **sucesso** |
| `python -c "import skillevaluator"` com `PYTHONPATH=src` | **sucesso** — o pacote importa em 3.11 |
| `python -m compileall -q src` | **falha**: 3 de 306 arquivos não compilam em 3.11 — `tier3/harbor/local_sandbox.py:723`, `inference/retry.py` e `_ci_onboarding_git.py`, todos com `SyntaxError: f-string expression part cannot include a backslash` (PEP 701, sintaxe de 3.12+). Os outros 303 compilam |
| `skillevaluator --help` | **falha antes da análise**: o `import` do CLI resolve `Tools` → `ExternalTool("SkillSpector", …, managed=True)` → `managed_skillspector_wheel()` → `_runtime_path()` → `import skillevaluator.tier3.harbor.local_runtime` → esbarra no `SyntaxError` acima |
| `pytest tests/validators` (com as correções de ambiente) | **59 erros de coleta** pelo mesmo encadeamento |

Dois achados que só apareceram ao tentar executar:

1. **o bloqueio não é o portão de versão, é o grafo de import.** `requires-python = ">=3.12,<3.15"`
   está certo no metadado, mas o mecanismo é mais fundo: três módulos usam sintaxe de 3.12, e um
   deles é alcançado **pelo caminho de Tier 1**. Ou seja, "Tier 1 sem chave" é verdadeiro quanto a
   LLM, mas **não** quanto a runtime: o Tier 1 tenta resolver/instalar scanners no momento do
   `import`, e a resolução passa por módulos do Tier 3. Em um ambiente sem rede para o PyPI, isso
   é um bloqueio absoluto.
2. **consequência prática para qualquer intake automatizado**: um validador que precisa instalar
   ferramentas externas no primeiro `import` não roda em sandbox restrito. Para o Hub, isso significa
   que a validação tem de viver **na CI do repositório** (onde os templates deles foram desenhados
   para rodar), não dentro de uma sessão de agente.

O que teria destravado: Python 3.12+ (não instalável aqui sem rede fora do permitido) e acesso de
rede para instalar os wheels dos scanners. Nenhum dos dois foi tentado — instalar toolchains e
baixar binários fora da allowlist está fora do escopo desta atividade.

## 4. Qualidade de engenharia, medida no que foi lido

| Sinal | Medição |
|---|---|
| Testes | **541 arquivos `test_*.py`** (560 `.py` em `tests/`) contra 306 módulos em `src/` |
| Portes | 223.895 linhas em `src/` |
| Proveniência de licença | SPDX `Copyright (c) 2026 NVIDIA…` + `SPDX-License-Identifier: Apache-2.0` em **301 de 306** arquivos do `src`; `NOTICE` próprio |
| Governança | `GOVERNANCE.md`, `SECURITY.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md`, `RELEASING.md`, `CONTRIBUTING.md`, `CITATION.cff`, `sonar-project.properties` |
| Documentação | 11 documentos só de referência de níveis (`tier1-reference`, `tier2-deduplication`, `tier3-grading`…), site em docs.nvidia.com (Fern), `docs/AGENTS.md` |
| CI como produto | `ci/templates/{github,gitlab}`, `ci/Dockerfile.tier1`, `ci/bundles/0.7.0…1.0.1`, `ci/run_tier1.py`, `ci/bootstrap_tiers.py`, `ci/verify_provenance.py` |
| Higiene de fronteira | `config/oss_boundary_allowlist.json` + testes que mutam cada regra do scanner para provar que a política nega, e que o **próprio código do scanner não casa com suas expressões de deny construídas** |
| Nota de release | o CHANGELOG é **pinned por teste**: `tests/changelog_entries.py` exige que a entrada exista exatamente uma vez (`assert len(found) == 1`) |
| Segurança como hábito | `Unreleased → Security` no CHANGELOG atualizando LiteLLM/AWS SDK e **rejeitando overrides HTTP de endpoint quando há bearer auth** |

Dois costumes valem cópia imediata, independentemente de adotar a ferramenta:
**SPDX por arquivo** com teste que confere, e **entry de changelog verificada por asserção**. O
primeiro é a lacuna exata das 47 Skills do Hub; o segundo é o que impede o tipo de divergência
índice × relatório que esta base caça com `tools/validate.py`.

## 5. Limitações e contrapesos

- **Volume.** 224 mil linhas de `src/` e 541 arquivos de teste são um projeto, não uma biblioteca. O
  Lia não tem condição de manter um fork. `ADAPT` aqui é **aos padrões e ao formato dos gates**, não
  ao pacote.
- **Requer Python 3.12–3.14.** Na data, a sandbox padrão de muitas sessões (incluindo esta base) é
  3.11 → o gate de versão é real, não cosmético. Vale comparar: é o mesmo motivo que bloqueou
  `anybase` para o objeto Bosch (`LR-FORGE-011`) no mesmo ciclo de rodadas.
- **Acoplamento de scanners.** 6 ferramentas externas (Gitleaks gerenciado, pip-audit, Safety,
  Bandit, Semgrep, SkillSpector) — cobertura boa, superfície de suprimento também. A existência de
  `SKILLEVALUATOR_BANDIT_PATH`/`SEMGREP_PATH`/`SKILLSPECTOR_PATH` mostra que o projeto já previu
  ambiente restrito; **não encontrei** variável equivalente para pular a resolução do Gitleaks/
  SkillSpector gerenciados no `import` (só `--tiers`/flags de execução).
- **Números de marketing não conferidos:** "500+ static rules", ranking no Artificial Analysis e o
  paper arXiv 2608.20614. Registro como `REPORTED`. Contar regras exigiria ler os pacotes de
  validadores, o que não foi feito.
- **Tier 2/3 exigem chave do NVIDIA Developer Program** e o Tier 3 exige Docker — ambos ausentes
  aqui: `BLOCKED`, não `FALHA`.

## 6. Compatibilidade com o ecossistema Lia

| Alvo | Encaixe |
|---|---|
| Lia Agent Hub | alto, **como CI do repositório de catálogo**: template `github-skill-checks.yml` sobre os 48 registros, Tier 1 primeiro; a decisão de publicar/promover continua sendo do humano |
| Lia Studio / Project | uso local de `quality-check` antes de propor uma Skill nova — o "não criar Skill se uma existente resolve" ganha um critério numérico em vez de discussão |
| Lia Research | o *harness check* por host é o formato que faltava para a coluna "disponível no Arena" ser verificada, não opinada |
| Lia Model Lab | nenhum |

Ressalva de vocabulário: o nível de "aprovação" do SkillEvaluator é técnico (nota, findings,
limiar 70). Ele **não substitui** `trust:`/`lifecycle:` do Hub, que são política de curadoria — e
política continua fora da autoridade desta base (`MISSION.md` §3, `agents/RESEARCH-ORCHESTRATOR.md` §0).

## 7. Recomendação

**`ADAPT`** — adaptar três coisas, sem incorporar o projeto:

1. **o formato do gate em três níveis** (estático → redundância → efeito medido), com o nível estático
   rodando sem chave em CI;
2. **SPDX por arquivo + `NOTICE`, com o próprio validador conferindo** — aplicável hoje aos 48
   registros do Hub e às Skills do Studio/Project;
3. **o *harness check* como coluna do catálogo**: "em quais hosts esta Skill carrega, e por que não
   em outros", no lugar de uma promessa genérica de compatibilidade.

Não é `DIRECT_INTEGRATION_CANDIDATE`: exige 3.12+, instala ferramentas externas no `import`, tem
224 mil linhas e o Lia não tem mantenedor para isso. A mudança de veredito teria gatilho objetivo:
se o projeto passar a expor o Tier 1 sem resolução de scanners no `import` (flag ou import lazy), o
uso em CI local do Hub volta à mesa.

## 9. O que falta no Lia hoje, e que este objeto evidencia

| Lacuna do Lia | Estado hoje | O que o SkillEvaluator prova ser necessário |
|---|---|---|
| validação de Skill no intake | não existe; `agents/SKILLS-OPERATING-SET.md` lista 48 registros, todos `unreviewed` | um gate **estático e sem chave**, rodando na CI do próprio catálogo |
| licença por Skill | 47 de 48 sem licença no payload | SPDX por arquivo é viável em escala (301/306 aqui) e testável |
| "a Skill está disponível no host X?" | a resposta é opinião | o harness check responde por host, com o motivo da falha |
| evidência de que a Skill **ajuda** | não se mede em nenhum projeto Lia | é para isso que existe o Tier 3; a ausência dele explica "listada" ≠ "útil" |
| changelog confiável | `RESEARCH-CHANGELOG.md` é mantido à mão e conferido por regras desta base | entrada de changelog **pinada por asserção de teste** é o estágio seguinte |
| ambiente de execução do agente | Python 3.11 na sandbox | uma ferramenta de gate que exige instalar scanners no `import` não roda aqui — o gate precisa ser leve por construção |

## 10. Evidências

| Afirmativa | Rótulo | Base |
|---|---|---|
| `pip install` das deps ok; `import skillevaluator` ok em 3.11 | `OBSERVED` | execução nesta sessão, venv 3.11.2 |
| 3 de 306 arquivos do `src` não compilam em 3.11 (PEP 701); CLI e suíte bloqueados pelo mesmo encadeamento | `OBSERVED` | `compileall`, traceback do `--help`, coleta de `pytest tests/validators` (59 erros) |
| 541 `test_*.py`; 223.895 linhas em `src`; SPDX em 301/306 | `CONFIRMED` | contagem direta no tarball do commit |
| tiers, requisitos de cada um e o `quality-check` sem chave | `REPORTED` | `README.md` + `docs/tier*.mdx` lidos no commit |
| harness check com motivos por host e limite de 1.024 unidades UTF-16 | `REPORTED` | saída exemplo no `README.md` |
| templates de CI GitHub/GitLab, `Dockerfile.tier1`, bundles por versão | `CONFIRMED` | `ci/` listado no commit |
| mudança de licença/dependências em `Unreleased → Security` | `CONFIRMED` | `CHANGELOG.md` |
| "500+ static rules"; #1 em leaderboard; arXiv 2608.20614 | `UNVERIFIED` | não conferidos aqui |
| Tier 2 e Tier 3 executados; dedup sobre as 48 Skills do Hub; lift de Skill | `BLOCKED` | sem 3.12, sem chave, sem Docker; nenhum testado |
| ★4.335 · 557 forks · 76 issues · criado 2026-06-24 · push 2026-11-21 | `CONFIRMED` | API do GitHub, 2026-11-22 |

## 11. Próximos passos

1. Se o Hub quiser o gate: **copiar o formato, não o software** — um `tools/validate.py` do Hub com
   checagem de SPDX + `NOTICE` + `description` por host é ~200 linhas, e o validador desta base já
   prova que o padrão funciona em escala pequena.
2. Reavaliar o SkillEvaluator como dependência **só** se aparecer uma versão que rode o Tier 1 sem
   rede e sem 3.12 — ou se o Hub ganhar CI com 3.12 e permissão de instalar scanners.
3. Revisão em 2027-02-20: projeto ativo (5 releases em 5 meses, `v1.0.1` em 2026-11-18), prazo curto
   por isso.

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · esquema `catalog/CATALOG-SCHEMA.md` · contexto em `cross-project/agents/SKILLS-MCP-LANDSCAPE.md` e `projects/lia-agent-hub/INDEX.md`.
