# AetherAI (aetherforgeai.com) — serviço de assets 2D para jogos

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-008` |
| Categoria | model (serviço comercial) |
| Projetos | Lia Forge 2.0, Lia Studio |
| Fontes | `aetherforgeai.com/pt` e `/en` (home, lidas em 2026-11-20); `/pt/policy/service` (Termos de Serviço, vigência 2026-04-01); `/pt/policy/privacy`; `/en/student-instructor-plan`; `/pt/free-assets`; `/pt/pricing` (não renderiza sem JavaScript) |
| Data | 2026-11-20 |
| Status | CURRENT |
| Confiança | **Alta em direitos e natureza do serviço** (texto contratual lido); **baixa em preço por operação e em qualidade** — a página de preços não renderiza e nada foi gerado |
| Natureza | pesquisa e documentação; **não é recomendação de contratação** e não autoriza abrir conta nem gastar créditos |

---

## 1. O que é

SaaS de **assets visuais 2D para jogos**, operado pela **Aether Forge Games Inc.** (termos
interpretados sob as leis da **República da Coreia**; disposição suplementar fixa vigência em
**2026-04-01**). Site com localização em português (além de inglês, presumivelmente coreano),
login por Google, GitHub ou Discord. O produto-irmão **Pixilmate** (`pixilmate.com`) é onde a
pixel art gerada vira animação e é compartilhada na comunidade.

Não é um modelo aberto, não é um runtime local e **não faz 3D**. É serviço gerenciado: você
descreve, ele gera, você baixa.

## 2. O que ele declara fazer

| # | Função | Detalhe declarado | Rótulo |
|---|---|---|---|
| 1 | Estúdio de geração de imagens | ideia curta → personagens, itens e cenários | `OFFICIAL_DOCUMENTATION` |
| 2 | Pixel art 32 px e 48 px "sem limites" | modelo **próprio** da AetherAI; personagens, itens, tiles. "Sem limites" é **alegação do site** — não há política publicada de limite por plano | `OFFICIAL_DOCUMENTATION` (a função) / `UNVALIDATED` (o "ilimitado") |
| 3 | Animação de sprites a partir de uma imagem | `sprite-pulsar-v2`: 1 imagem → sequência de sprites com movimento | `OFFICIAL_DOCUMENTATION` |
| 4 | Reskin de movimento (`sprite-to-sprite`) | mantém o movimento de uma animação existente e troca personagem/estilo | `OFFICIAL_DOCUMENTATION` |
| 5 | Assets gratuitos para download | personagens, monstros, itens, cenários; a listagem tem **filtro de licença** | `OFFICIAL_DOCUMENTATION` (licença por asset **não lida**) |
| 6 | Modelo de IP dedicado | treino com a IP/estilo do cliente; "da preparação dos dados ao treinamento" | `OFFICIAL_DOCUMENTATION` (contrato não lido) |
| 7 | Edição e preview de folha de sprites | editor no próprio site | `OFFICIAL_DOCUMENTATION` |

**Formatos de saída:** PNG (folhas de sprites, frames) e GIF são claramente visíveis no produto.
A *meta description* do site em inglês cita ainda **Lottie e JSON**; isso está no metadado da
página, **não** no corpo do texto que li — trato como `UNVALIDATED` até ver documentação de
exportação.

**O ponto de maior interesse para o Lia Forge** é o par 3+4: gerar uma animação a partir de
**uma única imagem** e depois **transferir o movimento** para outro personagem. É a versão
"serviço" do problema que `LR-STUDIO-009` (consistência de sheet) e `LR-FORGE-007` (2D→3D)
atacam por outro caminho — e é justamente onde o caminho local na RX 580 não tem resposta
(ver `LR-MODEL-007` §5).

## 3. O que ele **não** é

| Expectativa | Realidade documentada |
|---|---|
| Geração 3D / malha / rig / GLB | **não oferece**. Nada na home, nos termos ou na lista de funções menciona 3D |
| Runtime local / pesos baixáveis | não. Serviço em nuvem |
| API pública documentada | **não encontrei**. `docs.aetherforgeai.com` não resolve; não há página de API. `BLOCKED`, não "inexistente" |
| Rig de esqueleto / animação por osso | não declarado. A animação é **por sprites** (sequência de frames) |
| Character sheet multi-vista canônico | não declarado como função. Existe "editor de folha de sprites", que é organização de frames |
| Garantia de consistência entre gerações | **não**. A consistência de longo prazo é vendida via **modelo de IP dedicado** (item 6), que é contrato à parte |

## 4. Direitos sobre o resultado — o texto, não a impressão

Fonte: `https://www.aetherforgeai.com/pt/policy/service`, seção "Uso dos resultados gerados",
lida em 2026-11-20. Resumo fiel em oito pontos:

| # | O que o termo diz | Consequência prática |
|---|---|---|
| 1 | "Resultados gerados" = imagens, folhas de sprites, efeitos, ícones, fundos e outros conteúdos digitais criados/editados no uso normal | cobre sprite sheet e pixel art |
| 2 | A empresa **não reivindica propriedade nem direitos exclusivos**; se existe direito autoral e qual o alcance **será determinado caso a caso** conforme contribuição criativa e lei aplicável | honesto e realista — e significa que **não há garantia de que você terá copyright** |
| 3 | Uso **pessoal ou comercial livre**, incluindo personagens/monstros/itens/fundos/UI/efeitos em jogos pagos ou gratuitos; modificar, transformar, combinar, reproduzir, distribuir, vender | é o regime mais permissivo entre os serviços já catalogados |
| 4 | **Sem obrigação de atribuição** à AetherAI | diferente do Meshy Free (CC BY 4.0) |
| 5 | Resultados baixados **continuam utilizáveis** após cancelamento, exclusão de conta ou encerramento do serviço; mas o arquivo pode não estar mais disponível para re-download | **guardar localmente** é obrigação operacional |
| 6 | Sem restrição retroativa dos direitos já existentes, salvo mudança de lei/decisão judicial | reduz risco de "mudaram os termos e meu jogo quebrou" |
| 7 | O usuário responde por violação de direitos de terceiros (imagem, marca, direitos de personalidade) em prompts, referências e resultados | o risco jurídico do insumo é seu |
| 8 | A empresa **não garante** que o resultado não seja idêntico/semelhante a conteúdo de terceiros nem que surja qualquer PI específica | não há indenização por plágio acidental |

**Comparação direta com o que já está no catálogo** (`LR-MODEL-007` §6):

| Serviço | Plano gratuito | Atribuição | Output público? | Observação |
|---|---|---|---|---|
| **AetherAI** | "Comece grátis" + 70 tokens na 1ª compra (paga) | não exigida | não declarado como público | regime comercial declarado no termo, sem renúncia de direitos pelo usuário |
| Tripo | Free **`CONFLICTING`**: página diz "non-commercial", termo dá renúncia + licença pública de exploração comercial a terceiros | não exigida no Free | **sim, por padrão** | `LR-MODEL-007` §6.1 |
| Meshy | Free com CC BY 4.0 | **obrigatória** | não | `LR-MODEL-007` §6.2 |
| GPT Image | por token, sem nível gratuito próprio | não há exigência contratual de atribuição | não | `LR-MODEL-007` §6.3 |

Ou seja: em **direitos declarados**, a AetherAI tem o texto mais favorável dos quatro. Isso não
é elogio ao produto nem garantia: os pontos 2 e 8 do termo devolvem o risco para o usuário, e
`REQUIRES_LEGAL_REVIEW` para saber se a cláusula 2 (direito autoral caso a caso) é compatível
com o uso pretendido em produto comercial da Lia.

## 5. Proibições contratuais que afetam pesquisa e produção

Do artigo 6 dos termos (obrigações dos membros), três cláusulas têm consequência direta:

| Cláusula | Texto (resumo) | Efeito para nós |
|---|---|---|
| 6.3 | sem consentimento escrito, **não** usar o serviço primordialmente para desenvolver, melhorar ou operar **serviço concorrente**, nem conduzir análises organizadas/repetidas, **benchmarking** ou avaliação de desempenho para esses fins | avaliar a AetherAI para **substituí-la** é a fronteira. Pesquisa interna comparativa para decidir é zona cinzenta |
| 6.5 | não coletar/comparar/analisar sistematicamente funções, telas, resultados, desempenho ou padrões de uso **além** do escopo permitido, nem usar isso para treinar modelo ou **material comparativo** | publicar tabela comparativa com dados extraídos do serviço fica restrito |
| 6.6 | proibido engenharia reversa, scraping, crawling, bots, macros e scripts automatizados sobre o serviço | nada de automação de interface. Se não houver API, não haverá integração |

Isso é mais restritivo do que os termos de Tripo/Meshy lidos na rodada anterior e **muda o
modo de avaliar**: a comparação honesta que posso fazer é de **documento**, não de saída do
serviço medida por mim. `REQUIRES_LEGAL_REVIEW` antes de qualquer teste comparativo formal.

Conteúdo proibido também é relevante: **face swap/deepfake de pessoa real sem consentimento** e
**imitar celebridade/pessoa identificável** são vedados (artigo 6, condutas proibidas 1–3). Para
personagem original isso não é problema; para "personagem inspirado em ator" é.

## 6. Preço e tokens — o que dá para afirmar

| Item | Valor | Fonte | Rótulo |
|---|---|---|---|
| Primeira compra | **70 tokens por US$ 3,99** (só novos usuários) | home `/pt` e `/en` | `OFFICIAL_DOCUMENTATION` |
| Preço unitário implícito | ≈ **US$ 0,057 por token** | aritmética sobre o item acima | `INFERRED` |
| Plano educacional | **1.000 tokens** por **KRW 68.900** (KRW 64.900 para alunos de instituições membros), por transferência bancária | `/en/student-instructor-plan` | `OFFICIAL_DOCUMENTATION` |
| Equivalência aproximada | 1.000 tokens ≈ **US$ 48** (câmbio não verificado) | aritmética | `INFERRED`, taxa de câmbio `UNVALIDATED` |
| Tabela de planos | **não obtida**: `/pt/pricing` renderiza "Carregando produtos…" (JavaScript) e a listagem exige sessão | tentativa de leitura | `BLOCKED` |
| Custo por geração / por sprite sheet / por segundo de animação | **não obtido** | — | `BLOCKED` |

**O que isso significa:** sem a tabela de consumo, não sei dizer se 70 tokens geram um
personagem ou trinta. Qualquer frase do tipo "US$ 3,99 dá para X assets" seria invenção. A
rodada anterior corrigiu exatamente esse erro no Meshy ("100 créditos = 10 modelos"); **não vou
repeti-lo aqui**.

## 7. Privacidade — o que está e o que não está no texto

`https://www.aetherforgeai.com/pt/policy/privacy` (lida em 2026-11-20):

| Ponto | Texto |
|---|---|
| Coleta obrigatória | nome, e-mail, senha, dados de pagamento (parte do cartão + número de aprovação) |
| Coleta automática | IP, cookies, registros de acesso |
| Finalidades | identificação e gestão de conta; pagamento e reembolso; **melhoria do serviço** e atendimento |
| Retenção | destruição ao encerrar a conta; registros de pagamento mantidos **5 anos** (Lei de Comércio Eletrônico) |
| Terceiros | gateways de pagamento, provedores de nuvem e parceiros semelhantes |
| Encarregado | nome, e-mail (Gmail) e telefone celular coreano |

**O que a política não diz:** não há cláusula sobre **uso do conteúdo enviado/gerado para
treinar modelos**. A finalidade "melhoria do serviço" é ampla o bastante para gerar dúvida.
Ausência de cláusula não é permissão nem proibição — é **lacuna**, e para um estúdio que envia
IP própria isso importa. `UNVALIDATED` + `REQUIRES_LEGAL_REVIEW`.

## 8. Maturidade — o que a evidência mostra, sem adjetivo

Fatos: empresa identificada como Aether Forge Games Inc.; termos vigentes desde 2026-04-01;
home cita **"37 estúdios"** que "já experimentaram" o fluxo (número de marketing, `UNVALIDATED`
— não há lista, estudo de caso nomeado ou metodologia); depoimentos na home são anônimos
("01…05"); contato de privacidade é um Gmail; a página de preços depende de JavaScript e não
expõe a tabela publicamente.

Isso descreve **empresa pequena e recente**, não serviço inseguro. O que muda com isso é o
peso da continuidade: o termo promete manutenção de direitos após encerramento (item 5 do §4),
o que é a mitigação certa — e reforça que **baixar e arquivar localmente** é parte do fluxo.

## 9. Encaixe nas três frentes do Lia Research

| Frente | Encaixe | Rótulo |
|---|---|---|
| Silhueta primeiro (`LR-STUDIO-008`) | o serviço gera **a partir de** uma silhueta/conceito; não substitui o gate de forma. Útil depois da aprovação, não antes | `INFERRED` |
| Character sheet (`LR-STUDIO-009`) | "editor de folha de sprites" organiza frames; **não** é turnaround multi-vista de personagem 3D | `OFFICIAL_DOCUMENTATION` |
| 2D→3D (`LR-FORGE-007`) | não produz geometria. Serve como **fonte de frames 2D** para pipelines 1/2 e para jogo 2D | `OFFICIAL_DOCUMENTATION` |
| Hardware (`LR-STUDIO-007` §5) | não resolve o gargalo da RX 580 em geração de imagem; é serviço | `OFFICIAL_DOCUMENTATION` |
| Skills (`LR-AGENT-012`) | se houver API, é candidato a skill de "gerar frames"; **sem API documentada**, não há skill possível hoje | `BLOCKED` |

**Não recomendo contratar.** Recomendo o contrário do que já está catalogado: se o projeto
precisar de **animação 2D de sprite** e o caminho local não existir, a AetherAI é o primeiro
candidato a testar **porque o termo de direitos é o mais claro entre os serviços lidos** — e o
teste começa por descobrir o custo por operação, que é o dado que falta.

## 10. O que faria para validar (proposta, não execução)

1. Ler a tabela de planos autenticado (exige conta — **decisão do proprietário**).
2. Comprar o pacote de 70 tokens (US$ 3,99) e gerar **um** personagem já aprovado em silhueta,
   medindo tokens gastos, tempo e número de tentativas até resultado utilizável.
3. Rodar o item 4 (reskin de movimento) sobre o mesmo personagem e verificar se a identidade
   sobrevive — é o teste que decide se o serviço entra em algum pipeline.
4. Conferir exportação (PNG/sheet/GIF; Lottie/JSON se existir) e se o frame sai em 32/48 px sem
   reamostragem.
5. Só depois: perguntar sobre API e sobre modelo de IP dedicado (contrato e preço).

Nada disso foi feito. Nenhuma conta foi criada, nenhum token comprado.

## 11. Não validado (`UNVALIDATED` / `BLOCKED`)

| Item | Estado |
|---|---|
| Preço por geração e tabela de planos | `BLOCKED` (página em JavaScript) |
| Existência de API | `BLOCKED` (não encontrada; não provada inexistente) |
| Licença dos "free assets" (o filtro de licença existe, o texto não foi lido) | `UNVALIDATED` |
| Qualidade real de pixel art e de sprite animation | `UNVALIDATED` — não gerei nada |
| "37 estúdios" | `UNVALIDATED` (marketing sem lastro verificável) |
| Exportação Lottie/JSON | `UNVALIDATED` (só na meta description) |
| Uso de conteúdo do usuário para treino | `UNVALIDATED` (a política não trata) |
| Contrato e preço do modelo de IP dedicado | `BLOCKED` |
| Jurisdição na prática (lei coreana, foro coreano) para contratante brasileiro | `REQUIRES_LEGAL_REVIEW` |

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-GENERATION-MODEL-CATALOG.md` · `RESEARCH-INDEX.md`
