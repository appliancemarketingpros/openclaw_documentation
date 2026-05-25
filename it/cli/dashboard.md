---
title: Cruscotto
source_url: https://docs.openclaw.ai/it/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Apri la UI di controllo usando la tua autenticazione corrente.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Note:

  * `dashboard` risolve le SecretRef configurate in `gateway.auth.token` quando possibile.
  * `dashboard` segue `gateway.tls.enabled`: i Gateway con TLS abilitato stampano/aprono gli URL `https://` della UI di controllo e si connettono tramite `wss://`.
  * Se la consegna tramite appunti/browser non riesce per un URL della dashboard autenticato con token, `dashboard` registra un suggerimento sicuro per l'autenticazione manuale che nomina `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` e la chiave di frammento `token` senza stampare il valore del token.
  * Per i token gestiti da SecretRef (risolti o non risolti), `dashboard` stampa/copia/apre un URL senza token per evitare di esporre segreti esterni nell'output del terminale, nella cronologia degli appunti o negli argomenti di avvio del browser.
  * Se `gateway.auth.token` è gestito da SecretRef ma non viene risolto in questo percorso di comando, il comando stampa un URL senza token e indicazioni esplicite per la risoluzione invece di incorporare un segnaposto di token non valido.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Dashboard](</it/web/dashboard>)


Was this useful?YesNo