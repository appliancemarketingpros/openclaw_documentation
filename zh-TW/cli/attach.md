---
title: 附加命令列介面
source_url: https://docs.openclaw.ai/zh-TW/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` 會以嚴格的臨時 MCP 設定啟動 Claude Code，並綁定到單一閘道工作階段。

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

選項：

  * `--session <key>` 將授權綁定到閘道工作階段。預設為主工作階段。
  * `--ttl <ms>` 要求以毫秒為單位的正值授權 TTL。閘道會套用自己的上限。
  * `--bin <path>` 選取 Claude Code 二進位檔。預設：`claude`。
  * `--print-config` 會寫入臨時 `.mcp.json`，列印啟動命令與環境，並讓授權保持有效直到 TTL 到期（它不會產生 Claude Code 或撤銷授權）。


持有人權杖會透過環境變數傳遞，而不是透過命令列引數。OpenClaw 會以 `--strict-mcp-config --mcp-config <path>` 啟動 Claude Code，因此環境中的 Claude MCP 伺服器不會加入附加的工作階段。一般啟動（不使用 `--print-config`）會在 Claude Code 程序結束時撤銷授權。

另請參閱：[閘道命令列介面](</zh-TW/cli/gateway>)、[MCP 命令列介面](</zh-TW/cli/mcp>) 和 [ACP 命令列介面](</zh-TW/cli/acp>)。

Was this useful?YesNo

Open issue