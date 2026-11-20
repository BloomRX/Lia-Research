# Silhouette-first: método, linguagem de forma e avaliação

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-008` |
| Categoria | studio |
| Projetos | Lia Forge 2.0, Lia Studio |
| Fontes | 5 fontes de prática identificadas por título/autor/URL em §2.2; Pix3D (Sun et al., CVPR 2018) para o limite das métricas; CharNeRF (arXiv 2402.17115) para turnaround→3D; página pública do vídeo do pedido (transcrição parcial) para **descartar** a atribuição anterior |
| Data | 2026-11-20 |
| Revisão | 2026-11-20 (UTC) — 7.1: licença, hardware, vídeo e contagens; 7.3: conciliação Tripo/Meshy/Flow/ROCm |
| Status | CURRENT |
| Confiança | Média — o método converge entre fontes de prática; as métricas automáticas propostas são **hipótese não calibrada**; base bibliográfica é fraca e está declarada em §2.2 |
| Natureza | pesquisa e documentação; não autoriza implementação |

---

## 1. O que "silhouette-first" significa em termos operacionais

Não é "desenhar a silhueta primeiro" como etapa de arte. É uma **ordem de decisão**:

1. Decidir o que o personagem **é** (função, temperamento, escala, elenco).
2. Traduzir isso em **forma** — sem detalhe interno, sem cor, sem material.
3. Testar a forma isolada: reconhece? diferencia do resto do elenco? lê a 32 px?
4. Só então investir em conceito detalhado, sheet e 3D.

O argumento a favor é econômico, não estético: um erro de forma descoberto em blockout custa
horas de modelagem; descoberto em silhueta, custa minutos.

**Sobre o vídeo citado no pedido:** a rodada 7.1 obteve a página pública do vídeo, que é um
teste de modelos de linguagem para criação de jogos (MagmaDev, 2026-11-19) e **não descreve
esta sequência**. A atribuição anterior era erro e está registrada em
`CHARACTER-CREATION-RESEARCH.md` §1.1. A ordem acima vem **da ordem de pesquisa recebida do
proprietário**, e o apoio metodológico vem das fontes de prática de §2.2 — nada depende do
vídeo.

## 2. Base metodológica

### 2.1. O que a prática documenta

Cinco fontes independentes de prática de design (duas didáticas, três de estúdio) convergem
em quatro regras:

| Regra | Formulação encontrada | Por que importa para o Forge |
|---|---|---|
| Preencher em preto | "encher vinte miniaturas em preto sólido; se não é reconhecível como forma, nenhum detalhe salva" | o teste é objetivo e barato: dá para automatizar a extração |
| Ler em tamanho pequeno | "aperte os olhos; se virou borrão, refaça" | critério mensurável por redução de escala |
| Uma forma dominante | círculo, quadrado ou triângulo dominante, repetido em cabeça, corpo, props e postura | dá um eixo de comparação entre candidatos |
| Assimetria controlada | "assimetria lê como vivo" | evita elenco de silhuetas espelhadas |

Fonte primária de cada formulação: as cinco páginas listadas em §2.2. São material de
prática profissional, **não** estudo experimental: não existe, nas fontes que li, medição de
"quanto" a silhueta melhora reconhecimento. Registro isso como limitação, não como detalhe.

### 2.2. Fontes de prática consultadas (leitura em 2026-11-20)

| # | Título | Autor / instituição | URL | Data | Tipo | O que foi efetivamente lido | Qualidade da evidência |
|---|---|---|---|---|---|---|---|
| 1 | Shape Language Character Design | Heather Colbert (site pessoal de design) | `https://heather-colbert.com/shape-language-character-design/` | 2026-07-06 (indicada na página) | guia de estúdio, autoria individual | mapeamento traço→forma; teste em thumbnail; proporções 7–8 cabeças; checklist de escala | **baixa-média**: prática declarada, sem fonte citada |
| 2 | Character Design Principles (lista de revisão) | Fiveable (plataforma de estudo) | `https://fiveable.me/lists/character-design-principles` | sem data | material didático de terceiro | hierarquia "reconhecimento instantâneo antes de personalidade"; tabela de princípios | **baixa**: material de preparação, não fonte primária |
| 3 | Character design basics: from first sketch to concept art | Nextversity (escola/blog) | `https://nextversity.com/schools/graphic-design-illustration/blog/character-design-basics` | 2026-08-10 (indicada) | material didático | "vinte miniaturas em preto"; teste do borrão; assimetria; aviso de que estrutura importa | **baixa-média**: procedimento concreto e reproduzível |
| 4 | What Makes a Good Cartoon Character Design? 10 Essentials | Mimic Cartoon (estúdio) | `https://www.mimiccartoon.com/post/what-makes-a-good-cartoon-character-design` | 2026-08-14 (indicada) | post de estúdio | checklist: silhueta em preto, em miniatura e ao lado do elenco | **baixa-média**: prática de produção, sem metodologia |
| 5 | The Ultimate Guide to Character Design | Prints4Sure (blog comercial) | `https://www.prints4sure.com/blogs/news/the-ultimate-guide-to-character-design-principles-process-and-examples` | 2025-11-04 (indicada) | guia de blog | silhueta como "teste mais puro"; forma e legibilidade | **baixa**: conteúdo de marketing, uso apenas corroborativo |

