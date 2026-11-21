# image-render-generative (Bosch Research) — refinamento generativo sobre render sintético

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-011` |
| Nome | image-render-generative |
| Tipo | repositorio |
| Fonte oficial | https://github.com/boschresearch/image-render-generative |
| Responsável | Bosch Research (Bosch Engineering GmbH / Robert Bosch GmbH) |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | PARTIAL |
| Decisão de adoção | — nenhuma registrada |
| Categoria | forge (leitura transversal em model) |
| Projetos beneficiados | Lia Forge (forma de pipeline), Lia Model Lab (referência de ControlNet) |
| Versão analisada | `ba2a9608e885130b8154f316da667a22e3347ae4` (main, 2024-08-29) |
| SHA completo | `ba2a9608e885130b8154f316da667a22e3347ae4` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — conferido contra o HEAD de `main` na coleta |
| HEAD atual | `ba2a9608e885130b8154f316da667a22e3347ae4` (sem mudança desde a versão analisada) |
| Data | 2026-11-21 |
| Última verificação | 2026-11-21 |
| Upstream conferido | 2026-11-21 · HEAD `ba2a9608` · sem mudança desde a análise |
| Próxima revisão | 2027-05-20 |
| Licença | Apache-2.0 (`CONFIRMED` no `LICENSE.md` e em cabeçalho por arquivo) |
| Recomendação | **REFERENCE_ONLY** |
| Confiança | Alta para licença, estrutura e dependências; Alta para o veredito de inexecutabilidade |

---

## 1. Identificação

- **Repositório:** `boschresearch/image-render-generative` · Python · 65 KB · **42 arquivos** na árvore.
- **Métricas na coleta:** ★0 · 4 forks · criado 2023-11-30 · último push **2024-08-29** (814 dias antes desta análise).
- **Linhas:** `main` @ `ba2a960` (2024-08-29); `stable` @ `40a26cc` (2024-06-07); `feature/docs`.
- **Tags:** `v1.0.0`…`v1.0.3`. O `setup.cfg` deriva a versão de `version.py`, que declara **1.0.4** — a versão da `main` nunca foi publicada como tag.
- **Autodefinição no README:** "software is a research prototype… **not ready for production use**. It has neither been developed nor tested for a specific use case."

## 2. Resumo executivo

É um *plugin* do sistema de render de dados sintéticos **catharsys / image-render** da Bosch: pega as saídas de um render Blender (depth, openpose, semseg) e as passa por modelos generativos (ControlNet multi-controle sobre SD 1.5, ou Prompt-Free-Diffusion) para refinar realismo ou gerar variação.

Para o Lia **Forge**, o valor é **de conceito, não de código**: é a demonstração pública de um formato em que render programático e geração por difusão convivem como *ações* de um mesmo workspace declarativo, com configuração em arquivo e pesos fora do repositório. A execução real é inviável aqui: o repositório é uma peça de um sistema de 17 repositórios e não funciona sozinho.

Veredito: **REFERENCE_ONLY**. Nada foi adaptado, instalado em projeto Lia ou autorizado.

## 3. O que resolve

| Problema | Abordagem usada por eles |
|---|---|
| Render sintético com cara de foto | refinamento por ControlNet sobre os mapas do próprio render |
| Reprodutibilidade de lote | ações declaradas em `manifest/trial/launch.json5` por workspace |
| Dependências incompatíveis entre métodos | um ambiente conda separado por método, criado por script |
| Pesos fora do repositório | `scripts/get_*.sh` / `.ps1` baixam modelos para um diretório central |
| Rastreabilidade de terceiros | `3rd-party-licenses.md` + `NOTICE.md` + cabeçalho de licença em cada `.py` |

## 4. Arquitetura

- Pacote `generative-action-python`, instalado com `pip install -e .`; registra **3 entry points** do grupo `catharsys.action` (`/catharsys/action/generative/apply:1.0`, `.../generative/paint_pose:1.0`, `/catharsys/action/promptfreediffusion/apply:1.0`).
- 11 arquivos `.py` no `src`: 4 em `actions/` (`__init__.py`, `generative.py`, `paint_pose.py`,
  `promptfreediffusion.py`), 6 em `actions/lib/` (3 `cls_*` com a lógica e 3 `call_*` que invocam cada
  método externo) e `util/version.py`.
- Todo o estado vem de **config JSON5** em três níveis (manifest / trial / launch), no padrão do catharsys; o plugin não tem CLI própria — quem executa é o `cathy ws launch -a <acao>`.
- Pré-processamento de mapa (ex.: `Normalize`, `Invert`) é lista nomeada na config, não código do usuário.

## 5. Métodos suportados e estado de cada um

| Método | Base | Estado declarado |
|---|---|---|
| Takuma Multi Control Net | fork `takuma104/diffusers` (branch `multi_controlnet`) de SD 1.5 | documentado como o caminho principal; redes `sd-controlnet-depth`, `control_v11p_sd15_openpose`, `control_v11p_sd15_seg` baixadas por git lfs |
| Prompt-Free-Diffusion | repositório externo referenciado por caminho | ação própria, exige `reference_image` e IDs de difuser/see-coder enumerados |
| ControlNet Nightly | — | marcado **deprecated** no próprio README |

Os pesos de SD 1.5 e dos ControlNets têm licença própria em cada model card. **Não verificado nesta sessão** — ver §10.

## 6. O que impede o uso (testado, não inferido)

Executado em 2026-11-21 (UTC) num venv Python 3.11.2, tarball do commit pinado:

| Passo | Comando | Resultado |
|---|---|---|
| instalar o pacote | `pip install -e .` | **sucesso** — instala `generative-action-python 1.0.4` + `pyjson5 2.0.1` + `tqdm 4.70.1` |
| compilar os fontes | `python -m compileall -q src/` | **sucesso** (exit 0, sem erro de sintaxe em 3.11) |
| importar uma action | `python -c "import catharsys.plugins.generative.python.actions.generative"` | **falha**: `ModuleNotFoundError: No module named 'anybase'` (`generative.py:33`) |
| tentar suprir a dependência | `pip install anybase` | **bloqueado**: no PyPI existe só `anybase 1.1.0`, `Requires-Python >=3.12`, publicado 2026-11-18 — incompatível com o 3.11 do sandbox |
| resolver o resto | — | `catharsys` **não existe no PyPI** (404 em `pypi.org/pypi/catharsys/json`); só vem do workspace image-render |

Duas conclusões que não eram óbvias antes de executar:

1. **o metadado sub-declara dependências** — `setup.cfg` lista apenas `pyjson5` e `tqdm`; `anybase` e `catharsys` são pressupostos do ambiente conda gerenciado pelo `image-render-setup`. Instalar "por conta" produz um pacote que importa e falha na primeira linha útil;
2. **a janela de Python se fechou desde o último push**: o `anybase` atual exige 3.12+, enquanto o código do plugin é de 2024 e não foi ajustado.

## 7. Requisitos de hardware e sistema

- Conda + ambientes por método; scripts `.sh` (Linux) e `.ps1` (Windows) para montar ambiente e baixar redes.
- SD 1.5 com ControlNet: exigência de VRAM **não medida aqui** — nenhuma GPU foi usada, nenhum peso foi baixado. Nada neste relatório autoriza afirmação sobre a RX 580.
- Precisa de um workspace catharsys (Blender + a família image-render) para qualquer execução real.

## 8. Maturidade e manutenção

| Sinal | Observação |
|---|---|
| Atividade | 814 dias sem push; a família inteira parou em 2025-07-31 (478 dias) |
| Comunidade | ★0, 4 forks, nenhuma release no GitHub (só tags) |
| Testes | **nenhum teste automatizado no repositório**; sem CI |
| Documentação | Sphinx em `docs/`, style guide interno, README com exemplos de config por arquivo |
| Governança | `CONTRIBUTING.md` exige **DCO 1.1 e commits assinados com GPG** para contribuir |
| Versionamento | `repos-main.yaml` e `repos-release.yaml` do `image-render-setup` listam 17 repositórios; este aparece em ambos, a linha de release fixada em `tags/v1.0.3` |

O ponto interessante para o Lia é o último: **o manifest da plataforma fixa o plugin numa tag antiga enquanto a `main` já declara versão superior**. É o oposto do que a base do Lia faz hoje com branches de sessão: aqui existe mecanismo de pin por release, e ele é a razão pela qual a defasagem é visível.

## 9. Segurança e privacidade

- Executa modelos locais; o tráfego de rede é o download de pesos (HF/lustfs via git lfs) nos scripts, não em tempo de render.
- Não há sandbox, permissão ou isolamento: é código Python executando como *action* do workspace com acesso total ao sistema de arquivos, como qualquer pipeline Blender.
- Ausência de CI e de testes significa **nenhuma verificação de segurança disponível** — nem do próprio projeto, nem de terceiros (`BLOCKED`).

## 10. Licença e proveniência

| Item | Conteúdo lido |
|---|---|
| Licença do código | Apache-2.0 em `LICENSE.md` (texto integral) — `CONFIRMED` |
| Cabeçalho por arquivo | bloco `<LICENSE id="Apache-2.0"> … </LICENSE>` com copyright "Robert Bosch GmbH and its subsidiaries" nos `.py` lidos |
| `NOTICE.md` | lista de detentores de copyright: Bosch Engineering GmbH (D. Fortmeier), Robert Bosch GmbH (J. Kall, C. Perwass) |
| Terceiros | `3rd-party-licenses.md`: "**No third party licenses are used, so far**" |
| Pesos de modelo | SD 1.5 e os três ControlNets citados têm licença própria nas model cards; **não lidas nesta sessão** → `UNVALIDATED` |

Nota de precisão: `NOTICE.md` está com o cabeçalho padrão do template (menciona "Function JSON's copyright holders", projeto irmão) — o arquivo foi copiado do template sem ajuste do nome. É detalhe, mas é exatamente o tipo de coisa que um inventário automático de terceiros deixaria visível.

## 11. Custos e limitações

- **Custo direto zero:** software livre, execução local. Não há serviço, assinatura ou crédito envolvido.
- **Custo real é o encaixe:** operar catharsys significa adotar workspace, Blender, conda por método e um modelo de config JSON5 próprio. Para o Lia Forge isso é um segundo framework de render, não um componente plugável.
- Limitações duras: protótipo de pesquisa autodeclarado não pronto para produção, sem testes, sem CI, sem manutenção há 27 meses, dependências não declaradas e incompatibilidade crescente com o Python atual.

## 12. Compatibilidade com o ecossistema Lia

| Projeto | Encaixe |
|---|---|
| Lia Forge | só o **padrão**: ação declarada + config por arquivo + pesos por referência externa; nada de código |
| Lia Model Lab | referência histórica de multi-ControlNet (2024), já superada pelos modelos atuais |
| Lia Studio | irrelevante para pipeline de jogo |
| Lia Project / Agent Hub | nenhum ponto de contato |

Os pesos e engines que este plugin usa (SD 1.5 + ControlNets de 2023) já estão cobertos por `LR-MODEL-007`. Este relatório cobre o **runner** e o framework; não duplica o catálogo de modelos.

## 13. Padrões aproveitáveis (o que vale levar, sem código)

1. **Licença por arquivo com bloco marcado** (`<LICENSE id="…">`) — máquina-legível, e é o que falta nas Skills do Hub (47 das 48 sem licença no payload). Um parser simples consegue extrair isso; um `LICENSE.md` na raiz do repositório não resolve o arquivo copiado sozinho.
2. **`3rd-party-licenses.md` existindo mesmo quando está vazio** — o arquivo declara "nenhum" em vez de não existir, o que transforma ausência em afirmação verificável.
3. **Seção "Purpose of the project" com aviso de prontidão** no topo do README, antes de qualquer instrução de uso.
4. **Um ambiente por método, criado por script** — separa dependências incompatíveis em vez de unificar tudo num lockfile que explode.
5. **Manifest de release fixando tag por componente** (`repos-release.yaml`) — o antídoto contra "funciona no meu branch".

Cada item acima é **proposta de prática**, não decisão; implementação cabe aos projetos.

## 14. Riscos e incompatibilidades

- **Abandono:** 27 meses sem push, sem CI, sem testes; qualquer adaptação vira fork permanente e não reconduzível.
- **Acoplamento de plataforma:** sem catharsys não há como executar; e catharsys não é instalável por pip.
- **Cadeia de modelos antiga:** SD 1.5 + ControlNets de 2023; as licenças de cada peso não foram verificadas aqui e algumas famílias têm restrição de uso comercial.
- **Zero evidência de segurança:** sem CI nem revisão pública, não há sinal verificável.

## 15. O que precisaria ser verdade para mudar o veredito

1. Um workspace catharsys executável montado do zero, com tempo e atrito medidos (hoje é impossível neste ambiente: Python 3.12+ e Blender ausentes);
2. uma GPU com suporte no stack do ComfyUI/diffusers usado, para medir o caminho de refinamento;
3. releitura das model cards de SD 1.5 e dos ControlNets com data e URL;
4. sinal de manutenção: push novo ou release ≥ v1.0.4.

Nada disso é necessário enquanto o uso for apenas de referência de prática (§13).

## 16. Evidências e fontes

| Afirmativa | Rótulo | Base |
|---|---|---|
| licença Apache-2.0 e cabeçalhos por arquivo | `CONFIRMED` | `LICENSE.md`, `NOTICE.md`, `3rd-party-licenses.md` e dois `.py` lidos no commit `ba2a9608` |
| 814 dias sem push; ★0 · 4 forks; tags v1.0.0–v1.0.3 | `CONFIRMED` | API do GitHub em 2026-11-21 |
| `pip install -e .` e `compileall` ok; import falha por `anybase` | `OBSERVED` | execução local desta sessão, venv Python 3.11.2, registro em `data/testing/test-log.tsv` |
| `anybase 1.1.0` exige Python ≥3.12 | `CONFIRMED` | `pypi.org/pypi/anybase/json` (2026-11-21) |
| `catharsys` ausente do PyPI | `CONFIRMED` | 404 em `pypi.org/pypi/catharsys/json`; pacote só distribuído pela família image-render |
| plugin listado nas duas listas da plataforma, release em `tags/v1.0.3` | `CONFIRMED` | `image-render-setup` @ HEAD: `repos/repos-main.yaml`, `repos/repos-release.yaml` |
| DCO 1.1 + GPG obrigatórios para contribuir | `CONFIRMED` | `CONTRIBUTING.md` do repositório |
| licença dos pesos SD 1.5 / ControlNets | `UNVALIDATED` | model cards não lidas nesta sessão |
| VRAM necessária, qualidade do refinamento | `BLOCKED` | sem GPU, sem pesos, sem ambiente catharsys |
| qualquer afirmação de desempenho | `INFERRED` apenas do formato dos arquivos | nenhum benchmark — não afirmado |

## 17. Recomendação

**`REFERENCE_ONLY`** — usar como referência de disciplina de proveniência (§13) e de desenho de pipeline; não integrar, não adaptar código, não citar como dependência avaliada.

Não há risco jurídico em *ler* um repositório Apache-2.0; há risco operacional em *adotar* um protótipo de pesquisa abandonado que depende de um framework de 17 repositórios e de um ambiente conda por método. Registro também: qualquer consequência de redistribuição para um produto Lia é **`REQUIRES_LEGAL_REVIEW`** — este documento não é parecer jurídico.

## 18. Próximos passos

1. **Nenhum trabalho contínuo** sobre este repositório: está encerrado como referência.
2. Se um dia o Forge quiser avaliar "render + refinamento generativo" como recurso, o objeto a pesquisar é o **ComfyUI local com ControlNet** (via `LR-FORGE-012`), não o catharsys.
3. Reabrir apenas se houver push novo no repositório ou release ≥ v1.0.4 (gatilho objetivo, verificável pela API em uma chamada).

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · esquema `catalog/CATALOG-SCHEMA.md` · protocolo de teste `governance/TESTING-PROTOCOL.md`.
