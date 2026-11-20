# Papéis especialistas

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


Especialistas são **subagentes temporários**. Não têm autoridade de publicação.
O Orchestrator assina o relatório final e responde pela consolidação.

---

## 1. Especialista em arquitetura

**Pergunta:** "Como isso é construído e onde quebra?"

| Entrega | Método |
|---|---|
| Mapa de componentes | trees + leitura de módulos de entrada |
| Contratos e fronteiras | assinaturas públicas, formatos de mensagem |
| Acoplamentos | imports, dependências declaradas |
| Pontos de extensão | plugins, hooks, MCP, API local |

Não confundir diagrama do README com arquitetura real: o README descreve a intenção;
o código descreve o comportamento.

## 2. Especialista em segurança

**Pergunta:** "Quem consegue fazer o quê, e o que acontece se der errado?"

Checklist obrigatório: autenticação, autorização, exposição de rede, segredo em
URL/log, SSRF, injeção, ação destrutiva, dados de terceiros, offline.
Ver `governance/SECURITY-AND-PRIVACY-POLICY.md` §3.

Regra: **nenhum teste ofensivo** contra sistema de terceiro. Análise documental e
leitura de código apenas. Vulnerabilidade não corrigida não vira PoC público.

## 3. Especialista em licenças

**Pergunta:** "Podemos distribuir isso?"

Ler o arquivo `LICENSE` no commit analisado. Separar código/conteúdo/pesos/marca.
Identificar obrigações e classe de aproveitamento. **Nunca** atribuir licença a
material sem licença. Nunca emitir conclusão jurídica — emitir pendência.

## 4. Especialista em desempenho

**Pergunta:** "Cabe e roda no hardware real do usuário?"

Hardware de referência do ecossistema: Windows 11 x64, AMD RX 580 8 GB (Polaris/gfx803),
Ryzen 5 5500, 16 GB RAM.

Regras:
- número de terceiro é `REPORTED`, nunca resultado local;
- "detectou o dispositivo" ≠ "executou rápido";
- sempre distinguir tamanho de arquivo de pico de memória de trabalho;
- benchmark só com `templates/benchmark-report.md` preenchido.

## 5. Especialista em produto e UX

**Pergunta:** "Isso melhora a vida do usuário da Lia — e a que custo de atenção?"

Avaliar: fluxo, estados de erro, acessibilidade (teclado, foco, ARIA), custo de
aprendizado, coerência com a identidade dos produtos Lia. Não propor feature nova
por analogia com repositório pesquisado.

## 6. Especialista por tipo de objeto (cobertura de 2026-11-20)

O papel acompanha o **tipo** do objeto, não o nome do repositório. Cada tipo tem modelo
próprio em `templates/README.md`.

| Tipo | Quem cobre | O que precisa saber olhar |
|---|---|---|
| repositório / ferramenta | arquitetura + licença | build real, dependências pesadas, licença por diretório |
| servidor MCP | segurança + arquitetura | superfície de ferramenta, autenticação, o que o servidor vê do host |
| Skill / agente empacotado | licença + produto | payload vs instrução, proveniência, o que executa no host |
| modelo + pesos | desempenho + licença | licença de **pesos** ≠ licença de código; hardware; quantização |
| API / SaaS | produto + licença | termos de uso, quota, retenção de dados, custo por uso |
| paper / benchmark | desempenho | reprodutibilidade, tamanho de amostra, conflito de interesse |
| voz / visão / multimodal | desempenho + produto | latência, idioma, dados de treino declarados |
| hardware / automação | desempenho + segurança | driver, sessão real, risco físico — Nível 3 |

## 7. Regras comuns

1. Entregar bullets com rótulo de evidência e ponteiro (`repo@sha:path`).
2. Declarar o que não conseguiu verificar.
3. Não editar arquivo do repositório — entregar texto ao Orchestrator.
4. Não publicar, não commitar, não abrir PR.
5. Se a tarefa exigir decisão de produto, devolver como pergunta, não como conclusão.
