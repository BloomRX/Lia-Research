# RouterHub — roteador de modelos "uncensored/abliterated"

| Campo | Valor |
|---|---|
| ID | `LR-PROV-001` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | STATIC_REVIEW_ONLY |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | providers |
| Projetos beneficiados | Lia-Project (provider opcional), Lia Model Lab (avaliação) |
| Fontes | `api.github.com/orgs/routerhubSI`, repositórios da organização (2026-11-17), descrição da org, `routerhub-repos.json` |
| SHA completo | — não determinado (ver motivo) |
| Proveniência do SHA | **INCOMPLETA_ORGANIZACAO** — organização, não um repositório: não existe commit único analisado |
| HEAD atual | — (organização: sem HEAD único; ver §Fontes) |
| Versão/commit analisado | não aplicável (serviço comercial + repos de marketing); commits individuais listados em §16 |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `routerhubSI/litellm` · HEAD `187f936cb345` · sem SHA analisado registrado |
| Próxima revisão | 2027-11-20 |
| Recomendação | **REJECT** (com `PENDENTE` nos fatos não verificáveis) |
| Licença | MIT nos repositórios de marketing; **serviço sem termos verificáveis** |
| Confiança | **Alta** para o que a organização declara; **Baixa** para tudo que depende do site (inacessível nesta coleta) |

---

## 1. Identificação

- **Nome:** RouterHub (`routerhub.si`)
- **URL:** https://github.com/routerhubSI (organização; **o link `github.com/routerhubSI` da
  ordem de serviço é uma organização, não um repositório** — resolvido por
  `api.github.com/users/routerhubSI` → `type: Organization`)
- **Organização:** `routerhubSI`, nome exibido "routerhub.si"
- **Bio oficial:** *"Uncensored and abliterated AI models via one OpenAI- and
  Anthropic-compatible API: Claude, GPT, Gemini, Grok, DeepSeek, GLM, Qwen and Kimi.
  Pay per token."*
- **Licença:** MIT nos repositórios públicos de conteúdo; o **serviço** não tem termos
  de serviço acessíveis nesta coleta (`BLOCKED`)
- **Versão/commit:** serviço; repositórios analisados em 2026-11-17
- **Status da pesquisa:** `CURRENT`
- **Recomendação:** **`REJECT`** para inclusão no catálogo padrão de providers

> Nenhuma chamada autenticada ao serviço foi feita. Nenhuma chave foi criada. Nenhum
> dado de usuário foi enviado. Toda a análise é documental (`REPORTED`/`OBSERVED`).

## 2. Resumo executivo

RouterHub é um serviço comercial que revende acesso a modelos de fronteira
(Claude, GPT, Gemini, Grok, DeepSeek, GLM, Qwen, Kimi) sob uma API compatível com
OpenAI e Anthropic, **com foco explícito em versões "uncensored" e "abliterated"**,
cobrando por token. A organização no GitHub tem 11 repositórios, quase todos material
de marketing/SEO (MIT) e dois forks do LiteLLM.

O problema não é técnico. É que **três coisas que a Lia precisa verificar antes de
oferecer um provider a um usuário final não estão verificáveis**: (a) termos de
serviço e política de retenção de prompt, (b) procedência legal dos modelos servidos,
especialmente versões "abliterated" que são modificações de pesos de terceiros, e
(c) jurisdição/tratamento de dados. Sem isso, incluir o RouterHub no catálogo padrão
transferiria um risco de natureza jurídica e de política para o usuário da Lia.

O caso de uso legítimo é restrito e sempre opt-in: um usuário avançado que queira
acessar um modelo filtrado, com aviso claro de que os termos do provedor não foram
auditados pela Lia.

## 3. O que resolve

| Problema | Alegação |
|---|---|
| Uma chave para muitos modelos | "One key. All your models." (`REPORTED`) |
| Compatibilidade com SDKs existentes | API compatível OpenAI e Anthropic (`REPORTED`) |
| Acesso a modelos sem filtro | "uncensored / abliterated" (`REPORTED`) |
| Pagamento por uso | "Pay per token" (`REPORTED`) |

