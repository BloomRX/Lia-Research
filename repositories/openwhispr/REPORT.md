# OpenWhispr — transcrição local em app desktop que publica as próprias Skills e uma allowlist de rede

| Campo | Valor |
|---|---|
| ID | `LR-VOICE-004` |
| Nome | `OpenWhispr/openwhispr` — ditado e transcrição offline (Whisper, Parakeet, Cohere Transcribe, Orukeet) com alternativa em nuvem |
| Tipo | repositório |
| Fonte oficial | https://github.com/OpenWhispr/openwhispr |
| Responsável | "OpenWhispr Team" (`Copyright (c) 2024 OpenWhispr Team` no LICENSE) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN |
| Recomendação | **ADAPT** — três artefatos: `docs/network-allowlist.md`, o par de Skills operacionais do produto, e a tabela de versões suportadas |
| Decisão de adoção | — nenhuma registrada |
| Categoria | produto concorrente de voz (o par direto do `lia-voice-input`) |
| Projetos beneficiados | Lia Voice Input (arquitetura de app + modelos locais + helpers por SO), Lia Forge (notarização, builders por plataforma), Lia Project (Skills para API/CLI de um produto próprio), Lia Research (`network-allowlist` como formato de divulgação) |
| Versão analisada | `v1.12.0` (release 2026-11-17) · push em 2026-11-24 (no dia da medição) |
| Proveniência do conteúdo | **medido por nós** via API (repo, release, workflows, `agent-skills/`, `docs/`, LICENSE, SECURITY.md); nada foi executado nem baixado |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 · 12.132★ · 1.614 forks · **519 issues abertas** · 27 watchers · `size` 363.936 KB |
| Upstream conferido | 2026-11-24 · `has_discussions: true`, `has_wiki: false` · 19 workflows |
| Próxima revisão | 2027-02-24 |
| Licença | **MIT** (`LICENSE` lido: "MIT License / Copyright (c) 2024 OpenWhispr Team"); nenhum LICENSE adicional por diretório foi procurado nesta passada (limitação em §6) |
| Confiança | Alta para o que está nos arquivos; nenhuma para acurácia de transcrição, que é o assunto real do produto |

---

## 1. Por que este objeto entrou na base

É o peer arquitetural mais próximo do `lia-voice-input` entre os oito links da leva: app de desktop com
reconhecimento **local**, com nuvem como opção, e que resolve os mesmos três problemas incômodos —
captura de áudio por sistema operacional, distribuir/validar pesos de modelo, e entregar o produto a um
agente. Diferente do VoiceStudio (`LR-VOICE-003`), que é o par AGPL+multiplataforma com corpus de testes
de pinos, o OpenWhispr é Electron/JS com **helpers nativos por plataforma compilados um por workflow**, e
isso é exatamente o formato que o Lia Project precisa decidir se adota.

Os dois números que situam o objeto: **12.132 estrelas** e **519 issues abertas** — 1 issue a cada 23
estrelas (o VoiceStudio tem 22 issues para 117.344 estrelas). Não é julgamento de qualidade: é a
indicação de que é um projeto novo, com superfície de hardware grande, e com fila visível. O `SECURITY.md`
dele (lido) tem tabela "Supported Versions": `1.10.x ✔`, `< 1.10 ✘`, enquanto a release mais recente
medida é `v1.12.0` — a tabela **não acompanhou** o próprio release. Um detalhe, mas é o tipo que a nossa
casa deveria checar (`tools/validate.py` não tem nada equivalente).

## 2. O objeto medido

| Campo | Valor |
|---|---|
| Estrelas / forks / watchers / issues | 12.132 / 1.614 / 27 / **519** |
| Criado / último push / release | 2025-06-19 / 2026-11-24 / `v1.12.0` (2026-11-17) |
| Idiomas | JavaScript 58,2 % · TypeScript 36,8 % · Swift 3,4 % |
| `size` | 363.936 KB |
| Workflows | **19** |
| Raiz | .env.example, .gitattributes, .npmrc, .nvmrc, CHANGELOG.md, CLAUDE.md, DEBUG.md, LOCAL_WHISPER_SETUP.md, TROUBLESHOOTING.md, LICENSE, `.oss-scanner/`, `.prettierrc`, `.prettierignore`, docs/, agent-skills/ |
| Topics | ai, anthropic, cross-platform, gemini, groq, linux, macos, nvidia |
| Skill publicada | `agent-skills/openwhispr-api/SKILL.md` e `agent-skills/openwhispr-cli/SKILL.md` — **um único arquivo cada** |
| Scanner próprio | `.oss-scanner/` com `Dockerfile` e `threat_model.md` |

