---
title: Pluginの構築
source_url: https://docs.openclaw.ai/ja-JP/plugins/building-plugins
scraped_at: 2026-05-25
---

Plugin は、チャネル、モデルプロバイダー、音声、リアルタイム文字起こし、リアルタイム音声、メディア理解、画像生成、動画生成、web fetch、web search、エージェントツール、またはそれらの任意の組み合わせといった新しい機能で OpenClaw を拡張します。

Plugin を OpenClaw リポジトリに追加する必要はありません。[ClawHub](</ja-JP/clawhub>) に公開すると、ユーザーは `openclaw plugins install clawhub:<package-name>` でインストールできます。ベアパッケージ指定は、ローンチ移行期間中は引き続き npm からインストールされます。

## 前提条件

  * Node >= 22 とパッケージマネージャー（npm または pnpm）
  * TypeScript（ESM）に慣れていること
  * リポジトリ内 Plugin の場合: リポジトリをクローンし、`pnpm install` を完了していること。ソースチェックアウトでの Plugin 開発は pnpm のみです。OpenClaw は `extensions/*` ワークスペースパッケージからバンドル済み Plugin を読み込むためです。


## どの種類の Plugin ですか？

[**チャネル Plugin** OpenClaw をメッセージングプラットフォーム（Discord、IRC など）に接続します ](</ja-JP/plugins/sdk-channel-plugins>) [**プロバイダー Plugin** モデルプロバイダー（LLM、プロキシ、またはカスタムエンドポイント）を追加します ](</ja-JP/plugins/sdk-provider-plugins>) [**CLI バックエンド Plugin** ローカル AI CLI を OpenClaw のテキストフォールバックランナーに対応付けます ](</ja-JP/plugins/cli-backend-plugins>) [**ツール / フック Plugin** エージェントツール、イベントフック、またはサービスを登録します - 以下に進んでください ](</ja-JP/plugins/hooks>)

オンボーディング/セットアップの実行時にインストール済みであることが保証されないチャネル Plugin では、`openclaw/plugin-sdk/channel-setup` の `createOptionalChannelSetupSurface(...)` を使用してください。これは、インストール要件を通知し、Plugin がインストールされるまで実際の設定書き込みでフェイルクローズする、セットアップアダプターとウィザードのペアを生成します。

## クイックスタート: ツール Plugin

このウォークスルーでは、エージェントツールを登録する最小限の Plugin を作成します。チャネルおよびプロバイダー Plugin には、上記にリンクされた専用ガイドがあります。

* ### パッケージとマニフェストを作成する

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

すべての Plugin には、設定がない場合でもマニフェストが必要です。ランタイムで登録されるツールは `contracts.tools` に列挙する必要があります。これにより、OpenClaw はすべての Plugin ランタイムを読み込まずに、所有する Plugin を検出できます。Plugin は `activation.onStartup` も意図的に宣言する必要があります。この例では `true` に設定しています。完全なスキーマについては [マニフェスト](</ja-JP/plugins/manifest>) を参照してください。正規の ClawHub 公開スニペットは `docs/snippets/plugin-publish/` にあります。

