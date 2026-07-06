---
title: Подключение через CLI
source_url: https://docs.openclaw.ai/ru/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` запускает Claude Code со строгой временной конфигурацией MCP, привязанной к одному сеансу Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Параметры:

  * `--session <key>` привязывает grant к сеансу Gateway. По умолчанию используется основной сеанс.
  * `--ttl <ms>` запрашивает положительный TTL grant в миллисекундах. Gateway применяет собственный верхний предел.
  * `--bin <path>` выбирает бинарный файл Claude Code. По умолчанию используется `claude`.
  * `--print-config` записывает временный `.mcp.json`, выводит команду запуска и env и оставляет grant активным до истечения TTL.


Bearer-токен передается через переменные окружения, а не через argv. OpenClaw запускает Claude Code с `--strict-mcp-config --mcp-config <path>`, чтобы фоновые MCP-серверы Claude не подключались к присоединенному сеансу. При обычных запусках grant отзывается, когда процесс Claude Code завершается.

См. также: [Gateway CLI](</ru/cli/gateway>), [MCP CLI](</ru/cli/mcp>) и [ACP CLI](</ru/cli/acp>).

Was this useful?YesNo

Open issue