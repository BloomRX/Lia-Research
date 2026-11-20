# ai-memory — memória de longo prazo que atravessa agentes, sessões e máquinas

| Campo | Valor |
|---|---|
| ID | `LR-AGENT-011` |
| Tipo | repositorio |
| Estado da pesquisa | DOCUMENTED |
| Resultado de execução | BLOCKED |
| Decisão de adoção | — (nenhuma registrada) |
| Categoria | agent |
| Projetos beneficiados | Lia Agent Hub (memória compartilhada), Lia Model Lab (harness), Lia-Project (continuidade de sessão) |
| Fontes | `akitaonrails/ai-memory@main` (2026-11-19): `README.md`, árvore (859 subdiretórios em `crates/`, 211 hooks, 187 companions, 184 docs, 51 plugins, 41 evals), API do GitHub; site aimemory.sh |
| SHA completo | `6a141858bb88fbd025b144664a37271acd5e0e43` |
| Proveniência do SHA | **CANDIDATO_POR_DATA** — leitura de `main` em 2026-11-19 sem SHA registrado; candidato = último commit antes do fim do dia, NÃO confirmado |
| HEAD atual | `6a141858bb88fbd025b144664a37271acd5e0e43` (conferido em 2026-11-20) |
| Data | 2026-11-17 |
| Última verificação | 2026-11-20 |
| Upstream conferido | 2026-11-20 · `akitaonrails/ai-memory` · HEAD `6a141858bb88` · sem SHA analisado registrado |
| Próxima revisão | 2027-01-19 |
| Recomendação | **ADAPT** — o protocolo de *handoff* e o modelo de memória, não o binário |
| Licença | MIT (`CONFIRMED` no `LICENSE` e no README) |
| Confiança | Alta para o desenho (README lido); **UNVERIFIED** para funcionamento — não executado |

---

## 1. Identificação

| Item | Valor |
|---|---|
| Repositório | https://github.com/akitaonrails/ai-memory · site https://aimemory.sh |
| Autor | Fabio Akita (`akitaonrails`) |
| Métricas | ★ **16.172** · 55 MB · Rust 1.95+ · criado 2026-05-21 · push 2026-11-19 |
| Licença | MIT |
| Distribuição | binário por release; também roda como servidor próprio (Docker) |

## 2. Resumo executivo

O problema que ele resolve é exatamente o que a Lia tem hoje entre sessões: **o
conhecimento morre com a sessão**. A proposta é uma memória **compartilhada entre
harnesses** (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Grok, Devin, Kimi, Kiro e
outros — "mais de vinte"), com três peças que interessam:

1. **Handoff tipado** — não é um resumo solto: cada handoff tem **dono** e é
   **reivindicado uma única vez**. É o que evita dois agentes continuarem a mesma tarefa.
2. **Memória híbrida sem vetor obrigatório** — full-text + entidades + links, com vetores
   **opcionais** e fundidos na busca. Ou seja: funciona sem banco vetorial.
3. **Captura por hooks de ciclo de vida** — o trabalho é registrado enquanto acontece, com
   **fronteira de privacidade antes de armazenar**, e o servidor consolida depois.

E uma decisão de privacidade que vale copiar: ao transportar sessão entre harnesses, o
servidor remoto recebe **apenas o harness e a identidade da sessão** — nunca o caminho nem
o corpo do transcript local.

## 3. O que resolve

| Problema | Solução |
|---|---|
| Trocar de agente e reexplicar tudo | memória única alimentada por 20+ harnesses |
| Dois agentes pegam a mesma tarefa | handoff com dono, reivindicado uma única vez |
| Resumo perde detalhe | projeção local temporária do histórico nativo + pacote limitado |
| Perfil de trabalho recomeça a cada projeto | perfil de hábitos (gerenciador de pacotes, layout de teste, arquitetura) |
| Memória exige infra de vetor | full-text + entidades + links; vetor é opcional |
| Memória fica numa máquina | servidor próprio; equipe aponta para um servidor |

## 4. Arquitetura (como descrito)

```text
hooks de ciclo de vida (211 arquivos de hook no repo)
        │  observações saneadas
        ▼
servidor de memória (auto-hospedado/Docker)
   full-text + entidades + links (+ vetores opcionais)  →  busca fundida
        │
        ├── handoff tipado (dono, reivindicado 1×)
        ├── pacote de inicialização limitado (+ projeção local privada)
        └── console de gestão: usuários, inspeção, exclusão, chaves MCP por pessoa
```

`ai-memory run <harness>` inicia o agente com o workstream compartilhado; lançar o harness
diretamente mantém o comportamento antigo.

## 5. Funcionalidades

Memória entre agentes · entre sessões · entre projetos (perfil) · entre máquinas (servidor)
· handoff tipado · busca híbrida · captura por hooks · console de administração · chaves MCP
por usuário · políticas de privacidade antes do armazenamento · exclusão de sessão.

## 6. Dependências

Rust 1.95+ para build; servidor próprio (Docker disponível) para uso em equipe; nenhuma
dependência de banco vetorial declarada como obrigatória. `UNVERIFIED`: portabilidade para
Windows — não há menção explícita no trecho lido.

## 7. Requisitos de hardware e sistema

Serviço de texto: sem GPU. O custo real é **disco e política de retenção**, não
processamento — o que conversa com a lacuna de retenção (`DR-0009`).

## 8. Segurança e privacidade

| Item | Situação |
|---|---|
| Fronteira antes de armazenar | declarada (`CONFIRMED` no README) |
| Dados enviados ao servidor em `run` | só harness + identidade da sessão; nunca caminho/corpo do transcript |
| Chaves | chaves MCP por pessoa, no console |
| Exclusão | inspeção e exclusão de sessão pelo console |
| Risco | memória compartilhada = **ponto único de vazamento**; precisa de retenção e de criptografia explícitas (`DR-0009`) |

## 9. Licença e proveniência

**MIT** (`CONFIRMED`). Uso comercial, fork e modificação permitidos, com aviso. Sem
copyleft. Clone do padrão já registrado em `LR-LIC-005`: aviso junto do que for copiado.

## 10. Maturidade e manutenção

★16.172, ~6 meses de vida, push no dia da coleta, 41 diretórios de `evals` (sinal raro e
bom: o autor mede o próprio sistema), 184 docs. Estrutura muito grande (859 subdiretórios
em `crates/`) — provável workspace com dependências vendorizadas; **não auditado linha a
linha**. `UNVERIFIED` para qualidade interna.

## 11. Custos e limitações

Servidor para manter · modelo de ameaça novo (memória central) · integração depende de
hooks por harness · sem GPU, mas com custo de armazenamento e de privacidade.

## 12. Compatibilidade com o ecossistema Lia

| Dimensão | Situação |
|---|---|
| Windows 11 | `UNVERIFIED` |
| Electron/Vue | integração por servidor/MCP, não por biblioteca |
| Skills/MCP | **sim** — chaves MCP por usuário, superfície própria |
| Licença | MIT, sem trava |

## 13. Projetos beneficiados

**Hub** (memória compartilhada entre apps e agentes) · **Model Lab** (troca de harness sem
perder contexto) · **Project** (continuidade de sessão longa) · **Studio/Forge** (retomar
trabalho entre sessões).

## 14. Oportunidades de reutilização

| # | Prática | O que copiar |
|---|---|---|
| M1 | **Handoff com dono e reivindicação única** | protocolo de passagem de tarefa entre agentes; barato e resolve duplicação |
| M2 | **Vetor opcional, não requisito** | busca híbrida que funciona sem infra vetorial |
| M3 | **Fronteira de privacidade antes de armazenar** | regra de escrita, não de leitura |
| M4 | **Só harness + identidade atravessa** | mínimo de dados em trânsito |
| M5 | **`evals/` no próprio repo** | medir a memória, não só afirmar que funciona |

## 15. Riscos e incompatibilidades

Memória central é alvo único · retenção não resolvida (`DR-0009`) · dependência de hooks
por harness · concorre com `mempalace` (item 05 da triagem) e `mcpvault` (item 04) —
**comparar antes de escolher**.

## 16. Evidências e fontes

| # | Evidência | Rótulo |
|---|---|---|
| E1 | MIT, ★16.172, Rust, push 2026-11-19 | CONFIRMED (API) |
| E2 | 20+ harnesses, handoff tipado com dono e reivindicação única | CONFIRMED (README) |
| E3 | Busca híbrida com vetor opcional | CONFIRMED (README) |
| E4 | Servidor recebe só harness + identidade da sessão | CONFIRMED (README) |
| E5 | 211 hooks, 41 `evals`, 184 docs | CONFIRMED (árvore) |
| E6 | Funciona em Windows / em produção | **UNVERIFIED** |
| E7 | Qualidade interna do código | **UNVERIFIED** |

## 17. Recomendação

**Recomendação (opinião técnica, não é aprovação): ** ADAPT`.** Não instalar como dependência agora; adaptar o **protocolo de
handoff (M1)** e a regra de **privacidade antes de armazenar (M3)**, que servem ao Hub
mesmo sem o binário. Se a Lia for adotar uma memória, comparar com `mempalace` e
`mcpvault` num único digest — não três relatórios dizendo o mesmo.

## 18. Próximos passos

| # | Ação | Dono | Gate |
|---|---|---|---|
| 1 | Digest comparativo `ai-memory` × `mempalace` × `mcpvault` | Lia-Research | triagem §5 |
| 2 | Escrever o protocolo de handoff (M1) como proposta do Hub | Hub | `LR-AGENT-009` |
| 3 | Verificar Windows e testar 1 fluxo de handoff real | Model Lab | autorização |
| 4 | Ligar retenção ao `DR-0009` | Lia-Research | `DR-0009` |

## Reauditoria 2026-11-20

| Campo | Valor |
|---|---|
| Versão anteriormente analisada | ``6a141858bb88` (leitura de `main` em 2026-11-19; SHA **candidato**)` |
| Versão novamente examinada | ``6a141858bb88` (HEAD atual, release `v3.5.1` de 2026-11-19)` (2026-11-20) |
| Método | `compare` da API do GitHub (commits + arquivos), leitura de arquivos materiais no HEAD, estado de CI no HEAD, releases |
| Mudanças encontradas | Nenhum commit entre o candidato e o HEAD. A reavaliação confirma que o candidato coincide com o HEAD, mas **não** prova qual árvore foi lida em 2026-11-19 (ver `audits/PROVENANCE-2026-11-20.md` §2.2). |
| Evidências novas | Proveniência passa de 'sem SHA' para 'candidato por data, coincidente com o HEAD'. `LICENSE` MIT conferido no HEAD. |
| Testes próprios | **Bloqueado**: Rust; `cargo` ausente. |
| Testes independentes | Release `v3.5.1` publicada em 2026-11-19 — posterior à análise, portanto o relatório descreve versão anterior à release atual. |
| Conclusão | Recomendação **reavaliada e mantida em `ADAPT`** (protocolo de *handoff* e modelo de memória). |
| Próxima revisão | 60 dias — é o objeto com proveniência mais frágil. |

