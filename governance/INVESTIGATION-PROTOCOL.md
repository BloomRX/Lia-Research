# Protocolo de investigação — de um link solto a um relatório publicável

| Campo | Valor |
|---|---|
| Documento | Procedimento operacional de investigação |
| Versão | 1.1 — 2026-11-24 (incorpora o protocolo contínuo de links do proprietário, `decisions/ACCEPTED/DR-0019-PROTOCOLO-CONTINUO-DE-LINKS.md`) |
| Canônico em | este arquivo |
| Relacionado | `decisions/ACCEPTED/DR-0019-PROTOCOLO-CONTINUO-DE-LINKS.md` (norma do dono) · `MISSION.md` (autoridade) · `governance/TESTING-PROTOCOL.md` (experimentação) · `catalog/CATALOG-SCHEMA.md` (formato) |

---

## Etapa 0 — Entrada do link (sem briefing)

O dono manda um link, vários, ou só um nome. **Não se pede formulário.** A entrada está completa
quando se pode responder: (a) o que é e qual a fonte oficial; (b) se há relação entre os links —
**relacionados · complementares · concorrentes · independentes** — porque isso decide se a saída é
um dossiê por objeto, um comparativo ou um inventário; (c) o que este objeto pode mudar no que a
base já sabe.

Três regras de entrada:

1. **não presumir capacidade pelo nome, descrição ou README** — a lista de recursos do fornecedor é
   hipótese até aparecer no código, na interface ou num teste;
2. **antes de investigar, procurar o registro anterior** (`grep` no índice e no catálogo): se o
   objeto já foi tratado, a rodada procura **novidade ou lacuna relevante**, não refaz o trabalho;
3. **perguntar ao dono só o indispensável** — o que medição, leitura de arquivo ou busca resolvem, a
   Research resolve.

## Rótulos — equivalência com o protocolo do dono

O protocolo do dono nomeia cinco estados. Nesta base o vocabulário é o do validador
(`tools/validate.py`), e a correspondência é fixa:

| Termo do protocolo | Forma canônica aqui |
|---|---|
| `DOCUMENTED` | `Estado da pesquisa = DOCUMENTED`; evidência `CONFIRMED` (lido na fonte) ou `REPORTED` (afirmação do fornecedor) |
| `TESTED` | `Estado = TESTED` + `Resultado de execução = LOCAL_TESTS_PASS`/`LOCAL_SMOKE_PASS`/`OFFICIAL_CI_REVIEWED` + **linha obrigatória** em `data/testing/test-log.tsv` |
| `PARTIALLY_TESTED` | `Estado = PARTIALLY_TESTED` + `Resultado = PARTIAL`, com o que **não** foi testado nomeado no test-log |
| `UNVERIFIED` | rótulo `UNVALIDATED`; e `NOT_RUN` quando a verificação era possível aqui e não foi feita |
| `BLOCKED` | `Resultado = BLOCKED` (impedimento de execução) ou `Estado = BLOCKED` (impedimento de acesso), **com a limitação medida** |

`NOT_RUN` ≠ `BLOCKED`: o primeiro é dívida assumida desta base ("dava para fazer"), o segundo é
limite demonstrado ("falta ferramenta/conta/rede, e isto foi medido"). Citar `BLOCKED` sem a
limitação medida é a mesma falha de afirmar capacidade sem teste.

## Etapa A — Identificação

Antes de qualquer julgamento, responder por escrito:

| Pergunta | Onde buscar |
|---|---|
| O que é? | fonte oficial, não o agregador |
| Quem desenvolve/mantém? | org, autor, commits, licença |
| Que problema resolve? | README **e** código **e** issues |
| Para quem foi feito? | docs de uso, público declarado |
| Que funcionalidades oferece? | código e interfaces, não só a lista do README |
| Situação atual? | último push, releases, issues abertas, arquivado? |
| Fonte oficial? | URL canônica, não espelho |
| Que versão será investigada? | **SHA ou tag fixa** + data |

**Se for link:** abrir. **Se for nome:** localizar e, havendo homônimos, registrar a
ambiguidade e qual fonte foi escolhida — antes de concluir.

