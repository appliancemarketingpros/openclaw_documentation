---
title: CLI-Automatisierung
source_url: https://docs.openclaw.ai/de/start/wizard-cli-automation
scraped_at: 2026-05-25
---

Verwenden Sie `--non-interactive`, um `openclaw onboard` zu automatisieren.

## Grundlegendes nichtinteraktives Beispiel

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

Fügen Sie `--json` hinzu, um eine maschinenlesbare Zusammenfassung zu erhalten.

Verwenden Sie `--skip-bootstrap`, wenn Ihre Automatisierung Workspace-Dateien vorab bereitstellt und das Onboarding die standardmäßigen Bootstrap-Dateien nicht erstellen soll.

Verwenden Sie `--secret-input-mode ref`, um umgebungsbasierte Referenzen in Auth-Profilen statt Klartextwerten zu speichern. Die interaktive Auswahl zwischen Umgebungsreferenzen und konfigurierten Provider-Referenzen (`file` oder `exec`) ist im Onboarding-Ablauf verfügbar.

Im nichtinteraktiven `ref`-Modus müssen Provider-Umgebungsvariablen in der Prozessumgebung gesetzt sein. Das Übergeben von Inline-Schlüsselflags ohne die passende Umgebungsvariable schlägt jetzt frühzeitig fehl.

Beispiel:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Provider-spezifische Beispiele

Anthropic API key example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Gemini example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Z.AI example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Vercel AI Gateway example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Cloudflare AI Gateway example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Moonshot example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Mistral example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Synthetic example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

OpenCode example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Wechseln Sie für den Go-Katalog zu `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"`.

Ollama example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Custom provider example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` ist optional. Wenn es weggelassen wird, prüft das Onboarding `CUSTOM_API_KEY`. OpenClaw markiert gängige Vision-Modell-IDs automatisch als bildfähig. Fügen Sie `--custom-image-input` für unbekannte benutzerdefinierte Vision-IDs hinzu oder `--custom-text-input`, um reine Textmetadaten zu erzwingen.

Ref-Modus-Variante:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

In diesem Modus speichert das Onboarding `apiKey` als `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.

Anthropic-Setup-Token bleibt als unterstützter Onboarding-Token-Pfad verfügbar, aber OpenClaw bevorzugt jetzt die Wiederverwendung der Claude CLI, wenn verfügbar. Für Produktion verwenden Sie bevorzugt einen Anthropic-API-Schlüssel.

## Weiteren Agenten hinzufügen

Verwenden Sie `openclaw agents add <name>`, um einen separaten Agenten mit eigenem Workspace, eigenen Sitzungen und Auth-Profilen zu erstellen. Die Ausführung ohne `--workspace` startet den Assistenten.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

Was festgelegt wird:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Hinweise:

  * Standard-Workspaces folgen `~/.openclaw/workspace-<agentId>`.
  * Fügen Sie `bindings` hinzu, um eingehende Nachrichten weiterzuleiten (der Assistent kann dies übernehmen).
  * Nichtinteraktive Flags: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Verwandte Dokumentation

  * Onboarding-Hub: [Onboarding (CLI)](</de/start/wizard>)
  * Vollständige Referenz: [CLI-Einrichtungsreferenz](</de/start/wizard-cli-reference>)
  * Befehlsreferenz: [`openclaw onboard`](</de/cli/onboard>)


Was this useful?YesNo