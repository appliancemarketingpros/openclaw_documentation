---
title: Navigatore
source_url: https://docs.openclaw.ai/it/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Gestisci la superficie di controllo del browser di OpenClaw ed esegui azioni del browser (ciclo di vita, profili, schede, snapshot, screenshot, navigazione, input, emulazione dello stato e debug).

Correlati:

  * Strumento browser + API: [Strumento browser](</it/tools/browser>)


## Flag comuni

  * `--url <gatewayWsUrl>`: URL WebSocket del Gateway (predefinito dalla configurazione).
  * `--token <token>`: token del Gateway (se richiesto).
  * `--timeout <ms>`: timeout della richiesta (ms).
  * `--expect-final`: attende una risposta finale del Gateway.
  * `--browser-profile <name>`: sceglie un profilo del browser (predefinito dalla configurazione).
  * `--json`: output leggibile da macchina (dove supportato).


## Avvio rapido (locale)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Gli agenti possono eseguire lo stesso controllo di prontezza con `browser({ action: "doctor" })`.

## Risoluzione rapida dei problemi

Se `start` fallisce con `not reachable after start`, diagnostica prima la prontezza CDP. Se `start` e `tabs` riescono ma `open` o `navigate` fallisce, il piano di controllo del browser è integro e l'errore è di solito dovuto alla policy SSRF di navigazione.

