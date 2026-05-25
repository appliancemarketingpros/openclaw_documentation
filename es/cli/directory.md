---
title: Directorio
source_url: https://docs.openclaw.ai/es/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

Búsquedas de directorio para los canales que las admiten (contactos/pares, grupos y "me").

## Opciones comunes

  * `--channel <name>`: id/alias del canal (obligatorio cuando hay varios canales configurados; automático cuando solo hay uno configurado)
  * `--account <id>`: id de la cuenta (predeterminado: valor predeterminado del canal)
  * `--json`: generar JSON


## Notas

  * `directory` está pensado para ayudarte a encontrar IDs que puedes pegar en otros comandos (especialmente `openclaw message send --target ...`).
  * En muchos canales, los resultados se basan en la configuración (listas de permitidos / grupos configurados) en lugar de en un directorio del proveedor en vivo.
  * Los plugins de canal instalados aún pueden omitir la compatibilidad con directorio; en ese caso, el comando informa la operación de directorio no admitida en lugar de reinstalar el Plugin.
  * La salida predeterminada es `id` (y a veces `name`) separada por una tabulación; usa `--json` para scripts.


## Usar resultados con `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## Formatos de ID (por canal)

  * WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (grupo), `120363123456789@newsletter` (destino saliente de Canal/Boletín)
  * Telegram: `@username` o id numérico de chat; los grupos son ids numéricos
  * Slack: `user:U…` y `channel:C…`
  * Discord: `user:<id>` y `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server` o `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` y `conversation:<id>`
  * Zalo (Plugin): id de usuario (API de Bot)
  * Zalo Personal / `zalouser` (Plugin): id de hilo (DM/grupo) de `zca` (`me`, `friend list`, `group list`)


## Usuario propio ("me")

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Pares (contactos/usuarios)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Grupos

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## Relacionado

  * [Referencia de CLI](</es/cli>)


Was this useful?YesNo