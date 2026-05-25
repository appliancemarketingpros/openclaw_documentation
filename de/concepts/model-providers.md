---
title: Modell-Provider
source_url: https://docs.openclaw.ai/de/concepts/model-providers
scraped_at: 2026-05-25
---

Referenz für **LLM-/Modell-Provider** (nicht Chat-Kanäle wie WhatsApp/Telegram). Regeln zur Modellauswahl finden Sie unter [Modelle](</de/concepts/models>).

## Kurzregeln

Modell-Refs und CLI-Hilfsbefehle

  * Modell-Refs verwenden `provider/model` (Beispiel: `opencode/claude-opus-4-6`).
  * `agents.defaults.models` dient als Allowlist, wenn es gesetzt ist.
  * CLI-Hilfsbefehle: `openclaw onboard`, `openclaw models list`, `openclaw models set <provider/model>`.
  * `models.providers.*.contextWindow` / `contextTokens` / `maxTokens` legen Standardwerte auf Provider-Ebene fest; `models.providers.*.models[].contextWindow` / `contextTokens` / `maxTokens` überschreiben sie pro Modell.
  * Fallback-Regeln, Cooldown-Probes und Persistenz von Sitzungs-Overrides: [Modell-Failover](</de/concepts/model-failover>).

Das Hinzufügen von Provider-Auth ändert Ihr primäres Modell nicht

`openclaw configure` behält ein vorhandenes `agents.defaults.model.primary` bei, wenn Sie einen Provider hinzufügen oder erneut authentifizieren. `openclaw models auth login` verhält sich genauso, sofern Sie nicht `--set-default` übergeben. Provider-Plugins können weiterhin ein empfohlenes Standardmodell in ihrem Auth-Konfigurationspatch zurückgeben, aber OpenClaw behandelt dies als „dieses Modell verfügbar machen“, wenn bereits ein primäres Modell existiert, nicht als „das aktuelle primäre Modell ersetzen“.

Um das Standardmodell bewusst zu wechseln, verwenden Sie `openclaw models set <provider/model>` oder `openclaw models auth login --provider <id> --set-default`.

OpenAI-Provider-/Runtime-Trennung

Routen der OpenAI-Familie sind präfixspezifisch:

  * `openai/<model>` verwendet standardmäßig das native Codex-App-Server-Harness für Agent-Turns. Dies ist die übliche Einrichtung für ChatGPT-/Codex-Abonnements.
  * `openai-codex/<model>` ist Legacy-Konfiguration, die doctor zu `openai/<model>` umschreibt.
  * `openai/<model>` plus Provider-/Modell-`agentRuntime.id: "pi"` verwendet PI für explizite API-Key- oder Kompatibilitätsrouten.


Siehe [OpenAI](</de/providers/openai>) und [Codex-Harness](</de/plugins/codex-harness>). Wenn die Provider-/Runtime-Trennung verwirrend ist, lesen Sie zuerst [Agent-Runtimes](</de/concepts/agent-runtimes>).

Die automatische Plugin-Aktivierung folgt derselben Grenze: `openai/*`-Agent-Refs aktivieren das Codex-Plugin für die Standardroute, und explizite Provider-/Modell-`agentRuntime.id: "codex"`\- oder Legacy-`codex/<model>`-Refs benötigen es ebenfalls.

GPT-5.5 ist standardmäßig über das native Codex-App-Server-Harness unter `openai/gpt-5.5` verfügbar und über PI nur dann, wenn die Provider-/Modell-Runtime-Richtlinie explizit `pi` auswählt.

CLI-Runtimes

CLI-Runtimes verwenden dieselbe Trennung: Wählen Sie kanonische Modell-Refs wie `anthropic/claude-*`, `google/gemini-*` oder `openai/gpt-*`, und setzen Sie dann die Provider-/Modell-Runtime-Richtlinie auf `claude-cli`, `google-gemini-cli` oder `codex-cli`, wenn Sie ein lokales CLI-Backend verwenden möchten.

Legacy-Refs `claude-cli/*`, `google-gemini-cli/*` und `codex-cli/*` werden zurück zu kanonischen Provider-Refs migriert, wobei die Runtime separat erfasst wird.

## Plugin-eigenes Provider-Verhalten

Der Großteil der Provider-spezifischen Logik lebt in Provider-Plugins (`registerProvider(...)`), während OpenClaw die generische Inferenzschleife beibehält. Plugins besitzen Onboarding, Modellkataloge, Auth-Env-Var-Mapping, Transport-/Konfigurationsnormalisierung, Tool-Schema-Bereinigung, Failover-Klassifizierung, OAuth-Aktualisierung, Nutzungsberichte, Denk-/Reasoning-Profile und mehr.

Die vollständige Liste der Provider-SDK-Hooks und Beispiele für gebündelte Plugins finden Sie unter [Provider-Plugins](</de/plugins/sdk-provider-plugins>). Ein Provider, der einen vollständig benutzerdefinierten Request-Executor benötigt, ist eine separate, tiefere Erweiterungsfläche.

## API-Key-Rotation

Key-Quellen und Priorität

Konfigurieren Sie mehrere Keys über:

  * `OPENCLAW_LIVE_&lt;PROVIDER&gt;_KEY` (einzelner Live-Override, höchste Priorität)
  * `&lt;PROVIDER&gt;_API_KEYS` (durch Komma oder Semikolon getrennte Liste)
  * `&lt;PROVIDER&gt;_API_KEY` (primärer Key)
  * `&lt;PROVIDER&gt;_API_KEY_*` (nummerierte Liste, z. B. `&lt;PROVIDER&gt;_API_KEY_1`)


Für Google-Provider wird `GOOGLE_API_KEY` ebenfalls als Fallback einbezogen. Die Auswahlreihenfolge der Keys behält die Priorität bei und dedupliziert Werte.

Wann Rotation greift

  * Requests werden nur bei Rate-Limit-Antworten mit dem nächsten Key erneut versucht (zum Beispiel `429`, `rate_limit`, `quota`, `resource exhausted`, `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached`, `workers_ai ... quota limit exceeded` oder periodische Nutzungslimitmeldungen).
  * Fehler ohne Rate-Limit schlagen sofort fehl; es wird keine Key-Rotation versucht.
  * Wenn alle Kandidaten-Keys fehlschlagen, wird der abschließende Fehler aus dem letzten Versuch zurückgegeben.


## Integrierte Provider (pi-ai-Katalog)

OpenClaw wird mit dem pi-ai-Katalog ausgeliefert. Diese Provider benötigen **keine** `models.providers`-Konfiguration; setzen Sie einfach Auth und wählen Sie ein Modell.

### OpenAI

  * Provider: `openai`
  * Auth: `OPENAI_API_KEY`
  * Optionale Rotation: `OPENAI_API_KEYS`, `OPENAI_API_KEY_1`, `OPENAI_API_KEY_2` plus `OPENCLAW_LIVE_OPENAI_KEY` (einzelner Override)
  * Beispielmodelle: `openai/gpt-5.5`, `openai/gpt-5.4-mini`
  * Prüfen Sie die Verfügbarkeit von Konto/Modell mit `openclaw models list --provider openai`, wenn eine bestimmte Installation oder ein API-Key sich anders verhält.
  * CLI: `openclaw onboard --auth-choice openai-api-key`
  * Der Standardtransport ist `auto`; OpenClaw übergibt die Transportauswahl an pi-ai.
  * Override pro Modell über `agents.defaults.models["openai/<model>"].params.transport` (`"sse"`, `"websocket"` oder `"auto"`)
  * OpenAI Priority Processing kann über `agents.defaults.models["openai/<model>"].params.serviceTier` aktiviert werden
  * `/fast` und `params.fastMode` ordnen direkte `openai/*`-Responses-Requests `service_tier=priority` auf `api.openai.com` zu
  * Verwenden Sie `params.serviceTier`, wenn Sie statt des gemeinsamen `/fast`-Toggles eine explizite Stufe wünschen
  * Verborgene OpenClaw-Attributionsheader (`originator`, `version`, `User-Agent`) gelten nur für nativen OpenAI-Traffic zu `api.openai.com`, nicht für generische OpenAI-kompatible Proxys
  * Native OpenAI-Routen behalten außerdem Responses `store`, Prompt-Cache-Hinweise und OpenAI-Reasoning-kompatible Payload-Formung bei; Proxy-Routen tun dies nicht
  * `openai/gpt-5.3-codex-spark` wird in OpenClaw absichtlich unterdrückt, weil Live-OpenAI-API-Requests es ablehnen und der aktuelle Codex-Katalog es nicht bereitstellt

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

