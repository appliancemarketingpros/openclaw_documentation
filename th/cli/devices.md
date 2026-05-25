---
title: อุปกรณ์
source_url: https://docs.openclaw.ai/th/cli/devices
scraped_at: 2026-05-25
---

# `openclaw devices`

จัดการคำขอจับคู่อุปกรณ์และโทเค็นตามขอบเขตอุปกรณ์

## คำสั่ง

### `openclaw devices list`

แสดงรายการคำขอจับคู่ที่รอดำเนินการและอุปกรณ์ที่จับคู่แล้ว

CodeCopy code
[code]
    openclaw devices listopenclaw devices list --json
[/code]

เอาต์พุตคำขอที่รอดำเนินการจะแสดงสิทธิ์เข้าถึงที่ร้องขอถัดจากสิทธิ์เข้าถึงปัจจุบัน ที่ได้รับอนุมัติของอุปกรณ์ เมื่ออุปกรณ์จับคู่แล้ว วิธีนี้ทำให้การอัปเกรด scope/role ชัดเจน แทนที่จะดูเหมือนว่าการจับคู่สูญหายไป

### `openclaw devices remove <deviceId>`

ลบรายการอุปกรณ์ที่จับคู่แล้วหนึ่งรายการ

เมื่อคุณตรวจสอบสิทธิ์ด้วยโทเค็นอุปกรณ์ที่จับคู่แล้ว ผู้เรียกที่ไม่ใช่แอดมินสามารถ ลบได้เฉพาะรายการอุปกรณ์ของ**ตนเอง** เท่านั้น การลบอุปกรณ์อื่นต้องมี `operator.admin`

CodeCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices remove <deviceId> --json
[/code]

### `openclaw devices clear --yes [--pending]`

ล้างอุปกรณ์ที่จับคู่แล้วแบบเป็นกลุ่ม

CodeCopy code
[code]
    openclaw devices clear --yesopenclaw devices clear --yes --pendingopenclaw devices clear --yes --pending --json
[/code]

### `openclaw devices approve [requestId] [--latest]`

อนุมัติคำขอจับคู่อุปกรณ์ที่รอดำเนินการด้วย `requestId` ที่ตรงกันทุกตัว หากละเว้น `requestId` หรือส่ง `--latest` OpenClaw จะพิมพ์เฉพาะคำขอที่รอดำเนินการที่เลือกไว้ แล้วออก ให้เรียกใช้การอนุมัติอีกครั้งด้วย ID คำขอที่ตรงกันทุกตัวหลังจากตรวจสอบ รายละเอียดแล้ว

หากอุปกรณ์จับคู่แล้วและขอ scopes ที่กว้างขึ้นหรือ role ที่กว้างขึ้น OpenClaw จะคง การอนุมัติเดิมไว้ และสร้างคำขออัปเกรดใหม่ที่รอดำเนินการ ตรวจสอบคอลัมน์ `Requested` เทียบกับ `Approved` ใน `openclaw devices list` หรือใช้ `openclaw devices approve --latest` เพื่อดูตัวอย่างการอัปเกรดที่ตรงกันทุกตัวก่อนอนุมัติ

หาก Gateway ได้รับการกำหนดค่าอย่างชัดเจนด้วย `gateway.nodes.pairing.autoApproveCidrs` คำขอ `role: node` ครั้งแรกจาก IP ไคลเอ็นต์ ที่ตรงกันอาจได้รับการอนุมัติก่อนที่จะปรากฏในรายการนี้ นโยบายดังกล่าวปิดใช้งาน เป็นค่าเริ่มต้น และจะไม่ใช้กับไคลเอ็นต์ operator/browser หรือคำขออัปเกรด

CodeCopy code
[code]
    openclaw devices approveopenclaw devices approve <requestId>openclaw devices approve --latest
[/code]

### `openclaw devices reject <requestId>`

ปฏิเสธคำขอจับคู่อุปกรณ์ที่รอดำเนินการ

CodeCopy code
[code]
    openclaw devices reject <requestId>
[/code]

### `openclaw devices rotate --device <id> --role <role> [--scope <scope...>]`

