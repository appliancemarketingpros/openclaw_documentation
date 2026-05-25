---
title: Plugin リファレンス
source_url: https://docs.openclaw.ai/ja-JP/plugins/reference
scraped_at: 2026-05-25
---

# Plugin リファレンス

このページは `extensions/*/package.json` と `openclaw.plugin.json` から生成されます。次のコマンドで再生成します:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

Plugin | 説明 | 配布 | サーフェス  
---|---|---|---  
[acpx](</ja-JP/plugins/reference/acpx>) | Plugin が所有するセッションとトランスポート管理を備えた、組み込み ACP ランタイムバックエンド。 | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[alibaba](</ja-JP/plugins/reference/alibaba>) | 動画生成プロバイダー対応を追加します。 | `@openclaw/alibaba-provider` |   
OpenClaw に同梱 | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</ja-JP/plugins/reference/amazon-bedrock>) | OpenClaw に Amazon Bedrock モデルプロバイダー対応を追加します。 | `@openclaw/amazon-bedrock-provider` |   
OpenClaw に同梱 | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</ja-JP/plugins/reference/amazon-bedrock-mantle>) | OpenClaw に Amazon Bedrock Mantle モデルプロバイダー対応を追加します。 | `@openclaw/amazon-bedrock-mantle-provider` |   
OpenClaw に同梱 | providers: amazon-bedrock-mantle |  |   
[anthropic](</ja-JP/plugins/reference/anthropic>) | OpenClaw に Anthropic モデルプロバイダー対応を追加します。 | `@openclaw/anthropic-provider` |   
OpenClaw に同梱 | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</ja-JP/plugins/reference/anthropic-vertex>) | OpenClaw に Anthropic Vertex モデルプロバイダー対応を追加します。 | `@openclaw/anthropic-vertex-provider` |   
OpenClaw に同梱 | providers: anthropic-vertex |  |   
[arcee](</ja-JP/plugins/reference/arcee>) | OpenClaw に Arcee モデルプロバイダー対応を追加します。 | `@openclaw/arcee-provider` |   
OpenClaw に同梱 | providers: arcee |  |   
[azure-speech](</ja-JP/plugins/reference/azure-speech>) | Azure AI Speech のテキスト読み上げ（MP3、ネイティブ Ogg/Opus ボイスメモ、PCM 電話音声）。 | `@openclaw/azure-speech` |   
OpenClaw に同梱 | contracts: speechProviders |  |   
[bonjour](</ja-JP/plugins/reference/bonjour>) | ローカルの OpenClaw gateway を Bonjour/mDNS 経由でアドバタイズします。 | `@openclaw/bonjour` |   
OpenClaw に同梱 | plugin |  |   
[brave](</ja-JP/plugins/reference/brave>) | Web 検索プロバイダー対応を追加します。 | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[browser](</ja-JP/plugins/reference/browser>) | エージェントから呼び出せるツールを追加します。 | `@openclaw/browser-plugin` |   
OpenClaw に同梱 | contracts: tools; skills |  |   
[byteplus](</ja-JP/plugins/reference/byteplus>) | OpenClaw に BytePlus、BytePlus Plan モデルプロバイダー対応を追加します。 | `@openclaw/byteplus-provider` |   
OpenClaw に同梱 | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</ja-JP/plugins/reference/canvas>) | ペアリングされたノード向けの実験的な Canvas 制御と A2UI レンダリングサーフェス。 | `@openclaw/canvas-plugin` |   
OpenClaw に同梱 | contracts: tools |  |   
[cerebras](</ja-JP/plugins/reference/cerebras>) | OpenClaw に Cerebras モデルプロバイダー対応を追加します。 | `@openclaw/cerebras-provider` |   
OpenClaw に同梱 | providers: cerebras |  |   
[chutes](</ja-JP/plugins/reference/chutes>) | OpenClaw に Chutes モデルプロバイダー対応を追加します。 | `@openclaw/chutes-provider` |   
OpenClaw に同梱 | providers: chutes |  |   
[clickclack](</ja-JP/plugins/reference/clickclack>) | OpenClaw メッセージを送受信するための Clickclack チャネルサーフェスを追加します。 | `@openclaw/clickclack` |   
OpenClaw に同梱 | channels: clickclack |  |   
[cloudflare-ai-gateway](</ja-JP/plugins/reference/cloudflare-ai-gateway>) | OpenClaw に Cloudflare AI Gateway モデルプロバイダー対応を追加します。 | `@openclaw/cloudflare-ai-gateway-provider` |   
OpenClaw に同梱 | providers: cloudflare-ai-gateway |  |   
[codex](</ja-JP/plugins/reference/codex>) | Codex app-server ハーネスと Codex 管理の GPT モデルカタログ。 | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[comfy](</ja-JP/plugins/reference/comfy>) | OpenClaw に ComfyUI モデルプロバイダーのサポートを追加します。 | `@openclaw/comfy-provider` |   
OpenClaw に含まれる | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</ja-JP/plugins/reference/copilot-proxy>) | OpenClaw に Copilot Proxy モデルプロバイダーのサポートを追加します。 | `@openclaw/copilot-proxy` |   
OpenClaw に含まれる | providers: copilot-proxy |  |   
[deepgram](</ja-JP/plugins/reference/deepgram>) | メディア理解プロバイダーのサポートを追加します。リアルタイム文字起こしプロバイダーのサポートを追加します。 | `@openclaw/deepgram-provider` |   
OpenClaw に含まれる | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</ja-JP/plugins/reference/deepinfra>) | OpenClaw に DeepInfra モデルプロバイダーのサポートを追加します。 | `@openclaw/deepinfra-provider` |   
OpenClaw に含まれる | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</ja-JP/plugins/reference/deepseek>) | OpenClaw に DeepSeek モデルプロバイダーのサポートを追加します。 | `@openclaw/deepseek-provider` |   
OpenClaw に含まれる | providers: deepseek |  |   
[diagnostics-otel](</ja-JP/plugins/reference/diagnostics-otel>) | OpenClaw 診断用 OpenTelemetry エクスポーター。 | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</ja-JP/plugins/reference/diagnostics-prometheus>) | OpenClaw 診断用 Prometheus エクスポーター。 | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</ja-JP/plugins/reference/diffs>) | エージェント向けの読み取り専用 diff ビューアーおよびファイルレンダラー。 | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</ja-JP/plugins/reference/discord>) | OpenClaw メッセージを送受信するための Discord チャネルサーフェスを追加します。 | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[document-extract](</ja-JP/plugins/reference/document-extract>) | ローカルドキュメント添付ファイルからテキストとフォールバック用ページ画像を抽出します。 | `@openclaw/document-extract-plugin` |   
OpenClaw に含まれる | contracts: documentExtractors |  |   
[duckduckgo](</ja-JP/plugins/reference/duckduckgo>) | Web 検索プロバイダーのサポートを追加します。 | `@openclaw/duckduckgo-plugin` |   
OpenClaw に含まれる | contracts: webSearchProviders |  |   
[elevenlabs](</ja-JP/plugins/reference/elevenlabs>) | メディア理解プロバイダーのサポートを追加します。リアルタイム文字起こしプロバイダーのサポートを追加します。テキスト読み上げプロバイダーのサポートを追加します。 | `@openclaw/elevenlabs-speech` |   
OpenClaw に含まれる | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</ja-JP/plugins/reference/exa>) | Web 検索プロバイダーのサポートを追加します。 | `@openclaw/exa-plugin` |   
OpenClaw に含まれる | contracts: webSearchProviders |  |   
[fal](</ja-JP/plugins/reference/fal>) | OpenClaw に fal モデルプロバイダーのサポートを追加します。 | `@openclaw/fal-provider` |   
OpenClaw に含まれる | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[feishu](</ja-JP/plugins/reference/feishu>) | OpenClaw メッセージを送受信するための Feishu チャネルサーフェスを追加します。 | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[file-transfer](</ja-JP/plugins/reference/file-transfer>) | 専用のノードコマンドを介して、ペアリングされたノード上のファイルを取得、一覧表示、書き込みします。最大 16 MB のバイナリに対して node.invoke 経由で base64 を使用することで、bash stdout の切り詰めを回避します。 | `@openclaw/file-transfer` |   
OpenClaw に含まれる | contracts: tools |  |   
[firecrawl](</ja-JP/plugins/reference/firecrawl>) | エージェントから呼び出せるツールを追加します。Web 取得プロバイダーのサポートを追加します。Web 検索プロバイダーのサポートを追加します。 | `@openclaw/firecrawl-plugin` |   
OpenClaw に含まれる | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</ja-JP/plugins/reference/fireworks>) | OpenClaw に Fireworks モデルプロバイダーのサポートを追加します。 | `@openclaw/fireworks-provider` |   
OpenClaw に含まれる | providers: fireworks |  |   
[github-copilot](</ja-JP/plugins/reference/github-copilot>) | OpenClaw に GitHub Copilot モデルプロバイダーのサポートを追加します。 | `@openclaw/github-copilot-provider` |   
OpenClaw に含まれる | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</ja-JP/plugins/reference/google>) | OpenClaw に Google、Google Gemini CLI、Google Vertex モデルプロバイダーのサポートを追加します。 | `@openclaw/google-plugin` |   
OpenClaw に含まれる | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[google-meet](</ja-JP/plugins/reference/google-meet>) | Chrome または Twilio トランスポート経由で Google Meet 通話に参加します。 | `@openclaw/google-meet` |   
npm; ClawHub | contracts: tools |  |   
[googlechat](</ja-JP/plugins/reference/googlechat>) | OpenClaw メッセージの送受信用に Google Chat チャンネルサーフェスを追加します。 | `@openclaw/googlechat` |   
npm; ClawHub | channels: googlechat |  |   
[gradium](</ja-JP/plugins/reference/gradium>) | テキスト読み上げプロバイダー対応を追加します。 | `@openclaw/gradium-speech` |   
OpenClaw に含まれます | contracts: speechProviders |  |   
[groq](</ja-JP/plugins/reference/groq>) | OpenClaw に Groq モデルプロバイダー対応を追加します。 | `@openclaw/groq-provider` |   
OpenClaw に含まれます | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</ja-JP/plugins/reference/huggingface>) | OpenClaw に Hugging Face モデルプロバイダー対応を追加します。 | `@openclaw/huggingface-provider` |   
OpenClaw に含まれます | providers: huggingface |  |   
[imessage](</ja-JP/plugins/reference/imessage>) | OpenClaw メッセージの送受信用に iMessage チャンネルサーフェスを追加します。 | `@openclaw/imessage` |   
OpenClaw に含まれます | channels: imessage |  |   
[inworld](</ja-JP/plugins/reference/inworld>) | Inworld ストリーミングテキスト読み上げ（MP3、OGG_OPUS、PCM テレフォニー）。 | `@openclaw/inworld-speech` |   
OpenClaw に含まれます | contracts: speechProviders |  |   
[irc](</ja-JP/plugins/reference/irc>) | OpenClaw メッセージの送受信用に IRC チャンネルサーフェスを追加します。 | `@openclaw/irc` |   
OpenClaw に含まれます | channels: irc |  |   
[kilocode](</ja-JP/plugins/reference/kilocode>) | OpenClaw に Kilocode モデルプロバイダー対応を追加します。 | `@openclaw/kilocode-provider` |   
OpenClaw に含まれます | providers: kilocode |  |   
[kimi](</ja-JP/plugins/reference/kimi>) | OpenClaw に Kimi、Kimi Coding モデルプロバイダー対応を追加します。 | `@openclaw/kimi-provider` |   
OpenClaw に含まれます | providers: kimi, kimi-coding |  |   
[line](</ja-JP/plugins/reference/line>) | OpenClaw メッセージの送受信用に LINE チャンネルサーフェスを追加します。 | `@openclaw/line` |   
npm; ClawHub | channels: line |  |   
[litellm](</ja-JP/plugins/reference/litellm>) | OpenClaw に LiteLLM モデルプロバイダー対応を追加します。 | `@openclaw/litellm-provider` |   
OpenClaw に含まれます | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</ja-JP/plugins/reference/llm-task>) | ワークフローから呼び出せる、構造化タスク用の汎用 JSON 専用 LLM ツール。 | `@openclaw/llm-task` |   
OpenClaw に含まれます | contracts: tools |  |   
[lmstudio](</ja-JP/plugins/reference/lmstudio>) | OpenClaw に LM Studio モデルプロバイダー対応を追加します。 | `@openclaw/lmstudio-provider` |   
OpenClaw に含まれます | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[lobster](</ja-JP/plugins/reference/lobster>) | 再開可能な承認を備えた型付きワークフローツール。 | `@openclaw/lobster` |   
npm; ClawHub | contracts: tools |  |   
[matrix](</ja-JP/plugins/reference/matrix>) | OpenClaw メッセージの送受信用に Matrix チャンネルサーフェスを追加します。 | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | channels: matrix |  |   
[mattermost](</ja-JP/plugins/reference/mattermost>) | OpenClaw メッセージの送受信用に Mattermost チャンネルサーフェスを追加します。 | `@openclaw/mattermost` |   
OpenClaw に含まれます | channels: mattermost |  |   
[memory-core](</ja-JP/plugins/reference/memory-core>) | メモリー埋め込みプロバイダー対応を追加します。エージェントから呼び出せるツールを追加します。 | `@openclaw/memory-core` |   
OpenClaw に含まれます | contracts: memoryEmbeddingProviders, tools |  |   
[memory-lancedb](</ja-JP/plugins/reference/memory-lancedb>) | エージェントから呼び出せるツールを追加します。 | `@openclaw/memory-lancedb` |   
npm; ClawHub | contracts: tools |  |   
[memory-wiki](</ja-JP/plugins/reference/memory-wiki>) | OpenClaw 向けの永続的な wiki コンパイラーと、Obsidian に適したナレッジ保管庫。 | `@openclaw/memory-wiki` |   
OpenClaw に含まれます | contracts: tools; skills |  |   
[microsoft](</ja-JP/plugins/reference/microsoft>) | テキスト読み上げプロバイダー対応を追加します。 | `@openclaw/microsoft-speech` |   
OpenClaw に同梱 | contracts: speechProviders |  |   
[microsoft-foundry](</ja-JP/plugins/reference/microsoft-foundry>) | OpenClaw に Microsoft Foundry モデルプロバイダー対応を追加します。 | `@openclaw/microsoft-foundry` |   
OpenClaw に同梱 | providers: microsoft-foundry |  |   
[migrate-claude](</ja-JP/plugins/reference/migrate-claude>) | Claude Code と Claude Desktop の手順、MCP サーバー、Skills、安全な設定を OpenClaw にインポートします。 | `@openclaw/migrate-claude` |   
OpenClaw に同梱 | contracts: migrationProviders |  |   
[migrate-hermes](</ja-JP/plugins/reference/migrate-hermes>) | Hermes の設定、メモリ、Skills、対応している認証情報を OpenClaw にインポートします。 | `@openclaw/migrate-hermes` |   
OpenClaw に同梱 | contracts: migrationProviders |  |   
[minimax](</ja-JP/plugins/reference/minimax>) | OpenClaw に MiniMax、MiniMax Portal モデルプロバイダー対応を追加します。 | `@openclaw/minimax-provider` |   
OpenClaw に同梱 | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</ja-JP/plugins/reference/mistral>) | OpenClaw に Mistral モデルプロバイダー対応を追加します。 | `@openclaw/mistral-provider` |   
OpenClaw に同梱 | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</ja-JP/plugins/reference/moonshot>) | OpenClaw に Moonshot モデルプロバイダー対応を追加します。 | `@openclaw/moonshot-provider` |   
OpenClaw に同梱 | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[msteams](</ja-JP/plugins/reference/msteams>) | OpenClaw メッセージを送受信するための Microsoft Teams チャネルサーフェスを追加します。 | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</ja-JP/plugins/reference/nextcloud-talk>) | OpenClaw メッセージを送受信するための Nextcloud Talk チャネルサーフェスを追加します。 | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</ja-JP/plugins/reference/nostr>) | OpenClaw メッセージを送受信するための Nostr チャネルサーフェスを追加します。 | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[nvidia](</ja-JP/plugins/reference/nvidia>) | OpenClaw に NVIDIA モデルプロバイダー対応を追加します。 | `@openclaw/nvidia-provider` |   
OpenClaw に同梱 | providers: nvidia |  |   
[oc-path](</ja-JP/plugins/reference/oc-path>) | oc:// ワークスペースファイルアドレス指定用の openclaw path CLI を追加します。 | `@openclaw/oc-path` |   
OpenClaw に同梱 | plugin |  |   
[ollama](</ja-JP/plugins/reference/ollama>) | OpenClaw に Ollama モデルプロバイダー対応を追加します。 | `@openclaw/ollama-provider` |   
OpenClaw に同梱 | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</ja-JP/plugins/reference/open-prose>) | /prose スラッシュコマンドを備えた OpenProse VM Skills パックです。 | `@openclaw/open-prose` |   
OpenClaw に同梱 | skills |  |   
[openai](</ja-JP/plugins/reference/openai>) | OpenClaw に OpenAI、OpenAI Codex モデルプロバイダー対応を追加します。 | `@openclaw/openai-provider` |   
OpenClaw に同梱 | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</ja-JP/plugins/reference/opencode>) | OpenClaw に OpenCode モデルプロバイダー対応を追加します。 | `@openclaw/opencode-provider` |   
OpenClaw に同梱 | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</ja-JP/plugins/reference/opencode-go>) | OpenClaw に OpenCode Go モデルプロバイダー対応を追加します。 | `@openclaw/opencode-go-provider` |   
OpenClaw に同梱 | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</ja-JP/plugins/reference/openrouter>) | OpenClaw に OpenRouter モデルプロバイダー対応を追加します。 | `@openclaw/openrouter-provider` |   
OpenClaw に同梱 | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</ja-JP/plugins/reference/openshell>) | ミラーリングされたローカルワークスペースと SSH ベースのコマンド実行を備えた、OpenShell によるサンドボックスバックエンドです。 | `@openclaw/openshell-sandbox` |   
OpenClaw に同梱 | plugin |  |   
[perplexity](</ja-JP/plugins/reference/perplexity>) | Web 検索プロバイダー対応を追加します。 | `@openclaw/perplexity-plugin` |   
OpenClaw に同梱 | contracts: webSearchProviders |  |   
[qa-channel](</ja-JP/plugins/reference/qa-channel>) | OpenClaw メッセージを送受信するための QA Channel サーフェスを追加します。 | `@openclaw/qa-channel` |   
ソースチェックアウトのみ | channels: qa-channel |  |   
[qa-lab](</ja-JP/plugins/reference/qa-lab>) | プライベートデバッガー UI とシナリオランナーを備えた OpenClaw QA ラボ Plugin。 | `@openclaw/qa-lab` |   
ソースチェックアウトのみ | plugin |  |   
[qa-matrix](</ja-JP/plugins/reference/qa-matrix>) | Matrix QA トランスポートランナーと基盤。 | `@openclaw/qa-matrix` |   
ソースチェックアウトのみ | plugin |  |   
[qianfan](</ja-JP/plugins/reference/qianfan>) | OpenClaw に Qianfan モデルプロバイダーサポートを追加します。 | `@openclaw/qianfan-provider` |   
OpenClaw に同梱 | providers: qianfan |  |   
[qqbot](</ja-JP/plugins/reference/qqbot>) | OpenClaw メッセージを送受信するための QQ Bot チャネルサーフェスを追加します。 | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[qwen](</ja-JP/plugins/reference/qwen>) | OpenClaw に Qwen、Qwen Cloud、Model Studio、DashScope モデルプロバイダーサポートを追加します。 | `@openclaw/qwen-provider` |   
OpenClaw に同梱 | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</ja-JP/plugins/reference/runway>) | 動画生成プロバイダーサポートを追加します。 | `@openclaw/runway-provider` |   
OpenClaw に同梱 | contracts: videoGenerationProviders |  |   
[searxng](</ja-JP/plugins/reference/searxng>) | Web 検索プロバイダーサポートを追加します。 | `@openclaw/searxng-plugin` |   
OpenClaw に同梱 | contracts: webSearchProviders |  |   
[senseaudio](</ja-JP/plugins/reference/senseaudio>) | メディア理解プロバイダーサポートを追加します。 | `@openclaw/senseaudio-provider` |   
OpenClaw に同梱 | contracts: mediaUnderstandingProviders |  |   
[sglang](</ja-JP/plugins/reference/sglang>) | OpenClaw に SGLang モデルプロバイダーサポートを追加します。 | `@openclaw/sglang-provider` |   
OpenClaw に同梱 | providers: sglang |  |   
[signal](</ja-JP/plugins/reference/signal>) | OpenClaw メッセージを送受信するための Signal チャネルサーフェスを追加します。 | `@openclaw/signal` |   
OpenClaw に同梱 | channels: signal |  |   
[skill-workshop](</ja-JP/plugins/reference/skill-workshop>) | 保留中のレビュー、安全な書き込み、スキルプロンプトの更新とともに、反復可能なワークフローをワークスペーススキルとして取り込みます。 | `@openclaw/skill-workshop` |   
OpenClaw に同梱 | contracts: tools |  |   
[slack](</ja-JP/plugins/reference/slack>) | OpenClaw メッセージを送受信するための Slack チャネルサーフェスを追加します。 | `@openclaw/slack` |   
OpenClaw に同梱 | channels: slack |  |   
[stepfun](</ja-JP/plugins/reference/stepfun>) | OpenClaw に StepFun、StepFun Plan モデルプロバイダーサポートを追加します。 | `@openclaw/stepfun-provider` |   
OpenClaw に同梱 | providers: stepfun, stepfun-plan |  |   
[synology-chat](</ja-JP/plugins/reference/synology-chat>) | OpenClaw メッセージを送受信するための Synology Chat チャネルサーフェスを追加します。 | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[synthetic](</ja-JP/plugins/reference/synthetic>) | OpenClaw に Synthetic モデルプロバイダーサポートを追加します。 | `@openclaw/synthetic-provider` |   
OpenClaw に同梱 | providers: synthetic |  |   
[tavily](</ja-JP/plugins/reference/tavily>) | エージェントから呼び出せるツールを追加します。Web 検索プロバイダーサポートを追加します。 | `@openclaw/tavily-plugin` |   
OpenClaw に同梱 | contracts: tools, webSearchProviders; skills |  |   
[telegram](</ja-JP/plugins/reference/telegram>) | OpenClaw メッセージを送受信するための Telegram チャネルサーフェスを追加します。 | `@openclaw/telegram` |   
OpenClaw に同梱 | channels: telegram |  |   
[tencent](</ja-JP/plugins/reference/tencent>) | OpenClaw に Tencent TokenHub モデルプロバイダーサポートを追加します。 | `@openclaw/tencent-provider` |   
OpenClaw に同梱 | providers: tencent-tokenhub |  |   
[tlon](</ja-JP/plugins/reference/tlon>) | OpenClaw メッセージを送受信するための Tlon チャネルサーフェスを追加します。 | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[together](</ja-JP/plugins/reference/together>) | Together モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/together-provider` |   
OpenClaw に含まれる | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</ja-JP/plugins/reference/tokenjuice>) | tokenjuice リデューサーで exec と bash ツールの結果を圧縮します。 | `@openclaw/tokenjuice` |   
OpenClaw に含まれる | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</ja-JP/plugins/reference/tts-local-cli>) | テキスト読み上げプロバイダーサポートを追加します。 | `@openclaw/tts-local-cli` |   
OpenClaw に含まれる | contracts: speechProviders |  |   
[twitch](</ja-JP/plugins/reference/twitch>) | OpenClaw メッセージを送受信するための Twitch チャネルサーフェスを追加します。 | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[venice](</ja-JP/plugins/reference/venice>) | Venice モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/venice-provider` |   
OpenClaw に含まれる | providers: venice |  |   
[vercel-ai-gateway](</ja-JP/plugins/reference/vercel-ai-gateway>) | Vercel AI Gateway モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/vercel-ai-gateway-provider` |   
OpenClaw に含まれる | providers: vercel-ai-gateway |  |   
[vllm](</ja-JP/plugins/reference/vllm>) | vLLM モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/vllm-provider` |   
OpenClaw に含まれる | providers: vllm |  |   
[voice-call](</ja-JP/plugins/reference/voice-call>) | エージェントから呼び出し可能なツールを追加します。 | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[volcengine](</ja-JP/plugins/reference/volcengine>) | Volcengine、Volcengine Plan モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/volcengine-provider` |   
OpenClaw に含まれる | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</ja-JP/plugins/reference/voyage>) | メモリ埋め込みプロバイダーサポートを追加します。 | `@openclaw/voyage-provider` |   
OpenClaw に含まれる | contracts: memoryEmbeddingProviders |  |   
[vydra](</ja-JP/plugins/reference/vydra>) | Vydra モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/vydra-provider` |   
OpenClaw に含まれる | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</ja-JP/plugins/reference/web-readability>) | ローカル HTML Web 取得レスポンスから読みやすい記事コンテンツを抽出します。 | `@openclaw/web-readability-plugin` |   
OpenClaw に含まれる | contracts: webContentExtractors |  |   
[webhooks](</ja-JP/plugins/reference/webhooks>) | 外部自動化を OpenClaw TaskFlow に結び付ける、認証済みの受信 Webhook。 | `@openclaw/webhooks` |   
OpenClaw に含まれる | plugin |  |   
[whatsapp](</ja-JP/plugins/reference/whatsapp>) | OpenClaw メッセージを送受信するための WhatsApp チャネルサーフェスを追加します。 | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[xai](</ja-JP/plugins/reference/xai>) | xAI モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/xai-plugin` |   
OpenClaw に含まれる | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</ja-JP/plugins/reference/xiaomi>) | Xiaomi モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/xiaomi-provider` |   
OpenClaw に含まれる | providers: xiaomi; contracts: speechProviders |  |   
[zai](</ja-JP/plugins/reference/zai>) | [Z.AI](<http://Z.AI>) モデルプロバイダーサポートを OpenClaw に追加します。 | `@openclaw/zai-provider` |   
OpenClaw に含まれる | providers: zai; contracts: mediaUnderstandingProviders |  |   
[zalo](</ja-JP/plugins/reference/zalo>) | OpenClaw メッセージを送受信するための Zalo チャネルサーフェスを追加します。 | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</ja-JP/plugins/reference/zalouser>) | OpenClaw メッセージを送受信するための Zalo Personal チャネルサーフェスを追加します。 | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
Was this useful?YesNo