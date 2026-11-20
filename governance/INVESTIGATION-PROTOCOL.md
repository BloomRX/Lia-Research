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
| "Funciona" sem rótulo | vocabulário de evidência obrigatório |
| Relatório de 200 linhas para objeto de 1 arquivo | template por tipo |
