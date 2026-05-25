---
title: Einrichten
source_url: https://docs.openclaw.ai/de/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

Vollständig geführtes Onboarding für die lokale oder entfernte Gateway-Einrichtung. Verwenden Sie dies, wenn OpenClaw Modellauthentifizierung, Workspace, Gateway, Kanäle, Skills und Health in einem Ablauf durchgehen soll.

## Zugehörige Leitfäden

[**CLI onboarding hub** Schrittweise Anleitung des interaktiven CLI-Ablaufs. ](</de/start/wizard>) [**Onboarding overview** Wie das OpenClaw-Onboarding zusammenpasst. ](</de/start/onboarding-overview>) [**CLI setup reference** Ausgaben, Interna und Verhalten pro Schritt. ](</de/start/wizard-cli-reference>) [**CLI automation** Nicht interaktive Flags und geskriptete Einrichtungen. ](</de/start/wizard-cli-automation>) [**macOS app onboarding** Onboarding-Ablauf für die macOS-Menüleisten-App. ](</de/start/onboarding>)

## Beispiele

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` verwendet Plugin-eigene Migrations-Provider wie Hermes. Es wird nur für eine frische OpenClaw-Einrichtung ausgeführt; wenn vorhandene Konfiguration, Zugangsdaten, Sitzungen oder Workspace-Speicher-/Identitätsdateien vorhanden sind, setzen Sie vor dem Import zurück oder wählen Sie eine frische Einrichtung.

`--modern` startet die Vorschau des dialogbasierten Crestodian-Onboardings. Ohne `--modern` behält `openclaw onboard` den klassischen Onboarding-Ablauf bei.

Für Klartext-`ws://`-Ziele in privaten Netzwerken (nur vertrauenswürdige Netzwerke) setzen Sie `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` in der Prozessumgebung des Onboardings. Es gibt kein `openclaw.json`-Äquivalent für diese clientseitige Transport- Notfallfreigabe.

Nicht interaktiver benutzerdefinierter Provider:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` ist im nicht interaktiven Modus optional. Wenn es ausgelassen wird, prüft das Onboarding `CUSTOM_API_KEY`. OpenClaw markiert gängige Vision-Modell-IDs automatisch als bildfähig. Übergeben Sie `--custom-image-input` für unbekannte benutzerdefinierte Vision-IDs oder `--custom-text-input`, um reine Text-Metadaten zu erzwingen.

LM Studio unterstützt im nicht interaktiven Modus auch ein Provider-spezifisches Schlüssel-Flag:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Nicht interaktives Ollama:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` verwendet standardmäßig `http://127.0.0.1:11434`. `--custom-model-id` ist optional; wenn es ausgelassen wird, verwendet das Onboarding die von Ollama vorgeschlagenen Standardwerte. Cloud-Modell-IDs wie `kimi-k2.5:cloud` funktionieren hier ebenfalls.

Provider-Schlüssel als Referenzen statt als Klartext speichern:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

