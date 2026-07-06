---
title: ClawRouter
source_url: https://docs.openclaw.ai/de/providers/clawrouter
scraped_at: 2026-07-06
---

ModelsProviders

ClawRouter gibt OpenClaw einen richtlinienbezogenen Schlüssel für mehrere Upstream-Modell-Provider. Das gebündelte Plugin erkennt nur die Modelle, die für diesen Schlüssel erlaubt sind, leitet jedes Modell über sein deklariertes Protokoll weiter und meldet das Budget des Schlüssels sowie die aggregierte Nutzung auf den OpenClaw-Nutzungsoberflächen.

Sie installieren oder authentifizieren nicht jedes Upstream-Provider-Plugin auf dem OpenClaw-Host. Upstream-Zugangsdaten und providerspezifische Weiterleitung bleiben in ClawRouter. OpenClaw benötigt nur das gebündelte Plugin `@openclaw/clawrouter` und eine ausgestellte ClawRouter-Zugangsdaten.

Eigenschaft | Wert  
---|---  
Provider | `clawrouter`  
Paket | `@openclaw/clawrouter`  
Authentifizierung | `CLAWROUTER_API_KEY`  
Standard-URL | `https://clawrouter.openclaw.ai`  
Modellkatalog | Zugangsdatenbezogen über `/v1/catalog`  
Kontingente | Monatsbudget und Nutzung über `/v1/usage`  
  
## Erste Schritte

* ### Get a scoped credential

Bitten Sie Ihren ClawRouter-Administrator um Zugangsdaten, deren Richtlinie die Provider, Modelle und das Monatsbudget umfasst, die Sie verwenden sollen. Zugangsdaten werden bei der Ausstellung einmalig angezeigt.

* ### Configure OpenClaw

bashCopy code
[code]
    export CLAWROUTER_API_KEY="..."openclaw onboard --auth-choice clawrouter-api-keyopenclaw plugins enable clawrouter
[/code]

Das Plugin ist mit OpenClaw gebündelt. Wenn Ihre Konfiguration `plugins.allow` setzt, fügen Sie `clawrouter` zu dieser Liste hinzu, bevor Sie es aktivieren. Für eine benutzerdefinierte Bereitstellung setzen Sie `models.providers.clawrouter.baseUrl` auf den ClawRouter-Ursprung; der Standard ist `https://clawrouter.openclaw.ai`.

* ### List granted models

bashCopy code
[code]
    openclaw models list --all --provider clawrouter
[/code]

Verwenden Sie die zurückgegebenen Modellreferenzen exakt wie angezeigt. Sie behalten den Upstream-Namespace bei, etwa `clawrouter/openai/...`, `clawrouter/anthropic/...` oder `clawrouter/google/...`. Wenn `agents.defaults.models` in Ihrer Konfiguration eine Allowlist ist, fügen Sie jede ausgewählte ClawRouter-Referenz hinzu.

* ### Select a model

bashCopy code
[code]
    openclaw models set clawrouter/<provider>/<model>
[/code]

Sie können ein zurückgegebenes Modell auch für einen einzelnen Lauf mit `openclaw agent --model clawrouter/<provider>/<model> --message "..."` auswählen.

## Modellerkennung

`GET /v1/catalog` ist die maßgebliche Quelle. OpenClaw liefert keine zweite, feste Liste von ClawRouter-Modellen aus. Ein in ClawRouter konfiguriertes Modell erscheint, wenn:

  * die Richtlinie der Zugangsdaten seinen Provider erlaubt;
  * die Provider-Verbindung aktiviert und bereit ist;
  * das Katalogmodell eine unterstützte LLM-Fähigkeit ausweist; und
  * der Katalog einen vom Plugin unterstützten Transportvertrag offenlegt.


Das Hinzufügen eines weiteren Modells zu einem unterstützten ClawRouter-Provider erfordert daher kein OpenClaw-Release und kein weiteres Provider-Plugin. Die nächste Katalogaktualisierung erkennt es. Ein Modell, das ein neues Wire-Protokoll benötigt, erfordert Unterstützung im ClawRouter-Plugin, bevor OpenClaw es anzeigt.

## Protokoll- und Provider-Plugins

Sie müssen nicht das Authentifizierungs-Plugin jedes Upstream-Unternehmens installieren. ClawRouter besitzt die Upstream-Zugangsdaten; sein Katalog teilt OpenClaw mit, welchen Transport es verwenden soll. Das Plugin unterstützt:

