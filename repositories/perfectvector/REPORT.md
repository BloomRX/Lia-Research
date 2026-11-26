# PerfectVector — API e MCP de vetorização raster→SVG: contrato técnico íntegro, termos que proíbem a avaliação, e uma porta de app distribuído que só existe no servidor

| Campo | Valor |
|---|---|
| ID | `LR-VEC-001` |
| Nome | `perfectvector.com` (Rastrix Inc.) — API REST `https://api.perfectvector.com/v1`, MCP `https://mcp.perfectvector.com/mcp` e Studio no navegador |
| Tipo | **serviço proprietário (SaaS)** com API em beta público e conector MCP oficial — não é repositório: não há código para clonar nem pacote para virar dependência |
| Licença | **sem licença de código** — o que rege é contrato: Terms of Service (`updated 2026-11-25`), API Terms **v1.1** (2026-11-09), MCP Terms **v1.3** (2026-11-05), API Privacy Notice **v1.1** (2026-11-03). O §11 do Terms concede licença **limitada e revogável de usar o serviço**; nenhum software é concedido |
| Categoria | design-assets (vetorização de ícones e ativos) + superfície de API/MCP para produto |
| Projetos beneficiados | Lia Forge, Lia Studio, Lia Design Foundation (produção de ativos) |
| Fonte oficial | https://perfectvector.com · /api · /mcp · /docs/api · /docs/mcp · /terms |
| Responsável | **Rastrix Inc., República da Coreia** — `contact@perfectvector.com`; pagamento por Lemon Squeezy (Stripe company) como Merchant of Record |
| Versão analisada | contrato de docs `docs/catalog.json` `version d708a720db3296a67c2f38099289a4abb1cc65c06827322b79c39e6125e79ccf`; API em beta aberto desde **2026-11-03**; `updated` dos documentos que li: **2026-11-03** (API Privacy Notice, `introduction`) a **2026-11-26** (API Terms) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | PARTIAL — o serviço não foi executado: nenhuma requisição autenticada à API e nenhuma conexão ao MCP (sem conta, sem chave, sem crédito). O que foi executado e medido aqui é a alternativa aberta, VTracer 0.6.15, em 4 casos sintéticos (§8) — tentativa com as dez colunas em `data/testing/test-log.tsv` (2026-11-26, nível 2). A leitura de página nunca conta como teste do objeto |
| Recomendação | **REFERENCE_ONLY** — não entra como integração nem dependência em nenhum dos três produtos; vale como referência de processo (Studio) e como lista de condições contratuais (§10) |
| Decisão de adoção | — nenhuma registrada (fora da autoridade desta base) |
| SHA completo | — não determinado (serviço: não existe commit único) |
| Proveniência do SHA | **INCOMPLETA_ORGANIZACAO** — a âncora equivalente é o hash do catálogo de docs acima, lido em 2026-11-26 |
| HEAD atual | — (serviço; o catálogo de docs tem `version` própria) |
| Upstream conferido | 2026-11-26 — serviço ativo, docs com `reviewed` 2026-11-26 (`api-terms`) e 2026-11-17 (`troubleshooting`) |
| Proveniência do conteúdo | **16 páginas do fornecedor** lidas na fonte, mais 1 página de terceiro: 14 em markdown/JSON oficial (`/llms.txt`, `/api.md`, `/mcp.md`, `/product-facts.md`, `/pricing.md`, `/pricing/api.md`, `/docs/api/{introduction,limits,errors,troubleshooting,agents,privacy,terms}.md`, `/docs/mcp/terms.md`, `/docs/catalog.json`) + `/terms` em HTML lido em 3 chunks (7 seções completas) + a listagem do conector em `mcpservers.org` (terceiro, só para presença). Sete páginas pedidas deram `Failed to fetch page`: `/docs/api/{file-types,polling,results,credits,quickstart}.md` e `/docs/mcp/{introduction,limits}.md` — o catálogo oficial as anuncia, e a informação delas não foi inferida
| Data | 2026-11-26 |
| Última verificação | 2026-11-26 |
| Confiança | **Alta** para o que está em página oficial (endpoint, limite, preço, cláusula, retenção); **nula** para qualidade relativa de vetorização — não medido, e medir está proibido pelo §10 do Terms do fornecedor |
| Próxima revisão | 2027-01-15 |

---

## 1. Identificação e fornecedor

Vetorizador raster→SVG operado pela Rastrix Inc. (Coreia do Sul), cobrado por **crédito por resultado entregue**, com dois canais automatizáveis — uma REST API em beta público desde 2026-11-03 e um servidor MCP que se conecta por OAuth a ChatGPT/Claude/Claude Code/Codex — mais um "Studio" no navegador que é editor, não exportador em lote.

O que motiva a triagem é a hipótese "a Lia não desenha vetores a partir de imagem; contratar isso custa menos do que fazer?". A resposta curta medida aqui: **o contrato técnico é bom, o contrato jurídico fecha exatamente as três coisas que a Lia precisaria** — embutir num app distribuído sem back-end próprio, medir a fidelidade antes de adotar, e mandar material oficial da marca para fora.

A face pública do serviço é auto-descrita em `/product-facts.md` (formatos de entrada do site = 17; saída = SVG, PDF, EPS, DXF, AI); **a API e o MCP aceitam menos que o site** — ver §2. Essa diferença entre "o que o marketing diz" e "o que a porta programática entrega" é o primeiro fato decisivo da rodada.

## 2. Funcionalidades e o contrato real da superfície programática

### 2.1 API (`https://api.perfectvector.com/v1`)

| Aspecto | Regra medida na documentação oficial |
|---|---|
| Endpoints | `POST /v1/vectorizations` (1 crédito **no sucesso**) · `GET /v1/vectorizations/{id}` · `GET …/result` · `GET …/results/{index}` · `DELETE /v1/vectorizations/{id}` · `GET /v1/account`. Todos os outros custam 0 créditos |
| **Não há listagem** | "There is no endpoint that lists your conversions. Keep the `id` of each conversion you create." — o índice das conversões é **nossa** obrigação, desde o primeiro dia |
| Entrada | **PNG, JPEG e WebP apenas**, verificados pelo conteúdo do arquivo (não pela extensão). 5 MiB = **5.242.880 bytes**; lado entre **100 e 4.096 px**; **uma moldura** — animadas recusadas. Pedido `multipart/form-data` com o campo `image` e, opcional, `options`; nenhum outro campo |
| Parâmetros | não há o que ajustar em v1: `options` que peça algo fora do v1 responde `400 invalid_request`; `max_variants: 1`; `GET /v1/account` devolve os limites correntes em `limits` |
| Formato de saída | **SVG e só SVG** (o site tem PDF/EPS/DXF/AI; a API, não) |
| Entrega | `Accept: image/svg+xml` devolve o SVG no próprio `201`; senão espera até **120 s** (`Prefer: wait=N`) ou `Prefer: respond-async` + polling `~2 s` |
| Retentativa | `Idempotency-Key` por 24 h; reuso com outra imagem = `409 idempotency_conflict`; replay **não cobra e não conta** como create |
| Validade do resultado | **24 h**. Depois: `410 result_expired` — "The SVG cannot be recovered; convert the image again if you need it" (e isso cobra de novo) |
| Erros | RFC 9457 `application/problem+json` com `code` estável (19 códigos), `request_id` em todo corpo e em `X-Request-ID`; **conversão que falha não é erro HTTP**: responde `201`/`200` com `"status": "failed"` e `credits_charged: 0` |
| Autenticação | Bearer com `pv_live_…` ou `pv_test_…`, **só** no header `Authorization`; chave nunca armazenada por inteiro (`keyed one-way hash`); até **10 chaves** por conta (live+testes somadas) |
| Teste grátis | `pv_test_` roda o pedido inteiro (chaves, arquivo, rate limits) e devolve um **SVG de amostra fixo**, sem cobrar e sem guardar o arquivo — fica só nome, tamanho, dimensões e fingerprint SHA-256 |
| **Sem CORS** | dito pela doc: "It sends no CORS headers, so browsers block calls from web pages, and an API key in a web page would be public." ⇒ o Studio **não pode** chamar a API do browser, e embutir chave em página é proibido na prática |
| Acesso ainda pode faltar | `403 access_not_granted` ("The key is valid, but the API is not open to this account yet") convive com "open to everyone" ⇒ o beta tem liberação por conta |

### 2.2 Limites de requisição (docs de 2026-11-10, iguais para toda conta)

| Limite | live | test | Ao atingir |
|---|---|---|---|
| Conversões criadas por minuto | 20 | 20 | `429 rate_limited` |
| Tentativas de `POST` por minuto (inclusive recusadas e replays) | ~40 | ~40 | `429 rate_limited` |
| Demais requisições por minuto | ~120 (rajada 30) | ~120 | `429 rate_limited` |
| **Conversões live simultâneas** | **1** | sem limite | `429 too_many_in_flight`, `Retry-After: 5` — o segundo pedido é **recusado, não enfileirado** |
| Chaves ativas | 10 (live+test) | — | `409` na página Developer API |

Limites são **por conta**, não por chave. Em capacidade máxima o pedido espera na fila do fornecedor **até 10 minutos** e então falha `timeout`, sem cobrança. Cabeçalhos `X-RateLimit-Limit/Remaining/Reset` e `Retry-After` existem de verdade (raro num serviço desse porte); `429`/`503` de borda vêm **sem** corpo `problem+json` — não são para parsear. Um aumento de limite se pede por e-mail.

### 2.3 MCP (`https://mcp.perfectvector.com/mcp`)

Streamable HTTP + **OAuth com Google** — sem chave de API. Cobra do **saldo do site** (não dos créditos de API): 1 crédito por SVG entregue, falhas grátis, e verificação de preço gratuita antes de converter, com o "Yes, always" salvo **na conta PerfectVector** e válido em todo assistente (MCP Terms §4). Arquivos: os mesmos PNG/JPEG/WebP ≤ 5 MB e lado 100–4.096 px, **sem nenhum parâmetro** ("using our standard conversion settings" — a correção é editar a imagem antes). Entrega: **link válido 24 h** que continua funcionando depois de desconectar o assistente (MCP Terms §9). Conexão expira 30 dias após o último uso e 90 dias após o login no máximo; desconexão é na página da conta.

O que o MCP **não** é: gerador de imagem a partir de texto; meio de comprar créditos; canal de lote. E tem proibições próprias (§6): não usá-lo fora do fluxo oficial, **não copiar/partilhar/reusar as credenciais que ele emite ao assistente**, **não usá-lo como serviço de conversão em lote**, não usá-lo para montar datasets, não contornar limites ou pausas, não tentar alcançar conversões de outra conta. O §5 transfere a você a responsabilidade por tudo que o assistente pedir em seu nome, inclusive o pedido automático. Simultaneidade no Connector: **1 pedido por conta** hoje.

## 3. Preço, créditos, limites e disponibilidade (tabelas lidas em 2026-11-26)

| Canal | O que se paga | Números exatos lidos |
|---|---|---|
| Site/Studio | assinatura ou pay-as-you-go | Free USD 0 (1 crédito) · Pro **USD 8/mês** com 20 créditos · Max **USD 20/mês** com 100 · pay-as-you-go a **USD 0,50 por download**; reembolso de 14 dias se nenhum crédito de assinatura foi gasto |
| API | **packs one-time, sem assinatura e sem recarga automática** | Starter 10 créditos: regular **USD 5,00**, na beta **USD 4,00** = **USD 0,40/conversão** · Bulk 100: **USD 20,00 → 16,00** = **USD 0,16** · Bulk 1.000: **USD 100,00 → 80,00** = **USD 0,08** · ≥10.000 créditos: e-mail para a venda. Máximo **10 packs por pedido**; validade **12 meses após a compra** |
| MCP | o saldo do site | 1 crédito por SVG entregue; nada é convertido nem cobrado antes do seu OK; pedido que expira sem OK (30 min) apaga a imagem sem cobrar |

Pontos que importam para decisão de produto, na ordem em que doem:

1. **Os dois bolsos são separados.** "API credits are separate from the credits you use on the website and in AI assistants, and the two never convert into each other. Website plans include no API credits." Quem assina o plano Max (USD 20/100 créditos) **não tem** um crédito de API.
2. **Preço da API pode mudar sem aviso.** O §4.2 dos API Terms isenta explicitamente a API da regra de 30 dias do §14 do Terms, e créditos já comprados **não** são reembolsados quando a API muda de preço. (Para o MCP, a regra de aviso do §14 continua valendo.)
3. **Sem overdraft.** `402 insufficient_credits` com `credits_required`/`credits_available` no corpo; e um segundo pedido enquanto um roda pode responder `402` só porque o saldo cobre o que já está em andamento.
4. **Cobrança não depende de você receber.** Os API Terms cobram a conversão mesmo se o seu cliente desistiu de esperar — por isso o `Idempotency-Key` deixa de ser higiene e passa a ser controle de custo, com `connect-timeout ≈ 10 s` e `total ≈ 150 s` (a receita está na própria página de troubleshooting do fornecedor).
5. **Sem SLA.** §13 do Terms: "best-effort", "We do not commit to a formal uptime SLA at current pricing", e "operational restrictions" podem impor limites ou desativar recursos **sem aviso prévio**. §8 dos MCP Terms: o conector pode ser mudado, limitado, suspenso ou descontinuado a qualquer momento e pode "limit who can connect".
6. Custo, em material sintético, para dimensionar (estimativa derivada da tabela, **não** medida): 1.000 conversões pela API na beta = **USD 80,00**; pelo pay-as-you-go do site = **USD 500,00**. Com `max_in_flight: 1` e 20 criações/min, o tempo de parede desses 1.000 arquivos não é paralelo por conta própria — a fila é uma por vez por conta.

## 4. Evidência primária lida

| # | Fonte (oficial, exceto onde dito) | O que sustenta |
|---|---|---|
| P1 | `https://perfectvector.com/llms.txt` | índice oficial de páginas `.md`/`.json`; confirma a intenção de ser lido por agentes e dá o mapa do que existe |
| P2 | `/api.md` | contrato de marketing técnico do produto: "From $0.08 per SVG · free test keys", exemplos cURL/Python/Node, FAQ com "browsers block", "Are API credits the same as website credits? No" |
| P3 | `/docs/api/introduction.md` (2026-11-04) | os 6 endpoints, `There is no endpoint that lists your conversions`, convenções (`object`, RFC 3339, `X-Request-ID`, `X-Credits-Charged`), **sem CORS** |
| P4 | `/docs/api/limits.md` (2026-11-10) | a tabela de 20/~40/~120 por minuto, **1 conversão simultânea**, 10 chaves, fila de 10 min, objeto `limits` do `GET /v1/account`, respostas de borda |
| P5 | `/docs/api/errors.md` (2026-11-10) | os 19 códigos, `410 result_expired`, `409 idempotency_conflict`, `503 api_paused`, `422 invalid_image` (100–4.096 px), falha = `201` com `status: failed` e `credits_charged: 0` |
| P6 | `/docs/api/troubleshooting.md` (2026-11-17) | política de retry recomendada pelo fornecedor: `--connect-timeout 10 --max-time 150 --retry 3 --retry-connrefused` com a **mesma** `Idempotency-Key`; `timeout` = nova chave |
| P7 | `/docs/api/privacy.md` v1.1 (2026-11-03) | 24 h de disponibilidade / 48 h para apagar; test key não guarda arquivo; **"no previews or thumbnails of API files"**; request records 90 dias **sem IP**; lista nominal de subcontratados; revisão humana por "a small number of authorized staff"; "never used to train AI models and never sold"; `DELETE` e revogação como escolha do usuário |
| P8 | `/docs/mcp/terms.md` v1.3 (2026-11-05) | OAuth Google e a conta cujo saldo é gasto; §4 cobrança por entrega + "Ask every time"; §5 sua responsabilidade pelo pedido do assistente; **§6 proibições do Connector**; §7 o provedor do assistente é independente; §8 sem SLA; §9 link de 24 h sobrevive à desconexão |
| P9 | `/mcp.md` | configuração por cliente, limites de arquivo, "standard settings" sem opções, verificação de preço grátis, imagens apagadas em ≈30 dias, verificado em Claude/ChatGPT/Claude Code/Codex (ChatGPT custom MCP só Business/Enterprise/Edu) |
| P10 | `/pricing.md` e `/pricing/api.md` | as duas tabelas de preço do §3, Lemon Squeezy/Stripe, reembolsos, "1 credit per delivered SVG", 12 meses de validade, 20% de desconto de beta |
| P11 | `/terms` (updated 2026-11-25) | §2 early access; §8.1 "We claim no ownership of your inputs or of the SVG outputs"; §8.2 sem moderação ativa; §8.3 proibição de revenda/sublicença/acesso automatizado a terceiros; §9 scraping; **§10 proibição de uso para IA/ML e para validar concorrente**; §11 licença limitada e revogável; §13 sem SLA e **sem garantia de qualidade do resultado**; §16 teto de responsabilidade = maior entre o pago em 12 meses e **USD 100**; §17 você indeniza inclusive por **outputs distribuídos**; §19–§20 lei da Coreia, foro em Seul, **prescrição de 1 ano** |
| P12 | `/docs/api/terms.md` v1.1 (2026-11-09/26) | §1 API e MCP são **oficial integration**: scripts e lote pago são permitidos; "What stays prohibited" mantém de pé dataset/sistemas concorrentes; §4 cobra mesmo sem espera; §4.2/§14 isenção de aviso de preço para a API; §7 direito de arrependimento de 14 dias; §8 revisão humana de conversões recentes; **§9 "You may offer features built on the API to your own users; this is our consent under §8.3"** com termos próprios e **"Do not give your API keys to your users"** |
| P13 | `/product-facts.md` | **REPORTED** como política do fornecedor (não é página de termos): 17 formatos no site, 5 MiB de orçamento preparado no navegador, "all vectors you export are yours to use, including for commercial work", DXF = contornos R12 fechados em milímetros (não toolpath), AI = PDF com extensão compatível, retenção do Studio ≈3 meses, "we never use your files for model training, sell them, or share them with third parties", política de preços v7 |
| P14 | `/docs/catalog.json` | a âncora de versão do contrato de docs (`schemaVersion 1`, `version d708a720…`) e as datas `updated`/`reviewed` por documento — o substituto possível de um SHA para serviço |
| P15 | `/blog/best-ai-vectorizers-2026` e as páginas comparativas do próprio fornecedor | além de documentarem que o concorrente citado cobre DXF/EPS/PDF por API e SDK, elas **advertem** que não há medição pareada retida: «cós não completamos um benchmark de saídas pareadas retido» (frase lida na página em 2026-11-26) — ou seja, o próprio vendedor evita medir fidelidade, o mesmo motivo que o §10 impõe a nós |
| P16 | terceiros: diretório `mcpservers.org` para o conector (categoria “Design”, 1 crédito por SVG, falhas grátis, 5 MB) — usado **só** para confirmar que o MCP está listado fora do site do fornecedor, nunca como fonte de número |
| P17 | `/docs/api/agents.md` (2026-11-04) | a referência de uma página escrita para agentes: prefixos de chave (`pv_live_` cobra 1 crédito **só no sucesso**, `pv_test_` devolve SVG de amostra e nunca cobra), os 6 endpoints, `Prefer: wait=N`/`respond-async`, `Accept: image/svg+xml`, `X-Request-ID`/`X-Credits-Charged`/`X-Credits-Would-Charge`, idempotência de 24 h com `409` em reuso, `402` sem overdraft, packs de API separados dos créditos do site, resultado válido 24 h, `DELETE`, erros `problem+json` — e a frase que decide o §5.2: **"It sends no CORS headers, so browsers block calls from web pages, and an API key in a web page would be public"**. **Ressalva de método:** na primeira leitura o `fetch_page` cortou a tabela de packs no meio ("Bulk 1.000 … USD 8…"); os três preços saíram de P10, não desta página, e nada foi extrapolado do trecho truncado |

Não lidas, e declaradas como lacuna: a **Privacy Policy** do site (o §6 do aviso de API referencia `§2.2`, `§5`, `§7`, `§8.3` dela — retenção do Studio e transferências internacionais ficaram **REPORTED** via P13, não CONFIRMED na fonte) e a **MCP Privacy Notice** (`/docs/mcp/privacy`), citada no §7 dos MCP Terms. Nenhuma página de incidente, SOC 2 ou subprocessador adicional foi procurada: o serviço não publica nada disso, e §6 não tem o que conferir.

## 5. Termos: o que pode e o que não pode

### 5.1 Direitos comerciais — sim, e sem pegadinha
O §8.1 é limpo: "We claim no ownership of your inputs or of the SVG outputs". O `/product-facts.md` reforça "yours to use, including for commercial work", com a responsabilidade de direitos sobre o **original** caindo em você (§8.2: "We do not actively moderate uploads", e você declara ter o direito de converter o que envia). Não há cláusula de licença reversa sobre o resultado, não há exigência de atribuição, não há restrição de "não usar em produto concorrente" sobre o **SVG**.

### 5.2 Oferecer a terceiros — só com consentimento prévio, e o consentimento existe, mas é estreito
O §8.3 proíbe "resell, sublicense, or provide automated or derivative access to the Service to third parties without our prior written consent". O §9 dos API Terms resolve isso para a API: **"this is our consent under §8.3"** — você pode oferecer features construídas sobre a API aos **seus próprios usuários**, desde que (a) esses usuários aceitem termos seus **pelo menos tão protetores**, (b) você seja responsável pelo que eles enviarem, e (c) **nunca** der a chave a eles. Isso viabiliza o modelo "servidor nosso, chave nossa" — e inviabiliza exatamente o modelo "BYO-key" que é o princípio do Lia Forge.

Para o **MCP** não há tal consentimento: os MCP Terms o restringem ao fluxo oficial de conexão pessoal (§6) e proíbem reuso das credenciais emitidas ao assistente; usá-lo "as a bulk conversion service" é proibido explicitamente. Um produto que se ligasse ao MCP estaria pedindo que **cada usuário** faça OAuth com Google na conta dele — com o saldo do site, que não converte em crédito de API (§3, ponto 1).

### 5.3 Uso de dados — o lado bom, verificado
"Your images are never used to train AI models and never sold" (P7), com a arquitetura correspondente: `DELETE` a pedido, 48 h como teto de apagamento, request records sem IP e sem imagem, nenhuma miniatura gerada para a API. Para o Studio do site, o fornecedor afirma outra janela (≈3 meses) — **REPORTED**, porque a Privacy Policy que a rege não foi lida aqui.

### 5.4 O §10 é o que fecha a porta que a Lia precisa
O Terms proíbe usar "any input, output, preview, thumbnail or metadata" para "training, fine-tuning, evaluation, benchmarking, red-teaming, or dataset construction" sem consentimento escrito prévio, e proíbe usar os resultados para "develop, improve, or validate any system that competes with or replicates the Service (including image-vectorization)". Os API Terms (§1) e os MCP Terms (§1) explicitam que o uso **operacional** da API/Connector não é "AI or machine-learning purpose" — mas que as proibições de dataset e de sistema concorrente **continuam valendo**, e que o texto é cumulativo com o Terms, em uso comercial ou acadêmico.

Consequência direta para este relatório: **não existe caminho lícito para provar que o PerfectVector é melhor (ou pior) que VTracer/Potrace/Inkscape** usando as saídas dele. Toda comparação de fidelidade com material da Lia está bloqueada por contrato. É por isso que §8 mede só a alternativa aberta, e por isso que a recomendação é referência de processo, não adoção.

### 5.5 O que o contrato não cobre, e a Lia não deveria fingir que cobre
Sem SLA (§13), sem garantia de qualidade ("we do not guarantee that vectorization results will be of any particular quality, accuracy, or fitness for a particular purpose"), teto de responsabilidade **USD 100** ou o pago em 12 meses (§16), **você indeniza** a Rastrix por danos ligados aos "outputs you generate, download, or distribute" (§17), direito coreano e foro em Seul com prescrição de 1 ano (§19–§20). Para um app distribuído no Brasil, isso significa: o fornecedor não deve nada a ninguém, inclusive aos seus usuários. Não é parecer jurídico — é o que o texto diz.

## 6. Retenção, processamento externo e quem vê os bytes