* ### エントリーポイントを書く

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` は非チャネル Plugin 用です。チャネルでは `defineChannelPluginEntry` を使用してください - [チャネル Plugin](</ja-JP/plugins/sdk-channel-plugins>) を参照してください。エントリーポイントのすべてのオプションについては、[エントリーポイント](</ja-JP/plugins/sdk-entrypoints>) を参照してください。

* ### テストして公開する

**外部 Plugin:** ClawHub で検証して公開し、その後インストールします。

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

`@myorg/openclaw-my-plugin` のようなベアパッケージ指定は、ローンチ移行期間中は npm からインストールされます。ClawHub 解決を使いたい場合は `clawhub:` を使用してください。

**リポジトリ内 Plugin:** バンドル済み Plugin ワークスペースツリーの下に配置します - 自動的に検出されます。

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Plugin 機能

単一の Plugin は、`api` オブジェクトを介して任意の数の機能を登録できます。

機能 | 登録メソッド | 詳細ガイド  
---|---|---  
テキスト推論（LLM） | `api.registerProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins>)  
CLI 推論バックエンド | `api.registerCliBackend(...)` | [CLI バックエンド Plugin](</ja-JP/plugins/cli-backend-plugins>)  
チャネル / メッセージング | `api.registerChannel(...)` | [チャネル Plugin](</ja-JP/plugins/sdk-channel-plugins>)  
音声（TTS/STT） | `api.registerSpeechProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
リアルタイム文字起こし | `api.registerRealtimeTranscriptionProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
リアルタイム音声 | `api.registerRealtimeVoiceProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
メディア理解 | `api.registerMediaUnderstandingProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
画像生成 | `api.registerImageGenerationProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
音楽生成 | `api.registerMusicGenerationProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
動画生成 | `api.registerVideoGenerationProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Web fetch | `api.registerWebFetchProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Web search | `api.registerWebSearchProvider(...)` | [プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
ツール結果ミドルウェア | `api.registerAgentToolResultMiddleware(...)` | [SDK 概要](</ja-JP/plugins/sdk-overview#registration-api>)  
エージェントツール | `api.registerTool(...)` | 以下  
カスタムコマンド | `api.registerCommand(...)` | [エントリーポイント](</ja-JP/plugins/sdk-entrypoints>)  
Plugin フック | `api.on(...)` | [Plugin フック](</ja-JP/plugins/hooks>)  
内部イベントフック | `api.registerHook(...)` | [エントリーポイント](</ja-JP/plugins/sdk-entrypoints>)  
HTTP ルート | `api.registerHttpRoute(...)` | [内部構造](</ja-JP/plugins/architecture-internals#gateway-http-routes>)  
CLI サブコマンド | `api.registerCli(...)` | [エントリーポイント](</ja-JP/plugins/sdk-entrypoints>)  
  
完全な登録 API については、[SDK 概要](</ja-JP/plugins/sdk-overview#registration-api>) を参照してください。

バンドル済み Plugin は、モデルが出力を見る前に非同期のツール結果書き換えが必要な場合、`api.registerAgentToolResultMiddleware(...)` を使用できます。対象ランタイムを `contracts.agentToolResultMiddleware` に宣言してください。たとえば `["pi", "codex"]` です。これは信頼済みバンドル Plugin の接点です。外部 Plugin は、OpenClaw がこの機能の明示的な信頼ポリシーを拡張するまでは、通常の OpenClaw Plugin フックを優先してください。

Plugin がカスタム Gateway RPC メソッドを登録する場合は、Plugin 固有のプレフィックス上に保ってください。コア管理名前空間（`config.*`、`exec.approvals.*`、`wizard.*`、`update.*`）は予約されたままで、Plugin がより狭いスコープを要求しても常に `operator.admin` に解決されます。

覚えておくべきフックガードのセマンティクス:

  * `before_tool_call`: `{ block: true }` は終端であり、優先度の低いハンドラーを停止します。
  * `before_tool_call`: `{ block: false }` は判断なしとして扱われます。
  * `before_tool_call`: `{ requireApproval: true }` はエージェントの実行を一時停止し、exec 承認オーバーレイ、Telegram ボタン、Discord インタラクション、または任意のチャネルの `/approve` コマンドを介してユーザーに承認を求めます。
  * `before_install`: `{ block: true }` は終端であり、優先度の低いハンドラーを停止します。
  * `before_install`: `{ block: false }` は判断なしとして扱われます。
  * `message_sending`: `{ cancel: true }` は終端であり、優先度の低いハンドラーを停止します。
  * `message_sending`: `{ cancel: false }` は判断なしとして扱われます。
  * `message_received`: 受信スレッド/トピックのルーティングが必要な場合は、型付きの `threadId` フィールドを優先してください。`metadata` はチャネル固有の追加情報用に保ってください。
  * `message_sending`: チャネル固有のメタデータキーよりも、型付きの `replyToId` / `threadId` ルーティングフィールドを優先してください。


`/approve` コマンドは、有界フォールバックにより exec 承認と Plugin 承認の両方を処理します。exec 承認 ID が見つからない場合、OpenClaw は同じ ID で Plugin 承認を再試行します。Plugin 承認の転送は、設定内の `approvals.plugin` で独立して構成できます。

カスタム承認の配管で同じ有界フォールバックケースを検出する必要がある場合は、承認期限切れ文字列を手動で照合する代わりに、`openclaw/plugin-sdk/error-runtime` の `isApprovalNotFoundError` を優先してください。

例とフックリファレンスについては、[Plugin フック](</ja-JP/plugins/hooks>) を参照してください。

## エージェントツールの登録

ツールは、LLM が呼び出せる型付き関数です。必須（常に利用可能）または任意（ユーザーのオプトイン）にできます。

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Tool ファクトリは、ランタイムから提供されるコンテキストオブジェクトを受け取ります。ツールが現在のターンのアクティブなモデルを記録、表示、またはそれに適応する必要がある場合は、`ctx.activeModel` を使用してください。このオブジェクトには `provider`、`modelId`、`modelRef` を含められます。これは情報提供用のランタイムメタデータとして扱い、ローカルオペレーター、インストール済みの Plugin コード、または変更された OpenClaw ランタイムに対するセキュリティ境界として扱わないでください。機密性の高いローカルツールでは、明示的な Plugin またはオペレーターのオプトインを維持し、アクティブモデルメタデータがない場合や適切でない場合はフェイルクローズしてください。

`api.registerTool(...)` で登録されるすべてのツールは、Plugin マニフェストでも宣言する必要があります。

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw は登録されたツールから検証済みディスクリプターを取得してキャッシュするため、Plugin はマニフェスト内で `description` やスキーマデータを重複させません。マニフェストコントラクトは所有権と検出だけを宣言します。実行時には引き続き、ライブ登録されたツール実装が呼び出されます。 `api.registerTool(..., { optional: true })` で登録されたツールには `toolMetadata.<tool>.optional: true` を設定してください。これにより OpenClaw は、そのツールが明示的に許可リストに追加されるまで、その Plugin ランタイムのロードを回避できます。

ユーザーは設定で任意ツールを有効にします。

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * ツール名はコアツールと衝突してはいけません（衝突したものはスキップされます）
  * `parameters` の欠落を含む、不正な登録オブジェクトを持つツールは、エージェント実行を壊す代わりにスキップされ、Plugin 診断で報告されます
  * 副作用や追加のバイナリ要件を持つツールには `optional: true` を使用してください
  * ユーザーは Plugin ID を `tools.allow` に追加することで、その Plugin のすべてのツールを有効にできます


## CLI コマンドの登録

Plugin は `api.registerCli` を使って、ルート `openclaw` コマンドグループを追加できます。OpenClaw がすべての Plugin ランタイムを先読みせずにコマンドを表示してルーティングできるように、各トップレベルコマンドルートに `descriptors` を提供してください。

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

インストール後、ランタイム登録を検証してコマンドを実行します。

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## インポート規約

常に対象を絞った `openclaw/plugin-sdk/<subpath>` パスからインポートしてください。

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

完全なサブパスリファレンスについては、[SDK 概要](</ja-JP/plugins/sdk-overview>)を参照してください。

Plugin 内では、内部インポートにローカルのバレルファイル（`api.ts`、`runtime-api.ts`）を使用してください。自分の Plugin を SDK パス経由でインポートしてはいけません。

Provider Plugin では、そのつなぎ目が本当に汎用でない限り、プロバイダー固有のヘルパーをそれらのパッケージルートのバレルに保持してください。現在のバンドル例は次のとおりです。

  * Anthropic: Claude ストリームラッパーと `service_tier` / ベータヘルパー
  * OpenAI: プロバイダービルダー、デフォルトモデルヘルパー、リアルタイムプロバイダー
  * OpenRouter: プロバイダービルダーとオンボーディング/設定ヘルパー


ヘルパーが 1 つのバンドル済みプロバイダーパッケージ内でしか有用でない場合は、`openclaw/plugin-sdk/*` に昇格させるのではなく、そのパッケージルートのつなぎ目に保持してください。

一部の生成済み `openclaw/plugin-sdk/<bundled-id>` ヘルパーのつなぎ目は、所有者の使用状況が追跡されている場合のバンドル済み Plugin メンテナンス用としてまだ存在します。これらは予約済みサーフェスとして扱い、新しいサードパーティ Plugin の既定パターンとして扱わないでください。

## 提出前チェックリスト

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** に正しい `openclaw` メタデータがある OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **openclaw.plugin.json** マニフェストが存在し、有効である OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s エントリポイントが `defineChannelPluginEntry` または `definePluginEntry` を使用している OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s すべてのインポートが対象を絞った `plugin-sdk/<subpath>` パスを使用している OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo