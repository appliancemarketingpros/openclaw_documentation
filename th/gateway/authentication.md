---
title: การยืนยันตัวตน
source_url: https://docs.openclaw.ai/th/gateway/authentication
scraped_at: 2026-05-25
---

OpenClaw รองรับ OAuth และคีย์ API สำหรับผู้ให้บริการโมเดล สำหรับโฮสต์ Gateway ที่เปิดทำงานตลอดเวลา คีย์ API มักเป็นตัวเลือกที่คาดการณ์ได้มากที่สุด โฟลว์แบบการสมัครสมาชิก/OAuth ก็รองรับเช่นกันเมื่อสอดคล้องกับรูปแบบบัญชีผู้ให้บริการของคุณ

ดู [/concepts/oauth](</th/concepts/oauth>) สำหรับโฟลว์ OAuth และรูปแบบการจัดเก็บ ทั้งหมด สำหรับการยืนยันตัวตนแบบอิง SecretRef (ผู้ให้บริการ `env`/`file`/`exec`) โปรดดู [การจัดการความลับ](</th/gateway/secrets>) สำหรับกฎคุณสมบัติของข้อมูลประจำตัว/รหัสเหตุผลที่ใช้โดย `models status --probe` โปรดดู [ความหมายของข้อมูลประจำตัวการยืนยันตัวตน](</th/auth-credential-semantics>)

## การตั้งค่าที่แนะนำ (คีย์ API, ผู้ให้บริการใดก็ได้)

หากคุณกำลังเรียกใช้ Gateway ที่ใช้งานระยะยาว ให้เริ่มด้วยคีย์ API สำหรับ ผู้ให้บริการที่คุณเลือก สำหรับ Anthropic โดยเฉพาะ การยืนยันตัวตนด้วยคีย์ API ยังเป็นการตั้งค่าเซิร์ฟเวอร์ ที่คาดการณ์ได้มากที่สุด แต่ OpenClaw ยังรองรับการใช้การเข้าสู่ระบบ Claude CLI ในเครื่องซ้ำด้วย

  1. สร้างคีย์ API ในคอนโซลของผู้ให้บริการ
  2. วางคีย์ไว้บน**โฮสต์ Gateway** (เครื่องที่เรียกใช้ `openclaw gateway`)

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."openclaw models status
[/code]

  3. หาก Gateway ทำงานภายใต้ systemd/launchd แนะนำให้วางคีย์ไว้ใน `~/.openclaw/.env` เพื่อให้ daemon อ่านได้:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'&lt;PROVIDER&gt;_API_KEY=...EOF
[/code]

จากนั้นรีสตาร์ต daemon (หรือรีสตาร์ตกระบวนการ Gateway ของคุณ) แล้วตรวจสอบอีกครั้ง:

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

หากคุณไม่ต้องการจัดการตัวแปรสภาพแวดล้อมด้วยตัวเอง ขั้นตอนเริ่มต้นใช้งานสามารถจัดเก็บ คีย์ API สำหรับการใช้งานโดย daemon ได้: `openclaw onboard`

ดู [ความช่วยเหลือ](</th/help>) สำหรับรายละเอียดเกี่ยวกับการสืบทอดสภาพแวดล้อม (`env.shellEnv`, `~/.openclaw/.env`, systemd/launchd)

## Anthropic: ความเข้ากันได้ของ Claude CLI และโทเค็น

การยืนยันตัวตนด้วย setup-token ของ Anthropic ยังมีอยู่ใน OpenClaw ในฐานะเส้นทางโทเค็น ที่รองรับ เจ้าหน้าที่ Anthropic ได้แจ้งเราตั้งแต่นั้นว่าการใช้งาน Claude CLI แบบ OpenClaw ได้รับอนุญาตอีกครั้ง ดังนั้น OpenClaw จึงถือว่าการใช้ Claude CLI ซ้ำและการใช้งาน `claude -p` ได้รับการอนุมัติสำหรับการผสานรวมนี้ เว้นแต่ Anthropic จะเผยแพร่นโยบายใหม่ เมื่อ การใช้ Claude CLI ซ้ำพร้อมใช้งานบนโฮสต์ ตอนนี้นี่คือเส้นทางที่แนะนำ

