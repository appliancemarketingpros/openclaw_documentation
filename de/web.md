---
title: Web
source_url: https://docs.openclaw.ai/de/web
scraped_at: 2026-05-25
---

Das Gateway stellt eine kleine **Browser-Control UI** (Vite + Lit) über denselben Port wie das Gateway-WebSocket bereit:

  * Standard: `http://<host>:18789/`
  * mit `gateway.tls.enabled: true`: `https://<host>:18789/`
  * optionales Präfix: Legen Sie `gateway.controlUi.basePath` fest (z. B. `/openclaw`)


Funktionen finden Sie unter [Control UI](</de/web/control-ui>). Der Rest dieser Seite konzentriert sich auf Bind-Modi, Sicherheit und webseitige Oberflächen.

## Webhooks

Wenn `hooks.enabled=true` ist, stellt das Gateway außerdem einen kleinen Webhook-Endpunkt auf demselben HTTP-Server bereit. Siehe [Gateway-Konfiguration](</de/gateway/configuration>) → `hooks` für Authentifizierung + Payloads.

## Konfiguration (standardmäßig aktiviert)

Die Control UI ist **standardmäßig aktiviert** , wenn Assets vorhanden sind (`dist/control-ui`). Sie können sie über die Konfiguration steuern:

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath optional  },}
[/code]

## Tailscale-Zugriff

### Integriertes Serve (empfohlen)

Lassen Sie das Gateway auf loopback und lassen Sie Tailscale Serve es per Proxy weiterleiten:

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

Starten Sie dann das Gateway:

bashCopy code
[code]
    openclaw gateway
[/code]

Öffnen Sie:

  * `https://<magicdns>/` (oder Ihr konfiguriertes `gateway.controlUi.basePath`)


### Tailnet-Bind + Token

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

Starten Sie dann das Gateway (dieses Non-loopback-Beispiel verwendet Shared-Secret-Token-Authentifizierung):

bashCopy code
[code]
    openclaw gateway
[/code]

Öffnen Sie:

  * `http://<tailscale-ip>:18789/` (oder Ihr konfiguriertes `gateway.controlUi.basePath`)


### Öffentliches Internet (Funnel)

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // or OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## Sicherheitshinweise

  * Gateway-Authentifizierung ist standardmäßig erforderlich (Token, Passwort, Trusted-Proxy oder Tailscale Serve-Identity-Header, wenn aktiviert).
  * Non-loopback-Bindings **erfordern** weiterhin Gateway-Authentifizierung. In der Praxis bedeutet das Token-/Passwort-Authentifizierung oder einen identitätsbewussten Reverse Proxy mit `gateway.auth.mode: "trusted-proxy"`.
  * Der Assistent erstellt standardmäßig Shared-Secret-Authentifizierung und generiert in der Regel ein Gateway-Token (auch auf loopback).
  * Im Shared-Secret-Modus sendet die UI `connect.params.auth.token` oder `connect.params.auth.password`.
  * Wenn `gateway.tls.enabled: true` ist, geben lokale Dashboard- und Status-Helfer `https://`-Dashboard-URLs und `wss://`-WebSocket-URLs aus.
  * In Modi mit Identitätsinformationen wie Tailscale Serve oder `trusted-proxy` wird die WebSocket-Authentifizierungsprüfung stattdessen über Request-Header erfüllt.
  * Für Non-loopback-Control-UI-Bereitstellungen legen Sie `gateway.controlUi.allowedOrigins` explizit fest (vollständige Origins). Ohne diese Einstellung wird der Gateway-Start standardmäßig verweigert.
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` aktiviert den Host-Header-Origin-Fallback-Modus, ist jedoch eine gefährliche Sicherheitsherabstufung.
  * Mit Serve können Tailscale-Identity-Header die Control-UI-/WebSocket-Authentifizierung erfüllen, wenn `gateway.auth.allowTailscale` `true` ist (kein Token/Passwort erforderlich). HTTP-API-Endpunkte verwenden diese Tailscale-Identity-Header nicht; sie folgen stattdessen dem normalen HTTP-Authentifizierungsmodus des Gateways. Setzen Sie `gateway.auth.allowTailscale: false`, um explizite Zugangsdaten zu verlangen. Siehe [Tailscale](</de/gateway/tailscale>) und [Sicherheit](</de/gateway/security>). Dieser tokenlose Ablauf setzt voraus, dass der Gateway-Host vertrauenswürdig ist.
  * `gateway.tailscale.mode: "funnel"` erfordert `gateway.auth.mode: "password"` (gemeinsames Passwort).


## UI erstellen

Das Gateway stellt statische Dateien aus `dist/control-ui` bereit. Erstellen Sie sie mit:

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo