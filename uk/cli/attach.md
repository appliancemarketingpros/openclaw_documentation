---
title: Підключення CLI
source_url: https://docs.openclaw.ai/uk/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` запускає Claude Code зі суворою тимчасовою конфігурацією MCP, привʼязаною до одного сеансу Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Параметри:

  * `--session <key>` привʼязує дозвіл до сеансу Gateway. За замовчуванням використовується основний сеанс.
  * `--ttl <ms>` запитує додатний TTL дозволу в мілісекундах. Gateway застосовує власну верхню межу.
  * `--bin <path>` вибирає бінарний файл Claude Code. За замовчуванням використовується `claude`.
  * `--print-config` записує тимчасовий `.mcp.json`, виводить команду запуску й змінні середовища та залишає дозвіл активним до завершення TTL.


Bearer-токен передається через змінні середовища, а не через argv. OpenClaw запускає Claude Code з `--strict-mcp-config --mcp-config <path>`, щоб навколишні сервери Claude MCP не приєднувалися до прикріпленого сеансу. Звичайні запуски відкликають дозвіл, коли процес Claude Code завершується.

Див. також: [Gateway CLI](</uk/cli/gateway>), [MCP CLI](</uk/cli/mcp>) і [ACP CLI](</uk/cli/acp>).

Was this useful?YesNo

Open issue