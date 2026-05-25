---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/de/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot ist GitHubs KI-Coding-Assistent. Er bietet Zugriff auf Copilot-Modelle für Ihr GitHub-Konto und Ihren Plan. OpenClaw kann Copilot auf zwei verschiedene Arten als Modell-Provider verwenden.

## Zwei Möglichkeiten, Copilot in OpenClaw zu verwenden

### Integrierter Provider (github-copilot)

Verwenden Sie den nativen Geräte-Login-Ablauf, um ein GitHub-Token zu erhalten, und tauschen Sie es dann gegen Copilot-API-Token aus, wenn OpenClaw ausgeführt wird. Dies ist der **standardmäßige** und einfachste Weg, da dafür kein VS Code erforderlich ist.

* ### Login-Befehl ausführen

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Sie werden aufgefordert, eine URL aufzurufen und einen Einmalcode einzugeben. Lassen Sie das Terminal geöffnet, bis der Vorgang abgeschlossen ist.

* ### Standardmodell festlegen

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Oder in der Konfiguration:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Copilot Proxy-Plugin (copilot-proxy)

Verwenden Sie die VS Code-Erweiterung **Copilot Proxy** als lokale Bridge. OpenClaw kommuniziert mit dem `/v1`-Endpoint des Proxy und verwendet die dort konfigurierte Modellliste.

## Optionale Flags

Flag | Beschreibung  
---|---  
`--yes` | Bestätigungsabfrage überspringen  
`--set-default` | Auch das empfohlene Standardmodell des Providers anwenden  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Nicht interaktives Onboarding

Wenn Sie bereits ein GitHub-OAuth-Zugriffstoken für Copilot haben, importieren Sie es während der Headless-Einrichtung mit `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Sie können `--auth-choice` auch weglassen; die Übergabe von `--github-copilot-token` leitet die Auth-Auswahl für den GitHub Copilot-Provider ab. Wenn das Flag weggelassen wird, fällt das Onboarding auf `COPILOT_GITHUB_TOKEN`, `GH_TOKEN` und dann `GITHUB_TOKEN` zurück. Verwenden Sie `--secret-input-mode ref` mit gesetztem `COPILOT_GITHUB_TOKEN`, um ein env-gestütztes `tokenRef` statt Klartext in `auth-profiles.json` zu speichern.

Interaktives TTY erforderlich

Der Geräte-Login-Ablauf erfordert ein interaktives TTY. Führen Sie ihn direkt in einem Terminal aus, nicht in einem nicht interaktiven Skript oder einer CI-Pipeline.

Modellverfügbarkeit hängt von Ihrem Plan ab

Die Verfügbarkeit von Copilot-Modellen hängt von Ihrem GitHub-Plan ab. Wenn ein Modell abgelehnt wird, versuchen Sie eine andere ID (zum Beispiel `github-copilot/gpt-4.1`).

Live-Katalogaktualisierung über die Copilot-API

Sobald der Geräte-Login- oder Env-Var-Auth-Pfad ein GitHub-Token aufgelöst hat, aktualisiert OpenClaw den Modellkatalog bei Bedarf über `${baseUrl}/models` (denselben Endpoint, den VS Code Copilot verwendet), sodass die Runtime kontospezifische Berechtigungen und genaue Kontextfenster ohne Manifest- Änderungen verfolgt. Neu veröffentlichte Copilot-Modelle werden ohne OpenClaw- Upgrade sichtbar, und Kontextfenster spiegeln die realen Limits pro Modell wider (z. B. 400k für die gpt-5.x-Serie, 1M für die internen `claude-opus-*-1m`-Varianten).

Der gebündelte statische Katalog bleibt der sichtbare Fallback, wenn Discovery deaktiviert ist, der Benutzer kein GitHub-Auth-Profil hat, der Token-Austausch fehlschlägt oder der HTTPS-Aufruf an `/models` einen Fehler zurückgibt. Um dies zu deaktivieren und sich vollständig auf den statischen Manifest-Katalog zu verlassen (Offline-/Air-Gapped-Szenarien):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Transportauswahl

Claude-Modell-IDs verwenden automatisch den Anthropic Messages-Transport. GPT-, o-Series- und Gemini-Modelle behalten den OpenAI Responses-Transport. OpenClaw wählt den richtigen Transport anhand der Modell-Ref aus.

Request-Kompatibilität

OpenClaw sendet Copilot-IDE-artige Request-Header auf Copilot-Transporten, einschließlich integrierter Compaction, Tool-Ergebnis- und Bild-Follow-up-Turns. Es aktiviert keine Responses-Fortsetzung auf Provider-Ebene für Copilot, es sei denn, dieses Verhalten wurde gegen Copilots API verifiziert.

Auflösungsreihenfolge von Umgebungsvariablen

OpenClaw löst Copilot-Auth aus Umgebungsvariablen in der folgenden Prioritätsreihenfolge auf:

Priorität | Variable | Hinweise  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Höchste Priorität, Copilot-spezifisch  
2 | `GH_TOKEN` | GitHub-CLI-Token (Fallback)  
3 | `GITHUB_TOKEN` | Standard-GitHub-Token (niedrigste)  
  
Wenn mehrere Variablen gesetzt sind, verwendet OpenClaw die mit der höchsten Priorität. Der Geräte-Login-Ablauf (`openclaw models auth login-github-copilot`) speichert sein Token im Auth-Profilspeicher und hat Vorrang vor allen Umgebungsvariablen.

Token-Speicherung

Der Login speichert ein GitHub-Token im Auth-Profilspeicher und tauscht es gegen ein Copilot-API-Token aus, wenn OpenClaw ausgeführt wird. Sie müssen das Token nicht manuell verwalten.

## Embeddings für Memory-Suche

GitHub Copilot kann auch als Embedding-Provider für [Memory-Suche](</de/concepts/memory-search>) dienen. Wenn Sie ein Copilot-Abonnement haben und angemeldet sind, kann OpenClaw es ohne separaten API-Schlüssel für Embeddings verwenden.

### Automatische Erkennung

Wenn `memorySearch.provider` `"auto"` ist (die Standardeinstellung), wird GitHub Copilot mit Priorität 15 versucht -- nach lokalen Embeddings, aber vor OpenAI und anderen kostenpflichtigen Providern. Wenn ein GitHub-Token verfügbar ist, entdeckt OpenClaw verfügbare Embedding-Modelle über die Copilot-API und wählt automatisch das beste aus.

### Explizite Konfiguration

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Funktionsweise

  1. OpenClaw löst Ihr GitHub-Token auf (aus Env-Vars oder Auth-Profil).
  2. Tauscht es gegen ein kurzlebiges Copilot-API-Token aus.
  3. Fragt den Copilot-Endpoint `/models` ab, um verfügbare Embedding-Modelle zu entdecken.
  4. Wählt das beste Modell aus (bevorzugt `text-embedding-3-small`).
  5. Sendet Embedding-Requests an den Copilot-Endpoint `/embeddings`.


Die Modellverfügbarkeit hängt von Ihrem GitHub-Plan ab. Wenn keine Embedding-Modelle verfügbar sind, überspringt OpenClaw Copilot und versucht den nächsten Provider.

## Verwandt

[**Modellauswahl** Provider, Modell-Refs und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**OAuth und Auth** Auth-Details und Regeln zur Wiederverwendung von Zugangsdaten. ](</de/gateway/authentication>)

Was this useful?YesNo