| Fato | Fonte |
|---|---|
| Imagem e SVG ficam **24 h** disponíveis e são apagados do storage **em até 48 h**; `DELETE /v1/vectorizations/{id}` apaga na hora | P7, §6 |
| Com chave de teste: "we check the image and then discard it … we keep only its file name, size, dimensions and fingerprint, and store no files" | P7, §2 |
| "We keep no previews or thumbnails of API files" | P7, §2 |
| Registros de requisição: 90 dias, **sem imagem e sem IP**; conversões ficam com o histórico da conta (status, tempos, tamanhos, dimensões, créditos) | P7, §6 |
| Um pequeno número de funcionários autorizados **revê conversões recentes** em painel read-only para detectar conteúdo ilegal ou abuso; "review happens only while the files are still retained, and we never keep copies for this purpose" | P7, §3 |
| Subcontratados nominais: **Google Cloud** (Cloud Run, Cloud SQL, Cloud Storage, Cloud Tasks), **um provedor de GPU nos EUA** para o processamento — "per its documentation, it does not keep the inputs of synchronous calls after returning the result" — **Lemon Squeezy** (pagamento), **AWS SES** (aviso de saldo baixo, se ativado), **Sentry** (erros, com chaves removidas). "API requests are not sent to any other image processing provider." | P7, §4 |
| Chaves só como hash unidirecional; resultado entregue apenas à conta que o criou; logs e relatórios de erro sem chave | P7, §9 |
| MCP: imagens apagadas em ≈30 dias; link de 24 h funciona como segredo de portador, **inclusive depois de desconectar** | P9, P8 §9 |

O que isso significa para material não publicado: a imagem sai da sua máquina, passa por pelo menos dois provedores de nuvem (um deles de GPU, nos EUA), fica hospedada por até 48 h e **pode ser aberta por um humano** no painel de revisão. Não há "modo confidencial", nem contrato de não-divulgação no produto, nem região escolhível. Para os vetores oficiais e o material ainda não anunciado da Lia, isso é suficiente para dizer não — independentemente de qualidade.

## 7. Dependência do fornecedor e comportamento em falha

**Offline: nada funciona.** Não existe binário local, SDK com cache, nem modo degradado: sem rede, a superfície inteira desaparece — e mesmo os erros de borda (`403`, `429`) pressupõem um servidor do outro lado. E não é preferência de arquitetura: a Etapa D do `governance/INVESTIGATION-PROTOCOL.md` proíbe expressamente, numa rodada de pesquisa, «usar serviço pago, consumir crédito, criar conta, enviar dado proprietário para fora» — exatamente as quatro coisas que este serviço exige de quem o adota. Aqui a dependência é de primeira ordem **e** com contrato instável (§2 early access do Terms: "features, plan limits, pricing, retention windows … expected to evolve rapidly").

O lado bom, e é raro: a API **diz** o que está acontecendo. `X-Request-ID` em tudo, `X-Credits-Charged`/`X-Credits-Would-Charge`, `X-RateLimit-*`, `Retry-After`, corpo `problem+json` com `code` estável e `WWW-Authenticate` no `401`, suspensão surtindo efeito em ≤30 s, e a orientação explícita de que `detail` pode mudar — "Branch on `code`, never on `title` or `detail`". Um cliente Lia bem escrito teria como mapear cada código em estado de produto (retry, refile, recarregar, avisar) sem adivinhar.

O lado que dói em pipeline: **o resultado evapora em 24 h**, a re-conversão é cobrada de novo, e o histórico não é consultável por API. Isso empurra para a Lia a construção de um cache próprio (SVG + `id` + `X-Request-ID` + hash da imagem de origem), que é a mesma disciplina que a base já recomenda para notas e ativos em `LR-CMP-006`.

## 8. O que foi executado aqui (e o que não foi)

**Contra o serviço: nada.** Nenhuma conta criada, nenhuma chave `pv_test_` gerada, nenhuma conexão MCP. Um smoke test de 3 minutos com chave de teste daria `201` com SVG de amostra fixo e provaria alcance de rede, autenticação e formato de corpo — mas exigiria criar conta num serviço de terceiro, e isso é **Nível 3** do `governance/TESTING-PROTOCOL.md` ("Conta/credencial pessoal · quota de serviço externo · API autenticada · pagamento"), que só existe com autorização específica do proprietário. A ordem de serviço desta rodada não trouxe essa autorização, e a Etapa D do protocolo de investigação a proibiria mesmo assim. O campo `Resultado de execução` deste dossiê diz **`PARTIAL`**, não `NOT_RUN`, e é preciso explicar por quê: a Etapa D exige registro das tentativas, e a tentativa executada aqui (o ensaio local do §8) ganhou linha própria em `data/testing/test-log.tsv` — sem as dez colunas, o protocolo não deixa a tentativa ser citada no relatório. A linha está chaveada em `LR-VEC-001` porque o VTracer não tem objeto no catálogo: é medição **da alternativa**, feita a serviço deste veredito. O serviço em si continua sem uma chamada; o rótulo honesto das páginas lidas é **`DOCUMENTED`**, não “testado”.

**Contra a alternativa aberta: medido, com material sintético nosso.** Binários do sandbox: `inkscape`, `potrace`, `autotrace` e `vtracer` **não existem** (só ImageMagick 6.9.11-60 Q16) — a medição de Inkscape/Potrace fica **BLOCKED: FALTA_DEPENDENCIA**. O que rodou foi o binding Python do VTracer: `python3 -m venv` + `pip install vtracer` (**0.6.15**), com `convert` gerando quatro imagens e `vtracer.convert_image_to_svg_py` vetorizando as quatro. O SVG gerado se autointitula `Generator: visioncortex VTracer 0.6.12` — a versão embutida no wheel 0.6.15, lida no arquivo.

Superfície do binding, medida por sondagem (não por doc): 3 funções (`convert_image_to_svg_py`, `convert_pixels_to_svg`, `convert_raw_image_to_svg`) e, dos 31 nomes de opção testados, **só 5 são aceitos** (`mode`, `filter_speckle`, `color_precision`, `corner_threshold`, `path_precision`); `num_colors`, `hierarchical`, `stack_mode`, `color_fidelity`, `min_color_area` e outros 21 dão `TypeError`. Reduzir a superfície de parâmetros é um problema dos **dois** lados desta comparação — a API do PerfectVector também não tem nenhum.

| Caso (sintético) | PNG → SVG | Tempo local | Cores no SVG | Fato medido |
|---|---|---|---|---|
| marca 512×512, 3 cores chapadas | 18.859 B → 2.463 B, 3 paths | 0,023 s | azul `#1F6EEA` (era `#1F6FEB`, dist. 1,4) · laranja `#E3572E` (era `#E4572E`, dist. 1,0) · branco `#FEFDFD` (era `#FFFFFF`, dist. 3,0) | cor chapada **não sobrevive exata**; sem `viewBox`, sem `<g>`, sem `<title>`, sem `fill-rule` |
| marca reamostrada a 64×64 | 4.188 B → 1.253 B, 3 paths | 0,001 s | `#216EE8` (3,7) · `#DC5936` (11,5) · `#FCECE7` (30,8) | quanto menor o raster, pior a cor — e **100 px é o piso do PerfectVector**, o que elimina favicons e ícones pequenos por contrato |
| gradiente 256×256 (2 cores) | 1.565 B → 340 B, 1 path | 0,007 s | 1 cor `#81628C` = média aproximada | vetorizador por cor **destrói gradiente**; o SVG de marca "ficou limpo" e virou outra imagem |
| polyline de 1 px (`#111111`) em branco | 2.868 B → 564 B, 2 paths | 0,006 s | `#646464` (dist. **143,8**) · `#FCFCFC` | traço fino engrossa e clareia; o critério que o próprio workspace de identidade declara (`CODEX_HANDOFF.md`: “legibilidade em 32 × 32 px”) não sobrevive a um processo que suaviza por cima de anti-aliasing |

Nada disso é comparação com o PerfectVector — é o custo medido de *não medir*: 0,02 s por arquivo e nenhum dado fora da máquina. As quatro conclusões transferíveis: (i) **cor chapada precisa ser re-verificada** em qualquer vetorizador por cor, não só neste; (ii) ícone pequeno e traço fino são os casos que perdem; (iii) estrutura semântica (grupos, nomes, `viewBox`) **não volta** de um traço automático; (iv) o ensaio local é barato o suficiente para rodar no CI da Lia, enquanto o ensaio pago é proibido.

Reproduzir: `python3 -m venv /tmp/r28/venv && /tmp/r28/venv/bin/pip install vtracer`, gerar os quatro PNGs com `convert` (comando em bruto no roteiro da sessão `/tmp/r28/probe.py`), chamar `convert_image_to_svg_py(..., mode="spline", filter_speckle=4, color_precision=6, corner_threshold=60, path_precision=3)` e comparar `fill=` com a cor pedida. O roteiro e o JSON do ensaio estão **fora** da base (scratch de sessão): a base guarda o resultado medido, não o artefato — a contabilidade da execução está na linha `LR-VEC-001` de `data/testing/test-log.tsv`, com procedimento, ambiente, evidência e o que ficou de fora.

Licenças das alternativas, conferidas na fonte em 2026-11-26: `visioncortex/vtracer` = **MIT** (★7.614, Rust, `pushed_at` 2026-11-23, não arquivado); o pacote no PyPI 0.6.15 traz `license: None` e **zero** classifiers de licença (os 3 existentes são de implementação: CPython, PyPy, Rust) — **a licença não vem no pacote**, vem do repo (mesma classe de problema de `LR-AGENT-019`); wheels para manylinux/musllinux (aarch64, armv7l, i686, ppc64le, s390x, x86_64), `win_amd64` (843.383 B) e macOS, `requires_python: ">=3.7"` — medidos no JSON do registry em 2026-11-26. **Potrace**: versão **1.16** (17-09-2019), **GPL-2.0-or-later** ("either version 2, or (at your option) any later version"), copyright 2001-2019 Peter Selinger, marca registrada "Potrace" com política explícita sobre ports, entrada **PBM/PGM/PPM/BMP** (PNG **não** entra direto) e saídas SVG/PDF/EPS/PostScript/DXF/GeoJSON/PGM/Gimppath/XFig, além de um programa de **licenciamento duplo** com a versão comercial "Potrace Professional" (Icosasoft). Consequência para a Lia: Potrace é utilizável como **ferramenta separada** no pipeline local (CLI), nunca como biblioteca ligada a um app distribuído; o `pypotrace` listado pelo autor existe, mas **não há pacote `potrace` no PyPI** (404 medido hoje). Inkscape: a página oficial anuncia 1.4.4 (2026-05-06) com a 1.5 em andamento; o mirror `inkscape/inkscape` no GitHub devolve `license: null` pela API, e o binário não existe neste sandbox — fica `NOT_RUN`.

## 9. Riscos para ícones, cores e ativos oficiais da Lia

