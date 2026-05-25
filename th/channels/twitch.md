---
title: Twitch
source_url: https://docs.openclaw.ai/th/channels/twitch
scraped_at: 2026-05-25
---

รองรับแชท Twitch ผ่านการเชื่อมต่อ IRC OpenClaw เชื่อมต่อในฐานะผู้ใช้ Twitch (บัญชีบอท) เพื่อรับและส่งข้อความในช่องต่างๆ

## Plugin ที่รวมมาด้วย

หากคุณใช้บิลด์เก่ากว่าหรือการติดตั้งแบบกำหนดเองที่ไม่รวม Twitch ให้ติดตั้งแพ็กเกจ npm โดยตรง:

### npm registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Local checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

ใช้แพ็กเกจเปล่าเพื่อติดตามแท็กรุ่นทางการปัจจุบัน ปักหมุดเวอร์ชันที่แน่นอน เฉพาะเมื่อคุณต้องการการติดตั้งที่ทำซ้ำได้เท่านั้น

รายละเอียด: [Plugins](</th/tools/plugin>)

## การตั้งค่าแบบรวดเร็ว (ผู้เริ่มต้น)

* ### ตรวจสอบว่า Plugin พร้อมใช้งาน

OpenClaw รุ่นแพ็กเกจปัจจุบันรวม Plugin นี้อยู่แล้ว การติดตั้งแบบเก่าหรือแบบกำหนดเองสามารถเพิ่มได้ด้วยคำสั่งข้างต้น

* ### สร้างบัญชีบอท Twitch

สร้างบัญชี Twitch แยกสำหรับบอท (หรือใช้บัญชีที่มีอยู่)

* ### สร้างข้อมูลประจำตัว

ใช้ [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * เลือก **Bot Token**
  * ตรวจสอบว่าเลือกสโคป `chat:read` และ `chat:write` แล้ว
  * คัดลอก **Client ID** และ **Access Token**


* ### ค้นหา ID ผู้ใช้ Twitch ของคุณ

ใช้ <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> เพื่อแปลงชื่อผู้ใช้เป็น ID ผู้ใช้ Twitch

* ### กำหนดค่าโทเค็น

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (บัญชีเริ่มต้นเท่านั้น)
  * หรือ config: `channels.twitch.accessToken`


หากตั้งค่าทั้งสองอย่าง config จะมีลำดับความสำคัญก่อน (env fallback ใช้กับบัญชีเริ่มต้นเท่านั้น)

* ### เริ่มต้น Gateway

เริ่มต้น Gateway ด้วยช่องที่กำหนดค่าไว้

การกำหนดค่าขั้นต่ำ:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## คืออะไร

  * ช่อง Twitch ที่ Gateway เป็นเจ้าของ
  * การกำหนดเส้นทางแบบกำหนดได้แน่นอน: การตอบกลับจะย้อนกลับไปที่ Twitch เสมอ
  * แต่ละบัญชีแมปกับคีย์เซสชันแยก `agent:<agentId>:twitch:<accountName>`
  * `username` คือบัญชีของบอท (ผู้ยืนยันตัวตน), `channel` คือห้องแชทที่จะเข้าร่วม


## การตั้งค่า (ละเอียด)

### สร้างข้อมูลประจำตัว

ใช้ [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * เลือก **Bot Token**
  * ตรวจสอบว่าเลือกสโคป `chat:read` และ `chat:write` แล้ว
  * คัดลอก **Client ID** และ **Access Token**


### กำหนดค่าบอท

### Env var (บัญชีเริ่มต้นเท่านั้น)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Config

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

หากตั้งค่าทั้ง env และ config ไว้ config จะมีลำดับความสำคัญก่อน

### การควบคุมการเข้าถึง (แนะนำ)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

แนะนำให้ใช้ `allowFrom` สำหรับรายการอนุญาตแบบเข้มงวด ใช้ `allowedRoles` แทนหากคุณต้องการการเข้าถึงตามบทบาท

**บทบาทที่ใช้ได้:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`

## การรีเฟรชโทเค็น (ไม่บังคับ)

โทเค็นจาก [Twitch Token Generator](<https://twitchtokengenerator.com/>) ไม่สามารถรีเฟรชโดยอัตโนมัติได้ - ให้สร้างใหม่เมื่อหมดอายุ

สำหรับการรีเฟรชโทเค็นอัตโนมัติ ให้สร้างแอปพลิเคชัน Twitch ของคุณเองที่ [Twitch Developer Console](<https://dev.twitch.tv/console>) และเพิ่มลงใน config:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

บอทจะรีเฟรชโทเค็นโดยอัตโนมัติก่อนหมดอายุและบันทึกเหตุการณ์รีเฟรชลงในล็อก

## การรองรับหลายบัญชี

ใช้ `channels.twitch.accounts` พร้อมโทเค็นแยกตามบัญชี ดู [การกำหนดค่า](</th/gateway/configuration>) สำหรับรูปแบบที่ใช้ร่วมกัน

ตัวอย่าง (บัญชีบอทหนึ่งบัญชีในสองช่อง):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## การควบคุมการเข้าถึง

### รายการอนุญาต ID ผู้ใช้ (ปลอดภัยที่สุด)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### ตามบทบาท

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` เป็นรายการอนุญาตแบบเข้มงวด เมื่อตั้งค่าแล้ว จะอนุญาตเฉพาะ ID ผู้ใช้เหล่านั้น หากคุณต้องการการเข้าถึงตามบทบาท ให้ไม่ต้องตั้งค่า `allowFrom` และกำหนดค่า `allowedRoles` แทน

### ปิดข้อกำหนด @mention

โดยค่าเริ่มต้น `requireMention` เป็น `true` หากต้องการปิดและตอบกลับทุกข้อความ:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## การแก้ปัญหา

ก่อนอื่น ให้รันคำสั่งวินิจฉัย:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

บอทไม่ตอบกลับข้อความ

  * **ตรวจสอบการควบคุมการเข้าถึง:** ตรวจสอบว่า ID ผู้ใช้ของคุณอยู่ใน `allowFrom` หรือเอา `allowFrom` ออกชั่วคราวแล้วตั้งค่า `allowedRoles: ["all"]` เพื่อทดสอบ
  * **ตรวจสอบว่าบอทอยู่ในช่อง:** บอทต้องเข้าร่วมช่องที่ระบุใน `channel`

ปัญหาเกี่ยวกับโทเค็น

"Failed to connect" หรือข้อผิดพลาดการยืนยันตัวตน:

  * ตรวจสอบว่า `accessToken` เป็นค่าโทเค็นการเข้าถึง OAuth (โดยทั่วไปขึ้นต้นด้วยคำนำหน้า `oauth:`)
  * ตรวจสอบว่าโทเค็นมีสโคป `chat:read` และ `chat:write`
  * หากใช้การรีเฟรชโทเค็น ให้ตรวจสอบว่าตั้งค่า `clientSecret` และ `refreshToken` แล้ว

การรีเฟรชโทเค็นไม่ทำงาน

ตรวจสอบล็อกสำหรับเหตุการณ์รีเฟรช:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

หากคุณเห็น "token refresh disabled (no refresh token)":

  * ตรวจสอบว่าให้ `clientSecret` แล้ว
  * ตรวจสอบว่าให้ `refreshToken` แล้ว


## Config

### การกำหนดค่าบัญชี

ชื่อผู้ใช้บอท

โทเค็นการเข้าถึง OAuth ที่มี `chat:read` และ `chat:write`

Twitch Client ID (จาก Token Generator หรือแอปของคุณ)

ช่องที่จะเข้าร่วม

เปิดใช้งานบัญชีนี้

ไม่บังคับ: สำหรับการรีเฟรชโทเค็นอัตโนมัติ

ไม่บังคับ: สำหรับการรีเฟรชโทเค็นอัตโนมัติ

การหมดอายุของโทเค็นเป็นวินาที

เวลาประทับที่ได้รับโทเค็น

รายการอนุญาต ID ผู้ใช้

ต้องมี @mention

### ตัวเลือกผู้ให้บริการ

  * `channels.twitch.enabled` \- เปิด/ปิดการเริ่มต้นช่อง
  * `channels.twitch.username` \- ชื่อผู้ใช้บอท (config บัญชีเดียวแบบย่อ)
  * `channels.twitch.accessToken` \- โทเค็นการเข้าถึง OAuth (config บัญชีเดียวแบบย่อ)
  * `channels.twitch.clientId` \- Twitch Client ID (config บัญชีเดียวแบบย่อ)
  * `channels.twitch.channel` \- ช่องที่จะเข้าร่วม (config บัญชีเดียวแบบย่อ)
  * `channels.twitch.accounts.<accountName>` \- config หลายบัญชี (ฟิลด์บัญชีทั้งหมดข้างต้น)


ตัวอย่างแบบเต็ม:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## การทำงานของเครื่องมือ

เอเจนต์สามารถเรียก `twitch` พร้อมการทำงาน:

  * `send` \- ส่งข้อความไปยังช่อง


ตัวอย่าง:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## ความปลอดภัยและการปฏิบัติการ

  * **ปฏิบัติต่อโทเค็นเหมือนรหัสผ่าน** — อย่าคอมมิตโทเค็นลงใน git
  * **ใช้การรีเฟรชโทเค็นอัตโนมัติ** สำหรับบอทที่ทำงานระยะยาว
  * **ใช้รายการอนุญาต ID ผู้ใช้** แทนชื่อผู้ใช้สำหรับการควบคุมการเข้าถึง
  * **ตรวจสอบล็อก** สำหรับเหตุการณ์รีเฟรชโทเค็นและสถานะการเชื่อมต่อ
  * **จำกัดสโคปโทเค็นให้น้อยที่สุด** — ขอเฉพาะ `chat:read` และ `chat:write`
  * **หากติดขัด** : รีสตาร์ท Gateway หลังจากยืนยันว่าไม่มีกระบวนการอื่นเป็นเจ้าของเซสชัน


## ขีดจำกัด

  * **500 อักขระ** ต่อข้อความ (แบ่งเป็นส่วนอัตโนมัติที่ขอบเขตคำ)
  * Markdown จะถูกตัดออกก่อนแบ่งเป็นส่วน
  * ไม่มีการจำกัดอัตรา (ใช้ขีดจำกัดอัตราในตัวของ Twitch)


## ที่เกี่ยวข้อง

  * [การกำหนดเส้นทางช่อง](</th/channels/channel-routing>) — การกำหนดเส้นทางเซสชันสำหรับข้อความ
  * [ภาพรวมช่อง](</th/channels>) — ช่องทั้งหมดที่รองรับ
  * [กลุ่ม](</th/channels/groups>) — พฤติกรรมแชทกลุ่มและการกำหนดให้ต้อง mention
  * [การจับคู่](</th/channels/pairing>) — การยืนยันตัวตน DM และโฟลว์การจับคู่
  * [ความปลอดภัย](</th/gateway/security>) — โมเดลการเข้าถึงและการเสริมความปลอดภัย


Was this useful?YesNo