สำหรับโฮสต์ Gateway ที่ใช้งานระยะยาว คีย์ API ของ Anthropic ยังเป็นการตั้งค่า ที่คาดการณ์ได้มากที่สุด หากคุณต้องการใช้การเข้าสู่ระบบ Claude ที่มีอยู่บนโฮสต์เดียวกันซ้ำ ให้ใช้ เส้นทาง Anthropic Claude CLI ในขั้นตอนเริ่มต้นใช้งาน/กำหนดค่า

การตั้งค่าโฮสต์ที่แนะนำสำหรับการใช้ Claude CLI ซ้ำ:

bashCopy code
[code]
    # Run on the gateway hostclaude auth loginclaude auth status --textopenclaw models auth login --provider anthropic --method cli --set-default
[/code]

นี่คือการตั้งค่าแบบสองขั้นตอน:

  1. เข้าสู่ระบบ Claude Code เองกับ Anthropic บนโฮสต์ Gateway
  2. บอก OpenClaw ให้สลับการเลือกโมเดล Anthropic ไปใช้แบ็กเอนด์ `claude-cli` ในเครื่อง และจัดเก็บโปรไฟล์การยืนยันตัวตน OpenClaw ที่ตรงกัน


หาก `claude` ไม่อยู่ใน `PATH` ให้ติดตั้ง Claude Code ก่อนหรือตั้งค่า `agents.defaults.cliBackends.claude-cli.command` เป็นพาธไบนารีจริง

การป้อนโทเค็นด้วยตนเอง (ผู้ให้บริการใดก็ได้; เขียน `auth-profiles.json` \+ อัปเดตการกำหนดค่า):

bashCopy code
[code]
    openclaw models auth paste-token --provider openrouter
[/code]

`auth-profiles.json` จัดเก็บเฉพาะข้อมูลประจำตัว รูปแบบมาตรฐานคือ:

jsonCopy code
[code]
    {  "version": 1,  "profiles": {    "openrouter:default": {      "type": "api_key",      "provider": "openrouter",      "key": "OPENROUTER_API_KEY"    }  }}
[/code]

OpenClaw คาดหวังรูปแบบมาตรฐาน `version` \+ `profiles` ในระหว่างรันไทม์ หากการติดตั้งเก่ายังมีไฟล์แบบแบน เช่น `{ "openrouter": { "apiKey": "..." } }` ให้เรียกใช้ `openclaw doctor --fix` เพื่อเขียนใหม่เป็นโปรไฟล์คีย์ API `openrouter:default`; doctor จะเก็บสำเนา `.legacy-flat.*.bak` ไว้ข้างไฟล์ต้นฉบับ รายละเอียดปลายทาง เช่น `baseUrl`, `api`, รหัสโมเดล, ส่วนหัว และไทม์เอาต์ ควรอยู่ภายใต้ `models.providers.<id>` ใน `openclaw.json` หรือ `models.json` ไม่ใช่ใน `auth-profiles.json`

เส้นทางการยืนยันตัวตนภายนอก เช่น Bedrock `auth: "aws-sdk"` ก็ไม่ใช่ข้อมูลประจำตัวเช่นกัน หากคุณต้องการเส้นทาง Bedrock ที่มีชื่อ ให้วาง `auth.profiles.<id>.mode: "aws-sdk"` ใน `openclaw.json`; อย่าเขียน `type: "aws-sdk"` ลงใน `auth-profiles.json` `openclaw doctor --fix` จะย้ายตัวทำเครื่องหมาย AWS SDK แบบเดิมจากที่เก็บข้อมูลประจำตัวไปยังเมทาดาทาการกำหนดค่า

ยังรองรับการอ้างอิงโปรไฟล์การยืนยันตัวตนสำหรับข้อมูลประจำตัวแบบคงที่ด้วย:

  * ข้อมูลประจำตัว `api_key` สามารถใช้ `keyRef: { source, provider, id }`
  * ข้อมูลประจำตัว `token` สามารถใช้ `tokenRef: { source, provider, id }`
  * โปรไฟล์โหมด OAuth ไม่รองรับข้อมูลประจำตัว SecretRef; หากตั้งค่า `auth.profiles.<id>.mode` เป็น `"oauth"` อินพุต `keyRef`/`tokenRef` ที่อิง SecretRef สำหรับโปรไฟล์นั้นจะถูกปฏิเสธ


การตรวจสอบที่เหมาะกับระบบอัตโนมัติ (ออกด้วย `1` เมื่อหมดอายุ/หายไป, `2` เมื่อใกล้หมดอายุ):

bashCopy code
[code]
    openclaw models status --check
[/code]

การตรวจสอบการยืนยันตัวตนแบบสด:

bashCopy code
[code]
    openclaw models status --probe
[/code]

หมายเหตุ:

  * แถวการตรวจสอบอาจมาจากโปรไฟล์การยืนยันตัวตน, ข้อมูลประจำตัวสภาพแวดล้อม หรือ `models.json`
  * หาก `auth.order.<provider>` ที่ระบุชัดเจนละเว้นโปรไฟล์ที่จัดเก็บไว้ การตรวจสอบจะรายงาน `excluded_by_auth_order` สำหรับโปรไฟล์นั้นแทนที่จะลองใช้
  * หากมีการยืนยันตัวตนอยู่ แต่ OpenClaw ไม่สามารถแก้ไขตัวเลือกโมเดลที่ตรวจสอบได้สำหรับ ผู้ให้บริการนั้น การตรวจสอบจะรายงาน `status: no_model`
  * คูลดาวน์ของการจำกัดอัตราอาจมีขอบเขตตามโมเดล โปรไฟล์ที่กำลังคูลดาวน์สำหรับโมเดลหนึ่ง ยังอาจใช้งานได้กับโมเดลพี่น้องบนผู้ให้บริการเดียวกัน


สคริปต์ปฏิบัติการเสริม (systemd/Termux) มีเอกสารไว้ที่นี่: [สคริปต์ตรวจสอบการยืนยันตัวตน](</th/help/scripts#auth-monitoring-scripts>)

## หมายเหตุเกี่ยวกับ Anthropic

แบ็กเอนด์ Anthropic `claude-cli` รองรับอีกครั้งแล้ว

  * เจ้าหน้าที่ Anthropic แจ้งเราว่าเส้นทางการผสานรวม OpenClaw นี้ได้รับอนุญาตอีกครั้ง
  * ดังนั้น OpenClaw จึงถือว่าการใช้ Claude CLI ซ้ำและการใช้งาน `claude -p` ได้รับการอนุมัติ สำหรับการรันที่รองรับโดย Anthropic เว้นแต่ Anthropic จะเผยแพร่นโยบายใหม่
  * คีย์ API ของ Anthropic ยังคงเป็นตัวเลือกที่คาดการณ์ได้มากที่สุดสำหรับโฮสต์ Gateway ที่ใช้งานระยะยาวและการควบคุมการเรียกเก็บเงินฝั่งเซิร์ฟเวอร์อย่างชัดเจน


## การตรวจสอบสถานะการยืนยันตัวตนของโมเดล

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

## ลักษณะการหมุนเวียนคีย์ API (Gateway)

ผู้ให้บริการบางรายรองรับการลองคำขอซ้ำด้วยคีย์ทางเลือกเมื่อการเรียก API เจอการจำกัดอัตราจากผู้ให้บริการ

  * ลำดับความสำคัญ: 
    * `OPENCLAW_LIVE_&lt;PROVIDER&gt;_KEY` (การแทนที่รายการเดียว)
    * `&lt;PROVIDER&gt;_API_KEYS`
    * `&lt;PROVIDER&gt;_API_KEY`
    * `&lt;PROVIDER&gt;_API_KEY_*`
  * ผู้ให้บริการ Google ยังรวม `GOOGLE_API_KEY` เป็นตัวสำรองเพิ่มเติมด้วย
  * รายการคีย์เดียวกันจะถูกลบรายการซ้ำก่อนใช้งาน
  * OpenClaw จะลองซ้ำด้วยคีย์ถัดไปเฉพาะสำหรับข้อผิดพลาดการจำกัดอัตราเท่านั้น (เช่น `429`, `rate_limit`, `quota`, `resource exhausted`, `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached` หรือ `workers_ai ... quota limit exceeded`)
  * ข้อผิดพลาดที่ไม่ใช่การจำกัดอัตราจะไม่ถูกลองซ้ำด้วยคีย์ทางเลือก
  * หากคีย์ทั้งหมดล้มเหลว จะส่งคืนข้อผิดพลาดสุดท้ายจากความพยายามครั้งล่าสุด


## การควบคุมว่าจะใช้ข้อมูลประจำตัวใด

### ต่อเซสชัน (คำสั่งแชต)

ใช้ `/model <alias-or-id>@<profileId>` เพื่อปักหมุดข้อมูลประจำตัวผู้ให้บริการเฉพาะสำหรับเซสชันปัจจุบัน (ตัวอย่างรหัสโปรไฟล์: `anthropic:default`, `anthropic:work`)

ใช้ `/model` (หรือ `/model list`) สำหรับตัวเลือกแบบกะทัดรัด; ใช้ `/model status` สำหรับมุมมองเต็ม (ตัวเลือก + โปรไฟล์การยืนยันตัวตนถัดไป รวมถึงรายละเอียดปลายทางผู้ให้บริการเมื่อกำหนดค่าไว้)

### ต่อตัวแทน (การแทนที่ CLI)

ตั้งค่าการแทนที่ลำดับโปรไฟล์การยืนยันตัวตนอย่างชัดเจนสำหรับตัวแทน (จัดเก็บใน `auth-state.json` ของตัวแทนนั้น):

bashCopy code
[code]
    openclaw models auth order get --provider anthropicopenclaw models auth order set --provider anthropic anthropic:defaultopenclaw models auth order clear --provider anthropic
[/code]

ใช้ `--agent <id>` เพื่อกำหนดเป้าหมายตัวแทนเฉพาะ; ละไว้เพื่อใช้ตัวแทนเริ่มต้นที่กำหนดค่าไว้ เมื่อคุณแก้ไขปัญหาลำดับ `openclaw models status --probe` จะแสดงโปรไฟล์ที่จัดเก็บไว้ ซึ่งถูกละเว้นเป็น `excluded_by_auth_order` แทนที่จะข้ามแบบเงียบ เมื่อคุณแก้ไขปัญหาคูลดาวน์ โปรดจำว่าคูลดาวน์ของการจำกัดอัตราอาจผูกกับ รหัสโมเดลหนึ่งรายการแทนที่จะเป็นโปรไฟล์ผู้ให้บริการทั้งหมด

## การแก้ไขปัญหา

### "ไม่พบข้อมูลประจำตัว"

หากโปรไฟล์ Anthropic หายไป ให้กำหนดค่าคีย์ API ของ Anthropic บน **โฮสต์ Gateway** หรือตั้งค่าเส้นทาง setup-token ของ Anthropic แล้วตรวจสอบอีกครั้ง:

bashCopy code
[code]
    openclaw models status
[/code]

### โทเค็นใกล้หมดอายุ/หมดอายุแล้ว

เรียกใช้ `openclaw models status` เพื่อยืนยันว่าโปรไฟล์ใดกำลังจะหมดอายุ หาก โปรไฟล์โทเค็น Anthropic หายไปหรือหมดอายุ ให้รีเฟรชการตั้งค่านั้นผ่าน setup-token หรือย้ายไปใช้คีย์ API ของ Anthropic

## ที่เกี่ยวข้อง

  * [การจัดการความลับ](</th/gateway/secrets>)
  * [การเข้าถึงระยะไกล](</th/gateway/remote>)
  * [ที่เก็บข้อมูลการยืนยันตัวตน](</th/concepts/oauth>)


Was this useful?YesNo