---
title: Together AI
source_url: https://docs.openclaw.ai/fr/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) donne accès à des modèles open source de premier plan, notamment Llama, DeepSeek, Kimi et d’autres, via une API unifiée.

Propriété | Valeur  
---|---  
Fournisseur | `together`  
Authentification | `TOGETHER_API_KEY`  
API | compatible OpenAI  
URL de base | `https://api.together.xyz/v1`  
  
## Premiers pas

* ### Obtenir une clé API

Créez une clé API sur [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Exemple non interactif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Catalogue intégré

OpenClaw inclut ce catalogue Together groupé :

Réf. de modèle | Nom | Entrée | Contexte | Notes  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | texte, image | 262,144 | Modèle par défaut ; raisonnement activé  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | texte | 202,752 | Modèle de texte polyvalent  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | texte | 131,072 | Modèle d’instructions rapide  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | texte, image | 10,000,000 | Multimodal  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | texte, image | 20,000,000 | Multimodal  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | texte | 131,072 | Modèle de texte général  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | texte | 131,072 | Modèle de raisonnement  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | texte | 262,144 | Modèle de texte Kimi secondaire  
  
## Génération vidéo

Le Plugin `together` groupé enregistre également la génération vidéo via l’outil partagé `video_generate`.

Propriété | Valeur  
---|---  
Modèle vidéo par défaut | `together/Wan-AI/Wan2.2-T2V-A14B`  
Modes | texte vers vidéo, référence à image unique  
Paramètres pris en charge | `aspectRatio`, `resolution`  
  
Pour utiliser Together comme fournisseur vidéo par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Note sur l’environnement

Si le Gateway s’exécute comme un daemon (launchd/systemd), assurez-vous que `TOGETHER_API_KEY` est disponible pour ce processus (par exemple, dans `~/.openclaw/.env` ou via `env.shellEnv`).

Dépannage

  * Vérifiez que votre clé fonctionne : `openclaw models list --provider together`
  * Si les modèles n’apparaissent pas, confirmez que la clé API est définie dans le bon environnement pour votre processus Gateway.
  * Les références de modèle utilisent la forme `together/<model-id>`.


## Voir aussi

[**Sélection du modèle** Règles de fournisseur, références de modèle et comportement de basculement. ](</fr/concepts/model-providers>) [**Génération vidéo** Paramètres de l’outil de génération vidéo partagé et sélection du fournisseur. ](</fr/tools/video-generation>) [**Référence de configuration** Schéma de configuration complet incluant les paramètres de fournisseur. ](</fr/gateway/configuration-reference>) [**Together AI** Tableau de bord Together AI, documentation de l’API et tarifs. ](<https://together.ai>)

Was this useful?YesNo