### Anthropic

  * Provider: `anthropic`
  * Auth: `ANTHROPIC_API_KEY`
  * Optionale Rotation: `ANTHROPIC_API_KEYS`, `ANTHROPIC_API_KEY_1`, `ANTHROPIC_API_KEY_2` plus `OPENCLAW_LIVE_ANTHROPIC_KEY` (einzelner Override)
  * Beispielmodell: `anthropic/claude-opus-4-6`
  * CLI: `openclaw onboard --auth-choice apiKey`
  * Direkte öffentliche Anthropic-Requests unterstützen den gemeinsamen `/fast`-Toggle und `params.fastMode`, einschließlich API-Key- und OAuth-authentifiziertem Traffic, der an `api.anthropic.com` gesendet wird; OpenClaw ordnet dies Anthropic `service_tier` zu (`auto` vs `standard_only`)
  * Die bevorzugte Claude-CLI-Konfiguration hält die Modell-Ref kanonisch und wählt das CLI- Backend separat aus: `anthropic/claude-opus-4-7` mit modellgebundenem `agentRuntime.id: "claude-cli"`. Legacy- `claude-cli/claude-opus-4-7`-Refs funktionieren aus Kompatibilitätsgründen weiterhin.

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### OpenAI Codex OAuth

  * Provider: `openai-codex`
  * Auth: OAuth (ChatGPT)
  * Legacy-PI-Modell-Ref: `openai-codex/gpt-5.5`
  * Native Codex-App-Server-Harness-Ref: `openai/gpt-5.5`
  * Dokumentation zum nativen Codex-App-Server-Harness: [Codex-Harness](</de/plugins/codex-harness>)
  * Legacy-Modell-Refs: `codex/gpt-*`
  * Plugin-Grenze: `openai-codex/*` lädt das OpenAI-Plugin; das native Codex-App-Server-Plugin wird nur durch die Codex-Harness-Runtime oder Legacy-`codex/*`-Refs ausgewählt.
  * CLI: `openclaw onboard --auth-choice openai-codex` oder `openclaw models auth login --provider openai-codex`
  * Der Standardtransport ist `auto` (WebSocket zuerst, SSE-Fallback)
  * Override pro PI-Modell über `agents.defaults.models["openai-codex/<model>"].params.transport` (`"sse"`, `"websocket"` oder `"auto"`)
  * `params.serviceTier` wird außerdem bei nativen Codex-Responses-Requests (`chatgpt.com/backend-api`) weitergeleitet
  * Verborgene OpenClaw-Attributionsheader (`originator`, `version`, `User-Agent`) werden nur bei nativem Codex-Traffic zu `chatgpt.com/backend-api` angehängt, nicht bei generischen OpenAI-kompatiblen Proxys
  * Teilt denselben `/fast`-Toggle und dieselbe `params.fastMode`-Konfiguration wie direkte `openai/*`; OpenClaw ordnet dies `service_tier=priority` zu
  * `openai-codex/gpt-5.5` verwendet das native `contextWindow = 400000` des Codex-Katalogs und die Standard-Runtime `contextTokens = 272000`; überschreiben Sie die Runtime-Obergrenze mit `models.providers.openai-codex.models[].contextTokens`
  * Richtlinienhinweis: OpenAI Codex OAuth wird ausdrücklich für externe Tools/Workflows wie OpenClaw unterstützt.
  * Für die gängige Route aus Abonnement plus nativer Codex-Runtime melden Sie sich mit `openai-codex`-Auth an, konfigurieren aber `openai/gpt-5.5`; OpenAI-Agent-Turns wählen standardmäßig Codex aus.
  * Verwenden Sie Provider-/Modell-`agentRuntime.id: "pi"` nur, wenn Sie eine Kompatibilitätsroute über PI wünschen; andernfalls belassen Sie `openai/gpt-5.5` auf dem standardmäßigen Codex-Harness.
  * Ältere `openai-codex/gpt-5.1*`-, `openai-codex/gpt-5.2*`\- und `openai-codex/gpt-5.3*`-Refs werden unterdrückt, weil ChatGPT-/Codex-OAuth-Konten sie ablehnen; verwenden Sie stattdessen `openai-codex/gpt-5.5` oder die native Codex-Runtime-Route.

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