Nenhuma das quatro foi verificada em execução. Nenhuma foi testada com uma chamada
real — por decisão de segurança, não por falta de curiosidade.

## 4. Arquitetura

Inferida a partir dos repositórios públicos:

```text
cliente (SDK OpenAI/Anthropic) → RouterHub API (não auditada)
                                   ├── LiteLLM (fork público, "Rust core + Python SDK")
                                   ├── roteamento para modelos de múltiplos fornecedores
                                   └── cobrança por token
```

- O fork do LiteLLM (`routerhubSI/litellm`, marcado `fork: true`, licença
  `NOASSERTION`) sugere que o gateway usa LiteLLM ou inspira-se nele. **Não é prova**
  de que a produção usa esse código (`INFERRED`).
- Não há repositório do serviço em si, do backend de cobrança, nem de infraestrutura.
- Nenhuma documentação técnica de SLA, limites de taxa, limites de contexto ou
  versionamento de modelos foi localizada nos repositórios analisados.

## 5. Funcionalidades

| Funcionalidade | Estado | Evidência |
|---|---|---|
| API compatível OpenAI | `REPORTED` | bio da org + repo `uncensored-ai-api` |
| API compatível Anthropic | `REPORTED` | bio da org ("Anthropic-compatible") |
| Catálogo multi-fornecedor | `REPORTED` | bio; repos por fornecedor (`kimi-`, `deepseek-`, `glm-`) |
| Avaliações publicadas | existe | `routerhub-model-evals` ("recorded GLM standard, uncensored and abliterated coding comparisons") |
| Comparações uncensored vs abliterated | existe | `uncensored-vs-abliterated-ai` |
| Status/SLA, rate limits, retenção, jurisdição | **não localizado** | `BLOCKED` |

## 6. Dependências

- Do lado da Lia: nenhuma (seria um provider HTTP opcional).
- Do lado do RouterHub: LiteLLM (provável), fornecedores upstream dos modelos,
  processador de pagamento — todos fora de visibilidade.

## 7. Requisitos de hardware e sistema

- Nenhum: é serviço remoto. Compatível com Windows/AMD do usuário por definição.
- Custo: por token, tabela não verificada (`UNVERIFIED`).

## 8. Segurança e privacidade

| Pergunta obrigatória | Resposta obtida | Rótulo |
|---|---|---|
| Política de retenção de prompts | não localizada | `BLOCKED` |
| Uso de prompts para treino | não localizado | `BLOCKED` |
| Como as chaves são armazenadas | não localizado | `BLOCKED` |
| Jurisdição e subprocessadores | domínio `.si` (Eslovênia) é a única pista | `INFERRED` (não confirmado) |
| Logs de conversa | não localizado | `BLOCKED` |
| Termos de serviço | não acessíveis na coleta (site fora dos hosts permitidos) | `BLOCKED` |
| Conformidade (GDPR ou outra) | não localizada | `BLOCKED` |

Nenhuma dessas lacunas é acusação. É a razão pela qual a recomendação não pode ser
favorável: **um provider que processa conversas pessoais sem política verificável não
entra no catálogo padrão de um assistente pessoal.**

## 9. Licença e proveniência

Três camadas, todas problemáticas ou não verificadas:

1. **Repositórios de marketing:** MIT (`CONFIRMED`: `uncensored-ai-api`,
   `uncensored-models`, `kimi-uncensored`, `deepseek-uncensored`,
   `glm-5.3-abliterated`, `openrouter-alternative`, `uncensored-vs-abliterated-ai`,
   `routerhub-model-evals`). MIT de README não licencia o serviço.
2. **Gateway:** fork do LiteLLM com licença `NOASSERTION` no GitHub — precisa leitura
   manual. LiteLLM upstream é MIT com componentes de outras licenças.
