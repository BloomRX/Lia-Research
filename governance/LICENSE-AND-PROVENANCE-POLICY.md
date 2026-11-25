# Política de licença e proveniência

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


> Este documento não é parecer jurídico. É um procedimento para impedir que o
> ecossistema Lia redistribua algo que não pode.

---

## 1. Camadas separadas

Licença de **código** ≠ licença de **conteúdo** ≠ licença de **documentação** ≠
licença de **pesos de modelo** ≠ direito de **marca**. Cada camada é registrada
separadamente. Um repositório MIT pode conter assets com outra licença (caso real:
`witnesstodark/mr-mak-workspace`, cujo subprojeto `img2threejs` é Apache-2.0).

## 2. Regras inegociáveis

1. **Ausência de `LICENSE` significa todos os direitos reservados**, não "livre".
   Exemplo medido: `theclaymethod/unslop` (★1.132, 2026-11-17) não tem arquivo de
   licença. Uso: `RESEARCH_ONLY`. Nenhuma cópia.
2. **Repositório público não é autorização.** Visibilidade ≠ licença.

   **Modelo recomendado para conteúdo misto (evidência externa `LR-SEC-006`):** licença
   única por **classe de arquivo**, declarada no cabeçalho da política e no manifesto do
   pacote — código sob uma licença, conteúdo (`*.md`, wordlists, catálogos, rubricas) sob
   outra, com `NOTICE` + arquivo de créditos listando origem e contagem por categoria.
   O repo auditado usa MIT para código e CC BY 4.0 para conteúdo, com a fronteira escrita
   em uma frase ("`*.py`/`*.sh` são MIT; `*.md`/wordlists/rubricas são CC BY 4.0").
   Duas falhas do mesmo repo servem de aviso: `plugin.json` declarava só `MIT`, e o
   `NOTICE` contradizia o arquivo de créditos sobre redistribuição de terceiros.
3. **Estrelas não são licença.** Popularidade não cria permissão.
4. **O selo do GitHub não é a licença.** Ler o arquivo. `NOASSERTION` e `null`
   exigem leitura manual.
5. **Licença de terceiro não se estende ao nosso uso.** MIT permite adaptar com
   aviso; não permite usar a marca do autor.
6. **Copyleft exige decisão de arquitetura, não de bom senso.** GPL-3.0 em
   biblioteca incorporada obriga a liberar o conjunto; usar como processo separado
   (`CONFIRMED` apenas se houver análise dedicada) é outra história.
7. **Pesos de modelo têm licença própria**, frequentemente com limite de receita,
   proibição de uso comercial ou cláusula de uso aceitável.
8. **Ambiguidade vira pendência humana.** Nunca decisão do agente.

## 3. Classes de aproveitamento

| Classe | Significado | Consequência prática |
|---|---|---|
| `USE_AS_IS` | licença permissiva, obrigações compatíveis, sem modificação | pode usar/catalogar mantendo o aviso |
| `ADAPT_ALLOWED` | permite derivação sob condições | adaptar **cumprindo** as condições |
| `FORK_CANDIDATE` | há motivo técnico para fork | exige motivo escrito e avisos preservados |
| `INDEPENDENT_REIMPLEMENTATION` | ideia/comportamento público pode ser reimplementado | registrar a referência e o processo independente |
| `RESEARCH_ONLY` | útil para estudo, sem permissão clara | nenhuma cópia |
| `BLOCKED` | licença incompatível (AGPL de rede, NC, ND), ausente ou impedimento | não copiar, não adaptar, não redistribuir |

## 4. Obrigações por licença (referência rápida)

| Licença | Aviso | Texto da licença | Indicar alterações | Copyleft | Marca |
|---|---|---|---|---|---|
| MIT | sim | sim | não exigido | não | não licenciada |
| Apache-2.0 | sim | sim | **sim** | não | não licenciada |
| BSD-3 | sim | sim | não | não | não licenciada |
| GPL-3.0 | sim | sim | sim | **sim, forte** | não |
| AGPL-3.0 | sim | sim | sim | **sim, inclusive uso em rede** | não |
| Sem licença | — | — | — | todos os direitos reservados | não |
| CC-BY-4.0 (conteúdo) | sim | link | sim | não | não |
| CC-BY-NC | uso não comercial apenas | link | sim | — | não |
| Pesos (ex.: licenças "community") | conforme termo | conforme termo | conforme termo | varia | varia |

## 5. Proveniência obrigatória por item consolidado

Todo item que entra no Lia-Research carrega:

```yaml
fonte_repositorio: BloomRX/Lia-Project
fonte_branch: arena/7fa837f0-lia-project
fonte_caminho: docs/research/LIA-MODEL-PROVIDER-CATALOG.md
fonte_commit: 005a324 (data 2026-11-17)
data_coleta: 2026-11-17
modo: resumido | citado | copiado-integral | referenciado
licenca_do_objeto: não identificada no payload
autoria: Lia / terceiro / desconhecida
```

`modo: copiado-integral` exige justificativa e preservação de avisos.

Quando o objeto **não é um caminho do Git e sim um artefato publicado** (ZIP, AppImage, wheel,
binário de release), os quatro campos abaixo entram no lugar de `fonte_commit` como âncora — e o
hash **não** depende de baixar o arquivo:

