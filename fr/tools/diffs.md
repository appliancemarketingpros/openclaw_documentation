---
title: Différences
source_url: https://docs.openclaw.ai/fr/tools/diffs
scraped_at: 2026-05-25
---

`diffs` est un outil de plugin facultatif avec de brèves consignes système intégrées et une Skill associée qui transforme le contenu des changements en artefact diff en lecture seule pour les agents.

Il accepte soit :

  * du texte `before` et `after`
  * un `patch` unifié


Il peut renvoyer :

  * une URL de visualiseur Gateway pour une présentation sur canvas
  * un chemin de fichier rendu (PNG ou PDF) pour l’envoi par message
  * les deux sorties dans un seul appel


Lorsqu’il est activé, le plugin ajoute des consignes d’utilisation concises dans l’espace de l’invite système et expose aussi une Skill détaillée pour les cas où l’agent a besoin d’instructions plus complètes.

## Démarrage rapide

* ### Installer le plugin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### Activer le plugin

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### Choisir un mode

### view

Flux axés sur le canvas : les agents appellent `diffs` avec `mode: "view"` et ouvrent `details.viewerUrl` avec `canvas present`.

### file

Envoi de fichier par chat : les agents appellent `diffs` avec `mode: "file"` et envoient `details.filePath` avec `message` en utilisant `path` ou `filePath`.

### both

Combiné : les agents appellent `diffs` avec `mode: "both"` pour obtenir les deux artefacts en un seul appel.

## Désactiver les consignes système intégrées

Si vous souhaitez garder l’outil `diffs` activé mais désactiver ses consignes d’invite système intégrées, définissez `plugins.entries.diffs.hooks.allowPromptInjection` sur `false` :

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

Cela bloque le hook `before_prompt_build` du plugin diffs tout en gardant le plugin, l’outil et la Skill associée disponibles.

Si vous souhaitez désactiver à la fois les consignes et l’outil, désactivez plutôt le plugin.

## Flux de travail typique de l’agent

* ### Appeler diffs

L’agent appelle l’outil `diffs` avec une entrée.

* ### Lire les détails

L’agent lit les champs `details` dans la réponse.

* ### Présenter

L’agent ouvre `details.viewerUrl` avec `canvas present`, envoie `details.filePath` avec `message` en utilisant `path` ou `filePath`, ou fait les deux.

## Exemples d’entrée

### Avant et après

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## Référence des entrées de l’outil

Tous les champs sont facultatifs, sauf indication contraire.

Texte d’origine. Requis avec `after` lorsque `patch` est omis.

Texte mis à jour. Requis avec `before` lorsque `patch` est omis.

Texte de diff unifié. Mutuellement exclusif avec `before` et `after`.

Nom de fichier affiché pour le mode avant et après.

Indice de remplacement de langue pour le mode avant et après. Les valeurs inconnues utilisent le texte brut par défaut.

Remplacement du titre du visualiseur.

Mode de sortie. Utilise par défaut la valeur par défaut du plugin `defaults.mode`. Alias obsolète : `"image"` se comporte comme `"file"` et reste accepté pour la compatibilité descendante.

Thème du visualiseur. Utilise par défaut la valeur par défaut du plugin `defaults.theme`.

Disposition du diff. Utilise par défaut la valeur par défaut du plugin `defaults.layout`.

Développer les sections inchangées lorsque le contexte complet est disponible. Option par appel uniquement (pas une clé par défaut du plugin).

Format du fichier rendu. Utilise par défaut la valeur par défaut du plugin `defaults.fileFormat`.

Préréglage de qualité pour le rendu PNG ou PDF.

Remplacement de l’échelle de l’appareil (`1`-`4`).

Largeur maximale de rendu en pixels CSS (`640`-`2400`).

TTL de l’artefact en secondes pour les sorties de visualiseur et de fichier autonome. Maximum 21600.

Remplacement de l’origine de l’URL du visualiseur. Remplace `viewerBaseUrl` du plugin. Doit être `http` ou `https`, sans requête ni fragment.

Alias d’entrée hérités

Toujours acceptés pour la compatibilité descendante :

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

Validation et limites

  * `before` et `after` ont chacun une taille maximale de 512 KiB.
  * `patch` a une taille maximale de 2 MiB.
  * `path` a une taille maximale de 2048 octets.
  * `lang` a une taille maximale de 128 octets.
  * `title` a une taille maximale de 1024 octets.
  * Plafond de complexité des patchs : maximum 128 fichiers et 120000 lignes au total.
  * `patch` avec `before` ou `after` est rejeté.
  * Limites de sécurité des fichiers rendus (s’appliquent aux PNG et PDF) : 
    * `fileQuality: "standard"` : maximum 8 MP (8 000 000 pixels rendus).
    * `fileQuality: "hq"` : maximum 14 MP (14 000 000 pixels rendus).
    * `fileQuality: "print"` : maximum 24 MP (24 000 000 pixels rendus).
    * Le PDF a aussi un maximum de 50 pages.


