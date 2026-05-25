---
title: Codeausführung
source_url: https://docs.openclaw.ai/de/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` führt sandboxed Remote-Python-Analysen über die Responses API von xAI aus. Es wird vom mitgelieferten `xai`-Plugin (unter dem `tools`-Contract) registriert und leitet an denselben `https://api.x.ai/v1/responses`-Endpunkt weiter, den auch `x_search` verwendet.

Eigenschaft | Wert  
---|---  
Tool-Name | `code_execution`  
Provider-Plugin | `xai` (mitgeliefert, `enabledByDefault: true`)  
Authentifizierung | xAI-Auth-Profil, `XAI_API_KEY` oder `plugins.entries.xai.config.webSearch.apiKey`  
Standardmodell | `grok-4-1-fast`  
Standard-Timeout | 30 Sekunden  
Standard-`maxTurns` | nicht gesetzt (xAI wendet sein eigenes internes Limit an)  
  
Dies unterscheidet sich von lokalem [`exec`](</de/tools/exec>):

  * `exec` führt Shell-Befehle auf Ihrem Computer oder gekoppelten Node aus.
  * `code_execution` führt Python in der Remote-Sandbox von xAI aus.


Verwenden Sie `code_execution` für:

  * Berechnungen.
  * Tabellierung.
  * Schnelle Statistiken.
  * Diagrammartige Analysen.
  * Analyse von Daten, die von `x_search` oder `web_search` zurückgegeben wurden.


Verwenden Sie es **nicht** , wenn Sie lokale Dateien, Ihre Shell, Ihr Repo oder gekoppelte Geräte benötigen. Verwenden Sie dafür [`exec`](</de/tools/exec>).

## Einrichtung

* ### Provide an xAI API key

Führen Sie `openclaw onboard --auth-choice xai-api-key` für `code_execution` und `x_search` aus, oder setzen Sie `XAI_API_KEY` / konfigurieren Sie den Schlüssel unter dem xAI-Plugin, wenn auch die Grok-Websuche dieselben Anmeldedaten verwenden soll:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Oder über die Konfiguration:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Enable and tune code_execution

Das Tool ist über `plugins.entries.xai.config.codeExecution.enabled` abgesichert. Standardmäßig ist es deaktiviert.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // überschreibt das standardmäßige xAI-Code-Execution-Modell            maxTurns: 2,            // optionale Begrenzung interner Tool-Turns            timeoutSeconds: 30,     // Anfrage-Timeout (Standard: 30)          },        },      },    },  },}
[/code]

* ### Restart the Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` erscheint in der Tool-Liste des Agenten, sobald das xAI-Plugin erneut mit `enabled: true` registriert wurde.

## Verwendung

Fragen Sie natürlich und machen Sie die Analyseabsicht explizit:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

Das Tool nimmt intern einen einzelnen `task`-Parameter entgegen, daher sollte der Agent die vollständige Analyseanfrage und alle Inline-Daten in einem Prompt senden.

## Fehler

Wenn das Tool ohne Authentifizierung ausgeführt wird, gibt es einen strukturierten `missing_xai_api_key`-Fehler zurück, der auf das Auth-Profil, die Env-Var und die Konfigurationsoptionen verweist. Der Fehler ist JSON und keine ausgelöste Exception, sodass der Agent sich selbst korrigieren kann:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Grenzen

  * Dies ist Remote-Ausführung über xAI, keine lokale Prozessausführung.
  * Behandeln Sie Ergebnisse als kurzlebige Analyse, nicht als persistente Notebook-Sitzung.
  * Gehen Sie nicht davon aus, dass Zugriff auf lokale Dateien oder Ihren Workspace besteht.
  * Verwenden Sie für aktuelle X-Daten zuerst [`x_search`](</de/tools/web#x_search>) und leiten Sie das Ergebnis an `code_execution` weiter.


## Verwandt

[**Exec tool** Lokale Shell-Ausführung auf Ihrem Computer oder gekoppelten Node. ](</de/tools/exec>) [**Exec approvals** Zulassen-/Ablehnen-Richtlinie für Shell-Ausführung. ](</de/tools/exec-approvals>) [**Web tools** `web_search`, `x_search` und `web_fetch`. ](</de/tools/web>) [**xAI provider** Grok-Modelle, Web-/X-Suche und Codeausführungskonfiguration. ](</de/providers/xai>)

Was this useful?YesNo