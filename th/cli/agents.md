---
title: เอเจนต์
source_url: https://docs.openclaw.ai/th/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

จัดการเอเจนต์แบบแยกส่วน (พื้นที่ทำงาน + การยืนยันตัวตน + การกำหนดเส้นทาง).

ที่เกี่ยวข้อง:

  * [การกำหนดเส้นทางหลายเอเจนต์](</th/concepts/multi-agent>)
  * [พื้นที่ทำงานของเอเจนต์](</th/concepts/agent-workspace>)
  * [การกำหนดค่า Skills](</th/tools/skills-config>): การกำหนดค่าการมองเห็น Skills.


## ตัวอย่าง

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## การผูกการกำหนดเส้นทาง

ใช้การผูกการกำหนดเส้นทางเพื่อตรึงทราฟฟิกช่องทางขาเข้าไว้กับเอเจนต์เฉพาะ.

หากคุณต้องการให้แต่ละเอเจนต์เห็น Skills ต่างกันด้วย ให้กำหนดค่า `agents.defaults.skills` และ `agents.list[].skills` ใน `openclaw.json`. ดู [การกำหนดค่า Skills](</th/tools/skills-config>) และ [ข้อมูลอ้างอิงการกำหนดค่า](</th/gateway/config-agents#agents-defaults-skills>).

แสดงรายการการผูก:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

เพิ่มการผูก:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

หากคุณละเว้น `accountId` (`--bind <channel>`) OpenClaw จะระบุค่าจากค่าเริ่มต้นของช่องทางและฮุกการตั้งค่า Plugin เมื่อมีให้ใช้.

หากคุณละเว้น `--agent` สำหรับ `bind` หรือ `unbind` OpenClaw จะใช้เอเจนต์เริ่มต้นปัจจุบันเป็นเป้าหมาย.

### พฤติกรรมขอบเขตการผูก

  * การผูกที่ไม่มี `accountId` จะจับคู่กับบัญชีเริ่มต้นของช่องทางเท่านั้น.
  * `accountId: "*"` คือทางเลือกสำรองระดับทั้งช่องทาง (ทุกบัญชี) และมีความเฉพาะเจาะจงน้อยกว่าการผูกบัญชีแบบระบุชัดเจน.
  * หากเอเจนต์เดียวกันมีการผูกช่องทางที่ตรงกันโดยไม่มี `accountId` อยู่แล้ว และภายหลังคุณผูกด้วย `accountId` ที่ระบุชัดเจนหรือระบุได้ OpenClaw จะอัปเกรดการผูกที่มีอยู่นั้นแทนที่เดิม แทนที่จะเพิ่มรายการซ้ำ.


ตัวอย่าง:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

หลังการอัปเกรด การกำหนดเส้นทางสำหรับการผูกนั้นจะถูกจำกัดขอบเขตไว้ที่ `telegram:ops`. หากคุณต้องการการกำหนดเส้นทางสำหรับบัญชีเริ่มต้นด้วย ให้เพิ่มอย่างชัดเจน (เช่น `--bind telegram:default`).

ลบการผูก:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` รับได้ทั้ง `--all` หรือค่า `--bind` หนึ่งค่าหรือมากกว่า แต่ไม่ใช่ทั้งสองอย่างพร้อมกัน.

## พื้นผิวคำสั่ง

### `agents`

การเรียกใช้ `openclaw agents` โดยไม่มีคำสั่งย่อยเทียบเท่ากับ `openclaw agents list`.

### `agents list`

ตัวเลือก:

  * `--json`
  * `--bindings`: รวมกฎการกำหนดเส้นทางแบบเต็ม ไม่ใช่เฉพาะจำนวน/สรุปต่อเอเจนต์เท่านั้น


### `agents add [name]`

ตัวเลือก:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (ทำซ้ำได้)
  * `--non-interactive`
  * `--json`


หมายเหตุ:

  * การส่งแฟล็กเพิ่มแบบระบุชัดเจนใดๆ จะสลับคำสั่งไปยังเส้นทางแบบไม่โต้ตอบ.
  * โหมดไม่โต้ตอบต้องมีทั้งชื่อเอเจนต์และ `--workspace`.
  * `main` ถูกสงวนไว้และไม่สามารถใช้เป็น id ของเอเจนต์ใหม่ได้.
  * ในโหมดโต้ตอบ การเติมข้อมูลการยืนยันตัวตนจะคัดลอกเฉพาะโปรไฟล์แบบสแตติกที่พกพาได้ (`api_key` และ `token` แบบสแตติกโดยค่าเริ่มต้น). โปรไฟล์ OAuth refresh-token จะยังคง ใช้ได้ผ่านการสืบทอดแบบอ่านทะลุจากที่เก็บเอเจนต์ `main` จริงเท่านั้น. หากเอเจนต์เริ่มต้นที่กำหนดค่าไว้ไม่ใช่ `main` ให้ลงชื่อเข้าใช้แยกต่างหากสำหรับโปรไฟล์ OAuth บนเอเจนต์ใหม่.


### `agents bindings`

ตัวเลือก:

  * `--agent <id>`
  * `--json`


### `agents bind`

ตัวเลือก:

  * `--agent <id>` (ค่าเริ่มต้นคือเอเจนต์เริ่มต้นปัจจุบัน)
  * `--bind <channel[:accountId]>` (ทำซ้ำได้)
  * `--json`


### `agents unbind`

ตัวเลือก:

  * `--agent <id>` (ค่าเริ่มต้นคือเอเจนต์เริ่มต้นปัจจุบัน)
  * `--bind <channel[:accountId]>` (ทำซ้ำได้)
  * `--all`
  * `--json`


### `agents delete <id>`

ตัวเลือก:

  * `--force`
  * `--json`


หมายเหตุ:

  * ไม่สามารถลบ `main` ได้.
  * หากไม่มี `--force` ต้องมีการยืนยันแบบโต้ตอบ.
  * ไดเรกทอรีพื้นที่ทำงาน สถานะเอเจนต์ และทรานสคริปต์เซสชันจะถูกย้ายไปยังถังขยะ ไม่ใช่ลบถาวร.
  * เมื่อเข้าถึง Gateway ได้ การลบจะถูกส่งผ่าน Gateway เพื่อให้การล้างการกำหนดค่าและที่เก็บเซสชันใช้ตัวเขียนเดียวกับทราฟฟิกขณะรันไทม์. หากไม่สามารถเข้าถึง Gateway ได้ CLI จะถอยกลับไปใช้เส้นทางภายในแบบออฟไลน์.
  * หากพื้นที่ทำงานของเอเจนต์อื่นเป็นพาธเดียวกัน อยู่ภายในพื้นที่ทำงานนี้ หรือมีพื้นที่ทำงานนี้อยู่ภายใน พื้นที่ทำงานจะถูกเก็บไว้ และ `--json` จะรายงาน `workspaceRetained`, `workspaceRetainedReason` และ `workspaceSharedWith`.


## ไฟล์อัตลักษณ์

พื้นที่ทำงานของเอเจนต์แต่ละตัวสามารถมี `IDENTITY.md` ที่รากพื้นที่ทำงานได้:

  * พาธตัวอย่าง: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` อ่านจากรากพื้นที่ทำงาน (หรือ `--identity-file` ที่ระบุชัดเจน)


พาธอวาตาร์จะถูกระบุเทียบกับรากพื้นที่ทำงาน.

## ตั้งค่าอัตลักษณ์

`set-identity` เขียนฟิลด์ลงใน `agents.list[].identity`:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (พาธแบบสัมพันธ์กับพื้นที่ทำงาน, URL http(s) หรือ data URI)


ตัวเลือก:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


หมายเหตุ:

  * สามารถใช้ `--agent` หรือ `--workspace` เพื่อเลือกเอเจนต์เป้าหมายได้.
  * หากคุณพึ่งพา `--workspace` และมีหลายเอเจนต์ใช้พื้นที่ทำงานนั้นร่วมกัน คำสั่งจะล้มเหลวและขอให้คุณส่ง `--agent`.
  * เมื่อไม่มีการระบุฟิลด์อัตลักษณ์อย่างชัดเจน คำสั่งจะอ่านข้อมูลอัตลักษณ์จาก `IDENTITY.md`.


โหลดจาก `IDENTITY.md`:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

แทนที่ฟิลด์อย่างชัดเจน:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

ตัวอย่างการกำหนดค่า:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [การกำหนดเส้นทางหลายเอเจนต์](</th/concepts/multi-agent>)
  * [พื้นที่ทำงานของเอเจนต์](</th/concepts/agent-workspace>)


Was this useful?YesNo