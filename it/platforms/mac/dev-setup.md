---
title: Configurazione dell'ambiente di sviluppo su macOS
source_url: https://docs.openclaw.ai/it/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# Configurazione sviluppatore macOS

Compila ed esegui l'applicazione macOS di OpenClaw dal sorgente.

## Prerequisiti

Prima di compilare l'app, assicurati di avere installato quanto segue:

  1. **Xcode 26.2+** : richiesto per lo sviluppo Swift.
  2. **Node.js 24 e pnpm** : consigliati per Gateway, CLI e script di pacchettizzazione. Node 22 LTS, attualmente `22.16+`, resta supportato per compatibilità.


## 1\. Installa le dipendenze

Installa le dipendenze dell'intero progetto:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. Compila e pacchettizza l'app

Per compilare l'app macOS e pacchettizzarla in `dist/OpenClaw.app`, esegui:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Se non hai un certificato Apple Developer ID, lo script userà automaticamente la **firma ad-hoc** (`-`).

Per le modalità di esecuzione di sviluppo, i flag di firma e la risoluzione dei problemi relativi al Team ID, consulta il README dell'app macOS: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Nota** : le app firmate ad-hoc possono attivare avvisi di sicurezza. Se l'app va in crash immediatamente con "Abort trap 6", consulta la sezione Risoluzione dei problemi.

## 3\. Installa la CLI

L'app macOS richiede un'installazione globale della CLI `openclaw` per gestire le attività in background.

**Per installarla (consigliato):**

  1. Apri l'app OpenClaw.
  2. Vai alla scheda delle impostazioni **Generale**.
  3. Fai clic su **"Installa CLI"**.


In alternativa, installala manualmente:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

Anche `pnpm add -g openclaw@<version>` e `bun add -g openclaw@<version>` funzionano. Per il runtime Gateway, Node resta il percorso consigliato.

## Risoluzione dei problemi

### Compilazione non riuscita: toolchain o SDK non corrispondente

La compilazione dell'app macOS richiede l'SDK macOS più recente e la toolchain Swift 6.2.

**Dipendenze di sistema (richieste):**

  * **Ultima versione di macOS disponibile in Aggiornamento Software** (richiesta dagli SDK di Xcode 26.2)
  * **Xcode 26.2** (toolchain Swift 6.2)


**Controlli:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

Se le versioni non corrispondono, aggiorna macOS/Xcode ed esegui di nuovo la compilazione.

### L'app va in crash durante la concessione dei permessi

Se l'app va in crash quando provi a consentire l'accesso a **Riconoscimento vocale** o **Microfono** , la causa potrebbe essere una cache TCC danneggiata o una mancata corrispondenza della firma.

**Correzione:**

  1. Reimposta i permessi TCC:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. Se non funziona, modifica temporaneamente il `BUNDLE_ID` in [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) per forzare macOS a ripartire da una "situazione pulita".


### Gateway "Avvio..." indefinitamente

Se lo stato del Gateway resta su "Avvio...", controlla se un processo zombie sta occupando la porta:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # Se non stai usando un LaunchAgent (modalità dev / esecuzioni manuali), trova il listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

Se un'esecuzione manuale sta occupando la porta, arresta quel processo (Ctrl+C). Come ultima risorsa, termina il PID trovato sopra.

## Correlati

  * [App macOS](</it/platforms/macos>)
  * [Panoramica dell'installazione](</it/install>)


Was this useful?YesNo