# Bisqit — como um app fechado de "cachorro de desktop" faz exatamente o que o Lia Project lista como lacuna

| Campo | Valor |
|---|---|
| ID | `LR-FORGE-014` |
| Nome | Bisqit (bisqit.app) — desktop dog que fecha a aba onde você se dispersou |
| Tipo | outro (app fechado de desktop + servidor; nenhum código publicado) |
| Fonte oficial | https://bisqit.app/ (redireciona para `/dog`) |
| Responsável | "Ask" / Dawnce — contato `ask@dawnce.app`; apps publicados sob conta norueguesa (`apps.apple.com/no/app/dawnce/id6760565547`); DPA citada na política: Datatilsynet (Noruega) |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | NOT_RUN |
| Recomendação | **ADAPT** — levar o desenho do loop, das permissões e do disclosure; nada a integrar, nada a instalar |
| Decisão de adoção | — nenhuma registrada |
| Categoria | produto (leitura transversal em security, ui, forge) |
| Projetos beneficiados | Lia Project (automação de navegador e permissões), Lia Forge (empacotamento, atualização, preço), Lia Agent Hub (classificação com custo por chamada), Lia Research (formato de divulgação do que é lido) |
| Versão analisada | nenhuma versão pública identificada; páginas do site verificadas em 2026-11-24, com `privacy.html` datado de 22/11/2026 |
| Proveniência do conteúdo | **auto-declarado** — não há repositório, binário auditado ou changelog público; tudo o que segue vem das páginas oficiais do produto |
| Data | 2026-11-24 |
| Última verificação | 2026-11-24 |
| Upstream conferido | 2026-11-24 · `bisqit.app` · `sitemap.xml` com 8 URLs · nenhuma release pública para comparar |
| Próxima revisão | 2027-02-24 |
| Licença | **nenhuma** — proprietário fechado; nenhum texto de licença publicado no site (`CONFIRMED` por esgotamento do sitemap) |
| Confiança | Alta para **o que eles afirmam** (texto lido, duas páginas cruzadas); **nenhuma** para se o software faz o que a página diz |

---

## 1. Por que este objeto entrou na base

O dono apontou o link e pediu "pesquise esse link e como foi feito o app, pode ser útil para o Lia
Project". É um app de nicho — bichinho de tela que fecha abas — mas ele resolve, em produção, três
coisas que a nossa base registra como **lacuna aberta**:

| Lacuna nossa (medida nos dossiês) | O Bisqit tem rodando |
|---|---|
| `lia-browser-automation` — automação de navegador, marcada com **"risco de egress"** | controle de aba real em dois SOs, com o egress minimizado por lista local + cache + recorte de payload |
| permissões de runtime por execução (`LR-SEC-005`, ainda **PROPOSTA**, nada implementado) | duas permissões nomeadas, pedidas uma vez por navegador, com a função de cada uma declarada |
| como explicar ao usuário o que um recurso de IA lê (nosso padrão de docs ainda não tem isso) | uma página inteira por assunto: o que lê, o que sai, quem processa, por quanto tempo fica |

Nada aqui é sugestão de usar o app: é leitura de **como ele foi montado**, que é o que o pedido pedia.

## 2. O que é, e o que **não** é

- **É**: um app para macOS 13+ (Apple Silicon ou Intel) e Windows 10/11 64 bits. Um cachorro mora na
  parte de baixo da tela, anda, cochila quando clicado, pode ser pego e arrastado. Quando o usuário fica
  mais tempo que o "paciência" (padrão: um minuto) numa página julgada dispersão, o cachorro corre até a
  aba e **tapa a aba com a pata** — fecha.
- **Não é**: um app de código aberto (nenhum repositório); não é gratuito (assinatura); não tem extensão
  de navegador; não é para crianças menores de 13 anos, dizem eles; não roda em Linux (nenhuma menção).
- **É novíssimo**: o vídeo de demonstração foi publicado como *unlisted* em 2026-11-11, com 34 visualizações
  no momento da leitura, e a política é de 22/11/2026. Objeto com dias de vida tem risco de sumir ou
  mudar de modelo de preço sem aviso — ver §12.
- A busca na web por "Bisqit" devolve primeiro **outra coisa**: `Biscuit`, app britânico de recompensa por
  passeio de cachorro, e `Biscuit` (workspace de abas), e o sobrenome do forno `bisque`. Um relatório
  futuro não deve herdar essa colisão: o nome do objeto aqui é `Bisqit`, com `q`.