## Contrat des détails de sortie

L’outil renvoie des métadonnées structurées sous `details`.

Champs du visualiseur

Champs partagés pour les modes qui créent un visualiseur :

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, `agentAccountId` lorsque disponible)

Champs de fichier

Champs de fichier lorsqu’un PNG ou un PDF est rendu :

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (même valeur que `filePath`, pour la compatibilité avec l’outil de message)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

Alias de compatibilité

Également renvoyés pour les appelants existants :

  * `format` (même valeur que `fileFormat`)
  * `imagePath` (même valeur que `filePath`)
  * `imageBytes` (même valeur que `fileBytes`)
  * `imageQuality` (même valeur que `fileQuality`)
  * `imageScale` (même valeur que `fileScale`)
  * `imageMaxWidth` (même valeur que `fileMaxWidth`)


Résumé du comportement des modes :

Mode | Ce qui est renvoyé  
---|---  
`"view"` | Champs du visualiseur uniquement.  
`"file"` | Champs de fichier uniquement, aucun artefact de visualiseur.  
`"both"` | Champs du visualiseur plus champs de fichier. Si le rendu du fichier échoue, le visualiseur est quand même renvoyé avec l’alias `fileError` et `imageError`.  
  
## Sections inchangées repliées

  * Le visualiseur peut afficher des lignes comme `N unmodified lines`.
  * Les contrôles de développement sur ces lignes sont conditionnels et ne sont pas garantis pour chaque type d’entrée.
  * Les contrôles de développement apparaissent lorsque le diff rendu contient des données de contexte développables, ce qui est typique pour une entrée avant et après.
  * Pour de nombreuses entrées de patch unifié, les corps de contexte omis ne sont pas disponibles dans les hunks du patch analysé, donc la ligne peut apparaître sans contrôles de développement. Il s’agit du comportement attendu.
  * `expandUnchanged` ne s’applique que lorsqu’un contexte développable existe.


## Valeurs par défaut du plugin

Définissez les valeurs par défaut globales du plugin dans `~/.openclaw/openclaw.json` :

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

Valeurs par défaut prises en charge :

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


Les paramètres explicites de l’outil remplacent ces valeurs par défaut.

### Configuration d’URL de visualiseur persistante

Solution de repli détenue par le plugin pour les liens de visualiseur renvoyés lorsqu’un appel d’outil ne transmet pas `baseUrl`. Doit être `http` ou `https`, sans requête ni fragment.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## Configuration de sécurité

`false` : les requêtes non-loopback vers les routes du visualiseur sont refusées. `true` : les visualiseurs distants sont autorisés si le chemin avec jeton est valide.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## Cycle de vie et stockage des artefacts

  * Les artefacts sont stockés dans le sous-dossier temporaire : `$TMPDIR/openclaw-diffs`.
  * Les métadonnées d’artefact du visualiseur contiennent : 
    * un ID d’artefact aléatoire (20 caractères hexadécimaux)
    * un jeton aléatoire (48 caractères hexadécimaux)
    * `createdAt` et `expiresAt`
    * le chemin `viewer.html` stocké
  * La TTL d’artefact par défaut est de 30 minutes lorsqu’elle n’est pas spécifiée.
  * La TTL maximale acceptée pour le visualiseur est de 6 heures.
  * Le nettoyage s’exécute de manière opportuniste après la création de l’artefact.
  * Les artefacts expirés sont supprimés.
  * Le nettoyage de repli supprime les dossiers obsolètes de plus de 24 heures lorsque les métadonnées sont absentes.


## URL du visualiseur et comportement réseau

Route du visualiseur :

  * `/plugins/diffs/view/{artifactId}/{token}`


Ressources du visualiseur :

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


Le document du visualiseur résout ces ressources relativement à l’URL du visualiseur, donc un préfixe de chemin `baseUrl` facultatif est aussi conservé pour les deux requêtes de ressources.

Comportement de construction d’URL :

  * Si `baseUrl` de l’appel d’outil est fourni, il est utilisé après validation stricte.
  * Sinon, si `viewerBaseUrl` du plugin est configuré, il est utilisé.
  * Sans aucun remplacement, l’URL du visualiseur utilise par défaut le loopback `127.0.0.1`.
  * Si le mode de liaison du Gateway est `custom` et que `gateway.customBindHost` est défini, cet hôte est utilisé.


