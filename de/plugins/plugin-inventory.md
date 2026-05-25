---
title: Plugin-Inventar
source_url: https://docs.openclaw.ai/de/plugins/plugin-inventory
scraped_at: 2026-05-25
---

# Plugin-Bestand

Diese Seite wird aus `extensions/*/package.json`, `openclaw.plugin.json` und den `files`-Ausschlüssen des Root-npm-Pakets generiert. Generieren Sie sie neu mit:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

## Definitionen

  * **Kern-npm-Paket:** in das npm-Paket `openclaw` integriert und ohne separate Plugin-Installation verfügbar.
  * **Offizielles externes Paket:** von OpenClaw gepflegtes Plugin, das nicht im Kern-npm-Paket enthalten ist, in diesem offiziellen Bestand geführt wird und bei Bedarf über ClawHub und/oder npm installiert wird.
  * **Nur Source-Checkout:** repo-lokales Plugin, das nicht in veröffentlichten npm-Artefakten enthalten ist und nicht als installierbares Paket beworben wird.


Source-Checkouts unterscheiden sich von npm-Installationen: Nach `pnpm install` werden gebündelte Plugins aus `extensions/<id>` geladen, sodass lokale Änderungen und paketlokale Workspace- Abhängigkeiten verfügbar sind.

## Plugin installieren

Verwenden Sie die Spalte **Distribution** , um zu entscheiden, ob eine Installation erforderlich ist. Plugins, bei denen `included in OpenClaw` steht, sind bereits im Kernpaket vorhanden. Offizielle externe Pakete benötigen eine Installation und anschließend einen Gateway-Neustart.

Beispiel: Discord ist ein offizielles externes Paket:

bashCopy code
[code]
    openclaw plugins install @openclaw/discordopenclaw gateway restartopenclaw plugins inspect discord --runtime --json
[/code]

Paketangaben ohne Präfix versuchen zuerst ClawHub und dann npm als Fallback. Um eine Quelle zu erzwingen, verwenden Sie `clawhub:@openclaw/discord` oder `npm:@openclaw/discord`. Folgen Sie nach der Installation der Einrichtungsdokumentation des Plugins, z. B. [Discord](</de/channels/discord>), um Zugangsdaten und Channel-Konfiguration hinzuzufügen. Siehe [Plugins verwalten](</de/plugins/manage-plugins>) für Befehle zum Aktualisieren, Deinstallieren und Veröffentlichen.

## Kern-npm-Paket

Plugin | Beschreibung | Distribution | Oberfläche  
---|---|---|---  
[alibaba](</de/plugins/reference/alibaba>) | Fügt Unterstützung für Videoerzeugungs-Provider hinzu. | `@openclaw/alibaba-provider` |   
in OpenClaw enthalten | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</de/plugins/reference/amazon-bedrock>) | Fügt OpenClaw Unterstützung für Amazon Bedrock-Modell-Provider hinzu. | `@openclaw/amazon-bedrock-provider` |   
in OpenClaw enthalten | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</de/plugins/reference/amazon-bedrock-mantle>) | Fügt OpenClaw Unterstützung für Amazon Bedrock Mantle-Modell-Provider hinzu. | `@openclaw/amazon-bedrock-mantle-provider` |   
in OpenClaw enthalten | providers: amazon-bedrock-mantle |  |   
[anthropic](</de/plugins/reference/anthropic>) | Fügt OpenClaw Unterstützung für Anthropic-Modell-Provider hinzu. | `@openclaw/anthropic-provider` |   
in OpenClaw enthalten | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</de/plugins/reference/anthropic-vertex>) | Fügt OpenClaw Unterstützung für Anthropic Vertex-Modell-Provider hinzu. | `@openclaw/anthropic-vertex-provider` |   
in OpenClaw enthalten | providers: anthropic-vertex |  |   
[arcee](</de/plugins/reference/arcee>) | Fügt OpenClaw Unterstützung für Arcee-Modell-Provider hinzu. | `@openclaw/arcee-provider` |   
in OpenClaw enthalten | providers: arcee |  |   
[azure-speech](</de/plugins/reference/azure-speech>) | Azure AI Speech-Text-to-Speech (MP3, native Ogg/Opus-Sprachnachrichten, PCM-Telefonie). | `@openclaw/azure-speech` |   
in OpenClaw enthalten | contracts: speechProviders |  |   
[bonjour](</de/plugins/reference/bonjour>) | Gibt den lokalen OpenClaw-Gateway über Bonjour/mDNS bekannt. | `@openclaw/bonjour` |   
in OpenClaw enthalten | plugin |  |   
[browser](</de/plugins/reference/browser>) | Fügt vom Agenten aufrufbare Tools hinzu. | `@openclaw/browser-plugin` |   
in OpenClaw enthalten | contracts: tools; skills |  |   
[byteplus](</de/plugins/reference/byteplus>) | Fügt OpenClaw Unterstützung für BytePlus- und BytePlus Plan-Modell-Provider hinzu. | `@openclaw/byteplus-provider` |   
in OpenClaw enthalten | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</de/plugins/reference/canvas>) | Experimentelle Canvas-Steuerung und A2UI-Rendering-Oberflächen für gekoppelte Nodes. | `@openclaw/canvas-plugin` |   
in OpenClaw enthalten | contracts: tools |  |   
[cerebras](</de/plugins/reference/cerebras>) | Fügt OpenClaw Unterstützung für Cerebras-Modell-Provider hinzu. | `@openclaw/cerebras-provider` |   
in OpenClaw enthalten | providers: cerebras |  |   
[chutes](</de/plugins/reference/chutes>) | Fügt OpenClaw Unterstützung für Chutes-Modell-Provider hinzu. | `@openclaw/chutes-provider` |   
in OpenClaw enthalten | providers: chutes |  |   
[clickclack](</de/plugins/reference/clickclack>) | Fügt die Clickclack-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/clickclack` |   
in OpenClaw enthalten | channels: clickclack |  |   
[cloudflare-ai-gateway](</de/plugins/reference/cloudflare-ai-gateway>) | Fügt OpenClaw Unterstützung für Cloudflare AI Gateway-Modell-Provider hinzu. | `@openclaw/cloudflare-ai-gateway-provider` |   
in OpenClaw enthalten | providers: cloudflare-ai-gateway |  |   
[comfy](</de/plugins/reference/comfy>) | Fügt OpenClaw Unterstützung für ComfyUI-Modell-Provider hinzu. | `@openclaw/comfy-provider` |   
in OpenClaw enthalten | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</de/plugins/reference/copilot-proxy>) | Fügt OpenClaw Unterstützung für Copilot Proxy-Modell-Provider hinzu. | `@openclaw/copilot-proxy` |   
in OpenClaw enthalten | providers: copilot-proxy |  |   
[deepgram](</de/plugins/reference/deepgram>) | Fügt Unterstützung für Provider zur Medienerkennung hinzu. Fügt Unterstützung für Echtzeit-Transkriptions-Provider hinzu. | `@openclaw/deepgram-provider` |   
in OpenClaw enthalten | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</de/plugins/reference/deepinfra>) | Fügt OpenClaw Unterstützung für DeepInfra-Modell-Provider hinzu. | `@openclaw/deepinfra-provider` |   
in OpenClaw enthalten | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</de/plugins/reference/deepseek>) | Fügt OpenClaw Unterstützung für den DeepSeek-Modell-Provider hinzu. | `@openclaw/deepseek-provider` |   
in OpenClaw enthalten | providers: deepseek |  |   
[document-extract](</de/plugins/reference/document-extract>) | Extrahiert Text und Fallback-Seitenbilder aus lokalen Dokumentanhängen. | `@openclaw/document-extract-plugin` |   
in OpenClaw enthalten | contracts: documentExtractors |  |   
[duckduckgo](</de/plugins/reference/duckduckgo>) | Fügt Unterstützung für Websuche-Provider hinzu. | `@openclaw/duckduckgo-plugin` |   
in OpenClaw enthalten | contracts: webSearchProviders |  |   
[elevenlabs](</de/plugins/reference/elevenlabs>) | Fügt Unterstützung für Media-Understanding-Provider hinzu. Fügt Unterstützung für Echtzeit-Transkriptions-Provider hinzu. Fügt Unterstützung für Text-to-Speech-Provider hinzu. | `@openclaw/elevenlabs-speech` |   
in OpenClaw enthalten | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</de/plugins/reference/exa>) | Fügt Unterstützung für Websuche-Provider hinzu. | `@openclaw/exa-plugin` |   
in OpenClaw enthalten | contracts: webSearchProviders |  |   
[fal](</de/plugins/reference/fal>) | Fügt OpenClaw Unterstützung für den fal-Modell-Provider hinzu. | `@openclaw/fal-provider` |   
in OpenClaw enthalten | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[file-transfer](</de/plugins/reference/file-transfer>) | Ruft Dateien auf gekoppelten Nodes ab, listet sie auf und schreibt sie über dedizierte Node-Befehle. Umgeht die Kürzung von bash-stdout, indem base64 über node.invoke für Binärdateien bis zu 16 MB verwendet wird. | `@openclaw/file-transfer` |   
in OpenClaw enthalten | contracts: tools |  |   
[firecrawl](</de/plugins/reference/firecrawl>) | Fügt durch Agenten aufrufbare Tools hinzu. Fügt Unterstützung für Webabruf-Provider hinzu. Fügt Unterstützung für Websuche-Provider hinzu. | `@openclaw/firecrawl-plugin` |   
in OpenClaw enthalten | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</de/plugins/reference/fireworks>) | Fügt OpenClaw Unterstützung für den Fireworks-Modell-Provider hinzu. | `@openclaw/fireworks-provider` |   
in OpenClaw enthalten | providers: fireworks |  |   
[github-copilot](</de/plugins/reference/github-copilot>) | Fügt OpenClaw Unterstützung für den GitHub Copilot-Modell-Provider hinzu. | `@openclaw/github-copilot-provider` |   
in OpenClaw enthalten | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</de/plugins/reference/google>) | Fügt OpenClaw Unterstützung für die Modell-Provider Google, Google Gemini CLI und Google Vertex hinzu. | `@openclaw/google-plugin` |   
in OpenClaw enthalten | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[gradium](</de/plugins/reference/gradium>) | Fügt Unterstützung für Text-to-Speech-Provider hinzu. | `@openclaw/gradium-speech` |   
in OpenClaw enthalten | contracts: speechProviders |  |   
[groq](</de/plugins/reference/groq>) | Fügt OpenClaw Unterstützung für den Groq-Modell-Provider hinzu. | `@openclaw/groq-provider` |   
in OpenClaw enthalten | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</de/plugins/reference/huggingface>) | Fügt OpenClaw Unterstützung für den Hugging Face-Modell-Provider hinzu. | `@openclaw/huggingface-provider` |   
in OpenClaw enthalten | providers: huggingface |  |   
[imessage](</de/plugins/reference/imessage>) | Fügt die iMessage-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/imessage` |   
in OpenClaw enthalten | channels: imessage |  |   
[inworld](</de/plugins/reference/inworld>) | Inworld-Streaming-Text-to-Speech (MP3, OGG_OPUS, PCM-Telefonie). | `@openclaw/inworld-speech` |   
in OpenClaw enthalten | contracts: speechProviders |  |   
[irc](</de/plugins/reference/irc>) | Fügt die IRC-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/irc` |   
in OpenClaw enthalten | channels: irc |  |   
[kilocode](</de/plugins/reference/kilocode>) | Fügt OpenClaw Unterstützung für den Kilocode-Modell-Provider hinzu. | `@openclaw/kilocode-provider` |   
in OpenClaw enthalten | providers: kilocode |  |   
[kimi](</de/plugins/reference/kimi>) | Fügt OpenClaw Unterstützung für die Modell-Provider Kimi und Kimi Coding hinzu. | `@openclaw/kimi-provider` |   
in OpenClaw enthalten | providers: kimi, kimi-coding |  |   
[litellm](</de/plugins/reference/litellm>) | Fügt OpenClaw Unterstützung für den LiteLLM-Modell-Provider hinzu. | `@openclaw/litellm-provider` |   
in OpenClaw enthalten | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</de/plugins/reference/llm-task>) | Generisches reines JSON-LLM-Tool für strukturierte Aufgaben, das aus Workflows aufgerufen werden kann. | `@openclaw/llm-task` |   
in OpenClaw enthalten | contracts: tools |  |   
[lmstudio](</de/plugins/reference/lmstudio>) | Fügt OpenClaw Unterstützung für den LM Studio Model Provider hinzu. | `@openclaw/lmstudio-provider` |   
in OpenClaw enthalten | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[mattermost](</de/plugins/reference/mattermost>) | Fügt die Mattermost-Channel-Oberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/mattermost` |   
in OpenClaw enthalten | channels: mattermost |  |   
[memory-core](</de/plugins/reference/memory-core>) | Fügt Unterstützung für Memory-Embedding-Provider hinzu. Fügt Tools hinzu, die Agenten aufrufen können. | `@openclaw/memory-core` |   
in OpenClaw enthalten | contracts: memoryEmbeddingProviders, tools |  |   
[memory-wiki](</de/plugins/reference/memory-wiki>) | Persistenter Wiki-Compiler und Obsidian-freundlicher Wissens-Vault für OpenClaw. | `@openclaw/memory-wiki` |   
in OpenClaw enthalten | contracts: tools; skills |  |   
[microsoft](</de/plugins/reference/microsoft>) | Fügt Unterstützung für Text-to-Speech-Provider hinzu. | `@openclaw/microsoft-speech` |   
in OpenClaw enthalten | contracts: speechProviders |  |   
[microsoft-foundry](</de/plugins/reference/microsoft-foundry>) | Fügt OpenClaw Unterstützung für den Microsoft Foundry Model Provider hinzu. | `@openclaw/microsoft-foundry` |   
in OpenClaw enthalten | providers: microsoft-foundry |  |   
[migrate-claude](</de/plugins/reference/migrate-claude>) | Importiert Claude Code- und Claude Desktop-Anweisungen, MCP-Server, Skills und sichere Konfiguration in OpenClaw. | `@openclaw/migrate-claude` |   
in OpenClaw enthalten | contracts: migrationProviders |  |   
[migrate-hermes](</de/plugins/reference/migrate-hermes>) | Importiert Hermes-Konfiguration, Memories, Skills und unterstützte Anmeldedaten in OpenClaw. | `@openclaw/migrate-hermes` |   
in OpenClaw enthalten | contracts: migrationProviders |  |   
[minimax](</de/plugins/reference/minimax>) | Fügt OpenClaw Unterstützung für die MiniMax- und MiniMax Portal Model Provider hinzu. | `@openclaw/minimax-provider` |   
in OpenClaw enthalten | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</de/plugins/reference/mistral>) | Fügt OpenClaw Unterstützung für den Mistral Model Provider hinzu. | `@openclaw/mistral-provider` |   
in OpenClaw enthalten | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</de/plugins/reference/moonshot>) | Fügt OpenClaw Unterstützung für den Moonshot Model Provider hinzu. | `@openclaw/moonshot-provider` |   
in OpenClaw enthalten | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[nvidia](</de/plugins/reference/nvidia>) | Fügt OpenClaw Unterstützung für den NVIDIA Model Provider hinzu. | `@openclaw/nvidia-provider` |   
in OpenClaw enthalten | providers: nvidia |  |   
[oc-path](</de/plugins/reference/oc-path>) | Fügt die openclaw path CLI für die oc://-Adressierung von Workspace-Dateien hinzu. | `@openclaw/oc-path` |   
in OpenClaw enthalten | plugin |  |   
[ollama](</de/plugins/reference/ollama>) | Fügt OpenClaw Unterstützung für den Ollama Model Provider hinzu. | `@openclaw/ollama-provider` |   
in OpenClaw enthalten | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</de/plugins/reference/open-prose>) | OpenProse VM-Skill-Paket mit einem /prose-Slash-Command. | `@openclaw/open-prose` |   
in OpenClaw enthalten | skills |  |   
[openai](</de/plugins/reference/openai>) | Fügt OpenClaw Unterstützung für die OpenAI- und OpenAI Codex Model Provider hinzu. | `@openclaw/openai-provider` |   
in OpenClaw enthalten | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</de/plugins/reference/opencode>) | Fügt OpenClaw Unterstützung für den OpenCode Model Provider hinzu. | `@openclaw/opencode-provider` |   
in OpenClaw enthalten | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</de/plugins/reference/opencode-go>) | Fügt OpenClaw Unterstützung für den OpenCode Go Model Provider hinzu. | `@openclaw/opencode-go-provider` |   
in OpenClaw enthalten | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</de/plugins/reference/openrouter>) | Fügt OpenClaw Unterstützung für den OpenRouter Model Provider hinzu. | `@openclaw/openrouter-provider` |   
in OpenClaw enthalten | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</de/plugins/reference/openshell>) | Sandbox-Backend auf Basis von OpenShell mit gespiegelten lokalen Workspaces und SSH-basierter Befehlsausführung. | `@openclaw/openshell-sandbox` |   
in OpenClaw enthalten | plugin |  |   
[perplexity](</de/plugins/reference/perplexity>) | Fügt Unterstützung für Websuche-Provider hinzu. | `@openclaw/perplexity-plugin` |   
in OpenClaw enthalten | contracts: webSearchProviders |  |   
[qianfan](</de/plugins/reference/qianfan>) | Fügt OpenClaw Unterstützung für den Qianfan-Modell-Provider hinzu. | `@openclaw/qianfan-provider` |   
in OpenClaw enthalten | providers: qianfan |  |   
[qwen](</de/plugins/reference/qwen>) | Fügt OpenClaw Unterstützung für die Modell-Provider Qwen, Qwen Cloud, Model Studio und DashScope hinzu. | `@openclaw/qwen-provider` |   
in OpenClaw enthalten | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</de/plugins/reference/runway>) | Fügt Unterstützung für Videogenerierungs-Provider hinzu. | `@openclaw/runway-provider` |   
in OpenClaw enthalten | contracts: videoGenerationProviders |  |   
[searxng](</de/plugins/reference/searxng>) | Fügt Unterstützung für Websuch-Provider hinzu. | `@openclaw/searxng-plugin` |   
in OpenClaw enthalten | contracts: webSearchProviders |  |   
[senseaudio](</de/plugins/reference/senseaudio>) | Fügt Unterstützung für Medienverständnis-Provider hinzu. | `@openclaw/senseaudio-provider` |   
in OpenClaw enthalten | contracts: mediaUnderstandingProviders |  |   
[sglang](</de/plugins/reference/sglang>) | Fügt OpenClaw Unterstützung für den SGLang-Modell-Provider hinzu. | `@openclaw/sglang-provider` |   
in OpenClaw enthalten | providers: sglang |  |   
[signal](</de/plugins/reference/signal>) | Fügt die Signal-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/signal` |   
in OpenClaw enthalten | channels: signal |  |   
[skill-workshop](</de/plugins/reference/skill-workshop>) | Erfasst wiederholbare Workflows als Workspace-Skills, mit ausstehender Prüfung, sicheren Schreibvorgängen und Aktualisierung des Skill-Prompts. | `@openclaw/skill-workshop` |   
in OpenClaw enthalten | contracts: tools |  |   
[slack](</de/plugins/reference/slack>) | Fügt die Slack-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/slack` |   
in OpenClaw enthalten | channels: slack |  |   
[stepfun](</de/plugins/reference/stepfun>) | Fügt OpenClaw Unterstützung für die Modell-Provider StepFun und StepFun Plan hinzu. | `@openclaw/stepfun-provider` |   
in OpenClaw enthalten | providers: stepfun, stepfun-plan |  |   
[synthetic](</de/plugins/reference/synthetic>) | Fügt OpenClaw Unterstützung für den Synthetic-Modell-Provider hinzu. | `@openclaw/synthetic-provider` |   
in OpenClaw enthalten | providers: synthetic |  |   
[tavily](</de/plugins/reference/tavily>) | Fügt vom Agenten aufrufbare Tools hinzu. Fügt Unterstützung für Websuch-Provider hinzu. | `@openclaw/tavily-plugin` |   
in OpenClaw enthalten | contracts: tools, webSearchProviders; skills |  |   
[telegram](</de/plugins/reference/telegram>) | Fügt die Telegram-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/telegram` |   
in OpenClaw enthalten | channels: telegram |  |   
[tencent](</de/plugins/reference/tencent>) | Fügt OpenClaw Unterstützung für den Tencent TokenHub-Modell-Provider hinzu. | `@openclaw/tencent-provider` |   
in OpenClaw enthalten | providers: tencent-tokenhub |  |   
[together](</de/plugins/reference/together>) | Fügt OpenClaw Unterstützung für den Together-Modell-Provider hinzu. | `@openclaw/together-provider` |   
in OpenClaw enthalten | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</de/plugins/reference/tokenjuice>) | Komprimiert Ergebnisse der Tools `exec` und `bash` mit tokenjuice-Reducern. | `@openclaw/tokenjuice` |   
in OpenClaw enthalten | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</de/plugins/reference/tts-local-cli>) | Fügt Unterstützung für Text-to-Speech-Provider hinzu. | `@openclaw/tts-local-cli` |   
in OpenClaw enthalten | contracts: speechProviders |  |   
[venice](</de/plugins/reference/venice>) | Fügt OpenClaw Unterstützung für den Venice-Modell-Provider hinzu. | `@openclaw/venice-provider` |   
in OpenClaw enthalten | providers: venice |  |   
[vercel-ai-gateway](</de/plugins/reference/vercel-ai-gateway>) | Fügt OpenClaw Unterstützung für den Vercel AI Gateway-Modell-Provider hinzu. | `@openclaw/vercel-ai-gateway-provider` |   
in OpenClaw enthalten | providers: vercel-ai-gateway |  |   
[vllm](</de/plugins/reference/vllm>) | Fügt OpenClaw Unterstützung für den vLLM-Modell-Provider hinzu. | `@openclaw/vllm-provider` |   
in OpenClaw enthalten | providers: vllm |  |   
[volcengine](</de/plugins/reference/volcengine>) | Fügt OpenClaw Unterstützung für die Modell-Provider Volcengine und Volcengine Plan hinzu. | `@openclaw/volcengine-provider` |   
in OpenClaw enthalten | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</de/plugins/reference/voyage>) | Fügt Unterstützung für Memory-Embedding-Provider hinzu. | `@openclaw/voyage-provider` |   
in OpenClaw enthalten | contracts: memoryEmbeddingProviders |  |   
[vydra](</de/plugins/reference/vydra>) | Fügt OpenClaw Unterstützung für den Vydra-Modell-Provider hinzu. | `@openclaw/vydra-provider` |   
in OpenClaw enthalten | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</de/plugins/reference/web-readability>) | Extrahiert lesbaren Artikelinhalt aus lokalen HTML-Webabruf-Antworten. | `@openclaw/web-readability-plugin` |   
in OpenClaw enthalten | contracts: webContentExtractors |  |   
[webhooks](</de/plugins/reference/webhooks>) | Authentifizierte eingehende Webhooks, die externe Automatisierung an OpenClaw TaskFlows binden. | `@openclaw/webhooks` |   
in OpenClaw enthalten | plugin |  |   
[xai](</de/plugins/reference/xai>) | Fügt OpenClaw Unterstützung für den xAI-Modell-Provider hinzu. | `@openclaw/xai-plugin` |   
in OpenClaw enthalten | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</de/plugins/reference/xiaomi>) | Fügt OpenClaw Unterstützung für den Xiaomi-Modell-Provider hinzu. | `@openclaw/xiaomi-provider` |   
in OpenClaw enthalten | providers: xiaomi; contracts: speechProviders |  |   
[zai](</de/plugins/reference/zai>) | Fügt OpenClaw Unterstützung für den Z.AI-Modell-Provider hinzu. | `@openclaw/zai-provider` |   
in OpenClaw enthalten | providers: zai; contracts: mediaUnderstandingProviders |  |   
  
## Offizielle externe Pakete

Plugin | Beschreibung | Distribution | Oberfläche  
---|---|---|---  
[acpx](</de/plugins/reference/acpx>) | Eingebettetes ACP-Runtime-Backend mit Plugin-eigenem Sitzungs- und Transportmanagement. | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[brave](</de/plugins/reference/brave>) | Fügt Unterstützung für Websuche-Provider hinzu. | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[codex](</de/plugins/reference/codex>) | Codex-App-Server-Harness und von Codex verwalteter GPT-Modellkatalog. | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[diagnostics-otel](</de/plugins/reference/diagnostics-otel>) | OpenClaw-Diagnose-Exporter für OpenTelemetry. | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</de/plugins/reference/diagnostics-prometheus>) | OpenClaw-Diagnose-Exporter für Prometheus. | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</de/plugins/reference/diffs>) | Schreibgeschützter Diff-Viewer und Datei-Renderer für Agenten. | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</de/plugins/reference/discord>) | Fügt die Discord-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[feishu](</de/plugins/reference/feishu>) | Fügt die Feishu-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[google-meet](</de/plugins/reference/google-meet>) | An Google Meet-Anrufen über Chrome- oder Twilio-Transporte teilnehmen. | `@openclaw/google-meet` |   
npm; ClawHub | contracts: tools |  |   
[googlechat](</de/plugins/reference/googlechat>) | Fügt die Google Chat-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/googlechat` |   
npm; ClawHub | channels: googlechat |  |   
[line](</de/plugins/reference/line>) | Fügt die LINE-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/line` |   
npm; ClawHub | channels: line |  |   
[lobster](</de/plugins/reference/lobster>) | Typisiertes Workflow-Tool mit fortsetzbaren Genehmigungen. | `@openclaw/lobster` |   
npm; ClawHub | contracts: tools |  |   
[matrix](</de/plugins/reference/matrix>) | Fügt die Matrix-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | channels: matrix |  |   
[memory-lancedb](</de/plugins/reference/memory-lancedb>) | Fügt von Agenten aufrufbare Tools hinzu. | `@openclaw/memory-lancedb` |   
npm; ClawHub | contracts: tools |  |   
[msteams](</de/plugins/reference/msteams>) | Fügt die Microsoft Teams-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</de/plugins/reference/nextcloud-talk>) | Fügt die Nextcloud Talk-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</de/plugins/reference/nostr>) | Fügt die Nostr-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[qqbot](</de/plugins/reference/qqbot>) | Fügt die QQ Bot-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[synology-chat](</de/plugins/reference/synology-chat>) | Fügt die Synology Chat-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[tlon](</de/plugins/reference/tlon>) | Fügt die Tlon-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[twitch](</de/plugins/reference/twitch>) | Fügt die Twitch-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[voice-call](</de/plugins/reference/voice-call>) | Fügt von Agenten aufrufbare Tools hinzu. | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[whatsapp](</de/plugins/reference/whatsapp>) | Fügt die WhatsApp-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[zalo](</de/plugins/reference/zalo>) | Fügt die Zalo-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</de/plugins/reference/zalouser>) | Fügt die Zalo Personal-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
## Nur Source-Checkout

Plugin | Beschreibung | Distribution | Oberfläche  
---|---|---|---  
[qa-channel](</de/plugins/reference/qa-channel>) | Fügt die QA Channel-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu. | `@openclaw/qa-channel` |   
nur Source-Checkout | channels: qa-channel |  |   
[qa-lab](</de/plugins/reference/qa-lab>) | OpenClaw-QA-Lab-Plugin mit privater Debugger-UI und Szenario-Runner. | `@openclaw/qa-lab` |   
nur Source-Checkout | plugin |  |   
[qa-matrix](</de/plugins/reference/qa-matrix>) | Matrix-QA-Transport-Runner und Substrat. | `@openclaw/qa-matrix` |   
nur Source-Checkout | plugin |  |   
  
Was this useful?YesNo