---
title: DeepSeek
source_url: https://docs.openclaw.ai/fr/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) fournit de puissants modèles d’IA avec une API compatible OpenAI.

Propriété | Valeur  
---|---  
Fournisseur | `deepseek`  
Authentification | `DEEPSEEK_API_KEY`  
API | compatible OpenAI  
URL de base | `https://api.deepseek.com`  
  
## Premiers pas

* ### Obtenir votre clé API

Créez une clé API sur [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Exécuter la configuration initiale

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

Cela demandera votre clé API et définira `deepseek/deepseek-v4-flash` comme modèle par défaut.

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Pour inspecter le catalogue statique intégré sans nécessiter un Gateway en cours d’exécution, utilisez :

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Configuration non interactive

Pour les installations scriptées ou sans interface, passez directement tous les indicateurs :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catalogue intégré

Référence de modèle | Nom | Entrée | Contexte | Sortie max. | Notes  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | texte | 1,000,000 | 384,000 | Modèle par défaut ; surface V4 compatible avec la réflexion  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | texte | 1,000,000 | 384,000 | Surface V4 compatible avec la réflexion  
`deepseek/deepseek-chat` | DeepSeek Chat | texte | 131,072 | 8,192 | Surface DeepSeek V3.2 sans réflexion  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | texte | 131,072 | 65,536 | Surface V3.2 avec raisonnement activé  
  
## Réflexion et outils

Les sessions de réflexion DeepSeek V4 ont un contrat de rejeu plus strict que la plupart des fournisseurs compatibles OpenAI : après qu’un tour avec réflexion activée utilise des outils, DeepSeek s’attend à ce que les messages d’assistant rejoués depuis ce tour incluent `reasoning_content` dans les requêtes de suivi. OpenClaw gère cela dans le Plugin DeepSeek, donc l’utilisation normale des outils sur plusieurs tours fonctionne avec `deepseek/deepseek-v4-flash` et `deepseek/deepseek-v4-pro`.

Si vous basculez une session existante depuis un autre fournisseur compatible OpenAI vers un modèle DeepSeek V4, les anciens tours d’appels d’outils de l’assistant peuvent ne pas avoir de `reasoning_content` DeepSeek natif. OpenClaw renseigne ce champ manquant dans les messages d’assistant rejoués pour les requêtes de réflexion DeepSeek V4 afin que le fournisseur puisse accepter l’historique sans nécessiter `/new`.

Lorsque la réflexion est désactivée dans OpenClaw (y compris la sélection **Aucun** dans l’interface), OpenClaw envoie `thinking: { type: "disabled" }` à DeepSeek et retire le `reasoning_content` rejoué de l’historique sortant. Cela maintient les sessions sans réflexion sur le chemin DeepSeek sans réflexion.

Utilisez `deepseek/deepseek-v4-flash` pour le chemin rapide par défaut. Utilisez `deepseek/deepseek-v4-pro` lorsque vous voulez le modèle V4 plus puissant et pouvez accepter un coût ou une latence plus élevés.

## Tests en conditions réelles

La suite de modèles en conditions réelles directes inclut DeepSeek V4 dans l’ensemble de modèles modernes. Pour exécuter uniquement les vérifications de modèles directs DeepSeek V4 :

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Cette vérification en conditions réelles confirme que les deux modèles V4 peuvent terminer et que les tours de suivi réflexion/outil préservent la charge utile de rejeu requise par DeepSeek.

## Exemple de configuration

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Associé

[**Sélection du modèle** Choisir les fournisseurs, les références de modèle et le comportement de basculement. ](</fr/concepts/model-providers>) [**Référence de configuration** Référence complète de configuration pour les agents, les modèles et les fournisseurs. ](</fr/gateway/configuration-reference>)

Was this useful?YesNo