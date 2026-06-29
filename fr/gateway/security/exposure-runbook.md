---
title: Runbook d’exposition du Gateway
source_url: https://docs.openclaw.ai/fr/gateway/security/exposure-runbook
scraped_at: 2026-06-29
---

Gateway & OpsGateway

Ce runbook transforme les recommandations générales de [Sécurité](</fr/gateway/security>) en une check-list opérateur pour l’accès distant et l’exposition de la messagerie.

## Choisir le modèle d’exposition

Préférez le modèle le plus restreint qui satisfait le workflow.

Modèle | Recommandé lorsque | Contrôles requis  
---|---|---  
Bouclage + tunnel SSH | Usage personnel, accès admin, débogage | Conserver `gateway.bind: "loopback"` et créer un tunnel vers `127.0.0.1:18789`  
Bouclage + Tailscale Serve | Accès au tailnet personnel à l’interface de contrôle/WebSocket | Garder le Gateway limité au bouclage ; s’appuyer sur les en-têtes d’identité Tailscale uniquement pour les surfaces prises en charge  
Liaison tailnet/LAN | Réseau privé dédié avec appareils connus | Authentification du Gateway, liste d’autorisation du pare-feu, aucun transfert de port public  
Proxy inverse approuvé | SSO/OIDC d’organisation devant le Gateway | Authentification `trusted-proxy`, `trustedProxies` stricts, règles d’écrasement/suppression des en-têtes, utilisateurs autorisés explicites  
Internet public | Déploiements rares et à haut risque | Proxy sensible à l’identité, TLS, limites de débit, listes d’autorisation strictes, sessions non-main isolées  
  
Évitez le transfert direct d’un port public vers le Gateway. Si vous avez besoin d’un accès public, placez un proxy sensible à l’identité devant lui et faites du proxy le seul chemin réseau vers le Gateway.

## Inventaire préliminaire

Consignez ces éléments avant de modifier la liaison, le proxy, Tailscale ou la politique de canal :

  * Hôte du Gateway, utilisateur de l’OS et répertoire d’état.
  * URL du Gateway et mode de liaison.
  * Mode d’authentification, source du jeton/mot de passe ou source d’identité du proxy approuvé.
  * Tous les canaux activés et s’ils acceptent les DM, les groupes ou les webhooks.
  * Agents joignables depuis des expéditeurs non locaux.
  * Profil d’outils, mode sandbox et politique d’outils élevés pour chaque agent joignable.
  * Identifiants externes disponibles pour ces agents.
  * Emplacement de sauvegarde de `~/.openclaw/openclaw.json` et des identifiants.


Si plus d’une personne peut envoyer un message au bot, traitez cela comme une autorité d’outil déléguée partagée, et non comme une isolation hôte par utilisateur.

## Vérifications de référence

Exécutez ces commandes avant d’ouvrir l’accès :

bashCopy code
[code]
    openclaw doctoropenclaw security auditopenclaw security audit --deepopenclaw health
[/code]

Résolvez d’abord les constats critiques. Les avertissements ne peuvent être acceptables que lorsqu’ils sont intentionnels et documentés pour le déploiement.

Pour la validation CLI distante, transmettez explicitement les identifiants :

bashCopy code
[code]
    openclaw gateway probe --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

Ne supposez pas que les identifiants de configuration locale s’appliquent à une URL distante explicite.

## Référence minimale sûre

Utilisez cette forme comme point de départ pour les déploiements exposés :

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    auth: {      mode: "token",      token: "replace-with-a-long-random-token",    },  },  session: {    dmScope: "per-channel-peer",  },  agents: {    defaults: {      sandbox: { mode: "non-main" },    },  },  tools: {    profile: "messaging",    exec: { security: "deny", ask: "always" },    elevated: { enabled: false },  },}
[/code]

Élargissez ensuite un contrôle à la fois. Par exemple, ajoutez une liste d’autorisation de canal spécifique avant d’activer des outils capables d’écrire, ou activez un proxy inverse avant d’accepter du trafic distant vers l’interface de contrôle.

La référence stricte `exec.security: "deny"` bloque tous les appels exec, y compris les diagnostics bénins. Si des diagnostics ou des commandes à faible risque sont nécessaires, n’assouplissez cela qu’après avoir choisi les expéditeurs, agents, commandes et modes d’approbation spécifiques qui correspondent à votre modèle de menace.

## Exposition des DM et des groupes

Les canaux de messagerie sont des surfaces d’entrée non fiables. Avant d’autoriser les DM ou les groupes :

  * Préférez `dmPolicy: "pairing"` ou des listes `allowFrom` strictes.
  * Évitez `dmPolicy: "open"` sauf si chaque expéditeur est approuvé.
  * Ne combinez pas des listes d’autorisation `"*"` avec un accès large aux outils.
  * Exigez des mentions dans les groupes sauf si le salon est strictement contrôlé.
  * Utilisez `session.dmScope: "per-channel-peer"` lorsque plusieurs personnes peuvent envoyer des DM au bot.
  * Routez les canaux partagés vers des agents avec un minimum d’outils et sans identifiants personnels.


