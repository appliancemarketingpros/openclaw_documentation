---
title: Skills
source_url: https://docs.openclaw.ai/de/tools/skills
scraped_at: 2026-05-25
---

OpenClaw verwendet **[AgentSkills](<https://agentskills.io>)-kompatible** Skill-Ordner, um dem Agenten beizubringen, wie er Tools verwendet. Jeder Skill ist ein Verzeichnis, das eine `SKILL.md` mit YAML-Frontmatter und Anweisungen enthält. OpenClaw lädt gebündelte Skills sowie optionale lokale Überschreibungen und filtert sie zur Ladezeit basierend auf Umgebung, Konfiguration und Vorhandensein von Binaries.

## Speicherorte und Priorität

OpenClaw lädt Skills aus diesen Quellen, **höchste Priorität zuerst** :

# | Quelle | Pfad  
---|---|---  
1 | Workspace-Skills | `<workspace>/skills`  
2 | Projekt-Agent-Skills | `<workspace>/.agents/skills`  
3 | Persönliche Agent-Skills | `~/.agents/skills`  
4 | Verwaltete/lokale Skills | `~/.openclaw/skills`  
5 | Gebündelte Skills | mit der Installation ausgeliefert  
6 | Zusätzliche Skill-Ordner | `skills.load.extraDirs` (Konfiguration)  
  
Wenn ein Skill-Name kollidiert, gewinnt die Quelle mit der höchsten Priorität.

Das native Verzeichnis `$CODEX_HOME/skills` der Codex CLI gehört nicht zu diesen OpenClaw-Skill-Roots. Im Codex-Harness-Modus verwenden lokale App-Server-Starts isolierte Codex-Homes pro Agent, daher werden persönliche Codex CLI-Skills nicht implizit geladen. Verwenden Sie `openclaw migrate codex --dry-run`, um sie zu inventarisieren, und `openclaw migrate codex`, um Skill-Verzeichnisse über eine interaktive Checkbox-Eingabe auszuwählen, bevor sie in den aktuellen OpenClaw-Agent-Workspace kopiert werden. Für nicht interaktive Läufe wiederholen Sie `--skill <name>` für die exakt zu kopierenden Skills.

## Agent-spezifische und gemeinsam genutzte Skills

In **Multi-Agent** -Setups hat jeder Agent seinen eigenen Workspace:

Geltungsbereich | Pfad | Sichtbar für  
---|---|---  
Agent-spezifisch | `<workspace>/skills` | Nur diesen Agent  
Projekt-Agent | `<workspace>/.agents/skills` | Nur den Agent dieses Workspaces  
Persönlicher Agent | `~/.agents/skills` | Alle Agenten auf dieser Maschine  
Gemeinsam verwaltet/lokal | `~/.openclaw/skills` | Alle Agenten auf dieser Maschine  
Gemeinsame zusätzliche Verzeichnisse | `skills.load.extraDirs` (niedrigste Priorität) | Alle Agenten auf dieser Maschine  
  
Gleicher Name an mehreren Stellen → Quelle mit der höchsten Priorität gewinnt. Workspace schlägt Projekt-Agent, schlägt persönlichen Agent, schlägt verwaltet/lokal, schlägt gebündelt, schlägt zusätzliche Verzeichnisse.

## Agent-Skill-Allowlists

Skill-**Speicherort** und Skill-**Sichtbarkeit** sind getrennte Steuerungen. Speicherort/Priorität entscheidet, welche Kopie eines gleichnamigen Skills gewinnt; Agent-Allowlists entscheiden, welche Skills ein Agent tatsächlich verwenden kann.

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"],    },    list: [      { id: "writer" }, // inherits github, weather      { id: "docs", skills: ["docs-search"] }, // replaces defaults      { id: "locked-down", skills: [] }, // no skills    ],  },}
[/code]

Allowlist-Regeln

  * Lassen Sie `agents.defaults.skills` weg, um Skills standardmäßig uneingeschränkt zuzulassen.
  * Lassen Sie `agents.list[].skills` weg, um `agents.defaults.skills` zu erben.
  * Setzen Sie `agents.list[].skills: []`, um keine Skills zuzulassen.
  * Eine nicht leere Liste `agents.list[].skills` ist die **endgültige** Menge für diesen Agenten - sie wird nicht mit Defaults zusammengeführt.
  * Die effektive Allowlist gilt über Prompt-Erstellung, Skill-Slash-Command-Erkennung, Sandbox-Synchronisierung und Skill-Snapshots hinweg.


## Plugins und Skills

Plugins können eigene Skills mitliefern, indem sie `skills`-Verzeichnisse in `openclaw.plugin.json` aufführen (Pfade relativ zum Plugin-Root). Plugin-Skills werden geladen, wenn das Plugin aktiviert ist. Dies ist der richtige Ort für tool-spezifische Betriebsanleitungen, die zu lang für die Tool-Beschreibung sind, aber verfügbar sein sollten, wenn das Plugin installiert ist - zum Beispiel liefert das Browser-Plugin einen `browser-automation`-Skill für mehrstufige Browser-Steuerung mit.

Plugin-Skill-Verzeichnisse werden in denselben Pfad mit niedriger Priorität wie `skills.load.extraDirs` gemischt, sodass ein gleichnamiger gebündelter, verwalteter, Agent- oder Workspace-Skill sie überschreibt. Sie können sie über `metadata.openclaw.requires.config` im Konfigurationseintrag des Plugins sperren.

Siehe [Plugins](</de/tools/plugin>) für Erkennung/Konfiguration und [Tools](</de/tools>) für die Tool-Oberfläche, deren Verwendung diese Skills vermitteln.

## Skill Workshop

Das optionale, experimentelle **Skill Workshop** -Plugin kann Workspace-Skills aus wiederverwendbaren Verfahren erstellen oder aktualisieren, die während der Agent-Arbeit beobachtet wurden. Es ist standardmäßig deaktiviert und muss explizit über `plugins.entries.skill-workshop` aktiviert werden.

Skill Workshop schreibt nur nach `<workspace>/skills`, scannt generierte Inhalte, unterstützt ausstehende Genehmigung oder automatische sichere Schreibvorgänge, quarantänisiert unsichere Vorschläge und aktualisiert den Skill-Snapshot nach erfolgreichen Schreibvorgängen, damit neue Skills ohne Gateway-Neustart verfügbar werden.

Verwenden Sie es für Korrekturen wie _"beim nächsten Mal GIF-Attribution prüfen"_ oder hart erarbeitete Workflows wie Medien-QA-Checklisten. Beginnen Sie mit ausstehender Genehmigung; verwenden Sie automatische Schreibvorgänge nur in vertrauenswürdigen Workspaces, nachdem Sie seine Vorschläge geprüft haben. Vollständige Anleitung: [Skill Workshop-Plugin](</de/plugins/skill-workshop>).

## ClawHub (Installieren und Synchronisieren)

[ClawHub](<https://clawhub.ai>) ist die öffentliche Skills-Registry für OpenClaw. Verwenden Sie native `openclaw skills`-Befehle für Suche/Installation/Aktualisierung oder die separate `clawhub` CLI für Veröffentlichungs-/Synchronisierungs-Workflows. Vollständige Anleitung: [ClawHub](</de/clawhub>).

Aktion | Befehl  
---|---  
Einen Skill im Workspace installieren | `openclaw skills install <skill-slug>`  
Alle installierten Skills aktualisieren | `openclaw skills update --all`  
Synchronisieren (Scannen + Updates veröffentlichen) | `clawhub sync --all`  
  
Das native `openclaw skills install` installiert in das aktive Workspace-Verzeichnis `skills/`. Die separate `clawhub` CLI installiert ebenfalls in `./skills` unter Ihrem aktuellen Arbeitsverzeichnis (oder fällt auf den konfigurierten OpenClaw-Workspace zurück). OpenClaw nimmt dies in der nächsten Sitzung als `<workspace>/skills` auf. Konfigurierte Skill-Roots unterstützen außerdem eine Gruppierungsebene, etwa `skills/<group>/<skill>/SKILL.md`, sodass verwandte Drittanbieter-Skills unter einem gemeinsamen Ordner gehalten werden können, ohne breit rekursiv zu scannen.

Gateway-Clients, die eine private, nicht über ClawHub laufende Bereitstellung benötigen, können ein ZIP-Skill-Archiv mit `skills.upload.begin`, `skills.upload.chunk` und `skills.upload.commit` bereitstellen und den abgeschlossenen Upload dann mit `skills.install({ source: "upload", uploadId, slug, force?, sha256? })` installieren. Dies ist ein expliziter Admin-Upload-Pfad für vertrauenswürdige Clients, nicht der normale `openclaw skills install <slug>`\- oder ClawHub-Installationsfluss. Er ist standardmäßig deaktiviert und funktioniert nur, wenn `skills.install.allowUploadedArchives: true` in `openclaw.json` gesetzt ist. Der Upload-Modus installiert weiterhin in das Standardverzeichnis `skills/<slug>` des Agent-Workspaces; der interne Ordnername des Archivs wird für das endgültige Installationsziel ignoriert.

ClawHub-Skill-Seiten zeigen vor der Installation den neuesten Sicherheits-Scan-Status an, mit Scanner-Detailseiten für VirusTotal, ClawScan und statische Analyse. `openclaw skills install <slug>` bleibt ausschließlich der Installationspfad; Publisher beheben falsch positive Ergebnisse über das ClawHub-Dashboard oder `clawhub skill rescan <slug>`.

## Sicherheit

  * Workspace- und Extra-Dir-Skill-Erkennung akzeptiert nur Skill-Roots und `SKILL.md`-Dateien, deren aufgelöster Realpath innerhalb des konfigurierten Roots bleibt.
  * Private Gateway-Archivinstallationen sind standardmäßig deaktiviert. Wenn sie explizit aktiviert sind, erfordern sie einen abgeschlossenen ZIP-Upload mit `SKILL.md` und verwenden dieselben Archivextraktions-, Path-Traversal-, Symlink-, Force- und Rollback-Schutzmaßnahmen wie ClawHub-Skill-Installationen. Sie werden durch `skills.install.allowUploadedArchives` gesteuert; normale ClawHub-Installationen benötigen diese Einstellung nicht.
  * Gateway-gestützte Skill-Abhängigkeitsinstallationen (`skills.install`, Onboarding und die Skills-Einstellungsoberfläche) führen den integrierten Scanner für gefährlichen Code aus, bevor Installer-Metadaten ausgeführt werden. `critical`-Befunde blockieren standardmäßig, sofern der Aufrufer nicht explizit die Dangerous-Override setzt; verdächtige Befunde warnen weiterhin nur.
  * `openclaw skills install <slug>` ist anders - es lädt einen ClawHub-Skill-Ordner in den Workspace herunter und verwendet nicht den oben beschriebenen Installer-Metadatenpfad.
  * `skills.entries.*.env` und `skills.entries.*.apiKey` injizieren Secrets in den **Host** -Prozess für diesen Agent-Turn (nicht in die Sandbox). Halten Sie Secrets aus Prompts und Logs heraus.


Für ein breiteres Bedrohungsmodell und Checklisten siehe [Sicherheit](</de/gateway/security>).

## SKILL.md-Format

`SKILL.md` muss mindestens Folgendes enthalten:

markdownCopy code
[code]
    ---name: image-labdescription: Generate or edit images via a provider-backed image workflow---
[/code]

OpenClaw folgt der AgentSkills-Spezifikation für Layout/Intention. Der vom eingebetteten Agenten verwendete Parser unterstützt nur **einzeilige** Frontmatter-Schlüssel; `metadata` sollte ein **einzeiliges JSON-Objekt** sein. Verwenden Sie `{baseDir}` in Anweisungen, um auf den Skill-Ordnerpfad zu verweisen.

### Optionale Frontmatter-Schlüssel

URL, die in der macOS-Skills-Oberfläche als "Website" angezeigt wird. Wird auch über `metadata.openclaw.homepage` unterstützt.

Wenn `true`, wird der Skill als Benutzer-Slash-Command verfügbar gemacht.

Wenn `true`, hält OpenClaw die Anweisungen des Skills aus dem normalen Prompt des Agenten heraus. Der Skill ist weiterhin installiert und kann weiterhin explizit als Slash-Command ausgeführt werden, wenn `user-invocable` ebenfalls `true` ist.

Wenn auf `tool` gesetzt, umgeht der Slash-Command das Modell und wird direkt an ein Tool weitergeleitet.

Tool-Name, der aufgerufen wird, wenn `command-dispatch: tool` gesetzt ist.

Für Tool-Dispatch wird die unverarbeitete Argumentzeichenfolge an das Tool weitergeleitet (kein Core-Parsing). Das Tool wird mit `{ command: "<raw args>", commandName: "<slash command>", skillName: "<skill name>" }` aufgerufen.

## Gating (Ladezeitfilter)

OpenClaw filtert Skills zur Ladezeit mithilfe von `metadata` (einzeiliges JSON):

markdownCopy code
[code]
    ---name: image-labdescription: Generate or edit images via a provider-backed image workflowmetadata:  {    "openclaw":      {        "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"], "config": ["browser.enabled"] },        "primaryEnv": "GEMINI_API_KEY",      },  }---
