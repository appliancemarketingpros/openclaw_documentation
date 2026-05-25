---
title: Feux d’artifice
source_url: https://docs.openclaw.ai/fr/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) expose des modèles à pondérations ouvertes et routés via une API compatible OpenAI. OpenClaw inclut un Plugin de fournisseur Fireworks groupé, livré avec deux modèles Kimi pré-catalogués, et accepte n’importe quel modèle Fireworks ou id de routeur Fireworks à l’exécution.

Propriété | Valeur  
---|---  
Id du fournisseur | `fireworks` (alias : `fireworks-ai`)  
Plugin | groupé, `enabledByDefault: true`  
Variable d’env. auth | `FIREWORKS_API_KEY`  
Option d’intégration | `--auth-choice fireworks-api-key`  
Option CLI directe | `--fireworks-api-key <key>`  
API | compatible OpenAI (`openai-completions`)  
URL de base | `https://api.fireworks.ai/inference/v1`  
Modèle par défaut | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Alias par défaut | `Kimi K2.5 Turbo`  
  
## Bien démarrer

* ### Définir la clé API Fireworks

IntégrationCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Option directeCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env uniquementCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

L’intégration stocke la clé pour le fournisseur `fireworks` dans vos profils d’authentification et définit le routeur **Fire Pass** Kimi K2.5 Turbo comme modèle par défaut.

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

La liste doit inclure `Kimi K2.6` et `Kimi K2.5 Turbo (Fire Pass)`. Si `FIREWORKS_API_KEY` n’est pas résolu, `openclaw models status --json` signale l’identifiant manquant sous `auth.unusableProfiles`.

## Configuration non interactive

Pour les installations scriptées ou CI, passez tout sur la ligne de commande :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catalogue intégré

Réf. du modèle | Nom | Entrée | Contexte | Sortie max | Réflexion  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | texte + image | 262,144 | 262,144 | Désactivée de force  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | texte + image | 256,000 | 256,000 | Désactivée de force (défaut)  
  
## Ids de modèles Fireworks personnalisés

OpenClaw accepte n’importe quel modèle Fireworks ou id de routeur Fireworks à l’exécution. Utilisez l’id exact affiché par Fireworks et préfixez-le avec `fireworks/`. La résolution dynamique clone le modèle Fire Pass (entrée texte + image, API compatible OpenAI, coût par défaut nul) et désactive automatiquement la réflexion lorsque l’id correspond au motif Kimi.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

Fonctionnement du préfixage des ids de modèles

Chaque référence de modèle Fireworks dans OpenClaw commence par `fireworks/`, suivi de l’id exact ou du chemin de routeur issu de la plateforme Fireworks. Par exemple :

  * Modèle de routeur : `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Modèle direct : `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw supprime le préfixe `fireworks/` lors de la construction de la requête API et envoie le chemin restant au point de terminaison Fireworks comme champ `model` compatible OpenAI.

Pourquoi la réflexion est désactivée de force pour Kimi

Fireworks K2.6 renvoie une erreur 400 si la requête contient des paramètres `reasoning_*`, même si Kimi prend en charge la réflexion via l’API propre à Moonshot. La stratégie groupée (`extensions/fireworks/thinking-policy.ts`) annonce uniquement le niveau de réflexion `off` pour les ids de modèles Kimi, afin que les bascules manuelles `/think` et les surfaces de stratégie fournisseur restent alignées avec le contrat d’exécution.

Pour utiliser le raisonnement Kimi de bout en bout, configurez le [fournisseur Moonshot](</fr/providers/moonshot>) et routez le même modèle via celui-ci.

Disponibilité de l’environnement pour le démon

Si le Gateway s’exécute comme service géré (launchd, systemd, Docker), la clé Fireworks doit être visible par ce processus, et pas seulement par votre shell interactif.

Sur macOS, `openclaw gateway install` connecte déjà `~/.openclaw/.env` au fichier d’environnement LaunchAgent. Réexécutez l’installation (ou `openclaw doctor --fix`) après la rotation de la clé.

## Liens connexes

[**Fournisseurs de modèles** Choisir les fournisseurs, les références de modèles et le comportement de bascule. ](</fr/concepts/model-providers>) [**Modes de réflexion** Niveaux `/think`, stratégies fournisseur et routage de modèles capables de raisonnement. ](</fr/tools/thinking>) [**Moonshot** Exécuter Kimi avec une sortie de réflexion native via l’API propre à Moonshot. ](</fr/providers/moonshot>) [**Dépannage** Dépannage général et FAQ. ](</fr/help/troubleshooting>)

Was this useful?YesNo