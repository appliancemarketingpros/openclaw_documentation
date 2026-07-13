---
title: LongCat
source_url: https://docs.openclaw.ai/fr/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) fournit une API hébergée pour LongCat-2.0, un modèle de raisonnement conçu pour le codage et les charges de travail agentiques. OpenClaw fournit le plugin `longcat` officiel pour le point de terminaison compatible avec OpenAI de LongCat.

Propriété | Valeur  
---|---  
Fournisseur | `longcat`  
Authentification | `LONGCAT_API_KEY`  
API | Chat Completions compatible avec OpenAI  
URL de base | `https://api.longcat.chat/openai`  
Modèle | `longcat/LongCat-2.0`  
Contexte | 1 048 576 jetons  
Sortie maximale | 131 072 jetons  
Entrée | Texte  
  
## Installer le plugin

Installez le paquet officiel, puis redémarrez le Gateway :

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Prise en main

* ### Créer une clé API

Connectez-vous à la [plateforme API LongCat](<https://longcat.chat/platform/>) et créez une clé sur la page [API Keys](<https://longcat.chat/platform/api_keys>).

* ### Exécuter la configuration initiale

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Vérifier le modèle

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

La configuration initiale ajoute le catalogue hébergé et sélectionne `longcat/LongCat-2.0` si aucun modèle principal n'est déjà configuré.

### Configuration non interactive

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Comportement du raisonnement

LongCat propose un contrôle binaire de la réflexion. OpenClaw associe les niveaux de réflexion activés à `thinking: { type: "enabled" }` et `/think off` à `thinking: { type: "disabled" }`. LongCat ne documente actuellement pas `reasoning_effort`, donc OpenClaw ne l'envoie pas.

LongCat renvoie le raisonnement dans `reasoning_content`. OpenClaw conserve ce champ lors de la relecture des tours d'appel d'outil de l'assistant, afin que les sessions agentiques multi-tours conservent la structure de message attendue par le fournisseur.

## Tarification

Le catalogue intégré utilise les tarifs à l'usage de LongCat, en USD par million de jetons : 0,75 $ pour les entrées non mises en cache, 0,015 $ pour les entrées mises en cache et 2,95 $ pour les sorties. LongCat peut proposer des remises temporaires ; la [page de tarification](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) et vos relevés de facturation font foi.

## LongCat-2.0 auto-hébergé

Le fournisseur `longcat` cible l'API hébergée de LongCat. Pour les poids ouverts disponibles sur [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>), servez le modèle au moyen d'un environnement d'exécution compatible avec OpenAI et utilisez plutôt le fournisseur [vLLM](</fr/providers/vllm>) ou [SGLang](</fr/providers/sglang>) existant d'OpenClaw.

Conservez l'identifiant exact du modèle de l'environnement d'exécution dans le catalogue du fournisseur auto-hébergé ; n'acheminez pas un déploiement local via `longcat/LongCat-2.0`.

## Dépannage

La clé fonctionne dans un shell, mais pas dans le Gateway

Les processus Gateway gérés par un démon n'héritent pas de toutes les variables du shell interactif. Placez `LONGCAT_API_KEY` dans `~/.openclaw/.env`, configurez-la via la configuration initiale ou utilisez une référence de secret approuvée.

Les requêtes échouent avec le code 402 ou 429

`402` signifie que le compte ne dispose pas d'un quota de jetons suffisant. `429` signifie que la clé API a atteint une limite de débit. Consultez l'[utilisation de LongCat](<https://longcat.chat/platform/usage>) et réessayez les requêtes limitées une fois le délai d'attente imposé par le fournisseur écoulé.

Le modèle n'apparaît pas

Exécutez `openclaw plugins list` et confirmez que le plugin `longcat` est activé, puis exécutez `openclaw models list --provider longcat`.

## Ressources associées

[**Fournisseurs de modèles** Configuration des fournisseurs, références de modèles et comportement de basculement. ](</fr/concepts/model-providers>) [**Documentation de l'API LongCat** Points de terminaison de l'API hébergée, authentification, limites et exemples. ](<https://longcat.chat/platform/docs/>) [**Fiche du modèle LongCat-2.0** Architecture, recommandations de déploiement et détails du modèle. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Secrets** Stockez les identifiants du fournisseur sans incorporer de texte en clair dans la configuration. ](</fr/gateway/secrets>)

Was this useful?YesNo

Open issue