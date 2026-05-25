---
title: Node + tsx のクラッシュ
source_url: https://docs.openclaw.ai/ja-JP/debug/node-issue
scraped_at: 2026-05-25
---

# Node + tsx "__name is not a function" クラッシュ

## 概要

`tsx` を使って Node 経由で OpenClaw を実行すると、起動時に次のエラーで失敗します。

CodeCopy code
[code]
    [openclaw] Failed to start CLI: TypeError: __name is not a function    at createSubsystemLogger (.../src/logging/subsystem.ts:203:25)    at .../src/agents/auth-profiles/constants.ts:25:20
[/code]

これは、dev スクリプトを Bun から `tsx` に切り替えた後（コミット `2871657e`、2026-01-06）に発生し始めました。同じランタイムパスは Bun では動作していました。

## 環境

  * Node: v25.x（v25.3.0 で確認）
  * tsx: 4.21.0
  * OS: macOS（Node 25 を実行する他のプラットフォームでも再現する可能性あり）


## 再現手順（Node のみ）

bashCopy code
[code]
    # in repo rootnode --versionpnpm installnode --import tsx src/entry.ts status
[/code]

## リポジトリ内の最小再現

bashCopy code
[code]
    node --import tsx scripts/repro/tsx-name-repro.ts
[/code]

## Node バージョン確認

  * Node 25.3.0: 失敗
  * Node 22.22.0（Homebrew `node@22`）: 失敗
  * Node 24: ここではまだ未インストール。検証が必要


## メモ / 仮説

  * `tsx` は esbuild を使って TS/ESM を変換します。esbuild の `keepNames` は `__name` ヘルパーを生成し、関数定義を `__name(...)` でラップします。
  * このクラッシュは、実行時に `__name` は存在するものの関数ではないことを示しており、Node 25 のローダーパスでこのモジュールのヘルパーが欠落しているか上書きされていることを意味します。
  * 同様の `__name` ヘルパーの問題は、ヘルパーが欠落または書き換えられた場合に、他の esbuild 利用側でも報告されています。


## 回帰履歴

  * `2871657e`（2026-01-06）: Bun を任意にするため、スクリプトが Bun から tsx に変更されました。
  * それ以前（Bun パス）では、`openclaw status` と `gateway:watch` は動作していました。


## 回避策

  * dev スクリプトには Bun を使用します（現在の一時的な差し戻し）。

  * リポジトリの型チェックに `tsgo` を使用し、その後ビルド済み出力を実行します。

bashCopy code
[code]pnpm tsgonode openclaw.mjs status
[/code]

  * 履歴メモ: この Node/tsx 問題のデバッグ中はここで `tsc` が使われていましたが、現在のリポジトリの型チェックレーンは `tsgo` を使用しています。

  * 可能であれば、TS ローダーで esbuild の keepNames を無効化します（`__name` ヘルパーの挿入を防ぎます）。tsx は現在これを公開していません。

  * Node LTS（22/24）で `tsx` をテストし、この問題が Node 25 固有かどうかを確認します。


## 参考

  * <https://opennext.js.org/cloudflare/howtos/keep_names>
  * <https://esbuild.github.io/api/#keep-names>
  * <https://github.com/evanw/esbuild/issues/1031>


## 次の手順

  * Node 22/24 で再現し、Node 25 の回帰か確認します。
  * 既知の回帰がある場合は、`tsx` nightly をテストするか以前のバージョンに固定します。
  * Node LTS で再現する場合は、`__name` スタックトレースを含む最小再現を upstream に報告します。


## 関連

  * [Node.js インストール](</ja-JP/install/node>)
  * [Gateway トラブルシューティング](</ja-JP/gateway/troubleshooting>)


Was this useful?YesNo