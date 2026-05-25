---
title: Registro de macOS
source_url: https://docs.openclaw.ai/es/platforms/mac/logging
scraped_at: 2026-05-25
---

# Registro (macOS)

## Registro de archivo de diagnósticos rotativo (panel de depuración)

OpenClaw enruta los registros de la app de macOS a través de swift-log (registro unificado de forma predeterminada) y puede escribir un registro de archivo local y rotativo en disco cuando necesitas una captura duradera.

  * Nivel de detalle: **panel de depuración → Registros → Registro de la app → Nivel de detalle**
  * Activar: **panel de depuración → Registros → Registro de la app → "Escribir registro de diagnósticos rotativo (JSONL)"**
  * Ubicación: `~/Library/Logs/OpenClaw/diagnostics.jsonl` (rota automáticamente; los archivos antiguos reciben los sufijos `.1`, `.2`, …)
  * Borrar: **panel de depuración → Registros → Registro de la app → "Borrar"**


Notas:

  * Está **desactivado de forma predeterminada**. Actívalo solo mientras estés depurando activamente.
  * Trata el archivo como sensible; no lo compartas sin revisarlo.


## Datos privados del registro unificado en macOS

El registro unificado redacta la mayoría de las cargas útiles salvo que un subsistema active `privacy -off`. Según el artículo de Peter sobre [maniobras de privacidad en el registro](<https://steipete.me/posts/2025/logging-privacy-shenanigans>) de macOS (2025), esto se controla mediante un plist en `/Library/Preferences/Logging/Subsystems/` identificado por el nombre del subsistema. Solo las entradas de registro nuevas toman la marca, así que actívala antes de reproducir un problema.

## Activar para OpenClaw (`ai.openclaw`)

  * Escribe primero el plist en un archivo temporal y luego instálalo atómicamente como root:

bashCopy code
[code]
    cat <<'EOF' >/tmp/ai.openclaw.plist<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>DEFAULT-OPTIONS</key>    <dict>        <key>Enable-Private-Data</key>        <true/>    </dict></dict></plist>EOFsudo install -m 644 -o root -g wheel /tmp/ai.openclaw.plist /Library/Preferences/Logging/Subsystems/ai.openclaw.plist
[/code]

  * No se requiere reiniciar; logd detecta el archivo rápidamente, pero solo las líneas de registro nuevas incluirán cargas útiles privadas.
  * Consulta la salida más completa con el ayudante existente, por ejemplo, `./scripts/clawlog.sh --category WebChat --last 5m`.


## Desactivar después de depurar

  * Elimina la anulación: `sudo rm /Library/Preferences/Logging/Subsystems/ai.openclaw.plist`.
  * Opcionalmente, ejecuta `sudo log config --reload` para forzar que logd descarte la anulación de inmediato.
  * Recuerda que esta superficie puede incluir números de teléfono y cuerpos de mensajes; mantén el plist en su lugar solo mientras necesites activamente el detalle adicional.


## Relacionado

  * [app de macOS](</es/platforms/macos>)
  * [Registro de Gateway](</es/gateway/logging>)


Was this useful?YesNo