# jenalab-com — 8 repositórios; `jena-image-render` avaliado com execução local

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-012` |
| Nome | jenalab-com (org) — objeto auditado: `jena-image-render` |
| Tipo | repositorio |
| Fonte oficial | https://github.com/jenalab-com/jena-image-render |
| Responsável | jenalab (organização sem página, sem identidade de empresa verificada) |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | LOCAL_TESTS_PASS |
| Decisão de adoção | — nenhuma registrada |
| Categoria | forge (leitura transversal em licensing, ui) |
| Projetos beneficiados | Lia Forge (lote de imagem com custo controlado), Lia Model Lab (catálogo pinado de pesos) |
| Versão analisada | `3b9276fedf123a71166affa1dcda521aa78926e6` (main, "Initial release: jenair 0.1.0") |
| SHA completo | `3b9276fedf123a71166affa1dcda521aa78926e6` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — conferido contra o HEAD de `main` na coleta |
| HEAD atual | `3b9276fedf123a71166affa1dcda521aa78926e6` (único commit do repositório) |
| Data | 2026-11-21 |
| Última verificação | 2026-11-21 |
| Upstream conferido | 2026-11-21 · HEAD `3b9276fe` · sem mudança desde a análise |
| Próxima revisão | 2027-02-19 |
| Licença | MIT (`CONFIRMED` em `LICENSE`, © 2026 jenalab; `pyproject` declara `license = "MIT"`) |
| Recomendação | **ADAPT** |
| Confiança | Alta para execução e licença; Alta para o veredito de maturidade |

---

## 1. Por que a organização inteira entrou nesta análise, e como

O pedido foi "todos os repositórios de `jenalab-com`". Foram listados **8** pela API e os oito
foram abertos. Um único objeto de catálogo (`LR-FORGE-012`) é criado para o repositório que tem
relação com o Lia Forge e que **foi efetivamente executado**; os outros sete ficam registrados
aqui, com estado e motivo, sem inflar o catálogo com oito linhas de veredito idêntico.

## 2. Os 8 repositórios da organização

| Repositório | Língua | Licença | ★ | Criado | Último push | Release | O que é | Estado aqui |
|---|---|---|---:|---|---|---|---|---|
| `jena-image-render` | Python | MIT | 1 | 2026-11-21 | 2026-11-21 | nenhuma | render de lote ComfyUI por arquivo JSON, local ou RunPod | **executado nesta sessão** |
| `jena-note` | Swift | MIT | 3 | 2026-03-15 | 2026-11-14 | `v2.1.0` | editor Markdown WYSIWYG para macOS 13+ | lido em nível de README/licença |
| `jena-image` | Swift | MIT | 2 | 2026-03-18 | 2026-11-13 | `v2.0.1` | visualizador de imagens nativo, macOS 14+ | idem |
| `jena-file` | Swift + Rust | MIT | 1 | 2026-11-01 | 2026-11-16 | `v0.1.1` | SFTP + terminal num app macOS, com bastion | idem |
| `jenaMemory` | Swift | MIT | 1 | 2026-03-14 | 2026-11-01 | `v1.2.0` | monitor de memória na barra de menu do macOS | idem |
| `jena-web` | Swift | MIT | 0 | 2026-11-14 | 2026-11-14 | `v0.1.2` | navegador macOS sobre WebKit do sistema | idem |
| `SwiftTerm` | Swift | MIT (herdada) | 0 | 2026-11-01 | 2026-11-01 | — | **fork** de `migueldeicaza/SwiftTerm` | verificado como snapshot |
| `mediator` | Ruby/Jekyll | MIT em arquivo `LICENCE` | 0 | 2025-09-04 | 2024-05-28 | — | **fork** de `dirkfabisch/mediator` (tema de blog) | verificado como snapshot |

Três achados sobre a organização, todos verificáveis em uma chamada de API:

- **nenhum repositório sem licença** — MIT em todos os seis próprios; os dois forks carregam a
  licença do upstream. É o contrário do quadro das Skills do Hub (47 de 48 sem licença no payload);
- os dois forks não têm modificação: `SwiftTerm` está **0 commits à frente / 56 atrás** do
  upstream e `mediator` está **idêntico** (0/0) — comparação pela API em 2026-11-21. São
  snapshots de dependência/tema, não work derivado;
- cinco dos seis repositórios próprios são **apps macOS** (13+/14+) — para o ecossistema Lia, que
  não tem alvo macOS, são irrelevantes como dependência; valem apenas como referência de prática
  (§7). Detalhe de distribuição lido só em `jena-web`: zip **ad-hoc signed e não notarizado** pelo
  Apple, com instrução de remover o quarentena; se os demais apps seguem o mesmo caminho,
  **não foi conferido**.

## 3. O que é o `jena-image-render`

Ferramenta de linha de comando (`jenair`) que monta graphs do ComfyUI a partir de um arquivo JSON
de jobs e os executa — na sua máquina ou num pod RunPod alugado. Uma linha de decisão do projeto,
registrada no README: *"ComfyUI without the wires"* — sem nós, sem ligações, só prompts e defaults.

| Estrutura | Medido no commit pinado |
|---|---|
| Pacote | `jena-image-render 0.1.0`, entry point `jenair`, `requires-python >=3.10` |
| Porte | 83 arquivos na árvore, 41 `.py` no total; 17 módulos em `src/jena_image_render/` com **3.355 linhas**, mais o `catalog.json` |
| Testes | 15 `.py` em `tests/` (14 suítes + `helpers.py`) + 4 `.py` em `pod/tests/` |
| Dependências | `requests`, `websocket-client`, `certifi`, `huggingface_hub` — nada de torch no pacote |
| Exemplos | 18 JSON em `configs/` + um README (8 básicos, 5 por engine, 4 para arquivos próprios, `full.json`) |
| Docs | 4: `config.md`, `local.md`, `models.md`, `runpod.md` |
| CI | `ci.yml`: matriz Python 3.10/3.12, `unittest` das duas suítes e **dry-run de todo exemplo** nos dois alvos; `pod-image.yml` publica a imagem do pod |
| Rede | a `pip install` do pacote; nada de weights no repositório |

O ponto arquitetural relevante: **o pacote Python não importa ComfyUI nem torch**. Ele fala com
um ComfyUI existente por HTTP/WebSocket e envia um graph. Isso mantém o `jenair` MIT e deixa o
ComfyUI GPL-3.0 do outro lado da fronteira de processo.

## 4. O que foi executado nesta sessão (não é descrição do README)

Ambiente: sandbox Linux, CPython 3.11.2, venv isolado em `/tmp`, tarball do commit `3b9276fe`.
Nenhuma GPU, nenhum peso baixado, nenhuma conta, nenhuma chave, nenhum aluguel de instância.

| # | Comando | Resultado |
|---|---|---|
| 1 | `pip install -e .` + `pip install pytest` | sucesso; deps resolvidas do PyPI |
| 2 | `python -m unittest discover -s tests` (forma do CI) | **Ran 159 tests — OK**, exit 0, 0.256 s |
| 3 | `cd pod && python -m unittest discover -s tests` (forma do CI) | **Ran 22 tests — OK**, exit 0, 0.118 s |
| 4 | `python -m pytest -q` | **181 passed + 47 subtests passed**, exit 0, 0.72 s |
| 5 | `jenair --help` / `jenair engines` | tabelas de engine, tamanho padrão e aspects impressas corretamente |
| 6 | `jenair configs/basics/01-one-image.json --dry-run` | exit 0; "ComfyUI is not answering on http://127.0.0.1:8188: planning without it" + plano de 1 imagem e dos 3 arquivos que baixaria |
| 7 | `jenair configs/basics/03-compare-models.json --dry-run --no-download` | exit 0; plano de 12 imagens (4 por engine) |
| 8 | `for f in ...; do jenair "$f" --dry-run; jenair "$f" --runpod --dry-run; done` | **28 execuções, 0 falhas** — mesmo passo do CI, sem GPU e sem chave |
| 9 | `jenair runpod status` sem `RUNPOD_API_KEY` | erro limpo "RUNPOD_API_KEY is not set (put it in .env)"; **nenhuma tentativa de alugar** |
| 10 | sonda de validação: `model` inexistente | exit 1; lista os aliases conhecidos e diz onde colocar o arquivo ou como escrever o endereço |
| 11 | sonda: arquivo de config inexistente | exit 1 com `ERROR [Errno 2] No such file or directory` (mensagem crua de exceção) |
| 12 | sondas numéricas: `aspect 7:9`, `width` sem `height`, chave desconhecida, `steps 0`, `steps -5`, `cfg 99` | os três primeiros tratados (2 erros + 1 aviso de chave ignorada); **`steps 0` e `steps -5` aceitos em silêncio**, exit 0 |

**O que a suíte de testes não cobre, e foi achado por sonda:** `config.py:340` faz
`steps=int(_set(job, "steps", eng.steps))` sem verificação de faixa; `docs/config.md` descreve
`steps` como "sampling steps. Default per engine" sem prometer validação. A afirmação do README —
*"Checked before you pay: `--dry-run` validates models, files, LoRA/engine matches and output
paths"* — é **precisa e estreita**: não inclui faixa de parâmetros de amostragem. Consequência
prática: um `steps` negativo passa pelo plano e só falharia no ComfyUI — **não testado aqui**,
pois não há ComfyUI no sandbox → `UNVALIDATED`.

## 5. Modelo de custo: o que dá para afirmar

O desenho trata dinheiro explicitamente, e isso é verificável no código lido:

- GPU **nunca** é alugada sem flag `--runpod` (ou `JENA_TARGET=runpod`), e `--runpod --dry-run`
  produz o plano sem alugar (executado, item 9 da tabela acima);
- o pod se auto-termina após 20 min ocioso (`IDLE_SECONDS` default 1200) e há limite duro
  `--max-hours` (default 3 h), com `jenair runpod down` manual;
- tentativa em Community Cloud primeiro e *Secure* como fallback, e "a pod that fails to start is
  always terminated" — descrito em `docs/runpod.md`;
- retomada de lote: imagens já salvas são puladas, então um lote interrompido não repete custo;
- `--dry-run --no-download` evita puxar 20 GB para descobrir um erro de digitação.

**Preço de GPU não foi verificado:** `docs/runpod.md` escreve que "a Community RTX 3090 / A5000
was about $0.2–0.3 per hour" na data de escrita deles. Registro como `REPORTED` de terceiros — não
confere com a tabela da RunPod nesta sessão, e nenhuma conta por hora deve ser usada por nenhum
projeto Lia com base nesta linha.

## 6. Catálogo de pesos: o achado mais útil para o Lia

`src/jena_image_render/catalog.json` fixa cada arquivo de cada engine por **revisão do Hugging
Face + SHA-256 + tamanho em bytes** (23 arquivos pinados: 13 de modelo + 10 LoRAs). Medido:

| Engine | Arquivos pinados | Total | Defaults |
|---|---|---:|---|
| `zimage` | diffusion 12,31 GB · text_encoder 8,04 GB · vae 0,34 GB | 20,69 GB | 832×1248, 9 steps, CFG 1 fixo |
| `krea2` | 13,49 · 8,88 · 0,25 GB | 22,62 GB | 1024×1024, 8 steps, CFG 1 |
| `qwen` | 14,23 · **17,53** · 0,68 GB | 32,44 GB | 832×1248, 25 steps, CFG 1 fixo |
| `klein-4b` | 7,75 · 8,04 · 0,34 GB | 16,13 GB | 832×1248, 4 steps, CFG 1 fixo |
| `illustrious` | checkpoint 6,94 GB | 6,94 GB | 896×1152, 28 steps, CFG 6 |
| soma dos 13 arquivos de modelo | — | **98,82 GB** | — |

E a tabela de licença por alias, na mesma direção (o documento `docs/models.md`, com a
qualificação "as stated on each model card at the pinned revision — read the card before using
results commercially"):

| Alias | Fonte | Licença declarada por eles |
|---|---|---|
| `zimage` | `Comfy-Org/Z-Image-Turbo` | Apache-2.0 |
| `krea2` | `Comfy-Org/Krea-2` | Krea 2 Community |
| `qwen` | `Comfy-Org/Qwen-Image-2.1` | "see model card" |
| `klein-4b` | `Comfy-Org/Flux-2-Klein-4B` | Apache-2.0 |
| `illustrious` | `OnomaAIResearch/Illustrious-xl-early-release-v0` | Fair AI Public 1.0-SD |

LoRAs de exemplo seguem o mesmo formato, com gatilho de prompt embutido (`trigger`). `klein-9b` e
outros exigem aceitar licença no Hugging Face + `HF_TOKEN`; o projeto documenta isso em "Gated
models". **Nenhuma dessas licenças foi conferida na model card aqui** → `REPORTED`, e qualquer uso
comercial de saída gerada por esses pesos exige verificação própria.

Por que isso importa para o Lia: é exatamente a lacuna registrada em `LR-MODEL-007` (licença de
código × licença de pesos) e no inventário de Skills do Hub. Não é um problema de política, é de
**formato de registro**: um JSON pinado por arquivo com hash, tamanho e ponteiro de licença.

## 7. Padrões aproveáveis (proposta de prática, não de dependência)

1. **Catálogo de pesos pinado por revisão + SHA-256 + tamanho.** Aplicável a Lia Model Lab e a
   qualquer script de geração do Forge; hoje a base registra SHA de código-fonte, não de peso.
2. **`--dry-run` como portão de custo.** "Validar plano antes de alugar GPU" é transferível a
   qualquer caminho pago (RunPod, e por analogia chamadas a APIs de geração), e o Research já
   tem o análogo documental: critério de conclusão antes de abrir rodada.
3. **Auto-terminação por padrão** (ocioso 20 min, teto de 3 h) em vez de "lembre-se de desligar".
4. **Fronteira de licença por processo**: pacote permissivo falando com serviço copyleft por
   HTTP, com a origem GPL declarada em comentário do `Dockerfile`. Se um dia o Lia distribuir
   imagem contendo ComfyUI, isso é **`REQUIRES_LEGAL_REVIEW`** — não decidir por analogia com este
   repositório.
5. **CI que roda o dry-run de todos os exemplos** nos dois alvos: é o que permitiu a esta análise
   reproduzir 28 verificações em segundos, sem GPU.
6. **Vendoring com registro de procedência** (outro repositório da mesma organização,
   `jena-note`): `Vendor/Kiwi/upstream.json` guarda repositório, versão, commit do projeto **e os
   commits das 5 dependências transitivas**, com `LICENSE`/`NOTICE` por árvore vendada. É o modelo
   mais completo de procedência visto nesta base, e é o que falta às Skills Lia.

## 8. Limitações, riscos e o que não foi verificado

- **Idade zero.** Criado e publicado no mesmo dia da análise (2026-11-21, 03:23 → 03:24 UTC), com
  **um único commit**, sem releases, sem issues, sem histórico que permita avaliar manutenção,
  resposta a bug de segurança ou ritmo. Qualquer conclusão sobre durabilidade é impossível.
- **Organização sem identidade verificada**: sem página, sem política de segurança, sem
  `CODEOWNERS`, sem CLA; risco de suprimento é de pessoa física. Não é acusação — é ausência de
  sinal, registrada como `UNVERIFIED`.
- `init.sh` se propõe a instalar Python "if it is missing" e a escrever em `./.venv`, `.env` e nas
  pastas de models do ComfyUI (links/downloads). **Não executei `init.sh`**; a descrição vem do
  README → `REPORTED`. Instalação no sistema do usuário é um ponto a revisar antes de adotar o
  padrão.
- Efeito colateral por design: com ComfyUI local, o link de arquivos entra no diretório de models
  do ComfyUI (`--no-download` restringe apenas o download).
- **AMD/RX 580: nada afirmado.** O caminho local delega ao ComfyUI que o usuário já tem, e o
  caminho RunPod usa imagem CUDA (`pytorch/pytorch:2.14.1-cuda12.6-cudnn9-runtime`). Se um
  ComfyUI com backend AMD funciona com estas engines, **não foi testado e não está descartado** —
  é `UNVALIDATED`, e um requisito de imagem CUDA em nuvem não se transfere para GPU local.
- Verificação de VRAM, qualidade de imagem, tempo por imagem e comparação entre engines:
  `BLOCKED` — nenhuma execução de render ocorreu nesta sessão.
- Os 7 repositórios restantes: **não** executados nem compilados (exigem Xcode/macOS) →
  `DOCUMENTED`, com base em README, `LICENSE` e API.

## 9. Segurança do caminho remoto (lido no código, não apenas no README)

`pod/Dockerfile` + `pod/entrypoint.sh` + `pod/Caddyfile`:

- ComfyUI escuta em `127.0.0.1:8188` **somente local** dentro do container; a porta exposta é o
  Caddy;
- o entrypoint **recusa subir sem `COMFY_PASSWORD`** (`exit 1` com "refusing to expose ComfyUI
  without a login"), e faz `unset COMFY_PASSWORD` após gerar o hash;
- autenticação básica via hash (`caddy hash-password`), sem credencial no código;
- nenhum peso e nenhuma chave são gravados na imagem; `IDLE_SECONDS`/`MAX_SECONDS` limitam
  exposição;
- a extensão `jena_fetch` aceita baixar pesos por URL e receber uploads em chunks de 32 MB
  verificados por SHA-256 — ou seja, há um mecanismo de transferência de arquivo por design, e é
  ele que torna o `--runpod` prático. Não há sandbox para o que o graph faz dentro do ComfyUI.

Nada aqui foi testado contra um pod real: é leitura dos arquivos no commit pinado → `CONFIRMED`
como descrição do código, `BLOCKED` como comportamento em produção.

## 10. Recomendação

**`ADAPT`** — adaptar **os padrões** (§7), não o pacote. Nenhum código deste repositório entra em
projeto Lia por esta recomendação, e pesquisa não autoriza adoção (`MISSION.md` §3).

O que justificaria mudar para `DIRECT_INTEGRATION_CANDIDATE` seria: histórico de manutenção (a
partir de ~3 meses de atividade real com releases), um `SECURITY.md`/política de reporte, e
confirmação de que o caminho ComfyUI local funciona no hardware alvo do Forge. Nada disso existe
hoje, por idade — não por defeito.

## 11. Evidências e fontes

| Afirmativa | Rótulo | Base |
|---|---|---|
| 159 + 22 testes OK; 181 passed + 47 subtests | `OBSERVED` | execução local desta sessão no commit `3b9276fe`; linhas em `data/testing/test-log.tsv` |
| 28 dry-runs dos exemplos, 0 falhas, sem GPU/chave | `OBSERVED` | laço do CI reproduzido localmente, exit 0 em todos |
| `--runpod --dry-run` não aluga; sem chave, erro limpo | `OBSERVED` | itens 8–9 da §4 |
| `steps` sem validação de faixa | `OBSERVED` | sondas `steps 0` / `steps -5` com exit 0 + leitura de `config.py:340` |
| catálogo com 23 arquivos pinados por hash/tamanho; 98,82 GB nos modelos | `CONFIRMED` | `src/jena_image_render/catalog.json` lido no commit; soma calculada |
| licenças por alias e aviso "leia a model card" | `REPORTED` | `docs/models.md` do próprio repositório; model cards não conferidas |
| preço "about $0.2–0.3/h" em Community 3090/A5000 | `REPORTED` | `docs/runpod.md`, data de escrita deles; RunPod não consultada |
| MIT em todos os 6 repositórios próprios | `CONFIRMED` | `LICENSE` lido em cada repositório (textos idênticos, © 2026 jenalab/JenaLab) |
| forks sem modificação (0/56 e 0/0) | `CONFIRMED` | API `compare` com `migueldeicaza:main` e `dirkfabisch:master`, 2026-11-21 |
| CI verde no commit analisado | `CONFIRMED` | `actions/runs` — `ci`, success, 2026-11-21T03:24:39Z |
| pod não expõe ComfyUI sem senha; bind local | `CONFIRMED` | `pod/entrypoint.sh`, `pod/Caddyfile`, `pod/Dockerfile` |
| comportamento do `init.sh` | `REPORTED` | README; o script não foi executado |
| qualidade de imagem, VRAM, tempo, desempenho em AMD | `BLOCKED` | sem GPU, sem ComfyUI, sem pesos baixados |
| o que o ComfyUI faz com `steps` inválido | `UNVALIDATED` | fora do alcance do que foi executado |
| identidade/manutenção futura da organização | `UNVERIFIED` | sem página, sem política, 1 dia de histórico |

## 12. Próximos passos

1. Se o Lia Forge quiser **lote de imagem com custo controlado**, o caminho a prototipar é
   "plano antes de gastar": catálogo pinado + dry-run + auto-terminação. Isto é uma
   recomendação de **formato**, e o custo real (GPU local vs serviço) segue em aberto.
2. Levar o formato `catalog.json` (arquivo → revisão → sha256 → tamanho → licença → ponteiro de
   model card) para a discussão do `LR-MODEL-007`, como campo de registro, não como dependência.
3. Revisar este objeto em **2027-02-19** (90 dias, prazo curto deliberado por ser software de um
   dia de idade): verificar se há release, histórico de issues e política de segurança.
4. Os 7 repositórios restantes não pedem revisão periódica: 5 são apps macOS fora do escopo do
   Lia e 2 dos 8 são forks sem modificação.

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · esquema `catalog/CATALOG-SCHEMA.md` · protocolo de teste `governance/TESTING-PROTOCOL.md`.
