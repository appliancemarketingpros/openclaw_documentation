---
title: DeepInfra
source_url: https://docs.openclaw.ai/de/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra stellt eine **einheitliche API** bereit, die Anfragen an die beliebtesten Open-Source- und Frontier-Modelle hinter einem einzigen Endpunkt und API-Schlüssel weiterleitet. Sie ist OpenAI-kompatibel, sodass die meisten OpenAI-SDKs funktionieren, indem die Basis-URL geändert wird.

## API-Schlüssel abrufen

  1. Gehen Sie zu <https://deepinfra.com/>
  2. Melden Sie sich an oder erstellen Sie ein Konto
  3. Navigieren Sie zu Dashboard / Keys und generieren Sie einen neuen API-Schlüssel oder verwenden Sie den automatisch erstellten


## CLI-Einrichtung

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Oder setzen Sie die Umgebungsvariable:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Konfigurationsausschnitt

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Unterstützte OpenClaw-Oberflächen

Das gebündelte Plugin registriert alle DeepInfra-Oberflächen, die den aktuellen OpenClaw-Provider-Verträgen entsprechen:

Oberfläche | Standardmodell | OpenClaw-Konfiguration/-Tool  
---|---|---  
Chat / Modell-Provider | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Bilderzeugung/-bearbeitung | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Medienverständnis | `moonshotai/Kimi-K2.5` for images | Eingehendes Bildverständnis  
Speech-to-Text | `openai/whisper-large-v3-turbo` | Eingehende Audiotranskription  
Text-to-Speech | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Videogenerierung | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Memory-Einbettungen | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra stellt außerdem Reranking, Klassifizierung, Objekterkennung und andere native Modelltypen bereit. OpenClaw verfügt derzeit nicht über erstklassige Provider-Verträge für diese Kategorien, daher registriert dieses Plugin sie noch nicht.

## Verfügbare Modelle

OpenClaw erkennt verfügbare DeepInfra-Modelle beim Start dynamisch. Verwenden Sie `/models deepinfra`, um die vollständige Liste der verfügbaren Modelle anzuzeigen.

Jedes auf [DeepInfra.com](<https://deepinfra.com/>) verfügbare Modell kann mit dem Präfix `deepinfra/` verwendet werden:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...and many more
[/code]

## Hinweise

  * Modellreferenzen sind `deepinfra/<provider>/<model>` (z. B. `deepinfra/Qwen/Qwen3-Max`).
  * Standardmodell: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * Basis-URL: `https://api.deepinfra.com/v1/openai`
  * Native Videogenerierung verwendet `https://api.deepinfra.com/v1/inference/<model>`.


## Verwandte Themen

  * [Modell-Provider](</de/concepts/model-providers>)
  * [Alle Provider](</de/providers>)


Was this useful?YesNo