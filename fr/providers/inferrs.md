---
title: Infère
source_url: https://docs.openclaw.ai/fr/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) peut servir des modèles locaux derrière une API `/v1` compatible OpenAI. OpenClaw fonctionne avec `inferrs` via le chemin générique `openai-completions`.

Propriété | Valeur  
---|---  
ID du fournisseur | `inferrs` (personnalisé ; configurer sous `models.providers.inferrs`)  
Plugin | aucun — `inferrs` n’est pas un Plugin de fournisseur OpenClaw intégré  
Variable d’environnement d’authentification | Facultative. N’importe quelle valeur fonctionne si votre serveur inferrs n’a pas d’authentification  
API | compatible OpenAI (`openai-completions`)  
URL de base suggérée | `http://127.0.0.1:8080/v1` (ou là où se trouve votre serveur inferrs)  
  
## Premiers pas

* ### Démarrer inferrs avec un modèle

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Vérifier que le serveur est accessible

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Ajouter une entrée de fournisseur OpenClaw

Ajoutez une entrée de fournisseur explicite et pointez votre modèle par défaut vers celle-ci. Consultez l’exemple de configuration complet ci-dessous.

## Exemple de configuration complet

Cet exemple utilise Gemma 4 sur un serveur `inferrs` local.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Démarrage à la demande

Inferrs peut aussi être démarré par OpenClaw uniquement lorsqu’un modèle `inferrs/...` est sélectionné. Ajoutez `localService` à la même entrée de fournisseur :

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` doit être absolu. Utilisez `which inferrs` sur l’hôte Gateway et placez ce chemin dans la configuration. Pour la référence complète des champs, consultez [Services de modèles locaux](</fr/gateway/local-model-services>).

## Configuration avancée

Pourquoi requiresStringContent est important

Certaines routes Chat Completions de `inferrs` acceptent uniquement des chaînes `messages[].content`, et non des tableaux structurés de parties de contenu.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw aplatira les parties de contenu en texte pur en chaînes simples avant d’envoyer la requête.

Gemma et mise en garde sur le schéma d’outils

Certaines combinaisons actuelles `inferrs` \+ Gemma acceptent les petites requêtes directes `/v1/chat/completions`, mais échouent toujours lors des tours complets du runtime d’agent OpenClaw.

Si cela se produit, essayez d’abord ceci :

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Cela désactive la surface de schéma d’outils d’OpenClaw pour le modèle et peut réduire la pression de prompt sur les backends locaux plus stricts.

Si de très petites requêtes directes fonctionnent toujours mais que les tours d’agent OpenClaw normaux continuent de planter dans `inferrs`, le problème restant se situe généralement dans le comportement du modèle/serveur en amont plutôt que dans la couche de transport d’OpenClaw.

Test de fumée manuel

Une fois configuré, testez les deux couches :

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Si la première commande fonctionne mais que la seconde échoue, consultez la section de dépannage ci-dessous.

Comportement de type proxy

`inferrs` est traité comme un backend `/v1` compatible OpenAI de type proxy, et non comme un point de terminaison OpenAI natif.

  * La mise en forme des requêtes propre aux points de terminaison OpenAI natifs ne s’applique pas ici
  * Pas de `service_tier`, pas de Responses `store`, pas d’indications de cache de prompt, et pas de mise en forme de payload de compatibilité de raisonnement OpenAI
  * Les en-têtes d’attribution OpenClaw masqués (`originator`, `version`, `User-Agent`) ne sont pas injectés sur les URL de base `inferrs` personnalisées


## Dépannage

curl /v1/models échoue

`inferrs` n’est pas en cours d’exécution, n’est pas accessible, ou n’est pas lié à l’hôte/au port attendus. Assurez-vous que le serveur est démarré et écoute à l’adresse que vous avez configurée.

messages[].content attendait une chaîne

Définissez `compat.requiresStringContent: true` dans l’entrée de modèle. Consultez la section `requiresStringContent` ci-dessus pour plus de détails.

Les appels directs /v1/chat/completions réussissent, mais openclaw infer model run échoue

Essayez de définir `compat.supportsTools: false` pour désactiver la surface de schéma d’outils. Consultez la mise en garde sur le schéma d’outils de Gemma ci-dessus.

inferrs plante toujours sur les tours d’agent plus volumineux

Si OpenClaw n’obtient plus d’erreurs de schéma mais que `inferrs` plante toujours sur des tours d’agent plus volumineux, traitez cela comme une limitation en amont de `inferrs` ou du modèle. Réduisez la pression de prompt ou passez à un autre backend local ou modèle.

## Associés

[**Modèles locaux** Exécuter OpenClaw avec des serveurs de modèles locaux. ](</fr/gateway/local-models>) [**Services de modèles locaux** Démarrer des serveurs de modèles locaux à la demande pour les fournisseurs configurés. ](</fr/gateway/local-model-services>) [**Dépannage Gateway** Déboguer des backends locaux compatibles OpenAI qui réussissent les sondes mais échouent lors des exécutions d’agent. ](</fr/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Sélection du modèle** Vue d’ensemble de tous les fournisseurs, références de modèles et comportement de basculement. ](</fr/concepts/model-providers>)

Was this useful?YesNo