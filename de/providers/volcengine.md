---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/de/providers/volcengine
scraped_at: 2026-05-25
---

Der Volcengine-Provider bietet Zugriff auf Doubao-Modelle und Drittanbieter-Modelle, die auf Volcano Engine gehostet werden, mit separaten Endpunkten für allgemeine und Coding- Workloads. Dasselbe gebündelte Plugin kann auch Volcengine Speech als TTS- Provider registrieren.

Detail | Wert  
---|---  
Provider | `volcengine` (allgemein + TTS) + `volcengine-plan` (Coding)  
Modell-Auth | `VOLCANO_ENGINE_API_KEY`  
TTS-Auth | `VOLCENGINE_TTS_API_KEY` oder `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | OpenAI-kompatible Modelle, BytePlus Seed Speech TTS  
  
## Erste Schritte

* ### Set the API key

Führen Sie das interaktive Onboarding aus:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Dadurch werden sowohl der allgemeine Provider (`volcengine`) als auch der Coding-Provider (`volcengine-plan`) mit einem einzigen API-Schlüssel registriert.

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Provider und Endpunkte

Provider | Endpunkt | Anwendungsfall  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Allgemeine Modelle  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Coding-Modelle  
  
## Integrierter Katalog

### General (volcengine)

Modell-Ref | Name | Eingabe | Kontext  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | Text, Bild | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | Text, Bild | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | Text, Bild | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | Text, Bild | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | Text, Bild | 128,000  
  
### Coding (volcengine-plan)

Modell-Ref | Name | Eingabe | Kontext  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | Text | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | Text | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | Text | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | Text | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | Text | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | Text | 256,000  
  
## Text-to-Speech

Volcengine TTS verwendet die BytePlus Seed Speech HTTP API und wird getrennt vom OpenAI-kompatiblen Doubao-Modell-API-Schlüssel konfiguriert. Öffnen Sie in der BytePlus- Konsole Seed Speech > Settings > API Keys und kopieren Sie den API-Schlüssel. Setzen Sie dann:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Aktivieren Sie es dann in `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Für Voice-Note-Ziele fordert OpenClaw von Volcengine das providernative `ogg_opus` an. Für normale Audioanhänge fordert es `mp3` an. Die Provider-Aliase `bytedance` und `doubao` werden ebenfalls auf denselben Speech-Provider aufgelöst.

Die Standard-Resource-ID ist `seed-tts-1.0`, weil BytePlus diese neu erstellten Seed-Speech-API-Schlüsseln im Standardprojekt zuweist. Wenn Ihr Projekt eine TTS-2.0-Berechtigung hat, setzen Sie `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

Alte AppID-/Token-Authentifizierung bleibt für ältere Speech-Console-Anwendungen unterstützt:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Erweiterte Konfiguration

Default model after onboarding

`openclaw onboard --auth-choice volcengine-api-key` setzt derzeit `volcengine-plan/ark-code-latest` als Standardmodell und registriert gleichzeitig den allgemeinen Katalog `volcengine`.

Model picker fallback behavior

Während der Modellauswahl beim Onboarding/Konfigurieren bevorzugt die Volcengine-Auth-Auswahl sowohl Zeilen `volcengine/*` als auch `volcengine-plan/*`. Wenn diese Modelle noch nicht geladen sind, greift OpenClaw auf den ungefilterten Katalog zurück, anstatt einen leeren providerbezogenen Picker anzuzeigen.

Environment variables for daemon processes

Wenn das Gateway als Daemon läuft (launchd/systemd), stellen Sie sicher, dass Modell- und TTS- Umgebungsvariablen wie `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` und `VOLCENGINE_TTS_TOKEN` diesem Prozess zur Verfügung stehen (zum Beispiel in `~/.openclaw/.env` oder über `env.shellEnv`).

## Verwandt

[**Model selection** Auswahl von Providern, Modell-Refs und Failover-Verhalten. ](</de/concepts/model-providers>) [**Configuration** Vollständige Konfigurationsreferenz für Agenten, Modelle und Provider. ](</de/gateway/configuration>) [**Troubleshooting** Häufige Probleme und Schritte zur Fehlerbehebung. ](</de/help/troubleshooting>) [**FAQ** Häufig gestellte Fragen zum OpenClaw-Setup. ](</de/help/faq>)

Was this useful?YesNo