---
title: Intégration (application macOS)
source_url: https://docs.openclaw.ai/fr/start/onboarding
scraped_at: 2026-05-25
---

Ce document décrit le flux de configuration au premier lancement **actuel**. L’objectif est une expérience fluide de « jour 0 » : choisir où le Gateway s’exécute, connecter l’authentification, exécuter l’assistant et laisser l’agent s’amorcer lui-même. Pour un aperçu général des parcours d’onboarding, consultez [Aperçu de l’onboarding](</fr/start/onboarding-overview>).

* ### Approuver l’avertissement macOS

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Autoriser la recherche de réseaux locaux

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Accueil et avis de sécurité

Lisez l’avis de sécurité affiché et décidez en conséquence ![](/assets/macos-onboarding/03-security-notice.png)

Modèle de confiance de sécurité :

  * Par défaut, OpenClaw est un agent personnel : une seule frontière d’opérateur de confiance.
  * Les configurations partagées/multi-utilisateurs nécessitent un verrouillage (séparer les frontières de confiance, garder l’accès aux outils minimal et suivre [Sécurité](</fr/gateway/security>)).
  * L’onboarding local définit désormais par défaut les nouvelles configurations sur `tools.profile: "coding"` afin que les nouvelles configurations locales conservent les outils de système de fichiers/d’exécution sans imposer le profil `full` sans restriction.
  * Si des hooks/webhooks ou d’autres flux de contenu non fiable sont activés, utilisez un niveau de modèle moderne robuste et maintenez une politique d’outils/un sandboxing stricts.


* ### Local ou distant

![](/assets/macos-onboarding/04-choose-gateway.png)

Où le **Gateway** s’exécute-t-il ?

  * **Ce Mac (local uniquement) :** l’onboarding peut configurer l’authentification et écrire les identifiants localement.
  * **Distant (via SSH/Tailnet) :** l’onboarding ne configure **pas** l’authentification locale ; les identifiants doivent exister sur l’hôte du gateway.
  * **Configurer plus tard :** ignorer la configuration et laisser l’app non configurée.


* ### Autorisations

Choisissez les autorisations que vous souhaitez accorder à OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

L’onboarding demande les autorisations TCC nécessaires pour :

  * Automatisation (AppleScript)
  * Notifications
  * Accessibilité
  * Enregistrement de l’écran
  * Microphone
  * Reconnaissance vocale
  * Appareil photo
  * Localisation


* ### CLI

* ### Chat d’onboarding (session dédiée)

Après la configuration, l’app ouvre une session de chat d’onboarding dédiée afin que l’agent puisse se présenter et guider les prochaines étapes. Cela sépare les conseils du premier lancement de votre conversation normale. Consultez [Amorçage](</fr/start/bootstrapping>) pour savoir ce qui se passe sur l’hôte du gateway pendant la première exécution de l’agent.

## Liens connexes

  * [Aperçu de l’onboarding](</fr/start/onboarding-overview>)
  * [Premiers pas](</fr/start/getting-started>)


Was this useful?YesNo