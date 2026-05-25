---
title: Plugin-inventaris
source_url: https://docs.openclaw.ai/nl/plugins/plugin-inventory
scraped_at: 2026-05-25
---

# Plugin-inventaris

Deze pagina wordt gegenereerd op basis van `extensions/*/package.json`, `openclaw.plugin.json`, en de `files`-uitsluitingen van het root-npm-pakket. Genereer deze opnieuw met:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

## Definities

  * **Core npm-pakket:** ingebouwd in het `openclaw` npm-pakket en beschikbaar zonder een afzonderlijke Plugin-installatie.
  * **Officieel extern pakket:** door OpenClaw onderhouden Plugin die is weggelaten uit het core npm-pakket, in deze officiële inventaris wordt bijgehouden en op aanvraag wordt geïnstalleerd via ClawHub en/of npm.
  * **Alleen source-checkout:** repo-lokale Plugin die is weggelaten uit gepubliceerde npm-artefacten en niet wordt aangeboden als installeerbaar pakket.


Source-checkouts verschillen van npm-installaties: na `pnpm install` laden gebundelde Plugins vanuit `extensions/<id>`, zodat lokale bewerkingen en package-lokale workspace- dependencies beschikbaar zijn.

## Een Plugin installeren

Gebruik de kolom **Distributie** om te bepalen of installatie nodig is. Plugins die `included in OpenClaw` vermelden, zijn al aanwezig in het core-pakket. Officiële externe pakketten hebben één installatie nodig, gevolgd door een Gateway-herstart.

Discord is bijvoorbeeld een officieel extern pakket:

bashCopy code
[code]
    openclaw plugins install @openclaw/discordopenclaw gateway restartopenclaw plugins inspect discord --runtime --json
[/code]

Bare package-specs proberen eerst ClawHub en daarna npm als fallback. Gebruik `clawhub:@openclaw/discord` of `npm:@openclaw/discord` om een bron af te dwingen. Volg na installatie de setup-doc van de Plugin, zoals [Discord](</nl/channels/discord>), om credentials en kanaalconfiguratie toe te voegen. Zie [Plugins beheren](</nl/plugins/manage-plugins>) voor update-, verwijder- en publicatiecommando's.

## Core npm-pakket

