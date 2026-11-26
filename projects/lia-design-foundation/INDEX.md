# Índice — Lia Design Foundation

---

> **Estado deste índice (2026-11-26).** É o primeiro documento da pasta, criado pela triagem dirigida do
> PerfectVector. Este índice **aponta**: o achado mora em `repositories/perfectvector/REPORT.md`
> (`LR-VEC-001`). Nada aqui é decisão de produto, e nada aqui foi executado contra serviço algum.

## 1. Pesquisa consolidada no Lia-Research

| ID | Tema | Relatório principal | Origem |
|---|---|---|---|
| `LR-VEC-001` | Vetorização raster→SVG como serviço (API + MCP): contrato, limites, preço, retenção e a proibição de avaliar as saídas | `repositories/perfectvector/REPORT.md` | triagem dirigida pedida pelo dono (2026-11-26) |
| `LR-FORGE-024` | O que "não enviar nada para fora" quer dizer na prática: um conversor local que prova, por checagem estática, que não há código de rede | `repositories/animama-avatar-converter/REPORT.md` | leitura do `check.mjs` na rodada Animama |
| `LR-LIC-002` | Proveniência de ativo (E3): o que tem de viajar junto com um SVG que sai do estúdio | `cross-project/licensing/ASSET-PROVENANCE.md` | `docs/T11-E3-ASSET-PROVENANCE-AND-CONTENT-VALIDATION.md` |
| `LR-LIC-005` | Licenças prontas: o que é permitido colar, e o que é cláusula de serviço (não licença) | `cross-project/licensing/READY-TO-USE-LICENSES.md` | derivado de 59 relatórios |

## 2. O handoff, em sete regras

Regras de produção de ativos vetoriais que esta pesquisa sustenta. Nenhuma exige contratar um serviço.

| # | Regra | Por quê (fonte) |
|---|---|---|
| R1 | **O vetor oficial é a fonte. Nada de identidade — publicado ou não — vai a um serviço de vetorização.** Nem "só para testar", nem com chave de teste | `PerfectVector:docs/api/privacy.md` §3: revisão humana de conversões recentes por "a small number of authorized staff"; §6: 48 h de retenção; `/product-facts.md`: editor on-line retém ≈3 meses |
| R2 | Vetorização automática **só** em material sintético de teste, em máquina local | é o único caminho que não cria dívida de contrato e continua reproduzível; executado assim nesta rodada (`LR-VEC-001` §8) |
| R3 | Depois de qualquer auto-traçado, **verificar cor e traço antes de publicar**: comparar cada `fill` com a paleta, medir o peso de traço fino, e conferir `viewBox`, grupos e nomes | medido em VTracer 0.6.15: `#FFFFFF` do fundo virou `#FEFDFD` (512 px) e `#FCECE7` (64 px); a linha de 1 px `#111111` virou `#646464` (distância 143,8 em RGB); nenhum SVG saiu com `viewBox`, `<g>`, `<title>` ou `fill-rule` |
| R4 | **Nenhum ícone abaixo de 100 px por lado passa por serviço externo** — nem que ele aceitasse: os tamanhos que importam ficam fora da porta | `PerfectVector:docs/api/limits.md`: lado entre 100 e 4.096 px, `422 invalid_image` fora disso; o `BloomStudios-Branding-Review-TEMP` exporta `A1-Micro-Cor-16/24/32/64.png` |
| R5 | Se um dia for preciso avaliar um vetorizador de terceiro, **evaliar o de código aberto, localmente**, e não o serviço: medir entrada sintética, com parâmetros registrados, e guardar o roteiro | o §10 do Terms do fornecedor proíbe usar saída/preview/metadado em "evaluation, benchmarking, … or dataset construction" e em "develop, improve, or validate any system that competes with or replicates the Service" |
| R6 | Gradiente, transparência e traço capilar **não se vetorizam**: viram outra imagem. São redesenho manual | medido: gradiente de 2 cores → **1** path de 1 cor (`#81628C`), SVG de 340 B; o auto-traçado "limpou" o arquivo apagando a intenção |
| R7 | Toda saída de terceiros entra no inventário de licença **como processo**, com o que ela é (auto-traçado) e não como desenho autoral | `LR-LIC-002` (proveniência E3) + o padrão do Animama: um arquivo por ativo, com licença e revisão registradas |

