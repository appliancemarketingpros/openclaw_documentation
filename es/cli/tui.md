---
title: TUI
source_url: https://docs.openclaw.ai/es/cli/tui
scraped_at: 2026-05-25
---

# `openclaw tui`

Abre la interfaz de terminal conectada al Gateway, o ejecútala en modo local integrado.

Relacionado:

  * Guía de TUI: [TUI](</es/web/tui>)


## Opciones

Opción | Predeterminado | Descripción  
---|---|---  
`--local` | `false` | Ejecuta contra el entorno de ejecución local integrado del agente en lugar de un Gateway.  
`--url <url>` | `gateway.remote.url` de la configuración | URL WebSocket del Gateway.  
`--token <token>` | (ninguno) | Token del Gateway si es necesario.  
`--password <pass>` | (ninguna) | Contraseña del Gateway si es necesaria.  
`--session <key>` | `main` (o `global` cuando el ámbito es global) | Clave de sesión. Dentro de un espacio de trabajo de agente selecciona automáticamente ese agente salvo que tenga prefijo.  
`--deliver` | `false` | Entrega las respuestas del asistente mediante los canales configurados.  
`--thinking <level>` | (predeterminado del modelo) | Sobrescritura del nivel de pensamiento.  
`--message <text>` | (ninguno) | Envía un mensaje inicial después de conectar.  
`--timeout-ms <ms>` | `agents.defaults.timeoutSeconds` | Tiempo de espera del agente. Los valores no válidos registran una advertencia y se ignoran.  
`--history-limit <n>` | `200` | Entradas del historial que se cargan al adjuntar.  
  
Alias: `openclaw chat` y `openclaw terminal` invocan el mismo comando con `--local` implícito.

Notas:

  * `chat` y `terminal` son alias de `openclaw tui --local`.
  * `--local` no se puede combinar con `--url`, `--token` ni `--password`.
  * `tui` resuelve los SecretRefs de autenticación del Gateway configurados para autenticación con token/contraseña cuando es posible (proveedores `env`/`file`/`exec`).
  * Cuando se inicia desde dentro de un directorio de espacio de trabajo de agente configurado, TUI selecciona automáticamente ese agente para el valor predeterminado de la clave de sesión (salvo que `--session` sea explícitamente `agent:<id>:...`).
  * El modo local usa directamente el entorno de ejecución integrado del agente. La mayoría de las herramientas locales funcionan, pero las funciones exclusivas del Gateway no están disponibles.
  * El modo local agrega `/auth [provider]` dentro de la superficie de comandos de TUI.
  * Los controles de aprobación de Plugin siguen aplicándose en modo local. Las herramientas que requieren aprobación solicitan una decisión en la terminal; nada se aprueba automáticamente en silencio porque el Gateway no interviene.


## Ejemplos

bashCopy code
[code]
    openclaw chatopenclaw tui --localopenclaw tuiopenclaw tui --url ws://127.0.0.1:18789 --token <token>openclaw tui --session main --deliveropenclaw chat --message "Compare my config to the docs and tell me what to fix"# when run inside an agent workspace, infers that agent automaticallyopenclaw tui --session bugfix
[/code]

## Bucle de reparación de configuración

Usa el modo local cuando la configuración actual ya se valida y quieres que el agente integrado la inspeccione, la compare con la documentación y ayude a repararla desde la misma terminal:

Si `openclaw config validate` ya falla, usa primero `openclaw configure` o `openclaw doctor --fix`. `openclaw chat` no omite la protección de configuración no válida.

bashCopy code
[code]
    openclaw chat
[/code]

Luego dentro de TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Aplica correcciones específicas con `openclaw config set` o `openclaw configure`, luego vuelve a ejecutar `openclaw config validate`. Consulta [TUI](</es/web/tui>) y [Configuración](</es/cli/config>).

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [TUI](</es/web/tui>)


Was this useful?YesNo