---
title: 沙盒化
source_url: https://docs.openclaw.ai/zh-TW/gateway/sandboxing
scraped_at: 2026-05-25
---

OpenClaw 可以在**沙箱後端內執行工具** ，以降低影響範圍。這是**選用** 功能，並由設定控制（`agents.defaults.sandbox` 或 `agents.list[].sandbox`）。如果關閉沙箱化，工具會在主機上執行。Gateway 會留在主機上；啟用時，工具執行會在隔離的沙箱中執行。

## 會被沙箱化的內容

  * 工具執行（`exec`、`read`、`write`、`edit`、`apply_patch`、`process` 等）。
  * 選用的沙箱化瀏覽器（`agents.defaults.sandbox.browser`）。


Sandboxed browser details

  * 預設情況下，當瀏覽器工具需要時，沙箱瀏覽器會自動啟動（確保 CDP 可連線）。可透過 `agents.defaults.sandbox.browser.autoStart` 和 `agents.defaults.sandbox.browser.autoStartTimeoutMs` 設定。
  * 預設情況下，沙箱瀏覽器容器會使用專用的 Docker 網路（`openclaw-sandbox-browser`），而不是全域 `bridge` 網路。可透過 `agents.defaults.sandbox.browser.network` 設定。
  * 選用的 `agents.defaults.sandbox.browser.cdpSourceRange` 會使用 CIDR 允許清單限制容器邊界的 CDP 入口（例如 `172.21.0.1/32`）。
  * noVNC 觀察者存取預設受密碼保護；OpenClaw 會發出短效權杖 URL，用來提供本機啟動頁面，並在 URL 片段中帶入密碼開啟 noVNC（不會進入查詢字串或標頭記錄）。
  * `agents.defaults.sandbox.browser.allowHostControl` 允許沙箱化工作階段明確指定主機瀏覽器。
  * 選用的允許清單會管控 `target: "custom"`：`allowedControlUrls`、`allowedControlHosts`、`allowedControlPorts`。


不會被沙箱化：

  * Gateway 程序本身。
  * 任何明確允許在沙箱外執行的工具（例如 `tools.elevated`）。 
    * **提權 exec 會繞過沙箱化，並使用已設定的逃逸路徑（預設為`gateway`，或當 exec 目標為 `node` 時使用 `node`）。**
    * 如果沙箱化已關閉，`tools.elevated` 不會改變執行方式（已經在主機上）。請參閱[提權模式](</zh-TW/tools/elevated>)。


## 模式

`agents.defaults.sandbox.mode` 控制**何時** 使用沙箱化：

### off

無沙箱化。

### non-main

只沙箱化**非 main** 工作階段（如果你希望一般聊天在主機上執行，這是預設值）。

`"non-main"` 是以 `session.mainKey`（預設為 `"main"`）為準，而不是 agent id。群組/頻道工作階段會使用自己的 key，因此會被視為非 main 並被沙箱化。

### all

每個工作階段都在沙箱中執行。

## 範圍

`agents.defaults.sandbox.scope` 控制**會建立多少容器** ：

  * `"agent"`（預設）：每個 agent 一個容器。
  * `"session"`：每個工作階段一個容器。
  * `"shared"`：所有沙箱化工作階段共用一個容器。


## 後端

`agents.defaults.sandbox.backend` 控制**由哪個執行階段** 提供沙箱：

  * `"docker"`（啟用沙箱化時的預設值）：由本機 Docker 支援的沙箱執行階段。
  * `"ssh"`：通用的 SSH 支援遠端沙箱執行階段。
  * `"openshell"`：OpenShell 支援的沙箱執行階段。


SSH 專屬設定位於 `agents.defaults.sandbox.ssh` 之下。OpenShell 專屬設定位於 `plugins.entries.openshell.config` 之下。

### 選擇後端

| Docker | SSH | OpenShell  
---|---|---|---  
**執行位置** | 本機容器 | 任何可透過 SSH 存取的主機 | OpenShell 管理的沙箱  
**設定** | `scripts/sandbox-setup.sh` | SSH key + 目標主機 | 已啟用 OpenShell Plugin  
**工作區模型** | 繫結掛載或複製 | 遠端為準（播種一次） | `mirror` 或 `remote`  
**網路控制** | `docker.network`（預設：無） | 取決於遠端主機 | 取決於 OpenShell  
**瀏覽器沙箱** | 支援 | 不支援 | 尚不支援  
**繫結掛載** | `docker.binds` | N/A | N/A  
**最適合** | 本機開發、完整隔離 | 卸載到遠端機器 | 具選用雙向同步的受管遠端沙箱  
  
### Docker 後端

沙箱化預設關閉。如果你啟用沙箱化且未選擇後端，OpenClaw 會使用 Docker 後端。它會透過 Docker daemon socket（`/var/run/docker.sock`）在本機執行工具與沙箱瀏覽器。沙箱容器隔離由 Docker namespace 決定。

若要將主機 GPU 暴露給 Docker 沙箱，請設定 `agents.defaults.sandbox.docker.gpus`，或每個 agent 的覆寫值 `agents.list[].sandbox.docker.gpus`。該值會作為獨立引數傳遞給 Docker 的 `--gpus` 旗標，例如 `"all"` 或 `"device=GPU-uuid"`，並且需要相容的主機執行階段，例如 NVIDIA Container Toolkit。

### SSH 後端

當你希望 OpenClaw 在任意可透過 SSH 存取的機器上沙箱化 `exec`、檔案工具與媒體讀取時，請使用 `backend: "ssh"`。

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "ssh",        scope: "session",        workspaceAccess: "rw",        ssh: {          target: "user@gateway-host:22",          workspaceRoot: "/tmp/openclaw-sandboxes",          strictHostKeyChecking: true,          updateHostKeys: true,          identityFile: "~/.ssh/id_ed25519",          certificateFile: "~/.ssh/id_ed25519-cert.pub",          knownHostsFile: "~/.ssh/known_hosts",          // Or use SecretRefs / inline contents instead of local files:          // identityData: { source: "env", provider: "default", id: "SSH_IDENTITY" },          // certificateData: { source: "env", provider: "default", id: "SSH_CERTIFICATE" },          // knownHostsData: { source: "env", provider: "default", id: "SSH_KNOWN_HOSTS" },        },      },    },  },}
[/code]

How it works

  * OpenClaw 會在 `sandbox.ssh.workspaceRoot` 之下建立每個 scope 對應的遠端 root。
  * 建立或重新建立後首次使用時，OpenClaw 會從本機工作區將該遠端工作區播種一次。
  * 之後，`exec`、`read`、`write`、`edit`、`apply_patch`、提示媒體讀取，以及傳入媒體暫存，都會透過 SSH 直接對遠端工作區執行。
  * OpenClaw 不會自動將遠端變更同步回本機工作區。

Authentication material

  * `identityFile`、`certificateFile`、`knownHostsFile`：使用既有本機檔案，並透過 OpenSSH 設定傳遞。
  * `identityData`、`certificateData`、`knownHostsData`：使用內嵌字串或 SecretRefs。OpenClaw 會透過一般 secrets 執行階段快照解析它們，將它們寫入權限為 `0600` 的暫存檔，並在 SSH 工作階段結束時刪除。
  * 如果同一項目同時設定了 `*File` 和 `*Data`，該 SSH 工作階段會以 `*Data` 優先。

Remote-canonical consequences

這是**遠端為準** 模型。初始播種後，遠端 SSH 工作區會成為真正的沙箱狀態。

  * 播種步驟後在 OpenClaw 外部進行的主機本機編輯，不會在遠端可見，除非你重新建立沙箱。
  * `openclaw sandbox recreate` 會刪除每個 scope 對應的遠端 root，並在下次使用時再次從本機播種。
  * SSH 後端不支援瀏覽器沙箱化。
  * `sandbox.docker.*` 設定不適用於 SSH 後端。


### OpenShell 後端

當你希望 OpenClaw 在 OpenShell 管理的遠端環境中沙箱化工具時，請使用 `backend: "openshell"`。完整設定指南、設定參考與工作區模式比較，請參閱專屬的 [OpenShell 頁面](</zh-TW/gateway/openshell>)。

OpenShell 會重用與通用 SSH 後端相同的核心 SSH 傳輸與遠端檔案系統 bridge，並加入 OpenShell 專屬生命週期（`sandbox create/get/delete`、`sandbox ssh-config`）以及選用的 `mirror` 工作區模式。

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "session",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote", // mirror | remote          remoteWorkspaceDir: "/sandbox",          remoteAgentWorkspaceDir: "/agent",        },      },    },  },}
[/code]

OpenShell 模式：

  * `mirror`（預設）：本機工作區保持為準。OpenClaw 會在 exec 之前將本機檔案同步到 OpenShell，並在 exec 之後將遠端工作區同步回來。
  * `remote`：沙箱建立後，OpenShell 工作區即為準。OpenClaw 會從本機工作區將遠端工作區播種一次，之後檔案工具與 exec 會直接對遠端沙箱執行，不會同步變更回來。


Remote transport details

  * OpenClaw 會透過 `openshell sandbox ssh-config <name>` 向 OpenShell 要求沙箱專屬 SSH 設定。
  * Core 會將該 SSH 設定寫入暫存檔、開啟 SSH 工作階段，並重用 `backend: "ssh"` 所使用的相同遠端檔案系統 bridge。
  * 在 `mirror` 模式中，只有生命週期不同：exec 之前從本機同步到遠端，然後在 exec 之後同步回來。

Current OpenShell limitations

  * 尚不支援沙箱瀏覽器
  * OpenShell 後端不支援 `sandbox.docker.binds`
  * `sandbox.docker.*` 之下的 Docker 專屬執行階段旋鈕仍只適用於 Docker 後端


#### 工作區模式

OpenShell 有兩種工作區模型。這是在實務上最重要的部分。

### mirror (local canonical)

當你希望**本機工作區保持為準** 時，使用 `plugins.entries.openshell.config.mode: "mirror"`。

行為：

  * 在 `exec` 之前，OpenClaw 會將本機工作區同步到 OpenShell 沙盒。
  * 在 `exec` 之後，OpenClaw 會將遠端工作區同步回本機工作區。
  * 檔案工具仍會透過沙盒橋接運作，但在各回合之間，本機工作區仍是事實來源。


適用情境：

  * 你在 OpenClaw 外部於本機編輯檔案，並希望這些變更自動出現在沙盒中
  * 你希望 OpenShell 沙盒盡可能像 Docker 後端一樣運作
  * 你希望主機工作區在每個 exec 回合後反映沙盒寫入


取捨：exec 前後會產生額外同步成本。

### remote (OpenShell canonical)

當你希望 **OpenShell 工作區成為權威來源** 時，請使用 `plugins.entries.openshell.config.mode: "remote"`。

行為：

  * 第一次建立沙盒時，OpenClaw 會從本機工作區初始化一次遠端工作區。
  * 之後，`exec`、`read`、`write`、`edit` 和 `apply_patch` 會直接對遠端 OpenShell 工作區運作。
  * OpenClaw 不會在 exec 後將遠端變更同步回本機工作區。
  * 提示期間的媒體讀取仍可運作，因為檔案與媒體工具會透過沙盒橋接讀取，而不是假設有本機主機路徑。
  * 傳輸方式是 SSH 進入由 `openshell sandbox ssh-config` 傳回的 OpenShell 沙盒。


重要影響：

  * 如果你在初始化步驟後於 OpenClaw 外部編輯主機上的檔案，遠端沙盒**不會** 自動看到這些變更。
  * 如果重新建立沙盒，遠端工作區會再次從本機工作區初始化。
  * 使用 `scope: "agent"` 或 `scope: "shared"` 時，該遠端工作區會在相同作用域中共享。


適用情境：

  * 沙盒應主要存在於遠端 OpenShell 端
  * 你想降低每回合的同步負擔
  * 你不希望主機本機編輯靜默覆寫遠端沙盒狀態


如果你把沙盒視為暫時的執行環境，請選擇 `mirror`。如果你把沙盒視為真正的工作區，請選擇 `remote`。

#### OpenShell 生命週期

OpenShell 沙盒仍透過一般沙盒生命週期管理：

  * `openclaw sandbox list` 會顯示 OpenShell runtime 以及 Docker runtime
  * `openclaw sandbox recreate` 會刪除目前的 runtime，並讓 OpenClaw 在下次使用時重新建立它
  * 清理邏輯也會感知後端


對 `remote` 模式而言，重新建立尤其重要：

  * 重新建立會刪除該作用域的權威遠端工作區
  * 下次使用時會從本機工作區初始化新的遠端工作區


對 `mirror` 模式而言，重新建立主要是重設遠端執行環境，因為本機工作區無論如何仍是權威來源。

## 工作區存取

`agents.defaults.sandbox.workspaceAccess` 控制**沙盒可以看到什麼** ：

### none (default)

工具會看到位於 `~/.openclaw/sandboxes` 下的沙盒工作區。

### ro

將代理工作區以唯讀方式掛載到 `/agent`（停用 `write`/`edit`/`apply_patch`）。

### rw

將代理工作區以讀寫方式掛載到 `/workspace`。

使用 OpenShell 後端時：

  * `mirror` 模式在 exec 回合之間仍使用本機工作區作為權威來源
  * `remote` 模式在初始初始化後使用遠端 OpenShell 工作區作為權威來源
  * `workspaceAccess: "ro"` 和 `"none"` 仍會以相同方式限制寫入行為


傳入媒體會複製到作用中的沙盒工作區（`media/inbound/*`）。

## 自訂繫結掛載

`agents.defaults.sandbox.docker.binds` 會將其他主機目錄掛載到容器中。格式：`host:container:mode`（例如 `"/home/user/source:/source:rw"`）。

全域與每代理的繫結會被**合併** （不是取代）。在 `scope: "shared"` 下，會忽略每代理的繫結。

`agents.defaults.sandbox.browser.binds` 只會將其他主機目錄掛載到**沙盒瀏覽器** 容器。

  * 設定時（包括 `[]`），它會取代瀏覽器容器的 `agents.defaults.sandbox.docker.binds`。
  * 省略時，瀏覽器容器會退回使用 `agents.defaults.sandbox.docker.binds`（向後相容）。


範例（唯讀來源 + 額外資料目錄）：

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"],        },      },    },    list: [      {        id: "build",        sandbox: {          docker: {            binds: ["/mnt/cache:/cache:rw"],          },        },      },    ],  },}
[/code]

## 映像與設定

預設 Docker 映像：`openclaw-sandbox:bookworm-slim`

* ### Build the default image

從來源 checkout：

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

從 npm 安裝（不需要來源 checkout）：

bashCopy code
[code]
    docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'FROM debian:bookworm-slimENV DEBIAN_FRONTEND=noninteractiveRUN apt-get update && apt-get install -y --no-install-recommends \  bash ca-certificates curl git jq python3 ripgrep \  && rm -rf /var/lib/apt/lists/*RUN useradd --create-home --shell /bin/bash sandboxUSER sandboxWORKDIR /home/sandboxCMD ["sleep", "infinity"]DOCKERFILE
[/code]

預設映像**不** 包含 Node。如果某個 skill 需要 Node（或其他 runtime），請烘焙自訂映像，或透過 `sandbox.docker.setupCommand` 安裝（需要網路輸出 + 可寫入 root + root 使用者）。

當缺少 `openclaw-sandbox:bookworm-slim` 時，OpenClaw 不會靜默改用一般的 `debian:bookworm-slim`。以預設映像為目標的沙盒執行會快速失敗並顯示建置指示，直到你建置它為止，因為內建映像帶有 `python3`，供沙盒寫入/編輯輔助程式使用。

* ### Optional: build the common image

若要使用具備常用工具（例如 `curl`、`jq`、`nodejs`、`python3`、`git`）的功能更完整沙盒映像：

從來源 checkout：

bashCopy code
[code]
    scripts/sandbox-common-setup.sh
[/code]

從 npm 安裝時，先建置預設映像（見上方），然後使用儲存庫中的 [`scripts/docker/sandbox/Dockerfile.common`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.common>) 在其上建置 common 映像。

接著將 `agents.defaults.sandbox.docker.image` 設為 `openclaw-sandbox-common:bookworm-slim`。

* ### Optional: build the sandbox browser image

從來源 checkout：

bashCopy code
[code]
    scripts/sandbox-browser-setup.sh
[/code]

從 npm 安裝時，使用儲存庫中的 [`scripts/docker/sandbox/Dockerfile.browser`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.browser>) 建置。

預設情況下，Docker 沙盒容器執行時**沒有網路** 。可用 `agents.defaults.sandbox.docker.network` 覆寫。

Sandbox browser Chromium defaults

內建沙盒瀏覽器映像也會為容器化工作負載套用保守的 Chromium 啟動預設值。目前容器預設值包含：

  * `--remote-debugging-address=127.0.0.1`
  * `--remote-debugging-port=<derived from OPENCLAW_BROWSER_CDP_PORT>`
  * `--user-data-dir=${HOME}/.chrome`
  * `--no-first-run`
  * `--no-default-browser-check`
  * `--disable-3d-apis`
  * `--disable-gpu`
  * `--disable-dev-shm-usage`
  * `--disable-background-networking`
  * `--disable-extensions`
  * `--disable-features=TranslateUI`
  * `--disable-breakpad`
  * `--disable-crash-reporter`
  * `--disable-software-rasterizer`
  * `--no-zygote`
  * `--metrics-recording-only`
  * `--renderer-process-limit=2`
  * 啟用 `noSandbox` 時使用 `--no-sandbox`。
  * 三個圖形強化旗標（`--disable-3d-apis`、`--disable-software-rasterizer`、`--disable-gpu`）是選用項目，且在容器缺少 GPU 支援時很有用。如果你的工作負載需要 WebGL 或其他 3D/瀏覽器功能，請設定 `OPENCLAW_BROWSER_DISABLE_GRAPHICS_FLAGS=0`。
  * `--disable-extensions` 預設啟用；對依賴擴充功能的流程，可用 `OPENCLAW_BROWSER_DISABLE_EXTENSIONS=0` 停用。
  * `--renderer-process-limit=2` 由 `OPENCLAW_BROWSER_RENDERER_PROCESS_LIMIT=&lt;N&gt;` 控制，其中 `0` 會保留 Chromium 的預設值。


如果你需要不同的 runtime 設定檔，請使用自訂瀏覽器映像並提供自己的進入點。對於本機（非容器）Chromium 設定檔，請使用 `browser.extraArgs` 附加其他啟動旗標。

Network security defaults

  * `network: "host"` 會被封鎖。
  * `network: "container:<id>"` 預設會被封鎖（命名空間加入繞過風險）。
  * 緊急例外覆寫：`agents.defaults.sandbox.docker.dangerouslyAllowContainerNamespaceJoin: true`。


Docker 安裝與容器化 Gateway 位於此處：[Docker](</zh-TW/install/docker>)

對於 Docker Gateway 部署，`scripts/docker/setup.sh` 可以啟動沙盒設定。設定 `OPENCLAW_SANDBOX=1`（或 `true`/`yes`/`on`）即可啟用該路徑。你可以用 `OPENCLAW_DOCKER_SOCKET` 覆寫 socket 位置。完整設定與環境參考：[Docker](</zh-TW/install/docker#agent-sandbox>)。

## setupCommand（一次性容器設定）

`setupCommand` 會在沙盒容器建立後**執行一次** （不是每次執行都執行）。它會透過 `sh -lc` 在容器內執行。

路徑：

  * 全域：`agents.defaults.sandbox.docker.setupCommand`
  * 每代理：`agents.list[].sandbox.docker.setupCommand`


常見陷阱

  * 預設 `docker.network` 是 `"none"`（沒有對外連線），因此套件安裝會失敗。
  * `docker.network: "container:<id>"` 需要 `dangerouslyAllowContainerNamespaceJoin: true`，且僅供緊急破例使用。
  * `readOnlyRoot: true` 會阻止寫入；請設定 `readOnlyRoot: false` 或建置自訂映像檔。
  * `user` 必須是 root 才能安裝套件（省略 `user` 或設定 `user: "0:0"`）。
  * Sandbox exec **不會** 繼承主機的 `process.env`。請使用 `agents.defaults.sandbox.docker.env`（或自訂映像檔）設定 skill API keys。


## 工具政策與逃生出口

工具允許/拒絕政策仍會先於 sandbox 規則套用。如果工具已在全域或個別 agent 被拒絕，sandboxing 不會把它恢復。

`tools.elevated` 是明確的逃生出口，會在 sandbox 外執行 `exec`（預設為 `gateway`，或當 exec 目標為 `node` 時使用 `node`）。`/exec` 指令只適用於已授權的傳送者，並會在每個 session 中持續生效；若要強制停用 `exec`，請使用工具政策拒絕（請參閱 [Sandbox vs Tool Policy vs Elevated](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>)）。

偵錯：

  * 使用 `openclaw sandbox explain` 檢查有效的 sandbox 模式、工具政策，以及修正用的設定鍵。
  * 請參閱 [Sandbox vs Tool Policy vs Elevated](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>)，了解「為什麼這被封鎖？」的思考模型。


保持鎖定。

## 多 agent 覆寫

每個 agent 都可以覆寫 sandbox + tools：`agents.list[].sandbox` 和 `agents.list[].tools`（以及用於 sandbox 工具政策的 `agents.list[].tools.sandbox.tools`）。請參閱 [Multi-Agent Sandbox & Tools](</zh-TW/tools/multi-agent-sandbox-tools>) 了解優先順序。

## 最小啟用範例

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        scope: "session",        workspaceAccess: "none",      },    },  },}
[/code]

## 相關

  * [Multi-Agent Sandbox & Tools](</zh-TW/tools/multi-agent-sandbox-tools>) — 個別 agent 覆寫與優先順序
  * [OpenShell](</zh-TW/gateway/openshell>) — 受管理的 sandbox 後端設定、workspace 模式與設定參考
  * [Sandbox configuration](</zh-TW/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox vs Tool Policy vs Elevated](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>) — 偵錯「為什麼這被封鎖？」
  * [Security](</zh-TW/gateway/security>)


Was this useful?YesNo