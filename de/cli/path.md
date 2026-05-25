---
title: Pfad
source_url: https://docs.openclaw.ai/de/cli/path
scraped_at: 2026-05-25
---

# `openclaw path`

Vom Plugin bereitgestellter Shell-Zugriff auf das `oc://`-Adressierungssubstrat: ein nach Art dispatchendes Pfadschema zum Prüfen und Bearbeiten adressierbarer Arbeitsbereichsdateien (Markdown, JSONC, JSONL). Selbsthoster, Plugin-Autoren und Editor-Erweiterungen verwenden es, um eine eng eingegrenzte Stelle zu lesen, zu finden oder zu aktualisieren, ohne für jeden Dateityp eigene Parser zu schreiben.

Die CLI spiegelt die öffentlichen Verben des Substrats wider:

  * `resolve` ist konkret und liefert genau einen Treffer.
  * `find` ist das Mehrfachtreffer-Verb für Wildcards, Unions, Prädikate und positionale Erweiterung.
  * `set` akzeptiert nur konkrete Pfade oder Einfügemarker; Wildcard-Muster werden vor dem Schreiben abgelehnt.


`path` wird vom gebündelten optionalen Plugin `oc-path` bereitgestellt. Aktivieren Sie es vor der ersten Verwendung:

bashCopy code
[code]
    openclaw plugins enable oc-path
[/code]

## Warum es verwenden

OpenClaw-Zustand ist über von Menschen bearbeitetes Markdown, kommentierte JSONC-Konfiguration und nur anhängbare JSONL-Logs verteilt. Shell-Skripte, Hooks und Agenten benötigen oft einen kleinen Wert aus diesen Dateien: einen Frontmatter-Schlüssel, eine Plugin-Einstellung, ein Feld eines Log-Datensatzes oder einen Aufzählungspunkt unter einem benannten Abschnitt.

`openclaw path` gibt diesen Aufrufern eine stabile Adresse statt eines einmaligen `grep`, Regex oder Parsers für jeden Dateityp. Derselbe `oc://`-Pfad kann im Terminal validiert, aufgelöst, gesucht, als Probelauf ausgeführt und geschrieben werden. Dadurch wird eng eingegrenzte Automatisierung leichter prüfbar und sicherer wiederholbar. Das ist besonders nützlich, wenn Sie ein einzelnes Blatt aktualisieren möchten, während die übrigen Kommentare, Zeilenenden und die umgebende Formatierung der Datei erhalten bleiben.

Verwenden Sie es, wenn das gewünschte Element eine logische Adresse hat, die physische Dateiform aber variiert:

  * Ein Hook möchte eine Einstellung aus kommentiertem JSONC lesen, ohne Kommentare zu verlieren, wenn er den Wert zurückschreibt.
  * Ein Wartungsskript möchte jedes passende Ereignisfeld in einem JSONL-Log finden, ohne das gesamte Log in einen eigenen Parser zu laden.
  * Eine Editor-Erweiterung möchte anhand eines Slugs zu einem Markdown-Abschnitt oder Aufzählungspunkt springen und dann die exakt aufgelöste Zeile rendern.
  * Ein Agent möchte vor der Anwendung eine kleine Arbeitsbereichsänderung als Probelauf ausführen, wobei die geänderten Bytes in der Prüfung sichtbar sind.


Für gewöhnliche Ganzdatei-Bearbeitungen, umfangreiche Konfigurationsmigrationen oder speicherspezifische Schreibvorgänge benötigen Sie `openclaw path` wahrscheinlich nicht. Dafür sollte der zuständige Befehl oder das zuständige Plugin verwendet werden. `path` ist für kleine, adressierbare Dateioperationen gedacht, bei denen ein wiederholbarer Terminalbefehl klarer ist als ein weiterer maßgeschneiderter Parser.

## Verwendung

Einen Wert aus einer von Menschen bearbeiteten Konfigurationsdatei lesen:

bashCopy code
[code]
    openclaw path resolve 'oc://config.jsonc/plugins/github/enabled'
[/code]

Einen Schreibvorgang vorab ansehen, ohne die Festplatte zu ändern:

bashCopy code
[code]
    openclaw path set 'oc://config.jsonc/plugins/github/enabled' 'true' --dry-run
[/code]

Passende Datensätze in einem nur anhängbaren JSONL-Log finden:

bashCopy code
[code]
    openclaw path find 'oc://session.jsonl/[event=tool_call]/name'
[/code]

Eine Anweisung in Markdown nach Abschnitt und Element adressieren statt nach Zeilennummer:

