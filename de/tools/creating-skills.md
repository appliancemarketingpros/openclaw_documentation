---
title: Skills erstellen
source_url: https://docs.openclaw.ai/de/tools/creating-skills
scraped_at: 2026-05-25
---

Skills vermitteln dem Agenten, wie und wann er Tools verwenden soll. Jeder Skill ist ein Verzeichnis mit einer `SKILL.md`-Datei, die YAML-Frontmatter und Markdown-Anweisungen enthält.

Wie Skills geladen und priorisiert werden, erfahren Sie unter [Skills](</de/tools/skills>).

## Erstellen Sie Ihren ersten Skill

* ### Create the skill directory

Skills befinden sich in Ihrem Arbeitsbereich. Erstellen Sie einen neuen Ordner:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Write SKILL.md

Erstellen Sie `SKILL.md` in diesem Verzeichnis. Das Frontmatter definiert Metadaten, und der Markdown-Text enthält Anweisungen für den Agenten.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Verwenden Sie Bindestrich-Schreibweise mit Kleinbuchstaben, Ziffern und Bindestrichen für den Skill- `name`. Halten Sie den Ordnernamen und den Frontmatter-`name` konsistent.

* ### Add tools (optional)

Sie können benutzerdefinierte Tool-Schemas im Frontmatter definieren oder den Agenten anweisen, vorhandene System-Tools (wie `exec` oder `browser`) zu verwenden. Skills können auch innerhalb von Plugins zusammen mit den Tools ausgeliefert werden, die sie dokumentieren.

* ### Load the skill

Starten Sie eine neue Sitzung, damit OpenClaw den Skill übernimmt:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Prüfen Sie, ob der Skill geladen wurde:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Test it

Senden Sie eine Nachricht, die den Skill auslösen sollte:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Oder chatten Sie einfach mit dem Agenten und bitten Sie um eine Begrüßung.

## Referenz für Skill-Metadaten

Das YAML-Frontmatter unterstützt diese Felder:

Feld | Erforderlich | Beschreibung  
---|---|---  
`name` | Ja | Eindeutiger Bezeichner mit Kleinbuchstaben, Ziffern und Bindestrichen  
`description` | Ja | Einzeilige Beschreibung, die dem Agenten angezeigt wird  
`metadata.openclaw.os` | Nein | Betriebssystemfilter (`["darwin"]`, `["linux"]` usw.)  
`metadata.openclaw.requires.bins` | Nein | Erforderliche Binärdateien auf PATH  
`metadata.openclaw.requires.config` | Nein | Erforderliche Konfigurationsschlüssel  
  
## Best Practices

  * **Fassen Sie sich kurz** — weisen Sie das Modell an, _was_ zu tun ist, nicht wie es eine KI sein soll
  * **Sicherheit zuerst** — wenn Ihr Skill `exec` verwendet, stellen Sie sicher, dass Prompts keine beliebige Befehlsinjektion aus nicht vertrauenswürdigen Eingaben zulassen
  * **Lokal testen** — verwenden Sie `openclaw agent --message "..."`, um vor dem Teilen zu testen
  * **ClawHub verwenden** — durchsuchen Sie Skills und tragen Sie Skills unter [ClawHub](<https://clawhub.ai>) bei


## Wo Skills gespeichert sind

Speicherort | Vorrang | Geltungsbereich  
---|---|---  
`\<workspace\>/skills/` | Höchster | Pro Agent  
`\<workspace\>/.agents/skills/` | Hoch | Pro Arbeitsbereich-Agent  
`~/.agents/skills/` | Mittel | Geteiltes Agentenprofil  
`~/.openclaw/skills/` | Mittel | Geteilt (alle Agenten)  
Mitgeliefert (mit OpenClaw ausgeliefert) | Niedrig | Global  
`skills.load.extraDirs` | Niedrigster | Benutzerdefinierte geteilte Ordner  
  
## Verwandt

  * [Skills-Referenz](</de/tools/skills>) — Lade-, Vorrang- und Gating-Regeln
  * [Skills-Konfiguration](</de/tools/skills-config>) — `skills.*`-Konfigurationsschema
  * [ClawHub](</de/clawhub>) — öffentliches Skill-Register
  * [Plugins erstellen](</de/plugins/building-plugins>) — Plugins können Skills ausliefern


Was this useful?YesNo