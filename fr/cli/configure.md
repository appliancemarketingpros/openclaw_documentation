---
title: Configurer
source_url: https://docs.openclaw.ai/fr/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

Invite interactive pour apporter des modifications ciblées à une configuration existante : identifiants, appareils, valeurs par défaut des agents, Gateway, canaux, plugins, Skills et contrôles d’intégrité.

Utilisez `openclaw onboard` pour le parcours initial complet guidé, `openclaw setup` uniquement pour la configuration/l’espace de travail de base, et `openclaw channels add` lorsque vous avez seulement besoin de configurer un compte de canal.

Lorsque configure démarre depuis un choix d’authentification de fournisseur, les sélecteurs de modèle par défaut et de liste d’autorisation privilégient automatiquement ce fournisseur. Pour les fournisseurs associés comme Volcengine et BytePlus, la même préférence correspond également à leurs variantes de plans de codage (`volcengine-plan/*`, `byteplus-plan/*`). Si le filtre du fournisseur préféré produit une liste vide, configure revient au catalogue non filtré au lieu d’afficher un sélecteur vide.

Pour la recherche web, `openclaw configure --section web` vous permet de choisir un fournisseur et de configurer ses identifiants. Certains fournisseurs affichent également des invites de suivi propres au fournisseur :

  * **Grok** peut proposer une configuration facultative de `x_search` avec la même `XAI_API_KEY` et vous laisser choisir un modèle `x_search`.
  * **Kimi** peut demander la région de l’API Moonshot (`api.moonshot.ai` ou `api.moonshot.cn`) et le modèle de recherche web Kimi par défaut.


Connexe :

  * Référence de configuration du Gateway : [Configuration](</fr/gateway/configuration>)
  * CLI de configuration : [Config](</fr/cli/config>)


## Options

  * `--section <section>` : filtre de section répétable


Sections disponibles :

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


Notes :

  * Choisir où s’exécute le Gateway met toujours à jour `gateway.mode`. Vous pouvez sélectionner « Continuer » sans autres sections si c’est tout ce dont vous avez besoin.
  * Après les écritures dans la configuration locale, configure installe les plugins téléchargeables sélectionnés lorsque le parcours de configuration choisi les exige. La configuration d’un gateway distant n’installe pas de paquets de plugins locaux.
  * Les services orientés canal (Slack/Discord/Matrix/Microsoft Teams) demandent des listes d’autorisation de canaux/salles pendant la configuration. Vous pouvez saisir des noms ou des identifiants ; l’assistant résout les noms en identifiants lorsque c’est possible.
  * Si vous exécutez l’étape d’installation du daemon, que l’authentification par jeton exige un jeton et que `gateway.auth.token` est géré par SecretRef, configure valide le SecretRef mais ne persiste pas les valeurs de jeton en texte clair résolues dans les métadonnées d’environnement du service superviseur.
  * Si l’authentification par jeton exige un jeton et que le SecretRef de jeton configuré n’est pas résolu, configure bloque l’installation du daemon avec des conseils de remédiation exploitables.
  * Si `gateway.auth.token` et `gateway.auth.password` sont tous deux configurés et que `gateway.auth.mode` n’est pas défini, configure bloque l’installation du daemon jusqu’à ce que le mode soit défini explicitement.


## Exemples

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## Connexe

  * [Référence CLI](</fr/cli>)
  * [Configuration](</fr/gateway/configuration>)


Was this useful?YesNo