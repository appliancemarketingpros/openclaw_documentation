---
title: WeChat
source_url: https://docs.openclaw.ai/zh-TW/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw 透過腾讯的外部 `@tencent-weixin/openclaw-weixin` 通道 Plugin 連接 WeChat。

狀態：外部 Plugin。支援直接聊天和媒體。目前的 Plugin 能力中繼資料未宣告支援群組聊天。

## 命名

  * **WeChat** 是這些文件中的使用者介面名稱。
  * **Weixin** 是腾讯套件與 Plugin ID 使用的名稱。
  * `openclaw-weixin` 是 OpenClaw 通道 ID。
  * `@tencent-weixin/openclaw-weixin` 是 npm 套件。


在 CLI 命令和設定路徑中使用 `openclaw-weixin`。

## 運作方式

WeChat 程式碼不在 OpenClaw 核心 repo 中。OpenClaw 提供通用通道 Plugin 合約，而外部 Plugin 提供 WeChat 專屬執行階段：

  1. `openclaw plugins install` 會安裝 `@tencent-weixin/openclaw-weixin`。
  2. Gateway 會探索 Plugin manifest 並載入 Plugin 進入點。
  3. Plugin 會註冊通道 ID `openclaw-weixin`。
  4. `openclaw channels login --channel openclaw-weixin` 會啟動 QR 登入。
  5. Plugin 會將帳號憑證儲存在 OpenClaw 狀態目錄下。
  6. Gateway 啟動時，Plugin 會為每個已設定的帳號啟動其 Weixin 監控器。
  7. 傳入的 WeChat 訊息會透過通道合約正規化、路由至選取的 OpenClaw agent，並透過 Plugin 傳出路徑送回。


這種分離很重要：OpenClaw 核心應保持與通道無關。WeChat 登入、腾讯 iLink API 呼叫、媒體上傳/下載、內容脈絡 token，以及帳號監控都由外部 Plugin 擁有。

## 安裝

快速安裝：

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

手動安裝：

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

安裝後重新啟動 Gateway：

bashCopy code
[code]
    openclaw gateway restart
[/code]

## 登入

在執行 Gateway 的同一台機器上執行 QR 登入：

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

用手機上的 WeChat 掃描 QR code，並確認登入。成功掃描後，Plugin 會在本機儲存帳號 token。

若要新增另一個 WeChat 帳號，請再次執行相同的登入命令。若有多個帳號，請依帳號、通道和傳送者隔離直接訊息工作階段：

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## 存取控制

直接訊息會使用通道 Plugin 的一般 OpenClaw 配對和 allowlist 模型。

核准新的傳送者：

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

完整的存取控制模型請參閱[配對](</zh-TW/channels/pairing>)。

## 相容性

Plugin 會在啟動時檢查主機 OpenClaw 版本。

Plugin 系列 | OpenClaw 版本 | npm tag  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
如果 Plugin 回報你的 OpenClaw 版本太舊，請更新 OpenClaw，或安裝舊版 Plugin 系列：

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Sidecar 處理程序

WeChat Plugin 可以在 Gateway 旁執行輔助工作，同時監控腾讯 iLink API。在 issue #68451 中，該輔助路徑暴露了 OpenClaw 通用過期 Gateway 清理中的一個錯誤：子處理程序可能會嘗試清理父 Gateway 處理程序，導致在 systemd 等處理程序管理器下出現重新啟動迴圈。

目前的 OpenClaw 啟動清理會排除目前處理程序及其祖先，因此通道輔助程式不得終止啟動它的 Gateway。這項修正是通用的；它不是核心中的 WeChat 專屬路徑。

## 疑難排解

檢查安裝與狀態：

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

如果通道顯示已安裝但未連線，請確認 Plugin 已啟用並重新啟動：

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

如果啟用 WeChat 後 Gateway 反覆重新啟動，請同時更新 OpenClaw 和 Plugin：

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

如果啟動時回報已安裝的 Plugin 套件 `requires compiled runtime output for TypeScript entry`，表示 npm 套件在發佈時缺少 OpenClaw 所需的已編譯 JavaScript 執行階段檔案。請在 Plugin 發佈者推出修正套件後更新/重新安裝，或暫時停用/解除安裝該 Plugin。

暫時停用：

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## 相關文件

  * 通道概覽：[聊天通道](</zh-TW/channels>)
  * 配對：[配對](</zh-TW/channels/pairing>)
  * 通道路由：[通道路由](</zh-TW/channels/channel-routing>)
  * Plugin 架構：[Plugin 架構](</zh-TW/plugins/architecture>)
  * 通道 Plugin SDK：[通道 Plugin SDK](</zh-TW/plugins/sdk-channel-plugins>)
  * 外部套件：[@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo