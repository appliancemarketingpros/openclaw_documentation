---
title: Compréhension des médias
source_url: https://docs.openclaw.ai/fr/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw peut **résumer les médias entrants** (image/audio/vidéo) avant l’exécution du pipeline de réponse. Il détecte automatiquement quand des outils locaux ou des clés de fournisseur sont disponibles, et peut être désactivé ou personnalisé. Si la compréhension est désactivée, les modèles reçoivent toujours les fichiers/URL d’origine comme d’habitude.

Le comportement média propre aux vendeurs est enregistré par les plugins vendeurs, tandis que le cœur d’OpenClaw possède la configuration partagée `tools.media`, l’ordre de repli et l’intégration au pipeline de réponse.

## Objectifs

  * Optionnel : pré-digérer les médias entrants en texte court pour un routage plus rapide et une meilleure analyse des commandes.
  * Préserver la livraison des médias d’origine au modèle (toujours).
  * Prendre en charge les **API fournisseur** et les **solutions de repli CLI**.
  * Autoriser plusieurs modèles avec un repli ordonné (erreur/taille/délai d’expiration).


## Comportement général

* ### Collecter les pièces jointes

Collecter les pièces jointes entrantes (`MediaPaths`, `MediaUrls`, `MediaTypes`).

* ### Sélectionner par capacité

Pour chaque capacité activée (image/audio/vidéo), sélectionner les pièces jointes selon la politique (par défaut : **la première**).

* ### Choisir le modèle

Choisir la première entrée de modèle admissible (taille + capacité + auth).

* ### Se replier en cas d’échec

Si un modèle échoue ou si le média est trop volumineux, **se replier sur l’entrée suivante**.

* ### Appliquer le bloc de réussite

En cas de réussite :

  * `Body` devient un bloc `[Image]`, `[Audio]` ou `[Video]`.
  * L’audio définit `{{Transcript}}` ; l’analyse des commandes utilise le texte de légende lorsqu’il est présent, sinon la transcription.
  * Les légendes sont préservées comme `User text:` dans le bloc.


Si la compréhension échoue ou est désactivée, **le flux de réponse continue** avec le corps et les pièces jointes d’origine.

## Aperçu de la configuration

`tools.media` prend en charge des **modèles partagés** ainsi que des remplacements par capacité :

Clés de niveau supérieur

  * `tools.media.models` : liste de modèles partagée (utilisez `capabilities` pour filtrer).
  * `tools.media.image` / `tools.media.audio` / `tools.media.video` : 
    * valeurs par défaut (`prompt`, `maxChars`, `maxBytes`, `timeoutSeconds`, `language`)
    * remplacements de fournisseur (`baseUrl`, `headers`, `providerOptions`)
    * options audio Deepgram via `tools.media.audio.providerOptions.deepgram`
    * contrôles d’écho de transcription audio (`echoTranscript`, par défaut `false` ; `echoFormat`)
    * **liste`models` par capacité** optionnelle (préférée avant les modèles partagés)
    * politique `attachments` (`mode`, `maxAttachments`, `prefer`)
    * `scope` (filtrage optionnel par canal/chatType/clé de session)
  * `tools.media.concurrency` : nombre maximal d’exécutions de capacités simultanées (par défaut **2**).


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### Entrées de modèle

Chaque entrée `models[]` peut être de type **fournisseur** ou **CLI** :

### Entrée fournisseur

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### Entrée CLI

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

Les modèles CLI peuvent aussi utiliser :

  * `{{MediaDir}}` (répertoire contenant le fichier média)
  * `{{OutputDir}}` (répertoire temporaire créé pour cette exécution)
  * `{{OutputBase}}` (chemin de base du fichier temporaire, sans extension)


## Valeurs par défaut et limites

Valeurs par défaut recommandées :

  * `maxChars` : **500** pour image/vidéo (court, adapté aux commandes)
  * `maxChars` : **non défini** pour l’audio (transcription complète sauf si vous définissez une limite)
  * `maxBytes` : 
    * image : **10MB**
    * audio : **20MB**
    * vidéo : **50MB**


Règles

  * Si le média dépasse `maxBytes`, ce modèle est ignoré et le **modèle suivant est essayé**.
  * Les fichiers audio de moins de **1024 octets** sont traités comme vides/corrompus et ignorés avant la transcription fournisseur/CLI ; le contexte de réponse entrante reçoit une transcription de remplacement déterministe afin que l’agent sache que la note était trop courte.
  * Si le modèle renvoie plus de `maxChars`, la sortie est tronquée.
  * `prompt` utilise par défaut un simple "Describe the {media}." plus les indications `maxChars` (image/vidéo uniquement).
  * Si le modèle d’image principal actif prend déjà en charge la vision nativement, OpenClaw ignore le bloc de résumé `[Image]` et transmet plutôt l’image d’origine au modèle.
  * Si un modèle principal Gateway/WebChat est textuel uniquement, les pièces jointes image sont préservées sous forme de références externalisées `media://inbound/*` afin que les outils image/PDF ou le modèle d’image configuré puissent toujours les inspecter au lieu de perdre la pièce jointe.
  * Les requêtes explicites `openclaw infer image describe --model <provider/model>` sont différentes : elles exécutent directement ce fournisseur/modèle compatible image, y compris les références Ollama comme `ollama/qwen2.5vl:7b`.
  * Si `<capability>.enabled: true` mais qu’aucun modèle n’est configuré, OpenClaw essaie le **modèle de réponse actif** lorsque son fournisseur prend en charge la capacité.


### Détection automatique de la compréhension des médias (par défaut)

Si `tools.media.<capability>.enabled` n’est **pas** défini sur `false` et que vous n’avez pas configuré de modèles, OpenClaw détecte automatiquement dans cet ordre et **s’arrête à la première option fonctionnelle** :

* ### Modèle de réponse actif

Modèle de réponse actif lorsque son fournisseur prend en charge la capacité.

* ### agents.defaults.imageModel

Références principales/de repli `agents.defaults.imageModel` (image uniquement). Préférez les références `provider/model`. Les références nues sont qualifiées à partir des seules entrées de modèle de fournisseur compatibles image configurées lorsque la correspondance est unique.

* ### CLI locales (audio uniquement)

CLI locales (si installées) :

  * `sherpa-onnx-offline` (nécessite `SHERPA_ONNX_MODEL_DIR` avec encoder/decoder/joiner/tokens)
  * `whisper-cli` (`whisper-cpp` ; utilise `WHISPER_CPP_MODEL` ou le modèle tiny inclus)
  * `whisper` (CLI Python ; télécharge les modèles automatiquement)


* ### CLI Gemini

`gemini` utilisant `read_many_files`.

* ### Auth fournisseur

  * Les entrées `models.providers.*` configurées qui prennent en charge la capacité sont essayées avant l’ordre de repli inclus.
  * Les fournisseurs de configuration image uniquement avec un modèle compatible image s’enregistrent automatiquement pour la compréhension des médias même lorsqu’ils ne sont pas un Plugin vendeur inclus.
  * La compréhension d’image Ollama est disponible lorsqu’elle est sélectionnée explicitement, par exemple via `agents.defaults.imageModel` ou `openclaw infer image describe --model ollama/<vision-model>`.


Ordre de repli inclus :

  * Audio : OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * Image : OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * Vidéo : Google → Qwen → Moonshot


Pour désactiver la détection automatique, définissez :

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### Prise en charge de l’environnement de proxy (modèles fournisseur)

Lorsque la compréhension des médias **audio** et **vidéo** basée sur un fournisseur est activée, OpenClaw respecte les variables d’environnement de proxy sortant standard pour les appels HTTP fournisseur :

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


Si aucune variable d’environnement de proxy n’est définie, la compréhension des médias utilise une sortie directe. Si la valeur du proxy est mal formée, OpenClaw consigne un avertissement et revient à une récupération directe.

## Capacités (optionnel)

Si vous définissez `capabilities`, l’entrée ne s’exécute que pour ces types de médias. Pour les listes partagées, OpenClaw peut inférer les valeurs par défaut :

  * `openai`, `anthropic`, `minimax` : **image**
  * `minimax-portal` : **image**
  * `moonshot` : **image + vidéo**
  * `openrouter` : **image + audio**
  * `google` (API Gemini) : **image + audio + vidéo**
  * `qwen` : **image + vidéo**
  * `mistral` : **audio**
  * `zai` : **image**
  * `groq` : **audio**
  * `xai` : **audio**
  * `deepgram` : **audio**
  * Tout catalogue `models.providers.<id>.models[]` avec un modèle compatible image : **image**


Pour les entrées CLI, **définissez`capabilities` explicitement** afin d’éviter les correspondances surprenantes. Si vous omettez `capabilities`, l’entrée est admissible pour la liste dans laquelle elle apparaît.

## Matrice de prise en charge des fournisseurs (intégrations OpenClaw)

Capacité | Intégration fournisseur | Notes  
---|---|---  
Image | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), fournisseurs de configuration | Les plugins vendeurs enregistrent la prise en charge des images ; `openai-codex/*` utilise la plomberie du fournisseur OAuth ; `codex/*` utilise un tour borné du Codex app-server ; MiniMax et MiniMax OAuth utilisent tous deux `MiniMax-VL-01` ; les fournisseurs de configuration compatibles image s’enregistrent automatiquement.  
Audio | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | Transcription fournisseur (Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral).  
Vidéo | Google, Qwen, Moonshot | Compréhension vidéo fournisseur via des plugins vendeurs ; la compréhension vidéo Qwen utilise les points de terminaison DashScope Standard.  
  
## Conseils de sélection des modèles

  * Préférez le modèle de dernière génération le plus puissant disponible pour chaque capacité média lorsque la qualité et la sécurité importent.
  * Pour les agents avec outils traitant des entrées non fiables, évitez les modèles médias plus anciens/plus faibles.
  * Conservez au moins un repli par capacité pour la disponibilité (modèle de qualité + modèle plus rapide/moins coûteux).
  * Les replis CLI (`whisper-cli`, `whisper`, `gemini`) sont utiles lorsque les API fournisseur ne sont pas disponibles.
  * Note `parakeet-mlx` : avec `--output-dir`, OpenClaw lit `<output-dir>/<media-basename>.txt` lorsque le format de sortie est `txt` (ou non spécifié) ; les formats non `txt` se replient sur stdout.


## Politique des pièces jointes

Par capacité, `attachments` contrôle quelles pièces jointes sont traitées :

Traiter la première pièce jointe sélectionnée ou toutes les pièces jointes sélectionnées.

Limite le nombre d’éléments traités.

Préférence de sélection parmi les pièces jointes candidates.

Lorsque `mode: "all"`, les sorties sont étiquetées `[Image 1/2]`, `[Audio 2/2]`, etc.

File-attachment extraction behavior

  * Le texte extrait des fichiers est encapsulé comme **contenu externe non fiable** avant d’être ajouté à l’invite multimédia.
  * Le bloc injecté utilise des marqueurs de délimitation explicites comme `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` et inclut une ligne de métadonnées `Source: External`.
  * Ce chemin d’extraction des pièces jointes omet volontairement la longue bannière `SECURITY NOTICE:` afin d’éviter d’alourdir l’invite multimédia ; les marqueurs de délimitation et les métadonnées restent toutefois présents.
  * Si un fichier ne contient aucun texte extractible, OpenClaw injecte `[No extractable text]`.
  * Si un PDF revient aux images de pages rendues dans ce chemin, l’invite multimédia conserve l’espace réservé `[PDF content rendered to images; images not forwarded to model]`, car cette étape d’extraction des pièces jointes transmet des blocs de texte, et non les images PDF rendues.


## Exemples de configuration

### Shared models + overrides

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### Audio + video only

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Image-only

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Multi-modal single entry

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## Sortie d’état

Lorsque la compréhension multimédia s’exécute, `/status` inclut une courte ligne de résumé :

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

Cela affiche les résultats par capacité ainsi que le fournisseur/modèle choisi, le cas échéant.

## Notes

  * La compréhension fonctionne **au mieux**. Les erreurs ne bloquent pas les réponses.
  * Les pièces jointes sont toujours transmises aux modèles même lorsque la compréhension est désactivée.
  * Utilisez `scope` pour limiter l’endroit où la compréhension s’exécute (par exemple, uniquement dans les DM).


## Connexe

  * [Configuration](</fr/gateway/configuration>)
  * [Prise en charge des images et des médias](</fr/nodes/images>)


Was this useful?YesNo