bashCopy code
[code]
    openclaw path resolve 'oc://AGENTS.md/runtime-safety/openclaw-gateway'
[/code]

Einen Pfad in CI oder einem Preflight-Skript validieren, bevor das Skript liest oder schreibt:

bashCopy code
[code]
    openclaw path validate 'oc://AGENTS.md/tools/$last/risk'
[/code]

Diese Befehle sind so gedacht, dass sie in Shell-Skripte kopiert werden können. Verwenden Sie `--json`, wenn ein Aufrufer strukturierte Ausgabe benötigt, und `--human`, wenn eine Person das Ergebnis prüft.

## Funktionsweise

`openclaw path` macht vier Dinge:

  1. Es parst die `oc://`-Adresse in Slots: Datei, Abschnitt, Element, Feld und optionale Sitzung.
  2. Es wählt den Dateityp-Adapter anhand der Zielerweiterung (`.md`, `.jsonc`, `.jsonl` und verwandte Aliasse).
  3. Es löst die Slots gegen den AST dieses Dateityps auf: Markdown-Überschriften und -Elemente, JSONC-Objektschlüssel und Array-Indizes oder JSONL-Zeilendatensätze.
  4. Für `set` gibt es bearbeitete Bytes über denselben Adapter aus, sodass die unveränderten Teile der Datei ihre Kommentare, Zeilenenden und nahegelegene Formatierung behalten, sofern der Dateityp dies unterstützt.


`resolve` und `set` benötigen ein konkretes Ziel. `find` ist das explorative Verb: Es erweitert Wildcards, Unions, Prädikate und Ordinalzahlen in die konkreten Treffer, die Sie prüfen können, bevor Sie einen zum Schreiben auswählen.

## Unterbefehle

Unterbefehl | Zweck  
---|---  
`resolve <oc-path>` | Gibt den konkreten Treffer am Pfad aus (oder „nicht gefunden“).  
`find <pattern>` | Listet Treffer für einen Wildcard-/Union-/Prädikat-Pfad auf.  
`set <oc-path> <value>` | Schreibt ein Blatt oder Einfügeziel an einem konkreten Pfad. Unterstützt `--dry-run`.  
`validate <oc-path>` | Nur parsen; gibt die strukturelle Aufschlüsselung aus (Datei / Abschnitt / Element / Feld).  
`emit <file>` | Führt eine Datei über `parseXxx` \+ `emitXxx` im Roundtrip (Byte-Fidelity-Diagnose).  
  
## Globale Flags

Flag | Zweck  
---|---  
`--cwd <dir>` | Löst den Datei-Slot relativ zu diesem Verzeichnis auf (Standard: `process.cwd()`).  
`--file <path>` | Überschreibt den aufgelösten Pfad des Datei-Slots (absoluter Zugriff).  
`--json` | Erzwingt JSON-Ausgabe (Standard, wenn stdout kein TTY ist).  
`--human` | Erzwingt menschenlesbare Ausgabe (Standard, wenn stdout ein TTY ist).  
`--dry-run` | (nur bei `set`) gibt die Bytes aus, die geschrieben würden, ohne zu schreiben.  
  
## `oc://`-Syntax

CodeCopy code
[code]
    oc://FILE/SECTION/ITEM/FIELD?session=SCOPE
[/code]

Slot-Regeln: `field` erfordert `item`, und `item` erfordert `section`. Über alle vier Slots hinweg:

  * **Maskierte Segmente** — `"a/b.c"` übersteht `/`\- und `.`-Trennzeichen. Inhalt ist byte-literal; `"` und `\` sind innerhalb von Anführungszeichen nicht erlaubt. Auch der Datei-Slot berücksichtigt Anführungszeichen: `oc://"skills/email-drafter"/Tools/$last` behandelt `skills/email-drafter` als einzelnen Dateipfad.
  * **Prädikate** — `[k=v]`, `[k!=v]`, `[k<v]`, `[k<=v]`, `[k>v]`, `[k>=v]`. Numerische Operationen erfordern, dass beide Seiten in endliche Zahlen umgewandelt werden können.
  * **Unions** — `{a,b,c}` passt auf jede der Alternativen.
  * **Wildcards** — `*` (einzelnes Untersegment) und `**` (null oder mehr, rekursiv). `find` akzeptiert diese; `resolve` und `set` lehnen sie als mehrdeutig ab.
  * **Positional** — `$last` löst zum letzten Index / zuletzt deklarierten Schlüssel auf.
  * **Ordinal** — `#N` für den N-ten Treffer in Dokumentreihenfolge.
  * **Einfügemarker** — `+`, `+key`, `+nnn` für schlüsselbasierte / indizierte Einfügung (mit `set` verwenden).
  * **Sitzungsbereich** — `?session=cron-daily` usw. Orthogonal zur Slot-Verschachtelung. Sitzungswerte sind roh und nicht prozent-dekodiert; sie dürfen keine Steuerzeichen oder reservierten Query-Trennzeichen (`?`, `&`, `%`) enthalten.


Reservierte Zeichen (`?`, `&`, `%`) außerhalb von maskierten, Prädikat- oder Union-Segmenten werden abgelehnt. Steuerzeichen (U+0000-U+001F, U+007F) werden überall abgelehnt, einschließlich des Query-Werts `session`.

`formatOcPath(parseOcPath(path)) === path` ist für kanonische Pfade garantiert. Nicht-kanonische Query-Parameter werden ignoriert, außer dem ersten nicht leeren Wert `session=`.

## Adressierung nach Dateityp

Typ | Adressierungsmodell  
---|---  
Markdown | H2-Abschnitte nach Slug, Aufzählungspunkte nach Slug oder `#N`, Frontmatter über `[frontmatter]`.  
JSONC/JSON | Objektschlüssel und Array-Indizes; Punkte teilen verschachtelte Untersegmente, sofern nicht maskiert.  
JSONL | Top-Level-Zeilenadressen (`L1`, `L2`, `$last`), dann JSONC-artiger Abstieg innerhalb der Zeile.  
  
`resolve` gibt einen strukturierten Treffer zurück: `root`, `node`, `leaf` oder `insertion-point`, mit einer 1-basierten Zeilennummer. Blattwerte werden als Text plus `leafType` bereitgestellt, damit Plugin-Autoren Vorschauen rendern können, ohne von der AST-Form des jeweiligen Dateityps abhängig zu sein.

## Mutationsvertrag

`set` schreibt ein konkretes Ziel:

  * Markdown-Frontmatter-Werte und `- key: value`-Elementfelder sind String-Blätter. Markdown-Einfügungen hängen Abschnitte, Frontmatter-Schlüssel oder Abschnittselemente an und rendern eine kanonische Markdown-Form für die geänderte Datei.
  * JSONC-Blattschreibvorgänge wandeln den String-Wert in den bestehenden Blatttyp um (`string`, endliche `number`, `true`/`false` oder `null`). JSONC-Objekt- und Array-Einfügungen parsen `<value>` als JSON und verwenden den Bearbeitungspfad von `jsonc-parser` für gewöhnliche Blattschreibvorgänge, wobei Kommentare und nahegelegene Formatierung erhalten bleiben.
  * JSONL-Blattschreibvorgänge wandeln innerhalb einer Zeile wie JSONC um. Ganze-Zeile-Ersetzung und Anhängen parsen `<value>` als JSON. Gerendertes JSONL bewahrt die dominante LF/CRLF-Zeilenenden-Konvention der Datei.


Verwenden Sie `--dry-run` vor nutzersichtbaren Schreibvorgängen, wenn die exakten Bytes wichtig sind. Das Substrat bewahrt byte-identische Ausgabe für Parse-/Emit- Roundtrips, aber eine Mutation kann je nach Dateityp die bearbeitete Region oder Datei kanonisieren.

## Beispiele

bashCopy code
[code]
    # Validate a path (no filesystem access)openclaw path validate 'oc://AGENTS.md/Tools/$last/risk' # Read a leafopenclaw path resolve 'oc://gateway.jsonc/version' # Wildcard searchopenclaw path find 'oc://session.jsonl/*/event' --file ./logs/session.jsonl # Dry-run a writeopenclaw path set 'oc://gateway.jsonc/version' '2.0' --dry-run # Apply the writeopenclaw path set 'oc://gateway.jsonc/version' '2.0' # Byte-fidelity round-trip (diagnostic)openclaw path emit ./AGENTS.md
[/code]

Weitere Grammatikbeispiele:

bashCopy code
[code]
    # Quote keys containing / or .openclaw path resolve 'oc://config.jsonc/agents.defaults.models/"anthropic/claude-opus-4-7"/alias' # Predicate search over JSONC childrenopenclaw path find 'oc://config.jsonc/plugins/[enabled=true]/id' # Insert into a JSONC arrayopenclaw path set 'oc://config.jsonc/items/+1' '{"id":"new","enabled":true}' --dry-run # Insert a JSONC object keyopenclaw path set 'oc://config.jsonc/plugins/+github' '{"enabled":true}' --dry-run # Append a JSONL eventopenclaw path set 'oc://session.jsonl/+' '{"event":"checkpoint","ok":true}' --file ./logs/session.jsonl # Resolve the last JSONL value lineopenclaw path resolve 'oc://session.jsonl/$last/event' --file ./logs/session.jsonl # Address markdown frontmatteropenclaw path resolve 'oc://AGENTS.md/[frontmatter]/name' # Insert markdown frontmatteropenclaw path set 'oc://AGENTS.md/[frontmatter]/+description' 'Agent instructions' --dry-run # Find markdown item fieldsopenclaw path find 'oc://SKILL.md/Tools/*/send_email' # Validate a session-scoped pathopenclaw path validate 'oc://AGENTS.md/Tools/$last/risk?session=cron-daily'
