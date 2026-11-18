# BRUTAL — framework de jogo em C#, com licença de atribuição gráfica

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-005` |
| Categoria | studio (leitura transversal em licensing, hardware) |
| Projetos beneficiados | Lia Studio (referência de runtime), Lia Forge (interop nativo), Lia-Research (governança de contribuição) |
| Fontes | `ahwootech/BRUTAL@c4c62f55286828e51ba93b59ec7fa21ecedae3ca`: `README.md` (10 KB), `LICENSE.txt`, `NOTICE.txt`, `CONTRIBUTING.md`, árvore completa (6.016 entradas), API do GitHub |
| Data | 2026-11-17 |
| Próxima revisão | 2027-02-17 |
| Status | CURRENT |
| Recomendação | **REFERÊNCIA** — não adotar; três práticas a adaptar |
| Licença | **BRUTAL License v1.0** — base MIT + créditos + **logo antes do gameplay** + `NOTICE.txt`; **não é OSI** (`CONFIRMED` no texto) |
| Confiança | Alta para licença, escopo e estrutura (arquivos lidos); **UNVERIFIED** para desempenho e para rodar na RX 580 |

---

## 1. Identificação

| Item | Valor |
|---|---|
| Repositório | https://github.com/ahwootech/BRUTAL · site https://ahwoo.com/brutal |
| Autor | Ahwoo Limited (RocketWerkz) — © 2024 |
| Commit analisado | `c4c62f55` (2026-11-12) |
| Métricas | ★ **2.527** · 170 forks · 23 issues abertas · 4,2 MB · 6.016 entradas na árvore |
| Linguagem | C# (.NET **10**) + interop nativo; Vulkan via bindings |
| Plataformas | **Windows e Linux** (macOS não consta nos pré-requisitos) |
| Status | publicado como pacotes NuGet (`Ahwoo.Brutal.*`); **sem `.csproj`/`.sln` no repositório** |
| Em uso | RimWorld (Ludeon, motor *Waylith*), Kitten Space Agency, Torpedia, Gruntz, Afterskies (`REPORTED` no README) |

## 2. Resumo executivo

Não é mais um motor de jogo. É a **camada de fundação** que sobra quando você remove
editor, grafo de cena e renderizador: interop direto para C#, memória não gerenciada,
coleções sem alocação, job system, matemática, e bindings para Vulkan, GLFW/SDL, ImGui,
FMOD, Jolt, Box2D, glTF, FreeType.

O que interessa à Lia não é o código (C#/.NET 10 contra Electron/Vue). São **três práticas**
e **um aviso de licença**:

1. **Licença com atribuição gráfica** — MIT + créditos + **logo obrigatório antes do
   gameplay** + `NOTICE.txt`. Isso é a fronteira entre "open source" e "source available
   com branding", e a Lia vai encontrar exatamente essa dúvida ao licenciar os apps.
2. **Política explícita de contribuição assistida por IA** — você pode usar agente, mas
   responde por cada linha, precisa ter testado e precisa declarar. É a cláusula que falta
   no nosso `agents/`.
3. **`LICENSES/` por biblioteca** — cada pacote carrega os avisos de terceiros que ele
   redistribui. É a resposta estrutural ao erro que o ecossistema Lia comete (aviso na
   raiz, payload sem aviso).

E um dado de maturidade que ninguém deve ignorar: **5.070 dos 5.644 arquivos `.cs` são
gerados** (`.gen.cs`), não há CI além de um bot de boas-vindas, e o README admite que
"project files, a solution and build scripts are coming" — hoje o repositório serve para
**ler e forkar**, não para compilar.

## 3. O que resolve

| Problema | Como o BRUTAL resolve |
|---|---|
| Engine grande decide arquitetura por você | "não faz as decisões arquiteturais por você": você monta a pilha |
| C# com GC em código de tempo real | memória não gerenciada, coleções sem alocação, `unsafe` onde importa |
| Camadas de wrapper lentas | um interop próprio, acesso direto às APIs nativas |
| Dependência de um fornecedor de engine | "você só é tão independente quanto suas ferramentas" |
| Aviso de terceiros espalhado | `LICENSES/` por biblioteca publicada |

## 4. Arquitetura

```text
BRUTAL (um pacote NuGet por pasta de topo)
├── Brutal.Core            tipos base, atributos, detecção de plataforma, analyzers Roslyn
├── Brutal.Interop         camada própria de interop C# → nativo
├── Brutal.Memory          alocadores e memória não gerenciada
├── Brutal.Collections / Strings / Maths / Numerics / Concurrency / Logging / Localization
├── Brutal.Vulkan|.Abstractions|.Vma    bindings, abstrações, VMA
├── Brutal.ShaderC / Slang              compilação de shader
├── Brutal.Glfw / Sdl(+Image/Mixer/Ttf) / NotCurses / NativeFileDialog
├── Brutal.ImGui / ImGui.* / ImPlot     UI imediata e gráficos
├── Brutal.Texture / Ktx / Gli / Stb    texturas e formatos comprimidos
├── Brutal.Gltf / MeshOptimizer         glTF e otimização de malha
├── Brutal.FreeType                     rasterização de fonte
├── Brutal.Fmod / OpenAl                áudio
├── Brutal.RakNet                       rede
├── Brutal.Jolt / Box2D                 física 3D e 2D
└── samples/Demo/                       demos por recurso (Box2D, Gltf, ImGui, Jolt, RenderDoc, SDL, quad texturizado)
```

Cada pasta = um pacote `Ahwoo.Brutal.*` no NuGet. Sem editor, sem grafo de cena, sem
renderizador — por decisão declarada, com PRs que "driftam" sendo rejeitados.

## 5. Funcionalidades

| Grupo | O que oferece |
|---|---|
| Base | tipos, atributos, detecção de plataforma, analyzers |
| Memória e concorrência | alocadores, coleções e strings sem alocação, job system |
| Gráficos | Vulkan (+ abstrações e VMA), OpenGL, ShaderC/Slang, KTX/GLI, glTF, texturas |
| Janela e UI | GLFW, SDL (+image/mixer/ttf), Dear ImGui (branch docking), ImPlot |
| Áudio, rede, física | FMOD, OpenAL, RakNet, Jolt (3D), Box2D (2D) |
| Ferramentas | RenderDoc capture, monitor de runtime, terminal UI (NotCurses), diálogos nativos |

## 6. Dependências

| Dependência | Papel | Rótulo |
|---|---|---|
| .NET 10 SDK | compilar/consumir | `CONFIRMED` |
| Vulkan 1.3 + drivers | renderização | `CONFIRMED` (pré-requisito declarado) |
| Vulkan SDK | validation layers em desenvolvimento | `CONFIRMED` |
| Pacotes NuGet `Ahwoo.Brutal.*` | distribuição real (o repo não compila) | `CONFIRMED` |
| Bibliotecas nativas de terceiros (Vulkan, GLFW, SDL, FMOD, Jolt, Box2D, FreeType, ImGui…), cada uma com sua licença em `LICENSES/` | — | `CONFIRMED` |

## 7. Requisitos de hardware e sistema

- **Windows ou Linux**; macOS **não** aparece nos pré-requisitos.
- **GPU com Vulkan 1.3** — este é o ponto de contato direto com o hardware da Lia.
  A máquina de referência é Windows 11 + **RX 580** (Polaris). Se ela expõe Vulkan 1.3
  completo **não está verificado aqui** (`UNVERIFIED`): é um teste de 10 minutos
  (`vulkaninfo | head`) que vale registrar em `LR-HW-001` antes de qualquer plano que
  dependa de Vulkan 1.3.

## 8. Segurança e privacidade

| Item | Situação |
|---|---|
| Canal de segurança | `SECURITY.md` pede relato **privado**, não issue pública `CONFIRMED` |
| Código `unsafe` | explícito por desenho ("unmanaged memory and unsafe code where it makes sense") — superfície de risco inerente |
| CI de segurança | **nenhuma**: o único workflow é `first-interaction.yml` (bot de boas-vindas) `CONFIRMED` |
| Dependências | avisos por biblioteca em `LICENSES/` `CONFIRMED` |
| Dados de usuário | framework de runtime; não coleta nada por si |
| Risco para a Lia | nenhum direto — não há integração proposta |

## 9. Licença e proveniência

**BRUTAL License v1.0**, © 2024 Ahwoo Limited (`CONFIRMED`, texto integral lido):

| Cláusula | Obrigação |
|---|---|
| 1.0 | manter copyright + permissão em cópias |
| 2.1 | copyright na **tela de créditos** do produto |
| 2.2 | **logo BRUTAL exibido antes do gameplay**/função principal, não menos proeminente que outros logos; dispensado com permissão escrita, para projeto sem fins lucrativos, ou quando exibir o logo prejudica o propósito |
| 2.3 | distribuir `NOTICE.txt` junto do produto |
| 3.0 | "AS IS", sem garantia |
| 4.0 | terceiros mantêm suas licenças (`LICENSES/` por pacote) |
| 5.0 | **concessão de contribuição**: quem envia PR concede licença perpétua e irrevogável à Ahwoo |

Leitura honesta:

- **Não é copyleft** e permite uso comercial, modificação, fork e sublicença.
- **Não é OSI** — e o próprio README diz isso ("not yet OSI approved"). Uma cláusula de
  exibição obrigatória de logo é exatamente o tipo de restrição que a OSI costuma tratar
  como não-livre.
- Para a Lia, a consequência prática é de **produto**: se um app Lia usasse BRUTAL, teria
  que mostrar o logo da Ahwoo antes da função principal. Isso é decisão de branding, não
  de engenharia.
- O padrão **bom** a imitar: `NOTICE.txt` explícito + `LICENSES/` por pacote + seção que
  responde "posso usar comercialmente?" em uma frase.

VERDICT de licença: **`REFERENCE_ONLY`** para código; **`ADAPT_ALLOWED`** para as práticas.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | criado 2026-10-14, último push 2026-11-12 | novo na forma pública; o produto tem anos |
| Estrelas / forks | 2.527 / 170 | adoção real |
| Issues abertas | 23 | baixo |
| Projetos em produção | RimWorld, KSA, Torpedia, Gruntz, Afterskies | `REPORTED` — sinal forte |
| **Compila?** | **não**: 0 `.csproj`, 0 `.sln`, "build scripts are coming" | `CONFIRMED` |
| CI | 1 workflow (boas-vindas) | `CONFIRMED` |
| Código gerado | **5.070 de 5.644 `.cs`** são `.gen.cs` | `CONFIRMED` |
| Documentação | README + `samples/Demo` + fórum | `CONFIRMED` |
| Política de contribuição | DCO + concessão de licença + cláusula de IA | `CONFIRMED` |

## 11. Custos e limitações

| Item | Limite |
|---|---|
| Stack | C#/.NET 10 — não conversa com Electron/Vue/TS da Lia sem reescrever |
| Compilação | hoje só via NuGet; o repositório é para leitura/fork |
| Vulkan 1.3 | exclui GPUs antigas e não foi testado na RX 580 |
| Plataforma | sem macOS nos pré-requisitos |
| Licença | logo obrigatório no produto |
| Escopo | sem editor/renderizador por decisão — não substitui um motor |

## 12. Compatibilidade com o ecossistema Lia

| Dimensão | Situação |
|---|---|
| Windows 11 | **sim** (pré-requisito) |
| RX 580 / Vulkan 1.3 | `UNVERIFIED` — testar antes de planejar |
| Electron/Vue | incompatível como biblioteca |
| Python | incompatível; exigiria processo separado |
| Skills/MCP | nenhuma superfície de agente |
| Licença | permite uso comercial; exige logo |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| **Lia Studio** | referência de "framework, não engine" e de como embutir runtime nativo sem herdar arquitetura alheia |
| **Lia Forge** | referência de interop nativo e de `LICENSES/` por pacote |
| **Lia Agent Hub** | modelo de política de contribuição assistida por IA |
| **Lia Model Lab** | nenhum (não há camada de modelo) |
| **Lia-Research** | padrão de `NOTICE.txt` e de seção "posso usar comercialmente?" |

## 14. Oportunidades de reutilização

| # | Prática | O que copiar | Onde |
|---|---|---|---|
| B1 | **Política de IA em contribuição** | "você pode usar agente; responde por cada linha; declare no PR; PR grande, não testado e inexplicado é fechado" | `agents/` desta base e dos projetos |
| B2 | **`LICENSES/` por pacote** | avisos de terceiros viajam com o pacote que redistribui | `LR-LIC-005`, Forge, Studio |
| B3 | **Declaração de escopo** | "não é motor geral; PR que driftar é rejeitado" | README de cada app |
| B4 | **`NOTICE.txt` curto e explícito** | 3 linhas que respondem "o que é, quem fez, sob qual licença" | `LR-LIC-005` |
| B5 | **Teste de hardware** | `vulkaninfo` na RX 580 antes de qualquer plano Vulkan 1.3 | `LR-HW-001` |

## 15. Riscos e incompatibilidades

| Risco | Severidade | Nota |
|---|---|---|
| Tratar "open source" do README como OSI | média | a própria licença diz que não é aprovada |
| Logo obrigatório antes do gameplay | média | decisão de produto; alternativa é licença comercial paga |
| Assumir que compila | **alta** | não há projeto/solução no repositório |
| Vulkan 1.3 na RX 580 | média | `UNVERIFIED`; se falhar, o framework está fora do hardware-alvo |
| Cláusula 5.0 (concessão de contribuição) | baixa | quem contribui cede licença perpétua — ler antes de mandar PR |
| Código `unsafe` + ausência de CI | média | superfície de risco sem rede automática |

## 16. Evidências e fontes

| # | Evidência | Rótulo | Fonte |
|---|---|---|---|
| E1 | BRUTAL License v1.0: MIT + créditos + logo antes do gameplay + NOTICE, não OSI | CONFIRMED | `LICENSE.txt` + README §Licence |
| E2 | 6.016 entradas; um pacote por pasta de topo | CONFIRMED | Trees API |
| E3 | 0 `.csproj` / 0 `.sln`; "build scripts are coming" | CONFIRMED | Trees API + README |
| E4 | 5.070 de 5.644 `.cs` são gerados | CONFIRMED | contagem na árvore |
| E5 | 1 único workflow (boas-vindas) | CONFIRMED | `.github/workflows/` |
| E6 | .NET 10, Vulkan 1.3, Windows/Linux | CONFIRMED | README §Prerequisites |
| E7 | RimWorld/Waylith, KSA, Torpedia, Gruntz, Afterskies usam | REPORTED | README §Projects |
| E8 | RimWorld 2–4× mais rápido que Unity (teste do Ludeon) | REPORTED | README, citação de anúncio Steam |
| E9 | Política de contribuição assistida por IA + DCO + cláusula 5.0 | CONFIRMED | `CONTRIBUTING.md` |
| E10 | Desempenho no hardware da Lia | **UNVERIFIED** | não executado |
| E11 | Suporte a Vulkan 1.3 na RX 580 | **UNVERIFIED** | requer `vulkaninfo` |
| E12 | macOS suportado | `UNVERIFIED` | não consta nos pré-requisitos |

## 17. Recomendação

**VEREDITO: `REFERÊNCIA`** — não adotar; adaptar três práticas.

Não há caminho técnico para usar BRUTAL nos apps Lia sem trocar de stack inteira, e não há
motivo: os apps são Electron/Vue e o BRUTAL é fundação para quem escreve motor em C#.

O valor está em três coisas baratas e úteis:

1. **B1 — política de contribuição assistida por IA** (`agents/`): é a cláusula que falta
   na Lia, escrita por quem recebe contribuições de agente em projeto real.
2. **B2/B4 — `LICENSES/` por pacote + `NOTICE.txt` curto**: complementa `LR-LIC-005`
   com a estrutura física dos avisos.
3. **B5 — medir Vulkan 1.3 na RX 580**: 10 minutos que fecham uma dúvida de hardware que
   hoje é `UNVERIFIED` para qualquer plano gráfico.

E um alerta que serve ao proprietário: **"open source" no README não substitui a licença**.
O BRUTAL é permissivo, permite uso comercial, mas **não é OSI** e exige logo no produto.
A Lia, ao escolher `DR-0001`, deve evitar a mesma ambiguidade: licença clara, sem
cláusula de branding, ou o README não pode dizer "open source" sem qualificar.

## 18. Próximos passos

| # | Ação | Dono | Gate |
|---|---|---|---|
| 1 | Adotar a cláusula B1 em `agents/` (política de contribuição assistida por IA) | Lia-Research | nenhum |
| 2 | Acrescentar B2/B4 ao `LR-LIC-005` (estrutura de `LICENSES/` por pacote) | Lia-Research | `DR-0001` |
| 3 | Rodar `vulkaninfo` na RX 580 e registrar em `LR-HW-001` | Model Lab | acesso à máquina |
| 4 | Se um app Lia precisar de runtime nativo 3D, comparar BRUTAL com alternativas antes de decidir | Studio | — |
| 5 | Revisar em 2027-02-17 (licença pode ser submetida à OSI) | Lia-Research | — |
