---
title: DeepInfra
source_url: https://docs.openclaw.ai/nl/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra biedt een **uniforme API** die verzoeken naar de populairste open-source- en frontiermodellen routeert achter één endpoint en API-sleutel. Deze is OpenAI-compatibel, dus de meeste OpenAI-SDK's werken door de basis-URL te wijzigen.

## Een API-sleutel verkrijgen

  1. Ga naar <https://deepinfra.com/>
  2. Meld je aan of maak een account aan
  3. Navigeer naar Dashboard / Sleutels en genereer een nieuwe API-sleutel of gebruik de automatisch aangemaakte sleutel


## CLI-configuratie

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Of stel de omgevingsvariabele in:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Configuratiefragment

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Ondersteunde OpenClaw-interfaces

De gebundelde Plugin registreert alle DeepInfra-interfaces die overeenkomen met de huidige OpenClaw-providercontracten:

Interface | Standaardmodel | OpenClaw-configuratie/tool  
---|---|---  
Chat / modelprovider | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Afbeeldingen genereren/bewerken | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Mediabegrip | `moonshotai/Kimi-K2.5` voor afbeeldingen | begrip van inkomende afbeeldingen  
Spraak-naar-tekst | `openai/whisper-large-v3-turbo` | transcriptie van inkomende audio  
Tekst-naar-spraak | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Video genereren | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Geheugen-embeddings | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra biedt ook reranking, classificatie, objectdetectie en andere native modeltypen. OpenClaw heeft momenteel geen eersteklas providercontracten voor die categorieën, dus deze Plugin registreert ze nog niet.

## Beschikbare modellen

OpenClaw ontdekt beschikbare DeepInfra-modellen dynamisch bij het opstarten. Gebruik `/models deepinfra` om de volledige lijst met beschikbare modellen te zien.

Elk model dat beschikbaar is op [DeepInfra.com](<https://deepinfra.com/>) kan worden gebruikt met het voorvoegsel `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...en nog veel meer
[/code]

## Opmerkingen

  * Modelverwijzingen zijn `deepinfra/<provider>/<model>` (bijv. `deepinfra/Qwen/Qwen3-Max`).
  * Standaardmodel: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * Basis-URL: `https://api.deepinfra.com/v1/openai`
  * Native videogeneratie gebruikt `https://api.deepinfra.com/v1/inference/<model>`.


## Gerelateerd

  * [Modelproviders](</nl/concepts/model-providers>)
  * [Alle providers](</nl/providers>)


Was this useful?YesNo