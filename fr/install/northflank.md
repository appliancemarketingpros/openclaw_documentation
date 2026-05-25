---
title: Northflank
source_url: https://docs.openclaw.ai/fr/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Déployez OpenClaw sur Northflank avec un modèle en un clic et accédez-y via l’interface de contrôle web. C’est la voie la plus simple « sans terminal sur le serveur » : Northflank exécute le Gateway pour vous.

## Comment démarrer

  1. Cliquez sur [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) pour ouvrir le modèle.
  2. Créez un [compte sur Northflank](<https://app.northflank.com/signup>) si vous n’en avez pas déjà un.
  3. Cliquez sur **Deploy OpenClaw now**.
  4. Définissez la variable d’environnement requise : `OPENCLAW_GATEWAY_TOKEN` (utilisez une valeur aléatoire forte).
  5. Cliquez sur **Deploy stack** pour construire et exécuter le modèle OpenClaw.
  6. Attendez la fin du déploiement, puis cliquez sur **View resources**.
  7. Ouvrez le service OpenClaw.
  8. Ouvrez l’URL publique OpenClaw à `/openclaw` et connectez-vous à l’aide du secret partagé configuré. Ce modèle utilise `OPENCLAW_GATEWAY_TOKEN` par défaut ; si vous le remplacez par une authentification par mot de passe, utilisez ce mot de passe à la place.


## Ce que vous obtenez

  * Gateway OpenClaw hébergé + interface de contrôle
  * Stockage persistant via Northflank Volume (`/data`) afin que `openclaw.json`, `auth-profiles.json` par agent, l’état des canaux/fournisseurs, les sessions et l’espace de travail survivent aux redéploiements


## Connecter un canal

Utilisez l’interface de contrôle à `/openclaw` ou exécutez `openclaw onboard` via SSH pour obtenir les instructions de configuration des canaux :

  * [Telegram](</fr/channels/telegram>) (le plus rapide — juste un token de bot)
  * [Discord](</fr/channels/discord>)
  * [Tous les canaux](</fr/channels>)


## Étapes suivantes

  * Configurez les canaux de messagerie : [Channels](</fr/channels>)
  * Configurez le Gateway : [Configuration du Gateway](</fr/gateway/configuration>)
  * Gardez OpenClaw à jour : [Updating](</fr/install/updating>)


Was this useful?YesNo