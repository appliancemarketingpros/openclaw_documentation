---
title: llama.cpp プロバイダー
source_url: https://docs.openclaw.ai/ja-JP/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` は、ローカル GGUF 埋め込み用の公式外部プロバイダー Plugin です。 これは `memorySearch.provider: "local"` で使用される `node-llama-cpp` ランタイム依存関係を所有します。

ローカルメモリ埋め込みを使用する前にインストールしてください。

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

メインの `openclaw` npm パッケージには `node-llama-cpp` は含まれていません。ネイティブ依存関係をこの Plugin に置くことで、通常の OpenClaw npm 更新が、OpenClaw パッケージディレクトリ内に手動でインストールされたランタイムを削除してしまうことを防げます。

## 設定

メモリ検索プロバイダーを `local` に設定します。

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

デフォルトモデルは `embeddinggemma-300m-qat-Q8_0.gguf` です。`local.modelPath` にローカルの `.gguf` ファイルを指定することもできます。

## ネイティブランタイム

ネイティブインストール手順を最もスムーズに進めるには Node 24 を使用してください。pnpm を使用するソースチェックアウトでは、ネイティブ依存関係の承認と再ビルドが必要になる場合があります。

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

より手間の少ないローカル埋め込みには、代わりに Ollama や LM Studio などのローカルサービスプロバイダーを使用してください。

Was this useful?YesNo

Open issue