---
title: IPC บน macOS
source_url: https://docs.openclaw.ai/th/platforms/mac/xpc
scraped_at: 2026-05-25
---

# สถาปัตยกรรม IPC ของ OpenClaw บน macOS

**โมเดลปัจจุบัน:** local Unix socket ใช้เชื่อมต่อระหว่าง **บริการ node host** กับ **แอป macOS** สำหรับ exec approvals + `system.run` มี debug CLI ชื่อ `openclaw-mac` สำหรับการตรวจสอบการค้นพบ/การเชื่อมต่อ; ส่วน agent actions ยังคงไหลผ่าน Gateway WebSocket และ `node.invoke` การทำ UI automation ใช้ PeekabooBridge

## เป้าหมาย

  * แอป GUI อินสแตนซ์เดียวที่เป็นเจ้าของงานทั้งหมดที่เกี่ยวข้องกับ TCC (การแจ้งเตือน, การบันทึกหน้าจอ, ไมโครโฟน, เสียงพูด, AppleScript)
  * พื้นผิวขนาดเล็กสำหรับระบบอัตโนมัติ: Gateway + คำสั่ง node และ PeekabooBridge สำหรับ UI automation
  * สิทธิ์การเข้าถึงที่คาดเดาได้: ใช้ signed bundle ID เดิมเสมอ เปิดโดย launchd เพื่อให้สิทธิ์ TCC คงอยู่


## วิธีการทำงาน

### Gateway + การขนส่งของ node

  * แอปรัน Gateway (local mode) และเชื่อมต่อเข้ากับมันในฐานะ node
  * agent actions จะถูกดำเนินการผ่าน `node.invoke` (เช่น `system.run`, `system.notify`, `canvas.*`)


### บริการ node + IPC ของแอป

  * บริการ node host แบบ headless จะเชื่อมต่อกับ Gateway WebSocket
  * คำขอ `system.run` จะถูกส่งต่อไปยังแอป macOS ผ่าน local Unix socket
  * แอปจะทำ exec ในบริบท UI ถามยืนยันหากจำเป็น แล้วส่งผลลัพธ์กลับมา


แผนภาพ (SCI):

CodeCopy code
[code]
    Agent -> Gateway -> Node Service (WS)                      |  IPC (UDS + token + HMAC + TTL)                      v                  Mac App (UI + TCC + system.run)
[/code]

### PeekabooBridge (UI automation)

  * UI automation ใช้ UNIX socket แยกชื่อ `bridge.sock` และใช้โปรโตคอล JSON ของ PeekabooBridge
  * ลำดับความชอบของโฮสต์ (ฝั่งไคลเอนต์): Peekaboo.app → Claude.app → OpenClaw.app → การรันในเครื่อง
  * ความปลอดภัย: bridge hosts ต้องมี TeamID ที่ได้รับอนุญาต; ช่องทางหลบแบบ same-UID สำหรับ DEBUG-only ถูกป้องกันด้วย `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (ธรรมเนียมของ Peekaboo)
  * ดู: [การใช้งาน PeekabooBridge](</th/platforms/mac/peekaboo>) สำหรับรายละเอียด


## โฟลว์การปฏิบัติงาน

  * รีสตาร์ต/สร้างใหม่: `SIGN_IDENTITY="Apple Development: &lt;Developer Name&gt; (&lt;TEAMID&gt;)" scripts/restart-mac.sh`
    * kill อินสแตนซ์ที่มีอยู่
    * Swift build + package
    * เขียน/bootstrap/kickstart LaunchAgent
  * อินสแตนซ์เดียว: แอปจะออกทันทีหากมีอีกอินสแตนซ์หนึ่งที่ใช้ bundle ID เดียวกันกำลังทำงานอยู่


## หมายเหตุด้านการเสริมความปลอดภัย

  * ควรกำหนดให้ต้องมี TeamID ตรงกันสำหรับทุกพื้นผิวที่มีสิทธิ์สูง
  * PeekabooBridge: `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (DEBUG-only) อาจอนุญาตให้ผู้เรียกแบบ same-UID ใช้งานได้สำหรับการพัฒนาในเครื่อง
  * การสื่อสารทั้งหมดยังคงเป็น local-only; ไม่มี network sockets ถูกเปิดออก
  * พรอมป์ต์ TCC จะมาจาก GUI app bundle เท่านั้น; ให้คง signed bundle ID ให้เสถียรระหว่างการ rebuild
  * การเสริมความปลอดภัยของ IPC: socket mode `0600`, token, การตรวจ peer-UID, HMAC challenge/response, TTL สั้น


## ที่เกี่ยวข้อง

  * [macOS app](</th/platforms/macos>)
  * [โฟลว์ IPC บน macOS (Exec approvals)](</th/tools/exec-approvals-advanced#macos-ipc-flow>)


Was this useful?YesNo