Sequenza minima:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Indicazioni dettagliate: [Risoluzione dei problemi del browser](</it/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Ciclo di vita

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Note:

  * `doctor --deep` aggiunge una prova snapshot live. È utile quando la prontezza CDP di base è verde ma vuoi una prova che la scheda corrente possa essere ispezionata.
  * Per profili `attachOnly` e CDP remoti, `openclaw browser stop` chiude la sessione di controllo attiva e cancella gli override temporanei di emulazione anche quando OpenClaw non ha avviato direttamente il processo del browser.
  * Per i profili locali gestiti, `openclaw browser stop` arresta il processo del browser generato.
  * `openclaw browser start --headless` si applica solo a quella richiesta di avvio e solo quando OpenClaw avvia un browser locale gestito. Non riscrive `browser.headless` o la configurazione del profilo, ed è un no-op per un browser già in esecuzione.
  * Sugli host Linux senza `DISPLAY` o `WAYLAND_DISPLAY`, i profili locali gestiti vengono eseguiti automaticamente in modalità headless a meno che `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false` o `browser.profiles.<name>.headless=false` richieda esplicitamente un browser visibile.


## Se il comando manca

Se `openclaw browser` è un comando sconosciuto, controlla `plugins.allow` in `~/.openclaw/openclaw.json`.

Quando `plugins.allow` è presente, elenca esplicitamente il Plugin browser incluso a meno che la configurazione non abbia già un blocco radice `browser`:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Un blocco radice `browser` esplicito, per esempio `browser.enabled=true` o `browser.profiles.<name>`, attiva anche il Plugin browser incluso sotto una allowlist restrittiva dei Plugin.

Correlato: [Strumento browser](</it/tools/browser#missing-browser-command-or-tool>)

## Profili

I profili sono configurazioni denominate di instradamento del browser. In pratica:

  * `openclaw`: avvia o si collega a un'istanza Chrome dedicata gestita da OpenClaw (directory dati utente isolata).
  * `user`: controlla la tua sessione Chrome esistente con accesso già effettuato tramite Chrome DevTools MCP.
  * profili CDP personalizzati: puntano a un endpoint CDP locale o remoto.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Usa un profilo specifico:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Schede

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` restituisce prima `suggestedTargetId`, poi il `tabId` stabile come `t1`, l'etichetta opzionale e il `targetId` grezzo. Gli agenti devono passare `suggestedTargetId` di nuovo a `focus`, `close`, snapshot e azioni. Puoi assegnare un'etichetta con `open --label`, `tab new --label` o `tab label`; etichette, ID scheda, ID target grezzi e prefissi univoci degli ID target sono tutti accettati. Quando Chromium sostituisce il target grezzo sottostante durante una navigazione o l'invio di un modulo, OpenClaw mantiene il `tabId`/l'etichetta stabile collegati alla scheda sostitutiva quando può dimostrare la corrispondenza. Gli ID target grezzi restano volatili; preferisci `suggestedTargetId`.

## Snapshot / screenshot / azioni

Snapshot:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Screenshot:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Note:

  * `--full-page` è solo per acquisizioni di pagina; non può essere combinato con `--ref` o `--element`.
  * I profili `existing-session` / `user` supportano screenshot di pagina e screenshot `--ref` dall'output snapshot, ma non screenshot CSS `--element`.
  * `--labels` sovrappone i riferimenti snapshot correnti allo screenshot.
  * `snapshot --urls` aggiunge le destinazioni dei link rilevate agli snapshot AI così che gli agenti possano scegliere target di navigazione diretti invece di dedurli dal solo testo del link.


Naviga/fai clic/digita (automazione UI basata su ref):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Le risposte delle azioni restituiscono il `targetId` grezzo corrente dopo la sostituzione della pagina innescata dall'azione quando OpenClaw può dimostrare la scheda sostitutiva. Gli script devono comunque memorizzare e passare `suggestedTargetId`/etichette per workflow di lunga durata.

Helper per file e finestre di dialogo:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

I profili Chrome gestiti salvano i download ordinari attivati da clic nella directory dei download di OpenClaw (`/tmp/openclaw/downloads` per impostazione predefinita, o la radice temporanea configurata). Usa `waitfordownload` o `download` quando l'agente deve attendere un file specifico e restituirne il percorso; questi waiter espliciti possiedono il download successivo.

## Stato e archiviazione

Viewport + emulazione:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookie + archiviazione:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Debug

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Chrome esistente tramite MCP

Usa il profilo `user` integrato, oppure crea un tuo profilo `existing-session`:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Questo percorso è solo host. Per Docker, server headless, Browserless o altre configurazioni remote, usa invece un profilo CDP.

Limiti attuali di existing-session:

  * le azioni guidate da snapshot usano ref, non selettori CSS
  * `browser.actionTimeoutMs` imposta per impostazione predefinita le richieste `act` supportate a 60000 ms quando i chiamanti omettono `timeoutMs`; `timeoutMs` per chiamata ha comunque la precedenza.
  * `click` è solo clic sinistro
  * `type` non supporta `slowly=true`
  * `press` non supporta `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill` e `evaluate` rifiutano override di timeout per chiamata
  * `select` supporta un solo valore
  * `wait --load networkidle` non è supportato
  * i caricamenti di file richiedono `--ref` / `--input-ref`, non supportano CSS `--element` e attualmente supportano un file alla volta
  * gli hook delle finestre di dialogo non supportano `--timeout`
  * gli screenshot supportano acquisizioni di pagina e `--ref`, ma non CSS `--element`
  * `responsebody`, l'intercettazione dei download, l'esportazione PDF e le azioni batch richiedono ancora un browser gestito o un profilo CDP grezzo


## Controllo browser remoto (proxy host del node)

Se il Gateway viene eseguito su una macchina diversa dal browser, esegui un **host node** sulla macchina che ha Chrome/Brave/Edge/Chromium. Il Gateway inoltrerà le azioni del browser a quel node (non è richiesto un server di controllo browser separato).

Usa `gateway.nodes.browser.mode` per controllare l'instradamento automatico e `gateway.nodes.browser.node` per fissare un node specifico se ne sono connessi più di uno.

Sicurezza + configurazione remota: [Strumento browser](</it/tools/browser>), [Accesso remoto](</it/gateway/remote>), [Tailscale](</it/gateway/tailscale>), [Sicurezza](</it/gateway/security>)

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Browser](</it/tools/browser>)


Was this useful?YesNo