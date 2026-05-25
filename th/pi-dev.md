---
title: เวิร์กโฟลว์การพัฒนา Pi
source_url: https://docs.openclaw.ai/th/pi-dev
scraped_at: 2026-05-25
---

เวิร์กโฟลว์ที่สมเหตุสมผลสำหรับการทำงานกับการผสานรวม Pi ใน OpenClaw

## การตรวจชนิดและการลินต์

  * เกตภายในเครื่องค่าเริ่มต้น: `pnpm check`
  * เกตการบิลด์: `pnpm build` เมื่อการเปลี่ยนแปลงอาจส่งผลต่อเอาต์พุตการบิลด์ การแพ็กเกจ หรือขอบเขตของ lazy-loading/module
  * เกตเต็มก่อนนำการเปลี่ยนแปลงขึ้นสำหรับการเปลี่ยนแปลงที่เกี่ยวกับ Pi เป็นหลัก: `pnpm check && pnpm test`


## การรันทดสอบ Pi

รันชุดทดสอบที่เน้น Pi โดยตรงด้วย Vitest:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

เมื่อต้องการรวมการทดสอบผู้ให้บริการแบบสด:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

ส่วนนี้ครอบคลุมชุดทดสอบหน่วยหลักของ Pi:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## การทดสอบด้วยตนเอง

โฟลว์ที่แนะนำ:

  * รัน Gateway ในโหมดพัฒนา: 
    * `pnpm gateway:dev`
  * เรียกเอเจนต์โดยตรง: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * ใช้ TUI สำหรับการดีบักแบบโต้ตอบ: 
    * `pnpm tui`


สำหรับพฤติกรรมการเรียกเครื่องมือ ให้พรอมป์สำหรับการกระทำ `read` หรือ `exec` เพื่อให้คุณเห็นการสตรีมของเครื่องมือและการจัดการเพย์โหลด

## การรีเซ็ตให้เริ่มใหม่ทั้งหมด

สถานะอยู่ภายใต้ไดเรกทอรีสถานะของ OpenClaw ค่าเริ่มต้นคือ `~/.openclaw` หากตั้งค่า `OPENCLAW_STATE_DIR` ไว้ ให้ใช้ไดเรกทอรีนั้นแทน

เมื่อต้องการรีเซ็ตทุกอย่าง:

  * `openclaw.json` สำหรับการกำหนดค่า
  * `agents/<agentId>/agent/auth-profiles.json` สำหรับโปรไฟล์การยืนยันตัวตนของโมเดล (คีย์ API + OAuth)
  * `credentials/` สำหรับสถานะของผู้ให้บริการ/ช่องทางที่ยังอยู่นอกร้านโปรไฟล์การยืนยันตัวตน
  * `agents/<agentId>/sessions/` สำหรับประวัติเซสชันของเอเจนต์
  * `agents/<agentId>/sessions/sessions.json` สำหรับดัชนีเซสชัน
  * `sessions/` หากมีพาธเดิมอยู่
  * `workspace/` หากคุณต้องการพื้นที่ทำงานว่างเปล่า


หากคุณต้องการรีเซ็ตเฉพาะเซสชัน ให้ลบ `agents/<agentId>/sessions/` สำหรับเอเจนต์นั้น หากคุณต้องการเก็บการยืนยันตัวตนไว้ ให้คง `agents/<agentId>/agent/auth-profiles.json` และสถานะของผู้ให้บริการใดๆ ภายใต้ `credentials/` ไว้ตามเดิม

## อ้างอิง

  * [การทดสอบ](</th/help/testing>)
  * [เริ่มต้นใช้งาน](</th/start/getting-started>)


## ที่เกี่ยวข้อง

  * [สถาปัตยกรรมการผสานรวม Pi](</th/pi>)


Was this useful?YesNo