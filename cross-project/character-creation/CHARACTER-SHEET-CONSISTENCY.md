# Character sheet e consistência entre vistas

| Campo | Valor |
|---|---|
| ID | `LR-STUDIO-009` |
| Categoria | studio |
| Projetos | Lia Forge 2.0, Lia Studio |
| Fontes | catálogo `LR-MODEL-007` (licenças e hardware), READMEs de MV-Adapter / IP-Adapter / Qwen-Image-Edit / CharTurner (Civitai), CharNeRF (arXiv 2402.17115) |
| Data | 2026-11-20 |
| Revisão | 2026-11-21 (rodada 7.1: nenhuma afirmação deste documento foi invalidada; correções do conjunto em `CHARACTER-CREATION-RESEARCH.md` §8-ter) |
| Status | CURRENT |
| Confiança | Média — problema bem documentado na prática; nenhuma solução foi executada |
| Natureza | pesquisa e documentação; não autoriza implementação |

---

## 1. Por que o sheet é o gargalo real

O pedido trata o sheet como etapa 5. Na prática ele é o **contrato** entre 2D e 3D: sem
vistas coerentes, o modelador (humano ou IA) inventa o que não vê. E é onde a geração por
difusão falha mais, porque cada imagem é gerada de forma independente — não existe memória
do que foi decidido na vista anterior.

CharNeRF descreve o insumo padrão da indústria como **três a cinco vistas** (frente, perfil,
costas, opcional 3/4), em T ou A. É esse contrato que o pipeline precisa produzir.

## 2. Conteúdo mínimo de um sheet útil para 3D

| Item | Obrigatório? | Por quê | Falha típica |
|---|---|---|---|
| Frente neutra | sim | é a vista de comparação | pose com braço sobre o corpo esconde silhueta |
| Perfil | sim | profundidade de crânio, tórax, quadril | perfil "achatado" por falta de referência |
| Costas | sim | cabelo, mochila, caudas, capa | acessório que existe na frente desaparece |
| Três quartos | recomendado | resolve ambiguidade de volume | proporção muda em relação à frente |
| Ortográficas (sem perspectiva) | recomendado | é o que o 3D espera | perspectiva na frente e ortográfica no perfil = retrabalho |
| Pose neutra (T/A) | sim | evita oclusão e permite medir | pose dramática aprovada como "sheet" |
| Expressões | opcional | rigging facial | gera 8 expressões antes de resolver a forma |
| Detalhe de rosto | opcional | modelagem de cabeça | close que contradiz a vista frontal |
| Cabelo (frente/perfil/costas) | sim, se houver | é o item mais inconsistente | comprimento muda entre vistas |
| Roupas (frente/costas) | sim | costura, gola, bolsos | fecho muda de lado; bolso aparece/some |
| Acessórios | sim, com inventário | objeto pequeno é o primeiro a sumir | coldre na perna direita vira esquerda |
| Medidas / proporções | sim | validar 3D contra 2D | "7 cabeças" no texto, 6,2 na imagem |

## 3. Por que a consistência quebra (causas, não sintomas)

| Causa | Mecanismo | Sintoma visível |
|---|---|---|
| Geração independente por vista | cada imagem parte de ruído novo + prompt | roupa e proporção mudam |
| Prompt subespecificado | o modelo preenche lacuna | bolso "inventado" |
| Resolução/zoom diferente | detalhe só existe onde há pixels | acessório aparece grande na frente e ausente no perfil |
| Referência ambígua | uma imagem só, sem vista lateral | modelo escolhe um volume plausível, não o seu |
| Atenção global (não local) | a identidade "compete" com pose | rosto consistente, roupa inconsistente |
| Modelo treinado em sheet | aprendeu layouts de folha, não personagens | layout bonito, personagem diferente em cada quadro |
| Estilo do LoRA | o LoRA domina o conceito | personagem parece do dataset do LoRA |

## 4. Técnicas que reduzem o problema — com força real

