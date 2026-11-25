# Como se lê uma licença dividida: o método aplicado a 20 repositórios, e os nove formatos que encontrei

| Campo | Valor |
|---|---|
| ID | `LR-LIC-006` |
| Categoria | licensing |
| Objetos cobertos | `AppFlowy-IO/AppFlowy`, `appflowy-editor`, `AppFlowy-SelfHost-Commercial`, `appflowy-ai-plugins`, `opf/openproject`, `opf/openproject-agent-skills`, `opf/recense`, `calcom/cal.diy`, `chatwoot/chatwoot`, `capsoftware/cap`, `every-app/open-seo`, `debpalash/VoiceStudio`, `OpenWhispr/openwhispr` |
| Projetos beneficiados | todos os cinco; `lia-multiplatform` e `lia-studio` em particular (fronteira código × pesos), e o `data/inventory/license-matrix.tsv` |
| Fontes | `LICENSE`/`LICENSE*` decodificados por repositório via API; árvore recursiva (`git/trees/HEAD?recursive=1`, `truncated: false`) filtrada por `ee/`, `enterprise/`, `premium/`; clone raso onde houve teste de deriva; `LICENSE-NOTICE.md`, `enterprise/LICENSE`, `licenses/LICENSE-MIT`, `SELF_HOST_LICENSE_AGREEMENT.md` |
| Estado | DOCUMENTED — nenhum parecer jurídico; é o que os arquivos dizem |
| Recomendação | **ADAPT** o método (cinco passos, §2) como rotina desta casa; **não** adotar nenhuma das licenças como decisão |
| Decisão de adoção | — nenhuma registrada |
| Data | 2026-11-24 · ampliada em 2026-11-25 com mais 10 objetos medidos nesta base |
| Status | CURRENT — **não é parecer jurídico** |
| Confiança | Alta para os arquivos lidos; média para o que uma fronteira *significa* juridicamente (marcado em cada linha) |

---

## 1. Por que um documento de método em vez de mais uma tabela de licenças

O `READY-TO-USE-LICENSES.md` desta casa responde "o que cada projeto pode fazer". Este responde a
pergunta que apareceu nesta leva: **o que fazer quando o campo `license` da API não é uma licença**. De
treze repositórios medidos, três vieram como `NOASSERTION` e quatro como ausentes — e em todos os sete o
arquivo na raiz contava uma história que o campo não conta. A conclusão operacional é curta: `NOASSERTION`
quer dizer "leia o arquivo, há mais de uma licença"; `NONE`/`nenhuma` quer dizer "não há arquivo, procure
o acordo".

Foi assim que apareceram os três formatos abaixo — e o detalhe que importa para a Lia não é qual formato
é "melhor", é que **cada um muda o que quem consome tem de verificar antes de usar**.

## 2. O método, em cinco passos (todos executáveis com API, sem clone)

1. **`LICENSE` da raiz, por inteiro** — não o `spdx_id`. Aqui, o `head -c 600` bastou para separar AGPL de
   GPL de MIT de "composto", e o texto composto começa com os bullets que definem tudo;
2. **censurar `LICENSE*` na árvore recursiva** (`git/trees/HEAD?recursive=1`): quantos arquivos, em que
   diretórios. O `cal.diy` tem sete `LICENSE` além do raiz, todos MIT; o `opf/openproject` tem o raiz +
   módulos + fonte de ícones; o `cap` tem **um** (`licenses/LICENSE-MIT`) referenciado pelo raiz;
3. **procurar a fronteira na árvore, não na descrição**: `(^|/)(ee|enterprise|premium)/`. Medido:
   `chatwoot` = 759 blobs em `enterprise/`; `opf/openproject` = **0**; `cal.diy` = **0**; `cap` = 0
   (a fronteira dele não é diretório comercial, é família de crate);
4. **procurar o acordo privado em vez da licença**: `*LICENSE_AGREEMENT*`, `LICENSE-NOTICE*`,
   `NOTICE*`, `THIRD_PARTY*`. Deu: `SELF_HOST_LICENSE_AGREEMENT.md` (AppFlowy SelfHost Commercial),
   `LICENSE-NOTICE.md` (VoiceStudio), `THIRD_PARTY.md` (recense);
