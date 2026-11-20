# Ferramentas de produção: do blockout à exportação

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-008` |
| Categoria | forge |
| Projetos | Lia Forge 2.0 |
| Fontes | `gh api` (licença, atividade, releases) e arquivos de licença lidos em 2026-11-20: Blender (`COPYING`), MPFB2 (`LICENSE.md`), Instant Meshes (`LICENSE.txt`), ArmorPaint (`license.md`); glTF 2.0 (Khronos) |
| Data | 2026-11-20 |
| Status | CURRENT |
| Confiança | Média-alta em licença das ferramentas abertas; **baixa** em ferramentas comerciais não verificadas |
| Natureza | pesquisa e documentação; não instala nada, não autoriza integração |

---

## 1. O mapa do processo

```
1 blockout → 2 modelagem/escultura → 3 retopologia → 4 UV → 5 texturização
→ 6 cabelo → 7 roupas → 8 rigging → 9 skinning/pesos → 10 blendshapes
→ 11 animação → 12 otimização (LOD) → 13 exportação GLB/glTF
```

Para cada etapa, três perguntas: **a IA ajuda de verdade?**, **qual ferramenta aberta cobre?**,
**o que exige humano?**

## 2. Ferramentas abertas — fichas verificadas

| Ferramenta | Papel | Licença (lida) | Atividade | Observação |
|---|---|---|---|---|
| **Blender** | DCC central: modelagem, escultura, retopo, UV, rig, animação, exportação | **GPL-2.0-or-later** (texto: "Blender uses the GNU General Public License… not available under other licenses") | 22,2k★, ativo (2026-11-20) | GPL vale para o programa e para scripts que rodam **dentro** dele; chamar `blender --background --python` como processo externo mantém separação — mesma análise de `LR-FORGE-005` |
| **MPFB2** (MakeHuman Plugin for Blender) | base humana paramétrica com rig | licença própria (código + assets + cláusula sobre **saída**) | 718★, `v2.0.18` (2026-10-11) | resolve "humano base" sem IA; a cláusula de saída precisa ser lida antes de uso comercial |
| **Instant Meshes** | retopologia automática (campo de orientação) | **BSD-3-clause** (texto lido) | 6,3k★, **última atividade 2022-01-03** | ferramenta pontual, não biblioteca de produto; parada |
| **xatlas** | desempacotamento de UV | **MIT** | 2,6k★, 2024-06-16 | determinístico, ótimo para "UV sem sobreposição" automático |
| **Material Maker** | textura procedural por nós | **MIT** | 6,3k★, release `1.8` (2026-10-25) | gera PBR sem nuvem; alternativa aberta a Substance |
| **ArmorPaint** | pintura 3D | **zlib/libpng** (texto lido) | 5,5k★, release `26.11` (2026-11-18) | leve; bom para pintar sobre malha final |
| **Godot** | engine de destino (importação GLB) | **MIT** | 120,5k★, `4.7.2-stable` | valida o caminho de exportação, não a produção |
| **kimodo** (nv-tlabs) | geração de movimento | Apache-2.0 | 4,3k★, 2026-10-15 | relevante para animação, **não avaliado tecnicamente** |

### 2.1. O caso GPL, dito sem rodeio

Blender é GPL-2.0+. Duas consequências distintas, frequentemente confundidas:

| Situação | Efeito |
|---|---|
| Add-on/script que roda **dentro** do Blender e é distribuído | precisa ser compatível com GPL |
| Processo externo que chama `blender --background` e troca arquivos | separação preservada (o Blender é ferramenta) |
| Asset gerado no Blender (malha, textura) | não é obra derivada do programa |

Isso é a leitura que o próprio repo já registra em `LR-FORGE-005`; repito aqui porque qualquer
pipeline de personagem passa por essa decisão.

## 3. Ferramentas comerciais — o que **não** verifiquei

| Ferramenta | Papel | Situação nesta rodada |
|---|---|---|
| Auto-Rig Pro | rigging humanoide em Blender | licença e preço **não verificados** |
| QuadRemesher | retopologia automática | licença e preço **não verificados** |
| UVPackmaster | empacotamento de UV | **não verificado** |
| Mixamo (Adobe) | auto-rig + biblioteca de animação | termos de uso **não verificados**; exige conta |
| AccuRIG (Reallusion) | auto-rig | **não verificado** |
| MetaHuman (Epic) | humano de alta fidelidade | EULA **não verificado**; ecossistema Unreal |
| Substance / Marvelous Designer | textura e roupa | **não verificado** |

Registro explícito: estas linhas não são recomendação nem rejeição. São **lacunas**. Uma
pesquisa de produção que as ignore fica incompleta; uma que as preencha por suposição fica
errada.

## 4. Onde a IA ajuda — e onde atrapalha

| Etapa | IA ajuda? | Como | Risco |
|---|---|---|---|
| 1 Blockout | pouco | gerar proporções de referência | IA "resolve" proporção errada com confiança |
| 2 Modelagem/escultura | **sim** (image-to-3D como base) | base para esculpir por cima | topologia inutilizável |
| 3 Retopologia | **sim** (remesh automático) | Instant Meshes/QuadRemesher | loops ruins em articulação |
| 4 UV | **sim** | xatlas | costura feia, mas funcional |
| 5 Textura | **sim** | geração/projeção de textura | seams, UV stretching |
| 6 Cabelo | parcial | card-based gerado | malha de cabelo é arte, não geração |
| 7 Roupas | **não** (hoje) | simulação no DCC | IA não costura roupa peça a peça |
| 8–9 Rigging/skinning | parcial | auto-rig | pesos em ombro/quadril exigem correção |
| 10 Blendshapes | **não** | — | é modelagem de expressão |
| 11 Animação | parcial | geração de movimento (kimodo) | retarget e estilo |
| 12 Otimização | **sim** | decimate/LOD | perda de silhueta se mal configurado |
| 13 Exportação | **sim** | validador glTF | nenhum |

### 4.1. Conclusão da tabela

A IA cobre bem **entrada** (conceito, base, textura) e **saída** (otimização, exportação). O
meio — topologia, roupa, deformação — continua humano. É por isso que o pipeline 3 proposto
gasta a maior parte do tempo depois do modelo gerado.

## 5. Exportação: o que o Forge precisa validar

| Item | Verificação | Ferramenta |
|---|---|---|
| GLB válido | validador de glTF 2.0 | Khronos glTF-Validator |
| Materiais PBR exportados | presença de `pbrMetallicRoughness` | inspeção do GLB |
| Esqueleto e skin | `skins`, `joints`, pesos normalizados | inspeção do GLB |
| Escala/origem | altura, pés no chão | script |
| Animações embutidas | clipes nomeados | inspeção do GLB |
| Tamanho do arquivo | MB por personagem | script |

O formato é o ponto onde "pronto para jogo" deixa de ser opinião: ou o GLB passa, ou não passa.

## 6. Recomendação de stack (para avaliação, não adoção)

| Camada | Aberta | Comercial (a verificar) |
|---|---|---|
| DCC | Blender | — |
| Base humana | MPFB2 | MetaHuman |
| Retopo | Instant Meshes (pontual) | QuadRemesher |
| UV | xatlas + UV do Blender | UVPackmaster |
| Textura | Material Maker + ArmorPaint | Substance |
| Roupa | simulação do Blender | Marvelous Designer |
| Rig | Rigify (embutido) | Auto-Rig Pro, AccuRIG |
| Animação | kimodo (a avaliar) | Mixamo (biblioteca) |
| Engine | Godot | Unity/Unreal |

## 7. Não validado

- Nenhuma dessas ferramentas foi executada nesta sessão (não há Blender no sandbox).
- Licença de MPFB2 quanto à **saída** comercial: li que existe cláusula, não a interpretei.
- Termos de Mixamo e MetaHuman.
- Qualidade de retopo do Instant Meshes em personagem (é conhecida por ser boa em objeto).
- Se `kimodo` roda sem CUDA.

Voltar: `CHARACTER-2D-TO-3D-PIPELINES.md` · `CHARACTER-CREATION-RESEARCH.md`
