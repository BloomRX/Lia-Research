# Política de segurança e privacidade

---

## 1. Nunca armazenar

- Tokens (inclusive *long-lived access tokens* de Home Assistant, GitHub PAT, tokens de provider).
- API keys, secrets, client secrets OIDC, service accounts.
- Senhas, cookies de sessão, cookies de navegador.
- Credenciais de contas pessoais de qualquer serviço.
- Dumps de sessão privada, transcrições com dados de terceiros.
- Arquivos de configuração que contenham segredos (`.env`, `config.toml` com chave).
- Endereços residenciais, nomes de familiares, rotinas, localização.

Se um relatório precisa citar uma configuração, **sanitizar**:

```diff
- HOMEASSISTANT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOi...
+ HOMEASSISTANT_TOKEN=<REDACTED:HA_LLAT>
- MCP_BASE_URL=https://casa-do-usuario.duckdns.org
+ MCP_BASE_URL=https://<REDACTED:HOST>
```

## 2. Regra de teste com serviço de terceiro

Ao testar provider, roteador ou API comercial (categoria que inclui o RouterHub):

- usar conta descartável e chave descartável;
- **nunca** enviar dados pessoais, credenciais, trechos de código proprietário da
  Lia ou informação de usuário;
- prompts de teste são sintéticos e genéricos;
- registrar o que foi enviado, quando, e a política de retenção declarada;
- nunca colar a chave no relatório, em issue, ou em log.

Na fundação de 2026-11-17 **nenhuma chamada autenticada** a serviço comercial foi
feita. Toda análise de RouterHub é documental (`REPORTED`/`OBSERVED`).

## 3. Superfície de risco a avaliar em toda integração

Checklist mínimo (usado no HA-MCP e no Mister Download Manager):

| Vetor | Perguntas obrigatórias |
|---|---|
| Autenticação | como a ferramenta prova quem chama? token, OAuth, OIDC, segredo na URL? |
| Autorização | um cliente pode restringir a própria permissão (read-only) sem afetar outros? |
| Exposição de rede | escuta em loopback ou 0.0.0.0? qual porta? há TLS? |
| Segredos em URL | o segredo aparece em log, histórico ou referrer? |
| SSRF | há campo onde o cliente informa URL que o servidor busca? |
| Injeção | o conteúdo devolvido por dispositivo/modelo é tratado como dados ou como instrução? |
| Ações destrutivas | apagar, desligar, restaurar: há confirmação explícita e backup? |
| Rastreabilidade | há log auditável de quem pediu o quê? |
| Dados de terceiros | a ferramenta recebe cookies/credenciais do navegador? para onde vão? |
| Offline | funciona sem internet? depende de nuvem para o caminho principal? |

## 4. Ações de alto risco (regra do ecossistema)

Categoria de ação define o gates, **não** a ferramenta:

| Nível | Exemplos | Gate |
|---|---|---|
| R0 leitura | temperatura, estado de lâmpada, listar dispositivos | nenhum além de log |
| R1 ação comum | ligar/desligar luz, ajustar brilho, criar cena | confirmação configurável, reversível |
| R2 ação sensível | abrir fechadura, desativar alarme, apagar automação | autorização explícita por ação, não persistente |
| R3 sistêmico | desligar tudo, reiniciar Home Assistant, apagar backup, escrever YAML | dupla confirmação + backup + registro |

Essa matriz é proposta, não definitiva: ver `repositories/ha-mcp/RISK-MATRIX.md`.
Qualquer ajuste exige decisão registrada.

## 5. Dados de usuário em pesquisa

- Preferir dados sintéticos.
- Se um dado real for inevitável, agregar e anonimizar antes de escrever.
- Não criar CSV/JSON com dados pessoais no repositório. Se necessário, descrever o
  esquema, não o conteúdo.
- Dados de benchmark de hardware do usuário são aceitáveis (são do proprietário),
  mas não devem revelar hostname, IP ou serial.

## 6. Resposta a incidente

Se um segredo for commitado acidentalmente neste repositório:

1. **Rotacionar o segredo imediatamente** — remover o commit não basta.
2. Abrir issue `security` descrevendo o tipo (sem o valor).
3. Registrar em `RESEARCH-CHANGELOG.md` que houve remoção de segredo e rotação.
4. Se o repositório estava público no momento, tratar como comprometido.

> Contexto real: este repositório foi criado em 2026-11-17 com visibilidade
> **pública** e a alteração para privada retornou HTTP 403 (token sem permissão de
> administração). Até a correção pelo proprietário, **nada sensível pode ser
> commitado**. Ver `LIA-RESEARCH-FOUNDATION-REPORT.md` §2.

## 7. Segurança de terceiros citados

Relatar vulnerabilidades conhecidas de projetos pesquisados é permitido e útil
(exemplo: advisories SSRF/XSS do ha-mcp corrigidos na v7.0.0). Nunca publicar PoC
de exploração não corrigida, nem detalhes que facilitem ataque a instalação de
usuário.
