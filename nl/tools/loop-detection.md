---
title: Tool-loopdetectie
source_url: https://docs.openclaw.ai/nl/tools/loop-detection
scraped_at: 2026-05-25
---

OpenClaw heeft twee samenwerkende vangrails voor repetitieve toolaanroeppatronen:

  1. **Lusdetectie** (`tools.loopDetection.enabled`) — standaard uitgeschakeld. Bewaakt de doorlopende geschiedenis van toolaanroepen op herhaalde patronen en nieuwe pogingen voor onbekende tools.
  2. **Post-Compaction-beveiliging** (`tools.loopDetection.postCompactionGuard`) — standaard ingeschakeld tenzij `tools.loopDetection.enabled` expliciet `false` is. Wordt ingeschakeld na elke Compaction-herpoging en breekt de run af wanneer de agent binnen het venster dezelfde `(tool, args, result)`-triple uitzendt.


Beide worden geconfigureerd onder hetzelfde `tools.loopDetection`-blok, maar de post-Compaction-beveiliging draait wanneer de hoofdschakelaar niet expliciet uit staat. Stel `tools.loopDetection.enabled: false` in om beide oppervlakken te dempen.

## Waarom dit bestaat

  * Repetitieve reeksen detecteren die geen voortgang boeken.
  * Lussen zonder resultaat met hoge frequentie detecteren (dezelfde tool, dezelfde invoer, herhaalde fouten).
  * Specifieke patronen van herhaalde aanroepen detecteren voor bekende pollingtools.
  * Voorkomen dat context-overflow, gevolgd door Compaction en daarna dezelfde lus, oneindig blijft draaien.


## Configuratieblok

Globale standaardwaarden, met elk gedocumenteerd veld weergegeven:

json5Copy code
[code]
    {  tools: {    loopDetection: {      enabled: false, // master switch for the rolling-history detectors      historySize: 30,      warningThreshold: 10,      criticalThreshold: 20,      unknownToolThreshold: 10,      globalCircuitBreakerThreshold: 30,      detectors: {        genericRepeat: true,        knownPollNoProgress: true,        pingPong: true,      },      postCompactionGuard: {        windowSize: 3, // armed after compaction-retry; runs unless enabled is explicitly false      },    },  },}
[/code]

Override per agent (optioneel):

json5Copy code
[code]
    {  agents: {    list: [      {        id: "safe-runner",        tools: {          loopDetection: {            enabled: true,            warningThreshold: 8,            criticalThreshold: 16,          },        },      },    ],  },}
[/code]

### Veldgedrag

Veld | Standaard | Effect  
---|---|---  
`enabled` | `false` | Hoofdschakelaar voor de detectors met doorlopende geschiedenis. Instellen op `false` schakelt ook de post-Compaction-beveiliging uit.  
`historySize` | `30` | Aantal recente toolaanroepen dat voor analyse wordt bewaard.  
`warningThreshold` | `10` | Drempel voordat een patroon alleen als waarschuwing wordt geclassificeerd.  
`criticalThreshold` | `20` | Drempel voor het blokkeren van repetitieve luspatronen zonder voortgang.  
`unknownToolThreshold` | `10` | Blokkeer herhaalde aanroepen naar dezelfde niet-beschikbare tool na dit aantal missers.  
`globalCircuitBreakerThreshold` | `30` | Globale drempel voor de stroomonderbreker zonder voortgang, over alle detectors heen.  
`detectors.genericRepeat` | `true` | Waarschuwt bij herhaalde patronen met dezelfde tool + dezelfde parameters en blokkeert wanneer dezelfde aanroepen ook identieke uitkomsten opleveren.  
`detectors.knownPollNoProgress` | `true` | Detecteert bekende pollingachtige patronen zonder statuswijziging.  
`detectors.pingPong` | `true` | Detecteert afwisselende pingpongpatronen.  
`postCompactionGuard.windowSize` | `3` | Aantal post-Compaction-toolaanroepen waarin de beveiliging ingeschakeld blijft en het aantal identieke triples dat de run afbreekt.  
  
Voor `exec` vergelijken controles zonder voortgang stabiele opdrachtuitkomsten en negeren ze vluchtige runtime-metadata zoals duur, PID, sessie-ID en werkmap. Wanneer een run-id beschikbaar is, wordt recente toolaanroepgeschiedenis alleen binnen die run geëvalueerd, zodat geplande Heartbeat-cycli en nieuwe runs geen verouderde lustellingen van eerdere runs erven.

## Aanbevolen instelling

  * Stel voor kleinere modellen `enabled: true` in en laat de drempels op hun standaardwaarden. Flagshipmodellen hebben zelden detectie met doorlopende geschiedenis nodig en kunnen de hoofdschakelaar op `false` laten staan, terwijl ze toch profiteren van de post-Compaction-beveiliging.
  * Houd drempels geordend als `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold`.
  * Als fout-positieven optreden: 
    * Verhoog `warningThreshold` en/of `criticalThreshold`.
    * Verhoog eventueel `globalCircuitBreakerThreshold`.
    * Schakel alleen de specifieke detector uit die problemen veroorzaakt (`detectors.<name>: false`).
    * Verlaag `historySize` voor minder strikte historische context.
  * Om alles uit te schakelen (inclusief de post-Compaction-beveiliging), stel `tools.loopDetection.enabled: false` expliciet in.


## Post-Compaction-beveiliging

Wanneer de runner een Compaction-herpoging na een context-overflow voltooit, schakelt hij een beveiliging met een kort venster in die de volgende paar toolaanroepen bewaakt. Als de agent binnen het venster meerdere keren dezelfde `(toolName, argsHash, resultHash)`-triple uitzendt, concludeert de beveiliging dat Compaction de lus niet heeft doorbroken en breekt hij de run af met een `compaction_loop_persisted`-fout.

De beveiliging wordt begrensd door de hoofdvlag `tools.loopDetection.enabled`, met één nuance: hij blijft **ingeschakeld wanneer de vlag niet is ingesteld of`true` is** en wordt alleen gedeactiveerd wanneer de vlag expliciet `false` is. Dit is opzettelijk. De beveiliging bestaat om aan Compaction-lussen te ontsnappen die anders onbeperkt tokens zouden verbruiken, dus een gebruiker zonder configuratie krijgt nog steeds de bescherming.

json5Copy code
[code]
    {  tools: {    loopDetection: {      // master switch; set false to disable the guard along with the rolling detectors      enabled: true,      postCompactionGuard: {        windowSize: 3, // default      },    },  },}
[/code]

  * Een lagere `windowSize` is strikter (minder pogingen vóór afbreken).
  * Een hogere `windowSize` geeft de agent meer herstelpogingen.
  * De beveiliging breekt nooit af wanneer resultaten veranderen, alleen wanneer resultaten byte-identiek zijn binnen het venster.
  * Hij is opzettelijk smal: hij wordt alleen geactiveerd direct na een Compaction-herpoging.


## Logs en verwacht gedrag

Wanneer een lus wordt gedetecteerd, meldt OpenClaw een lusgebeurtenis en dempt of blokkeert het de volgende toolcyclus afhankelijk van de ernst. Dit beschermt gebruikers tegen ontsporende tokenuitgaven en vastlopers, terwijl normale tooltoegang behouden blijft.

  * Waarschuwingen komen eerst.
  * Onderdrukking volgt wanneer patronen voorbij de waarschuwingsdrempel blijven bestaan.
  * Kritieke drempels blokkeren de volgende toolcyclus en tonen een duidelijke reden voor lusdetectie in het runrecord.
  * De post-Compaction-beveiliging geeft `compaction_loop_persisted`-fouten met de naam van de betrokken tool en het aantal identieke aanroepen.


## Gerelateerd

[**Exec-goedkeuringen** Beleid voor toestaan/weigeren van shelluitvoering. ](</nl/tools/exec-approvals>) [**Denkniveaus** Redeneerinspanningsniveaus en interactie met providerbeleid. ](</nl/tools/thinking>) [**Subagenten** Geïsoleerde agents starten om ontsporend gedrag te begrenzen. ](</nl/tools/subagents>) [**Configuratiereferentie** Volledig `tools.loopDetection`-schema en samenvoegsemantiek. ](</nl/gateway/configuration-reference>)

Was this useful?YesNo