Das 19 workflows, 8 são **builders de helper por plataforma** (medidas pelo nome):
`build-windows-fast-paste.yml`, `build-windows-key-listener.yml`, `build-windows-mic-listener.yml`,
`build-windows-system-audio-helper.yml`, `build-windows-text-monitor.yml`,
`build-linux-text-monitor.yml`, `build-meeting-aec-helper.yml`, `build-and-notarize.yml`. Somam-se a
elas `ci-changes.yml`, `codeql.yml`, `llm-canary.yml`, `lockfile-lint.yml` e mais quatro não abertas.

Três coisas merecem destaque do jeito que foram medidas:

1. **um helper nativo = uma workflow = um binário**: captura de teclado, colagem rápida, microfone, áudio
   do sistema e monitor de texto são artefatos separados, compilados separadamente. O `build-meeting-aec-*`
   é o cancelamento de eco para reunião — a parte mais difícil do produto, isolada;
2. `build-and-notarize.yml` separa **notarizar** de *empacotar*: no `LR-FORGE-014` (Bisqit) a notarização
   era afirmação de marketing; aqui é um passo nomeado de CI;
3. `llm-canary.yml` existe — um canário para comportamento de modelo. O arquivo não foi aberto nesta
   passada; registro a existência e deixo a pergunta em §6.

## 3. O que o produto diz que faz (REPORTED) e o que eu li (CONFIRMED)

Do README (trechos lidos, marcados como **afirmação do fornecedor**): "offline transcription with local
speech-to-text models like Orukeet, Whisper, NVIDIA Parakeet, and Cohere Transcribe — where your audio
never leaves your device"; "GPU-accelerated local Whisper on Metal, CUDA, and Vulkan (AMD/Intel)";
stack declarada "whisper.cpp, sherpa-onnx, shadcn/ui"; lista de modelos incluindo
`nvidia/parakeet-tdt-0.6b-v3` (link direto para o Hugging Face) e menção a "Whisper, Parakeet, and
embedding model weights"; plano gratuito com "2,000 hosted words/week".

Confirmado por mim em arquivo, não por eles: o `LICENSE` é MIT **com copyright de 2024** enquanto o
repositório foi criado em 2025-06-19 — o que é consistente com código reaproveitado ou projeto começado
fora do GitHub, e é tudo que tenho para dizer (§6).

## 4. Os dois artefatos transplantáveis

### 4.1 `docs/network-allowlist.md`

Título e primeiro parágrafo, lidos: "Network Allowlist — Outbound hosts the OpenWhispr desktop app
contacts. For firewall, proxy, and DNS filter configuration. Destination connections are client-initiated
over TLS. **A configured HTTP proxy uses an unencrypted CONNECT hop; use an HTTPS proxy when that hop also
requires TLS. No inbound ports.**" e a tabela começa sob "Required by default — Contacted by every
install using OpenWhispr Cloud (the default after onboarding)".

É a versão de engenharia do que o Bisqit fez em página de privacidade (`LR-FORGE-014` §9), com três
vantagens: está **no repositório**, é **por host** (não por "parceiros"), e admite a **fraqueza do
próprio desenho** (o CONNECT sem TLS em proxy HTTP). Para o Lia Project isso é um formato melhor do que
qualquer "política de privacidade" genérica, e o custo é uma tabela. Fica como recomendação para o
`lia-voice-input`, que tem exatamente esse problema: microfone + modelo + (opcionalmente) provedor.

### 4.2 `agent-skills/` com um arquivo cada

Frontmatter das duas Skills (lido): só `name` + `description`. O da API: "Use this skill when building
integrations with the OpenWhispr REST API, calling OpenWhispr endpoints, managing notes/folders/
transcriptions programmatically, accessing team-space content with workspace keys, or connecting …". A do
CLI: "… whenever the user wants to operate on OpenWhispr notes, folders, transcriptions, or audio from a
terminal or shell. The OpenWhispr CLI (`openwhispr` binary, npm package `@openwhispr/cli`) talks to either
…".

Registro a comparação honestamente: é o **mínimo** (um arquivo, sem scripts, sem `references/`, sem
validação), enquanto `LR-FORGE-017` tem 28 Skills com espelho gerado por CI e `LR-FORGE-016` o pack MIT
com `validation/baseline.md` + `validation/loopholes.md`. Ou seja: **publicar Skills dentro do app virou
prática comum** (três dos oito objetos desta leva fazem isso), e a qualidade vai de "um `SKILL.md`" a
"corpus com teste de deriva". A nossa régua (48 registros em `agents/SKILLS-OPERATING-SET.md`) está no
terço de cima; isso é o que o `projects/lia-agent-hub` tem para oferecer a um projeto como este, e não o
contrário.

### 4.3 Os `docs/` que valem leitura futura

