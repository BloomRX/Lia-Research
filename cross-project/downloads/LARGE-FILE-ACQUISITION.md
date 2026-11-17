# Aquisição de arquivos grandes

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-006` |
| Categoria | downloads |
| Projetos | Lia Forge, Lia Model Lab, Lia Agent Hub |
| Fontes | `repositories/misterdownloadmanager/REPORT.md` + observação interna: nenhum projeto Lia tem solução |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Alta para o problema; Média para a solução |

## 1. O problema real

| Necessidade | Tamanho típico | Hoje |
|---|---|---|
| Pesos GGUF (LFM3-1.7B Q4, Qwen pequeno) | 1–4 GB | download manual |
| Pesos maiores / vision / audio | 4–16 GB | download manual |
| Assets de jogo (texturas, HDRI, packs) | 100 MB–5 GB | download manual |
| Modelos 3D / vídeos | GB | download manual |

Nenhum dos cinco projetos tem: retomada, verificação de integridade, fila, quota,
nem UI de progresso unificada.

## 2. Requisitos mínimos (propostos)

| # | Requisito | Por quê |
|---|---|---|
| D1 | retomada de download | rede instável, arquivos de GB |
| D2 | verificação por hash (SHA-256) | pesos corrompidos falham de forma obscura |
| D3 | fila com prioridade e pausa | usuário joga enquanto baixa |
| D4 | quota de disco e de banda | 16 GB de RAM e disco limitado |
| D5 | origem declarada + licença do arquivo | pesos têm licença |
| D6 | log de aquisição | proveniência do que entrou no app |

## 3. Solução candidata

**Mister Download Manager como processo externo via MCP** (`LR-FORGE-001`), com os
gates:

1. GPL-3.0 → **nunca** incorporar código; só processo separado (exige parecer);
2. quota e allowlist de domínio implementadas na Lia, não nele;
3. verificação de hash feita pela Lia após o download (não confiar no gerenciador);
4. projeto imaturo (3 semanas) → pin e fallback manual.

Alternativa sem terceiros: implementar D1–D6 sobre o cliente HTTP existente. Mais
trabalho, zero risco de licença.

## 4. Recomendação de pesquisa

`PENDENTE` — decide-se após o parecer de licença (`DR-0013` proposto). O que **não** é
opcional é D2 (hash) e D5 (licença): sem isso, qualquer download de peso é
irreprodutível e sem proveniência.
