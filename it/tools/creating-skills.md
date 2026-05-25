---
title: Creare Skills
source_url: https://docs.openclaw.ai/it/tools/creating-skills
scraped_at: 2026-05-25
---

Skills insegna all'agente come e quando usare gli strumenti. Ogni skill è una directory contenente un file `SKILL.md` con frontmatter YAML e istruzioni markdown.

Per sapere come vengono caricate e prioritarizzate le Skills, consulta [Skills](</it/tools/skills>).

## Crea la tua prima skill

* ### Crea la directory della skill

Le Skills risiedono nel tuo workspace. Crea una nuova cartella:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Scrivi SKILL.md

Crea `SKILL.md` dentro quella directory. Il frontmatter definisce i metadati, e il corpo markdown contiene le istruzioni per l'agente.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Usa il formato con trattini, lettere minuscole, cifre e trattini per il `name` della skill. Mantieni allineati il nome della cartella e il `name` nel frontmatter.

* ### Aggiungi strumenti (facoltativo)

Puoi definire schemi di strumenti personalizzati nel frontmatter o istruire l'agente a usare strumenti di sistema esistenti (come `exec` o `browser`). Le Skills possono anche essere distribuite dentro i Plugin insieme agli strumenti che documentano.

* ### Carica la skill

Avvia una nuova sessione in modo che OpenClaw rilevi la skill:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Verifica che la skill sia stata caricata:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Testala

Invia un messaggio che dovrebbe attivare la skill:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Oppure chatta semplicemente con l'agente e chiedi un saluto.

## Riferimento dei metadati della skill

Il frontmatter YAML supporta questi campi:

Campo | Obbligatorio | Descrizione  
---|---|---  
`name` | Sì | Identificatore univoco con lettere minuscole, cifre e trattini  
`description` | Sì | Descrizione su una riga mostrata all'agente  
`metadata.openclaw.os` | No | Filtro OS (`["darwin"]`, `["linux"]`, ecc.)  
`metadata.openclaw.requires.bins` | No | Binari richiesti su PATH  
`metadata.openclaw.requires.config` | No | Chiavi di configurazione richieste  
  
## Buone pratiche

  * **Sii conciso** — istruisci il modello su _cosa_ fare, non su come essere un'AI
  * **La sicurezza prima di tutto** — se la tua skill usa `exec`, assicurati che i prompt non consentano l'iniezione arbitraria di comandi da input non attendibile
  * **Testa localmente** — usa `openclaw agent --message "..."` per testare prima di condividere
  * **Usa ClawHub** — esplora e contribuisci con skill su [ClawHub](<https://clawhub.ai>)


## Dove risiedono le Skills

Posizione | Precedenza | Ambito  
---|---|---  
`\<workspace\>/skills/` | Massima | Per agente  
`\<workspace\>/.agents/skills/` | Alta | Agente per workspace  
`~/.agents/skills/` | Media | Profilo agente condiviso  
`~/.openclaw/skills/` | Media | Condiviso (tutti gli agenti)  
Integrate (distribuite con OpenClaw) | Bassa | Globale  
`skills.load.extraDirs` | Minima | Cartelle condivise personalizzate  
  
## Correlati

  * [Riferimento Skills](</it/tools/skills>) — regole di caricamento, precedenza e gating
  * [Configurazione Skills](</it/tools/skills-config>) — schema di configurazione `skills.*`
  * [ClawHub](</it/clawhub>) — registro pubblico delle skill
  * [Creare Plugin](</it/plugins/building-plugins>) — i Plugin possono distribuire skill


Was this useful?YesNo