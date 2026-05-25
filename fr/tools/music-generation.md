---
title: Génération de musique
source_url: https://docs.openclaw.ai/fr/tools/music-generation
scraped_at: 2026-05-25
---

L’outil `music_generate` permet à l’agent de créer de la musique ou de l’audio via la capacité partagée de génération musicale avec des fournisseurs configurés — Google, MiniMax, et ComfyUI configuré par workflow aujourd’hui.

Pour les exécutions d’agent adossées à une session, OpenClaw lance la génération musicale comme une tâche en arrière-plan, la suit dans le registre des tâches, puis réveille à nouveau l’agent lorsque la piste est prête afin que l’agent puisse prévenir l’utilisateur et joindre l’audio terminé. Dans les discussions de groupe/canal qui utilisent une livraison visible uniquement via l’outil de message, l’agent relaie le résultat via l’outil de message. Si l’agent de complétion écrit uniquement une réponse finale privée, OpenClaw se rabat sur un envoi direct au canal avec le média généré. Le réveil de complétion avertit explicitement l’agent que les réponses finales normales sont privées dans ces routes.

## Démarrage rapide

### Shared provider-backed

* ### Configure auth

Définissez une clé d’API pour au moins un fournisseur — par exemple `GEMINI_API_KEY` ou `MINIMAX_API_KEY`.

* ### Pick a default model (optional)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Ask the agent

_« Génère une piste synthpop entraînante sur une conduite de nuit à travers une ville au néon. »_

L’agent appelle automatiquement `music_generate`. Aucune liste d’autorisation d’outils n’est nécessaire.

Pour les contextes synchrones directs sans exécution d’agent adossée à une session, l’outil intégré se rabat tout de même sur une génération en ligne et renvoie le chemin du média final dans le résultat de l’outil.

### ComfyUI workflow

* ### Configure the workflow

Configurez `plugins.entries.comfy.config.music` avec un workflow JSON et des nœuds d’invite/de sortie.

* ### Cloud auth (optional)

Pour Comfy Cloud, définissez `COMFY_API_KEY` ou `COMFY_CLOUD_API_KEY`.

* ### Call the tool

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Exemples d’invites :

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Fournisseurs pris en charge

Fournisseur | Modèle par défaut | Entrées de référence | Contrôles pris en charge | Authentification  
---|---|---|---|---  
ComfyUI | `workflow` | Jusqu’à 1 image | Musique ou audio défini par le workflow | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Jusqu’à 10 images | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Aucune | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` ou OAuth MiniMax  
  
### Matrice de capacités

Le contrat de mode explicite utilisé par `music_generate`, les tests de contrat et le balayage live partagé :

Fournisseur | `generate` | `edit` | Limite de modification | Voies live partagées  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 image | Non inclus dans le balayage partagé ; couvert par `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 images | `generate`, `edit`  
MiniMax | ✓ | — | Aucune | `generate`  
  
Utilisez `action: "list"` pour inspecter les fournisseurs et modèles partagés disponibles à l’exécution :

textCopy code
[code]
    /tool music_generate action=list
[/code]

Utilisez `action: "status"` pour inspecter la tâche musicale active adossée à une session :

textCopy code
[code]
    /tool music_generate action=status
[/code]

Exemple de génération directe :

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Paramètres de l’outil

Invite de génération musicale. Requise pour `action: "generate"`.

`"status"` renvoie la tâche de session actuelle ; `"list"` inspecte les fournisseurs.

Remplacement fournisseur/modèle (par ex. `google/lyria-3-pro-preview`, `comfy/workflow`).

Paroles facultatives lorsque le fournisseur prend en charge une entrée de paroles explicite.

Demande une sortie uniquement instrumentale lorsque le fournisseur la prend en charge.

Chemin ou URL d’une seule image de référence.

Plusieurs images de référence (jusqu’à 10 avec les fournisseurs compatibles).

Durée cible en secondes lorsque le fournisseur prend en charge les indications de durée.

Indication de format de sortie lorsque le fournisseur la prend en charge.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Délai d’expiration facultatif de la requête fournisseur, en millisecondes. S’il est omis, OpenClaw utilise `agents.defaults.musicGenerationModel.timeoutMs` s’il est configuré. Les valeurs inférieures à 10000ms sont relevées à 10000ms et signalées dans le résultat de l’outil. OPENCLAW_DOCS_MARKER:paramClose:

## Comportement asynchrone

La génération musicale adossée à une session s’exécute comme tâche en arrière-plan :

  * **Tâche en arrière-plan :** `music_generate` crée une tâche en arrière-plan, renvoie immédiatement une réponse démarrée/tâche, et publie la piste terminée plus tard dans un message d’agent de suivi.
  * **Prévention des doublons :** tant qu’une tâche est `queued` ou `running`, les appels `music_generate` ultérieurs dans la même session renvoient l’état de la tâche au lieu de lancer une autre génération. Utilisez `action: "status"` pour vérifier explicitement.
  * **Consultation de l’état :** `openclaw tasks list` ou `openclaw tasks show <taskId>` inspecte les états en file d’attente, en cours d’exécution et terminaux.
  * **Réveil de complétion :** OpenClaw injecte un événement de complétion interne dans la même session afin que le modèle puisse écrire lui-même le suivi visible par l’utilisateur.
  * **Indice d’invite :** les tours utilisateur/manuels ultérieurs dans la même session reçoivent un petit indice d’exécution lorsqu’une tâche musicale est déjà en cours, afin que le modèle n’appelle pas aveuglément `music_generate` à nouveau.
  * **Repli sans session :** les contextes directs/locaux sans véritable session d’agent s’exécutent en ligne et renvoient le résultat audio final dans le même tour.


### Cycle de vie de la tâche

État | Signification  
---|---  
`queued` | Tâche créée, en attente d’acceptation par le fournisseur.  
`running` | Le fournisseur traite la requête (généralement 30 secondes à 3 minutes selon le fournisseur et la durée).  
`succeeded` | Piste prête ; l’agent se réveille et la publie dans la conversation.  
`failed` | Erreur fournisseur ou délai expiré ; l’agent se réveille avec les détails de l’erreur.  
  
Vérifier l’état depuis la CLI :

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Configuration

### Sélection du modèle

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Ordre de sélection des fournisseurs

OpenClaw essaie les fournisseurs dans cet ordre :

  1. Paramètre `model` de l’appel d’outil (si l’agent en spécifie un).
  2. `musicGenerationModel.primary` depuis la configuration.
  3. `musicGenerationModel.fallbacks` dans l’ordre.
  4. Détection automatique utilisant uniquement les valeurs par défaut des fournisseurs adossés à une authentification : 
     * fournisseur par défaut actuel en premier ;
     * fournisseurs de génération musicale enregistrés restants dans l’ordre des identifiants de fournisseur.


Si un fournisseur échoue, le candidat suivant est essayé automatiquement. S’ils échouent tous, l’erreur inclut les détails de chaque tentative.

Définissez `agents.defaults.mediaGenerationAutoProviderFallback: false` pour utiliser uniquement les entrées explicites `model`, `primary` et `fallbacks`.

## Notes sur les fournisseurs

ComfyUI

Piloté par workflow, et dépend du graphe configuré ainsi que de la correspondance des nœuds pour les champs d’invite/de sortie. Le Plugin `comfy` inclus s’intègre à l’outil partagé `music_generate` via le registre des fournisseurs de génération musicale.

Google (Lyria 3)

Utilise la génération par lots Lyria 3. Le flux inclus actuel prend en charge l’invite, le texte de paroles facultatif et les images de référence facultatives.

MiniMax

Utilise le point de terminaison par lots `music_generation`. Prend en charge l’invite, les paroles facultatives, le mode instrumental, le guidage de durée et la sortie mp3 via une authentification par clé d’API `minimax` ou OAuth `minimax-portal`.

## Choisir le bon chemin

  * **Adossé à un fournisseur partagé** lorsque vous voulez la sélection de modèle, le basculement entre fournisseurs et le flux intégré de tâche/état asynchrone.
  * **Chemin Plugin (ComfyUI)** lorsque vous avez besoin d’un graphe de workflow personnalisé ou d’un fournisseur qui ne fait pas partie de la capacité musicale partagée incluse.


Si vous déboguez un comportement propre à ComfyUI, consultez [ComfyUI](</fr/providers/comfy>). Si vous déboguez le comportement du fournisseur partagé, commencez par [Google (Gemini)](</fr/providers/google>) ou [MiniMax](</fr/providers/minimax>).

## Modes de capacité des fournisseurs

Le contrat partagé de génération musicale prend en charge des déclarations de mode explicites :

  * `generate` pour la génération à partir d’une invite seule.
  * `edit` lorsque la requête inclut une ou plusieurs images de référence.


Les nouvelles implémentations de fournisseur devraient privilégier des blocs de mode explicites :

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Les champs plats hérités tels que `maxInputImages`, `supportsLyrics` et `supportsFormat` ne suffisent **pas** à annoncer la prise en charge de la modification. Les fournisseurs devraient déclarer explicitement `generate` et `edit` afin que les tests live, les tests de contrat et l’outil partagé `music_generate` puissent valider la prise en charge des modes de manière déterministe.

## Tests live

Couverture live optionnelle pour les fournisseurs inclus partagés :

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Wrapper du dépôt :

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Ce fichier live charge les variables d'environnement de fournisseur manquantes depuis `~/.profile`, privilégie par défaut les clés d'API live/env par rapport aux profils d'authentification stockés, et exécute à la fois la couverture `generate` et la couverture `edit` déclarée lorsque le fournisseur active le mode d'édition. Couverture actuelle :

  * `google` : `generate` plus `edit`
  * `minimax` : `generate` uniquement
  * `comfy` : couverture live Comfy distincte, pas le balayage partagé des fournisseurs


Couverture live optionnelle pour le chemin musical ComfyUI inclus :

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Le fichier live Comfy couvre aussi les workflows d'image et de vidéo comfy lorsque ces sections sont configurées.

## Voir aussi

  * [Tâches en arrière-plan](</fr/automation/tasks>) — suivi des tâches pour les exécutions `music_generate` détachées
  * [ComfyUI](</fr/providers/comfy>)
  * [Référence de configuration](</fr/gateway/config-agents#agent-defaults>) — configuration `musicGenerationModel`
  * [Google (Gemini)](</fr/providers/google>)
  * [MiniMax](</fr/providers/minimax>)
  * [Modèles](</fr/concepts/models>) — configuration des modèles et basculement
  * [Vue d'ensemble des outils](</fr/tools>)


Was this useful?YesNo