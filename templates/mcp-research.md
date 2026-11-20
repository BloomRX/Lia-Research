# Template — servidor MCP

| Campo | Valor |
|---|---|
| ID | `LR-MCP-000` |
| Tipo | mcp |
| Estado da pesquisa | DISCOVERED \| TRIAGED \| INVESTIGATING \| DOCUMENTED \| PARTIALLY_TESTED \| NOT_TESTED \| BLOCKED |
| Resultado de execução | NOT_RUN \| STATIC_REVIEW_ONLY \| LOCAL_SMOKE_PASS \| PARTIAL \| BLOCKED |
| Recomendação | ADAPT \| REFERENCE_ONLY \| REJECT \| INSUFFICIENT_EVIDENCE |
| Decisão de adoção | — (nenhuma registrada) |
| Versão analisada | `repo@sha` (data) |
| Última verificação | AAAA-MM-DD |
| Licença | SPDX lido do arquivo |

## 1. Identificação e fonte oficial
## 2. Protocolo e transporte (stdio · SSE · streamable HTTP · stdio+HTTP)
## 3. Ferramentas expostas (nome, descrição, parâmetros, schema)
## 4. Operações destrutivas (o que apaga/move/gasta; há confirmação?)
## 5. Autenticação e permissões (token, OAuth, escopo, raiz de arquivo)
## 6. Isolamento (processo separado? rede? acesso a FS? sandbox?)
## 7. Conexão e configuração (como registrar sem tocar no ambiente do proprietário)
## 8. Compatibilidade com agentes (Claude Code, Hub, clientes genéricos)
## 9. Testes (Nível 0/1/2 conforme `governance/TESTING-PROTOCOL.md` + linha no log)
## 10. Segurança (superfície, prompt injection via resposta, exfiltração)
## 11. Licença e proveniência
## 12. Maturidade e manutenção
## 13. Limitações
## 14. Aplicações potenciais no ecossistema Lia
## 15. Evidências (com rótulo)
## 16. Recomendação (opinião técnica — não é aprovação)
## 17. Próximos passos
