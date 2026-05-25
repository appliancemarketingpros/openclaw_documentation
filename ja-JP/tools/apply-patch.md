---
title: apply_patch ツール
source_url: https://docs.openclaw.ai/ja-JP/tools/apply-patch
scraped_at: 2026-05-25
---

構造化されたパッチ形式を使用してファイル変更を適用します。これは、単一の `edit` 呼び出しでは壊れやすくなる複数ファイルまたは複数ハンクの編集に最適です。

このツールは、1 つ以上のファイル操作をラップする単一の `input` 文字列を受け取ります。

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## パラメーター

  * `input`（必須）: `*** Begin Patch` と `*** End Patch` を含む完全なパッチ内容。


## 注意事項

  * パッチパスは相対パス（ワークスペースディレクトリから）と絶対パスに対応しています。
  * `tools.exec.applyPatch.workspaceOnly` のデフォルトは `true`（ワークスペース内に限定）です。意図的に `apply_patch` でワークスペースディレクトリ外へ書き込みまたは削除したい場合にのみ、`false` に設定してください。
  * ファイル名を変更するには、`*** Update File:` ハンク内で `*** Move to:` を使用します。
  * `*** End of File` は、必要な場合に EOF のみの挿入を示します。
  * OpenAI および OpenAI Codex モデルではデフォルトで利用できます。無効にするには、 `tools.exec.applyPatch.enabled: false` を設定します。
  * 必要に応じて、モデル別に `tools.exec.applyPatch.allowModels` で制限できます。
  * 設定は `tools.exec` の下にのみあります。


## 例

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## 関連

[**差分** 変更内容の表示用の読み取り専用差分ビューアー。 ](</ja-JP/tools/diffs>) [**Exec ツール** エージェントからのシェルコマンド実行。 ](</ja-JP/tools/exec>) [**コード実行** xAI によるサンドボックス化されたリモート Python 解析。 ](</ja-JP/tools/code-execution>)

Was this useful?YesNo