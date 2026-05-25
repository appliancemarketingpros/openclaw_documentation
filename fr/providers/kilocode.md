---
title: Gateway Kilo
source_url: https://docs.openclaw.ai/fr/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway fournit une **API unifiée** qui achemine les requêtes vers de nombreux modèles derrière un seul point de terminaison et une seule clé API. Elle est compatible avec OpenAI, donc la plupart des SDK OpenAI fonctionnent en changeant l’URL de base.

Propriété | Valeur  
---|---  
Fournisseur | `kilocode`  
Authentification | `KILOCODE_API_KEY`  
API | Compatible avec OpenAI  
URL de base | `https://api.kilo.ai/api/gateway/`  
  
## Premiers pas

* ### Create an account

Accédez à [app.kilo.ai](<https://app.kilo.ai>), connectez-vous ou créez un compte, puis allez dans API Keys et générez une nouvelle clé.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Ou définissez directement la variable d’environnement :

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Modèle par défaut

Le modèle par défaut est `kilocode/kilo/auto`, un modèle de routage intelligent appartenant au fournisseur et géré par Kilo Gateway.

## Catalogue intégré

OpenClaw découvre dynamiquement les modèles disponibles auprès de Kilo Gateway au démarrage. Utilisez `/models kilocode` pour voir la liste complète des modèles disponibles avec votre compte.

Tout modèle disponible sur le Gateway peut être utilisé avec le préfixe `kilocode/` :

Référence du modèle | Notes  
---|---  
`kilocode/kilo/auto` | Par défaut — routage intelligent  
`kilocode/anthropic/claude-sonnet-4` | Anthropic via Kilo  
`kilocode/openai/gpt-5.5` | OpenAI via Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google via Kilo  
...et beaucoup d’autres | Utilisez `/models kilocode` pour tout lister  
  
## Exemple de configuration

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transport and compatibility

Kilo Gateway est documenté dans la source comme compatible avec OpenRouter, il reste donc sur le chemin compatible OpenAI de style proxy plutôt que sur la mise en forme native des requêtes OpenAI.

  * Les références Kilo adossées à Gemini restent sur le chemin proxy-Gemini, donc OpenClaw conserve l’assainissement des signatures de pensée Gemini à cet endroit sans activer la validation native de relecture Gemini ni les réécritures d’amorçage.
  * Kilo Gateway utilise en interne un jeton Bearer avec votre clé API.

Stream wrapper and reasoning

Le wrapper de flux partagé de Kilo ajoute l’en-tête d’application du fournisseur et normalise les charges utiles de raisonnement du proxy pour les références de modèles concrètes prises en charge.

Troubleshooting

  * Si la découverte des modèles échoue au démarrage, OpenClaw se rabat sur le catalogue statique intégré contenant `kilocode/kilo/auto`.
  * Vérifiez que votre clé API est valide et que les modèles souhaités sont activés pour votre compte Kilo.
  * Lorsque le Gateway s’exécute comme démon, assurez-vous que `KILOCODE_API_KEY` est disponible pour ce processus (par exemple dans `~/.openclaw/.env` ou via `env.shellEnv`).


## Connexe

[**Model selection** Choisir les fournisseurs, les références de modèles et le comportement de basculement. ](</fr/concepts/model-providers>) [**Configuration reference** Référence complète de la configuration OpenClaw. ](</fr/gateway/configuration-reference>) [**Kilo Gateway** Tableau de bord Kilo Gateway, clés API et gestion du compte. ](<https://app.kilo.ai>)

Was this useful?YesNo