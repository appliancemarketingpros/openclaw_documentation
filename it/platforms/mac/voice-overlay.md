---
title: Sovrapposizione vocale
source_url: https://docs.openclaw.ai/it/platforms/mac/voice-overlay
scraped_at: 2026-05-25
---

# Ciclo di vita della sovrapposizione vocale (macOS)

Destinatari: contributori dell’app macOS. Obiettivo: mantenere prevedibile la sovrapposizione vocale quando parola di attivazione e premi-per-parlare si sovrappongono.

## Intento attuale

  * Se la sovrapposizione è già visibile per la parola di attivazione e l’utente preme il tasto di scelta rapida, la sessione del tasto di scelta rapida _adotta_ il testo esistente invece di reimpostarlo. La sovrapposizione resta visibile mentre il tasto di scelta rapida è tenuto premuto. Quando l’utente rilascia: invia se c’è testo ripulito dagli spazi, altrimenti chiude.
  * La sola parola di attivazione continua a inviare automaticamente al silenzio; premi-per-parlare invia subito al rilascio.


## Implementato (9 dicembre 2025)

  * Le sessioni di sovrapposizione ora trasportano un token per ogni acquisizione (parola di attivazione o premi-per-parlare). Gli aggiornamenti parziali/finali/di invio/chiusura/livello vengono scartati quando il token non corrisponde, evitando callback obsolete.
  * Premi-per-parlare adotta qualsiasi testo visibile nella sovrapposizione come prefisso (quindi premere il tasto di scelta rapida mentre la sovrapposizione di attivazione è visibile mantiene il testo e aggiunge il nuovo parlato). Attende fino a 1,5 s una trascrizione finale prima di ripiegare sul testo corrente.
  * I log di segnale acustico/sovrapposizione sono emessi a livello `info` nelle categorie `voicewake.overlay`, `voicewake.ptt` e `voicewake.chime` (avvio sessione, parziale, finale, invio, chiusura, motivo del segnale acustico).


## Passaggi successivi

  1. **VoiceSessionCoordinator (actor)**
     * Possiede esattamente una `VoiceSession` alla volta.
     * API (basata su token): `beginWakeCapture`, `beginPushToTalk`, `updatePartial`, `endCapture`, `cancel`, `applyCooldown`.
     * Scarta le callback che trasportano token obsoleti (impedisce ai vecchi riconoscitori di riaprire la sovrapposizione).
  2. **VoiceSession (modello)**
     * Campi: `token`, `source` (wakeWord|pushToTalk), testo confermato/volatile, flag dei segnali acustici, timer (invio automatico, inattività), `overlayMode` (display|editing|sending), scadenza del cooldown.
  3. **Associazione della sovrapposizione**
     * `VoiceSessionPublisher` (`ObservableObject`) rispecchia la sessione attiva in SwiftUI.
     * `VoiceWakeOverlayView` renderizza solo tramite il publisher; non modifica mai direttamente singleton globali.
     * Le azioni utente della sovrapposizione (`sendNow`, `dismiss`, `edit`) richiamano il coordinator con il token della sessione.
  4. **Percorso di invio unificato**
     * Su `endCapture`: se il testo ripulito dagli spazi è vuoto → chiude; altrimenti `performSend(session:)` (riproduce il segnale acustico di invio una sola volta, inoltra, chiude).
     * Premi-per-parlare: nessun ritardo; parola di attivazione: ritardo opzionale per l’invio automatico.
     * Applica un breve cooldown al runtime di attivazione dopo la fine di premi-per-parlare, così la parola di attivazione non si riattiva immediatamente.
  5. **Logging**
     * Il coordinator emette log `.info` nel sottosistema `ai.openclaw`, categorie `voicewake.overlay` e `voicewake.chime`.
     * Eventi chiave: `session_started`, `adopted_by_push_to_talk`, `partial`, `finalized`, `send`, `dismiss`, `cancel`, `cooldown`.


## Checklist di debug

  * Trasmetti i log in streaming mentre riproduci una sovrapposizione bloccata:

bashCopy code
[code]sudo log stream --predicate 'subsystem == "ai.openclaw" AND category CONTAINS "voicewake"' --level info --style compact
[/code]

  * Verifica che ci sia un solo token di sessione attivo; le callback obsolete dovrebbero essere scartate dal coordinator.

  * Assicurati che il rilascio di premi-per-parlare chiami sempre `endCapture` con il token attivo; se il testo è vuoto, aspettati `dismiss` senza segnale acustico né invio.


## Passaggi di migrazione (suggeriti)

  1. Aggiungi `VoiceSessionCoordinator`, `VoiceSession` e `VoiceSessionPublisher`.
  2. Rifattorizza `VoiceWakeRuntime` per creare/aggiornare/terminare sessioni invece di toccare direttamente `VoiceWakeOverlayController`.
  3. Rifattorizza `VoicePushToTalk` per adottare sessioni esistenti e chiamare `endCapture` al rilascio; applica il cooldown del runtime.
  4. Collega `VoiceWakeOverlayController` al publisher; rimuovi le chiamate dirette da runtime/PTT.
  5. Aggiungi test di integrazione per adozione della sessione, cooldown e chiusura con testo vuoto.


## Correlati

  * [app macOS](</it/platforms/macos>)
  * [Attivazione vocale (macOS)](</it/platforms/mac/voicewake>)
  * [Modalità conversazione](</it/nodes/talk>)


Was this useful?YesNo