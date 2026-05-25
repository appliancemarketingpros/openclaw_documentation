---
title: Chutes
source_url: https://docs.openclaw.ai/de/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) stellt Open-Source-Modellkataloge über eine OpenAI-kompatible API bereit. OpenClaw unterstützt sowohl Browser-OAuth als auch direkte API-Schlüssel- Authentifizierung für den gebündelten `chutes`-Provider.

Eigenschaft | Wert  
---|---  
Provider | `chutes`  
API | OpenAI-kompatibel  
Basis-URL | `https://llm.chutes.ai/v1`  
Auth | OAuth oder API-Schlüssel (siehe unten)  
  
## Erste Schritte

### OAuth

* ### OAuth-Onboarding-Ablauf ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw startet den Browser-Ablauf lokal oder zeigt auf Remote-/Headless-Hosts einen Ablauf mit URL und Einfügen der Weiterleitung an. OAuth-Token werden automatisch über OpenClaw-Auth- Profile aktualisiert.

* ### Standardmodell überprüfen

Nach dem Onboarding ist das Standardmodell auf `chutes/zai-org/GLM-4.7-TEE` gesetzt und der gebündelte Chutes-Katalog ist registriert.

### API-Schlüssel

* ### API-Schlüssel abrufen

Erstellen Sie einen Schlüssel unter [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### API-Schlüssel-Onboarding-Ablauf ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Standardmodell überprüfen

Nach dem Onboarding ist das Standardmodell auf `chutes/zai-org/GLM-4.7-TEE` gesetzt und der gebündelte Chutes-Katalog ist registriert.

## Discovery-Verhalten

Wenn Chutes-Auth verfügbar ist, fragt OpenClaw den Chutes-Katalog mit diesen Anmeldedaten ab und verwendet die gefundenen Modelle. Wenn die Discovery fehlschlägt, greift OpenClaw auf einen gebündelten statischen Katalog zurück, sodass Onboarding und Start weiterhin funktionieren.

## Standard-Aliasse

OpenClaw registriert drei praktische Aliasse für den gebündelten Chutes-Katalog:

Alias | Zielmodell  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Integrierter Starterkatalog

Der gebündelte Fallback-Katalog enthält aktuelle Chutes-Refs:

Modell-Ref  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Config-Beispiel

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth-Überschreibungen

Sie können den OAuth-Ablauf mit optionalen Umgebungsvariablen anpassen:

Variable | Zweck  
---|---  
`CHUTES_CLIENT_ID` | Benutzerdefinierte OAuth-Client-ID  
`CHUTES_CLIENT_SECRET` | Benutzerdefiniertes OAuth-Client-Secret  
`CHUTES_OAUTH_REDIRECT_URI` | Benutzerdefinierte Weiterleitungs-URI  
`CHUTES_OAUTH_SCOPES` | Benutzerdefinierte OAuth-Scopes  
  
Informationen zu Anforderungen für Weiterleitungs-Apps und Hilfe finden Sie in der [Chutes-OAuth-Dokumentation](<https://chutes.ai/docs/sign-in-with-chutes/overview>).

Hinweise

  * API-Schlüssel- und OAuth-Discovery verwenden beide dieselbe `chutes`-Provider-ID.
  * Chutes-Modelle werden als `chutes/<model-id>` registriert.
  * Wenn die Discovery beim Start fehlschlägt, wird automatisch der gebündelte statische Katalog verwendet.


## Verwandte Themen

[**Modellauswahl** Provider-Regeln, Modell-Refs und Failover-Verhalten. ](</de/concepts/model-providers>) [**Config-Referenz** Vollständiges Config-Schema einschließlich Provider-Einstellungen. ](</de/gateway/configuration-reference>) [**Chutes** Chutes-Dashboard und API-Dokumentation. ](<https://chutes.ai>) [**Chutes-API-Schlüssel** Chutes-API-Schlüssel erstellen und verwalten. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo