---
title: Gateway IA de Vercel
source_url: https://docs.openclaw.ai/fr/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

Le [Vercel AI Gateway](<https://vercel.com/ai-gateway>) fournit une API unifiée pour accéder à des centaines de modèles via un seul point de terminaison.

Propriété | Valeur  
---|---  
Fournisseur | `vercel-ai-gateway`  
Authentification | `AI_GATEWAY_API_KEY`  
API | Compatible avec Anthropic Messages  
Catalogue de modèles | Découvert automatiquement via `/v1/models`  
  
## Premiers pas

* ### Définir la clé API

Exécutez l’intégration initiale et choisissez l’option d’authentification AI Gateway :

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Définir un modèle par défaut

Ajoutez le modèle à votre configuration OpenClaw :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Exemple non interactif

Pour les configurations scriptées ou CI, transmettez toutes les valeurs en ligne de commande :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Raccourci d’ID de modèle

OpenClaw accepte les références abrégées de modèles Claude de Vercel et les normalise à l’exécution :

Entrée abrégée | Référence de modèle normalisée  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Configuration avancée

Variable d’environnement pour les processus daemon

Si l’OpenClaw Gateway s’exécute comme un daemon (launchd/systemd), assurez-vous que `AI_GATEWAY_API_KEY` est disponible pour ce processus.

Routage du fournisseur

Vercel AI Gateway achemine les requêtes vers le fournisseur en amont en fonction du préfixe de référence de modèle. Par exemple, `vercel-ai-gateway/anthropic/claude-opus-4.6` est acheminé via Anthropic, tandis que `vercel-ai-gateway/openai/gpt-5.5` est acheminé via OpenAI et `vercel-ai-gateway/moonshotai/kimi-k2.6` via MoonshotAI. Votre unique `AI_GATEWAY_API_KEY` gère l’authentification pour tous les fournisseurs en amont.

Niveaux de réflexion

Les options `/think` suivent les préfixes de modèles en amont fiables quand OpenClaw connaît le contrat du fournisseur en amont. `vercel-ai-gateway/anthropic/...` utilise le profil de réflexion Claude, y compris les valeurs adaptatives par défaut pour les modèles Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` et les références de style Codex exposent `/think xhigh`, comme les fournisseurs directs OpenAI/OpenAI Codex. Les autres références avec espace de noms conservent les niveaux de raisonnement normaux, sauf si les métadonnées de leur catalogue en déclarent davantage.

## Articles connexes

[**Sélection de modèles** Choix des fournisseurs, des références de modèles et du comportement de basculement. ](</fr/concepts/model-providers>) [**Dépannage** Dépannage général et FAQ. ](</fr/help/troubleshooting>)

Was this useful?YesNo