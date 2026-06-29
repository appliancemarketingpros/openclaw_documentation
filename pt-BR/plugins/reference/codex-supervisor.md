---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/pt-BR/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin Codex Supervisor

Supervisione sessões do servidor de aplicativo Codex pelo OpenClaw.

## Distribuição

  * Pacote: `@openclaw/codex-supervisor`
  * Rota de instalação: incluído no OpenClaw


## Superfície

contratos: ferramentas

## Listagem de sessões

`codex_sessions_list` usa por padrão apenas sessões Codex carregadas. Defina `include_stored` para incluir o histórico armazenado; o plugin usa o caminho de listagem apenas do banco de dados de estado do servidor de aplicativo Codex e limita os resultados armazenados a 200 por padrão. Passe `max_stored_sessions` para reduzir ou aumentar esse limite, até 1000.

Was this useful?YesNo

Open issue