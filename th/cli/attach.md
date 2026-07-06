---
title: แนบ CLI
source_url: https://docs.openclaw.ai/th/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` เปิด Claude Code ด้วยการกำหนดค่า MCP ชั่วคราวที่เข้มงวดซึ่งผูกกับ หนึ่งเซสชันของ Gateway

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

ตัวเลือก:

  * `--session <key>` ผูกสิทธิ์อนุญาตกับเซสชันของ Gateway ค่าเริ่มต้นคือเซสชันหลัก
  * `--ttl <ms>` ขอ TTL ของสิทธิ์อนุญาตที่เป็นค่าบวกในหน่วยมิลลิวินาที Gateway จะใช้เพดานของตัวเอง
  * `--bin <path>` เลือกไบนารี Claude Code ค่าเริ่มต้นคือ `claude`
  * `--print-config` เขียน `.mcp.json` ชั่วคราว พิมพ์คำสั่งเปิดใช้งานและ env และปล่อยให้สิทธิ์อนุญาตยังมีผลจนกว่า TTL จะหมดอายุ


โทเค็น bearer ถูกส่งผ่านตัวแปรสภาพแวดล้อม ไม่ใช่ argv OpenClaw เปิด Claude Code ด้วย `--strict-mcp-config --mcp-config <path>` เพื่อให้เซิร์ฟเวอร์ Claude MCP ในสภาพแวดล้อมโดยรอบไม่เข้าร่วมเซสชันที่แนบอยู่ การเปิดใช้งานตามปกติจะเพิกถอน สิทธิ์อนุญาตเมื่อกระบวนการ Claude Code ออก

ดูเพิ่มเติม: [Gateway CLI](</th/cli/gateway>), [MCP CLI](</th/cli/mcp>), และ [ACP CLI](</th/cli/acp>).

Was this useful?YesNo

Open issue