---
title: Web
source_url: https://docs.openclaw.ai/es/web
scraped_at: 2026-05-25
---

El Gateway sirve una pequeña **UI de control en navegador** (Vite + Lit) desde el mismo puerto que el WebSocket del Gateway:

  * predeterminado: `http://<host>:18789/`
  * con `gateway.tls.enabled: true`: `https://<host>:18789/`
  * prefijo opcional: configura `gateway.controlUi.basePath` (p. ej., `/openclaw`)


Las capacidades están en [UI de control](</es/web/control-ui>). El resto de esta página se centra en los modos de enlace, la seguridad y las superficies expuestas a la web.

## Webhooks

Cuando `hooks.enabled=true`, el Gateway también expone un pequeño endpoint de webhook en el mismo servidor HTTP. Consulta [Configuración del Gateway](</es/gateway/configuration>) → `hooks` para autenticación y cargas útiles.

## Configuración (activada de forma predeterminada)

La UI de control está **activada de forma predeterminada** cuando los recursos están presentes (`dist/control-ui`). Puedes controlarla mediante configuración:

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath optional  },}
[/code]

## Acceso con Tailscale

### Serve integrado (recomendado)

Mantén el Gateway en loopback y deja que Tailscale Serve lo proxifique:

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

Luego inicia el gateway:

bashCopy code
[code]
    openclaw gateway
[/code]

Abre:

  * `https://<magicdns>/` (o tu `gateway.controlUi.basePath` configurado)


### Enlace de tailnet + token

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

Luego inicia el gateway (este ejemplo no loopback usa autenticación con token de secreto compartido):

bashCopy code
[code]
    openclaw gateway
[/code]

Abre:

  * `http://<tailscale-ip>:18789/` (o tu `gateway.controlUi.basePath` configurado)


### Internet público (Funnel)

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // or OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## Notas de seguridad

  * La autenticación del Gateway es obligatoria de forma predeterminada (token, contraseña, proxy de confianza o encabezados de identidad de Tailscale Serve cuando están activados).
  * Los enlaces que no son loopback siguen **requiriendo** autenticación del gateway. En la práctica, eso significa autenticación con token/contraseña o un proxy inverso consciente de identidad con `gateway.auth.mode: "trusted-proxy"`.
  * El asistente crea autenticación con secreto compartido de forma predeterminada y normalmente genera un token de gateway (incluso en loopback).
  * En modo de secreto compartido, la UI envía `connect.params.auth.token` o `connect.params.auth.password`.
  * Cuando `gateway.tls.enabled: true`, los ayudantes locales de panel y estado renderizan URLs de panel `https://` y URLs de WebSocket `wss://`.
  * En modos con identidad, como Tailscale Serve o `trusted-proxy`, la comprobación de autenticación del WebSocket se satisface en su lugar desde los encabezados de la solicitud.
  * Para despliegues de la UI de control que no sean loopback, configura `gateway.controlUi.allowedOrigins` explícitamente (orígenes completos). Sin esto, el arranque del gateway se rechaza de forma predeterminada.
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` activa el modo de respaldo de origen basado en el encabezado Host, pero es una degradación de seguridad peligrosa.
  * Con Serve, los encabezados de identidad de Tailscale pueden satisfacer la autenticación de la UI de control/WebSocket cuando `gateway.auth.allowTailscale` es `true` (no se requiere token/contraseña). Los endpoints de la API HTTP no usan esos encabezados de identidad de Tailscale; en su lugar siguen el modo normal de autenticación HTTP del gateway. Configura `gateway.auth.allowTailscale: false` para exigir credenciales explícitas. Consulta [Tailscale](</es/gateway/tailscale>) y [Seguridad](</es/gateway/security>). Este flujo sin token presupone que el host del gateway es de confianza.
  * `gateway.tailscale.mode: "funnel"` requiere `gateway.auth.mode: "password"` (contraseña compartida).


## Compilar la UI

El Gateway sirve archivos estáticos desde `dist/control-ui`. Compílalos con:

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo