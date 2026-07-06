---
title: Adjuntar CLI
source_url: https://docs.openclaw.ai/es/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` inicia Claude Code con una configuración MCP temporal estricta vinculada a una sesión de Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Opciones:

  * `--session <key>` vincula la concesión a una sesión de Gateway. De forma predeterminada, usa la sesión principal.
  * `--ttl <ms>` solicita un TTL de concesión positivo en milisegundos. El Gateway aplica su propio límite máximo.
  * `--bin <path>` selecciona el binario de Claude Code. Valor predeterminado: `claude`.
  * `--print-config` escribe el `.mcp.json` temporal, imprime el comando de inicio y el entorno, y deja la concesión activa hasta que expire el TTL (no inicia Claude Code ni revoca la concesión).


El token de portador se pasa mediante variables de entorno, no por argv. OpenClaw inicia Claude Code con `--strict-mcp-config --mcp-config <path>` para que los servidores MCP de Claude del entorno no se unan a la sesión adjunta. Los inicios normales (sin `--print-config`) revocan la concesión cuando finaliza el proceso de Claude Code.

Consulta también: [CLI de Gateway](</es/cli/gateway>), [CLI de MCP](</es/cli/mcp>) y [CLI de ACP](</es/cli/acp>).

Was this useful?YesNo

Open issue