## 3. "Como foi feito": a máquina inteira, camada por camada

Isto é o núcleo do pedido. A fonte é `privacy.html` (que, ao descrever o que sai da máquina, acaba
descrevendo a arquitetura) cruzada com `is-bisqit-safe`. Nenhum trecho abaixo foi verificado contra
binário — rótulo `REPORTED` na §13.

| Camada | O que eles dizem usar | Papel exato |
|---|---|---|
| App no Mac | `app.bisqit.mac`; desinstalar com `defaults delete app.bisqit.mac` | estado local em NSUserDefaults/contêiner do usuário; bundle id em domínio reverso, não `.app` genérico |
| App no Windows | instalador que escreve em `%APPDATA%\Bisqit`; distribuído (ou planejado) na Microsoft Store | mesma ideia de estado por usuário; a Store cuidaria de assinatura e atualização |
| Permissões | **Accessibility** (achar o botão de fechar da aba) e **Automation** (ler o endereço e fechar a aba; perguntado uma vez por navegador). No Windows: **UI Automation**, que não pede nada | decisão central do produto — ver §5 |
| Lista de dispersão | lista embutida dos "time sinks" conhecidos (TikTok, Instagram, YouTube Shorts…) + lista do próprio usuário | o que bate na lista **não faz chamada de rede** — é o que segura o custo e o egresso |
| Servidor próprio | hospedado na **Vercel** ("este site e o nosso servidor") | ponto único entre o app e os provedores; o servidor **não** guarda o que julga |
| Modelo | **OpenRouter → Google Gemini** (hoje), resposta `focus` / `neutral` / `drift` + algumas palavras de justificativa | só para o que a lista não cobre; chave do modelo "só no servidor, nunca no app" |
| Cache do veredito | 6 h, no computador do usuário | mesma página não é enviada de novo nesse intervalo |
| Geração do cachorro | **fal** para imagem e clipes; verificação "tem um cachorro nesta foto?" por **Gemini**; um **worker no Railway** monta o bicho; o resultado volta hospedado no armazenamento do fal | pipeline foto → primeiro frame → conjunto animado, com o binário do app só baixando o resultado final |
| Licença/assinatura | **Upstash** guarda registros de licença e contadores; chave amarrada a até 5 máquinas | sem banco próprio, sem sessão |
| Pagamentos | **Stripe** como *seller of record* (imposto, recibo, reembolso); o `install ID` viaja com o checkout para a chave achar o caminho de volta | o servidor deles recebe só ID/status da assinatura, não o e-mail nem o cartão |
| E-mail transacional | **Resend** para mandar o link (fluxo de celular → desktop) | um e-mail só; o endereço não fica, fica o hash por 1 dia |
| Analytics do site | **Vercel Web Analytics**, sem cookies; fonte carregada do Google; vídeo do YouTube em modo *privacy-enhanced* | eles próprios listam os vazamentos do próprio site (IP para Google/YouTube) |
| Analytics do app | eventos nomeados + `install ID` aleatório; totais diários; únicos não reversíveis; país derivado do IP pela Vercel e não guardado | sem nome, sem URL, sem página |

O desenho que se vê: **nenhum dado de terceiros é armazenado de propósito**. Servidor é *proxy* com
limitação de taxa por IP em memória, não banco. O estado vive na máquina do usuário; o que vive no
servidor são licenças e contadores. É um formato de arquitetura que cabe em um projeto do tamanho do Lia
e que dá para copiar sem copiar código.

## 4. O loop de detecção, escrito como ciclo

Extraído das duas páginas, em ordem:

1. a cada poucos segundos, ler app em primeiro plano + título da janela;
2. se for navegador, ler endereço e título da aba atual — **incluindo janelas privadas** — e a posição do
   botão de fechar, para a pata acertar;
3. ler só o **instante** do último teclado/mouse, nunca quais teclas;
4. se ficou acima do "paciência" (padrão 1 min) e o endereço **não** está na lista embutida nem na lista do
   usuário → mandar o pacote mínimo (app, endereço sem nada depois de `?`, título cortado em 140
   caracteres, a linha "o que você faz", os *time sinks* escolhidos, e até 6 julgamentos anteriores com
   hora e veredito);
5. receber veredito + justificativa curta e **guardar 6 h** local;
6. `drift` → o cachorro corre até a aba; há uma janela para **segurar o cachorro** antes da pata cair, o
   que dá mais 70 s;
7. apps de dispersão (jogos etc.) são **guardados para fora da tela, nunca fechados** — "para não perder
   trabalho não salvo";
8. erro do modelo → o usuário marca **"Not a drift"** e aquela página fica em paz para sempre (correção
   persistida localmente).

Dois detalhes de engenharia valem mais que o resto: o cache de 6 h por página (transforma um classificador
pago em chamadas raras) e a correção local que **aprende sem modelo** (o "não" do usuário vira lista, não
vira *fine-tune*).

## 5. A escolha que define o produto: AX/UIA em vez de extensão

Eles afirmam "não há extensão de navegador, então nada é adicionado ao seu navegador" — e, para chegar
nesse resultado, pedem **duas das permissões mais largas do macOS**. Não é contradição, é troca:

| | Extensão de navegador | Acessibilidade/Automação (o que eles fizeram) |
|---|---|---|
| Escopo | só o navegador | qualquer app em primeiro plano (o que é justamente o produto: "cuida da sua atenção") |
| Persistência no alvo | código rodando dentro do navegador, atualizado pela loja dele | nenhuma modificação do navegador |
| Leitura de aba privada | normalmente bloqueada/detectável | **incluída**, eles dizem isso sem pedir desculpa |
| Custo de confiança | instalar algo no navegador | dar ao app a capacidade de clicar por você |

A parte copiável é o **meio-termo que eles escolheram**: não ler conteúdo de página, nunca ler teclas, e
dizer em voz alta o resíduo que sobra — *"títulos podem conter dados pessoais, como o assunto de um
e-mail; o Bisqit encurta, mas não consegue filtrar"*. Essa frase é o oposto do padrão de mercado, e é o
que faz a página de "segurança" funcionar como marketing. Vale como molde para qualquer recurso nosso que
lê o ambiente do usuário (ver §11).

Uma inferência nossa, marcada como tal: a descrição "Automation, perguntado uma vez por navegador, deixa
ler o endereço da aba e fechar a aba" é compatível com Apple Events/AppleScript por navegador (e não com
injeção), enquanto "Accessibility para achar o botão de fechar" é compatível com leitura de geometria do
`AXCloseButton`. Não verifiquei binário — `INFERRED`.

## 6. O pipeline "seu cachorro", que é o assunto do `LR-STUDIO-012` encontrar aqui

Fluxo completo, do lado do servidor deles:

1. o usuário escolhe uma foto no app **ou no site, pelo celular**;
2. antes de qualquer pagamento: foto + `install ID` → Gemini responde "tem um cachorro aí?" → **fal** gera
   **uma** primeira imagem; nada de foto fica no servidor deles; por **1 dia** guardam `install ID` ×
   endereços das imagens do fal, por **1 semana** o endereço da primeira imagem, "para o checkout poder
   mostrar o seu cachorro"; tentativas contadas por `install ID` e IP;
3. no celular: o cachorro fica guardado **30 dias** sob um código de 6 caracteres, com nome, sexo, idade e
   descrição digitados; e-mail via Resend com o link; o IP do computador que abrir a página fica associado
   ao código por **1 semana** "para o Bisqit achar o seu cachorro sem o código";
4. depois de assinar: o app manda foto + primeira imagem + nome + chave de licença + `install ID`; o
   servidor põe os arquivos no armazenamento do fal; um **worker no Railway** baixa, pede ao fal as outras
   imagens e clipes, monta o cachorro final e devolve ao armazenamento do fal; o app baixa o resultado; o
   worker **apaga a cópia dele** quando acaba — e **mantém** quando falha, para tentar de novo.

Três coisas a levar para o Studio/Forge, que vivem de gerar asset por agente:

- o **estágio caro vem depois do pagamento**, e o estágio barato (uma imagem de confirmação) vem antes —
  é a mesma economia do "silhueta primeiro" da nossa criação de personagens, aplicada a custo de GPU;
- a **entrega é por URL de armazenamento de terceiro com validade curta**, não por anexo;
- o **estado de falha** do worker é "guarda a cópia e re-tenta", não "apaga e recomeça do zero".

E o aviso que eles mesmos escrevem e que vale para nós: *"qualquer outra coisa na foto vai junto — escolha
uma foto que mostre só o seu cachorro"*. Um produto que manda imagem do usuário a um gerador deveria
sempre dizer isso.

