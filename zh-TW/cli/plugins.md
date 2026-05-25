---
title: Plugin
source_url: https://docs.openclaw.ai/zh-TW/cli/plugins
scraped_at: 2026-05-25
---

管理 Gateway Plugin、hook 套件與相容套件組合。

[**Plugin 系統** 安裝、啟用與疑難排解 Plugin 的終端使用者指南。 ](</zh-TW/tools/plugin>) [**管理 Plugin** 安裝、列出、更新、解除安裝與發布的快速範例。 ](</zh-TW/plugins/manage-plugins>) [**Plugin 套件組合** 套件組合相容性模型。 ](</zh-TW/plugins/bundles>) [**Plugin manifest** Manifest 欄位與設定結構描述。 ](</zh-TW/plugins/manifest>) [**安全性** Plugin 安裝的安全性強化。 ](</zh-TW/gateway/security>)

## 命令

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

若要調查緩慢的安裝、檢查、解除安裝或 registry 重新整理，請搭配 `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1` 執行命令。追蹤會將階段計時寫入 stderr，並保持 JSON 輸出可解析。請參閱[偵錯](</zh-TW/help/debugging#plugin-lifecycle-trace>)。

### 安裝

bashCopy code
[code]
    openclaw plugins search "calendar"                   # 搜尋 ClawHub Pluginopenclaw plugins install <package>                      # 預設使用 npmopenclaw plugins install clawhub:<package>              # 僅 ClawHubopenclaw plugins install npm:<package>                  # 僅 npmopenclaw plugins install npm-pack:<path.tgz>            # 透過 npm install 語意安裝本機 npm packopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # 覆寫現有安裝openclaw plugins install <package> --pin                # 釘選版本openclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # 本機路徑openclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace（明確指定）openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

測試設定期間安裝的維護者，可以使用受保護的環境變數覆寫自動 Plugin 安裝來源。請參閱 [Plugin 安裝覆寫](</zh-TW/plugins/install-overrides>)。

`plugins search` 會查詢 ClawHub 中可安裝的 Plugin 套件，並列印可直接安裝的套件名稱。它會搜尋 code-plugin 與 bundle-plugin 套件，而不是 Skills。若要搜尋 ClawHub skills，請使用 `openclaw skills search`。

設定 include 與無效設定修復

如果你的 `plugins` 區段由單一檔案 `$include` 支援，`plugins install/update/enable/disable/uninstall` 會寫入該 include 檔案，並保持 `openclaw.json` 不變。Root include、include 陣列，以及帶有同層覆寫的 include 會失敗關閉，而不是攤平成一般設定。支援的形狀請參閱[設定 include](</zh-TW/gateway/configuration>)。

如果安裝期間設定無效，`plugins install` 通常會失敗關閉，並告知你先執行 `openclaw doctor --fix`。在 Gateway 啟動與 hot reload 期間，無效的 Plugin 設定會像其他無效設定一樣失敗關閉；`openclaw doctor --fix` 可以隔離無效的 Plugin 項目。唯一記載的安裝期間例外，是一條狹窄的內建 Plugin 復原路徑，僅適用於明確選擇加入 `openclaw.install.allowInvalidConfigRecovery` 的 Plugin。

\--force 與重新安裝相較於更新

`--force` 會重用現有安裝目標，並就地覆寫已安裝的 Plugin 或 hook 套件。當你有意從新的本機路徑、封存檔、ClawHub 套件或 npm artifact 重新安裝相同 id 時使用它。若是已追蹤 npm Plugin 的例行升級，建議使用 `openclaw plugins update <id-or-npm-spec>`。

如果你對已安裝的 Plugin id 執行 `plugins install`，OpenClaw 會停止，並指向 `plugins update <id-or-npm-spec>` 進行一般升級，或在你真的想從不同來源覆寫目前安裝時，指向 `plugins install <package> --force`。

\--pin 範圍

`--pin` 僅適用於 npm 安裝。它不支援 `git:` 安裝；當你想要釘選來源時，請使用明確的 git ref，例如 `git:github.com/acme/plugin@v1.2.3`。它不支援 `--marketplace`，因為 marketplace 安裝會保留 marketplace 來源中繼資料，而不是 npm spec。

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` 是內建危險程式碼掃描器誤判時的破例選項。即使內建掃描器回報 `critical` 發現，它也允許安裝繼續，但它**不會** 略過 Plugin `before_install` hook 政策封鎖，也**不會** 略過掃描失敗。

此 CLI 旗標適用於 Plugin 安裝/更新流程。Gateway 支援的 skill 相依項安裝會使用對應的 `dangerouslyForceUnsafeInstall` 請求覆寫，而 `openclaw skills install` 仍是獨立的 ClawHub skill 下載/安裝流程。

如果你發布到 ClawHub 的 Plugin 被 registry 掃描封鎖，請使用 [ClawHub](</zh-TW/clawhub/security>) 中的發布者步驟。

Hook 套件與 npm specs

`plugins install` 也是安裝在 `package.json` 中公開 `openclaw.hooks` 的 hook 套件的介面。請使用 `openclaw hooks` 取得經篩選的 hook 可見性與逐 hook 啟用，而不是用來安裝套件。

Npm specs **僅限 registry** （套件名稱 + 選用的**精確版本** 或 **dist-tag** ）。Git/URL/file specs 與 semver 範圍會被拒絕。為了安全，即使你的 shell 有全域 npm install 設定，相依項安裝也會以專案本機方式搭配 `--ignore-scripts` 執行。受管理的 Plugin npm root 會繼承 OpenClaw 的套件層級 npm `overrides`，因此主機安全性釘選也會套用到 hoisted Plugin 相依項。

當你想明確指定 npm 解析時，請使用 `npm:<package>`。在 launch cutover 期間，裸套件 spec 也會直接從 npm 安裝。

裸 specs 與 `@latest` 會留在穩定軌。OpenClaw 日期戳記修正版，例如 `2026.5.3-1`，在此檢查中屬於穩定版本。如果 npm 將其中任一者解析為預發行版本，OpenClaw 會停止並要求你使用預發行標籤（例如 `@beta`/`@rc`）或精確的預發行版本（例如 `@1.2.3-beta.4`）明確選擇加入。

如果裸安裝 spec 符合官方 Plugin id（例如 `diffs`），OpenClaw 會直接安裝目錄項目。若要安裝同名 npm 套件，請使用明確的 scoped spec（例如 `@scope/diffs`）。

Git 儲存庫

使用 `git:<repo>` 直接從 git 儲存庫安裝。支援形式包含 `git:github.com/owner/repo`、`git:owner/repo`、完整 `https://`、`ssh://`、`git://`、`file://`，以及 `git@host:owner/repo.git` clone URL。加入 `@<ref>` 或 `#<ref>` 可在安裝前 checkout 分支、標籤或 commit。

Git 安裝會 clone 到暫存目錄，在有提供時 checkout 要求的 ref，然後使用一般 Plugin 目錄安裝器。這表示 manifest 驗證、危險程式碼掃描、套件管理器安裝工作，以及安裝記錄都會像 npm 安裝一樣運作。記錄的 git 安裝包含來源 URL/ref 與解析出的 commit，因此 `openclaw plugins update` 之後可以重新解析該來源。

從 git 安裝後，請使用 `openclaw plugins inspect <id> --runtime --json` 驗證執行階段註冊，例如 gateway methods 與 CLI 命令。如果 Plugin 使用 `api.registerCli` 註冊 CLI root，請透過 OpenClaw root CLI 直接執行該命令，例如 `openclaw demo-plugin ping`。

封存檔

支援的封存檔：`.zip`、`.tgz`、`.tar.gz`、`.tar`。原生 OpenClaw Plugin 封存檔必須在解壓後的 Plugin root 包含有效的 `openclaw.plugin.json`；只包含 `package.json` 的封存檔會在 OpenClaw 寫入安裝記錄前被拒絕。

當檔案是 npm-pack tarball，且你想測試 registry 安裝所使用的同一條受管理 npm-root 安裝路徑時，請使用 `npm-pack:<path.tgz>`，包含 `package-lock.json` 驗證、hoisted 相依項掃描，以及 npm 安裝記錄。一般封存檔路徑仍會作為本機封存檔安裝到 Plugin extensions root 底下。

也支援 Claude marketplace 安裝。

ClawHub 安裝會使用明確的 `clawhub:<package>` locator：

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

在 launch cutover 期間，裸 npm-safe Plugin specs 預設會從 npm 安裝：

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

使用 `npm:` 讓僅 npm 解析變得明確：

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw 會在安裝前檢查宣告的 Plugin API / 最低 Gateway 相容性。當選取的 ClawHub 版本發布 ClawPack 成品時，OpenClaw 會下載已版本化的 npm-pack `.tgz`，驗證 ClawHub 摘要標頭和成品摘要，然後透過一般封存路徑安裝。沒有 ClawPack 中繼資料的舊版 ClawHub 版本仍會透過舊式套件封存驗證路徑安裝。已記錄的安裝會保留其 ClawHub 來源中繼資料、成品種類、npm integrity、npm shasum、tarball 名稱，以及 ClawPack 摘要事實，以供之後更新使用。 未指定版本的 ClawHub 安裝會保留未指定版本的已記錄規格，讓 `openclaw plugins update` 可以跟隨較新的 ClawHub 發行；明確版本或標籤選擇器，例如 `clawhub:pkg@1.2.3` 和 `clawhub:pkg@beta`，會維持固定在該選擇器。

#### 市集簡寫

當市集名稱存在於 Claude 位於 `~/.claude/plugins/known_marketplaces.json` 的本機登錄快取時，使用 `plugin@marketplace` 簡寫：

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

當你想要明確傳遞市集來源時，使用 `--marketplace`：

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### 市集來源

  * 來自 `~/.claude/plugins/known_marketplaces.json` 的 Claude 已知市集名稱
  * 本機市集根目錄或 `marketplace.json` 路徑
  * GitHub repo 簡寫，例如 `owner/repo`
  * GitHub repo URL，例如 `https://github.com/owner/repo`
  * git URL


### 遠端市集規則

對於從 GitHub 或 git 載入的遠端市集，Plugin 項目必須留在複製下來的市集 repo 內。OpenClaw 會接受來自該 repo 的相對路徑來源，並拒絕遠端 manifest 中的 HTTP(S)、絕對路徑、git、GitHub，以及其他非路徑 Plugin 來源。

對於本機路徑和封存檔，OpenClaw 會自動偵測：

  * 原生 OpenClaw Plugin（`openclaw.plugin.json`）
  * Codex 相容套件組合（`.codex-plugin/plugin.json`）
  * Claude 相容套件組合（`.claude-plugin/plugin.json` 或預設的 Claude 元件版面配置）
  * Cursor 相容套件組合（`.cursor-plugin/plugin.json`）


### 列出

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

只顯示已啟用的 Plugin。

從表格檢視切換為每個 Plugin 的詳細行，包含 source/origin/version/activation 中繼資料。

機器可讀的清單，加上登錄診斷與套件相依項安裝狀態。

`plugins search` 是遠端 ClawHub catalog 查詢。它不會檢查本機 狀態、變更 config、安裝套件，或載入 Plugin runtime 程式碼。搜尋 結果會包含 ClawHub 套件名稱、family、channel、version、summary，以及 安裝提示，例如 `openclaw plugins install clawhub:<package>`。

若要在封裝好的 Docker 映像中處理內建 Plugin，請將 Plugin 來源目錄 bind-mount 到相符的封裝來源路徑上，例如 `/app/extensions/synology-chat`。OpenClaw 會先於 `/app/dist/extensions/synology-chat` 探索該掛載的來源 覆蓋；單純複製的來源 目錄會保持無作用，因此一般封裝安裝仍會使用已編譯的 dist。

對於 runtime hook 偵錯：

  * `openclaw plugins inspect <id> --runtime --json` 會顯示來自模組載入檢查流程的已註冊 hook 和診斷。Runtime 檢查絕不會安裝相依項；使用 `openclaw doctor --fix` 清理舊式相依項狀態，或復原 config 中引用的遺失可下載 Plugin。
  * `openclaw gateway status --deep --require-rpc` 會確認可連線的 Gateway、服務/程序提示、config 路徑，以及 RPC 健康狀態。
  * 非內建 conversation hook（`llm_input`、`llm_output`、`before_model_resolve`、`before_agent_reply`、`before_agent_run`、`before_agent_finalize`、`agent_end`）需要 `plugins.entries.<id>.hooks.allowConversationAccess=true`。


使用 `--link` 以避免複製本機目錄（會新增到 `plugins.load.paths`）：

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Plugin index

Plugin 安裝中繼資料是由機器管理的狀態，不是使用者 config。安裝和更新會將它寫入有效 OpenClaw state 目錄下的 `plugins/installs.json`。其頂層 `installRecords` map 是安裝中繼資料的持久來源，包含損壞或遺失 Plugin manifest 的記錄。`plugins` array 是由 manifest 衍生的冷登錄快取。此檔案包含請勿編輯警告，並供 `openclaw plugins update`、uninstall、診斷，以及冷 Plugin 登錄使用。

當 OpenClaw 在 config 中看到已隨附的舊式 `plugins.installs` 記錄時，runtime 讀取會將它們視為相容性輸入，而不會重寫 `openclaw.json`。明確的 Plugin 寫入和 `openclaw doctor --fix` 會在允許 config 寫入時，將這些記錄移入 Plugin index 並移除 config key；如果任一寫入失敗，config 記錄會被保留，避免安裝中繼資料遺失。

### 解除安裝

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` 會從 `plugins.entries`、持久化 Plugin index、Plugin allow/deny list 項目，以及適用時的已連結 `plugins.load.paths` 項目中移除 Plugin 記錄。除非設定了 `--keep-files`，uninstall 也會移除受追蹤的受管理安裝目錄，前提是該目錄位於 OpenClaw 的 Plugin extensions 根目錄內。對於 Active Memory Plugin，memory slot 會重設為 `memory-core`。

### 更新

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

更新會套用到受管理 Plugin index 中受追蹤的 Plugin 安裝，以及 `hooks.internal.installs` 中受追蹤的 hook-pack 安裝。

解析 Plugin id 與 npm spec

當你傳入 Plugin id 時，OpenClaw 會重用該 Plugin 的已記錄安裝規格。這表示先前儲存的 dist-tag（例如 `@beta`）和精確固定版本，會在之後的 `update <id>` 執行中繼續使用。

對於 npm 安裝，你也可以傳入帶有 dist-tag 或精確版本的明確 npm 套件規格。OpenClaw 會將該套件名稱解析回受追蹤的 Plugin 記錄，更新該已安裝的 Plugin，並記錄新的 npm 規格以供未來基於 id 的更新使用。

傳入不含版本或標籤的 npm 套件名稱，也會解析回受追蹤的 Plugin 記錄。當 Plugin 固定到精確版本，而你想把它移回登錄的預設發行線時，請使用這種方式。

Beta channel 更新

`openclaw plugins update` 會重用受追蹤的 Plugin 規格，除非你傳入新的規格。`openclaw update` 另外知道有效的 OpenClaw 更新 channel：在 beta channel 上，預設線的 npm 和 ClawHub Plugin 記錄會先嘗試 `@beta`，如果沒有 Plugin beta 發行，則退回已記錄的 default/latest 規格。該退回會以警告回報，且不會使 core 更新失敗。精確版本和明確標籤會維持固定在該選擇器。

版本檢查與完整性漂移

在即時 npm 更新前，OpenClaw 會對照 npm registry 中繼資料檢查已安裝的套件版本。如果已安裝版本和已記錄的成品身分已經符合解析出的目標，更新會略過，不會下載、重新安裝或重寫 `openclaw.json`。

當存在已儲存的 integrity hash 且擷取到的成品 hash 發生變化時，OpenClaw 會將其視為 npm 成品漂移。互動式 `openclaw plugins update` 命令會列印預期和實際 hash，並在繼續前要求確認。非互動式更新 helper 會預設關閉失敗，除非呼叫端提供明確的繼續政策。

更新時使用 --dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` 也可在 `plugins update` 上使用，作為 Plugin 更新期間內建危險程式碼掃描誤判的緊急覆寫。它仍不會略過 Plugin `before_install` 政策封鎖或掃描失敗封鎖，而且只適用於 Plugin 更新，不適用於 hook-pack 更新。

### 檢查

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect 會顯示身分、載入狀態、來源、manifest 能力、政策旗標、診斷、安裝中繼資料、套件組合能力，以及任何偵測到的 MCP 或 LSP server 支援，預設不匯入 Plugin runtime。加入 `--runtime` 以載入 Plugin 模組，並包含已註冊的 hook、tool、command、service、gateway method 和 HTTP route。Runtime 檢查會直接回報遺失的 Plugin 相依項；安裝和修復仍位於 `openclaw plugins install`、`openclaw plugins update` 和 `openclaw doctor --fix`。

Plugin 擁有的 CLI command 通常會安裝為根層級 `openclaw` command group，但 Plugin 也可能在 core parent 下註冊巢狀 command，例如 `openclaw nodes`。在 `inspect --runtime` 顯示 `cliCommands` 下的 command 後，請在列出的路徑執行它；例如，註冊 `demo-git` 的 Plugin 可以用 `openclaw demo-git ping` 驗證。

每個 Plugin 會依照它在 runtime 實際註冊的內容分類：

  * **plain-capability** — 一種能力類型（例如，僅提供提供者的 Plugin）
  * **hybrid-capability** — 多種能力類型（例如，文字 + 語音 + 圖片）
  * **hook-only** — 只有 hook，沒有能力或介面
  * **non-capability** — 工具/命令/服務，但沒有能力


請參閱 [Plugin 形態](</zh-TW/plugins/architecture#plugin-shapes>)，深入了解能力模型。

### 診斷

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` 會回報 Plugin 載入錯誤、manifest/探索診斷，以及相容性通知。當一切正常時，會印出 `No plugin issues detected.`

如果已設定的 Plugin 存在於磁碟上，但遭載入器的路徑安全檢查阻擋，設定驗證會保留該 Plugin 項目，並將其回報為 `present but blocked`。請修正前面的遭阻擋 Plugin 診斷，例如路徑擁有權或全域可寫權限，而不是移除 `plugins.entries.<id>` 或 `plugins.allow` 設定。

針對模組形態失敗，例如缺少 `register`/`activate` 匯出，請使用 `OPENCLAW_PLUGIN_LOAD_DEBUG=1` 重新執行，以在診斷輸出中包含精簡的匯出形態摘要。

### 登錄檔

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

本機 Plugin 登錄檔是 OpenClaw 為已安裝 Plugin 身分、啟用狀態、來源中繼資料，以及貢獻擁有權所持久化的冷讀模型。一般啟動、提供者擁有者查找、頻道設定分類，以及 Plugin 清查都可以讀取它，而不必匯入 Plugin runtime 模組。

使用 `plugins registry` 檢查持久化登錄檔是否存在、是否為目前版本或是否過期。使用 `--refresh` 從持久化的 Plugin 索引、設定政策，以及 manifest/package 中繼資料重建它。這是修復路徑，不是 runtime 啟用路徑。

`openclaw doctor --fix` 也會修復與登錄檔相鄰的受管理 npm 漂移：如果受管理 Plugin npm 根目錄下的孤立或復原 `@openclaw/*` package 遮蔽了內建 Plugin，doctor 會移除該過期 package 並重建登錄檔，讓啟動能依照內建 manifest 驗證。Doctor 也會將主機 `openclaw` package 重新連結到宣告 `peerDependencies.openclaw` 的受管理 npm Plugin 中，因此更新或 npm 修復後，package 本機 runtime 匯入（例如 `openclaw/plugin-sdk/*`）仍可解析。

### 市集

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

Marketplace list 接受本機 marketplace 路徑、`marketplace.json` 路徑、像 `owner/repo` 這樣的 GitHub 簡寫、GitHub repo URL，或 git URL。`--json` 會印出已解析的來源標籤，以及已剖析的 marketplace manifest 和 Plugin 項目。

## 相關內容

  * [建置 Plugin](</zh-TW/plugins/building-plugins>)
  * [CLI 參考](</zh-TW/cli>)
  * [ClawHub](</zh-TW/clawhub>)


Was this useful?YesNo