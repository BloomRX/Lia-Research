# Política de segurança e privacidade

> **Limite de autoridade.** Pesquisa recomenda; não aprova adoção. Vocabulário fechado,
> estados e resultado de execução: `catalog/CATALOG-SCHEMA.md`. Protocolo de
> investigação: `governance/INVESTIGATION-PROTOCOL.md`; de teste:
> `governance/TESTING-PROTOCOL.md`.


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

> **Contexto (atualizado em 2026-11-17):** este repositório é **público por decisão do
> proprietário** (`BloomRX/Lia-Research@c9e6e97`, README da `main`). Não há correção de
> visibilidade pendente: a fundação havia registrado a tentativa como bloqueio
> (`DR-0006`), e o proprietário resolveu a questão decidindo manter público.
>
> Consequência: a política de conteúdo é **permanente**, não transitória. Nada sensível
> entra, em nenhuma hipótese, e toda coleta passa por revisão de exposição pública antes
> de ser versionada — procedimento em
> `governance/PUBLIC-EXPOSURE-REVIEW-2026-11-17.md`.

## 7. Segurança de terceiros citados

Relatar vulnerabilidades conhecidas de projetos pesquisados é permitido e útil
(exemplo: advisories SSRF/XSS do ha-mcp corrigidos na v7.0.0). Nunca publicar PoC
de exploração não corrigida, nem detalhes que facilitem ataque a instalação de
usuário.

## 8. Repositório público: higiene obrigatória (2026-11-20)

Este repositório é público por decisão do proprietário (`DR-0006`). Todo byte publicado é
legível por terceiros, inclusive por agentes que não são da Lia.

| Nunca entra | Como é verificado |
|---|---|
| token, chave, cookie, sessão, `id_rsa` | padrões de segredo em `tools/validate.py` (`gh*_`, `sk-`, `AKIA`, chave privada) |
| `.env` real, string de conexão com senha | revisão manual + validador |
| dado pessoal de terceiro (e-mail, telefone, endereço) | revisão do revisor; e-mail de autor de pacote só em tabela de atribuição |
| dump de sessão de agente, log com payload do usuário | não se publica log bruto; publica-se o achado |
| caminho local do proprietário (`C:\Users\…`) | trocar por caminho relativo |
| credencial real em exemplo de código | placeholder explícito (`<TOKEN_AQUI>`) |

Varredura de 2026-11-20, feita antes de publicar esta rodada: `git grep` sobre todos os
arquivos versionados (`.md`, `.tsv`, `.py`, `.gz` descompactado) não encontrou segredo real.
As únicas correspondências de padrão de chave eram fixtures sintéticos já documentados
(prefixo `gsk-` seguido de 26 caracteres fictícios `ABCDEF…`, usado por um teste que prova que a chave não vaza).

**Fronteira com o jurídico.** Esta base investiga licença e proveniência; **não emite
parecer jurídico** e não "concede" licença. O que se escreve é: o que o arquivo diz, o que
ele exige, e o que fica em dúvida. A decisão sobre risco jurídico é do proprietário.
