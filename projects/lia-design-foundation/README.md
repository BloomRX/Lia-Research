# Lia Design Foundation — handoffs de pesquisa

| Campo | Valor |
|---|---|
| Data deste índice | 2026-11-26 |
| Origem | ordem de serviço do proprietário (triagem dirigida do PerfectVector) |
| Estado do projeto nesta base | **sem dossiê** — `projects/lia-design-foundation/` foi criado nesta rodada como pasta de handoff; não existe inventário, ROADMAP próprio nem relatório de estado |
| Repositório | nenhum `BloomRX/Lia-Design-Foundation` localizado (HTTP 404 na API em 2026-11-26); o único material de identidade visível do ecossistema está em `BloomRX/BloomStudios-Branding-Review-TEMP`, `main` @ `350891e0b8e2d7611ccd3bd0e556c8be2996254b` (2026-11-18T22:02:06Z), **95** entradas, **23** `.svg`, **7** `.md`, **sem `LICENSE`** (`gh api …/license` → 404) |

---

## Para que serve este índice

Guardar, aqui na Research, o que a pesquisa externa decide sobre produção de ativos vetoriais da marca —
para que o produto consulte um handoff em vez de reabrir a pesquisa. É o ponto de aterrissagem de
`LR-VEC-001` (`repositories/perfectvector/REPORT.md`) para a produção de ícones e ativos oficiais.

## Ponto da pesquisa

Um veredito só nesta data: **serviços externos de vetorização não entram no fluxo de ativos da Lia** —
nem o PerfectVector, nem nenhum dos serviços com que ele concorre. Três razões, cada uma independente das outras:

1. **Os ativos oficiais não vão para fora.** O aviso de privacidade da API admite revisão humana
   ("a small number of authorized staff review recent conversions in our internal, read-only dashboard")
   e hospedagem por até 48 h em pelo menos duas nuvens de terceiros; a política do site afirma ainda
   retenção de ≈3 meses no editor on-line. Material de identidade não publicado não entra nesse caminho.
2. **Não há como provar qualidade sem violar o contrato.** O §10 do Terms do fornecedor proíbe usar
   entrada, saída, preview, thumbnail ou metadado para avaliação, benchmark, red-teaming, construção de
   dataset, ou para "develop, improve, or validate any system that competes with or replicates the
   Service (including image-vectorization)". "Testar se é melhor para a Lia" é exatamente o ato proibido.
3. **O que a API entrega não é o que a marca precisa.** A API entrega **só SVG**, com 1 imagem por
   pedido, 1 conversão simultânea por conta, sem nenhum parâmetro, e recusa lado menor que **100 px**.
   O repositório de identidade em uso exporta `A1-Micro-Cor-16.png`, `-24`, `-32`, `-64` — ou seja,
   **os tamanhos onde um ícone é julgado são justamente os que a API não aceita**.

## O que este índice **não** guarda

Nenhum desenho, nenhuma decisão de marca, nenhum arquivo-mestre, nada que substitua o editor de desenho e a aprovação humana do produto.
Guardamos pesquisa e condição de uso: o que a base sabe, com fonte, e o que está bloqueado por contrato.
Medição de desempenho humano, aprovação de identidade e escolha de ferramenta continuam no produto.

## Regras de atualização

1. Um handoff novo entra aqui **só** quando existe relatório com ID próprio em `repositories/*/REPORT.md`
   ou digest em `cross-project/` — a linha cita o documento, nunca reescreve o achado.
2. Esta pasta é **handoff**, não dossiê: não cria estado de produto, não promete ROADMAP, e enquanto o
   repositório do produto não for legível por esta sessão, nenhuma linha sua dirá "o projeto faz X".
3. Nenhum ativo oficial (SVG, PNG de prancha, wordmark, ícone de app, material não anunciado) é enviado
   a serviço externo de vetorização, avaliação ou conversão — sem exceção por conveniência.
4. Vetorização automática é permitida **apenas** em material sintético de teste, medido localmente
   (VTracer 0.6.15, MIT — superfície e desvios em `LR-VEC-001` §8); qualquer cor de saída volta para
   verificação manual contra a paleta oficial antes de existir como artefato.

## Índice de arquivos

| Arquivo | Conteúdo |
|---|---|
| `README.md` | este documento — cabeçalho, estado do handoff e as quatro regras |
| `INDEX.md` | handoff completo da rodada 2026-11-26 (regras de vetorização, precedentes medidos, condições para qualquer serviço futuro) |
