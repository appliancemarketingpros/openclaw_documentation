---
title: Inwentarz Plugin
source_url: https://docs.openclaw.ai/pl/plugins/plugin-inventory
scraped_at: 2026-05-25
---

# Spis Plugin

Ta strona jest generowana z `extensions/*/package.json`, `openclaw.plugin.json` oraz wykluczeń `files` głównego pakietu npm. Wygeneruj ją ponownie poleceniem:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

## Definicje

  * **Główny pakiet npm:** wbudowany w pakiet npm `openclaw` i dostępny bez osobnej instalacji Plugin.
  * **Oficjalny pakiet zewnętrzny:** utrzymywany przez OpenClaw Plugin pominięty w głównym pakiecie npm, przechowywany w tym oficjalnym spisie i instalowany na żądanie przez ClawHub i/lub npm.
  * **Tylko checkout źródłowy:** lokalny dla repozytorium Plugin pominięty w publikowanych artefaktach npm i niereklamowany jako pakiet możliwy do zainstalowania.


Checkouty źródłowe różnią się od instalacji npm: po `pnpm install` dołączone Pluginy ładują się z `extensions/<id>`, więc dostępne są lokalne zmiany i zależności obszaru roboczego lokalne dla pakietu.

## Zainstaluj Plugin

Użyj kolumny **Dystrybucja** , aby zdecydować, czy instalacja jest potrzebna. Pluginy, które mają wartość `included in OpenClaw`, są już obecne w głównym pakiecie. Oficjalne pakiety zewnętrzne wymagają jednej instalacji, a następnie ponownego uruchomienia Gateway.

Na przykład Discord jest oficjalnym pakietem zewnętrznym:

bashCopy code
[code]
    openclaw plugins install @openclaw/discordopenclaw gateway restartopenclaw plugins inspect discord --runtime --json
[/code]

Surowe specyfikacje pakietów najpierw próbują ClawHub, a potem zapasowo npm. Aby wymusić źródło, użyj `clawhub:@openclaw/discord` lub `npm:@openclaw/discord`. Po instalacji postępuj zgodnie z dokumentacją konfiguracji Plugin, taką jak [Discord](</pl/channels/discord>), aby dodać dane uwierzytelniające i konfigurację kanału. Zobacz [Zarządzaj Pluginami](</pl/plugins/manage-plugins>), aby poznać polecenia aktualizacji, odinstalowania i publikowania.

## Główny pakiet npm

Plugin | Opis | Dystrybucja | Powierzchnia  
---|---|---|---  
[alibaba](</pl/plugins/reference/alibaba>) | Dodaje obsługę dostawcy generowania wideo. | `@openclaw/alibaba-provider` |   
zawarte w OpenClaw | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</pl/plugins/reference/amazon-bedrock>) | Dodaje do OpenClaw obsługę dostawcy modeli Amazon Bedrock. | `@openclaw/amazon-bedrock-provider` |   
zawarte w OpenClaw | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</pl/plugins/reference/amazon-bedrock-mantle>) | Dodaje do OpenClaw obsługę dostawcy modeli Amazon Bedrock Mantle. | `@openclaw/amazon-bedrock-mantle-provider` |   
zawarte w OpenClaw | providers: amazon-bedrock-mantle |  |   
[anthropic](</pl/plugins/reference/anthropic>) | Dodaje do OpenClaw obsługę dostawcy modeli Anthropic. | `@openclaw/anthropic-provider` |   
zawarte w OpenClaw | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</pl/plugins/reference/anthropic-vertex>) | Dodaje do OpenClaw obsługę dostawcy modeli Anthropic Vertex. | `@openclaw/anthropic-vertex-provider` |   
zawarte w OpenClaw | providers: anthropic-vertex |  |   
[arcee](</pl/plugins/reference/arcee>) | Dodaje do OpenClaw obsługę dostawcy modeli Arcee. | `@openclaw/arcee-provider` |   
zawarte w OpenClaw | providers: arcee |  |   
[azure-speech](</pl/plugins/reference/azure-speech>) | Azure AI Speech text-to-speech (MP3, natywne notatki głosowe Ogg/Opus, telefonia PCM). | `@openclaw/azure-speech` |   
zawarte w OpenClaw | contracts: speechProviders |  |   
[bonjour](</pl/plugins/reference/bonjour>) | Rozgłasza lokalny Gateway OpenClaw przez Bonjour/mDNS. | `@openclaw/bonjour` |   
zawarte w OpenClaw | plugin |  |   
[browser](</pl/plugins/reference/browser>) | Dodaje narzędzia wywoływane przez agenta. | `@openclaw/browser-plugin` |   
zawarte w OpenClaw | contracts: tools; skills |  |   
[byteplus](</pl/plugins/reference/byteplus>) | Dodaje do OpenClaw obsługę dostawców modeli BytePlus i BytePlus Plan. | `@openclaw/byteplus-provider` |   
zawarte w OpenClaw | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</pl/plugins/reference/canvas>) | Eksperymentalne powierzchnie sterowania Canvas i renderowania A2UI dla sparowanych węzłów. | `@openclaw/canvas-plugin` |   
zawarte w OpenClaw | contracts: tools |  |   
[cerebras](</pl/plugins/reference/cerebras>) | Dodaje do OpenClaw obsługę dostawcy modeli Cerebras. | `@openclaw/cerebras-provider` |   
zawarte w OpenClaw | providers: cerebras |  |   
[chutes](</pl/plugins/reference/chutes>) | Dodaje do OpenClaw obsługę dostawcy modeli Chutes. | `@openclaw/chutes-provider` |   
zawarte w OpenClaw | providers: chutes |  |   
[clickclack](</pl/plugins/reference/clickclack>) | Dodaje powierzchnię kanału Clickclack do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/clickclack` |   
zawarte w OpenClaw | channels: clickclack |  |   
[cloudflare-ai-gateway](</pl/plugins/reference/cloudflare-ai-gateway>) | Dodaje do OpenClaw obsługę dostawcy modeli Cloudflare AI Gateway. | `@openclaw/cloudflare-ai-gateway-provider` |   
zawarte w OpenClaw | providers: cloudflare-ai-gateway |  |   
[comfy](</pl/plugins/reference/comfy>) | Dodaje do OpenClaw obsługę dostawcy modeli ComfyUI. | `@openclaw/comfy-provider` |   
zawarte w OpenClaw | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</pl/plugins/reference/copilot-proxy>) | Dodaje do OpenClaw obsługę dostawcy modeli Copilot Proxy. | `@openclaw/copilot-proxy` |   
zawarte w OpenClaw | providers: copilot-proxy |  |   
[deepgram](</pl/plugins/reference/deepgram>) | Dodaje obsługę dostawcy rozumienia multimediów. Dodaje obsługę dostawcy transkrypcji w czasie rzeczywistym. | `@openclaw/deepgram-provider` |   
zawarte w OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</pl/plugins/reference/deepinfra>) | Dodaje do OpenClaw obsługę dostawcy modeli DeepInfra. | `@openclaw/deepinfra-provider` |   
zawarte w OpenClaw | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</pl/plugins/reference/deepseek>) | Dodaje obsługę dostawcy modeli DeepSeek do OpenClaw. | `@openclaw/deepseek-provider` |   
zawarte w OpenClaw | providers: deepseek |  |   
[document-extract](</pl/plugins/reference/document-extract>) | Wyodrębnia tekst i zapasowe obrazy stron z lokalnych załączników dokumentów. | `@openclaw/document-extract-plugin` |   
zawarte w OpenClaw | contracts: documentExtractors |  |   
[duckduckgo](</pl/plugins/reference/duckduckgo>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/duckduckgo-plugin` |   
zawarte w OpenClaw | contracts: webSearchProviders |  |   
[elevenlabs](</pl/plugins/reference/elevenlabs>) | Dodaje obsługę dostawcy rozumienia multimediów. Dodaje obsługę dostawcy transkrypcji w czasie rzeczywistym. Dodaje obsługę dostawcy zamiany tekstu na mowę. | `@openclaw/elevenlabs-speech` |   
zawarte w OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</pl/plugins/reference/exa>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/exa-plugin` |   
zawarte w OpenClaw | contracts: webSearchProviders |  |   
[fal](</pl/plugins/reference/fal>) | Dodaje obsługę dostawcy modeli fal do OpenClaw. | `@openclaw/fal-provider` |   
zawarte w OpenClaw | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[file-transfer](</pl/plugins/reference/file-transfer>) | Pobiera, wyświetla listę i zapisuje pliki na sparowanych węzłach za pomocą dedykowanych poleceń węzła. Omija obcinanie stdout przez bash, używając base64 przez node.invoke dla plików binarnych do 16 MB. | `@openclaw/file-transfer` |   
zawarte w OpenClaw | contracts: tools |  |   
[firecrawl](</pl/plugins/reference/firecrawl>) | Dodaje narzędzia wywoływane przez agenta. Dodaje obsługę dostawcy pobierania treści z sieci. Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/firecrawl-plugin` |   
zawarte w OpenClaw | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</pl/plugins/reference/fireworks>) | Dodaje obsługę dostawcy modeli Fireworks do OpenClaw. | `@openclaw/fireworks-provider` |   
zawarte w OpenClaw | providers: fireworks |  |   
[github-copilot](</pl/plugins/reference/github-copilot>) | Dodaje obsługę dostawcy modeli GitHub Copilot do OpenClaw. | `@openclaw/github-copilot-provider` |   
zawarte w OpenClaw | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</pl/plugins/reference/google>) | Dodaje obsługę dostawców modeli Google, Google Gemini CLI i Google Vertex do OpenClaw. | `@openclaw/google-plugin` |   
zawarte w OpenClaw | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[gradium](</pl/plugins/reference/gradium>) | Dodaje obsługę dostawcy zamiany tekstu na mowę. | `@openclaw/gradium-speech` |   
zawarte w OpenClaw | contracts: speechProviders |  |   
[groq](</pl/plugins/reference/groq>) | Dodaje obsługę dostawcy modeli Groq do OpenClaw. | `@openclaw/groq-provider` |   
zawarte w OpenClaw | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</pl/plugins/reference/huggingface>) | Dodaje obsługę dostawcy modeli Hugging Face do OpenClaw. | `@openclaw/huggingface-provider` |   
zawarte w OpenClaw | providers: huggingface |  |   
[imessage](</pl/plugins/reference/imessage>) | Dodaje powierzchnię kanału iMessage do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/imessage` |   
zawarte w OpenClaw | channels: imessage |  |   
[inworld](</pl/plugins/reference/inworld>) | Strumieniowa zamiana tekstu na mowę Inworld (MP3, OGG_OPUS, PCM dla telefonii). | `@openclaw/inworld-speech` |   
zawarte w OpenClaw | contracts: speechProviders |  |   
[irc](</pl/plugins/reference/irc>) | Dodaje powierzchnię kanału IRC do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/irc` |   
zawarte w OpenClaw | channels: irc |  |   
[kilocode](</pl/plugins/reference/kilocode>) | Dodaje obsługę dostawcy modeli Kilocode do OpenClaw. | `@openclaw/kilocode-provider` |   
zawarte w OpenClaw | providers: kilocode |  |   
[kimi](</pl/plugins/reference/kimi>) | Dodaje obsługę dostawców modeli Kimi i Kimi Coding do OpenClaw. | `@openclaw/kimi-provider` |   
zawarte w OpenClaw | providers: kimi, kimi-coding |  |   
[litellm](</pl/plugins/reference/litellm>) | Dodaje obsługę dostawcy modeli LiteLLM do OpenClaw. | `@openclaw/litellm-provider` |   
zawarte w OpenClaw | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</pl/plugins/reference/llm-task>) | Ogólne narzędzie LLM wyłącznie JSON do ustrukturyzowanych zadań, wywoływane z przepływów pracy. | `@openclaw/llm-task` |   
zawarte w OpenClaw | contracts: tools |  |   
[lmstudio](</pl/plugins/reference/lmstudio>) | Dodaje obsługę dostawcy modeli LM Studio do OpenClaw. | `@openclaw/lmstudio-provider` |   
zawarty w OpenClaw | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[mattermost](</pl/plugins/reference/mattermost>) | Dodaje powierzchnię kanału Mattermost do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/mattermost` |   
zawarty w OpenClaw | channels: mattermost |  |   
[memory-core](</pl/plugins/reference/memory-core>) | Dodaje obsługę dostawcy osadzeń pamięci. Dodaje narzędzia wywoływalne przez agenta. | `@openclaw/memory-core` |   
zawarty w OpenClaw | contracts: memoryEmbeddingProviders, tools |  |   
[memory-wiki](</pl/plugins/reference/memory-wiki>) | Trwały kompilator wiki oraz zgodny z Obsidianem magazyn wiedzy dla OpenClaw. | `@openclaw/memory-wiki` |   
zawarty w OpenClaw | contracts: tools; skills |  |   
[microsoft](</pl/plugins/reference/microsoft>) | Dodaje obsługę dostawcy zamiany tekstu na mowę. | `@openclaw/microsoft-speech` |   
zawarty w OpenClaw | contracts: speechProviders |  |   
[microsoft-foundry](</pl/plugins/reference/microsoft-foundry>) | Dodaje obsługę dostawcy modeli Microsoft Foundry do OpenClaw. | `@openclaw/microsoft-foundry` |   
zawarty w OpenClaw | providers: microsoft-foundry |  |   
[migrate-claude](</pl/plugins/reference/migrate-claude>) | Importuje instrukcje Claude Code i Claude Desktop, serwery MCP, umiejętności oraz bezpieczną konfigurację do OpenClaw. | `@openclaw/migrate-claude` |   
zawarty w OpenClaw | contracts: migrationProviders |  |   
[migrate-hermes](</pl/plugins/reference/migrate-hermes>) | Importuje konfigurację Hermes, pamięci, umiejętności i obsługiwane dane uwierzytelniające do OpenClaw. | `@openclaw/migrate-hermes` |   
zawarty w OpenClaw | contracts: migrationProviders |  |   
[minimax](</pl/plugins/reference/minimax>) | Dodaje obsługę dostawców modeli MiniMax i MiniMax Portal do OpenClaw. | `@openclaw/minimax-provider` |   
zawarty w OpenClaw | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</pl/plugins/reference/mistral>) | Dodaje obsługę dostawcy modeli Mistral do OpenClaw. | `@openclaw/mistral-provider` |   
zawarty w OpenClaw | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</pl/plugins/reference/moonshot>) | Dodaje obsługę dostawcy modeli Moonshot do OpenClaw. | `@openclaw/moonshot-provider` |   
zawarty w OpenClaw | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[nvidia](</pl/plugins/reference/nvidia>) | Dodaje obsługę dostawcy modeli NVIDIA do OpenClaw. | `@openclaw/nvidia-provider` |   
zawarty w OpenClaw | providers: nvidia |  |   
[oc-path](</pl/plugins/reference/oc-path>) | Dodaje CLI ścieżek openclaw do adresowania plików obszaru roboczego `oc://`. | `@openclaw/oc-path` |   
zawarty w OpenClaw | plugin |  |   
[ollama](</pl/plugins/reference/ollama>) | Dodaje obsługę dostawcy modeli Ollama do OpenClaw. | `@openclaw/ollama-provider` |   
zawarty w OpenClaw | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</pl/plugins/reference/open-prose>) | Pakiet Skills OpenProse VM z poleceniem ukośnikowym `/prose`. | `@openclaw/open-prose` |   
zawarty w OpenClaw | skills |  |   
[openai](</pl/plugins/reference/openai>) | Dodaje obsługę dostawców modeli OpenAI i OpenAI Codex do OpenClaw. | `@openclaw/openai-provider` |   
zawarty w OpenClaw | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</pl/plugins/reference/opencode>) | Dodaje obsługę dostawcy modeli OpenCode do OpenClaw. | `@openclaw/opencode-provider` |   
zawarty w OpenClaw | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</pl/plugins/reference/opencode-go>) | Dodaje obsługę dostawcy modeli OpenCode Go do OpenClaw. | `@openclaw/opencode-go-provider` |   
zawarty w OpenClaw | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</pl/plugins/reference/openrouter>) | Dodaje obsługę dostawcy modeli OpenRouter do OpenClaw. | `@openclaw/openrouter-provider` |   
zawarty w OpenClaw | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</pl/plugins/reference/openshell>) | Backend piaskownicy oparty na OpenShell z lustrzanymi lokalnymi obszarami roboczymi i wykonywaniem poleceń przez SSH. | `@openclaw/openshell-sandbox` |   
zawarty w OpenClaw | plugin |  |   
[perplexity](</pl/plugins/reference/perplexity>) | Dodaje obsługę dostawcy wyszukiwania w internecie. | `@openclaw/perplexity-plugin` |   
zawarty w OpenClaw | contracts: webSearchProviders |  |   
[qianfan](</pl/plugins/reference/qianfan>) | Dodaje obsługę dostawcy modeli Qianfan do OpenClaw. | `@openclaw/qianfan-provider` |   
dołączony do OpenClaw | providers: qianfan |  |   
[qwen](</pl/plugins/reference/qwen>) | Dodaje obsługę dostawców modeli Qwen, Qwen Cloud, Model Studio i DashScope do OpenClaw. | `@openclaw/qwen-provider` |   
dołączony do OpenClaw | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</pl/plugins/reference/runway>) | Dodaje obsługę dostawcy generowania wideo. | `@openclaw/runway-provider` |   
dołączony do OpenClaw | contracts: videoGenerationProviders |  |   
[searxng](</pl/plugins/reference/searxng>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/searxng-plugin` |   
dołączony do OpenClaw | contracts: webSearchProviders |  |   
[senseaudio](</pl/plugins/reference/senseaudio>) | Dodaje obsługę dostawcy rozumienia multimediów. | `@openclaw/senseaudio-provider` |   
dołączony do OpenClaw | contracts: mediaUnderstandingProviders |  |   
[sglang](</pl/plugins/reference/sglang>) | Dodaje obsługę dostawcy modeli SGLang do OpenClaw. | `@openclaw/sglang-provider` |   
dołączony do OpenClaw | providers: sglang |  |   
[signal](</pl/plugins/reference/signal>) | Dodaje powierzchnię kanału Signal do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/signal` |   
dołączony do OpenClaw | channels: signal |  |   
[skill-workshop](</pl/plugins/reference/skill-workshop>) | Ujmuje powtarzalne przepływy pracy jako Skills obszaru roboczego, z oczekującym przeglądem, bezpiecznymi zapisami i odświeżaniem promptu Skills. | `@openclaw/skill-workshop` |   
dołączony do OpenClaw | contracts: tools |  |   
[slack](</pl/plugins/reference/slack>) | Dodaje powierzchnię kanału Slack do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/slack` |   
dołączony do OpenClaw | channels: slack |  |   
[stepfun](</pl/plugins/reference/stepfun>) | Dodaje obsługę dostawców modeli StepFun i StepFun Plan do OpenClaw. | `@openclaw/stepfun-provider` |   
dołączony do OpenClaw | providers: stepfun, stepfun-plan |  |   
[synthetic](</pl/plugins/reference/synthetic>) | Dodaje obsługę dostawcy modeli Synthetic do OpenClaw. | `@openclaw/synthetic-provider` |   
dołączony do OpenClaw | providers: synthetic |  |   
[tavily](</pl/plugins/reference/tavily>) | Dodaje narzędzia wywoływalne przez agenta. Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/tavily-plugin` |   
dołączony do OpenClaw | contracts: tools, webSearchProviders; skills |  |   
[telegram](</pl/plugins/reference/telegram>) | Dodaje powierzchnię kanału Telegram do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/telegram` |   
dołączony do OpenClaw | channels: telegram |  |   
[tencent](</pl/plugins/reference/tencent>) | Dodaje obsługę dostawcy modeli Tencent TokenHub do OpenClaw. | `@openclaw/tencent-provider` |   
dołączony do OpenClaw | providers: tencent-tokenhub |  |   
[together](</pl/plugins/reference/together>) | Dodaje obsługę dostawcy modeli Together do OpenClaw. | `@openclaw/together-provider` |   
dołączony do OpenClaw | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</pl/plugins/reference/tokenjuice>) | Kompaktuje wyniki narzędzi exec i bash za pomocą reduktorów tokenjuice. | `@openclaw/tokenjuice` |   
dołączony do OpenClaw | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</pl/plugins/reference/tts-local-cli>) | Dodaje obsługę dostawcy syntezy mowy. | `@openclaw/tts-local-cli` |   
dołączony do OpenClaw | contracts: speechProviders |  |   
[venice](</pl/plugins/reference/venice>) | Dodaje obsługę dostawcy modeli Venice do OpenClaw. | `@openclaw/venice-provider` |   
dołączony do OpenClaw | providers: venice |  |   
[vercel-ai-gateway](</pl/plugins/reference/vercel-ai-gateway>) | Dodaje obsługę dostawcy modeli Vercel AI Gateway do OpenClaw. | `@openclaw/vercel-ai-gateway-provider` |   
dołączony do OpenClaw | providers: vercel-ai-gateway |  |   
[vllm](</pl/plugins/reference/vllm>) | Dodaje obsługę dostawcy modeli vLLM do OpenClaw. | `@openclaw/vllm-provider` |   
dołączony do OpenClaw | providers: vllm |  |   
[volcengine](</pl/plugins/reference/volcengine>) | Dodaje obsługę dostawców modeli Volcengine i Volcengine Plan do OpenClaw. | `@openclaw/volcengine-provider` |   
dołączony do OpenClaw | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</pl/plugins/reference/voyage>) | Dodaje obsługę dostawcy osadzania pamięci. | `@openclaw/voyage-provider` |   
zawarte w OpenClaw | contracts: memoryEmbeddingProviders |  |   
[vydra](</pl/plugins/reference/vydra>) | Dodaje do OpenClaw obsługę dostawcy modeli Vydra. | `@openclaw/vydra-provider` |   
zawarte w OpenClaw | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</pl/plugins/reference/web-readability>) | Wyodrębnia czytelną treść artykułu z lokalnych odpowiedzi pobierania stron internetowych w formacie HTML. | `@openclaw/web-readability-plugin` |   
zawarte w OpenClaw | contracts: webContentExtractors |  |   
[webhooks](</pl/plugins/reference/webhooks>) | Uwierzytelnione przychodzące Webhook, które wiążą zewnętrzną automatyzację z TaskFlow OpenClaw. | `@openclaw/webhooks` |   
zawarte w OpenClaw | plugin |  |   
[xai](</pl/plugins/reference/xai>) | Dodaje do OpenClaw obsługę dostawcy modeli xAI. | `@openclaw/xai-plugin` |   
zawarte w OpenClaw | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</pl/plugins/reference/xiaomi>) | Dodaje do OpenClaw obsługę dostawcy modeli Xiaomi. | `@openclaw/xiaomi-provider` |   
zawarte w OpenClaw | providers: xiaomi; contracts: speechProviders |  |   
[zai](</pl/plugins/reference/zai>) | Dodaje do OpenClaw obsługę dostawcy modeli [Z.AI](<http://Z.AI>). | `@openclaw/zai-provider` |   
zawarte w OpenClaw | providers: zai; contracts: mediaUnderstandingProviders |  |   
  
## Oficjalne pakiety zewnętrzne

Plugin | Opis | Dystrybucja | Powierzchnia  
---|---|---|---  
[acpx](</pl/plugins/reference/acpx>) | Osadzony backend środowiska uruchomieniowego ACP z zarządzaniem sesją i transportem po stronie pluginu. | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[brave](</pl/plugins/reference/brave>) | Dodaje obsługę dostawcy wyszukiwania w sieci. | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[codex](</pl/plugins/reference/codex>) | Uprząż serwera aplikacji Codex oraz zarządzany przez Codex katalog modeli GPT. | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[diagnostics-otel](</pl/plugins/reference/diagnostics-otel>) | Eksporter diagnostyki OpenClaw OpenTelemetry. | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</pl/plugins/reference/diagnostics-prometheus>) | Eksporter diagnostyki OpenClaw Prometheus. | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</pl/plugins/reference/diffs>) | Przeglądarka różnic tylko do odczytu i renderer plików dla agentów. | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</pl/plugins/reference/discord>) | Dodaje powierzchnię kanału Discord do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[feishu](</pl/plugins/reference/feishu>) | Dodaje powierzchnię kanału Feishu do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[google-meet](</pl/plugins/reference/google-meet>) | Dołączanie do rozmów Google Meet przez transporty Chrome lub Twilio. | `@openclaw/google-meet` |   
npm; ClawHub | contracts: tools |  |   
[googlechat](</pl/plugins/reference/googlechat>) | Dodaje powierzchnię kanału Google Chat do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/googlechat` |   
npm; ClawHub | channels: googlechat |  |   
[line](</pl/plugins/reference/line>) | Dodaje powierzchnię kanału LINE do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/line` |   
npm; ClawHub | channels: line |  |   
[lobster](</pl/plugins/reference/lobster>) | Typowane narzędzie przepływu pracy z wznawialnymi zatwierdzeniami. | `@openclaw/lobster` |   
npm; ClawHub | contracts: tools |  |   
[matrix](</pl/plugins/reference/matrix>) | Dodaje powierzchnię kanału Matrix do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | channels: matrix |  |   
[memory-lancedb](</pl/plugins/reference/memory-lancedb>) | Dodaje narzędzia wywoływalne przez agenta. | `@openclaw/memory-lancedb` |   
npm; ClawHub | contracts: tools |  |   
[msteams](</pl/plugins/reference/msteams>) | Dodaje powierzchnię kanału Microsoft Teams do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</pl/plugins/reference/nextcloud-talk>) | Dodaje powierzchnię kanału Nextcloud Talk do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</pl/plugins/reference/nostr>) | Dodaje powierzchnię kanału Nostr do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[qqbot](</pl/plugins/reference/qqbot>) | Dodaje powierzchnię kanału QQ Bot do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[synology-chat](</pl/plugins/reference/synology-chat>) | Dodaje powierzchnię kanału Synology Chat do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[tlon](</pl/plugins/reference/tlon>) | Dodaje powierzchnię kanału Tlon do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[twitch](</pl/plugins/reference/twitch>) | Dodaje powierzchnię kanału Twitch do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[voice-call](</pl/plugins/reference/voice-call>) | Dodaje narzędzia wywoływalne przez agenta. | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[whatsapp](</pl/plugins/reference/whatsapp>) | Dodaje powierzchnię kanału WhatsApp do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[zalo](</pl/plugins/reference/zalo>) | Dodaje powierzchnię kanału Zalo do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</pl/plugins/reference/zalouser>) | Dodaje powierzchnię kanału Zalo Personal do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
## Tylko checkout źródła

Plugin | Opis | Dystrybucja | Powierzchnia  
---|---|---|---  
[qa-channel](</pl/plugins/reference/qa-channel>) | Dodaje powierzchnię kanału QA Channel do wysyłania i odbierania wiadomości OpenClaw. | `@openclaw/qa-channel` |   
tylko checkout źródła | channels: qa-channel |  |   
[qa-lab](</pl/plugins/reference/qa-lab>) | Plugin laboratorium QA OpenClaw z prywatnym interfejsem debuggera i runnerem scenariuszy. | `@openclaw/qa-lab` |   
tylko checkout źródła | plugin |  |   
[qa-matrix](</pl/plugins/reference/qa-matrix>) | Runner i substrat transportu Matrix QA. | `@openclaw/qa-matrix` |   
tylko checkout źródła | plugin |  |   
  
Was this useful?YesNo