---
title: Protocolo de puente
source_url: https://docs.openclaw.ai/es/gateway/bridge-protocol
scraped_at: 2026-05-25
---

## Por qué existía

  * **Límite de seguridad** : el puente expone una pequeña lista de permitidos en lugar de toda la superficie de la API del gateway.
  * **Emparejamiento + identidad del nodo** : la admisión de nodos pertenece al gateway y está vinculada a un token por nodo.
  * **UX de descubrimiento** : los nodos pueden descubrir gateways mediante Bonjour en la LAN, o conectarse directamente a través de una tailnet.
  * **WS de loopback** : el plano de control WS completo permanece local salvo que se tunelice mediante SSH.


## Transporte

  * TCP, un objeto JSON por línea (JSONL).
  * TLS opcional (cuando `bridge.tls.enabled` es true).
  * El puerto listener predeterminado histórico era `18790` (las compilaciones actuales no inician un puente TCP).


Cuando TLS está habilitado, los registros TXT de descubrimiento incluyen `bridgeTls=1` más `bridgeTlsSha256` como pista no secreta. Ten en cuenta que los registros TXT de Bonjour/mDNS no están autenticados; los clientes no deben tratar la huella anunciada como un pin autorizado sin intención explícita del usuario u otra verificación fuera de banda.

## Handshake + emparejamiento

  1. El cliente envía `hello` con metadatos del nodo + token (si ya está emparejado).
  2. Si no está emparejado, el gateway responde `error` (`NOT_PAIRED`/`UNAUTHORIZED`).
  3. El cliente envía `pair-request`.
  4. El Gateway espera aprobación y luego envía `pair-ok` y `hello-ok`.


Históricamente, `hello-ok` devolvía `serverName`; las superficies de Plugin alojadas ahora se anuncian mediante `pluginSurfaceUrls`. Canvas/A2UI usa `pluginSurfaceUrls.canvas`; el alias obsoleto `canvasHostUrl` no forma parte del protocolo refactorizado.

## Frames

Cliente → Gateway:

  * `req` / `res`: RPC de gateway con alcance (chat, sesiones, configuración, salud, voicewake, skills.bins)
  * `event`: señales del nodo (transcripción de voz, solicitud de agente, suscripción a chat, ciclo de vida de exec)


Gateway → Cliente:

  * `invoke` / `invoke-res`: comandos de nodo (`canvas.*`, `camera.*`, `screen.record`, `location.get`, `sms.send`)
  * `event`: actualizaciones de chat para sesiones suscritas
  * `ping` / `pong`: keepalive


La aplicación histórica de la lista de permitidos vivía en `src/gateway/server-bridge.ts` (eliminado).

## Eventos del ciclo de vida de exec

Los nodos pueden emitir eventos `exec.finished` o `exec.denied` para exponer actividad de system.run. Estos se asignan a eventos del sistema en el gateway. (Los nodos heredados todavía pueden emitir `exec.started`.)

Campos de payload (todos opcionales salvo que se indique lo contrario):

  * `sessionKey` (obligatorio): sesión del agente que recibe el evento del sistema.
  * `runId`: id único de exec para agrupación.
  * `command`: cadena de comando sin procesar o formateada.
  * `exitCode`, `timedOut`, `success`, `output`: detalles de finalización (solo finished).
  * `reason`: motivo de denegación (solo denied).


## Uso histórico de tailnet

  * Vincula el puente a una IP de tailnet: `bridge.bind: "tailnet"` en `~/.openclaw/openclaw.json` (solo histórico; `bridge.*` ya no es válido).
  * Los clientes se conectan mediante nombre MagicDNS o IP de tailnet.
  * Bonjour **no** atraviesa redes; usa host/puerto manual o DNS-SD de área amplia cuando sea necesario.


## Versionado

El puente era **v1 implícita** (sin negociación min/max). Esta sección es solo referencia histórica; los clientes actuales de nodo/operador usan el WebSocket [Protocolo Gateway](</es/gateway/protocol>).

## Relacionado

  * [Protocolo Gateway](</es/gateway/protocol>)
  * [Nodos](</es/nodes>)


Was this useful?YesNo