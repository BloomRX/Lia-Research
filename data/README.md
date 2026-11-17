# data/ — inventário e evidência reproduzível

Este diretório guarda **dados derivados de coleta**, não pesquisa. É o único lugar do
repositório onde cabe material bruto — e mesmo aqui com regras.

## 1. Conteúdo

| Arquivo | O que é | Tamanho |
|---|---|---:|
| `inventory/lia-all-files.tsv.gz` | 58.478 arquivos dos 5 repositórios Lia, por branch | 679 KB |
| `inventory/lia-docs-by-branch.tsv.gz` | 1.620 documentos distintos e em quais branches vivem | 24 KB |
| `inventory/lia-docs-names.tsv.gz` | lista de nomes de documento + volumes | 1,6 KB |
| `inventory/lia-doc-versions.tsv.gz` | 644 documentos próprios da Lia com tamanho por branch | 11 KB |
| `inventory/corpus-manifest.tsv` | 236 documentos lidos, com tamanho e SHA-256 curto | 30 KB |
| `external/pinned-targets.tsv` | 14 repositórios externos: SHA pinado, licença, estrelas, datas | 2 KB |
| `snapshots/lia-corpus-2026-11-17.tar.gz` | cópia compactada pontual do corpus lido | 1,7 MB |

## 2. Por que um snapshot existe

Os documentos do corpus vivem em branches `arena/*` dos cinco projetos. Essas branches
são de sessão e **podem desaparecer** quando o trabalho de agente é encerrado. O
snapshot de 2026-11-17 preserva o que foi lido, com hash no manifesto, para que a
evidência citada em qualquer relatório continue verificável mesmo se a branch sumir.

**O snapshot não é fonte de verdade.** Se o projeto mudou, vale o projeto. O snapshot
está aqui para provar *o que existia quando a afirmação foi escrita* — nem mais, nem
menos.

## 3. Regras

1. Nada de segredo, token, cookie, host real ou dado pessoal (ver `governance/SECURITY-AND-PRIVACY-POLICY.md`).
2. Material de terceiros **não** é incluído: só manifestos com SHA, caminho e commit.
   A cópia de terceiros fica na origem; aqui só o ponteiro.
3. Todo arquivo aqui precisa de um lugar que o cite. Dado órfão é dado morto.
4. Reprodução: `tools/enum2.py` (árvore/documentos), `tools/fetch3.py` (corpus),
   `tools/collect.py` (metadados externos). Rodar de novo em outro dia dá números
   diferentes — é o esperado.

## 4. Data de coleta

Todos os números acima foram coletados em **2026-11-17** (fuso de São Paulo).