3. **Modelos servidos:** a camada crítica. "Abliterated"/"uncensored" são
   **modificações de pesos** de modelos de terceiros. Cada modelo base tem licença
   própria (frequentemente com cláusulas de uso aceitável, proibição de remover
   salvaguardas ou restrições de uso comercial). Servir uma versão modificada de
   Claude/GPT/Gemini — modelos proprietários sem pesos públicos — é conceitualmente
   incompatível com a origem: **não há como "abliterar" um modelo fechado sem acesso
   a pesos**. Isso levanta questão direta sobre o que está sendo servido sob esses
   nomes (`INFERRED`, com base em fato técnico: modelos de API fechada não expõem pesos).
4. **Distribuição:** se a Lia listar esse provider, a Lia passa a recomendar um serviço
   cuja legalidade da oferta não pode verificar.

Classe de aproveitamento: `BLOCKED` (não por licença do repositório, mas por
impossibilidade de verificar a cadeia de direitos do produto vendido).

## 10. Maturidade e manutenção

| Indicador | Valor | Leitura |
|---|---|---|
| Organização no GitHub | 11 repos, criados recentemente | presença nova |
| Estrelas | 413 (`uncensored-ai-api`), 351 (`glm-5.3-abliterated`), 171 (`uncensored-models`) | marketing ativo; números modestos |
| Repositórios de código do serviço | **nenhum** | opacidade total do backend |
| Documentação técnica | ausente nos repos | — |
| Histórico/SLA | não localizado | `BLOCKED` |

## 11. Custos e limitações

- Preço por token: não verificado (`UNVERIFIED`); nenhuma chamada feita.
- Limite de contexto, rate limit, disponibilidade, versionamento de modelo: todos
  `BLOCKED`.
- Custo de integração baixa (API compatível), custo de **risco** alta.

## 12. Compatibilidade com o ecossistema Lia

| Requisito | Atende? |
|---|---|
| API compatível OpenAI/Anthropic (integração técnica) | `REPORTED` sim |
| Política de dados verificável | **não** |
| Procedência legal dos modelos | **não verificável** |
| Alinhamento com a política de providers da Lia | **não** |
| Provider opcional e desativável | sim, tecnicamente |

## 13. Projetos beneficiados

| Projeto | Como |
|---|---|
| Lia-Project | apenas como provider opcional *opt-in*, se algum dia aprovado |
| Lia Model Lab | como objeto de avaliação de qualidade de modelos abertos alternativos |

## 14. Oportunidades de reutilização

Praticamente nenhuma de código. Duas de **método**:

1. `routerhub-model-evals` publica comparações "standard vs uncensored vs abliterated"
   — o desenho desse tipo de avaliação é útil para a bancada do Model Lab medir o
   custo de qualidade de modelos filtrados.
2. A existência do serviço é evidência de demanda por "API única, muitos modelos" —
   exatamente o problema que o catálogo de providers da Lia resolve internamente.

## 15. Riscos e incompatibilidades

| # | Risco | Severidade | Probabilidade | Mitigação |
|---|---|---|---|---|
| R1 | Retenção/uso de prompts desconhecidos em conversas pessoais | **alta** | desconhecida | não incluir no catálogo padrão |
| R2 | Procedência legal dos modelos "uncensored" de fornecedores fechados | **alta** | alta | não recomendar; exigir documentação |
| R3 | Violação de ToS de fornecedores upstream transferindo risco ao usuário | **alta** | média | aviso explícito se algum dia listado |
| R4 | Chaves do usuário em serviço sem política de segurança publicada | **alta** | média | nunca armazenar; exigir política |
| R5 | Jurisdição/transferência internacional de dados | média | desconhecida | documentar antes |
| R6 | Mudança de catálogo/preço sem aviso (serviço comercial) | média | alta | revisão a cada 30 dias |
| R7 | Conteúdo sem filtro chegar a usuário não avisado | média | média | aviso de conteúdo + opt-in |

## 16. Evidências e fontes

