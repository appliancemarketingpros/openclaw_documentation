---
title: Dołącz CLI
source_url: https://docs.openclaw.ai/pl/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` uruchamia Claude Code ze ścisłą tymczasową konfiguracją MCP powiązaną z jedną sesją Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Opcje:

  * `--session <key>` wiąże przyznane uprawnienie z sesją Gateway. Domyślnie jest to sesja główna.
  * `--ttl <ms>` żąda dodatniego TTL przyznanego uprawnienia w milisekundach. Gateway stosuje własny limit maksymalny.
  * `--bin <path>` wybiera plik binarny Claude Code. Domyślnie `claude`.
  * `--print-config` zapisuje tymczasowy plik `.mcp.json`, wypisuje polecenie uruchomieniowe i zmienne środowiskowe oraz pozostawia przyznane uprawnienie aktywne do wygaśnięcia TTL.


Token okaziciela jest przekazywany przez zmienne środowiskowe, a nie przez argv. OpenClaw uruchamia Claude Code z `--strict-mcp-config --mcp-config <path>`, dzięki czemu otaczające serwery MCP Claude nie dołączają do dołączonej sesji. Zwykłe uruchomienia unieważniają przyznane uprawnienie po zakończeniu procesu Claude Code.

Zobacz też: [CLI Gateway](</pl/cli/gateway>), [CLI MCP](</pl/cli/mcp>) i [CLI ACP](</pl/cli/acp>).

Was this useful?YesNo

Open issue