Mit `--secret-input-mode ref` schreibt das Onboarding env-gestützte Referenzen statt Klartext-Schlüsselwerte. Für Provider mit Auth-Profil schreibt dies `keyRef`-Einträge; für benutzerdefinierte Provider schreibt dies `models.providers.<id>.apiKey` als env-Referenz (zum Beispiel `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

Vertrag des nicht interaktiven `ref`-Modus:

  * Setzen Sie die Provider-Umgebungsvariable in der Prozessumgebung des Onboardings (zum Beispiel `OPENAI_API_KEY`).
  * Übergeben Sie keine Inline-Schlüssel-Flags (zum Beispiel `--openai-api-key`), es sei denn, diese Umgebungsvariable ist ebenfalls gesetzt.
  * Wenn ein Inline-Schlüssel-Flag ohne die erforderliche Umgebungsvariable übergeben wird, schlägt das Onboarding sofort mit einer Anleitung fehl.


Gateway-Token-Optionen im nicht interaktiven Modus:

  * `--gateway-auth token --gateway-token <token>` speichert ein Klartext-Token.
  * `--gateway-auth token --gateway-token-ref-env <name>` speichert `gateway.auth.token` als env-SecretRef.
  * `--gateway-token` und `--gateway-token-ref-env` schließen sich gegenseitig aus.
  * `--gateway-token-ref-env` erfordert eine nicht leere Umgebungsvariable in der Prozessumgebung des Onboardings.
  * Mit `--install-daemon`, wenn Token-Authentifizierung ein Token erfordert, werden von SecretRef verwaltete Gateway-Token validiert, aber nicht als aufgelöster Klartext in den Metadaten der Supervisor-Dienstumgebung persistiert.
  * Mit `--install-daemon`, wenn der Token-Modus ein Token erfordert und der konfigurierte Token-SecretRef nicht aufgelöst ist, schlägt das Onboarding geschlossen mit Abhilfehinweisen fehl.
  * Mit `--install-daemon`, wenn sowohl `gateway.auth.token` als auch `gateway.auth.password` konfiguriert sind und `gateway.auth.mode` nicht gesetzt ist, blockiert das Onboarding die Installation, bis der Modus explizit gesetzt ist.
  * Lokales Onboarding schreibt `gateway.mode="local"` in die Konfiguration. Wenn in einer späteren Konfigurationsdatei `gateway.mode` fehlt, behandeln Sie dies als Konfigurationsschaden oder unvollständige manuelle Bearbeitung, nicht als gültige Abkürzung für den lokalen Modus.
  * Lokales Onboarding installiert ausgewählte herunterladbare Plugins, wenn der gewählte Einrichtungspfad sie erfordert.
  * Entferntes Onboarding schreibt nur Verbindungsinformationen für das entfernte Gateway und installiert keine lokalen Plugin-Pakete.
  * `--allow-unconfigured` ist eine separate Escape Hatch für die Gateway-Laufzeit. Es bedeutet nicht, dass das Onboarding `gateway.mode` auslassen darf.


Beispiel:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

Nicht interaktive Health-Prüfung des lokalen Gateways:

  * Sofern Sie nicht `--skip-health` übergeben, wartet das Onboarding auf ein erreichbares lokales Gateway, bevor es erfolgreich beendet wird.
  * `--install-daemon` startet zuerst den verwalteten Gateway-Installationspfad. Ohne diese Option müssen Sie bereits ein lokales Gateway ausführen, zum Beispiel `openclaw gateway run`.
  * Wenn Sie in der Automatisierung nur Konfigurations-/Workspace-/Bootstrap-Schreibvorgänge möchten, verwenden Sie `--skip-health`.
  * Wenn Sie Workspace-Dateien selbst verwalten, übergeben Sie `--skip-bootstrap`, um `agents.defaults.skipBootstrap: true` zu setzen und das Erstellen von `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md` und `BOOTSTRAP.md` zu überspringen.
  * Unter nativem Windows versucht `--install-daemon` zuerst Geplante Tasks und fällt auf einen Login-Eintrag im benutzerspezifischen Autostart-Ordner zurück, wenn die Task-Erstellung verweigert wird.


Interaktives Onboarding-Verhalten im Referenzmodus:

  * Wählen Sie **Geheime Referenz verwenden** , wenn Sie dazu aufgefordert werden.
  * Wählen Sie dann entweder: 
    * Umgebungsvariable
    * Konfigurierter Secret-Provider (`file` oder `exec`)
  * Das Onboarding führt vor dem Speichern der Referenz eine schnelle Preflight-Validierung durch. 
    * Wenn die Validierung fehlschlägt, zeigt das Onboarding den Fehler an und lässt Sie es erneut versuchen.


### Nicht interaktive Z.AI-Endpunktoptionen

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

Nicht interaktives Mistral-Beispiel:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## Ablaufhinweise

Flow types

  * `quickstart`: minimale Eingabeaufforderungen, generiert automatisch ein Gateway-Token.
  * `manual`: vollständige Eingabeaufforderungen für Port, Bind und Authentifizierung (Alias von `advanced`).
  * `import`: führt einen erkannten Migrations-Provider aus, zeigt eine Vorschau des Plans an und wendet ihn dann nach Bestätigung an.

Provider prefiltering

Wenn eine Authentifizierungsauswahl einen bevorzugten Provider impliziert, filtert das Onboarding die Picker für Standardmodell und Allowlist auf diesen Provider vor. Für Volcengine und BytePlus passt dies auch auf die Coding-Plan-Varianten (`volcengine-plan/*`, `byteplus-plan/*`).

Wenn der Filter für den bevorzugten Provider noch keine geladenen Modelle ergibt, fällt das Onboarding auf den ungefilterten Katalog zurück, statt den Picker leer zu lassen.

Web-search follow-ups

Einige Websuche-Provider lösen Provider-spezifische Folgeaufforderungen aus:

  * **Grok** kann eine optionale `x_search`-Einrichtung mit demselben `XAI_API_KEY` und einer `x_search`-Modellauswahl anbieten.
  * **Kimi** kann nach der Moonshot-API-Region (`api.moonshot.ai` vs. `api.moonshot.cn`) und dem standardmäßigen Kimi-Websuche-Modell fragen.

Other behaviors

  * DM-Scope-Verhalten des lokalen Onboardings: [CLI-Einrichtungsreferenz](</de/start/wizard-cli-reference#outputs-and-internals>).
  * Schnellster erster Chat: `openclaw dashboard` (Control UI, keine Kanaleinrichtung).
  * Benutzerdefinierter Provider: Verbinden Sie jeden OpenAI- oder Anthropic-kompatiblen Endpunkt, einschließlich gehosteter Provider, die nicht aufgeführt sind. Verwenden Sie Unknown für die automatische Erkennung.
  * Wenn Hermes-Status erkannt wird, bietet das Onboarding einen Migrationsablauf an. Verwenden Sie [Migrieren](</de/cli/migrate>) für Dry-Run-Pläne, Überschreibmodus, Berichte und genaue Zuordnungen.


## Häufige Folgekommandos

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

Verwenden Sie stattdessen `openclaw setup`, wenn Sie nur die Basiskonfiguration/den Basis-Workspace benötigen. Verwenden Sie später `openclaw configure` für gezielte Änderungen und `openclaw channels add` für reine Kanaleinrichtung.

Was this useful?YesNo