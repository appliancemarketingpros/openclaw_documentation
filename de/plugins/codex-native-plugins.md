---
title: Native Codex-Plugins
source_url: https://docs.openclaw.ai/de/plugins/codex-native-plugins
scraped_at: 2026-05-25
---

Native Codex-Plugin-Unterstützung ermöglicht einem OpenClaw-Agenten im Codex-Modus, die eigenen App- und Plugin-Fähigkeiten des Codex-App-Servers in demselben Codex-Thread zu verwenden, der den OpenClaw-Turn verarbeitet.

OpenClaw übersetzt Codex-Plugins nicht in synthetische dynamische `codex_plugin_*`-Tools von OpenClaw. Plugin-Aufrufe bleiben im nativen Codex-Transkript, und der Codex-App-Server ist für die App-gestützte MCP-Ausführung zuständig.

Verwenden Sie diese Seite, nachdem der grundlegende [Codex-Harness](</de/plugins/codex-harness>) funktioniert.

## Anforderungen

  * Die ausgewählte OpenClaw-Agent-Laufzeit muss der native Codex-Harness sein.
  * `plugins.entries.codex.enabled` muss true sein.
  * `plugins.entries.codex.config.codexPlugins.enabled` muss true sein.
  * V1 unterstützt nur `openai-curated`-Plugins, die die Migration im Quell-Codex-Home als aus der Quelle installiert erkannt hat.
  * Der Ziel-Codex-App-Server muss das erwartete Marketplace-, Plugin- und App-Inventar sehen können.


`codexPlugins` hat keine Wirkung auf PI-Läufe, normale OpenAI-Provider-Läufe, ACP-Konversationsbindungen oder andere Harnesses, weil diese Pfade keine Codex-App-Server-Threads mit nativer `apps`-Konfiguration erstellen.

## Schnellstart

Migration aus dem Quell-Codex-Home in der Vorschau anzeigen:

bashCopy code
[code]
    openclaw migrate codex --dry-run
[/code]

Verwenden Sie strenge Quell-App-Verifizierung, wenn die Migration die Erreichbarkeit der Quell-App prüfen soll, bevor die native Plugin-Aktivierung geplant wird:

bashCopy code
[code]
    openclaw migrate codex --dry-run --verify-plugin-apps
[/code]

Wenden Sie die Migration an, wenn der Plan richtig aussieht:

bashCopy code
[code]
    openclaw migrate apply codex --yes
[/code]

Die Migration schreibt explizite `codexPlugins`-Einträge für berechtigte Plugins und ruft Codex-App-Server `plugin/install` für ausgewählte Plugins auf. Eine typische migrierte Konfiguration sieht so aus:

json5Copy code
[code]
    {  plugins: {    entries: {      codex: {        enabled: true,        config: {          codexPlugins: {            enabled: true,            allow_destructive_actions: true,            plugins: {              "google-calendar": {                enabled: true,                marketplaceName: "openai-curated",                pluginName: "google-calendar",              },            },          },        },      },    },  },}
[/code]

Nach dem Ändern von `codexPlugins` verwenden Sie `/new`, `/reset` oder starten Sie den Gateway neu, damit zukünftige Codex-Harness-Sitzungen mit dem aktualisierten App-Satz starten.

## Funktionsweise der nativen Plugin-Einrichtung

Die Integration hat drei separate Zustände:

  * Installiert: Codex hat das lokale Plugin-Bundle in der Ziel-App-Server-Laufzeit.
  * Aktiviert: Die OpenClaw-Konfiguration ist bereit, das Plugin für Codex-Harness-Turns verfügbar zu machen.
  * Erreichbar: Der Codex-App-Server bestätigt, dass die App-Einträge des Plugins für das aktive Konto verfügbar sind und der migrierten Plugin-Identität zugeordnet werden können.


Die Migration ist der dauerhafte Installations- und Berechtigungsschritt. Während der Planung liest OpenClaw Quell-Codex-Details aus `plugin/read` und prüft, ob die Kontoantwort des Quell-Codex-App-Servers ein ChatGPT-Abonnementkonto ist. Nicht-ChatGPT-Kontoantworten oder fehlende Kontoantworten überspringen App-gestützte Plugins mit `codex_subscription_required`. Standardmäßig ruft die Migration kein Quell-`app/list` auf; App-gestützte Quell-Plugins, die die Konto-Schranke bestehen, werden ohne Verifizierung der Quell-App-Erreichbarkeit geplant, und Transportfehler bei der Kontoabfrage überspringen mit `codex_account_unavailable`. Mit `--verify-plugin-apps` erstellt die Migration einen frischen Quell-`app/list`-Snapshot und verlangt, dass jede eigene App vorhanden, aktiviert und erreichbar ist, bevor die native Aktivierung geplant wird. In diesem Modus fallen Transportfehler bei der Kontoabfrage auf die Quell-App-Inventar-Schranke zurück. Das Laufzeit-App-Inventar ist die Erreichbarkeitsprüfung der Zielsitzung nach der Migration. Die Einrichtung der Codex-Harness-Sitzung berechnet dann eine restriktive Thread-App-Konfiguration für die aktivierten und erreichbaren Plugin-Apps.

Die Thread-App-Konfiguration wird berechnet, wenn OpenClaw eine Codex-Harness-Sitzung einrichtet oder eine veraltete Codex-Thread-Bindung ersetzt. Sie wird nicht bei jedem Turn neu berechnet.

## V1-Unterstützungsgrenze

V1 ist absichtlich eng gefasst:

  * Nur `openai-curated`-Plugins, die bereits im App-Server-Inventar des Quell-Codex installiert waren, sind für die Migration berechtigt.
  * App-gestützte Quell-Plugins müssen die Abonnement-Schranke zur Migrationszeit bestehen. `--verify-plugin-apps` fügt die Quell-App-Inventar-Schranke hinzu. Konten, die durch Abonnements gesperrt sind, sowie im Verifizierungsmodus nicht erreichbare, deaktivierte oder fehlende Quell-Apps oder fehlgeschlagene Aktualisierungen des Quell-App-Inventars werden als übersprungene manuelle Elemente statt als aktivierte Konfigurationseinträge gemeldet. Nicht lesbare Plugin-Details werden vor der Quell-App-Inventar-Schranke übersprungen.
  * Die Migration schreibt explizite Plugin-Identitäten mit `marketplaceName` und `pluginName`; sie schreibt keine lokalen `marketplacePath`-Cache-Pfade.
  * `codexPlugins.enabled` ist der globale Aktivierungsschalter.
  * Es gibt keinen `plugins["*"]`-Wildcard und keinen Konfigurationsschlüssel, der beliebige Installationsberechtigung gewährt.
  * Nicht unterstützte Marketplaces, gecachte Plugin-Bundles, Hooks und Codex-Konfigurationsdateien werden im Migrationsbericht zur manuellen Prüfung beibehalten.


## App-Inventar und Eigentümerschaft

OpenClaw liest das Codex-App-Inventar über App-Server `app/list`, cached es eine Stunde lang und aktualisiert veraltete oder fehlende Einträge asynchron. Der Cache liegt nur im Arbeitsspeicher; ein Neustart der CLI oder des Gateway verwirft ihn, und OpenClaw baut ihn aus dem nächsten `app/list`-Lesevorgang neu auf.

Migration und Laufzeit verwenden separate Cache-Schlüssel:

  * Die Quell-Migrationsverifizierung verwendet das Quell-Codex-Home und die Startoptionen des Quell-App-Servers. Dies läuft nur, wenn `--verify-plugin-apps` gesetzt ist, und erzwingt eine frische Quell-`app/list`-Traversal für diesen Planungslauf.
  * Die Ziellaufzeit-Einrichtung verwendet die Codex-App-Server-Identität des Zielagenten, wenn sie die Codex-Thread-App-Konfiguration erstellt. Die Plugin-Aktivierung invalidiert diesen Ziel-Cache-Schlüssel und aktualisiert ihn danach nach `plugin/install` erzwungen.


Eine Plugin-App wird nur offengelegt, wenn OpenClaw sie über stabile Eigentümerschaft dem migrierten Plugin zuordnen kann:

  * exakte App-ID aus Plugin-Details
  * bekannter MCP-Servername
  * eindeutige stabile Metadaten


Nur Anzeigename oder mehrdeutige Eigentümerschaft wird ausgeschlossen, bis die nächste Inventaraktualisierung die Eigentümerschaft belegt.

## Thread-App-Konfiguration

OpenClaw injiziert einen restriktiven `config.apps`-Patch für den Codex-Thread: `_default` ist deaktiviert, und nur Apps, die aktivierten migrierten Plugins gehören, sind aktiviert.

OpenClaw setzt `destructive_enabled` auf App-Ebene aus der effektiven globalen oder Plugin-spezifischen `allow_destructive_actions`-Richtlinie und lässt Codex destruktive Tool-Metadaten aus seinen nativen App-Tool-Annotationen erzwingen. Die `_default`-App-Konfiguration ist mit `open_world_enabled: false` deaktiviert. Aktivierte Plugin-Apps werden mit `open_world_enabled: true` ausgegeben; OpenClaw stellt keinen separaten Plugin-Regler für Open-World-Richtlinien bereit und pflegt keine Plugin-spezifischen Ablehnungslisten für destruktive Tool-Namen.

Der Tool-Genehmigungsmodus ist standardmäßig automatisch für Plugin-Apps, sodass nicht destruktive Lesetools ohne Genehmigungs-UI im selben Thread ausgeführt werden können. Destruktive Tools bleiben durch die `destructive_enabled`-Richtlinie der jeweiligen App gesteuert.

## Richtlinie für destruktive Aktionen

Destruktive Plugin-Elicitations sind für migrierte Codex-Plugins standardmäßig erlaubt, während unsichere Schemas und mehrdeutige Eigentümerschaft weiterhin geschlossen fehlschlagen:

  * Globales `allow_destructive_actions` ist standardmäßig `true`.
  * Plugin-spezifisches `allow_destructive_actions` überschreibt die globale Richtlinie für dieses Plugin.
  * Wenn die Richtlinie `false` ist, gibt OpenClaw eine deterministische Ablehnung zurück.
  * Wenn die Richtlinie `true` ist, akzeptiert OpenClaw automatisch nur sichere Schemas, die es einer Genehmigungsantwort zuordnen kann, etwa einem booleschen Genehmigungsfeld.
  * Fehlende Plugin-Identität, mehrdeutige Eigentümerschaft, eine fehlende Turn-ID, eine falsche Turn-ID oder ein unsicheres Elicitation-Schema führen zur Ablehnung statt zu einer Nachfrage.


## Fehlerbehebung

**`auth_required`:** Die Migration hat das Plugin installiert, aber eine seiner Apps benötigt noch Authentifizierung. Der explizite Plugin-Eintrag wird deaktiviert geschrieben, bis Sie es erneut autorisieren und aktivieren.

**`app_inaccessible`, `app_disabled` oder `app_missing`:** Die Migration hat das Plugin nicht installiert, weil das Quell-Codex-App-Inventar nicht alle eigenen Apps als vorhanden, aktiviert und erreichbar angezeigt hat, während `--verify-plugin-apps` gesetzt war. Autorisieren oder aktivieren Sie die App in Codex erneut und führen Sie die Migration dann erneut mit `--verify-plugin-apps` aus.

**`app_inventory_unavailable`:** Die Migration hat das Plugin nicht installiert, weil strenge Quell-App-Verifizierung angefordert wurde und die Aktualisierung des Quell-Codex-App-Inventars fehlgeschlagen ist. Beheben Sie den Zugriff auf den Quell-Codex-App-Server oder versuchen Sie es ohne `--verify-plugin-apps` erneut, wenn Sie den schnelleren kontogesteuerten Plan akzeptieren.

**`codex_subscription_required`:** Die Migration hat das App-gestützte Plugin nicht installiert, weil das Konto des Quell-Codex-App-Servers nicht mit einem ChatGPT-Abonnementkonto angemeldet war. Melden Sie sich in der Codex-App mit Abonnementauthentifizierung an und führen Sie die Migration dann erneut aus.

**`codex_account_unavailable`:** Die Migration hat das App-gestützte Plugin nicht installiert, weil das Konto des Quell-Codex-App-Servers nicht gelesen werden konnte. Beheben Sie die Authentifizierung des Quell-Codex-App-Servers oder führen Sie erneut mit `--verify-plugin-apps` aus, wenn das Quell-App-Inventar bei fehlgeschlagener Kontoabfrage über die Berechtigung entscheiden soll.

**`marketplace_missing` oder `plugin_missing`:** Der Ziel-Codex-App-Server kann den erwarteten `openai-curated`-Marketplace oder das Plugin nicht sehen. Führen Sie die Migration erneut gegen die Ziellaufzeit aus oder prüfen Sie den Plugin-Status des Codex-App-Servers.

**`app_inventory_missing` oder `app_inventory_stale`:** Die App-Bereitschaft stammt aus einem leeren oder veralteten Cache. OpenClaw plant eine asynchrone Aktualisierung und schließt Plugin-Apps aus, bis Eigentümerschaft und Bereitschaft bekannt sind.

**`app_ownership_ambiguous`:** Das App-Inventar stimmte nur nach Anzeigename überein, daher wird die App dem Codex-Thread nicht offengelegt.

**Konfiguration geändert, aber der Agent kann das Plugin nicht sehen:** Verwenden Sie `/new`, `/reset` oder starten Sie den Gateway neu. Bestehende Codex-Thread-Bindungen behalten die App-Konfiguration, mit der sie gestartet wurden, bis OpenClaw eine neue Harness-Sitzung einrichtet oder eine veraltete Bindung ersetzt.

**Destruktive Aktion wird abgelehnt:** Prüfen Sie die globalen und Plugin-spezifischen `allow_destructive_actions`-Werte. Selbst wenn die Richtlinie true ist, schlagen unsichere Elicitation-Schemas und mehrdeutige Plugin-Identität weiterhin geschlossen fehl.

## Verwandte Themen

  * [Codex-Harness](</de/plugins/codex-harness>)
  * [Codex-Harness-Referenz](</de/plugins/codex-harness-reference>)
  * [Codex-Harness-Laufzeit](</de/plugins/codex-harness-runtime>)
  * [Konfigurationsreferenz](</de/gateway/configuration-reference#codex-harness-plugin-config>)
  * [Migrate-CLI](</de/cli/migrate>)


Was this useful?YesNo