Le jumelage autorise l’expéditeur à déclencher le bot. Il ne fait pas de cet expéditeur une frontière de sécurité hôte distincte.

## Vérifications du proxy inverse

Pour les proxys sensibles à l’identité :

  * Le proxy doit authentifier les utilisateurs avant de transférer vers le Gateway.
  * L’accès direct au port du Gateway doit être bloqué par un pare-feu ou une politique réseau.
  * `gateway.trustedProxies` ne doit contenir que les IP sources du proxy.
  * Le proxy doit supprimer ou écraser les en-têtes d’identité et de transfert fournis par le client.
  * `gateway.auth.trustedProxy.allowUsers` doit lister les utilisateurs attendus lorsque le proxy sert plusieurs audiences.
  * Le mode proxy de bouclage sur le même hôte ne doit utiliser `allowLoopback` que lorsque les processus locaux sont approuvés et que le proxy possède les en-têtes d’identité.


Exécutez `openclaw security audit --deep` après les changements de proxy. Les constats liés au proxy approuvé sont volontairement à fort signal, car le proxy devient la frontière d’authentification.

## Revue des outils et du sandbox

Avant d’exposer un agent à des expéditeurs distants :

  * Confirmez quelles sessions s’exécutent sur l’hôte plutôt que dans le sandbox.
  * Refusez ou exigez une approbation pour l’exec sur l’hôte.
  * Gardez les outils élevés désactivés sauf si un expéditeur spécifique et approuvé en a besoin.
  * Évitez les outils de navigateur, canvas, node, cron, gateway et génération de session pour les surfaces de messagerie ouvertes ou semi-ouvertes.
  * Gardez les montages de liaison restreints et évitez les chemins d’identifiants, de répertoire personnel, de socket Docker et de système.
  * Utilisez des gateways, utilisateurs OS ou hôtes séparés pour des frontières de confiance matériellement différentes.


Si les utilisateurs distants ne sont pas entièrement approuvés, l’isolation doit venir de déploiements séparés, pas seulement de prompts ou d’étiquettes de session.

## Validation après modification

Après chaque changement d’exposition :

  1. Relancez `openclaw security audit --deep`.
  2. Testez une connexion autorisée réussie.
  3. Testez qu’un expéditeur ou une session de navigateur non autorisé est refusé.
  4. Confirmez que les journaux masquent les secrets.
  5. Confirmez que le routage DM/groupe atteint uniquement l’agent prévu.
  6. Confirmez que les outils à fort impact demandent une approbation ou sont refusés.
  7. Documentez les avertissements résiduels acceptés.


Ne passez pas au changement d’exposition suivant tant que le changement actuel n’est pas compris.

## Plan de rollback

Si le Gateway peut être surexposé :

json5Copy code
[code]
    {  gateway: {    bind: "loopback",  },  channels: {    whatsapp: { dmPolicy: "disabled" },    telegram: { dmPolicy: "disabled" },    discord: { dmPolicy: "disabled" },    slack: { dmPolicy: "disabled" },  },  tools: {    exec: { security: "deny", ask: "always" },    elevated: { enabled: false },  },}
[/code]

Ensuite :

  1. Arrêtez le transfert public, Tailscale Funnel ou les routes de proxy inverse.
  2. Faites tourner les jetons/mots de passe du Gateway et les identifiants d’intégration affectés.
  3. Supprimez `"*"` et les expéditeurs inattendus des listes d’autorisation.
  4. Passez en revue les journaux d’audit récents, l’historique des exécutions, les appels d’outils et les changements de configuration.
  5. Relancez `openclaw security audit --deep`.
  6. Réactivez l’accès avec le modèle le plus restreint qui satisfait le workflow.


## Check-list de revue

  * Le Gateway reste limité au bouclage sauf raison documentée.
  * L’accès hors bouclage dispose d’une authentification, d’un filtrage pare-feu et d’aucune route directe publique.
  * Les déploiements avec proxy approuvé ont des IP de proxy et des contrôles d’en-têtes stricts.
  * Les DM utilisent le jumelage ou des listes d’autorisation, pas un accès ouvert par défaut.
  * Les groupes exigent des mentions ou des listes d’autorisation explicites.
  * Les canaux partagés n’atteignent pas les identifiants personnels.
  * Les sessions non-main s’exécutent en mode sandbox.
  * L’exec sur l’hôte et les outils élevés sont refusés ou soumis à approbation.
  * Les journaux masquent les secrets.
  * Les constats d’audit critiques sont résolus.
  * Les étapes de rollback sont testées et documentées.


Was this useful?YesNo

Open issue