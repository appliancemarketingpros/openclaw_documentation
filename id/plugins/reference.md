---
title: Referensi Plugin
source_url: https://docs.openclaw.ai/id/plugins/reference
scraped_at: 2026-05-25
---

# Referensi Plugin

Halaman ini dihasilkan dari `extensions/*/package.json` dan `openclaw.plugin.json`. Hasilkan ulang dengan:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

Plugin | Deskripsi | Distribusi | Permukaan  
---|---|---|---  
[acpx](</id/plugins/reference/acpx>) | Backend runtime ACP tertanam dengan manajemen sesi dan transport yang dimiliki Plugin. | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[alibaba](</id/plugins/reference/alibaba>) | Menambahkan dukungan penyedia pembuatan video. | `@openclaw/alibaba-provider` |   
disertakan dalam OpenClaw | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</id/plugins/reference/amazon-bedrock>) | Menambahkan dukungan penyedia model Amazon Bedrock ke OpenClaw. | `@openclaw/amazon-bedrock-provider` |   
disertakan dalam OpenClaw | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</id/plugins/reference/amazon-bedrock-mantle>) | Menambahkan dukungan penyedia model Amazon Bedrock Mantle ke OpenClaw. | `@openclaw/amazon-bedrock-mantle-provider` |   
disertakan dalam OpenClaw | providers: amazon-bedrock-mantle |  |   
[anthropic](</id/plugins/reference/anthropic>) | Menambahkan dukungan penyedia model Anthropic ke OpenClaw. | `@openclaw/anthropic-provider` |   
disertakan dalam OpenClaw | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</id/plugins/reference/anthropic-vertex>) | Menambahkan dukungan penyedia model Anthropic Vertex ke OpenClaw. | `@openclaw/anthropic-vertex-provider` |   
disertakan dalam OpenClaw | providers: anthropic-vertex |  |   
[arcee](</id/plugins/reference/arcee>) | Menambahkan dukungan penyedia model Arcee ke OpenClaw. | `@openclaw/arcee-provider` |   
disertakan dalam OpenClaw | providers: arcee |  |   
[azure-speech](</id/plugins/reference/azure-speech>) | Text-to-speech Azure AI Speech (MP3, catatan suara Ogg/Opus native, telefoni PCM). | `@openclaw/azure-speech` |   
disertakan dalam OpenClaw | contracts: speechProviders |  |   
[bonjour](</id/plugins/reference/bonjour>) | Mengiklankan Gateway OpenClaw lokal melalui Bonjour/mDNS. | `@openclaw/bonjour` |   
disertakan dalam OpenClaw | plugin |  |   
[brave](</id/plugins/reference/brave>) | Menambahkan dukungan penyedia pencarian web. | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[browser](</id/plugins/reference/browser>) | Menambahkan alat yang dapat dipanggil agen. | `@openclaw/browser-plugin` |   
disertakan dalam OpenClaw | contracts: tools; skills |  |   
[byteplus](</id/plugins/reference/byteplus>) | Menambahkan dukungan penyedia model BytePlus, BytePlus Plan ke OpenClaw. | `@openclaw/byteplus-provider` |   
disertakan dalam OpenClaw | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</id/plugins/reference/canvas>) | Permukaan kontrol Canvas eksperimental dan rendering A2UI untuk Node yang dipasangkan. | `@openclaw/canvas-plugin` |   
disertakan dalam OpenClaw | contracts: tools |  |   
[cerebras](</id/plugins/reference/cerebras>) | Menambahkan dukungan penyedia model Cerebras ke OpenClaw. | `@openclaw/cerebras-provider` |   
disertakan dalam OpenClaw | providers: cerebras |  |   
[chutes](</id/plugins/reference/chutes>) | Menambahkan dukungan penyedia model Chutes ke OpenClaw. | `@openclaw/chutes-provider` |   
disertakan dalam OpenClaw | providers: chutes |  |   
[clickclack](</id/plugins/reference/clickclack>) | Menambahkan permukaan kanal Clickclack untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/clickclack` |   
disertakan dalam OpenClaw | channels: clickclack |  |   
[cloudflare-ai-gateway](</id/plugins/reference/cloudflare-ai-gateway>) | Menambahkan dukungan penyedia model Cloudflare AI Gateway ke OpenClaw. | `@openclaw/cloudflare-ai-gateway-provider` |   
disertakan dalam OpenClaw | providers: cloudflare-ai-gateway |  |   
[codex](</id/plugins/reference/codex>) | Harness server aplikasi Codex dan katalog model GPT yang dikelola Codex. | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[comfy](</id/plugins/reference/comfy>) | Menambahkan dukungan penyedia model ComfyUI ke OpenClaw. | `@openclaw/comfy-provider` |   
disertakan dalam OpenClaw | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</id/plugins/reference/copilot-proxy>) | Menambahkan dukungan penyedia model Copilot Proxy ke OpenClaw. | `@openclaw/copilot-proxy` |   
disertakan dalam OpenClaw | providers: copilot-proxy |  |   
[deepgram](</id/plugins/reference/deepgram>) | Menambahkan dukungan penyedia pemahaman media. Menambahkan dukungan penyedia transkripsi waktu nyata. | `@openclaw/deepgram-provider` |   
disertakan dalam OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</id/plugins/reference/deepinfra>) | Menambahkan dukungan penyedia model DeepInfra ke OpenClaw. | `@openclaw/deepinfra-provider` |   
disertakan dalam OpenClaw | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</id/plugins/reference/deepseek>) | Menambahkan dukungan penyedia model DeepSeek ke OpenClaw. | `@openclaw/deepseek-provider` |   
disertakan dalam OpenClaw | providers: deepseek |  |   
[diagnostics-otel](</id/plugins/reference/diagnostics-otel>) | Eksportir OpenTelemetry diagnostik OpenClaw. | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</id/plugins/reference/diagnostics-prometheus>) | Eksportir Prometheus diagnostik OpenClaw. | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</id/plugins/reference/diffs>) | Penampil diff hanya-baca dan perender file untuk agen. | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</id/plugins/reference/discord>) | Menambahkan permukaan channel Discord untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[document-extract](</id/plugins/reference/document-extract>) | Mengekstrak teks dan gambar halaman fallback dari lampiran dokumen lokal. | `@openclaw/document-extract-plugin` |   
disertakan dalam OpenClaw | contracts: documentExtractors |  |   
[duckduckgo](</id/plugins/reference/duckduckgo>) | Menambahkan dukungan penyedia pencarian web. | `@openclaw/duckduckgo-plugin` |   
disertakan dalam OpenClaw | contracts: webSearchProviders |  |   
[elevenlabs](</id/plugins/reference/elevenlabs>) | Menambahkan dukungan penyedia pemahaman media. Menambahkan dukungan penyedia transkripsi waktu nyata. Menambahkan dukungan penyedia text-to-speech. | `@openclaw/elevenlabs-speech` |   
disertakan dalam OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</id/plugins/reference/exa>) | Menambahkan dukungan penyedia pencarian web. | `@openclaw/exa-plugin` |   
disertakan dalam OpenClaw | contracts: webSearchProviders |  |   
[fal](</id/plugins/reference/fal>) | Menambahkan dukungan penyedia model fal ke OpenClaw. | `@openclaw/fal-provider` |   
disertakan dalam OpenClaw | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[feishu](</id/plugins/reference/feishu>) | Menambahkan permukaan channel Feishu untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[file-transfer](</id/plugins/reference/file-transfer>) | Mengambil, mencantumkan, dan menulis file pada node yang dipasangkan melalui perintah node khusus. Melewati pemotongan stdout bash dengan menggunakan base64 melalui node.invoke untuk biner hingga 16 MB. | `@openclaw/file-transfer` |   
disertakan dalam OpenClaw | contracts: tools |  |   
[firecrawl](</id/plugins/reference/firecrawl>) | Menambahkan alat yang dapat dipanggil agen. Menambahkan dukungan penyedia pengambilan web. Menambahkan dukungan penyedia pencarian web. | `@openclaw/firecrawl-plugin` |   
disertakan dalam OpenClaw | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</id/plugins/reference/fireworks>) | Menambahkan dukungan penyedia model Fireworks ke OpenClaw. | `@openclaw/fireworks-provider` |   
disertakan dalam OpenClaw | providers: fireworks |  |   
[github-copilot](</id/plugins/reference/github-copilot>) | Menambahkan dukungan penyedia model GitHub Copilot ke OpenClaw. | `@openclaw/github-copilot-provider` |   
disertakan dalam OpenClaw | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</id/plugins/reference/google>) | Menambahkan dukungan penyedia model Google, Google Gemini CLI, dan Google Vertex ke OpenClaw. | `@openclaw/google-plugin` |   
disertakan dalam OpenClaw | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[google-meet](</id/plugins/reference/google-meet>) | Bergabung ke panggilan Google Meet melalui transport Chrome atau Twilio. | `@openclaw/google-meet` |   
npm; ClawHub | kontrak: alat |  |   
[googlechat](</id/plugins/reference/googlechat>) | Menambahkan permukaan saluran Google Chat untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/googlechat` |   
npm; ClawHub | saluran: googlechat |  |   
[gradium](</id/plugins/reference/gradium>) | Menambahkan dukungan penyedia text-to-speech. | `@openclaw/gradium-speech` |   
disertakan dalam OpenClaw | kontrak: speechProviders |  |   
[groq](</id/plugins/reference/groq>) | Menambahkan dukungan penyedia model Groq ke OpenClaw. | `@openclaw/groq-provider` |   
disertakan dalam OpenClaw | penyedia: groq; kontrak: mediaUnderstandingProviders |  |   
[huggingface](</id/plugins/reference/huggingface>) | Menambahkan dukungan penyedia model Hugging Face ke OpenClaw. | `@openclaw/huggingface-provider` |   
disertakan dalam OpenClaw | penyedia: huggingface |  |   
[imessage](</id/plugins/reference/imessage>) | Menambahkan permukaan saluran iMessage untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/imessage` |   
disertakan dalam OpenClaw | saluran: imessage |  |   
[inworld](</id/plugins/reference/inworld>) | Text-to-speech streaming Inworld (MP3, OGG_OPUS, PCM teleponi). | `@openclaw/inworld-speech` |   
disertakan dalam OpenClaw | kontrak: speechProviders |  |   
[irc](</id/plugins/reference/irc>) | Menambahkan permukaan saluran IRC untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/irc` |   
disertakan dalam OpenClaw | saluran: irc |  |   
[kilocode](</id/plugins/reference/kilocode>) | Menambahkan dukungan penyedia model Kilocode ke OpenClaw. | `@openclaw/kilocode-provider` |   
disertakan dalam OpenClaw | penyedia: kilocode |  |   
[kimi](</id/plugins/reference/kimi>) | Menambahkan dukungan penyedia model Kimi, Kimi Coding ke OpenClaw. | `@openclaw/kimi-provider` |   
disertakan dalam OpenClaw | penyedia: kimi, kimi-coding |  |   
[line](</id/plugins/reference/line>) | Menambahkan permukaan saluran LINE untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/line` |   
npm; ClawHub | saluran: line |  |   
[litellm](</id/plugins/reference/litellm>) | Menambahkan dukungan penyedia model LiteLLM ke OpenClaw. | `@openclaw/litellm-provider` |   
disertakan dalam OpenClaw | penyedia: litellm; kontrak: imageGenerationProviders |  |   
[llm-task](</id/plugins/reference/llm-task>) | Alat LLM generik khusus JSON untuk tugas terstruktur yang dapat dipanggil dari workflow. | `@openclaw/llm-task` |   
disertakan dalam OpenClaw | kontrak: alat |  |   
[lmstudio](</id/plugins/reference/lmstudio>) | Menambahkan dukungan penyedia model LM Studio ke OpenClaw. | `@openclaw/lmstudio-provider` |   
disertakan dalam OpenClaw | penyedia: lmstudio; kontrak: memoryEmbeddingProviders |  |   
[lobster](</id/plugins/reference/lobster>) | Alat workflow bertipe dengan persetujuan yang dapat dilanjutkan. | `@openclaw/lobster` |   
npm; ClawHub | kontrak: alat |  |   
[matrix](</id/plugins/reference/matrix>) | Menambahkan permukaan saluran Matrix untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | saluran: matrix |  |   
[mattermost](</id/plugins/reference/mattermost>) | Menambahkan permukaan saluran Mattermost untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/mattermost` |   
disertakan dalam OpenClaw | saluran: mattermost |  |   
[memory-core](</id/plugins/reference/memory-core>) | Menambahkan dukungan penyedia embedding memori. Menambahkan alat yang dapat dipanggil agen. | `@openclaw/memory-core` |   
disertakan dalam OpenClaw | kontrak: memoryEmbeddingProviders, alat |  |   
[memory-lancedb](</id/plugins/reference/memory-lancedb>) | Menambahkan alat yang dapat dipanggil agen. | `@openclaw/memory-lancedb` |   
npm; ClawHub | kontrak: alat |  |   
[memory-wiki](</id/plugins/reference/memory-wiki>) | Kompiler wiki persisten dan brankas pengetahuan yang ramah Obsidian untuk OpenClaw. | `@openclaw/memory-wiki` |   
disertakan dalam OpenClaw | kontrak: alat; Skills |  |   
[microsoft](</id/plugins/reference/microsoft>) | Menambahkan dukungan penyedia text-to-speech. | `@openclaw/microsoft-speech` |   
disertakan dalam OpenClaw | contracts: speechProviders |  |   
[microsoft-foundry](</id/plugins/reference/microsoft-foundry>) | Menambahkan dukungan penyedia model Microsoft Foundry ke OpenClaw. | `@openclaw/microsoft-foundry` |   
disertakan dalam OpenClaw | providers: microsoft-foundry |  |   
[migrate-claude](</id/plugins/reference/migrate-claude>) | Mengimpor instruksi Claude Code dan Claude Desktop, server MCP, skills, dan konfigurasi aman ke OpenClaw. | `@openclaw/migrate-claude` |   
disertakan dalam OpenClaw | contracts: migrationProviders |  |   
[migrate-hermes](</id/plugins/reference/migrate-hermes>) | Mengimpor konfigurasi Hermes, memori, skills, dan kredensial yang didukung ke OpenClaw. | `@openclaw/migrate-hermes` |   
disertakan dalam OpenClaw | contracts: migrationProviders |  |   
[minimax](</id/plugins/reference/minimax>) | Menambahkan dukungan penyedia model MiniMax, MiniMax Portal ke OpenClaw. | `@openclaw/minimax-provider` |   
disertakan dalam OpenClaw | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</id/plugins/reference/mistral>) | Menambahkan dukungan penyedia model Mistral ke OpenClaw. | `@openclaw/mistral-provider` |   
disertakan dalam OpenClaw | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</id/plugins/reference/moonshot>) | Menambahkan dukungan penyedia model Moonshot ke OpenClaw. | `@openclaw/moonshot-provider` |   
disertakan dalam OpenClaw | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[msteams](</id/plugins/reference/msteams>) | Menambahkan permukaan saluran Microsoft Teams untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</id/plugins/reference/nextcloud-talk>) | Menambahkan permukaan saluran Nextcloud Talk untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</id/plugins/reference/nostr>) | Menambahkan permukaan saluran Nostr untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[nvidia](</id/plugins/reference/nvidia>) | Menambahkan dukungan penyedia model NVIDIA ke OpenClaw. | `@openclaw/nvidia-provider` |   
disertakan dalam OpenClaw | providers: nvidia |  |   
[oc-path](</id/plugins/reference/oc-path>) | Menambahkan CLI jalur openclaw untuk pengalamatan file ruang kerja oc://. | `@openclaw/oc-path` |   
disertakan dalam OpenClaw | plugin |  |   
[ollama](</id/plugins/reference/ollama>) | Menambahkan dukungan penyedia model Ollama ke OpenClaw. | `@openclaw/ollama-provider` |   
disertakan dalam OpenClaw | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</id/plugins/reference/open-prose>) | Paket skill OpenProse VM dengan perintah slash /prose. | `@openclaw/open-prose` |   
disertakan dalam OpenClaw | skills |  |   
[openai](</id/plugins/reference/openai>) | Menambahkan dukungan penyedia model OpenAI, OpenAI Codex ke OpenClaw. | `@openclaw/openai-provider` |   
disertakan dalam OpenClaw | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</id/plugins/reference/opencode>) | Menambahkan dukungan penyedia model OpenCode ke OpenClaw. | `@openclaw/opencode-provider` |   
disertakan dalam OpenClaw | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</id/plugins/reference/opencode-go>) | Menambahkan dukungan penyedia model OpenCode Go ke OpenClaw. | `@openclaw/opencode-go-provider` |   
disertakan dalam OpenClaw | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</id/plugins/reference/openrouter>) | Menambahkan dukungan penyedia model OpenRouter ke OpenClaw. | `@openclaw/openrouter-provider` |   
disertakan dalam OpenClaw | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</id/plugins/reference/openshell>) | Backend sandbox yang didukung oleh OpenShell dengan ruang kerja lokal yang dicerminkan dan eksekusi perintah berbasis SSH. | `@openclaw/openshell-sandbox` |   
disertakan dalam OpenClaw | plugin |  |   
[perplexity](</id/plugins/reference/perplexity>) | Menambahkan dukungan penyedia pencarian web. | `@openclaw/perplexity-plugin` |   
disertakan dalam OpenClaw | contracts: webSearchProviders |  |   
[qa-channel](</id/plugins/reference/qa-channel>) | Menambahkan permukaan QA Channel untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/qa-channel` |   
hanya checkout sumber | saluran: qa-channel |  |   
[qa-lab](</id/plugins/reference/qa-lab>) | Plugin lab QA OpenClaw dengan UI debugger pribadi dan runner skenario. | `@openclaw/qa-lab` |   
hanya checkout sumber | plugin |  |   
[qa-matrix](</id/plugins/reference/qa-matrix>) | Runner dan substrat transport QA Matrix. | `@openclaw/qa-matrix` |   
hanya checkout sumber | plugin |  |   
[qianfan](</id/plugins/reference/qianfan>) | Menambahkan dukungan penyedia model Qianfan ke OpenClaw. | `@openclaw/qianfan-provider` |   
disertakan dalam OpenClaw | penyedia: qianfan |  |   
[qqbot](</id/plugins/reference/qqbot>) | Menambahkan permukaan channel QQ Bot untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/qqbot` |   
npm; ClawHub | saluran: qqbot; kontrak: tools; skills |  |   
[qwen](</id/plugins/reference/qwen>) | Menambahkan dukungan penyedia model Qwen, Qwen Cloud, Model Studio, DashScope ke OpenClaw. | `@openclaw/qwen-provider` |   
disertakan dalam OpenClaw | penyedia: qwen, qwencloud, modelstudio, dashscope; kontrak: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</id/plugins/reference/runway>) | Menambahkan dukungan penyedia pembuatan video. | `@openclaw/runway-provider` |   
disertakan dalam OpenClaw | kontrak: videoGenerationProviders |  |   
[searxng](</id/plugins/reference/searxng>) | Menambahkan dukungan penyedia pencarian web. | `@openclaw/searxng-plugin` |   
disertakan dalam OpenClaw | kontrak: webSearchProviders |  |   
[senseaudio](</id/plugins/reference/senseaudio>) | Menambahkan dukungan penyedia pemahaman media. | `@openclaw/senseaudio-provider` |   
disertakan dalam OpenClaw | kontrak: mediaUnderstandingProviders |  |   
[sglang](</id/plugins/reference/sglang>) | Menambahkan dukungan penyedia model SGLang ke OpenClaw. | `@openclaw/sglang-provider` |   
disertakan dalam OpenClaw | penyedia: sglang |  |   
[signal](</id/plugins/reference/signal>) | Menambahkan permukaan channel Signal untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/signal` |   
disertakan dalam OpenClaw | saluran: signal |  |   
[skill-workshop](</id/plugins/reference/skill-workshop>) | Menangkap alur kerja yang dapat diulang sebagai keterampilan ruang kerja, dengan peninjauan tertunda, penulisan aman, dan penyegaran prompt keterampilan. | `@openclaw/skill-workshop` |   
disertakan dalam OpenClaw | kontrak: tools |  |   
[slack](</id/plugins/reference/slack>) | Menambahkan permukaan channel Slack untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/slack` |   
disertakan dalam OpenClaw | saluran: slack |  |   
[stepfun](</id/plugins/reference/stepfun>) | Menambahkan dukungan penyedia model StepFun, StepFun Plan ke OpenClaw. | `@openclaw/stepfun-provider` |   
disertakan dalam OpenClaw | penyedia: stepfun, stepfun-plan |  |   
[synology-chat](</id/plugins/reference/synology-chat>) | Menambahkan permukaan channel Synology Chat untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/synology-chat` |   
npm; ClawHub | saluran: synology-chat |  |   
[synthetic](</id/plugins/reference/synthetic>) | Menambahkan dukungan penyedia model Synthetic ke OpenClaw. | `@openclaw/synthetic-provider` |   
disertakan dalam OpenClaw | penyedia: synthetic |  |   
[tavily](</id/plugins/reference/tavily>) | Menambahkan alat yang dapat dipanggil agen. Menambahkan dukungan penyedia pencarian web. | `@openclaw/tavily-plugin` |   
disertakan dalam OpenClaw | kontrak: tools, webSearchProviders; skills |  |   
[telegram](</id/plugins/reference/telegram>) | Menambahkan permukaan channel Telegram untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/telegram` |   
disertakan dalam OpenClaw | saluran: telegram |  |   
[tencent](</id/plugins/reference/tencent>) | Menambahkan dukungan penyedia model Tencent TokenHub ke OpenClaw. | `@openclaw/tencent-provider` |   
disertakan dalam OpenClaw | penyedia: tencent-tokenhub |  |   
[tlon](</id/plugins/reference/tlon>) | Menambahkan permukaan channel Tlon untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/tlon` |   
npm; ClawHub | saluran: tlon; kontrak: tools; skills |  |   
[together](</id/plugins/reference/together>) | Menambahkan dukungan penyedia model Together ke OpenClaw. | `@openclaw/together-provider` |   
disertakan dalam OpenClaw | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</id/plugins/reference/tokenjuice>) | Memadatkan hasil alat exec dan bash dengan reducer tokenjuice. | `@openclaw/tokenjuice` |   
disertakan dalam OpenClaw | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</id/plugins/reference/tts-local-cli>) | Menambahkan dukungan penyedia teks-ke-ucapan. | `@openclaw/tts-local-cli` |   
disertakan dalam OpenClaw | contracts: speechProviders |  |   
[twitch](</id/plugins/reference/twitch>) | Menambahkan permukaan saluran Twitch untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[venice](</id/plugins/reference/venice>) | Menambahkan dukungan penyedia model Venice ke OpenClaw. | `@openclaw/venice-provider` |   
disertakan dalam OpenClaw | providers: venice |  |   
[vercel-ai-gateway](</id/plugins/reference/vercel-ai-gateway>) | Menambahkan dukungan penyedia model Vercel AI Gateway ke OpenClaw. | `@openclaw/vercel-ai-gateway-provider` |   
disertakan dalam OpenClaw | providers: vercel-ai-gateway |  |   
[vllm](</id/plugins/reference/vllm>) | Menambahkan dukungan penyedia model vLLM ke OpenClaw. | `@openclaw/vllm-provider` |   
disertakan dalam OpenClaw | providers: vllm |  |   
[voice-call](</id/plugins/reference/voice-call>) | Menambahkan alat yang dapat dipanggil agen. | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[volcengine](</id/plugins/reference/volcengine>) | Menambahkan dukungan penyedia model Volcengine, Volcengine Plan ke OpenClaw. | `@openclaw/volcengine-provider` |   
disertakan dalam OpenClaw | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</id/plugins/reference/voyage>) | Menambahkan dukungan penyedia embedding memori. | `@openclaw/voyage-provider` |   
disertakan dalam OpenClaw | contracts: memoryEmbeddingProviders |  |   
[vydra](</id/plugins/reference/vydra>) | Menambahkan dukungan penyedia model Vydra ke OpenClaw. | `@openclaw/vydra-provider` |   
disertakan dalam OpenClaw | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</id/plugins/reference/web-readability>) | Mengekstrak konten artikel yang mudah dibaca dari respons pengambilan web HTML lokal. | `@openclaw/web-readability-plugin` |   
disertakan dalam OpenClaw | contracts: webContentExtractors |  |   
[webhooks](</id/plugins/reference/webhooks>) | Webhook masuk terautentikasi yang mengikat automasi eksternal ke TaskFlow OpenClaw. | `@openclaw/webhooks` |   
disertakan dalam OpenClaw | plugin |  |   
[whatsapp](</id/plugins/reference/whatsapp>) | Menambahkan permukaan saluran WhatsApp untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[xai](</id/plugins/reference/xai>) | Menambahkan dukungan penyedia model xAI ke OpenClaw. | `@openclaw/xai-plugin` |   
disertakan dalam OpenClaw | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</id/plugins/reference/xiaomi>) | Menambahkan dukungan penyedia model Xiaomi ke OpenClaw. | `@openclaw/xiaomi-provider` |   
disertakan dalam OpenClaw | providers: xiaomi; contracts: speechProviders |  |   
[zai](</id/plugins/reference/zai>) | Menambahkan dukungan penyedia model [Z.AI](<http://Z.AI>) ke OpenClaw. | `@openclaw/zai-provider` |   
disertakan dalam OpenClaw | providers: zai; contracts: mediaUnderstandingProviders |  |   
[zalo](</id/plugins/reference/zalo>) | Menambahkan permukaan saluran Zalo untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</id/plugins/reference/zalouser>) | Menambahkan permukaan saluran Zalo Personal untuk mengirim dan menerima pesan OpenClaw. | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
Was this useful?YesNo