```yaml
fonte_release: v0.4.14
asset_publicado: Mr-Mak-Skills-0.4.14.zip
tamanho_bytes: 3352656
digest_asset: sha256:9e4ad7fe…08ee2   # gh api repos/<dono>/<repo>/releases → .assets[].digest
```

Motivo, medido em 2026-11-25: baixar asset de release pode cair fora da allowlist de rede de um
sandbox de pesquisa (302 para `release-assets.githubusercontent.com`, 0 bytes), mas o GitHub já serve
o SHA-256 de cada asset na API de releases. Reconstruir o empacotador no commit da tag prova o
**algoritmo**, não o **artefato** — identidade de pacote se fecha por digest. Caso completo:
`repositories/mr-mak-workspace/REPORT.md` §14, e a pendência de registro em
`decisions/PENDING/DR-0004-STUDIO-THIRD-PARTY-ZIP.md`.

Consequência prática para a matriz: um objeto distribuído **só** por release (caso medido:
`nanocle/Charakuru`, `LR-FORGE-020` — o repositório contém 0 arquivos de código) não pode ter
afirmação de comportamento marcada como `TESTED`; no máximo `DOCUMENTED` + `BLOCKED` no artefato.


## 6. Skills `lia-*`

Situação medida em 2026-11-17:

- 47 Skills autorais/adaptadas; **0 com arquivo de licença dentro do payload**;
- o importador do Agent Hub detecta licença apenas por arquivo na raiz do payload
  → as 47 entrariam como `licenseKnown: false`;
- 12 Skills do Studio têm seção `## Origem` apontando o commit upstream (bom), mas
  o aviso MIT vive na raiz do repositório, **fora** do pacote exportável: se a
  Skill viajar sozinha, o aviso não viaja.

Consequência: antes de qualquer distribuição de Skill para usuário final, é
necessário (a) decisão de licenciamento das Skills Lia e (b) empacotamento do
`NOTICE`/`THIRD_PARTY_NOTICES.md` **dentro** do pacote.
Registro: `decisions/PENDING/DR-0001-LIA-SKILLS-LICENSING.md`.

## 7. Terceiros já consumidos pelo ecossistema (estado, não permissão nova)

| Upstream | Licença lida | Uso atual | Classe | Pendência |
|---|---|---|---|---|
| `Donchitos/Claude-Code-Game-Studios` | MIT | 7 skills adaptadas no Studio | `ADAPT_ALLOWED` | aviso dentro do pacote |
| `witnesstodark/mr-mak-workspace` | MIT (+ `img2threejs` Apache-2.0 lida na origem) | 5 skills adaptadas + ZIP guardado | `ADAPT_ALLOWED` / `RESEARCH_ONLY` | ZIP identificado por reconstrução (tags v0.4.14→v0.5.0): falta registrar **tag + hash**, não identificar o arquivo |
| `Kc1t/alethe-orchestrate-skill` | verificar na origem | skill vendorizada no Lia-Project | `FORK_CANDIDATE` (com patches) | registrar patches e aviso |
| AIRI (`moeru-ai/airi`) | MIT (Neko Ayaka) `CONFIRMED` | 890 arquivos de doc + **28 Skills** vendorizadas no Lia-Project | 4 `USE_AS_IS` · 5 `ADAPT_ALLOWED` · 19 `RESEARCH_ONLY` (`LR-LIC-003`) | separar o que é Lia do que é upstream |

Auditoria do upstream no commit `f096373f` (2026-11-22), em `repositories/mr-mak-workspace/REPORT.md`
(`LR-STUDIO-012`): `LICENSE` MIT com detentor coletivo ("Mr. Mak Workspace contributors") e
`THIRD_PARTY_NOTICES.md` cobrindo imagens, samples de IA e marca. O `img2threejs` é Apache-2.0 e a
pendência de `NOTICE` que a auditoria inicial apontou **não existe**: a árvore inteira do upstream tem
só `LICENSE`, então não há `NOTICE` a reter (cláusula 4(d) satisfeita) — a retratação está na §13 do
relatório. O erro real do vendoring deles foi outro: a chave `version:` foi movida para dentro de
`metadata:`, e os testes de release do próprio projeto falham por isso.

Nenhuma linha desta tabela constitui licença nova nem autorização de distribuição.

## 8. Registro de decisão

Toda mudança de classe de aproveitamento exige registro em `decisions/` com:
objeto, licença lida (commit), obrigações, quem decidiu, data, e o que muda no
produto. Pesquisa não altera classe; pessoa decide.

## 9. O selo não é a licença (achado de 2026-11-20)

A API do GitHub devolve **uma** licença por repositório, detectada por heurística. Ela erra
em três direções, todas observadas nesta base:

| Caso | O que a API disse | O que o arquivo diz | Efeito prático |
|---|---|---|---|
| `storytold/photocraft` (pasta `artcraft`) | `Apache-2.0` | `LICENSE-MIT` **e** `LICENSE-APACHE` | o consumidor pode escolher MIT; quem lê o selo perde a opção |
| `ahwootech/BRUTAL` | `NOASSERTION` | licença própria de atribuição gráfica em `LICENSE.txt` | há licença, só não é OSI — a API não sabe ler |
| `theclaymethod/unslop` | ausência (`404`) | nenhum arquivo | aqui o "não" está certo: sem arquivo, sem permissão |

Regra: licença se lê no **arquivo**, no commit pinado, e se registra o caminho lido. Selo,
badge e `license` da API servem para triagem, nunca para o parecer.