Règles de `baseUrl` :

  * Doit être `http://` ou `https://`.
  * La requête et le fragment sont rejetés.
  * L’origine plus un chemin de base facultatif est autorisée.


## Modèle de sécurité

Renforcement du visualiseur

  * Local loopback uniquement par défaut.
  * Chemins de visualiseur avec jeton, avec validation stricte de l’ID et du jeton.
  * CSP de réponse du visualiseur : 
    * `default-src 'none'`
    * scripts et ressources uniquement depuis la même origine
    * aucun `connect-src` sortant
  * Limitation des échecs distants lorsque l’accès distant est activé : 
    * 40 échecs par 60 secondes
    * verrouillage de 60 secondes (`429 Too Many Requests`)

Renforcement du rendu des fichiers

  * Le routage des requêtes du navigateur de capture d’écran refuse tout par défaut.
  * Seules les ressources locales du visualiseur depuis `http://127.0.0.1/plugins/diffs/assets/*` sont autorisées.
  * Les requêtes réseau externes sont bloquées.


## Exigences de navigateur pour le mode fichier

`mode: "file"` et `mode: "both"` nécessitent un navigateur compatible avec Chromium.

Ordre de résolution :

* ### Configuration

`browser.executablePath` dans la configuration OpenClaw.

* ### Variables d’environnement

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### Solution de repli de la plateforme

Solution de repli de découverte de commande/chemin de la plateforme.

Texte d’échec courant :

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


Corrigez en installant Chrome, Chromium, Edge ou Brave, ou en définissant l’une des options de chemin d’exécutable ci-dessus.

## Dépannage

Erreurs de validation d’entrée

  * `Provide patch or both before and after text.` — incluez à la fois `before` et `after`, ou fournissez `patch`.
  * `Provide either patch or before/after input, not both.` — ne mélangez pas les modes d’entrée.
  * `Invalid baseUrl: ...` — utilisez une origine `http(s)` avec un chemin facultatif, sans requête ni fragment.
  * `{field} exceeds maximum size (...)` — réduisez la taille de la charge utile.
  * Rejet d’un correctif volumineux — réduisez le nombre de fichiers du correctif ou le nombre total de lignes.

Accessibilité du visualiseur

  * L’URL du visualiseur se résout vers `127.0.0.1` par défaut.
  * Pour les scénarios d’accès distant, vous pouvez : 
    * définir le `viewerBaseUrl` du Plugin, ou
    * passer `baseUrl` à chaque appel d’outil, ou
    * utiliser `gateway.bind=custom` et `gateway.customBindHost`
  * Si `gateway.trustedProxies` inclut le local loopback pour un proxy sur le même hôte (par exemple Tailscale Serve), les requêtes brutes du visualiseur en local loopback sans en-têtes d’IP client transférés échouent de manière fermée par conception.
  * Pour cette topologie de proxy : 
    * préférez `mode: "file"` ou `mode: "both"` lorsque vous avez seulement besoin d’une pièce jointe, ou
    * activez intentionnellement `security.allowRemoteViewer` et définissez le `viewerBaseUrl` du Plugin ou passez un `baseUrl` proxy/public lorsque vous avez besoin d’une URL de visualiseur partageable
  * Activez `security.allowRemoteViewer` uniquement lorsque vous voulez permettre un accès externe au visualiseur.

La ligne des lignes non modifiées n’a pas de bouton de développement

Cela peut se produire pour une entrée de correctif lorsque le correctif ne contient pas de contexte développable. C’est attendu et cela n’indique pas un échec du visualiseur.

Artefact introuvable

  * L’artefact a expiré en raison de la TTL.
  * Le jeton ou le chemin a changé.
  * Le nettoyage a supprimé des données obsolètes.


## Conseils opérationnels

  * Préférez `mode: "view"` pour les revues interactives locales dans le canevas.
  * Préférez `mode: "file"` pour les canaux de discussion sortants qui nécessitent une pièce jointe.
  * Gardez `allowRemoteViewer` désactivé sauf si votre déploiement nécessite des URL de visualiseur distantes.
  * Définissez des `ttlSeconds` courts explicites pour les diffs sensibles.
  * Évitez d’envoyer des secrets dans l’entrée de diff lorsque ce n’est pas nécessaire.
  * Si votre canal compresse fortement les images (par exemple Telegram ou WhatsApp), préférez la sortie PDF (`fileFormat: "pdf"`).


## Connexe

  * [Navigateur](</fr/tools/browser>)
  * [Plugins](</fr/tools/plugin>)
  * [Vue d’ensemble des outils](</fr/tools>)


Was this useful?YesNo