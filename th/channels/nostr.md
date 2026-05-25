---
title: Nostr
source_url: https://docs.openclaw.ai/th/channels/nostr
scraped_at: 2026-05-25
---

**สถานะ:** Plugin ที่บันเดิลมาให้แบบไม่บังคับ (ปิดใช้งานโดยค่าเริ่มต้นจนกว่าจะกำหนดค่า)

Nostr เป็นโปรโตคอลแบบกระจายศูนย์สำหรับเครือข่ายสังคม ช่องทางนี้ทำให้ OpenClaw รับและตอบกลับข้อความโดยตรง (DMs) ที่เข้ารหัสผ่าน NIP-04 ได้

## Plugin ที่บันเดิลมา

รุ่น OpenClaw ปัจจุบันจัดส่ง Nostr เป็น Plugin ที่บันเดิลมาให้ ดังนั้นบิลด์แบบแพ็กเกจปกติจึงไม่ต้องติดตั้งแยกต่างหาก

### การติดตั้งรุ่นเก่าหรือแบบกำหนดเอง

  * Onboarding (`openclaw onboard`) และ `openclaw channels add` ยังคงแสดง Nostr จากแคตตาล็อกช่องทางที่ใช้ร่วมกัน
  * หากบิลด์ของคุณไม่รวม Nostr ที่บันเดิลมา ให้ติดตั้งแพ็กเกจ npm โดยตรง

bashCopy code
[code]
    openclaw plugins install @openclaw/nostr
[/code]

ใช้แพ็กเกจแบบไม่ระบุเวอร์ชันเพื่อให้ตามแท็กรีลีสทางการปัจจุบัน ระบุเวอร์ชันแบบแน่นอนเฉพาะเมื่อคุณต้องการการติดตั้งที่ทำซ้ำได้

ใช้เช็กเอาต์ในเครื่อง (เวิร์กโฟลว์สำหรับพัฒนา):

bashCopy code
[code]
    openclaw plugins install --link <path-to-local-nostr-plugin>
[/code]

รีสตาร์ต Gateway หลังจากติดตั้งหรือเปิดใช้งาน Plugin

### การตั้งค่าแบบไม่โต้ตอบ

bashCopy code
[code]
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY" --relay-urls "wss://relay.damus.io,wss://relay.primal.net"
[/code]

ใช้ `--use-env` เพื่อเก็บ `NOSTR_PRIVATE_KEY` ไว้ในสภาพแวดล้อมแทนการจัดเก็บคีย์ใน config

## การตั้งค่าอย่างรวดเร็ว

  1. สร้างคู่คีย์ Nostr (หากจำเป็น):

bashCopy code
[code]
    # Using naknak key generate
[/code]

  2. เพิ่มลงใน config:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",    },  },}
[/code]

  3. ส่งออกคีย์:

bashCopy code
[code]
    export NOSTR_PRIVATE_KEY="nsec1..."
[/code]

  4. รีสตาร์ต Gateway


## ข้อมูลอ้างอิงการกำหนดค่า

คีย์ | ประเภท | ค่าเริ่มต้น | คำอธิบาย  
---|---|---|---  
`privateKey` | string | จำเป็น | คีย์ส่วนตัวในรูปแบบ `nsec` หรือ hex  
`relays` | string[] | `['wss://relay.damus.io', 'wss://nos.lol']` | URL ของรีเลย์ (WebSocket)  
`dmPolicy` | string | `pairing` | นโยบายการเข้าถึง DM  
`allowFrom` | string[] | `[]` | pubkey ของผู้ส่งที่อนุญาต  
`enabled` | boolean | `true` | เปิด/ปิดใช้งานช่องทาง  
`name` | string | - | ชื่อที่แสดง  
`profile` | object | - | เมทาดาทาโปรไฟล์ NIP-01  
  
## เมทาดาทาโปรไฟล์

ข้อมูลโปรไฟล์ถูกเผยแพร่เป็นอีเวนต์ NIP-01 `kind:0` คุณสามารถจัดการได้จาก Control UI (Channels -> Nostr -> Profile) หรือตั้งค่าโดยตรงใน config

ตัวอย่าง:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      profile: {        name: "openclaw",        displayName: "OpenClaw",        about: "Personal assistant DM bot",        picture: "https://example.com/avatar.png",        banner: "https://example.com/banner.png",        website: "https://example.com",        nip05: "openclaw@example.com",        lud16: "openclaw@example.com",      },    },  },}
[/code]

หมายเหตุ:

  * URL โปรไฟล์ต้องใช้ `https://`
  * การนำเข้าจากรีเลย์จะผสานฟิลด์และคงการแทนที่ในเครื่องไว้


## การควบคุมการเข้าถึง

### นโยบาย DM

  * **pairing** (ค่าเริ่มต้น): ผู้ส่งที่ไม่รู้จักจะได้รับโค้ดจับคู่
  * **allowlist** : เฉพาะ pubkey ใน `allowFrom` เท่านั้นที่ส่ง DM ได้
  * **open** : DM ขาเข้าสาธารณะ (ต้องใช้ `allowFrom: ["*"]`)
  * **disabled** : ไม่สนใจ DM ขาเข้า


