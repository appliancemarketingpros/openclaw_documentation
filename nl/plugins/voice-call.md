---
title: Plugin voor spraakoproepen
source_url: https://docs.openclaw.ai/nl/plugins/voice-call
scraped_at: 2026-05-25
---

Spraakoproepen voor OpenClaw via een Plugin. Ondersteunt uitgaande meldingen, gesprekken met meerdere beurten, full-duplex realtime spraak, streaming transcriptie en inkomende oproepen met allowlist-beleid.

**Huidige providers:** `twilio` (Programmable Voice + Media Streams), `telnyx` (Call Control v2), `plivo` (Voice API + XML transfer + GetInput speech), `mock` (dev/geen netwerk).

## Snelstart

* ### Installeer de Plugin

### Vanaf npm

bashCopy code
[code]
    openclaw plugins install @openclaw/voice-call
[/code]

### Vanuit een lokale map (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/voice-call-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Gebruik het kale pakket om de huidige officiële releasetag te volgen. Pin alleen een exacte versie wanneer je een reproduceerbare installatie nodig hebt.

Herstart daarna de Gateway zodat de Plugin wordt geladen.

* ### Configureer provider en Webhook

Stel configuratie in onder `plugins.entries.voice-call.config` (zie Configuratie hieronder voor de volledige vorm). Minimaal: `provider`, providerreferenties, `fromNumber` en een publiek bereikbare Webhook-URL.

* ### Controleer de installatie

bashCopy code
[code]
    openclaw voicecall setup
[/code]

De standaarduitvoer is leesbaar in chatlogs en terminals. Deze controleert of de Plugin is ingeschakeld, providerreferenties, Webhook-blootstelling en dat slechts één audiomodus (`streaming` of `realtime`) actief is. Gebruik `--json` voor scripts.

* ### Rooktest

bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"
[/code]

Beide zijn standaard dry-runs. Voeg `--yes` toe om daadwerkelijk een korte uitgaande meldingsoproep te plaatsen:

bashCopy code
[code]
    openclaw voicecall smoke --to "+15555550123" --yes
[/code]

## Configuratie

Als `enabled: true` is ingesteld maar voor de geselecteerde provider referenties ontbreken, logt het starten van de Gateway een waarschuwing dat de installatie onvolledig is met de ontbrekende sleutels en wordt het starten van de runtime overgeslagen. Commando's, RPC-aanroepen en agenttools geven nog steeds de exacte ontbrekende providerconfiguratie terug wanneer ze worden gebruikt.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio", // or "telnyx" | "plivo" | "mock"          fromNumber: "+15550001234", // or TWILIO_FROM_NUMBER for Twilio          toNumber: "+15550005678",          sessionScope: "per-phone", // per-phone | per-call          numbers: {            "+15550009999": {              inboundGreeting: "Silver Fox Cards, how can I help?",              responseSystemPrompt: "You are a concise baseball card specialist.",              tts: {                providers: {                  openai: { voice: "alloy" },                },              },            },          },           twilio: {            accountSid: "ACxxxxxxxx",            authToken: "...",          },          telnyx: {            apiKey: "...",            connectionId: "...",            // Telnyx webhook public key from the Mission Control Portal            // (Base64; can also be set via TELNYX_PUBLIC_KEY).            publicKey: "...",          },          plivo: {            authId: "MAxxxxxxxxxxxxxxxxxxxx",            authToken: "...",          },           // Webhook server          serve: {            port: 3334,            path: "/voice/webhook",          },           // Webhook security (recommended for tunnels/proxies)          webhookSecurity: {            allowedHosts: ["voice.example.com"],            trustedProxyIPs: ["100.64.0.1"],          },           // Public exposure (pick one)          // publicUrl: "https://example.ngrok.app/voice/webhook",          // tunnel: { provider: "ngrok" },          // tailscale: { mode: "funnel", path: "/voice/webhook" },           outbound: {            defaultMode: "notify", // notify | conversation          },           streaming: { enabled: true /* see Streaming transcription */ },          realtime: { enabled: false /* see Realtime voice */ },        },      },    },  },}
[/code]

