---
title: Gateway d’IA Cloudflare
source_url: https://docs.openclaw.ai/fr/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway se place devant les API des fournisseurs et vous permet d’ajouter des analytics, de la mise en cache et des contrôles. Pour Anthropic, OpenClaw utilise l’API Messages d’Anthropic via votre point de terminaison Gateway.

Propriété | Valeur  
---|---  
Fournisseur | `cloudflare-ai-gateway`  
URL de base | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Modèle par défaut | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Clé d’API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (votre clé d’API fournisseur pour les requêtes via le Gateway)  
  
Lorsque le mode de réflexion est activé pour les modèles Anthropic Messages, OpenClaw supprime les tours de préremplissage finaux de l’assistant avant d’envoyer la charge utile via Cloudflare AI Gateway. Anthropic rejette le préremplissage des réponses avec la réflexion étendue, tandis que le préremplissage ordinaire sans réflexion reste disponible.

## Bien démarrer

* ### Définir la clé d’API fournisseur et les détails du Gateway

Lancez l’onboarding et choisissez l’option d’authentification Cloudflare AI Gateway :

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Cela vous demande votre ID de compte, votre ID de Gateway et votre clé d’API.

* ### Définir un modèle par défaut

Ajoutez le modèle à votre configuration OpenClaw :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Exemple non interactif

Pour les configurations scriptées ou CI, passez toutes les valeurs sur la ligne de commande :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Configuration avancée

Gateways authentifiés

Si vous avez activé l’authentification Gateway dans Cloudflare, ajoutez l’en-tête `cf-aig-authorization`. Cela s’ajoute à votre clé d’API fournisseur.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Note sur l’environnement

Si le Gateway s’exécute comme daemon (launchd/systemd), assurez-vous que `CLOUDFLARE_AI_GATEWAY_API_KEY` est disponible pour ce processus.

## Liens connexes

[**Sélection du modèle** Choisir les fournisseurs, les références de modèles et le comportement de basculement. ](</fr/concepts/model-providers>) [**Dépannage** Dépannage général et FAQ. ](</fr/help/troubleshooting>)

Was this useful?YesNo