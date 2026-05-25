---
title: Moonshot AI
source_url: https://docs.openclaw.ai/fr/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot fournit l’API Kimi avec des endpoints compatibles OpenAI. Configurez le provider et définissez le modèle par défaut sur `moonshot/kimi-k2.6`, ou utilisez Kimi Coding avec `kimi/kimi-for-coding`.

## Catalogue de modèles intégré

Ref de modèle | Nom | Raisonnement | Entrée | Contexte | Sortie max  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | Non | texte, image | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | Non | texte, image | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Oui | texte | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Oui | texte | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | Non | texte | 256,000 | 16,384  
  
Les estimations de coût intégrées pour les modèles K2 actuels hébergés par Moonshot utilisent les tarifs à l’usage publiés par Moonshot : Kimi K2.6 coûte 0,16 $/MTok en cache hit, 0,95 $/MTok en entrée et 4,00 $/MTok en sortie ; Kimi K2.5 coûte 0,10 $/MTok en cache hit, 0,60 $/MTok en entrée et 3,00 $/MTok en sortie. Les autres entrées héritées du catalogue conservent des espaces réservés à coût nul, sauf si vous les remplacez dans la config.

## Premiers pas

Choisissez votre provider et suivez les étapes de configuration.

### API Moonshot

**Idéal pour :** les modèles Kimi K2 via la Moonshot Open Platform.

* ### Choisir la région de votre endpoint

Choix d’authentification | Endpoint | Région  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | International  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | Chine  
* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

Ou pour l’endpoint Chine :

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Exécuter un smoke test en direct

Utilisez un répertoire d’état isolé lorsque vous voulez vérifier l’accès au modèle et le suivi des coûts sans toucher à vos sessions habituelles :

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

La réponse JSON doit indiquer `provider: "moonshot"` et `model: "kimi-k2.6"`. L’entrée de transcription de l’assistant stocke l’utilisation normalisée des tokens ainsi que le coût estimé sous `usage.cost` lorsque Moonshot renvoie les métadonnées d’utilisation.

### Exemple de config

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**Idéal pour :** les tâches centrées sur le code via l’endpoint Kimi Coding.

* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Exemple de config

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Recherche web Kimi

OpenClaw fournit également **Kimi** comme provider `web_search`, adossé à la recherche web Moonshot.

* ### Exécuter la configuration interactive de la recherche web

bashCopy code
[code]
    openclaw configure --section web
[/code]

Choisissez **Kimi** dans la section de recherche web pour stocker `plugins.entries.moonshot.config.webSearch.*`.

* ### Configurer la région et le modèle de recherche web

La configuration interactive demande :

Paramètre | Options  
---|---  
Région de l’API | `https://api.moonshot.ai/v1` (international) ou `https://api.moonshot.cn/v1` (Chine)  
Modèle de recherche web | Par défaut `kimi-k2.6`  
  
La config se trouve sous `plugins.entries.moonshot.config.webSearch` :

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Configuration avancée

Mode de réflexion natif

Moonshot Kimi prend en charge la réflexion native binaire :

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Configurez-la par modèle via `agents.defaults.models.<provider/model>.params` :

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw mappe également les niveaux `/think` d’exécution pour Moonshot :

Niveau `/think` | Comportement Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
Tout niveau autre que off | `thinking.type=enabled`  
  
Kimi K2.6 accepte également un champ facultatif `thinking.keep` qui contrôle la conservation multi-tour de `reasoning_content`. Définissez-le sur `"all"` pour conserver le raisonnement complet entre les tours ; omettez-le (ou laissez-le à `null`) pour utiliser la stratégie par défaut du serveur. OpenClaw ne transmet `thinking.keep` que pour `moonshot/kimi-k2.6` et le retire des autres modèles.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Assainissement des ids d’appel d’outil

Moonshot Kimi fournit des ids tool_call sous la forme `functions.<name>:<index>`. OpenClaw les conserve inchangés afin que les appels d’outils multi-tours continuent de fonctionner.

Pour forcer un assainissement strict sur un provider personnalisé compatible OpenAI, définissez `sanitizeToolCallIds: true` :

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Compatibilité d’utilisation en streaming

Les endpoints Moonshot natifs (`https://api.moonshot.ai/v1` et `https://api.moonshot.cn/v1`) annoncent la compatibilité de l’utilisation en streaming sur le transport partagé `openai-completions`. OpenClaw la détermine à partir des capacités des endpoints, afin que les ids de provider personnalisés compatibles ciblant les mêmes hôtes Moonshot natifs héritent du même comportement d’utilisation en streaming.

Avec la tarification K2.6 intégrée, l’utilisation streamée qui inclut les tokens d’entrée, de sortie et de lecture du cache est également convertie en coût local estimé en USD pour `/status`, `/usage full`, `/usage cost` et la comptabilité des sessions basée sur les transcriptions.

Référence des points de terminaison et des références de modèle Fournisseur | Préfixe de référence de modèle | Point de terminaison | Variable d’env d’auth  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Point de terminaison Kimi Coding | `KIMI_API_KEY`  
Recherche Web | N/A | Identique à la région de l’API Moonshot | `KIMI_API_KEY` ou `MOONSHOT_API_KEY`  
  
  * La recherche Web Kimi utilise `KIMI_API_KEY` ou `MOONSHOT_API_KEY`, et utilise par défaut `https://api.moonshot.ai/v1` avec le modèle `kimi-k2.6`.
  * Remplacez les métadonnées de tarification et de contexte dans `models.providers` si nécessaire.
  * Si Moonshot publie des limites de contexte différentes pour un modèle, ajustez `contextWindow` en conséquence.


## Connexe

[**Sélection du modèle** Choisir les fournisseurs, les références de modèle et le comportement de basculement. ](</fr/concepts/model-providers>) [**Recherche Web** Configurer les fournisseurs de recherche Web, y compris Kimi. ](</fr/tools/web>) [**Référence de configuration** Schéma de configuration complet pour les fournisseurs, les modèles et les plugins. ](</fr/gateway/configuration-reference>) [**Moonshot Open Platform** Gestion des clés d’API Moonshot et documentation. ](<https://platform.moonshot.ai>)

Was this useful?YesNo