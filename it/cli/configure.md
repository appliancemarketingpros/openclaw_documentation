---
title: Configura
source_url: https://docs.openclaw.ai/it/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

Prompt interattivo per modifiche mirate a una configurazione esistente: credenziali, dispositivi, impostazioni predefinite degli agenti, Gateway, canali, plugin, Skills e controlli di integrità.

Usa `openclaw onboard` per il percorso completo guidato di primo avvio, `openclaw setup` solo per la configurazione/area di lavoro di base e `openclaw channels add` quando ti serve soltanto configurare l'account del canale.

Quando configure viene avviato da una scelta di autenticazione del provider, i selettori del modello predefinito e della allowlist preferiscono automaticamente quel provider. Per provider accoppiati come Volcengine e BytePlus, la stessa preferenza corrisponde anche alle loro varianti di piano di codifica (`volcengine-plan/*`, `byteplus-plan/*`). Se il filtro del provider preferito producesse un elenco vuoto, configure ripiega sul catalogo non filtrato invece di mostrare un selettore vuoto.

Per la ricerca web, `openclaw configure --section web` ti consente di scegliere un provider e configurarne le credenziali. Alcuni provider mostrano anche prompt successivi specifici del provider:

  * **Grok** può offrire la configurazione facoltativa di `x_search` con la stessa `XAI_API_KEY` e consentirti di scegliere un modello `x_search`.
  * **Kimi** può chiedere l'area dell'API Moonshot (`api.moonshot.ai` rispetto a `api.moonshot.cn`) e il modello di ricerca web Kimi predefinito.


Correlati:

  * Riferimento di configurazione del Gateway: [Configuration](</it/gateway/configuration>)
  * CLI di configurazione: [Config](</it/cli/config>)


## Opzioni

  * `--section <section>`: filtro di sezione ripetibile


Sezioni disponibili:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


Note:

  * La scelta di dove viene eseguito il Gateway aggiorna sempre `gateway.mode`. Puoi selezionare "Continua" senza altre sezioni se è tutto ciò che ti serve.
  * Dopo le scritture della configurazione locale, configure installa i plugin scaricabili selezionati quando il percorso di configurazione scelto li richiede. La configurazione del Gateway remoto non installa pacchetti plugin locali.
  * I servizi orientati ai canali (Slack/Discord/Matrix/Microsoft Teams) richiedono allowlist di canali/stanze durante la configurazione. Puoi inserire nomi o ID; la procedura guidata risolve i nomi in ID quando possibile.
  * Se esegui il passaggio di installazione del daemon, l'autenticazione con token richiede un token e `gateway.auth.token` è gestito da SecretRef, configure convalida il SecretRef ma non persiste i valori del token in chiaro risolti nei metadati dell'ambiente del servizio supervisor.
  * Se l'autenticazione con token richiede un token e il SecretRef del token configurato non è risolto, configure blocca l'installazione del daemon con indicazioni di correzione utilizzabili.
  * Se sia `gateway.auth.token` sia `gateway.auth.password` sono configurati e `gateway.auth.mode` non è impostato, configure blocca l'installazione del daemon finché la modalità non viene impostata esplicitamente.


## Esempi

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Configuration](</it/gateway/configuration>)


Was this useful?YesNo