## 7. O que fica, o que sai, por quanto tempo

| Dado | Onde fica | Retenção declarada |
|---|---|---|
| configurações, nome, respostas do onboarding, lista de dispersão, agenda, números do dia, correções "Not a drift", chave, foto e imagens do cachorro, `install ID` | disco do usuário, "arquivos comuns protegidos pela conta" | até o usuário apagar (um comando no Mac, uma pasta no Windows) |
| texto julgado (app, URL sem query, título em 140 caracteres, contexto do usuário, últimos 6 vereditos) | **não** armazenado no servidor deles | zero; IP só em memória, para limitar taxa |
| veredito do modelo | cache no cliente | 6 h |
| registro da licença | Upstash | "não expira sozinho; peça e apagamos" |
| cachorro feito no celular | servidor deles | 30 dias (código) + 1 semana (IP do computador que resgatou) |
| contadores de uso | Upstash | diários por 400 dias; únicos diários por 120; totais históricos irreversíveis |
| foto/imagens no fal | armazenamento do fal | **"não definimos quanto tempo"** — a política deles devolve o problema ao provedor |

A última linha é a única sombra real no resto do texto: um arquivo gerado num terceiro que eles admitem
não controlar. É um ângulo que falta nas nossas próprias políticas (`cross-project/licensing/ASSET-PROVENANCE.md`
trata proveniência de quem cria, não retenção de quem gera).

## 8. Preço, experimentação e o demo que vende sozinho

- **Sem trial**: "não há período de teste: em vez disso, você vê ele fazer o trabalho e então decide". O
  onboarding abre o YouTube e o cachorro **fecha a aba de verdade**, na frente do usuário, antes de cobrar.
- Uma assinatura cobre os dois visuais (4 cachorros realistas + o filhete desenhado) em até 5 máquinas;
  cancela pelo menu do próprio app.
- **Preço por país**: eles declaram que "pessoas em muitos países, como Índia, **Brasil**, Turquia e grande
  parte da África veem preços menores" — derivado do IP pela Vercel, que não guardam.
- **Experimentação declarada**: metade das instalações vê plano mensal + anual mais barato; outra metade é
  levada direto a um **pagamento único**; o braço vem do `install ID`; cachorros feitos no celular têm braço
  próprio pelo código. Eles descrevem o A/B na **política de privacidade**, não num blog de produto.
- Justificativa do preço: *"quando o Bisqit encontra uma página que não reconhece, um modelo decide, e
  cada uma dessas checagens custa dinheiro a nós"*. Custo variável explícito como razão da assinatura, e a
  consequente ausência de anúncio/venda de dado.
- Eles **não** dão número de preço no site consultado — o valor aparece no app/Stripe. Não cotado aqui.

Para o Lia Project o padrão é duplamente útil: o "demo que executa a ação real no onboarding" é uma
mecânica de confiança barata, e o preço por país com A/B está documentado em texto público — o que dá
para citar sem copiar decisão.

## 9. O disclosure como peça de produto

Três frases que valem transcrição, porque são o oposto do usual:

| Frase deles | Por que é um padrão copiável |
|---|---|
| "Isso acontece em **todos** os apps, inclusive janelas privadas" | a exceção que o produto poderia esconder é escrita sem rodeio |
| "Encurtamos, mas **não conseguimos filtrar**" | admite o limite do mecanismo em vez de prometer anonimato |
| "Pausar o Bisqit impede o cachorro de fechar, **mas não de julgar**. Para parar de vez, saia do app." | separa o efeito visível do efeito de telemetria — a distinção que quase todo app omite |
| "Ainda **não existe** uma chave separada para desligar o julgamento por IA ou as contagens de uso" | publica a lacuna do próprio controle de privacidade |

Comparação direta com o que a nossa base cobra de terceiros: isto cumpre o espírito de
`governance/SECURITY-AND-PRIVACY-POLICY.md` §5 (dado do usuário em pesquisa) sem que ninguém tenha lido
código. É um formato de texto para o `lia-*` docs, não um código para importar.

## 10. O mesmo nicho, seis jeitos diferentes de ser feito (o "como" por contraste)

Busca livre, 2026-11-24; tudo auto-relatado pelas páginas oficiais dos concorrentes — nada foi
instalado nem conferido:

