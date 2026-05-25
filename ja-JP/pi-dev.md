---
title: Pi 開発ワークフロー
source_url: https://docs.openclaw.ai/ja-JP/pi-dev
scraped_at: 2026-05-25
---

OpenClaw の Pi 統合に取り組むための健全なワークフロー。

## 型チェックと lint

  * デフォルトのローカルゲート: `pnpm check`
  * ビルドゲート: 変更がビルド出力、パッケージング、または lazy-loading/module 境界に影響する可能性がある場合は `pnpm build`
  * Pi 関連の大きな変更向けの完全な landing ゲート: `pnpm check && pnpm test`


## Pi テストの実行

Pi に重点を置いたテストセットを Vitest で直接実行します。

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

live provider の演習を含めるには、次を実行します。

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

これは主要な Pi ユニットスイートをカバーします。

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## 手動テスト

推奨フロー:

  * Gateway を開発モードで実行します。 
    * `pnpm gateway:dev`
  * エージェントを直接トリガーします。 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * 対話的なデバッグには TUI を使用します。 
    * `pnpm tui`


ツール呼び出しの動作については、ツールストリーミングとペイロード処理を確認できるように、`read` または `exec` アクションを促してください。

## クリーンスレートのリセット

状態は OpenClaw の状態ディレクトリ配下にあります。デフォルトは `~/.openclaw` です。`OPENCLAW_STATE_DIR` が設定されている場合は、代わりにそのディレクトリを使用します。

すべてをリセットするには、次を対象にします。

  * 設定用の `openclaw.json`
  * モデル認証プロファイル（APIキー + OAuth）用の `agents/<agentId>/agent/auth-profiles.json`
  * 認証プロファイルストアの外側にまだ存在するプロバイダー/チャネル状態用の `credentials/`
  * エージェントセッション履歴用の `agents/<agentId>/sessions/`
  * セッションインデックス用の `agents/<agentId>/sessions/sessions.json`
  * レガシーパスが存在する場合は `sessions/`
  * 空のワークスペースが必要な場合は `workspace/`


セッションだけをリセットしたい場合は、そのエージェントの `agents/<agentId>/sessions/` を削除します。認証を保持したい場合は、`agents/<agentId>/agent/auth-profiles.json` と `credentials/` 配下のプロバイダー状態をそのまま残します。

## 参考資料

  * [テスト](</ja-JP/help/testing>)
  * [はじめに](</ja-JP/start/getting-started>)


## 関連

  * [Pi 統合アーキテクチャ](</ja-JP/pi>)


Was this useful?YesNo