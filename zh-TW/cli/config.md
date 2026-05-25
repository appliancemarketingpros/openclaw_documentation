---
title: 設定
source_url: https://docs.openclaw.ai/zh-TW/cli/config
scraped_at: 2026-05-25
---

`openclaw.json` 中用於非互動式編輯的設定輔助工具：依路徑取得/設定/修補/取消設定/檔案/結構描述/驗證值，並列印作用中的設定檔。不帶子命令執行時，會開啟設定精靈（等同於 `openclaw configure`）。

## 根選項

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> 當你執行不帶子命令的 `openclaw config` 時，可重複使用的引導式設定區段篩選器。

支援的引導式區段：`workspace`、`model`、`web`、`gateway`、`daemon`、`channels`、`plugins`、`skills`、`health`。

## 範例

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

將為 `openclaw.json` 產生的 JSON 結構描述以 JSON 形式列印到 stdout。

What it includes

  * 目前的根設定結構描述，加上一個供編輯器工具使用的根 `$schema` 字串欄位。
  * Control UI 使用的欄位 `title` 和 `description` 文件中繼資料。
  * 當存在相符的欄位文件時，巢狀物件、萬用字元（`*`）和陣列項目（`[]`）節點會繼承相同的 `title` / `description` 中繼資料。
  * 當存在相符的欄位文件時，`anyOf` / `oneOf` / `allOf` 分支也會繼承相同的文件中繼資料。
  * 當執行階段資訊清單可載入時，會盡力提供即時 Plugin + 通道結構描述中繼資料。
  * 即使目前設定無效，也會提供乾淨的後援結構描述。

Related runtime RPC

`config.schema.lookup` 會傳回一個正規化的設定路徑，其中包含淺層結構描述節點（`title`、`description`、`type`、`enum`、`const`、常見邊界）、相符的 UI 提示中繼資料，以及直接子項摘要。可在 Control UI 或自訂用戶端中用於路徑範圍的深入檢視。

bashCopy code
[code]
    openclaw config schema
[/code]

若你想用其他工具檢查或驗證它，可將其透過管線輸出到檔案：

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### 路徑

路徑使用點記法或括號記法：

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

使用 agent 清單索引來指定特定 agent：

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## 值

值會在可能時解析為 JSON5；否則會被視為字串。使用 `--strict-json` 要求 JSON5 解析。`--json` 仍支援作為舊版別名。

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` 會以 JSON 列印原始值，而不是終端格式化文字。

將項目加入這些 map 時，請使用 `--merge`：

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

只有在你刻意希望提供的值成為完整目標值時，才使用 `--replace`。

## `config set` 模式

`openclaw config set` 支援四種指派樣式：

### Value mode

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### SecretRef builder mode

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Provider builder mode

Provider 建構器模式只以 `secrets.providers.<alias>` 路徑為目標：

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Batch mode

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

批次解析一律使用批次承載（`--batch-json`/`--batch-file`）作為事實來源。`--strict-json` / `--json` 不會改變批次解析行為。

## `config patch`

當你想貼上或透過管線傳入設定形狀的修補，而不是執行許多基於路徑的 `config set` 命令時，請使用 `config patch`。輸入是 JSON5 物件。物件會遞迴合併，陣列和純量值會取代目標值，而 `null` 會刪除目標路徑。

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

你也可以透過 stdin 傳入修補，這對遠端設定腳本很有用：

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

修補範例：

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

當某個物件或陣列必須精確成為提供的值，而不是被遞迴修補時，請使用 `--replace-path <path>`：

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` 會在不寫入的情況下執行結構描述和 SecretRef 可解析性檢查。在 dry-run 期間，預設會略過 exec 後端的 SecretRef；當你刻意希望 dry-run 執行 provider 命令時，請加入 `--allow-exec`。

JSON 路徑/值模式仍同時支援 SecretRefs 和 providers：

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Provider 建構器旗標

Provider 建構器目標必須使用 `secrets.providers.<alias>` 作為路徑。

Common flags

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>`（`file`、`exec`）

Env provider (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;`（可重複）

File provider (--provider-source file)

  * `--provider-path <path>`（必填）
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Exec provider (--provider-source exec)

  * `--provider-command <path>`（必填）
  * `--provider-arg <arg>`（可重複）
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;`（可重複）
  * `--provider-pass-env &lt;ENV_VAR&gt;`（可重複）
  * `--provider-trusted-dir <path>`（可重複）
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


強化的 exec provider 範例：

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Dry run

使用 `--dry-run` 可在不寫入 `openclaw.json` 的情況下驗證變更。

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Dry-run behavior

  * 建構器模式：對變更的 refs/providers 執行 SecretRef 可解析性檢查。
  * JSON 模式（`--strict-json`、`--json` 或批次模式）：執行結構描述驗證加上 SecretRef 可解析性檢查。
  * 政策驗證也會針對已知不支援的 SecretRef 目標表面執行。
  * 政策檢查會評估完整的變更後設定，因此父物件寫入（例如將 `hooks` 設為物件）無法繞過不支援表面驗證。
  * Exec SecretRef 檢查在 dry-run 期間預設會略過，以避免命令副作用。
  * 搭配 `--dry-run` 使用 `--allow-exec`，可選擇加入 exec SecretRef 檢查（這可能會執行 provider 命令）。
  * `--allow-exec` 僅適用於 dry-run；若未搭配 `--dry-run` 使用會報錯。

\--dry-run --json fields

`--dry-run --json` 會列印機器可讀的報告：

  * `ok`: 試執行是否通過
  * `operations`: 已評估的指派數量
  * `checks`: 結構描述/可解析性檢查是否已執行
  * `checks.resolvabilityComplete`: 可解析性檢查是否執行至完成（跳過 exec refs 時為 false）
  * `refsChecked`: 試執行期間實際解析的 ref 數量
  * `skippedExecRefs`: 因未設定 `--allow-exec` 而跳過的 exec refs 數量
  * `errors`: 當 `ok=false` 時的結構化結構描述/可解析性失敗


### JSON 輸出形狀

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### 成功範例

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### 失敗範例

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

如果試執行失敗

  * `config schema validation failed`: 變更後的設定形狀無效；請修正路徑/值或 provider/ref 物件形狀。
  * `Config policy validation failed: unsupported SecretRef usage`: 將該認證移回純文字/字串輸入，並只在支援的介面上保留 SecretRefs。
  * `SecretRef assignment(s) could not be resolved`: 參照的 provider/ref 目前無法解析（缺少環境變數、檔案指標無效、exec provider 失敗，或 provider/source 不相符）。
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: 試執行已跳過 exec refs；如果需要驗證 exec 可解析性，請使用 `--allow-exec` 重新執行。
  * 批次模式請先修正失敗項目，並在寫入前重新執行 `--dry-run`。


## 寫入安全性

`openclaw config set` 和其他 OpenClaw 擁有的設定寫入器，會在提交到磁碟前驗證完整的變更後設定。如果新的 payload 未通過結構描述驗證，或看起來像破壞性覆寫，作用中的設定會保持不變，而被拒絕的 payload 會以 `openclaw.json.rejected.*` 儲存在旁邊。

小幅編輯建議使用 CLI 寫入：

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

如果寫入遭拒，請檢查儲存的 payload 並修正完整設定形狀：

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

仍允許直接用編輯器寫入，但執行中的 Gateway 在驗證通過前會將其視為不受信任。無效的直接編輯會導致啟動失敗，或被熱重載略過；Gateway 不會重寫 `openclaw.json`。執行 `openclaw doctor --fix` 來修復加上前綴/遭覆寫的設定，或還原最後已知良好的副本。請參閱 [Gateway 疑難排解](</zh-TW/gateway/troubleshooting#gateway-rejected-invalid-config>)。

整檔復原僅保留給 doctor 修復使用。Plugin 結構描述變更或 `minHostVersion` 偏差會保持明確報錯，而不是回復不相關的使用者設定，例如 models、providers、auth profiles、channels、gateway exposure、tools、memory、browser 或 cron config。

## 子命令

  * `config file`: 列印作用中的設定檔路徑（由 `OPENCLAW_CONFIG_PATH` 或預設位置解析）。該路徑應指向一般檔案，而不是符號連結。


編輯後請重新啟動 Gateway。

## 驗證

在不啟動 Gateway 的情況下，依作用中結構描述驗證目前設定。

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

當 `openclaw config validate` 已通過後，你可以使用本機 TUI，讓內嵌代理程式在同一個終端機中協助你驗證每項變更時，比對作用中設定與文件：

bashCopy code
[code]
    openclaw chat
[/code]

然後在 TUI 內：

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

典型修復流程：

* ### 與文件比對

請代理程式比對你目前的設定與相關文件頁面，並建議最小修正。

* ### 套用目標式編輯

使用 `openclaw config set` 或 `openclaw configure` 套用目標式編輯。

* ### 重新驗證

每次變更後重新執行 `openclaw config validate`。

* ### 針對執行階段問題執行 Doctor

如果驗證通過但執行階段仍不健康，請執行 `openclaw doctor` 或 `openclaw doctor --fix` 取得遷移與修復協助。

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [設定](</zh-TW/gateway/configuration>)


Was this useful?YesNo