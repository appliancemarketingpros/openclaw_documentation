---
title: @openclaw/ai-Paket
source_url: https://docs.openclaw.ai/de/reference/openclaw-ai
scraped_at: 2026-07-13
---

ReferenceTechnical reference

`@openclaw/ai` ist die veröffentlichbare Bibliotheksform der Modellausführungsschicht von OpenClaw: Provider-neutrale Nachrichten-, Tool- und Stream-Verträge, Validierung, Diagnose, Ereignisstreams, eine isolierte Laufzeitregistrierung und verzögert geladene Adapter für die acht integrierten API-Familien (Anthropic Messages, OpenAI Completions, OpenAI Responses, Azure OpenAI Responses, ChatGPT/Codex Responses, Google Generative AI, Google Vertex, Mistral Conversations).

Sie wird bei jeder Veröffentlichung zusammen mit dem Stammpaket `openclaw` in derselben Version veröffentlicht und verfügt über eine eigene `npm-shrinkwrap.json`, damit ihr transitiver Abhängigkeitsbaum zum Installationszeitpunkt festgeschrieben ist. Bei der Installation von `openclaw` wird das passende `@openclaw/ai` automatisch installiert; Bibliotheksnutzer können es direkt als Abhängigkeit verwenden, ohne Anwendungscode von OpenClaw einzubinden.

## Schnellstart

jsCopy code
[code]
      const runtime = createLlmRuntime();registerBuiltInApiProviders(runtime.registry); const stream = runtime.streamSimple(model, { messages }, { apiKey });for await (const event of stream) {  if (event.type === "text_delta") process.stdout.write(event.delta);}const result = await stream.result();
[/code]

Eine ausführbare Version befindet sich im Repository unter `examples/ai-chat`.

## Designvertrag

  * **Standardmäßig instanzbezogen.** Beim Importieren des Pakets wird nichts global registriert. `createApiRegistry()` / `createLlmRuntime()` geben isolierte Instanzen zurück; `registerBuiltInApiProviders(registry)` aktiviert die integrierten Transporte für eine Registrierung. Provider-SDK-Module werden bei der ersten Verwendung verzögert geladen.
  * **Host-Richtlinien werden injiziert, nicht gebündelt.** Die Absicherung von Request-Fetches (zum Beispiel SSRF-Richtlinien), die Schwärzung von Geheimnissen in erneut wiedergegebenem Tool-Ergebnistext, strikte Tool-Standardeinstellungen von OpenAI und die Diagnoseprotokollierung sind `AiTransportHost`-Ports, die mit `configureAiTransportHost` konfiguriert werden. Die Standardeinstellungen der Bibliothek sind inaktiv; OpenClaw installiert die tatsächlichen Implementierungen in seiner Stream-Fassade.
  * **Eine Ereignisstream-Identität.** `@openclaw/ai/event-stream` ist der kanonische `EventStream`-Konstruktor, den OpenClaw Core, Agent Core und externe Nutzer gemeinsam verwenden.
  * **`internal/*`-Unterpfade sind keine API.** Sie sind für die OpenClaw-Anwendung selbst vorgesehen und bieten keine Semver-Garantie.
  * Provider-IDs, Anmeldedaten, Modellkataloge, Wiederholungsversuche und Failover bleiben Belange der Anwendung. OpenClaw legt diese Funktionen um dieses Paket; ein Bibliotheksnutzer stellt direkt ein `Model`-Objekt und Optionen bereit.


## Unterpfadexporte

Unterpfad | Inhalt  
---|---  
`.` | Verträge, `createApiRegistry`, `createLlmRuntime`, `configureAiTransportHost`  
`./providers` | `registerBuiltInApiProviders`, `resetApiProviders`  
`./types` | Modell-, Nachrichten-, Tool- und Stream-Typen  
`./validation` | Validierung von Tool-Argumenten  
`./diagnostics` | Diagnoseverträge  
`./event-stream` | Gemeinsame `EventStream`-Implementierung  
`./internal/*` | OpenClaw-intern, keine Semver-Garantie  
  
Was this useful?YesNo

Open issue