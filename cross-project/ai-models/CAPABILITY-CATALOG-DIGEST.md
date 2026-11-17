# Catálogo de capacidades e modelos — digest

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-004` |
| Categoria | models |
| Projetos | Lia-Project, Lia Model Lab |
| Fontes | `Lia-Project@005a324:docs/research/lia-capability-catalog/` (8 documentos, 121 KB total) |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | **Alta** para a estrutura; **nula** para desempenho (0 validados) |

## 1. Os oito documentos

| # | Documento | Bytes | Papel |
|---|---|---:|---|
| 01 | `01-ESTADO-DA-ARQUITETURA.md` | 6,2 KB | o que já existe no código |
| 02 | `02-CATALOGO-MESTRE.md` | 30 KB | modelos, pesos, runtimes, providers |
| 03 | `03-ESQUEMA-E-DADOS.md` | 21 KB | esquema do catálogo selecionável |
| 04 | `04-MATRIZES-E-PRIORIDADES.md` | 13 KB | compatibilidade e prioridade |
| 05 | `05-PLANO-DE-TESTES-E-RISCOS.md` | 12 KB | testes, segurança, licenças, lacunas |
| 06 | `06-ERRATA-E-REVISAO.md` | 12 KB | correções ponto a ponto |
| 07 | `07-CATALOGO-ESTRUTURADO.md` | 8,4 KB | registros rastreáveis e o que falta |
| 08 | `08-BANCADA-DE-MEDICAO.md` | 11 KB | como validar sem baixar 175 modelos |

## 2. O número que define o estado

| Métrica | Valor |
|---|---:|
| Registros catalogados | **44** |
| Itens descobertos e não catalogados | ~**131** |
| **Validados em hardware real** | **0** |

Este é o achado mais consequente do corpus interno: existe um catálogo formal, com
esquema e plano de testes, e **nenhum modelo foi medido**. Toda decisão de "melhor
modelo" no ecossistema é, hoje, baseada em ficha técnica de terceiro → `REPORTED`.

## 3. O que já está resolvido e deve ser reutilizado

- **Esquema de dados** (doc 03): base para o catálogo selecionável do produto.
- **Bancada de medição** (doc 08): método para validar sem baixar tudo — a peça que
  falta para transformar 44 em 0→N validados.
- **Errata** (doc 06): raro e valioso; mostra correção de erros anteriores em vez de
  reescrever o passado.

## 4. Encaminhamento

`RESEARCH-ROADMAP.md` item M-2: executar a bancada em 3 modelos (LFM3-1.7B,
Qwen pequeno, um embedding) e publicar os primeiros resultados `CONFIRMED`.
