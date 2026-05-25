---
title: Proxy de API Claude Max
source_url: https://docs.openclaw.ai/es/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** es una herramienta de la comunidad que expone tu suscripción Claude Max/Pro como un endpoint de API compatible con OpenAI. Esto te permite usar tu suscripción con cualquier herramienta que admita el formato de API de OpenAI.

## ¿Por qué usar esto?

Enfoque | Costo | Ideal para  
---|---|---  
API de Anthropic | Pago por token (~$15/M entrada, $75/M salida para Opus) | Apps de producción, alto volumen  
Suscripción Claude Max | $200/mes fijo | Uso personal, desarrollo, uso ilimitado  
  
Si tienes una suscripción Claude Max y quieres usarla con herramientas compatibles con OpenAI, este proxy puede reducir el costo en algunos flujos de trabajo. Las claves API siguen siendo la vía de política más clara para uso en producción.

## Cómo funciona

CodeCopy code
[code]
    Tu app → claude-max-api-proxy → Claude Code CLI → Anthropic (mediante suscripción) (formato OpenAI)              (convierte formato)      (usa tu inicio de sesión)
[/code]

El proxy:

  1. Acepta solicitudes en formato OpenAI en `http://localhost:3456/v1/chat/completions`
  2. Las convierte en comandos de Claude Code CLI
  3. Devuelve respuestas en formato OpenAI (admite streaming)


## Primeros pasos

* ### Instalar el proxy

Requiere Node.js 20+ y Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verifica que Claude CLI esté autenticadoclaude --version
[/code]

* ### Iniciar el servidor

bashCopy code
[code]
    claude-max-api# El servidor se ejecuta en http://localhost:3456
[/code]

* ### Probar el proxy

bashCopy code
[code]
    # Comprobación de estadocurl http://localhost:3456/health # Enumerar modeloscurl http://localhost:3456/v1/models # Finalización de chatcurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Configurar OpenClaw

Apunta OpenClaw al proxy como endpoint personalizado compatible con OpenAI:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Catálogo integrado

ID del modelo | Se asigna a  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Configuración avanzada

Notas de estilo proxy compatibles con OpenAI

Esta ruta usa la misma ruta de estilo proxy compatible con OpenAI que otros backends personalizados `/v1`:

  * No se aplica el moldeado de solicitudes nativo exclusivo de OpenAI
  * No hay `service_tier`, ni `store` de Responses, ni sugerencias de caché de prompts, ni moldeado de carga útil de compatibilidad de razonamiento de OpenAI
  * Los encabezados ocultos de atribución de OpenClaw (`originator`, `version`, `User-Agent`) no se inyectan en la URL del proxy

Inicio automático en macOS con LaunchAgent

Crea un LaunchAgent para ejecutar el proxy automáticamente:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Enlaces

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Notas

  * Esta es una **herramienta de la comunidad** , sin soporte oficial de Anthropic ni de OpenClaw
  * Requiere una suscripción activa Claude Max/Pro con Claude Code CLI autenticado
  * El proxy se ejecuta localmente y no envía datos a servidores de terceros
  * Las respuestas en streaming están totalmente admitidas


## Relacionado

[**Proveedor Anthropic** Integración nativa de OpenClaw con Claude CLI o claves API. ](</es/providers/anthropic>) [**Proveedor OpenAI** Para suscripciones OpenAI/Codex. ](</es/providers/openai>) [**Selección de modelo** Descripción general de todos los proveedores, referencias de modelo y comportamiento de failover. ](</es/concepts/model-providers>) [**Configuración** Referencia completa de configuración. ](</es/gateway/configuration>)

Was this useful?YesNo