`affiliate-integration.md`, `enterprise-audio-runbook.md`, `integrations-compatibility.md`,
`integrations/`, `network-allowlist.md`, `orukeet-benchmarks.md`, `orukeet-streaming.md`,
`orukeet-streaming-language.md`, `private-note-conversations.md`, `private-notes-release-checklist.md`,
`product-help.md`, `product-help-qa-2026-10-07.md`, `superpowers/plans`, `superpowers/specs`,
`validation/local-selection-edit`.

Três nomes dizem muito: `enterprise-audio-runbook.md` (runbook de áudio para empresa, dentro de um MIT
comunitário), `private-notes-release-checklist.md` (checklist de release de um recurso) e
`orukeet-benchmarks.md` (benchmark do modelo próprio dentro do repositório do app). É o mesmo movimento do
`docs/maintainers/` do `LR-FORGE-017`: operação de produto versionada junto do código.

## 5. Comparação direta na leva (voz)

| | OpenWhispr | VoiceStudio (`LR-VOICE-003`) | Lia Voice Input (hoje) |
|---|---|---|---|
| Licença | MIT | AGPL-3.0-only + NOTICE de assets | ver `data/inventory/license-matrix.tsv` |
| Shell do app | Electron/JS + Swift | Python + TS + Swift + Kotlin | Tauri/Rust |
| Modelo local | Whisper/Parakeet/Cohere/Orukeet via whisper.cpp e sherpa-onnx | OmniVoice (TTS) com revisão pinada + cache retrocompatível | decisão pendente no Lia Model Lab |
| Áudio avançado | AEC por helper dedicado | pedalboard com pin de workaround por sinal (SIGILL) | — |
| Rede | **allowlist de hosts publicada** | não medi | nada |
| Skills | 2 arquivos `SKILL.md` | `.agents/` + `.claude/` na raiz | 48 registros em `agents/SKILLS-OPERATING-SET.md` |
| CI de release | 8 builders de helper + notarização | 34 workflows com pins verificados por teste | n/a |
| Ameaça | `.oss-scanner/threat_model.md` | `.gitleaks.toml` | `governance/SECURITY-AND-PRIVACY-POLICY.md` |

## 6. O que não verifiquei, e por quê

| Item | Estado | Motivo |
|---|---|---|
| Executar o app, medir latência/acurácia em PT-BR | `BLOCKED` | exigiria instalar um app Electron com acesso a microfone; nada foi instalado (regra permanente) |
| Baixar os pesos (Whisper/Parakeet/Orukeet) | `NOT_RUN` | proibido por esta política: nenhum modelo baixado; os termos de cada peso **não** foram lidos |
| Conteúdo de `threat_model.md`, `llm-canary.yml`, `orukeet-benchmarks.md` | `NOT_RUN` | existência medida, arquivos não abertos nesta passada — é o que fecha a §4 e fica como pendência de nível 1 |
| Se `TROUBLESHOOTING.md`/`DEBUG.md`/`LOCAL_WHISPER_SETUP.md` cobrem o hardware da Lia (RX 580/gfx803 é o caso nosso em `LR-HW-001`) | `NOT_RUN` | não lido; é a checagem que decidiria se vale recomendar |
| Licenças por subdiretório e termos dos modelos linkados | `UNVALIDATED` | nenhum LICENSE aninhado foi procurado; o `nvidia/parakeet-…` no HF tem termos próprios que não abri |
| Por que o copyright é 2024 e o repo 2025 | `UNVALIDATED` | histórico não medido (sem clone) |
| O que as 519 issues contêm | `NOT_RUN` | fora da pergunta; uma varredura de rótulos seria a próxima passada se o dono quiser |

## 7. Recomendação: **ADAPT** (duas formas, zero código)

1. **Adaptar a allowlist de rede** como formato de divulgação do `lia-voice-input` — tabela de hosts de
   saída + "no inbound ports" + a fraqueza do proxy explicitada, dentro do repositório, não num site.
2. **Adaptar o nome `Supported Versions` no `SECURITY.md`** e corrigir o nosso quando a release passar da
   linha da tabela; é um caso concreto de "declaração que envelhece", que a nossa base ainda não checa.
3. **Registrar, sem adotar**: o padrão "um helper nativo por workflow" para captura de áudio/teclado por SO
   — se o `lia-voice-input` crescer para Windows, é o desenho a copiar (e o oposto do app monolítico).
4. **Não recomendo** citar o OpenWhispr como "verificado" para PT-BR, custo de modelo ou folga de hardware:
   nada disso foi medido (§6) e o `LR-HW-001` mostra que nossa máquina é o caso raro.
