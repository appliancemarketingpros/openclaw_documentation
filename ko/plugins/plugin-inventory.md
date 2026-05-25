---
title: Plugin 인벤토리
source_url: https://docs.openclaw.ai/ko/plugins/plugin-inventory
scraped_at: 2026-05-25
---

# Plugin 인벤토리

이 페이지는 `extensions/*/package.json`, `openclaw.plugin.json`, 그리고 루트 npm 패키지 `files` 제외 항목에서 생성됩니다. 다음 명령으로 다시 생성하세요.

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

## 정의

  * **핵심 npm 패키지:** `openclaw` npm 패키지에 포함되어 있으며 별도의 Plugin 설치 없이 사용할 수 있습니다.
  * **공식 외부 패키지:** 핵심 npm 패키지에서는 제외되지만 이 공식 인벤토리에 유지되며 ClawHub 및/또는 npm을 통해 필요할 때 설치되는 OpenClaw 유지 관리 Plugin입니다.
  * **소스 체크아웃 전용:** 게시된 npm 아티팩트에서 제외되며 설치 가능한 패키지로 안내되지 않는 저장소 로컬 Plugin입니다.


소스 체크아웃은 npm 설치와 다릅니다. `pnpm install` 후에는 번들된 Plugin이 `extensions/<id>`에서 로드되므로 로컬 편집 사항과 패키지 로컬 워크스페이스 의존성을 사용할 수 있습니다.

## Plugin 설치

설치가 필요한지 판단하려면 **배포 방식** 열을 사용하세요. `included in OpenClaw`라고 표시된 Plugin은 핵심 패키지에 이미 포함되어 있습니다. 공식 외부 패키지는 한 번 설치한 다음 Gateway를 다시 시작해야 합니다.

예를 들어 Discord는 공식 외부 패키지입니다.

bashCopy code
[code]
    openclaw plugins install @openclaw/discordopenclaw gateway restartopenclaw plugins inspect discord --runtime --json
[/code]

bare 패키지 명세는 먼저 ClawHub를 시도한 다음 npm으로 대체합니다. 소스를 강제하려면 `clawhub:@openclaw/discord` 또는 `npm:@openclaw/discord`를 사용하세요. 설치 후에는 자격 증명과 채널 구성을 추가하기 위해 [Discord](</ko/channels/discord>)와 같은 Plugin의 설정 문서를 따르세요. 업데이트, 제거, 게시 명령은 [Plugin 관리](</ko/plugins/manage-plugins>)를 참조하세요.

## 핵심 npm 패키지

Plugin | 설명 | 배포 | 노출면  
---|---|---|---  
[alibaba](</ko/plugins/reference/alibaba>) | 비디오 생성 제공자 지원을 추가합니다. | `@openclaw/alibaba-provider` |   
OpenClaw에 포함 | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</ko/plugins/reference/amazon-bedrock>) | OpenClaw에 Amazon Bedrock 모델 제공자 지원을 추가합니다. | `@openclaw/amazon-bedrock-provider` |   
OpenClaw에 포함 | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</ko/plugins/reference/amazon-bedrock-mantle>) | OpenClaw에 Amazon Bedrock Mantle 모델 제공자 지원을 추가합니다. | `@openclaw/amazon-bedrock-mantle-provider` |   
OpenClaw에 포함 | providers: amazon-bedrock-mantle |  |   
[anthropic](</ko/plugins/reference/anthropic>) | OpenClaw에 Anthropic 모델 제공자 지원을 추가합니다. | `@openclaw/anthropic-provider` |   
OpenClaw에 포함 | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</ko/plugins/reference/anthropic-vertex>) | OpenClaw에 Anthropic Vertex 모델 제공자 지원을 추가합니다. | `@openclaw/anthropic-vertex-provider` |   
OpenClaw에 포함 | providers: anthropic-vertex |  |   
[arcee](</ko/plugins/reference/arcee>) | OpenClaw에 Arcee 모델 제공자 지원을 추가합니다. | `@openclaw/arcee-provider` |   
OpenClaw에 포함 | providers: arcee |  |   
[azure-speech](</ko/plugins/reference/azure-speech>) | Azure AI Speech 텍스트 음성 변환(MP3, 네이티브 Ogg/Opus 음성 노트, PCM 전화 통신). | `@openclaw/azure-speech` |   
OpenClaw에 포함 | contracts: speechProviders |  |   
[bonjour](</ko/plugins/reference/bonjour>) | Bonjour/mDNS를 통해 로컬 OpenClaw Gateway를 광고합니다. | `@openclaw/bonjour` |   
OpenClaw에 포함 | plugin |  |   
[browser](</ko/plugins/reference/browser>) | 에이전트가 호출할 수 있는 도구를 추가합니다. | `@openclaw/browser-plugin` |   
OpenClaw에 포함 | contracts: tools; skills |  |   
[byteplus](</ko/plugins/reference/byteplus>) | OpenClaw에 BytePlus, BytePlus Plan 모델 제공자 지원을 추가합니다. | `@openclaw/byteplus-provider` |   
OpenClaw에 포함 | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</ko/plugins/reference/canvas>) | 페어링된 Node를 위한 실험적 Canvas 제어 및 A2UI 렌더링 노출면입니다. | `@openclaw/canvas-plugin` |   
OpenClaw에 포함 | contracts: tools |  |   
[cerebras](</ko/plugins/reference/cerebras>) | OpenClaw에 Cerebras 모델 제공자 지원을 추가합니다. | `@openclaw/cerebras-provider` |   
OpenClaw에 포함 | providers: cerebras |  |   
[chutes](</ko/plugins/reference/chutes>) | OpenClaw에 Chutes 모델 제공자 지원을 추가합니다. | `@openclaw/chutes-provider` |   
OpenClaw에 포함 | providers: chutes |  |   
[clickclack](</ko/plugins/reference/clickclack>) | OpenClaw 메시지를 보내고 받기 위한 Clickclack 채널 노출면을 추가합니다. | `@openclaw/clickclack` |   
OpenClaw에 포함 | channels: clickclack |  |   
[cloudflare-ai-gateway](</ko/plugins/reference/cloudflare-ai-gateway>) | OpenClaw에 Cloudflare AI Gateway 모델 제공자 지원을 추가합니다. | `@openclaw/cloudflare-ai-gateway-provider` |   
OpenClaw에 포함 | providers: cloudflare-ai-gateway |  |   
[comfy](</ko/plugins/reference/comfy>) | OpenClaw에 ComfyUI 모델 제공자 지원을 추가합니다. | `@openclaw/comfy-provider` |   
OpenClaw에 포함 | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</ko/plugins/reference/copilot-proxy>) | OpenClaw에 Copilot Proxy 모델 제공자 지원을 추가합니다. | `@openclaw/copilot-proxy` |   
OpenClaw에 포함 | providers: copilot-proxy |  |   
[deepgram](</ko/plugins/reference/deepgram>) | 미디어 이해 제공자 지원을 추가합니다. 실시간 전사 제공자 지원을 추가합니다. | `@openclaw/deepgram-provider` |   
OpenClaw에 포함 | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</ko/plugins/reference/deepinfra>) | OpenClaw에 DeepInfra 모델 제공자 지원을 추가합니다. | `@openclaw/deepinfra-provider` |   
OpenClaw에 포함 | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</ko/plugins/reference/deepseek>) | OpenClaw에 DeepSeek 모델 제공자 지원을 추가합니다. | `@openclaw/deepseek-provider` |   
OpenClaw에 포함됨 | providers: deepseek |  |   
[document-extract](</ko/plugins/reference/document-extract>) | 로컬 문서 첨부 파일에서 텍스트와 대체 페이지 이미지를 추출합니다. | `@openclaw/document-extract-plugin` |   
OpenClaw에 포함됨 | contracts: documentExtractors |  |   
[duckduckgo](</ko/plugins/reference/duckduckgo>) | 웹 검색 제공자 지원을 추가합니다. | `@openclaw/duckduckgo-plugin` |   
OpenClaw에 포함됨 | contracts: webSearchProviders |  |   
[elevenlabs](</ko/plugins/reference/elevenlabs>) | 미디어 이해 제공자 지원을 추가합니다. 실시간 전사 제공자 지원을 추가합니다. 텍스트 음성 변환 제공자 지원을 추가합니다. | `@openclaw/elevenlabs-speech` |   
OpenClaw에 포함됨 | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</ko/plugins/reference/exa>) | 웹 검색 제공자 지원을 추가합니다. | `@openclaw/exa-plugin` |   
OpenClaw에 포함됨 | contracts: webSearchProviders |  |   
[fal](</ko/plugins/reference/fal>) | OpenClaw에 fal 모델 제공자 지원을 추가합니다. | `@openclaw/fal-provider` |   
OpenClaw에 포함됨 | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[file-transfer](</ko/plugins/reference/file-transfer>) | 전용 Node 명령을 통해 페어링된 노드에서 파일을 가져오고, 나열하고, 씁니다. 최대 16MB 바이너리에 대해 node.invoke에서 base64를 사용하여 bash stdout 잘림을 우회합니다. | `@openclaw/file-transfer` |   
OpenClaw에 포함됨 | contracts: tools |  |   
[firecrawl](</ko/plugins/reference/firecrawl>) | 에이전트가 호출할 수 있는 도구를 추가합니다. 웹 가져오기 제공자 지원을 추가합니다. 웹 검색 제공자 지원을 추가합니다. | `@openclaw/firecrawl-plugin` |   
OpenClaw에 포함됨 | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</ko/plugins/reference/fireworks>) | OpenClaw에 Fireworks 모델 제공자 지원을 추가합니다. | `@openclaw/fireworks-provider` |   
OpenClaw에 포함됨 | providers: fireworks |  |   
[github-copilot](</ko/plugins/reference/github-copilot>) | OpenClaw에 GitHub Copilot 모델 제공자 지원을 추가합니다. | `@openclaw/github-copilot-provider` |   
OpenClaw에 포함됨 | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</ko/plugins/reference/google>) | OpenClaw에 Google, Google Gemini CLI, Google Vertex 모델 제공자 지원을 추가합니다. | `@openclaw/google-plugin` |   
OpenClaw에 포함됨 | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[gradium](</ko/plugins/reference/gradium>) | 텍스트 음성 변환 제공자 지원을 추가합니다. | `@openclaw/gradium-speech` |   
OpenClaw에 포함됨 | contracts: speechProviders |  |   
[groq](</ko/plugins/reference/groq>) | OpenClaw에 Groq 모델 제공자 지원을 추가합니다. | `@openclaw/groq-provider` |   
OpenClaw에 포함됨 | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</ko/plugins/reference/huggingface>) | OpenClaw에 Hugging Face 모델 제공자 지원을 추가합니다. | `@openclaw/huggingface-provider` |   
OpenClaw에 포함됨 | providers: huggingface |  |   
[imessage](</ko/plugins/reference/imessage>) | OpenClaw 메시지를 보내고 받기 위한 iMessage 채널 표면을 추가합니다. | `@openclaw/imessage` |   
OpenClaw에 포함됨 | channels: imessage |  |   
[inworld](</ko/plugins/reference/inworld>) | Inworld 스트리밍 텍스트 음성 변환(MP3, OGG_OPUS, PCM 전화 통신). | `@openclaw/inworld-speech` |   
OpenClaw에 포함됨 | contracts: speechProviders |  |   
[irc](</ko/plugins/reference/irc>) | OpenClaw 메시지를 보내고 받기 위한 IRC 채널 표면을 추가합니다. | `@openclaw/irc` |   
OpenClaw에 포함됨 | channels: irc |  |   
[kilocode](</ko/plugins/reference/kilocode>) | OpenClaw에 Kilocode 모델 제공자 지원을 추가합니다. | `@openclaw/kilocode-provider` |   
OpenClaw에 포함됨 | providers: kilocode |  |   
[kimi](</ko/plugins/reference/kimi>) | OpenClaw에 Kimi, Kimi Coding 모델 제공자 지원을 추가합니다. | `@openclaw/kimi-provider` |   
OpenClaw에 포함됨 | providers: kimi, kimi-coding |  |   
[litellm](</ko/plugins/reference/litellm>) | OpenClaw에 LiteLLM 모델 제공자 지원을 추가합니다. | `@openclaw/litellm-provider` |   
OpenClaw에 포함됨 | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</ko/plugins/reference/llm-task>) | 워크플로에서 호출할 수 있는 구조화된 작업용 범용 JSON 전용 LLM 도구입니다. | `@openclaw/llm-task` |   
OpenClaw에 포함됨 | contracts: tools |  |   
[lmstudio](</ko/plugins/reference/lmstudio>) | OpenClaw에 LM Studio 모델 제공자 지원을 추가합니다. | `@openclaw/lmstudio-provider` |   
OpenClaw에 포함됨 | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[mattermost](</ko/plugins/reference/mattermost>) | OpenClaw 메시지를 주고받기 위한 Mattermost 채널 인터페이스를 추가합니다. | `@openclaw/mattermost` |   
OpenClaw에 포함됨 | channels: mattermost |  |   
[memory-core](</ko/plugins/reference/memory-core>) | 메모리 임베딩 제공자 지원을 추가합니다. 에이전트가 호출할 수 있는 도구를 추가합니다. | `@openclaw/memory-core` |   
OpenClaw에 포함됨 | contracts: memoryEmbeddingProviders, tools |  |   
[memory-wiki](</ko/plugins/reference/memory-wiki>) | OpenClaw용 영구 wiki 컴파일러 및 Obsidian 친화적 지식 볼트입니다. | `@openclaw/memory-wiki` |   
OpenClaw에 포함됨 | contracts: tools; skills |  |   
[microsoft](</ko/plugins/reference/microsoft>) | 텍스트 음성 변환 제공자 지원을 추가합니다. | `@openclaw/microsoft-speech` |   
OpenClaw에 포함됨 | contracts: speechProviders |  |   
[microsoft-foundry](</ko/plugins/reference/microsoft-foundry>) | OpenClaw에 Microsoft Foundry 모델 제공자 지원을 추가합니다. | `@openclaw/microsoft-foundry` |   
OpenClaw에 포함됨 | providers: microsoft-foundry |  |   
[migrate-claude](</ko/plugins/reference/migrate-claude>) | Claude Code 및 Claude Desktop 지침, MCP 서버, skills, 안전한 구성을 OpenClaw로 가져옵니다. | `@openclaw/migrate-claude` |   
OpenClaw에 포함됨 | contracts: migrationProviders |  |   
[migrate-hermes](</ko/plugins/reference/migrate-hermes>) | Hermes 구성, memories, skills, 지원되는 자격 증명을 OpenClaw로 가져옵니다. | `@openclaw/migrate-hermes` |   
OpenClaw에 포함됨 | contracts: migrationProviders |  |   
[minimax](</ko/plugins/reference/minimax>) | OpenClaw에 MiniMax, MiniMax Portal 모델 제공자 지원을 추가합니다. | `@openclaw/minimax-provider` |   
OpenClaw에 포함됨 | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</ko/plugins/reference/mistral>) | OpenClaw에 Mistral 모델 제공자 지원을 추가합니다. | `@openclaw/mistral-provider` |   
OpenClaw에 포함됨 | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</ko/plugins/reference/moonshot>) | OpenClaw에 Moonshot 모델 제공자 지원을 추가합니다. | `@openclaw/moonshot-provider` |   
OpenClaw에 포함됨 | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[nvidia](</ko/plugins/reference/nvidia>) | OpenClaw에 NVIDIA 모델 제공자 지원을 추가합니다. | `@openclaw/nvidia-provider` |   
OpenClaw에 포함됨 | providers: nvidia |  |   
[oc-path](</ko/plugins/reference/oc-path>) | oc:// 워크스페이스 파일 주소 지정을 위한 openclaw path CLI를 추가합니다. | `@openclaw/oc-path` |   
OpenClaw에 포함됨 | plugin |  |   
[ollama](</ko/plugins/reference/ollama>) | OpenClaw에 Ollama 모델 제공자 지원을 추가합니다. | `@openclaw/ollama-provider` |   
OpenClaw에 포함됨 | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</ko/plugins/reference/open-prose>) | /prose 슬래시 명령이 포함된 OpenProse VM skill pack입니다. | `@openclaw/open-prose` |   
OpenClaw에 포함됨 | skills |  |   
[openai](</ko/plugins/reference/openai>) | OpenClaw에 OpenAI, OpenAI Codex 모델 제공자 지원을 추가합니다. | `@openclaw/openai-provider` |   
OpenClaw에 포함됨 | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</ko/plugins/reference/opencode>) | OpenClaw에 OpenCode 모델 제공자 지원을 추가합니다. | `@openclaw/opencode-provider` |   
OpenClaw에 포함됨 | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</ko/plugins/reference/opencode-go>) | OpenClaw에 OpenCode Go 모델 제공자 지원을 추가합니다. | `@openclaw/opencode-go-provider` |   
OpenClaw에 포함됨 | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</ko/plugins/reference/openrouter>) | OpenClaw에 OpenRouter 모델 제공자 지원을 추가합니다. | `@openclaw/openrouter-provider` |   
OpenClaw에 포함됨 | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</ko/plugins/reference/openshell>) | 미러링된 로컬 워크스페이스와 SSH 기반 명령 실행을 갖춘 OpenShell 기반 샌드박스 백엔드입니다. | `@openclaw/openshell-sandbox` |   
OpenClaw에 포함됨 | plugin |  |   
[perplexity](</ko/plugins/reference/perplexity>) | 웹 검색 제공자 지원을 추가합니다. | `@openclaw/perplexity-plugin` |   
OpenClaw에 포함됨 | contracts: webSearchProviders |  |   
[qianfan](</ko/plugins/reference/qianfan>) | OpenClaw에 Qianfan 모델 공급자 지원을 추가합니다. | `@openclaw/qianfan-provider` |   
OpenClaw에 포함됨 | providers: qianfan |  |   
[qwen](</ko/plugins/reference/qwen>) | OpenClaw에 Qwen, Qwen Cloud, Model Studio, DashScope 모델 공급자 지원을 추가합니다. | `@openclaw/qwen-provider` |   
OpenClaw에 포함됨 | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</ko/plugins/reference/runway>) | 비디오 생성 공급자 지원을 추가합니다. | `@openclaw/runway-provider` |   
OpenClaw에 포함됨 | contracts: videoGenerationProviders |  |   
[searxng](</ko/plugins/reference/searxng>) | 웹 검색 공급자 지원을 추가합니다. | `@openclaw/searxng-plugin` |   
OpenClaw에 포함됨 | contracts: webSearchProviders |  |   
[senseaudio](</ko/plugins/reference/senseaudio>) | 미디어 이해 공급자 지원을 추가합니다. | `@openclaw/senseaudio-provider` |   
OpenClaw에 포함됨 | contracts: mediaUnderstandingProviders |  |   
[sglang](</ko/plugins/reference/sglang>) | OpenClaw에 SGLang 모델 공급자 지원을 추가합니다. | `@openclaw/sglang-provider` |   
OpenClaw에 포함됨 | providers: sglang |  |   
[signal](</ko/plugins/reference/signal>) | OpenClaw 메시지를 보내고 받기 위한 Signal 채널 표면을 추가합니다. | `@openclaw/signal` |   
OpenClaw에 포함됨 | channels: signal |  |   
[skill-workshop](</ko/plugins/reference/skill-workshop>) | 검토 대기, 안전한 쓰기, Skill 프롬프트 새로 고침과 함께 반복 가능한 워크플로를 작업공간 Skills로 캡처합니다. | `@openclaw/skill-workshop` |   
OpenClaw에 포함됨 | contracts: tools |  |   
[slack](</ko/plugins/reference/slack>) | OpenClaw 메시지를 보내고 받기 위한 Slack 채널 표면을 추가합니다. | `@openclaw/slack` |   
OpenClaw에 포함됨 | channels: slack |  |   
[stepfun](</ko/plugins/reference/stepfun>) | OpenClaw에 StepFun, StepFun Plan 모델 공급자 지원을 추가합니다. | `@openclaw/stepfun-provider` |   
OpenClaw에 포함됨 | providers: stepfun, stepfun-plan |  |   
[synthetic](</ko/plugins/reference/synthetic>) | OpenClaw에 Synthetic 모델 공급자 지원을 추가합니다. | `@openclaw/synthetic-provider` |   
OpenClaw에 포함됨 | providers: synthetic |  |   
[tavily](</ko/plugins/reference/tavily>) | 에이전트가 호출할 수 있는 도구를 추가합니다. 웹 검색 공급자 지원을 추가합니다. | `@openclaw/tavily-plugin` |   
OpenClaw에 포함됨 | contracts: tools, webSearchProviders; skills |  |   
[telegram](</ko/plugins/reference/telegram>) | OpenClaw 메시지를 보내고 받기 위한 Telegram 채널 표면을 추가합니다. | `@openclaw/telegram` |   
OpenClaw에 포함됨 | channels: telegram |  |   
[tencent](</ko/plugins/reference/tencent>) | OpenClaw에 Tencent TokenHub 모델 공급자 지원을 추가합니다. | `@openclaw/tencent-provider` |   
OpenClaw에 포함됨 | providers: tencent-tokenhub |  |   
[together](</ko/plugins/reference/together>) | OpenClaw에 Together 모델 공급자 지원을 추가합니다. | `@openclaw/together-provider` |   
OpenClaw에 포함됨 | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</ko/plugins/reference/tokenjuice>) | tokenjuice 리듀서로 exec 및 bash 도구 결과를 압축합니다. | `@openclaw/tokenjuice` |   
OpenClaw에 포함됨 | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</ko/plugins/reference/tts-local-cli>) | 텍스트 음성 변환 공급자 지원을 추가합니다. | `@openclaw/tts-local-cli` |   
OpenClaw에 포함됨 | contracts: speechProviders |  |   
[venice](</ko/plugins/reference/venice>) | OpenClaw에 Venice 모델 공급자 지원을 추가합니다. | `@openclaw/venice-provider` |   
OpenClaw에 포함됨 | providers: venice |  |   
[vercel-ai-gateway](</ko/plugins/reference/vercel-ai-gateway>) | OpenClaw에 Vercel AI Gateway 모델 공급자 지원을 추가합니다. | `@openclaw/vercel-ai-gateway-provider` |   
OpenClaw에 포함됨 | providers: vercel-ai-gateway |  |   
[vllm](</ko/plugins/reference/vllm>) | OpenClaw에 vLLM 모델 공급자 지원을 추가합니다. | `@openclaw/vllm-provider` |   
OpenClaw에 포함됨 | providers: vllm |  |   
[volcengine](</ko/plugins/reference/volcengine>) | OpenClaw에 Volcengine, Volcengine Plan 모델 공급자 지원을 추가합니다. | `@openclaw/volcengine-provider` |   
OpenClaw에 포함됨 | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</ko/plugins/reference/voyage>) | 메모리 임베딩 프로바이더 지원을 추가합니다. | `@openclaw/voyage-provider` |   
OpenClaw에 포함됨 | contracts: memoryEmbeddingProviders |  |   
[vydra](</ko/plugins/reference/vydra>) | Vydra 모델 프로바이더 지원을 OpenClaw에 추가합니다. | `@openclaw/vydra-provider` |   
OpenClaw에 포함됨 | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</ko/plugins/reference/web-readability>) | 로컬 HTML 웹 가져오기 응답에서 읽기 쉬운 문서 콘텐츠를 추출합니다. | `@openclaw/web-readability-plugin` |   
OpenClaw에 포함됨 | contracts: webContentExtractors |  |   
[webhooks](</ko/plugins/reference/webhooks>) | 외부 자동화를 OpenClaw TaskFlow에 바인딩하는 인증된 인바운드 Webhook입니다. | `@openclaw/webhooks` |   
OpenClaw에 포함됨 | plugin |  |   
[xai](</ko/plugins/reference/xai>) | xAI 모델 프로바이더 지원을 OpenClaw에 추가합니다. | `@openclaw/xai-plugin` |   
OpenClaw에 포함됨 | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</ko/plugins/reference/xiaomi>) | Xiaomi 모델 프로바이더 지원을 OpenClaw에 추가합니다. | `@openclaw/xiaomi-provider` |   
OpenClaw에 포함됨 | providers: xiaomi; contracts: speechProviders |  |   
[zai](</ko/plugins/reference/zai>) | [Z.AI](<http://Z.AI>) 모델 프로바이더 지원을 OpenClaw에 추가합니다. | `@openclaw/zai-provider` |   
OpenClaw에 포함됨 | providers: zai; contracts: mediaUnderstandingProviders |  |   
  
## 공식 외부 패키지

Plugin | 설명 | 배포 | 표면  
---|---|---|---  
[acpx](</ko/plugins/reference/acpx>) | Plugin이 소유하는 세션 및 전송 관리를 갖춘 내장 ACP 런타임 백엔드입니다. | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[brave](</ko/plugins/reference/brave>) | 웹 검색 공급자 지원을 추가합니다. | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[codex](</ko/plugins/reference/codex>) | Codex 앱 서버 하네스 및 Codex가 관리하는 GPT 모델 카탈로그입니다. | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[diagnostics-otel](</ko/plugins/reference/diagnostics-otel>) | OpenClaw 진단 OpenTelemetry 익스포터입니다. | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</ko/plugins/reference/diagnostics-prometheus>) | OpenClaw 진단 Prometheus 익스포터입니다. | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</ko/plugins/reference/diffs>) | 에이전트를 위한 읽기 전용 diff 뷰어 및 파일 렌더러입니다. | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</ko/plugins/reference/discord>) | OpenClaw 메시지를 보내고 받기 위한 Discord 채널 표면을 추가합니다. | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[feishu](</ko/plugins/reference/feishu>) | OpenClaw 메시지를 보내고 받기 위한 Feishu 채널 표면을 추가합니다. | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[google-meet](</ko/plugins/reference/google-meet>) | Chrome 또는 Twilio 전송을 통해 Google Meet 통화에 참여합니다. | `@openclaw/google-meet` |   
npm; ClawHub | contracts: tools |  |   
[googlechat](</ko/plugins/reference/googlechat>) | OpenClaw 메시지를 보내고 받기 위한 Google Chat 채널 표면을 추가합니다. | `@openclaw/googlechat` |   
npm; ClawHub | channels: googlechat |  |   
[line](</ko/plugins/reference/line>) | OpenClaw 메시지를 보내고 받기 위한 LINE 채널 표면을 추가합니다. | `@openclaw/line` |   
npm; ClawHub | channels: line |  |   
[lobster](</ko/plugins/reference/lobster>) | 재개 가능한 승인을 지원하는 타입 지정 워크플로 도구입니다. | `@openclaw/lobster` |   
npm; ClawHub | contracts: tools |  |   
[matrix](</ko/plugins/reference/matrix>) | OpenClaw 메시지를 보내고 받기 위한 Matrix 채널 표면을 추가합니다. | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | channels: matrix |  |   
[memory-lancedb](</ko/plugins/reference/memory-lancedb>) | 에이전트가 호출할 수 있는 도구를 추가합니다. | `@openclaw/memory-lancedb` |   
npm; ClawHub | contracts: tools |  |   
[msteams](</ko/plugins/reference/msteams>) | OpenClaw 메시지를 보내고 받기 위한 Microsoft Teams 채널 표면을 추가합니다. | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</ko/plugins/reference/nextcloud-talk>) | OpenClaw 메시지를 보내고 받기 위한 Nextcloud Talk 채널 표면을 추가합니다. | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</ko/plugins/reference/nostr>) | OpenClaw 메시지를 보내고 받기 위한 Nostr 채널 표면을 추가합니다. | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[qqbot](</ko/plugins/reference/qqbot>) | OpenClaw 메시지를 보내고 받기 위한 QQ Bot 채널 표면을 추가합니다. | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[synology-chat](</ko/plugins/reference/synology-chat>) | OpenClaw 메시지를 보내고 받기 위한 Synology Chat 채널 표면을 추가합니다. | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[tlon](</ko/plugins/reference/tlon>) | OpenClaw 메시지를 보내고 받기 위한 Tlon 채널 표면을 추가합니다. | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[twitch](</ko/plugins/reference/twitch>) | OpenClaw 메시지를 보내고 받기 위한 Twitch 채널 표면을 추가합니다. | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[voice-call](</ko/plugins/reference/voice-call>) | 에이전트가 호출할 수 있는 도구를 추가합니다. | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[whatsapp](</ko/plugins/reference/whatsapp>) | OpenClaw 메시지를 보내고 받기 위한 WhatsApp 채널 표면을 추가합니다. | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[zalo](</ko/plugins/reference/zalo>) | OpenClaw 메시지를 보내고 받기 위한 Zalo 채널 표면을 추가합니다. | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</ko/plugins/reference/zalouser>) | OpenClaw 메시지를 보내고 받기 위한 Zalo Personal 채널 표면을 추가합니다. | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
## 소스 체크아웃 전용

Plugin | 설명 | 배포 | 표면  
---|---|---|---  
[qa-channel](</ko/plugins/reference/qa-channel>) | OpenClaw 메시지를 보내고 받기 위한 QA Channel 표면을 추가합니다. | `@openclaw/qa-channel` |   
소스 체크아웃 전용 | channels: qa-channel |  |   
[qa-lab](</ko/plugins/reference/qa-lab>) | 비공개 디버거 UI와 시나리오 러너를 갖춘 OpenClaw QA lab Plugin입니다. | `@openclaw/qa-lab` |   
소스 체크아웃 전용 | plugin |  |   
[qa-matrix](</ko/plugins/reference/qa-matrix>) | Matrix QA 전송 러너 및 기반입니다. | `@openclaw/qa-matrix` |   
소스 체크아웃 전용 | plugin |  |   
  
Was this useful?YesNo