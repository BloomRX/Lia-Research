# Comparação — modelos de expressão de licença em projeto

| Campo | Valor |
|---|---|
| ID | `LR-CMP-001` |
| Pergunta | como expressar licença e proveniência em repositório com código próprio + material de terceiro + assets |
| Data | 2026-11-17 |
| Evidência | `CONFIRMED` (arquivos lidos na origem) |

## 1. Os quatro modelos observados

| Modelo | Exemplo | Como funciona | Força | Fraqueza |
|---|---|---|---|---|
| **Licença única na raiz** | `openjarvis` (Apache-2.0), `unslop` (nenhuma) | um `LICENSE` cobre o repo | simples | mente quando há terceiro ou asset |
| **Mapa por diretório no LICENSE** | `rescript-lang/rescript` | o `LICENSE` declara qual licença vale em cada pasta (`compiler/` LGPL, `runtime/` MIT) | correto em licença mista | exige leitura; badge do GitHub mostra "Other" |
| **Árvore `LICENSES/` (REUSE)** | `manimgx` | um arquivo de licença por licença usada | legível por máquina; fácil auditar | mais arquivos; exige disciplina |
| **`NOTICE` por camada de conteúdo** | `pixelfx` | `NOTICE.md` diz que `sim.js` adapta obra MIT de X, e que a fonte da galeria **não** é coberta pela licença do repo | resolve o caso "código meu + trecho de outro" | depende de alguém manter |

## 2. O caso Lia

O ecossistema tem os três problemas de uma vez:

1. código próprio sem licença declarada (`lia-*` Skills, 47);
2. material de terceiro adaptado sem NOTICE dentro do payload (12 Skills do Studio + 5 do mr-mak);
3. assets gerados cuja licença depende da ferramenta (`LR-LIC-002`).

Nenhum dos quatro modelos, sozinho, resolve os três.

## 3. Combinação recomendada (proposta, não decisão)

```text
LICENSE                  → licença do código próprio do projeto
LICENSES/                → uma entrada por licença presente (REUSE)
NOTICE.md                → o que foi adaptado de quem, com commit
<skill>/NOTICE           → aviso viajando junto com o payload exportável
```

Isso corresponde ao modelo `manimgx` + `pixelfx`, com o mapa de `rescript` apenas quando
um diretório tiver licença diferente da raiz.

## 4. O que esta comparação **não** decide

Qual licença usar (`DR-0001`) e se haverá distribuição. São decisões do titular.
