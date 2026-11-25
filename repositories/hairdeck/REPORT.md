# HairDeck — código de artigo que roda 28 dos seus 106 testes sem GPU nenhuma, baixa o `LICENSE` junto com cada peso, e publica a medição em JSON dentro do repositório

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-021` |
| Nome | `hyz317/HairDeck` — "Animation-Ready Stylized Hair Cards from a Single Image": gera cartas de cabelo estilizadas **e as chains de spring-bones** a partir de uma imagem |
| Tipo | repositório de código (artefato de artigo, arXiv 2610.40599) |
| Fonte oficial | https://github.com/hyz317/HairDeck · página do projeto `hyzcluster.github.io/HairDeck` · pesos e demo em Hugging Face |
| Responsável | Yuze He e Yixiang Wei (contribuição igual), Wang Zhao, Chuhao Chen, Yanning Zhou, Yong-Jin Liu — Tsinghua, CMU, CUHK; no Git: `hyz317` (6 commits), `Jetha Chan` (4), `Exkiober` (1) |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | PARTIAL |
| Recomendação | **ADAPT** — sugestão ao dono: o padrão "peso baixado chega com a licença ao lado e com `sha256` esperado"; os JSONs de medição commitados; e o teste do verificador de ambiente |
| Decisão de adoção | — nenhuma registrada |
| Categoria | geração 3D/VRM + engenharia de aquisição de pesos + hábito de medição |
| Projetos beneficiados | Lia Model Lab (aquisição de pesos com termos e hash), Lia Studio (registro de proveniência por ID, medição de desempenho), Lia Forge (teste do próprio script de ambiente), Research (formato de evidência) |
| Versão analisada | `main` = HEAD raso de 2026-11-13 21:04 +0900 — **não há tag nem release**; o SHA do commit é a única âncora possível |
| Proveniência do conteúdo | **medido por nós**: clone, censo de árvore, execução da suíte de testes e do verificador de ambiente neste sandbox; afirmações de desempenho são dos JSONs do repositório (lidos, não reproduzidos) |
| Data | 2026-11-25 |
| Última verificação | 2026-11-25 · `gh api repos/hyz317/HairDeck` + `git/trees/HEAD?recursive=1` (`truncated: false`, 224 entradas) + `releases` (0) + `tags` (0) + clone |
| Upstream conferido | 1224 ★ · 96 forks · 3 issues abertas · 4 watchers · `size` 831 KB · 123 arquivos `.py`, 16.566 linhas |
| Próxima revisão | 2026-12-09 (projeto em semana de lançamento: 4 PRs incorporados em 2026-11-13; revisar cedo) |
| Licença | **Apache-2.0** para código **e checkpoints** (frase do README; `LICENSE` lido na raiz) — mas a execução depende de dois modelos *gated* cujos termos não estão no repositório e que eu não pude ler (§7) |
| Confiança | Alta no que rodei (testes, verificador de ambiente, censos); média nos números de desempenho — são medições deles, commitadas com hardware e semente, mas não reproduzidas aqui (sem GPU) |

---

## 1. Por que este objeto entrou na base

Veio na mesma leva do Charakuru (`LR-FORGE-020`), pelo mesmo motivo de formato: produziram o mesmo tipo
de artefato (cabelo/cartas → avatar VRM animável) por caminhos opostos. Onde o Charakuru esconde o código
e abre a documentação, o HairDeck abre **tudo** — código, testes, dados de avaliação, medições cruas — e
não enumera os termos de terceiros. Os dois juntos cobrem um espaço que nenhum dos dois cobre sozinho, e é
esse par que eu proponho como referência para a política de distribuição de Skills e de pesos da Lia.

`grep` no índice e no catálogo antes de começar: nenhum registro anterior de `HairDeck`.

## 2. O que é, medido na árvore (224 entradas, `truncated: false`)

| Grandeza | Medido |
|---|---|
| Python | 123 arquivos `.py`, 16.566 linhas; **1.568 linhas (9,5 %) estão em `tests/`** |
| Testes | 13 módulos, **106 `def test`**, framework `unittest` puro (13 arquivos o importam), 8 usam `unittest.mock.patch`, 6 usam `types` + `importlib.util` para **stub de dependência pesada** |
| Config | 26 `.json`; um deles é `configs/charm_test_pc.sha256` — entrada de avaliação **pinada por hash** |
| Docs | 9 `.md`: README em EN/JA/zh-CN + `fast-sampler.md`, `image-cache.md`, `macos.md`, `windows.md`, `rocm.md` e a pasta `docs/measurements/` |
| Medições commitadas | 20 `.json` em `docs/measurements/{fast-sampler,image-cache,rocm-compat}` |
| Contêiner | `docker/` com 6 arquivos, incluindo `compose.rocm.yml` (o único `.yml` do repositório) |
| CI | **zero** — não existe `.github/`; nada roda no GitHub |
| Release/tag | **zero e zero** — distribuição é `git clone` + pesos do Hugging Face |
| Binários no Git | nenhum: `.gitattributes` só normaliza EOL (`*.sh`, `*.py`, `*.Dockerfile`, `*.txt`, `*.md` com `eol=lf`) — não há LFS |
| Histórico | **11 commits** em 15 dias (2026-10-30 → 2026-11-13), 3 autores; 1.224 ★ no período |

## 3. O que eu executei aqui (e é o resultado mais interessante da visita)

Objetivo declarado: ver quanto do projeto é verificável **sem GPU, sem pesos e sem ambiente deles**.

| Comando | Saída |
|---|---|
| `python3 -m unittest discover -s tests -p 'test_*.py'` (Python 3.11.2, **nenhuma dependência instalada**) | `Ran 38 tests`, **28 passaram**, 10 erros de importação, **0 falha de asserção** |
| mesmo comando no venv com `numpy` apenas | idêntico: `Ran 38 tests`, 28 passaram; os 10 erros mudam de causa (`numpy` sai, entram `torch` ×5, `PIL`, `trimesh`, `gradio`) |
| `python3 scripts/check_environment.py` (sem dependências) | `[FAIL] Python: RuntimeError: Use Python 3.12 x64 for the pinned release environment.` · `[FAIL] Device / bfloat16: ModuleNotFoundError: No module named 'torch'` · `[FAIL] Dependencies: PackageNotFoundError: No package metadata was found for numpy` — e o processo sai com **código 1** |
| `check_environment.py` no venv com `numpy` | a linha de `Dependencies` passa a reclamar de `transformers` — o verificador reporta **o próximo item a consertar**, não uma parede de texto |

Três propriedades que valem transporte, todas medidas (não deduzidas):

1. **a suíte é particionada por dependência de propósito.** Um terço dos testes definidos roda sem nada
   instalado, porque os módulos de ambiente/plataforma (`test_environment_dependencies`, `test_sam3_patch`,
   `test_windows_setup` com 20 testes, `test_windows_dependencies`) verificam *policy* — conteúdo de
   `requirements.txt`, presença de patch, forma do script PowerShell — sem importar o modelo. Nada que
   rodou falhou: o que depende de GPU está isolado, não espalhado pelo teste.
2. **o portão de versão do interpretador é código, com motivo na mensagem.** Não é "requer Python 3.12" no
   README: é uma asserção que se manifesta como `RuntimeError` com a razão ("for the pinned release
   environment"). Mesma família do que a base já mediu em VoiceStudio (testes sobre pinos de action), mas
   aplicado ao ambiente do usuário.
3. **falha de checagem devolve exit 1 e um relatório por área.** Registrei o cuidado óbvio: a primeira vez
   que rodei, pipei para `head` e o `$?` era do `head` (0). Refiz com redirecionamento para arquivo: exit
   1. Um verificador cujo exit code só aparece sem pipe é uma armadilha de CI — a deles não é.

O que **não** rodei e por quê: inferência real (`scripts/image_to_hair.py`) exige CUDA/MPS + os pesos +
Blender; instalar torch (~2 GB) e baixar pesos não é permitido a esta base. Fica `NOT_RUN` — dívida desta
base, não limitação de ferramenta: `python3` e `pip` funcionam aqui; a restrição é de peso e de licença.

## 4. Aquisição de pesos: `download_weights.py`, lido por dentro

O script (~470 linhas, um único ponto de entrada com `--only`) faz quatro coisas que nenhum outro objeto
desta base fazia tão bem:

| Mecanismo | Evidência no código | Por que importa |
|---|---|---|
| **hash esperado por arquivo** | cada entrada leva um `want` para `gated_get(...)`/`local_get(...)` | não é "confie no que baixou"; é verificação de integridade antes de carregar |
| **a licença vem junto com o peso** | `gated_get(a, repo, 'LICENSE', paths.weights('sam3', 'LICENSE'))` e o análogo `LICENSE.md` do DINOv3, com `log('... LICENSE not fetched:', e)` quando falha | o arquivo de termos **aterrissa ao lado do `.pt`/`.safetensors`**, então a proveniência viaja com o ativo; a falha de busca é logada e não aborta |
| **fonte local é cidadã de primeira classe** | `local_get(a.src, rel_of(dst), dst, want) if a.src else gated_get(...)` | qualquer componente pode vir de um caminho local em vez do hub — é o desenho que permite operação sem rede / espelho |
| **hub alternativo e revisão fixa** | `hf_endpoint()` respeita `HF_ENDPOINT`; `--gated-source {huggingface,modelscope}`; o DINOv3 vem "at a fixed revision" | ambiente restrito ou rede lenta trocam de origem sem trocar o código; o pin de revisão é explícito para o modelo *gated* |

Isto responde, com implementação de terceiros, uma pergunta que a base vem acumulando: os projetos que a
Lia usa tratam `LICENSE` de peso como enfeite de página. Aqui a licença é um **arquivo baixado com o
peso**, sujeito ao mesmo `sha256` esperado que o peso.

## 5. Medição como arquivo versionado

`docs/measurements/` tem 20 JSONs. O de amostra (`fast-sampler/rtx5060ti-windows.json`) abre com

```
"gpu": "NVIDIA GeForce RTX 5060 Ti", "torch": "2.8.0+cu128", "cuda": "12.8", "hip": null,
"platform": "Windows-11-10.0.26200-SP0", "example": "ex02.png", "seeds": [1, 2], "steps": 50, "cfg": 2
```

e abaixo traz `modes.release.first` e `modes.release.warm[]` com o tempo **por estágio** — `prep` 18,502 s
na primeira passada contra 1,019 s e 0,837 s nas mornas, `dino+dit+decode`, `colors`, `chains`, `glb`,
`total`, `wall`. Três plataformas cobertas (RTX 5060 Ti Linux, RTX 5060 Ti Windows, Radeon 8060S/ROCm) e,
na pasta `image-cache`, arquivos `*-variations-2-numerics.json` / `-4-numerics.json` que registram
**equivalência numérica entre variações**, não só tempo. E um par de arquivos
`rtx5060ti-default-branch.json` × `rtx5060ti-default-upstream.json`: o mesmo benchmark rodado na branch e
no upstream, isto é, **a deriva medida em vez de negada**.

Consequência prática para a nossa base, e é a menor coisa possível: `data/testing/test-log.tsv` tem nove
colunas e uma só para `evidence`. O ganho não é uma coluna nova — é uma convenção de conteúdo: `primeira
passada × morna`, por etapa, com hardware/versão/semente declarados no mesmo registro. Nosso registro de
`open-seo` diz "2.130 testes exit 0"; não diz quanto tempo, em que máquina, nem em que condição. Os deles
dizem.

## 6. Proveniência por lista de IDs, sem copiar nada

`data/lists/`: `train_keys_cards.txt` com **36.440** linhas, `train_keys_index.txt` com **36.455**, e os
conjuntos de teste com **76** e **100** chaves. As chaves têm a forma `vroid-hair/<n>/<id-numérico>` —
identificadores de ativos do VRoid Hub, **não cópias dos ativos**. Eles publicam *o que* entrou no
treinamento e no teste, em tamanho tal que qualquer pessoa pode recuar até a fonte, sem redistribuir nada.

É o oposto exato do nosso `Mr-Mak-Skills-Free.zip` (3,35 MB de cópia versionada dentro do repositório do
Studio, ver `DR-0004`) e do modelo `READY-TO-USE-LICENSES.md` desta base (registrar a licença lida). A
terceira alternativa — registrar **o identificador de origem por item** — é a que não cria cópia, não
encha o repositório e sobrevive à remoção do arquivo. Vale como pergunta para o Studio: o catálogo de
assets dele guarda o arquivo ou guarda a chave?

## 7. O empilhamento de termos que o repo não enumera (e eu não consegui ler)

O `LICENSE` na raiz é Apache-2.0 e a frase do README é "HairDeck code **and checkpoints** are licensed
under Apache-2.0. Third-party models, code and datasets retain their respective licences." Código e pesos
próprios permissivos é raro e bom. O problema é a cadeia de dependência declarada no próprio README:

| Item | O que o repo diz | O que eu pude ler |
|---|---|---|
| SAM 3 (`facebook/sam3`) | "a gated repository: accept the licence on its page and log in first" | termos: **não lidos** — `huggingface.co` fora da allowlist |
| DINOv3 (`facebook/dinov3-vitl16-…`) | "a gated repository like facebook/sam3", obtido "at a fixed revision" | termos: **não lidos**, mesma causa |
| BiRefNet-matting, CHARM (dataset `hyz317/CHARM`), Dora-VAE (`Seed3D/…`), VRM Add-on (`saturday06/…`) | listados em Acknowledgments | termos: não abertos; os quatro últimos estão em GitHub (atingível) mas não eram necessários à pergunta desta rodada |

Ou seja: **a licença pormissiva do HairDeck não é a licença do resultado**. Uma saída de HairDeck carrega
os termos do pipeline inteiro, e a frase de uma linha não diz quais. `README` §License tem uma sentença,
sem tabela; não há `THIRD_PARTY_NOTICES` nem `NOTICE` (procurei na árvore inteira: 0 arquivos `NOTICE`).
Comparação direta que a base já mediu: o Charakuru tem 5 linhas de aviso + 5 arquivos de licença no
pacote; o VoiceStudio (`LR-VOICE-003`) tem um `LICENSE-NOTICE.md` que assume "commercial and internal
business use" e diz que os pesos retêm termos próprios; o cal.diy (`LR-FORGE-019`) é MIT por remoção. O
HairDeck é o caso em que a **aquisição** compensa a **falta de enumeração** — o `download_weights.py`
traz cada `LICENSE` para dentro do workspace (§4). É um formato novo de fronteira de licença para o nosso
levantamento: a informação de termos não está no repositório, está no **artefato montado pelo instalador**.

## 8. Como o projeto lida com o mundo em volta (medido no histórico e nas issues)

- Aceita PR: os quatro últimos commits de 2026-11-13 terminam em `(#4)`, `(#5)`, `(#6)`, `(#7)`.
- Uma das mensagens: "Add tested ROCm gfx1151 setup **with NVIDIA regression coverage**" — adicionar
  plataforma leva junto cobertura da antiga; e o `docs/measurements/rocm-compat/` existe para sustentar a
  frase. Mesma disciplina do `open-seo`, por outro caminho (sem CI, com medição commitada).
- "Add a fast sampler for small batches (2-3x faster sampling, measured on NVIDIA and AMD)" — o número
  vai no título do commit, com a condição ("on NVIDIA and AMD") e com o JSON na pasta de medições.
- Issues abertas (3): `#8` "hair strands have internal geometry" (2026-11-19, 0 respostas), `#3` "ComfyUI
  (not an issue)" com 4 comentários, `#1` em chinês pedindo conversão de cartões para Groom do Unreal.
  A `#3` virou entrada no README: **`ComfyUI-HairDeck` (visualbruno)** está listado em §Community como
  nós de ComfyUI com export GLB/rigged/VRM. Integração de terceiros nasce de issue e é creditada no
  README — o oposto do `retroactive-contributions.md` do open-seo, que era confissão de ausência de
  crédito.
- Zero `.github` também custa algo: sem CI, as alegações de "tested" não têm trilha automatizada; a
  garantia é o `check_environment.py` rodado pelo usuário + os JSONs. É uma escolha de custo, não um
  descuido — e é a alternativa legítima ao modelo "tudo na CI" do open-seo.

## 9. Onde isto poderia se aplicar (a viabilidade é do dono)

> **Escopo desta seção** — sugestão a partir do que a evidência suporta, com a pergunta de viabilidade de
> cada app. Não é instrução para nenhum app e nada foi aplicado fora desta base (`MISSION.md` §3;
> `DR-0019` §5).

| App | O que sugiro considerar | O que custaria no app |
|---|---|---|
| Lia Model Lab | o padrão do §4: peso + `LICENSE` + `sha256` esperado no mesmo passo de aquisição, com `local_get` como alternativa e `HF_ENDPOINT` respeitado | um manifesto por modelo já baixado; é o ponto de partida, não uma reescrita |
| Lia Studio | proveniência por ID de ativo (§6) em vez de cópia versionada; e o `first × warm` por estágio nas medições de render | toca o registro de assets existentes; a decisão de remover o ZIP continua sendo do dono (`DR-0004`) |
| Lia Forge | testar o verificador de ambiente como eles testam (há dois módulos de teste só para isso) | baixo: é acrescentar teste ao script que já existe |
| Research (esta base) | adotar o formato de registro de medição (hardware, versão, sementes, etapa) no `data/testing/test-log.tsv` | zero de código; é convenção de preenchimento |

**Nada aqui propor em relação a pesos**: baixar, espelhar ou embutir SAM 3 / DINOv3 implicaria aceitar
licença gated com conta — fora do que esta base faz, e fora do que eu posso verificar daqui.

## 10. O que não verifiquei, e por quê

- Não rodei inferência, export VRM, demo Gradio nem Blender: exige GPU/pesos/instalador de 4 GB de
  dependências. `NOT_RUN`, por peso e por conta, não por ferramenta ausente.
- Não li os termos de SAM 3 nem DINOv3 (hosts fora da allowlist) — por isso §7 para em "não lidos" em vez
  de "não comerciais".
- Não reproduzi nenhum número de desempenho: os 20 JSONs são evidência **documentada por eles com
  hardware declarado**, não medida por nós. Se alguém citar "2-3x" como nosso, está errado.
- Não abri os checkpoints do Hugging Face nem o `model-card` deles (mesmo bloqueio de host); o README
  afirma que os checkpoints são Apache-2.0 e eu não confirmei contra a página do repositório de pesos.
- Não avaliei qualidade visual/robustez do modelo (fora do alcance de medição deste sandbox).
- `hairdeck/paths.py`, `hairdeck/eval/*` e `scripts/train/*` foram lidos só o bastante para as afirmações
  acima; não fiz auditoria de código do pipeline de amostragem.

## 11. Recomendação: **ADAPT**

`ADAPT` no sentido estreito que a base usa: **não** é "adotar HairDeck", é "estas quatro práticas têm forma
melhor do que a nossa equivalente, e a evidência é verificável":

1. aquisição de peso com hash esperado **e licença ao lado** (§4) — resolve uma categoria de dívida que o
   `ASSET-PROVENANCE` desta base só descreve;
2. testes particionados por dependência pesada, com stub de módulo (§3, medido: 28 de 106 rodam sem nada)
   — o padrão que faltava ao `LR-FORGE-017` para o caso de ambiente restrito;
3. medição commitada com condição experimental declarada e o par "branch × upstream" (§5);
4. proveniência por lista de IDs (§6) como alternativa a versionar cópia.

Custo de risco: nenhum dos quatro toca licença dos ativos do HairDeck; o **próprio HairDeck** como
dependência é outra conversa, e ela passa por §7 — enquanto os termos de SAM 3 e DINOv3 não estiverem
lidos, o uso do modelo (não das práticas) não tem como ser aprovado por pesquisa.

**Propor** ao dono, sem aplicar: fixar em `data/inventory/license-matrix.tsv` o estado do HairDeck como
"Apache-2.0 no que é deles / termos dos pesos upstream não lidos"; e decidir se vale abrir um `DR` para
adotar a convenção do item 1 como formato de registro de pesos desta base.

## 12. Evidências

| Afirmação | Rótulo | Como foi medida |
|---|---|---|
| 123 `.py`, 16.566 linhas, 106 `def test` em 13 módulos, 1.568 linhas em `tests/` | `OBSERVED` | censo no clone + `grep -c "def test"` |
| 28 testes passam sem nenhuma dependência; 10 módulos não importam por `torch`/`PIL`/`trimesh`/`gradio`; 0 falha de asserção | `LOCAL_TESTS_PASS` (parcial) | `python3 -m unittest discover -s tests -p 'test_*.py'` × 2 (sistema e venv com numpy), saída integral em `/tmp/r24/ut1.txt` |
| Portão de Python 3.12 e relatório por área, exit 1 | `OBSERVED` | `python3 scripts/check_environment.py` com redirecionamento; saída `[FAIL] Python: RuntimeError: Use Python 3.12 x64 for the pinned release environment.` |
| Download de peso com `want` (sha256), `local_get`, `HF_ENDPOINT`, `--gated-source`, licença ao lado | `OBSERVED` (código lido) | `scripts/setup/download_weights.py`, linhas do `gated_get`/`local_get`/`hf_endpoint` |
| 20 JSONs de medição com hardware/torch/cuda/seeds e primeira × morna por estágio | `OBSERVED` (os arquivos), `DOCUMENTED` (o número) | `docs/measurements/**` lidos; nenhum reproduzido aqui |
| Zero CI, zero tag, zero release; `.gitattributes` sem LFS | `OBSERVED` | `find .github` vazio + `gh api …/releases` = `0` + `…/tags` vazio + `.gitattributes` lido |
| Proveniência: 36.440 / 36.455 chaves de treino e 76 / 100 de teste no formato `vroid-hair/<n>/<id>` | `OBSERVED` | contagem de linhas/elementos em `data/lists/*` |
| Termos de SAM 3 e DINOv3 | `BLOCKED` | `huggingface.co` fora da allowlist do ambiente (o mesmo bloqueio que medimos para `release-assets.githubusercontent.com`) |
| Pipeline de amostragem correto / saída de boa qualidade | `NOT_RUN` | precisaria de GPU + pesos; decisão de escopo, não ausência de ferramenta |
| Licença dos checkpoints confirmada contra a página de pesos | `NOT_RUN` | depende do mesmo host bloqueado; só o README afirma |