| Produto | O que o criador diz sobre como é feito | Contraste com o Bisqit |
|---|---|---|
| Furever Dock | "adicione seu próprio bichinho à tela"; foto → animação; gratuito para adotar, "um pet feito com suas fotos pode custar extra" (segundo a página de um concorrente) | é o alvo declarado da página `is-bisqit-safe` ("#1 Safest desktop pet / safe alternative to Furever Dock") |
| Dumple (Masko) | **US$ 18 únicos**, sem assinatura; "usa a internet só para confirmar que a sua cópia é sua e buscar os movimentos novos" | mesmo problema de custo, resposta inversa: pagamento único + rede mínima |
| Desktop Dog (`desktopdog.app`) | "sinais locais — teclado e ponteiro ficam no dispositivo"; **sem** permissão de Acessibilidade/Input Monitoring; só pede Gravação de Tela se você usar o print da ferramenta; SmartScreen contornado com "Mais info → Executar assim mesmo" | o caminho estreito: menos capacidade, menos permissão; o Bisqit escolheu o largo |
| Paw-Paw | app **nativo em Swift, macOS 13+**, Apple Silicon e Intel; clique passaThrough para a janela de baixo; "boa parte da arte e muito do código foi feito com ajuda de IA, e eu reviso, ajusto e testo tudo"; um extra opcional de US$ 2,99 | o disclosure de trabalho feito com IA, que é o que nós pedimos nos nossos relatórios e quase ninguém faz |
| AgentPet | macOS em Swift/SwiftUI, Windows em **Tauri (Rust)**, web em Astro + Cloudflare Workers/D1; estado dos agentes vem dos **hooks de cada ferramenta por socket local**; opcional login, "totalmente offline se pular o sign-in"; livre e aberto | o concorrente que resolve "o que o agente está fazendo" sem LLM: hook local em vez de julgar título de janela |
| Desktop Pet (`apps.apple.com` id 6792518134) | "1 a 3 fotos → conceito grátis de 3 vistas para confirmar o visual **antes de qualquer coisa ser feita** → algumas horas depois, animações em loop"; presets gratuitos; "nunca bloqueia seus cliques" | mesmo pipeline bifásico (confirmar barato, gerar caro depois), com humano no meio |

Duas lições transversais: (a) quem não tem IA no loop usa **hooks/telemetria local** (AgentPet) ou não
precisa de permissão nenhuma (Desktop Dog); (b) todo mundo que gera o pet a partir de foto separa
**confirmação barata** de **geração cara** — igual ao Bisqit. Não há, no nicho, uma terceira via.

## 11. Mapa para o Lia Project (o que levar, por destinatário)

| Destinatário | Padrão a levar | Custo de adoção |
|---|---|---|
| **Lia Project** — `lia-browser-automation` (hoje ❌, nota "risco de egress") | o conjunto mínimo de sinais: app em primeiro plano + título + URL sem query; lista local para o que é conhecido; cache de decisão por chave (6 h aqui); **nunca** ler conteúdo da página nem teclas | um classificador com fallback local; a lista do usuário é o que torna o resto barato |
| **Lia Project** — UX de permissão | dizer, antes de pedir, **para que** serve cada permissão, e uma vez por navegador no macOS; no Windows, explicar que UI Automation não pede nada | texto, não código |
| **Lia Project** — ação arriscada | grace period antes de agir (segurar o cachorro = +70 s), "Not a drift" persistente, e **minimizar em vez de fechar** para nunca destruir trabalho | três decisões de design, todas sem custo |
| **Lia Forge** — empacotamento | Mac assinado **e notarizado**; Windows sem assinatura **até** entrar na Store, com o aviso explicado na própria página; `defaults delete` como desinstalação documentada | checklist de release, não ferramenta |
| **Lia Forge** — preço/lançamento | demo que executa a ação real no onboarding em vez de trial; preço por país; A/B declarado publicamente | política do dono, não da pesquisa |
| **Lia Agent Hub** | veredito de IA com **cache no cliente** e chave de API **fora do app**, servidor como *proxy* que não persiste | mesmo formato que já propusemos para chamadas de classificação |
| **Lia Research** | a tabela "o que fica × o que sai × por quanto tempo × quem processa" como bloco obrigatório de todo relatório que envolva dado do usuário | ajuste de template |

Registrado também o **contra-exemplo**: o Bisqit julga **mesmo com o app pausado e fora do horário**. Um
produto nosso que ofereça "pausar" tem de decidir se pausa a coleta junto — nós temos vocabulário para
isso em `cross-project/security/PER-EXECUTION-PERMISSIONS.md` (escopo, delegação, revogação) e aqui está o
caso real que mostra o buraco.

