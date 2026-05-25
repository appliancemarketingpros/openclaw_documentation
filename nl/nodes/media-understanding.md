---
title: Mediabegrip
source_url: https://docs.openclaw.ai/nl/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw kan **binnenkomende media samenvatten** (afbeelding/audio/video) voordat de antwoordpipeline wordt uitgevoerd. Het detecteert automatisch wanneer lokale tools of providersleutels beschikbaar zijn, en kan worden uitgeschakeld of aangepast. Als begrip uitstaat, ontvangen modellen nog steeds zoals gebruikelijk de oorspronkelijke bestanden/URL’s.

Leveranciersspecifiek mediagedrag wordt geregistreerd door leverancierplugins, terwijl OpenClaw core eigenaar is van de gedeelde `tools.media`-configuratie, fallbackvolgorde en integratie met de antwoordpipeline.

## Doelen

  * Optioneel: verwerk binnenkomende media vooraf tot korte tekst voor snellere routering + betere opdrachtanalyse.
  * Behoud levering van oorspronkelijke media aan het model (altijd).
  * Ondersteun **provider-API’s** en **CLI-fallbacks**.
  * Sta meerdere modellen toe met geordende fallback (fout/grootte/time-out).


## Gedrag op hoofdlijnen

* ### Bijlagen verzamelen

Verzamel binnenkomende bijlagen (`MediaPaths`, `MediaUrls`, `MediaTypes`).

* ### Per capaciteit selecteren

Selecteer voor elke ingeschakelde capaciteit (afbeelding/audio/video) bijlagen volgens beleid (standaard: **eerste**).

* ### Model kiezen

Kies de eerste geschikte modelvermelding (grootte + capaciteit + auth).

* ### Fallback bij mislukking

Als een model mislukt of de media te groot zijn, **val terug op de volgende vermelding**.

* ### Succesblok toepassen

Bij succes:

  * `Body` wordt een `[Image]`-, `[Audio]`\- of `[Video]`-blok.
  * Audio stelt `{{Transcript}}` in; opdrachtanalyse gebruikt bijschrijfttekst wanneer aanwezig, anders het transcript.
  * Bijschriften blijven behouden als `User text:` in het blok.


Als begrip mislukt of is uitgeschakeld, **gaat de antwoordflow door** met de oorspronkelijke body + bijlagen.

## Configuratieoverzicht

`tools.media` ondersteunt **gedeelde modellen** plus overrides per capaciteit:

Sleutels op het hoogste niveau

  * `tools.media.models`: gedeelde modellenlijst (gebruik `capabilities` om te beperken).
  * `tools.media.image` / `tools.media.audio` / `tools.media.video`: 
    * standaardwaarden (`prompt`, `maxChars`, `maxBytes`, `timeoutSeconds`, `language`)
    * provideroverrides (`baseUrl`, `headers`, `providerOptions`)
    * Deepgram-audio-opties via `tools.media.audio.providerOptions.deepgram`
    * echo-instellingen voor audiotranscript (`echoTranscript`, standaard `false`; `echoFormat`)
    * optionele **per-capaciteit`models`-lijst** (heeft voorkeur boven gedeelde modellen)
    * `attachments`-beleid (`mode`, `maxAttachments`, `prefer`)
    * `scope` (optionele gating op channel/chatType/sessiesleutel)
  * `tools.media.concurrency`: maximaal gelijktijdige capaciteitsruns (standaard **2**).


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### Modelvermeldingen

Elke `models[]`-vermelding kan **provider** of **CLI** zijn:

### Providervermelding

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### CLI-vermelding

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

CLI-sjablonen kunnen ook gebruiken:

  * `{{MediaDir}}` (map die het mediabestand bevat)
  * `{{OutputDir}}` (scratchmap gemaakt voor deze run)
  * `{{OutputBase}}` (basispad van scratchbestand, zonder extensie)


## Standaardwaarden en limieten

Aanbevolen standaardwaarden:

  * `maxChars`: **500** voor afbeelding/video (kort, opdrachtvriendelijk)
  * `maxChars`: **niet ingesteld** voor audio (volledig transcript tenzij je een limiet instelt)
  * `maxBytes`: 
    * afbeelding: **10MB**
    * audio: **20MB**
    * video: **50MB**


Regels

  * Als media `maxBytes` overschrijden, wordt dat model overgeslagen en wordt het **volgende model geprobeerd**.
  * Audiobestanden kleiner dan **1024 bytes** worden behandeld als leeg/beschadigd en overgeslagen vóór provider-/CLI-transcriptie; de binnenkomende antwoordcontext ontvangt een deterministisch placeholdertranscript zodat de agent weet dat de notitie te klein was.
  * Als het model meer dan `maxChars` retourneert, wordt de uitvoer ingekort.
  * `prompt` gebruikt standaard eenvoudige "Describe the {media}." plus de `maxChars`-richtlijn (alleen afbeelding/video).
  * Als het actieve primaire afbeeldingsmodel al native vision ondersteunt, slaat OpenClaw het `[Image]`-samenvattingsblok over en geeft het de oorspronkelijke afbeelding in plaats daarvan door aan het model.
  * Als een Gateway-/WebChat-primair model alleen tekst ondersteunt, blijven afbeeldingsbijlagen behouden als offloaded `media://inbound/*`-refs zodat de afbeelding-/PDF-tools of het geconfigureerde afbeeldingsmodel ze nog steeds kunnen inspecteren in plaats van de bijlage kwijt te raken.
  * Expliciete `openclaw infer image describe --model <provider/model>`-verzoeken zijn anders: ze voeren dat afbeeldingscapabele provider/model direct uit, inclusief Ollama-refs zoals `ollama/qwen2.5vl:7b`.
  * Als `<capability>.enabled: true` maar er geen modellen zijn geconfigureerd, probeert OpenClaw het **actieve antwoordmodel** wanneer de provider de capaciteit ondersteunt.


### Mediabegrip automatisch detecteren (standaard)

Als `tools.media.<capability>.enabled` **niet** is ingesteld op `false` en je geen modellen hebt geconfigureerd, detecteert OpenClaw automatisch in deze volgorde en **stopt bij de eerste werkende optie** :

* ### Actief antwoordmodel

Actief antwoordmodel wanneer de provider de capaciteit ondersteunt.

* ### agents.defaults.imageModel

`agents.defaults.imageModel` primaire/fallback-refs (alleen afbeelding). Geef de voorkeur aan `provider/model`-refs. Kale refs worden alleen gekwalificeerd vanuit geconfigureerde afbeeldingscapabele providermodelvermeldingen wanneer de match uniek is.

* ### Lokale CLI’s (alleen audio)

Lokale CLI’s (indien geïnstalleerd):

  * `sherpa-onnx-offline` (vereist `SHERPA_ONNX_MODEL_DIR` met encoder/decoder/joiner/tokens)
  * `whisper-cli` (`whisper-cpp`; gebruikt `WHISPER_CPP_MODEL` of het gebundelde tiny-model)
  * `whisper` (Python-CLI; downloadt modellen automatisch)


* ### Gemini CLI

`gemini` met `read_many_files`.

* ### Providerauth

  * Geconfigureerde `models.providers.*`-vermeldingen die de capaciteit ondersteunen, worden geprobeerd vóór de gebundelde fallbackvolgorde.
  * Providers met alleen afbeeldingsconfiguratie en een afbeeldingscapabel model registreren zich automatisch voor mediabegrip, zelfs wanneer ze geen gebundelde leverancierplugin zijn.
  * Ollama-afbeeldingsbegrip is beschikbaar wanneer expliciet geselecteerd, bijvoorbeeld via `agents.defaults.imageModel` of `openclaw infer image describe --model ollama/<vision-model>`.


Gebundelde fallbackvolgorde:

  * Audio: OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * Afbeelding: OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * Video: Google → Qwen → Moonshot


Om automatische detectie uit te schakelen, stel in:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### Ondersteuning voor proxyomgevingen (providermodellen)

Wanneer providergebaseerd **audio** \- en **video** mediabegrip is ingeschakeld, respecteert OpenClaw standaard uitgaande proxyomgevingsvariabelen voor provider-HTTP-aanroepen:

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


Als er geen proxy-env-vars zijn ingesteld, gebruikt mediabegrip directe egress. Als de proxywaarde ongeldig is, logt OpenClaw een waarschuwing en valt het terug op direct ophalen.

## Capaciteiten (optioneel)

Als je `capabilities` instelt, draait de vermelding alleen voor die mediatypen. Voor gedeelde lijsten kan OpenClaw standaardwaarden afleiden:

  * `openai`, `anthropic`, `minimax`: **afbeelding**
  * `minimax-portal`: **afbeelding**
  * `moonshot`: **afbeelding + video**
  * `openrouter`: **afbeelding + audio**
  * `google` (Gemini API): **afbeelding + audio + video**
  * `qwen`: **afbeelding + video**
  * `mistral`: **audio**
  * `zai`: **afbeelding**
  * `groq`: **audio**
  * `xai`: **audio**
  * `deepgram`: **audio**
  * Elke `models.providers.<id>.models[]`-catalogus met een afbeeldingscapabel model: **afbeelding**


