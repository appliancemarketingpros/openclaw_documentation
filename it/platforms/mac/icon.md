---
title: Icona della barra dei menu
source_url: https://docs.openclaw.ai/it/platforms/mac/icon
scraped_at: 2026-05-25
---

# Stati dell'icona della barra dei menu

Autore: steipete · Aggiornato: 2025-12-06 · Ambito: app macOS (`apps/macos`)

  * **Inattivo:** Animazione normale dell'icona (lampeggio, oscillazione occasionale).
  * **In pausa:** L'elemento di stato usa `appearsDisabled`; nessun movimento.
  * **Attivatore vocale (orecchie grandi):** Il rilevatore di attivazione vocale chiama `AppState.triggerVoiceEars(ttl: nil)` quando viene rilevata la parola di attivazione, mantenendo `earBoostActive=true` mentre l'enunciato viene acquisito. Le orecchie si ingrandiscono (1,9x), ricevono fori auricolari circolari per la leggibilità, poi tornano indietro tramite `stopVoiceEars()` dopo 1 s di silenzio. Attivato solo dalla pipeline vocale in-app.
  * **In esecuzione (agent in esecuzione):** `AppState.isWorking=true` pilota un micro-movimento di "scatto di coda/zampe": oscillazione delle zampe più rapida e leggero offset mentre il lavoro è in corso. Attualmente viene attivato attorno alle esecuzioni dell'agent WebChat; aggiungi lo stesso toggle attorno ad altri task lunghi quando li colleghi.


Punti di collegamento

  * Attivazione vocale: la chiamata runtime/tester chiama `AppState.triggerVoiceEars(ttl: nil)` all'attivazione e `stopVoiceEars()` dopo 1 s di silenzio per corrispondere alla finestra di acquisizione.
  * Attività dell'agent: imposta `AppStateStore.shared.setWorking(true/false)` attorno agli intervalli di lavoro (già fatto nella chiamata agent WebChat). Mantieni gli intervalli brevi e reimposta nei blocchi `defer` per evitare animazioni bloccate.


Forme e dimensioni

  * Icona di base disegnata in `CritterIconRenderer.makeIcon(blink:legWiggle:earWiggle:earScale:earHoles:)`.
  * La scala delle orecchie predefinita è `1.0`; il potenziamento vocale imposta `earScale=1.9` e attiva `earHoles=true` senza modificare il frame complessivo (immagine template da 18×18 pt renderizzata in un backing store Retina da 36×36 px).
  * Lo scatto usa un'oscillazione delle zampe fino a ~1.0 con un piccolo tremolio orizzontale; è additivo rispetto a qualsiasi oscillazione inattiva esistente.


Note comportamentali

  * Nessun toggle esterno CLI/broker per orecchie/in esecuzione; mantienilo interno ai segnali propri dell'app per evitare oscillazioni accidentali.
  * Mantieni i TTL brevi (<10 s) così l'icona torna rapidamente allo stato di base se un job si blocca.


## Correlati

  * [Barra dei menu](</it/platforms/mac/menu-bar>)
  * [app macOS](</it/platforms/macos>)


Was this useful?YesNo