Providerblootstelling en beveiligingsnotities

  * Twilio, Telnyx en Plivo vereisen allemaal een **publiek bereikbare** Webhook-URL.
  * `mock` is een lokale dev-provider (geen netwerkaanroepen).
  * Telnyx vereist `telnyx.publicKey` (of `TELNYX_PUBLIC_KEY`), tenzij `skipSignatureVerification` true is.
  * `skipSignatureVerification` is alleen voor lokaal testen.
  * Stel bij de gratis laag van ngrok `publicUrl` in op de exacte ngrok-URL; handtekeningverificatie wordt altijd afgedwongen.
  * `tunnel.allowNgrokFreeTierLoopbackBypass: true` staat Twilio-webhooks met ongeldige handtekeningen **alleen** toe wanneer `tunnel.provider="ngrok"` en `serve.bind` loopback is (lokale ngrok-agent). Alleen lokale dev.
  * URL's van de gratis laag van ngrok kunnen veranderen of interstitial-gedrag toevoegen; als `publicUrl` afwijkt, mislukken Twilio-handtekeningen. Productie: geef de voorkeur aan een stabiel domein of een Tailscale-funnel.

Streaming-verbindingslimieten

  * `streaming.preStartTimeoutMs` sluit sockets die nooit een geldig `start`-frame sturen.
  * `streaming.maxPendingConnections` beperkt het totale aantal niet-geverifieerde pre-start-sockets.
  * `streaming.maxPendingConnectionsPerIp` beperkt niet-geverifieerde pre-start-sockets per bron-IP.
  * `streaming.maxConnections` beperkt het totale aantal open mediastream-sockets (in behandeling + actief).

Migraties van oude configuratie

Oudere configuraties die `provider: "log"`, `twilio.from` of oude `streaming.*` OpenAI-sleutels gebruiken, worden herschreven door `openclaw doctor --fix`. Runtime-fallback accepteert voorlopig nog de oude voice-call-sleutels, maar het herschrijfpad is `openclaw doctor --fix` en de compat-shim is tijdelijk.

Automatisch gemigreerde streaming-sleutels:

  * `streaming.sttProvider` → `streaming.provider`
  * `streaming.openaiApiKey` → `streaming.providers.openai.apiKey`
  * `streaming.sttModel` → `streaming.providers.openai.model`
  * `streaming.silenceDurationMs` → `streaming.providers.openai.silenceDurationMs`
  * `streaming.vadThreshold` → `streaming.providers.openai.vadThreshold`


## Sessiebereik

Standaard gebruikt Voice Call `sessionScope: "per-phone"`, zodat herhaalde oproepen van dezelfde beller gespreksgeheugen behouden. Stel `sessionScope: "per-call"` in wanneer elke carrier-oproep met verse context moet starten, bijvoorbeeld receptie-, boekings-, IVR- of Google Meet-bridgeflows waarbij hetzelfde telefoonnummer verschillende vergaderingen kan vertegenwoordigen.

## Realtime spraakgesprekken

`realtime` selecteert een full-duplex realtime spraakprovider voor live oproepaudio. Dit staat los van `streaming`, dat audio alleen doorstuurt naar realtime transcriptieproviders.

Huidig runtimegedrag:

  * `realtime.enabled` wordt ondersteund voor Twilio Media Streams.
  * `realtime.provider` is optioneel. Indien niet ingesteld, gebruikt Voice Call de eerste geregistreerde realtime spraakprovider.
  * Gebundelde realtime spraakproviders: Google Gemini Live (`google`) en OpenAI (`openai`), geregistreerd door hun provider-Plugins.
  * Ruwe configuratie van de provider staat onder `realtime.providers.<providerId>`.
  * Voice Call stelt standaard de gedeelde realtime-tool `openclaw_agent_consult` beschikbaar. Het realtime model kan deze aanroepen wanneer de beller vraagt om diepere redenering, actuele informatie of normale OpenClaw-tools.
  * `realtime.consultPolicy` voegt optioneel richtlijnen toe voor wanneer het realtime model `openclaw_agent_consult` moet aanroepen.
  * `realtime.agentContext.enabled` staat standaard uit. Wanneer dit is ingeschakeld, injecteert Voice Call tijdens de sessie-installatie een begrensde agentidentiteit, systeem-promptoverride en geselecteerde werkruimtebestandscapsule in de instructies van de realtime provider.
  * `realtime.fastContext.enabled` staat standaard uit. Wanneer dit is ingeschakeld, zoekt Voice Call eerst in geïndexeerd geheugen/sessiecontext naar de consultvraag en retourneert deze fragmenten binnen `realtime.fastContext.timeoutMs` aan het realtime model voordat er alleen wordt teruggevallen op de volledige consultagent als `realtime.fastContext.fallbackToConsult` true is.
  * Als `realtime.provider` naar een niet-geregistreerde provider verwijst, of als er helemaal geen realtime spraakprovider is geregistreerd, logt Voice Call een waarschuwing en slaat het realtime media over in plaats van de hele Plugin te laten mislukken.
  * Consultsessiesleutels hergebruiken de opgeslagen oproepsessie wanneer die beschikbaar is en vallen daarna terug op het geconfigureerde `sessionScope` (`per-phone` standaard, of `per-call` voor geïsoleerde oproepen).


### Toolbeleid

`realtime.toolPolicy` bepaalt de consult-run:

Beleid | Gedrag  
---|---  
`safe-read-only` | Stel de consulttool beschikbaar en beperk de gewone agent tot `read`, `web_search`, `web_fetch`, `x_search`, `memory_search` en `memory_get`.  
`owner` | Stel de consulttool beschikbaar en laat de gewone agent het normale agenttoolbeleid gebruiken.  
`none` | Stel de consulttool niet beschikbaar. Aangepaste `realtime.tools` worden nog steeds doorgegeven aan de realtime provider.  
  
`realtime.consultPolicy` bepaalt alleen de instructies voor het realtime model:

Beleid | Richtlijn  
---|---  
`auto` | Behoud de standaardprompt en laat de provider bepalen wanneer de consulttool moet worden aangeroepen.  
`substantive` | Beantwoord eenvoudige gespreksbruggetjes rechtstreeks en consulteer vóór feiten, geheugen, tools of context.  
`always` | Consulteer vóór elk inhoudelijk antwoord.  
  
### Agent-spraakcontext

Schakel `realtime.agentContext` in wanneer de spraakbridge moet klinken als de geconfigureerde OpenClaw-agent zonder voor gewone beurten een volledige agent-consult-roundtrip te betalen. De contextcapsule wordt één keer toegevoegd wanneer de realtime sessie wordt gemaakt, zodat dit geen per-turn latentie toevoegt. Aanroepen naar `openclaw_agent_consult` voeren nog steeds de volledige OpenClaw-agent uit en moeten worden gebruikt voor toolwerk, actuele informatie, geheugenopzoekingen of werkruimtestatus.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          agentId: "main",          realtime: {            enabled: true,            provider: "google",            toolPolicy: "safe-read-only",            consultPolicy: "substantive",            agentContext: {              enabled: true,              maxChars: 6000,              includeIdentity: true,              includeSystemPrompt: true,              includeWorkspaceFiles: true,              files: ["SOUL.md", "IDENTITY.md", "USER.md"],            },          },        },      },    },  },}
[/code]

### Voorbeelden van realtime providers

### Google Gemini Live

Standaardwaarden: API-sleutel uit `realtime.providers.google.apiKey`, `GEMINI_API_KEY` of `GOOGLE_GENERATIVE_AI_API_KEY`; model `gemini-2.5-flash-native-audio-preview-12-2025`; stem `Kore`. `sessionResumption` en `contextWindowCompression` staan standaard aan voor langere, opnieuw te verbinden gesprekken. Gebruik `silenceDurationMs`, `startSensitivity` en `endSensitivity` om snellere beurtwisseling op telefonie-audio af te stemmen.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          provider: "twilio",          inboundPolicy: "allowlist",          allowFrom: ["+15550005678"],          realtime: {            enabled: true,            provider: "google",            instructions: "Speak briefly. Call openclaw_agent_consult before using deeper tools.",            toolPolicy: "safe-read-only",            consultPolicy: "substantive",            consultThinkingLevel: "low",            consultFastMode: true,            agentContext: { enabled: true },            providers: {              google: {                apiKey: "${GEMINI_API_KEY}",                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                silenceDurationMs: 500,                startSensitivity: "high",              },            },          },        },      },    },  },}
[/code]

### OpenAI

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          realtime: {            enabled: true,            provider: "openai",            providers: {              openai: { apiKey: "${OPENAI_API_KEY}" },            },          },        },      },    },  },}
[/code]

