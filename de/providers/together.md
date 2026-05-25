---
title: Together AI
source_url: https://docs.openclaw.ai/de/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) bietet Zugriff auf führende Open-Source- Modelle wie Llama, DeepSeek, Kimi und weitere über eine einheitliche API.

Eigenschaft | Wert  
---|---  
Provider | `together`  
Auth | `TOGETHER_API_KEY`  
API | OpenAI-kompatibel  
Basis-URL | `https://api.together.xyz/v1`  
  
## Erste Schritte

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel unter [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Nicht interaktives Beispiel

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Integrierter Katalog

OpenClaw liefert diesen gebündelten Together-Katalog mit:

Modellreferenz | Name | Eingabe | Kontext | Hinweise  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | Text, Bild | 262,144 | Standardmodell; Reasoning aktiviert  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | Text | 202,752 | Allzweck-Textmodell  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | Text | 131,072 | Schnelles Instruktionsmodell  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | Text, Bild | 10,000,000 | Multimodal  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | Text, Bild | 20,000,000 | Multimodal  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | Text | 131,072 | Allgemeines Textmodell  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | Text | 131,072 | Reasoning-Modell  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | Text | 262,144 | Sekundäres Kimi-Textmodell  
  
## Videogenerierung

Das gebündelte `together`-Plugin registriert außerdem Videogenerierung über das gemeinsame Tool `video_generate`.

Eigenschaft | Wert  
---|---  
Standard-Videomodell | `together/Wan-AI/Wan2.2-T2V-A14B`  
Modi | Text-zu-Video, Einzelbildreferenz  
Unterstützte Parameter | `aspectRatio`, `resolution`  
  
So verwenden Sie Together als Standard-Provider für Video:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Hinweis zur Umgebung

Wenn der Gateway als Daemon läuft (launchd/systemd), stellen Sie sicher, dass `TOGETHER_API_KEY` für diesen Prozess verfügbar ist (zum Beispiel in `~/.openclaw/.env` oder über `env.shellEnv`).

Fehlerbehebung

  * Prüfen Sie, ob Ihr Schlüssel funktioniert: `openclaw models list --provider together`
  * Wenn Modelle nicht angezeigt werden, bestätigen Sie, dass der API-Schlüssel in der richtigen Umgebung für Ihren Gateway-Prozess gesetzt ist.
  * Modellreferenzen verwenden die Form `together/<model-id>`.


## Verwandte Themen

[**Modellauswahl** Provider-Regeln, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Videogenerierung** Gemeinsame Videogenerierungs-Tool-Parameter und Provider-Auswahl. ](</de/tools/video-generation>) [**Konfigurationsreferenz** Vollständiges Konfigurationsschema einschließlich Provider-Einstellungen. ](</de/gateway/configuration-reference>) [**Together AI** Together AI-Dashboard, API-Dokumentation und Preise. ](<https://together.ai>)

Was this useful?YesNo