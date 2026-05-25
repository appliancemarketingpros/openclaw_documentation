---
title: Autocompletado
source_url: https://docs.openclaw.ai/es/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Genera scripts de autocompletado del shell y, opcionalmente, los instala en el perfil de tu shell.

## Uso

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Opciones

  * `-s, --shell <shell>`: destino del shell (`zsh`, `bash`, `powershell`, `fish`; predeterminado: `zsh`)
  * `-i, --install`: instala el autocompletado añadiendo una línea `source` a tu perfil de shell
  * `--write-state`: escribe los scripts de autocompletado en `$OPENCLAW_STATE_DIR/completions` sin imprimirlos en stdout
  * `-y, --yes`: omite las solicitudes de confirmación de instalación


## Notas

  * `--install` escribe un pequeño bloque "OpenClaw Completion" en el perfil de tu shell y lo apunta al script almacenado en caché.
  * Sin `--install` ni `--write-state`, el comando imprime el script en stdout.
  * La generación de autocompletado carga de forma anticipada los árboles de comandos para incluir subcomandos anidados.


## Relacionado

  * [Referencia de la CLI](</es/cli>)


Was this useful?YesNo