---
title: Dashboard
source_url: https://docs.openclaw.ai/nl/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Open de Control UI met je huidige authenticatie.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Opmerkingen:

  * `dashboard` zet geconfigureerde `gateway.auth.token` SecretRefs om wanneer dat mogelijk is.
  * `dashboard` volgt `gateway.tls.enabled`: gateways met TLS ingeschakeld tonen/openen `https://` Control UI-URL's en verbinden via `wss://`.
  * Als levering via klembord/browser mislukt voor een dashboard-URL met tokenauthenticatie, logt `dashboard` een veilige hint voor handmatige authenticatie met de namen `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` en fragmentsleutel `token`, zonder de tokenwaarde te tonen.
  * Voor door SecretRef beheerde tokens (opgelost of onopgelost) toont/kopieert/opent `dashboard` een URL zonder token om te voorkomen dat externe geheimen worden blootgesteld in terminaluitvoer, klembordgeschiedenis of browserstartargumenten.
  * Als `gateway.auth.token` door SecretRef wordt beheerd maar in dit opdrachtpad niet kan worden opgelost, toont de opdracht een URL zonder token en expliciete herstelrichtlijnen in plaats van een ongeldige tokenplaceholder in te sluiten.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Dashboard](</nl/web/dashboard>)


Was this useful?YesNo