| Técnica | Como funciona | Reduz o quê | Limite | Evidência |
|---|---|---|---|---|
| Prompt estruturado com inventário | lista fixa de itens (cabelo, casaco, coldre) repetida em cada vista | invenção e desaparecimento | não corrige geometria | prática; `OBSERVED` |
| Referência por imagem (IP-Adapter, DreamO, UNO) | injeta embedding da imagem aprovada | estilo, paleta, rosto | detalhe fino se perde | documentação dos projetos; `REPORTED` |
| Edição a partir da vista aprovada (Qwen-Image-Edit, Kontext) | gera a vista nova **editando** a existente | mudança de roupa e proporção | exige modelo de edição forte | README + licença; `REPORTED` |
| Adapter multi-view (MV-Adapter) | uma passada gera conjunto de vistas consistentes | coerência geométrica entre vistas | preso a SDXL; qualidade limitada | paper/repo; `REPORTED` |
| ControlNet de pose/depth | fixa a geometria por mapa | pose, silhueta, perspectiva | mapa ruim = resultado ruim | `CONFIRMED` como técnica |
| Sheet em grade única | tudo numa imagem (uma geração) | consistência entre células | resolução por vista cai | prática (CharTurner); `REPORTED` |
| Fine-tuning por personagem (LoRA) | aprende o personagem | identidade em várias poses | custo por personagem; risco de overfit | `CONFIRMED` como técnica |
| Congelar referência + hash | não regenerar o aprovado | perda silenciosa da referência | disciplina de processo | proposta; `UNVERIFIED` |

### 4.1. Ordem de eficácia que eu proporia

1. **Editar em vez de gerar** (vista nova derivada da aprovada) — ataca a causa raiz.
2. **Grade única** quando o modelo suporta — barato e surpreendentemente eficaz para
   exploração, ruim para produção por perda de resolução.
3. **Multi-view adapter** quando há modelo compatível — melhor coerência, menos controle.
4. **Referência por imagem** como reforço, não como solução.
5. **LoRA por personagem** só quando o personagem vai render dezenas de imagens.

## 5. Preservar a referência aprovada

Regra de produto que a pesquisa sustenta: **o aprovado não é recriado, é versionado.**

| Prática | Implementação possível (sem escrever código aqui) |
|---|---|
| Hash do arquivo aprovado | registrar SHA-256 no artefato de proveniência (`LR-LIC-002`) |
| Vista canônica imutável | frente neutra aprovada é a única fonte das demais |
| Derivação registrada | cada vista nova aponta para o pai + técnica usada |
| Style Lock separado do personagem | estilo é do projeto; personagem é do asset |
| Diff visual em cada revisão | comparar silhueta nova × aprovada; divergência é decisão, não ruído |

## 6. Checklist de QA de sheet (o que dá para automatizar)

| Verificação | Automatizável | Como |
|---|---|---|
| Todas as vistas presentes e nomeadas | **sim** | estrutura de arquivos/manifesto |
| Mesma altura na imagem (normalização) | **sim** | bounding box da silhueta |
| Contagem de membros visíveis | parcial | pose estimation; falha em criatura |
| Simetria aproximada de acessórios | parcial | comparar lado esquerdo/direito da máscara |
| Inventário de acessórios presente | parcial | detecção por segmentação com texto (exige modelo) |
| Proporção cabeça:corpo consistente | parcial | medição sobre pose canônica |
| Coerência de cor de roupa | **sim** | histograma por região |
| Silhueta da vista nova ≈ aprovada | **sim** | IoU após normalização |
| "Está bom para modelar" | **não** | julgamento |

As verificações "sim" são suficientes para pegar os erros mais caros (vista faltando,
personagem desalinhado, altura mudada, cor trocada, silhueta divergente) sem nenhum modelo
de IA — e todas são auditáveis.

## 7. O que não funciona, apesar de parecer que funciona

| Ideia | Por que falha |
|---|---|
| Pedir "character sheet, 6 views" e confiar | vira folha bonita com personagens diferentes; resolução por vista insuficiente |
| Usar seed fixa como garantia de consistência | seed fixa dá variação correlacionada, não identidade |
| Consistência por prompt negativo | não cria memória |
| Aprovar sheet com uma vista "quase" certa | o 3D herda o erro e amplia |
| Confiar em "turnaround" de embedding comunitário (CharTurner) como padrão de produção | é ajuda de geração (SD1.5), sem garantia de layout nem de licença clara para redistribuição |

## 8. Limites desta análise

- Não executei MV-Adapter, IP-Adapter, Qwen-Image-Edit nem CharTurner; a força relativa das
  técnicas em §4.1 é **inferência a partir de documentação**, não medição.
- Não avaliei licença de embeddings comunitários do Civitai; a plataforma tem termos próprios
  e o modelo pode ter restrições não declaradas no cartão.
- Não há número de qualidade visual comparando as técnicas.

Voltar: `CHARACTER-CREATION-RESEARCH.md` · `SILHOUETTE-FIRST-DESIGN-RESEARCH.md` · `CHARACTER-2D-TO-3D-PIPELINES.md`
