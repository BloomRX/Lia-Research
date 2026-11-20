# Proveniência dos SHAs — 2026-11-20

| Campo | Valor |
|---|---|
| Data | 2026-11-20 |
| Objetos | 23 (22 herdados de 2026-11-17 + `LR-STUDIO-006`) |
| Ferramenta | `gh api` somente leitura (`repos`, `commits`, `commits/<branch>`) |
| Saída bruta | `data/inventory/provenance-2026-11-20.tsv` |

## 1. O que estava inconsistente

`audits/REAUDIT-2026-11-20.md` §6 dizia "quatro objetos sem SHA no cabeçalho". A tabela
mostrava **cinco** linhas com `—` na coluna de SHA analisado:

`ai-memory` · `cloudflare-security-audit-skill` · `freellmapi` · `rescript-lang` · `routerhub`

**A contagem correta é cinco.** O texto estava errado, não a tabela: ele contava quatro
porque tratava `rescript-lang` e `routerhub` como "uma linha só" (ambos são organização).
Corrigido no próprio digest.

## 2. Como cada SHA foi tratado

| Situação | Objetos | Rótulo |
|---|---:|---|
| SHA citado no relatório | 17 | `INFORMADO_NO_RELATORIO` |
| Branch sem SHA, mas repo parado desde a data citada | 1 | `RECUPERADO_POR_ESTABILIDADE` |
| Branch sem SHA, com commits no dia da leitura | 2 | `CANDIDATO_POR_DATA` |
| Organização: não existe commit único | 2 | `INCOMPLETA_ORGANIZACAO` |

### 2.1 `RECUPERADO_POR_ESTABILIDADE` — cloudflare/security-audit-skill

O relatório cita `@main (2026-09-14)`. O último push do repositório é **2026-09-14**, e o
HEAD de hoje é `c1c8a8c14710…`, o mesmo commit daquela data. Qualquer leitura feita depois
de 2026-09-14 leu esse conteúdo — por isso o SHA é recuperável com segurança, não por
adivinhação.

### 2.2 `CANDIDATO_POR_DATA` — ai-memory e freellmapi

Os dois foram lidos de `@main` em **2026-11-19**, sem SHA. Em vez de inventar, registrei o
último commit **antes do fim daquele dia** e marquei como candidato:

| Pasta | Candidato | HEAD atual | Distância |
|---|---|---|---|
| `ai-memory` | `6a141858bb88…` | `6a141858bb88…` | **idêntico** |
| `freellmapi` | `dd0fb7135174…` | `dd0fb7135174…` | **idêntico** |

Que o HEAD coincida aumenta a confiança, mas não prova: o commit de 22:24 pode ter entrado
depois da leitura. O rótulo continua `CANDIDATO`, e a próxima reauditoria desses dois deve
começar confirmando o SHA antes de comparar conteúdo.

### 2.3 `INCOMPLETA_ORGANIZACAO` — rescript-lang e routerhub

- `rescript-lang`: a unidade analisada foi uma **organização** (39 repositórios). O
  relatório já declarava "não fixado". Não há SHA único a recuperar; para o compilador
  (`rescript-lang/rescript`) o HEAD atual está registrado, mas a análise foi do conjunto.
- `routerhub`: idem — 11 repositórios de marketing + serviço comercial. O que foi avaliado
  é a organização e o produto, não um commit. `DR-0005` rejeitou o **fork** `routerhubSI/litellm`;
  esse fork tem HEAD, mas ele não é o objeto do relatório.

Esses dois **não** devem ganhar SHA retroativo: seria inventar uma precisão que a pesquisa
não teve.

## 3. O que mudou nos relatórios

Cada um dos 23 relatórios ganhou três linhas de cabeçalho, sem tocar nas linhas antigas:

| Campo novo | Conteúdo |
|---|---|
| `SHA completo` | 40 caracteres quando conhecido; "não determinado" + motivo quando não |
| `Proveniência do SHA` | um dos quatro rótulos acima |
| `HEAD atual` | SHA de 40 caracteres, conferido em 2026-11-20 (organização: "sem HEAD único") |

`Versão analisada` / `Versão/commit` **não foram alteradas**: o valor histórico continua
onde estava, mesmo quando divergente do SHA completo.

## 4. Tabela completa

