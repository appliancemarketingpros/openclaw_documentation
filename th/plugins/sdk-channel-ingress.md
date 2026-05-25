---
title: API ขาเข้าของช่องทาง
source_url: https://docs.openclaw.ai/th/plugins/sdk-channel-ingress
scraped_at: 2026-05-25
---

# API ทางเข้าของช่องทาง

ทางเข้าของช่องทางคือขอบเขตการควบคุมการเข้าถึงแบบทดลองสำหรับเหตุการณ์ช่องทางขาเข้า ใช้ `openclaw/plugin-sdk/channel-ingress-runtime` สำหรับเส้นทางการรับเข้า พาธย่อย `openclaw/plugin-sdk/channel-ingress` รุ่นเก่ายังคงถูกส่งออกเป็น facade ความเข้ากันได้ที่เลิกแนะนำแล้วสำหรับ Plugin ภายนอก

Plugin เป็นเจ้าของข้อเท็จจริงของแพลตฟอร์มและ side effect แกนหลักเป็นเจ้าของนโยบายทั่วไป: รายการอนุญาต DM/กลุ่ม, รายการ DM ใน pairing-store, เกตเส้นทาง, เกตคำสั่ง, การยืนยันสิทธิ์เหตุการณ์, การเปิดใช้งานด้วยการกล่าวถึง, diagnostics ที่ปกปิดข้อมูลแล้ว และการรับเข้า

## ตัวแก้ค่าในรันไทม์

tsCopy code
[code]
       defineStableChannelIngressIdentity,  resolveChannelMessageIngress,} from "openclaw/plugin-sdk/channel-ingress-runtime"; const identity = defineStableChannelIngressIdentity({  key: "platform-user-id",  normalize: normalizePlatformUserId,  sensitivity: "pii",}); const result = await resolveChannelMessageIngress({  channelId: "my-channel",  accountId,  identity,  subject: { stableId: platformUserId },  conversation: { kind: isGroup ? "group" : "direct", id: conversationId },  event: { kind: "message", authMode: "inbound", mayPair: !isGroup },  policy: {    dmPolicy: config.dmPolicy,    groupPolicy: config.groupPolicy,    groupAllowFromFallbackToAllowFrom: true,  },  allowFrom: config.allowFrom,  groupAllowFrom: config.groupAllowFrom,  accessGroups: cfg.accessGroups,  route,  readStoreAllowFrom,  command: hasControlCommand ? { allowTextCommands: true, hasControlCommand } : undefined,});
[/code]

อย่าคำนวณรายการอนุญาตที่มีผลจริง เจ้าของคำสั่ง หรือกลุ่มคำสั่งไว้ล่วงหน้า ตัวแก้ค่าจะอนุมานสิ่งเหล่านั้นจากรายการอนุญาตดิบ, callback ของ store, descriptor เส้นทาง, กลุ่มการเข้าถึง, นโยบาย และชนิดของบทสนทนา

## ผลลัพธ์

Plugin ที่บันเดิลมาควรใช้ projection สมัยใหม่โดยตรง:

  * `ingress`: การตัดสินใจของเกตแบบเรียงลำดับและการรับเข้า
  * `senderAccess`: การอนุญาตผู้ส่ง/บทสนทนาเท่านั้น
  * `routeAccess`: projection ของเส้นทางและผู้ส่งของเส้นทาง
  * `commandAccess`: การอนุญาตคำสั่ง; เป็น false เมื่อไม่มีเกตคำสั่งทำงาน
  * `activationAccess`: ผลลัพธ์การกล่าวถึง/การเปิดใช้งาน


การอนุญาตเหตุการณ์ยังคงมีอยู่บน `ingress.graph` แบบเรียงลำดับและ `ingress.reasonCode` ที่เป็นตัวตัดสิน; ไม่มีการปล่อย projection ของเหตุการณ์แยกต่างหาก

ตัวช่วย SDK ภายนอกที่เลิกแนะนำแล้วอาจสร้างรูปทรงเก่าขึ้นใหม่ภายใน เส้นทางรับเข้าที่บันเดิลมาใหม่ไม่ควรแปลงผลลัพธ์สมัยใหม่กลับเป็น DTO ภายในเครื่อง

## กลุ่มการเข้าถึง

รายการ `accessGroup:<name>` ยังคงถูกปกปิดข้อมูล แกนหลักแก้ค่ากลุ่ม `message.senders` แบบสแตติกเอง และเรียก `resolveAccessGroupMembership` เฉพาะสำหรับกลุ่มแบบไดนามิกที่ต้องค้นหาบนแพลตฟอร์ม กลุ่มที่ขาดหาย ไม่รองรับ หรือทำงานล้มเหลวจะล้มเหลวแบบปิด

## โหมดเหตุการณ์

`authMode` | ความหมาย  
---|---  
`inbound` | เกตผู้ส่งขาเข้าปกติ  
`command` | เกตคำสั่งสำหรับ callback หรือปุ่มที่มีขอบเขต  
`origin-subject` | ผู้กระทำต้องตรงกับ subject ของข้อความต้นฉบับ  
`route-only` | เกตเส้นทางเท่านั้นสำหรับเหตุการณ์ที่เชื่อถือได้ภายใต้ขอบเขตเส้นทาง  
`none` | เหตุการณ์ภายในที่ Plugin เป็นเจ้าของจะข้าม auth ที่ใช้ร่วมกัน  
  
ใช้ `mayPair: false` สำหรับ reaction, ปุ่ม, callback และคำสั่งเนทีฟ

## เส้นทางและการเปิดใช้งาน

ใช้ descriptor เส้นทางสำหรับนโยบายห้อง หัวข้อ guild เธรด หรือเส้นทางแบบซ้อน:

tsCopy code
[code]
    route: {  id: "room",  allowed: roomAllowed,  enabled: roomEnabled,  senderPolicy: "replace",  senderAllowFrom: roomAllowFrom,  blockReason: "room_sender_not_allowlisted",}
[/code]

ใช้ `channelIngressRoutes(...)` เมื่อ Plugin มี descriptor เส้นทางที่เป็นทางเลือกหลายรายการ; ฟังก์ชันนี้จะกรองกิ่งที่ปิดใช้งานออก ขณะยังคงข้อเท็จจริงของเส้นทางให้เป็นแบบทั่วไปและเรียงตาม `precedence` ของแต่ละ descriptor

การเกตการกล่าวถึงคือเกตการเปิดใช้งาน เมื่อไม่พบการกล่าวถึงจะคืนค่า `admission: "skip"` เพื่อให้ turn kernel ไม่ประมวลผล turn แบบ observe-only ช่องทางส่วนใหญ่ควรปล่อยให้การเปิดใช้งานอยู่หลังเกตผู้ส่งและเกตคำสั่ง พื้นที่แชตสาธารณะที่ต้องทำให้ทราฟฟิกที่ไม่ได้ถูกกล่าวถึงเงียบลงก่อนเสียงรบกวนจากรายการอนุญาตของผู้ส่งสามารถเลือกใช้ `activation.order: "before-sender"` ได้เมื่อปิดใช้งานการข้ามด้วยคำสั่งข้อความ ช่องทางที่มีการเปิดใช้งานโดยนัย เช่น การตอบกลับในเธรดของบอต สามารถส่ง `activation.allowedImplicitMentionKinds`; จากนั้น `activationAccess.shouldBypassMention` ที่ถูก project จะรายงานเมื่อคำสั่งหรือการเปิดใช้งานโดยนัยข้ามการกล่าวถึงอย่างชัดเจน

## การปกปิดข้อมูล

ค่าผู้ส่งดิบและรายการอนุญาตดิบเป็นเพียงอินพุตของตัวแก้ค่าเท่านั้น ค่าเหล่านี้ต้องไม่ปรากฏในสถานะที่แก้ค่าแล้ว การตัดสินใจ diagnostics snapshot หรือข้อเท็จจริงความเข้ากันได้ ใช้ id ของ subject แบบทึบ, id ของรายการ, id ของเส้นทาง และ id ของ diagnostic

## การตรวจสอบ

bashCopy code
[code]
    pnpm test src/channels/message-access/message-access.test.ts src/plugin-sdk/channel-ingress-runtime.test.tspnpm plugin-sdk:api:check
[/code]

Was this useful?YesNo