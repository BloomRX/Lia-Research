# DR-0006 — Lia-Research permanece público

| Campo | Valor |
|---|---|
| ID | DR-0006 |
| Estado | **ACCEPTED** (decisão do proprietário) |
| Decisor | proprietário BloomRX |
| Data da decisão | 2026-11-17 (commit `c9e6e97` na `main`) |
| Data de abertura | 2026-11-17 (como bloqueio de privacidade) |
| Reverte | a suposição da ordem de serviço de que o repositório deveria ser privado |
| Registro de origem | `BloomRX/Lia-Research@c9e6e97:README.md` — "The repository is public so agents across the ecosystem can read it." |

## Histórico (preservado)

A ordem de serviço original pedia repositório **privado**. A fundação tentou a alteração
por duas rotas e recebeu `403 Resource not accessible by integration` — o token da
integração não tem permissão de administração. O item foi registrado como `BLOCKED`, com
a consequência explícita: "nada sensível pode ser commitado até a correção".

## Decisão do proprietário

O repositório **permanece público**, por três motivos declarados no README da `main`:

1. agentes dos cinco projetos precisam **ler** a base sem infraestrutura de credencial;
2. o consumo é **read-only** para agentes de projeto (não editam a branch de pesquisa);
3. a coleção completa vive na branch `arena/7cf9c65e-lia-research`, referenciada
   explicitamente — `main` é porta de entrada.

## Consequências

| Consequência | Tratamento |
|---|---|
| Conteúdo sensível nunca entra | política permanente em `governance/SECURITY-AND-PRIVACY-POLICY.md` §6 |
| Toda coleta precisa de revisão de exposição | `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md` |
| Snapshot de corpus pode conter material de projeto | sanitizado: 1 arquivo excluído, 3 e-mails redigidos |
| Público ≠ aprovado | `governance/LICENSE-AND-PROVENANCE-POLICY.md`: visibilidade não é licença |
| Público ≠ atual | status/`Próxima revisão` por documento continuam valendo |

## O que a decisão **não** autoriza

1. Publicar segredo, token, dado pessoal ou dump de sessão — proibido sem exceção.
2. Conceder licença sobre conteúdo de terceiro — licença é do titular.
3. Tornar a base dependência de runtime de qualquer projeto.
4. Publicar PoC de vulnerabilidade não corrigida.

## Ação que **não** é mais necessária

A troca de visibilidade para privada deixou de ser pendência. O gate correspondente passa
a ser: **a revisão de exposição pública foi feita antes de cada commit com material de
projeto?**