## 12. O que não foi verificado, e por quê

| Item | Estado | Motivo |
|---|---|---|
| instalar/rodar o app; conferir se ele lê só o que diz | **`NOT_RUN`** — deliberado | é um binário proprietário fechando abas com permissão de Acessibilidade; esta base não instala terceiros em projeto Lia, e o sandbox não tem macOS nem Windows |
| baixar o `Bisqit-Dog.dmg` e conferir assinatura/notarização | `BLOCKED` | download fora da allowlist do ambiente; a `privacy.html` redireciona para o `.dmg`, que a ferramenta de leitura devolveu vazio (binário) |
| "assinado e notarizado", "sem anúncios", "não vendemos seu dado", "servidor não guarda" | `REPORTED` | só o texto deles; nenhuma verificação independente existe (sem fonte, sem auditoria publicada) |
| framework do app (Swift nativo? Tauri? outro?) | `UNVALIDATED` | indícios (`app.bisqit.mac`, `%APPDATA%\Bisqit`, "macOS 13+, Apple Silicon ou Intel") são **consistentes** com app nativo, não prova |
| preço em BRL | `NOT_RUN` | o preço é mostrado no app/checkout por país; não há página de preço no sitemap |
| existência de lista na Microsoft Store | `DIVERGENCE` interna do site | a `privacy.html` escreve "se você obtiver o Bisqit pela Microsoft Store" (como se houvesse); a `is-bisqit-safe` escreve "esse aviso some quando o Bisqit estiver na Store" (ainda não está). Não achamos listagem na busca que fizemos |
| "o trial" | `DIVERGENCE` | a política condiciona o julgamento a "assinatura **ou trial** ativo"; a página de preço afirma "não há período de teste". Um dos dois textos está defasado |
| termos de uso | ausente | o sitemap tem 8 URLs: `/demo`, `/desktop-dog`, `/desktop-pet`, `/dog`, `/focus`, `/free-desktop-pet`, `/is-bisqit-safe`, `/privacy.html` — nenhuma página de termos, licença ou reembolso; probes em `terms.html`, `terms-of-service.html`, `pricing.html` e `how-it-works` retornaram erro, enquanto `/demo.html` e `/privacy.html` respondem |
| LGPD/GDPR para um produto nosso com o mesmo desenho | não analisado | fora do escopo desta rodada; o processamento nos EUA é declarado por eles |
| custo por veredito em dinheiro | não cotado | dá para estimar em tokens (payload pequeno, cache de 6 h), mas o preço de tabela do modelo não foi conferido nesta rodada — não inventamos número |

Soma: **nada estrutural foi medido por nós aqui** — não há o que medir sem o binário. O que este relatório
entrega é a engenharia descrita pelo autor, lida em duas páginas que se cruzam sem se contradizer nos
pontos técnicos, o que é um bom sinal, não uma verificação.

## 13. Recomendação: **ADAPT**

Não `REFERENCE_ONLY`, porque três peças são transplantáveis hoje, sem código deles; não
`DIRECT_INTEGRATION_CANDIDATE`, porque não há artefato a integrar — o objeto é fechado.

1. **Adaptar o loop de classificação** (lista local → cache → modelo → correção do usuário persistida) como
   forma de qualquer função "sabe o que o usuário está fazendo" no Lia Project: §4.
2. **Adaptar o disclosure** (o que fica / o que sai / retenção / quem processa / o que ainda não dá para
   desligar) como bloco de texto nos nossos docs de feature: §9.
3. **Adaptar a política de ação** (grace de 70 s, "Not a drift", minimizar em vez de fechar): §11.
4. **Não levar**: assinatura como único modelo (o Dumple mostra o pagamento único no mesmo nicho), o
   A/B de preço por `install ID`, nem o julgamento ativo com o app pausado.

Próximos passos que fecham o que está `NOT_RUN`/`BLOCKED` — cada um exige máquina ou conta, então são do
dono, não meus:

1. numa Mac de teste, baixar o `.dmg` e rodar `spctl -a -vv` no `.app` (confirma a afirmação de
   notarização) e observar o tráfego com o app pausado × aberto — é o teste que prova ou não o §12 linha 7;
2. conferir o preço mostrado no Brasil, se o experimento de preço por país nos interessar como dado;
3. reabrir `is-bisqit-safe` e a política em 2027-02-24 (ou quando a Store aparecer): com dias de produto,
   o texto muda antes do código;
4. se o Lia Project decidir construir o `lia-browser-automation`, abrir `LR-FORGE-014` como base da
   discussão de escopo — a pergunta "extensão ou Acessibilidade?" precisa de resposta antes de código.

## 14. Evidências

| Afirmativa | Rótulo | Base (2026-11-24, UTC) |
|---|---|---|
| O site tem 8 URLs e nenhuma página de licença ou termos | `CONFIRMED` | `sitemap.xml` + `robots.txt` + probes com erro em `terms.html`, `terms-of-service.html`, `pricing.html`, `how-it-works` |
| Licença: nenhuma publicada; produto fechado | `CONFIRMED` (esgotamento do sitemap) + `REPORTED` (terceiros: AlternativeTo lista "Free · Proprietary · Mac · since 2026") | `bisqit.app/sitemap.xml`; listagem do AlternativeTo |
| macOS 13+ (Apple Silicon ou Intel) e Windows 10/11 64 bits; sem extensão de navegador | `REPORTED` | `/desktop-pet`, `/desktop-dog` |
| Lê app em primeiro plano, título, URL+título da aba (incl. privadas), posição do botão de fechar, hora do último teclado/mouse; nunca conteúdo nem teclas | `REPORTED` | `privacy.html` §"What Bisqit reads"; `/is-bisqit-safe` §"What Bisqit looks at" |
| Payload do julgamento: app, URL sem query, título em 140 caracteres, linha "o que você faz", *time sinks*, até 6 vereditos anteriores; cache local de 6 h; servidor não guarda | `REPORTED` | `privacy.html` §"To judge a page" |
| Cadeia Vercel + Upstash + OpenRouter→Gemini + fal + Railway + Resend + Stripe; chaves fora do app; desinstala por `defaults delete app.bisqit.mac` / `%APPDATA%\Bisqit` | `REPORTED` | `privacy.html` §"Who handles your information", §"Your choices", §"Security" |
| Preço por país com Brasil na lista de preço menor; A/B por `install ID` entre mensal+anual e pagamento único | `REPORTED` | `privacy.html` §"When you buy" |
| Onboarding fecha uma aba real do YouTube; sem trial; 5 máquinas por assinatura; custo de IA declarado como motivo do preço | `REPORTED` | `/free-desktop-pet` |
| Mac assinado e notarizado; Windows ainda sem assinatura até a Store | `REPORTED` (não verificável aqui) | `/is-bisqit-safe` §"Installing it safely" |
| Pipeline do cachorro personalizado: verificação por Gemini, primeiro frame no fal antes do pagamento, worker no Railway, retenções 1 dia / 1 semana / 30 dias | `REPORTED` | `privacy.html` §"To make your own dog" |
| Duas contradições internas do site: "trial" vs "sem trial"; Store no presente vs no futuro | `DIVERGENCE` | `privacy.html` × `/free-desktop-pet`; `privacy.html` × `/is-bisqit-safe` |
| Vídeo de demonstração *unlisted*, 22 s, canal `@buildwithask`, publicado 2026-11-11, 34 visualizações | `OBSERVED` | metadados públicos do YouTube (não assistido; transcrição sem fala, só música) |
| Nenhum repositório do Bisqit no GitHub; 5 resultados para a string, todos alheios (inclusive um simulador quântico) | `CONFIRMED` | `gh api search/repositories?q=bisqit` |
| Concorrentes: Dumple US$ 18 único e rede mínima; Desktop Dog sem permissão de Acessibilidade; AgentPet com hooks por socket local e Tauri no Windows; Paw-Paw nativo em Swift com arte e código assistidos por IA declarados; Furever Dock gratuito com custo na foto própria | `REPORTED` | páginas oficiais de cada um, via busca |
| Framework do app, comportamento real do binário, preço em BRL, notarização | `UNVALIDATED` | nada medido por nós; exige Mac de teste |

---

Voltar: índice `RESEARCH-INDEX.md` (seção 1) · catálogo `catalog/catalog.tsv` · política de privacidade
lida em `https://bisqit.app/privacy.html` (22/11/2026) · objeto de Skills e empacotamento mais próximo:
`LR-STUDIO-012` · padrão de permissão por execução: `LR-SEC-005` · lacuna que este objeto toca:
`lia-browser-automation` em `projects/lia-project/INDEX.md`.
