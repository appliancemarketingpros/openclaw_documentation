---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/fr/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw inclut un plugin `alibaba` intégré qui enregistre un fournisseur de génération vidéo pour les modèles Wan sur Alibaba Model Studio (le nom international de DashScope). Le plugin est activé par défaut ; vous devez seulement définir une clé API.

Propriété | Valeur  
---|---  
ID du fournisseur | `alibaba`  
Plugin | intégré, `enabledByDefault: true`  
Variables d’environnement d’auth | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (la première correspondance l’emporte)  
Indicateur d’onboarding | `--auth-choice alibaba-model-studio-api-key`  
Indicateur CLI direct | `--alibaba-model-studio-api-key <key>`  
Modèle par défaut | `alibaba/wan2.6-t2v`  
URL de base par défaut | `https://dashscope-intl.aliyuncs.com`  
  
## Premiers pas

* ### Définir une clé API

Utilisez l’onboarding pour stocker la clé pour le fournisseur `alibaba` :

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Ou transmettez la clé directement pendant l’installation/onboarding :

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Ou exportez l’une des variables d’environnement acceptées avant de démarrer le Gateway :

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Définir un modèle vidéo par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Vérifier que le fournisseur est configuré

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

La liste doit inclure les cinq modèles Wan intégrés. Si `MODELSTUDIO_API_KEY` n’est pas résolue, `openclaw models status --json` signale l’identifiant manquant sous `auth.unusableProfiles`.

## Modèles Wan intégrés

Référence du modèle | Mode  
---|---  
`alibaba/wan2.6-t2v` | Texte vers vidéo (par défaut)  
`alibaba/wan2.6-i2v` | Image vers vidéo  
`alibaba/wan2.6-r2v` | Référence vers vidéo  
`alibaba/wan2.6-r2v-flash` | Référence vers vidéo (rapide)  
`alibaba/wan2.7-r2v` | Référence vers vidéo  
  
## Capacités et limites

Le fournisseur intégré reflète les limites de l’API vidéo Wan de DashScope. Les trois modes partagent le même plafond de nombre de vidéos et de durée par requête ; seule la forme de l’entrée diffère.

Mode | Nombre max. de vidéos en sortie | Nombre max. d’images en entrée | Nombre max. de vidéos en entrée | Durée max. | Contrôles pris en charge  
---|---|---|---|---|---  
Texte vers vidéo | 1 | s/o | s/o | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Image vers vidéo | 1 | 1 | s/o | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Référence vers vidéo | 1 | s/o | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Lorsqu’une requête omet `durationSeconds`, le fournisseur envoie la valeur par défaut acceptée par DashScope, soit **5 secondes**. Définissez explicitement `durationSeconds` dans l’[outil de génération vidéo](</fr/tools/video-generation>) pour l’étendre jusqu’à 10 s.

## Configuration avancée

Remplacer l’URL de base de DashScope

Le fournisseur utilise par défaut le point de terminaison international de DashScope. Pour cibler le point de terminaison de la région Chine, définissez :

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

Le fournisseur supprime les barres obliques finales avant de construire les URL de tâches AIGC.

Priorité des variables d’environnement d’auth

OpenClaw résout la clé API Alibaba depuis les variables d’environnement dans cet ordre, en prenant la première valeur non vide :

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Les entrées `auth.profiles` configurées (définies via `openclaw models auth login`) remplacent la résolution des variables d’environnement. Consultez les [profils d’auth dans la FAQ des modèles](</fr/help/faq-models#what-is-an-auth-profile>) pour la rotation des profils, le cooldown et les mécanismes de remplacement.

Relation avec le plugin Qwen

Les deux plugins intégrés communiquent avec DashScope et acceptent des clés API qui se chevauchent. Utilisez :

  * les ID `alibaba/wan*.*` pour piloter le fournisseur vidéo Wan dédié documenté sur cette page.
  * les ID `qwen/*` pour la discussion, l’embedding et la compréhension multimédia Qwen (voir [Qwen](</fr/providers/qwen>)).


Définir `MODELSTUDIO_API_KEY` une seule fois authentifie les deux plugins, car la liste des variables d’environnement d’auth se chevauche intentionnellement ; vous n’avez pas besoin d’onboarder chaque plugin séparément.

## Associés

[**Génération vidéo** Paramètres partagés de l’outil vidéo et sélection du fournisseur. ](</fr/tools/video-generation>) [**Qwen** Configuration de la discussion, de l’embedding et de la compréhension multimédia Qwen avec la même authentification DashScope. ](</fr/providers/qwen>) [**Référence de configuration** Valeurs par défaut des agents et configuration des modèles. ](</fr/gateway/config-agents#agent-defaults>) [**FAQ des modèles** Profils d’auth, changement de modèles et résolution des erreurs « no profile ». ](</fr/help/faq-models>)

Was this useful?YesNo