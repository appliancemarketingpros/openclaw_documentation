---
title: Accesso tramite browser
source_url: https://docs.openclaw.ai/it/tools/browser-login
scraped_at: 2026-05-25
---

## Accesso manuale (consigliato)

Quando un sito richiede l'accesso, **accedi manualmente** nel profilo del browser **host** (il browser openclaw).

**Non** fornire al modello le tue credenziali. Gli accessi automatizzati spesso attivano le difese anti-bot e possono bloccare l'account.

Torna alla documentazione principale del browser: [Browser](</it/tools/browser>).

## Quale profilo Chrome viene usato?

OpenClaw controlla un **profilo Chrome dedicato** (chiamato `openclaw`, con interfaccia a tonalità arancione). Questo è separato dal tuo profilo browser quotidiano.

Per le chiamate allo strumento browser dell'agente:

  * Scelta predefinita: l'agente dovrebbe usare il proprio browser `openclaw` isolato.
  * Usa `profile="user"` solo quando le sessioni con accesso esistenti sono rilevanti e l'utente è al computer per fare clic/approvare eventuali prompt di collegamento.
  * Se hai più profili del browser utente, specifica esplicitamente il profilo invece di tirare a indovinare.


Due modi semplici per accedervi:

  1. **Chiedi all'agente di aprire il browser** e poi accedi tu.
  2. **Aprilo tramite CLI** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Se hai più profili, passa `--browser-profile <name>` (il valore predefinito è `openclaw`).

## X/Twitter: flusso consigliato

  * **Lettura/ricerca/thread:** usa il browser **host** (accesso manuale).
  * **Pubblicazione aggiornamenti:** usa il browser **host** (accesso manuale).


## Sandboxing + accesso al browser host

Le sessioni browser in sandbox hanno **maggiori probabilità** di attivare il rilevamento dei bot. Per X/Twitter (e altri siti rigorosi), preferisci il browser **host**.

Se l'agente è in sandbox, lo strumento browser usa per impostazione predefinita la sandbox. Per consentire il controllo dell'host:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Poi apri tu il browser host (le invocazioni CLI vengono sempre eseguite rispetto al browser host):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

Le chiamate allo strumento `browser` dell'agente possono quindi puntare all'host una volta impostato `sandbox.browser.allowHostControl: true`. In alternativa, disabilita il sandboxing per l'agente che pubblica aggiornamenti.

## Correlati

  * [Browser](</it/tools/browser>)
  * [Risoluzione dei problemi del browser su Linux](</it/tools/browser-linux-troubleshooting>)
  * [Risoluzione dei problemi del browser WSL2](</it/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo