# Decisões (`DR-*`) — o que esta pasta decide e o que ela **não** decide

| Campo | Valor |
|---|---|
| Natureza | registro de **governança do próprio Lia Research** |
| Não é | aprovação de adoção de tecnologia em nenhum projeto |
| Canônico em | `MISSION.md` §3 · `catalog/CATALOG-SCHEMA.md` §4 |

---

## 1. O que um `DR-*` aqui representa

Um `DR` registra uma decisão **de governança da base de pesquisa**: visibilidade do
repositório, política de acesso, formato de manifesto, retenção de log, escopo de
publicação, tratamento de material de terceiros.

## 2. O que um `DR-*` aqui **não** representa

**Nenhum `DR` desta pasta autoriza adotar, integrar, forkar ou instalar tecnologia** em
Lia-Project, Lia Forge, Lia Studio, Lia Agent Hub, Lia Model Lab ou qualquer outro projeto.

Uma tecnologia pode ter relatório completo, teste local aprovado e recomendação
`DIRECT_INTEGRATION_CANDIDATE` — e **continuar sem permissão de entrar em produto**. A
decisão de adoção pertence ao proprietário e ao responsável do projeto, fora desta base.

## 3. Estados das pastas (e o risco de confusão)

| Pasta | Significa | **Não** significa |
|---|---|---|
| `ACCEPTED/` | decisão de governança aceita pelo proprietário | tecnologia aprovada para uso |
| `ADAPTED/` | decisão de governança ajustada | adaptação autorizada em produto |
| `PENDING/` | aguardando decisão do proprietário | bloqueio de leitura ou de pesquisa |
| `REFERENCE-ONLY/` | decisão de manter apenas como referência | permissão de cópia |
| `REJECTED/` | decisão de não seguir, com condição de reabertura | proibição de reavaliar |

Para evitar a leitura errada, cada pasta mantém um `README.md` próprio com essa ressalva, e
o validador (`tools/validate.py`) exige que o cabeçalho de todo `DR-*` declare
`| Alcance |` com `GOVERNANCA` (nunca `ADOCAO`).

## 4. Onde vive uma decisão de adoção

Fora daqui: no repositório do projeto, em ADR próprio, com o responsável identificado.
Quando o proprietário comunicar uma decisão de adoção, esta base pode **registrá-la como
fato citado** no campo `decisao_de_adocao` do objeto — com origem e data — mas nunca
inventá-la nem inferi-la de uma recomendação.

## 7. Índice dos registros

| DR | Assunto | Caminho | Decisão sobre adoção? |
|---|---|---|---|
| DR-0001 | Licenciamento e distribuição das Skills `lia-*` | [`PENDING/DR-0001-LIA-SKILLS-LICENSING.md`](PENDING/DR-0001-LIA-SKILLS-LICENSING.md) | não — governança |
| DR-0002 | Acesso de agentes ao Lia-Research | [`PENDING/DR-0002-LIA-RESEARCH-ACCESS.md`](PENDING/DR-0002-LIA-RESEARCH-ACCESS.md) | não — governança |
| DR-0003 | Adotar adaptador residencial (HA-MCP)? | [`PENDING/DR-0003-HA-MCP-ADAPTER.md`](PENDING/DR-0003-HA-MCP-ADAPTER.md) | não — governança |
| DR-0004 | Destino do ZIP de terceiros no Lia-Studio | [`PENDING/DR-0004-STUDIO-THIRD-PARTY-ZIP.md`](PENDING/DR-0004-STUDIO-THIRD-PARTY-ZIP.md) | não — governança |
| DR-0005 | RouterHub não entra no catálogo de providers | [`REJECTED/DR-0005-ROUTERHUB.md`](REJECTED/DR-0005-ROUTERHUB.md) | não — governança |
| DR-0006 | Lia-Research permanece público | [`ACCEPTED/DR-0006-REPOSITORY-PUBLIC.md`](ACCEPTED/DR-0006-REPOSITORY-PUBLIC.md) | não — governança |
| DR-0007 | Consolidação de Skills duplicadas | [`PENDING/DR-0007-CONSOLIDACAO-SKILLS-DUPLICADAS.md`](PENDING/DR-0007-CONSOLIDACAO-SKILLS-DUPLICADAS.md) | não — governança |
| DR-0008 | Aceitar a matriz de risco R0–R3 | [`PENDING/DR-0008-RISK-MATRIX-ACCEPTANCE.md`](PENDING/DR-0008-RISK-MATRIX-ACCEPTANCE.md) | não — governança |
| DR-0009 | Retenção de log de auditoria de automação | [`PENDING/DR-0009-AUDIT-LOG-RETENTION.md`](PENDING/DR-0009-AUDIT-LOG-RETENTION.md) | não — governança |
| DR-0010 | Câmera habilitada por padrão? | [`PENDING/DR-0010-CAMERA-DEFAULT.md`](PENDING/DR-0010-CAMERA-DEFAULT.md) | não — governança |
| DR-0011 | Modelo de registro de servidor MCP no Hub | [`PENDING/DR-0011-MCP-REGISTRY-MODEL.md`](PENDING/DR-0011-MCP-REGISTRY-MODEL.md) | não — governança |
| DR-0012 | Política de instalação de servidor MCP de terceiro | [`PENDING/DR-0012-MCP-INSTALL-POLICY.md`](PENDING/DR-0012-MCP-INSTALL-POLICY.md) | não — governança |
| DR-0013 | Parecer sobre GPL do Mister Download Manager | [`PENDING/DR-0013-MDM-GPL-OPINION.md`](PENDING/DR-0013-MDM-GPL-OPINION.md) | não — governança |
| DR-0014 | Critério de "modelo validado" | [`PENDING/DR-0014-MODEL-VALIDATION-CRITERIA.md`](PENDING/DR-0014-MODEL-VALIDATION-CRITERIA.md) | não — governança |
| DR-0015 | unslop rejeitado por ausência de licença | [`REJECTED/DR-0015-UNSLOP.md`](REJECTED/DR-0015-UNSLOP.md) | não — governança |
| DR-0016 | ReScript não é adotado como stack | [`REJECTED/DR-0016-RESCRIPT.md`](REJECTED/DR-0016-RESCRIPT.md) | não — governança |
| DR-0017 | OpenJarvis mantido como referência | [`REFERENCE-ONLY/DR-0017-OPENJARVIS.md`](REFERENCE-ONLY/DR-0017-OPENJARVIS.md) | não — governança |
| DR-0018 | OpenIDEA, SculptForge, ManimGX e pixelfx como referência | [`REFERENCE-ONLY/DR-0018-FERRAMENTAS-CRIACAO.md`](REFERENCE-ONLY/DR-0018-FERRAMENTAS-CRIACAO.md) | não — governança |
| DR-0019 | Protocolo contínuo de investigação de links (método e autonomia do Research) | [`ACCEPTED/DR-0019-PROTOCOLO-CONTINUO-DE-LINKS.md`](ACCEPTED/DR-0019-PROTOCOLO-CONTINUO-DE-LINKS.md) | não — governança |
