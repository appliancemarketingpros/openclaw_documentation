---
title: เอกสารอ้างอิง Plugin
source_url: https://docs.openclaw.ai/th/plugins/reference
scraped_at: 2026-05-25
---

# ข้อมูลอ้างอิง Plugin

หน้านี้สร้างจาก `extensions/*/package.json` และ `openclaw.plugin.json` สร้างใหม่ด้วยคำสั่ง:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

Plugin | คำอธิบาย | การแจกจ่าย | พื้นผิว  
---|---|---|---  
[acpx](</th/plugins/reference/acpx>) | แบ็กเอนด์รันไทม์ ACP แบบฝังตัว พร้อมการจัดการเซสชันและการขนส่งที่ Plugin เป็นเจ้าของ. | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[alibaba](</th/plugins/reference/alibaba>) | เพิ่มการรองรับผู้ให้บริการสร้างวิดีโอ. | `@openclaw/alibaba-provider` |   
รวมอยู่ใน OpenClaw | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</th/plugins/reference/amazon-bedrock>) | เพิ่มการรองรับผู้ให้บริการโมเดล Amazon Bedrock ให้กับ OpenClaw. | `@openclaw/amazon-bedrock-provider` |   
รวมอยู่ใน OpenClaw | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</th/plugins/reference/amazon-bedrock-mantle>) | เพิ่มการรองรับผู้ให้บริการโมเดล Amazon Bedrock Mantle ให้กับ OpenClaw. | `@openclaw/amazon-bedrock-mantle-provider` |   
รวมอยู่ใน OpenClaw | providers: amazon-bedrock-mantle |  |   
[anthropic](</th/plugins/reference/anthropic>) | เพิ่มการรองรับผู้ให้บริการโมเดล Anthropic ให้กับ OpenClaw. | `@openclaw/anthropic-provider` |   
รวมอยู่ใน OpenClaw | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</th/plugins/reference/anthropic-vertex>) | เพิ่มการรองรับผู้ให้บริการโมเดล Anthropic Vertex ให้กับ OpenClaw. | `@openclaw/anthropic-vertex-provider` |   
รวมอยู่ใน OpenClaw | providers: anthropic-vertex |  |   
[arcee](</th/plugins/reference/arcee>) | เพิ่มการรองรับผู้ให้บริการโมเดล Arcee ให้กับ OpenClaw. | `@openclaw/arcee-provider` |   
รวมอยู่ใน OpenClaw | providers: arcee |  |   
[azure-speech](</th/plugins/reference/azure-speech>) | Azure AI Speech แบบแปลงข้อความเป็นเสียงพูด (MP3, บันทึกเสียง Ogg/Opus ดั้งเดิม, PCM สำหรับโทรศัพท์). | `@openclaw/azure-speech` |   
รวมอยู่ใน OpenClaw | contracts: speechProviders |  |   
[bonjour](</th/plugins/reference/bonjour>) | ประกาศ Gateway ภายในเครื่องของ OpenClaw ผ่าน Bonjour/mDNS. | `@openclaw/bonjour` |   
รวมอยู่ใน OpenClaw | plugin |  |   
[brave](</th/plugins/reference/brave>) | เพิ่มการรองรับผู้ให้บริการค้นหาเว็บ. | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[browser](</th/plugins/reference/browser>) | เพิ่มเครื่องมือที่เอเจนต์เรียกใช้ได้. | `@openclaw/browser-plugin` |   
รวมอยู่ใน OpenClaw | contracts: tools; skills |  |   
[byteplus](</th/plugins/reference/byteplus>) | เพิ่มการรองรับผู้ให้บริการโมเดล BytePlus, BytePlus Plan ให้กับ OpenClaw. | `@openclaw/byteplus-provider` |   
รวมอยู่ใน OpenClaw | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</th/plugins/reference/canvas>) | พื้นผิวการควบคุม Canvas และการเรนเดอร์ A2UI แบบทดลองสำหรับโหนดที่จับคู่กัน. | `@openclaw/canvas-plugin` |   
รวมอยู่ใน OpenClaw | contracts: tools |  |   
[cerebras](</th/plugins/reference/cerebras>) | เพิ่มการรองรับผู้ให้บริการโมเดล Cerebras ให้กับ OpenClaw. | `@openclaw/cerebras-provider` |   
รวมอยู่ใน OpenClaw | providers: cerebras |  |   
[chutes](</th/plugins/reference/chutes>) | เพิ่มการรองรับผู้ให้บริการโมเดล Chutes ให้กับ OpenClaw. | `@openclaw/chutes-provider` |   
รวมอยู่ใน OpenClaw | providers: chutes |  |   
[clickclack](</th/plugins/reference/clickclack>) | เพิ่มพื้นผิวช่องทาง Clickclack สำหรับส่งและรับข้อความ OpenClaw. | `@openclaw/clickclack` |   
รวมอยู่ใน OpenClaw | channels: clickclack |  |   
[cloudflare-ai-gateway](</th/plugins/reference/cloudflare-ai-gateway>) | เพิ่มการรองรับผู้ให้บริการโมเดล Cloudflare AI Gateway ให้กับ OpenClaw. | `@openclaw/cloudflare-ai-gateway-provider` |   
รวมอยู่ใน OpenClaw | providers: cloudflare-ai-gateway |  |   
[codex](</th/plugins/reference/codex>) | ฮาร์เนสเซิร์ฟเวอร์แอป Codex และแค็ตตาล็อกโมเดล GPT ที่ Codex จัดการ. | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[comfy](</th/plugins/reference/comfy>) | เพิ่มการรองรับผู้ให้บริการโมเดล ComfyUI ให้กับ OpenClaw | `@openclaw/comfy-provider` |   
รวมอยู่ใน OpenClaw | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</th/plugins/reference/copilot-proxy>) | เพิ่มการรองรับผู้ให้บริการโมเดล Copilot Proxy ให้กับ OpenClaw | `@openclaw/copilot-proxy` |   
รวมอยู่ใน OpenClaw | providers: copilot-proxy |  |   
[deepgram](</th/plugins/reference/deepgram>) | เพิ่มการรองรับผู้ให้บริการความเข้าใจสื่อ เพิ่มการรองรับผู้ให้บริการการถอดเสียงแบบเรียลไทม์ | `@openclaw/deepgram-provider` |   
รวมอยู่ใน OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</th/plugins/reference/deepinfra>) | เพิ่มการรองรับผู้ให้บริการโมเดล DeepInfra ให้กับ OpenClaw | `@openclaw/deepinfra-provider` |   
รวมอยู่ใน OpenClaw | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</th/plugins/reference/deepseek>) | เพิ่มการรองรับผู้ให้บริการโมเดล DeepSeek ให้กับ OpenClaw | `@openclaw/deepseek-provider` |   
รวมอยู่ใน OpenClaw | providers: deepseek |  |   
[diagnostics-otel](</th/plugins/reference/diagnostics-otel>) | ตัวส่งออก OpenTelemetry สำหรับการวินิจฉัยของ OpenClaw | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</th/plugins/reference/diagnostics-prometheus>) | ตัวส่งออก Prometheus สำหรับการวินิจฉัยของ OpenClaw | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</th/plugins/reference/diffs>) | ตัวดู diff แบบอ่านอย่างเดียวและตัวเรนเดอร์ไฟล์สำหรับเอเจนต์ | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</th/plugins/reference/discord>) | เพิ่มพื้นผิวช่องทาง Discord สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[document-extract](</th/plugins/reference/document-extract>) | แยกข้อความและรูปภาพหน้าสำรองจากไฟล์แนบเอกสารภายในเครื่อง | `@openclaw/document-extract-plugin` |   
รวมอยู่ใน OpenClaw | contracts: documentExtractors |  |   
[duckduckgo](</th/plugins/reference/duckduckgo>) | เพิ่มการรองรับผู้ให้บริการค้นหาเว็บ | `@openclaw/duckduckgo-plugin` |   
รวมอยู่ใน OpenClaw | contracts: webSearchProviders |  |   
[elevenlabs](</th/plugins/reference/elevenlabs>) | เพิ่มการรองรับผู้ให้บริการความเข้าใจสื่อ เพิ่มการรองรับผู้ให้บริการการถอดเสียงแบบเรียลไทม์ เพิ่มการรองรับผู้ให้บริการแปลงข้อความเป็นเสียงพูด | `@openclaw/elevenlabs-speech` |   
รวมอยู่ใน OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</th/plugins/reference/exa>) | เพิ่มการรองรับผู้ให้บริการค้นหาเว็บ | `@openclaw/exa-plugin` |   
รวมอยู่ใน OpenClaw | contracts: webSearchProviders |  |   
[fal](</th/plugins/reference/fal>) | เพิ่มการรองรับผู้ให้บริการโมเดล fal ให้กับ OpenClaw | `@openclaw/fal-provider` |   
รวมอยู่ใน OpenClaw | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[feishu](</th/plugins/reference/feishu>) | เพิ่มพื้นผิวช่องทาง Feishu สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[file-transfer](</th/plugins/reference/file-transfer>) | ดึงข้อมูล แสดงรายการ และเขียนไฟล์บนโหนดที่จับคู่ผ่านคำสั่งโหนดเฉพาะ เลี่ยงการตัดทอน stdout ของ bash โดยใช้ base64 ผ่าน node.invoke สำหรับไบนารีขนาดสูงสุด 16 MB | `@openclaw/file-transfer` |   
รวมอยู่ใน OpenClaw | contracts: tools |  |   
[firecrawl](</th/plugins/reference/firecrawl>) | เพิ่มเครื่องมือที่เอเจนต์เรียกใช้ได้ เพิ่มการรองรับผู้ให้บริการดึงข้อมูลจากเว็บ เพิ่มการรองรับผู้ให้บริการค้นหาเว็บ | `@openclaw/firecrawl-plugin` |   
รวมอยู่ใน OpenClaw | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</th/plugins/reference/fireworks>) | เพิ่มการรองรับผู้ให้บริการโมเดล Fireworks ให้กับ OpenClaw | `@openclaw/fireworks-provider` |   
รวมอยู่ใน OpenClaw | providers: fireworks |  |   
[github-copilot](</th/plugins/reference/github-copilot>) | เพิ่มการรองรับผู้ให้บริการโมเดล GitHub Copilot ให้กับ OpenClaw | `@openclaw/github-copilot-provider` |   
รวมอยู่ใน OpenClaw | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</th/plugins/reference/google>) | เพิ่มการรองรับผู้ให้บริการโมเดล Google, Google Gemini CLI, Google Vertex ให้กับ OpenClaw | `@openclaw/google-plugin` |   
รวมอยู่ใน OpenClaw | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[google-meet](</th/plugins/reference/google-meet>) | เข้าร่วมสาย Google Meet ผ่านการขนส่งของ Chrome หรือ Twilio | `@openclaw/google-meet` |   
npm; ClawHub | สัญญา: เครื่องมือ |  |   
[googlechat](</th/plugins/reference/googlechat>) | เพิ่มพื้นผิวช่องทาง Google Chat สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/googlechat` |   
npm; ClawHub | ช่องทาง: googlechat |  |   
[gradium](</th/plugins/reference/gradium>) | เพิ่มการรองรับผู้ให้บริการแปลงข้อความเป็นเสียง | `@openclaw/gradium-speech` |   
รวมอยู่ใน OpenClaw | สัญญา: speechProviders |  |   
[groq](</th/plugins/reference/groq>) | เพิ่มการรองรับผู้ให้บริการโมเดล Groq ให้กับ OpenClaw | `@openclaw/groq-provider` |   
รวมอยู่ใน OpenClaw | ผู้ให้บริการ: groq; สัญญา: mediaUnderstandingProviders |  |   
[huggingface](</th/plugins/reference/huggingface>) | เพิ่มการรองรับผู้ให้บริการโมเดล Hugging Face ให้กับ OpenClaw | `@openclaw/huggingface-provider` |   
รวมอยู่ใน OpenClaw | ผู้ให้บริการ: huggingface |  |   
[imessage](</th/plugins/reference/imessage>) | เพิ่มพื้นผิวช่องทาง iMessage สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/imessage` |   
รวมอยู่ใน OpenClaw | ช่องทาง: imessage |  |   
[inworld](</th/plugins/reference/inworld>) | การแปลงข้อความเป็นเสียงแบบสตรีมมิงของ Inworld (MP3, OGG_OPUS, PCM telephony) | `@openclaw/inworld-speech` |   
รวมอยู่ใน OpenClaw | สัญญา: speechProviders |  |   
[irc](</th/plugins/reference/irc>) | เพิ่มพื้นผิวช่องทาง IRC สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/irc` |   
รวมอยู่ใน OpenClaw | ช่องทาง: irc |  |   
[kilocode](</th/plugins/reference/kilocode>) | เพิ่มการรองรับผู้ให้บริการโมเดล Kilocode ให้กับ OpenClaw | `@openclaw/kilocode-provider` |   
รวมอยู่ใน OpenClaw | ผู้ให้บริการ: kilocode |  |   
[kimi](</th/plugins/reference/kimi>) | เพิ่มการรองรับผู้ให้บริการโมเดล Kimi, Kimi Coding ให้กับ OpenClaw | `@openclaw/kimi-provider` |   
รวมอยู่ใน OpenClaw | ผู้ให้บริการ: kimi, kimi-coding |  |   
[line](</th/plugins/reference/line>) | เพิ่มพื้นผิวช่องทาง LINE สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/line` |   
npm; ClawHub | ช่องทาง: line |  |   
[litellm](</th/plugins/reference/litellm>) | เพิ่มการรองรับผู้ให้บริการโมเดล LiteLLM ให้กับ OpenClaw | `@openclaw/litellm-provider` |   
รวมอยู่ใน OpenClaw | ผู้ให้บริการ: litellm; สัญญา: imageGenerationProviders |  |   
[llm-task](</th/plugins/reference/llm-task>) | เครื่องมือ LLM แบบ JSON เท่านั้นทั่วไปสำหรับงานที่มีโครงสร้าง ซึ่งเรียกใช้ได้จากเวิร์กโฟลว์ | `@openclaw/llm-task` |   
รวมอยู่ใน OpenClaw | สัญญา: เครื่องมือ |  |   
[lmstudio](</th/plugins/reference/lmstudio>) | เพิ่มการรองรับผู้ให้บริการโมเดล LM Studio ให้กับ OpenClaw | `@openclaw/lmstudio-provider` |   
รวมอยู่ใน OpenClaw | ผู้ให้บริการ: lmstudio; สัญญา: memoryEmbeddingProviders |  |   
[lobster](</th/plugins/reference/lobster>) | เครื่องมือเวิร์กโฟลว์แบบมีชนิดพร้อมการอนุมัติที่ดำเนินต่อได้ | `@openclaw/lobster` |   
npm; ClawHub | สัญญา: เครื่องมือ |  |   
[matrix](</th/plugins/reference/matrix>) | เพิ่มพื้นผิวช่องทาง Matrix สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | ช่องทาง: matrix |  |   
[mattermost](</th/plugins/reference/mattermost>) | เพิ่มพื้นผิวช่องทาง Mattermost สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/mattermost` |   
รวมอยู่ใน OpenClaw | ช่องทาง: mattermost |  |   
[memory-core](</th/plugins/reference/memory-core>) | เพิ่มการรองรับผู้ให้บริการฝังหน่วยความจำ เพิ่มเครื่องมือที่เอเจนต์เรียกใช้ได้ | `@openclaw/memory-core` |   
รวมอยู่ใน OpenClaw | สัญญา: memoryEmbeddingProviders, เครื่องมือ |  |   
[memory-lancedb](</th/plugins/reference/memory-lancedb>) | เพิ่มเครื่องมือที่เอเจนต์เรียกใช้ได้ | `@openclaw/memory-lancedb` |   
npm; ClawHub | สัญญา: เครื่องมือ |  |   
[memory-wiki](</th/plugins/reference/memory-wiki>) | คอมไพเลอร์วิกิถาวรและคลังความรู้ที่เป็นมิตรกับ Obsidian สำหรับ OpenClaw | `@openclaw/memory-wiki` |   
รวมอยู่ใน OpenClaw | สัญญา: เครื่องมือ; skills |  |   
[microsoft](</th/plugins/reference/microsoft>) | เพิ่มการรองรับผู้ให้บริการแปลงข้อความเป็นเสียงพูด | `@openclaw/microsoft-speech` |   
รวมอยู่ใน OpenClaw | contracts: speechProviders |  |   
[microsoft-foundry](</th/plugins/reference/microsoft-foundry>) | เพิ่มการรองรับผู้ให้บริการโมเดล Microsoft Foundry ให้กับ OpenClaw | `@openclaw/microsoft-foundry` |   
รวมอยู่ใน OpenClaw | providers: microsoft-foundry |  |   
[migrate-claude](</th/plugins/reference/migrate-claude>) | นำเข้าคำแนะนำของ Claude Code และ Claude Desktop, เซิร์ฟเวอร์ MCP, Skills และการกำหนดค่าที่ปลอดภัยเข้าสู่ OpenClaw | `@openclaw/migrate-claude` |   
รวมอยู่ใน OpenClaw | contracts: migrationProviders |  |   
[migrate-hermes](</th/plugins/reference/migrate-hermes>) | นำเข้าการกำหนดค่า Hermes, หน่วยความจำ, Skills และข้อมูลรับรองที่รองรับเข้าสู่ OpenClaw | `@openclaw/migrate-hermes` |   
รวมอยู่ใน OpenClaw | contracts: migrationProviders |  |   
[minimax](</th/plugins/reference/minimax>) | เพิ่มการรองรับผู้ให้บริการโมเดล MiniMax, MiniMax Portal ให้กับ OpenClaw | `@openclaw/minimax-provider` |   
รวมอยู่ใน OpenClaw | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</th/plugins/reference/mistral>) | เพิ่มการรองรับผู้ให้บริการโมเดล Mistral ให้กับ OpenClaw | `@openclaw/mistral-provider` |   
รวมอยู่ใน OpenClaw | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</th/plugins/reference/moonshot>) | เพิ่มการรองรับผู้ให้บริการโมเดล Moonshot ให้กับ OpenClaw | `@openclaw/moonshot-provider` |   
รวมอยู่ใน OpenClaw | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[msteams](</th/plugins/reference/msteams>) | เพิ่มพื้นผิวช่องทาง Microsoft Teams สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</th/plugins/reference/nextcloud-talk>) | เพิ่มพื้นผิวช่องทาง Nextcloud Talk สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</th/plugins/reference/nostr>) | เพิ่มพื้นผิวช่องทาง Nostr สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[nvidia](</th/plugins/reference/nvidia>) | เพิ่มการรองรับผู้ให้บริการโมเดล NVIDIA ให้กับ OpenClaw | `@openclaw/nvidia-provider` |   
รวมอยู่ใน OpenClaw | providers: nvidia |  |   
[oc-path](</th/plugins/reference/oc-path>) | เพิ่ม openclaw path CLI สำหรับการอ้างที่อยู่ไฟล์พื้นที่ทำงานแบบ oc:// | `@openclaw/oc-path` |   
รวมอยู่ใน OpenClaw | plugin |  |   
[ollama](</th/plugins/reference/ollama>) | เพิ่มการรองรับผู้ให้บริการโมเดล Ollama ให้กับ OpenClaw | `@openclaw/ollama-provider` |   
รวมอยู่ใน OpenClaw | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</th/plugins/reference/open-prose>) | OpenProse VM skill pack พร้อมคำสั่ง slash /prose | `@openclaw/open-prose` |   
รวมอยู่ใน OpenClaw | skills |  |   
[openai](</th/plugins/reference/openai>) | เพิ่มการรองรับผู้ให้บริการโมเดล OpenAI, OpenAI Codex ให้กับ OpenClaw | `@openclaw/openai-provider` |   
รวมอยู่ใน OpenClaw | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</th/plugins/reference/opencode>) | เพิ่มการรองรับผู้ให้บริการโมเดล OpenCode ให้กับ OpenClaw | `@openclaw/opencode-provider` |   
รวมอยู่ใน OpenClaw | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</th/plugins/reference/opencode-go>) | เพิ่มการรองรับผู้ให้บริการโมเดล OpenCode Go ให้กับ OpenClaw | `@openclaw/opencode-go-provider` |   
รวมอยู่ใน OpenClaw | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</th/plugins/reference/openrouter>) | เพิ่มการรองรับผู้ให้บริการโมเดล OpenRouter ให้กับ OpenClaw | `@openclaw/openrouter-provider` |   
รวมอยู่ใน OpenClaw | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</th/plugins/reference/openshell>) | แบ็กเอนด์แซนด์บ็อกซ์ที่ขับเคลื่อนโดย OpenShell พร้อมพื้นที่ทำงานภายในเครื่องที่มิเรอร์กันและการดำเนินคำสั่งผ่าน SSH | `@openclaw/openshell-sandbox` |   
รวมอยู่ใน OpenClaw | plugin |  |   
[perplexity](</th/plugins/reference/perplexity>) | เพิ่มการรองรับผู้ให้บริการค้นหาเว็บ | `@openclaw/perplexity-plugin` |   
รวมอยู่ใน OpenClaw | contracts: webSearchProviders |  |   
[qa-channel](</th/plugins/reference/qa-channel>) | เพิ่มพื้นผิวช่องทาง QA สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/qa-channel` |   
เฉพาะการ checkout ซอร์ส | channels: qa-channel |  |   
[qa-lab](</th/plugins/reference/qa-lab>) | Plugin แล็บ QA ของ OpenClaw พร้อม UI ดีบักเกอร์ส่วนตัวและตัวรันสถานการณ์ | `@openclaw/qa-lab` |   
เฉพาะการ checkout ซอร์ส | plugin |  |   
[qa-matrix](</th/plugins/reference/qa-matrix>) | ตัวรันและฐานรองรับทรานสปอร์ต Matrix QA | `@openclaw/qa-matrix` |   
เฉพาะการ checkout ซอร์ส | plugin |  |   
[qianfan](</th/plugins/reference/qianfan>) | เพิ่มการรองรับผู้ให้บริการโมเดล Qianfan ให้กับ OpenClaw | `@openclaw/qianfan-provider` |   
รวมอยู่ใน OpenClaw | providers: qianfan |  |   
[qqbot](</th/plugins/reference/qqbot>) | เพิ่มพื้นผิวช่องทาง QQ Bot สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[qwen](</th/plugins/reference/qwen>) | เพิ่มการรองรับผู้ให้บริการโมเดล Qwen, Qwen Cloud, Model Studio, DashScope ให้กับ OpenClaw | `@openclaw/qwen-provider` |   
รวมอยู่ใน OpenClaw | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</th/plugins/reference/runway>) | เพิ่มการรองรับผู้ให้บริการสร้างวิดีโอ | `@openclaw/runway-provider` |   
รวมอยู่ใน OpenClaw | contracts: videoGenerationProviders |  |   
[searxng](</th/plugins/reference/searxng>) | เพิ่มการรองรับผู้ให้บริการค้นเว็บ | `@openclaw/searxng-plugin` |   
รวมอยู่ใน OpenClaw | contracts: webSearchProviders |  |   
[senseaudio](</th/plugins/reference/senseaudio>) | เพิ่มการรองรับผู้ให้บริการทำความเข้าใจสื่อ | `@openclaw/senseaudio-provider` |   
รวมอยู่ใน OpenClaw | contracts: mediaUnderstandingProviders |  |   
[sglang](</th/plugins/reference/sglang>) | เพิ่มการรองรับผู้ให้บริการโมเดล SGLang ให้กับ OpenClaw | `@openclaw/sglang-provider` |   
รวมอยู่ใน OpenClaw | providers: sglang |  |   
[signal](</th/plugins/reference/signal>) | เพิ่มพื้นผิวช่องทาง Signal สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/signal` |   
รวมอยู่ใน OpenClaw | channels: signal |  |   
[skill-workshop](</th/plugins/reference/skill-workshop>) | จับเวิร์กโฟลว์ที่ทำซ้ำได้เป็น Skills ของเวิร์กสเปซ พร้อมการรอตรวจสอบ การเขียนอย่างปลอดภัย และการรีเฟรชพรอมป์ของ Skills | `@openclaw/skill-workshop` |   
รวมอยู่ใน OpenClaw | contracts: tools |  |   
[slack](</th/plugins/reference/slack>) | เพิ่มพื้นผิวช่องทาง Slack สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/slack` |   
รวมอยู่ใน OpenClaw | channels: slack |  |   
[stepfun](</th/plugins/reference/stepfun>) | เพิ่มการรองรับผู้ให้บริการโมเดล StepFun, StepFun Plan ให้กับ OpenClaw | `@openclaw/stepfun-provider` |   
รวมอยู่ใน OpenClaw | providers: stepfun, stepfun-plan |  |   
[synology-chat](</th/plugins/reference/synology-chat>) | เพิ่มพื้นผิวช่องทาง Synology Chat สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[synthetic](</th/plugins/reference/synthetic>) | เพิ่มการรองรับผู้ให้บริการโมเดล Synthetic ให้กับ OpenClaw | `@openclaw/synthetic-provider` |   
รวมอยู่ใน OpenClaw | providers: synthetic |  |   
[tavily](</th/plugins/reference/tavily>) | เพิ่มเครื่องมือที่เอเจนต์เรียกใช้ได้ เพิ่มการรองรับผู้ให้บริการค้นเว็บ | `@openclaw/tavily-plugin` |   
รวมอยู่ใน OpenClaw | contracts: tools, webSearchProviders; skills |  |   
[telegram](</th/plugins/reference/telegram>) | เพิ่มพื้นผิวช่องทาง Telegram สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/telegram` |   
รวมอยู่ใน OpenClaw | channels: telegram |  |   
[tencent](</th/plugins/reference/tencent>) | เพิ่มการรองรับผู้ให้บริการโมเดล Tencent TokenHub ให้กับ OpenClaw | `@openclaw/tencent-provider` |   
รวมอยู่ใน OpenClaw | providers: tencent-tokenhub |  |   
[tlon](</th/plugins/reference/tlon>) | เพิ่มพื้นผิวช่องทาง Tlon สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[together](</th/plugins/reference/together>) | เพิ่มการรองรับผู้ให้บริการโมเดล Together ให้กับ OpenClaw | `@openclaw/together-provider` |   
รวมอยู่ใน OpenClaw | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</th/plugins/reference/tokenjuice>) | บีบอัดผลลัพธ์เครื่องมือ exec และ bash ด้วยตัวลดขนาดของ tokenjuice | `@openclaw/tokenjuice` |   
รวมอยู่ใน OpenClaw | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</th/plugins/reference/tts-local-cli>) | เพิ่มการรองรับผู้ให้บริการแปลงข้อความเป็นเสียงพูด | `@openclaw/tts-local-cli` |   
รวมอยู่ใน OpenClaw | contracts: speechProviders |  |   
[twitch](</th/plugins/reference/twitch>) | เพิ่มอินเทอร์เฟซช่องทาง Twitch สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[venice](</th/plugins/reference/venice>) | เพิ่มการรองรับผู้ให้บริการโมเดล Venice ให้กับ OpenClaw | `@openclaw/venice-provider` |   
รวมอยู่ใน OpenClaw | providers: venice |  |   
[vercel-ai-gateway](</th/plugins/reference/vercel-ai-gateway>) | เพิ่มการรองรับผู้ให้บริการโมเดล Vercel AI Gateway ให้กับ OpenClaw | `@openclaw/vercel-ai-gateway-provider` |   
รวมอยู่ใน OpenClaw | providers: vercel-ai-gateway |  |   
[vllm](</th/plugins/reference/vllm>) | เพิ่มการรองรับผู้ให้บริการโมเดล vLLM ให้กับ OpenClaw | `@openclaw/vllm-provider` |   
รวมอยู่ใน OpenClaw | providers: vllm |  |   
[voice-call](</th/plugins/reference/voice-call>) | เพิ่มเครื่องมือที่เอเจนต์เรียกใช้ได้ | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[volcengine](</th/plugins/reference/volcengine>) | เพิ่มการรองรับผู้ให้บริการโมเดล Volcengine, Volcengine Plan ให้กับ OpenClaw | `@openclaw/volcengine-provider` |   
รวมอยู่ใน OpenClaw | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</th/plugins/reference/voyage>) | เพิ่มการรองรับผู้ให้บริการเอ็มเบดดิ้งหน่วยความจำ | `@openclaw/voyage-provider` |   
รวมอยู่ใน OpenClaw | contracts: memoryEmbeddingProviders |  |   
[vydra](</th/plugins/reference/vydra>) | เพิ่มการรองรับผู้ให้บริการโมเดล Vydra ให้กับ OpenClaw | `@openclaw/vydra-provider` |   
รวมอยู่ใน OpenClaw | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</th/plugins/reference/web-readability>) | ดึงเนื้อหาบทความที่อ่านง่ายจากการตอบกลับการดึงเว็บ HTML ในเครื่อง | `@openclaw/web-readability-plugin` |   
รวมอยู่ใน OpenClaw | contracts: webContentExtractors |  |   
[webhooks](</th/plugins/reference/webhooks>) | Webhook ขาเข้าที่ตรวจสอบสิทธิ์แล้ว ซึ่งผูกระบบอัตโนมัติภายนอกเข้ากับ OpenClaw TaskFlows | `@openclaw/webhooks` |   
รวมอยู่ใน OpenClaw | plugin |  |   
[whatsapp](</th/plugins/reference/whatsapp>) | เพิ่มอินเทอร์เฟซช่องทาง WhatsApp สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[xai](</th/plugins/reference/xai>) | เพิ่มการรองรับผู้ให้บริการโมเดล xAI ให้กับ OpenClaw | `@openclaw/xai-plugin` |   
รวมอยู่ใน OpenClaw | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</th/plugins/reference/xiaomi>) | เพิ่มการรองรับผู้ให้บริการโมเดล Xiaomi ให้กับ OpenClaw | `@openclaw/xiaomi-provider` |   
รวมอยู่ใน OpenClaw | providers: xiaomi; contracts: speechProviders |  |   
[zai](</th/plugins/reference/zai>) | เพิ่มการรองรับผู้ให้บริการโมเดล [Z.AI](<http://Z.AI>) ให้กับ OpenClaw | `@openclaw/zai-provider` |   
รวมอยู่ใน OpenClaw | providers: zai; contracts: mediaUnderstandingProviders |  |   
[zalo](</th/plugins/reference/zalo>) | เพิ่มอินเทอร์เฟซช่องทาง Zalo สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</th/plugins/reference/zalouser>) | เพิ่มอินเทอร์เฟซช่องทาง Zalo Personal สำหรับส่งและรับข้อความ OpenClaw | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
Was this useful?YesNo