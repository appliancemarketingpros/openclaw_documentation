---
title: Journaux
source_url: https://docs.openclaw.ai/fr/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Affiche la fin des journaux de fichier du Gateway via RPC (fonctionne en mode distant).

Associé :

  * Vue d’ensemble de la journalisation : [Journalisation](</fr/logging>)
  * CLI du Gateway : [gateway](</fr/cli/gateway>)


## Options

  * `--limit <n>` : nombre maximal de lignes de journal à renvoyer (par défaut `200`)
  * `--max-bytes <n>` : nombre maximal d’octets à lire depuis le fichier journal (par défaut `250000`)
  * `--follow` : suivre le flux de journaux
  * `--interval <ms>` : intervalle d’interrogation pendant le suivi (par défaut `1000`)
  * `--json` : émettre des événements JSON délimités par ligne
  * `--plain` : sortie en texte brut sans mise en forme stylisée
  * `--no-color` : désactiver les couleurs ANSI
  * `--local-time` : afficher les horodatages dans votre fuseau horaire local


## Options RPC partagées du Gateway

`openclaw logs` accepte aussi les indicateurs client standard du Gateway :

  * `--url <url>` : URL WebSocket du Gateway
  * `--token <token>` : jeton du Gateway
  * `--timeout <ms>` : délai d’expiration en ms (par défaut `30000`)
  * `--expect-final` : attendre une réponse finale lorsque l’appel au Gateway est adossé à un agent


Lorsque vous passez `--url`, la CLI n’applique pas automatiquement la configuration ni les identifiants d’environnement. Incluez explicitement `--token` si le Gateway cible exige une authentification.

## Exemples

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## Notes

  * Utilisez `--local-time` pour afficher les horodatages dans votre fuseau horaire local.
  * Si le Gateway local loopback implicite demande un appairage, se ferme pendant la connexion ou expire avant que `logs.tail` ne réponde, `openclaw logs` se rabat automatiquement sur le journal de fichier configuré du Gateway. Les cibles `--url` explicites n’utilisent pas ce repli.
  * Lorsque vous utilisez `--follow`, les déconnexions transitoires du gateway (fermeture WebSocket, délai d’expiration, perte de connexion) déclenchent une reconnexion automatique avec backoff exponentiel (jusqu’à 8 tentatives, plafonnées à 30 s entre les tentatives). Un avertissement est imprimé sur stderr à chaque nouvelle tentative, et un avis `[logs] gateway reconnected` est imprimé dès qu’une interrogation réussit. En mode `--json`, l’avertissement de nouvelle tentative et la transition de reconnexion sont tous deux émis sous forme d’enregistrements `{"type":"notice"}` sur stderr. Les erreurs non récupérables (échec d’authentification, mauvaise configuration) provoquent toujours une sortie immédiate.


## Associé

  * [Référence CLI](</fr/cli>)
  * [Journalisation du Gateway](</fr/gateway/logging>)


Was this useful?YesNo