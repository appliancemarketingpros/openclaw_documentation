---
title: LongCat
source_url: https://docs.openclaw.ai/nl/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) biedt een gehoste API voor LongCat-2.0, een redeneermodel dat is ontwikkeld voor programmeer- en agentische workloads. OpenClaw biedt de officiële `longcat`-Plugin voor het OpenAI-compatibele eindpunt van LongCat.

Eigenschap | Waarde  
---|---  
Provider | `longcat`  
Authenticatie | `LONGCAT_API_KEY`  
API | OpenAI-compatibele Chat Completions  
Basis-URL | `https://api.longcat.chat/openai`  
Model | `longcat/LongCat-2.0`  
Context | 1.048.576 tokens  
Maximale uitvoer | 131.072 tokens  
Invoer | Tekst  
  
## Plugin installeren

Installeer het officiële pakket en start daarna de Gateway opnieuw:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Aan de slag

* ### Een API-sleutel maken

Meld u aan bij het [LongCat API-platform](<https://longcat.chat/platform/>) en maak een sleutel aan op de pagina [API Keys](<https://longcat.chat/platform/api_keys>).

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Het model verifiëren

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

Onboarding voegt de gehoste catalogus toe en selecteert `longcat/LongCat-2.0` als er nog geen primair model is geconfigureerd.

### Niet-interactieve configuratie

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Redeneergedrag

LongCat biedt binaire besturing van het denkproces. OpenClaw koppelt ingeschakelde denkniveaus aan `thinking: { type: "enabled" }` en `/think off` aan `thinking: { type: "disabled" }`. LongCat documenteert momenteel geen `reasoning_effort`, dus OpenClaw verzendt dit niet.

LongCat retourneert redeneringen in `reasoning_content`. OpenClaw behoudt dit veld bij het opnieuw afspelen van assistentbeurten met toolaanroepen, zodat agentsessies met meerdere beurten de door de provider verwachte berichtstructuur behouden.

## Prijzen

De ingebouwde catalogus gebruikt de pay-as-you-go-lijstprijzen van LongCat in USD per miljoen tokens: $0,75 voor niet-gecachete invoer, $0,015 voor gecachete invoer en $2,95 voor uitvoer. LongCat kan tijdelijke kortingen aanbieden; de [prijzenpagina](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) en uw facturatiegegevens zijn leidend.

## Zelfgehoste LongCat-2.0

De `longcat`-provider is bedoeld voor de gehoste API van LongCat. Voor de open gewichten op [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>) stelt u het model beschikbaar via een OpenAI-compatibele runtime en gebruikt u in plaats daarvan de bestaande [vLLM](</nl/providers/vllm>)\- of [SGLang](</nl/providers/sglang>)-provider van OpenClaw.

Behoud de exacte model-ID van de runtime in de catalogus van de zelfgehoste provider; routeer een lokale implementatie niet via `longcat/LongCat-2.0`.

## Problemen oplossen

De sleutel werkt in een shell, maar niet in de Gateway

Door een daemon beheerde Gateway-processen nemen niet alle variabelen uit een interactieve shell over. Plaats `LONGCAT_API_KEY` in `~/.openclaw/.env`, configureer deze via onboarding of gebruik een goedgekeurde geheimverwijzing.

Aanvragen mislukken met 402 of 429

`402` betekent dat het account onvoldoende tokenquotum heeft. `429` betekent dat de API- sleutel een snelheidslimiet heeft bereikt. Controleer het [LongCat-verbruik](<https://longcat.chat/platform/usage>) en probeer aanvragen met een snelheidsbeperking opnieuw na de back-offperiode van de provider.

Het model wordt niet weergegeven

Voer `openclaw plugins list` uit en bevestig dat de `longcat`-Plugin is ingeschakeld. Voer daarna `openclaw models list --provider longcat` uit.

## Gerelateerd

[**Modelproviders** Providerconfiguratie, modelverwijzingen en failovergedrag. ](</nl/concepts/model-providers>) [**LongCat API-documentatie** Gehoste API-eindpunten, authenticatie, limieten en voorbeelden. ](<https://longcat.chat/platform/docs/>) [**LongCat-2.0-modelkaart** Architectuur, implementatierichtlijnen en modeldetails. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Geheimen** Sla providerreferenties op zonder platte tekst in de configuratie op te nemen. ](</nl/gateway/secrets>)

Was this useful?YesNo

Open issue