Voor CLI-vermeldingen: **stel`capabilities` expliciet in** om verrassende matches te voorkomen. Als je `capabilities` weglaat, komt de vermelding in aanmerking voor de lijst waarin deze staat.

## Providerondersteuningsmatrix (OpenClaw-integraties)

Capaciteit | Providerintegratie | Notities  
---|---|---  
Afbeelding | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), config providers | Leverancierplugins registreren afbeeldingsondersteuning; `openai-codex/*` gebruikt OAuth-providerplumbing; `codex/*` gebruikt een begrensde Codex app-server-turn; MiniMax en MiniMax OAuth gebruiken allebei `MiniMax-VL-01`; afbeeldingscapabele config providers registreren zich automatisch.  
Audio | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | Providertranscriptie (Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral).  
Video | Google, Qwen, Moonshot | Providervideobegrip via leverancierplugins; Qwen-videobegrip gebruikt de Standard DashScope-endpoints.  
  
## Richtlijnen voor modelselectie

  * Geef de voorkeur aan het sterkste beschikbare nieuwste-generatiemodel voor elke mediacapaciteit wanneer kwaliteit en veiligheid belangrijk zijn.
  * Vermijd oudere/zwakkere mediamodellen voor tool-enabled agents die onvertrouwde invoer verwerken.
  * Houd ten minste één fallback per capaciteit voor beschikbaarheid (kwaliteitsmodel + sneller/goedkoper model).
  * CLI-fallbacks (`whisper-cli`, `whisper`, `gemini`) zijn nuttig wanneer provider-API’s niet beschikbaar zijn.
  * `parakeet-mlx`-notitie: met `--output-dir` leest OpenClaw `<output-dir>/<media-basename>.txt` wanneer de uitvoerindeling `txt` is (of niet is opgegeven); niet-`txt`-indelingen vallen terug op stdout.


## Bijlagebeleid

Per-capaciteit `attachments` bepaalt welke bijlagen worden verwerkt:

Of de eerste geselecteerde bijlage of alle geselecteerde bijlagen moeten worden verwerkt.

Beperk het aantal dat wordt verwerkt.

Selectievoorkeur tussen kandidaatbijlagen.

Wanneer `mode: "all"` is, krijgen uitvoerresultaten labels zoals `[Image 1/2]`, `[Audio 2/2]`, enzovoort.

File-attachment extraction behavior

  * Geëxtraheerde bestandstekst wordt verpakt als **niet-vertrouwde externe inhoud** voordat deze aan de mediaprompt wordt toegevoegd.
  * Het geïnjecteerde blok gebruikt expliciete grensmarkeringen zoals `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` en bevat een metadataregel `Source: External`.
  * Dit pad voor bijlage-extractie laat bewust de lange banner `SECURITY NOTICE:` weg om te voorkomen dat de mediaprompt opzwelt; de grensmarkeringen en metadata blijven wel behouden.
  * Als een bestand geen extraheerbare tekst heeft, injecteert OpenClaw `[No extractable text]`.
  * Als een PDF in dit pad terugvalt op gerenderde pagina-afbeeldingen, behoudt de mediaprompt de placeholder `[PDF content rendered to images; images not forwarded to model]`, omdat deze stap voor bijlage-extractie tekstblokken doorstuurt, niet de gerenderde PDF-afbeeldingen.


## Configuratievoorbeelden

### Shared models + overrides

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### Audio + video only

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Image-only

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Multi-modal single entry

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## Statusuitvoer

Wanneer mediabegrip wordt uitgevoerd, bevat `/status` een korte samenvattingsregel:

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

Dit toont resultaten per capability en, waar van toepassing, de gekozen provider/het gekozen model.

## Opmerkingen

  * Begrip is **best-effort**. Fouten blokkeren antwoorden niet.
  * Bijlagen worden nog steeds aan modellen doorgegeven, zelfs wanneer begrip is uitgeschakeld.
  * Gebruik `scope` om te beperken waar begrip wordt uitgevoerd (bijvoorbeeld alleen DM's).


## Gerelateerd

  * [Configuratie](</nl/gateway/configuration>)
  * [Afbeeldings- en mediaondersteuning](</nl/nodes/images>)


Was this useful?YesNo