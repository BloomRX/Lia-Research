# Credenciais e fronteira de confiança — digest

| Campo | Valor |
|---|---|
| ID | `LR-SEC-001` |
| Categoria | security |
| Projetos | Lia-Project (primário), Lia Agent Hub, Lia Model Lab |
| Fontes | `Lia-Project@005a324:docs/architecture/LIA-CREDENTIAL-OWNER.md` (4,6 KB), `docs/architecture/LIA-BETA-CREDENTIAL-AUDIT-2026-11-08.md` (26 KB), `docs/reports/LIA-BETA-SECURITY-FIXES-2026-11-14.md` (8,8 KB), `LIA-SECURITY-RECONCILIATION.md` (22 KB), `LIA-AUTH-RECONCILIATION-SECURITY-AUDIT.md` (11,6 KB), `LIA-OIDC-STREAMING-PREPARATION-2026-11-10.md` (12,8 KB) |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média-Alta (auditorias internas dedicadas, não reproduzidas aqui) |

## 1. Por que este é o tema crítico do ecossistema

Um assistente pessoal desktop guarda credenciais de: providers de modelo, STT/TTS,
contas (OIDC), e — se o HA-MCP for adotado — um **token de administrador da casa**.
A fronteira de confiança entre renderer, main process, Stage sandbox e serviços é o
que decide se um XSS no Stage vira vazamento de chave.

## 2. O que os documentos estabelecem

| Documento | Contribuição |
|---|---|
| `LIA-CREDENTIAL-OWNER.md` | define quem é o dono da credencial (processo, não renderer) |
| `LIA-BETA-CREDENTIAL-AUDIT-2026-11-08.md` | auditoria de credenciais do beta (26 KB) |
| `LIA-BETA-SECURITY-FIXES-2026-11-14.md` | correções de segurança do beta |
| `LIA-SECURITY-RECONCILIATION.md` | reconciliação Architecture/Security × Principal (6× `ADAPTAR`) |
| `LIA-AUTH-RECONCILIATION-SECURITY-AUDIT.md` | auditoria de autenticação |
| `LIA-OIDC-STREAMING-PREPARATION-2026-11-10.md` | preparação de OIDC/streaming |
| `LIA-STAGE-SANDBOX-AF1B-FIX.md` | correção de sandbox do Stage (12 KB) |

## 3. Padrões que o ecossistema já pratica (a copiar)

1. **Dono único da credencial** — um processo, explícito.
2. **Sandbox do Stage** com correção documentada de falha.
3. **Reconciliação** entre auditoria independente e implementação, com itens `ADAPTAR`.
4. **OIDC preparado antes de streaming** — autenticação antes de recurso novo.

## 4. Regras do Lia-Research aplicáveis

Ver `governance/SECURITY-AND-PRIVACY-POLICY.md`: nada de token no repositório, nada de
host real, nada de PoC de falha não corrigida.

## 5. Ligação com a pesquisa externa

- HA-MCP: token de admin da casa → `LR-MCP-001` §8 e `RISK-MATRIX.md`.
- Mister Download Manager: cookies de navegador → `LR-FORGE-001` §8.
- RouterHub: chave de serviço comercial sem política publicada → `LR-PROV-001`.
