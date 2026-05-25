---
title: iMessage
source_url: https://docs.openclaw.ai/nl/channels/imessage
scraped_at: 2026-05-25
---

Status: native integratie met externe CLI. Gateway start `imsg rpc` en communiceert via JSON-RPC op stdio (geen aparte daemon/poort). Geavanceerde acties vereisen `imsg launch` en een geslaagde private API-probe.

**Private API-acties** Antwoorden, tapbacks, effecten, bijlagen en groepsbeheer. [**Koppelen** iMessage-DM's gebruiken standaard de koppelmodus. ](</nl/channels/pairing>) **Externe Mac** Gebruik een SSH-wrapper wanneer de Gateway niet op de Messages-Mac draait. [**Configuratiereferentie** Volledige iMessage-veldreferentie. ](</nl/gateway/config-channels#imessage>)

## Snelle installatie

### Lokale Mac (snelste pad)

* ### Installeer en verifieer imsg

bashCopy code
[code]
    brew install steipete/tap/imsgimsg rpc --helpimsg launchopenclaw channels status --probe
[/code]

* ### Configureer OpenClaw

json5Copy code
[code]
    {channels: {imessage: {enabled: true,cliPath: "/usr/local/bin/imsg",dbPath: "/Users/user/Library/Messages/chat.db",},},}
[/code]

* ### Start Gateway

bashCopy code
[code]
    openclaw gateway
[/code]

* ### Keur eerste DM-koppeling goed (standaard dmPolicy)

bashCopy code
[code]
    openclaw pairing list imessageopenclaw pairing approve imessage &lt;CODE&gt;
[/code]

Koppelverzoeken verlopen na 1 uur.

### Externe Mac via SSH

OpenClaw vereist alleen een stdio-compatibele `cliPath`, dus je kunt `cliPath` naar een wrapperscript laten wijzen dat via SSH verbinding maakt met een externe Mac en `imsg` uitvoert.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T gateway-host imsg "$@"
[/code]

Aanbevolen configuratie wanneer bijlagen zijn ingeschakeld:

json5Copy code
[code]
    {channels: {imessage: {  enabled: true,  cliPath: "~/.openclaw/scripts/imsg-ssh",  remoteHost: "user@gateway-host", // used for SCP attachment fetches  includeAttachments: true,  // Optional: override allowed attachment roots.  // Defaults include /Users/*/Library/Messages/Attachments  attachmentRoots: ["/Users/*/Library/Messages/Attachments"],  remoteAttachmentRoots: ["/Users/*/Library/Messages/Attachments"],},},}
[/code]

Als `remoteHost` niet is ingesteld, probeert OpenClaw dit automatisch te detecteren door het SSH-wrapperscript te parseren. `remoteHost` moet `host` of `user@host` zijn (geen spaties of SSH-opties). OpenClaw gebruikt strikte host-key-controle voor SCP, dus de relay-hostsleutel moet al bestaan in `~/.ssh/known_hosts`. Bijlagepaden worden gevalideerd tegen toegestane roots (`attachmentRoots` / `remoteAttachmentRoots`).

## Vereisten en machtigingen (macOS)

  * Messages moet zijn aangemeld op de Mac waarop `imsg` draait.
  * Full Disk Access is vereist voor de procescontext waarin OpenClaw/`imsg` draait (toegang tot de Messages-database).
  * Automatiseringsmachtiging is vereist om berichten via Messages.app te verzenden.
  * Voor geavanceerde acties (reageren / bewerken / verzenden ongedaan maken / antwoord in thread / effecten / groepsbewerkingen) moet System Integrity Protection zijn uitgeschakeld — zie De imsg private API inschakelen hieronder. Basis verzenden/ontvangen van tekst en media werkt zonder.


## De imsg private API inschakelen

`imsg` wordt geleverd in twee operationele modi:

  * **Basismodus** (standaard, geen SIP-wijzigingen nodig): uitgaande tekst en media via `send`, inkomende watch/geschiedenis, chatlijst. Dit krijg je direct na een nieuwe `brew install steipete/tap/imsg` plus de standaard macOS-machtigingen hierboven.
  * **Private API-modus** : `imsg` injecteert een helper-dylib in `Messages.app` om interne `IMCore`-functies aan te roepen. Hiermee worden `react`, `edit`, `unsend`, `reply` (threaded), `sendWithEffect`, `renameGroup`, `setGroupIcon`, `addParticipant`, `removeParticipant`, `leaveGroup`, plus typindicatoren en leesbevestigingen ontgrendeld.


Om het geavanceerde actieoppervlak te bereiken dat deze kanaalpagina documenteert, heb je Private API-modus nodig. De `imsg` README is expliciet over de vereiste:

> Geavanceerde functies zoals `read`, `typing`, `launch`, bridge-backed rich send, berichtmutatie en chatbeheer zijn opt-in. Ze vereisen dat SIP is uitgeschakeld en dat een helper-dylib in `Messages.app` wordt geïnjecteerd. `imsg launch` weigert te injecteren wanneer SIP is ingeschakeld.

De helper-injectietechniek gebruikt `imsg`'s eigen dylib om private API's van Messages te bereiken. Er is geen server van derden of BlueBubbles-runtime in het OpenClaw iMessage-pad.

### Installatie

  1. **Installeer (of upgrade)`imsg`** op de Mac waarop Messages.app draait:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg status --json
[/code]

De uitvoer van `imsg status --json` rapporteert `bridge_version`, `rpc_methods` en per methode `selectors`, zodat je kunt zien wat de huidige build ondersteunt voordat je begint.

  2. **Schakel System Integrity Protection uit.** Dit is macOS-versiespecifiek omdat de onderliggende Apple-vereiste afhangt van het OS en de hardware:

     * **macOS 10.13–10.15 (Sierra–Catalina):** schakel Library Validation uit via Terminal, herstart naar Recovery Mode, voer `csrutil disable` uit, herstart.
     * **macOS 11+ (Big Sur en later), Intel:** Recovery Mode (of Internet Recovery), `csrutil disable`, herstart.
     * **macOS 11+, Apple Silicon:** opstartprocedure met de aan/uit-knop om Recovery te openen; houd op recente macOS-versies de **linker Shift** -toets ingedrukt wanneer je op Continue klikt, daarna `csrutil disable`. Virtual-machine-installaties volgen een aparte flow — maak eerst een VM-snapshot.
     * **macOS 26 / Tahoe:** library-validation-beleid en private-entitlement-controles van `imagent` zijn verder aangescherpt; `imsg` heeft mogelijk een bijgewerkte build nodig om bij te blijven. Als `imsg launch`-injectie of specifieke `selectors` na een grote macOS-upgrade false beginnen terug te geven, controleer dan de release notes van `imsg` voordat je aanneemt dat de SIP-stap is geslaagd.

Volg Apple's Recovery-mode-flow voor je Mac om SIP uit te schakelen voordat je `imsg launch` uitvoert.

  3. **Injecteer de helper.** Met SIP uitgeschakeld en Messages.app aangemeld:

bashCopy code
[code]imsg launch
[/code]

`imsg launch` weigert te injecteren wanneer SIP nog is ingeschakeld, dus dit dient ook als bevestiging dat stap 2 is gelukt.

  4. **Verifieer de bridge vanuit OpenClaw:**

bashCopy code
[code]openclaw channels status --probe
[/code]

De iMessage-vermelding moet `works` rapporteren, en `imsg status --json | jq '.selectors'` moet `retractMessagePart: true` tonen plus de edit-/typing-/read-selectors die je macOS-build blootstelt. De per-method gating van de OpenClaw-plugin in `actions.ts` adverteert alleen acties waarvan de onderliggende selector `true` is, dus het actieoppervlak dat je in de toollijst van de agent ziet, weerspiegelt wat de bridge daadwerkelijk op deze host kan doen.


Als `openclaw channels status --probe` het kanaal als `works` rapporteert maar specifieke acties tijdens dispatch "iMessage `<action>` requires the imsg private API bridge" geven, voer `imsg launch` dan opnieuw uit — de helper kan wegvallen (Messages.app-herstart, OS-update, enz.) en de gecachte status `available: true` blijft acties adverteren totdat de volgende probe wordt vernieuwd.

### Wanneer je SIP niet kunt uitschakelen

Als uitgeschakelde SIP niet acceptabel is voor je dreigingsmodel:

  * `imsg` valt terug naar basismodus — alleen tekst + media + ontvangen.
  * De OpenClaw-plugin adverteert nog steeds tekst/media verzenden en inkomende monitoring; hij verbergt alleen `react`, `edit`, `unsend`, `reply`, `sendWithEffect` en groepsbewerkingen uit het actieoppervlak (volgens de per-method capability gate).
  * Je kunt een aparte niet-Apple-Silicon-Mac (of een dedicated bot-Mac) met SIP uit gebruiken voor de iMessage-workload, terwijl je SIP ingeschakeld houdt op je primaire apparaten. Zie Dedicated bot macOS-gebruiker (aparte iMessage-identiteit) hieronder.


## Toegangscontrole en routing

### DM-beleid

`channels.imessage.dmPolicy` beheert directe berichten:

  * `pairing` (standaard)
  * `allowlist`
  * `open` (vereist dat `allowFrom` `"*"` bevat)
  * `disabled`


Allowlist-veld: `channels.imessage.allowFrom`.

Allowlist-vermeldingen moeten afzenders identificeren: handles of statische afzendertoegangsgroepen (`accessGroup:<name>`). Gebruik `channels.imessage.groupAllowFrom` voor chatdoelen zoals `chat_id:*`, `chat_guid:*` of `chat_identifier:*`; gebruik `channels.imessage.groups` voor numerieke `chat_id`-registratiesleutels.

### Groepsbeleid + vermeldingen

`channels.imessage.groupPolicy` beheert groepsafhandeling:

  * `allowlist` (standaard wanneer geconfigureerd)
  * `open`
  * `disabled`


Allowlist voor groepsafzenders: `channels.imessage.groupAllowFrom`.

`groupAllowFrom`-vermeldingen kunnen ook verwijzen naar statische afzendertoegangsgroepen (`accessGroup:<name>`).

Runtime-fallback: als `groupAllowFrom` niet is ingesteld, gebruiken iMessage-controles voor groepsafzenders `allowFrom`; stel `groupAllowFrom` in wanneer DM- en groepstoelating moeten verschillen. Runtime-opmerking: als `channels.imessage` volledig ontbreekt, valt runtime terug naar `groupPolicy="allowlist"` en logt een waarschuwing (zelfs als `channels.defaults.groupPolicy` is ingesteld).

Vermeldingscontrole voor groepen:

  * iMessage heeft geen native vermeldingsmetadata
  * vermeldingsdetectie gebruikt regex-patronen (`agents.list[].groupChat.mentionPatterns`, fallback `messages.groupChat.mentionPatterns`)
  * zonder geconfigureerde patronen kan vermeldingscontrole niet worden afgedwongen


Besturingsopdrachten van geautoriseerde afzenders kunnen vermeldingscontrole in groepen omzeilen.

`systemPrompt` per groep:

Elke vermelding onder `channels.imessage.groups.*` accepteert een optionele `systemPrompt`-tekenreeks. De waarde wordt bij elke beurt die een bericht in die groep verwerkt in de systeemprompt van de agent geïnjecteerd. De resolutie weerspiegelt de promptresolutie per groep die door `channels.whatsapp.groups` wordt gebruikt:

  1. **Groepsspecifieke systeemprompt** (`groups["<chat_id>"].systemPrompt`): gebruikt wanneer de specifieke groepsvermelding in de map bestaat **en** de sleutel `systemPrompt` is gedefinieerd. Als `systemPrompt` een lege tekenreeks is (`""`), wordt de wildcard onderdrukt en wordt er geen systeemprompt op die groep toegepast.
  2. **Systeemprompt met groepswildcard** (`groups["*"].systemPrompt`): gebruikt wanneer de specifieke groepsvermelding volledig ontbreekt in de map, of wanneer deze bestaat maar geen sleutel `systemPrompt` definieert.

json5Copy code
[code]
    {  channels: {    imessage: {      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { systemPrompt: "Use British spelling." },        "8421": {          requireMention: true,          systemPrompt: "This is the on-call rotation chat. Keep replies under 3 sentences.",        },        "9907": {          // explicit suppression: the wildcard "Use British spelling." does not apply here          systemPrompt: "",        },      },    },  },}
[/code]

Prompts per groep gelden alleen voor groepsberichten — directe berichten in dit kanaal blijven onaangetast.

### Sessions and deterministic replies

  * DM's gebruiken directe routering; groepen gebruiken groepsroutering.
  * Met de standaardinstelling `session.dmScope=main` worden iMessage-DM's samengevoegd in de hoofdsessie van de agent.
  * Groepssessies zijn geïsoleerd (`agent:<agentId>:imessage:group:<chat_id>`).
  * Antwoorden worden terug naar iMessage gerouteerd met de metadata van het oorspronkelijke kanaal/doel.


Groepsachtig threadgedrag:

Sommige iMessage-threads met meerdere deelnemers kunnen binnenkomen met `is_group=false`. Als die `chat_id` expliciet is geconfigureerd onder `channels.imessage.groups`, behandelt OpenClaw deze als groepsverkeer (groepscontrole + isolatie van groepssessies).

## ACP-gespreksbindingen

Oude iMessage-chats kunnen ook aan ACP-sessies worden gebonden.

Snelle operatorflow:

  * Voer `/acp spawn codex --bind here` uit in de DM of toegestane groepschat.
  * Toekomstige berichten in datzelfde iMessage-gesprek worden naar de gespawnde ACP-sessie gerouteerd.
  * `/new` en `/reset` resetten dezelfde gebonden ACP-sessie op zijn plaats.
  * `/acp close` sluit de ACP-sessie en verwijdert de binding.


Geconfigureerde persistente bindingen worden ondersteund via top-level vermeldingen `bindings[]` met `type: "acp"` en `match.channel: "imessage"`.

`match.peer.id` kan gebruiken:

  * genormaliseerde DM-handle zoals `+15555550123` of `user@example.com`
  * `chat_id:<id>` (aanbevolen voor stabiele groepsbindingen)
  * `chat_guid:<guid>`
  * `chat_identifier:<identifier>`


Voorbeeld:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "codex",        runtime: {          type: "acp",          acp: { agent: "codex", backend: "acpx", mode: "persistent" },        },      },    ],  },  bindings: [    {      type: "acp",      agentId: "codex",      match: {        channel: "imessage",        accountId: "default",        peer: { kind: "group", id: "chat_id:123" },      },      acp: { label: "codex-group" },    },  ],}
[/code]

Zie [ACP-agenten](</nl/tools/acp-agents>) voor gedeeld gedrag van ACP-bindingen.

## Implementatiepatronen

Dedicated bot macOS user (separate iMessage identity)

Gebruik een speciale Apple ID en macOS-gebruiker zodat botverkeer is geïsoleerd van je persoonlijke Messages-profiel.

Typische flow:

  1. Maak een speciale macOS-gebruiker aan of log erop in.
  2. Log in bij Messages met de Apple ID van de bot in die gebruiker.
  3. Installeer `imsg` in die gebruiker.
  4. Maak een SSH-wrapper zodat OpenClaw `imsg` in de context van die gebruiker kan uitvoeren.
  5. Laat `channels.imessage.accounts.<id>.cliPath` en `.dbPath` naar dat gebruikersprofiel verwijzen.


De eerste uitvoering kan GUI-goedkeuringen vereisen (Automation + Full Disk Access) in die botgebruikerssessie.

Remote Mac over Tailscale (example)

Veelgebruikte topologie:

  * Gateway draait op Linux/VM
  * iMessage + `imsg` draait op een Mac in je tailnet
  * `cliPath`-wrapper gebruikt SSH om `imsg` uit te voeren
  * `remoteHost` schakelt SCP-ophalen van bijlagen in


Voorbeeld:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "~/.openclaw/scripts/imsg-ssh",      remoteHost: "bot@mac-mini.tailnet-1234.ts.net",      includeAttachments: true,      dbPath: "/Users/bot/Library/Messages/chat.db",    },  },}
[/code]

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T bot@mac-mini.tailnet-1234.ts.net imsg "$@"
[/code]

Gebruik SSH-sleutels zodat zowel SSH als SCP niet-interactief zijn. Zorg eerst dat de hostsleutel wordt vertrouwd (bijvoorbeeld `ssh bot@mac-mini.tailnet-1234.ts.net`) zodat `known_hosts` wordt gevuld.

Multi-account pattern

iMessage ondersteunt configuratie per account onder `channels.imessage.accounts`.

Elk account kan velden overschrijven zoals `cliPath`, `dbPath`, `allowFrom`, `groupPolicy`, `mediaMaxMb`, geschiedenisinstellingen en allowlists voor rootpaden van bijlagen.

## Media, opsplitsing en bezorgdoelen

Attachments and media

  * opname van inkomende bijlagen staat **standaard uit** — stel `channels.imessage.includeAttachments: true` in om foto's, spraakmemo's, video en andere bijlagen door te sturen naar de agent. Als dit is uitgeschakeld, worden iMessages met alleen bijlagen verwijderd voordat ze de agent bereiken en produceren ze mogelijk helemaal geen logregel `Inbound message`.
  * externe bijlagepaden kunnen via SCP worden opgehaald wanneer `remoteHost` is ingesteld
  * bijlagepaden moeten overeenkomen met toegestane rootpaden: 
    * `channels.imessage.attachmentRoots` (lokaal)
    * `channels.imessage.remoteAttachmentRoots` (externe SCP-modus)
    * standaard rootpatroon: `/Users/*/Library/Messages/Attachments`
  * SCP gebruikt strikte hostsleutelcontrole (`StrictHostKeyChecking=yes`)
  * grootte van uitgaande media gebruikt `channels.imessage.mediaMaxMb` (standaard 16 MB)

Outbound chunking

  * limiet voor tekstchunks: `channels.imessage.textChunkLimit` (standaard 4000)
  * chunkmodus: `channels.imessage.chunkMode`
    * `length` (standaard)
    * `newline` (eerst op alinea splitsen)

Addressing formats

Voorkeursdoelen met expliciete aanduiding:

  * `chat_id:123` (aanbevolen voor stabiele routering)
  * `chat_guid:...`
  * `chat_identifier:...`


Handledoelen worden ook ondersteund:

  * `imessage:+1555...`
  * `sms:+1555...`
  * `user@example.com`

bashCopy code
[code]
    imsg chats --limit 20
[/code]

## Acties van de private API

Wanneer `imsg launch` draait en `openclaw channels status --probe` `privateApi.available: true` rapporteert, kan de berichttool naast normale tekstverzending ook iMessage-native acties gebruiken.

json5Copy code
[code]
    {  channels: {    imessage: {      actions: {        reactions: true,        edit: true,        unsend: true,        reply: true,        sendWithEffect: true,        sendAttachment: true,        renameGroup: true,        setGroupIcon: true,        addParticipant: true,        removeParticipant: true,        leaveGroup: true,      },    },  },}
[/code]

Available actions

  * **react** : Voeg iMessage-tapbacks toe of verwijder ze (`messageId`, `emoji`, `remove`). Ondersteunde tapbacks mappen naar liefde, leuk, niet leuk, lachen, nadruk en vraag.
  * **reply** : Verstuur een threaded antwoord op een bestaand bericht (`messageId`, `text` of `message`, plus `chatGuid`, `chatId`, `chatIdentifier` of `to`).
  * **sendWithEffect** : Verstuur tekst met een iMessage-effect (`text` of `message`, `effect` of `effectId`).
  * **edit** : Bewerk een verzonden bericht op ondersteunde macOS-/private API-versies (`messageId`, `text` of `newText`).
  * **unsend** : Trek een verzonden bericht in op ondersteunde macOS-/private API-versies (`messageId`).
  * **upload-file** : Verstuur media/bestanden (`buffer` als base64 of een gehydrateerde `media`/`path`/`filePath`, `filename`, optioneel `asVoice`). Oude alias: `sendAttachment`.
  * **renameGroup** , **setGroupIcon** , **addParticipant** , **removeParticipant** , **leaveGroup** : Beheer groepschats wanneer het huidige doel een groepsgesprek is.

Message IDs

Inkomende iMessage-context bevat zowel korte `MessageSid`-waarden als volledige bericht-GUID's wanneer beschikbaar. Korte ID's zijn beperkt tot de recente in-memory antwoordcache en worden voor gebruik gecontroleerd tegen de huidige chat. Als een korte ID is verlopen of bij een andere chat hoort, probeer het dan opnieuw met de volledige `MessageSidFull`.

Capability detection

OpenClaw verbergt private API-acties alleen wanneer de gecachte probestatus aangeeft dat de bridge niet beschikbaar is. Als de status onbekend is, blijven acties zichtbaar en dispatcht de uitvoering probes lui, zodat de eerste actie kan slagen na `imsg launch` zonder een afzonderlijke handmatige statusverversing.

Read receipts and typing

Wanneer de private API-bridge actief is, worden geaccepteerde inkomende chats voor dispatch als gelezen gemarkeerd en wordt er een typballon aan de afzender getoond terwijl de agent genereert. Schakel leesmarkering uit met:

json5Copy code
[code]
    {  channels: {    imessage: {      sendReadReceipts: false,    },  },}
[/code]

Oudere `imsg`-builds van voor de lijst met mogelijkheden per methode schakelen typen/lezen stilzwijgend uit; OpenClaw logt eenmaal per herstart een waarschuwing zodat de ontbrekende ontvangstbevestiging herleidbaar is.

Inbound tapbacks

OpenClaw abonneert zich op iMessage-tapbacks en routeert geaccepteerde reacties als systeemgebeurtenissen in plaats van normale berichttekst, zodat een tapback van een gebruiker geen gewone antwoordlus triggert.

Meldingsmodus wordt beheerd door `channels.imessage.reactionNotifications`:

  * `"own"` (standaard): meld alleen wanneer gebruikers reageren op berichten die door de bot zijn geschreven.
  * `"all"`: meld alle inkomende tapbacks van geautoriseerde afzenders.
  * `"off"`: negeer inkomende tapbacks.


Overschrijvingen per account gebruiken `channels.imessage.accounts.<id>.reactionNotifications`.

## Configuratiewrites

iMessage staat standaard door het kanaal geïnitieerde configuratiewrites toe (voor `/config set|unset` wanneer `commands.config: true`).

Uitschakelen:

json5Copy code
[code]
    {  channels: {    imessage: {      configWrites: false,    },  },}
[/code]

## Gesplitst verzonden DM's samenvoegen (opdracht + URL in één compositie)

Wanneer een gebruiker samen een opdracht en een URL typt — bijv. `Dump https://example.com/article` — splitst Apple's Messages-app de verzending in **twee afzonderlijke`chat.db`-rijen**:

  1. Een tekstbericht (`"Dump"`).
  2. Een URL-previewballon (`"https://..."`) met OG-previewafbeeldingen als bijlagen.


De twee rijen komen op de meeste setups ~0,8-2,0 s na elkaar bij OpenClaw aan. Zonder samenvoegen ontvangt de agent alleen de opdracht in beurt 1, antwoordt (vaak "stuur me de URL") en ziet de URL pas in beurt 2 — op dat moment is de opdrachtcontext al verloren. Dit is Apple's verzendpipeline, niet iets dat OpenClaw of `imsg` introduceert.

`channels.imessage.coalesceSameSenderDms` laat een DM opeenvolgende rijen van dezelfde afzender samenvoegen tot een enkele agentbeurt. Groepschats blijven per bericht dispatchen, zodat de beurtstructuur met meerdere gebruikers behouden blijft.

### Wanneer inschakelen

Schakel in wanneer:

  * Je Skills levert die `command + payload` in één bericht verwachten (dump, paste, save, queue, enz.).
  * Je gebruikers URL's, afbeeldingen of lange inhoud naast opdrachten plakken.
  * Je de toegevoegde DM-beurtlatentie kunt accepteren (zie hieronder).


Laat uitgeschakeld wanneer:

  * Je minimale opdrachtlatentie nodig hebt voor DM-triggers van één woord.
  * Al je flows eenmalige opdrachten zijn zonder payload-vervolgberichten.


### Inschakelen

json5Copy code
[code]
    {  channels: {    imessage: {      coalesceSameSenderDms: true, // opt in (default: false)    },  },}
[/code]

Met de vlag aan en zonder expliciete `messages.inbound.byChannel.imessage` wordt het debounce-venster verbreed naar **2500 ms** (de legacy-standaard is 0 ms — geen debounce). Het bredere venster is vereist omdat Apple's split-send-cadans van 0,8-2,0 s niet in een strakkere standaard past.

Om het venster zelf af te stemmen:

json5Copy code
[code]
    {  messages: {    inbound: {      byChannel: {        // 2500 ms works for most setups; raise to 4000 ms if your Mac is        // slow or under memory pressure (observed gap can stretch past 2 s        // then).        imessage: 2500,      },    },  },}
[/code]

### Afwegingen

  * **Toegevoegde latentie voor DM-berichten.** Met de vlag aan wacht elke DM (inclusief zelfstandige besturingsopdrachten en losse tekstvervolgen) maximaal het debounce-venster voordat deze wordt gedispatcht, voor het geval er een payload-rij aankomt. Groepschatberichten blijven direct dispatchen.
  * **Samengevoegde uitvoer is begrensd.** Samengevoegde tekst is begrensd op 4000 tekens met een expliciete markering `…[truncated]`; bijlagen zijn begrensd op 20; bronvermeldingen zijn begrensd op 10 (eerste-plus-laatste blijven daarboven behouden). Elke bron-GUID wordt bijgehouden in `coalescedMessageGuids` voor downstreamtelemetrie.
  * **Alleen DM's.** Groepschats vallen terug op dispatch per bericht, zodat de bot responsief blijft wanneer meerdere mensen typen.
  * **Opt-in, per kanaal.** Andere kanalen (Telegram, WhatsApp, Slack, …) blijven onaangetast. Legacy BlueBubbles-configuraties die `channels.bluebubbles.coalesceSameSenderDms` instellen, moeten die waarde migreren naar `channels.imessage.coalesceSameSenderDms`.


### Scenario's en wat de agent ziet

Gebruiker stelt op | `chat.db` produceert | Vlag uit (standaard) | Vlag aan + venster van 2500 ms  
---|---|---|---  
`Dump https://example.com` (één verzending) | 2 rijen ~1 s uit elkaar | Twee agentbeurten: alleen "Dump", daarna URL | Eén beurt: samengevoegde tekst `Dump https://example.com`  
`Save this 📎image.jpg caption` (bijlage + tekst) | 2 rijen | Twee beurten (bijlage valt weg bij samenvoeging) | Eén beurt: tekst + afbeelding behouden  
`/status` (zelfstandige opdracht) | 1 rij | Directe dispatch | **Wacht maximaal het venster en dispatcht daarna**  
Alleen URL geplakt | 1 rij | Directe dispatch | Directe dispatch (slechts één item in bucket)  
Tekst + URL verzonden als twee bewuste afzonderlijke berichten, minuten uit elkaar | 2 rijen buiten venster | Twee beurten | Twee beurten (venster verloopt ertussen)  
Snelle stroom (>10 kleine DM's binnen venster) | N rijen | N beurten | Eén beurt, begrensde uitvoer (eerste + laatste, tekst-/bijlagelimieten toegepast)  
Twee mensen typen in een groepschat | N rijen van M afzenders | M+ beurten (één per afzenderbucket) | M+ beurten — groepschats worden niet samengevoegd  
  
## Inhalen na Gateway-downtime

Wanneer de Gateway offline is (crash, herstart, Mac in slaapstand, machine uit), hervat `imsg watch` vanaf de huidige `chat.db`-staat zodra de Gateway weer opkomt — alles wat tijdens de onderbreking is binnengekomen, wordt standaard nooit gezien. Catchup speelt die berichten opnieuw af bij de volgende start, zodat de agent inkomend verkeer niet stilzwijgend mist.

Catchup is **standaard uitgeschakeld**. Schakel het per kanaal in:

tsCopy code
[code]
    channels: {  imessage: {    catchup: {      enabled: true,             // master switch (default: false)      maxAgeMinutes: 120,        // skip rows older than now - 2h (default: 120, clamp 1..720)      perRunLimit: 50,           // max rows replayed per startup (default: 50, clamp 1..500)      firstRunLookbackMinutes: 30, // first run with no cursor: look back 30 min (default: 30)      maxFailureRetries: 10,     // give up on a wedged guid after 10 dispatch failures (default: 10)    },  },}
[/code]

### Hoe het draait

Eén pass per `monitorIMessageProvider`-start, geordend als `imsg launch` gereed → `watch.subscribe` → `performIMessageCatchup` → live dispatch-loop. Catchup zelf gebruikt `chats.list` \+ per-chat `messages.history` via dezelfde JSON-RPC-client die door `imsg watch` wordt gebruikt. Alles wat tijdens de catchup-pass binnenkomt, loopt normaal via live dispatch; de bestaande inbound-dedupe-cache vangt eventuele overlap met opnieuw afgespeelde rijen op.

Elke opnieuw afgespeelde rij wordt door het live dispatch-pad gevoerd (`evaluateIMessageInbound` \+ `dispatchInboundMessage`), zodat allowlists, groepsbeleid, debouncer, echo-cache en leesbewijzen zich identiek gedragen bij opnieuw afgespeelde en live berichten.

### Cursor- en retrysemantiek

Catchup houdt een cursor per account bij op `<openclawStateDir>/imessage/catchup/<account>__<hash>.json` (de standaard OpenClaw-statusmap is `~/.openclaw`, overschrijfbaar met `OPENCLAW_STATE_DIR`):

jsonCopy code
[code]
    {  "lastSeenMs": 1717900800000,  "lastSeenRowid": 482910,  "updatedAt": 1717900801234,  "failureRetries": { "<guid>": 1 }}
[/code]

  * De cursor schuift op na elke succesvolle dispatch en blijft staan wanneer de dispatch van een rij een exception gooit — de volgende start probeert dezelfde rij opnieuw vanaf de vastgehouden cursor.
  * Na `maxFailureRetries` opeenvolgende exceptions voor dezelfde `guid` logt catchup een `warn` en forceert het opschuiven van de cursor voorbij het vastgelopen bericht, zodat latere starts voortgang kunnen maken.
  * GUID's die al zijn opgegeven, worden bij later runs bij zicht overgeslagen (geen dispatch-poging) en meegeteld onder `skippedGivenUp` in de run-samenvatting.


### Operator-zichtbare signalen

CodeCopy code
[code]
    imessage catchup: replayed=N skippedFromMe=… skippedGivenUp=… failed=… givenUp=… fetchedCount=…imessage catchup: giving up on guid=<guid> after &lt;N&gt; failures; advancing cursor past itimessage catchup: fetched &lt;X&gt; rows across chats, capped to perRunLimit=&lt;Y&gt;
[/code]

Een regel `WARN ... capped to perRunLimit` betekent dat één start niet de volledige achterstand heeft weggewerkt. Verhoog `perRunLimit` (max 500) als je onderbrekingen regelmatig de standaardpass van 50 rijen overschrijden.

### Wanneer je het uit laat

  * Gateway draait continu met watchdog-autoherstart en onderbrekingen zijn altijd < een paar seconden — de standaard uitgeschakelde stand is prima.
  * DM-volume is laag en gemiste berichten zouden het gedrag van de agent niet veranderen — het initiële venster `firstRunLookbackMinutes` kan bij de eerste inschakeling verrassende oude context dispatchen.


Wanneer je catchup inschakelt, kijkt de eerste start zonder cursor alleen `firstRunLookbackMinutes` terug (standaard 30 min), niet het volledige venster `maxAgeMinutes` — dit voorkomt dat een lange geschiedenis van berichten van vóór inschakeling opnieuw wordt afgespeeld.

## Probleemoplossing

imsg niet gevonden of RPC niet ondersteund

Valideer de binary en RPC-ondersteuning:

bashCopy code
[code]
    imsg rpc --helpimsg status --jsonopenclaw channels status --probe
[/code]

Als probe meldt dat RPC niet wordt ondersteund, werk `imsg` bij. Als private API-acties niet beschikbaar zijn, voer `imsg launch` uit in de ingelogde macOS-gebruikerssessie en probe opnieuw. Als de Gateway niet op macOS draait, gebruik dan de Remote Mac over SSH-setup hierboven in plaats van het standaard lokale `imsg`-pad.

Gateway draait niet op macOS

De standaard `cliPath: "imsg"` moet draaien op de Mac die is ingelogd bij Berichten. Stel op Linux of Windows `channels.imessage.cliPath` in op een wrapperscript dat via SSH naar die Mac gaat en `imsg "$@"` uitvoert.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T messages-mac imsg "$@"
[/code]

Voer daarna uit:

bashCopy code
[code]
    openclaw channels status --probe --channel imessage
[/code]

DM's worden genegeerd

Controleer:

  * `channels.imessage.dmPolicy`
  * `channels.imessage.allowFrom`
  * koppelingsgoedkeuringen (`openclaw pairing list imessage`)

Groepsberichten worden genegeerd

Controleer:

  * `channels.imessage.groupPolicy`
  * `channels.imessage.groupAllowFrom`
  * allowlist-gedrag van `channels.imessage.groups`
  * configuratie van vermeldingspatronen (`agents.list[].groupChat.mentionPatterns`)

Externe bijlagen mislukken

Controleer:

  * `channels.imessage.remoteHost`
  * `channels.imessage.remoteAttachmentRoots`
  * SSH/SCP-sleutelauthenticatie vanaf de Gateway-host
  * hostsleutel bestaat in `~/.ssh/known_hosts` op de Gateway-host
  * leesbaarheid van het externe pad op de Mac waarop Berichten draait

macOS-permissieprompts zijn gemist

Voer opnieuw uit in een interactieve GUI-terminal in dezelfde gebruikers-/sessiecontext en keur prompts goed:

bashCopy code
[code]
    imsg chats --limit 1imsg send <handle> "test"
[/code]

Bevestig dat Full Disk Access + Automation zijn verleend voor de procescontext die OpenClaw/`imsg` uitvoert.

## Verwijzingen naar configuratiereferentie

  * [Configuratiereferentie - iMessage](</nl/gateway/config-channels#imessage>)
  * [Gateway-configuratie](</nl/gateway/configuration>)
  * [Koppeling](</nl/channels/pairing>)


## Gerelateerd

  * [Kanaaloverzicht](</nl/channels>) — alle ondersteunde kanalen
  * [BlueBubbles-verwijdering en het imsg iMessage-pad](</nl/announcements/bluebubbles-imessage>) — aankondiging en migratiesamenvatting
  * [Overstappen vanaf BlueBubbles](</nl/channels/imessage-from-bluebubbles>) — configuratievertaaltabel en stapsgewijze overgang
  * [Koppeling](</nl/channels/pairing>) — DM-authenticatie en koppelingsflow
  * [Groepen](</nl/channels/groups>) — groepschatgedrag en vermeldingsgate
  * [Kanaalroutering](</nl/channels/channel-routing>) — sessieroutering voor berichten
  * [Beveiliging](</nl/gateway/security>) — toegangsmodel en hardening


Was this useful?YesNo