Plugin | Beschrijving | Distributie | Oppervlak  
---|---|---|---  
[alibaba](</nl/plugins/reference/alibaba>) | Voegt ondersteuning voor een provider voor videogeneratie toe. | `@openclaw/alibaba-provider` |   
opgenomen in OpenClaw | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</nl/plugins/reference/amazon-bedrock>) | Voegt ondersteuning voor de Amazon Bedrock-modelprovider toe aan OpenClaw. | `@openclaw/amazon-bedrock-provider` |   
opgenomen in OpenClaw | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</nl/plugins/reference/amazon-bedrock-mantle>) | Voegt ondersteuning voor de Amazon Bedrock Mantle-modelprovider toe aan OpenClaw. | `@openclaw/amazon-bedrock-mantle-provider` |   
opgenomen in OpenClaw | providers: amazon-bedrock-mantle |  |   
[anthropic](</nl/plugins/reference/anthropic>) | Voegt ondersteuning voor de Anthropic-modelprovider toe aan OpenClaw. | `@openclaw/anthropic-provider` |   
opgenomen in OpenClaw | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</nl/plugins/reference/anthropic-vertex>) | Voegt ondersteuning voor de Anthropic Vertex-modelprovider toe aan OpenClaw. | `@openclaw/anthropic-vertex-provider` |   
opgenomen in OpenClaw | providers: anthropic-vertex |  |   
[arcee](</nl/plugins/reference/arcee>) | Voegt ondersteuning voor de Arcee-modelprovider toe aan OpenClaw. | `@openclaw/arcee-provider` |   
opgenomen in OpenClaw | providers: arcee |  |   
[azure-speech](</nl/plugins/reference/azure-speech>) | Azure AI Speech tekst-naar-spraak (MP3, native Ogg/Opus-spraaknotities, PCM-telefonie). | `@openclaw/azure-speech` |   
opgenomen in OpenClaw | contracts: speechProviders |  |   
[bonjour](</nl/plugins/reference/bonjour>) | Adverteer de lokale OpenClaw-Gateway via Bonjour/mDNS. | `@openclaw/bonjour` |   
opgenomen in OpenClaw | plugin |  |   
[browser](</nl/plugins/reference/browser>) | Voegt tools toe die door agents kunnen worden aangeroepen. | `@openclaw/browser-plugin` |   
opgenomen in OpenClaw | contracts: tools; skills |  |   
[byteplus](</nl/plugins/reference/byteplus>) | Voegt ondersteuning voor de BytePlus- en BytePlus Plan-modelprovider toe aan OpenClaw. | `@openclaw/byteplus-provider` |   
opgenomen in OpenClaw | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</nl/plugins/reference/canvas>) | Experimentele Canvas-besturing en A2UI-renderingoppervlakken voor gekoppelde nodes. | `@openclaw/canvas-plugin` |   
opgenomen in OpenClaw | contracts: tools |  |   
[cerebras](</nl/plugins/reference/cerebras>) | Voegt ondersteuning voor de Cerebras-modelprovider toe aan OpenClaw. | `@openclaw/cerebras-provider` |   
opgenomen in OpenClaw | providers: cerebras |  |   
[chutes](</nl/plugins/reference/chutes>) | Voegt ondersteuning voor de Chutes-modelprovider toe aan OpenClaw. | `@openclaw/chutes-provider` |   
opgenomen in OpenClaw | providers: chutes |  |   
[clickclack](</nl/plugins/reference/clickclack>) | Voegt het Clickclack-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/clickclack` |   
opgenomen in OpenClaw | channels: clickclack |  |   
[cloudflare-ai-gateway](</nl/plugins/reference/cloudflare-ai-gateway>) | Voegt ondersteuning voor de Cloudflare AI Gateway-modelprovider toe aan OpenClaw. | `@openclaw/cloudflare-ai-gateway-provider` |   
opgenomen in OpenClaw | providers: cloudflare-ai-gateway |  |   
[comfy](</nl/plugins/reference/comfy>) | Voegt ondersteuning voor de ComfyUI-modelprovider toe aan OpenClaw. | `@openclaw/comfy-provider` |   
opgenomen in OpenClaw | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</nl/plugins/reference/copilot-proxy>) | Voegt ondersteuning voor de Copilot Proxy-modelprovider toe aan OpenClaw. | `@openclaw/copilot-proxy` |   
opgenomen in OpenClaw | providers: copilot-proxy |  |   
[deepgram](</nl/plugins/reference/deepgram>) | Voegt ondersteuning voor een provider voor mediabegrip toe. Voegt ondersteuning voor een realtime-transcriptieprovider toe. | `@openclaw/deepgram-provider` |   
opgenomen in OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</nl/plugins/reference/deepinfra>) | Voegt ondersteuning voor de DeepInfra-modelprovider toe aan OpenClaw. | `@openclaw/deepinfra-provider` |   
opgenomen in OpenClaw | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</nl/plugins/reference/deepseek>) | Voegt ondersteuning voor DeepSeek-modelproviders toe aan OpenClaw. | `@openclaw/deepseek-provider` |   
opgenomen in OpenClaw | providers: deepseek |  |   
[document-extract](</nl/plugins/reference/document-extract>) | Extraheert tekst en fallback-pagina-afbeeldingen uit lokale documentbijlagen. | `@openclaw/document-extract-plugin` |   
opgenomen in OpenClaw | contracts: documentExtractors |  |   
[duckduckgo](</nl/plugins/reference/duckduckgo>) | Voegt ondersteuning voor webzoekproviders toe. | `@openclaw/duckduckgo-plugin` |   
opgenomen in OpenClaw | contracts: webSearchProviders |  |   
[elevenlabs](</nl/plugins/reference/elevenlabs>) | Voegt ondersteuning voor providers voor mediabegrip toe. Voegt ondersteuning voor providers voor realtime-transcriptie toe. Voegt ondersteuning voor tekst-naar-spraakproviders toe. | `@openclaw/elevenlabs-speech` |   
opgenomen in OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</nl/plugins/reference/exa>) | Voegt ondersteuning voor webzoekproviders toe. | `@openclaw/exa-plugin` |   
opgenomen in OpenClaw | contracts: webSearchProviders |  |   
[fal](</nl/plugins/reference/fal>) | Voegt ondersteuning voor fal-modelproviders toe aan OpenClaw. | `@openclaw/fal-provider` |   
opgenomen in OpenClaw | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[file-transfer](</nl/plugins/reference/file-transfer>) | Haal bestanden op, geef ze weer en schrijf ze op gekoppelde nodes via speciale node-opdrachten. Omzeilt het afkappen van bash stdout door base64 via node.invoke te gebruiken voor binaries tot 16 MB. | `@openclaw/file-transfer` |   
opgenomen in OpenClaw | contracts: tools |  |   
[firecrawl](</nl/plugins/reference/firecrawl>) | Voegt tools toe die door agents kunnen worden aangeroepen. Voegt ondersteuning voor webophaalproviders toe. Voegt ondersteuning voor webzoekproviders toe. | `@openclaw/firecrawl-plugin` |   
opgenomen in OpenClaw | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</nl/plugins/reference/fireworks>) | Voegt ondersteuning voor Fireworks-modelproviders toe aan OpenClaw. | `@openclaw/fireworks-provider` |   
opgenomen in OpenClaw | providers: fireworks |  |   
[github-copilot](</nl/plugins/reference/github-copilot>) | Voegt ondersteuning voor GitHub Copilot-modelproviders toe aan OpenClaw. | `@openclaw/github-copilot-provider` |   
opgenomen in OpenClaw | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</nl/plugins/reference/google>) | Voegt ondersteuning voor Google-, Google Gemini CLI- en Google Vertex-modelproviders toe aan OpenClaw. | `@openclaw/google-plugin` |   
opgenomen in OpenClaw | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[gradium](</nl/plugins/reference/gradium>) | Voegt ondersteuning voor tekst-naar-spraakproviders toe. | `@openclaw/gradium-speech` |   
opgenomen in OpenClaw | contracts: speechProviders |  |   
[groq](</nl/plugins/reference/groq>) | Voegt ondersteuning voor Groq-modelproviders toe aan OpenClaw. | `@openclaw/groq-provider` |   
opgenomen in OpenClaw | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</nl/plugins/reference/huggingface>) | Voegt ondersteuning voor Hugging Face-modelproviders toe aan OpenClaw. | `@openclaw/huggingface-provider` |   
opgenomen in OpenClaw | providers: huggingface |  |   
[imessage](</nl/plugins/reference/imessage>) | Voegt het iMessage-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/imessage` |   
opgenomen in OpenClaw | channels: imessage |  |   
[inworld](</nl/plugins/reference/inworld>) | Inworld streaming tekst-naar-spraak (MP3, OGG_OPUS, PCM-telefonie). | `@openclaw/inworld-speech` |   
opgenomen in OpenClaw | contracts: speechProviders |  |   
[irc](</nl/plugins/reference/irc>) | Voegt het IRC-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/irc` |   
opgenomen in OpenClaw | channels: irc |  |   
[kilocode](</nl/plugins/reference/kilocode>) | Voegt ondersteuning voor Kilocode-modelproviders toe aan OpenClaw. | `@openclaw/kilocode-provider` |   
opgenomen in OpenClaw | providers: kilocode |  |   
[kimi](</nl/plugins/reference/kimi>) | Voegt ondersteuning voor Kimi- en Kimi Coding-modelproviders toe aan OpenClaw. | `@openclaw/kimi-provider` |   
opgenomen in OpenClaw | providers: kimi, kimi-coding |  |   
[litellm](</nl/plugins/reference/litellm>) | Voegt ondersteuning voor LiteLLM-modelproviders toe aan OpenClaw. | `@openclaw/litellm-provider` |   
opgenomen in OpenClaw | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</nl/plugins/reference/llm-task>) | Generieke JSON-only LLM-tool voor gestructureerde taken die vanuit workflows kan worden aangeroepen. | `@openclaw/llm-task` |   
opgenomen in OpenClaw | contracts: tools |  |   
[lmstudio](</nl/plugins/reference/lmstudio>) | Voegt ondersteuning voor LM Studio-modelproviders toe aan OpenClaw. | `@openclaw/lmstudio-provider` |   
meegeleverd met OpenClaw | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[mattermost](</nl/plugins/reference/mattermost>) | Voegt het Mattermost-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/mattermost` |   
meegeleverd met OpenClaw | channels: mattermost |  |   
[memory-core](</nl/plugins/reference/memory-core>) | Voegt ondersteuning voor geheugen-embeddingproviders toe. Voegt tools toe die door agents kunnen worden aangeroepen. | `@openclaw/memory-core` |   
meegeleverd met OpenClaw | contracts: memoryEmbeddingProviders, tools |  |   
[memory-wiki](</nl/plugins/reference/memory-wiki>) | Persistente wiki-compiler en Obsidian-vriendelijke kennisvault voor OpenClaw. | `@openclaw/memory-wiki` |   
meegeleverd met OpenClaw | contracts: tools; skills |  |   
[microsoft](</nl/plugins/reference/microsoft>) | Voegt ondersteuning voor tekst-naar-spraakproviders toe. | `@openclaw/microsoft-speech` |   
meegeleverd met OpenClaw | contracts: speechProviders |  |   
[microsoft-foundry](</nl/plugins/reference/microsoft-foundry>) | Voegt ondersteuning voor Microsoft Foundry-modelproviders toe aan OpenClaw. | `@openclaw/microsoft-foundry` |   
meegeleverd met OpenClaw | providers: microsoft-foundry |  |   
[migrate-claude](</nl/plugins/reference/migrate-claude>) | Importeert Claude Code- en Claude Desktop-instructies, MCP-servers, skills en veilige configuratie in OpenClaw. | `@openclaw/migrate-claude` |   
meegeleverd met OpenClaw | contracts: migrationProviders |  |   
[migrate-hermes](</nl/plugins/reference/migrate-hermes>) | Importeert Hermes-configuratie, herinneringen, skills en ondersteunde referenties in OpenClaw. | `@openclaw/migrate-hermes` |   
meegeleverd met OpenClaw | contracts: migrationProviders |  |   
[minimax](</nl/plugins/reference/minimax>) | Voegt ondersteuning voor MiniMax- en MiniMax Portal-modelproviders toe aan OpenClaw. | `@openclaw/minimax-provider` |   
meegeleverd met OpenClaw | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</nl/plugins/reference/mistral>) | Voegt ondersteuning voor Mistral-modelproviders toe aan OpenClaw. | `@openclaw/mistral-provider` |   
meegeleverd met OpenClaw | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</nl/plugins/reference/moonshot>) | Voegt ondersteuning voor Moonshot-modelproviders toe aan OpenClaw. | `@openclaw/moonshot-provider` |   
meegeleverd met OpenClaw | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[nvidia](</nl/plugins/reference/nvidia>) | Voegt ondersteuning voor NVIDIA-modelproviders toe aan OpenClaw. | `@openclaw/nvidia-provider` |   
meegeleverd met OpenClaw | providers: nvidia |  |   
[oc-path](</nl/plugins/reference/oc-path>) | Voegt de openclaw path CLI toe voor oc://-werkruimtebestandsadressering. | `@openclaw/oc-path` |   
meegeleverd met OpenClaw | plugin |  |   
[ollama](</nl/plugins/reference/ollama>) | Voegt ondersteuning voor Ollama-modelproviders toe aan OpenClaw. | `@openclaw/ollama-provider` |   
meegeleverd met OpenClaw | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</nl/plugins/reference/open-prose>) | OpenProse VM-skillpakket met een /prose-slashcommand. | `@openclaw/open-prose` |   
meegeleverd met OpenClaw | skills |  |   
[openai](</nl/plugins/reference/openai>) | Voegt ondersteuning voor OpenAI- en OpenAI Codex-modelproviders toe aan OpenClaw. | `@openclaw/openai-provider` |   
meegeleverd met OpenClaw | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</nl/plugins/reference/opencode>) | Voegt ondersteuning voor OpenCode-modelproviders toe aan OpenClaw. | `@openclaw/opencode-provider` |   
meegeleverd met OpenClaw | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</nl/plugins/reference/opencode-go>) | Voegt ondersteuning voor OpenCode Go-modelproviders toe aan OpenClaw. | `@openclaw/opencode-go-provider` |   
meegeleverd met OpenClaw | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</nl/plugins/reference/openrouter>) | Voegt ondersteuning voor OpenRouter-modelproviders toe aan OpenClaw. | `@openclaw/openrouter-provider` |   
meegeleverd met OpenClaw | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</nl/plugins/reference/openshell>) | Sandbox-backend aangedreven door OpenShell met gespiegelde lokale werkruimten en op SSH gebaseerde opdrachtuitvoering. | `@openclaw/openshell-sandbox` |   
meegeleverd met OpenClaw | plugin |  |   
[perplexity](</nl/plugins/reference/perplexity>) | Voegt ondersteuning voor webzoekproviders toe. | `@openclaw/perplexity-plugin` |   
meegeleverd met OpenClaw | contracts: webSearchProviders |  |   
[qianfan](</nl/plugins/reference/qianfan>) | Voegt ondersteuning voor de Qianfan-modelprovider toe aan OpenClaw. | `@openclaw/qianfan-provider` |   
opgenomen in OpenClaw | providers: qianfan |  |   
[qwen](</nl/plugins/reference/qwen>) | Voegt ondersteuning voor de modelproviders Qwen, Qwen Cloud, Model Studio en DashScope toe aan OpenClaw. | `@openclaw/qwen-provider` |   
opgenomen in OpenClaw | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</nl/plugins/reference/runway>) | Voegt ondersteuning voor videogeneratieproviders toe. | `@openclaw/runway-provider` |   
opgenomen in OpenClaw | contracts: videoGenerationProviders |  |   
[searxng](</nl/plugins/reference/searxng>) | Voegt ondersteuning voor webzoekproviders toe. | `@openclaw/searxng-plugin` |   
opgenomen in OpenClaw | contracts: webSearchProviders |  |   
[senseaudio](</nl/plugins/reference/senseaudio>) | Voegt ondersteuning voor media-understandingproviders toe. | `@openclaw/senseaudio-provider` |   
opgenomen in OpenClaw | contracts: mediaUnderstandingProviders |  |   
[sglang](</nl/plugins/reference/sglang>) | Voegt ondersteuning voor de SGLang-modelprovider toe aan OpenClaw. | `@openclaw/sglang-provider` |   
opgenomen in OpenClaw | providers: sglang |  |   
[signal](</nl/plugins/reference/signal>) | Voegt de Signal-kanaalinterface toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/signal` |   
opgenomen in OpenClaw | channels: signal |  |   
[skill-workshop](</nl/plugins/reference/skill-workshop>) | Legt herhaalbare workflows vast als workspace-Skills, met wachtende review, veilige schrijfacties en vernieuwing van skill-prompts. | `@openclaw/skill-workshop` |   
opgenomen in OpenClaw | contracts: tools |  |   
[slack](</nl/plugins/reference/slack>) | Voegt de Slack-kanaalinterface toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/slack` |   
opgenomen in OpenClaw | channels: slack |  |   
[stepfun](</nl/plugins/reference/stepfun>) | Voegt ondersteuning voor de modelproviders StepFun en StepFun Plan toe aan OpenClaw. | `@openclaw/stepfun-provider` |   
opgenomen in OpenClaw | providers: stepfun, stepfun-plan |  |   
[synthetic](</nl/plugins/reference/synthetic>) | Voegt ondersteuning voor de Synthetic-modelprovider toe aan OpenClaw. | `@openclaw/synthetic-provider` |   
opgenomen in OpenClaw | providers: synthetic |  |   
[tavily](</nl/plugins/reference/tavily>) | Voegt door agents aanroepbare hulpmiddelen toe. Voegt ondersteuning voor webzoekproviders toe. | `@openclaw/tavily-plugin` |   
opgenomen in OpenClaw | contracts: tools, webSearchProviders; skills |  |   
[telegram](</nl/plugins/reference/telegram>) | Voegt de Telegram-kanaalinterface toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/telegram` |   
opgenomen in OpenClaw | channels: telegram |  |   
[tencent](</nl/plugins/reference/tencent>) | Voegt ondersteuning voor de Tencent TokenHub-modelprovider toe aan OpenClaw. | `@openclaw/tencent-provider` |   
opgenomen in OpenClaw | providers: tencent-tokenhub |  |   
[together](</nl/plugins/reference/together>) | Voegt ondersteuning voor de Together-modelprovider toe aan OpenClaw. | `@openclaw/together-provider` |   
opgenomen in OpenClaw | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</nl/plugins/reference/tokenjuice>) | Comprimeert resultaten van exec- en bash-tools met tokenjuice-reducers. | `@openclaw/tokenjuice` |   
opgenomen in OpenClaw | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</nl/plugins/reference/tts-local-cli>) | Voegt ondersteuning voor tekst-naar-spraakproviders toe. | `@openclaw/tts-local-cli` |   
opgenomen in OpenClaw | contracts: speechProviders |  |   
[venice](</nl/plugins/reference/venice>) | Voegt ondersteuning voor de Venice-modelprovider toe aan OpenClaw. | `@openclaw/venice-provider` |   
opgenomen in OpenClaw | providers: venice |  |   
[vercel-ai-gateway](</nl/plugins/reference/vercel-ai-gateway>) | Voegt ondersteuning voor de Vercel AI Gateway-modelprovider toe aan OpenClaw. | `@openclaw/vercel-ai-gateway-provider` |   
opgenomen in OpenClaw | providers: vercel-ai-gateway |  |   
[vllm](</nl/plugins/reference/vllm>) | Voegt ondersteuning voor de vLLM-modelprovider toe aan OpenClaw. | `@openclaw/vllm-provider` |   
opgenomen in OpenClaw | providers: vllm |  |   
[volcengine](</nl/plugins/reference/volcengine>) | Voegt ondersteuning voor de modelproviders Volcengine en Volcengine Plan toe aan OpenClaw. | `@openclaw/volcengine-provider` |   
opgenomen in OpenClaw | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</nl/plugins/reference/voyage>) | Voegt ondersteuning voor memory-embeddingproviders toe. | `@openclaw/voyage-provider` |   
opgenomen in OpenClaw | contracts: memoryEmbeddingProviders |  |   
[vydra](</nl/plugins/reference/vydra>) | Voegt ondersteuning voor Vydra-modelproviders toe aan OpenClaw. | `@openclaw/vydra-provider` |   
opgenomen in OpenClaw | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</nl/plugins/reference/web-readability>) | Extraheert leesbare artikelinhoud uit lokale HTML-webophaalreacties. | `@openclaw/web-readability-plugin` |   
opgenomen in OpenClaw | contracts: webContentExtractors |  |   
[webhooks](</nl/plugins/reference/webhooks>) | Geverifieerde inkomende Webhooks die externe automatisering koppelen aan OpenClaw TaskFlows. | `@openclaw/webhooks` |   
opgenomen in OpenClaw | plugin |  |   
[xai](</nl/plugins/reference/xai>) | Voegt ondersteuning voor xAI-modelproviders toe aan OpenClaw. | `@openclaw/xai-plugin` |   
opgenomen in OpenClaw | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</nl/plugins/reference/xiaomi>) | Voegt ondersteuning voor Xiaomi-modelproviders toe aan OpenClaw. | `@openclaw/xiaomi-provider` |   
opgenomen in OpenClaw | providers: xiaomi; contracts: speechProviders |  |   
[zai](</nl/plugins/reference/zai>) | Voegt ondersteuning voor Z.AI-modelproviders toe aan OpenClaw. | `@openclaw/zai-provider` |   
opgenomen in OpenClaw | providers: zai; contracts: mediaUnderstandingProviders |  |   
  
## Officiële externe pakketten

Plugin | Beschrijving | Distributie | Oppervlak  
---|---|---|---  
[acpx](</nl/plugins/reference/acpx>) | Ingebedde ACP-runtimebackend met door de Plugin beheerd sessie- en transportbeheer. | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[brave](</nl/plugins/reference/brave>) | Voegt ondersteuning toe voor webzoekproviders. | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[codex](</nl/plugins/reference/codex>) | Codex-app-serverharnas en door Codex beheerde GPT-modelcatalogus. | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[diagnostics-otel](</nl/plugins/reference/diagnostics-otel>) | OpenClaw-diagnostiekexporter voor OpenTelemetry. | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</nl/plugins/reference/diagnostics-prometheus>) | OpenClaw-diagnostiekexporter voor Prometheus. | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</nl/plugins/reference/diffs>) | Alleen-lezen diffviewer en bestandsrenderer voor agents. | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</nl/plugins/reference/discord>) | Voegt het Discord-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[feishu](</nl/plugins/reference/feishu>) | Voegt het Feishu-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[google-meet](</nl/plugins/reference/google-meet>) | Neem deel aan Google Meet-gesprekken via Chrome- of Twilio-transports. | `@openclaw/google-meet` |   
npm; ClawHub | contracts: tools |  |   
[googlechat](</nl/plugins/reference/googlechat>) | Voegt het Google Chat-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/googlechat` |   
npm; ClawHub | channels: googlechat |  |   
[line](</nl/plugins/reference/line>) | Voegt het LINE-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/line` |   
npm; ClawHub | channels: line |  |   
[lobster](</nl/plugins/reference/lobster>) | Getypte workflowtool met hervatbare goedkeuringen. | `@openclaw/lobster` |   
npm; ClawHub | contracts: tools |  |   
[matrix](</nl/plugins/reference/matrix>) | Voegt het Matrix-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | channels: matrix |  |   
[memory-lancedb](</nl/plugins/reference/memory-lancedb>) | Voegt door agents aanroepbare tools toe. | `@openclaw/memory-lancedb` |   
npm; ClawHub | contracts: tools |  |   
[msteams](</nl/plugins/reference/msteams>) | Voegt het Microsoft Teams-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</nl/plugins/reference/nextcloud-talk>) | Voegt het Nextcloud Talk-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</nl/plugins/reference/nostr>) | Voegt het Nostr-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[qqbot](</nl/plugins/reference/qqbot>) | Voegt het QQ Bot-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[synology-chat](</nl/plugins/reference/synology-chat>) | Voegt het Synology Chat-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[tlon](</nl/plugins/reference/tlon>) | Voegt het Tlon-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[twitch](</nl/plugins/reference/twitch>) | Voegt het Twitch-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[voice-call](</nl/plugins/reference/voice-call>) | Voegt door agents aanroepbare tools toe. | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[whatsapp](</nl/plugins/reference/whatsapp>) | Voegt het WhatsApp-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[zalo](</nl/plugins/reference/zalo>) | Voegt het Zalo-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</nl/plugins/reference/zalouser>) | Voegt het Zalo Personal-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
## Alleen bron-checkout

Plugin | Beschrijving | Distributie | Oppervlak  
---|---|---|---  
[qa-channel](</nl/plugins/reference/qa-channel>) | Voegt het QA Channel-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten. | `@openclaw/qa-channel` |   
alleen bron-checkout | channels: qa-channel |  |   
[qa-lab](</nl/plugins/reference/qa-lab>) | OpenClaw-QA-labplugin met privé-debugger-UI en scenariorunner. | `@openclaw/qa-lab` |   
alleen bron-checkout | plugin |  |   
[qa-matrix](</nl/plugins/reference/qa-matrix>) | Matrix-QA-transportrunner en substraat. | `@openclaw/qa-matrix` |   
alleen bron-checkout | plugin |  |   
  
Was this useful?YesNo