**Limite honesto desta base:** são cinco fontes de prática, nenhuma acadêmica, nenhuma de
estúdio AAA com metodologia publicada. A convergência entre elas é o que sustenta o princípio —
**convergência de prática não é demonstração experimental**. Não encontrei, nas fontes que li,
livro técnico, GDC talk ou artigo revisado que quantifique o ganho de "silhueta primeiro".
Se o proprietário quiser subir o nível da evidência, o caminho é livro de referência de design
de personagem (comprar/ler) ou talk de estúdio — `BLOCKED` nesta sessão por não haver acesso.

### 2.3. O que a literatura técnica acrescenta

- **CharNeRF** (arXiv 2402.17115) trata explicitamente o insumo "turnaround consistente de
  três a cinco vistas, em T ou A" como o padrão da indústria de modelagem — o que valida a
  premissa do sheet canônico, e não só a silhueta.
- **Pix3D** (Sun et al., CVPR 2018) conduziu estudo comportamental **sobre reconstrução 3D de
  objetos a partir de imagem única** — inclusive a categoria *chair* — comparando métricas
  geométricas com julgamento humano. Reporta correlação de Spearman de **0,32** (IoU),
  **0,43** (EMD) e **0,49** (Chamfer) com a nota humana.
  **Uso adequado:** demonstra que métricas automáticas podem se correlacionar imperfeitamente
  com avaliação humana.
  **Uso inadequado (removido nesta rodada):** extrapolar para silhueta de personagem,
  reconhecimento de identidade, qualidade de sheet ou originalidade; e converter 0,49 em
  "menos de um quarto da variância" — essa conversão não está no estudo e não é legítima
  como inferência.

## 3. Linguagem de forma — o que dá para usar sem virar clichê

| Forma dominante | Leitura convencional | Uso típico | Risco |
|---|---|---|---|
| Círculo / arredondado | acolhedor, jovem, inofensivo | mascote, aliado, criança | vira genérico se todo o elenco for redondo |
| Quadrado / maciço | estável, confiável, pesado | guardião, ferreiro, tanque | rigidez visual, pouca leitura de ação |
| Triângulo / angular | rápido, perigoso, instável | vilão, assassino, velocista | excesso de espinhos = ruído em 32 px |
| Combinação dominante + contraponto | "este personagem é X, mas tem Y" | praticamente todo personagem memorável | exige disciplina: contraponto é 1, não 5 |

A tabela acima é convenção de prática, não regra universal. O Forge deve tratá-la como
**vocabulário configurável por Project Visual Profile**, não como verdade embutida.

### 3.1. Por arquétipo — o que muda no teste

| Tipo | O que a silhueta precisa provar | Erro comum |
|---|---|---|
| Humano estilizado | proporção (cabeças), postura, silhueta de roupa/cabelo | detalhe de rosto cedo demais |
| Criatura | massa e locomoção (quantas pernas? como anda?) | membros ilegíveis quando sobrepostos |
| Monstro | escala e ameaça (o que é maior que o quê) | silhueta simétrica e "blob" |
| Robô | articulação e peças (o que dobra, o que é rígido) | painéis que somem em miniatura |
| Mascote | leitura em 32 px e em uma cor | detalhe fino que vira sujeira |