[/code]

## Rezepte nach Dateityp

Dieselben fünf Verben funktionieren über alle Typen hinweg; das Adressierungsschema dispatcht anhand der Dateierweiterung. Die folgenden Beispiele verwenden die Fixtures aus der PR-Beschreibung.

### Markdown

textCopy code
[code]
    <!-- frontmatter.md -->---name: drafterdescription: email drafting agenttier: core---## Tools- gh: GitHub CLI- curl: HTTP client- send_email: enabled
[/code]

bashCopy code
[code]
    $ openclaw path resolve 'oc://x.md/[frontmatter]/tier' --file frontmatter.md --humanleaf @ L4: "core" (string) $ openclaw path resolve 'oc://x.md/tools/gh/gh' --file frontmatter.md --humanleaf @ L9: "GitHub CLI" (string) $ openclaw path find 'oc://x.md/tools/*' --file frontmatter.md --human3 matches for oc://x.md/tools/*:  oc://x.md/tools/gh           →  node @ L9 [md-item]  oc://x.md/tools/curl         →  node @ L10 [md-item]  oc://x.md/tools/send-email   →  node @ L11 [md-item]
[/code]

Das Prädikat `[frontmatter]` adressiert den YAML-Frontmatter-Block; `tools` passt über den Slug auf die Überschrift `## Tools`, und Elementblätter behalten ihre Slug-Form, auch wenn die Quelle Unterstriche verwendet (`send_email` → `send-email`).

### JSONC

textCopy code
[code]
    // config.jsonc{  "plugins": {    "github": {"enabled": true, "role": "vcs"},    "slack":  {"enabled": false, "role": "chat"}  }}
[/code]

bashCopy code
[code]
    $ openclaw path resolve 'oc://config.jsonc/plugins/github/enabled' --file config.jsonc --humanleaf @ L4: "true" (boolean) $ openclaw path set 'oc://config.jsonc/plugins/slack/enabled' 'true' --file config.jsonc --dry-run--dry-run: would write 142 bytes to /…/config.jsonc{  "plugins": {    "github": {"enabled": true, "role": "vcs"},    "slack":  {"enabled": true, "role": "chat"}  }}
[/code]

JSONC-Bearbeitungen laufen über `jsonc-parser`, daher bleiben Kommentare und Leerraum bei einem `set` erhalten. Führen Sie es zuerst mit `--dry-run` aus, um die Bytes vor dem Commit zu prüfen.

### JSONL

textCopy code
[code]
    {"event":"start","userId":"u1","ts":1}{"event":"action","userId":"u1","ts":2}{"event":"end","userId":"u1","ts":3}
[/code]

bashCopy code
[code]
    $ openclaw path find 'oc://session.jsonl/[event=action]/userId' --file session.jsonl --human1 match for oc://session.jsonl/[event=action]/userId:  oc://session.jsonl/L2/userId  →  leaf @ L2: "u1" (string) $ openclaw path resolve 'oc://session.jsonl/L2/ts' --file session.jsonl --humanleaf @ L2: "2" (number)
[/code]

Jede Zeile ist ein Datensatz. Adressieren Sie per Prädikat (`[event=action]`), wenn Sie die Zeilennummer nicht kennen, oder über das kanonische Segment `LN`, wenn Sie sie kennen.

## Unterbefehlsreferenz

### `resolve <oc-path>`

Liest ein einzelnes Blatt oder einen einzelnen Knoten. Wildcards werden abgelehnt - verwenden Sie dafür `find`. Beendet mit `0` bei einem Treffer, `1` bei einem sauberen Fehltreffer, `2` bei einem Parse-Fehler oder verweigerten Muster.

bashCopy code
[code]
    openclaw path resolve 'oc://AGENTS.md/tools/gh/risk' --humanopenclaw path resolve 'oc://gateway.jsonc/server/port' --json
[/code]

### `find <pattern>`

