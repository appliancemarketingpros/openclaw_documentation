---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/nl/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud wordt als gebundelde provider-Plugin in OpenClaw geleverd. Het geeft toegang tot Tencent Hy3 preview via het TokenHub-eindpunt (`tencent-tokenhub`) met een OpenAI-compatibele API.

Eigenschap | Waarde  
---|---  
Provider-id | `tencent-tokenhub`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `TOKENHUB_API_KEY`  
Onboarding-vlag | `--auth-choice tokenhub-api-key`  
Directe CLI-vlag | `--tokenhub-api-key <key>`  
API | OpenAI-compatibel (`openai-completions`)  
Standaard basis-URL | `https://tokenhub.tencentmaas.com/v1`  
Globale basis-URL | `https://tokenhub-intl.tencentmaas.com/v1` (override)  
Standaardmodel | `tencent-tokenhub/hy3-preview`  
  
## Snelle start

* ### Een TokenHub-API-sleutel aanmaken

Maak een API-sleutel aan in Tencent Cloud TokenHub. Als je een beperkte toegangsscope voor de sleutel kiest, neem dan **Hy3 preview** op in de toegestane modellen.

* ### Onboarding uitvoeren

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Het model verifiëren

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Niet-interactieve configuratie

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Ingebouwde catalogus

Model-ref | Naam | Invoer | Context | Maximale uitvoer | Opmerkingen  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | tekst | 256,000 | 64,000 | Standaard; reasoning-enabled  
  
Hy3 preview is het grote MoE-taalmodel van Tencent Hunyuan voor redeneren, instructies volgen met lange context, code en agentworkflows. De OpenAI-compatibele voorbeelden van Tencent gebruiken `hy3-preview` als model-id en ondersteunen standaard toolaanroepen voor chat-completions plus `reasoning_effort`.

## Gelaagde prijzen

De gebundelde catalogus levert gelaagde kostenmetadata die schaalt met de lengte van het invoervenster, zodat kostenschattingen worden ingevuld zonder handmatige overrides.

Bereik invoertokens | Invoertarief | Uitvoertarief | Cache-lezen  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Tarieven zijn per miljoen tokens in USD zoals geadverteerd door Tencent. Overschrijf prijzen onder `models.providers.tencent-tokenhub` alleen wanneer je een ander oppervlak nodig hebt.

## Geavanceerde configuratie

Eindpunt-override

OpenClaw gebruikt standaard het eindpunt `https://tokenhub.tencentmaas.com/v1` van Tencent Cloud. Tencent documenteert ook een internationaal TokenHub-eindpunt:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Overschrijf het eindpunt alleen wanneer je TokenHub-account of regio dit vereist.

Beschikbaarheid van de omgeving voor de daemon

Als de Gateway als beheerde service draait (launchd, systemd, Docker), moet `TOKENHUB_API_KEY` zichtbaar zijn voor dat proces. Stel deze in `~/.openclaw/.env` of via `env.shellEnv` in, zodat launchd-, systemd- of Docker exec-omgevingen deze kunnen lezen.

## Gerelateerd

[**Modelproviders** Providers, model-refs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledig configuratieschema, inclusief providerinstellingen. ](</nl/gateway/configuration>) [**Tencent TokenHub** De TokenHub-productpagina van Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Hy3 preview-modelkaart** Details en benchmarks van Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo