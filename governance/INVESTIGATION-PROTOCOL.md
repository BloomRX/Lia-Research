# Protocolo de investigação — de um link solto a um relatório publicável

| Campo | Valor |
|---|---|
| Documento | Procedimento operacional de investigação |
| Versão | 1.0 — 2026-11-20 |
| Canônico em | este arquivo |
| Relacionado | `MISSION.md` (autoridade) · `governance/TESTING-PROTOCOL.md` (experimentação) · `catalog/CATALOG-SCHEMA.md` (formato) |

---

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

## Etapa E — Publicação

`agents/PUBLISHING-PROTOCOL.md`: um documento principal, ID estável, cabeçalho completo,
índice atualizado, changelog, validador verde.

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
| Comparar tamanho de artefato derivado sem conferir a unidade (`.zip` comprimido × conteúdo extraído, entrada de manifest × arquivo em disco) | medir a mesma grandeza; se o artefato tem gerador, **reproduzir o gerador no commit de origem** antes de declarar divergência (`LR-STUDIO-012` §7/§13) |
| Abrir pendência jurídica por arquivo de aviso ausente sem olhar a origem | verificar se o upstream tem o arquivo: obrigação que não existe no original não é pendência nossa (§13) |
| Devolver ao proprietário pergunta que é respondível com medição | aplicar `MISSION.md` §3: fechar primeiro o que é fato técnico e opinar o que é recomendação; sobrar para o dono só adoção, gasto, publicação e remoção |
