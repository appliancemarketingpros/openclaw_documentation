---
title: แซนด์บ็อกซ์และเครื่องมือแบบหลายเอเจนต์
source_url: https://docs.openclaw.ai/th/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

เอเจนต์แต่ละตัวในการตั้งค่าแบบหลายเอเจนต์สามารถเขียนทับ sandbox และนโยบายเครื่องมือส่วนกลางได้ หน้านี้ครอบคลุมการกำหนดค่ารายเอเจนต์ กฎลำดับความสำคัญ และตัวอย่างต่าง ๆ

[**Sandboxing** แบ็กเอนด์และโหมดต่าง ๆ — เอกสารอ้างอิง sandbox ฉบับเต็ม ](</th/gateway/sandboxing>) [**Sandbox กับนโยบายเครื่องมือกับ elevated** ดีบัก "ทำไมสิ่งนี้ถึงถูกบล็อก?" ](</th/gateway/sandbox-vs-tool-policy-vs-elevated>) [**โหมด Elevated** exec แบบ Elevated สำหรับผู้ส่งที่เชื่อถือได้ ](</th/tools/elevated>)

* * *

## ตัวอย่างการกำหนดค่า

ตัวอย่างที่ 1: เอเจนต์ส่วนตัว + เอเจนต์ครอบครัวแบบจำกัด jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**ผลลัพธ์:**

  * เอเจนต์ `main`: ทำงานบนโฮสต์ เข้าถึงเครื่องมือได้เต็มรูปแบบ
  * เอเจนต์ `family`: ทำงานใน Docker (หนึ่งคอนเทนเนอร์ต่อเอเจนต์) ส่งข้อความได้เฉพาะ `read` และบทสนทนาปัจจุบัน

ตัวอย่างที่ 2: เอเจนต์งานพร้อม sandbox ที่แชร์ร่วมกัน jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

ตัวอย่างที่ 2b: โปรไฟล์เขียนโค้ดส่วนกลาง + เอเจนต์เฉพาะการส่งข้อความ jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**ผลลัพธ์:**

  * เอเจนต์เริ่มต้นได้รับเครื่องมือเขียนโค้ด
  * เอเจนต์ `support` เป็นแบบเฉพาะการส่งข้อความเท่านั้น (+ เครื่องมือ Slack)

ตัวอย่างที่ 3: โหมด sandbox ต่างกันตามเอเจนต์ jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## ลำดับความสำคัญของการกำหนดค่า

เมื่อมีทั้งการกำหนดค่าส่วนกลาง (`agents.defaults.*`) และการกำหนดค่าเฉพาะเอเจนต์ (`agents.list[].*`):

### การกำหนดค่า sandbox

การตั้งค่าเฉพาะเอเจนต์จะเขียนทับส่วนกลาง:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### ข้อจำกัดของเครื่องมือ

ลำดับการกรองคือ:

* ### โปรไฟล์เครื่องมือ

`tools.profile` หรือ `agents.list[].tools.profile`

* ### โปรไฟล์เครื่องมือของผู้ให้บริการ

`tools.byProvider[provider].profile` หรือ `agents.list[].tools.byProvider[provider].profile`

* ### นโยบายเครื่องมือส่วนกลาง

`tools.allow` / `tools.deny`

* ### นโยบายเครื่องมือของผู้ให้บริการ

`tools.byProvider[provider].allow/deny`

* ### นโยบายเครื่องมือเฉพาะเอเจนต์

`agents.list[].tools.allow/deny`

* ### นโยบายผู้ให้บริการของเอเจนต์

`agents.list[].tools.byProvider[provider].allow/deny`

* ### นโยบายเครื่องมือของ sandbox

`tools.sandbox.tools` หรือ `agents.list[].tools.sandbox.tools`

* ### นโยบายเครื่องมือของเอเจนต์ย่อย

`tools.subagents.tools` หากเกี่ยวข้อง

กฎลำดับความสำคัญ

  * แต่ละระดับสามารถจำกัดเครื่องมือเพิ่มเติมได้ แต่ไม่สามารถให้สิทธิ์เครื่องมือที่ถูกปฏิเสธจากระดับก่อนหน้ากลับคืนมาได้
  * หากตั้งค่า `agents.list[].tools.sandbox.tools` ไว้ ค่านี้จะแทนที่ `tools.sandbox.tools` สำหรับเอเจนต์นั้น
  * หากตั้งค่า `agents.list[].tools.profile` ไว้ ค่านี้จะเขียนทับ `tools.profile` สำหรับเอเจนต์นั้น
  * คีย์เครื่องมือของผู้ให้บริการรับได้ทั้ง `provider` (เช่น `google-antigravity`) หรือ `provider/model` (เช่น `openai/gpt-5.4`)

พฤติกรรมของ allowlist ว่าง

หาก allowlist ที่ระบุไว้อย่างชัดเจนในเชนดังกล่าวทำให้การรันไม่มีเครื่องมือที่เรียกใช้ได้ OpenClaw จะหยุดก่อนส่งพรอมป์ไปยังโมเดล นี่เป็นพฤติกรรมที่ตั้งใจไว้: เอเจนต์ที่กำหนดค่าด้วยเครื่องมือที่หายไป เช่น `agents.list[].tools.allow: ["query_db"]` ควรล้มเหลวอย่างชัดเจนจนกว่า Plugin ที่ลงทะเบียน `query_db` จะถูกเปิดใช้งาน ไม่ใช่ดำเนินการต่อในฐานะเอเจนต์แบบข้อความเท่านั้น