หมุนเวียนโทเค็นอุปกรณ์สำหรับ role เฉพาะ (อัปเดต scopes ได้ตามต้องการ) role เป้าหมายต้องมีอยู่แล้วในสัญญาการจับคู่ที่ได้รับอนุมัติของอุปกรณ์นั้น การหมุนเวียนไม่สามารถ mint role ใหม่ที่ยังไม่ได้รับอนุมัติได้ หากคุณละเว้น `--scope` การเชื่อมต่อใหม่ในภายหลังด้วยโทเค็นที่หมุนเวียนและจัดเก็บไว้ จะนำ scopes ที่ได้รับอนุมัติซึ่งแคชไว้ของโทเค็นนั้นกลับมาใช้ หากคุณส่งค่า `--scope` อย่างชัดเจน ค่าเหล่านั้นจะกลายเป็นชุด scope ที่จัดเก็บไว้สำหรับการเชื่อมต่อใหม่ ด้วย cached-token ในอนาคต ผู้เรียกที่เป็น paired-device ซึ่งไม่ใช่แอดมินสามารถหมุนเวียนได้เฉพาะโทเค็นอุปกรณ์ ของ**ตนเอง** เท่านั้น ชุด scope ของโทเค็นเป้าหมายต้องยังอยู่ภายใน operator scopes ของเซสชันผู้เรียกเอง การหมุนเวียนไม่สามารถ mint หรือคงโทเค็น operator ที่กว้างกว่าที่ผู้เรียกมีอยู่แล้วได้

CodeCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator --scope operator.read --scope operator.write
[/code]

ส่งคืน metadata การหมุนเวียนเป็น JSON หากผู้เรียกกำลังหมุนเวียนโทเค็นของตนเอง ขณะตรวจสอบสิทธิ์ด้วยโทเค็นอุปกรณ์นั้น การตอบกลับจะรวมโทเค็นทดแทนไว้ด้วย เพื่อให้ไคลเอ็นต์สามารถเก็บไว้ก่อนเชื่อมต่อใหม่ การหมุนเวียนแบบ shared/admin จะไม่ echo bearer token

### `openclaw devices revoke --device <id> --role <role>`

เพิกถอนโทเค็นอุปกรณ์สำหรับ role เฉพาะ

ผู้เรียกที่เป็น paired-device ซึ่งไม่ใช่แอดมินสามารถเพิกถอนได้เฉพาะโทเค็นอุปกรณ์ ของ**ตนเอง** เท่านั้น การเพิกถอนโทเค็นของอุปกรณ์อื่นต้องมี `operator.admin` ชุด scope ของโทเค็นเป้าหมายต้องอยู่ภายใน operator scopes ของเซสชันผู้เรียกเองด้วย ผู้เรียกแบบ pairing-only ไม่สามารถเพิกถอนโทเค็น operator แบบ admin/write ได้

CodeCopy code
[code]
    openclaw devices revoke --device <deviceId> --role node
[/code]

ส่งคืนผลการเพิกถอนเป็น JSON

## ตัวเลือกทั่วไป

  * `--url <url>`: URL WebSocket ของ Gateway (ค่าเริ่มต้นคือ `gateway.remote.url` เมื่อกำหนดค่าไว้)
  * `--token <token>`: โทเค็น Gateway (หากจำเป็น)
  * `--password <password>`: รหัสผ่าน Gateway (password auth)
  * `--timeout <ms>`: หมดเวลา RPC
  * `--json`: เอาต์พุต JSON (แนะนำสำหรับการเขียนสคริปต์)


