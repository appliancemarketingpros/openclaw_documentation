---
title: Plugin Webhooks
source_url: https://docs.openclaw.ai/fr/plugins/webhooks
scraped_at: 2026-05-25
---

Le Plugin Webhooks ajoute des routes HTTP authentifiées qui relient l’automatisation externe aux TaskFlows OpenClaw.

Utilisez-le lorsque vous voulez qu’un système approuvé, comme Zapier, n8n, une tâche CI ou un service interne, crée et pilote des TaskFlows gérés sans écrire d’abord de Plugin personnalisé.

## Où il s’exécute

Le Plugin Webhooks s’exécute dans le processus Gateway.

Si votre Gateway s’exécute sur une autre machine, installez et configurez le Plugin sur cet hôte Gateway, puis redémarrez le Gateway.

## Configurer les routes

Définissez la configuration sous `plugins.entries.webhooks.config` :

json5Copy code
[code]
    {  plugins: {    entries: {      webhooks: {        enabled: true,        config: {          routes: {            zapier: {              path: "/plugins/webhooks/zapier",              sessionKey: "agent:main:main",              secret: {                source: "env",                provider: "default",                id: "OPENCLAW_WEBHOOK_SECRET",              },              controllerId: "webhooks/zapier",              description: "Zapier TaskFlow bridge",            },          },        },      },    },  },}
[/code]

Champs de route :

  * `enabled` : facultatif, vaut `true` par défaut
  * `path` : facultatif, vaut `/plugins/webhooks/<routeId>` par défaut
  * `sessionKey` : session requise qui possède les TaskFlows liés
  * `secret` : secret partagé ou SecretRef requis
  * `controllerId` : identifiant de contrôleur facultatif pour les flux gérés créés
  * `description` : note opérateur facultative


Entrées `secret` prises en charge :

  * Chaîne simple
  * SecretRef avec `source: "env" | "file" | "exec"`


Si une route adossée à un secret ne peut pas résoudre son secret au démarrage, le Plugin ignore cette route et journalise un avertissement au lieu d’exposer un endpoint défectueux.

## Modèle de sécurité

Chaque route est approuvée pour agir avec l’autorité TaskFlow de son `sessionKey` configuré.

Cela signifie que la route peut inspecter et modifier les TaskFlows appartenant à cette session ; vous devriez donc :

  * Utiliser un secret fort et unique par route
  * Préférer les références de secrets aux secrets en texte clair intégrés
  * Lier les routes à la session la plus restreinte qui convient au workflow
  * Exposer uniquement le chemin Webhook précis dont vous avez besoin


Le Plugin applique :

  * Authentification par secret partagé
  * Protections de taille et de délai d’expiration du corps de requête
  * Limitation de débit à fenêtre fixe
  * Limitation des requêtes en cours
  * Accès aux TaskFlows lié au propriétaire via `api.runtime.tasks.managedFlows.bindSession(...)`


## Format de requête

Envoyez des requêtes `POST` avec :

  * `Content-Type: application/json`
  * `Authorization: Bearer <secret>` ou `x-openclaw-webhook-secret: <secret>`


Exemple :

bashCopy code
[code]
    curl -X POST https://gateway.example.com/plugins/webhooks/zapier \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_SHARED_SECRET' \  -d '{"action":"create_flow","goal":"Review inbound queue"}'
[/code]

## Actions prises en charge

Le Plugin accepte actuellement ces valeurs JSON `action` :

  * `create_flow`
  * `get_flow`
  * `list_flows`
  * `find_latest_flow`
  * `resolve_flow`
  * `get_task_summary`
  * `set_waiting`
  * `resume_flow`
  * `finish_flow`
  * `fail_flow`
  * `request_cancel`
  * `cancel_flow`
  * `run_task`


### `create_flow`

Crée un TaskFlow géré pour la session liée de la route.

Exemple :

jsonCopy code
[code]
    {  "action": "create_flow",  "goal": "Review inbound queue",  "status": "queued",  "notifyPolicy": "done_only"}
[/code]

### `run_task`

Crée une tâche enfant gérée dans un TaskFlow géré existant.

Les runtimes autorisés sont :

  * `subagent`
  * `acp`


Exemple :

jsonCopy code
[code]
    {  "action": "run_task",  "flowId": "flow_123",  "runtime": "acp",  "childSessionKey": "agent:main:acp:worker",  "task": "Inspect the next message batch"}
[/code]

## Forme de réponse

Les réponses réussies renvoient :

jsonCopy code
[code]
    {  "ok": true,  "routeId": "zapier",  "result": {}}
[/code]

Les requêtes rejetées renvoient :

jsonCopy code
[code]
    {  "ok": false,  "routeId": "zapier",  "code": "not_found",  "error": "TaskFlow not found.",  "result": {}}
[/code]

Le Plugin supprime intentionnellement les métadonnées de propriétaire/session des réponses Webhook.

## Docs connexes

  * [SDK d’exécution du Plugin](</fr/plugins/sdk-runtime>)
  * [Vue d’ensemble des hooks et webhooks](</fr/automation/hooks>)
  * [Webhooks CLI](</fr/cli/webhooks>)


Was this useful?YesNo