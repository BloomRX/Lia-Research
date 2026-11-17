# SculptForge — escultura 3D open source em C++ (GPL-3.0)

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-002` |
| Categoria | forge |
| Projetos beneficiados | Lia Forge (referência), Lia Studio (referência de integração 3D) |
| Fontes | `islandmed/SculptForge@363e2b86cf8da3834206a9465a31560a8ea7e583:README.md`, tree, `LICENSE`, releases |
| Versão/commit | `363e2b8` (2026-11-17), release `v0.13.6` |
| Data | 2026-11-17 |
| Próxima revisão | 2027-02-17 |
| Status | CURRENT |
| Recomendação | **REFERÊNCIA** |
| Licença | GPL-3.0-or-later (`CONFIRMED`) |
| Confiança | Alta para licença/estrutura; Baixa para desempenho |

---

## 1. Identificação

- **Nome:** SculptForge
- **URL:** https://github.com/islandmed/SculptForge · site islandmed.github.io/SculptForge
- **Organização:** `islandmed`
- **Licença:** GPL-3.0-or-later (badge do README e `LICENSE` — `CONFIRMED`)
- **Commit:** `363e2b8` (2026-11-17T14:01:35Z) · release `v0.13.6`
- **Métricas:** ★722 · 90 forks · 21 issues · criado 2026-10-21 · **2.497 arquivos** · 526 `.cpp` + 291 `.h` · 695 arquivos em `tests/` · 247 em `docs/` · 187 em `tools/` · 51 em `bench/` · 450 em `website/` · 26 em `integrations/` · 26 em `third_party/` · 21 workflows · 143 `.md`

## 2. Resumo executivo

SculptForge é um aplicativo de escultura 3D em C++ (Dear ImGui + OpenGL) para
Windows/macOS/Linux, com malhas densas, remeshing, pintura, IA embutida
(image/text-to-3D), "Send to Unreal", LODs game-ready, Gaussian splats, OpenUSD,
add-on para Blender, integração MCP e uma página de benchmarks com pack de cenas e
resultados da comunidade.

Para o Lia Forge o valor é de **referência de produto e de disciplina de medição**:
existe um `bench/` com 51 arquivos e uma política pública de benchmark reproduzível
(exatamente o que falta no ecossistema Lia, onde 44 modelos estão catalogados e 0
validados). A licença GPL-3.0 impede qualquer incorporação de código ao Forge
proprietário; o uso como aplicativo externo é possível.

## 3. O que resolve

| Problema | Abordagem |
|---|---|
| Escultura 3D acessível e gratuita | app standalone multiplataforma |
| Malha pesada travando a UI | trabalho em background por gesto (`REPORTED` no changelog) |
| Levar escultura para o pipeline de jogo | "Send to Unreal", LODs game-ready, glTF/FBX |
| Medir hardware de forma comparável | benchmark pack + tabela pública de resultados |
| Integrar com agentes | tópico `mcp` + `integrations/` |

## 4. Arquitetura

```text
src/ (628)            núcleo C++ (dear-imgui, opengl)
third_party/ (26)     dependências vendorizadas
tools/ (187)          CLIs, conversores, benchmark pack
integrations/ (26)    Blender add-on, Unreal, MCP
bench/ (51)           cenas e harness de medição
docs/ (247)           documentação + guia
website/ (450)        site com resultados de benchmark
android/ (11)         experimento mobile
tests/ (695)          suíte extensa
```

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| Escultura em malha densa | estável (0.13.x) | `REPORTED` README |
| Remeshing, pintura | estável | `REPORTED` |
| IA image/text-to-3D embutida | `REPORTED` | README |
| Export glTF/FBX/OpenUSD | estável | `REPORTED` + topics |
| Gaussian splats | `REPORTED` | README |
| Add-on Blender | existe | `integrations/` |
| Servidor/integração MCP | existe | topic `mcp` |
| Benchmark pack (`sculptforge --benchmark-pack`) | em release iminente | `CONFIRMED` (commit message) |

## 6. Dependências

- C++ toolchain, Dear ImGui, OpenGL, bibliotecas em `third_party/` (lista completa
  não inventariada — `UNVERIFIED` por item de licença).
- Python para scripts (119 `.py`).
- Modelos de IA locais/remotos para image-to-3D: licenças próprias, não avaliadas.

## 7. Requisitos de hardware e sistema

- Windows/macOS/Linux; GPU com OpenGL moderno.
- RX 580: OpenGL 4.6 é suportado pela arquitetura Polaris — **plausível**, não medido
  (`UNVERIFIED`).
- A página de benchmarks publica resultados por hardware da comunidade — método
  verificável, resultado alheio (`REPORTED`).

## 8. Segurança e privacidade

| Item | Rótulo | Nota |
|---|---|---|
| Integração MCP dá a agente controle de escultura/export | `OBSERVED` (topic) | superfície de risco em app de criação |
| image/text-to-3D pode enviar imagem a serviço | `UNVERIFIED` | verificar se é local ou remoto antes de usar |
| Dependências vendorizadas em `third_party/` | `OBSERVED` | auditoria de licença e CVE necessária |
| Telemetria | não identificada | `UNVERIFIED` |

## 9. Licença e proveniência

- **GPL-3.0-or-later** (`CONFIRMED`). Copyleft forte: incorporar código no Lia Forge
  contaminaria o produto. Obrigações: aviso, fonte, mesma licença.
- `third_party/` pode conter licenças distintas (não auditado — `UNVERIFIED`).
- Classe: `REFERENCE_ONLY`. Uso como app externo é aceitável; integração por
  arquivo/CLI também, com cautela jurídica.
- Marca: "SculptForge" não é licenciada pela GPL.

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Idade | ~4 semanas | muito jovem |
| Releases | 0.13.x, várias por semana | cadência altíssima |
| Testes | 695 arquivos | sério |
| CI | 21 workflows | forte |
| Documentação | 247 arquivos + site | acima da média |
| Issues | 21 | baixo |

Mesma ressalva do OpenIDEA: escopo enorme em pouco tempo exige cautela sobre
profundidade; aqui, porém, há benchmark público e suíte de testes, o que é sinal
qualitativo melhor.

## 11. Custos e limitações

- Gratuito. Custo de adoção: alto (C++ próprio; não é biblioteca).
- Limitações: pré-1.0; integração com Unreal/Blender pode exigir versões específicas
  (`UNVERIFIED`).

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? | Nota |
|---|---|---|
| Windows 11 | sim (`REPORTED`) | — |
| GPU AMD | provável (OpenGL) | não medido |
| Não incorporar GPL | só como app externo | — |
| Pipeline de asset do Forge | conceitualmente complementar | Blender continua central |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia Forge | referência de benchmark reproduzível e de fluxo escultura → engine |
| Lia Studio | referência de integração 3D em app de criação |

## 14. Oportunidades de reutilização

1. **Benchmark pack + tabela pública por hardware**: modelo direto para a bancada do
   Lia Model Lab (hoje inexistente).
2. **Blender add-on como integração oficial** em vez de fork: padrão para Forge.
3. **Documentar o "Send to engine"** como contrato explícito entre ferramentas.
4. **`third_party/` declarado** como diretório: facilita auditoria (ao contrário de
   dependência misturada em `src/`).

## 15. Riscos e incompatibilidades

| Risco | Severidade | Mitigação |
|---|---|---|
| GPL contaminar produto | alta | referência apenas |
| Projeto imaturo | média | não depender |
| IA embutida com egress de imagem | média | verificar antes de usar com dado real |
| `third_party/` sem auditoria | média | não copiar |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | GPL-3.0-or-later | CONFIRMED | `@363e2b8:LICENSE` + badge | 2026-11-17 |
| E2 | 2.497 arquivos, 695 testes, 21 workflows | CONFIRMED | tree (contagem) | 2026-11-17 |
| E3 | Benchmark pack + resultados públicos | CONFIRMED | commit message + `bench/`, `website/` | 2026-11-17 |
| E4 | Integração MCP | REPORTED | topic + `integrations/` | 2026-11-17 |
| E5 | Desempenho em RX 580 | UNVERIFIED | não executado | — |

## 17. Recomendação

**`REFERÊNCIA`** — copiar a disciplina de benchmark e o padrão de integração; não
adotar código nem dependência.

**Não autoriza:** incorporar código, redistribuir binário modificado, ou substituir o
pipeline Blender do Forge.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Propor formato de benchmark pack para a Lia (inspirado, não copiado) | Model-Lab | spec |
| 2 | Avaliar se escultura dedicada é necessária ao Forge (ou Blender basta) | Forge | decisão de produto |
| 3 | Revisar em 90 dias | Research | — |
