# DR-0002 — Acesso de agentes ao Lia-Research

| Campo | Valor |
|---|---|
| ID | DR-0002 |
| Estado | **PENDING (parcial)** |
| Dono | proprietário |
| Data | 2026-11-17 · revisado 2026-11-17 |
| Bloqueia | publicação e revisão pela base — **não** a leitura |
| Resolvido por | `DR-0006` (ACCEPTED): repositório **público** |

## 0. O que já está decidido (não reabrir)

`DR-0006` (ACCEPTED) tornou o repositório **público por decisão do proprietário**.
Consequência direta para este DR:

- **Leitura é aberta e sem credencial.** Qualquer sessão, agente ou pessoa lê
  `https://raw.githubusercontent.com/BloomRX/Lia-Research/<branch>/<caminho>` sem token,
  sem deploy key e sem GitHub App.
- As opções A (deploy key), B (GitHub App) e C (clone manual) desta versão anterior
  **deixaram de ser caminho de leitura**; A e B só fariam sentido para escrita, que
  este repositório não delega a agente de projeto.
- A pergunta 1 da versão anterior ("com qual token/deploy key") está **respondida**:
  nenhum.

## 1. Perguntas que continuam abertas

1. Quem **publica** (só o Orchestrator? agente de projeto via PR?).
2. Quem **revisa** pesquisa de alto impacto.
3. Cópia local de leitura: política de sincronização e de citação de versão.
4. Logs de acesso são necessários — hoje não existem e a leitura pública dispensa.

## 2. Opções ainda em avaliação (escrita, não leitura)

| Opção | Prós | Contras |
|---|---|---|
| A. Orchestrator publica; projeto só lê | simplicidade, sem segredo distribuído | gargalo num papel |
| B. Agente de projeto publica via PR | paralelismo | exige revisão consistente |
| C. Sem publicação delegada | menor risco | base envelhece |

## 3. Fora de escopo

Não autoriza conceder **escrita** automática a agente de projeto, nem criar dependência
de runtime (`D. Submodule` segue proibido pela ordem de serviço). A visibilidade pública
**não** está em discussão aqui: foi decidida em `DR-0006`.
