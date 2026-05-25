---
title: Panel de control
source_url: https://docs.openclaw.ai/es/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Abre la IU de Control con tu autenticación actual.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Notas:

  * `dashboard` resuelve las SecretRefs configuradas de `gateway.auth.token` cuando es posible.
  * `dashboard` respeta `gateway.tls.enabled`: las instancias de Gateway con TLS habilitado imprimen/abren URL de la IU de Control con `https://` y se conectan mediante `wss://`.
  * Si falla la entrega al portapapeles/navegador de una URL de dashboard autenticada con token, `dashboard` registra una indicación segura de autenticación manual que nombra `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` y la clave de fragmento `token` sin imprimir el valor del token.
  * Para tokens administrados por SecretRef (resueltos o sin resolver), `dashboard` imprime/copia/abre una URL sin token para evitar exponer secretos externos en la salida del terminal, el historial del portapapeles o los argumentos de inicio del navegador.
  * Si `gateway.auth.token` está administrado por SecretRef pero no se resuelve en esta ruta de comando, el comando imprime una URL sin token y una guía de corrección explícita en lugar de incrustar un marcador de posición de token no válido.


## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Dashboard](</es/web/dashboard>)


Was this useful?YesNo