json5Copy code
[code]
    {  models: {    providers: {      "openai-codex": {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### Weitere gehostete Optionen im Abonnement-Stil

[**GLM-Modelle** [Z.AI](<http://Z.AI>) Coding Plan oder allgemeine API-Endpunkte. ](</de/providers/glm>) [**MiniMax** MiniMax Coding Plan OAuth oder API-Key-Zugriff. ](</de/providers/minimax>) [**Qwen Cloud** Qwen Cloud-Provider-Oberfläche plus Alibaba DashScope und Endpunktzuordnung für Coding Plan. ](</de/providers/qwen>)

### OpenCode

  * Auth: `OPENCODE_API_KEY` (oder `OPENCODE_ZEN_API_KEY`)
  * Zen-Runtime-Provider: `opencode`
  * Go-Runtime-Provider: `opencode-go`
  * Beispielmodelle: `opencode/claude-opus-4-6`, `opencode-go/kimi-k2.6`
  * CLI: `openclaw onboard --auth-choice opencode-zen` oder `openclaw onboard --auth-choice opencode-go`

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

### Google Gemini (API-Key)

  * Provider: `google`
  * Authentifizierung: `GEMINI_API_KEY`
  * Optionale Rotation: `GEMINI_API_KEYS`, `GEMINI_API_KEY_1`, `GEMINI_API_KEY_2`, `GOOGLE_API_KEY`-Fallback und `OPENCLAW_LIVE_GEMINI_KEY` (einzelne Überschreibung)
  * Beispielmodelle: `google/gemini-3.1-pro-preview`, `google/gemini-3-flash-preview`
  * Kompatibilität: Die ältere OpenClaw-Konfiguration mit `google/gemini-3.1-flash-preview` wird zu `google/gemini-3-flash-preview` normalisiert
  * Alias: `google/gemini-3.1-pro` wird akzeptiert und zu Googles Live-Gemini-API-ID `google/gemini-3.1-pro-preview` normalisiert
  * CLI: `openclaw onboard --auth-choice gemini-api-key`
  * Denken: `/think adaptive` verwendet Googles dynamisches Denken. Gemini 3/3.1 lassen ein festes `thinkingLevel` weg; Gemini 2.5 sendet `thinkingBudget: -1`.
  * Direkte Gemini-Ausführungen akzeptieren auch `agents.defaults.models["google/<model>"].params.cachedContent` (oder das ältere `cached_content`), um ein Provider-natives `cachedContents/...`-Handle weiterzuleiten; Gemini-Cachetreffer erscheinen als OpenClaw `cacheRead`


### Google Vertex und Gemini CLI

  * Provider: `google-vertex`, `google-gemini-cli`
  * Authentifizierung: Vertex verwendet gcloud ADC; Gemini CLI verwendet seinen OAuth-Ablauf


Gemini CLI OAuth wird als Teil des gebündelten `google`-Plugins ausgeliefert.

* ### Gemini CLI installieren

### brew

bashCopy code
[code]
    brew install gemini-cli
[/code]

### npm

bashCopy code
[code]
    npm install -g @google/gemini-cli
[/code]

* ### Plugin aktivieren

bashCopy code
[code]
    openclaw plugins enable google
[/code]

* ### Anmelden

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

Standardmodell: `google-gemini-cli/gemini-3-flash-preview`. Sie fügen **keine** Client-ID und kein Secret in `openclaw.json` ein. Der CLI-Anmeldeablauf speichert Tokens in Auth-Profilen auf dem Gateway-Host.

* ### Projekt festlegen (falls erforderlich)

Wenn Anfragen nach der Anmeldung fehlschlagen, legen Sie `GOOGLE_CLOUD_PROJECT` oder `GOOGLE_CLOUD_PROJECT_ID` auf dem Gateway-Host fest.

JSON-Antworten von Gemini CLI werden aus `response` geparst; die Nutzung greift ersatzweise auf `stats` zurück, wobei `stats.cached` in OpenClaw `cacheRead` normalisiert wird.

### [Z.AI](<http://Z.AI>) (GLM)

  * Provider: `zai`
  * Authentifizierung: `ZAI_API_KEY`
  * Beispielmodell: `zai/glm-5.1`
  * CLI: `openclaw onboard --auth-choice zai-api-key`
    * Aliasse: `z.ai/*` und `z-ai/*` werden zu `zai/*` normalisiert
    * `zai-api-key` erkennt den passenden Z.AI-Endpunkt automatisch; `zai-coding-global`, `zai-coding-cn`, `zai-global` und `zai-cn` erzwingen eine bestimmte Oberfläche


### Vercel AI Gateway

  * Provider: `vercel-ai-gateway`
  * Authentifizierung: `AI_GATEWAY_API_KEY`
  * Beispielmodelle: `vercel-ai-gateway/anthropic/claude-opus-4.6`, `vercel-ai-gateway/moonshotai/kimi-k2.6`
  * CLI: `openclaw onboard --auth-choice ai-gateway-api-key`


### Kilo Gateway

  * Provider: `kilocode`
  * Authentifizierung: `KILOCODE_API_KEY`
  * Beispielmodell: `kilocode/kilo/auto`
  * CLI: `openclaw onboard --auth-choice kilocode-api-key`
  * Basis-URL: `https://api.kilo.ai/api/gateway/`
  * Der statische Fallback-Katalog liefert `kilocode/kilo/auto` aus; die Live-Erkennung über `https://api.kilo.ai/api/gateway/models` kann den Laufzeitkatalog weiter erweitern.
  * Das exakte Upstream-Routing hinter `kilocode/kilo/auto` liegt bei Kilo Gateway und ist nicht in OpenClaw fest codiert.


Einrichtungsdetails finden Sie unter [/providers/kilocode](</de/providers/kilocode>).

### Andere gebündelte Provider-Plugins

Provider | ID | Auth-Env | Beispielmodell  
---|---|---|---  
BytePlus | `byteplus` / `byteplus-plan` | `BYTEPLUS_API_KEY` | `byteplus-plan/ark-code-latest`  
Cerebras | `cerebras` | `CEREBRAS_API_KEY` | `cerebras/zai-glm-4.7`  
Cloudflare AI Gateway | `cloudflare-ai-gateway` | `CLOUDFLARE_AI_GATEWAY_API_KEY` | -  
DeepInfra | `deepinfra` | `DEEPINFRA_API_KEY` | `deepinfra/deepseek-ai/DeepSeek-V3.2`  
DeepSeek | `deepseek` | `DEEPSEEK_API_KEY` | `deepseek/deepseek-v4-flash`  
GitHub Copilot | `github-copilot` | `COPILOT_GITHUB_TOKEN` / `GH_TOKEN` / `GITHUB_TOKEN` | -  
Groq | `groq` | `GROQ_API_KEY` | -  
Hugging Face Inference | `huggingface` | `HUGGINGFACE_HUB_TOKEN` oder `HF_TOKEN` | `huggingface/deepseek-ai/DeepSeek-R1`  
Kilo Gateway | `kilocode` | `KILOCODE_API_KEY` | `kilocode/kilo/auto`  
Kimi Coding | `kimi` | `KIMI_API_KEY` oder `KIMICODE_API_KEY` | `kimi/kimi-for-coding`  
MiniMax | `minimax` / `minimax-portal` | `MINIMAX_API_KEY` / `MINIMAX_OAUTH_TOKEN` | `minimax/MiniMax-M2.7`  
Mistral | `mistral` | `MISTRAL_API_KEY` | `mistral/mistral-large-latest`  
Moonshot | `moonshot` | `MOONSHOT_API_KEY` | `moonshot/kimi-k2.6`  
NVIDIA | `nvidia` | `NVIDIA_API_KEY` | `nvidia/nvidia/nemotron-3-super-120b-a12b`  
OpenRouter | `openrouter` | `OPENROUTER_API_KEY` | `openrouter/auto`  
Qianfan | `qianfan` | `QIANFAN_API_KEY` | `qianfan/deepseek-v3.2`  
Qwen Cloud | `qwen` | `QWEN_API_KEY` / `MODELSTUDIO_API_KEY` / `DASHSCOPE_API_KEY` | `qwen/qwen3.5-plus`  
StepFun | `stepfun` / `stepfun-plan` | `STEPFUN_API_KEY` | `stepfun/step-3.5-flash`  
Together | `together` | `TOGETHER_API_KEY` | `together/moonshotai/Kimi-K2.5`  
Venice | `venice` | `VENICE_API_KEY` | -  
Vercel AI Gateway | `vercel-ai-gateway` | `AI_GATEWAY_API_KEY` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
Volcano Engine (Doubao) | `volcengine` / `volcengine-plan` | `VOLCANO_ENGINE_API_KEY` | `volcengine-plan/ark-code-latest`  
xAI | `xai` | `XAI_API_KEY` | `xai/grok-4.3`  
Xiaomi | `xiaomi` | `XIAOMI_API_KEY` | `xiaomi/mimo-v2-flash`  
  
#### Wissenswerte Besonderheiten

OpenRouter

Wendet seine App-Attributions-Header und Anthropic-`cache_control`-Marker nur auf verifizierten `openrouter.ai`-Routen an. DeepSeek-, Moonshot- und ZAI-Referenzen sind für von OpenRouter verwaltetes Prompt-Caching mit Cache-TTL geeignet, erhalten aber keine Anthropic-Cache-Marker. Als proxyartiger OpenAI-kompatibler Pfad überspringt er nur für natives OpenAI geltende Formanpassungen (`serviceTier`, Responses `store`, Prompt-Cache-Hinweise, OpenAI-Reasoning-Kompatibilität). Gemini-gestützte Referenzen behalten nur die proxybezogene Gemini-Bereinigung von Thought-Signatures bei.

Kilo Gateway

Gemini-gestützte Referenzen folgen demselben proxybezogenen Gemini-Bereinigungspfad; `kilocode/kilo/auto` und andere Referenzen ohne Proxy-Reasoning-Unterstützung überspringen die Proxy-Reasoning-Injektion.

MiniMax

Das API-Key-Onboarding schreibt explizite reine Textdefinitionen für M2.7-Chatmodelle; Bildverständnis bleibt beim Plugin-eigenen Medien-Provider `MiniMax-VL-01`.

NVIDIA

Modell-IDs verwenden einen Namespace `nvidia/<vendor>/<model>` (zum Beispiel `nvidia/nvidia/nemotron-...` neben `nvidia/moonshotai/kimi-k2.5`); Picker bewahren die wörtliche Zusammensetzung `<provider>/<model-id>`, während der kanonische an die API gesendete Schlüssel einfach präfixiert bleibt.

xAI

Verwendet den xAI-Responses-Pfad. `grok-4.3` ist das gebündelte Standard-Chatmodell. `/fast` oder `params.fastMode: true` schreibt `grok-3`, `grok-3-mini`, `grok-4` und `grok-4-0709` auf ihre `*-fast`-Varianten um. `tool_stream` ist standardmäßig aktiviert; deaktivieren Sie es über `agents.defaults.models["xai/<model>"].params.tool_stream=false`.

Cerebras

Wird als gebündeltes `cerebras`-Provider-Plugin ausgeliefert. GLM verwendet `zai-glm-4.7`; die OpenAI-kompatible Basis-URL ist `https://api.cerebras.ai/v1`.

## Provider über `models.providers` (benutzerdefiniert/Basis-URL)

Verwenden Sie `models.providers` (oder `models.json`), um **benutzerdefinierte** Provider oder OpenAI-/Anthropic-kompatible Proxys hinzuzufügen.

Viele der unten aufgeführten gebündelten Provider-Plugins veröffentlichen bereits einen Standardkatalog. Verwenden Sie explizite `models.providers.<id>`-Einträge nur, wenn Sie die standardmäßige Basis-URL, Header oder Modellliste überschreiben möchten.

Gateway-Modellfähigkeitsprüfungen lesen auch explizite `models.providers.<id>.models[]`-Metadaten. Wenn ein benutzerdefiniertes oder Proxy-Modell Bilder akzeptiert, setzen Sie bei diesem Modell `input: ["text", "image"]`, damit WebChat- und von Nodes ausgehende Anhangspfade Bilder als native Modelleingaben statt als reine Text-Medienreferenzen übergeben.

`agents.defaults.models["provider/model"]` steuert nur Modellsichtbarkeit, Aliase und modellbezogene Metadaten für Agenten. Es registriert allein kein neues Laufzeitmodell. Fügen Sie für benutzerdefinierte Provider-Modelle außerdem `models.providers.<provider>.models[]` mit mindestens der passenden `id` hinzu.

### Moonshot AI (Kimi)

Moonshot wird als gebündeltes Provider-Plugin ausgeliefert. Verwenden Sie standardmäßig den integrierten Provider und fügen Sie nur dann einen expliziten `models.providers.moonshot`-Eintrag hinzu, wenn Sie die Basis-URL oder Modellmetadaten überschreiben müssen:

  * Provider: `moonshot`
  * Auth: `MOONSHOT_API_KEY`
  * Beispielmodell: `moonshot/kimi-k2.6`
  * CLI: `openclaw onboard --auth-choice moonshot-api-key` oder `openclaw onboard --auth-choice moonshot-api-key-cn`


Kimi-K2-Modell-IDs:

  * `moonshot/kimi-k2.6`
  * `moonshot/kimi-k2.5`
  * `moonshot/kimi-k2-thinking`
  * `moonshot/kimi-k2-thinking-turbo`
  * `moonshot/kimi-k2-turbo`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "moonshot/kimi-k2.6" } },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [{ id: "kimi-k2.6", name: "Kimi K2.6" }],      },    },  },}
[/code]

### Kimi Coding

Kimi Coding verwendet den Anthropic-kompatiblen Endpunkt von Moonshot AI:

  * Provider: `kimi`
  * Authentifizierung: `KIMI_API_KEY`
  * Beispielmodell: `kimi/kimi-for-coding`

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: { model: { primary: "kimi/kimi-for-coding" } },  },}
[/code]

Die Legacy-IDs `kimi/kimi-code` und `kimi/k2p5` werden weiterhin als Kompatibilitätsmodell-IDs akzeptiert und auf Kimis stabile API-Modell-ID normalisiert.

### Volcano Engine (Doubao)

Volcano Engine (火山引擎) bietet Zugriff auf Doubao und andere Modelle in China.

  * Provider: `volcengine` (Coding: `volcengine-plan`)
  * Authentifizierung: `VOLCANO_ENGINE_API_KEY`
  * Beispielmodell: `volcengine-plan/ark-code-latest`
  * CLI: `openclaw onboard --auth-choice volcengine-api-key`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "volcengine-plan/ark-code-latest" } },  },}
[/code]

Das Onboarding verwendet standardmäßig die Coding-Oberfläche, aber der allgemeine `volcengine/*`-Katalog wird gleichzeitig registriert.

In den Modellauswahlen für Onboarding/Konfiguration bevorzugt die Volcengine-Authentifizierungsoption sowohl `volcengine/*`\- als auch `volcengine-plan/*`-Zeilen. Wenn diese Modelle noch nicht geladen sind, fällt OpenClaw auf den ungefilterten Katalog zurück, statt eine leere Provider-bezogene Auswahl anzuzeigen.

### Standardmodelle

  * `volcengine/doubao-seed-1-8-251228` (Doubao Seed 1.8)
  * `volcengine/doubao-seed-code-preview-251028`
  * `volcengine/kimi-k2-5-260127` (Kimi K2.5)
  * `volcengine/glm-4-7-251222` (GLM 4.7)
  * `volcengine/deepseek-v3-2-251201` (DeepSeek V3.2 128K)


### Coding-Modelle (volcengine-plan)

  * `volcengine-plan/ark-code-latest`
  * `volcengine-plan/doubao-seed-code`
  * `volcengine-plan/kimi-k2.5`
  * `volcengine-plan/kimi-k2-thinking`
  * `volcengine-plan/glm-4.7`


### BytePlus (International)

BytePlus ARK bietet internationalen Benutzern Zugriff auf dieselben Modelle wie Volcano Engine.

  * Provider: `byteplus` (Coding: `byteplus-plan`)
  * Authentifizierung: `BYTEPLUS_API_KEY`
  * Beispielmodell: `byteplus-plan/ark-code-latest`
  * CLI: `openclaw onboard --auth-choice byteplus-api-key`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "byteplus-plan/ark-code-latest" } },  },}
[/code]

Das Onboarding verwendet standardmäßig die Coding-Oberfläche, aber der allgemeine `byteplus/*`-Katalog wird gleichzeitig registriert.

In den Modellauswahlen für Onboarding/Konfiguration bevorzugt die BytePlus-Authentifizierungsoption sowohl `byteplus/*`\- als auch `byteplus-plan/*`-Zeilen. Wenn diese Modelle noch nicht geladen sind, fällt OpenClaw auf den ungefilterten Katalog zurück, statt eine leere Provider-bezogene Auswahl anzuzeigen.

### Standardmodelle

  * `byteplus/seed-1-8-251228` (Seed 1.8)
  * `byteplus/kimi-k2-5-260127` (Kimi K2.5)
  * `byteplus/glm-4-7-251222` (GLM 4.7)


### Coding-Modelle (byteplus-plan)

  * `byteplus-plan/ark-code-latest`
  * `byteplus-plan/doubao-seed-code`
  * `byteplus-plan/kimi-k2.5`
  * `byteplus-plan/kimi-k2-thinking`
  * `byteplus-plan/glm-4.7`