| Pasta | Upstream | SHA analisado | Proveniência |
|---|---|---|---|
| `ai-design-skills` | `elayadesign/ai-design-skills` | `456d9e0d3e2d84c748bb143c6ca3d90c45e16213` | INFORMADO_NO_RELATORIO |
| `ai-memory` | `akitaonrails/ai-memory` | `6a141858bb88fbd025b144664a37271acd5e0e43` | CANDIDATO_POR_DATA |
| `artcraft` | `storytold/photocraft` | `a858d42a5028287662e28e89be0bbce9d0bec6b5` | INFORMADO_NO_RELATORIO |
| `awesome-gamedev-agent-skills` | `gamedev-skills/awesome-gamedev-agent-skills` | `c6ca6c41c839b68319ffc08430b99ab768debc32` | INFORMADO_NO_RELATORIO |
| `brutal` | `ahwootech/BRUTAL` | `c4c62f55286828e51ba93b59ec7fa21ecedae3ca` | INFORMADO_NO_RELATORIO |
| `claude-bughunter` | `elementalsouls/Claude-BugHunter` | `b63ae349afad88772e6d854a277ae9965fd4c369` | INFORMADO_NO_RELATORIO |
| `claude-code-game-studios` | `Donchitos/Claude-Code-Game-Studios` | `abc0de79d6ceb0b5d7aa693945849b3937afbe6a` | INFORMADO_NO_RELATORIO |
| `claude-trading-skills` | `tradermonty/claude-trading-skills` | `a627d17dd1d8fde1c8fa73b3cc69ffe83b33cb71` | INFORMADO_NO_RELATORIO |
| `cloudflare-security-audit-skill` | `cloudflare/security-audit-skill` | `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` | RECUPERADO_POR_ESTABILIDADE |
| `freellmapi` | `tashfeenahmed/freellmapi` | `dd0fb71351746ed7bfcbe061a7aa7c6bdb291e1d` | CANDIDATO_POR_DATA |
| `ha-mcp` | `homeassistant-ai/ha-mcp` | `3dd26d45fbefa6fed999b618092a56005bb5d79c` | INFORMADO_NO_RELATORIO |
| `manimgx` | `academa-labs/manimgx` | `1fb4dd7327bf5ed7d0c40d022c05cb816455ae1d` | INFORMADO_NO_RELATORIO |
| `meldwork` | `Ryder-Sun/Meldwork` | `db9b6c84cbb1c86f3e3facf3cbebdcd6f1f79397` | INFORMADO_NO_RELATORIO |
| `misterdownloadmanager` | `anefzaoui/misterdownloadmanager` | `d9a9ef0621cb494a39999ab9adf433515a9d36a1` | INFORMADO_NO_RELATORIO |
| `openidea` | `l0ng-ai/openidea` | `182285647ee2a80e84c01157ae35d6b63f572d71` | INFORMADO_NO_RELATORIO |
| `openjarvis` | `open-jarvis/OpenJarvis` | `6656b7fed28e2ff1efa4e77987cf351f2d71eec0` | INFORMADO_NO_RELATORIO |
| `pixelfx` | `patch-gg/pixelfx` | `5294518ce7c72e48b6100a744596e0acf57f2826` | INFORMADO_NO_RELATORIO |
| `plannotator` | `backnotprop/plannotator` | `b5b3077838a1758960198dc404ee98e2a57acf6d` | INFORMADO_NO_RELATORIO |
| `rescript-lang` | `rescript-lang/rescript` | `` | INCOMPLETA_ORGANIZACAO |
| `routerhub` | `routerhubSI/litellm` | `` | INCOMPLETA_ORGANIZACAO |
| `sculptforge` | `islandmed/SculptForge` | `363e2b86cf8da3834206a9465a31560a8ea7e583` | INFORMADO_NO_RELATORIO |
| `unslop` | `theclaymethod/unslop` | `0f4a07f5ca8bb400b4d4450b00d67c6e4a30b85a` | INFORMADO_NO_RELATORIO |
| `vercel-ui` | `vercel-labs/ui` | `10b3b6c0eccfd176a6d60ce4efaccf0d1584da08` | INFORMADO_NO_RELATORIO |

## 5. Pendências

- `ai-memory` e `freellmapi`: confirmar SHA na próxima leitura (hoje `CANDIDATO`).
- `rescript-lang`: se o compilador for adotado como objeto próprio, abrir relatório de
  repositório (não de organização) com SHA.
- 4 relatórios ainda citam `@main` na seção de fontes, apesar de o cabeçalho já ter SHA —
  texto histórico, mantido e anotado.

Voltar: `audits/README.md` · `audits/REAUDIT-2026-11-20.md` · `catalog/catalog.tsv`
