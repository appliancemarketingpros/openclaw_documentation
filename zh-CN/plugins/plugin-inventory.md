---
title: 插件清册
source_url: https://docs.openclaw.ai/zh-CN/plugins/plugin-inventory
scraped_at: 2026-05-25
---

# 插件清单

此页面由 `extensions/*/package.json`、`openclaw.plugin.json` 以及根 npm 包的 `files` 排除项生成。使用以下命令重新生成：

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

## 定义

  * **核心 npm 包：** 内置于 `openclaw` npm 包中，无需单独安装插件即可使用。
  * **官方外部包：** OpenClaw 维护的插件，未包含在核心 npm 包中，保留在此官方清单中，并可按需通过 ClawHub 和/或 npm 安装。
  * **仅源码检出：** 仓库本地插件，未包含在已发布的 npm 构件中，也不会作为可安装包宣传。


源码检出不同于 npm 安装：执行 `pnpm install` 后，内置 插件会从 `extensions/<id>` 加载，因此本地编辑和包本地 workspace 依赖都可用。

## 安装插件

使用 **分发方式** 列来判断是否需要安装。标为 `included in OpenClaw` 的插件已经存在于核心包中。官方 外部包需要安装一次，然后重启 Gateway 网关。

例如，Discord 是一个官方外部包：

bashCopy code
[code]
    openclaw plugins install @openclaw/discordopenclaw gateway restartopenclaw plugins inspect discord --runtime --json
[/code]

裸包规格会先尝试 ClawHub，然后回退到 npm。若要强制指定来源，请使用 `clawhub:@openclaw/discord` 或 `npm:@openclaw/discord`。安装后，按照 该插件的设置文档（例如 [Discord](</zh-CN/channels/discord>)）添加凭证 和渠道配置。有关更新、卸载和发布命令，请参阅 [管理插件](</zh-CN/plugins/manage-plugins>)。

## 核心 npm 包

插件 | 描述 | 分发 | 接口面  
---|---|---|---  
[alibaba](</zh-CN/plugins/reference/alibaba>) | 添加视频生成提供商支持。 | `@openclaw/alibaba-provider` |   
包含在 OpenClaw 中 | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</zh-CN/plugins/reference/amazon-bedrock>) | 为 OpenClaw 添加 Amazon Bedrock 模型提供商支持。 | `@openclaw/amazon-bedrock-provider` |   
包含在 OpenClaw 中 | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</zh-CN/plugins/reference/amazon-bedrock-mantle>) | 为 OpenClaw 添加 Amazon Bedrock Mantle 模型提供商支持。 | `@openclaw/amazon-bedrock-mantle-provider` |   
包含在 OpenClaw 中 | providers: amazon-bedrock-mantle |  |   
[anthropic](</zh-CN/plugins/reference/anthropic>) | 为 OpenClaw 添加 Anthropic 模型提供商支持。 | `@openclaw/anthropic-provider` |   
包含在 OpenClaw 中 | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</zh-CN/plugins/reference/anthropic-vertex>) | 为 OpenClaw 添加 Anthropic Vertex 模型提供商支持。 | `@openclaw/anthropic-vertex-provider` |   
包含在 OpenClaw 中 | providers: anthropic-vertex |  |   
[arcee](</zh-CN/plugins/reference/arcee>) | 为 OpenClaw 添加 Arcee 模型提供商支持。 | `@openclaw/arcee-provider` |   
包含在 OpenClaw 中 | providers: arcee |  |   
[azure-speech](</zh-CN/plugins/reference/azure-speech>) | Azure AI Speech 文本转语音（MP3、原生 Ogg/Opus 语音便条、PCM 电话音频）。 | `@openclaw/azure-speech` |   
包含在 OpenClaw 中 | contracts: speechProviders |  |   
[bonjour](</zh-CN/plugins/reference/bonjour>) | 通过 Bonjour/mDNS 公布本地 OpenClaw gateway。 | `@openclaw/bonjour` |   
包含在 OpenClaw 中 | plugin |  |   
[browser](</zh-CN/plugins/reference/browser>) | 添加可由智能体调用的工具。 | `@openclaw/browser-plugin` |   
包含在 OpenClaw 中 | contracts: tools; skills |  |   
[byteplus](</zh-CN/plugins/reference/byteplus>) | 为 OpenClaw 添加 BytePlus、BytePlus Plan 模型提供商支持。 | `@openclaw/byteplus-provider` |   
包含在 OpenClaw 中 | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</zh-CN/plugins/reference/canvas>) | 为已配对节点提供实验性 Canvas 控制和 A2UI 渲染接口面。 | `@openclaw/canvas-plugin` |   
包含在 OpenClaw 中 | contracts: tools |  |   
[cerebras](</zh-CN/plugins/reference/cerebras>) | 为 OpenClaw 添加 Cerebras 模型提供商支持。 | `@openclaw/cerebras-provider` |   
包含在 OpenClaw 中 | providers: cerebras |  |   
[chutes](</zh-CN/plugins/reference/chutes>) | 为 OpenClaw 添加 Chutes 模型提供商支持。 | `@openclaw/chutes-provider` |   
包含在 OpenClaw 中 | providers: chutes |  |   
[clickclack](</zh-CN/plugins/reference/clickclack>) | 添加用于发送和接收 OpenClaw 消息的 Clickclack 频道接口面。 | `@openclaw/clickclack` |   
包含在 OpenClaw 中 | channels: clickclack |  |   
[cloudflare-ai-gateway](</zh-CN/plugins/reference/cloudflare-ai-gateway>) | 为 OpenClaw 添加 Cloudflare AI Gateway 模型提供商支持。 | `@openclaw/cloudflare-ai-gateway-provider` |   
包含在 OpenClaw 中 | providers: cloudflare-ai-gateway |  |   
[comfy](</zh-CN/plugins/reference/comfy>) | 为 OpenClaw 添加 ComfyUI 模型提供商支持。 | `@openclaw/comfy-provider` |   
包含在 OpenClaw 中 | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</zh-CN/plugins/reference/copilot-proxy>) | 为 OpenClaw 添加 Copilot Proxy 模型提供商支持。 | `@openclaw/copilot-proxy` |   
包含在 OpenClaw 中 | providers: copilot-proxy |  |   
[deepgram](</zh-CN/plugins/reference/deepgram>) | 添加媒体理解提供商支持。添加实时转录提供商支持。 | `@openclaw/deepgram-provider` |   
包含在 OpenClaw 中 | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</zh-CN/plugins/reference/deepinfra>) | 为 OpenClaw 添加 DeepInfra 模型提供商支持。 | `@openclaw/deepinfra-provider` |   
包含在 OpenClaw 中 | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</zh-CN/plugins/reference/deepseek>) | 为 OpenClaw 添加 DeepSeek 模型提供商支持。 | `@openclaw/deepseek-provider` |   
OpenClaw 内置 | providers: deepseek |  |   
[document-extract](</zh-CN/plugins/reference/document-extract>) | 从本地文档附件中提取文本和备用页面图像。 | `@openclaw/document-extract-plugin` |   
OpenClaw 内置 | contracts: documentExtractors |  |   
[duckduckgo](</zh-CN/plugins/reference/duckduckgo>) | 添加 Web 搜索提供商支持。 | `@openclaw/duckduckgo-plugin` |   
OpenClaw 内置 | contracts: webSearchProviders |  |   
[elevenlabs](</zh-CN/plugins/reference/elevenlabs>) | 添加媒体理解提供商支持。添加实时转录提供商支持。添加文本转语音提供商支持。 | `@openclaw/elevenlabs-speech` |   
OpenClaw 内置 | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</zh-CN/plugins/reference/exa>) | 添加 Web 搜索提供商支持。 | `@openclaw/exa-plugin` |   
OpenClaw 内置 | contracts: webSearchProviders |  |   
[fal](</zh-CN/plugins/reference/fal>) | 为 OpenClaw 添加 fal 模型提供商支持。 | `@openclaw/fal-provider` |   
OpenClaw 内置 | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[file-transfer](</zh-CN/plugins/reference/file-transfer>) | 通过专用节点命令在已配对节点上获取、列出和写入文件。通过对最大 16 MB 的二进制文件在 node.invoke 上使用 base64，绕过 bash stdout 截断。 | `@openclaw/file-transfer` |   
OpenClaw 内置 | contracts: tools |  |   
[firecrawl](</zh-CN/plugins/reference/firecrawl>) | 添加可由智能体调用的工具。添加 Web 获取提供商支持。添加 Web 搜索提供商支持。 | `@openclaw/firecrawl-plugin` |   
OpenClaw 内置 | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</zh-CN/plugins/reference/fireworks>) | 为 OpenClaw 添加 Fireworks 模型提供商支持。 | `@openclaw/fireworks-provider` |   
OpenClaw 内置 | providers: fireworks |  |   
[github-copilot](</zh-CN/plugins/reference/github-copilot>) | 为 OpenClaw 添加 GitHub Copilot 模型提供商支持。 | `@openclaw/github-copilot-provider` |   
OpenClaw 内置 | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</zh-CN/plugins/reference/google>) | 为 OpenClaw 添加 Google、Google Gemini CLI、Google Vertex 模型提供商支持。 | `@openclaw/google-plugin` |   
OpenClaw 内置 | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[gradium](</zh-CN/plugins/reference/gradium>) | 添加文本转语音提供商支持。 | `@openclaw/gradium-speech` |   
OpenClaw 内置 | contracts: speechProviders |  |   
[groq](</zh-CN/plugins/reference/groq>) | 为 OpenClaw 添加 Groq 模型提供商支持。 | `@openclaw/groq-provider` |   
OpenClaw 内置 | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</zh-CN/plugins/reference/huggingface>) | 为 OpenClaw 添加 Hugging Face 模型提供商支持。 | `@openclaw/huggingface-provider` |   
OpenClaw 内置 | providers: huggingface |  |   
[imessage](</zh-CN/plugins/reference/imessage>) | 添加用于发送和接收 OpenClaw 消息的 iMessage 渠道表面。 | `@openclaw/imessage` |   
OpenClaw 内置 | channels: imessage |  |   
[inworld](</zh-CN/plugins/reference/inworld>) | Inworld 流式文本转语音（MP3、OGG_OPUS、PCM 电话音频）。 | `@openclaw/inworld-speech` |   
OpenClaw 内置 | contracts: speechProviders |  |   
[irc](</zh-CN/plugins/reference/irc>) | 添加用于发送和接收 OpenClaw 消息的 IRC 渠道表面。 | `@openclaw/irc` |   
OpenClaw 内置 | channels: irc |  |   
[kilocode](</zh-CN/plugins/reference/kilocode>) | 为 OpenClaw 添加 Kilocode 模型提供商支持。 | `@openclaw/kilocode-provider` |   
OpenClaw 内置 | providers: kilocode |  |   
[kimi](</zh-CN/plugins/reference/kimi>) | 为 OpenClaw 添加 Kimi、Kimi Coding 模型提供商支持。 | `@openclaw/kimi-provider` |   
OpenClaw 内置 | providers: kimi, kimi-coding |  |   
[litellm](</zh-CN/plugins/reference/litellm>) | 为 OpenClaw 添加 LiteLLM 模型提供商支持。 | `@openclaw/litellm-provider` |   
OpenClaw 内置 | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</zh-CN/plugins/reference/llm-task>) | 用于结构化任务的通用、仅 JSON 的 LLM 工具，可从工作流调用。 | `@openclaw/llm-task` |   
OpenClaw 内置 | contracts: tools |  |   
[lmstudio](</zh-CN/plugins/reference/lmstudio>) | 为 OpenClaw 添加 LM Studio 模型提供商支持。 | `@openclaw/lmstudio-provider` |   
包含在 OpenClaw 中 | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[mattermost](</zh-CN/plugins/reference/mattermost>) | 添加 Mattermost 渠道界面，用于发送和接收 OpenClaw 消息。 | `@openclaw/mattermost` |   
包含在 OpenClaw 中 | channels: mattermost |  |   
[memory-core](</zh-CN/plugins/reference/memory-core>) | 添加记忆嵌入提供商支持。添加可由智能体调用的工具。 | `@openclaw/memory-core` |   
包含在 OpenClaw 中 | contracts: memoryEmbeddingProviders, tools |  |   
[memory-wiki](</zh-CN/plugins/reference/memory-wiki>) | 面向 OpenClaw 的持久化 wiki 编译器和 Obsidian 友好的知识库。 | `@openclaw/memory-wiki` |   
包含在 OpenClaw 中 | contracts: tools; skills |  |   
[microsoft](</zh-CN/plugins/reference/microsoft>) | 添加文本转语音提供商支持。 | `@openclaw/microsoft-speech` |   
包含在 OpenClaw 中 | contracts: speechProviders |  |   
[microsoft-foundry](</zh-CN/plugins/reference/microsoft-foundry>) | 为 OpenClaw 添加 Microsoft Foundry 模型提供商支持。 | `@openclaw/microsoft-foundry` |   
包含在 OpenClaw 中 | providers: microsoft-foundry |  |   
[migrate-claude](</zh-CN/plugins/reference/migrate-claude>) | 将 Claude Code 和 Claude Desktop 指令、MCP 服务器、技能以及安全配置导入 OpenClaw。 | `@openclaw/migrate-claude` |   
包含在 OpenClaw 中 | contracts: migrationProviders |  |   
[migrate-hermes](</zh-CN/plugins/reference/migrate-hermes>) | 将 Hermes 配置、记忆、技能和受支持的凭证导入 OpenClaw。 | `@openclaw/migrate-hermes` |   
包含在 OpenClaw 中 | contracts: migrationProviders |  |   
[minimax](</zh-CN/plugins/reference/minimax>) | 为 OpenClaw 添加 MiniMax、MiniMax Portal 模型提供商支持。 | `@openclaw/minimax-provider` |   
包含在 OpenClaw 中 | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</zh-CN/plugins/reference/mistral>) | 为 OpenClaw 添加 Mistral 模型提供商支持。 | `@openclaw/mistral-provider` |   
包含在 OpenClaw 中 | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</zh-CN/plugins/reference/moonshot>) | 为 OpenClaw 添加 Moonshot 模型提供商支持。 | `@openclaw/moonshot-provider` |   
包含在 OpenClaw 中 | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[nvidia](</zh-CN/plugins/reference/nvidia>) | 为 OpenClaw 添加 NVIDIA 模型提供商支持。 | `@openclaw/nvidia-provider` |   
包含在 OpenClaw 中 | providers: nvidia |  |   
[oc-path](</zh-CN/plugins/reference/oc-path>) | 添加用于 oc:// 工作区文件寻址的 openclaw path CLI。 | `@openclaw/oc-path` |   
包含在 OpenClaw 中 | plugin |  |   
[ollama](</zh-CN/plugins/reference/ollama>) | 为 OpenClaw 添加 Ollama 模型提供商支持。 | `@openclaw/ollama-provider` |   
包含在 OpenClaw 中 | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</zh-CN/plugins/reference/open-prose>) | 带有 /prose 斜杠命令的 OpenProse VM 技能包。 | `@openclaw/open-prose` |   
包含在 OpenClaw 中 | skills |  |   
[openai](</zh-CN/plugins/reference/openai>) | 为 OpenClaw 添加 OpenAI、OpenAI Codex 模型提供商支持。 | `@openclaw/openai-provider` |   
包含在 OpenClaw 中 | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</zh-CN/plugins/reference/opencode>) | 为 OpenClaw 添加 OpenCode 模型提供商支持。 | `@openclaw/opencode-provider` |   
包含在 OpenClaw 中 | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</zh-CN/plugins/reference/opencode-go>) | 为 OpenClaw 添加 OpenCode Go 模型提供商支持。 | `@openclaw/opencode-go-provider` |   
包含在 OpenClaw 中 | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</zh-CN/plugins/reference/openrouter>) | 为 OpenClaw 添加 OpenRouter 模型提供商支持。 | `@openclaw/openrouter-provider` |   
包含在 OpenClaw 中 | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</zh-CN/plugins/reference/openshell>) | 由 OpenShell 提供支持的沙箱后端，具备镜像本地工作区和基于 SSH 的命令执行。 | `@openclaw/openshell-sandbox` |   
包含在 OpenClaw 中 | plugin |  |   
[perplexity](</zh-CN/plugins/reference/perplexity>) | 添加 Web 搜索提供商支持。 | `@openclaw/perplexity-plugin` |   
包含在 OpenClaw 中 | contracts: webSearchProviders |  |   
[qianfan](</zh-CN/plugins/reference/qianfan>) | 为 OpenClaw 添加 Qianfan 模型提供商支持。 | `@openclaw/qianfan-provider` |   
包含在 OpenClaw 中 | providers: qianfan |  |   
[qwen](</zh-CN/plugins/reference/qwen>) | 为 OpenClaw 添加 Qwen、Qwen Cloud、Model Studio、DashScope 模型提供商支持。 | `@openclaw/qwen-provider` |   
包含在 OpenClaw 中 | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</zh-CN/plugins/reference/runway>) | 添加视频生成提供商支持。 | `@openclaw/runway-provider` |   
包含在 OpenClaw 中 | contracts: videoGenerationProviders |  |   
[searxng](</zh-CN/plugins/reference/searxng>) | 添加 Web 搜索提供商支持。 | `@openclaw/searxng-plugin` |   
包含在 OpenClaw 中 | contracts: webSearchProviders |  |   
[senseaudio](</zh-CN/plugins/reference/senseaudio>) | 添加媒体理解提供商支持。 | `@openclaw/senseaudio-provider` |   
包含在 OpenClaw 中 | contracts: mediaUnderstandingProviders |  |   
[sglang](</zh-CN/plugins/reference/sglang>) | 为 OpenClaw 添加 SGLang 模型提供商支持。 | `@openclaw/sglang-provider` |   
包含在 OpenClaw 中 | providers: sglang |  |   
[signal](</zh-CN/plugins/reference/signal>) | 添加用于发送和接收 OpenClaw 消息的 Signal 渠道界面。 | `@openclaw/signal` |   
包含在 OpenClaw 中 | channels: signal |  |   
[skill-workshop](</zh-CN/plugins/reference/skill-workshop>) | 将可重复工作流捕获为工作区技能，包含待审查状态、安全写入和技能提示词刷新。 | `@openclaw/skill-workshop` |   
包含在 OpenClaw 中 | contracts: tools |  |   
[slack](</zh-CN/plugins/reference/slack>) | 添加用于发送和接收 OpenClaw 消息的 Slack 渠道界面。 | `@openclaw/slack` |   
包含在 OpenClaw 中 | channels: slack |  |   
[stepfun](</zh-CN/plugins/reference/stepfun>) | 为 OpenClaw 添加 StepFun、StepFun Plan 模型提供商支持。 | `@openclaw/stepfun-provider` |   
包含在 OpenClaw 中 | providers: stepfun, stepfun-plan |  |   
[synthetic](</zh-CN/plugins/reference/synthetic>) | 为 OpenClaw 添加 Synthetic 模型提供商支持。 | `@openclaw/synthetic-provider` |   
包含在 OpenClaw 中 | providers: synthetic |  |   
[tavily](</zh-CN/plugins/reference/tavily>) | 添加 agent 可调用的工具。添加 Web 搜索提供商支持。 | `@openclaw/tavily-plugin` |   
包含在 OpenClaw 中 | contracts: tools, webSearchProviders; skills |  |   
[telegram](</zh-CN/plugins/reference/telegram>) | 添加用于发送和接收 OpenClaw 消息的 Telegram 渠道界面。 | `@openclaw/telegram` |   
包含在 OpenClaw 中 | channels: telegram |  |   
[tencent](</zh-CN/plugins/reference/tencent>) | 为 OpenClaw 添加 Tencent TokenHub 模型提供商支持。 | `@openclaw/tencent-provider` |   
包含在 OpenClaw 中 | providers: tencent-tokenhub |  |   
[together](</zh-CN/plugins/reference/together>) | 为 OpenClaw 添加 Together 模型提供商支持。 | `@openclaw/together-provider` |   
包含在 OpenClaw 中 | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</zh-CN/plugins/reference/tokenjuice>) | 使用 tokenjuice reducer 压缩 exec 和 bash 工具结果。 | `@openclaw/tokenjuice` |   
包含在 OpenClaw 中 | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</zh-CN/plugins/reference/tts-local-cli>) | 添加文本转语音提供商支持。 | `@openclaw/tts-local-cli` |   
包含在 OpenClaw 中 | contracts: speechProviders |  |   
[venice](</zh-CN/plugins/reference/venice>) | 为 OpenClaw 添加 Venice 模型提供商支持。 | `@openclaw/venice-provider` |   
包含在 OpenClaw 中 | providers: venice |  |   
[vercel-ai-gateway](</zh-CN/plugins/reference/vercel-ai-gateway>) | 为 OpenClaw 添加 Vercel AI Gateway 网关模型提供商支持。 | `@openclaw/vercel-ai-gateway-provider` |   
包含在 OpenClaw 中 | providers: vercel-ai-gateway |  |   
[vllm](</zh-CN/plugins/reference/vllm>) | 为 OpenClaw 添加 vLLM 模型提供商支持。 | `@openclaw/vllm-provider` |   
包含在 OpenClaw 中 | providers: vllm |  |   
[volcengine](</zh-CN/plugins/reference/volcengine>) | 为 OpenClaw 添加 Volcengine、Volcengine Plan 模型提供商支持。 | `@openclaw/volcengine-provider` |   
包含在 OpenClaw 中 | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</zh-CN/plugins/reference/voyage>) | 添加记忆嵌入提供商支持。 | `@openclaw/voyage-provider` |   
包含在 OpenClaw 中 | contracts: memoryEmbeddingProviders |  |   
[vydra](</zh-CN/plugins/reference/vydra>) | 为 OpenClaw 添加 Vydra 模型提供商支持。 | `@openclaw/vydra-provider` |   
包含在 OpenClaw 中 | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</zh-CN/plugins/reference/web-readability>) | 从本地 HTML 网页获取响应中提取可读的文章内容。 | `@openclaw/web-readability-plugin` |   
包含在 OpenClaw 中 | contracts: webContentExtractors |  |   
[webhooks](</zh-CN/plugins/reference/webhooks>) | 经过身份验证的入站网络钩子，将外部自动化绑定到 OpenClaw 任务流。 | `@openclaw/webhooks` |   
包含在 OpenClaw 中 | plugin |  |   
[xai](</zh-CN/plugins/reference/xai>) | 为 OpenClaw 添加 xAI 模型提供商支持。 | `@openclaw/xai-plugin` |   
包含在 OpenClaw 中 | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</zh-CN/plugins/reference/xiaomi>) | 为 OpenClaw 添加 Xiaomi 模型提供商支持。 | `@openclaw/xiaomi-provider` |   
包含在 OpenClaw 中 | providers: xiaomi; contracts: speechProviders |  |   
[zai](</zh-CN/plugins/reference/zai>) | 为 OpenClaw 添加 [Z.AI](<http://Z.AI>) 模型提供商支持。 | `@openclaw/zai-provider` |   
包含在 OpenClaw 中 | providers: zai; contracts: mediaUnderstandingProviders |  |   
  
## 官方外部包

插件 | 描述 | 分发 | 暴露面  
---|---|---|---  
[acpx](</zh-CN/plugins/reference/acpx>) | 嵌入式 ACP 运行时后端，包含插件自有的会话和传输管理。 | `@openclaw/acpx` |   
npm；ClawHub | skills |  |   
[brave](</zh-CN/plugins/reference/brave>) | 添加 Web 搜索提供商支持。 | `@openclaw/brave-plugin` |   
npm；ClawHub | contracts: webSearchProviders |  |   
[codex](</zh-CN/plugins/reference/codex>) | Codex 应用服务器 harness 和 Codex 管理的 GPT 模型目录。 | `@openclaw/codex` |   
npm；ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[diagnostics-otel](</zh-CN/plugins/reference/diagnostics-otel>) | OpenClaw 诊断 OpenTelemetry 导出器。 | `@openclaw/diagnostics-otel` |   
npm；ClawHub：`clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</zh-CN/plugins/reference/diagnostics-prometheus>) | OpenClaw 诊断 Prometheus 导出器。 | `@openclaw/diagnostics-prometheus` |   
npm；ClawHub：`clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</zh-CN/plugins/reference/diffs>) | 面向智能体的只读 diff 查看器和文件渲染器。 | `@openclaw/diffs` |   
npm；ClawHub | contracts: tools; skills |  |   
[discord](</zh-CN/plugins/reference/discord>) | 添加 Discord 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/discord` |   
npm；ClawHub | channels: discord |  |   
[feishu](</zh-CN/plugins/reference/feishu>) | 添加 Feishu 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/feishu` |   
npm；ClawHub | channels: feishu; contracts: tools; skills |  |   
[google-meet](</zh-CN/plugins/reference/google-meet>) | 通过 Chrome 或 Twilio 传输协议加入 Google Meet 通话。 | `@openclaw/google-meet` |   
npm；ClawHub | contracts: tools |  |   
[googlechat](</zh-CN/plugins/reference/googlechat>) | 添加 Google Chat 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/googlechat` |   
npm；ClawHub | channels: googlechat |  |   
[line](</zh-CN/plugins/reference/line>) | 添加 LINE 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/line` |   
npm；ClawHub | channels: line |  |   
[lobster](</zh-CN/plugins/reference/lobster>) | 带可恢复审批的类型化工作流工具。 | `@openclaw/lobster` |   
npm；ClawHub | contracts: tools |  |   
[matrix](</zh-CN/plugins/reference/matrix>) | 添加 Matrix 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/matrix` |   
ClawHub：`clawhub:@openclaw/matrix`；npm | channels: matrix |  |   
[memory-lancedb](</zh-CN/plugins/reference/memory-lancedb>) | 添加智能体可调用的工具。 | `@openclaw/memory-lancedb` |   
npm；ClawHub | contracts: tools |  |   
[msteams](</zh-CN/plugins/reference/msteams>) | 添加 Microsoft Teams 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/msteams` |   
npm；ClawHub | channels: msteams |  |   
[nextcloud-talk](</zh-CN/plugins/reference/nextcloud-talk>) | 添加 Nextcloud Talk 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/nextcloud-talk` |   
npm；ClawHub | channels: nextcloud-talk |  |   
[nostr](</zh-CN/plugins/reference/nostr>) | 添加 Nostr 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/nostr` |   
npm；ClawHub | channels: nostr |  |   
[qqbot](</zh-CN/plugins/reference/qqbot>) | 添加 QQ Bot 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/qqbot` |   
npm；ClawHub | channels: qqbot; contracts: tools; skills |  |   
[synology-chat](</zh-CN/plugins/reference/synology-chat>) | 添加 Synology Chat 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/synology-chat` |   
npm；ClawHub | channels: synology-chat |  |   
[tlon](</zh-CN/plugins/reference/tlon>) | 添加 Tlon 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/tlon` |   
npm；ClawHub | channels: tlon; contracts: tools; skills |  |   
[twitch](</zh-CN/plugins/reference/twitch>) | 添加 Twitch 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/twitch` |   
npm；ClawHub | channels: twitch |  |   
[voice-call](</zh-CN/plugins/reference/voice-call>) | 添加智能体可调用的工具。 | `@openclaw/voice-call` |   
npm；ClawHub | contracts: tools |  |   
[whatsapp](</zh-CN/plugins/reference/whatsapp>) | 添加 WhatsApp 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/whatsapp` |   
npm；ClawHub | channels: whatsapp |  |   
[zalo](</zh-CN/plugins/reference/zalo>) | 添加 Zalo 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/zalo` |   
npm；ClawHub | channels: zalo |  |   
[zalouser](</zh-CN/plugins/reference/zalouser>) | 添加 Zalo Personal 渠道暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/zalouser` |   
npm；ClawHub | channels: zalouser; contracts: tools |  |   
  
## 仅源代码检出

插件 | 描述 | 分发 | 暴露面  
---|---|---|---  
[qa-channel](</zh-CN/plugins/reference/qa-channel>) | 添加 QA channel 暴露面，用于发送和接收 OpenClaw 消息。 | `@openclaw/qa-channel` |   
仅源代码检出 | channels: qa-channel |  |   
[qa-lab](</zh-CN/plugins/reference/qa-lab>) | OpenClaw QA 实验室插件，包含私有调试器 UI 和场景运行器。 | `@openclaw/qa-lab` |   
仅源代码检出 | plugin |  |   
[qa-matrix](</zh-CN/plugins/reference/qa-matrix>) | Matrix QA 传输运行器和底层基底。 | `@openclaw/qa-matrix` |   
仅源代码检出 | plugin |  |   
  
Was this useful?YesNo