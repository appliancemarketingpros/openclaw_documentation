---
title: Webhooks
source_url: https://docs.openclaw.ai/fr/cli/webhooks
scraped_at: 2026-05-25
---

# `openclaw webhooks`

Assistants et intégrations Webhook. Aujourd’hui, cette surface est limitée aux flux Gmail Pub/Sub qui s’intègrent à l’observateur `gog` intégré.

## Sous-commandes

bashCopy code
[code]
    openclaw webhooks gmail setup --account <email> [...]openclaw webhooks gmail run   [--account <email>] [...]
[/code]

Sous-commande | Description  
---|---  
`gmail setup` | Configurer la surveillance Gmail, le sujet/l’abonnement Pub/Sub et la cible de livraison Webhook OpenClaw.  
`gmail run` | Exécuter `gog watch serve` plus la boucle de renouvellement automatique de la surveillance.  
  
## `webhooks gmail setup`

Configurer la surveillance Gmail, Pub/Sub et la livraison Webhook OpenClaw.

bashCopy code
[code]
    openclaw webhooks gmail setup --account you@example.comopenclaw webhooks gmail setup --account you@example.com --project my-gcp-project --jsonopenclaw webhooks gmail setup --account you@example.com --hook-url https://gateway.example.com/hooks/gmail
[/code]

### Requis

Option | Description  
---|---  
`--account <email>` | Compte Gmail à surveiller.  
  
### Options Pub/Sub

Option | Valeur par défaut | Description  
---|---|---  
`--project <id>` | (aucune) | ID du projet GCP (le propriétaire du client OAuth).  
`--topic <name>` | `gog-gmail-watch` | Nom du sujet Pub/Sub.  
`--subscription <name>` | `gog-gmail-watch-push` | Nom de l’abonnement Pub/Sub.  
`--label <label>` | `INBOX` | Libellé Gmail à surveiller.  
`--push-endpoint <url>` | (aucune) | Point de terminaison push Pub/Sub explicite. Remplace Tailscale.  
  
### Options de livraison OpenClaw

Option | Valeur par défaut | Description  
---|---|---  
`--hook-url <url>` | (aucune) | URL Webhook OpenClaw.  
`--hook-token <token>` | (aucune) | Jeton Webhook OpenClaw.  
`--push-token <token>` | (aucune) | Jeton push transmis à `gog watch serve`.  
  
### Options `gog watch serve`

Option | Valeur par défaut | Description  
---|---|---  
`--bind <host>` | `127.0.0.1` | Hôte de liaison de `gog watch serve`.  
`--port <port>` | `8788` | Port de `gog watch serve`.  
`--path <path>` | `/gmail-pubsub` | Chemin de `gog watch serve`.  
`--include-body` | `true` | Inclure les extraits du corps des e-mails. Passez `--no-include-body` pour désactiver.  
`--max-bytes <n>` | `20000` | Nombre maximal d’octets par extrait de corps.  
`--renew-minutes <n>` | `720` (12h) | Renouveler la surveillance Gmail toutes les N minutes.  
  
### Exposition Tailscale

Option | Valeur par défaut | Description  
---|---|---  
`--tailscale <mode>` | `funnel` | Exposer le point de terminaison push via Tailscale : `funnel`, `serve` ou `off`.  
`--tailscale-path <path>` | (aucune) | Chemin pour Tailscale serve/funnel.  
`--tailscale-target <t>` | (aucune) | Cible Tailscale serve/funnel (port, `host:port` ou URL).  
  
### Sortie

Option | Description  
---|---  
`--json` | Afficher un résumé lisible par machine au lieu de texte.  
  
## `webhooks gmail run`

Exécuter `gog watch serve` plus la boucle de renouvellement automatique de la surveillance au premier plan.

bashCopy code
[code]
    openclaw webhooks gmail run --account you@example.com
[/code]

`run` accepte les mêmes options `gog watch serve`, de livraison OpenClaw, Pub/Sub et Tailscale que `setup`, sauf :

  * `--account` est **facultatif** sur `run` (il revient au compte configuré).
  * `run` n’accepte **pas** `--project`, `--push-endpoint` ni `--json`.
  * Les options de `run` n’ont pas de valeurs par défaut intégrées ; les valeurs manquantes reviennent aux valeurs écrites par `setup`.

Catégorie | Options  
---|---  
Pub/Sub | `--account`, `--topic`, `--subscription`, `--label`  
Livraison OpenClaw | `--hook-url`, `--hook-token`, `--push-token`  
`gog watch serve` | `--bind`, `--port`, `--path`, `--include-body`, `--max-bytes`, `--renew-minutes`  
Tailscale | `--tailscale`, `--tailscale-path`, `--tailscale-target`  
  
## Flux de bout en bout

Consultez [l’intégration Gmail Pub/Sub](</fr/automation/cron-jobs#gmail-pubsub-integration>) pour la configuration du projet GCP, d’OAuth et côté Gateway qui va avec ces commandes CLI.

## Connexe

  * [Référence CLI](</fr/cli>)
  * [Automatisation Webhook](</fr/automation/cron-jobs>)
  * [Gmail Pub/Sub](</fr/automation/cron-jobs#gmail-pubsub-integration>)


Was this useful?YesNo