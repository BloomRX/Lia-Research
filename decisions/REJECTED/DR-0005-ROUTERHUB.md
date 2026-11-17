# DR-0005 — RouterHub não entra no catálogo de providers

| Campo | Valor |
|---|---|
| ID | DR-0005 |
| Estado | **REJECTED** |
| Dono da decisão | Research Orchestrator (recomendação) — reabertura exige proprietário |
| Data | 2026-11-17 |
| Escopo | inclusão como provider no catálogo da Lia |
| Pesquisa | `LR-PROV-001` (`repositories/routerhub/REPORT.md`) |
| Reversível? | sim, com as condições abaixo |

## Contexto
Serviço comercial que revende acesso a modelos sob API compatível com OpenAI/Anthropic,
posicionado em modelos "uncensored/abliterated", sem termos de serviço, política de
retenção ou procedência de modelos verificáveis na coleta.

## Evidência considerada
`E1` organização (não repositório); `E2` 11 repos, 8 MIT, 2 forks do LiteLLM;
`E4` nenhum repositório de backend; `E5` ToS/jurisdição `BLOCKED`; `E7` incoerência
técnica de "abliteration" em modelos de pesos fechados (`INFERRED`).

## Decisão
RouterHub **não** é incluído no catálogo padrão nem em lista de sugestão.

## Fora de escopo
Não proíbe o usuário de usar o serviço por conta própria, nem proíbe pesquisa futura.

## Consequências
Usuários não recebem recomendação de serviço com termos não auditáveis. Perde-se uma
opção de conveniência (API única, muitos modelos).

## Condição de reabertura
1. ToS + política de retenção/uso de dados publicadas, com jurisdição;
2. procedência/licença de cada modelo servido documentada;
3. política de segurança de chaves;
4. se listado: desabilitado por padrão, aviso de conteúdo e de que a Lia não audita o
   provedor, proibição de dados pessoais por padrão.
