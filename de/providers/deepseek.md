---
title: DeepSeek
source_url: https://docs.openclaw.ai/de/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) stellt leistungsstarke KI-Modelle mit einer OpenAI-kompatiblen API bereit.

Eigenschaft | Wert  
---|---  
Provider | `deepseek`  
Auth | `DEEPSEEK_API_KEY`  
API | OpenAI-kompatibel  
Basis-URL | `https://api.deepseek.com`  
  
## Erste Schritte

* ### Ihren API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel unter [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

Dadurch werden Sie nach Ihrem API-Schlüssel gefragt, und `deepseek/deepseek-v4-flash` wird als Standardmodell festgelegt.

* ### Verifizieren, dass Modelle verfügbar sind

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Um den gebündelten statischen Katalog zu prüfen, ohne dass ein laufender Gateway erforderlich ist, verwenden Sie:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Nicht interaktive Einrichtung

Für skriptgesteuerte oder headless Installationen übergeben Sie alle Flags direkt:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Integrierter Katalog

Modellreferenz | Name | Eingabe | Kontext | Maximale Ausgabe | Hinweise  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | Text | 1,000,000 | 384,000 | Standardmodell; V4-Oberfläche mit Thinking-Unterstützung  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | Text | 1,000,000 | 384,000 | V4-Oberfläche mit Thinking-Unterstützung  
`deepseek/deepseek-chat` | DeepSeek Chat | Text | 131,072 | 8,192 | DeepSeek V3.2-Oberfläche ohne Thinking  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | Text | 131,072 | 65,536 | V3.2-Oberfläche mit Reasoning-Unterstützung  
  
## Thinking und Tools

DeepSeek-V4-Thinking-Sitzungen haben einen strengeren Replay-Vertrag als die meisten OpenAI-kompatiblen Provider: Nachdem ein Turn mit aktiviertem Thinking Tools verwendet hat, erwartet DeepSeek, dass erneut abgespielte Assistant-Nachrichten aus diesem Turn bei Folgeanfragen `reasoning_content` enthalten. OpenClaw behandelt dies innerhalb des DeepSeek-Plugins, sodass normale Tool-Nutzung über mehrere Turns mit `deepseek/deepseek-v4-flash` und `deepseek/deepseek-v4-pro` funktioniert.

Wenn Sie eine vorhandene Sitzung von einem anderen OpenAI-kompatiblen Provider zu einem DeepSeek-V4-Modell wechseln, haben ältere Assistant-Tool-Call-Turns möglicherweise kein natives DeepSeek-`reasoning_content`. OpenClaw ergänzt dieses fehlende Feld bei erneut abgespielten Assistant-Nachrichten für DeepSeek-V4-Thinking-Anfragen, damit der Provider den Verlauf akzeptieren kann, ohne dass `/new` erforderlich ist.

Wenn Thinking in OpenClaw deaktiviert ist (einschließlich der UI-Auswahl **Keine**), sendet OpenClaw DeepSeek `thinking: { type: "disabled" }` und entfernt erneut abgespieltes `reasoning_content` aus dem ausgehenden Verlauf. Dadurch bleiben Sitzungen mit deaktiviertem Thinking auf dem DeepSeek-Pfad ohne Thinking.

Verwenden Sie `deepseek/deepseek-v4-flash` für den standardmäßigen schnellen Pfad. Verwenden Sie `deepseek/deepseek-v4-pro`, wenn Sie das stärkere V4-Modell möchten und höhere Kosten oder Latenz akzeptieren können.

## Live-Tests

Die direkte Live-Modellsuite enthält DeepSeek V4 im modernen Modellset. Um nur die direkten DeepSeek-V4-Modellprüfungen auszuführen:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Diese Live-Prüfung verifiziert, dass beide V4-Modelle abschließen können und dass Thinking-/Tool- Folgeturns die von DeepSeek benötigte Replay-Nutzlast beibehalten.

## Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Verwandt

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständige Konfigurationsreferenz für Agenten, Modelle und Provider. ](</de/gateway/configuration-reference>)

Was this useful?YesNo