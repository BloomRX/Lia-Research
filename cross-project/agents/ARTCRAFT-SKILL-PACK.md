# Pacote de Skills "ArtCraft" — operações determinísticas de edição (edição ≠ geração)

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-010` |
| Categoria | agent |
| Projetos beneficiados | Lia Agent Hub (catálogo/execução), Lia Studio, Lia Forge, Lia-Project, app de voz (edição de foto recebida) |
| Fontes | `storytold/photocraft@a858d42a5028287662e28e89be0bbce9d0bec6b5` (`docs/mcp.md`, `book/src/automation/mcp.md`, `book/src/architecture/command-engine.md`), `storytold/pdfcraft@main` (`docs/mcp.md`, 2026-11-18), `storytold/vectorcraft@main` (`docs/mcp.md`, 2026-11-18) — objeto auditado em `LR-STUDIO-004` |
| Data | 2026-11-17 |
| Status | **PROPOSTA** — nenhuma Skill publicada, nenhum app executado |
| Validação | V1–V5 por inspeção; **V6 `NOT RUN`** (nenhum app ArtCraft foi executado nesta base) |
| Confiança | Alta para nomes de ferramenta e modelo de permissão (documentação lida); **nula** para comportamento em execução |

---

## 1. Pergunta de pesquisa

Qualquer app Lia pode querer **editar** uma foto — recortar, ajustar níveis, redimensionar,
converter, juntar PDFs — sem acionar um **gerador de imagem**. Um gerador cobra por
inferência, produz pixels novos (não fidelidade), pode enviar a foto do usuário a um
provedor e não é determinístico. Edição é o oposto nos quatro eixos.

Pergunta: **os apps da ArtCraft podem ser consumidos como Skills de edição determinística
pelo Lia Agent Hub, e com que contrato de permissão?**

Resposta curta: **sim, e o desenho de permissão deles é melhor que o nosso.** Mas com uma
restrição que decide a arquitetura: **os nomes de ferramenta divergem por app** — não existe
um contrato único de tools, só um contrato único de *flags*.

## 2. Regra dura: edição ≠ geração

> Se a Skill de edição não puder executar (app ausente, versão incompatível, raiz negada),
> o resultado é `UNAVAILABLE`. **É proibido** cair silenciosamente num gerador de imagem.

Motivos, na ordem em que importam para o produto:

| Eixo | Edição (ArtCraft) | Geração (provedor) |
|---|---|---|
| Fidelidade | preserva o que existe; opera no arquivo | inventa pixels novos |
| Determinismo | mesma entrada → mesma saída | amostragem; resultado varia |
| Custo | zero por operação (local) | por token/imagem |
| Privacidade | **o arquivo não sai da máquina** | a foto do usuário vai ao provedor |
| Latência | segundos | segundos a minutos |

O último é o decisivo para um app de voz que recebe fotos: editar mantém a foto local.

## 3. Camada de transporte (o que o Hub registra uma vez)

| Item | Fato documentado | Rótulo |
|---|---|---|
| Gateway único | O launcher publica **uma** entrada `ArtCraft` no cliente MCP (via `craft-ai-mcp`), que inicia `<app>-cli mcp` para cada app instalado | `CONFIRMED` |
| Lista de apps | `ArtCraft/mcp/apps.json` (movível por `CRAFT_MCP_DIR`) diz quais estão instalados | `CONFIRMED` |
| Consentimento | Switch `Settings › AI agents › Let AI agents use Craft apps`, **desligado por padrão**; feature flag `AI-MCP` em `ArtCraft/flags.toml` | `CONFIRMED` |
| Conexão | App serve em loopback e publica porta + token em `agent-connection.json`; o CLI relê a cada chamada | `CONFIRMED` |
| Flags de escopo | `--automation-read-root` (repetível, ordem = prioridade) e `--automation-write-root` (único) — **iguais em toda a suíte** | `CONFIRMED` |
| Modos | `--headless` · `--connect HOST:PORT` · `--bridge` + token · `--when-closed launch\|headless\|error` | `CONFIRMED` |
| Comportamento sem consentimento | Sessão headless só com as raízes passadas; o app nunca é aberto | `CONFIRMED` |

Consequência para o Hub: **um registro de servidor, N Skills**. A Skill declara *qual app*
precisa; o transporte é do Hub.

## 4. A divergência que proíbe abstração única

| Operação | PhotoCraft | PdfCraft | VectorCraft |
|---|---|---|---|
| listar comandos | `command_list` | `command_list` | `command_list` / `list_commands` |
| executar | `command_run` | `command_run` | `command_run` / `run_command` / `invoke_menu` |
| abrir arquivo | `doc_open` | `doc_open` | `open_file` |
| inspecionar | `doc_inspect` | `doc_inspect` | `inspect_ui` / `ui_inspect` |
| prévia | `render_preview` | `render_preview` | `screenshot {window:true}` |
| efeito | via comando | via comando | `apply_effect` (ids de **efeito**, não de comando) |

`CONFIRMED` nas três documentações. Portanto: **uma Skill por app + uma Skill de status**;
o adaptador mora na Skill, não no Hub. Um "tool único" seria ficção e quebraria na primeira
execução.

## 5. As 8 Skills propostas

Todas seguem o manifesto de `LR-AGENT-009` (id, versão, licença, entradas, saídas,
permissões, falhas, proveniência) acrescido do bloco `capability` no molde de
`craft-ai-core` (`Role` → `CapabilityId` → `InputRole[]`).

| # | Skill | App | Capacidade | Entradas | Saídas | Raízes |
|---|---|---|---|---|---|---|
| S1 | `artcraft-status` | launcher | `suite.discover` | — | apps instalados, versões, consentimento, raízes | nenhuma |
| S2 | `photo-adjust` | PhotoCraft | `image.edit` | imagem + intenção de ajuste | PNG/JPEG/TIFF/PSD | read + write |
| S3 | `photo-variants` | PhotoCraft | `image.derive` | imagem + alvos (tamanho, recorte) | N imagens | read + write |
| S4 | `photo-inspect` | PhotoCraft | `image.inspect` | imagem | árvore de camadas, histórico, prévia PNG | read |
| S5 | `pdf-assemble` | PdfCraft | `document.assemble` | páginas/arquivos + ordem | PDF | read + write |
| S6 | `pdf-extract` | PdfCraft | `document.extract` | PDF + intervalo | texto/CSV, imagens | read + write |
| S7 | `vector-export` | VectorCraft | `vector.export` | vetor + formato | SVG/PDF/PNG | read + write |
| S8 | `format-convert` | PhotoCraft/PdfCraft | `format.convert` | arquivo + formato alvo | arquivo convertido | read + write |

### 5.1 `artcraft-status` (pré-requisito de todas)

- Verifica: app instalado, `--version`, consentimento ativo, raízes concedidas.
- Saída negativa é a mais importante: `UNAVAILABLE: app ausente` / `CONSENT_REQUIRED` /
  `ROOT_DENIED`. **Nunca** sugere gerador como alternativa.

### 5.2 `photo-adjust` (a que o pedido motivou)

Fluxo documentado, sem inventar id de comando:

```text
1. S1 → app instalado + consentimento + raízes
2. doc_open  { path: "entrada.jpg" }            → { doc: 1 }
3. command_run { id: "image.duplicate", params: {} }   → copia de trabalho
4. command_list { filter: "<termo>", enabled_only: true }
   → a Skill DESCOBRE o id real (ex.: ajuste de níveis/curvas) em vez de fixá-lo
