# DR-0004 — Destino do ZIP de terceiros no Lia-Studio

| Campo | Valor |
|---|---|
| ID | DR-0004 |
| Alcance | **GOVERNANCA** — decisão administrativa; não aprova adoção de tecnologia |
| Estado | **PENDING** |
| Dono | proprietário + responsável do Studio |
| Data | 2026-11-17 |
| Pesquisa | `LR-LIC-001` |

## Situação
`Lia-Studio:docs/Mr-Mak-Skills-Free.zip` — 9,9 MB, 764 arquivos, 20 skills de terceiros,
**não importadas**. O `THIRD_PARTY_NOTICES.md` do Studio registra que o ZIP não foi
comparado arquivo a arquivo com a fonte pública.

## Opções
| Opção | Efeito |
|---|---|
| A. Manter versionado | conveniência; 9,9 MB de terceiros com proveniência não verificada |
| B. Remover do Git e registrar hash + URL | proveniência clara, sem binário no repo |
| C. Auditar e importar skills selecionadas | requer licença por skill + NOTICE |
| D. Manter e auditar depois | dívida crescente |

## Recomendação de pesquisa
**B** (remover do versionamento mantendo registro de hash/URL), com C apenas após
auditoria. A remoção exige autorização do responsável do Studio — não é ação do agente.

*(Revista em 2026-11-22: a base desta recomendação era a proveniência desconhecida, que deixou de
existir — ver "Evidência nova". A B segue defensável, mas agora por peso de repositório; a ação mínima
passou a ser registrar tag + `sha256`.)*

## Evidência nova (2026-11-22, sem decisão) — inclui retificação

Auditoria do upstream em `repositories/mr-mak-workspace/REPORT.md` (`LR-STUDIO-012`, §7 e §13):

- **correção do diagnóstico anterior.** A primeira leitura desta auditoria comparou o tamanho
  *comprimido* dos assets publicados (3.352.656 B em `v0.4.14`, 4.263.307 B em `v0.6.0`) com os
  9,9 MB do arquivo local e concluiu que o ZIP "não corresponde a nenhuma release". A conclusão
  estava errada: 9,9 MB é o tamanho **extraído**. As unidades não eram as mesmas; não havia
  divergência nenhuma a explicar;
- reconstruir o empacotador do próprio autor (`scripts/package_skills.py`) no clone de cada tag dá,
  para **v0.4.14, v0.4.15, v0.4.16, v0.4.17, v0.4.19 e v0.5.0**, **764 entradas** e **9,83 MB
  descompactados** — o par exato registrado acima para o arquivo do Studio. O `main` atual
  (`f096373f`) dá 769 / 10,78 MB. O empacotador é determinístico: dois builds seguidos no `main`
  geraram o mesmo `sha256` do ZIP;
- o que **não** foi possível fazer neste sandbox: baixar os assets publicados (o `download`
  redireciona para fora da allowlist de rede) para confirmar o `sha256` do `.zip` daquela release e a
  lista real de arquivos. A identificação acima é **por reconstrução do conteúdo no commit da tag**,
  não por comparação de hash.

**Estado da pergunta, reescrito.** O ZIP não é um blob de proveniência desconhecida: é um pacote
oficial do projeto, de uma faixa de tags de 2026-09-30 a 2026-10-08, **defasado** em relação ao
upstream (5 arquivos e ~0,9 MB). A opção A ("manter versionado com proveniência não verificada") e a
C mudam de natureza; a B continua válida por outro motivo — peso no repositório, não risco de
proveniência. A ação mínima que fecha o pendente é de registro, na máquina do Studio:

1. `sha256sum docs/Mr-Mak-Skills-Free.zip` e gravar o hash no `THIRD_PARTY_NOTICES.md` deles;
2. anotar a **tag de origem** proposta pela reconstrução (v0.4.14…v0.5.0) como inferência, não como
   fato, até o hash bater com um asset baixado;
3. decidir **quando** reempacotar — o nome do arquivo não é evidência, o hash é.

Nada aqui é autorização para baixar, manter ou apagar o arquivo: decisão do proprietário e do
responsável do Studio.

## Por que a pergunta foi mal feita antes

Registrado como lição de método da base: antes de tratar um artefato derivado como desconhecido, (a)
conferir se as **unidades** comparadas são a mesma grandeza (comprimido × extraído, entrada de
manifest × arquivo em disco) e (b) **medir a origem** — clonar o commit de onde ele veio e reproduzir
o gerador — em vez de olhar só a vitrine de releases. Custou seis clones descartáveis e uma hora de
rede; a afirmação errada publicada teria encerrado um pendente com diagnóstico invertido.

## Evidência de 2026-11-25 — a pergunta técnica está encerrada (por hash, não por reconstrução)

A ação mínima que este registro deixava "na máquina do Studio" foi executada aqui, sem tocar no
Studio e sem baixar asset de release: o campo **`digest`** da API de releases do GitHub traz o
SHA-256 de cada asset, e o blob do próprio repositório do Studio responde pelo `git/blobs`.

| Grandeza | Lado Studio | Lado upstream publicado |
|---|---|---|
| caminho | `docs/Mr-Mak-Skills-Free.zip` (em 4 ramos `arena/*`; **ausente de `main`**) | asset `Mr-Mak-Skills-0.4.14.zip` da release `v0.4.14` |
| tamanho | 3.352.656 B | 3.352.656 B |
| blob Git | `af7648c2ea09aec8e79cb9c493b87acee4358fa2` (o mesmo nos 4 ramos) | — |
| SHA-256 | `9e4ad7fea76ffd982190a7a4eb7d4875e54138c4b7fc326d2259deab8bf08ee2` | `sha256:9e4ad7fea76ffd982190a7a4eb7d4875e54138c4b7fc326d2259deab8bf08ee2` |

**Identidade confirmada byte a byte.** Consequências diretas para este registro:

- a **"tag de origem proposta pela reconstrução (v0.4.14…v0.5.0) como inferência"** deixa de ser
  inferência: é `v0.4.14`, a única daquela faixa com pacote de Skills publicado. As tags `v0.4.15` a
  `v0.5.0` nunca publicaram esse asset;
- o item 1 da ação pendente (`sha256sum` local) está **respondido pela pesquisa** — o hash é o acima.
  O que resta de registro é colá-lo no `THIRD_PARTY_NOTICES.md` do Studio, com a tag;
- o item 3 continua vivo e é a única decisão real: **quando reempacotar**. O único pacote mais novo
  existente é `v0.6.0` (4.263.307 B, `sha256:45b3cbef…9e4e7`) — medido por tamanho e digest, conteúdo
  não aberto aqui;
- o nome do arquivo não é evidência: `-Free` não existe no upstream, foi acrescentado ao vendorizar;
- o "**9,9 MB**" deste documento, que gerou a retratação de 2026-11-22 sobre unidades, é o tamanho
  **extraído**: 9.940.122 B em 764 entradas, medidos agora no arquivo real. O `.zip` em si tem
  3.352.656 B — menos de 3,4 MB de peso no repositório, o que enfraquece a opção B quando ela era
  justificada por "peso no repo" e sobrepõe a ela a pergunta nova: **por que o arquivo existe em quatro
  ramos `arena/*` e não está no `main`?**

Recomendação reescrita, mantida a autoridade do dono: **registrar** (tag + digest no aviso de terceiros,
sem remover nada), **decidir o ramo de verdade** do `docs/` deles, e **não reempacotar por impulso** —
`v0.6.0` é a única atualização disponível e ela também precisa de registro. Nada foi aplicado fora
desta base: isto é sugerido ao dono e ao responsável do Studio.