### Synthetic

Synthetic stellt Anthropic-kompatible Modelle hinter dem Provider `synthetic` bereit:

  * Provider: `synthetic`
  * Authentifizierung: `SYNTHETIC_API_KEY`
  * Beispielmodell: `synthetic/hf:MiniMaxAI/MiniMax-M2.5`
  * CLI: `openclaw onboard --auth-choice synthetic-api-key`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" } },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [{ id: "hf:MiniMaxAI/MiniMax-M2.5", name: "MiniMax M2.5" }],      },    },  },}
[/code]

### MiniMax

MiniMax wird über `models.providers` konfiguriert, da es benutzerdefinierte Endpunkte verwendet:

  * MiniMax OAuth (Global): `--auth-choice minimax-global-oauth`
  * MiniMax OAuth (CN): `--auth-choice minimax-cn-oauth`
  * MiniMax API-Schlüssel (Global): `--auth-choice minimax-global-api`
  * MiniMax API-Schlüssel (CN): `--auth-choice minimax-cn-api`
  * Authentifizierung: `MINIMAX_API_KEY` für `minimax`; `MINIMAX_OAUTH_TOKEN` oder `MINIMAX_API_KEY` für `minimax-portal`


Siehe [/providers/minimax](</de/providers/minimax>) für Einrichtungsdetails, Modelloptionen und Konfigurationsausschnitte.

Plugin-eigene Aufteilung der Fähigkeiten:

  * Text-/Chat-Standards bleiben auf `minimax/MiniMax-M2.7`
  * Bilderzeugung ist `minimax/image-01` oder `minimax-portal/image-01`
  * Bildverständnis ist Plugin-eigenes `MiniMax-VL-01` auf beiden MiniMax-Authentifizierungspfaden
  * Websuche bleibt auf der Provider-ID `minimax`


### LM Studio

LM Studio wird als gebündeltes Provider-Plugin ausgeliefert, das die native API verwendet:

  * Provider: `lmstudio`
  * Authentifizierung: `LM_API_TOKEN`
  * Standard-Basis-URL für Inferenz: `http://localhost:1234/v1`


Legen Sie dann ein Modell fest (ersetzen Sie es durch eine der IDs, die von `http://localhost:1234/api/v1/models` zurückgegeben werden):

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "lmstudio/openai/gpt-oss-20b" } },  },}
[/code]

OpenClaw verwendet LM Studios native `/api/v1/models` und `/api/v1/models/load` für Erkennung + automatisches Laden, standardmäßig mit `/v1/chat/completions` für Inferenz. Wenn Sie möchten, dass LM Studio JIT-Laden, TTL und automatische Entfernung den Modelllebenszyklus besitzen, setzen Sie `models.providers.lmstudio.params.preload: false`. Siehe [/providers/lmstudio](</de/providers/lmstudio>) für Einrichtung und Fehlerbehebung.

### Ollama

Ollama wird als gebündeltes Provider-Plugin ausgeliefert und verwendet Ollamas native API:

  * Provider: `ollama`
  * Authentifizierung: Nicht erforderlich (lokaler Server)
  * Beispielmodell: `ollama/llama3.3`
  * Installation: <https://ollama.com/download>

bashCopy code
[code]
    # Install Ollama, then pull a model:ollama pull llama3.3
[/code]

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "ollama/llama3.3" } },  },}
[/code]

Ollama wird lokal unter `http://127.0.0.1:11434` erkannt, wenn Sie sich mit `OLLAMA_API_KEY` dafür entscheiden, und das gebündelte Provider-Plugin fügt Ollama direkt zu `openclaw onboard` und der Modellauswahl hinzu. Siehe [/providers/ollama](</de/providers/ollama>) für Onboarding, Cloud-/lokalen Modus und benutzerdefinierte Konfiguration.

### vLLM

vLLM wird als gebündeltes Provider-Plugin für lokale/selbst gehostete OpenAI-kompatible Server ausgeliefert:

  * Provider: `vllm`
  * Authentifizierung: Optional (abhängig von Ihrem Server)
  * Standard-Basis-URL: `http://127.0.0.1:8000/v1`


Um die automatische Erkennung lokal zu aktivieren (jeder Wert funktioniert, wenn Ihr Server keine Authentifizierung erzwingt):

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

Legen Sie dann ein Modell fest (ersetzen Sie es durch eine der IDs, die von `/v1/models` zurückgegeben werden):

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "vllm/your-model-id" } },  },}
[/code]

Siehe [/providers/vllm](</de/providers/vllm>) für Details.

### SGLang

SGLang wird als gebündeltes Provider-Plugin für schnelle selbst gehostete OpenAI-kompatible Server ausgeliefert:

  * Provider: `sglang`
  * Authentifizierung: Optional (abhängig von Ihrem Server)
  * Standard-Basis-URL: `http://127.0.0.1:30000/v1`


Um die automatische Erkennung lokal zu aktivieren (jeder Wert funktioniert, wenn Ihr Server keine Authentifizierung erzwingt):

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

Legen Sie dann ein Modell fest (ersetzen Sie es durch eine der IDs, die von `/v1/models` zurückgegeben werden):

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "sglang/your-model-id" } },  },}
[/code]

