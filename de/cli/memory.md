---
title: Speicher
source_url: https://docs.openclaw.ai/de/cli/memory
scraped_at: 2026-05-25
---

# `openclaw memory`

Semantische Memory-Indizierung und Suche verwalten. Bereitgestellt vom Active Memory-Plugin (Standard: `memory-core`; setzen Sie `plugins.slots.memory = "none"`, um es zu deaktivieren).

Verwandt:

  * Memory-Konzept: [Memory](</de/concepts/memory>)
  * Memory-Wiki: [Memory-Wiki](</de/plugins/memory-wiki>)
  * Wiki-CLI: [wiki](</de/cli/wiki>)
  * Plugins: [Plugins](</de/tools/plugin>)


## Beispiele

bashCopy code
[code]
    openclaw memory statusopenclaw memory status --deepopenclaw memory status --fixopenclaw memory index --forceopenclaw memory search "meeting notes"openclaw memory search --query "deployment" --max-results 20openclaw memory promote --limit 10 --min-score 0.75openclaw memory promote --applyopenclaw memory promote --json --min-recall-count 0 --min-unique-queries 0openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --jsonopenclaw memory rem-harnessopenclaw memory rem-harness --jsonopenclaw memory status --jsonopenclaw memory status --deep --indexopenclaw memory status --deep --index --verboseopenclaw memory status --agent mainopenclaw memory index --agent main --verbose
[/code]

## Optionen

`memory status` und `memory index`:

  * `--agent <id>`: auf einen einzelnen Agenten beschränken. Ohne diese Option werden diese Befehle für jeden konfigurierten Agenten ausgeführt; wenn keine Agentenliste konfiguriert ist, verwenden sie den Standardagenten.
  * `--verbose`: während Probes und Indizierung detaillierte Logs ausgeben.


`memory status`:

  * `--deep`: Bereitschaft des lokalen Vektorspeichers, Bereitschaft des Embedding-Providers und Bereitschaft der semantischen Vektorsuche prüfen. Einfaches `memory status` bleibt schnell und führt keine Live-Embedding- oder Provider-Erkennungsarbeit aus; ein unbekannter Vektorspeicher- oder semantischer Vektorstatus bedeutet, dass er in diesem Befehl nicht geprüft wurde. QMD-lexikalisches `searchMode: "search"` überspringt semantische Vektor-Probes und Embedding-Wartung auch mit `--deep`.
  * `--index`: eine Neuindizierung ausführen, wenn der Speicher dirty ist (impliziert `--deep`).
  * `--fix`: veraltete Recall-Sperren reparieren und Promotion-Metadaten normalisieren.
  * `--json`: JSON-Ausgabe ausgeben.


Wenn `memory status` `Dreaming status: blocked` anzeigt, ist der verwaltete Dreaming-Cron aktiviert, aber der Heartbeat, der ihn antreibt, wird für den Standardagenten nicht ausgelöst. Unter [Dreaming wird nie ausgeführt](</de/concepts/dreaming#dreaming-never-runs-status-shows-blocked>) finden Sie die zwei häufigen Ursachen.

`memory index`:

  * `--force`: eine vollständige Neuindizierung erzwingen.


`memory search`:

  * Abfrageeingabe: entweder positionales `[query]` oder `--query <text>` übergeben.
  * Wenn beide angegeben sind, hat `--query` Vorrang.
  * Wenn keines angegeben ist, beendet sich der Befehl mit einem Fehler.
  * `--agent <id>`: auf einen einzelnen Agenten beschränken (Standard: der Standardagent).
  * `--max-results <n>`: die Anzahl der zurückgegebenen Ergebnisse begrenzen.
  * `--min-score <n>`: Treffer mit niedrigem Score herausfiltern.
  * `--json`: JSON-Ergebnisse ausgeben.


`memory promote`:

Kurzfristige Memory-Promotions als Vorschau anzeigen und anwenden.

bashCopy code
[code]
    openclaw memory promote [--apply] [--limit <n>] [--include-promoted]
[/code]

  * `--apply` \-- Promotions nach `MEMORY.md` schreiben (Standard: nur Vorschau).
  * `--limit <n>` \-- die Anzahl der angezeigten Kandidaten begrenzen.
  * `--include-promoted` \-- Einträge einschließen, die bereits in vorherigen Zyklen promoted wurden.


Vollständige Optionen:

  * Bewertet kurzfristige Kandidaten aus `memory/YYYY-MM-DD.md` anhand gewichteter Promotion-Signale (`frequency`, `relevance`, `query diversity`, `recency`, `consolidation`, `conceptual richness`).
  * Verwendet kurzfristige Signale sowohl aus Memory-Recalls als auch aus täglichen Ingestion-Durchläufen sowie Verstärkungssignale aus Light-/REM-Phasen.
  * Wenn Dreaming aktiviert ist, verwaltet `memory-core` automatisch einen Cron-Job, der im Hintergrund einen vollständigen Sweep (`light -> REM -> deep`) ausführt (kein manuelles `openclaw cron add` erforderlich).
  * `--agent <id>`: auf einen einzelnen Agenten beschränken (Standard: der Standardagent).
  * `--limit <n>`: maximale Anzahl der zurückzugebenden/anzuwendenden Kandidaten.
  * `--min-score <n>`: minimaler gewichteter Promotion-Score.
  * `--min-recall-count <n>`: minimale Recall-Anzahl, die für einen Kandidaten erforderlich ist.
  * `--min-unique-queries <n>`: minimale Anzahl unterschiedlicher Abfragen, die für einen Kandidaten erforderlich ist.
  * `--apply`: ausgewählte Kandidaten an `MEMORY.md` anhängen und als promoted markieren.
  * `--include-promoted`: bereits promoted Kandidaten in die Ausgabe einschließen.
  * `--json`: JSON-Ausgabe ausgeben.


`memory promote-explain`:

Einen bestimmten Promotion-Kandidaten und seine Score-Aufschlüsselung erklären.

bashCopy code
[code]
    openclaw memory promote-explain <selector> [--agent <id>] [--include-promoted] [--json]
[/code]

  * `<selector>`: nachzuschlagender Kandidatenschlüssel, Pfadfragment oder Snippet-Fragment.
  * `--agent <id>`: auf einen einzelnen Agenten beschränken (Standard: der Standardagent).
  * `--include-promoted`: bereits promoted Kandidaten einschließen.
  * `--json`: JSON-Ausgabe ausgeben.


`memory rem-harness`:

REM-Reflexionen, Kandidatenwahrheiten und Deep-Promotion-Ausgabe als Vorschau anzeigen, ohne etwas zu schreiben.

bashCopy code
[code]
    openclaw memory rem-harness [--agent <id>] [--include-promoted] [--json]
[/code]

  * `--agent <id>`: auf einen einzelnen Agenten beschränken (Standard: der Standardagent).
  * `--include-promoted`: bereits promoted Deep-Kandidaten einschließen.
  * `--json`: JSON-Ausgabe ausgeben.


## Dreaming

Dreaming ist das Hintergrundsystem zur Memory-Konsolidierung mit drei kooperativen Phasen: **light** (kurzfristiges Material sortieren/stagen), **deep** (dauerhafte Fakten nach `MEMORY.md` promoten) und **REM** (reflektieren und Themen sichtbar machen).

  * Mit `plugins.entries.memory-core.config.dreaming.enabled: true` aktivieren.
  * Im Chat mit `/dreaming on|off` umschalten (oder mit `/dreaming status` prüfen).
  * Dreaming läuft nach einem verwalteten Sweep-Zeitplan (`dreaming.frequency`) und führt Phasen der Reihe nach aus: light, REM, deep.
  * Nur die Deep-Phase schreibt dauerhafte Memory nach `MEMORY.md`.
  * Menschenlesbare Phasenausgaben und Tagebucheinträge werden nach `DREAMS.md` (oder vorhandenes `dreams.md`) geschrieben, mit optionalen Berichten pro Phase in `memory/dreaming/<phase>/YYYY-MM-DD.md`.
  * Das Ranking verwendet gewichtete Signale: Recall-Häufigkeit, Retrieval-Relevanz, Abfragevielfalt, zeitliche Aktualität, Konsolidierung über mehrere Tage und abgeleitete konzeptuelle Reichhaltigkeit.
  * Promotion liest die Live-Tagesnotiz vor dem Schreiben nach `MEMORY.md` erneut, sodass bearbeitete oder gelöschte kurzfristige Snippets nicht aus veralteten Recall-Store-Snapshots promoted werden.
  * Geplante und manuelle `memory promote`-Läufe teilen dieselben Deep-Phasen-Standards, sofern Sie keine CLI-Schwellenwertüberschreibungen übergeben.
  * Automatische Läufe verteilen sich über konfigurierte Memory-Workspaces.


Standardplanung:

  * **Sweep-Taktung** : `dreaming.frequency = 0 3 * * *`
  * **Deep-Schwellenwerte** : `minScore=0.8`, `minRecallCount=3`, `minUniqueQueries=3`, `recencyHalfLifeDays=14`, `maxAgeDays=30`


Beispiel:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

Hinweise:

  * `memory index --verbose` gibt Details pro Phase aus (Provider, Modell, Quellen, Batch-Aktivität).
  * `memory status` enthält alle zusätzlichen Pfade, die über `memorySearch.extraPaths` konfiguriert sind.
  * Wenn effektiv aktive Remote-API-Schlüsselfelder für Memory als SecretRefs konfiguriert sind, löst der Befehl diese Werte aus dem aktiven Gateway-Snapshot auf. Wenn Gateway nicht verfügbar ist, schlägt der Befehl schnell fehl.
  * Hinweis zu Gateway-Versionsabweichung: Dieser Befehlspfad erfordert ein Gateway, das `secrets.resolve` unterstützt; ältere Gateways geben einen Fehler wegen unbekannter Methode zurück.
  * Stimmen Sie die geplante Sweep-Taktung mit `dreaming.frequency` ab. Die Deep-Promotion-Richtlinie ist ansonsten intern; verwenden Sie CLI-Flags für `memory promote`, wenn Sie einmalige manuelle Überschreibungen benötigen.
  * `memory rem-harness --path <file-or-dir> --grounded` zeigt grounded `What Happened`, `Reflections` und `Possible Lasting Updates` aus historischen Tagesnotizen als Vorschau an, ohne etwas zu schreiben.
  * `memory rem-backfill --path <file-or-dir>` schreibt reversible grounded Tagebucheinträge zur UI-Prüfung nach `DREAMS.md`.
  * `memory rem-backfill --path <file-or-dir> --stage-short-term` speist außerdem grounded dauerhafte Kandidaten in den Live-Speicher für kurzfristige Promotions ein, damit die normale Deep-Phase sie bewerten kann.
  * `memory rem-backfill --rollback` entfernt zuvor geschriebene grounded Tagebucheinträge, und `memory rem-backfill --rollback-short-term` entfernt zuvor gestagte grounded kurzfristige Kandidaten.
  * Vollständige Phasenbeschreibungen und die Konfigurationsreferenz finden Sie unter [Dreaming](</de/concepts/dreaming>).


## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Memory-Übersicht](</de/concepts/memory>)


Was this useful?YesNo