## 3. Precedentes medidos fora do PerfectVector

| Fato | Como foi medido (2026-11-26) | O que significa para a marca |
|---|---|---|
| O workspace de identidade em uso tem **23 `.svg`**, **95** entradas, `main` @ `350891e0b8e2d7611ccd3bd0e556c8be2996254b` (2026-11-18) e **nenhum `LICENSE`** | `gh api repos/…/git/trees/HEAD?recursive=1` + `gh api repos/…/license` (404) | a cadeia de ativos da Lia está **sem licença declarada** — isso é dívida própria, anterior e independente de qualquer serviço externo; resolver é mais útil do que contratar vetorizador |
| `CODEX_HANDOFF.md` do mesmo repositório pede "Avaliar silhueta isolada, monocromática e legibilidade em 32 × 32 px" e lista `Exports/` + `Source/…/PNG/*-16/-24/-32/-64` | arquivo lido pela API | o critério de qualidade do projeto é **legibilidade em tamanho pequeno**, exatamente onde a API de vetorização não aceita entrar (piso de 100 px) e onde o auto-traçado mais deforma (R3, R4) |
| O próprio fornecedor de vetorização admite que não manteve benchmark pareado de fidelidade em suas páginas comparativas | `/blog/best-ai-vectorizers-2026`: "We did not complete a retained paired-output benchmark" | não existe "número do fornecedor" para confiar; a alternativa é medida local, e ela é barata (0,001–0,023 s por arquivo) |

## 4. Condições para qualquer serviço futuro (a lista que um "sim" teria de cumprir)

Se um dia a produção de ativos contratar vetorização externa, a lista de gates é a de `LR-VEC-001` §10,
aqui resumida na ordem em que cada item mata a proposta:

1. consentimento **escrito** do fornecedor para o modelo de uso (o §9 dos API Terms cobre oferecer o
   recurso aos nossos usuários; nada cobre usar as saídas para avaliar, treinar ou comparar);
2. canal **server-side** com chave nossa, nunca do usuário, e retransmissão de bytes com cópia
   imediata do SVG no projeto (o resultado do fornecedor morre em 24 h);
3. saída nos formatos que a marca usa — SVG **e** PNG/ICO **e** PDF vetorial (a API devolve só SVG);
4. nenhum piso de dimensão que exclude 16–64 px;
5. parâmetros expostos (suavização, cantos, número de cores, piso de mancha) — sem eles, o auto-traçado
   não é ajustável ao traço da Lia;
6. sem revisão humana dos envios e sem retenção após a entrega;
7. preço com aviso prévio e reembolso do crédito não gasto.

Nenhum dos objetos lidos nesta rodada passa nos sete. Os itens 4 e 5 são estruturais: não são
configuração que falte hoje, são o desenho do produto (o site aceita 17 formatos e entrega PDF/EPS/DXF/AI;
a porta programática aceita 3 formatos e devolve 1 tipo de arquivo).

## 5. Lacunas

| Lacuna | Situação |
|---|---|
| Fidelidade relativa entre serviços pagos e os vetores abertos | **NÃO MENSURÁVEL sem consentimento escrito** — o §10 do Terms do fornecedor proíbe avaliação/benchmark com suas saídas; registrado em `RESEARCH-INDEX.md` §6 |
| Retenção do editor on-line e da conta (≈3 meses / ≈30 dias) | **REPORTED** — está em `/product-facts.md` e `/docs/mcp.md`, não conferido na Privacy Policy do site (documento seguinte na fila) |
| Licença dos 23 `.svg` do workspace de identidade | **ABSENTE** no repositório (404 na API de licença); é pergunta de governança do produto, não desta base |
| Medição da alternativa aberta em escala real (VTracer + Inkscape 1.4.4 + Potrace 1.16 sobre os ativos da Lia, tudo local) | **PARCIAL** — 4 casos sintéticos medidos aqui; os binários `inkscape`/`potrace`/`autotrace`/`vtracer` não existem neste sandbox, e nenhuma imagem real da marca foi processada |
