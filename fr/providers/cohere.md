---
title: Cohere
source_url: https://docs.openclaw.ai/fr/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) fournit une inférence compatible avec OpenAI via son API Compatibility. OpenClaw embarque le fournisseur Cohere pendant sa transition d’externalisation et le publie également comme Plugin externe officiel avec le catalogue de modèles Command A.

Propriété | Valeur  
---|---  
ID du fournisseur | `cohere`  
Plugin | embarqué pendant la transition ; paquet externe officiel  
Variable d’env d’auth | `COHERE_API_KEY`  
Option d’onboarding | `--auth-choice cohere-api-key`  
Option CLI directe | `--cohere-api-key <key>`  
API | compatible avec OpenAI (`openai-completions`)  
URL de base | `https://api.cohere.ai/compatibility/v1`  
Modèle par défaut | `cohere/command-a-03-2025`  
  
## Démarrer

  1. Cohere est inclus dans les paquets OpenClaw actuels. S’il n’est pas disponible, installez le paquet externe et redémarrez le Gateway :

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Créez une clé API Cohere.
  3. Exécutez l’onboarding :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Confirmez que le catalogue est disponible :

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Le modèle par défaut n’est défini que lorsqu’aucun modèle principal n’est déjà configuré.

## Configuration uniquement par environnement

Rendez `COHERE_API_KEY` disponible pour le processus Gateway, puis sélectionnez le modèle Cohere :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Voir aussi

  * [Fournisseurs de modèles](</fr/concepts/model-providers>)
  * [CLI des modèles](</fr/cli/models>)
  * [Répertoire des fournisseurs](</fr/providers>)


Was this useful?YesNo

Open issue