---
title: Configurazione iniziale (app macOS)
source_url: https://docs.openclaw.ai/it/start/onboarding
scraped_at: 2026-05-25
---

Questo documento descrive il flusso di configurazione iniziale **attuale**. L'obiettivo è un'esperienza fluida del "giorno 0": scegliere dove viene eseguito il Gateway, collegare l'autenticazione, eseguire la procedura guidata e lasciare che l'agente inizializzi se stesso. Per una panoramica generale dei percorsi di onboarding, consulta [Panoramica dell'onboarding](</it/start/onboarding-overview>).

* ### Approva l'avviso macOS

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Approva la ricerca delle reti locali

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Benvenuto e avviso di sicurezza

Leggi l'avviso di sicurezza visualizzato e decidi di conseguenza ![](/assets/macos-onboarding/03-security-notice.png)

Modello di fiducia per la sicurezza:

  * Per impostazione predefinita, OpenClaw è un agente personale: un unico perimetro di operatore attendibile.
  * Le configurazioni condivise/multiutente richiedono un irrigidimento (separa i perimetri di fiducia, mantieni l'accesso agli strumenti al minimo e segui [Sicurezza](</it/gateway/security>)).
  * L'onboarding locale ora imposta per impostazione predefinita le nuove configurazioni su `tools.profile: "coding"`, così le nuove configurazioni locali mantengono gli strumenti di filesystem/runtime senza imporre il profilo `full` senza restrizioni.
  * Se sono abilitati hook/webhook o altri feed di contenuti non attendibili, usa un livello di modello moderno e robusto e mantieni criteri degli strumenti/sandboxing rigorosi.


* ### Locale vs remoto

![](/assets/macos-onboarding/04-choose-gateway.png)

Dove viene eseguito il **Gateway**?

  * **Questo Mac (solo locale):** l'onboarding può configurare l'autenticazione e scrivere le credenziali localmente.
  * **Remoto (tramite SSH/Tailnet):** l'onboarding **non** configura l'autenticazione locale; le credenziali devono esistere sull'host del Gateway.
  * **Configura più tardi:** salta la configurazione e lascia l'app non configurata.


* ### Autorizzazioni

Scegli quali autorizzazioni vuoi concedere a OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

L'onboarding richiede le autorizzazioni TCC necessarie per:

  * Automazione (AppleScript)
  * Notifiche
  * Accessibilità
  * Registrazione dello schermo
  * Microfono
  * Riconoscimento vocale
  * Fotocamera
  * Posizione


* ### CLI

* ### Chat di onboarding (sessione dedicata)

Dopo la configurazione, l'app apre una sessione di chat di onboarding dedicata, così l'agente può presentarsi e guidare i passaggi successivi. Questo mantiene la guida al primo avvio separata dalla tua conversazione normale. Consulta [Bootstrapping](</it/start/bootstrapping>) per vedere cosa accade sull'host del Gateway durante la prima esecuzione dell'agente.

## Correlati

  * [Panoramica dell'onboarding](</it/start/onboarding-overview>)
  * [Guida introduttiva](</it/start/getting-started>)


Was this useful?YesNo