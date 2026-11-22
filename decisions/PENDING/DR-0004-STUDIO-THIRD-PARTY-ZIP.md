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