## 4. Processo proposto (para o Forge, não implementado)

```
Character Brief  →  N silhuetas (20 sugerido)  →  triagem automática (ordenação)
                 →  revisão humana (aprovação)  →  Concept  →  Sheet
```

Regras que eu proporia como hipótese:

1. **Exploração ampla antes de refino.** 12–20 silhuetas, não 3. Variedade vem de *decisão*
   (proporção, postura, silhueta de roupa), não de *ruído* de seed.
2. **Exploração controlada.** Cada variação muda **um** eixo declarado (ex.: proporção
   cabeça:corpo) e registra o eixo no artefato. Sem isso, o histórico não ensina nada.
3. **Pose neutra primeiro.** A silhueta é avaliada em T/A/relaxado; pose de apresentação é
   etapa separada, porque pose esconde erro de forma.
4. **Elenco junto.** Aprovar um personagem isolado é meio teste: a pergunta é "diferencia dos
   outros?". O Forge precisa do conjunto, não do arquivo único.
5. **Congelar o aprovado.** Depois da aprovação, a silhueta vira referência imutável (hash),
   e toda etapa seguinte aponta para ela.

## 5. Critérios de avaliação — o que é legítimo medir

| Critério | Pergunta | Como medir (proposta) | Confiança no número |
|---|---|---|---|
| Legibilidade | reconhece sem detalhe interno? | silhueta preenchida + redução a 32/64 px; entropia de borda e nº de componentes | média — proxy razoável |
| Reconhecimento | o mesmo personagem é reconhecido entre vistas? | similaridade de embedding (DINOv2/CLIP) entre vistas | **baixa** — não calibrado para personagem |
| Originalidade | parece distinto do elenco e do corpus? | distância mínima a embeddings do elenco + acervo aprovado | **baixa** — "original" não é distância |
| Coerência com briefing | a forma responde ao texto? | comparação texto↔imagem (CLIP score) | **baixa** — sensível a prompt |
| Proporção | relação cabeça:corpo e membros | razões medidas sobre máscara/pose | média, se a pose for canônica |
| Adequação ao estilo | pertence ao mundo visual? | distância ao Style Lock | média, dentro do mesmo estilo |
| Legibilidade em miniatura | lê a 32 px? | mesma métrica de legibilidade em escala reduzida | média |
| Construtibilidade 3D | dá para modelar sem ambiguidade? | simetria, oclusão, nº de membros visíveis, T-pose | **baixa** — heurística |

A coluna "confiança" é a parte importante: **cinco dos oito critérios têm base fraca**. Isso
não os invalida como *ranking*, invalida como *veredito*.

### 5.1. Regra de uso das notas

1. Score **ordena**; humano **decide**.
2. Nenhum score bloqueia sozinho; no máximo sinaliza para revisão.
3. Toda nota carrega versão do modelo que a produziu — trocar de modelo muda a escala.
4. Score nunca é comparado entre projetos diferentes (Style Lock diferente, escala diferente).
5. Quando score e humano discordam, o caso vira exemplo de calibração, não erro a corrigir.

## 6. O que pode ser automatizado, e o que não pode

| Etapa | Automatizável? | Justificativa |
|---|---|---|
| Extração de silhueta (fundo → máscara) | **sim** | determinístico, com segmentação ou remoção de fundo |
| Preenchimento e normalização (recorte, escala, centralização) | **sim** | geometria pura |
| Teste de miniatura (32/64 px) | **sim** | reamostragem + métrica de borda |
| Contagem de membros / checagem de pose | **parcial** | estimador de pose erra em criatura/robô |
| Similaridade entre vistas | **parcial** | embedding serve para triagem; não para afirmar identidade |
| Diversidade do elenco | **parcial** | distância mede diferença, não qualidade da diferença |
| Originalidade real (risco de plágio) | **não** | exige busca em corpus e julgamento jurídico |
| Coerência narrativa com o briefing | **não** | é leitura de intenção |
| Aprovação | **não** | é decisão de produto |