5. **registrar o que a fronteira exige do consumidor**, em uma frase por objeto — é a única coluna que o
   dono lê ("preciso de dois arquivos para redistribuir?", "posso rodar em produção?", "o binário tem
   fonte?").

O passo que quase todos pulam, e que mudou duas conclusões desta leva: **o bullet 1 do LICENSE composto**.
No Chatwoot ele é condicional ("**if that directory exists**"), o que significa que a licença do que você
baixa depende de um diretório poder estar ausente. No Cap ele nomeia **famílias de crates**. Nos dois casos
a licença "oficial" da API é inútil sem esse passo.

## 3. Os formatos medidos (nove)

| Formato | Quem (medido) | Como a fronteira é escrita | O que muda para quem consome |
|---|---|---|---|
| **A. diretório com licença própria** | `chatwoot/chatwoot` | raiz = "MIT Expat" exceto o que estiver sob `enterprise/`, "*if that directory exists*, is licensed under the license defined in 'enterprise/LICENSE'"; `enterprise/LICENSE` proíbe uso em produção sem assinatura | a licença depende da **presença de um diretório**; e existe artefato separado por variante (`publish_foss_docker.yml` × `publish_ee_docker.yml`) |
| **B. famílias de código com licença própria** | `capsoftware/cap` | raiz = AGPLv3 com exceção MIT "**All code residing in the `cap-camera*` and `scap-*` families of crates** … see licenses/LICENSE-MIT" | redistribuir exige **carregar os dois arquivos**; a fronteira segue o que toca hardware, não o que é comercial |
| **C. licença única + aviso separado** | `debpalash/VoiceStudio` | `LICENSE` = AGPL-3.0 **e** `LICENSE-NOTICE.md` declarando (i) "That **includes commercial and internal business use** of the application itself", (ii) "Model weights, tokenizers, and other third-party assets **retain their own terms**", (iii) a obrigação AGPL de modificação em rede | a fronteira **não é estrutural** (nada é cortado da árvore), é **declarada** — o que é a melhor opção para produto com pesos, e a pior para quem quer fechar parte do código |
| D. dual-licença por componente | `AppFlowy-IO/appflowy-editor` | "All code contributed to the AppFlowy Editor project is **dual-licensed**" (AGPL-3.0 + MPL-2.0) | o *consumidor* escolhe; é o único caso medido em que usar sem copyleft é defensável sem pedir nada a ninguém |
| E. sem licença, com acordo | `AppFlowy-IO/AppFlowy-SelfHost-Commercial` | **nenhum `LICENSE`**; `SELF_HOST_LICENSE_AGREEMENT.md` ("non-exclusive, non-transferable license to use the Software for your internal …") de AppFlowy Pte. Ltd. | clone ≠ direito de uso; e **não há fonte do que roda** — o servidor virou imagem Docker (`LR-FORGE-015` §4) |
| F. MIT puro por remoção | `calcom/cal.diy` | raiz MIT em 21 linhas, **zero** ocorrências de AGPL/Affero; 0 `ee/`; 7 `LICENSE` aninhados também MIT | o que você consome é MIT de verdade — **mas** a máquina de validação de chave continua no código com o serviço devolvendo `return true` (`LR-FORGE-019` §3): a fronteira comercial saiu da licença, não das rotas |
| **G. elegibilidade quantitativa do lado do usuário** | `nanocle/Charakuru` | licença própria de 287 linhas: "Covered Materials" **inclui as Skills e o texto de referência delas**; uso gratuito se pessoal **ou** se faturamento e captação estiverem ambos abaixo de **JPY 100.000.000**; acima disso exige acordo escrito; fork no GitHub sempre permitido (§4), publicar pacote ou app hospedado a partir dele nunca sem autorização | a pergunta deixa de ser "que licença é" e passa a ser "em que faixa eu estou, e quando isso é reavaliado"; e o §5 renuncia explicitamente a "ideias, técnicas, workflows" — **o padrão é reimplementável, a expressão não é copiável** |
| **I. exceção por diretório com licença futura** | `dyad-sh/dyad` | raiz `NOASSERTION` porque o `LICENSE` abre com 2 *bullets*: tudo sob `src/pro/` vai para `src/pro/LICENSE` (FSL-1.1-ALv2, 104 linhas), o resto é Apache-2.0; `Grant of Future License` converte a parte fechada em Apache no prazo |
| **H. termos no artefato montado, não no repositório** | `hyz317/HairDeck` | uma frase no README ("code **and checkpoints** are licensed under Apache-2.0. Third-party models, code and datasets retain their respective licences"); **nenhum `NOTICE`** na árvore inteira (0 em 224 entradas); `scripts/setup/download_weights.py` baixa `LICENSE`/`LICENSE.md` dos modelos gated **para dentro do workspace**, com `sha256` esperado por arquivo | auditar o Git é insuficiente: a informação de termos não está no repositório, está no **diretório que o instalador monta**. O complemento é bom (proveniência viaja com o peso); a lacuna é real (o repo não enumera nada) |

## 4. Tabela dos 27 repositórios (o que foi lido, não o que a API diz)

| Objeto | `spdx_id` da API | Licença real lida | Fronteira na árvore | Aviso/NOTICE |
|---|---|---|---|---|
| `AppFlowy-IO/AppFlowy` | AGPL-3.0 | AGPL-3.0 (cópia verbatim do documento, preâmbulo incluído) | nenhuma | — |
| `AppFlowy-IO/appflowy-editor` | NOASSERTION | **dual AGPL-3.0 + MPL-2.0** | nenhuma | frase de dual-licença no topo do LICENSE |
| `AppFlowy-IO/AppFlowy-Cloud` (arquivado) | AGPL-3.0 | AGPL-3.0 | nenhuma | `SELF_HOST_LICENSE_AGREEMENT.md` **também** aqui |
| `AppFlowy-IO/AppFlowy-SelfHost-Commercial` | NOASSERTION | **nenhuma licença aberta** | n/a | acordo AppFlowy Pte. Ltd. |
| `AppFlowy-IO/appflowy-ai-plugins` | AGPL-3.0 | AGPL-3.0-only (confirmado em `plugin.json`: `license: AGPL-3.0-only`) | n/a | — |
| `opf/openproject` | GPL-3.0 | **GPL-3.0** (não AGPL) | **0** `ee/`/`enterprise/`/`premium/` | LICENSE em módulos e na fonte de ícones |
| `opf/openproject-agent-skills` | MIT | MIT — "Copyright (c) 2026 the OpenProject GmbH" | n/a | WARNING de maturidade no README (não é licença, é aviso) |
| `opf/recense` | MIT | MIT — "Copyright (c) 2026 **Recense contributors**" | n/a | `THIRD_PARTY.md` (Syft/Grype são componentes de terceiros pinados) |
| `opf/opilot` · `opf/openproject-llm-evals` | GPL-3.0 | GPL-3.0 | n/a | README "EXPERIMENTAL PROOF OF CONCEPT" |
| `calcom/cal.diy` | MIT | **MIT puro**, 21 linhas | **0** `ee/` | 7 LICENSE aninhados, todos MIT |
| `chatwoot/chatwoot` | NOASSERTION | MIT exceto `enterprise/` (formato A) | `enterprise/` com **759** blobs | `enterprise/LICENSE` próprio |
| `capsoftware/cap` | NOASSERTION | AGPLv3 exceto crates `cap-camera*`/`scap-*` = MIT (formato B) | por nome de crate | `licenses/LICENSE-MIT` único |
| `every-app/open-seo` | MIT | MIT — "Copyright (c) 2026 Ben Senescu" | nenhuma | um único LICENSE na árvore |
| `debpalash/VoiceStudio` | AGPL-3.0 | AGPL-3.0-only (formato C) | nenhuma | `LICENSE-NOTICE.md` + submódulo `omnivoice-gallery` **com licença própria não lida** |
| `OpenWhispr/openwhispr` | MIT | MIT — "Copyright (c) 2024 OpenWhispr Team" | não censurada por diretório | nenhum LICENSE aninhado procurado (limitação) |
| `nanocle/Charakuru` | **NOASSERTION** | **sem SPDX**: `Charakuru Source-Available License and Terms of Use`, v1.2, 2026-10-07 (287 linhas, 11 seções, inglês autoritativo) | nenhum `ee/` — a fronteira é **o usuário** (limiar de faturamento) e os ativos do pacote (não extraíveis, §8) | `THIRD_PARTY_NOTICES.md` com 5 linhas + os 5 arquivos de licença em `public/`; MIT ×4 (three.js, fflate, three-vrm ×2) e SIL OFL 1.1 (Orbitron) |
| `hyz317/HairDeck` | Apache-2.0 | Apache-2.0 no código **e nos checkpoints** (declaração de uma linha no README) | nenhuma fronteira no repo; o empilhamento vem dos modelos gated que o instalador baixa | **nenhum** — 0 arquivos `NOTICE`; os termos dos upstream chegam como arquivo no workspace |
| `aaif-goose/goose` | Apache-2.0 | Apache-2.0 | nenhuma (1 `LICENSE` em 3.130 entradas) | nenhum `NOTICE` na árvore |
| `bytedance/deer-flow` | MIT | MIT **no código**, com exclusão de produto/marca dentro do próprio arquivo | 7 caminhos `LICENSE`, 4 em `examples/deerflow-extension-*` | `README.md:556` avisa que Skills podem ter outra licença |
| `anthropics/skills` | **nenhuma** (`null`) | nenhuma na raiz; **18 `LICENSE.txt` um-por-Skill** com `license: Complete terms in LICENSE.txt` no frontmatter | 0 `LICENSE` raiz; Skills em `skills/*/` | `THIRD_PARTY_NOTICES.md` (404 linhas) cobre os terceiros |
| `obra/superpowers` | MIT | MIT (1.070 B) | nenhuma por Skill: **15 `SKILL.md`, 0 licenças ao lado** | nenhum |
| `pipecat-ai/pipecat` | BSD-2-Clause | BSD-2-Clause | 3 caminhos: raiz + `LICENSE-shadcn.md` **dentro do template vendorizado** | aviso do componente viaja com o componente |
| `D4Vinci/Scrapling` | BSD-3-Clause | BSD-3-Clause na lib **e** `LICENSE.txt` próprio na Skill | `agent-skill/Scrapling-Skill/` (Skill + ZIP versionados) | nenhum |
| `johannesjo/parallel-code` | MIT | MIT | 1 `LICENSE` em 2.085 entradas | `package.json` não declara `license` |
| `infiniflow/ragflow` | Apache-2.0 | Apache-2.0 (11.357 B) | 3 caminhos com "license", **2 são código do produto** (`internal/dao`, `internal/entity`) | nenhum |
| `daytonaio/daytona` | **nenhuma** (`null`) | AGPL-3.0 **só nas tags** (`v0.190.0`, 34.522 B); a `main` não tem `LICENSE` (404) | 3 arquivos na árvore: `README.md` + 2 PNG | o `README` ancora o link da licença na tag (commit 2026-06-25) |
| `dyad-sh/dyad` | **`NOASSERTION`** | split declarado na 1ª linha do `LICENSE`: Apache-2.0 + `src/pro/` sob FSL-1.1-ALv2 | 5 caminhos `LICENSE` (raiz, `src/pro/`, 2 pacotes internos, 1 template de benchmark) | `remove-unauthorized-release.yml` apaga release fora do CI |

Duas linhas que valem o destaque que lhes dei: o `recense` é o único do censo com copyright em
"**contributors**" em vez de pessoa jurídica — escolha de titularidade visível no texto da licença; e o
`VoiceStudio` tem **um submódulo de terceiros fora do escopo da licença do repositório**, o que é o jeito
mais fácil de quebrar uma política de assets sem perceber (o mesmo tipo de problema do `DR-0004` desta
casa, do outro lado da mesa).

## 5. Consequências por projeto da Lia (sem decidir nada)

| Projeto | O que este censo esclarece |
|---|---|
| `lia-multiplatform` | dois precedentes de **AGPL com saída binária pública** (AppFlowy) e **AGPL com aviso de uso comercial permitido** (VoiceStudio). A diferença entre eles é só o NOTICE — o que barateia a decisão de escrever um |
| `lia-studio` | o formato C é o único dos oito que **não exige cortar nada da árvore** para tratar pesos: declara. É o ajuste natural para o que o `DR-0004` revelou (pacote com conteúdo de terceiros sem NOTICE) |
| `lia-forge` | formato B (por família de crate) é o caminho se câmera/microfone forem crates separadas; formato A exige que a CI construa duas variantes, como o Chatwoot faz com dois Dockerfiles |
| `lia-agent-hub` | Skills: o `openproject-agent-skills` publica o pack em **MIT** enquanto o produto é GPL-3.0 — separar licença do conteúdo publicável para agentes é praticável; e o `cal.diy` publica a Skill de terceiros com `license:` no frontmatter |
| `lia-model-lab` | nada neste censo resolve termos de pesos: o `LICENSE-NOTICE.md` do VoiceStudio **remete** para os termos dos pesos, e o `recense` não tem pesos. A lacuna continua e é maior do que os arquivos medidos alcançam |
| Research (esta casa) | a regra do §2 deve virar rotina: nenhum objeto entra na matriz com base no `spdx_id` da API. A matriz tem 15 colunas; sugiro usar a coluna de evidência para o arquivo exato lido, como fiz nesta leva |

## 6. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Leitura integral das licenças (AGPL/GPL inteiras) | `NOT_RUN` | li cabeçalho + bullets de exceção + cláusulas nomeadas; o corpo padrão da FSF não foi re-lido por objeto |
| Licença de **cada** crate do Cap (só o `LICENSE` raiz e o `licenses/LICENSE-MIT`) | `NOT_RUN` | abrir os 40+ `Cargo.toml` é outra passada; anotei que a fronteira está declarada, não que foi verificada por crate |
| Licença de arquivos individuais dentro de `enterprise/` do Chatwoot | `NOT_RUN` | li o `enterprise/LICENSE` do diretório |
| `NOTICE` do ragflow, `helm-charts` e `daytona/sdk` | `NOT_RUN` | o censador desta rodada casou caminhos `LICENSE*`; um `NOTICE` não entra nessa contagem (é a limitação registrada em `LR-RAG-001` §5) |
| se o conteúdo de `src/pro/` respeita o preâmbulo de exceção do dyad | `NOT_RUN` | o diff por diretório não foi auditado |
| Termos dos modelos/pesos baixados por VoiceStudio e OpenWhispr | `BLOCKED` | nenhum peso foi baixado (regra da casa) e os termos no Hugging Face não foram abertos |
| Se o `SELF_HOST_LICENSE_AGREEMENT.md` do AppFlowy proíbe o que ele parece organizar | `UNVALIDATED` | li o preâmbulo e a cláusula 1; o documento continua além do trecho transcrito |
| Efeito jurídico de "if that directory exists" em redistribuição | `UNVALIDATED` | formulação lida; interpretação é para o dono + assessoria, não para a Research |
| Histórico de mudança de licença (ex.: AppFlowy-Cloud tinha AGPL e virou acordo?) | `NOT_RUN` | nenhum `git log` de LICENSE foi feito |
| Licenças das **123 − 77** repositórios-fork do org `opf` e dos 27 − … do `AppFlowy-IO` | `NOT_RUN` | forks herdam a licença do upstream; os agregados estão em `LR-FORGE-016` §2 |

## 7. Recomendações (proposta ao dono; nada aplicado)
> **Escopo desta seção** — o que segue é recomendação técnica desta base, não instrução para nenhum app. Se vale, cabe e é possível implementar em cada projeto é decisão do dono (`MISSION.md` §3: o Research não aprova nada).


1. **Adotar o método de cinco passos como rotina de casa** — escrito em uma linha em
   `governance/SECURITY-AND-PRIVACY-POLICY.md`? Não: o lugar correto é a Skill/checklist de auditoria de
   dependência, §8.
2. **Adicionar uma coluna implícita à matriz**: para cada objeto, registrar *quantos* `LICENSE*` existem na
   árvore e *se* há `ee|enterprise|premium`. São duas checagens de API por objeto, e foram exatamente elas
   que produziram os três formatos deste documento.
3. **Escrever o nosso `LICENSE-NOTICE.md`** (formato C) se o Lia Studio publicar pesos/modelos: três frases
   — uso permitido, o que os pesos retêm termos próprios, o que a obrigação de rede implica. O VoiceStudio
   prova que o custo é de uma página e o benefício é não discutir isso num issue.
4. **Não recomendo** o formato A ("if that directory exists"): favorece quem distribui e deixa quem
   consome dependendo de um diretório poder sumir.
5. **Decisão do dono**: (a) qual formato a Lia adota para o `lia-multiplatform` e para o Studio; (b) se a
   checagem da matriz (item 2) entra no `tools/validate.py` como aviso ou como erro; (c) se abrimos
   pendência para ler os termos dos pesos que o Studio consome (linha `BLOCKED` §6).

## 8. Checklist sugerido (se o dono quiser transformá-lo em Skill de auditoria de dependência)

```
para cada dependência nova:
  1. GET contents/LICENSE                 → tipo real, não o campo da API
  2. GET git/trees/HEAD?recursive=1       → contar LICENSE*, procurar (ee|enterprise|premium)/
  3. GET contents/                        → NOTICE*, LICENSE-NOTICE*, THIRD_PARTY*, .gitmodules
  4. registrar: nº de LICENSE na árvore, fronteira encontrada, arquivo exato lido
  5. se spdx == NOASSERTION → o item 1 é obrigatório e a linha da matriz precisa citar o trecho
  6. se houver submódulo → licença do submódulo é outra linha da matriz, não uma nota
```

## 9. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| Chatwoot: cláusula condicional + `enterprise/` com 759 blobs + `enterprise/LICENSE` restringindo produção | `CONFIRMED` | `LICENSE` e `enterprise/LICENSE` decodificados; contagem na árvore recursiva |
| Cap: MIT só para `cap-camera*`/`scap-*`, AGPLv3 no resto, `licenses/` com um único `LICENSE-MIT` | `CONFIRMED` | `LICENSE` lido na íntegra (3 bullets transcritos) + `contents/licenses` |
| OpenProject: GPL-3.0 sem `ee/`/`enterprise/`/`premium/` (0 blobs) e LICENSEs em módulos | `CONFIRMED` | árvore recursiva de 34.051 entradas (`truncated: false`) |
| Cal.diy: MIT puro, zero ocorrências de AGPL/Affero, 7 `LICENSE` aninhados MIT, 0 `ee/`, serviço de chave stubado em `return true` | `CONFIRMED` | `grep -ci` no LICENSE + filtro da árvore + `validateLicense.handler.ts` lido |
| VoiceStudio: AGPL-3.0-only + `LICENSE-NOTICE.md` com as três frases transcritas + submódulo `omnivoice-gallery` | `CONFIRMED` | `LICENSE`, `LICENSE-NOTICE.md`, `.gitmodules` |
| AppFlowy-SelfHost-Commercial: nenhum `LICENSE` na raiz, acordo de AppFlowy Pte. Ltd. com licença "non-exclusive, non-transferable … for your internal" | `CONFIRMED` | árvore da raiz + 620 caracteres do acordo |
| `appflowy-editor`: dual-licença declarada na primeira linha do LICENSE | `CONFIRMED` | `LICENSE` decodificado |
| `recense`: copyright "Recense contributors" | `CONFIRMED` | `LICENSE` lido |
| `NOASSERTION` na API correlaciona com licença composta (3 casos) e ausência de arquivo (4 casos) | `CONFIRMED` | confronto entre `license.spdx_id` e os arquivos lidos nos 16 objetos varridos |
| O que cada fronteira significa juridicamente; se o stub do cal.diy é ou não uma violação | `UNVALIDATED` | não é matéria de Research; nada aqui é parecer jurídico |
| Licenças dos 24 repositórios do `AppFlowy-IO` fora dos 5 varridos arquivo a arquivo | `REPORTED` | só o `spdx_id` da API, sem leitura do arquivo — por isso não entraram na tabela §4 |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 3) · tabela-mestra desta casa:
`cross-project/licensing/READY-TO-USE-LICENSES.md` · matriz: `data/inventory/license-matrix.tsv` ·
dossiês com os dados brutos desta leva: `repositories/appflowy-io/REPORT.md`,
`repositories/opf-openproject/REPORT.md`, `repositories/chatwoot/REPORT.md`, `repositories/cap/REPORT.md`,
`repositories/cal-diy/REPORT.md`, `repositories/voicestudio/REPORT.md`,
`repositories/open-seo/REPORT.md`, `repositories/openwhispr/REPORT.md` · decisão pendente sobre assets:
`decisions/PENDING/DR-0004-STUDIO-THIRD-PARTY-ZIP.md`.
