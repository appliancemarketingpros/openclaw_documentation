---
title: ds4
source_url: https://docs.openclaw.ai/fr/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) sert DeepSeek V4 Flash depuis un backend local Metal avec une API `/v1` compatible avec OpenAI. OpenClaw se connecte à ds4 via la famille de fournisseurs générique `openai-completions`.

ds4 n’est pas un Plugin de fournisseur OpenClaw intégré. Configurez-le sous `models.providers.ds4`, puis sélectionnez `ds4/deepseek-v4-flash`.

  * Identifiant du fournisseur : `ds4`
  * Plugin : aucun
  * API : Chat Completions compatible avec OpenAI (`openai-completions`)
  * URL de base suggérée : `http://127.0.0.1:18000/v1`
  * Identifiant du modèle : `deepseek-v4-flash`
  * Appels d’outils : pris en charge via `tools` et `tool_calls` au style OpenAI
  * Raisonnement : `thinking` et `reasoning_effort` au style DeepSeek


## Prérequis

  * macOS avec prise en charge de Metal.
  * Un checkout ds4 fonctionnel avec `ds4-server` et le fichier GGUF DeepSeek V4 Flash.
  * Suffisamment de mémoire pour le contexte que vous choisissez. Les valeurs `--ctx` plus élevées allouent davantage de mémoire KV au démarrage du serveur.


## Démarrage rapide

* ### Démarrer ds4-server

Remplacez `&lt;DS4_DIR&gt;` par le chemin de votre checkout ds4.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Vérifier le point de terminaison compatible avec OpenAI

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

La réponse doit inclure `deepseek-v4-flash`.

* ### Ajouter la configuration du fournisseur OpenClaw

Ajoutez la configuration depuis Configuration complète, puis exécutez une vérification ponctuelle du modèle :

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Configuration complète

Utilisez cette configuration quand ds4 est déjà exécuté sur `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Gardez `contextWindow` aligné sur la valeur `ds4-server --ctx`. Gardez `maxTokens` aligné sur `--tokens`, sauf si vous voulez intentionnellement qu’OpenClaw demande une sortie plus courte que la valeur par défaut du serveur.

## Démarrage à la demande

OpenClaw peut démarrer ds4 uniquement quand un modèle `ds4/...` est sélectionné. Ajoutez `localService` à la même entrée de fournisseur :

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` doit être un chemin absolu vers un exécutable. La recherche par le shell et l’expansion de `~` ne sont pas utilisées. Consultez [Services de modèles locaux](</fr/gateway/local-model-services>) pour chaque champ `localService`.

## Think Max

ds4 applique Think Max seulement lorsque les deux conditions sont vraies :

  * `ds4-server` démarre avec `--ctx 393216` ou plus.
  * La requête utilise `reasoning_effort: "max"` ou le champ d’effort ds4 équivalent.


Si vous exécutez ce grand contexte, mettez à jour à la fois les indicateurs du serveur et les métadonnées du modèle OpenClaw :

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Test

Commencez par une vérification HTTP directe :

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Testez ensuite le routage de modèle OpenClaw :

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Pour un test de fumée complet d’agent et d’appel d’outil, utilisez un contexte d’au moins 32768 :

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Résultat attendu :

  * `executionTrace.winnerProvider` vaut `ds4`
  * `executionTrace.winnerModel` vaut `deepseek-v4-flash`
  * `toolSummary.calls` vaut au moins `1`
  * `finalAssistantVisibleText` commence par `tool-ok`


## Dépannage

curl /v1/models ne peut pas se connecter

ds4 n’est pas exécuté ou n’est pas lié à l’hôte et au port dans `baseUrl`. Démarrez `ds4-server`, puis réessayez :

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

La valeur `--ctx` configurée est trop petite pour le tour OpenClaw. Augmentez `ds4-server --ctx`, puis mettez à jour `models.providers.ds4.models[].contextWindow` pour qu’elle corresponde. Les tours complets d’agent avec outils nécessitent beaucoup plus de contexte qu’une requête curl directe à un seul message.

Think Max ne s’active pas

ds4 n’utilise Think Max que lorsque `--ctx` vaut au moins `393216` et que la requête demande `reasoning_effort: "max"`. Les contextes plus petits reviennent au raisonnement élevé.

La première requête est lente

ds4 a une phase de résidence Metal à froid et de préchauffage du modèle. Utilisez `localService.readyTimeoutMs: 300000` quand OpenClaw démarre le serveur à la demande.

## Connexe

[**Services de modèles locaux** Démarrez des serveurs de modèles locaux à la demande avant les requêtes de modèle. ](</fr/gateway/local-model-services>) [**Modèles locaux** Choisissez et exploitez des backends de modèles locaux. ](</fr/gateway/local-models>) [**Fournisseurs de modèles** Configurez les références de fournisseur, l’authentification et le basculement. ](</fr/concepts/model-providers>) [**DeepSeek** Comportement natif du fournisseur DeepSeek et contrôles de réflexion. ](</fr/providers/deepseek>)

Was this useful?YesNo

Open issue