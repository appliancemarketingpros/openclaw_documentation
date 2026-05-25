---
title: Feishu
source_url: https://docs.openclaw.ai/th/channels/feishu
scraped_at: 2026-05-25
---

Feishu/Lark เป็นแพลตฟอร์มการทำงานร่วมกันแบบครบวงจรที่ทีมใช้แชต แชร์เอกสาร จัดการปฏิทิน และทำงานร่วมกันให้เสร็จได้

**สถานะ:** พร้อมใช้งานจริงสำหรับ DM ของบอต + แชตกลุ่ม WebSocket เป็นโหมดเริ่มต้น; โหมด Webhook เป็นตัวเลือก

* * *

## เริ่มต้นอย่างรวดเร็ว

* ### รันตัวช่วยตั้งค่าช่องทาง

bashCopy code
[code]
    openclaw channels login --channel feishu
[/code]

เลือกการตั้งค่าแบบแมนนวลเพื่อวาง App ID และ App Secret จาก Feishu Open Platform หรือเลือกการตั้งค่าด้วย QR เพื่อสร้างบอตโดยอัตโนมัติ หากแอปมือถือ Feishu ในประเทศไม่ตอบสนองต่อโค้ด QR ให้รันการตั้งค่าอีกครั้งแล้วเลือกการตั้งค่าแบบแมนนวล

* ### หลังจากตั้งค่าเสร็จแล้ว ให้รีสตาร์ท Gateway เพื่อใช้การเปลี่ยนแปลง

bashCopy code
[code]
    openclaw gateway restart
[/code]

* * *

## การควบคุมการเข้าถึง

### ข้อความโดยตรง

กำหนดค่า `dmPolicy` เพื่อควบคุมว่าใครสามารถ DM บอตได้:

  * `"pairing"` \- ผู้ใช้ที่ไม่รู้จักจะได้รับโค้ดจับคู่; อนุมัติผ่าน CLI
  * `"allowlist"` \- เฉพาะผู้ใช้ที่อยู่ใน `allowFrom` เท่านั้นที่แชตได้ (ค่าเริ่มต้น: เจ้าของบอตเท่านั้น)
  * `"open"` \- อนุญาต DM สาธารณะเฉพาะเมื่อ `allowFrom` มี `"*"`; หากมีรายการจำกัด เฉพาะผู้ใช้ที่ตรงกันเท่านั้นที่แชตได้
  * `"disabled"` \- ปิดใช้งาน DM ทั้งหมด


**อนุมัติคำขอจับคู่:**

bashCopy code
[code]
    openclaw pairing list feishuopenclaw pairing approve feishu &lt;CODE&gt;
[/code]

### แชตกลุ่ม

**นโยบายกลุ่ม** (`channels.feishu.groupPolicy`):

ค่า | พฤติกรรม  
---|---  
`"open"` | ตอบกลับทุกข้อความในกลุ่ม  
`"allowlist"` | ตอบกลับเฉพาะกลุ่มใน `groupAllowFrom` หรือที่กำหนดค่าไว้อย่างชัดเจนภายใต้ `groups.<chat_id>`  
`"disabled"` | ปิดใช้งานข้อความกลุ่มทั้งหมด; รายการ `groups.<chat_id>` ที่ระบุชัดเจนจะไม่แทนที่ค่านี้  
  
ค่าเริ่มต้น: `allowlist`

**ข้อกำหนดการกล่าวถึง** (`channels.feishu.requireMention`):

  * `true` \- ต้อง @mention (ค่าเริ่มต้น)
  * `false` \- ตอบกลับโดยไม่ต้อง @mention
  * การแทนที่รายกลุ่ม: `channels.feishu.groups.<chat_id>.requireMention`
  * `@all` และ `@_all` สำหรับประกาศถึงทุกคนเท่านั้น จะไม่ถือเป็นการกล่าวถึงบอต ข้อความที่กล่าวถึงทั้ง `@all` และบอตโดยตรงยังคงนับเป็นการกล่าวถึงบอต


* * *

## ตัวอย่างการกำหนดค่ากลุ่ม

### อนุญาตทุกกลุ่ม โดยไม่ต้อง @mention

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "open",    },  },}
[/code]

### อนุญาตทุกกลุ่ม แต่ยังต้อง @mention

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "open",      requireMention: true,    },  },}
[/code]

### อนุญาตเฉพาะบางกลุ่มเท่านั้น

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      // Group IDs look like: oc_xxx      groupAllowFrom: ["oc_xxx", "oc_yyy"],    },  },}
[/code]

ในโหมด `allowlist` คุณยังสามารถอนุญาตกลุ่มได้โดยเพิ่มรายการ `groups.<chat_id>` อย่างชัดเจน รายการที่ระบุชัดเจนจะไม่แทนที่ `groupPolicy: "disabled"` ค่าเริ่มต้นแบบไวลด์การ์ดภายใต้ `groups.*` ใช้กำหนดค่ากลุ่มที่ตรงกัน แต่จะไม่อนุญาตกลุ่มด้วยตัวเอง

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      groups: {        oc_xxx: {          requireMention: false,        },      },    },  },}
[/code]

### จำกัดผู้ส่งภายในกลุ่ม

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      groupAllowFrom: ["oc_xxx"],      groups: {        oc_xxx: {          // User open_ids look like: ou_xxx          allowFrom: ["ou_user1", "ou_user2"],        },      },    },  },}
[/code]

* * *

## รับ ID ของกลุ่ม/ผู้ใช้

### ID ของกลุ่ม (`chat_id`, รูปแบบ: `oc_xxx`)

เปิดกลุ่มใน Feishu/Lark คลิกไอคอนเมนูที่มุมขวาบน แล้วไปที่ **การตั้งค่า** ID ของกลุ่ม (`chat_id`) จะแสดงอยู่ในหน้าการตั้งค่า

![รับ ID ของกลุ่ม](/images/feishu-get-group-id.png)

### ID ของผู้ใช้ (`open_id`, รูปแบบ: `ou_xxx`)

เริ่ม Gateway ส่ง DM ไปยังบอต แล้วตรวจสอบบันทึก:

bashCopy code
[code]
    openclaw logs --follow
[/code]

มองหา `open_id` ในผลลัพธ์บันทึก คุณยังสามารถตรวจสอบคำขอจับคู่ที่รอดำเนินการได้:

bashCopy code
[code]
    openclaw pairing list feishu
[/code]

* * *

## คำสั่งทั่วไป

คำสั่ง | คำอธิบาย  
---|---  
`/status` | แสดงสถานะบอต  
`/reset` | รีเซ็ตเซสชันปัจจุบัน  
`/model` | แสดงหรือสลับโมเดล AI  
  
* * *

## การแก้ไขปัญหา

### บอตไม่ตอบกลับในแชตกลุ่ม

  1. ตรวจสอบให้แน่ใจว่าเพิ่มบอตเข้าไปในกลุ่มแล้ว
  2. ตรวจสอบให้แน่ใจว่าคุณ @mention บอต (จำเป็นตามค่าเริ่มต้น)
  3. ตรวจสอบว่า `groupPolicy` ไม่ใช่ `"disabled"`
  4. ตรวจสอบบันทึก: `openclaw logs --follow`


### บอตไม่ได้รับข้อความ

  1. ตรวจสอบให้แน่ใจว่าบอตเผยแพร่และได้รับการอนุมัติใน Feishu Open Platform / Lark Developer แล้ว
  2. ตรวจสอบให้แน่ใจว่าการสมัครรับเหตุการณ์มี `im.message.receive_v1`
  3. ตรวจสอบให้แน่ใจว่าเลือก **persistent connection** (WebSocket) แล้ว
  4. ตรวจสอบให้แน่ใจว่าอนุญาตขอบเขตสิทธิ์ที่จำเป็นทั้งหมดแล้ว
  5. ตรวจสอบให้แน่ใจว่า Gateway กำลังทำงาน: `openclaw gateway status`
  6. ตรวจสอบบันทึก: `openclaw logs --follow`


### การตั้งค่าด้วย QR ไม่ตอบสนองในแอปมือถือ Feishu

  1. รันการตั้งค่าอีกครั้ง: `openclaw channels login --channel feishu`
  2. เลือกการตั้งค่าแบบแมนนวล
  3. ใน Feishu Open Platform ให้สร้างแอปที่สร้างเองและคัดลอก App ID กับ App Secret
  4. วางข้อมูลรับรองเหล่านั้นลงในตัวช่วยตั้งค่า


### App Secret รั่วไหล

  1. รีเซ็ต App Secret ใน Feishu Open Platform / Lark Developer
  2. อัปเดตค่าใน config ของคุณ
  3. รีสตาร์ท Gateway: `openclaw gateway restart`


* * *

## การกำหนดค่าขั้นสูง

### หลายบัญชี

json5Copy code
[code]
    {  channels: {    feishu: {      defaultAccount: "main",      accounts: {        main: {          appId: "cli_xxx",          appSecret: "xxx",          name: "Primary bot",          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },        backup: {          appId: "cli_yyy",          appSecret: "yyy",          name: "Backup bot",          enabled: false,        },      },    },  },}
[/code]

`defaultAccount` ควบคุมว่าจะใช้บัญชีใดเมื่อ API ขาออกไม่ได้ระบุ `accountId` `accounts.<id>.tts` ใช้โครงสร้างเดียวกับ `messages.tts` และ deep-merge ทับ config TTS ส่วนกลาง ดังนั้นการตั้งค่า Feishu แบบหลายบอตจึงสามารถเก็บข้อมูลรับรอง provider ที่ใช้ร่วมกันไว้ส่วนกลาง พร้อมแทนที่เฉพาะเสียง โมเดล persona หรือโหมดอัตโนมัติ แยกตามบัญชีได้

### ขีดจำกัดข้อความ

  * `textChunkLimit` \- ขนาดชิ้นข้อความขาออก (ค่าเริ่มต้น: `2000` อักขระ)
  * `mediaMaxMb` \- ขีดจำกัดการอัปโหลด/ดาวน์โหลดสื่อ (ค่าเริ่มต้น: `30` MB)


### การสตรีม

Feishu/Lark รองรับการตอบกลับแบบสตรีมผ่านการ์ดแบบโต้ตอบ เมื่อเปิดใช้งาน บอตจะอัปเดตการ์ดแบบเรียลไทม์ขณะสร้างข้อความ

json5Copy code
[code]
    {  channels: {    feishu: {      streaming: true, // enable streaming card output (default: true)      blockStreaming: true, // opt into completed-block streaming    },  },}
[/code]

ตั้งค่า `streaming: false` เพื่อส่งคำตอบทั้งหมดในข้อความเดียว `blockStreaming` ปิดอยู่ตามค่าเริ่มต้น; เปิดใช้งานเฉพาะเมื่อคุณต้องการให้บล็อกของผู้ช่วยที่เสร็จแล้วถูกส่งออกก่อนคำตอบสุดท้าย

### การปรับโควตาให้เหมาะสม

ลดจำนวนการเรียก API ของ Feishu/Lark ด้วยแฟล็กเสริมสองรายการ:

  * `typingIndicator` (ค่าเริ่มต้น `true`): ตั้งค่า `false` เพื่อข้ามการเรียกปฏิกิริยาการพิมพ์
  * `resolveSenderNames` (ค่าเริ่มต้น `true`): ตั้งค่า `false` เพื่อข้ามการค้นหาโปรไฟล์ผู้ส่ง

json5Copy code
[code]
    {  channels: {    feishu: {      typingIndicator: false,      resolveSenderNames: false,    },  },}
[/code]

### เซสชัน ACP

Feishu/Lark รองรับ ACP สำหรับ DM และข้อความเธรดกลุ่ม ACP ของ Feishu/Lark ขับเคลื่อนด้วยคำสั่งข้อความ - ไม่มีเมนูคำสั่งแบบสแลชดั้งเดิม ดังนั้นให้ใช้ข้อความ `/acp ...` โดยตรงในการสนทนา

#### การผูก ACP แบบถาวร

json5Copy code
[code]
    {  agents: {    list: [      {        id: "codex",        runtime: {          type: "acp",          acp: {            agent: "codex",            backend: "acpx",            mode: "persistent",            cwd: "/workspace/openclaw",          },        },      },    ],  },  bindings: [    {      type: "acp",      agentId: "codex",      match: {        channel: "feishu",        accountId: "default",        peer: { kind: "direct", id: "ou_1234567890" },      },    },    {      type: "acp",      agentId: "codex",      match: {        channel: "feishu",        accountId: "default",        peer: { kind: "group", id: "oc_group_chat:topic:om_topic_root" },      },      acp: { label: "codex-feishu-topic" },    },  ],}
[/code]

#### สร้าง ACP จากแชต

ใน DM หรือเธรดของ Feishu/Lark:

textCopy code
[code]
    /acp spawn codex --thread here
[/code]

`--thread here` ใช้ได้กับ DM และข้อความเธรดของ Feishu/Lark ข้อความติดตามผลในการสนทนาที่ผูกไว้จะถูกส่งต่อไปยังเซสชัน ACP นั้นโดยตรง

### การกำหนดเส้นทางหลายเอเจนต์

ใช้ `bindings` เพื่อกำหนดเส้นทาง DM หรือกลุ่มของ Feishu/Lark ไปยังเอเจนต์ต่าง ๆ

json5Copy code
[code]
    {  agents: {    list: [      { id: "main" },      { id: "agent-a", workspace: "/home/user/agent-a" },      { id: "agent-b", workspace: "/home/user/agent-b" },    ],  },  bindings: [    {      agentId: "agent-a",      match: {        channel: "feishu",        peer: { kind: "direct", id: "ou_xxx" },      },    },    {      agentId: "agent-b",      match: {        channel: "feishu",        peer: { kind: "group", id: "oc_zzz" },      },    },  ],}
[/code]

ฟิลด์การกำหนดเส้นทาง:

  * `match.channel`: `"feishu"`
  * `match.peer.kind`: `"direct"` (DM) หรือ `"group"` (แชตกลุ่ม)
  * `match.peer.id`: Open ID ของผู้ใช้ (`ou_xxx`) หรือ ID ของกลุ่ม (`oc_xxx`)


ดู รับ ID ของกลุ่ม/ผู้ใช้ สำหรับเคล็ดลับการค้นหา

* * *

## อ้างอิงการกำหนดค่า

การกำหนดค่าแบบเต็ม: [การกำหนดค่า Gateway](</th/gateway/configuration>)

การตั้งค่า | คำอธิบาย | ค่าเริ่มต้น  
---|---|---  
`channels.feishu.enabled` | เปิด/ปิดใช้งานช่องทาง | `true`  
`channels.feishu.domain` | โดเมน API (`feishu` หรือ `lark`) | `feishu`  
`channels.feishu.connectionMode` | การส่งอีเวนต์ (`websocket` หรือ `webhook`) | `websocket`  
`channels.feishu.defaultAccount` | บัญชีเริ่มต้นสำหรับการกำหนดเส้นทางขาออก | `default`  
`channels.feishu.verificationToken` | จำเป็นสำหรับโหมด Webhook | -  
`channels.feishu.encryptKey` | จำเป็นสำหรับโหมด Webhook | -  
`channels.feishu.webhookPath` | พาธเส้นทาง Webhook | `/feishu/events`  
`channels.feishu.webhookHost` | โฮสต์สำหรับผูก Webhook | `127.0.0.1`  
`channels.feishu.webhookPort` | พอร์ตสำหรับผูก Webhook | `3000`  
`channels.feishu.accounts.<id>.appId` | App ID | -  
`channels.feishu.accounts.<id>.appSecret` | App Secret | -  
`channels.feishu.accounts.<id>.domain` | การเขียนทับโดเมนต่อบัญชี | `feishu`  
`channels.feishu.accounts.<id>.tts` | การเขียนทับ TTS ต่อบัญชี | `messages.tts`  
`channels.feishu.dmPolicy` | นโยบาย DM | `allowlist`  
`channels.feishu.allowFrom` | รายการอนุญาต DM (รายการ open_id) | [BotOwnerId]  
`channels.feishu.groupPolicy` | นโยบายกลุ่ม | `allowlist`  
`channels.feishu.groupAllowFrom` | รายการอนุญาตกลุ่ม | -  
`channels.feishu.requireMention` | กำหนดให้ @mention ในกลุ่ม | `true`  
`channels.feishu.groups.<chat_id>.requireMention` | การเขียนทับ @mention ต่อกลุ่ม; ID ที่ระบุชัดเจนยังอนุญาตให้กลุ่มเข้าได้ในโหมดรายการอนุญาต | inherited  
`channels.feishu.groups.<chat_id>.enabled` | เปิด/ปิดใช้งานกลุ่มเฉพาะ | `true`  
`channels.feishu.textChunkLimit` | ขนาดชิ้นส่วนข้อความ | `2000`  
`channels.feishu.mediaMaxMb` | ขีดจำกัดขนาดสื่อ | `30`  
`channels.feishu.streaming` | เอาต์พุตการ์ดแบบสตรีม | `true`  
`channels.feishu.blockStreaming` | การสตรีมการตอบกลับแบบบล็อกที่เสร็จสมบูรณ์ | `false`  
`channels.feishu.typingIndicator` | ส่งรีแอ็กชันการพิมพ์ | `true`  
`channels.feishu.resolveSenderNames` | แปลงชื่อที่แสดงของผู้ส่ง | `true`  
  
* * *

## ประเภทข้อความที่รองรับ

### รับ

  * ✅ ข้อความ
  * ✅ ข้อความแบบ Rich text (post)
  * ✅ รูปภาพ
  * ✅ ไฟล์
  * ✅ เสียง
  * ✅ วิดีโอ/สื่อ
  * ✅ สติกเกอร์


ข้อความเสียงขาเข้าของ Feishu/Lark จะถูกทำให้เป็นมาตรฐานเป็นตัวยึดตำแหน่งสื่อแทน JSON `file_key` ดิบ เมื่อกำหนดค่า `tools.media.audio` แล้ว OpenClaw จะดาวน์โหลดทรัพยากรบันทึกเสียงและเรียกใช้การถอดเสียงร่วมก่อนเทิร์นของ เอเจนต์ เพื่อให้เอเจนต์ได้รับข้อความถอดเสียงพูด หาก Feishu รวม ข้อความถอดเสียงไว้โดยตรงในเพย์โหลดเสียง ข้อความนั้นจะถูกใช้โดยไม่เรียก ASR อีกครั้ง หากไม่มีผู้ให้บริการถอดเสียง เอเจนต์จะยังได้รับ ตัวยึดตำแหน่ง `<media:audio>` พร้อมไฟล์แนบที่บันทึกไว้ ไม่ใช่เพย์โหลด ทรัพยากร Feishu ดิบ

### ส่ง

  * ✅ ข้อความ
  * ✅ รูปภาพ
  * ✅ ไฟล์
  * ✅ เสียง
  * ✅ วิดีโอ/สื่อ
  * ✅ การ์ดแบบอินเทอร์แอกทีฟ (รวมถึงการอัปเดตแบบสตรีม)
  * ⚠️ ข้อความแบบ Rich text (การจัดรูปแบบสไตล์ post; ไม่รองรับความสามารถการสร้างเนื้อหา Feishu/Lark แบบเต็ม)


บับเบิลเสียงแบบเนทีฟของ Feishu/Lark ใช้ประเภทข้อความ `audio` ของ Feishu และต้องใช้ สื่ออัปโหลด Ogg/Opus (`file_type: "opus"`) สื่อ `.opus` และ `.ogg` ที่มีอยู่ จะถูกส่งโดยตรงเป็นเสียงแบบเนทีฟ MP3/WAV/M4A และรูปแบบเสียงอื่นที่น่าจะเป็นเสียง จะถูกแปลงเป็น Ogg/Opus 48kHz ด้วย `ffmpeg` เฉพาะเมื่อการตอบกลับร้องขอการส่ง แบบเสียงพูด (`audioAsVoice` / เครื่องมือข้อความ `asVoice` รวมถึงการตอบกลับบันทึกเสียง TTS) ไฟล์แนบ MP3 ทั่วไปจะยังคงเป็นไฟล์ปกติ หากไม่มี `ffmpeg` หรือ การแปลงล้มเหลว OpenClaw จะถอยกลับไปใช้ไฟล์แนบและบันทึกเหตุผลลงล็อก

### เธรดและการตอบกลับ

  * ✅ การตอบกลับแบบอินไลน์
  * ✅ การตอบกลับในเธรด
  * ✅ การตอบกลับด้วยสื่อยังคงรับรู้เธรดเมื่อกำลังตอบกลับข้อความในเธรด


สำหรับ `groupSessionScope: "group_topic"` และ `"group_topic_sender"` กลุ่มหัวข้อ Feishu/Lark แบบเนทีฟจะใช้ `thread_id` (`omt_*`) ของอีเวนต์เป็นคีย์เซสชัน หัวข้อแบบมาตรฐาน หากอีเวนต์เริ่มต้นหัวข้อแบบเนทีฟละเว้น `thread_id` OpenClaw จะเติมข้อมูลจาก Feishu ก่อนกำหนดเส้นทางเทิร์น การตอบกลับกลุ่มปกติที่ OpenClaw แปลงเป็นเธรดจะยังคงใช้ ID ข้อความรากของการตอบกลับ (`om_*`) เพื่อให้ เทิร์นแรกและเทิร์นติดตามอยู่ในเซสชันเดียวกัน

* * *

## ที่เกี่ยวข้อง

  * [ภาพรวมช่องทาง](</th/channels>) \- ช่องทางที่รองรับทั้งหมด
  * [การจับคู่](</th/channels/pairing>) \- การยืนยันตัวตนและโฟลว์การจับคู่ผ่าน DM
  * [กลุ่ม](</th/channels/groups>) \- พฤติกรรมแชตกลุ่มและการกั้นด้วยการกล่าวถึง
  * [การกำหนดเส้นทางช่องทาง](</th/channels/channel-routing>) \- การกำหนดเส้นทางเซสชันสำหรับข้อความ
  * [ความปลอดภัย](</th/gateway/security>) \- โมเดลการเข้าถึงและการเสริมความแข็งแกร่ง


Was this useful?YesNo