---
title: Onboarden
source_url: https://docs.openclaw.ai/nl/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

Volledige begeleide onboarding voor lokale of externe Gateway-configuratie. Gebruik dit wanneer je wilt dat OpenClaw modelauthenticatie, werkruimte, Gateway, kanalen, Skills en gezondheid in één flow doorloopt.

## Gerelateerde gidsen

[**CLI-onboardinghub** Doorloop van de interactieve CLI-flow. ](</nl/start/wizard>) [**Onboardingoverzicht** Hoe OpenClaw-onboarding samenhangt. ](</nl/start/onboarding-overview>) [**CLI-configuratiereferentie** Uitvoer, internals en gedrag per stap. ](</nl/start/wizard-cli-reference>) [**CLI-automatisering** Niet-interactieve flags en gescripte configuraties. ](</nl/start/wizard-cli-automation>) [**macOS-app-onboarding** Onboardingflow voor de macOS-menubalk-app. ](</nl/start/onboarding>)

## Voorbeelden

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` gebruikt migratieproviders die eigendom zijn van plugins, zoals Hermes. Het draait alleen op een nieuwe OpenClaw-configuratie; als bestaande config, inloggegevens, sessies of geheugen-/identiteitsbestanden van de werkruimte aanwezig zijn, reset dan of kies een nieuwe configuratie voordat je importeert.

`--modern` start de preview van de conversationele Crestodian-onboarding. Zonder `--modern` behoudt `openclaw onboard` de klassieke onboardingflow.

Voor plaintext private-network `ws://`-doelen (alleen vertrouwde netwerken), stel je `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` in de procesomgeving van onboarding in. Er is geen `openclaw.json`-equivalent voor deze break-glass voor clientzijdig transport.

Niet-interactieve aangepaste provider:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` is optioneel in niet-interactieve modus. Als deze wordt weggelaten, controleert onboarding `CUSTOM_API_KEY`. OpenClaw markeert gangbare vision-model-ID's automatisch als geschikt voor beeldinvoer. Geef `--custom-image-input` door voor onbekende aangepaste vision-ID's, of `--custom-text-input` om metadata voor alleen tekst af te dwingen.

LM Studio ondersteunt ook een providerspecifieke key-flag in niet-interactieve modus:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Niet-interactieve Ollama:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` gebruikt standaard `http://127.0.0.1:11434`. `--custom-model-id` is optioneel; als deze wordt weggelaten, gebruikt onboarding de voorgestelde standaardwaarden van Ollama. Cloudmodel-ID's zoals `kimi-k2.5:cloud` werken hier ook.

Sla providerkeys op als refs in plaats van plaintext:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

Met `--secret-input-mode ref` schrijft onboarding door env ondersteunde refs in plaats van plaintext keywaarden. Voor providers met auth-profielen schrijft dit `keyRef`-items; voor aangepaste providers schrijft dit `models.providers.<id>.apiKey` als een env-ref (bijvoorbeeld `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

Contract voor niet-interactieve `ref`-modus:

  * Stel de env-var van de provider in de procesomgeving van onboarding in (bijvoorbeeld `OPENAI_API_KEY`).
  * Geef geen inline key-flags door (bijvoorbeeld `--openai-api-key`), tenzij die env-var ook is ingesteld.
  * Als een inline key-flag wordt doorgegeven zonder de vereiste env-var, faalt onboarding snel met begeleiding.


Gateway-tokenopties in niet-interactieve modus:

  * `--gateway-auth token --gateway-token <token>` slaat een plaintext token op.
  * `--gateway-auth token --gateway-token-ref-env <name>` slaat `gateway.auth.token` op als een env SecretRef.
  * `--gateway-token` en `--gateway-token-ref-env` sluiten elkaar uit.
  * `--gateway-token-ref-env` vereist een niet-lege env-var in de procesomgeving van onboarding.
  * Met `--install-daemon`, wanneer tokenauthenticatie een token vereist, worden door SecretRef beheerde Gateway-tokens gevalideerd maar niet als opgeloste plaintext bewaard in metadata van de supervisor-serviceomgeving.
  * Met `--install-daemon`, als tokenmodus een token vereist en de geconfigureerde token-SecretRef niet kan worden opgelost, faalt onboarding gesloten met hersteladvies.
  * Met `--install-daemon`, als zowel `gateway.auth.token` als `gateway.auth.password` zijn geconfigureerd en `gateway.auth.mode` niet is ingesteld, blokkeert onboarding de installatie totdat de modus expliciet is ingesteld.
  * Lokale onboarding schrijft `gateway.mode="local"` naar de config. Als een later configuratiebestand `gateway.mode` mist, behandel dat dan als configschade of een onvolledige handmatige bewerking, niet als een geldige snelkoppeling voor lokale modus.
  * Lokale onboarding installeert geselecteerde downloadbare plugins wanneer het gekozen configuratiepad die vereist.
  * Externe onboarding schrijft alleen verbindingsinformatie voor de externe Gateway en installeert geen lokale pluginpakketten.
  * `--allow-unconfigured` is een afzonderlijke ontsnappingsmogelijkheid voor de Gateway-runtime. Het betekent niet dat onboarding `gateway.mode` mag weglaten.


Voorbeeld:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

Niet-interactieve gezondheid van lokale Gateway:

  * Tenzij je `--skip-health` doorgeeft, wacht onboarding op een bereikbare lokale Gateway voordat het succesvol afsluit.
  * `--install-daemon` start eerst het beheerde Gateway-installatiepad. Zonder deze optie moet er al een lokale Gateway draaien, bijvoorbeeld `openclaw gateway run`.
  * Als je in automatisering alleen config-/werkruimte-/bootstrap-writes wilt, gebruik dan `--skip-health`.
  * Als je werkruimtebestanden zelf beheert, geef dan `--skip-bootstrap` door om `agents.defaults.skipBootstrap: true` in te stellen en het maken van `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md` en `BOOTSTRAP.md` over te slaan.
  * Op native Windows probeert `--install-daemon` eerst Scheduled Tasks en valt het terug op een loginitem in de Startup-map per gebruiker als het maken van de taak wordt geweigerd.


Interactief onboardinggedrag met referentiemodus:

  * Kies **Geheime referentie gebruiken** wanneer daarom wordt gevraagd.
  * Kies daarna een van beide: 
    * Omgevingsvariabele
    * Geconfigureerde secretprovider (`file` of `exec`)
  * Onboarding voert een snelle preflightvalidatie uit voordat de ref wordt opgeslagen. 
    * Als validatie faalt, toont onboarding de fout en kun je het opnieuw proberen.


### Niet-interactieve Z.AI-endpointkeuzes

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

Niet-interactief Mistral-voorbeeld:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## Flow-opmerkingen

Flowtypen

  * `quickstart`: minimale prompts, genereert automatisch een Gateway-token.
  * `manual`: volledige prompts voor poort, bind en authenticatie (alias van `advanced`).
  * `import`: voert een gedetecteerde migratieprovider uit, toont een preview van het plan en past het daarna na bevestiging toe.

Providervoorfiltering

Wanneer een auth-keuze een voorkeursprovider impliceert, filtert onboarding de standaardmodel- en allowlist-kiezers vooraf op die provider. Voor Volcengine en BytePlus komt dit ook overeen met de coding-plan-varianten (`volcengine-plan/*`, `byteplus-plan/*`).

Als de voorkeursproviderfilter nog geen geladen modellen oplevert, valt onboarding terug op de ongefilterde catalogus in plaats van de kiezer leeg te laten.

Vervolgprompts voor webzoekopdrachten

Sommige webzoekproviders activeren providerspecifieke vervolgprompts:

  * **Grok** kan optionele `x_search`-configuratie aanbieden met dezelfde `XAI_API_KEY` en een `x_search`-modelkeuze.
  * **Kimi** kan vragen naar de Moonshot API-regio (`api.moonshot.ai` versus `api.moonshot.cn`) en het standaard Kimi-webzoekmodel.

Ander gedrag

  * DM-scopegedrag van lokale onboarding: [CLI-configuratiereferentie](</nl/start/wizard-cli-reference#outputs-and-internals>).
  * Snelste eerste chat: `openclaw dashboard` (Control UI, geen kanaalconfiguratie).
  * Aangepaste provider: verbind elk OpenAI- of Anthropic-compatibel endpoint, inclusief gehoste providers die niet worden vermeld. Gebruik Unknown voor automatische detectie.
  * Als Hermes-status wordt gedetecteerd, biedt onboarding een migratieflow aan. Gebruik [Migreren](</nl/cli/migrate>) voor dry-run-plannen, overschrijfmodus, rapporten en exacte mappings.


## Veelgebruikte vervolgcommando's

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

Gebruik in plaats daarvan `openclaw setup` wanneer je alleen de basisconfiguratie/werkruimte nodig hebt. Gebruik later `openclaw configure` voor gerichte wijzigingen en `openclaw channels add` voor configuratie van alleen kanalen.

Was this useful?YesNo