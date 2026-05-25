---
title: Nix
source_url: https://docs.openclaw.ai/ja-JP/install/nix
scraped_at: 2026-05-25
---

OpenClaw を **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** で宣言的にインストールします - ファーストパーティの、必要な機能を含む Home Manager モジュールです。

## 得られるもの

  * Gateway + macOS アプリ + ツール (whisper, spotify, cameras) -- すべてピン留め済み
  * 再起動後も維持される launchd サービス
  * 宣言的設定に対応した Plugin システム
  * 即時ロールバック: `home-manager switch --rollback`


## クイックスタート

* ### Determinate Nix をインストールする

Nix がまだインストールされていない場合は、[Determinate Nix installer](<https://github.com/DeterminateSystems/nix-installer>) の手順に従ってください。

* ### ローカル flake を作成する

nix-openclaw リポジトリのエージェント優先テンプレートを使用します:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### シークレットを設定する

メッセージングボットのトークンとモデルプロバイダーの API キーを設定します。`~/.secrets/` にあるプレーンファイルで問題なく機能します。

* ### テンプレートのプレースホルダーを埋めて切り替える

bashCopy code
[code]
    home-manager switch
[/code]

* ### 検証する

launchd サービスが実行中で、ボットがメッセージに応答することを確認します。

完全なモジュールオプションと例については、[nix-openclaw README](<https://github.com/openclaw/nix-openclaw>) を参照してください。

## Nix モードのランタイム動作

`OPENCLAW_NIX_MODE=1` が設定されている場合 (nix-openclaw では自動)、OpenClaw は Nix 管理のインストール向けの決定論的モードに入ります。他の Nix パッケージも同じモードを設定できます。nix-openclaw はファーストパーティのリファレンスです。

手動で設定することもできます:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

macOS では、GUI アプリはシェル環境変数を自動的には継承しません。代わりに defaults 経由で Nix モードを有効にします:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Nix モードで変わること

  * 自動インストールと自己変更フローが無効になります
  * `openclaw.json` はイミュータブルとして扱われます。起動時に導出されるデフォルトはランタイムのみのままで、setup、オンボーディング、変更を伴う `openclaw update`、Plugin のインストール/更新/アンインストール/有効化、`doctor --fix`、`doctor --generate-gateway-token`、`openclaw config set` などの設定ライターはファイルの編集を拒否します。
  * エージェントは代わりに Nix ソースを編集する必要があります。nix-openclaw では、エージェント優先の [クイックスタート](<https://github.com/openclaw/nix-openclaw#quick-start>) を使用し、`programs.openclaw.config` または `instances.<name>.config` の下に設定を置きます。
  * 不足している依存関係には Nix 固有の修復メッセージが表示されます
  * UI に読み取り専用の Nix モードバナーが表示されます


### 設定と状態のパス

OpenClaw は `OPENCLAW_CONFIG_PATH` から JSON5 設定を読み取り、可変データを `OPENCLAW_STATE_DIR` に保存します。Nix 下で実行する場合は、ランタイム状態と設定がイミュータブルなストアに入らないよう、これらを Nix 管理の場所へ明示的に設定してください。

変数 | デフォルト  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### サービス PATH の検出

launchd/systemd の gateway サービスは Nix プロファイルのバイナリを自動検出するため、 Plugin や、`nix` でインストールされた実行可能ファイルをシェルアウトするツールは、 手動の PATH 設定なしで機能します:

  * `NIX_PROFILES` が設定されている場合、すべてのエントリが右から左の優先順位でサービス PATH に追加されます (Nix シェルの優先順位と一致します - 右端が優先されます)。
  * `NIX_PROFILES` が未設定の場合、フォールバックとして `~/.nix-profile/bin` が追加されます。


これは macOS launchd と Linux systemd の両方のサービス環境に適用されます。

## 関連

[**nix-openclaw** 信頼できる情報源である Home Manager モジュールと完全なセットアップガイド。 ](<https://github.com/openclaw/nix-openclaw>) [**セットアップウィザード** Nix 以外の CLI セットアップ手順。 ](</ja-JP/start/wizard>) [**Docker** Nix 以外の代替手段としてのコンテナ化セットアップ。 ](</ja-JP/install/docker>) [**更新** パッケージとあわせて Home Manager 管理のインストールを更新する方法。 ](</ja-JP/install/updating>)

Was this useful?YesNo