[/code]

Felder unter `metadata.openclaw`:

Wenn `true`, den Skill immer einschließen (andere Gates überspringen).

Optionales Emoji, das von der macOS Skills UI verwendet wird.

Optionale URL, die in der macOS Skills UI als "Website" angezeigt wird.

Optionale Liste von Plattformen. Wenn festgelegt, ist der Skill nur auf diesen Betriebssystemen geeignet.

Jeder Eintrag muss in `PATH` vorhanden sein.

Mindestens einer muss in `PATH` vorhanden sein.

Die Umgebungsvariable muss vorhanden sein oder in der Konfiguration bereitgestellt werden.

Liste von `openclaw.json`-Pfaden, die wahr sein müssen.

Name der Umgebungsvariable, die `skills.entries.<name>.apiKey` zugeordnet ist.

Optionale Installer-Spezifikationen, die von der macOS Skills UI verwendet werden (brew/node/go/uv/download).

Wenn kein `metadata.openclaw` vorhanden ist, ist der Skill immer geeignet (außer er ist in der Konfiguration deaktiviert oder durch `skills.allowBundled` für gebündelte Skills blockiert).

### Sandbox-Hinweise

  * `requires.bins` wird beim Laden des Skills auf dem **Host** geprüft.
  * Wenn ein Agent in einer Sandbox ausgeführt wird, muss die Binärdatei auch **innerhalb des Containers** vorhanden sein. Installieren Sie sie über `agents.defaults.sandbox.docker.setupCommand` (oder ein benutzerdefiniertes Image). `setupCommand` wird einmal ausgeführt, nachdem der Container erstellt wurde. Paketinstallationen erfordern außerdem Netzwerk-Egress, ein beschreibbares Root-Dateisystem und einen Root-Benutzer in der Sandbox.
  * Beispiel: Der Skill `summarize` (`skills/summarize/SKILL.md`) benötigt die `summarize`-CLI im Sandbox-Container, um dort ausgeführt zu werden.


### Installer-Spezifikationen

markdownCopy code
[code]
    ---name: geminidescription: Use Gemini CLI for coding assistance and Google search lookups.metadata:  {    "openclaw":      {        "emoji": "♊️",        "requires": { "bins": ["gemini"] },        "install":          [            {              "id": "brew",              "kind": "brew",              "formula": "gemini-cli",              "bins": ["gemini"],              "label": "Install Gemini CLI (brew)",            },          ],      },  }---
[/code]

Regeln für die Installer-Auswahl

  * Wenn mehrere Installer aufgeführt sind, wählt der Gateway eine einzelne bevorzugte Option aus (brew, wenn verfügbar, andernfalls node).
  * Wenn alle Installer `download` sind, listet OpenClaw jeden Eintrag auf, damit Sie die verfügbaren Artefakte sehen können.
  * Installer-Spezifikationen können `os: ["darwin"|"linux"|"win32"]` enthalten, um Optionen nach Plattform zu filtern.
  * Node-Installationen berücksichtigen `skills.install.nodeManager` in `openclaw.json` (Standard: npm; Optionen: npm/pnpm/yarn/bun). Dies betrifft nur Skill-Installationen; die Gateway-Laufzeit sollte weiterhin Node sein - Bun wird für WhatsApp/Telegram nicht empfohlen.
  * Die Gateway-gestützte Installer-Auswahl ist präferenzgesteuert: Wenn Installer-Spezifikationen verschiedene Arten mischen, bevorzugt OpenClaw Homebrew, wenn `skills.install.preferBrew` aktiviert ist und `brew` vorhanden ist, dann `uv`, dann den konfigurierten Node-Manager, dann andere Fallbacks wie `go` oder `download`.
  * Wenn jede Installationsspezifikation `download` ist, zeigt OpenClaw alle Download-Optionen an, statt sie auf einen bevorzugten Installer zu reduzieren.

Details pro Installer

  * **Go-Installationen:** Wenn `go` fehlt und `brew` verfügbar ist, installiert der Gateway zuerst Go über Homebrew und setzt `GOBIN` wenn möglich auf das `bin` von Homebrew.
  * **Download-Installationen:** `url` (erforderlich), `archive` (`tar.gz` | `tar.bz2` | `zip`), `extract` (Standard: automatisch, wenn Archiv erkannt), `stripComponents`, `targetDir` (Standard: `~/.openclaw/tools/<skillKey>`).


## Konfigurationsüberschreibungen

Gebündelte und verwaltete Skills können umgeschaltet und mit Umgebungswerten unter `skills.entries` in `~/.openclaw/openclaw.json` versorgt werden:

json5Copy code
[code]
    {  skills: {    entries: {      "image-lab": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" }, // or plaintext string        env: {          GEMINI_API_KEY: "GEMINI_KEY_HERE",        },        config: {          endpoint: "https://example.invalid",          model: "nano-pro",        },      },      peekaboo: { enabled: true },      sag: { enabled: false },    },  },}
[/code]

`false` deaktiviert den Skill, selbst wenn er gebündelt oder installiert ist. Der gebündelte Skill `coding-agent` ist Opt-in: Legen Sie `skills.entries.coding-agent.enabled: true` fest, bevor Sie ihn Agenten verfügbar machen, und stellen Sie dann sicher, dass eines von `claude`, `codex`, `opencode` oder `pi` installiert und für seine eigene CLI authentifiziert ist.

Komfortfunktion für Skills, die `metadata.openclaw.primaryEnv` deklarieren. Unterstützt Klartext oder SecretRef.

Optionaler Container für benutzerdefinierte Felder pro Skill. Benutzerdefinierte Schlüssel müssen hier liegen.

Optionale Zulassungsliste nur für **gebündelte** Skills. Wenn gesetzt, sind nur gebündelte Skills in der Liste geeignet (verwaltete/Workspace-Skills bleiben unberührt).

Wenn der Skill-Name Bindestriche enthält, setzen Sie den Schlüssel in Anführungszeichen (JSON5 erlaubt Schlüssel in Anführungszeichen). Konfigurationsschlüssel entsprechen standardmäßig dem **Skill-Namen** \- wenn ein Skill `metadata.openclaw.skillKey` definiert, verwenden Sie diesen Schlüssel unter `skills.entries`.

## Umgebungsinjektion

Wenn ein Agent-Lauf startet, führt OpenClaw Folgendes aus:

  1. Liest Skill-Metadaten.
  2. Wendet `skills.entries.<key>.env` und `skills.entries.<key>.apiKey` auf `process.env` an.
  3. Erstellt den System-Prompt mit **geeigneten** Skills.
  4. Stellt die ursprüngliche Umgebung wieder her, nachdem der Lauf endet.


Die Umgebungsinjektion ist **auf den Agent-Lauf beschränkt** , nicht auf eine globale Shell- Umgebung.

Für das gebündelte Backend `claude-cli` materialisiert OpenClaw außerdem denselben geeigneten Snapshot als temporäres Claude Code Plugin und übergibt ihn mit `--plugin-dir`. Claude Code kann dann seinen nativen Skill-Resolver verwenden, während OpenClaw weiterhin Vorrang, Agent-spezifische Zulassungslisten, Gating und `skills.entries.*`-Umgebungs-/API-Schlüssel-Injektion verwaltet. Andere CLI-Backends verwenden nur den Prompt-Katalog.

## Snapshots und Aktualisierung

OpenClaw erstellt einen Snapshot der geeigneten Skills **beim Start einer Sitzung** und verwendet diese Liste für nachfolgende Turns in derselben Sitzung wieder. Änderungen an Skills oder Konfiguration werden in der nächsten neuen Sitzung wirksam.

Skills können in zwei Fällen während einer Sitzung aktualisiert werden:

  * Der Skills-Watcher ist aktiviert.
  * Ein neuer geeigneter Remote-Node erscheint.


Betrachten Sie dies als **Hot Reload** : Die aktualisierte Liste wird beim nächsten Agent-Turn übernommen. Wenn sich die effektive Skill-Zulassungsliste des Agenten für diese Sitzung ändert, aktualisiert OpenClaw den Snapshot, damit sichtbare Skills mit dem aktuellen Agenten synchron bleiben.

### Skills-Watcher

Standardmäßig überwacht OpenClaw Skill-Ordner und erhöht den Skills-Snapshot, wenn sich `SKILL.md`-Dateien ändern. Konfigurieren Sie dies unter `skills.load`:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/agent-scripts/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],      watch: true,      watchDebounceMs: 250,    },  },}
[/code]