| # | Risco | Estado | Por quê |
|---|---|---|---|
| R1 | **Perda de cor exata** em qualquer vetorização automática | CONFIRMED na alternativa (medição própria, §8) / REPORTED para o serviço | vetorizador por cor estima `fill`; o risco de publicar ícone com `#1F6EEA` no lugar de `#1F6FEB` é real e silencioso |
| R2 | **Ícone abaixo de 100 px por lado é recusado** | CONFIRMED (P4, P5) | `min_dimension: 100` + `422 invalid_image` — elimina favicons 32/48, muitos ícones de UI e qualquer ativo de 64 px |
| R3 | **Um único SVG, sem parâmetros** | CONFIRMED (P3, P4, P9) | `max_variants: 1`, `options` inútil em v1, "standard settings" no MCP — nada de controlar suavização, cantos, número de cores ou piso de mancha |
| R4 | **Saída insuficiente para uma cadeia de marca** | CONFIRMED (P2, P3, P13) | pela API sai **só SVG**; PDF/EPS/DXF/AI existem **apenas** no site e no editor, e as pranchas por tamanho que o workspace de identidade exporta hoje (`A1-Micro-Cor-16/24/32/64/128/512.png`, medido no repositório) continuariam sendo trabalho nosso — o serviço nunca fecha a cadeia, abre um degrau dela |
| R5 | **Estrutura semântica não volta** | CONFIRMED na alternativa / não testado no serviço | saída com path único, sem grupos, nomes, `<title>`, `viewBox` ou `fill-rule` — e a árvore do repositório de identidade localizado (medida hoje por API: **95** entradas, **23** `.svg` — 17 em `Source/`, 6 em `Exports/`) já está organizada assim: mestre em `Source/Symbol/Exploration-05/A1-Master.svg` e `A1-Micro.svg`, com **12 pranchas** de exportação em `Source/Symbol/Exploration-05/PNG/` (`A1-Micro-Cor-` e `A1-Micro-Mono-` em 16, 24, 32, 64, 128 e 512 px, de 613 a 60.520 bytes). Um traço automático sem estrutura não substitui esse mestre — só o reescreve pior |
| R6 | **Revisão humana + 48 h em nuvem de terceiro** | CONFIRMED (P7 §3) | material não publicado não deveria entrar num sistema onde a equipe "spots misuse" lendo conversões recentes |
| R7 | **Perda do resultado e custo repetido** | CONFIRMED (P5 `result_expired`, P3) | 24 h de janela de download, sem listagem, re-conversão cobra de novo |
| R8 | **Preço volátil sem aviso + sem reembolso do comprado** | CONFIRMED (P12 §4.2) | a única proteção de preço do Terms (§14) é suspensa para a API |
| R9 | **Sufocamento de lote** | CONFIRMED (P4) | 1 conversão simultânea por conta; segundo pedido é recusado, não enfileirado |
| R10 | **Impossibilidade de validar antes de adotar** | CONFIRMED (P11 §10 + P12 §1) | vedado usar output/preview para evaluation/benchmark ou para validar sistema concorrente; sem consentimento escrito, o relatório fica **sem** como trocar `NOT_RUN` por medição |
| R11 | **Recurso prático inexistente** | CONFIRMED (P11 §16–§20) | USD 100, lei coreana, Seul, 1 ano, e você indenizando por outputs distribuídos |
| R12 | **Credenciais compartilhadas** | CONFIRMED (P8 §6, P12 §9) | as credenciais do MCP não podem ser reusadas nem repassadas; a chave da API não pode ir ao usuário — num produto cujo modelo é o usuário trazer a própria chave, isto åo fecha por construção: a chave teria de ser da Lia, e o consumo deixaria de ser do usuário |

## 10. Recomendação e handoffs

**Veredito: `REFERENCE_ONLY` — não catalogar como integração opcional em nenhum dos três produtos, e não usar como dependência.** Não é um "serviço não recomendado" no sentido amplo: para uma pessoa convertendo um PNG seu, é bem documentado, mede os próprios limites, cobra só no sucesso, avisa em `X-Credits-Would-Charge` e apaga cedo quando você pede. A recomendação é negativa por **encaixe**, não por qualidade: sem CORS (browser não pode), sem chave do usuário (um modelo em que o usuário traz a chave não cabe aqui), sem parâmetros (o controle que a Lia tem no Figma não pode), sem listagem (o cache é nosso por obrigação), sem garantia (o §13 não deve qualidade alguma) e sem direito de medir (o §10 proíbe evaluation/benchmark).

**Handoff — Lia Forge.** Nada a integrar. Se um dia houver back-end pago pela Lia, a única porta legítima é a API server-side com consentimento do §9 dos API Terms, e as condições mínimas ficam registradas aqui: (1) chave **da Lia**, nunca do usuário (`pv_live_` no servidor, `pv_test_` no CI); (2) `Idempotency-Key` derivado do hash da imagem de origem; (3) `Accept: image/svg+xml` com `connect-timeout 10 s`/`total 150 s`; (4) **persistir o SVG e o `id` imediatamente** (24 h); (5) fila própria de 1 pedido por conta, com `Retry-After` respeitado; (6) tratar `201 status:failed` como falha de negócio e `410` como refile; (7) o pipeline de **rejeitar antes de enviar** qualquer imagem com lado <100 px, >5 MiB, animada ou não-PNG/JPEG/WebP; (8) termos próprios ≥ protetores para o usuário final; (9) nada de material oficial da marca no fluxo. O custo de referência: **USD 0,08–0,40 por conversão** conforme o pack, com preço da API sujeito a mudança sem aviso.

**Handoff — Lia Studio.** Aqui o serviço é uma **referência de processo** — cinco padrões que valem copiar sem contratar nada: (a) preview irrestrito e gratuito, cobrança por resultado entregue ("one credit per delivered SVG", falha grátis); (b) `X-Credits-Would-Charge` — avisar o preço **antes** de executar; (c) "Yes, always" memorizado como escolha do usuário, não do app; (d) verificação de saúde/limites por uma chamada grátis (`GET /v1/account` devolve saldo, preços e limites num só corpo); (e) o link de 24 h — que para nós é o exemplo do que **não** fazer num app local: o Studio serve o arquivo do projeto do usuário, não um segredo temporário. O caminho de vetorização do Studio continua local (a cadeia atual + a medição de §8), e o §2.1 (sem CORS) encerra a hipótese de "chamar de qualquer jeito do browser".

**Handoff — Lia Design Foundation (produção de ativos e ícones).** Regra única: **nenhum ativo oficial, nenhum ícone da Lia e nenhum material não publicado é enviado a um serviço externo** — e a própria regra do workspace de identidade já diz isso em outra linguagem: `CODEX_HANDOFF.md` de `BloomRX/BloomStudios-Branding-Review-TEMP` exige “Avaliar silhueta isolada, monocromática e legibilidade em 32 × 32 px” e proíbe “exportar mockups como se fossem arquivos mestres” — por R6 (retenção + revisão humana), R10 (impossibilidade de validar) e R1/R2/R5 (o que a vetorização automática faz com cor chapada, ícone pequeno e estrutura). O vetor oficial **é a fonte**: vetorizar é operação para raster de terceiros, e só depois de re-desenho verificado. Se um vetorizador externo for preciso um dia, a ordem de precedência é (1) desenho manual no editor do projeto, com as pranchas de 16–64 px que o próprio workspace já exporta como prova de legibilidade, (2) `vtracer` local (MIT, medido em §8 — as opções que existem são `mode`, `filter_speckle`, `color_precision`, `corner_threshold`, `path_precision`) com verificação automática de `fill=` contra a paleta, (3) Inkscape 1.4.4 com Potrace embutido (licença da ferramenta GPL-2.0-or-later ⇒ separada do app, nunca linkada), e só então (4) qualquer serviço pago, com consentimento escrito prévio para uso dos resultados em avaliação.

