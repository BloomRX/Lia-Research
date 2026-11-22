# anymachine — evidência numérica por peça de mecânica construída em Blender

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-013` |
| Nome | apekshik/anymachine |
| Tipo | repositorio |
| Fonte oficial | https://github.com/apekshik/anymachine |
| Responsável | `apekshik` |
| Estado da pesquisa | PARTIALLY_TESTED |
| Resultado de execução | BLOCKED |
| Recomendação | **REFERENCE_ONLY** |
| Decisão de adoção | — nenhuma registrada |
| Categoria | forge |
| Projetos beneficiados | Lia Forge (método de prova por objeto procedural), Lia Research (formato de log de verificacao) |
| Versão analisada | commit `d5e8889eef0bf63527b31f24f363cb31e0038f14` (main, 2026-11-17) |
| SHA completo | `d5e8889eef0bf63527b31f24f363cb31e0038f14` |
| Proveniência do SHA | **INFORMADO_NO_RELATORIO** — SHA do `main` lido da API de commits |
| HEAD atual | `d5e8889eef0bf63527b31f24f363cb31e0038f14` |
| Data | 2026-11-22 |
| Última verificação | 2026-11-22 |
| Upstream conferido | 2026-11-22 · HEAD `d5e8889e` · sem mudanca desde a análise |
| Próxima revisão | 2027-02-22 |
| Licença | **MIT** (`CONFIRMED` em `LICENSE`) |
| Confiança | Alta para conteúdo e método; baixa para executabilidade fora do Blender |

---

## 1. O que é

Um sistema de **geracao procedural de objeto interativo**: um agente usa o Blender via MCP para
construir mecanicas articuladas — teclado que digita, laptop que fecha, mochila que abre, relogio que
anda — e entrega um GLB que funciona no navegador, "sem servidor, sem runtime". Nao e malha gerada por
rede neural: e geometria construida, com cada articulacao numerada e verificada.

★1.004 · 111 forks · **3 issues abertas** · 265.058 KB (~259 MB) · criado 2026-11-04 · ultimo push
2026-11-17T22:14Z · **nenhum release, nenhuma tag, nenhum topic**.

Contagem real da árvore: **579 blobs**, 103 arquivos `.py`, um `.glb` de 34,2 MB.

## 2. O objeto de valor: `PIPELINE.md`, 243 linhas de metodo

O `README.md` tem 6 linhas de marketing ("Built with Claude Code and AI agents"). O conteudo
pesquisavel e o pipeline — dez etapas, **reference-first**, cada uma com um produto nomeado:

| # | Etapa | Saida exigida |
|---|---|---|
| 1 | brief → "o que este objeto faz com as maos?" | lista de interacoes |
| 2 | turnaround: ~12 imagens do MESMO modelo | `refs/source/` |
| 3 | um close-up por mecanismo (fecho, dobradica, tranca, pulseira) | `refs/closeups/` |
| 4 | texto de estilo para material/cor | `refs/style.txt` |
| 5 | anatomia: partes, pares cinematicos, folgas, curso | `PARTS.md` |
| 6 | geometria parametrizada | script construtor (um por peca) |
| 7 | render por passo de verificacao | `checks/` |
| 8 | referencia de movimento por articulacao | `refs/motion/` |
| 9 | teste interativo | driver + `states/` |
| 10 | teste de colisao + casca fisica | `collision_check` + `check.json` |

A regua de custo, dita sem eufemismo: a aranha de 8 pernas levou **40 imagens de referencia, um script
de ~2.200 linhas e ~40 renders de comparacao**; o Stilt e "a quarta maquina construida assim, e a
primeira com cada articulacao referenciada, movida e testada". E a linha de honestidade mais util do
arquivo inteiro:

> "A aranha de oito pernas nao generaliza: as geradoras davam seis pernas, as oito vem do brief."

E, na mesma pagina, a regra que o Lia precisa ouvir sobre o que e offline: "o teste da peca
(`blender -b -P scripts/_check.py -- <raiz>`) so abre arquivos locais, constroi, renderiza e
verifica — nenhuma rede; so os geradores de referencia e video precisam de `FAL_KEY`".

## 3. A peca que torna a reivindicacao auditavel: um `check.json` por objeto

`scripts/blender/validate/check.py` produz um arquivo por peca no diretorio da build, com as
tolerancias do autor como padrao e numeros medidos como saida. Lidos nesta sessao:

| Peca | Conteudo medido | Resultado |
|---|---|---|
| `laptop` | `{steps: 136, any_overlap: false, min_clearance_mm: 0.319, clamp: 135.0 mm}` | **pass** |
| `rolltop` | `states: 159, tol_mm: 4.0, max_penetration_mm: 0, tri_overlaps: 0, cover: pass` | **pass** |
| `daypack` | `states: 212, max_penetration_mm: 6.5, tri_overlaps: 1619`, slider do zipper em 14,45 mm | **fail** (commitado assim mesmo) |
| `rucksack` | tampa `pass: false, penetration 11.61 mm, 179 de 10.792 triangulos`; fivela 13,69 mm | **fail** |

E o oposto do catalogo de sucesso. A peca falha, o numero da falha fica no repositorio, e o `README`
das builds descreve o estado real ("the daypack's sternum strap and lid buckles still clash under
animation, so those are work in progress"). Nenhum dos ~16 projetos desta base faz isso com objetos
procedurais; o Lia Studio tem `evidenceLevel: unreviewed` em toda a biblioteca de Skills e nada
numerico equivalente.

## 4. Fronteira de licença, medida com cuidado (e o motivo de ser `REFERENCE_ONLY`)

| Item | Licença | Como sei |
|---|---|---|
| codigo, scripts, GLB | **MIT** | `LICENSE` no commit |
| imagens em `media/` | **direito dos criadores**, usadas como referencia/ilustracao | `media/LICENSE.md` ("Images belong to their creators and are used here for reference and illustration. Code and models are under the repository's MIT License.") |
| `data/` (incluindo `data/3dmodels/`) | **desconhecida** | nenhuma busca por arquivo de licenca dentro de `data/` retorna nada |
| pesos para as 4 funcoes opcionais | **fora do repositorio** | `models/README.md`: "Nothing here is downloaded to your repo; models live in `~/.anymachine/models/`"; "Nothing is required — the core (build, check, game) runs with no weights at all" |

`models/README.md` e o exemplo mais limpo que vi de separacao de camadas: 4 funcoes (`image-edit`,
`video-gen`, `image-gen`, `text-gen`) x backend, cada uma com "Where the model comes from" explícito
(`huggingface.co`, `github.com`) — e o texto de instalacao abre com o aviso de que "o maior e ~13 GB e
**prefers CUDA**, e os menores querem MLX ou ONNX DirectML". Nao localizei declaracao de licenca nos
arquivos de `models/`, portanto nao se sabe se **os pesos** permitem redistribuicao ou uso comercial.
Nao verifiquei.

Comparacao que justifica o veredito: `LR-FORGE-011` (Bosch, `image-render-generative`) foi
`PARTIALLY_TESTED` porque da para importar e instalar; aqui o `LICENSE` e MIT (melhor que o do Bosch em
termos de reuso), mas **nada e instalavel**: os 103 scripts sao scripts de sessao de agente (com
`from build import ...` resolvido por manipulacao manual de `sys.path` dentro de `check.py`) e nao um
pacote — o `pyproject.toml` existe, mas sem entry point de biblioteca, e nao ha teste nenhum no
repositorio. E o caminho de verificacao exige um Blender que a sandbox nao tem.

## 5. Execução e o que bloqueou (registrado, nao resolvido por suposicao)

| Etapa | Resultado |
|---|---|
| baixar o tarball do commit | 579 blobs, íntegro |
| `python3 -m compileall -q .` sobre a arvore inteira (CPython 3.11.2) | **exit 0 — os 103 `.py` compilam**, inclusive os que importam `bpy` |
| `shasum -a 256 -c CHECKSUMS.sha256` | **nao executado** neste ciclo (ver §7); os arquivos existem no commit |
| rodar `validate/check.py` na build do laptop | **BLOCKED**: nenhum `blender` no `PATH`; o script e `import bpy` puro e depende do `game_data.json` da build |
| auditar "navegador sem servidor" | fora do escopo: nenhum HTML aberto em navegador, o GLB de 34,2 MB nao foi medido |

## 6. Compatibilidade com o ecossistema Lia

| Alvo | Encaixe |
|---|---|
| Lia Forge | metodo de prova por peca mecanica: um `check.json` por artefato, com tolerancia e numero; falha commitada |
| Lia Studio | `PARTS.md` + pares cinematicos + folga em mm e o analogo procedimental do "asset quality bar" |
| Lia Research | formato: `PIPELINE.md` como documento de metodo versionado junto do artefato, em vez de README de marketing |
| Lia Agent Hub | o `SKILL.md` deles e curto e generico (10 linhas de "process") — nao e modelo a seguir |

## 7. Riscos

- **Nenhum teste automatizado no repositorio**: zero arquivos de teste; a verificacao e o `check.py`
  manual por peca. Sem Blender, nao ha como reproduzir.
- **`FAL_KEY`** para os geradores de referencia/video (falha com mensagem explicita: "This project does
  not bundle media") → custo real de uso dos modos de imagem/video, valor nao pesquisado aqui.
- A lista de APIs de terceiros no `README` inclui provedores pagos: nada foi aberto, nenhum custo
  estimado — `NOT_PRICED`.
- Sem releases/tags, a unica ancora e o SHA do commit; e o `CHECKSUMS.sha256` **nao foi verificado
  nesta sessao** — registrar essa lacuna e mais honesto do que assumir que bateria.

## 8. Recomendação

**`REFERENCE_ONLY`** — adotar **o metodo de verificacao**, nao o software. Concretamente, para o Lia
Forge: cada artefato procedural gerado por agente deveria ter um JSON de verificacao commitado ao lado
(estados, folga minima em mm, contagem de intersecoes, veredito), e a falha **precisa** poder ser
commitada. O `tools/validate.py` desta base cobre coesao de catalogo, nao qualidade de artefato — esse
segundo degrau e exatamente o que o anymachine mostra existir.

## 9. Evidências

| Afirmativa | Rótulo | Base |
|---|---|---|
| 579 blobs, 103 `.py`, 1 `.glb` de 34,2 MB, zero releases/tags | `CONFIRMED` | tarball do commit + API do GitHub |
| 103 de 103 `.py` compilam em CPython 3.11.2 | `OBSERVED` | `python3 -m compileall -q .` → exit 0 |
| MIT em codigo + GLB; imagens sob direito dos criadores; `data/` sem licenca | `CONFIRMED` | `LICENSE`, `media/LICENSE.md`, busca em `data/` |
| pesos fora do repo em `~/.anymachine/models/`; core roda sem pesos | `CONFIRMED` | `models/README.md` |
| `check.json` por peca com pass/fail numerico (136 steps / 0,319 mm; daypack fail 6,5 mm; rucksack fail 11,61 mm) | `CONFIRMED` | quatro arquivos lidos em `builds/` |
| pipeline de 10 etapas com produtos nomeados; custo da aranha explicitado | `CONFIRMED` | `PIPELINE.md` lido (243 linhas) |
| rodar o verificador local | `BLOCKED` | sem `blender` no PATH |
| `CHECKSUMS.sha256` integro | `NOT_RUN` | nao executado neste ciclo |
| qualidade das mecanicas no navegador; "zero cost"; "works with any agent" | `UNVERIFIED` | nada aberto em navegador nem em outro host |
| custo de `FAL_KEY` e dos provedores listados | `NOT_PRICED` | nenhum preco pesquisado |
| ★1.004 · 111 forks · 3 issues · 265.058 KB · push 2026-11-17T22:14Z | `CONFIRMED` | API do GitHub, 2026-11-22 |

## 10. Próximos passos

1. Levar o formato do `check.json` para a conversa de assets do Studio/Forge (uma linha de
   especificacao, nao codigo deste projeto).
2. Revisao em 2027-02-22; gatilho objetivo: saida de um release/tag, ou adicao de teste automatizado.
3. Nenhuma nova execucao: sem Blender neste ambiente, repetir a tentativa so gasta ciclo.

---

Voltar: indice `RESEARCH-INDEX.md` (secao 1) · objeto irmao `repositories/image-render-generative/REPORT.md`.
