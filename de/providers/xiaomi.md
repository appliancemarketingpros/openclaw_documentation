---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/de/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo ist die API-Plattform für **MiMo** -Modelle. OpenClaw enthält ein gebündeltes `xiaomi`-Plugin, das sowohl einen OpenAI-kompatiblen Chat-Provider als auch einen Sprach-Provider (TTS) mit demselben `XIAOMI_API_KEY` registriert.

Eigenschaft | Wert  
---|---  
Provider-ID | `xiaomi`  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Env-Var | `XIAOMI_API_KEY`  
Onboarding-Flag | `--auth-choice xiaomi-api-key`  
Direkte CLI-Flag | `--xiaomi-api-key <key>`  
Verträge | Chat-Completions + `speechProviders`  
API | OpenAI-kompatibel (`openai-completions`)  
Basis-URL | `https://api.xiaomimimo.com/v1`  
Standardmodell | `xiaomi/mimo-v2-flash`  
TTS-Standard | `mimo-v2.5-tts`, Stimme `mimo_default`  
  
## Erste Schritte

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel in der [Xiaomi MiMo-Konsole](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Oder übergeben Sie den Schlüssel direkt:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Verfügbarkeit des Modells prüfen

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Integrierter Katalog

Modell-Ref | Eingabe | Kontext | Maximale Ausgabe | Reasoning | Hinweise  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | Text | 262.144 | 8.192 | Nein | Standardmodell  
`xiaomi/mimo-v2-pro` | Text | 1.048.576 | 32.000 | Ja | Großer Kontext  
`xiaomi/mimo-v2-omni` | Text, Bild | 262.144 | 32.000 | Ja | Multimodal  
  
## Text-to-Speech

Das gebündelte `xiaomi`-Plugin registriert Xiaomi MiMo außerdem als Sprach-Provider für `messages.tts`. Es ruft Xiaomis Chat-Completions-TTS-Vertrag mit dem Text als `assistant`-Nachricht und optionalen Stilvorgaben als `user`-Nachricht auf.

Eigenschaft | Wert  
---|---  
TTS-ID | `xiaomi` (`mimo`-Alias)  
Auth | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` mit `audio`  
Standard | `mimo-v2.5-tts`, Stimme `mimo_default`  
Ausgabe | Standardmäßig MP3; WAV bei entsprechender Konfiguration  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Zu den unterstützten integrierten Stimmen gehören `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` und `Dean`. `mimo-v2-tts` wird für ältere MiMo- TTS-Konten unterstützt; der Standard verwendet das aktuelle MiMo-V2.5-TTS-Modell. Für Sprachnotiz- Ziele wie Feishu und Telegram transkodiert OpenClaw die Xiaomi-Ausgabe vor der Zustellung mit `ffmpeg` in 48-kHz-Opus.

## Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Verhalten bei automatischer Injektion

Der `xiaomi`-Provider wird automatisch injiziert, wenn `XIAOMI_API_KEY` in Ihrer Umgebung gesetzt ist oder ein Auth-Profil vorhanden ist. Sie müssen den Provider nicht manuell konfigurieren, es sei denn, Sie möchten Modellmetadaten oder die Basis-URL überschreiben.

Modelldetails

  * **mimo-v2-flash** — leichtgewichtig und schnell, ideal für allgemeine Textaufgaben. Keine Reasoning-Unterstützung.
  * **mimo-v2-pro** — unterstützt Reasoning mit einem Kontextfenster von 1 Mio. Token für Workloads mit langen Dokumenten.
  * **mimo-v2-omni** — Reasoning-fähiges multimodales Modell, das sowohl Text- als auch Bildeingaben akzeptiert.

Fehlerbehebung

  * Wenn Modelle nicht angezeigt werden, bestätigen Sie, dass `XIAOMI_API_KEY` gesetzt und gültig ist.
  * Wenn der Gateway als Daemon ausgeführt wird, stellen Sie sicher, dass der Schlüssel für diesen Prozess verfügbar ist (zum Beispiel in `~/.openclaw/.env` oder über `env.shellEnv`).


## Verwandte Themen

[**Modellauswahl** Provider, Modell-Refs und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständige OpenClaw-Konfigurationsreferenz. ](</de/gateway/configuration-reference>) [**Xiaomi MiMo-Konsole** Xiaomi MiMo-Dashboard und API-Schlüsselverwaltung. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo