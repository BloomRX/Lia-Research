# Blender e MCP — digest

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-005` |
| Categoria | forge |
| Projetos | Lia Forge, Lia Studio |
| Fontes | `Lia-Forge@…:docs/BLENDER-MCP-RESEARCH.md` (16 KB), `docs/ECOSYSTEM-RESEARCH-BLENDER-ADDONS.md` (45 KB), `docs/auditoria-blender-local/` (README + matriz de licenças) |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média |

## 1. O que existe na pesquisa interna

| Documento | Conteúdo |
|---|---|
| `BLENDER-MCP-RESEARCH.md` | automação, agentes e integração MCP com Blender |
| `ECOSYSTEM-RESEARCH-BLENDER-ADDONS.md` | auditoria revisada de add-ons (45 KB) |
| `auditoria-blender-local/LICENCAS-E-DEPENDENCIAS.md` | **matriz de licenças** de dependências Blender |
| `docs/3D-CHARACTER-PRODUCTION-PIPELINE.md`, `3D-RENDERING-TOOLS-RESEARCH.md` | produção e render |

## 2. Pontos de atenção de licença (GPL do Blender)

Blender é GPL-2.0+. Add-ons e scripts que rodam **dentro** do Blender herdam obrigações
compatíveis; chamar o Blender como **processo externo** (`blender --background
--python`) mantém separação. A matriz de licenças do próprio Forge já endereça parte
disto — é o único documento de licença de ferramenta no ecossistema.

## 3. Referência externa relevante

`SculptForge` (`LR-FORGE-002`) mantém add-on oficial para Blender e um diretório
`third_party/` declarado — padrão de organização que facilita auditoria de licença.

## 4. Lacuna

| Lacuna | Status |
|---|---|
| Teste de automação Blender headless no Windows do usuário | `NOT RUN` |
| Catálogo de add-ons com licença por item | parcial (45 KB, não estruturado) |
| Servidor MCP de Blender validado | `UNVERIFIED` |