Verwenden Sie `allowSymlinkTargets` für beabsichtigte Layouts mit benachbarten Repositories, bei denen ein integrierter Skill-Root einen Symlink enthält, zum Beispiel `~/.agents/skills/manager -> ~/Projects/manager/skills`. Die Zielliste wird nach Realpath-Auflösung abgeglichen und sollte eng gefasst bleiben.

### Remote-macOS-Nodes (Linux-Gateway)

Wenn der Gateway unter Linux läuft, aber ein **macOS-Node** mit erlaubtem `system.run` verbunden ist (Exec-Genehmigungssicherheit nicht auf `deny` gesetzt), kann OpenClaw macOS-exklusive Skills als geeignet behandeln, wenn die erforderlichen Binärdateien auf diesem Node vorhanden sind. Der Agent sollte diese Skills über das Werkzeug `exec` mit `host=node` ausführen.

Dies hängt davon ab, dass der Node seine Befehlsunterstützung meldet und ein Bin-Probe über `system.which` oder `system.run` möglich ist. Offline-Nodes machen Remote-exklusive Skills **nicht** sichtbar. Wenn ein verbundener Node nicht mehr auf Bin- Probes antwortet, löscht OpenClaw seine gecachten Bin-Treffer, sodass Agenten keine Skills mehr sehen, die dort derzeit nicht ausgeführt werden können.