Katalogroute | OpenClaw-Transport  
---|---  
OpenAI-kompatibler Chat | `openai-completions`  
OpenAI-kompatible Responses | `openai-responses`  
Native Anthropic Messages | `anthropic-messages`  
Natives Google Gemini-Streaming | `google-generative-ai`  
  
Das Plugin wendet außerdem die passenden Replay- und Tool-Schema-Richtlinien für diese Familien an. Katalogzeilen, die ein anderes Anfrage-/Stream-Format verwenden, werden absichtlich nicht als OpenClaw-Textmodelle angezeigt. Normalisieren Sie diese Provider in ClawRouter auf einen der unterstützten Verträge, anstatt eine inkompatible Payload zu senden.

## Kontingente und Nutzung

Die Antwort von ClawRouter unter `/v1/usage` speist die normalen OpenClaw-Oberflächen für Provider-Nutzung. `/status` und verwandte Dashboard-Statusanzeigen zeigen das monatliche Budgetfenster, wenn der Schlüssel ein Limit hat, sowie Summen für Anfragen, Token und Ausgaben. Unlimitierte Schlüssel zeigen weiterhin aggregierte Nutzung ohne Prozentfenster.

Die Kontingentabfrage verwendet denselben bezogenen Schlüssel wie die Modellerkennung. Eine fehlgeschlagene Kontingentabfrage blockiert die Modellausführung nicht.

Prüfen Sie den Live-Snapshot mit:

bashCopy code
[code]
    openclaw status --usageopenclaw models status
[/code]

Derselbe Provider-Snapshot ist für `/status` im Chat und in der Nutzungsoberfläche von OpenClaw verfügbar. Das Budget gilt richtlinienweit, sodass Anfragen eines anderen Clients mit derselben ClawRouter-Richtlinie den verbleibenden Prozentsatz ändern können.

## Fehlerbehebung

Symptom | Prüfung  
---|---  
Keine ClawRouter-Modelle | Bestätigen Sie, dass das Plugin aktiviert und durch `plugins.allow` erlaubt ist, und prüfen Sie dann, ob die Zugangsdaten aktiv sind und mindestens einen bereiten Provider erlauben.  
Ein konfiguriertes ClawRouter-Modell fehlt | Prüfen Sie seine `/v1/catalog`-Fähigkeit und sein Routenformat. Nicht unterstützte Transportverträge werden absichtlich gefiltert.  
`Unknown model: clawrouter/...` | Fügen Sie die exakte Katalogreferenz zu `agents.defaults.models` hinzu, wenn diese Konfigurationszuordnung als Allowlist verwendet wird.  
`401` oder `403` von Katalog oder Nutzung | Stellen Sie die ClawRouter-Zugangsdaten neu aus oder passen Sie deren Geltungsbereich an; OpenClaw fällt nicht auf Upstream-Provider-Schlüssel zurück.  
Modellaufruf schlägt nach Erkennung fehl | Prüfen Sie die Provider-Verbindung und den Upstream-Zustand in ClawRouter, und versuchen Sie es erneut, nachdem der Bereitschaftszustand wiederhergestellt ist.  
Nutzung hat Summen, aber keinen Prozentsatz | Die Richtlinie ist unlimitiert; fügen Sie in ClawRouter ein Monatsbudget hinzu, um ein Prozentfenster anzuzeigen.  
  
## Sicherheitsverhalten

  * Die Katalogerkennung ist auf den konfigurierten Proxy-Schlüssel begrenzt und wird pro Schlüssel zwischengespeichert.
  * Der Proxy-Schlüssel wird nur beim Request-Dispatch angehängt; er wird nicht in Modellmetadaten gespeichert.
  * Native Anthropic- und Gemini-Modell-IDs werden erst beim Dispatch in ihre Upstream-IDs umgeschrieben.
  * Nicht unterstützte oder nicht erlaubte Katalogzeilen schlagen geschlossen fehl und sind nicht auswählbar.


## Verwandt

[**Model providers** Provider-Konfiguration und Modellauswahl. ](</de/concepts/model-providers>) [**Usage tracking** OpenClaw-Nutzungs- und Statusoberflächen. ](</de/concepts/usage-tracking>)

Was this useful?YesNo

Open issue