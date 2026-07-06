---
title: Anexar CLI
source_url: https://docs.openclaw.ai/pt-BR/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` inicia o Claude Code com uma configuração MCP temporária estrita vinculada a uma sessão do Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Opções:

  * `--session <key>` vincula a concessão a uma sessão do Gateway. O padrão é a sessão principal.
  * `--ttl <ms>` solicita um TTL positivo para a concessão, em milissegundos. O Gateway aplica seu próprio limite máximo.
  * `--bin <path>` seleciona o binário do Claude Code. O padrão é `claude`.
  * `--print-config` grava o `.mcp.json` temporário, imprime o comando de inicialização e o ambiente, e mantém a concessão ativa até o TTL expirar.


O token de portador é passado por variáveis de ambiente, não por argv. O OpenClaw inicia o Claude Code com `--strict-mcp-config --mcp-config <path>` para que os servidores MCP do Claude do ambiente não entrem na sessão anexada. Inicializações normais revogam a concessão quando o processo do Claude Code termina.

Veja também: [CLI do Gateway](</pt-BR/cli/gateway>), [CLI MCP](</pt-BR/cli/mcp>) e [CLI ACP](</pt-BR/cli/acp>).

Was this useful?YesNo

Open issue