## หมายเหตุ

  * การหมุนเวียนโทเค็นจะส่งคืนโทเค็นใหม่ (ข้อมูลอ่อนไหว) ให้จัดการเหมือน secret
  * คำสั่งเหล่านี้ต้องมี scope `operator.pairing` (หรือ `operator.admin`) การอนุมัติบางรายการ ยังต้องให้ผู้เรียกมี operator scopes ที่อุปกรณ์เป้าหมายจะ mint หรือสืบทอดด้วย ดู [Operator scopes](</th/gateway/operator-scopes>)
  * `gateway.nodes.pairing.autoApproveCidrs` เป็นนโยบาย Gateway แบบ opt-in สำหรับ การจับคู่อุปกรณ์ node ใหม่เท่านั้น โดยไม่เปลี่ยนอำนาจอนุมัติของ CLI
  * การหมุนเวียนและเพิกถอนโทเค็นจะอยู่ภายในชุด role การจับคู่ที่ได้รับอนุมัติและ baseline scope ที่ได้รับอนุมัติสำหรับอุปกรณ์นั้น รายการโทเค็นแคชที่หลงเหลืออยู่ ไม่ให้สิทธิ์เป็นเป้าหมายการจัดการโทเค็น
  * สำหรับเซสชันโทเค็น paired-device การจัดการข้ามอุปกรณ์เป็นของแอดมินเท่านั้น: `remove`, `rotate` และ `revoke` ทำได้เฉพาะกับตนเอง เว้นแต่ผู้เรียกจะมี `operator.admin`
  * การเปลี่ยนแปลงโทเค็นยังถูกจำกัดด้วย caller-scope: เซสชันแบบ pairing-only ไม่สามารถ หมุนเวียนหรือเพิกถอนโทเค็นที่มี `operator.admin` หรือ `operator.write` อยู่ในปัจจุบันได้
  * `devices clear` ถูก gate ด้วย `--yes` โดยเจตนา
  * หาก pairing scope ใช้ไม่ได้บน local loopback (และไม่ได้ส่ง `--url` อย่างชัดเจน) list/approve สามารถใช้ local pairing fallback ได้
  * `devices approve` ต้องมี ID คำขอที่ชัดเจนก่อน mint โทเค็น การละเว้น `requestId` หรือส่ง `--latest` จะแสดงตัวอย่างเฉพาะคำขอล่าสุดที่รอดำเนินการเท่านั้น


## เช็กลิสต์การกู้คืน token drift

ใช้รายการนี้เมื่อ Control UI หรือไคลเอ็นต์อื่นล้มเหลวต่อเนื่องด้วย `AUTH_TOKEN_MISMATCH`, `AUTH_DEVICE_TOKEN_MISMATCH` หรือ `AUTH_SCOPE_MISMATCH`

  1. ยืนยันแหล่งที่มาของโทเค็น gateway ปัจจุบัน:

bashCopy code
[code]
    openclaw config get gateway.auth.token
[/code]

  2. แสดงรายการอุปกรณ์ที่จับคู่แล้วและระบุ id อุปกรณ์ที่ได้รับผลกระทบ:

bashCopy code
[code]
    openclaw devices list
[/code]

  3. หมุนเวียนโทเค็น operator สำหรับอุปกรณ์ที่ได้รับผลกระทบ:

bashCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator
[/code]

  4. หากการหมุนเวียนยังไม่พอ ให้ลบการจับคู่ที่เก่าแล้วอนุมัติอีกครั้ง:

bashCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices listopenclaw devices approve <requestId>
[/code]

  5. ลองเชื่อมต่อไคลเอ็นต์อีกครั้งด้วย shared token/password ปัจจุบัน


หมายเหตุ:

  * ลำดับความสำคัญ auth สำหรับการเชื่อมต่อใหม่ปกติคือ shared token/password ที่ระบุอย่างชัดเจนก่อน จากนั้น `deviceToken` ที่ระบุอย่างชัดเจน จากนั้นโทเค็นอุปกรณ์ที่จัดเก็บไว้ แล้วจึง bootstrap token
  * การกู้คืน `AUTH_TOKEN_MISMATCH` ที่เชื่อถือได้สามารถส่งทั้ง shared token และโทเค็นอุปกรณ์ที่จัดเก็บไว้พร้อมกันชั่วคราวสำหรับการลองใหม่ที่มีขอบเขตจำกัดหนึ่งครั้ง
  * `AUTH_SCOPE_MISMATCH` หมายความว่าโทเค็นอุปกรณ์ถูกรับรู้แล้ว แต่ไม่มีชุด scope ที่ร้องขอ ให้แก้สัญญาการอนุมัติ pairing/scope ก่อนเปลี่ยน shared gateway auth


ที่เกี่ยวข้อง:

  * [การแก้ไขปัญหา auth ของแดชบอร์ด](</th/web/dashboard#if-you-see-unauthorized-1008>)
  * [การแก้ไขปัญหา Gateway](</th/gateway/troubleshooting#dashboard-control-ui-connectivity>)


## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [Nodes](</th/nodes>)


Was this useful?YesNo