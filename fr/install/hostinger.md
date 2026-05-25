---
title: Hostinger
source_url: https://docs.openclaw.ai/fr/install/hostinger
scraped_at: 2026-05-25
---

Exécutez un Gateway OpenClaw persistant sur [Hostinger](<https://www.hostinger.com/openclaw>) via un déploiement géré en **1 clic** ou une installation sur **VPS**.

## Prérequis

  * Compte Hostinger ([inscription](<https://www.hostinger.com/openclaw>))
  * Environ 5 à 10 minutes


## Option A : OpenClaw en 1 clic

Le moyen le plus rapide pour commencer. Hostinger gère l’infrastructure, Docker et les mises à jour automatiques.

* ### Acheter et lancer

  1. Depuis la [page Hostinger OpenClaw](<https://www.hostinger.com/openclaw>), choisissez un plan OpenClaw géré et terminez le paiement.


* ### Sélectionner un canal de messagerie

Choisissez un ou plusieurs canaux à connecter :

  * **WhatsApp** \-- scannez le code QR affiché dans l’assistant de configuration.
  * **Telegram** \-- collez le jeton du bot depuis [BotFather](<https://t.me/BotFather>).


* ### Terminer l’installation

Cliquez sur **Finish** pour déployer l’instance. Une fois prête, accédez au tableau de bord OpenClaw depuis **OpenClaw Overview** dans hPanel.

## Option B : OpenClaw sur VPS

Davantage de contrôle sur votre serveur. Hostinger déploie OpenClaw via Docker sur votre VPS et vous le gérez via le **Docker Manager** dans hPanel.

* ### Acheter un VPS

  1. Depuis la [page Hostinger OpenClaw](<https://www.hostinger.com/openclaw>), choisissez un plan OpenClaw sur VPS et terminez le paiement.


* ### Configurer OpenClaw

Une fois le VPS provisionné, remplissez les champs de configuration :

  * **Gateway token** \-- généré automatiquement ; enregistrez-le pour plus tard.
  * **WhatsApp number** \-- votre numéro avec indicatif de pays (facultatif).
  * **Telegram bot token** \-- depuis [BotFather](<https://t.me/BotFather>) (facultatif).
  * **API keys** \-- nécessaires uniquement si vous n’avez pas sélectionné de crédits Ready-to-Use AI pendant le paiement.


* ### Démarrer OpenClaw

Cliquez sur **Deploy**. Une fois lancé, ouvrez le tableau de bord OpenClaw depuis hPanel en cliquant sur **Open**.

Les journaux, redémarrages et mises à jour sont gérés directement depuis l’interface Docker Manager dans hPanel. Pour mettre à jour, cliquez sur **Update** dans Docker Manager ; cela récupérera la dernière image.

## Vérifier votre configuration

Envoyez « Hi » à votre assistant sur le canal que vous avez connecté. OpenClaw répondra et vous guidera dans les préférences initiales.

## Dépannage

**Le tableau de bord ne se charge pas** \-- Attendez quelques minutes que le conteneur termine son provisionnement. Vérifiez les journaux Docker Manager dans hPanel.

**Le conteneur Docker redémarre sans cesse** \-- Ouvrez les journaux Docker Manager et recherchez des erreurs de configuration (jetons manquants, clés API invalides).

**Le bot Telegram ne répond pas** \-- Envoyez votre message de code de pairing depuis Telegram directement comme message dans votre discussion OpenClaw pour terminer la connexion.

## Prochaines étapes

  * [Canaux](</fr/channels>) \-- connecter Telegram, WhatsApp, Discord, et plus encore
  * [Configuration du Gateway](</fr/gateway/configuration>) \-- toutes les options de configuration


## Articles connexes

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Hébergement VPS](</fr/vps>)
  * [DigitalOcean](</fr/install/digitalocean>)


Was this useful?YesNo