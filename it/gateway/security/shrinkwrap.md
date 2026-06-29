---
title: npm shrinkwrap
source_url: https://docs.openclaw.ai/it/gateway/security/shrinkwrap
scraped_at: 2026-06-29
---

Gateway & OpsGateway

I checkout sorgente di OpenClaw usano `pnpm-lock.yaml`. I pacchetti npm pubblicati di OpenClaw usano `npm-shrinkwrap.json`, il lockfile delle dipendenze pubblicabile di npm, quindi le installazioni dei pacchetti usano il grafo delle dipendenze revisionato durante il rilascio.

## La versione semplice

Shrinkwrap è una ricevuta per l'albero delle dipendenze distribuito con un pacchetto npm. Indica a npm quali versioni esatte dei pacchetti transitivi installare.

Per i rilasci di OpenClaw, questo significa che:

  * il pacchetto pubblicato non chiede a npm di inventare un nuovo grafo delle dipendenze al momento dell'installazione;
  * le modifiche alle dipendenze diventano più facili da revisionare perché compaiono in un lockfile;
  * la validazione del rilascio può testare lo stesso grafo che gli utenti installeranno;
  * le sorprese legate alla dimensione del pacchetto o alle dipendenze native sono più facili da individuare prima della pubblicazione.


Shrinkwrap non è una sandbox. Non rende una dipendenza sicura di per sé e non sostituisce l'isolamento dell'host, `openclaw security audit`, la provenienza dei pacchetti o gli smoke test di installazione.

Il modello mentale breve:

File | Dove conta | Cosa significa  
---|---|---  
`pnpm-lock.yaml` | checkout sorgente OpenClaw | Grafo delle dipendenze dei maintainer  
`npm-shrinkwrap.json` | Pacchetto npm pubblicato | Grafo di installazione npm per gli utenti  
`package-lock.json` | App npm locali | Non è il contratto di pubblicazione di OpenClaw  
  
## Perché OpenClaw lo usa

OpenClaw è un Gateway, host di Plugin, router di modelli e runtime di agenti. Un'installazione predefinita può influire sul tempo di avvio, sull'uso del disco, sui download di pacchetti nativi e sull'esposizione alla supply chain.

Shrinkwrap offre alla revisione del rilascio un confine stabile:

  * i revisori possono vedere il movimento delle dipendenze transitive;
  * i validatori dei pacchetti possono rifiutare derive inattese del lockfile;
  * l'accettazione del pacchetto può testare le installazioni con il grafo che verrà distribuito;
  * i pacchetti Plugin possono portare il proprio grafo delle dipendenze bloccato invece di fare affidamento sul pacchetto root per possedere le dipendenze solo del Plugin.


L'obiettivo non è "più lockfile". L'obiettivo sono installazioni di rilascio riproducibili con proprietà chiara.

## Dettagli tecnici

Il pacchetto npm root `openclaw` e i pacchetti Plugin npm di proprietà OpenClaw includono `npm-shrinkwrap.json` quando vengono pubblicati. I pacchetti Plugin di proprietà OpenClaw idonei possono anche essere pubblicati con `bundledDependencies` esplicite, così i file delle dipendenze di runtime vengono trasportati nel tarball del Plugin invece di dipendere solo dalla risoluzione in fase di installazione.

Mantieni il confine così:

bashCopy code
[code]
    pnpm deps:shrinkwrap:generatepnpm deps:shrinkwrap:check
[/code]

Il generatore risolve il formato lock pubblicabile di npm ma rifiuta le versioni dei pacchetti generate che non sono già presenti in `pnpm-lock.yaml`. Questo mantiene intatti l'età delle dipendenze pnpm, gli override e il confine di revisione delle patch.

Usa i comandi solo root solo quando aggiorni intenzionalmente il pacchetto root senza toccare i pacchetti Plugin:

bashCopy code
[code]
    pnpm deps:shrinkwrap:root:generatepnpm deps:shrinkwrap:root:check
[/code]

Revisiona questi file come sensibili alla sicurezza:

  * `pnpm-lock.yaml`
  * `npm-shrinkwrap.json`
  * payload delle dipendenze dei Plugin in bundle
  * qualsiasi diff di `package-lock.json`


I validatori dei pacchetti OpenClaw richiedono shrinkwrap nei nuovi tarball del pacchetto root. Il percorso di pubblicazione npm del Plugin controlla lo shrinkwrap locale del Plugin, installa le dipendenze in bundle locali del pacchetto e poi esegue il pack o pubblica. I validatori dei pacchetti rifiutano `package-lock.json` per i pacchetti OpenClaw pubblicati.

Per ispezionare un pacchetto root pubblicato:

bashCopy code
[code]
    npm pack openclaw@<version> --json --pack-destination /tmp/openclaw-packtar -tf /tmp/openclaw-pack/openclaw-<version>.tgz | grep '^package/npm-shrinkwrap.json$'
[/code]

Per ispezionare un pacchetto Plugin di proprietà OpenClaw:

bashCopy code
[code]
    npm pack @openclaw/discord@<version> --json --pack-destination /tmp/openclaw-plugin-packtar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/npm-shrinkwrap.json$'tar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/node_modules/'
[/code]

Contesto: [npm-shrinkwrap.json](<https://docs.npmjs.com/cli/v11/configuring-npm/npm-shrinkwrap-json>).

Was this useful?YesNo

Open issue