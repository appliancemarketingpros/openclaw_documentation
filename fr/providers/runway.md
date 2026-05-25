---
title: Piste
source_url: https://docs.openclaw.ai/fr/providers/runway
scraped_at: 2026-05-25
---

OpenClaw inclut un fournisseur `runway` groupé pour la génération de vidéos hébergée. Le Plugin est activé par défaut et enregistre le fournisseur `runway` avec le contrat `videoGenerationProviders`.

Propriété | Valeur  
---|---  
ID du fournisseur | `runway`  
Plugin | groupé, `enabledByDefault: true`  
Variables d’environnement d’authentification | `RUNWAYML_API_SECRET` (canonique) ou `RUNWAY_API_KEY`  
Option d’intégration | `--auth-choice runway-api-key`  
Option CLI directe | `--runway-api-key <key>`  
API | Génération de vidéos Runway basée sur des tâches (interrogation `GET /v1/tasks/{id}`)  
Modèle par défaut | `runway/gen4.5`  
  
## Démarrage

* ### Définir la clé API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Définir Runway comme fournisseur vidéo par défaut

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Générer une vidéo

Demandez à l’agent de générer une vidéo. Runway sera utilisé automatiquement.

## Modes et modèles pris en charge

Le fournisseur expose sept modèles Runway répartis entre trois modes. Le même ID de modèle peut servir plusieurs modes (par exemple, `gen4.5` fonctionne à la fois pour le texte-vers-vidéo et l’image-vers-vidéo).

Mode | Modèles | Entrée de référence  
---|---|---  
Texte-vers-vidéo | `gen4.5` (par défaut), `veo3.1`, `veo3.1_fast`, `veo3` | Aucune  
Image-vers-vidéo | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 image locale ou distante  
Vidéo-vers-vidéo | `gen4_aleph` | 1 vidéo locale ou distante  
  
Les références locales à des images et vidéos sont prises en charge via des URI de données.

Rapports d’aspect | Valeurs autorisées  
---|---  
Texte-vers-vidéo | `16:9`, `9:16`  
Modifications d’images et de vidéos | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Configuration

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Configuration avancée

Alias de variables d’environnement

OpenClaw reconnaît à la fois `RUNWAYML_API_SECRET` (canonique) et `RUNWAY_API_KEY`. L’une ou l’autre variable authentifiera le fournisseur Runway.

Interrogation des tâches

Runway utilise une API basée sur des tâches. Après l’envoi d’une demande de génération, OpenClaw interroge `GET /v1/tasks/{id}` jusqu’à ce que la vidéo soit prête. Aucune configuration supplémentaire n’est nécessaire pour le comportement d’interrogation.

## Connexe

[**Génération de vidéos** Paramètres d’outil partagés, sélection du fournisseur et comportement asynchrone. ](</fr/tools/video-generation>) [**Référence de configuration** Paramètres par défaut de l’agent, y compris le modèle de génération vidéo. ](</fr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo