---
title: Création de Skills
source_url: https://docs.openclaw.ai/fr/tools/creating-skills
scraped_at: 2026-05-25
---

Skills apprennent à l’agent comment et quand utiliser les outils. Chaque skill est un répertoire contenant un fichier `SKILL.md` avec un frontmatter YAML et des instructions en markdown.

Pour savoir comment les skills sont chargées et priorisées, consultez [Skills](</fr/tools/skills>).

## Créer votre première skill

* ### Créer le répertoire de la skill

Les skills résident dans votre espace de travail. Créez un nouveau dossier :

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Écrire SKILL.md

Créez `SKILL.md` dans ce répertoire. Le frontmatter définit les métadonnées, et le corps en markdown contient les instructions pour l’agent.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Utilisez le kebab-case avec des lettres minuscules, des chiffres et des traits d’union pour le `name` de la skill. Gardez le nom du dossier et le `name` du frontmatter alignés.

* ### Ajouter des outils (facultatif)

Vous pouvez définir des schémas d’outils personnalisés dans le frontmatter ou demander à l’agent d’utiliser les outils système existants (comme `exec` ou `browser`). Les skills peuvent aussi être livrées dans des plugins avec les outils qu’elles documentent.

* ### Charger la skill

Démarrez une nouvelle session pour qu’OpenClaw détecte la skill :

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Vérifiez que la skill est chargée :

bashCopy code
[code]
    openclaw skills list
[/code]

* ### La tester

Envoyez un message qui devrait déclencher la skill :

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Ou discutez simplement avec l’agent et demandez une salutation.

## Référence des métadonnées de skill

Le frontmatter YAML prend en charge ces champs :

Champ | Obligatoire | Description  
---|---|---  
`name` | Oui | Identifiant unique utilisant des lettres minuscules, des chiffres et des traits d’union  
`description` | Oui | Description sur une ligne affichée à l’agent  
`metadata.openclaw.os` | Non | Filtre d’OS (`["darwin"]`, `["linux"]`, etc.)  
`metadata.openclaw.requires.bins` | Non | Binaires requis dans PATH  
`metadata.openclaw.requires.config` | Non | Clés de configuration requises  
  
## Bonnes pratiques

  * **Soyez concis** — indiquez au modèle _quoi_ faire, pas comment être une IA
  * **La sécurité d’abord** — si votre skill utilise `exec`, assurez-vous que les prompts ne permettent pas l’injection de commandes arbitraires depuis une entrée non fiable
  * **Testez localement** — utilisez `openclaw agent --message "..."` pour tester avant de partager
  * **Utilisez ClawHub** — parcourez les skills et contribuez-y sur [ClawHub](<https://clawhub.ai>)


## Où résident les skills

Emplacement | Priorité | Portée  
---|---|---  
`\<workspace\>/skills/` | La plus élevée | Par agent  
`\<workspace\>/.agents/skills/` | Élevée | Agent par espace de travail  
`~/.agents/skills/` | Moyenne | Profil d’agent partagé  
`~/.openclaw/skills/` | Moyenne | Partagé (tous les agents)  
Intégrées (livrées avec OpenClaw) | Faible | Globale  
`skills.load.extraDirs` | La plus faible | Dossiers partagés personnalisés  
  
## Connexe

  * [Référence Skills](</fr/tools/skills>) — règles de chargement, de priorité et de contrôle
  * [Configuration Skills](</fr/tools/skills-config>) — schéma de configuration `skills.*`
  * [ClawHub](</fr/clawhub>) — registre public de skills
  * [Créer des Plugins](</fr/plugins/building-plugins>) — les plugins peuvent livrer des skills


Was this useful?YesNo