นโยบายเครื่องมือรองรับรูปแบบย่อ `group:*` ที่ขยายเป็นหลายเครื่องมือ ดูรายการทั้งหมดที่ [กลุ่มเครื่องมือ](</th/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>)

การเขียนทับ elevated แบบรายเอเจนต์ (`agents.list[].tools.elevated`) สามารถจำกัด exec แบบ elevated เพิ่มเติมสำหรับเอเจนต์เฉพาะได้ ดูรายละเอียดที่ [โหมด Elevated](</th/tools/elevated>)

* * *

## การย้ายจากเอเจนต์เดียว

### ก่อนหน้า (เอเจนต์เดียว)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### หลังจากนั้น (หลายเอเจนต์)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## ตัวอย่างการจำกัดเครื่องมือ

### เอเจนต์แบบอ่านอย่างเดียว

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### การเรียกใช้เชลล์โดยปิดใช้งานเครื่องมือระบบไฟล์

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### การสื่อสารเท่านั้น

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` ในโปรไฟล์นี้ยังคงส่งคืนมุมมองการเรียกคืนที่มีขอบเขตและผ่านการทำให้ปลอดภัยแล้ว แทนที่จะเป็นการ dump transcript ดิบ การเรียกคืนของผู้ช่วยจะลบแท็กการคิด, โครง `<relevant-memories>`, payload XML ของการเรียกเครื่องมือแบบข้อความล้วน (รวมถึง `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` และบล็อกการเรียกเครื่องมือที่ถูกตัดทอน), โครงการเรียกเครื่องมือที่ถูกลดระดับ, โทเค็นควบคุมโมเดล ASCII/แบบเต็มความกว้างที่รั่วไหล และ XML การเรียกเครื่องมือ MiniMax ที่ผิดรูป ก่อนการปกปิด/ตัดทอน

* * *

## ข้อผิดพลาดที่พบบ่อย: "non-main"

* * *

## การทดสอบ

หลังจากกำหนดค่า sandbox และเครื่องมือสำหรับหลายเอเจนต์แล้ว:

* ### ตรวจสอบการ resolve เอเจนต์

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### ตรวจสอบคอนเทนเนอร์ sandbox

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### ทดสอบการจำกัดเครื่องมือ

  * ส่งข้อความที่ต้องใช้เครื่องมือที่ถูกจำกัด
  * ตรวจสอบว่าเอเจนต์ไม่สามารถใช้เครื่องมือที่ถูกปฏิเสธได้


* ### ติดตามบันทึก

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## การแก้ไขปัญหา

เอเจนต์ไม่ถูก sandbox แม้จะตั้งค่า `mode: 'all'`

  * ตรวจสอบว่ามี `agents.defaults.sandbox.mode` แบบ global ที่ override ค่านี้หรือไม่
  * การตั้งค่าเฉพาะเอเจนต์มีลำดับความสำคัญสูงกว่า ดังนั้นให้ตั้งค่า `agents.list[].sandbox.mode: "all"`

เครื่องมือยังพร้อมใช้งานแม้จะมีรายการปฏิเสธ

  * ตรวจสอบลำดับการกรองเครื่องมือ: global → agent → sandbox → subagent
  * แต่ละระดับทำได้เพียงจำกัดเพิ่มเติมเท่านั้น ไม่สามารถให้สิทธิ์กลับคืนได้
  * ตรวจสอบด้วยบันทึก: `[tools] filtering tools for agent:${agentId}`

คอนเทนเนอร์ไม่ได้แยกตามเอเจนต์

  * ตั้งค่า `scope: "agent"` ในการตั้งค่า sandbox เฉพาะเอเจนต์
  * ค่าเริ่มต้นคือ `"session"` ซึ่งสร้างหนึ่งคอนเทนเนอร์ต่อหนึ่งเซสชัน


* * *

## ที่เกี่ยวข้อง

  * [โหมดยกระดับ](</th/tools/elevated>)
  * [การกำหนดเส้นทางหลายเอเจนต์](</th/concepts/multi-agent>)
  * [การกำหนดค่าแซนด์บ็อกซ์](</th/gateway/config-agents#agentsdefaultssandbox>)
  * [แซนด์บ็อกซ์เทียบกับนโยบายเครื่องมือเทียบกับโหมดยกระดับ](</th/gateway/sandbox-vs-tool-policy-vs-elevated>) — การดีบัก “ทำไมสิ่งนี้จึงถูกบล็อก?”
  * [การทำแซนด์บ็อกซ์](</th/gateway/sandboxing>) — เอกสารอ้างอิงแซนด์บ็อกซ์ฉบับเต็ม (โหมด, ขอบเขต, แบ็กเอนด์, อิมเมจ)
  * [การจัดการเซสชัน](</th/concepts/session>)


Was this useful?YesNo