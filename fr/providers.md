---
title: Répertoire des fournisseurs
source_url: https://docs.openclaw.ai/fr/providers
scraped_at: 2026-05-25
---

OpenClaw peut utiliser de nombreux fournisseurs de LLM. Choisissez un fournisseur, authentifiez-vous, puis définissez le modèle par défaut sous la forme `provider/model`.

Vous cherchez la documentation des canaux de chat (WhatsApp/Telegram/Discord/Slack/Mattermost (Plugin)/etc.) ? Consultez [Canaux](</fr/channels>).

## Démarrage rapide

  1. Authentifiez-vous auprès du fournisseur (généralement via `openclaw onboard`).
  2. Définissez le modèle par défaut :

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## Documentation des fournisseurs

  * [Alibaba Model Studio](</fr/providers/alibaba>)
  * [Amazon Bedrock](</fr/providers/bedrock>)
  * [Amazon Bedrock Mantle](</fr/providers/bedrock-mantle>)
  * [Anthropic (API + Claude CLI)](</fr/providers/anthropic>)
  * [Arcee AI (modèles Trinity)](</fr/providers/arcee>)
  * [Azure Speech](</fr/providers/azure-speech>)
  * [BytePlus (international)](</fr/concepts/model-providers#byteplus-international>)
  * [Cerebras](</fr/providers/cerebras>)
  * [Chutes](</fr/providers/chutes>)
  * [Cloudflare AI Gateway](</fr/providers/cloudflare-ai-gateway>)
  * [ComfyUI](</fr/providers/comfy>)
  * [DeepSeek](</fr/providers/deepseek>)
  * [ElevenLabs](</fr/providers/elevenlabs>)
  * [fal](</fr/providers/fal>)
  * [Fireworks](</fr/providers/fireworks>)
  * [GitHub Copilot](</fr/providers/github-copilot>)
  * [modèles GLM](</fr/providers/glm>)
  * [Google (Gemini)](</fr/providers/google>)
  * [Gradium](</fr/providers/gradium>)
  * [Groq (inférence LPU)](</fr/providers/groq>)
  * [Hugging Face (inférence)](</fr/providers/huggingface>)
  * [inferrs (modèles locaux)](</fr/providers/inferrs>)
  * [Kilocode](</fr/providers/kilocode>)
  * [LiteLLM (gateway unifié)](</fr/providers/litellm>)
  * [LM Studio (modèles locaux)](</fr/providers/lmstudio>)
  * [MiniMax](</fr/providers/minimax>)
  * [Mistral](</fr/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</fr/providers/moonshot>)
  * [NVIDIA](</fr/providers/nvidia>)
  * [Ollama (cloud + modèles locaux)](</fr/providers/ollama>)
  * [OpenAI (API + Codex)](</fr/providers/openai>)
  * [OpenCode](</fr/providers/opencode>)
  * [OpenCode Go](</fr/providers/opencode-go>)
  * [OpenRouter](</fr/providers/openrouter>)
  * [Perplexity (recherche web)](</fr/providers/perplexity-provider>)
  * [Qianfan](</fr/providers/qianfan>)
  * [Qwen Cloud](</fr/providers/qwen>)
  * [Runway](</fr/providers/runway>)
  * [SenseAudio](</fr/providers/senseaudio>)
  * [SGLang (modèles locaux)](</fr/providers/sglang>)
  * [StepFun](</fr/providers/stepfun>)
  * [Synthetic](</fr/providers/synthetic>)
  * [Tencent Cloud (TokenHub)](</fr/providers/tencent>)
  * [Together AI](</fr/providers/together>)
  * [Venice (Venice AI, axé sur la confidentialité)](</fr/providers/venice>)
  * [Vercel AI Gateway](</fr/providers/vercel-ai-gateway>)
  * [vLLM (modèles locaux)](</fr/providers/vllm>)
  * [Volcengine (Doubao)](</fr/providers/volcengine>)
  * [Vydra](</fr/providers/vydra>)
  * [xAI](</fr/providers/xai>)
  * [Xiaomi](</fr/providers/xiaomi>)
  * [Z.AI](</fr/providers/zai>)


## Pages de présentation partagées

  * [Variantes groupées supplémentaires](</fr/providers/models#additional-bundled-provider-variants>) \- Anthropic Vertex, Copilot Proxy et Gemini CLI OAuth
  * [Génération d’images](</fr/tools/image-generation>) \- Outil `image_generate` partagé, sélection du fournisseur et basculement
  * [Génération de musique](</fr/tools/music-generation>) \- Outil `music_generate` partagé, sélection du fournisseur et basculement
  * [Génération de vidéos](</fr/tools/video-generation>) \- Outil `video_generate` partagé, sélection du fournisseur et basculement


## Fournisseurs de transcription

  * [Deepgram (transcription audio)](</fr/providers/deepgram>)
  * [ElevenLabs](</fr/providers/elevenlabs#speech-to-text>)
  * [Mistral](</fr/providers/mistral#audio-transcription-voxtral>)
  * [OpenAI](</fr/providers/openai#speech-to-text>)
  * [SenseAudio](</fr/providers/senseaudio>)
  * [xAI](</fr/providers/xai#speech-to-text>)


## Outils communautaires

  * [Claude Max API Proxy](</fr/providers/claude-max-api-proxy>) \- Proxy communautaire pour les identifiants d’abonnement Claude (vérifiez la politique/les conditions d’Anthropic avant utilisation)


Pour le catalogue complet des fournisseurs (xAI, Groq, Mistral, etc.) et la configuration avancée, consultez [Fournisseurs de modèles](</fr/concepts/model-providers>).

Was this useful?YesNo