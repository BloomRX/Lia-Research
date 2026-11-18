# Política de licença e proveniência

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
| `witnesstodark/mr-mak-workspace` | MIT (+ `img2threejs` Apache-2.0) | 5 skills adaptadas + ZIP guardado | `ADAPT_ALLOWED` / `RESEARCH_ONLY` | ler licença do subprojeto; decidir se ZIP de 9,9 MB continua versionado |
| `Kc1t/alethe-orchestrate-skill` | verificar na origem | skill vendorizada no Lia-Project | `FORK_CANDIDATE` (com patches) | registrar patches e aviso |
| AIRI (`moeru-ai/airi`) | MIT (Neko Ayaka) `CONFIRMED` | 890 arquivos de doc + **28 Skills** vendorizadas no Lia-Project | 4 `USE_AS_IS` · 5 `ADAPT_ALLOWED` · 19 `RESEARCH_ONLY` (`LR-LIC-003`) | separar o que é Lia do que é upstream |

Nenhuma linha desta tabela constitui licença nova nem autorização de distribuição.

## 8. Registro de decisão

Toda mudança de classe de aproveitamento exige registro em `decisions/` com:
objeto, licença lida (commit), obrigações, quem decidiu, data, e o que muda no
produto. Pesquisa não altera classe; pessoa decide.