## Etapa B — Investigação profunda

Conforme o tipo (ver template correspondente): documentação e tutoriais · estrutura real do
código · funcionalidades relevantes · dependências · licença e termos (**no arquivo**, nunca
no badge) · releases e histórico · issues e problemas conhecidos · testes e CI · segurança e
vulnerabilidades · requisitos de hardware/SO · custos, quotas, limites · compatibilidade e
pontos de extensão · avaliação independente.

> **README não é prova.** Ele afirma intenção. Código, teste e interface mostram realidade.
> Quando divergirem, registre a divergência — é achado, não ruído.

**A profundidade é proporcional à relevância e à complexidade**, não ao tamanho do repositório. Itens
a cobrir conforme o caso: o que faz de fato · capacidades e como funcionam · arquitetura e
tecnologias · diferença em relação às alternativas · casos de uso · qualidade, maturidade e
atividade · licença, restrição comercial e **direitos sobre dados e outputs** · segurança e
privacidade · requisitos de hardware/infra/dependências · custo, quota, APIs e serviços externos ·
possibilidade de teste reproduzível · limitações e o que não está provado. O que não foi coberto
aparece na seção "o que não verifiquei, e por quê" — uma lista vazia ali é suspeita.

## Etapa C — Descoberta de aplicações

Explicar como funciona **na prática** e para que **poderia** servir, inclusive o que o autor
não destacou. Toda Skill, MCP ou ferramenta deve ser aberta por dentro: scripts, ferramentas,
fluxos, validações, integrações e mecanismos costumam valer mais que a descrição.

Formato da conclusão: `o que é` → `como funciona` → `o que permite fazer` → `o que impede`.

**A Etapa C termina na sugestão.** Onde um documento desta base aponta para um app
(Lia-Project, Lia Forge, Lia Studio, Lia Agent Hub, Lia Model Lab — ou qualquer outro
repositório do proprietário), o que se escreve é *o que a evidência sustenta* e *a pergunta de
viabilidade*; **não** se escreve instrução de implementação. Diretrizes que o Research pode dar e
aplicar são as desta base: `tools/`, `governance/`, `templates/`, `agents/`, índice, catálogo,
matrizes em `data/`. Para os outros apps, "o que levar" virou "o que sugiro considerar", e
"cabe ou não cabe, é possível ou não" é decisão do dono (`MISSION.md` §3). Mudança de
vocabulário feita em 2026-11-24 por determinação do proprietário; não é licença para o Research
reescrever o texto de um app — é o contrário: o texto de um app não é deste repo.

Documento anterior a 2026-11-24 pode ainda usar "levar"/"transportar" no corpo, e expressões
como "Custo de adoção" — são estimativa descritiva, não ordem. A regra acima vale para a leitura de
qualquer relatório desta base; não houve reescrita em massa justamente para não reescrever história.

## Etapa D — Experimentação

Aplicar `governance/TESTING-PROTOCOL.md`: tentar o Nível 2 quando for seguro e viável;
registrar a tentativa no log; separar teste próprio de evidência de terceiro.

Nenhum relatório é "documental por padrão". Documental é o que sobra depois de tentar.

**Fronteira do experimento controlado** (determinação do dono, `DR-0019` §4.5): dentro do sandbox de
pesquisa, instalar a ferramenta **dele** para executar o verificador **do objeto** é permitido e
desejado — inclusive `pnpm`/`venv`/`pytest` em `/tmp`. O que não é: instalar dependência em projeto
Lia, baixar peso/modelo grande, usar serviço pago, consumir crédito, criar conta, enviar dado
proprietário para fora. Toda execução entra no test-log com ambiente, procedimento e o que ficou de
fora, para que o dono do sandbox de amanhã reproduza sem adivinhar.

**Descoberta antes de cadastro.** Uma rodada que só cadastra links está incompleta, mesmo com todos
registrados. O piso é uma das quatro saídas: capacidade que a Lia não tem e não tinha mapeada;
alternativa melhor para problema já documentado nesta base; combinação entre dois objetos já
pesquisados; experimento barato que fecharia uma lacuna declarada.