Listet jeden Treffer für ein Wildcard-, Prädikat- oder Union-Muster auf. Beendet mit `0` bei mindestens einem Treffer, `1` bei null Treffern. Wildcards im Dateislot werden mit `OC_PATH_FILE_WILDCARD_UNSUPPORTED` abgelehnt - übergeben Sie eine konkrete Datei (Globbing über mehrere Dateien ist eine geplante Folgefunktion).

bashCopy code
[code]
    openclaw path find 'oc://AGENTS.md/tools/**/risk'openclaw path find 'oc://session.jsonl/[event=action]/userId'openclaw path find 'oc://config.jsonc/plugins/{github,slack}/enabled'
[/code]

### `set <oc-path> <value>`

Schreibt ein Blatt. Kombinieren Sie es mit `--dry-run`, um eine Vorschau der Bytes zu sehen, die geschrieben würden, ohne die Datei zu ändern. Beendet mit `0` bei erfolgreichem Schreiben, `1`, wenn das Substrat verweigert (zum Beispiel, wenn ein Sentinel-Guard ausgelöst wurde), `2` bei Parse-Fehlern.

bashCopy code
[code]
    openclaw path set 'oc://gateway.jsonc/version' '2.0' --dry-runopenclaw path set 'oc://gateway.jsonc/version' '2.0'openclaw path set 'oc://AGENTS.md/Tools/+gh/risk' 'low'
[/code]

Der Einfügemarker `+key` erstellt das benannte Kind, falls es noch nicht existiert; `+nnn` und das bloße `+` funktionieren entsprechend für indexiertes Einfügen und Anhängen.

### `validate <oc-path>`

Reine Parse-Prüfung. Kein Dateisystemzugriff. Nützlich, wenn Sie bestätigen möchten, dass ein Vorlagenpfad wohlgeformt ist, bevor Sie Variablen einsetzen, oder wenn Sie die strukturelle Aufschlüsselung zum Debuggen benötigen:

bashCopy code
[code]
    $ openclaw path validate 'oc://AGENTS.md/tools/gh' --humanvalid: oc://AGENTS.md/tools/gh  file:    AGENTS.md  section: tools  item:    gh
[/code]

Beendet mit `0`, wenn gültig, mit `1`, wenn ungültig (mit strukturiertem `code` und `message`), und mit `2` bei Argumentfehlern.

### `emit <file>`

Führt für eine Datei einen Roundtrip durch den Parser und Emitter der jeweiligen Art aus. Die Ausgabe sollte bei einer fehlerfreien Datei byteidentisch mit der Eingabe sein - Abweichungen deuten auf einen Parserfehler oder einen Sentinel-Treffer hin. Nützlich zum Debuggen des Substratverhaltens bei realen Eingaben.

bashCopy code
[code]
    openclaw path emit ./AGENTS.mdopenclaw path emit ./gateway.jsonc --json
[/code]

## Exit-Codes

Code | Bedeutung  
---|---  
`0` | Erfolg. (`resolve` / `find`: mindestens ein Treffer. `set`: Schreiben erfolgreich.)  
`1` | Kein Treffer, oder `set` wurde vom Substrat abgelehnt (kein Fehler auf Systemebene).  
`2` | Argument- oder Parse-Fehler.  
  
## Ausgabemodus

`openclaw path` ist TTY-bewusst: lesbare Ausgabe auf einem Terminal, JSON, wenn stdout per Pipe weitergeleitet oder umgeleitet wird. `--json` und `--human` überschreiben die automatische Erkennung.

## Hinweise

  * `set` schreibt Bytes über den Emit-Pfad des Substrats, der den Redaction-Sentinel-Guard automatisch anwendet. Ein Blatt, das `__OPENCLAW_REDACTED__` trägt (wörtlich oder als Teilzeichenfolge), wird zur Schreibzeit verweigert.
  * JSONC-Parsing und Blattbearbeitungen verwenden die Plugin-lokale `jsonc-parser`\- Abhängigkeit, sodass Kommentare und Formatierung bei gewöhnlichen Blatt- Schreibvorgängen erhalten bleiben, statt über einen handgeschriebenen Parser-/Re-Render-Pfad zu laufen.
  * `path` weiß nichts über LKG. Wenn die Datei LKG-verfolgt ist, entscheidet der nächste Observe-Aufruf, ob hochgestuft oder wiederhergestellt wird. `set --batch` für atomare Mehrfach-Set-Operationen über den LKG-Hochstufungs-/Wiederherstellungslebenszyklus ist zusammen mit dem LKG-Wiederherstellungssubstrat geplant.


## Verwandt

  * [CLI-Referenz](</de/cli>)


Was this useful?YesNo