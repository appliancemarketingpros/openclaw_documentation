---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/fr/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo est la plateforme d’API pour les modèles **MiMo**. OpenClaw inclut un plugin `xiaomi` intégré qui enregistre à la fois un fournisseur de chat compatible OpenAI et un fournisseur de synthèse vocale (TTS) avec le même `XIAOMI_API_KEY`.

Propriété | Valeur  
---|---  
ID du fournisseur | `xiaomi`  
Plugin | intégré, `enabledByDefault: true`  
Variable d’env. d’authentification | `XIAOMI_API_KEY`  
Option d’onboarding | `--auth-choice xiaomi-api-key`  
Option CLI directe | `--xiaomi-api-key <key>`  
Contrats | complétions de chat + `speechProviders`  
API | compatible OpenAI (`openai-completions`)  
URL de base | `https://api.xiaomimimo.com/v1`  
Modèle par défaut | `xiaomi/mimo-v2-flash`  
TTS par défaut | `mimo-v2.5-tts`, voix `mimo_default`  
  
## Premiers pas

* ### Get an API key

Créez une clé d’API dans la [console Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Ou transmettez directement la clé :

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Catalogue intégré

Réf. de modèle | Entrée | Contexte | Sortie max. | Raisonnement | Notes  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | texte | 262,144 | 8,192 | Non | Modèle par défaut  
`xiaomi/mimo-v2-pro` | texte | 1,048,576 | 32,000 | Oui | Grand contexte  
`xiaomi/mimo-v2-omni` | texte, image | 262,144 | 32,000 | Oui | Multimodal  
  
## Synthèse vocale

Le plugin `xiaomi` intégré enregistre également Xiaomi MiMo comme fournisseur de synthèse vocale pour `messages.tts`. Il appelle le contrat TTS de complétions de chat de Xiaomi avec le texte comme message `assistant` et des indications de style facultatives comme message `user`.

Propriété | Valeur  
---|---  
ID TTS | `xiaomi` (alias `mimo`)  
Authentification | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` avec `audio`  
Par défaut | `mimo-v2.5-tts`, voix `mimo_default`  
Sortie | MP3 par défaut ; WAV si configuré  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Les voix intégrées prises en charge incluent `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` et `Dean`. `mimo-v2-tts` est pris en charge pour les anciens comptes MiMo TTS ; la valeur par défaut utilise le modèle TTS MiMo-V2.5 actuel. Pour les cibles de notes vocales comme Feishu et Telegram, OpenClaw transcode la sortie Xiaomi en Opus 48 kHz avec `ffmpeg` avant la livraison.

## Exemple de configuration

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Auto-injection behavior

Le fournisseur `xiaomi` est injecté automatiquement lorsque `XIAOMI_API_KEY` est défini dans votre environnement ou lorsqu’un profil d’authentification existe. Vous n’avez pas besoin de configurer manuellement le fournisseur, sauf si vous voulez remplacer les métadonnées du modèle ou l’URL de base.

Model details

  * **mimo-v2-flash** — léger et rapide, idéal pour les tâches textuelles généralistes. Pas de prise en charge du raisonnement.
  * **mimo-v2-pro** — prend en charge le raisonnement avec une fenêtre de contexte de 1M de tokens pour les charges de travail sur de longs documents.
  * **mimo-v2-omni** — modèle multimodal avec raisonnement qui accepte à la fois les entrées texte et image.

Troubleshooting

  * Si les modèles n’apparaissent pas, vérifiez que `XIAOMI_API_KEY` est défini et valide.
  * Lorsque le Gateway s’exécute comme daemon, assurez-vous que la clé est disponible pour ce processus (par exemple dans `~/.openclaw/.env` ou via `env.shellEnv`).


## Connexe

[**Model selection** Choisir les fournisseurs, les références de modèles et le comportement de bascule. ](</fr/concepts/model-providers>) [**Configuration reference** Référence complète de configuration OpenClaw. ](</fr/gateway/configuration-reference>) [**Xiaomi MiMo console** Tableau de bord Xiaomi MiMo et gestion des clés d’API. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo