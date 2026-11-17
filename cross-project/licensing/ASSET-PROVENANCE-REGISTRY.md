# Registro executável de proveniência de assets — proposta

| Campo | Valor |
|---|---|
| ID | `LR-LIC-004` |
| Categoria | licensing |
| Projetos beneficiados | Lia Forge (primário), Lia Studio, Lia Agent Hub |
| Fontes | `Lia-Forge@a4fc756` (branch `arena/ee48e1c5-lia-forge`): `docs/T11-E3-ASSET-PROVENANCE-AND-CONTENT-VALIDATION.md` (6.490 B), `local-renderer-test/manifests/example-synthetic-own-asset.manifest.json` (**schemaVersion 2**); `docs/auditoria-blender-local/LICENCAS-E-DEPENDENCIAS.md`; `LR-LIC-002`, `LR-FORGE-004` (pixelfx NOTICE), `LR-FORGE-003` (manimgx `LICENSES/`) |
| Data | 2026-11-17 |
| Status | **PROPOSTA** (não implementada; nenhum asset baixado ou renderizado) |
| Confiança | **Alta** para o schema existente (lido no arquivo); média para a extensão proposta |

---

## 1. Pergunta

Existe hoje um registro de proveniência de asset que seja **executável** — que possa ser
validado por máquina, que sobreviva à cadeia de transformações e que distinga metadado
obrigatório de opcional?

## 2. O que já existe (e não deve ser reinventado)

O Lia Forge **já tem** um manifesto de proveniência, `schemaVersion: 2`, com campos que
resolvem a maior parte do problema (`CONFIRMED` no arquivo):

| Grupo | Campos reais |
|---|---|
| Identidade | `id`, `sourceVersion`, `characterTitle`, `sourceFormat`, `preparedWithBlenderVersion` |
| Autoria | `authorship.author`, `authorship.modifications`, `authorship.derivedFrom` |
| Licença e evidência | `licenseRecord.status`, `sourceUrl`, `exactTermsUrlReviewed`, `termsReviewDate`, `localRenderingConfirmed`, `commercialRightsConfirmed`, `redistributionRightsConfirmed`, `evidence` |
| Conteúdo | `animations[]` com `action`, `sourceClipTitle`, `sourceFilePath`, `blenderActionName`, `confirmedByUser` |
| Restrições | `restrictions[]` |
| Autorização | `authorizationForTest.grantedBy/grantedAt/scope` |
| Contrato de saída | `rendererContract.*` (grid, frames, arquivos) |
| Atividade do agente | `agentActivity.assetsDownloaded/credentialsUsed/toolsOrAddonsInstalled/blenderExecuted` |
| Revisão de termos | `termsReview.status/reviewedAt/currentOfficialTermsVerified` |

Duas regras do documento de origem merecem virar norma, porque são raras:

1. **"Registrar fatos, não conceder licença."** O manifesto nunca autoriza; ele descreve.
2. **`"not supplied by source"`** em vez de inventar versão/autoria ausente.

O que **não** existe: (a) separação explícita obrigatório/opcional; (b) suporte a asset
**gerado por IA**; (c) cadeia de transformação entre assets; (d) índice consultável.

## 3. Estrutura proposta

```text
assets/
├── <asset-id>/
│   ├── asset.provenance.json     # schemaVersion 3 (base = v2 do Forge + extensões)
│   └── files/                    # opcional; o asset pode viver fora do repo
└── provenance-index.json         # índice: sha256 → asset-id + licença + status
```

O manifesto continua por asset (como no Forge). O **índice** é o que torna o registro
executável: permite responder "de onde veio este arquivo?" por hash, sem abrir cada JSON.

## 4. Campos — obrigatório × opcional

### 4.1 Obrigatórios (sem eles, o asset não entra em produto)

| Campo | Tipo | Regra |
|---|---|---|
| `schemaVersion` | int | `3` |
| `id` | string | kebab-case, único no índice |
| `origin.kind` | enum | `authored` \| `downloaded` \| `purchased` \| `generated` |
| `origin.author` | string | `"not supplied by source"` é valor válido e **visível** |
| `origin.derivedFrom` | string\|null | id de outro asset, ou `null` |
| `license.spdx` | string\|null | `null` só com `license.reason` preenchido |
| `license.reason` | string | por que não há SPDX (sem licença, licença própria, pendente) |
| `license.redistribution` | enum | `allowed` \| `not_allowed` \| `unknown` |
| `license.evidence` | string | URL exata revisada **ou** declaração datada |
| `files[]` | lista | cada item: `path`, `role`, `sizeBytes`, `sha256` |
| `status` | enum | `draft` \| `reviewed` \| `approved_for_internal` \| `approved_for_distribution` \| `blocked` |
| `recordedAt` | date | data do registro |
| `recordedBy` | string | pessoa ou agente + identificação |

### 4.2 Obrigatórios **quando** `origin.kind = generated`

| Campo | Por quê |
|---|---|
| `generation.tool` + `generation.toolVersion` | resultado não é reproduzível sem a ferramenta |
| `generation.model` + `generation.modelVersion` | capacidade e licença dependem do modelo |
| `generation.promptSha256` | prova do que foi pedido, sem versionar o prompt inteiro |
| `generation.seed` | reprodutibilidade (quando o modelo aceita) |
| `generation.modelLicense.spdx` | licença do **modelo** é independente da do asset |
| `generation.commercialUseAllowed` | muitos modelos proíbem uso comercial |

### 4.3 Opcionais

| Campo | Uso |
|---|---|
| `authorship.modifications` | lista de alterações sobre a origem |
| `restrictions[]` | limites textuais herdados (ex.: "não redistribuir textura de terceiro") |
| `authorization` | quem autorizou uso, quando, com que escopo |
| `animations[]`, `rendererContract`, `termsReview` | preservados do v2 (específicos do Forge) |
| `contentChecks` | resultado de validação de conteúdo (alpha por célula etc.) |
| `notes` | observação humana |

### 4.4 Proibidos

Nunca no manifesto: credencial, token, caminho absoluto do usuário (`C:\Users\...`),
prompt integral com dado pessoal, e qualquer campo que **conceda** licença.

## 5. Cadeia de transformação

O problema real não é o asset inicial: é o quinto derivado.

```json
{
  "id": "sprite-sheet-hero-v3",
  "origin": { "kind": "derived", "derivedFrom": "sprite-sheet-hero-v2" },
  "transform": {
    "tool": "spriteforge",
    "toolVersion": "0.9.2",
    "params": { "grid": [8, 3], "frame": [48, 48], "padding": 0 },
    "paramsSha256": "…",
    "inputHashes": ["…", "…"]
  },
  "files": [
    { "path": "sheet.png", "role": "output", "sizeBytes": 18422, "sha256": "…" }
  ]
}
```

Regras:

1. `transform.inputHashes[]` deve coincidir com `files[].sha256` dos pais, senão o
   registro está quebrado.
2. `paramsSha256` cobre os parâmetros que mudam o resultado — permite refazer o pipeline
   sem guardar o binário.
3. Licença **herda** do pai, salvo `license.reason` explícito dizendo por que não.
   Herança silenciosa é o mecanismo pelo qual material GPL "aparece" em asset próprio.
4. Asset sem `derivedFrom` e sem `origin.kind` coerente é `blocked`, não `unknown`.

## 6. Validação (o que torna "executável")

| # | Checagem | Falha |
|---|---|---|
| P1 | JSON válido contra schema | manifesto quebrado |
| P2 | todo `files[].sha256` corresponde ao arquivo real (ou ao índice) | proveniência falsa |
| P3 | `license.spdx` nulo **exige** `license.reason` | ausência invisível |
| P4 | `redistribution: allowed` exige `evidence` não vazia | permissão inventada |
| P5 | `origin.kind = generated` exige bloco `generation` completo | IA sem rastro |
| P6 | `derivedFrom` resolve e os hashes de entrada batem | cadeia quebrada |
| P7 | `status: approved_for_distribution` exige `NOTICE` quando `license.noticeRequired` | distribuição ilegal |
| P8 | nenhum campo proibido (segredo, caminho absoluto) | vazamento |

P1–P8 são estáticas. **Nenhuma delas prova que o asset é bom** — provam que o registro
não mente sobre a origem, que é coisa diferente e mais modesta.

## 7. Integração com os projetos (sem acoplamento)

| Projeto | Papel | Lê | Escreve |
|---|---|---|---|
| **Forge** | produz o asset e o manifesto (base v2 já existe) | esquema | seu `assets/<id>/` |
| **Studio** | edita/renderiza | esquema para exibir aviso de licença | manifesto do asset editado |
| **Agent Hub** | cataloga | índice (`provenance-index.json`) | nada do asset |
| **Lia-Research** | consolida a política | — | este documento |

O índice é copiável; nenhum projeto importa código do outro.

## 8. Por que obrigatório ≠ documentado

Três exemplos reais do ecossistema mostram o custo de metadado opcional:

| Caso | O que faltou | Consequência |
|---|---|---|
| `web-design-guidelines` (`LR-LIC-003`) | licença no payload | material de terceiro sem base de redistribuição |
| ZIP de 9,9 MB no Studio (`DR-0004`) | hash + origem por arquivo | impossível provar o que está lá |
| 12 Skills MIT do Studio (`LR-LIC-001`) | NOTICE no payload | obrigação legal não viaja com o export |

Metadado opcional é metadado que ninguém preenche. O que protege é o campo obrigatório
com falha automática.

## 9. Limitações e pendências

| Item | Rótulo |
|---|---|
| Nenhum asset real foi registrado com este esquema | `NOT RUN` |
| Nenhum render executado; nenhum asset de terceiro baixado | `BLOCKED` (política) |
| Padrão de credenciais de conteúdo (C2PA / Content Credentials) não pesquisado | `UNVERIFIED` — possível campo futuro |
| `paramsSha256`: normalização de JSON não definida (ordem de chaves, floats) | pendência técnica |
| Validação de conteúdo (alpha por célula) segue proposta do Forge, não implementada | `NOT RUN` |
| Herança de licença em pipelines multi-ferramenta não testada | `UNVERIFIED` |

## 10. Encaminhamento

| Ação | Dono | Gate |
|---|---|---|
| Adotar `schemaVersion: 3` (ou justificar manter 2 + extensão) | Forge | `DR-0021` (proposto) |
| Publicar `provenance-index.json` com 0 assets | Forge | nenhum (é vazio por definição) |
| Exigir P3/P4 no primeiro asset real | Forge | primeiro asset |
| Pesquisar C2PA antes de inventar campo proprietário | Research | `RESEARCH-ROADMAP.md` L-5 |