Siehe [/providers/sglang](</de/providers/sglang>) für Details.

### Lokale Proxys (LM Studio, vLLM, LiteLLM usw.)

Beispiel (OpenAI-kompatibel):

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "lmstudio/my-local-model" },      models: { "lmstudio/my-local-model": { alias: "Local" } },    },  },  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        apiKey: "${LM_API_TOKEN}",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "my-local-model",            name: "Local Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

Optionale Standardfelder

Für benutzerdefinierte Provider sind `reasoning`, `input`, `cost`, `contextWindow` und `maxTokens` optional. Wenn sie ausgelassen werden, verwendet OpenClaw standardmäßig:

  * `reasoning: false`
  * `input: ["text"]`
  * `cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 }`
  * `contextWindow: 200000`
  * `maxTokens: 8192`


Empfehlung: Legen Sie explizite Werte fest, die zu den Limits Ihres Proxys/Modells passen.

Regeln zur Proxy-Routen-Formung

  * Für `api: "openai-completions"` auf nicht-nativen Endpunkten (jede nicht leere `baseUrl`, deren Host nicht `api.openai.com` ist) erzwingt OpenClaw `compat.supportsDeveloperRole: false`, um Provider-400-Fehler wegen nicht unterstützter `developer`-Rollen zu vermeiden.
  * OpenAI-kompatible Routen im Proxy-Stil überspringen außerdem native, nur für OpenAI geltende Anfrageformung: kein `service_tier`, kein Responses-`store`, kein Completions-`store`, keine Prompt-Cache-Hinweise, keine OpenAI-Reasoning-Kompatibilitäts-Payload-Formung und keine versteckten OpenClaw-Zuordnungsheader.
  * Für OpenAI-kompatible Completions-Proxys, die anbieterspezifische Felder benötigen, setzen Sie `agents.defaults.models["provider/model"].params.extra_body` (oder `extraBody`), um zusätzliches JSON in den ausgehenden Anfrage-Body zusammenzuführen.
  * Für vLLM-Chat-Template-Steuerungen setzen Sie `agents.defaults.models["provider/model"].params.chat_template_kwargs`. Das gebündelte vLLM-Plugin sendet automatisch `enable_thinking: false` und `force_nonempty_content: true` für `vllm/nemotron-3-*`, wenn das Thinking-Level der Sitzung ausgeschaltet ist.
  * Für langsame lokale Modelle oder entfernte LAN-/Tailnet-Hosts setzen Sie `models.providers.<id>.timeoutSeconds`. Dies erweitert die HTTP-Anfrageverarbeitung des Provider-Modells, einschließlich Verbindung, Headern, Body-Streaming und dem gesamten guarded-fetch-Abbruch, ohne das gesamte Agent-Laufzeit-Timeout zu erhöhen.
  * HTTP-Aufrufe von Modell-Providern erlauben Surge-, Clash- und sing-box-Fake-IP-DNS-Antworten in `198.18.0.0/15` und `fc00::/7` nur für den konfigurierten Provider-`baseUrl`-Hostnamen. Andere private, Loopback-, Link-Local- und Metadaten-Ziele erfordern weiterhin eine explizite `models.providers.<id>.request.allowPrivateNetwork: true`-Aktivierung.
  * Wenn `baseUrl` leer ist oder ausgelassen wird, behält OpenClaw das Standardverhalten von OpenAI bei (das zu `api.openai.com` auflöst).
  * Aus Sicherheitsgründen wird ein explizites `compat.supportsDeveloperRole: true` auf nicht-nativen `openai-completions`-Endpunkten weiterhin überschrieben.
  * Für `api: "anthropic-messages"` auf nicht-direkten Endpunkten (jeder Provider außer dem kanonischen `anthropic` oder eine benutzerdefinierte `models.providers.anthropic.baseUrl`, deren Host kein öffentlicher `api.anthropic.com`-Endpunkt ist) unterdrückt OpenClaw implizite Anthropic-Beta-Header wie `claude-code-20250219`, `interleaved-thinking-2025-05-14` und OAuth-Marker, damit benutzerdefinierte Anthropic-kompatible Proxys nicht unterstützte Beta-Flags nicht ablehnen. Setzen Sie `models.providers.<id>.headers["anthropic-beta"]` explizit, wenn Ihr Proxy bestimmte Beta-Funktionen benötigt.


## CLI-Beispiele

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zenopenclaw models set opencode/claude-opus-4-6openclaw models list
[/code]

Siehe auch: [Konfiguration](</de/gateway/configuration>) für vollständige Konfigurationsbeispiele.

## Verwandte Themen

  * [Konfigurationsreferenz](</de/gateway/config-agents#agent-defaults>) \- Modellkonfigurationsschlüssel
  * [Modell-Failover](</de/concepts/model-failover>) \- Fallback-Ketten und Wiederholungsverhalten
  * [Modelle](</de/concepts/models>) \- Modellkonfiguration und Aliase
  * [Provider](</de/providers>) \- Einrichtungshandbücher pro Provider


Was this useful?YesNo