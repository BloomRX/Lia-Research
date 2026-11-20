# Mister Download Manager — gerenciador de downloads em Rust (GPL-3.0)

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-001` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | forge (aquisição de arquivos grandes) |
| Projetos beneficiados | Lia Forge, Lia Agent Hub, Lia Model Lab (eventual) |
| Fontes | `anefzaoui/misterdownloadmanager@d9a9ef0621cb494a39999ab9adf433515a9d36a1:README.md`, `crates/mcp/Cargo.toml`, `docs/browser-integration.md`, tree, `LICENSE` |
| Versão/commit | `d9a9ef0` (2026-11-17), release `v0.5.2` (2026-11-09) |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `anefzaoui/misterdownloadmanager` · HEAD `f648a0c2bc58` · mudou desde a análise (conteúdo novo não lido) |
| Próxima revisão | 2027-02-17 |
| Recomendação | **REFERENCE_ONLY** para o produto; **`ADAPT`** apenas se usado como processo externo via MCP |
| Licença | **GPL-3.0** (`CONFIRMED`) |
| Confiança | Alta para licença, arquitetura, MCP e integração de navegador; Baixa para desempenho |

---

## 1. Identificação

- **Nome:** Mister Download Manager (MDM), binário `misterdownloadmanager-mcp` (MCP)
- **URL:** https://github.com/anefzaoui/misterdownloadmanager · site misterdownloadmanager.com
- **Autor:** `anefzaoui`
- **Licença:** **GNU GPL v3.0** — `CONFIRMED` no arquivo `LICENSE`
- **Commit:** `d9a9ef0` (2026-11-17T11:20:53Z) · release `v0.5.2`
- **Métricas:** ★11.806 · 989 forks · 67 issues · criado 2026-10-29 (≈3 semanas) · **622 MB** de repositório · 2.428 arquivos · 257 `.rs` · 236 docs (218 `.md`) · 197 arquivos i18n (**86 idiomas**) · 7 workflows · 102 arquivos de teste

## 2. Resumo executivo

MDM é um gerenciador de downloads escrito em Rust, com GUI `egui`, suporte a HTTP
segmentado, torrent/magnet/seeding, debrid, HLS/DASH, yt-dlp/gallery-dl, extensão de
navegador e — o ponto que interessa à Lia — **um servidor MCP próprio**
(`crates/mcp`, crate `mdm-mcp`, com `rmcp` e teste stdio), cuja descrição declarada é
"lets AI assistants list, add and control the running app's downloads".

O encaixe conceitual com a Lia é forte: baixar pesos de modelo, texturas, assets e
vídeos grandes é uma necessidade recorrente do Forge e do Model Lab, e hoje não há
solução no ecossistema. O bloqueio é jurídico: **GPL-3.0**. Incorporar o crate
`mdm-mcp` a um app Lia proprietário contaminaria o conjunto. Usar o MDM como
**aplicação separada**, conversando por MCP/stdio, é arquiteturalmente limpo.

Além da licença, há um ponto de segurança concreto: a integração de navegador
transfere **cookies e referrer** da sessão do usuário para o gerenciador de downloads.
Isso é funcional (sites autenticados) e é exatamente o tipo de fluxo que exige
consentimento explícito no produto Lia.

## 3. O que resolve

| Problema | Solução observada |
|---|---|
| Download de arquivo grande com retomada | engine segmentada, retomada, múltiplas conexões (`crates/engine`) |
| Filas e paralelismo | `crates/app` + `crates/nmhost` |
| Verificação de integridade | `crates/extract`, `crates/tools` (`OBSERVED` pela estrutura) |
| Captura de downloads do navegador | extensão + helper nativo (Chrome/Edge/Brave/Opera/Vivaldi/Firefox 140+/Safari 17+) |
| Automação por agente | servidor MCP (`mdm-mcp`) |
| Vídeo/stream | HLS/DASH, m3u8 (`OBSERVED`) |
| Torrent | magnet, `.torrent`, seeding (`REPORTED` + `crates/torrent`) |

## 4. Arquitetura

```text
crates/
├── app        GUI (egui) + orquestração
├── engine     motor de download (segmentos, retomada)
├── nmhost     host do native messaging (integração navegador)
├── ipc        canal local app ↔ MCP ↔ CLI
├── mcp        ★ servidor MCP (bin: misterdownloadmanager-mcp, dep: rmcp)
├── cli        interface de linha de comando
├── torrent    magnet/BT
├── debrid     serviços debrid
├── extract    extração/verificação
├── remote     acesso remoto
├── labserver  servidor de laboratório/teste
├── cnl, crash, geo, tools
└── extension/ (JS)  extensão de navegador
```

Ponto de projeto relevante: o MCP **não** reimplementa o download; ele fala IPC com o
app rodando (`mdm-ipc`). Isso é o mesmo padrão saudável do HA-MCP: adaptador fino
sobre um serviço que já existe.

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Downloads HTTP segmentados com retomada | estável | `OBSERVED` (crates) |
| Torrent/magnet/seeding | estável | `REPORTED` (README) + `crates/torrent` |
| Debrid (Real-Debrid etc.) | estável | `REPORTED` + `crates/debrid` |
| yt-dlp / gallery-dl / HLS / DASH | estável | `REPORTED` |
| Extensão para 6 famílias de navegador | estável | `CONFIRMED` (`docs/browser-integration.md`) |
| Servidor MCP com controle de downloads | existe | `CONFIRMED` (`crates/mcp`, bin + teste stdio) |
| 86 idiomas | estável | `CONFIRMED` (197 arquivos i18n) |
| Portátil/instalável Windows x64/ARM64/x86, Linux, macOS experimental | estável | `REPORTED` |
| API local documentada | `UNVERIFIED` | não localizada doc de API HTTP; MCP e IPC existem |

## 6. Dependências

- Rust (edition/toolchain do workspace), `rmcp` (SDK MCP em Rust), `tokio`, `serde`,
  `schemars`, `url`.
- GUI `egui` (`REPORTED` pelo tópico do repositório e pela stack).
- Ferramentas externas opcionais: yt-dlp, gallery-dl, ffmpeg (para mux) — `INFERRED`.
- Nenhuma dependência de nuvem obrigatória; debrid é opcional e pago.

## 7. Requisitos de hardware e sistema

- Windows 10/11 x64, ARM64 e 32-bit; Linux (deb/rpm/AppImage); macOS experimental.
- Disco: domínio do usuário (baixa arquivos grandes).
- RAM/CPU: não medido (`UNVERIFIED`).
- Windows 11 + Ryzen 5 5500 + RX 580: compatível; GUI leve, sem uso de GPU relevante
  (`INFERRED` do `egui`).

## 8. Segurança e privacidade

| Item | Rótulo | Avaliação |
|---|---|---|
| Extensão envia **cookies** do site para o MDM | `CONFIRMED` (`docs/browser-integration.md`) | necessário para sites autenticados; exige consentimento explícito e escopo por site |
| Envia **referrer** e User-Agent | `CONFIRMED` | fingerprint; documentar |
| Repete requisição imitando o navegador em caso de bot-check | `CONFIRMED` | **não** resolve challenge; declara isso honestamente |
| Servidor MCP controla downloads locais | `CONFIRMED` | qualquer cliente MCP autorizado pode adicionar/gerenciar downloads |
| IPC local (não TCP público) | `OBSERVED` | reduz exposição de rede; verificar bind real antes de uso |
| Debrid = credencial de terceiro | `REPORTED` | armazenamento de token de serviço pago |

O texto do projeto é notavelmente honesto sobre limites ("It solves no challenge: a
site that still wants one answered refuses again"). Isso é bom sinal de engenharia.

Risco específico para a Lia: dar a um agente MCP a capacidade de **iniciar downloads
arbitrários** é equivalente a dar a ele a capacidade de **consumir disco e rede sem
limite**. Precisa de quota, allowlist de domínio e limite de tamanho — nada disso é
responsabilidade do MDM.

## 9. Licença e proveniência

- **GPL-3.0**, `CONFIRMED`. Copyleft forte.
- Consequências práticas (`INFERRED`, não parecer jurídico):
  - **incorporar** `crates/mcp` (ou qualquer crate) em app Lia proprietário obriga a
    distribuir o conjunto sob GPL-3.0 — inaceitável para os apps Lia;
  - **usar como processo separado** comunicando por MCP/stdio/IPC é a forma usual de
    manter separação, mas a fronteira precisa ser avaliada juridicamente
    (`AGUARDA DECISÃO`), porque "programa separado" tem critérios técnicos;
  - redistribuir o binário é permitido **com** código-fonte e avisos.
- Classe: `REFERENCE_ONLY` para código; `RESEARCH_ONLY` para trechos.
- Marca: nome e logo do MDM não são licenciados pela GPL.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~3 semanas (criado 2026-10-29) | **muito novo** |
| Estrelas | 11.806 em 3 semanas | crescimento anômalo; validar antes de confiar |
| Releases | v0.5.x em ~3 semanas | cadência altíssima, pré-1.0 |
| Testes | 102 arquivos, incluindo `crates/mcp/tests/stdio.rs` | bom para a idade |
| CI | 7 workflows | ativo |
| Issues | 67 | projeto sob carga |

O crescimento de estrelas e a maturidade de código de um projeto de três semanas com
622 MB de repositório merecem a ressalva de `EVIDENCE-STANDARDS.md` §2.5: popularidade
não é maturidade. Tratar como beta até haver histórico.

## 11. Custos e limitações

- Financeiro: GPL-3.0 gratuito; debrid opcional é pago.
- Integração: **jurídica**, não técnica. Tecnicamente o MCP facilita.
- Limitações: pré-1.0; macOS experimental; não resolve captcha; sem garantia de API
  estável (`rmcp` também jovem).

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 | sim | x64 nativo |
| Sem CUDA/ROCm | sim | irrelevante |
| Não incorporar GPL | **somente como processo externo** | decisão jurídica necessária |
| Automação por agente | sim | MCP |
| Consumo de rede/disco controlado | **não** | quotas seriam da Lia |
| Distribuição a usuário final | possível, mas sob GPL | avaliar |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Forge | baixar assets, texturas, HDRIs, packs grandes |
| Lia Agent Hub | registrar `mdm` como servidor MCP de utilidade |
| Lia Model Lab | baixar pesos GGUF de 2–8 GB com retomada |

## 14. Oportunidades de reutilização

1. **Padrão adaptador-fino sobre serviço existente** (MCP → IPC → app), replicável.
2. **Retomada + verificação de integridade** como requisito mínimo de qualquer download
   de peso de modelo (a Lia hoje não tem isso).
3. **Extensão de navegador com consentimento por site** — modelo de UX para capturar
   downloads sem sequestrar a sessão.
4. **Honestidade documental** sobre o que não faz (não resolve captcha).

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| GPL-3.0 contaminar app proprietário | **alta** | só processo externo; parecer antes |
| Projeto imaturo (3 semanas, pré-1.0) | alta | não depender de estabilidade; pin |
| Cookies de navegador expostos ao downloader | **alta** (privacidade) | consentimento explícito, escopo por site |
| Agente disparando downloads sem quota | média | allowlist + limite de tamanho + disco |
| Crescimento anômalo de estrelas | baixa | tratar como sinal, não como prova |
| Sem API HTTP documentada | baixa | usar MCP, não inventar integração |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | GPL-3.0 | CONFIRMED | `@d9a9ef0:LICENSE` | 2026-11-17 |
| E2 | Servidor MCP existe (crate `mdm-mcp`, `rmcp`, teste stdio) | CONFIRMED | `crates/mcp/Cargo.toml`, `crates/mcp/tests/stdio.rs` | 2026-11-17 |
| E3 | Extensão de navegador envia cookies/referrer/UA | CONFIRMED | `docs/browser-integration.md` | 2026-11-17 |
| E4 | 86 idiomas | CONFIRMED | 197 arquivos i18n no tree | 2026-11-17 |
| E5 | "5× mais rápido que IDM", 1 GB em 1 s | REPORTED | README (badge) — método e hardware não declarados; plausível apenas em loopback | 2026-11-17 |
| E6 | Consumo de RAM/CPU/ disco | BLOCKED | não executado | — |
| E7 | Binding de rede do IPC/MCP | UNVERIFIED | não lido `crates/ipc/src` a fundo | — |

## 17. Recomendação

**`REFERENCE_ONLY`** para o produto, com **`ADAPT`** permitido apenas na forma
"processo externo + MCP".

**Gates:**

1. parecer jurídico sobre a fronteira GPL antes de qualquer empacotamento;
2. nunca copiar código de `crates/*` para repositório Lia;
3. se integrado: quota de disco, allowlist de domínio, limite de tamanho, log;
4. consentimento explícito para cookies de navegador;
5. versão pinada; tratar como beta.

**Não autoriza:** incorporar o crate MCP, redistribuir o binário no instalador da Lia
sem análise, ou habilitar download arbitrário por agente.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Parecer sobre GPL × distribuição Lia | proprietário / jurídico | `AGUARDA DECISÃO` |
| 2 | Protótipo: MDM externo baixando um GGUF de 2 GB com retomada e hash | Model-Lab | download verificado |
| 3 | Verificar bind do IPC/MCP (loopback?) | Research | `CONFIRMED` de exposição |
| 4 | Definir política de quota de download para agentes | Forge | spec |
| 5 | Revisar em 90 dias (projeto jovem) | Research | novo commit |
