---
title: Plugin de WhatsApp
source_url: https://docs.openclaw.ai/es/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin de WhatsApp

Agrega la superficie de canal de WhatsApp para enviar y recibir mensajes de OpenClaw.

## Distribución

  * Paquete: `@openclaw/whatsapp`
  * Ruta de instalación: npm; ClawHub


## Superficie

channels: whatsapp

## Nota de instalación en Windows

En Windows, el Plugin de WhatsApp necesita Git en `PATH` durante la instalación de npm porque una de sus dependencias de Baileys/libsignal se obtiene desde una URL de git. Instala Git for Windows, luego reinicia el shell y vuelve a ejecutar la instalación:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Git portátil también funciona si su directorio `bin` está en `PATH`.

## Documentación relacionada

  * [WhatsApp](</es/channels/whatsapp>)


Was this useful?YesNo