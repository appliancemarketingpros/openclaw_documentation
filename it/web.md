---
title: Web
source_url: https://docs.openclaw.ai/it/web
scraped_at: 2026-05-25
---

Il Gateway serve una piccola **UI di controllo nel browser** (Vite + Lit) dalla stessa porta del WebSocket del Gateway:

  * predefinito: `http://<host>:18789/`
  * con `gateway.tls.enabled: true`: `https://<host>:18789/`
  * prefisso facoltativo: imposta `gateway.controlUi.basePath` (ad es. `/openclaw`)


Le funzionalità sono in [UI di controllo](</it/web/control-ui>). Il resto di questa pagina si concentra sulle modalità di bind, sulla sicurezza e sulle superfici esposte al web.

## Webhook

Quando `hooks.enabled=true`, il Gateway espone anche un piccolo endpoint Webhook sullo stesso server HTTP. Vedi [configurazione del Gateway](</it/gateway/configuration>) → `hooks` per autenticazione + payload.

## Configurazione (attiva per impostazione predefinita)

La UI di controllo è **abilitata per impostazione predefinita** quando gli asset sono presenti (`dist/control-ui`). Puoi controllarla tramite configurazione:

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath optional  },}
[/code]

## Accesso Tailscale

### Serve integrato (consigliato)

Mantieni il Gateway su loopback e lascia che Tailscale Serve lo esponga tramite proxy:

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

Poi avvia il gateway:

bashCopy code
[code]
    openclaw gateway
[/code]

Apri:

  * `https://<magicdns>/` (o il tuo `gateway.controlUi.basePath` configurato)


### Bind Tailnet + token

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

Poi avvia il gateway (questo esempio non loopback usa l'autenticazione con token segreto condiviso):

bashCopy code
[code]
    openclaw gateway
[/code]

Apri:

  * `http://<tailscale-ip>:18789/` (o il tuo `gateway.controlUi.basePath` configurato)


### Internet pubblico (Funnel)

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // or OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## Note di sicurezza

  * L'autenticazione del Gateway è richiesta per impostazione predefinita (token, password, trusted-proxy o intestazioni di identità di Tailscale Serve quando abilitate).
  * I bind non loopback **richiedono** comunque l'autenticazione del gateway. In pratica, questo significa autenticazione con token/password oppure un reverse proxy consapevole dell'identità con `gateway.auth.mode: "trusted-proxy"`.
  * La procedura guidata crea l'autenticazione con segreto condiviso per impostazione predefinita e di solito genera un token gateway (anche su loopback).
  * In modalità con segreto condiviso, la UI invia `connect.params.auth.token` o `connect.params.auth.password`.
  * Quando `gateway.tls.enabled: true`, la dashboard locale e gli helper di stato mostrano URL della dashboard `https://` e URL WebSocket `wss://`.
  * Nelle modalità con identità, come Tailscale Serve o `trusted-proxy`, il controllo di autenticazione WebSocket viene invece soddisfatto dalle intestazioni della richiesta.
  * Per distribuzioni della UI di controllo non loopback, imposta esplicitamente `gateway.controlUi.allowedOrigins` (origini complete). Senza questa impostazione, l'avvio del gateway viene rifiutato per impostazione predefinita.
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` abilita la modalità di fallback dell'origine basata sull'intestazione Host, ma è una pericolosa riduzione della sicurezza.
  * Con Serve, le intestazioni di identità Tailscale possono soddisfare l'autenticazione della UI di controllo/WebSocket quando `gateway.auth.allowTailscale` è `true` (nessun token/password richiesto). Gli endpoint API HTTP non usano quelle intestazioni di identità Tailscale; seguono invece la normale modalità di autenticazione HTTP del gateway. Imposta `gateway.auth.allowTailscale: false` per richiedere credenziali esplicite. Vedi [Tailscale](</it/gateway/tailscale>) e [Sicurezza](</it/gateway/security>). Questo flusso senza token presuppone che l'host del gateway sia attendibile.
  * `gateway.tailscale.mode: "funnel"` richiede `gateway.auth.mode: "password"` (password condivisa).


## Compilazione della UI

Il Gateway serve file statici da `dist/control-ui`. Compilali con:

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo