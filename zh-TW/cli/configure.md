---
title: 設定
source_url: https://docs.openclaw.ai/zh-TW/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

針對現有設定進行目標變更的互動式提示：認證資訊、裝置、代理預設值、Gateway、頻道、Plugin、Skills，以及健康檢查。

使用 `openclaw onboard` 進行完整引導式首次執行流程，使用 `openclaw setup` 僅建立基準設定/工作區，當你只需要設定頻道帳號時，使用 `openclaw channels add`。

當 configure 從提供者驗證選項開始時，預設模型與允許清單選擇器會自動偏好該提供者。對於 Volcengine 和 BytePlus 這類成對提供者，相同偏好也會比對其 coding-plan 變體（`volcengine-plan/*`、`byteplus-plan/*`）。如果偏好的提供者篩選器會產生空清單，configure 會退回未篩選的目錄，而不是顯示空白選擇器。

對於網頁搜尋，`openclaw configure --section web` 可讓你選擇提供者並設定其認證資訊。某些提供者也會顯示提供者專屬的後續提示：

  * **Grok** 可以使用相同的 `XAI_API_KEY` 提供選用的 `x_search` 設定，並讓你挑選 `x_search` 模型。
  * **Kimi** 可以詢問 Moonshot API 區域（`api.moonshot.ai` 或 `api.moonshot.cn`）以及預設的 Kimi 網頁搜尋模型。


相關：

  * Gateway 設定參考：[設定](</zh-TW/gateway/configuration>)
  * 設定 CLI：[設定](</zh-TW/cli/config>)


## 選項

  * `--section <section>`：可重複的區段篩選器


可用區段：

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


注意事項：

  * 選擇 Gateway 執行位置時，一律會更新 `gateway.mode`。如果這就是你需要的全部內容，你可以選擇「繼續」，而不選擇其他區段。
  * 在寫入本機設定後，當所選設定路徑需要時，configure 會安裝所選的可下載 Plugin。遠端 Gateway 設定不會安裝本機 Plugin 套件。
  * 以頻道為導向的服務（Slack/Discord/Matrix/Microsoft Teams）會在設定期間提示輸入頻道/房間允許清單。你可以輸入名稱或 ID；精靈會盡可能將名稱解析為 ID。
  * 如果你執行 daemon 安裝步驟，token 驗證需要 token，且 `gateway.auth.token` 由 SecretRef 管理，configure 會驗證 SecretRef，但不會將解析後的純文字 token 值持久保存到 supervisor 服務環境中繼資料。
  * 如果 token 驗證需要 token，且已設定的 token SecretRef 無法解析，configure 會阻止 daemon 安裝，並提供可操作的修復指引。
  * 如果同時設定了 `gateway.auth.token` 和 `gateway.auth.password`，且 `gateway.auth.mode` 未設定，configure 會阻止 daemon 安裝，直到明確設定 mode 為止。


## 範例

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [設定](</zh-TW/gateway/configuration>)


Was this useful?YesNo