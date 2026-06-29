---
title: 権限モード
source_url: https://docs.openclaw.ai/ja-JP/tools/permission-modes
scraped_at: 2026-06-29
---

CapabilitiesTools

権限モードは、エージェントがホストコマンドを実行したり、ファイルを書き込んだり、backend harness に追加アクセスを求めたりする前に、どれだけの権限を持つかを決定します。OpenClaw にまず許可リストを使わせ、未一致の場合は Codex ネイティブ自動レビューまたは人間の承認ルートを使わせたい場合は、`tools.exec.mode: "auto"` から始めます。

## 推奨デフォルト

すべての未一致を人間への確認にせず、有用なホストアクセスが必要なコーディングエージェントには `auto` を使います。

bashCopy code
[code]
    openclaw config set tools.exec.mode autoopenclaw approvals getopenclaw gateway restart
[/code]

次に、有効なポリシーを確認します。

bashCopy code
[code]
    openclaw exec-policy show
[/code]

`auto` モードでは、OpenClaw は決定的な許可リスト一致を直接実行します。承認の未一致はまず OpenClaw のネイティブ自動レビューに渡され、必要に応じて設定済みの人間の承認ルートへフォールバックします。

## OpenClaw ホスト exec モード

`tools.exec.mode` はホスト `exec` の正規化されたポリシーサーフェスです。

モード | 動作 | 使用する場合  
---|---|---  
`deny` | ホスト exec をブロックします。 | ホストコマンドを一切許可しない場合。  
`allowlist` | 許可リスト済みのコマンドのみを実行します。 | 既知で安全なコマンドセットがある場合。  
`ask` | 許可リスト一致を実行し、未一致では確認します。 | 人間が新しいコマンドをレビューすべき場合。  
`auto` | 許可リスト一致を実行し、その後自動レビューを使います。 | コーディングセッションに実用的な保護付きアクセスが必要な場合。  
`full` | プロンプトなしでホスト exec を実行します。 | この信頼済みホスト/セッションで承認ゲートをスキップすべき場合。  
  
完全なホスト exec ポリシー、ローカル承認ファイル、許可リストスキーマ、安全なバイナリ、転送動作については、[Exec approvals](</ja-JP/tools/exec-approvals>) を参照してください。

## Codex Guardian のマッピング

ネイティブ Codex app-server セッションでは、ローカル Codex 要件が許可する場合、`tools.exec.mode: "auto"` は Codex Guardian にレビューされる承認へマッピングされます。OpenClaw は通常、次を送信します。

Codex フィールド | 一般的な値  
---|---  
`approvalPolicy` | `on-request`  
`approvalsReviewer` | `auto_review`  
`sandbox` | `workspace-write`  
  
`auto` モードでは、OpenClaw は `approvalPolicy: "never"` や `sandbox: "danger-full-access"` のような従来の安全でない Codex オーバーライドを保持しません。承認なしの姿勢を意図的に使いたい場合にのみ `tools.exec.mode: "full"` を使います。

app-server のセットアップ、認証順序、ネイティブ Codex ランタイムの詳細については、[Codex harness](</ja-JP/plugins/codex-harness>) を参照してください。

## ACPX ハーネス権限

ACPX セッションは非対話型のため、TTY 権限プロンプトをクリックできません。ACPX は `plugins.entries.acpx.config` 配下の別個のハーネスレベル設定を使います。

設定 | 一般的な値 | 意味  
---|---|---  
`permissionMode` | `approve-reads` | 読み取りのみを自動承認します。  
`permissionMode` | `approve-all` | 書き込みとシェルコマンドを自動承認します。  
`permissionMode` | `deny-all` | すべての権限プロンプトを拒否します。  
`nonInteractivePermissions` | `fail` | プロンプトが必要になる場合は中止します。  
`nonInteractivePermissions` | `deny` | プロンプトを拒否し、可能な場合は続行します。  
  
ACPX 権限は OpenClaw exec 承認とは別に設定します。

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions failopenclaw gateway restart
[/code]

`approve-all` は、プロンプトなしのハーネスセッションに相当する ACPX の非常時用設定として使います。セットアップの詳細と失敗モードについては、[ACP agents setup](</ja-JP/tools/acp-agents-setup#permission-configuration>) を参照してください。

## モードの選択

目的 | 設定  
---|---  
ホストコマンドを完全にブロックする | `tools.exec.mode: "deny"`  
既知で安全なコマンドのみを実行させる | `tools.exec.mode: "allowlist"`  
すべての新しいコマンド形状について人間に確認する | `tools.exec.mode: "ask"`  
人間の前に Codex/OpenClaw 自動レビューを使う | `tools.exec.mode: "auto"`  
ホスト exec 承認を完全にスキップする | `tools.exec.mode: "full"` と一致するホスト承認ファイル  
非対話型 ACPX セッションで書き込み/exec を可能にする | `plugins.entries.acpx.config.permissionMode: "approve-all"`  
  
モード変更後もコマンドがプロンプトを表示する、または失敗する場合は、両方のレイヤーを確認します。

bashCopy code
[code]
    openclaw approvals getopenclaw exec-policy show
[/code]

ホスト exec は OpenClaw 設定とホストローカル承認ファイルのうち、より厳しい結果を使います。ACPX ハーネス権限がホスト exec 承認を緩めることはなく、ホスト exec 承認が ACPX ハーネスプロンプトを緩めることもありません。

## 関連

  * [Exec approvals](</ja-JP/tools/exec-approvals>)
  * [Exec approvals - advanced](</ja-JP/tools/exec-approvals-advanced>)
  * [Codex harness](</ja-JP/plugins/codex-harness>)
  * [ACP agents setup](</ja-JP/tools/acp-agents-setup#permission-configuration>)


Was this useful?YesNo

Open issue