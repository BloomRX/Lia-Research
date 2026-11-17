# LFM3 — avaliação combinada (Lia-Project + Lia Model Lab)

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-003` |
| Categoria | models |
| Projetos | Lia-Project, Lia Model Lab |
| Fontes | `Lia-Project@005a324:docs/research/LIA-LFM3-EVALUATION.md` (17,5 KB); `Lia-Model-Lab@3ec4313:docs/17-LFM3-RESEARCH.md` (22 KB) |
| Data | 2026-11-17 |
| Status | **CONFLICTING de método** (duas avaliações, critérios diferentes) |
| Confiança | Média — documental, sem execução |

## 1. Duas avaliações, dois projetos

| Projeto | Documento | Data | Foco |
|---|---|---|---|
| Lia-Project | `LIA-LFM3-EVALUATION.md` | 14/11/2026 | adequação a produto (texto, áudio, VO, VL) |
| Lia Model Lab | `17-LFM3-RESEARCH.md` | 02/11/2026 | contrato de arquitetura e decisão de modelo |

As duas chegam a conclusões compatíveis, mas **não idênticas**, e nenhuma das duas cita
a outra. Isso é `CONFLICTING de método`, não de conclusão: mesmo objeto, critérios
distintos, nenhuma reconciliação.

## 2. Conclusões convergentes (preservadas)

1. **LFM3-1.7B** é o melhor primeiro candidato a texto local (GGUF Q4, llama.cpp).
2. **LFM3-Audio-2B** é candidato a áudio, mas *voice chat* e *live ASR* são
   **inglês-only** na ficha consultada → PT-BR não provado (`UNVERIFIED`).
3. **LFM3-Omni** não substitui benchmark modular; não carregar por padrão.
4. **Licença LFM Open** tem limite de receita — precisa leitura caso a caso, por modelo.
5. Nada foi medido na RX 580 (`BLOCKED`).

## 3. Encaminhamento

A reconciliação formal é decisão dos dois projetos, não desta base. Registrado em
`RESEARCH-ROADMAP.md` (item M-1): **uma** avaliação canônica de LFM3, com critérios
declarados, citada por ambos.
