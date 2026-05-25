---
title: Synthetic
source_url: https://docs.openclaw.ai/fr/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) expose des endpoints compatibles Anthropic. OpenClaw l’enregistre comme fournisseur `synthetic` et utilise l’API Anthropic Messages.

Propriété | Valeur  
---|---  
Fournisseur | `synthetic`  
Authentification | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
URL de base | `https://api.synthetic.new/anthropic`  
  
## Premiers pas

* ### Obtenir une clé API

Obtenez une `SYNTHETIC_API_KEY` depuis votre compte Synthetic, ou laissez l’assistant d’onboarding vous en demander une.

* ### Lancer l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Vérifier le modèle par défaut

Après l’onboarding, le modèle par défaut est défini sur :

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Exemple de configuration

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Catalogue intégré

Tous les modèles Synthetic utilisent un coût `0` (entrée/sortie/cache).

ID du modèle | Fenêtre de contexte | Max tokens | Raisonnement | Entrée  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192 000 | 65 536 | non | texte  
`hf:moonshotai/Kimi-K2-Thinking` | 256 000 | 8 192 | oui | texte  
`hf:zai-org/GLM-4.7` | 198 000 | 128 000 | non | texte  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128 000 | 8 192 | non | texte  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128 000 | 8 192 | non | texte  
`hf:deepseek-ai/DeepSeek-V3.1` | 128 000 | 8 192 | non | texte  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128 000 | 8 192 | non | texte  
`hf:deepseek-ai/DeepSeek-V3.2` | 159 000 | 8 192 | non | texte  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128 000 | 8 192 | non | texte  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524 000 | 8 192 | non | texte  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256 000 | 8 192 | non | texte  
`hf:moonshotai/Kimi-K2.5` | 256 000 | 8 192 | oui | texte + image  
`hf:openai/gpt-oss-120b` | 128 000 | 8 192 | non | texte  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256 000 | 8 192 | non | texte  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256 000 | 8 192 | non | texte  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250 000 | 8 192 | non | texte + image  
`hf:zai-org/GLM-4.5` | 128 000 | 128 000 | non | texte  
`hf:zai-org/GLM-4.6` | 198 000 | 128 000 | non | texte  
`hf:zai-org/GLM-5` | 256 000 | 128 000 | oui | texte + image  
`hf:deepseek-ai/DeepSeek-V3` | 128 000 | 8 192 | non | texte  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256 000 | 8 192 | oui | texte  
  
Liste d’autorisation de modèles

Si vous activez une liste d’autorisation de modèles (`agents.defaults.models`), ajoutez tous les modèles Synthetic que vous prévoyez d’utiliser. Les modèles absents de la liste d’autorisation seront cachés à l’agent.

Surcharge d’URL de base

Si Synthetic change son endpoint API, surchargez l’URL de base dans votre configuration :

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

N’oubliez pas qu’OpenClaw ajoute automatiquement `/v1`.

## Articles connexes

[**Sélection des modèles** Règles des fournisseurs, références de modèles et comportement de bascule. ](</fr/concepts/model-providers>) [**Référence de configuration** Schéma de configuration complet incluant les paramètres des fournisseurs. ](</fr/gateway/configuration-reference>) [**Synthetic** Tableau de bord Synthetic et documentation de l’API. ](<https://synthetic.new>)

Was this useful?YesNo