5. **Decisão do dono**: (a) se abrimos pendência para os termos dos pesos que um app desses baixa
   (o mesmo eixo do `LR-MODEL-009`); (b) se o `network-allowlist` vira template em `templates/`; (c) se a
   casa responde publicamente a Skills de terceiros no nível "um arquivo" com uma nota de comparação, ou
   se ficamos só no nosso inventário.

## 8. O que o objeto afirma × o que este relatório sustenta

| Afirmação do README deles | Nosso estado | Por quê |
|---|---|---|
| Transcrição offline, "your audio never leaves your device" | `REPORTED` | não executamos o app nem observamos tráfego; a allowlist (§4.1) torna a afirmação *auditável*, não auditada |
| "646 languages" (frase do VoiceStudio, citada aqui para contraste) / cobertura linguística do OpenWhispr | `UNVALIDATED` | nenhuma lista de idiomas foi conferida |
| GPU local em Metal, CUDA e Vulkan (AMD/Intel) | `REPORTED` | a RX 580 da Lia é o caso difícil (`LR-HW-001`); não testado |
| 2.000 palavras/semana no plano nuvem | `REPORTED` | nenhuma conta criada |
| `threat_model.md` existe | `CONFIRMED` (existência) / `NOT_RUN` (conteúdo) | listado, não lido |
| As Skills de API e CLI funcionam como escritas | `UNVALIDATED` | nenhum binário `openwhispr` executado |

## 9. Pendência que a Research fecha sozinha (nenhuma precisa de autorização)

1. abrir `.oss-scanner/threat_model.md`, `docs/orukeet-benchmarks.md`, `docs/enterprise-audio-runbook.md`
   e `llm-canary.yml` — os quatro são o material que transformaria a §2 de "listagem" em avaliação; é
   nível 1, só leitura de arquivo;
2. ler `LOCAL_WHISPER_SETUP.md`/`TROUBLESHOOTING.md` contra o hardware da Lia (`gfx803`) e fechar se há
   ou não algo a recomendar ao `lia-voice-input`;
3. censurar `LICENSE*` e `NOTICE*` na árvore recursiva (fizemos isso para os outros sete; aqui ficou
   faltando — linha honesta em §6) e conferir se os pesos linkados trazem termos incompatíveis com MIT;
4. varrer rótulos das 519 issues abertas para ver se o volume é de suporte ou de defeito — essa
   diferença muda a leitura de "projeto novo com fila grande".

## 10. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| 12.132★ · 1.614 forks · 519 issues · 27 watchers · JS 58,2/TS 36,8/Swift 3,4 · `size` 363.936 KB · criado 2025-06-19 · push 2026-11-24 · `v1.12.0` (2026-11-17) | `CONFIRMED` | `gh api repos/OpenWhispr/openwhispr` + `releases/latest` + `languages` |
| 19 workflows, das quais 8 builders de helper por plataforma + `build-and-notarize.yml` + `llm-canary.yml` + `lockfile-lint.yml` + `codeql.yml` | `CONFIRMED` | `contents/.github/workflows` |
| `agent-skills/{openwhispr-api,openwhispr-cli}` com **um** `SKILL.md` cada, frontmatter `name` + `description` | `CONFIRMED` | `contents/agent-skills` + os dois arquivos |
| `docs/network-allowlist.md` com o texto sobre CONNECT sem TLS e "No inbound ports" | `CONFIRMED` | arquivo decodificado (trecho transcrito em §4.1) |
| `SECURITY.md`: tabela de versões suportando `1.10.x` enquanto a release é `v1.12.0` | `CONFIRMED` (as duas leituras) | `SECURITY.md` + `releases/latest` |
| `.oss-scanner/{Dockerfile,threat_model.md}` e os 15+ itens de `docs/` nomeados na §4.3 | `CONFIRMED` | `contents/.oss-scanner` + `contents/docs` |
| MIT "Copyright (c) 2024 OpenWhispr Team" | `CONFIRMED` | `LICENSE` lido |
| Transcrição offline com Orukeet/Whisper/Parakeet/Cohere; 2.000 palavras/semana no plano nuvem; AEC; Vulkan/Metal/CUDA | `REPORTED` | README (nada executado nem medido) |
| Qualidade em PT-BR, consumo de VRAM, termos dos pesos, conteúdo dos benchmarks | `UNVALIDATED` | fora do escopo medível aqui |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · par da mesma leva:
`repositories/voicestudio/REPORT.md` · digest de voz desta casa: `cross-project/voice/VOICE-STACK-DIGEST.md`
· hardware da Lia: `cross-project/hardware/WINDOWS-AMD-COMPATIBILITY.md` · formato de divulgação
comparado: `repositories/bisqit/REPORT.md` (`LR-FORGE-014` §9).
