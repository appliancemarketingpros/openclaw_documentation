---
title: Groq
source_url: https://docs.openclaw.ai/de/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) bietet ultraschnelle Inferenz für Open-Weight-Modelle (Llama, Gemma, Kimi, Qwen, GPT OSS und mehr) mit eigener LPU-Hardware. OpenClaw enthält ein gebündeltes Groq-Plugin, das sowohl einen OpenAI-kompatiblen Chat-Provider als auch einen Audio-Medienverständnis-Provider registriert.

Eigenschaft | Wert  
---|---  
Provider-ID | `groq`  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Umgebungsvariable | `GROQ_API_KEY`  
Onboarding-Flag | `--auth-choice groq-api-key`  
API | OpenAI-kompatibel (`openai-completions`)  
Basis-URL | `https://api.groq.com/openai/v1`  
Audio-Transkription | `whisper-large-v3-turbo` (Standard)  
Empfohlener Chat-Standardwert | `groq/llama-3.3-70b-versatile`  
  
## Erste Schritte

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel unter [console.groq.com/keys](<https://console.groq.com/keys>).

* ### API-Schlüssel festlegen

OnboardingCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

Nur UmgebungCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Erreichbarkeit des Katalogs prüfen

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Beispiel für eine Konfigurationsdatei

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Integrierter Katalog

OpenClaw liefert einen manifestgestützten Groq-Katalog mit Einträgen für Reasoning und ohne Reasoning aus. Führen Sie `openclaw models list --provider groq` aus, um die gebündelten Zeilen für Ihre installierte Version anzuzeigen, oder prüfen Sie [console.groq.com/docs/models](<https://console.groq.com/docs/models>) für die maßgebliche Liste von Groq.

Modellreferenz | Name | Reasoning | Eingabe | Kontext  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | nein | Text | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | nein | Text | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | nein | Text + Bild | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | nein | Text + Bild | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | nein | Text | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | nein | Text | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | nein | Text | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | nein | Text | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | nein | Text | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | nein | Text | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | ja | Text | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | ja | Text | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | ja | Text | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | ja | Text | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | ja | Text | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | ja | Text | 131,072  
`groq/groq/compound` | Compound | ja | Text | 131,072  
`groq/groq/compound-mini` | Compound Mini | ja | Text | 131,072  
  
## Reasoning-Modelle

OpenClaw ordnet seine gemeinsamen `/think`-Stufen den modellspezifischen `reasoning_effort`-Werten von Groq zu:

  * Für `qwen/qwen3-32b` sendet deaktiviertes Denken `none` und aktiviertes Denken `default`.
  * Für Groq GPT OSS-Reasoning-Modelle (`openai/gpt-oss-*`) sendet OpenClaw je nach `/think`-Stufe `low`, `medium` oder `high`. Bei deaktiviertem Denken wird `reasoning_effort` ausgelassen, da diese Modelle keinen deaktivierten Wert unterstützen.
  * DeepSeek R1 Distill, Qwen QwQ und Compound verwenden die native Reasoning-Oberfläche von Groq; `/think` steuert die Sichtbarkeit, aber das Modell führt immer Reasoning aus.


Siehe [Denkmodi](</de/tools/thinking>) für die gemeinsamen `/think`-Stufen und wie OpenClaw sie pro Provider übersetzt.

## Audio-Transkription

Das gebündelte Plugin von Groq registriert außerdem einen **Audio-Medienverständnis-Provider** , sodass Sprachnachrichten über die gemeinsame Oberfläche `tools.media.audio` transkribiert werden können.

Eigenschaft | Wert  
---|---  
Gemeinsamer Konfigurationspfad | `tools.media.audio`  
Standard-Basis-URL | `https://api.groq.com/openai/v1`  
Standardmodell | `whisper-large-v3-turbo`  
Automatische Priorität | 20  
API-Endpunkt | OpenAI-kompatibel `/audio/transcriptions`  
  
So machen Sie Groq zum Standard-Audio-Backend:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Umgebungsverfügbarkeit für den Daemon

Wenn der Gateway als verwalteter Dienst (launchd, systemd, Docker) läuft, muss `GROQ_API_KEY` für diesen Prozess sichtbar sein, nicht nur für Ihre interaktive Shell.

Benutzerdefinierte Groq-Modell-IDs

OpenClaw akzeptiert zur Laufzeit jede Groq-Modell-ID. Verwenden Sie die exakte von Groq angezeigte ID und stellen Sie ihr `groq/` voran. Der gebündelte Katalog deckt die gängigen Fälle ab; nicht katalogisierte IDs fallen auf die standardmäßige OpenAI-kompatible Vorlage zurück.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## Verwandte Themen

[**Modell-Provider** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Denkmodi** Reasoning-Aufwandsstufen und Interaktion mit Provider-Richtlinien. ](</de/tools/thinking>) [**Konfigurationsreferenz** Vollständiges Konfigurationsschema einschließlich Provider- und Audio-Einstellungen. ](</de/gateway/configuration-reference>) [**Groq Console** Groq-Dashboard, API-Dokumentation und Preise. ](<https://console.groq.com>)

Was this useful?YesNo