## Etapa E — Publicação

`agents/PUBLISHING-PROTOCOL.md`: um documento principal, ID estável, cabeçalho completo,
índice atualizado, changelog, validador verde.

**Parcimônia documental** (`DR-0019` §4.6): não se cria arquivo por link. As saídas possíveis de um
objeto são — na ordem de preferência — uma linha em inventário existente, uma linha nova em digest
existente, uma retificação/ampliação num relatório antigo, um dossiê próprio, ou nada. Documento
novo exige evidência que mude o que a base sabe; "o dono mandou o link" não é critério.

## Resumo de rodada (formato fixo, 9 itens)

Formato da resposta ao dono ao fim de cada leva — não do relatório, que continua em
`templates/repository-research.md` e congêneres:

| # | Item | Conteúdo |
|---|---|---|
| 1 | Identificação | nome, link, versão/commit efetivamente investigados |
| 2 | Descoberta | o que foi encontrado de relevante (não o que existe) |
| 3 | Capacidades | o que a tecnologia oferece, com base em código/interface |
| 4 | Evidências | o que foi documentado × testado × incerto × bloqueado, com números |
| 5 | Relevância para a Lia | aplicações potenciais por app, **sem** determinar adoção |
| 6 | Limitações | licença, custo, segurança, hardware, dependências |
| 7 | Resultado | classificação (estado + recomendação) e conclusão em uma linha |
| 8 | Registro | arquivos criados/atualizados, contagens, validador, commits |
| 9 | Continuidade | **uma** próxima ação útil; sem etapas artificiais |

## Autonomia e limites de execução

Na própria base, ajuste de baixo risco entra sem consulta: vocabulário do validador, formato de
índice e catálogo, `templates/`, `agents/`, governança, reparo de dado. Registro no changelog
substitui o pedido de licença.

Para aí, e vira oportunidade registrada + decisão pendente: mexer em outro repositório; publicar,
instalar ou integrar em outro app; qualquer gasto, conta ou obrigação legal; sobrescrever trabalho
de outro agente; reescrever branch, commit ou histórico desta base (inclusive `RESEARCH-CHANGELOG.md`,
que é append-only).

## Anti-padrões que esta base já cometeu (não repetir)

| Anti-padrão | Correção |
|---|---|
| Contar objeto como "pesquisado" porque o arquivo existe | estado vem de verificação, não de existência |
| Repetir contagem de documento anterior | medir de novo com comando |
| Citar badge de licença | ler `LICENSE` no commit |
| Confundir recomendação com aprovação | três campos separados |
| Escrever "transportar X para o app Y" como se houvesse autorização | verbo de sugestão + a pergunta de viabilidade; implementação fora desta base não é pauta do Research |
| "Funciona" sem rótulo | vocabulário de evidência obrigatório |
| Relatório de 200 linhas para objeto de 1 arquivo | template por tipo |
| Documento novo por link recebido | Etapa E: linha de inventário, linha de digest, retificação — ou nada |
| Usar `BLOCKED` para o que era só não feito | `BLOCKED` exige a limitação medida; sem ela, `NOT_RUN` |
| Rodada que só cadastra links | critério de descoberta da Etapa D: uma das quatro saídas |
| Comparar tamanho de artefato derivado sem conferir a unidade (`.zip` comprimido × conteúdo extraído, entrada de manifest × arquivo em disco) | medir a mesma grandeza; se o artefato tem gerador, **reproduzir o gerador no commit de origem** antes de declarar divergência (`LR-STUDIO-012` §7/§13) |
| Abrir pendência jurídica por arquivo de aviso ausente sem olhar a origem | verificar se o upstream tem o arquivo: obrigação que não existe no original não é pendência nossa (§13) |
| Devolver ao proprietário pergunta que é respondível com medição | aplicar `MISSION.md` §3: fechar primeiro o que é fato técnico e opinar o que é recomendação; sobrar para o dono só adoção, gasto, publicação e remoção |
