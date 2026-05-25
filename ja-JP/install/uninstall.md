---
title: アンインストール
source_url: https://docs.openclaw.ai/ja-JP/install/uninstall
scraped_at: 2026-05-25
---

方法は 2 つあります:

  * `openclaw` がまだインストールされている場合の **簡単な方法**
  * CLI は消えたがサービスがまだ動いている場合の **手動サービス削除**


## 簡単な方法（CLI がまだインストールされている）

推奨: 組み込みアンインストーラーを使います:

bashCopy code
[code]
    openclaw uninstall
[/code]

非対話モード（自動化 / npx）:

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

手動手順（結果は同じ）:

  1. gateway サービスを停止:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. gateway サービスをアンインストール（launchd/systemd/schtasks）:

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. state + config を削除:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

`OPENCLAW_CONFIG_PATH` を state dir 外のカスタム場所に設定していた場合は、そのファイルも削除してください。

  4. workspace を削除（任意。エージェントファイルも削除されます）:

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. CLI インストールを削除（使った方法に応じて選ぶ）:

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. macOS アプリをインストールしていた場合:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

注記:

  * profile（`--profile` / `OPENCLAW_PROFILE`）を使っていた場合は、各 state dir に対して手順 3 を繰り返してください（デフォルトは `~/.openclaw-<profile>`）。
  * リモートモードでは state dir は **gateway ホスト** 上にあるため、手順 1〜4 もそこで実行してください。


## 手動サービス削除（CLI がインストールされていない）

gateway サービスが動き続けているが `openclaw` が存在しない場合は、これを使ってください。

### macOS（launchd）

デフォルトラベルは `ai.openclaw.gateway`（または `ai.openclaw.<profile>`。旧来の `com.openclaw.*` が残っていることもあります）です:

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

profile を使っていた場合は、ラベルと plist 名を `ai.openclaw.<profile>` に置き換えてください。旧来の `com.openclaw.*` plist がある場合はそれも削除してください。

### Linux（systemd user unit）

デフォルト unit 名は `openclaw-gateway.service`（または `openclaw-gateway-<profile>.service`）です:

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows（Scheduled Task）

デフォルトタスク名は `OpenClaw Gateway`（または `OpenClaw Gateway (<profile>)`）です。 タスクスクリプトは state dir 配下にあります。

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

profile を使っていた場合は、対応するタスク名と `~\.openclaw-<profile>\gateway.cmd` を削除してください。

## 通常インストールとソース checkout の違い

### 通常インストール（[install.sh](<http://install.sh>) / npm / pnpm / bun）

`https://openclaw.ai/install.sh` または `install.ps1` を使った場合、CLI は `npm install -g openclaw@latest` でインストールされています。 `npm rm -g openclaw`（または、その方法でインストールしたなら `pnpm remove -g` / `bun remove -g`）で削除してください。

### ソース checkout（git clone）

リポジトリ checkout から実行している場合（`git clone` \+ `openclaw ...` / `bun run openclaw ...`）:

  1. リポジトリを削除する **前に** gateway サービスをアンインストールしてください（上記の簡単な方法または手動サービス削除を使う）。
  2. リポジトリディレクトリを削除します。
  3. 上記のとおり state + workspace を削除します。


## 関連

  * [Install overview](</ja-JP/install>)
  * [Migration guide](</ja-JP/install/migrating>)


Was this useful?YesNo