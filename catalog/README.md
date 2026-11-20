# Catálogo de tecnologias

| Campo | Valor |
|---|---|
| Papel | visão de máquina + porta de entrada do conhecimento catalogado |
| Fonte principal | `repositories/*/REPORT.md` (o catálogo é derivado) |
| Esquema | `catalog/CATALOG-SCHEMA.md` |
| Regeração | `python3 tools/build_catalog.py` |

Arquivos:

- `catalog.tsv` — uma linha por objeto, gerada a partir do cabeçalho dos relatórios.
- `INTAKE-2026-11-17.md` — triagem de 20 itens (identificados, **não** investigados).

> O catálogo registra **conhecimento e estado**. Não registra permissão de uso:
> ver `MISSION.md` §3 e `decisions/README.md`.