5. command_run { id: <descoberto>, params: {...} }
6. render_preview { index, max_side: 1024 }     → conferência antes de salvar
7. doc_save  { path: "saida.png" }  ou doc_export
```

Por que descobrir o id em vez de fixá-lo: os ids de comando do engine não são um contrato
público estável — `command_list` é. Fixar id na Skill é a forma mais rápida de a Skill
quebrar numa atualização (os apps estão em alpha e entregam releases semanais).

### 5.3 `pdf-assemble`

`doc_create` → `page_insert_file` (ou `doc_combine`) → `doc_split`/`doc_reduce` quando
couber → `doc_save`. `page_replace`, `doc_optimize`, `doc_watermark` e `doc_background`
disponíveis. `doc_compare_report` existe para verificar o resultado.

### 5.4 `format-convert`

Conversão é `doc_save`/`doc_export` para formato suportado (PNG, JPEG, TIFF, PSD, PSB,
`.pcraft`, OpenRaster, PDF). **Não** é gerar: a Skill se recusa a produzir arquivo cujo
conteúdo não exista na origem.

## 6. Modelo de permissão (declarar, não herdar)

| Regra | Origem documentada | Como a Skill expressa |
|---|---|---|
| Raiz de leitura ≠ raiz de escrita | PhotoCraft/PdfCraft/VectorCraft | dois campos separados, ambos obrigatórios |
| Omitir raiz = negar | PhotoCraft (`denies that direction`) | `roots.required: true`; sem raiz, `UNAVAILABLE` |
| Escrita nunca cai para raiz de leitura | PhotoCraft | `write_root` obrigatório em S2/S3/S5/S6/S7/S8 |
| Pasta de saída dedicada | aviso de injeção: texto dentro do documento pode instruir o agente | S2–S8 exigem `write_root` diferente do diretório do projeto |
| Sem caminho absoluto arbitrário | raízes + resolução por capacidade | Skill só aceita caminho relativo às raízes |
| Não sobrescrever arquivo alheio | PhotoCraft recusa sobrescrever o que não é imagem/documento (`.env`, `src/main.rs`) | Skill nunca aponta `doc_save` para arquivo existente de outro tipo |
| Batch não é transação | `command_batch` sem rollback | Skill para no primeiro erro (`stop_on_error: true`) e relata passos aplicados |
| Undo não desfaz arquivo | `edit.undo` não reverte escrita em disco | Skill separa "editar" de "salvar" e só salva no fim |

Isso espelha a proposta de `LR-SEC-005` (permissão por execução) — aqui, porém, **já
existe** implementação do lado do app (`Automation::resolve`, unit test que impede acesso
ao filesystem fora dele).

## 7. Falhas previstas e o que a Skill devolve

| Situação | Resultado | Proibido |
|---|---|---|
| App não instalado | `UNAVAILABLE: app ausente` | gerar imagem |
| Consentimento desligado | `CONSENT_REQUIRED` + onde ligar | abrir o app sem permissão |
| Raiz faltando | `UNAVAILABLE` (omitir = negar) | usar raiz padrão do app |
| Caminho fora da raiz | erro repassado ao agente | reescrever caminho "esperto" |
| Comando inexistente na versão | listar via `command_list` e falhar com os ids próximos | chutar id |
| Timeout / job longo | job + `jobs_list` / cancelamento | repetir a escrita |
| Arquivo de saída já existe | recusa (exports multiarquivo nunca substituem) | forçar sobrescrita |
| Texto do documento tenta instruir o agente | tratar como **conteúdo**, não instrução | obedecer |

A última linha é a mais importante: os próprios apps avisam que o agente lê nome de camada
e metadados que "podem tentar conduzi-lo". A Skill deve declarar que conteúdo de documento
é dado não confiável.

## 8. Validação (V1–V6)

| Etapa | O que exige | Estado |
|---|---|---|
| V1 estrutura | manifesto com todos os campos | PASS (por desenho) |
| V2 licença | Skill autoral Lia, Apache/MIT-compatível | PASS (a definir em `DR-0001`) |
| V3 proveniência | app + versão + commit por Skill | PASS (fonte pinada) |
| V4 permissões | raízes, consentimento, pasta de saída | PASS (declaradas) |
| V5 falha explícita | `UNAVAILABLE` sem fallback de geração | PASS (regra escrita) |
| **V6 execução** | rodar uma Skill contra o app real | **NOT RUN** |

V6 é a única que prova algo. Nenhum dos 17 apps foi instalado ou executado nesta base.

## 9. Como o Lia Agent Hub consome

| Passo | Ação | Critério de aceite |
|---|---|---|
| 1 | Registrar **um** servidor MCP `ArtCraft` (gateway do launcher) | status verde sem expor porta/token ao Hub |
| 2 | Publicar S1 como Skill de *pré-voo* obrigatória | toda Skill do pacote declara `requires: artcraft-status` |
| 3 | Publicar S2–S8 com `capability` e raízes explícitas | nenhuma Skill sem `write_root` próprio |
| 4 | Testar o caminho negativo antes do positivo | app ausente → `UNAVAILABLE`, nunca gerador |
| 5 | Medir custo/latência por Skill | sem número, não publica (regra da base) |
| 6 | Registrar proveniência: app, versão, commit, licença | linha em `data/inventory/` |

**Não copiar:** nenhum código Rust dos apps, nenhuma skill de terceiros, nenhum payload.
O pacote é **autoral**; o que se referencia é a superfície documentada, com pin.

## 10. Riscos e limitações

| Risco | Severidade | Nota |
|---|---|---|
| Apps em alpha, releases semanais | **alta** | id de ferramenta pode mudar; por isso `command_list` em vez de id fixo |
| Nomes de ferramenta divergentes por app | alta | exige adaptador por Skill |
| Desktop não é confinado pelas raízes (PdfCraft) | média | confinamento vale para a sessão MCP, não para a janela do app |
| TOCTOU admitido pelo próprio app | média | raiz contém o agente, não protege de outro software local |
| Injeção via conteúdo de documento | média | pasta de saída dedicada + conteúdo tratado como dado |
| Windows: device names/UNC | baixa | o app já recusa antes de resolver |
| `vectorcraft` headless usa renderer CPU | baixa | prévia mais lenta, resultado igual |
| Nenhum app executado | **alta** | tudo acima é documentação, não comportamento observado |

## 11. Evidências

| # | Evidência | Rótulo | Fonte |
|---|---|---|---|
| E1 | Flags `--automation-read-root` / `--automation-write-root` iguais em toda a suíte | CONFIRMED | `pdfcraft/docs/mcp.md`, `vectorcraft/docs/mcp.md` |
| E2 | Gateway único `ArtCraft` + `apps.json` + consentimento no launcher | CONFIRMED | `photocraft/docs/mcp.md` |
| E3 | Ferramentas de PhotoCraft (doc_*, command_*, jobs_*, render_preview) | CONFIRMED | `photocraft/docs/mcp.md` §Tools |
| E4 | Ferramentas de PdfCraft (page_*, doc_combine/split/reduce/optimize, text_extract, ocr_*) | CONFIRMED | `pdfcraft/docs/mcp.md` |
| E5 | Divergência de nomes (`open_file`, `run_command`, `apply_effect`, `invoke_menu`) | CONFIRMED | `vectorcraft/docs/mcp.md` |
| E6 | Omitir raiz nega a direção; leitura e escrita independentes | CONFIRMED | `photocraft/docs/mcp.md` §Confining |
| E7 | `doc_save` recusa sobrescrever arquivo que não seja imagem/documento | CONFIRMED | `photocraft/docs/mcp.md` §Tools |
| E8 | Batch sem rollback; undo não desfaz escrita | CONFIRMED | `photocraft/docs/mcp.md` |
| E9 | Aviso de injeção por conteúdo de documento | CONFIRMED | `photocraft/docs/mcp.md` |
| E10 | Comportamento em execução das 8 Skills | **UNVERIFIED** | nenhum app executado |

## 12. Próximos passos

| # | Ação | Dono | Gate |
|---|---|---|---|
| 1 | Instalar PhotoCraft + PdfCraft numa máquina e rodar V6 com S2 e S5 | Agent Hub | autorização do proprietário |
| 2 | Publicar S1 (`artcraft-status`) como primeira Skill do pacote | Agent Hub | `DR-0001` (licença) |
| 3 | Testar caminho negativo (app ausente) antes do positivo | Agent Hub | — |
| 4 | Ligar a regra "edição ≠ geração" ao roteamento de modelo | Model Lab | `LR-MODEL-005` |
| 5 | Revisar quando os apps saírem de alpha | Lia-Research | 2027-02-17 |