| # | Afirmação | Rótulo | Evidência | Data |
|---|---|---|---|---|
| E1 | `routerhubSI` é organização, não repositório | CONFIRMED | `GET /users/routerhubSI` → `type: Organization` | 2026-11-17 |
| E2 | 11 repositórios; 8 MIT, 2 forks (`litellm`, `litellm-docs`) | CONFIRMED | `GET /orgs/routerhubSI/repos` | 2026-11-17 |
| E3 | Posicionamento "uncensored/abliterated", API OpenAI+Anthropic, pay per token | CONFIRMED (como declaração) | bio da organização | 2026-11-17 |
| E4 | Nenhum repositório de backend do serviço | CONFIRMED | listagem da org | 2026-11-17 |
| E5 | Termos de serviço / retenção / jurisdição | BLOCKED | site fora dos hosts acessíveis nesta coleta | — |
| E6 | Preço por token | UNVERIFIED | não consultado | — |
| E7 | Modelos fechados não expõem pesos → "abliteration" de modelo fechado é tecnicamente incoerente | INFERRED | conhecimento técnico + nomes no catálogo declarado | — |
| E8 | Qualidade real dos modelos servidos | BLOCKED | exigiria chamadas reais com conta | — |

## 17. Recomendação

**`REJECT`** para o catálogo padrão de providers da Lia, mantendo a pesquisa em
`decisions/REJECTED/` com condição de reabertura.

Justificativa: a integração é tecnicamente trivial, e é exatamente por isso que o
risco é desproporcional — a Lia estaria recomendando a seus usuários um serviço cujo
tratamento de dados, termos e procedência de modelos não podem ser verificados, e cujo
próprio posicionamento (revender modelos fechados como "abliterated") levanta dúvida
sobre a cadeia de direitos.

**Condições de reabertura** (todas necessárias):

1. publicação de termos de serviço e política de retenção/uso de dados, com jurisdição;
2. documentação da procedência de cada modelo servido (licença do modelo base);
3. política de segurança de chaves;
4. se listado algum dia: **provider desabilitado por padrão**, aviso de conteúdo,
   aviso de que a Lia não audita os termos do provedor, e proibição de uso com dados
   pessoais por padrão.

**Não autoriza:** criar conta, testar chamadas, adicionar como provider, ou mencionar
o serviço como opção recomendada.

## 18. Próximos passos

| # | Ação | Dono | Conclusão |
|---|---|---|---|
| 1 | Registrar decisão `REJECTED` com condições de reabertura | Research | `decisions/REJECTED/DR-0005` |
| 2 | Consultar termos e política de privacidade do site (fora do sandbox atual) | proprietário | evidência para reabrir ou encerrar |
| 3 | Não incluir em nenhuma lista de providers até (2) | Lia-Project | garantir |
| 4 | Usar `routerhub-model-evals` apenas como referência de método de avaliação | Model-Lab | nota de método |
| 5 | Revisar em 30 dias se houver nova informação pública | Research | — |

## Reauditoria 2026-11-20

| Campo | Valor |
|---|---|
| Versão anteriormente analisada | ``—` (organização + serviço comercial; sem commit único)` |
| Versão novamente examinada | ``—` (11 repositórios; o fork `routerhubSI/litellm` tem HEAD próprio, mas não é o objeto)` (2026-11-20) |
| Método | `compare` da API do GitHub (commits + arquivos), leitura de arquivos materiais no HEAD, estado de CI no HEAD, releases |
| Mudanças encontradas | Sem mudança detectada nos repositórios de marketing da organização. Termos do serviço **não foram reverificados** nesta rodada (exigiria abrir o site e ler contrato). |
| Evidências novas | A proveniência segue incompleta por desenho: `DR-0005` rejeitou o **fork**, e o objeto avaliado é o produto. |
| Testes próprios | Não executado: serviço comercial; testar exigiria conta e pagamento (Nível 3). |
| Testes independentes | CI no HEAD: não aplicável. |
| Conclusão | Recomendação **reavaliada e mantida em `REJECT`**. Os termos continuam `BLOCKED` como lacuna declarada. |
| Próxima revisão | 365 dias. |