## Token-Auswirkung

Wenn Skills geeignet sind, injiziert OpenClaw eine kompakte XML-Liste verfügbarer Skills in den System-Prompt (über `formatSkillsForPrompt` in `pi-coding-agent`). Die Kosten sind deterministisch:

  * **Basis-Overhead** (nur bei ≥1 Skill): 195 Zeichen.
  * **Pro Skill:** 97 Zeichen + die Länge der XML-escaped Werte `<name>`, `<description>` und `<location>`.


Formel (Zeichen):

textCopy code
[code]
    total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
[/code]

XML-Escaping erweitert `& < > " '` zu Entitäten (`&amp;`, `&lt;` usw.) und erhöht dadurch die Länge. Token-Zahlen variieren je nach Modell-Tokenizer. Eine grobe Schätzung im OpenAI-Stil ist ~4 Zeichen/Token, also **97 Zeichen ≈ 24 Token** pro Skill plus Ihre tatsächlichen Feldlängen.

## Lebenszyklus verwalteter Skills

OpenClaw liefert eine Baseline-Menge von Skills als **gebündelte Skills** mit der Installation aus (npm-Paket oder OpenClaw.app). `~/.openclaw/skills` ist für lokale Überschreibungen vorgesehen - zum Beispiel zum Pinning oder Patchen eines Skills, ohne die gebündelte Kopie zu ändern. Workspace-Skills gehören dem Benutzer und überschreiben beide bei Namenskonflikten.

## Suchen Sie nach weiteren Skills?

Durchsuchen Sie <https://clawhub.ai>. Vollständiges Konfigurationsschema: [Skills-Konfiguration](</de/tools/skills-config>).

## Verwandt

  * [ClawHub](</de/clawhub>) \- öffentliches Skills-Registry
  * [Skills erstellen](</de/tools/creating-skills>) \- benutzerdefinierte Skills erstellen
  * [Plugins](</de/tools/plugin>) \- Überblick über das Plugin-System
  * [Skill Workshop Plugin](</de/plugins/skill-workshop>) \- Skills aus Agent-Arbeit generieren
  * [Skills-Konfiguration](</de/tools/skills-config>) \- Referenz zur Skill-Konfiguration
  * [Slash-Befehle](</de/tools/slash-commands>) \- alle verfügbaren Slash-Befehle


Was this useful?YesNo