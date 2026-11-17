# Armazenamento e portabilidade de dados

| Campo | Valor |
|---|---|
| ID | `LR-SEC-004` |
| Categoria | storage |
| Projetos | Lia Agent Hub (primário), Lia-Project |
| Fontes | `Lia-AgentHub:docs/architecture/DATA-STORAGE-AND-PORTABILITY.md` (25 KB), `CAPABILITY-HOST-AND-DISTRIBUTION-CONTRACT.md` (25 KB) |
| Data | 2026-11-17 |
| Status | CURRENT |
| Confiança | Média-Alta (documento de arquitetura do próprio projeto) |

## 1. Por que está aqui

O Hub guarda catálogo, registros e (potencialmente) payloads de Skill. Portabilidade
é requisito de produto **e** de liberdade do usuário: sair deve ser possível.

## 2. Requisitos que o documento estabelece

- dados em formato aberto, não em banco proprietário opaco;
- exportação completa a qualquer momento;
- separação entre dados do usuário e dados de catálogo (recuperáveis de novo);
- nenhum dado do usuário em serviço externo por padrão.

## 3. Ligação com a política de segurança

`governance/SECURITY-AND-PRIVACY-POLICY.md` §1: este repositório não armazena token,
credencial ou dado pessoal. O mesmo princípio vale para o catálogo do Hub: metadados
sim, payload com segredo não.

## 4. Lacuna

Não há, nos cinco projetos, política única de retenção/exclusão de dados do usuário.
É item de produto, registrado em `RESEARCH-ROADMAP.md` (L-3).
