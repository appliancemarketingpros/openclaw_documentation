---
title: Tableau de bord
source_url: https://docs.openclaw.ai/fr/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Ouvrez l’interface utilisateur de contrôle avec votre authentification actuelle.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Notes :

  * `dashboard` résout les SecretRefs `gateway.auth.token` configurées lorsque c’est possible.
  * `dashboard` suit `gateway.tls.enabled` : les passerelles avec TLS activé affichent/ouvrent des URL d’interface utilisateur de contrôle en `https://` et se connectent via `wss://`.
  * Si la livraison via le presse-papiers ou le navigateur échoue pour une URL de tableau de bord authentifiée par jeton, `dashboard` consigne un indice sûr d’authentification manuelle nommant `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` et la clé de fragment `token`, sans afficher la valeur du jeton.
  * Pour les jetons gérés par SecretRef (résolus ou non résolus), `dashboard` affiche/copie/ouvre une URL sans jeton afin d’éviter d’exposer des secrets externes dans la sortie du terminal, l’historique du presse-papiers ou les arguments de lancement du navigateur.
  * Si `gateway.auth.token` est géré par SecretRef mais non résolu dans ce chemin de commande, la commande affiche une URL sans jeton et des consignes de correction explicites au lieu d’intégrer un espace réservé de jeton invalide.


## Associé

  * [Référence CLI](</fr/cli>)
  * [Tableau de bord](</fr/web/dashboard>)


Was this useful?YesNo