# Consumo de recursos em desktop sempre ativo

| Campo | Valor |
|---|---|
| ID | `LR-HW-002` |
| Categoria | hardware |
| Projetos | Lia-Project (primário), todos |
| Fontes | `Lia-Project@005a324:docs/research/2026-11-14-runtime-resource-research.md` (31 KB), `Lia-Project@005a324:tools/desktop-benchmark/README.md` (10 KB), `Lia-Project@005a324:tools/agents-docs/README.md` |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | **Média** — pesquisa documental com classificação `REFERENCE_ONLY`/`ADAPT` no original |

## 1. Pergunta

Quanto um assistente sempre ativo pode consumir sem degradar jogos e trabalho na mesma
máquina (16 GB RAM, RX 580)?

## 2. Conclusões preservadas

1. O custo não é só do modelo: inclui Stage (renderer), áudio, STT/VAD e o próprio
   app Electron. Medir só o modelo subestima o consumo.
2. Existe bancada de medição no projeto (`tools/desktop-benchmark/`) para comparar
   presença de desktop durante jogo — instrumento correto, resultado não consolidado aqui.
3. Prioridade de otimização: evitar trabalho em idle > reduzir pico > reduzir média.
4. Modelos "sempre carregados" competem com o jogo pela VRAM/banda; carregar sob demanda
   é preferível a manter residente.

## 3. Referências de método externas (novo)

| Fonte | Contribuição |
|---|---|
| OpenJarvis | energia, FLOPs e custo em dólar como métricas de primeira classe |
| SculptForge | benchmark pack com hardware declarado e resultados da comunidade |
| ManimGX | fixtures com hash para verificação reprodutível |

## 4. Lacuna

| Lacuna | Status |
|---|---|
| Medição própria em idle e durante jogo | `BLOCKED` — exige execução na máquina do usuário |
| Comparação de 3 configurações de runtime | `NOT RUN` |

Ver `RESEARCH-ROADMAP.md` item H-2.
