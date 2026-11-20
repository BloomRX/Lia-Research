# ArtCraft (storytold) — 17 apps criativos em Rust e uma suíte inteira feita para agentes

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-004` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | studio (com leitura transversal em forge, agent, model, security) |
| Projetos beneficiados | Lia Studio (primário), Lia Forge, Lia Agent Hub, Lia Model Lab, Lia-Project |
| Fontes | `storytold/photocraft@a858d42a5028287662e28e89be0bbce9d0bec6b5`, `storytold/craft-libs@2466fd7ad8371a3551946a0795dbae11e0c3f805`, `storytold/artcraft@a6d52df45e553a6119116e560403155b0c65dc60`, `storytold/craft-ai-integrations@d94a3593adcff504eaaad9e5aee4c84fd2f07a72`: READMEs, `book/src/{architecture/command-engine,automation/mcp}.md`, `docs/ai-shared-layer.md`, árvores recursivas, API do GitHub; site `getartcraft.com/apps` (2026-11-17) |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `storytold/photocraft` · HEAD `359051359fee` · mudou desde a análise (conteúdo novo não lido) |
| Próxima revisão | 2027-02-17 |
| Recomendação | **ADAPT** — o desenho arquitetural, não o código |
| Licença | **MIT OR Apache-2.0** (dual) em todos os repos verificados `CONFIRMED` |
| Confiança | **Alta** para arquitetura e segurança (docs e código lidos); **baixa** para qualidade de execução (nenhum app executado; tudo alpha) |

---

## 1. Identificação

| Item | Valor |
|---|---|
| Organização | `storytold` (ArtCraft) — 82 repositórios públicos, criada 2021-01-03 |
| Site | https://getartcraft.com / https://getartcraft.com/apps |
| Proposta | "17 apps criativos de código aberto, em Rust puro, nativos" |
| Flagship | `photocraft` — ★ **80.269** · 14.169 forks · 5.655 issues abertas · 203 MB · 3.448 arquivos |
| Framework compartilhado | `craft-libs` — **186 crates** num workspace Cargo |
| Camada de IA | `craft-ai-integrations` ("first draft", ★173) |
| Distribuição | `craft-launcher` (★5.475, v0.19.2) + instaladores por app |
| Engine de IA | `artcraft` — "IDE for interactive AI image and video creation", ★41.512, 1,3 GB, criado 2022-03-31 |
| Stack | Rust (edition 2024, resolver 3, Rust ≥1.95), **egui 0.36**, wgpu (Metal/Vulkan/DX12/WebGPU) |
| Plataformas | macOS · Windows · Linux · FreeBSD · **WebAssembly no navegador** (16 dos 17 apps) |
| Status declarado | 2 apps "early alpha", 14 "in development", 1 "early alpha" — **nenhuma estável** |
| Licença | MIT **ou** Apache-2.0 (arquivos `LICENSE-MIT` + `LICENSE-APACHE` + `NOTICE`) |

**Observação de método:** a API classifica os repos como `Apache-2.0` (o GitHub escolhe uma
das duas); os arquivos provam a dupla. Mesmo tipo de subdeclaração encontrado em
`LR-SEC-006` — metadado de licença **não** é fonte de verdade.

## 2. Resumo executivo

Não é "mais um Figma open source". É um **conjunto de 17 aplicativos de desktop** —
edição de imagem, vetor, vídeo, foto/RAW, PDF, motion graphics, animação 2D, diagramação,
design de interface, textura 3D, materiais procedurais, áudio, texto, apresentações, CAD,
planilhas — construídos sobre uma biblioteca compartilhada de **186 crates** e uma
arquitetura que trata *agente* como **cidadão de primeira classe**, não como plugin.

Três achados valem mais que o resto:

1. **Um único barramento de comandos serve quatro entradas.** Toda ação editável é um
   comando registrado; a UI, o CLI, o protocolo JSON de controle e o servidor MCP despacham
   no **mesmo** registro (`book/src/architecture/command-engine.md`). É a resposta pronta
   para "como um app da Lia pode ser operável por agente sem duplicar código".
2. **Autoridade de agente é escopo por lançamento, não por schema.** O MCP declara
   *read root* e *write root* na inicialização, autentica o canal loopback com **token em
   arquivo privado**, fica **desligado por padrão** (switch no launcher, com consentimento),
   e a documentação diz explicitamente: "**tool schemas improve correctness but are not
   authorization boundaries**". É a formulação mais honesta do problema que a Lia registrou
   em `LR-SEC-005`.
3. **Contrato de IA único e tipado, com proibição de fallback silencioso.**
   `craft-ai-core` define `Role` → `CapabilityId` → `InputRole[]`, valida compatibilidade
   antes de gravar o vínculo, e exige que o app **falhe explicitamente** quando o adaptador
   não existe — "must fail explicitly when the selected adapter is absent, **not silently
   substitute another engine**". Isso ataca a mesma lacuna de `LR-MODEL-005` (só 5 de 10
   providers declaram raciocínio; `embed` = 0) por desenho, não por tabela.

Também há um **custo de credibilidade**: tudo nasceu entre 2026-09-30 e 2026-10-11, está em
alpha, acumula 5.655 + 807 + 802 issues abertas, e a proposta inclui "reimplementação
clean-room do Photoshop/Figma/Excel" com "atalhos que você já conhece" — o que é competência
técnica impressionante e exposição jurídica de trade dress ao mesmo tempo.

## 3. O que resolve

| Problema real de quem constrói app criativo | Como o ArtCraft resolve |
|---|---|
| Cada entrada (UI, CLI, automação, agente) reimplementa a mesma ação | um registro de comandos; quatro chamadores |
| Deixar agente controlar o app = dar shell disfarçado | roots de leitura/escrita por lançamento + token + loopback + consentimento |
| Formatos de arquivo proprietários como portão | 186 crates de leitura/escrita bounded (PSD, AI/AEP, Affinity, Figma, Sketch, XCF, KRA, DWG, DXF, OOXML, ICC…) |
| Reimplementar suíte = 17 bases de código divergentes | libs compartilhadas versionadas por tag + app como repositório próprio |
| "Funciona no meu app" sem verificação de contrato | `Role`/`Capability`/`InputRole` validados antes do vínculo; conformance tests |
| Instalar 17 apps separadas | launcher único que instala e atualiza, com Flatpak/deb/rpm/MSI |

## 4. Arquitetura

```text
suite (17 repos de app + repos de lib)
  app (ex.: photocraft)
    crates/engine          registro de comandos + Session + history
    crates/ui-egui         shell desktop
    crates/automation      CLI · control protocol (JSON-RPC) · servidor MCP (stdio)
    book/                  documentação de arquitetura e de automação

  craft-libs (workspace, 186 crates)
    formatos     psd aep aaf affinity fig sketch xcf kra ora dwg dxf idml indd offcrypto
                 ooxml opc docx pptx xlsx odf epub pdf cfb pcap elf macho dex evm …
    mídia        image-codecs raster-codecs stream-codecs hdr heif jxl exr tiff webp
    IA           ai-core (modelo) · ai · cloud · cloud-local
    agente       ipc · control-protocol · jsonrpc · mcp · mcp-server
    plataforma   platform dialogs window menu settings atomic quit i18n keymap
    cor/tipos    cms (ICC) color font-manager font-store text
  craft-launcher   instalador/atualizador + switch de consentimento de agente
  craft-ai-integrations  provedores, chaves, client, widgets egui (primeiro rascunho)
  artcraft         engine de composição e geração (2D/3D, imagem→malha, pose)
```

**Regra de promoção declarada:** "se alguma biblioteca crescer além do uso da suíte, pode
ser promovida para repositório próprio" — mesma disciplina que a Lia precisa para Skills
e assets (`LR-LIC-002`), aplicada a código.

## 5. Funcionalidades (as 17 apps)

| # | App | Função | Status |
|---|---|---|---|
| 1 | PhotoCraft | edição de imagem, PSD real (307/309 arquivos de teste preservados) | early alpha |
| 2 | VectorCraft | ilustração vetorial | in development |
| 3 | FilmCraft | edição de vídeo não-linear, escopos | in development |
| 4 | LightCraft | biblioteca de fotos + revelação RAW | in development |
| 5 | PdfCraft | PDF: ler, organizar, combinar, dividir, proteger | early alpha |
| 6 | EffectCraft | motion graphics e VFX | in development |
| 7 | AniCraft | animação vetorial 2D | early alpha |
| 8 | DesignCraft | diagramação e publicação | in development |
| 9 | FigCraft | design de interface e prototipagem | early alpha |
| 10 | TextureCraft | pintura de textura 3D | in development |
| 11 | MaterialCraft | materiais procedurais por nós | in development |
| 12 | SoundCraft | DAW | in development |
| 13 | WordCraft | processamento de texto | in development |
| 14 | DeckCraft | apresentações | in development |
| 15 | CADCraft | CAD e desenho técnico | in development |
| 16 | GridCraft | planilhas e análise | in development |
| 17 | Craft Anything | "entender como um software funciona e construir o seu" | early alpha |

## 6. Dependências

| Dependência | Papel | Rótulo |
|---|---|---|
| Rust ≥ 1.95, edition 2024, resolver 3 | compilador da suíte | `CONFIRMED` |
| `egui` 0.36 (fork próprio da org) | UI imediata | `CONFIRMED` |
| `wgpu` (fork próprio), `winit` (fork próprio) | GPU e janelas; backends Metal/Vulkan/DX12/WebGPU | `CONFIRMED` |
| `craft-libs` por tag Git (`v0.1.0`) | base compartilhada | `CONFIRMED` |
| SonarCloud + CodeRabbit | análise estática e revisão de PR | `CONFIRMED` (badges + workflow) |
| Flatpak / MSI / deb / rpm / zip macOS | distribuição | `CONFIRMED` |
| Provedores de IA externos | geração de imagem/vídeo, via chaves do usuário | `REPORTED` |

Sem Electron, sem web view, sem Node — decisão declarada, não acidente.

## 7. Requisitos de hardware e sistema

GPU real por trás de wgpu (Metal no macOS, Vulkan/DX12 no Windows, WebGPU no navegador) —
é o oposto do perfil de uma stack Electron, e é o ponto onde a stack da Lia (Windows 11 +
RX 580) encontra terreno: Vulkan/DX12 existem na placa, mas o backend precisa ser testado
**no** alvo, não presumido. Tamanho de repo é proibitivo para cópia cega (photocraft 203 MB,
vectorcraft 540 MB, artcraft 1,3 GB).

## 8. Segurança e privacidade

A seção mais útil do objeto inteiro. Modelo de autoridade do agente, em cinco camadas:

| Camada | Mecanismo | Evidência |
|---|---|---|
| Consentimento | switch "AI agents" no launcher, **desligado por padrão**; uma chave cobre todos os apps | `book/src/automation/mcp.md` `CONFIRMED` |
| Escopo de arquivo | `--automation-read-root` / `--automation-write-root` no lançamento; **omitir um root omite a autoridade** | idem `CONFIRMED` |
| Transporte | stdio (sem listener) **ou** bridge loopback com **bearer token** em arquivo privado, user-only no Unix, apagável para rotacionar | idem `CONFIRMED` |
| Fronteira declarada | "Tool schemas improve correctness but **are not authorization boundaries**" | idem `CONFIRMED` |
| Lacuna admitida | transportes atuais **não** têm capability por comando: quem alcança o dispatch pede qualquer comando cujo predicado `enabled` permita | `command-engine.md` §Security boundary note `CONFIRMED` |

Outros controles relevantes:

- **Parâmetros são não confiáveis na fronteira do comando**; valores derivados não podem
  chegar a índice não checado, divisão, dimensionamento de alocação ou pânico; há teste
  adversarial ignorado por padrão (`panic_hunt`) e exigência de testes de falha graciosa.
- **Caminhos guardados em documento** obedecem a `craft-docpath`: só abre caminho local ou
  no próprio compartilhamento de rede do documento; **recusa** caminho de rede externo,
  device path e URL não-`file`. Regra diretamente aplicável ao IPC da Lia.
- Leitores de formato hostil (**PE/COFF**, CFB, PDF) declarados "bounded on hostile input",
  com `craft-assuan` limitando "tudo que o agente envia".
- Segredos vivem em *secret store*, "nunca no JSON compartilhado nem na declaração de tool".
- `AGENTS.md` no repo define regras para agentes que editam o próprio código.

**Não verificado:** se essas garantias sobrevivem a um alvo real — nenhum app foi executado
aqui. Rótulo `UNVERIFIED` para eficácia; `CONFIRMED` para existência e texto das garantias.

## 9. Licença e proveniência

| Item | Situação |
|---|---|
| Licença | **MIT OR Apache-2.0** (escolha do consumidor) — `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE` |
| Metadado GitHub | `Apache-2.0` (classificação do GitHub, não a realidade) |
| Royalty de patente | Apache-2.0 traz concessão explícita de patente — melhor para a Lia que MIT puro |
| Obra derivada? | "clean-room reimplementation" declarada em vários apps; nomes e atalhos de concorrentes citados explicitamente |
| Conteúdo de mídia | screenshots usam obras em domínio público (Hokusai, Monet, Earthrise/NASA) com crédito no `alt` e na legenda |
| Compatibilidade com a Lia | alta para **ideias**; nula para **código** (Rust ≠ Electron/Vue) |

**Risco não coberto pela licença:** reimplementar produto alheio mantendo "os mesmos menus,
atalhos e painéis" toca trade dress e marca — Apache-2.0 não protege disso. Vale como aviso
para qualquer "clone familiar" que a Lia venha a fazer: licença permissiva ≠ liberdade
jurídica plena.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | 7–8 semanas (criados 2026-09-30 … 2026-10-11) | novíssimo |
| Estrelas | 80.269 (photocraft) · 41.512 (artcraft) · 5.475 (launcher) | adoção excepcional, atípica |
| Issues abertas | 5.655 · 807 · 802 | backlog enorme |
| Releases | `photocraft` v0.23.1 (2026-11-12) · launcher v0.19.2 | cadência altíssima |
| Versionamento | `craft-libs` tag `v0.1.0` **imutável**, política escrita: resolver tag → `rev`, `cargo build --locked` | disciplina acima da média |
| Qualidade | SonarCloud + CodeRabbit + `book/` de arquitetura + testes de protocolo MCP | sério |
| Contribuidores | 100+ em photocraft e craft-libs (paginado) | comunidade real |
| Estabilidade | **nenhuma app estável**; 2 early alpha, 14 em desenvolvimento | não é dependência |

**Leitura honesta:** maturidade de *processo* alta, maturidade de *produto* baixa. A
velocidade (5 apps alpha em 7 semanas, 186 crates) é compatível com desenvolvimento
fortemente assistido por IA — o que não invalida o desenho, mas impede tratá-lo como base
confiável para produção.

## 11. Custos e limitações

| Item | Custo/limite |
|---|---|
| Adotar como dependência | inviável: Rust/egui vs Electron/Vue; 17 apps alpha |
| Portar o barramento de comandos | barato conceitualmente, exige mapear cada ação da Lia em comando com ID, predicado e histórico |
| Escopo por root | exige que o app da Lia pense em termos de raiz de arquivo, não de IPC aberto |
| IA embutida | depende de chaves do usuário e de provedores externos; `craft-ai-integrations` é "first draft" |
| Manutenção | acompanhar 186 crates é trabalho de equipe, não de projeto solo |
| Legal | "familiar layouts" de produtos Adobe/Figma = risco de trade dress |

## 12. Compatibilidade com o ecossistema Lia

| Dimensão | Situação |
|---|---|
| Windows 11 | **sim** (MSI, CLI com caminho padrão documentado) `CONFIRMED` |
| RX 580 / GPU | Vulkan/DX12 disponíveis; não testado neste hardware `UNVERIFIED` |
| Electron/Vue | nenhuma relação direta — é o **contraste** arquitetural mais instrutivo |
| Formato de Skill | irrelevante (não usa Skills) |
| Agente | **altamente compatível**: MCP stdio, `claude mcp add`, roots explícitos |
| Licença | MIT/Apache-2.0 — sem trava para a Lia |
| Distribuição | launcher + instaladores por app — modelo replicável no Hub |

## 13. Projetos beneficiados

| Projeto | O que levar |
|---|---|
| **Lia Studio** | barramento único de comandos (UI/CLI/IPC/MCP); histórico por comando; editor com "toda ação é comando" |
| **Lia Forge** | `artcraft` como referência de composição/geração (2D/3D, imagem→malha, pose, identidade); crates de formato para importar/exportar assets |
| **Lia Agent Hub** | superfície de agente por app: roots + token + consentimento + MCP stdio; `craft-libs` como prova de que libs compartilhadas escalam |
| **Lia Model Lab** | `craft-ai-core`: contrato `Role`/`Capability`/`InputRole`, consentimento, jobs, proibição de fallback silencioso |
| **Lia-Project** | `craft-docpath` (confiança em caminho vindo de documento) e leitores bounded para entrada hostil |
| **Lia-Research** | `book/` (mdBook) como documentação de arquitetura versionada; política de tag imutável |

## 14. Oportunidades de reutilização

| # | Mecanismo | O que adaptar na Lia | Esforço |
|---|---|---|---|
| A1 | **Registro único de comandos** | toda ação do Studio/Forge vira comando com `id`, `label`, `enabled`, params + histórico; UI, IPC, CLI e MCP chamam o mesmo despacho | médio |
| A2 | **Autoridade por lançamento** | `read_root`/`write_root` explícitos na sessão de agente; omitir = negar; token em arquivo privado; loopback apenas | baixo |
| A3 | **Consentimento no nível da suíte** | um switch por instalação, off por padrão, cobrindo todos os apps | baixo |
| A4 | **Contrato de IA tipado** | `Capability`/`InputRole` validados antes de rotear; **falhar explícito** em vez de trocar de motor | médio |
| A5 | **Regra de caminho de documento** | caminho vindo de arquivo só abre se local ou no próprio share; recusa device path e URL não-`file` | baixo |
| A6 | **Tag imutável + `rev` + `--locked`** | releases de Skill/asset pinadas por hash, com política de nunca mover tag | baixo |
| A7 | **Book de arquitetura** | documentação navegável por app, não README gigante | baixo |
| A8 | **Formato como crate bounded** | todo parser da Lia assume entrada hostil, com teste adversarial no CI | médio |

## 15. Riscos e incompatibilidades

| Risco | Severidade | Nota |
|---|---|---|
| Tratar alpha de 7 semanas como dependência estável | **alta** | 5.655 issues; nenhum app estável |
| Copiar Rust para stack Electron/Vue | alta | incompatível por construção |
| "Familiaridade" com produtos Adobe/Figma | média | trade dress/marca; licença não cobre |
| 186 crates para manter | média | só faz sentido com equipe |
| IA embutida depende de terceiros e chaves | média | `craft-ai-integrations` é rascunho |
| Backlog de issues como sinal de fragilidade | média | pode ser também sinal de uso real intenso |
| Assumir que a fronteira de segurança implementada é a documentada | média | o próprio repo admite ausência de capability por comando |

## 16. Evidências e fontes

| # | Evidência | Rótulo | Fonte |
|---|---|---|---|
| E1 | 17 apps, 2 early alpha, 14 in development | CONFIRMED | `getartcraft.com/apps` + READMEs |
| E2 | 186 crates em `craft-libs`, workspace edition 2024 | CONFIRMED | Trees API + README |
| E3 | Um registro de comandos serve UI/CLI/controle/MCP | CONFIRMED | `book/src/architecture/command-engine.md` |
| E4 | MCP stdio/bridge, roots, bearer token, off-by-default, "schemas não são autorização" | CONFIRMED | `book/src/automation/mcp.md` |
| E5 | Lacuna admitida: sem capability por comando | CONFIRMED | `command-engine.md` §Security boundary |
| E6 | Contrato `Role`/`Capability`/`InputRole`, consentimento, jobs, sem fallback silencioso, segredos fora do JSON | CONFIRMED | `craft-libs/docs/ai-shared-layer.md` |
| E7 | `craft-docpath` recusa rede externa, device path e URL não-`file` | CONFIRMED | `craft-libs/crates/docpath` |
| E8 | Dual MIT OR Apache-2.0; GitHub diz só Apache | CONFIRMED | `LICENSE-MIT`/`LICENSE-APACHE` + API |
| E9 | 80.269★ / 5.655 issues / 203 MB / criado 2026-09-30 | CONFIRMED | API GitHub |
| E10 | Tag `v0.1.0` imutável, pin por `rev`, `--locked` | CONFIRMED | `craft-libs/README.md` |
| E11 | Qualidade de execução dos 17 apps | **UNVERIFIED** | nenhum app executado |
| E12 | Eficácia das garantias de segurança em alvo real | **UNVERIFIED** | não testado |
| E13 | Conformidade de trade dress | **BLOCKED** | fora do escopo desta base |
| Vizinhos | Graphite ★27.981 Apache-2.0 Rust · Penpot ★62.523 MPL-2.0 Clojure · ComfyUI ★147.500 **GPL-3.0** Python | CONFIRMED | API GitHub (2026-11-17) |

## 17. Recomendação

**Recomendação (opinião técnica, não é aprovação): `ADAPT`** — arquitetura, não código.

O ArtCraft é a melhor referência já encontrada por esta base para **um app criativo que é
operável por agente sem virar shell** — e o único objeto que já resolveu, com documentação
e admissão de lacuna, aquilo que a Lia tem só como intenção em `LR-SEC-005`,
`LR-MCP-002`, `LR-MODEL-005` e `LR-UI-005`.

Adaptar, nesta ordem:

1. **A1 + A2 + A3** no Studio/Forge: comando único, roots por sessão, consentimento global.
2. **A4** no Model Lab/Hub: contrato tipado com falha explícita.
3. **A5** no Lia-Project: caminho de documento é entrada não confiável.
4. **A6 + A7** como prática de base: tag imutável e book de arquitetura.

**Não** portar Rust, **não** tratar como dependência, **não** reproduzir "familiaridade"
com produto alheio. A lição mais valiosa é de postura: o repo documenta a própria lacuna de
segurança na mesma página em que descreve a defesa. É o padrão que esta base exige de si.

## 18. Próximos passos

| # | Ação | Dono | Gate |
|---|---|---|---|
| 1 | Escrever ADR de "comando único" para Studio/Forge (A1) | Lia Studio | `DR-0023` |
| 2 | Propor raiz de leitura/escrita por sessão de agente (A2/A3) | Lia Agent Hub | `DR-0019` |
| 3 | Cruzar `craft-ai-core` com `LR-MODEL-005` e propor contrato de capability (A4) | Lia Model Lab | `DR-0020` |
| 4 | Adotar a regra de caminho de documento (A5) no IPC | Lia-Project | `LR-SEC-005` |
| 5 | Piloto do book + tag imutável (A6/A7) | Lia-Research | nenhum |
| 6 | Revisar em 2027-02-17 — objetos de 7 semanas envelhecem rápido | Lia-Research | — |
