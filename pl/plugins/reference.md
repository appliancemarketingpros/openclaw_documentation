---
title: Dokumentacja referencyjna dla Plugin
source_url: https://docs.openclaw.ai/pl/plugins/reference
scraped_at: 2026-05-25
---

# Referencja Pluginu

Ta strona jest generowana na podstawie `extensions/*/package.json` oraz `openclaw.plugin.json`. Wygeneruj ją ponownie za pomocą:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

Plugin | Opis | Dystrybucja | Powierzchnia  
---|---|---|---  
[acpx](</pl/plugins/reference/acpx>) | Wbudowany backend środowiska wykonawczego ACP z zarządzaniem sesją i transportem należącym do Plugin. | `@openclaw/acpx` |   
npm; ClawHub | Skills |  |   
[alibaba](</pl/plugins/reference/alibaba>) | Dodaje obsługę dostawcy generowania wideo. | `@openclaw/alibaba-provider` |   
zawarty w OpenClaw | kontrakty: videoGenerationProviders |  |   
[amazon-bedrock](</pl/plugins/reference/amazon-bedrock>) | Dodaje obsługę dostawcy modeli Amazon Bedrock do OpenClaw. | `@openclaw/amazon-bedrock-provider` |   
zawarty w OpenClaw | dostawcy: amazon-bedrock; kontrakty: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</pl/plugins/reference/amazon-bedrock-mantle>) | Dodaje obsługę dostawcy modeli Amazon Bedrock Mantle do OpenClaw. | `@openclaw/amazon-bedrock-mantle-provider` |   
zawarty w OpenClaw | dostawcy: amazon-bedrock-mantle |  |   
[anthropic](</pl/plugins/reference/anthropic>) | Dodaje obsługę dostawcy modeli Anthropic do OpenClaw. | `@openclaw/anthropic-provider` |   
zawarty w OpenClaw | dostawcy: anthropic; kontrakty: mediaUnderstandingProviders |  |   
[anthropic-vertex](</pl/plugins/reference/anthropic-vertex>) | Dodaje obsługę dostawcy modeli Anthropic Vertex do OpenClaw. | `@openclaw/anthropic-vertex-provider` |   
zawarty w OpenClaw | dostawcy: anthropic-vertex |  |   
[arcee](</pl/plugins/reference/arcee>) | Dodaje obsługę dostawcy modeli Arcee do OpenClaw. | `@openclaw/arcee-provider` |   
zawarty w OpenClaw | dostawcy: arcee |  |   
[azure-speech](</pl/plugins/reference/azure-speech>) | Zamiana tekstu na mowę Azure AI Speech (MP3, natywne notatki głosowe Ogg/Opus, telefonia PCM). | `@openclaw/azure-speech` |   
zawarty w OpenClaw | kontrakty: speechProviders |  |   
[bonjour](</pl/plugins/reference/bonjour>) | Rozgłasza lokalny Gateway OpenClaw przez Bonjour/mDNS. | `@openclaw/bonjour` |   
zawarty w OpenClaw | Plugin |  |   
[brave](</pl/plugins/reference/brave>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/brave-plugin` |   
npm; ClawHub | kontrakty: webSearchProviders |  |   
[browser](</pl/plugins/reference/browser>) | Dodaje narzędzia wywoływane przez agenta. | `@openclaw/browser-plugin` |   
zawarty w OpenClaw | kontrakty: tools; Skills |  |   
[byteplus](</pl/plugins/reference/byteplus>) | Dodaje obsługę dostawców modeli BytePlus i BytePlus Plan do OpenClaw. | `@openclaw/byteplus-provider` |   
zawarty w OpenClaw | dostawcy: byteplus, byteplus-plan; kontrakty: videoGenerationProviders |  |   
[canvas](</pl/plugins/reference/canvas>) | Eksperymentalne powierzchnie sterowania Canvas i renderowania A2UI dla sparowanych węzłów. | `@openclaw/canvas-plugin` |   
zawarty w OpenClaw | kontrakty: tools |  |   
[cerebras](</pl/plugins/reference/cerebras>) | Dodaje obsługę dostawcy modeli Cerebras do OpenClaw. | `@openclaw/cerebras-provider` |   
zawarty w OpenClaw | dostawcy: cerebras |  |   
[chutes](</pl/plugins/reference/chutes>) | Dodaje obsługę dostawcy modeli Chutes do OpenClaw. | `@openclaw/chutes-provider` |   
zawarty w OpenClaw | dostawcy: chutes |  |   
[clickclack](</pl/plugins/reference/clickclack>) | Dodaje powierzchnię kanału Clickclack do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/clickclack` |   
zawarty w OpenClaw | kanały: clickclack |  |   
[cloudflare-ai-gateway](</pl/plugins/reference/cloudflare-ai-gateway>) | Dodaje obsługę dostawcy modeli Cloudflare AI Gateway do OpenClaw. | `@openclaw/cloudflare-ai-gateway-provider` |   
zawarty w OpenClaw | dostawcy: cloudflare-ai-gateway |  |   
[codex](</pl/plugins/reference/codex>) | Uprząż serwera aplikacji Codex i katalog modeli GPT zarządzany przez Codex. | `@openclaw/codex` |   
npm; ClawHub | dostawcy: codex; kontrakty: mediaUnderstandingProviders, migrationProviders |  |   
[comfy](</pl/plugins/reference/comfy>) | Dodaje obsługę dostawcy modeli ComfyUI do OpenClaw. | `@openclaw/comfy-provider` |   
zawarte w OpenClaw | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</pl/plugins/reference/copilot-proxy>) | Dodaje obsługę dostawcy modeli Copilot Proxy do OpenClaw. | `@openclaw/copilot-proxy` |   
zawarte w OpenClaw | providers: copilot-proxy |  |   
[deepgram](</pl/plugins/reference/deepgram>) | Dodaje obsługę dostawcy rozumienia mediów. Dodaje obsługę dostawcy transkrypcji w czasie rzeczywistym. | `@openclaw/deepgram-provider` |   
zawarte w OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</pl/plugins/reference/deepinfra>) | Dodaje obsługę dostawcy modeli DeepInfra do OpenClaw. | `@openclaw/deepinfra-provider` |   
zawarte w OpenClaw | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</pl/plugins/reference/deepseek>) | Dodaje obsługę dostawcy modeli DeepSeek do OpenClaw. | `@openclaw/deepseek-provider` |   
zawarte w OpenClaw | providers: deepseek |  |   
[diagnostics-otel](</pl/plugins/reference/diagnostics-otel>) | Eksporter OpenTelemetry diagnostyki OpenClaw. | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</pl/plugins/reference/diagnostics-prometheus>) | Eksporter Prometheus diagnostyki OpenClaw. | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</pl/plugins/reference/diffs>) | Przeglądarka różnic tylko do odczytu i renderer plików dla agentów. | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</pl/plugins/reference/discord>) | Dodaje powierzchnię kanału Discord do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[document-extract](</pl/plugins/reference/document-extract>) | Wyodrębnia tekst i awaryjne obrazy stron z lokalnych załączników dokumentów. | `@openclaw/document-extract-plugin` |   
zawarte w OpenClaw | contracts: documentExtractors |  |   
[duckduckgo](</pl/plugins/reference/duckduckgo>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/duckduckgo-plugin` |   
zawarte w OpenClaw | contracts: webSearchProviders |  |   
[elevenlabs](</pl/plugins/reference/elevenlabs>) | Dodaje obsługę dostawcy rozumienia mediów. Dodaje obsługę dostawcy transkrypcji w czasie rzeczywistym. Dodaje obsługę dostawcy zamiany tekstu na mowę. | `@openclaw/elevenlabs-speech` |   
zawarte w OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</pl/plugins/reference/exa>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/exa-plugin` |   
zawarte w OpenClaw | contracts: webSearchProviders |  |   
[fal](</pl/plugins/reference/fal>) | Dodaje obsługę dostawcy modeli fal do OpenClaw. | `@openclaw/fal-provider` |   
zawarte w OpenClaw | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[feishu](</pl/plugins/reference/feishu>) | Dodaje powierzchnię kanału Feishu do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[file-transfer](</pl/plugins/reference/file-transfer>) | Pobiera, wyświetla listę i zapisuje pliki na sparowanych węzłach za pomocą dedykowanych poleceń węzłów. Omija obcinanie wyjścia bash stdout, używając base64 przez node.invoke dla plików binarnych do 16 MB. | `@openclaw/file-transfer` |   
zawarte w OpenClaw | contracts: tools |  |   
[firecrawl](</pl/plugins/reference/firecrawl>) | Dodaje narzędzia wywoływane przez agenta. Dodaje obsługę dostawcy pobierania stron z sieci. Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/firecrawl-plugin` |   
zawarte w OpenClaw | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</pl/plugins/reference/fireworks>) | Dodaje obsługę dostawcy modeli Fireworks do OpenClaw. | `@openclaw/fireworks-provider` |   
zawarte w OpenClaw | providers: fireworks |  |   
[github-copilot](</pl/plugins/reference/github-copilot>) | Dodaje obsługę dostawcy modeli GitHub Copilot do OpenClaw. | `@openclaw/github-copilot-provider` |   
zawarte w OpenClaw | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</pl/plugins/reference/google>) | Dodaje obsługę dostawców modeli Google, Google Gemini CLI i Google Vertex do OpenClaw. | `@openclaw/google-plugin` |   
zawarte w OpenClaw | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[google-meet](</pl/plugins/reference/google-meet>) | Dołącza do rozmów Google Meet przez transporty Chrome lub Twilio. | `@openclaw/google-meet` |   
npm; ClawHub | contracts: tools |  |   
[googlechat](</pl/plugins/reference/googlechat>) | Dodaje interfejs kanału Google Chat do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/googlechat` |   
npm; ClawHub | channels: googlechat |  |   
[gradium](</pl/plugins/reference/gradium>) | Dodaje obsługę dostawcy zamiany tekstu na mowę. | `@openclaw/gradium-speech` |   
dołączone do OpenClaw | contracts: speechProviders |  |   
[groq](</pl/plugins/reference/groq>) | Dodaje obsługę dostawcy modeli Groq do OpenClaw. | `@openclaw/groq-provider` |   
dołączone do OpenClaw | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</pl/plugins/reference/huggingface>) | Dodaje obsługę dostawcy modeli Hugging Face do OpenClaw. | `@openclaw/huggingface-provider` |   
dołączone do OpenClaw | providers: huggingface |  |   
[imessage](</pl/plugins/reference/imessage>) | Dodaje interfejs kanału iMessage do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/imessage` |   
dołączone do OpenClaw | channels: imessage |  |   
[inworld](</pl/plugins/reference/inworld>) | Strumieniowa zamiana tekstu na mowę Inworld (MP3, OGG_OPUS, PCM dla telefonii). | `@openclaw/inworld-speech` |   
dołączone do OpenClaw | contracts: speechProviders |  |   
[irc](</pl/plugins/reference/irc>) | Dodaje interfejs kanału IRC do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/irc` |   
dołączone do OpenClaw | channels: irc |  |   
[kilocode](</pl/plugins/reference/kilocode>) | Dodaje obsługę dostawcy modeli Kilocode do OpenClaw. | `@openclaw/kilocode-provider` |   
dołączone do OpenClaw | providers: kilocode |  |   
[kimi](</pl/plugins/reference/kimi>) | Dodaje obsługę dostawców modeli Kimi i Kimi Coding do OpenClaw. | `@openclaw/kimi-provider` |   
dołączone do OpenClaw | providers: kimi, kimi-coding |  |   
[line](</pl/plugins/reference/line>) | Dodaje interfejs kanału LINE do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/line` |   
npm; ClawHub | channels: line |  |   
[litellm](</pl/plugins/reference/litellm>) | Dodaje obsługę dostawcy modeli LiteLLM do OpenClaw. | `@openclaw/litellm-provider` |   
dołączone do OpenClaw | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</pl/plugins/reference/llm-task>) | Ogólne narzędzie LLM zwracające wyłącznie JSON do zadań strukturalnych, wywoływane z przepływów pracy. | `@openclaw/llm-task` |   
dołączone do OpenClaw | contracts: tools |  |   
[lmstudio](</pl/plugins/reference/lmstudio>) | Dodaje obsługę dostawcy modeli LM Studio do OpenClaw. | `@openclaw/lmstudio-provider` |   
dołączone do OpenClaw | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[lobster](</pl/plugins/reference/lobster>) | Typowane narzędzie przepływu pracy ze wznawialnymi zatwierdzeniami. | `@openclaw/lobster` |   
npm; ClawHub | contracts: tools |  |   
[matrix](</pl/plugins/reference/matrix>) | Dodaje interfejs kanału Matrix do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | channels: matrix |  |   
[mattermost](</pl/plugins/reference/mattermost>) | Dodaje interfejs kanału Mattermost do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/mattermost` |   
dołączone do OpenClaw | channels: mattermost |  |   
[memory-core](</pl/plugins/reference/memory-core>) | Dodaje obsługę dostawcy osadzania pamięci. Dodaje narzędzia wywoływane przez agenta. | `@openclaw/memory-core` |   
dołączone do OpenClaw | contracts: memoryEmbeddingProviders, tools |  |   
[memory-lancedb](</pl/plugins/reference/memory-lancedb>) | Dodaje narzędzia wywoływane przez agenta. | `@openclaw/memory-lancedb` |   
npm; ClawHub | contracts: tools |  |   
[memory-wiki](</pl/plugins/reference/memory-wiki>) | Trwały kompilator wiki i przyjazny dla Obsidian magazyn wiedzy dla OpenClaw. | `@openclaw/memory-wiki` |   
dołączone do OpenClaw | contracts: tools; skills |  |   
[microsoft](</pl/plugins/reference/microsoft>) | Dodaje obsługę dostawcy zamiany tekstu na mowę. | `@openclaw/microsoft-speech` |   
zawarte w OpenClaw | contracts: speechProviders |  |   
[microsoft-foundry](</pl/plugins/reference/microsoft-foundry>) | Dodaje do OpenClaw obsługę dostawcy modeli Microsoft Foundry. | `@openclaw/microsoft-foundry` |   
zawarte w OpenClaw | providers: microsoft-foundry |  |   
[migrate-claude](</pl/plugins/reference/migrate-claude>) | Importuje instrukcje Claude Code i Claude Desktop, serwery MCP, Skills oraz bezpieczną konfigurację do OpenClaw. | `@openclaw/migrate-claude` |   
zawarte w OpenClaw | contracts: migrationProviders |  |   
[migrate-hermes](</pl/plugins/reference/migrate-hermes>) | Importuje konfigurację Hermes, pamięci, Skills i obsługiwane dane uwierzytelniające do OpenClaw. | `@openclaw/migrate-hermes` |   
zawarte w OpenClaw | contracts: migrationProviders |  |   
[minimax](</pl/plugins/reference/minimax>) | Dodaje do OpenClaw obsługę dostawców modeli MiniMax i MiniMax Portal. | `@openclaw/minimax-provider` |   
zawarte w OpenClaw | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</pl/plugins/reference/mistral>) | Dodaje do OpenClaw obsługę dostawcy modeli Mistral. | `@openclaw/mistral-provider` |   
zawarte w OpenClaw | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</pl/plugins/reference/moonshot>) | Dodaje do OpenClaw obsługę dostawcy modeli Moonshot. | `@openclaw/moonshot-provider` |   
zawarte w OpenClaw | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[msteams](</pl/plugins/reference/msteams>) | Dodaje powierzchnię kanału Microsoft Teams do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</pl/plugins/reference/nextcloud-talk>) | Dodaje powierzchnię kanału Nextcloud Talk do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</pl/plugins/reference/nostr>) | Dodaje powierzchnię kanału Nostr do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[nvidia](</pl/plugins/reference/nvidia>) | Dodaje do OpenClaw obsługę dostawcy modeli NVIDIA. | `@openclaw/nvidia-provider` |   
zawarte w OpenClaw | providers: nvidia |  |   
[oc-path](</pl/plugins/reference/oc-path>) | Dodaje CLI ścieżki openclaw do adresowania plików obszaru roboczego oc://. | `@openclaw/oc-path` |   
zawarte w OpenClaw | plugin |  |   
[ollama](</pl/plugins/reference/ollama>) | Dodaje do OpenClaw obsługę dostawcy modeli Ollama. | `@openclaw/ollama-provider` |   
zawarte w OpenClaw | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</pl/plugins/reference/open-prose>) | Pakiet Skills OpenProse VM z poleceniem ukośnikowym /prose. | `@openclaw/open-prose` |   
zawarte w OpenClaw | skills |  |   
[openai](</pl/plugins/reference/openai>) | Dodaje do OpenClaw obsługę dostawców modeli OpenAI i OpenAI Codex. | `@openclaw/openai-provider` |   
zawarte w OpenClaw | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</pl/plugins/reference/opencode>) | Dodaje do OpenClaw obsługę dostawcy modeli OpenCode. | `@openclaw/opencode-provider` |   
zawarte w OpenClaw | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</pl/plugins/reference/opencode-go>) | Dodaje do OpenClaw obsługę dostawcy modeli OpenCode Go. | `@openclaw/opencode-go-provider` |   
zawarte w OpenClaw | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</pl/plugins/reference/openrouter>) | Dodaje do OpenClaw obsługę dostawcy modeli OpenRouter. | `@openclaw/openrouter-provider` |   
zawarte w OpenClaw | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</pl/plugins/reference/openshell>) | Backend piaskownicy oparty na OpenShell z lustrzanymi lokalnymi obszarami roboczymi i wykonywaniem poleceń przez SSH. | `@openclaw/openshell-sandbox` |   
zawarte w OpenClaw | plugin |  |   
[perplexity](</pl/plugins/reference/perplexity>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/perplexity-plugin` |   
zawarte w OpenClaw | contracts: webSearchProviders |  |   
[qa-channel](</pl/plugins/reference/qa-channel>) | Dodaje powierzchnię kanału QA Channel do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/qa-channel` |   
tylko checkout źródłowy | channels: qa-channel |  |   
[qa-lab](</pl/plugins/reference/qa-lab>) | Plugin laboratorium QA OpenClaw z prywatnym interfejsem debuggera i mechanizmem uruchamiania scenariuszy. | `@openclaw/qa-lab` |   
tylko checkout źródłowy | plugin |  |   
[qa-matrix](</pl/plugins/reference/qa-matrix>) | Mechanizm uruchamiania transportu Matrix QA i jego warstwa bazowa. | `@openclaw/qa-matrix` |   
tylko checkout źródłowy | plugin |  |   
[qianfan](</pl/plugins/reference/qianfan>) | Dodaje obsługę dostawcy modeli Qianfan do OpenClaw. | `@openclaw/qianfan-provider` |   
zawarte w OpenClaw | providers: qianfan |  |   
[qqbot](</pl/plugins/reference/qqbot>) | Dodaje powierzchnię kanału QQ Bot do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[qwen](</pl/plugins/reference/qwen>) | Dodaje obsługę dostawców modeli Qwen, Qwen Cloud, Model Studio i DashScope do OpenClaw. | `@openclaw/qwen-provider` |   
zawarte w OpenClaw | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</pl/plugins/reference/runway>) | Dodaje obsługę dostawcy generowania wideo. | `@openclaw/runway-provider` |   
zawarte w OpenClaw | contracts: videoGenerationProviders |  |   
[searxng](</pl/plugins/reference/searxng>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/searxng-plugin` |   
zawarte w OpenClaw | contracts: webSearchProviders |  |   
[senseaudio](</pl/plugins/reference/senseaudio>) | Dodaje obsługę dostawcy rozumienia mediów. | `@openclaw/senseaudio-provider` |   
zawarte w OpenClaw | contracts: mediaUnderstandingProviders |  |   
[sglang](</pl/plugins/reference/sglang>) | Dodaje obsługę dostawcy modeli SGLang do OpenClaw. | `@openclaw/sglang-provider` |   
zawarte w OpenClaw | providers: sglang |  |   
[signal](</pl/plugins/reference/signal>) | Dodaje powierzchnię kanału Signal do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/signal` |   
zawarte w OpenClaw | channels: signal |  |   
[skill-workshop](</pl/plugins/reference/skill-workshop>) | Przechwytuje powtarzalne przepływy pracy jako workspace Skills, z oczekującą recenzją, bezpiecznymi zapisami i odświeżaniem promptu Skills. | `@openclaw/skill-workshop` |   
zawarte w OpenClaw | contracts: tools |  |   
[slack](</pl/plugins/reference/slack>) | Dodaje powierzchnię kanału Slack do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/slack` |   
zawarte w OpenClaw | channels: slack |  |   
[stepfun](</pl/plugins/reference/stepfun>) | Dodaje obsługę dostawców modeli StepFun i StepFun Plan do OpenClaw. | `@openclaw/stepfun-provider` |   
zawarte w OpenClaw | providers: stepfun, stepfun-plan |  |   
[synology-chat](</pl/plugins/reference/synology-chat>) | Dodaje powierzchnię kanału Synology Chat do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[synthetic](</pl/plugins/reference/synthetic>) | Dodaje obsługę dostawcy modeli Synthetic do OpenClaw. | `@openclaw/synthetic-provider` |   
zawarte w OpenClaw | providers: synthetic |  |   
[tavily](</pl/plugins/reference/tavily>) | Dodaje narzędzia wywoływalne przez agenta. Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/tavily-plugin` |   
zawarte w OpenClaw | contracts: tools, webSearchProviders; skills |  |   
[telegram](</pl/plugins/reference/telegram>) | Dodaje powierzchnię kanału Telegram do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/telegram` |   
zawarte w OpenClaw | channels: telegram |  |   
[tencent](</pl/plugins/reference/tencent>) | Dodaje obsługę dostawcy modeli Tencent TokenHub do OpenClaw. | `@openclaw/tencent-provider` |   
zawarte w OpenClaw | providers: tencent-tokenhub |  |   
[tlon](</pl/plugins/reference/tlon>) | Dodaje powierzchnię kanału Tlon do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[together](</pl/plugins/reference/together>) | Dodaje do OpenClaw obsługę dostawcy modeli Together. | `@openclaw/together-provider` |   
dołączony do OpenClaw | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</pl/plugins/reference/tokenjuice>) | Kompaktuje wyniki narzędzi exec i bash za pomocą reduktorów tokenjuice. | `@openclaw/tokenjuice` |   
dołączony do OpenClaw | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</pl/plugins/reference/tts-local-cli>) | Dodaje obsługę dostawcy zamiany tekstu na mowę. | `@openclaw/tts-local-cli` |   
dołączony do OpenClaw | contracts: speechProviders |  |   
[twitch](</pl/plugins/reference/twitch>) | Dodaje powierzchnię kanału Twitch do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[venice](</pl/plugins/reference/venice>) | Dodaje do OpenClaw obsługę dostawcy modeli Venice. | `@openclaw/venice-provider` |   
dołączony do OpenClaw | providers: venice |  |   
[vercel-ai-gateway](</pl/plugins/reference/vercel-ai-gateway>) | Dodaje do OpenClaw obsługę dostawcy modeli Vercel AI Gateway. | `@openclaw/vercel-ai-gateway-provider` |   
dołączony do OpenClaw | providers: vercel-ai-gateway |  |   
[vllm](</pl/plugins/reference/vllm>) | Dodaje do OpenClaw obsługę dostawcy modeli vLLM. | `@openclaw/vllm-provider` |   
dołączony do OpenClaw | providers: vllm |  |   
[voice-call](</pl/plugins/reference/voice-call>) | Dodaje narzędzia wywoływane przez agenta. | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[volcengine](</pl/plugins/reference/volcengine>) | Dodaje do OpenClaw obsługę dostawców modeli Volcengine i Volcengine Plan. | `@openclaw/volcengine-provider` |   
dołączony do OpenClaw | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</pl/plugins/reference/voyage>) | Dodaje obsługę dostawcy osadzania pamięci. | `@openclaw/voyage-provider` |   
dołączony do OpenClaw | contracts: memoryEmbeddingProviders |  |   
[vydra](</pl/plugins/reference/vydra>) | Dodaje do OpenClaw obsługę dostawcy modeli Vydra. | `@openclaw/vydra-provider` |   
dołączony do OpenClaw | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</pl/plugins/reference/web-readability>) | Wyodrębnia czytelną treść artykułu z lokalnych odpowiedzi pobierania stron HTML. | `@openclaw/web-readability-plugin` |   
dołączony do OpenClaw | contracts: webContentExtractors |  |   
[webhooks](</pl/plugins/reference/webhooks>) | Uwierzytelnione przychodzące webhooki, które wiążą zewnętrzną automatyzację z TaskFlow OpenClaw. | `@openclaw/webhooks` |   
dołączony do OpenClaw | plugin |  |   
[whatsapp](</pl/plugins/reference/whatsapp>) | Dodaje powierzchnię kanału WhatsApp do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[xai](</pl/plugins/reference/xai>) | Dodaje do OpenClaw obsługę dostawcy modeli xAI. | `@openclaw/xai-plugin` |   
dołączony do OpenClaw | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</pl/plugins/reference/xiaomi>) | Dodaje do OpenClaw obsługę dostawcy modeli Xiaomi. | `@openclaw/xiaomi-provider` |   
dołączony do OpenClaw | providers: xiaomi; contracts: speechProviders |  |   
[zai](</pl/plugins/reference/zai>) | Dodaje do OpenClaw obsługę dostawcy modeli [Z.AI](<http://Z.AI>). | `@openclaw/zai-provider` |   
dołączony do OpenClaw | providers: zai; contracts: mediaUnderstandingProviders |  |   
[zalo](</pl/plugins/reference/zalo>) | Dodaje powierzchnię kanału Zalo do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</pl/plugins/reference/zalouser>) | Dodaje powierzchnię kanału Zalo Personal do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
Was this useful?YesNo