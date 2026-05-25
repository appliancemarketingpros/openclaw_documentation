---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/fr/providers/volcengine
scraped_at: 2026-05-25
---

Le fournisseur Volcengine donne accès aux modèles Doubao et aux modèles tiers hébergés sur Volcano Engine, avec des points de terminaison séparés pour les charges de travail générales et de code. Le même Plugin intégré peut également enregistrer Volcengine Speech comme fournisseur de TTS.

Détail | Valeur  
---|---  
Fournisseurs | `volcengine` (général + TTS) + `volcengine-plan` (code)  
Authentification des modèles | `VOLCANO_ENGINE_API_KEY`  
Authentification TTS | `VOLCENGINE_TTS_API_KEY` ou `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | Modèles compatibles OpenAI, TTS BytePlus Seed Speech  
  
## Premiers pas

* ### Définir la clé API

Exécutez l’onboarding interactif :

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Cela enregistre à la fois les fournisseurs général (`volcengine`) et de code (`volcengine-plan`) à partir d’une seule clé API.

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Fournisseurs et points de terminaison

Fournisseur | Point de terminaison | Cas d’usage  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Modèles généraux  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Modèles de code  
  
## Catalogue intégré

### Général (volcengine)

Réf. de modèle | Nom | Entrée | Contexte  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | texte, image | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | texte, image | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | texte, image | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | texte, image | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | texte, image | 128,000  
  
### Code (volcengine-plan)

Réf. de modèle | Nom | Entrée | Contexte  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | texte | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | texte | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | texte | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | texte | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | texte | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | texte | 256,000  
  
## Synthèse vocale

Le TTS Volcengine utilise l’API HTTP BytePlus Seed Speech et se configure séparément de la clé API du modèle Doubao compatible OpenAI. Dans la console BytePlus, ouvrez Seed Speech > Settings > API Keys et copiez la clé API, puis définissez :

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Ensuite, activez-le dans `openclaw.json` :

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Pour les cibles de note vocale, OpenClaw demande à Volcengine le format natif du fournisseur `ogg_opus`. Pour les pièces jointes audio normales, il demande `mp3`. Les alias de fournisseur `bytedance` et `doubao` pointent également vers le même fournisseur vocal.

L’identifiant de ressource par défaut est `seed-tts-1.0` car c’est celui que BytePlus accorde aux clés API Seed Speech nouvellement créées dans le projet par défaut. Si votre projet dispose du droit TTS 2.0, définissez `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

L’authentification héritée AppID/jeton reste prise en charge pour les anciennes applications Speech Console :

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Configuration avancée

Modèle par défaut après l’onboarding

`openclaw onboard --auth-choice volcengine-api-key` définit actuellement `volcengine-plan/ark-code-latest` comme modèle par défaut tout en enregistrant également le catalogue général `volcengine`.

Comportement de repli du sélecteur de modèles

Pendant l’onboarding/la configuration de la sélection du modèle, le choix d’authentification Volcengine privilégie à la fois les lignes `volcengine/*` et `volcengine-plan/*`. Si ces modèles ne sont pas encore chargés, OpenClaw se replie sur le catalogue non filtré au lieu d’afficher un sélecteur limité au fournisseur vide.

Variables d’environnement pour les processus daemon

Si le Gateway s’exécute comme un daemon (launchd/systemd), assurez-vous que les variables d’environnement du modèle et du TTS telles que `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID`, et `VOLCENGINE_TTS_TOKEN` sont disponibles pour ce processus (par exemple dans `~/.openclaw/.env` ou via `env.shellEnv`).

## Lié

[**Sélection du modèle** Choisir les fournisseurs, les références de modèles et le comportement de bascule. ](</fr/concepts/model-providers>) [**Configuration** Référence complète de configuration pour les agents, les modèles et les fournisseurs. ](</fr/gateway/configuration>) [**Dépannage** Problèmes courants et étapes de débogage. ](</fr/help/troubleshooting>) [**FAQ** Questions fréquentes sur la configuration d’OpenClaw. ](</fr/help/faq>)

Was this useful?YesNo