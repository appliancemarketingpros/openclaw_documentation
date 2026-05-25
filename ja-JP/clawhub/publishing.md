---
title: 公開
source_url: https://docs.openclaw.ai/ja-JP/clawhub/publishing
scraped_at: 2026-05-25
---

# 公開

ClawHub の公開は所有者スコープです。すべての公開はパブリッシャーを対象にし、サーバーがサインイン中のユーザーにそこで公開する権限があるかどうかを判断します。

## 所有者

所有者は、`@alice` や `@openclaw` のような ClawHub のパブリッシャーハンドルです。個人所有者はユーザー向けに作成されます。組織所有者は複数のメンバーを持つことができます。

公開するときは、自分の個人所有者を使うか、パブリッシャーアクセス権を持つ組織所有者を選びます。

## Skills

Skills はスキルフォルダーから公開されます。公開ページは次のとおりです。

textCopy code
[code]
    https://clawhub.ai/<owner>/<slug>
[/code]

例:

textCopy code
[code]
    https://clawhub.ai/alice/review-helper
[/code]

公開リクエストには、選択した所有者、スラッグ、バージョン、変更履歴、ファイルが含まれます。サーバーはリリースを作成する前に、そのアクターがその所有者として公開できることを検証します。

新しいバージョンを公開しながら既存のスキルを別の所有者へ移動するには、新しい所有者を選び、所有権の移動を明示的に確認します。CLI/API では、移行のオプトインとともに対象の所有者を渡します。

shCopy code
[code]
    clawhub skill publish ./review-helper --owner openclaw --migrate-owner --version 1.2.0
[/code]

スキル所有者の移行には、現在の所有者と移行先の所有者の両方で admin または owner アクセス権が必要です。これはスキル、バージョン履歴、統計、コメント、フォーク、エイリアス、監査証跡を保持します。古い所有者 URL はエイリアス/リダイレクトパスを通じて引き続き機能します。

## Plugin

Plugin は npm スタイルのパッケージ名を使います。スコープ付きパッケージ名では、名前の最初の部分に所有者が含まれます。

textCopy code
[code]
    @owner/package-name
[/code]

スコープは、選択した公開所有者と一致している必要があります。パッケージ名が `@openclaw/dronzer` の場合、`@openclaw` としてのみ公開できます。`@vintageayu` として公開する場合は、パッケージ名を `@vintageayu/dronzer` に変更してください。

これにより、パブリッシャーが管理していない組織名前空間をパッケージが主張することを防ぎます。

## リリースフロー

  1. UI、CLI、または GitHub ワークフローがパッケージメタデータとファイルを収集します。
  2. 公開リクエストが、選択した所有者とともに ClawHub に送信されます。
  3. サーバーは所有者の権限、パッケージスコープ、パッケージ名、バージョン、ファイル制限、ソースメタデータを検証します。
  4. ClawHub はリリースを保存し、自動セキュリティチェックを開始します。
  5. 新しいリリースは、レビューと検証が完了するまで通常のインストール/ダウンロード画面には表示されません。


検証に失敗した場合、リリースは作成されません。

## よくある質問

### パッケージスコープは選択した所有者と一致する必要があります

パッケージスコープと選択した所有者が一致しない場合、ClawHub は公開を拒否します。

textCopy code
[code]
    Package scope "@openclaw" must match selected owner "@vintageayu".Publish as "@openclaw" or rename this package to "@vintageayu/dronzer".
[/code]

修正するには、パッケージスコープで指定された所有者を選ぶか、公開可能な所有者とスコープが一致するようにパッケージ名を変更します。

パッケージ名にすでに正しいスコープが付いているものの、パッケージが誤ったパブリッシャーに所有されている場合は、代わりに所有権を移管します。

shCopy code
[code]
    clawhub package transfer @opik/opik-openclaw --to opik
[/code]

パッケージまたはスキルの移管は、現在の所有者と移行先パブリッシャーの両方に対する admin アクセス権を持っている場合にのみ使用してください。パッケージ移管では、管理できないスコープへ公開することはできません。

これは組織名前空間を保護します。`@openclaw/dronzer` という名前のパッケージは `@openclaw` 名前空間を主張するため、`@openclaw` 所有者へのアクセス権を持つパブリッシャーだけがそれを公開できます。

Was this useful?YesNo