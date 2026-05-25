---
title: Hugging Face (inférence)
source_url: https://docs.openclaw.ai/fr/providers/huggingface
scraped_at: 2026-05-25
---

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) proposent des chat completions compatibles OpenAI via une API routeur unique. Vous accédez à de nombreux modèles (DeepSeek, Llama, et d’autres) avec un seul jeton. OpenClaw utilise l’**endpoint compatible OpenAI** (chat completions uniquement) ; pour le texte-vers-image, les embeddings ou la parole, utilisez directement les [clients d’inférence HF](<https://huggingface.co/docs/api-inference/quicktour>).

  * Fournisseur : `huggingface`
  * Authentification : `HUGGINGFACE_HUB_TOKEN` ou `HF_TOKEN` (jeton à granularité fine avec **Make calls to Inference Providers**)
  * API : compatible OpenAI (`https://router.huggingface.co/v1`)
  * Facturation : jeton HF unique ; la [tarification](<https://huggingface.co/docs/inference-providers/pricing>) suit les tarifs des fournisseurs avec un niveau gratuit.


## Premiers pas

* ### Créer un jeton à granularité fine

Allez sur [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) et créez un nouveau jeton à granularité fine.

* ### Lancer l’onboarding

Choisissez **Hugging Face** dans la liste déroulante des fournisseurs, puis saisissez votre clé API lorsque cela vous est demandé :

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### Sélectionner un modèle par défaut

Dans la liste déroulante **Default Hugging Face model** , choisissez le modèle que vous voulez. La liste est chargée depuis l’API Inference lorsque vous avez un jeton valide ; sinon une liste intégrée est affichée. Votre choix est enregistré comme modèle par défaut.

Vous pouvez aussi définir ou modifier le modèle par défaut plus tard dans la configuration :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Configuration non interactive

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

Cela définira `huggingface/deepseek-ai/DeepSeek-R1` comme modèle par défaut.

## IDs de modèles

Les références de modèles utilisent la forme `huggingface/<org>/<model>` (identifiants de style Hub). La liste ci-dessous provient de **GET** `https://router.huggingface.co/v1/models` ; votre catalogue peut en inclure davantage.

Modèle | Référence (préfixer avec `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## Configuration avancée

Découverte des modèles et liste déroulante d’onboarding

OpenClaw découvre les modèles en appelant **directement l’endpoint Inference** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(Facultatif : envoyez `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` ou `$HF_TOKEN` pour la liste complète ; certains endpoints renvoient un sous-ensemble sans authentification.) La réponse est de style OpenAI `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

Lorsque vous configurez une clé API Hugging Face (via l’onboarding, `HUGGINGFACE_HUB_TOKEN`, ou `HF_TOKEN`), OpenClaw utilise ce GET pour découvrir les modèles de chat completion disponibles. Pendant le **setup interactif** , après avoir saisi votre jeton, vous voyez une liste déroulante **Default Hugging Face model** alimentée à partir de cette liste (ou du catalogue intégré si la requête échoue). Au runtime (par ex. au démarrage du Gateway), lorsqu’une clé est présente, OpenClaw appelle à nouveau **GET** `https://router.huggingface.co/v1/models` pour rafraîchir le catalogue. La liste est fusionnée avec un catalogue intégré (pour des métadonnées comme la fenêtre de contexte et le coût). Si la requête échoue ou qu’aucune clé n’est définie, seul le catalogue intégré est utilisé.

Noms de modèles, alias, et suffixes de politique

  * **Nom depuis l’API :** le nom d’affichage du modèle est **hydraté depuis GET /v1/models** lorsque l’API renvoie `name`, `title`, ou `display_name` ; sinon il est dérivé de l’identifiant du modèle (par ex. `deepseek-ai/DeepSeek-R1` devient « DeepSeek R1 »).
  * **Surcharger le nom d’affichage :** vous pouvez définir un libellé personnalisé par modèle dans la configuration pour qu’il apparaisse comme vous le souhaitez dans la CLI et l’interface :

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **Suffixes de politique :** la documentation et les helpers Hugging Face inclus d’OpenClaw traitent actuellement ces deux suffixes comme variantes de politique intégrées :

    * **`:fastest`** — débit le plus élevé.
    * **`:cheapest`** — coût le plus faible par jeton de sortie.

Vous pouvez les ajouter comme entrées séparées dans `models.providers.huggingface.models` ou définir `model.primary` avec le suffixe. Vous pouvez aussi définir votre ordre de fournisseur par défaut dans les [paramètres Inference Provider](<https://hf.co/settings/inference-providers>) (pas de suffixe = utiliser cet ordre).

  * **Fusion de configuration :** les entrées existantes dans `models.providers.huggingface.models` (par ex. dans `models.json`) sont conservées lors de la fusion de la configuration. Ainsi, tout `name`, `alias`, ou option de modèle personnalisé que vous y définissez est préservé.


Environnement et configuration du daemon

Si le Gateway s’exécute comme daemon (launchd/systemd), assurez-vous que `HUGGINGFACE_HUB_TOKEN` ou `HF_TOKEN` est disponible pour ce processus (par exemple, dans `~/.openclaw/.env` ou via `env.shellEnv`).

Configuration : DeepSeek R1 avec repli Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Configuration : Qwen avec variantes cheapest et fastest json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Configuration : DeepSeek + Llama + GPT-OSS avec alias json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Configuration : plusieurs Qwen et DeepSeek avec suffixes de politique json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## Articles connexes

[**Sélection des modèles** Vue d’ensemble de tous les fournisseurs, références de modèles et comportement de bascule. ](</fr/concepts/model-providers>) [**Sélection des modèles** Comment choisir et configurer les modèles. ](</fr/concepts/models>) [**Documentation Inference Providers** Documentation officielle Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**Configuration** Référence complète de configuration. ](</fr/gateway/configuration>)

Was this useful?YesNo