### 6.1. Métricas que eu proporia primeiro (baratas e honestas)

1. **IoU entre silhuetas normalizadas** de variações do mesmo briefing — mede o quanto a
   exploração está repetindo a si mesma. Barato, sem modelo.
2. **Componentes conexos + área relativa** — com regra **por arquétipo** (ver §6.2): detecta
   membro colado ou arma fundida no corpo; **não** pune quem legitimamente tem peças soltas.
3. **Perímetro²/área** (compacidade) — separa forma "macia" de "espinhosa" sem julgar.
4. **Legibilidade a 32 px**: reduzir, reamostrar para o tamanho original e medir perda de
   contorno. Proxy, não verdade.

Nenhuma dessas quatro precisa de modelo de IA, e todas são reprodutíveis — o que as torna
auditáveis, ao contrário de "nota de beleza".

### 6.2. Regra de "componente conexo único" — corrigida

A versão anterior tratava "mais de um componente conexo" como sinal de erro. Isso está errado
para boa parte do elenco: **armas separadas, asas, caudas, chifres, acessórios, peças de roupa
independentes, elementos flutuantes e apêndices desacoplados** são legítimos — robôs, criaturas
e mascotes são justamente os casos em que a silhueta tem partes soltas.

Regra corrigida, configurável por arquétipo/estilo/projeto:

| Arquétipo | Componentes esperados | O que é anomalia |
|---|---|---|
| Humano estilizado | 1 (corpo+roupa) + N declarados (arma, cabelo solto) | 2ª cabeça, membro flutuante não declarado |
| Criatura | corpo + cauda + asas + chifres (declarados no brief) | peça não declarada ou peça declarada ausente |
| Robô / mecânico | várias peças rígidas, juntas visíveis | peça que colide/funde sem intenção |
| Mascote | 1 dominante, detalhe pequeno permitido | detalhe que desaparece a 32 px |
| Com acessório | +1 por item do inventário | item do inventário ausente |

Critério de aceitação operacional: **comparar o número de componentes com o inventário do
brief**, não com um número fixo. Sem inventário, o teste é `UNVALIDATED` — não "reprovado".

### 6.3. O que **não** proporia

- Um "score de personagem" único, de 0 a 100. Composto de métricas fracas vira confiança
  falsa e é impossível de auditar.
- Julgamento por LLM multimodal como aprovação. Serve como checklist textual ("a silhueta
  tem cauda?"), não como nota.
- Comparação de scores entre estilos (chibi × realista). Escalas não são comensuráveis.

## 7. Evidências e limites

| Afirmação | Evidência | Nível |
|---|---|---|
| Silhueta em preto é teste padrão de prática | 5 fontes de prática convergentes (§2.2) | `COMMUNITY_REPORTED` (prática profissional) |
| Ler em miniatura é critério de qualidade | idem | `COMMUNITY_REPORTED` |
| Linguagem de forma comunica temperamento | idem; convenção cultural | `COMMUNITY_REPORTED` |
| Métricas geométricas se correlacionam imperfeitamente com humano | Pix3D (CVPR 2018), Spearman 0,32/0,43/0,49 em reconstrução de objeto | `PAPER_OR_RESEARCH` |
| Turnaround 3–5 vistas é insumo padrão da indústria | CharNeRF (arXiv 2402.17115) | `PAPER_OR_RESEARCH` |
| As métricas propostas em §6.1 funcionam | **não testado** | `UNVALIDATED` |

## 8. Riscos

| Risco | Efeito | Mitigação |
|---|---|---|
| Automatizar aprovação | elenco homogêneo e "aprovado por número" | aprovação humana explícita, registrada |
| Silhueta bonita, modelo impossível | retrabalho no 3D | critério de construtibilidade + teste de blockout barato antes do sheet final |
| Estilo imposto pelo modelo | perda de identidade | Style Lock como entrada, não como saída do gerador |
| Viés de forma (todo herói quadrado) | elenco sem variedade | métrica de diversidade do elenco no pacote |

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `CHARACTER-SHEET-CONSISTENCY.md`