Zie [Google-provider](</nl/providers/google>) en [OpenAI-provider](</nl/providers/openai>) voor providerspecifieke realtime spraakopties.

## Streaming transcriptie

`streaming` selecteert een realtime transcriptieprovider voor live gespreksaudio.

Huidig runtimegedrag:

  * `streaming.provider` is optioneel. Als deze niet is ingesteld, gebruikt Voice Call de eerste geregistreerde realtime transcriptieprovider.
  * Gebundelde realtime transcriptieproviders: Deepgram (`deepgram`), ElevenLabs (`elevenlabs`), Mistral (`mistral`), OpenAI (`openai`) en xAI (`xai`), geregistreerd door hun providerplugins.
  * Ruwe configuratie die eigendom is van de provider staat onder `streaming.providers.<providerId>`.
  * Nadat Twilio een geaccepteerd stream-`start`-bericht verzendt, registreert Voice Call de stream onmiddellijk, zet inkomende media in de wachtrij via de transcriptieprovider terwijl de provider verbinding maakt, en start de eerste begroeting pas nadat realtime transcriptie gereed is.
  * Als `streaming.provider` naar een niet-geregistreerde provider verwijst, of als er geen provider is geregistreerd, logt Voice Call een waarschuwing en slaat het mediastreaming over in plaats van de hele plugin te laten falen.


### Voorbeelden van streamingproviders

### OpenAI

