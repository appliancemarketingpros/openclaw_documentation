---
title: Erkennung von Tool-Schleifen
source_url: https://docs.openclaw.ai/de/tools/loop-detection
scraped_at: 2026-05-25
---

OpenClaw hat zwei zusammenwirkende Schutzmechanismen für repetitive Tool-Aufrufmuster:

  1. **Loop-Erkennung** (`tools.loopDetection.enabled`) – standardmäßig deaktiviert. Überwacht die rollierende Tool-Aufrufhistorie auf wiederholte Muster und Wiederholungsversuche für unbekannte Tools.
  2. **Post-Compaction-Schutz** (`tools.loopDetection.postCompactionGuard`) – standardmäßig aktiviert, sofern `tools.loopDetection.enabled` nicht ausdrücklich `false` ist. Wird nach jedem Compaction-Wiederholungsversuch aktiviert und bricht den Lauf ab, wenn der Agent innerhalb des Fensters dasselbe `(tool, args, result)`-Tripel ausgibt.


Beide werden im selben `tools.loopDetection`-Block konfiguriert, aber der Post-Compaction-Schutz läuft immer dann, wenn der Hauptschalter nicht ausdrücklich ausgeschaltet ist. Setzen Sie `tools.loopDetection.enabled: false`, um beide Oberflächen stummzuschalten.

## Warum es das gibt

  * Repetitive Sequenzen erkennen, die keinen Fortschritt erzielen.
  * Hochfrequente Schleifen ohne Ergebnis erkennen (gleiches Tool, gleiche Eingaben, wiederholte Fehler).
  * Bestimmte Wiederholungsaufrufmuster für bekannte Polling-Tools erkennen.
  * Verhindern, dass Zyklen aus Kontextüberlauf, anschließender Compaction und derselben Schleife unbegrenzt weiterlaufen.


## Konfigurationsblock

Globale Standardwerte, mit allen dokumentierten Feldern:

json5Copy code
[code]
    {  tools: {    loopDetection: {      enabled: false, // master switch for the rolling-history detectors      historySize: 30,      warningThreshold: 10,      criticalThreshold: 20,      unknownToolThreshold: 10,      globalCircuitBreakerThreshold: 30,      detectors: {        genericRepeat: true,        knownPollNoProgress: true,        pingPong: true,      },      postCompactionGuard: {        windowSize: 3, // armed after compaction-retry; runs unless enabled is explicitly false      },    },  },}
[/code]

Optionale Überschreibung pro Agent:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "safe-runner",        tools: {          loopDetection: {            enabled: true,            warningThreshold: 8,            criticalThreshold: 16,          },        },      },    ],  },}
[/code]

### Feldverhalten

Feld | Standardwert | Auswirkung  
---|---|---  
`enabled` | `false` | Hauptschalter für die Detektoren der rollierenden Historie. Das Setzen auf `false` deaktiviert auch den Post-Compaction-Schutz.  
`historySize` | `30` | Anzahl der letzten Tool-Aufrufe, die für die Analyse aufbewahrt werden.  
`warningThreshold` | `10` | Schwellenwert, ab dem ein Muster nur als Warnung klassifiziert wird.  
`criticalThreshold` | `20` | Schwellenwert zum Blockieren repetitiver Schleifenmuster ohne Fortschritt.  
`unknownToolThreshold` | `10` | Blockiert wiederholte Aufrufe desselben nicht verfügbaren Tools nach so vielen Fehlschlägen.  
`globalCircuitBreakerThreshold` | `30` | Globaler Schwellenwert für den Fortschrittsausfall über alle Detektoren hinweg.  
`detectors.genericRepeat` | `true` | Warnt bei wiederholten Mustern aus gleichem Tool und gleichen Parametern und blockiert, wenn dieselben Aufrufe identische Ergebnisse zurückgeben.  
`detectors.knownPollNoProgress` | `true` | Erkennt bekannte pollingartige Muster ohne Zustandsänderung.  
`detectors.pingPong` | `true` | Erkennt alternierende Ping-Pong-Muster.  
`postCompactionGuard.windowSize` | `3` | Anzahl der Post-Compaction-Tool-Aufrufe, während derer der Schutz aktiv bleibt, sowie die Anzahl identischer Tripel, die den Lauf abbrechen.  
  
Für `exec` vergleichen Fortschrittslosigkeitsprüfungen stabile Befehlsausgänge und ignorieren flüchtige Laufzeitmetadaten wie Dauer, PID, Sitzungs-ID und Arbeitsverzeichnis. Wenn eine Lauf-ID verfügbar ist, wird die aktuelle Tool-Aufrufhistorie nur innerhalb dieses Laufs ausgewertet, sodass geplante Heartbeat-Zyklen und neue Läufe keine veralteten Loop-Zählungen aus früheren Läufen übernehmen.

## Empfohlene Einrichtung

  * Setzen Sie für kleinere Modelle `enabled: true` und lassen Sie die Schwellenwerte auf ihren Standardwerten. Flaggschiffmodelle benötigen die Erkennung über rollierende Historien selten und können den Hauptschalter auf `false` belassen, profitieren aber weiterhin vom Post-Compaction-Schutz.
  * Halten Sie die Schwellenwerte in der Reihenfolge `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold`.
  * Falls falsch positive Treffer auftreten: 
    * Erhöhen Sie `warningThreshold` und/oder `criticalThreshold`.
    * Erhöhen Sie optional `globalCircuitBreakerThreshold`.
    * Deaktivieren Sie nur den spezifischen Detektor, der Probleme verursacht (`detectors.<name>: false`).
    * Reduzieren Sie `historySize`, um weniger strikten historischen Kontext zu verwenden.
  * Um alles zu deaktivieren (einschließlich des Post-Compaction-Schutzes), setzen Sie `tools.loopDetection.enabled: false` ausdrücklich.


## Post-Compaction-Schutz

Wenn der Runner nach einem Kontextüberlauf einen Compaction-Wiederholungsversuch abgeschlossen hat, aktiviert er einen Schutz mit kurzem Fenster, der die nächsten wenigen Tool-Aufrufe überwacht. Wenn der Agent dasselbe `(toolName, argsHash, resultHash)`-Tripel mehrfach innerhalb des Fensters ausgibt, kommt der Schutz zu dem Schluss, dass die Compaction die Schleife nicht unterbrochen hat, und bricht den Lauf mit einem `compaction_loop_persisted`-Fehler ab.

Der Schutz wird durch das Haupt-Flag `tools.loopDetection.enabled` gesteuert, mit einer Besonderheit: Er bleibt **aktiviert, wenn das Flag nicht gesetzt oder`true` ist**, und deaktiviert sich nur, wenn das Flag ausdrücklich `false` ist. Das ist beabsichtigt. Der Schutz dient dazu, Compaction-Schleifen zu verlassen, die andernfalls unbegrenzt Tokens verbrauchen würden, sodass auch Benutzer ohne Konfiguration diesen Schutz erhalten.

json5Copy code
[code]
    {  tools: {    loopDetection: {      // master switch; set false to disable the guard along with the rolling detectors      enabled: true,      postCompactionGuard: {        windowSize: 3, // default      },    },  },}
[/code]

  * Ein niedrigerer `windowSize` ist strenger (weniger Versuche vor dem Abbruch).
  * Ein höherer `windowSize` gibt dem Agent mehr Wiederherstellungsversuche.
  * Der Schutz bricht niemals ab, wenn sich Ergebnisse ändern, sondern nur, wenn Ergebnisse im gesamten Fenster byteidentisch sind.
  * Er ist absichtlich eng gefasst: Er löst nur unmittelbar nach einem Compaction-Wiederholungsversuch aus.


## Logs und erwartetes Verhalten

Wenn ein Loop erkannt wird, meldet OpenClaw ein Loop-Ereignis und dämpft oder blockiert je nach Schweregrad den nächsten Tool-Zyklus. Das schützt Benutzer vor unkontrolliertem Token-Verbrauch und Blockierungen, während normaler Tool-Zugriff erhalten bleibt.

  * Warnungen kommen zuerst.
  * Eine Unterdrückung folgt, wenn Muster über den Warnschwellenwert hinaus bestehen bleiben.
  * Kritische Schwellenwerte blockieren den nächsten Tool-Zyklus und zeigen einen klaren Grund der Loop-Erkennung im Laufdatensatz an.
  * Der Post-Compaction-Schutz gibt `compaction_loop_persisted`-Fehler mit dem Namen des betroffenen Tools und der Anzahl identischer Aufrufe aus.


## Verwandte Themen

[**Exec-Genehmigungen** Zulassen-/Ablehnen-Richtlinie für Shell-Ausführung. ](</de/tools/exec-approvals>) [**Denkstufen** Reasoning-Aufwandsstufen und Interaktion mit Provider-Richtlinien. ](</de/tools/thinking>) [**Sub-Agents** Starten isolierter Agents, um ausuferndes Verhalten zu begrenzen. ](</de/tools/subagents>) [**Konfigurationsreferenz** Vollständiges `tools.loopDetection`-Schema und Zusammenführungssemantik. ](</de/gateway/configuration-reference>)

Was this useful?YesNo