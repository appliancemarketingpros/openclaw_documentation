---
title: macOS-VM's
source_url: https://docs.openclaw.ai/nl/install/macos-vm
scraped_at: 2026-05-25
---

## Aanbevolen standaardoptie (meeste gebruikers)

  * **Kleine Linux-VPS** voor een altijd ingeschakelde Gateway tegen lage kosten. Zie [VPS-hosting](</nl/vps>).
  * **Toegewijde hardware** (Mac mini of Linux-machine) als je volledige controle wilt en een **residentieel IP-adres** voor browserautomatisering. Veel sites blokkeren datacenter-IP's, dus lokaal browsen werkt vaak beter.
  * **Hybride:** houd de Gateway op een goedkope VPS en verbind je Mac als een **node** wanneer je browser-/UI-automatisering nodig hebt. Zie [Nodes](</nl/nodes>) en [Gateway op afstand](</nl/gateway/remote>).


Gebruik een macOS-VM wanneer je specifiek macOS-only mogelijkheden nodig hebt, zoals iMessage, of strikte isolatie van je dagelijkse Mac wilt.

## macOS-VM-opties

### Lokale VM op je Apple Silicon-Mac (Lume)

Voer OpenClaw uit in een gesandboxte macOS-VM op je bestaande Apple Silicon-Mac met [Lume](<https://cua.ai/docs/lume>).

Dit geeft je:

  * Volledige macOS-omgeving in isolatie (je host blijft schoon)
  * iMessage-ondersteuning via `imsg` (het standaard lokale pad is onmogelijk op Linux/Windows)
  * Direct resetten door VM's te klonen
  * Geen extra hardware- of cloudkosten


### Gehoste Mac-aanbieders (cloud)

Als je macOS in de cloud wilt, werken gehoste Mac-aanbieders ook:

  * [MacStadium](<https://www.macstadium.com/>) (gehoste Macs)
  * Andere gehoste Mac-leveranciers werken ook; volg hun VM- en SSH-documentatie


Zodra je SSH-toegang tot een macOS-VM hebt, ga je verder met stap 6 hieronder.

* * *

## Snel pad (Lume, ervaren gebruikers)

  1. Installeer Lume
  2. `lume create openclaw --os macos --ipsw latest`
  3. Voltooi Setup Assistant, schakel Remote Login (SSH) in
  4. `lume run openclaw --no-display`
  5. Log in via SSH, installeer OpenClaw, configureer kanalen
  6. Klaar


* * *

## Wat je nodig hebt (Lume)

  * Apple Silicon-Mac (M1/M2/M3/M4)
  * macOS Sequoia of later op de host
  * ~60 GB vrije schijfruimte per VM
  * ~20 minuten


* * *

## 1) Installeer Lume

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

Als `~/.local/bin` niet in je PATH staat:

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

Controleer:

bashCopy code
[code]
    lume --version
[/code]

Docs: [Lume-installatie](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) Maak de macOS-VM

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

Dit downloadt macOS en maakt de VM. Er wordt automatisch een VNC-venster geopend.

* * *

## 3) Voltooi Setup Assistant

In het VNC-venster:

  1. Selecteer taal en regio
  2. Sla Apple ID over (of log in als je later iMessage wilt gebruiken)
  3. Maak een gebruikersaccount aan (onthoud de gebruikersnaam en het wachtwoord)
  4. Sla alle optionele functies over


Schakel SSH in nadat de setup is voltooid:

  1. Open Systeeminstellingen → Algemeen → Delen
  2. Schakel "Remote Login" in


* * *

## 4) Haal het IP-adres van de VM op

bashCopy code
[code]
    lume get openclaw
[/code]

Zoek het IP-adres (meestal `192.168.64.x`).

* * *

## 5) Log via SSH in op de VM

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

Vervang `youruser` door het account dat je hebt aangemaakt en het IP-adres door het IP-adres van je VM.

* * *

## 6) Installeer OpenClaw

Binnen de VM:

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Volg de onboarding-prompts om je modelprovider (Anthropic, OpenAI, enz.) in te stellen.

* * *

## 7) Configureer kanalen

Bewerk het configuratiebestand:

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

Voeg je kanalen toe:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

Log daarna in bij WhatsApp (scan QR):

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) Voer de VM headless uit

Stop de VM en start opnieuw zonder display:

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

De VM draait op de achtergrond. De daemon van OpenClaw houdt de Gateway actief.

Status controleren:

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## Bonus: iMessage-integratie

Dit is de belangrijkste functie van draaien op macOS. Gebruik [iMessage](</nl/channels/imessage>) met `imsg` om Berichten aan OpenClaw toe te voegen.

Binnen de VM:

  1. Log in bij Berichten.
  2. Installeer `imsg`.
  3. Verleen Volledige schijftoegang en Automatisering-toestemming voor het proces dat OpenClaw/`imsg` uitvoert.
  4. Controleer RPC-ondersteuning met `imsg rpc --help`.


Voeg dit toe aan je OpenClaw-configuratie:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

Herstart de Gateway. Nu kan je agent iMessages verzenden en ontvangen.

Volledige setupdetails: [iMessage-kanaal](</nl/channels/imessage>)

* * *

## Sla een gouden image op

Maak een snapshot van je schone staat voordat je verder aanpast:

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

Altijd resetten:

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## 24/7 draaien

Houd de VM actief door:

  * Je Mac aangesloten te houden op stroom
  * Sluimerstand uit te schakelen in Systeeminstellingen → Energiestand
  * `caffeinate` te gebruiken indien nodig


Voor echt altijd ingeschakeld gebruik kun je een toegewijde Mac mini of een kleine VPS overwegen. Zie [VPS-hosting](</nl/vps>).

* * *

## Probleemoplossing

Probleem | Oplossing  
---|---  
Kan niet via SSH inloggen op VM | Controleer of "Remote Login" is ingeschakeld in de Systeeminstellingen van de VM  
VM-IP wordt niet weergegeven | Wacht tot de VM volledig is opgestart en voer `lume get openclaw` opnieuw uit  
Lume-opdracht niet gevonden | Voeg `~/.local/bin` toe aan je PATH  
WhatsApp-QR scant niet | Zorg dat je bent ingelogd op de VM (niet de host) wanneer je `openclaw channels login` uitvoert  
  
* * *

## Gerelateerde docs

  * [VPS-hosting](</nl/vps>)
  * [Nodes](</nl/nodes>)
  * [Gateway op afstand](</nl/gateway/remote>)
  * [iMessage-kanaal](</nl/channels/imessage>)
  * [Lume-snelstart](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [Lume CLI-referentie](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [Onbeheerde VM-setup](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>) (geavanceerd)
  * [Docker-sandboxing](</nl/install/docker>) (alternatieve isolatieaanpak)


Was this useful?YesNo