---
title: Speicher-Wiki
source_url: https://docs.openclaw.ai/de/plugins/memory-wiki
scraped_at: 2026-05-25
---

`memory-wiki` ist ein gebündeltes Plugin, das dauerhaften Speicher in einen kompilierten Wissens-Tresor verwandelt.

Es ersetzt **nicht** das Active Memory-Plugin. Das Active Memory-Plugin bleibt weiterhin für Abruf, Promotion, Indexierung und Dreaming zuständig. `memory-wiki` arbeitet daneben und kompiliert dauerhaftes Wissen in ein navigierbares Wiki mit deterministischen Seiten, strukturierten Claims, Provenienz, Dashboards und maschinenlesbaren Digests.

Verwenden Sie es, wenn Speicher sich eher wie eine gepflegte Wissensschicht verhalten soll und weniger wie ein Haufen Markdown-Dateien.

## Was es hinzufügt

  * Einen dedizierten Wiki-Tresor mit deterministischem Seitenlayout
  * Strukturierte Claim- und Evidenzmetadaten, nicht nur Fließtext
  * Provenienz, Konfidenz, Widersprüche und offene Fragen auf Seitenebene
  * Kompilierte Digests für Agent-/Runtime-Consumer
  * Wiki-native Such-/Abruf-/Anwendungs-/Lint-Tools
  * Optionalen Bridge-Modus, der öffentliche Artefakte aus dem Active Memory-Plugin importiert
  * Optionalen Obsidian-freundlichen Render-Modus und CLI-Integration


## Wie es mit Speicher zusammenspielt

Stellen Sie sich die Aufteilung so vor:

Ebene | Zuständig für  
---|---  
Active Memory-Plugin (`memory-core`, QMD, Honcho usw.) | Abruf, semantische Suche, Promotion, Dreaming, Speicher-Runtime  
`memory-wiki` | Kompilierte Wiki-Seiten, provenienzreiche Synthesen, Dashboards, wiki-spezifische Suche/Abruf/Anwendung  
  
Wenn das Active Memory-Plugin gemeinsame Abrufartefakte bereitstellt, kann OpenClaw beide Ebenen in einem Durchlauf mit `memory_search corpus=all` durchsuchen.

Wenn Sie wiki-spezifisches Ranking, Provenienz oder direkten Seitenzugriff benötigen, verwenden Sie stattdessen die wiki-nativen Tools.

## Empfohlenes Hybridmuster

Eine starke Voreinstellung für Local-first-Setups ist:

  * QMD als Active Memory-Backend für Abruf und breite semantische Suche
  * `memory-wiki` im `bridge`-Modus für dauerhafte synthetisierte Wissensseiten


Diese Aufteilung funktioniert gut, weil jede Ebene fokussiert bleibt:

  * QMD hält Rohnotizen, Sitzungsexporte und zusätzliche Sammlungen durchsuchbar
  * `memory-wiki` kompiliert stabile Entitäten, Claims, Dashboards und Quellseiten


Praktische Regel:

  * Verwenden Sie `memory_search`, wenn Sie einen breiten Abrufdurchlauf über Speicher hinweg möchten
  * Verwenden Sie `wiki_search` und `wiki_get`, wenn Sie provenienzbewusste Wiki-Ergebnisse möchten
  * Verwenden Sie `memory_search corpus=all`, wenn die gemeinsame Suche beide Ebenen abdecken soll


Wenn der Bridge-Modus null exportierte Artefakte meldet, stellt das Active Memory-Plugin derzeit noch keine öffentlichen Bridge-Eingaben bereit. Führen Sie zuerst `openclaw wiki doctor` aus und bestätigen Sie dann, dass das Active Memory-Plugin öffentliche Artefakte unterstützt.

Wenn der Bridge-Modus aktiv ist und `bridge.readMemoryArtifacts` aktiviert ist, lesen `openclaw wiki status`, `openclaw wiki doctor` und `openclaw wiki bridge import` über den laufenden Gateway. Dadurch bleiben CLI-Bridge-Prüfungen am Runtime-Kontext des Speicher-Plugins ausgerichtet. Wenn Bridge deaktiviert ist oder Artefaktlesevorgänge ausgeschaltet sind, behalten diese Befehle ihr lokales/Offline-Verhalten bei.

## Tresor-Modi

`memory-wiki` unterstützt drei Tresor-Modi:

### `isolated`

Eigener Tresor, eigene Quellen, keine Abhängigkeit von `memory-core`.

Verwenden Sie dies, wenn das Wiki ein eigener kuratierter Wissensspeicher sein soll.

### `bridge`

Liest öffentliche Speicherartefakte und Speicherereignisse aus dem Active Memory-Plugin über öffentliche Plugin-SDK-Schnittstellen.

Verwenden Sie dies, wenn das Wiki die exportierten Artefakte des Speicher-Plugins kompilieren und organisieren soll, ohne auf private Plugin-Interna zuzugreifen.

Der Bridge-Modus kann Folgendes indexieren:

  * exportierte Speicherartefakte
  * Dream-Berichte
  * tägliche Notizen
  * Speicher-Root-Dateien
  * Speicherereignisprotokolle


### `unsafe-local`

Explizite Ausstiegsluke für private lokale Pfade auf derselben Maschine.

Dieser Modus ist absichtlich experimentell und nicht portabel. Verwenden Sie ihn nur, wenn Sie die Vertrauensgrenze verstehen und speziell lokalen Dateisystemzugriff benötigen, den der Bridge-Modus nicht bereitstellen kann.

## Tresor-Layout

Das Plugin initialisiert einen Tresor wie folgt:

textCopy code
[code]
    <vault>/  AGENTS.md  WIKI.md  index.md  inbox.md  entities/  concepts/  syntheses/  sources/  reports/  _attachments/  _views/  .openclaw-wiki/
[/code]

Verwaltete Inhalte bleiben innerhalb generierter Blöcke. Menschliche Notizblöcke bleiben erhalten.

Die Hauptseitengruppen sind:

  * `sources/` für importiertes Rohmaterial und Bridge-gestützte Seiten
  * `entities/` für dauerhafte Dinge, Personen, Systeme, Projekte und Objekte
  * `concepts/` für Ideen, Abstraktionen, Muster und Richtlinien
  * `syntheses/` für kompilierte Zusammenfassungen und gepflegte Rollups
  * `reports/` für generierte Dashboards


## Strukturierte Claims und Evidenz

Seiten können strukturiertes `claims`-Frontmatter enthalten, nicht nur freien Text.

Jeder Claim kann Folgendes enthalten:

  * `id`
  * `text`
  * `status`
  * `confidence`
  * `evidence[]`
  * `updatedAt`


Evidenzeinträge können Folgendes enthalten:

  * `kind`
  * `sourceId`
  * `path`
  * `lines`
  * `weight`
  * `confidence`
  * `privacyTier`
  * `note`
  * `updatedAt`


Dadurch verhält sich das Wiki eher wie eine Glaubensschicht als wie eine passive Notizablage. Claims können verfolgt, bewertet, bestritten und bis zu den Quellen zurück aufgelöst werden.

## Agentenorientierte Entitätsmetadaten

Entitätsseiten können auch Routing-Metadaten für die Agentennutzung enthalten. Dies ist generisches Frontmatter und funktioniert daher für Personen, Teams, Systeme, Projekte oder jeden anderen Entitätstyp.

Häufige Felder sind:

  * `entityType`: zum Beispiel `person`, `team`, `system` oder `project`
  * `canonicalId`: stabiler Identitätsschlüssel, der über Aliasse und Importe hinweg verwendet wird
  * `aliases`: Namen, Handles oder Labels, die auf dieselbe Seite auflösen sollen
  * `privacyTier`: `public`, `local-private`, `sensitive` oder `confirm-before-use`
  * `bestUsedFor` / `notEnoughFor`: kompakte Routing-Hinweise
  * `lastRefreshedAt`: Zeitstempel der Quellenaktualisierung getrennt von der Seitenbearbeitungszeit
  * `personCard`: optionale personenspezifische Routing-Karte mit Handles, sozialen Profilen, E-Mails, Zeitzone, Lane, ask-for, avoid-asking-for, Konfidenz und Datenschutz
  * `relationships`: typisierte Kanten zu verwandten Seiten mit Ziel, Art, Gewicht, Konfidenz, Evidenzart, Datenschutzstufe und Notiz


Für ein Personen-Wiki sollte der Agent normalerweise mit `reports/person-agent-directory.md` beginnen und dann die Personenseite mit `wiki_get` öffnen, bevor Kontaktdaten oder abgeleitete Fakten verwendet werden.

Beispiel:

yamlCopy code
[code]
    pageType: entityentityType: personid: entity.brad-grouxcanonicalId: maintainer.brad-grouxaliases:  - Brad  - bgrouxprivacyTier: local-privatebestUsedFor:  - Microsoft Teams and Azure routingnotEnoughFor:  - legal approvallastRefreshedAt: "2026-04-29T00:00:00.000Z"personCard:  handles:    - "@bgroux"  socials:    - "https://x.example/bgroux"  emails:    - brad@example.com  timezone: America/Chicago  lane: Microsoft ecosystem  askFor:    - Teams rollout questions  avoidAskingFor:    - unrelated billing decisions  confidence: 0.8  privacyTier: confirm-before-userelationships:  - targetId: entity.alice    targetTitle: Alice    kind: collaborates-with    confidence: 0.7    evidenceKind: discrawl-statclaims:  - id: claim.brad.teams    text: Brad is useful for Microsoft Teams routing.    status: supported    confidence: 0.9    evidence:      - kind: maintainer-whois        sourceId: source.maintainers        privacyTier: local-private
[/code]

## Kompilierungspipeline

Der Kompilierungsschritt liest Wiki-Seiten, normalisiert Zusammenfassungen und gibt stabile maschinenorientierte Artefakte aus unter:

  * `.openclaw-wiki/cache/agent-digest.json`
  * `.openclaw-wiki/cache/claims.jsonl`


Diese Digests existieren, damit Agenten und Runtime-Code keine Markdown-Seiten scrapen müssen.

Kompilierte Ausgabe treibt außerdem Folgendes an:

  * Wiki-Indexierung im ersten Durchlauf für Such-/Abruf-Flows
  * Claim-ID-Auflösung zurück zu den besitzenden Seiten
  * kompakte Prompt-Ergänzungen
  * Berichts-/Dashboard-Generierung


## Dashboards und Zustandsberichte

Wenn `render.createDashboards` aktiviert ist, pflegt die Kompilierung Dashboards unter `reports/`.

Eingebaute Berichte umfassen:

  * `reports/open-questions.md`
  * `reports/contradictions.md`
  * `reports/low-confidence.md`
  * `reports/claim-health.md`
  * `reports/stale-pages.md`
  * `reports/person-agent-directory.md`
  * `reports/relationship-graph.md`
  * `reports/provenance-coverage.md`
  * `reports/privacy-review.md`


Diese Berichte verfolgen Dinge wie:

  * Widerspruchsnotiz-Cluster
  * konkurrierende Claim-Cluster
  * Claims ohne strukturierte Evidenz
  * Seiten und Claims mit niedriger Konfidenz
  * veraltete oder unbekannte Aktualität
  * Seiten mit ungelösten Fragen
  * Personen-/Entitäts-Routing-Karten
  * strukturierte Beziehungskanten
  * Abdeckung von Evidenzklassen
  * nicht öffentliche Datenschutzstufen, die vor der Verwendung überprüft werden müssen


## Suche und Abruf

`memory-wiki` unterstützt zwei Such-Backends:

  * `shared`: den gemeinsamen Speichersuch-Flow verwenden, wenn verfügbar
  * `local`: das Wiki lokal durchsuchen


Es unterstützt außerdem drei Korpora:

  * `wiki`
  * `memory`
  * `all`


Wichtiges Verhalten:

  * `wiki_search` und `wiki_get` verwenden nach Möglichkeit kompilierte Digests als ersten Durchlauf
  * Claim-IDs können zurück zur besitzenden Seite aufgelöst werden
  * bestrittene/veraltete/frische Claims beeinflussen das Ranking
  * Provenienzlabels können in Ergebnissen erhalten bleiben
  * Der Suchmodus kann das Ranking für Personensuche, Fragenrouting, Quellen- evidenz oder Roh-Claims gewichten


Praktische Regel:

  * Verwenden Sie `memory_search corpus=all` für einen breiten Abrufdurchlauf
  * Verwenden Sie `wiki_search` \+ `wiki_get`, wenn Ihnen wiki-spezifisches Ranking, Provenienz oder Glaubensstruktur auf Seitenebene wichtig ist


Suchmodi:

  * `auto`: ausgewogener Standard
  * `find-person`: personähnliche Entitäten, Aliasse, Handles, soziale Profile und kanonische IDs stärker gewichten
  * `route-question`: Agentenkarten, ask-for-Hinweise, best-used-for-Hinweise und Beziehungskontext stärker gewichten
  * `source-evidence`: Quellseiten und strukturierte Evidenzmetadaten stärker gewichten
  * `raw-claim`: passende strukturierte Claims stärker gewichten und Claim-/Evidenz- metadaten in Ergebnissen zurückgeben


Wenn ein Ergebnis zu einem strukturierten Claim passt, kann `wiki_search` `matchedClaimId`, `matchedClaimStatus`, `matchedClaimConfidence`, `evidenceKinds` und `evidenceSourceIds` in seiner Detail-Payload zurückgeben. Die Textausgabe enthält außerdem kompakte `Claim:`\- und `Evidence:`-Zeilen, wenn verfügbar.

## Agenten-Tools

Das Plugin registriert diese Tools:

  * `wiki_status`
  * `wiki_search`
  * `wiki_get`
  * `wiki_apply`
  * `wiki_lint`


Was sie tun:

  * `wiki_status`: aktueller Tresor-Modus, Zustand, Verfügbarkeit der Obsidian-CLI
  * `wiki_search`: durchsucht Wiki-Seiten und, wenn konfiguriert, gemeinsame Speicherkorpora; akzeptiert `mode` für Personensuche, Fragenrouting, Quellenevidenz oder Roh- Claim-Drilldown
  * `wiki_get`: liest eine Wiki-Seite nach ID/Pfad oder fällt auf den gemeinsamen Speicherkorpus zurück
  * `wiki_apply`: enge Synthese-/Metadatenmutationen ohne freie Seitenchirurgie
  * `wiki_lint`: Strukturprüfungen, Provenienzlücken, Widersprüche, offene Fragen


Das Plugin registriert außerdem eine nicht-exklusive Speicherkorpus-Ergänzung, damit gemeinsame `memory_search` und `memory_get` das Wiki erreichen können, wenn das Active Memory- Plugin Korpusauswahl unterstützt.

## Prompt- und Kontextverhalten

Wenn `context.includeCompiledDigestPrompt` aktiviert ist, hängen Speicher-Prompt-Abschnitte einen kompakten kompilierten Snapshot aus `agent-digest.json` an.

Dieser Snapshot ist absichtlich klein und signalstark:

  * nur wichtigste Seiten
  * nur wichtigste Claims
  * Anzahl der Widersprüche
  * Anzahl der Fragen
  * Konfidenz-/Aktualitätsqualifizierer


Dies ist Opt-in, weil es die Prompt-Form verändert und hauptsächlich für Kontext- Engines oder Legacy-Prompt-Assembly nützlich ist, die ausdrücklich Speicherergänzungen verbrauchen.

## Konfiguration

Legen Sie die Konfiguration unter `plugins.entries.memory-wiki.config` ab:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-wiki": {        enabled: true,        config: {          vaultMode: "isolated",          vault: {            path: "~/.openclaw/wiki/main",            renderMode: "obsidian",          },          obsidian: {            enabled: true,            useOfficialCli: true,            vaultName: "OpenClaw Wiki",            openAfterWrites: false,          },          bridge: {            enabled: false,            readMemoryArtifacts: true,            indexDreamReports: true,            indexDailyNotes: true,            indexMemoryRoot: true,            followMemoryEvents: true,          },          ingest: {            autoCompile: true,            maxConcurrentJobs: 1,            allowUrlIngest: true,          },          search: {            backend: "shared",            corpus: "wiki",          },          context: {            includeCompiledDigestPrompt: false,          },          render: {            preserveHumanBlocks: true,            createBacklinks: true,            createDashboards: true,          },        },      },    },  },}
[/code]

Wichtige Schalter:

  * `vaultMode`: `isolated`, `bridge`, `unsafe-local`
  * `vault.renderMode`: `native` oder `obsidian`
  * `bridge.readMemoryArtifacts`: öffentliche Artefakte des Active Memory Plugin importieren
  * `bridge.followMemoryEvents`: Ereignisprotokolle im Bridge-Modus einschließen
  * `search.backend`: `shared` oder `local`
  * `search.corpus`: `wiki`, `memory` oder `all`
  * `context.includeCompiledDigestPrompt`: kompakten Digest-Snapshot an Memory-Prompt-Abschnitte anhängen
  * `render.createBacklinks`: deterministische Blöcke mit verwandten Inhalten erzeugen
  * `render.createDashboards`: Dashboard-Seiten erzeugen


### Beispiel: QMD + Bridge-Modus

Verwenden Sie dies, wenn Sie QMD für den Abruf und `memory-wiki` für eine gepflegte Wissensebene nutzen möchten:

json5Copy code
[code]
    {  memory: {    backend: "qmd",  },  plugins: {    entries: {      "memory-wiki": {        enabled: true,        config: {          vaultMode: "bridge",          bridge: {            enabled: true,            readMemoryArtifacts: true,            indexDreamReports: true,            indexDailyNotes: true,            indexMemoryRoot: true,            followMemoryEvents: true,          },          search: {            backend: "shared",            corpus: "all",          },          context: {            includeCompiledDigestPrompt: false,          },        },      },    },  },}
[/code]

Dies sorgt dafür, dass:

  * QMD für den Active Memory Abruf zuständig bleibt
  * `memory-wiki` auf kompilierte Seiten und Dashboards fokussiert bleibt
  * die Prompt-Form unverändert bleibt, bis Sie kompilierte Digest-Prompts bewusst aktivieren


## CLI

`memory-wiki` stellt außerdem eine CLI-Oberfläche auf oberster Ebene bereit:

bashCopy code
[code]
    openclaw wiki statusopenclaw wiki doctoropenclaw wiki initopenclaw wiki ingest ./notes/alpha.mdopenclaw wiki compileopenclaw wiki lintopenclaw wiki search "alpha"openclaw wiki get entity.alphaopenclaw wiki apply synthesis "Alpha Summary" --body "..." --source-id source.alphaopenclaw wiki bridge importopenclaw wiki obsidian status
[/code]

Siehe [CLI: wiki](</de/cli/wiki>) für die vollständige Befehlsreferenz.

## Obsidian-Unterstützung

Wenn `vault.renderMode` `obsidian` ist, schreibt das Plugin Obsidian-freundliches Markdown und kann optional die offizielle `obsidian` CLI verwenden.

Unterstützte Workflows sind unter anderem:

  * Statusprüfung
  * Vault-Suche
  * Öffnen einer Seite
  * Aufrufen eines Obsidian-Befehls
  * Springen zur Tagesnotiz


Dies ist optional. Das Wiki funktioniert im nativen Modus auch ohne Obsidian.

## Empfohlener Workflow

  1. Behalten Sie Ihr Active Memory Plugin für Abruf, Promotion und Dreaming bei.
  2. Aktivieren Sie `memory-wiki`.
  3. Beginnen Sie mit dem Modus `isolated`, sofern Sie nicht ausdrücklich den Bridge-Modus verwenden möchten.
  4. Verwenden Sie `wiki_search` / `wiki_get`, wenn Herkunftsnachweise wichtig sind.
  5. Verwenden Sie `wiki_apply` für eng begrenzte Synthesen oder Metadatenaktualisierungen.
  6. Führen Sie `wiki_lint` nach wesentlichen Änderungen aus.
  7. Aktivieren Sie Dashboards, wenn Sie Sichtbarkeit für veraltete Inhalte und Widersprüche wünschen.


## Verwandte Dokumentation

  * [Memory-Übersicht](</de/concepts/memory>)
  * [CLI: memory](</de/cli/memory>)
  * [CLI: wiki](</de/cli/wiki>)
  * [Plugin SDK-Übersicht](</de/plugins/sdk-overview>)


Was this useful?YesNo