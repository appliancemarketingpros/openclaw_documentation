---
title: Vydra
source_url: https://docs.openclaw.ai/nl/providers/vydra
scraped_at: 2026-05-25
---

De gebundelde Vydra-plugin voegt toe:

  * Afbeeldingen genereren via `vydra/grok-imagine`
  * Video's genereren via `vydra/veo3` en `vydra/kling`
  * Spraaksynthese via Vydra's door ElevenLabs ondersteunde TTS-route


OpenClaw gebruikt dezelfde `VYDRA_API_KEY` voor alle drie mogelijkheden.

Eigenschap | Waarde  
---|---  
Provider-id | `vydra`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `VYDRA_API_KEY`  
Onboarding-flag | `--auth-choice vydra-api-key`  
Directe CLI-flag | `--vydra-api-key <key>`  
Contracten | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
Basis-URL | `https://www.vydra.ai/api/v1` (gebruik de `www`-host)  
  
## Instellen

* ### Voer interactieve onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Of stel de env-var direct in:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Kies een standaardmogelijkheid

Kies een of meer van de onderstaande mogelijkheden (afbeelding, video of spraak) en pas de bijbehorende configuratie toe.

## Mogelijkheden

Afbeeldingen genereren

Standaard afbeeldingsmodel:

  * `vydra/grok-imagine`


Stel dit in als de standaard afbeeldingsprovider:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

De huidige gebundelde ondersteuning is alleen tekst-naar-afbeelding. Vydra's gehoste bewerkingsroutes verwachten externe afbeeldings-URL's, en OpenClaw voegt nog geen Vydra-specifieke uploadbrug toe in de gebundelde plugin.

Video's genereren

Geregistreerde videomodellen:

  * `vydra/veo3` voor tekst-naar-video
  * `vydra/kling` voor afbeelding-naar-video


Stel Vydra in als de standaard videoprovider:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Opmerkingen:

  * `vydra/veo3` is alleen als tekst-naar-video gebundeld.
  * `vydra/kling` vereist momenteel een externe afbeeldings-URL-referentie. Lokale bestandsuploads worden vooraf geweigerd.
  * Vydra's huidige `kling`-HTTP-route is inconsistent geweest over de vraag of `image_url` of `video_url` vereist is; de gebundelde provider koppelt dezelfde externe afbeeldings-URL aan beide velden.
  * De gebundelde plugin blijft conservatief en stuurt geen ongedocumenteerde stijlknoppen door, zoals beeldverhouding, resolutie, watermerk of gegenereerde audio.

Video-live-tests

Provider-specifieke live-dekking:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Het gebundelde Vydra-livebestand dekt nu:

  * `vydra/veo3` tekst-naar-video
  * `vydra/kling` afbeelding-naar-video met een externe afbeeldings-URL


Overschrijf de externe afbeeldingsfixture wanneer nodig:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Spraaksynthese

Stel Vydra in als spraakprovider:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Standaardwaarden:

  * Model: `elevenlabs/tts`
  * Stem-id: `21m00Tcm4TlvDq8ikWAM`


De gebundelde plugin biedt momenteel een bekende, goed werkende standaardstem en retourneert MP3-audiobestanden.

## Gerelateerd

[**Providerdirectory** Blader door alle beschikbare providers. ](</nl/providers>) [**Afbeeldingen genereren** Gedeelde afbeeldings-toolparameters en providerselectie. ](</nl/tools/image-generation>) [**Video's genereren** Gedeelde video-toolparameters en providerselectie. ](</nl/tools/video-generation>) [**Configuratiereferentie** Agentstandaarden en modelconfiguratie. ](</nl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo