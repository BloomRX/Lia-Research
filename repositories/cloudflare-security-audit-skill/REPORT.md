# Cloudflare security-audit-skill — auditoria com achado validado por código

| Campo | Valor |
|---|---|
| ID | `LR-SEC-007` |
| Categoria | security |
| Projetos beneficiados | Lia-Project (auditoria dos apps), Lia Studio (Electron/IPC), Lia Agent Hub (LLM), Lia-Research (padrão de Skill auditável) |
| Fontes | `cloudflare/security-audit-skill@main` (2026-09-14): `README.md`, `LICENSE`, árvore completa, `skills/security-audit/*.md`, `report-schema.json`, `validate-*.cjs`; API do GitHub |
| Data | 2026-11-17 |
| Próxima revisão | 2027-02-17 |
| Status | CURRENT |
| Recomendação | **ADAPTAR** — usar como checklist de auditoria; a estrutura de Skill é o modelo |
| Licença | MIT (`CONFIRMED`) |
| Confiança | Alta para conteúdo e estrutura (arquivos lidos); **UNVERIFIED** para eficácia das auditorias |

---

## 1. Identificação

| Item | Valor |
|---|---|
| Repositório | https://github.com/cloudflare/security-audit-skill |
| Autor | Cloudflare |
| Métricas | ★ **75.939** · 170 forks · **143 KB** · JS · criado 2026-06-18 · push 2026-09-14 |
| Licença | MIT |
| Natureza | uma **Skill** (conteúdo em Markdown + validadores em Node) |

## 2. Resumo executivo

São **143 KB** e 75.939 estrelas. O que há dentro é o mais relevante desta lista de
triagem: uma Skill de auditoria de segurança **por classes**, com dois arquivos que falam
direto da Lia — `DESKTOP-MOBILE-AND-LOCAL-IPC.md` (app desktop e IPC local) e
`AI-AND-LLM.md` (aplicação com modelo) — e um mecanismo que quase nenhuma Skill tem:
**o resultado é validado por código**.

| Peça | Tamanho | Função |
|---|---:|---|
| 11 arquivos de classe (`ATTACK-CLASSES`, `CLIENT-SIDE`, `CLOUD-AND-DEPLOYMENT`, `DATA-ISOLATION-AND-LIFECYCLE`, `DESKTOP-MOBILE-AND-LOCAL-IPC`, `HUNTING`, `MEMORY-SAFETY-AND-BINARY`, `PROTOCOLS-RPC-AND-MESSAGING`, `RECONNAISSANCE`, `RESOURCE-EXHAUSTION`, `AI-AND-LLM`) | 7–22 KB | o que procurar, por classe |
| `report-schema.json` | 14 KB | formato do achado, legível por máquina |
| `validate-findings.cjs` (+ teste de 26 KB) | 28 KB | recusa achado fora do schema |
| `validate-coverage-ledger.cjs` (+ teste de 28 KB) | 33 KB | recusa auditoria que não cobriu o que diz ter coberto |

É a única Skill já lida por esta base em que o **output é verificado** — e isso responde a
uma das três fraquezas registradas em `LR-AGENT-009` (V6) e a `LR-SEC-005`.

## 3. O que resolve

| Problema de auditoria | Solução aqui |
|---|---|
| "Auditei" sem cobertura declarada | *coverage ledger* validado por script |
| Achado vago em texto livre | `report-schema.json` + validador |
| Auditoria genérica que ignora desktop | arquivo específico de **IPC local / app desktop** |
| Auditoria que ignora IA | arquivo específico de **AI/LLM** |
| Skill que não mede nada | validadores com teste próprio |

## 4. Arquitetura

```text
skills/security-audit/
├── README.md (na raiz do repo)          como usar
├── <classe>.md  × 11                    o que procurar
├── report-schema.json                   contrato do achado
├── validate-findings.cjs + .test.cjs    schema → aceita/recusa
└── validate-coverage-ledger.cjs + test  cobertura → aceita/recusa
```

Sem servidor, sem dependência: Node puro, executável no CI.

## 5. Funcionalidades

Auditoria por classe · trilha de cobertura · achado com schema · validação automática de
achado e de cobertura · foco explícito em desktop/IPC e em aplicação com LLM.

## 6. Dependências

Node.js para os validadores; nada além disso. Nenhuma dependência de nuvem (apesar do
autor ser a Cloudflare) — `CONFIRMED` na árvore.

## 7. Requisitos de hardware e sistema

Nenhum. É texto + script.

## 8. Segurança e privacidade

| Item | Situação |
|---|---|
| Superfície de exemplo | inclui app desktop, IPC local, LLM — exatamente a superfície da Lia |
| Dados | a Skill não coleta nada; o auditor é que decide o que anotar |
| Risco | checklist não é prova: uma auditoria "completa" no papel não substitui teste de execução |
| Coerência | o validador impede achado malformado; **não** impede achado errado |

## 9. Licença e proveniência

**MIT** (`CONFIRMED`). Adaptação permitida com aviso. Marca: "Cloudflare" **não** é
licenciada pelo MIT — não usar como endosso. Aplicar `LR-LIC-005` §3.1 (aviso viaja com o
payload).

## 10. Maturidade e manutenção

★75.939, 170 forks, **último push 2026-09-14** (dois meses antes da coleta — mais parado
que a média desta lista). Conteúdo pequeno e estável; validadores têm teste. Não é
biblioteca: envelhece bem devagar, mas o *conteúdo* de classes envelhece (novas classes
aparecem).

## 11. Custos e limitações

Sem custo de execução. Limites: cobre classes, não o código real; os validadores garantem
**forma**, não **verdade**; não há orquestração de fases automatizada no repo (o README
descreve o processo).

## 12. Compatibilidade com o ecossistema Lia

| Dimensão | Situação |
|---|---|
| Windows/Linux/macOS | sim (texto + Node) |
| Electron/IPC | **conteúdo específico** — o único material lido que trata disso |
| Skills do ecossistema | formato compatível (pasta + Markdown) |
| Licença | MIT |

## 13. Projetos beneficiados

**Lia-Project** (auditoria dos apps e do IPC) · **Studio** (desktop) · **Agent Hub** (LLM,
permissões) · **Lia-Research** (modelo de Skill com validador).

## 14. Oportunidades de reutilização

| # | Prática | O que copiar |
|---|---|---|
| S1 | **Schema de achado** | todo relatório de auditoria da Lia com formato fixo, validável |
| S2 | **Coverage ledger** | declarar o que foi coberto e provar |
| S3 | **Validador com teste** | a Skill deixa de ser opinião em Markdown |
| S4 | **Arquivo por classe** | revisão por especialista sem ler 100 KB |
| S5 | **Classe desktop/IPC** | checklist direta para `LR-SEC-005` e para o Stage |

## 15. Riscos e incompatibilidades

Checklist dá falsa segurança · conteúdo envelhece · MIT não dá endosso da marca ·
auditoria continua exigindo execução (o buraco `V6` permanece).

## 16. Evidências e fontes

| # | Evidência | Rótulo |
|---|---|---|
| E1 | MIT, ★75.939, 143 KB, push 2026-09-14 | CONFIRMED (API) |
| E2 | 11 arquivos de classe, incluindo desktop/IPC e AI/LLM | CONFIRMED (árvore) |
| E3 | `report-schema.json` + dois validadores com testes | CONFIRMED (árvore) |
| E4 | Eficácia em auditoria real | **UNVERIFIED** |
| E5 | Cobertura de classes novas em 2027 | **UNVERIFIED** |

## 17. Recomendação

**VEREDITO: `ADAPTAR`.** É o item desta lista com melhor relação valor/esforço para a Lia:
o conteúdo serve de checklist imediata para o IPC do Stage, e a **estrutura** (schema +
dois validadores) é o que falta nas 48 Skills do ecossistema. Não copiar o texto: usar como
fonte citada e escrever o checklist da Lia com as classes que existem aqui.

## 18. Próximos passos

| # | Ação | Dono | Gate |
|---|---|---|---|
| 1 | Extrair a classe desktop/IPC para um checklist do Lia-Project | Lia-Project | `LR-SEC-005` |
| 2 | Adotar `report-schema.json` como formato de achado | Lia-Research | nenhum |
| 3 | Escrever `validate-findings` próprio em Python (sem Node) | Lia-Research | — |
| 4 | Comparar com `LR-SEC-006` R1/R4 (eval/lint do Claude-BugHunter) | Lia-Research | — |
