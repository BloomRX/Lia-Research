# FreeLLMAPI — agrega free tiers num único `/v1`, com roteamento e orçamento por chave

| Campo | Valor |
|---|---|
| ID | `LR-MODEL-006` |
| Categoria | model |
| Projetos beneficiados | Lia Model Lab (roteamento), Lia Agent Hub (provider adapter), Lia-Research (política de termos) |
| Fontes | `tashfeenahmed/freellmapi@main` (2026-11-19): `README.md`, `LICENSE`, API do GitHub; site freellmapi.co/models |
| Data | 2026-11-17 |
| Próxima revisão | 2027-02-17 |
| Status | CURRENT |
| Recomendação | **REFERÊNCIA** — o desenho de roteamento/orçamento serve; o serviço, não |
| Licença | MIT (`CONFIRMED`) — a licença do **software**, não dos provedores que ele agrega |
| Confiança | Alta para o que o README declara; **UNVERIFIED** para conformidade com termos de uso |

---

## 1. Identificação

| Item | Valor |
|---|---|
| Repositório | https://github.com/tashfeenahmed/freellmapi · site https://freellmapi.co |
| Métricas | ★ **55.337** · 31 MB · TypeScript · criado 2026-04-21 · push 2026-11-19 |
| Licença | MIT |
| Distribuição | self-host (Docker), apps macOS/Windows/Android/iOS, Store |

## 2. Resumo executivo

É um **agregador de free tiers**: 87 provedores, 1.313 endpoints gratuitos, atrás de um
`/v1` compatível com OpenAI. Faz três coisas bem: **roteia** para o melhor modelo
disponível, **falha para o próximo** quando um provedor limita, e **contabiliza uso por
chave** para não estourar cota.

O desenho técnico é diretamente aplicável ao problema que o Model Lab tem hoje (54
providers lidos, 0 medidos, roteamento inexistente). O **uso prático**, não: agregar free
tiers de terceiros é campo minado de termos de uso — o próprio repositório se descreve como
"personal experimentation only". Isso precisa estar escrito com todas as letras antes de
qualquer projeto pensar em depender dele.

## 3. O que resolve

| Problema | Solução |
|---|---|
| Muitos provedores, contratos diferentes | um endpoint compatível com OpenAI |
| Estourar cota gratuita sem perceber | orçamento e uso por chave |
| Provedor limitou no meio da tarefa | failover automático |
| Catálogo de modelos desatualiza | feed assinado; snapshot mensal no plano gratuito |
| Chaves espalhadas | armazenamento cifrado |

## 4. Arquitetura (como descrito)

```text
cliente (OpenAI-compatible) → /v1
        │
        ├── router: escolhe modelo conforme pedido/cota/capacidade
        ├── contadores por chave (evita estourar free tier)
        ├── failover para o próximo provedor em 429/erro
        └── catálogo (feed assinado; snapshot mensal no gratuito, diário no pago)
```

## 5. Funcionalidades

Chat/embedding/imagem/áudio por endpoint compatível · roteamento · failover · uso por
chave · chaves cifradas · catálogo assinado · clientes desktop/mobile · Docker.

## 6. Dependências

Node/TypeScript para rodar; Docker para self-host; contas nos provedores de origem (cada uma
com seus próprios termos).

## 7. Requisitos de hardware e sistema

Nenhum requisito de GPU no agregador; o custo é de rede e de cadastro em 87 serviços.

## 8. Segurança e privacidade

| Item | Situação |
|---|---|
| Chaves | cifradas no produto (`REPORTED`) |
| Tráfego | **o conteúdo das requisições passa por provedores de terceiros** — a política de privacidade de cada um se aplica |
| Terceirização | um intermediário a mais no caminho; para dados de usuário da Lia, isso é decisão de privacidade, não de engenharia |
| Termos | **risco principal** (ver §9) |

## 9. Licença e proveniência

Duas camadas que **não** se confundem:

1. **Software**: MIT (`CONFIRMED`) — pode forkar, modificar, usar comercialmente, com aviso.
2. **Serviço que ele agrega**: cada free tier tem termos próprios, e a maioria proíbe
   revenda/agregação automatizada ou exige atribuição/cota por aplicação. O repo se
   descreve como **"personal experimentation only"** (`CONFIRMED` na descrição).

Logo: MIT no código **não** concede direito de usar os free tiers de terceiros. Esta é a
mesma armadilha registrada em `LR-PROV-001` (RouterHub): licença permissiva do invólucro,
licença desconhecida do que ele serve.

## 10. Maturidade e manutenção

★55.337, 7 meses, push no dia da coleta, CI por badge, apps publicados em 3 lojas, modelo
de negócio (US$ 19/ano pelo catálogo ao vivo) — produto real. `UNVERIFIED`: se o catálogo
declarado corresponde ao que os provedores permitem hoje.

## 11. Custos e limitações

Gratuito = snapshot de 30 dias do catálogo; pago = ao vivo. Custo escondido: cadastro em
dezenas de serviços, termos de uso, e fragilidade (provedor pode cortar free tier).

## 12. Compatibilidade com o ecossistema Lia

| Dimensão | Situação |
|---|---|
| Windows 11 | sim (app publicado) |
| Electron/Vue | consome por HTTP — integrável |
| Skills/MCP | não é MCP, é API compatível com OpenAI |
| Licença | MIT |
| **Conformidade** | **não verificada** — bloqueia uso em produto |

## 13. Projetos beneficiados

**Model Lab** (desenho de roteamento e orçamento por chave) · **Agent Hub** (adapter de
provider) · **Lia-Research** (política de termos de uso de agregação).

## 14. Oportunidades de reutilização

| # | Prática | O que copiar |
|---|---|---|
| F1 | **Orçamento por chave com contagem** | evita surpresa de cota em qualquer provider |
| F2 | **Failover com registro de motivo** | troca de modelo auditável, não silenciosa |
| F3 | **Catálogo assinado** | atualização de catálogo sem `git pull` |
| F4 | **`/v1` compatível** | trocar provedor sem tocar no cliente |

## 15. Riscos e incompatibilidades

| Risco | Severidade |
|---|---|
| Violar termos de free tiers | **alta** — pode derrubar conta e produto |
| Conteúdo do usuário passar por intermediário | alta (privacidade) |
| Catálogo envelhecer/cortar | média |
| Dependência de 87 terceiros | média |

## 16. Evidências e fontes

| # | Evidência | Rótulo |
|---|---|---|
| E1 | MIT, ★55.337, TypeScript, push 2026-11-19 | CONFIRMED (API) |
| E2 | 87 provedores, 1.313 endpoints, `/v1` compatível | REPORTED (README) |
| E3 | Roteamento, failover, uso por chave, chaves cifradas | REPORTED (README) |
| E4 | "Personal experimentation only" | CONFIRMED (descrição do repo) |
| E5 | Conformidade com termos dos provedores | **UNVERIFIED** — e não é verificável por leitura |
| E6 | Qualidade do roteamento | **UNVERIFIED** |

## 17. Recomendação

**VEREDITO: `REFERÊNCIA`.** Copiar o **desenho** (F1–F4) para o roteamento da Lia — é
exatamente o que falta em `LR-MODEL-005`. **Não** usar o agregador como dependência de
produto: a licença MIT cobre o código, não os free tiers, e o próprio autor restringe o uso
a experimentação pessoal.

Se o proprietário quiser usar como ferramenta pessoal de teste de modelos, isso é decisão
dele; o que esta base registra é que **não pode virar caminho de produto** sem parecer sobre
termos de uso.

## 18. Próximos passos

| # | Ação | Dono | Gate |
|---|---|---|---|
| 1 | Escrever o desenho de orçamento por chave + failover no Model Lab | Model Lab | `DR-0020` |
| 2 | Registrar política: agregação de free tier não entra em produto | Lia-Research | decisão do proprietário |
| 3 | Comparar com `litellm` (upstream) antes de qualquer gateway caseiro | Lia-Research | fila da triagem |
| 4 | Se usar pessoalmente, medir o roteamento e registrar | Model Lab | — |
