---
title: Modelle
source_url: https://docs.openclaw.ai/de/cli/models
scraped_at: 2026-05-25
---

# `openclaw models`

Modellerkennung, Scans und Konfiguration (Standardmodell, Fallbacks, Auth-Profile).

Verwandt:

  * Provider + Modelle: [Modelle](</de/providers/models>)
  * Konzepte zur Modellauswahl + Slash-Befehl `/models`: [Modellkonzept](</de/concepts/models>)
  * Einrichtung der Provider-Authentifizierung: [Erste Schritte](</de/start/getting-started>)


## Häufige Befehle

bashCopy code
[code]
    openclaw models statusopenclaw models listopenclaw models set <model-or-alias>openclaw models scan
[/code]

`openclaw models status` zeigt den aufgelösten Standardwert/die Fallbacks sowie eine Auth-Übersicht. Wenn Snapshots zur Provider-Nutzung verfügbar sind, enthält der Abschnitt zum OAuth-/API-Schlüsselstatus Nutzungsfenster und Quota-Snapshots der Provider. Aktuelle Provider mit Nutzungsfenstern: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi und [z.ai](<http://z.ai>). Die Nutzungs-Authentifizierung stammt aus Provider-spezifischen Hooks, wenn verfügbar; andernfalls greift OpenClaw auf passende OAuth-/API-Schlüssel- Anmeldedaten aus Auth-Profilen, Umgebung oder Konfiguration zurück. In der Ausgabe `--json` ist `auth.providers` die umgebungs-/konfigurations-/speicherbewusste Provider- Übersicht, während `auth.oauth` nur den Zustand der Profile im Auth-Speicher darstellt. Fügen Sie `--probe` hinzu, um Live-Auth-Prüfungen für jedes konfigurierte Provider-Profil auszuführen. Prüfungen sind echte Anfragen (sie können Tokens verbrauchen und Rate Limits auslösen). Verwenden Sie `--agent <id>`, um den Modell-/Auth-Zustand eines konfigurierten Agents zu prüfen. Wenn dies weggelassen wird, verwendet der Befehl `OPENCLAW_AGENT_DIR`/`PI_CODING_AGENT_DIR`, falls gesetzt, andernfalls den konfigurierten Standard-Agent. Prüfzeilen können aus Auth-Profilen, Umgebungs-Anmeldedaten oder `models.json` stammen. Für die Fehlerbehebung bei Codex OAuth sind `openclaw models status`, `openclaw models auth list --provider openai-codex` und `openclaw config get agents.defaults.model --json` der schnellste Weg, um zu bestätigen, ob ein Agent über ein verwendbares `openai-codex`-Auth-Profil für `openai/*` über die native Codex-Laufzeit verfügt. Siehe [Einrichtung des OpenAI-Providers](</de/providers/openai#check-and-recover-codex-oauth-routing>).

Hinweise:

  * `models set <model-or-alias>` akzeptiert `provider/model` oder einen Alias.
  * `models list` ist schreibgeschützt: Es liest Konfiguration, Auth-Profile, vorhandenen Katalog- Zustand und Provider-eigene Katalogzeilen, schreibt aber `models.json` nicht neu.
  * Die Spalte `Auth` ist Provider-bezogen und schreibgeschützt. Sie wird aus lokalen Auth-Profilmetadaten, Umgebungsmarkern, konfigurierten Provider-Schlüsseln, Local-Provider- Markern, AWS-Bedrock-Umgebungs-/Profilmarkern und synthetischen Plugin-Auth-Metadaten berechnet; sie lädt keine Provider-Laufzeit, liest keine Schlüsselbund-Geheimnisse, ruft keine Provider- APIs auf und weist keine exakte Ausführungsbereitschaft pro Modell nach.
  * `models list --all --provider <id>` kann Provider-eigene statische Katalogzeilen aus Plugin-Manifesten oder gebündelten Provider-Katalogmetadaten enthalten, selbst wenn Sie sich noch nicht bei diesem Provider authentifiziert haben. Diese Zeilen werden weiterhin als nicht verfügbar angezeigt, bis passende Authentifizierung konfiguriert ist.
  * `models list` hält die Steuerungsebene reaktionsfähig, während die Provider-Katalogerkennung langsam ist. Die Standard- und konfigurierten Ansichten fallen nach kurzer Wartezeit auf konfigurierte oder synthetische Modellzeilen zurück und lassen die Erkennung im Hintergrund abschließen. Verwenden Sie `--all`, wenn Sie den exakten vollständigen erkannten Katalog benötigen und bereit sind, auf die Provider-Erkennung zu warten.
  * Breite `models list --all`-Aufrufe führen Manifest-Katalogzeilen über Registry-Zeilen zusammen, ohne Provider-Laufzeit-Supplement-Hooks zu laden. Provider-gefilterte Manifest- Schnellpfade verwenden nur Provider, die als `static` markiert sind; Provider, die als `refreshable` markiert sind, bleiben Registry-/Cache-gestützt und hängen Manifestzeilen als Ergänzungen an, während Provider, die als `runtime` markiert sind, bei Registry-/Laufzeiterkennung bleiben.
  * `models list` hält native Modellmetadaten und Laufzeitobergrenzen getrennt. In der Tabellen- Ausgabe zeigt `Ctx` `contextTokens/contextWindow`, wenn eine effektive Laufzeitobergrenze vom nativen Kontextfenster abweicht; JSON-Zeilen enthalten `contextTokens`, wenn ein Provider diese Obergrenze bereitstellt.
  * `models list --provider <id>` filtert nach Provider-ID, zum Beispiel `moonshot` oder `openai-codex`. Anzeigenamen aus interaktiven Provider-Auswahlen, wie `Moonshot AI`, werden nicht akzeptiert.
  * Modellreferenzen werden durch Aufteilen am **ersten** `/` geparst. Wenn die Modell-ID `/` enthält (OpenRouter-Stil), geben Sie das Provider-Präfix an (Beispiel: `openrouter/moonshotai/kimi-k2`).
  * Wenn Sie den Provider weglassen, löst OpenClaw die Eingabe zuerst als Alias auf, dann als eindeutige Übereinstimmung bei konfigurierten Providern für genau diese Modell-ID und erst danach mit einer Deprecation-Warnung auf den konfigurierten Standard-Provider. Wenn dieser Provider das konfigurierte Standardmodell nicht mehr bereitstellt, fällt OpenClaw auf den ersten konfigurierten Provider/das erste konfigurierte Modell zurück, statt einen veralteten Standard eines entfernten Providers anzuzeigen.
  * `models status` kann in der Auth-Ausgabe `marker(<value>)` für nicht geheime Platzhalter anzeigen (zum Beispiel `OPENAI_API_KEY`, `secretref-managed`, `minimax-oauth`, `oauth:chutes`, `ollama-local`), statt sie als Geheimnisse zu maskieren.


### Modellscan

`models scan` liest den öffentlichen `:free`-Katalog von OpenRouter und bewertet Kandidaten für die Fallback-Nutzung. Der Katalog selbst ist öffentlich, daher benötigen Metadaten-only-Scans keinen OpenRouter-Schlüssel.

Standardmäßig versucht OpenClaw, Tool- und Bildunterstützung mit Live-Modellaufrufen zu prüfen. Wenn kein OpenRouter-Schlüssel konfiguriert ist, fällt der Befehl auf Metadaten-only- Ausgabe zurück und erklärt, dass `:free`-Modelle weiterhin `OPENROUTER_API_KEY` für Prüfungen und Inferenz benötigen.

Optionen:

  * `--no-probe` (nur Metadaten; keine Konfigurations-/Geheimnissuche)
  * `--min-params <b>`
  * `--max-age-days <days>`
  * `--provider <name>`
  * `--max-candidates <n>`
  * `--timeout <ms>` (Kataloganfrage und Timeout pro Prüfung)
  * `--concurrency <n>`
  * `--yes`
  * `--no-input`
  * `--set-default`
  * `--set-image`
  * `--json`


`--set-default` und `--set-image` erfordern Live-Prüfungen; Metadaten-only-Scan- Ergebnisse sind informativ und werden nicht auf die Konfiguration angewendet.

### Modellstatus

Optionen:

  * `--json`
  * `--plain`
  * `--check` (Exit 1=abgelaufen/fehlend, 2=läuft bald ab)
  * `--probe` (Live-Prüfung konfigurierter Auth-Profile)
  * `--probe-provider <name>` (einen Provider prüfen)
  * `--probe-profile <id>` (Profil-IDs wiederholt oder kommagetrennt)
  * `--probe-timeout <ms>`
  * `--probe-concurrency <n>`
  * `--probe-max-tokens <n>`
  * `--agent <id>` (konfigurierte Agent-ID; überschreibt `OPENCLAW_AGENT_DIR`/`PI_CODING_AGENT_DIR`)


`--json` hält stdout für die JSON-Nutzdaten reserviert. Auth-Profil-, Provider- und Startdiagnosen werden an stderr geleitet, damit Skripte stdout direkt in Tools wie `jq` leiten können.

Statusgruppen für Prüfungen:

  * `ok`
  * `auth`
  * `rate_limit`
  * `billing`
  * `timeout`
  * `format`
  * `unknown`
  * `no_model`


Zu erwartende Detail-/Reason-Code-Fälle für Prüfungen:

  * `excluded_by_auth_order`: Ein gespeichertes Profil existiert, aber explizites `auth.order.<provider>` hat es ausgelassen, daher meldet die Prüfung den Ausschluss, statt es auszuprobieren.
  * `missing_credential`, `invalid_expires`, `expired`, `unresolved_ref`: Profil ist vorhanden, aber nicht berechtigt/auflösbar.
  * `no_model`: Provider-Authentifizierung existiert, aber OpenClaw konnte keinen prüfbaren Modellkandidaten für diesen Provider auflösen.


## Aliasse + Fallbacks

bashCopy code
[code]
    openclaw models aliases listopenclaw models fallbacks list
[/code]

## Auth-Profile

bashCopy code
[code]
    openclaw models auth addopenclaw models auth list [--provider <id>] [--json]openclaw models auth login --provider <id>openclaw models auth setup-token --provider <id>openclaw models auth paste-token
[/code]

`models auth add` ist der interaktive Auth-Helfer. Er kann je nach ausgewähltem Provider einen Provider-Auth-Ablauf (OAuth/API-Schlüssel) starten oder Sie zum manuellen Einfügen eines Tokens führen.

`models auth list` listet gespeicherte Auth-Profile für den ausgewählten Agent auf, ohne Token-, API-Schlüssel- oder OAuth-Geheimmaterial auszugeben. Verwenden Sie `--provider <id>`, um auf einen Provider zu filtern, zum Beispiel `openai-codex`, und `--json` für Skripting.

`models auth login` führt den Auth-Ablauf (OAuth/API-Schlüssel) eines Provider-Plugins aus. Verwenden Sie `openclaw plugins list`, um zu sehen, welche Provider installiert sind. Verwenden Sie `openclaw models auth --agent <id> <subcommand>`, um Auth-Ergebnisse in einen bestimmten konfigurierten Agent-Speicher zu schreiben. Das übergeordnete Flag `--agent` wird von `add`, `list`, `login`, `setup-token`, `paste-token` und `login-github-copilot` berücksichtigt.

Für OpenAI-Modelle ist `--provider openai` standardmäßig die Anmeldung mit ChatGPT-/Codex-Konto. Verwenden Sie `--method api-key` nur, wenn Sie ein OpenAI-API-Schlüsselprofil hinzufügen möchten, üblicherweise als Absicherung für Codex-Abonnementlimits. Die ältere Schreibweise `--provider openai-codex` funktioniert weiterhin für bestehende Skripte.

Beispiele:

bashCopy code
[code]
    openclaw models auth login --provider openai --set-defaultopenclaw models auth login --provider openai --method api-keyopenclaw models auth list --provider openai
[/code]

Hinweise:

  * `setup-token` und `paste-token` bleiben generische Token-Befehle für Provider, die Token-Auth-Methoden bereitstellen.
  * `setup-token` erfordert ein interaktives TTY und führt die Token-Auth- Methode des Providers aus (standardmäßig die Methode `setup-token` dieses Providers, wenn er eine bereitstellt).
  * `paste-token` akzeptiert eine Token-Zeichenfolge, die anderswo oder durch Automatisierung erzeugt wurde.
  * `paste-token` erfordert `--provider`, fragt nach dem Tokenwert und schreibt ihn in die Standardprofil-ID `<provider>:manual`, sofern Sie nicht `--profile-id` übergeben.
  * `paste-token --expires-in <duration>` speichert einen absoluten Token-Ablauf aus einer relativen Dauer wie `365d` oder `12h`.
  * Hinweis zu Anthropic: Mitarbeitende von Anthropic haben uns mitgeteilt, dass Claude-CLI-Nutzung im OpenClaw-Stil wieder erlaubt ist. Daher behandelt OpenClaw die Wiederverwendung der Claude CLI und die Nutzung von `claude -p` für diese Integration als genehmigt, sofern Anthropic keine neue Richtlinie veröffentlicht.
  * Anthropic `setup-token` / `paste-token` bleiben als unterstützter OpenClaw-Token-Pfad verfügbar, aber OpenClaw bevorzugt jetzt die Wiederverwendung der Claude CLI und `claude -p`, wenn verfügbar.


## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Modellauswahl](</de/concepts/model-providers>)
  * [Modell-Failover](</de/concepts/model-failover>)


Was this useful?YesNo