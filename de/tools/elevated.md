---
title: Modus mit erhöhten Rechten
source_url: https://docs.openclaw.ai/de/tools/elevated
scraped_at: 2026-05-25
---

Wenn ein Agent innerhalb einer Sandbox ausgeführt wird, sind seine `exec`-Befehle auf die Sandbox-Umgebung beschränkt. **Elevated mode** lässt den Agent stattdessen ausbrechen und Befehle außerhalb der Sandbox ausführen, mit konfigurierbaren Genehmigungs-Gates.

## Direktiven

Steuern Sie Elevated mode pro Sitzung mit Slash-Befehlen:

Direktive | Funktion  
---|---  
`/elevated on` | Außerhalb der Sandbox auf dem konfigurierten Host-Pfad ausführen, Genehmigungen beibehalten  
`/elevated ask` | Wie `on` (Alias)  
`/elevated full` | Außerhalb der Sandbox auf dem konfigurierten Host-Pfad ausführen und Genehmigungen überspringen  
`/elevated off` | Zur auf die Sandbox beschränkten Ausführung zurückkehren  
  
Auch verfügbar als `/elev on|off|ask|full`.

Senden Sie `/elevated` ohne Argument, um die aktuelle Ebene anzuzeigen.

## Funktionsweise

* ### Verfügbarkeit prüfen

Elevated muss in der Konfiguration aktiviert sein und der Absender muss auf der Allowlist stehen:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Ebene festlegen

Senden Sie eine Nachricht, die nur aus einer Direktive besteht, um den Sitzungsstandard festzulegen:

CodeCopy code
[code]
    /elevated full
[/code]

Oder verwenden Sie sie inline (gilt nur für diese Nachricht):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Befehle außerhalb der Sandbox ausführen

Wenn Elevated aktiv ist, verlassen `exec`-Aufrufe die Sandbox. Der effektive Host ist standardmäßig `gateway` oder `node`, wenn das konfigurierte bzw. Sitzungs-Exec-Ziel `node` ist. Im Modus `full` werden exec-Genehmigungen übersprungen. Im Modus `on`/`ask` gelten konfigurierte Genehmigungsregeln weiterhin.

## Auflösungsreihenfolge

  1. **Inline-Direktive** in der Nachricht (gilt nur für diese Nachricht)
  2. **Sitzungs-Override** (festgelegt durch Senden einer Nachricht, die nur aus einer Direktive besteht)
  3. **Globaler Standard** (`agents.defaults.elevatedDefault` in der Konfiguration)


## Verfügbarkeit und Allowlists

  * **Globales Gate** : `tools.elevated.enabled` (muss `true` sein)
  * **Absender-Allowlist** : `tools.elevated.allowFrom` mit Listen pro Kanal
  * **Gate pro Agent** : `agents.list[].tools.elevated.enabled` (kann nur weiter einschränken)
  * **Allowlist pro Agent** : `agents.list[].tools.elevated.allowFrom` (Absender muss sowohl global als auch pro Agent übereinstimmen)
  * **Discord-Fallback** : Wenn `tools.elevated.allowFrom.discord` ausgelassen wird, wird `channels.discord.allowFrom` als Fallback verwendet
  * **Alle Gates müssen bestehen** ; andernfalls wird Elevated als nicht verfügbar behandelt


Formate für Allowlist-Einträge:

Präfix | Übereinstimmung  
---|---  
(keines) | Absender-ID, E.164 oder From-Feld  
`name:` | Anzeigename des Absenders  
`username:` | Benutzername des Absenders  
`tag:` | Tag des Absenders  
`id:`, `from:`, `e164:` | Explizites Identity-Targeting  
  
## Was Elevated nicht steuert

  * **Tool-Policy** : Wenn `exec` durch die Tool-Policy verweigert wird, kann Elevated das nicht überschreiben.
  * **Host-Auswahlrichtlinie** : Elevated macht aus `auto` keinen freien Cross-Host-Override. Es verwendet die konfigurierten bzw. Sitzungsregeln für das Exec-Ziel und wählt `node` nur dann, wenn das Ziel bereits `node` ist.
  * **Getrennt von`/exec`**: Die Direktive `/exec` passt Exec-Standards pro Sitzung für autorisierte Absender an und erfordert keinen Elevated mode.


## Verwandt

[**Exec-Tool** Shell-Befehlsausführung vom Agent aus. ](</de/tools/exec>) [**Exec-Genehmigungen** Genehmigungs- und Allowlist-System für `exec`. ](</de/tools/exec-approvals>) [**Sandboxing** Sandbox-Konfiguration auf Gateway-Ebene. ](</de/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** Wie die drei Gates während eines Tool-Aufrufs zusammenspielen. ](</de/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo