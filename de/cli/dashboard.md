---
title: Übersicht
source_url: https://docs.openclaw.ai/de/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Öffnen Sie die Control UI mit Ihrer aktuellen Authentifizierung.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Hinweise:

  * `dashboard` löst konfigurierte `gateway.auth.token`-SecretRefs auf, wenn möglich.
  * `dashboard` folgt `gateway.tls.enabled`: Gateways mit aktiviertem TLS geben/öffnen Control-UI-URLs mit `https://` aus und verbinden sich über `wss://`.
  * Wenn die Übergabe an Zwischenablage/Browser für eine tokenauthentifizierte Dashboard-URL fehlschlägt, protokolliert `dashboard` einen sicheren Hinweis zur manuellen Authentifizierung, der `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` und den Fragment-Schlüssel `token` nennt, ohne den Tokenwert auszugeben.
  * Für SecretRef-verwaltete Token (aufgelöst oder nicht aufgelöst) gibt/kopiert/öffnet `dashboard` eine URL ohne Token, um zu vermeiden, dass externe Secrets in der Terminalausgabe, im Zwischenablageverlauf oder in Browser-Startargumenten offengelegt werden.
  * Wenn `gateway.auth.token` SecretRef-verwaltet ist, aber in diesem Befehlspfad nicht aufgelöst wurde, gibt der Befehl eine URL ohne Token und explizite Hinweise zur Behebung aus, statt einen ungültigen Token-Platzhalter einzubetten.


## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Dashboard](</de/web/dashboard>)


Was this useful?YesNo