# Proveniência de assets — digest

| Campo | Valor |
|---|---|
| ID | `LR-LIC-002` |
| Categoria | licensing |
| Projetos | Lia Forge (primário), Lia Studio |
| Fontes | `Lia-Forge@…:docs/T11-E3-ASSET-PROVENANCE-AND-CONTENT-VALIDATION.md` (6,3 KB), `docs/auditoria-blender-local/LICENCAS-E-DEPENDENCIAS.md` (5 KB), `Lia-Project:docs/licenses/THIRD-PARTY-NOTICES.md`, `Lia-Studio:docs/licenses/*` |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Alta (é o único documento do ecossistema sobre proveniência de conteúdo) |

## 1. O problema

Licença de código ≠ licença de asset. Um modelo 3D, textura, HDRI, fonte, som ou
animação gerada por IA carrega sua própria licença, frequentemente com restrições de
uso comercial, proibição de redistribuição ou exigência de atribuição.

O Forge produz assets para jogos — ou seja, produz **conteúdo distribuível**.

## 2. O que o documento E3 estabelece

- proveniência do asset no primeiro render E3;
- proposta de validação de conteúdo;
- necessidade de rastrear origem (humano, IA, terceiro) por asset.

## 3. Camadas a registrar por asset (proposta desta base)

| Camada | Pergunta |
|---|---|
| Origem | criado, comprado, baixado, gerado por IA? |
| Ferramenta | qual modelo/pipeline (e qual licença de uso do modelo)? |
| Licença do asset | qual, onde está o texto? |
| Direito de redistribuição | pode ir dentro de um jogo do usuário? |
| Atribuição exigida | onde e como? |
| Restrição de uso comercial | sim/não, e limite? |

## 4. Casos reais já mapeados no ecossistema

| Item | Licença | Risco |
|---|---|---|
| Fonte da galeria do pixelfx | fora da MIT | não usar sem ler `gallery/fonts/NOTICE.md` |
| `img2threejs` (dentro do mr-mak-workspace) | Apache-2.0 lida na origem | aviso + indicar alterações; **`NOTICE` não se aplica** — a árvore do upstream só tem `LICENSE` (medido 2026-11-22, `LR-STUDIO-012` §13) |
| ZIP de 9,9 MB de terceiros no Lia-Studio | MIT (identificado por reconstrução: pacote das tags v0.4.14→v0.5.0) | falta registrar tag + hash no aviso do Studio (`DR-0004`) |
| Skills AIRI vendorizadas (29) | a verificar | `RESEARCH_ONLY` até auditoria |
| Fontes OFL em ManimGX/Meldwork | OFL-1.1 | embutir ok; vender a fonte isolada, não |

## 5. Lacuna

Não existe, em nenhum dos cinco projetos, um **registro de proveniência de asset**
executável. O documento E3 propõe; nada implementa. Isso é aceitável — implementar é
decisão do Forge — mas precisa estar visível.

Ver `RESEARCH-ROADMAP.md` item L-2.