หมายเหตุการบังคับใช้:

  * ลายเซ็นอีเวนต์ขาเข้าจะถูกตรวจสอบก่อนนโยบายผู้ส่งและการถอดรหัส NIP-04 ดังนั้นอีเวนต์ปลอมจะถูกปฏิเสธตั้งแต่ต้น
  * การตอบกลับการจับคู่จะถูกส่งโดยไม่ประมวลผลเนื้อหา DM เดิม
  * DM ขาเข้าถูกจำกัดอัตรา และเพย์โหลดที่มีขนาดใหญ่เกินไปจะถูกทิ้งก่อนถอดรหัส


### ตัวอย่าง allowlist

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      dmPolicy: "allowlist",      allowFrom: ["npub1abc...", "npub1xyz..."],    },  },}
[/code]

## รูปแบบคีย์

รูปแบบที่ยอมรับ:

  * **คีย์ส่วนตัว:** `nsec...` หรือ hex 64 อักขระ
  * **Pubkeys (`allowFrom`):** `npub...` หรือ hex


## รีเลย์

ค่าเริ่มต้น: `relay.damus.io` และ `nos.lol`

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["wss://relay.damus.io", "wss://relay.primal.net", "wss://nostr.wine"],    },  },}
[/code]

เคล็ดลับ:

  * ใช้รีเลย์ 2-3 รายการเพื่อความซ้ำซ้อน
  * หลีกเลี่ยงการใช้รีเลย์มากเกินไป (เวลาแฝง, การซ้ำซ้อน)
  * รีเลย์แบบชำระเงินสามารถเพิ่มความน่าเชื่อถือได้
  * รีเลย์ในเครื่องใช้ทดสอบได้ (`ws://localhost:7777`)


## การรองรับโปรโตคอล

NIP | สถานะ | คำอธิบาย  
---|---|---  
NIP-01 | รองรับ | รูปแบบอีเวนต์พื้นฐาน + เมทาดาทาโปรไฟล์  
NIP-04 | รองรับ | DM ที่เข้ารหัส (`kind:4`)  
NIP-17 | วางแผนไว้ | DM แบบ gift-wrapped  
NIP-44 | วางแผนไว้ | การเข้ารหัสแบบมีเวอร์ชัน  
  
## การทดสอบ

### รีเลย์ในเครื่อง

bashCopy code
[code]
    # Start strfrydocker run -p 7777:7777 ghcr.io/hoytech/strfry
[/code]

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["ws://localhost:7777"],    },  },}
[/code]

### การทดสอบด้วยตนเอง

  1. จด pubkey (npub) ของบอทจากบันทึก
  2. เปิดไคลเอนต์ Nostr (Damus, Amethyst ฯลฯ)
  3. ส่ง DM ไปยัง pubkey ของบอท
  4. ตรวจสอบการตอบกลับ


## การแก้ไขปัญหา

### ไม่ได้รับข้อความ

  * ตรวจสอบว่าคีย์ส่วนตัวถูกต้อง
  * ตรวจสอบให้แน่ใจว่า URL รีเลย์เข้าถึงได้และใช้ `wss://` (หรือ `ws://` สำหรับในเครื่อง)
  * ยืนยันว่า `enabled` ไม่ใช่ `false`
  * ตรวจสอบบันทึก Gateway สำหรับข้อผิดพลาดการเชื่อมต่อรีเลย์


### ไม่ส่งการตอบกลับ

  * ตรวจสอบว่ารีเลย์ยอมรับการเขียน
  * ตรวจสอบการเชื่อมต่อขาออก
  * เฝ้าดูขีดจำกัดอัตราของรีเลย์


### การตอบกลับซ้ำ

  * เป็นสิ่งที่คาดได้เมื่อใช้รีเลย์หลายรายการ
  * ข้อความจะถูกขจัดรายการซ้ำด้วย ID อีเวนต์ เฉพาะการส่งมอบครั้งแรกเท่านั้นที่กระตุ้นการตอบกลับ


## ความปลอดภัย

  * อย่า commit คีย์ส่วนตัว
  * ใช้ตัวแปรสภาพแวดล้อมสำหรับคีย์
  * พิจารณาใช้ `allowlist` สำหรับบอทในการใช้งานจริง
  * ลายเซ็นจะถูกตรวจสอบก่อนนโยบายผู้ส่ง และนโยบายผู้ส่งจะถูกบังคับใช้ก่อนถอดรหัส ดังนั้นอีเวนต์ปลอมจะถูกปฏิเสธตั้งแต่ต้น และผู้ส่งที่ไม่รู้จักไม่สามารถบังคับให้ทำงานเข้ารหัสเต็มรูปแบบได้


## ข้อจำกัด (MVP)

  * เฉพาะข้อความโดยตรงเท่านั้น (ไม่มีแชทกลุ่ม)
  * ไม่มีไฟล์แนบสื่อ
  * เฉพาะ NIP-04 เท่านั้น (วางแผน NIP-17 gift-wrap ไว้)


## ที่เกี่ยวข้อง

  * [ภาพรวมช่องทาง](</th/channels>) — ช่องทางที่รองรับทั้งหมด
  * [การจับคู่](</th/channels/pairing>) — การยืนยันตัวตน DM และโฟลว์การจับคู่
  * [กลุ่ม](</th/channels/groups>) — พฤติกรรมแชทกลุ่มและการควบคุมด้วยการกล่าวถึง
  * [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>) — การกำหนดเส้นทางเซสชันสำหรับข้อความ
  * [ความปลอดภัย](</th/gateway/security>) — โมเดลการเข้าถึงและการเสริมความแข็งแกร่ง


Was this useful?YesNo