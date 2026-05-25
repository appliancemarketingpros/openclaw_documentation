---
title: Permessi macOS
source_url: https://docs.openclaw.ai/it/platforms/mac/permissions
scraped_at: 2026-05-25
---

Le concessioni dei permessi macOS sono fragili. TCC associa una concessione di permesso alla firma del codice dell'app, all'identificatore del bundle e al percorso su disco. Se uno di questi cambia, macOS tratta l'app come nuova e può eliminare o nascondere i prompt.

## Requisiti per permessi stabili

  * Stesso percorso: esegui l'app da una posizione fissa (per OpenClaw, `dist/OpenClaw.app`).
  * Stesso identificatore del bundle: cambiare il bundle ID crea una nuova identità di permesso.
  * App firmata: le build non firmate o firmate ad hoc non mantengono i permessi.
  * Firma coerente: usa un vero certificato Apple Development o Developer ID in modo che la firma resti stabile tra una build e l'altra.


Le firme ad hoc generano una nuova identità a ogni build. macOS dimenticherà le concessioni precedenti, e i prompt possono scomparire del tutto finché le voci obsolete non vengono eliminate.

## Checklist di recupero quando i prompt scompaiono

  1. Chiudi l'app.
  2. Rimuovi la voce dell'app in Impostazioni di Sistema -> Privacy e Sicurezza.
  3. Riavvia l'app dallo stesso percorso e concedi di nuovo i permessi.
  4. Se il prompt continua a non apparire, reimposta le voci TCC con `tccutil` e riprova.
  5. Alcuni permessi riappaiono solo dopo un riavvio completo di macOS.


Esempi di reset (sostituisci il bundle ID secondo necessità):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## Permessi per file e cartelle (Desktop/Documents/Downloads)

macOS può anche limitare Desktop, Documents e Downloads per processi terminal/background. Se le letture dei file o gli elenchi delle directory restano bloccati, concedi l'accesso allo stesso contesto di processo che esegue le operazioni sui file (ad esempio Terminal/iTerm, app avviata da LaunchAgent o processo SSH).

Soluzione alternativa: sposta i file nel workspace OpenClaw (`~/.openclaw/workspace`) se vuoi evitare concessioni per singola cartella.

Se stai testando i permessi, firma sempre con un certificato reale. Le build ad hoc sono accettabili solo per esecuzioni locali rapide in cui i permessi non contano.

## Correlati

  * [App macOS](</it/platforms/macos>)
  * [Firma macOS](</it/platforms/mac/signing>)


Was this useful?YesNo