Standaardwaarden: API-sleutel `streaming.providers.openai.apiKey` of `OPENAI_API_KEY`; model `gpt-4o-transcribe`; `silenceDurationMs: 800`; `vadThreshold: 0.5`.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "openai",            streamPath: "/voice/stream",            providers: {              openai: {                apiKey: "sk-...", // optional if OPENAI_API_KEY is set                model: "gpt-4o-transcribe",                silenceDurationMs: 800,                vadThreshold: 0.5,              },            },          },        },      },    },  },}
[/code]

### xAI

Standaardwaarden: API-sleutel `streaming.providers.xai.apiKey` of `XAI_API_KEY`; endpoint `wss://api.x.ai/v1/stt`; codering `mulaw`; samplefrequentie `8000`; `endpointingMs: 800`; `interimResults: true`.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            streamPath: "/voice/stream",            providers: {              xai: {                apiKey: "${XAI_API_KEY}", // optional if XAI_API_KEY is set                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

## TTS voor gesprekken

Voice Call gebruikt de core-`messages.tts`-configuratie voor streaming spraak tijdens gesprekken. Je kunt deze onder de pluginconfiguratie overschrijven met **dezelfde vorm** — deze wordt diep samengevoegd met `messages.tts`.

json5Copy code
[code]
    {  tts: {    provider: "elevenlabs",    providers: {      elevenlabs: {        voiceId: "pMsXgVXv3BLzUgSXRplE",        modelId: "eleven_multilingual_v2",      },    },  },}
[/code]

Gedragsnotities:

  * Verouderde `tts.<provider>`-sleutels binnen pluginconfiguratie (`openai`, `elevenlabs`, `microsoft`, `edge`) worden gerepareerd door `openclaw doctor --fix`; vastgelegde configuratie moet `tts.providers.<provider>` gebruiken.
  * Core-TTS wordt gebruikt wanneer Twilio-mediastreaming is ingeschakeld; anders vallen gesprekken terug op provider-native stemmen.
  * Als een Twilio-mediastream al actief is, valt Voice Call niet terug op TwiML `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5`. Als telefonie-TTS in die status niet beschikbaar is, mislukt het afspeelverzoek in plaats van twee afspeelpaden te mengen.
  * Wanneer telefonie-TTS terugvalt op een secundaire provider, logt Voice Call een waarschuwing met de providerketen (`from`, `to`, `attempts`) voor debugging.
  * Wanneer Twilio barge-in of het afbreken van de stream de wachtende TTS-wachtrij wist, worden in de wachtrij geplaatste afspeelverzoeken afgehandeld in plaats van bellers te laten hangen terwijl ze wachten op voltooiing van het afspelen.


### TTS-voorbeelden

### Core TTS only

json5Copy code
[code]
    {messages: {tts: {provider: "openai",providers: {  openai: { voice: "alloy" },},},},}
[/code]

### Override to ElevenLabs (calls only)

json5Copy code
[code]
    {plugins: {entries: {"voice-call": {  config: {    tts: {      provider: "elevenlabs",      providers: {        elevenlabs: {          apiKey: "elevenlabs_key",          voiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },},},},}
[/code]

### OpenAI model override (deep-merge)

json5Copy code
[code]
    {plugins: {entries: {"voice-call": {  config: {    tts: {      providers: {        openai: {          model: "gpt-4o-mini-tts",          voice: "marin",        },      },    },  },},},},}
[/code]

## Inkomende gesprekken

Inkomend beleid staat standaard op `disabled`. Stel het volgende in om inkomende gesprekken in te schakelen:

json5Copy code
[code]
    {inboundPolicy: "allowlist",allowFrom: ["+15550001234"],inboundGreeting: "Hello! How can I help?",}
[/code]

Automatische antwoorden gebruiken het agentsysteem. Stem af met `responseModel`, `responseSystemPrompt` en `responseTimeoutMs`.

### Routering per nummer

Gebruik `numbers` wanneer één Voice Call-plugin gesprekken ontvangt voor meerdere telefoonnummers en elk nummer zich als een andere lijn moet gedragen. Zo kan één nummer een informele persoonlijke assistent gebruiken, terwijl een ander een zakelijke persona, een andere antwoordagent en een andere TTS-stem gebruikt.

Routes worden geselecteerd op basis van het door de provider geleverde gebelde `To`-nummer. Sleutels moeten E.164-nummers zijn. Wanneer een gesprek binnenkomt, lost Voice Call de overeenkomende route één keer op, slaat de overeenkomende route op in het gespreksrecord en hergebruikt die effectieve configuratie voor de begroeting, het klassieke pad voor automatische antwoorden, het realtime consultpad en TTS- afspelen. Als geen route overeenkomt, wordt de globale Voice Call-configuratie gebruikt. Uitgaande gesprekken gebruiken `numbers` niet; geef het uitgaande doel, het bericht en de sessie expliciet door wanneer je het gesprek start.

Route-overschrijvingen ondersteunen momenteel:

  * `inboundGreeting`
  * `tts`
  * `agentId`
  * `responseModel`
  * `responseSystemPrompt`
  * `responseTimeoutMs`


De `tts`-routewaarde wordt diep samengevoegd over de globale Voice Call-`tts`-configuratie, zodat je meestal alleen de providerstem hoeft te overschrijven:

json5Copy code
[code]
    {inboundGreeting: "Hello from the main line.",responseSystemPrompt: "You are the default voice assistant.",tts: {  provider: "openai",  providers: {    openai: { voice: "coral" },  },},numbers: {  "+15550001111": {    inboundGreeting: "Silver Fox Cards, how can I help?",    responseSystemPrompt: "You are a concise baseball card specialist.",    tts: {      providers: {        openai: { voice: "alloy" },      },    },  },},}
[/code]

### Contract voor gesproken uitvoer

Voor automatische antwoorden voegt Voice Call een strikt contract voor gesproken uitvoer toe aan de systeemprompt:

textCopy code
[code]
    {"spoken":"..."}
[/code]

Voice Call extraheert spraaktekst defensief:

  * Negeert payloads die zijn gemarkeerd als redeneer-/foutinhoud.
  * Parseert directe JSON, omheinde JSON of inline `"spoken"`-sleutels.
  * Valt terug op platte tekst en verwijdert waarschijnlijke plannings-/meta-inleidende alinea's.


Dit houdt gesproken weergave gericht op tekst voor de beller en voorkomt dat planningstekst in audio lekt.

### Opstartgedrag van gesprekken

Voor uitgaande `conversation`-gesprekken is de verwerking van het eerste bericht gekoppeld aan de live afspeelstatus:

  * Het wissen van de barge-in-wachtrij en automatische antwoorden worden alleen onderdrukt terwijl de eerste begroeting actief wordt uitgesproken.
  * Als het eerste afspelen mislukt, keert het gesprek terug naar `listening` en blijft het eerste bericht in de wachtrij voor een nieuwe poging.
  * Het eerste afspelen voor Twilio-streaming start bij streamverbinding zonder extra vertraging.
  * Barge-in breekt actief afspelen af en wist Twilio-TTS-items die in de wachtrij staan maar nog niet worden afgespeeld. Gewiste items worden opgelost als overgeslagen, zodat vervolgresponslogica kan doorgaan zonder te wachten op audio die nooit zal worden afgespeeld.
  * Realtime spraakgesprekken gebruiken de eigen openingsturn van de realtime stream. Voice Call plaatst **geen** verouderde `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5` TwiML-update voor dat eerste bericht, zodat uitgaande `&lt;Connect&gt;&lt;Stream&gt;`-sessies gekoppeld blijven.


### Genadeperiode voor Twilio-streamverbinding verbreken

Wanneer een Twilio-mediastream de verbinding verbreekt, wacht Voice Call **2000 ms** voordat het gesprek automatisch wordt beëindigd:

  * Als de stream binnen dat venster opnieuw verbinding maakt, wordt automatisch beëindigen geannuleerd.
  * Als geen stream zich na de genadeperiode opnieuw registreert, wordt het gesprek beëindigd om vastgelopen actieve gesprekken te voorkomen.


## Verouderde gesprekken opruimen

Gebruik `staleCallReaperSeconds` om gesprekken te beëindigen die nooit een terminale Webhook ontvangen (bijvoorbeeld notify-modusgesprekken die nooit worden voltooid). De standaardwaarde is `0` (uitgeschakeld).

Aanbevolen bereiken:

  * **Productie:** `120`-`300` seconden voor notify-achtige flows.
  * Houd deze waarde **hoger dan`maxDurationSeconds`** zodat normale aanroepen kunnen afronden. Een goed startpunt is `maxDurationSeconds + 30-60` seconden.

json5Copy code
[code]
    {plugins: {entries: {  "voice-call": {    config: {      maxDurationSeconds: 300,      staleCallReaperSeconds: 360,    },  },},},}
[/code]

## Webhook-beveiliging

Wanneer er een proxy of tunnel voor de Gateway staat, reconstrueert de Plugin de publieke URL voor handtekeningverificatie. Deze opties bepalen welke doorgestuurde headers worden vertrouwd:

Sta hosts uit forwarding-headers toe.

Vertrouw doorgestuurde headers zonder allowlist.

Vertrouw doorgestuurde headers alleen wanneer het externe IP-adres van de aanvraag overeenkomt met de lijst.

Aanvullende beschermingen:

  * Webhook-**replaybeveiliging** is ingeschakeld voor Twilio en Plivo. Opnieuw afgespeelde geldige Webhook-aanvragen worden bevestigd, maar overgeslagen voor bijwerkingen.
  * Twilio-gespreksbeurten bevatten een token per beurt in `&lt;Gather&gt;`-callbacks, zodat verouderde/opnieuw afgespeelde spraakcallbacks geen nieuwere wachtende transcriptbeurt kunnen vervullen.
  * Niet-geverifieerde Webhook-aanvragen worden geweigerd voordat de body wordt gelezen wanneer de vereiste handtekeningheaders van de provider ontbreken.
  * De voice-call-Webhook gebruikt het gedeelde pre-auth-bodyprofiel (64 KB / 5 seconden) plus een in-flight limiet per IP vóór handtekeningverificatie.


Voorbeeld met een stabiele publieke host:

json5Copy code
[code]
    {plugins: {entries: {  "voice-call": {    config: {      publicUrl: "https://voice.example.com/voice/webhook",      webhookSecurity: {        allowedHosts: ["voice.example.com"],      },    },  },},},}
[/code]

## CLI

bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello from OpenClaw"openclaw voicecall start --to "+15555550123"   # alias for callopenclaw voicecall continue --call-id <id> --message "Any questions?"openclaw voicecall speak --call-id <id> --message "One moment"openclaw voicecall dtmf --call-id <id> --digits "ww123456#"openclaw voicecall end --call-id <id>openclaw voicecall status --call-id <id>openclaw voicecall tailopenclaw voicecall latency                      # summarize turn latency from logsopenclaw voicecall expose --mode funnel
[/code]

Wanneer de Gateway al draait, delegeren operationele `voicecall`-opdrachten naar de door de Gateway beheerde voice-call-runtime, zodat de CLI geen tweede Webhook-server bindt. Als er geen Gateway bereikbaar is, vallen de opdrachten terug op een zelfstandige CLI-runtime.

`latency` leest `calls.jsonl` uit het standaardopslagpad voor voice-call. Gebruik `--file <path>` om naar een ander log te wijzen en `--last <n>` om de analyse te beperken tot de laatste N records (standaard 200). De uitvoer bevat p50/p90/p99 voor beurtlatentie en luister-wachttijden.

## Agent-tool

Toolnaam: `voice_call`.

Actie | Argumenten  
---|---  
`initiate_call` | `message`, `to?`, `mode?`, `dtmfSequence?`  
`continue_call` | `callId`, `message`  
`speak_to_user` | `callId`, `message`  
`send_dtmf` | `callId`, `digits`  
`end_call` | `callId`  
`get_status` | `callId`  
  
Deze repo levert een bijbehorend skill-document mee op `skills/voice-call/SKILL.md`.

## Gateway-RPC

Methode | Argumenten  
---|---  
`voicecall.initiate` | `to?`, `message`, `mode?`, `dtmfSequence?`  
`voicecall.continue` | `callId`, `message`  
`voicecall.speak` | `callId`, `message`  
`voicecall.dtmf` | `callId`, `digits`  
`voicecall.end` | `callId`  
`voicecall.status` | `callId`  
  
`dtmfSequence` is alleen geldig met `mode: "conversation"`. Aanroepen in notify-modus moeten `voicecall.dtmf` gebruiken nadat de oproep bestaat als ze cijfers na het verbinden nodig hebben.

## Probleemoplossing

### Setup mislukt bij Webhook-blootstelling

Voer setup uit vanuit dezelfde omgeving die de Gateway uitvoert:

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

Voor `twilio`, `telnyx` en `plivo` moet `webhook-exposure` groen zijn. Een geconfigureerde `publicUrl` mislukt nog steeds wanneer deze naar lokale of privénetwerkruimte wijst, omdat de carrier niet naar die adressen kan terugbellen. Gebruik `localhost`, `127.0.0.1`, `0.0.0.0`, `10.x`, `172.16.x`-`172.31.x`, `192.168.x`, `169.254.x`, `fc00::/7` of `fd00::/8` niet als `publicUrl`.

Uitgaande Twilio-oproepen in notify-modus sturen hun initiële `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5` TwiML rechtstreeks in de create-call-aanvraag, zodat het eerste gesproken bericht niet afhangt van Twilio dat Webhook-TwiML ophaalt. Een publieke Webhook is nog steeds vereist voor statuscallbacks, gespreksoproepen, DTMF vóór het verbinden, realtime streams en oproepbeheer na het verbinden.

Gebruik één publiek blootstellingspad:

json5Copy code
[code]
    {plugins: {entries: {"voice-call": {  config: {    publicUrl: "https://voice.example.com/voice/webhook",    // or    tunnel: { provider: "ngrok" },    // or    tailscale: { mode: "funnel", path: "/voice/webhook" },  },},},},}
[/code]

Start of herlaad de Gateway nadat je de configuratie hebt gewijzigd en voer daarna uit:

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall smoke
[/code]

`voicecall smoke` is een dry run tenzij je `--yes` doorgeeft.

### Providerreferenties mislukken

Controleer de geselecteerde provider en de vereiste referentievelden:

  * Twilio: `twilio.accountSid`, `twilio.authToken` en `fromNumber`, of `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN` en `TWILIO_FROM_NUMBER`.
  * Telnyx: `telnyx.apiKey`, `telnyx.connectionId`, `telnyx.publicKey` en `fromNumber`.
  * Plivo: `plivo.authId`, `plivo.authToken` en `fromNumber`.


Referenties moeten op de Gateway-host bestaan. Het bewerken van een lokaal shellprofiel heeft geen invloed op een al draaiende Gateway totdat deze opnieuw start of zijn omgeving herlaadt.

### Oproepen starten, maar provider-Webhooks komen niet aan

Bevestig dat de providerconsole naar de exacte publieke Webhook-URL wijst:

textCopy code
[code]
    https://voice.example.com/voice/webhook
[/code]

Inspecteer daarna de runtimestatus:

bashCopy code
[code]
    openclaw voicecall status --call-id <id>openclaw voicecall tailopenclaw logs --follow
[/code]

Veelvoorkomende oorzaken:

  * `publicUrl` wijst naar een ander pad dan `serve.path`.
  * De tunnel-URL is gewijzigd nadat de Gateway is gestart.
  * Een proxy stuurt de aanvraag door, maar verwijdert of herschrijft host/proto-headers.
  * Firewall of DNS routeert de publieke hostnaam naar iets anders dan de Gateway.
  * De Gateway is opnieuw gestart zonder dat de Voice Call-Plugin is ingeschakeld.


Wanneer er een reverse proxy of tunnel voor de Gateway staat, stel je `webhookSecurity.allowedHosts` in op de publieke hostnaam, of gebruik je `webhookSecurity.trustedProxyIPs` voor een bekend proxyadres. Gebruik `webhookSecurity.trustForwardingHeaders` alleen wanneer de proxygrens onder jouw controle staat.

### Handtekeningverificatie mislukt

Providerhandtekeningen worden gecontroleerd tegen de publieke URL die OpenClaw reconstrueert uit de inkomende aanvraag. Als handtekeningen mislukken:

  * Bevestig dat de provider-Webhook-URL exact overeenkomt met `publicUrl`, inclusief schema, host en pad.
  * Werk voor ngrok-URL's in de free-tier `publicUrl` bij wanneer de tunnelhostnaam verandert.
  * Zorg dat de proxy de oorspronkelijke host- en proto-headers behoudt, of configureer `webhookSecurity.allowedHosts`.
  * Schakel `skipSignatureVerification` niet in buiten lokaal testen.


### Google Meet Twilio-joins mislukken

Google Meet gebruikt deze Plugin voor Twilio-inbeljoins. Verifieer eerst Voice Call:

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall smoke --to "+15555550123"
[/code]

Verifieer daarna expliciet het Google Meet-transport:

bashCopy code
[code]
    openclaw googlemeet setup --transport twilio
[/code]

Als Voice Call groen is maar de Meet-deelnemer nooit deelneemt, controleer dan het Meet-inbelnummer, de PIN en `--dtmf-sequence`. De telefoonoproep kan gezond zijn terwijl de vergadering een onjuiste DTMF-reeks weigert of negeert.

Google Meet start de Twilio-telefoonleg via `voicecall.start` met een DTMF-reeks vóór het verbinden. Uit PIN afgeleide reeksen bevatten de `voiceCall.dtmfDelayMs` van de Google Meet-Plugin als leidende Twilio-wachtcijfers. De standaardwaarde is 12 seconden omdat Meet-inbelprompts laat kunnen aankomen. Voice Call leidt daarna terug naar realtime afhandeling voordat de introbegroeting wordt aangevraagd.

Gebruik `openclaw logs --follow` voor de live fasetrace. Een gezonde Twilio Meet-join logt deze volgorde:

  * Google Meet delegeert de Twilio-join aan Voice Call.
  * Voice Call slaat DTMF-TwiML vóór het verbinden op.
  * Initiële TwiML van Twilio wordt verbruikt en geserveerd vóór realtime afhandeling.
  * Voice Call serveert realtime TwiML voor de Twilio-oproep.
  * Google Meet vraagt introspraak aan met `voicecall.speak` na de post-DTMF-vertraging.


`openclaw voicecall tail` toont nog steeds blijvende oproeprecords; het is nuttig voor oproepstatus en transcripties, maar niet elke Webhook-/realtime-overgang verschijnt daar.

### Realtime-oproep heeft geen spraak

Bevestig dat slechts één audiomodus is ingeschakeld. `realtime.enabled` en `streaming.enabled` kunnen niet allebei true zijn.

Verifieer voor realtime Twilio-oproepen ook:

  * Er is een realtime provider-Plugin geladen en geregistreerd.
  * `realtime.provider` is niet ingesteld of noemt een geregistreerde provider.
  * De provider-API-sleutel is beschikbaar voor het Gateway-proces.
  * `openclaw logs --follow` toont dat realtime TwiML is geserveerd, de realtime bridge is gestart en de initiële begroeting in de wachtrij is geplaatst.


## Gerelateerd

  * [Praatmodus](</nl/nodes/talk>)
  * [Tekst-naar-spraak](</nl/tools/tts>)
  * [Voice wake](</nl/nodes/voicewake>)


Was this useful?YesNo