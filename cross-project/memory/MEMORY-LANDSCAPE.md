# Memória — panorama

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-007` |
| Categoria | agents |
| Projetos | Lia-Project, Lia Agent Hub |
| Fontes | `Lia-Project@005a324:docs/architecture/LIA-ARCHITECTURE.md` (25 KB, 2 versões), `Lia-AgentHub:docs/architecture/DATA-STORAGE-AND-PORTABILITY.md` (25 KB), `repositories/openjarvis/REPORT.md` |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média (documental; nenhuma medição de recall) |

## 1. Estado na Lia

Memória local existe (`REPORTED`), com autorização de tools; a arquitetura prevê
recuperação com atribuição de fonte. Não há métrica pública de recall.

## 2. Referência externa (OpenJarvis)

Cinco backends com contrato único: **SQLite/FTS5** (padrão zero-dependência), FAISS,
ColBERTv2, BM25, Hybrid (RRF). Pipeline: ingestão → chunking → embedding → injeção de
contexto com atribuição (`CONFIRMED` em `docs/architecture/overview.md`).

Lição: começar por **FTS5/lexical** e só adicionar embedding quando o recall lexical
falhar comprovadamente. O catálogo de modelos do Project recomenda o mesmo (embeddings
"only after current memory tests", classe B).

## 3. Regra de ouro

> Não adicionar banco vetorial antes de medir falha do lexical. Custo de embedding:
> modelo extra, RAM extra, latência por query — em uma máquina de 16 GB que também
> roda Stage e jogo.

## 4. Lacunas

| Lacuna | Status |
|---|---|
| Métrica de recall da memória atual | `NOT RUN` |
| Política de retenção de memória (quanto tempo, onde) | não documentada |
| Portabilidade/exportação de memória | documentada no Hub; não implementada |
| Memória compartilhada entre projetos | **não deve existir** por decisão de independência |
