# DR-0006 — Visibilidade do Lia-Research

| Campo | Valor |
|---|---|
| ID | DR-0006 |
| Estado | **PENDING / BLOCKED** |
| Dono | proprietário (ação de administração) |
| Data | 2026-11-17 |

## Situação
`BloomRX/Lia-Research` foi criado em 2026-11-17 com visibilidade **pública** e conteúdo
apenas inicial. A ordem de serviço exige **privado**.

Tentativa de correção pelo agente:

```text
PATCH /repos/BloomRX/Lia-Research {private: true}
→ 403 "Resource not accessible by integration"
```

`gh repo edit --visibility private` também falha. O token da integração não tem
permissão de administração sobre o repositório.

## Consequência
Até a correção, **nada sensível pode ser commitado** (ver
`governance/SECURITY-AND-PRIVACY-POLICY.md` §6). Esta fundação não contém segredos,
dados pessoais nem host real — verificado por `tools/validate.py`.

## Ação necessária
Proprietário: Settings → General → Danger Zone → Change visibility → Private
(ou conceder ao token permissão `administration: write`).

## Critério de conclusão
`GET /repos/BloomRX/Lia-Research` → `"private": true`.