**Lacunas abertas por esta rodada** (registradas no índice §6): Privacy Policy do site e MCP Privacy Notice não lidas na fonte; nenhuma execução do serviço, hoje e até que o dono autorize conta/chave (o campo do cabeçalho é `PARTIAL` por causa da medição local, não por teste do serviço); comparação de fidelidade **bloqueada por contrato**; e a alternativa local medida em apenas 4 casos sintéticos — o item 6 da fila do backlog (`RESEARCH-BACKLOG.md` §5) e a tarefa D-2 do roadmap tratam de estender a bateria a Inkscape 1.4.4 + Potrace 1.16 e à varredura de 16/24/32/64/512 px, o que exige instalar os binários e não cabe numa rodada documental.

## 11. Evidências

| # | Afirmação | Rótulo | Como reproduzir |
|---|---|---|---|
| E1 | 6 endpoints; sem listagem de conversões; sem CORS; `pv_test_` devolve SVG de amostra grátis; SVG é a única saída da API | **CONFIRMED** (P3, P2) | `curl -s https://perfectvector.com/docs/api/introduction.md`; `curl -si -X OPTIONS https://api.perfectvector.com/v1/account \| grep -i access-control` (sem credencial: resposta sem cabeçalho CORS) |
| E2 | 20 criações/min, ~40 POST/min, ~120 leituras/min, **1 conversão live simultânea**, 10 chaves, 5 MiB = 5.242.880 B, 100–4.096 px, 1 moldura, fila de 10 min | **CONFIRMED** (P4) | `curl -s https://perfectvector.com/docs/api/limits.md` (o JSON `limits` do `GET /v1/account` é a via autoritativa com chave) |
| E3 | 19 códigos de erro; `result_expired` 410; falha = `201 status:failed` com `credits_charged: 0`; `429`/`403` de borda sem `problem+json` | **CONFIRMED** (P5) | `curl -s https://perfectvector.com/docs/api/errors.md` |
| E4 | política de retry do fornecedor (10 s / 150 s / `--retry 3` com a mesma chave; `timeout` pede chave nova) | **CONFIRMED** (P6) | `curl -s https://perfectvector.com/docs/api/troubleshooting.md` |
| E5 | retenção 24 h → 48 h; test key sem arquivo; sem previews; request records 90 dias sem IP; revisão humana por poucos autorizados; "never used to train AI models and never sold"; Google Cloud + provedor de GPU nos EUA + Lemon Squeezy + SES + Sentry | **CONFIRMED** (P7) | `curl -s https://perfectvector.com/docs/api/privacy.md` |
| E6 | preços de API USD 4/16/80 (0,40 · 0,16 · 0,08 por conversão), 12 meses, 10 packs por pedido, ≥10.000 via vendas, beta −20% | **CONFIRMED** (P10) | `curl -s https://perfectvector.com/pricing/api.md` |
| E7 | MCP: OAuth Google, saldo do site, sem parâmetros, link de 24 h que sobrevive à desconexão, proibido usar como lote/reusar credenciais, sem SLA | **CONFIRMED** (P8, P9) | `curl -s https://perfectvector.com/docs/mcp/terms.md`; `curl -s https://perfectvector.com/mcp.md` |
| E8 | "You may offer features built on the API to your own users; this is our consent under §8.3" + "Do not give your API keys to your users" + termos próprios obrigatórios | **CONFIRMED** (P12 §9) | `curl -s https://perfectvector.com/docs/api/terms.md` |
| E9 | §10 proíbe evaluation/benchmark/dataset e "validate any system that competes with or replicates the Service"; cumulativo e válido para uso comercial e acadêmico | **CONFIRMED** (P11 §10 + P12 §1 + P8 §1) | `curl -s https://perfectvector.com/terms` |
| E10 | preço da API muda sem aviso (isenção do §14) e créditos comprados não são reembolsados | **CONFIRMED** (P12 §4.2) | idem E8 |
| E11 | sem SLA, sem garantia de qualidade, teto **USD 100**, você indeniza por outputs distribuídos, lei coreana/Seul/1 ano | **CONFIRMED** (P11 §13, §15–§20) | `curl -s https://perfectvector.com/terms` |
| E12 | VTracer 0.6.15 instalado e executado localmente; 3 funções; **5 de 31** nomes de opção aceitos; 4 casos medidos com bytes, paths, tempo e desvio de cor | **MEASURED** (material sintético próprio) | §8; roteiro `/tmp/r28/probe.py` + `resultado-vtracer.json` (scratch, não versionado) |
| E13 | `visioncortex/vtracer` = MIT (★7.614, push 2026-11-23); PyPI 0.6.15 com `license: None` e **zero** classifiers de licença (3 de implementação: CPython, PyPy, Rust); wheels por plataforma (incl. `win_amd64` 843.383 B) | **CONFIRMED** | `gh api repos/visioncortex/vtracer`; `curl https://pypi.org/pypi/vtracer/0.6.15/json` |
| E14 | Potrace 1.16 (2019-09-17), GPL-2.0-or-later, marca registrada, entrada PBM/PGM/PPM/BMP, 9 saídas, licenciamento duplo com "Potrace Professional"; **nenhum pacote `potrace` no PyPI** | **CONFIRMED** | `curl -s https://potrace.sourceforge.net/` (seções Version/License/Ports); `curl -o /dev/null -w '%{http_code}\n' https://pypi.org/pypi/potrace/json` → 404 |
| E15 | ausência de `inkscape`/`potrace`/`autotrace`/`vtracer` no sandbox; ImageMagick 6.9.11-60 Q16 | **OBSERVED** | `for b in inkscape potrace autotrace vtracer convert; do command -v $b || echo "sem $b"; done`; `convert --version` |
| E16 | chamada autenticada à API, smoke com `pv_test_`, conexão MCP, qualidade relativa de vetorização, conversão dos ativos oficiais da marca | **NOT RUN** | exige conta OAuth Google + crédito pago; e o §10 do Terms do fornecedor proíbe usar as saídas em avaliação — decisão de criar conta é do dono, não desta base |
| E17 | retenção do Studio (≈3 meses) e janela do site (≈30 dias) | **REPORTED** (P13, P9) | não conferido na Privacy Policy do site — lacuna declarada em §4 |
| E18 | custo de parede dos 1.000 arquivos com `max_in_flight: 1` | **INFERRED** | derivado dos limites de P4; nenhuma medição de latência do serviço foi feita |
