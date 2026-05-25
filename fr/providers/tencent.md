---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/fr/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud est fourni comme Plugin fournisseur groupé dans OpenClaw. Il donne accès à Tencent Hy3 preview via le point de terminaison TokenHub (`tencent-tokenhub`) avec une API compatible OpenAI.

Propriété | Valeur  
---|---  
ID fournisseur | `tencent-tokenhub`  
Plugin | groupé, `enabledByDefault: true`  
Variable d’environnement d’authentification | `TOKENHUB_API_KEY`  
Indicateur d’onboarding | `--auth-choice tokenhub-api-key`  
Indicateur CLI direct | `--tokenhub-api-key <key>`  
API | compatible OpenAI (`openai-completions`)  
URL de base par défaut | `https://tokenhub.tencentmaas.com/v1`  
URL de base globale | `https://tokenhub-intl.tencentmaas.com/v1` (remplacement)  
Modèle par défaut | `tencent-tokenhub/hy3-preview`  
  
## Démarrage rapide

* ### Créer une clé API TokenHub

Créez une clé API dans Tencent Cloud TokenHub. Si vous choisissez un périmètre d’accès limité pour la clé, incluez **Hy3 preview** dans les modèles autorisés.

* ### Exécuter l’onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Indicateur directCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env uniquementCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Vérifier le modèle

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Configuration non interactive

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catalogue intégré

Réf. du modèle | Nom | Entrée | Contexte | Sortie max. | Notes  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | texte | 256,000 | 64,000 | Par défaut ; raisonnement activé  
  
Hy3 preview est le grand modèle de langage MoE de Tencent Hunyuan pour le raisonnement, le suivi d’instructions en contexte long, le code et les workflows d’agents. Les exemples compatibles OpenAI de Tencent utilisent `hy3-preview` comme ID de modèle et prennent en charge les appels d’outils standard de chat completions ainsi que `reasoning_effort`.

## Tarification par paliers

Le catalogue groupé fournit des métadonnées de coût par paliers qui s’adaptent à la longueur de la fenêtre d’entrée, afin que les estimations de coût soient renseignées sans remplacements manuels.

Plage de tokens d’entrée | Tarif d’entrée | Tarif de sortie | Lecture du cache  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Les tarifs sont indiqués par million de tokens en USD, tels qu’annoncés par Tencent. Remplacez la tarification sous `models.providers.tencent-tokenhub` uniquement lorsque vous avez besoin d’une surface différente.

## Configuration avancée

Remplacement du point de terminaison

OpenClaw utilise par défaut le point de terminaison Tencent Cloud `https://tokenhub.tencentmaas.com/v1`. Tencent documente également un point de terminaison TokenHub international :

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Remplacez le point de terminaison uniquement lorsque votre compte TokenHub ou votre région l’exige.

Disponibilité de l’environnement pour le démon

Si le Gateway s’exécute comme service géré (launchd, systemd, Docker), `TOKENHUB_API_KEY` doit être visible par ce processus. Définissez-le dans `~/.openclaw/.env` ou via `env.shellEnv` afin que les environnements launchd, systemd ou Docker exec puissent le lire.

## Associés

[**Fournisseurs de modèles** Choisir les fournisseurs, les références de modèles et le comportement de basculement. ](</fr/concepts/model-providers>) [**Référence de configuration** Schéma de configuration complet, y compris les paramètres des fournisseurs. ](</fr/gateway/configuration>) [**Tencent TokenHub** Page produit TokenHub de Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Fiche du modèle Hy3 preview** Détails et benchmarks de Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo