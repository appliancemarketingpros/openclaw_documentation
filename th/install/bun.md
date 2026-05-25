---
title: Bun (เชิงทดลอง)
source_url: https://docs.openclaw.ai/th/install/bun
scraped_at: 2026-05-25
---

Bun เป็นรันไทม์ภายในเครื่องแบบไม่บังคับสำหรับรัน TypeScript โดยตรง (`bun run ...`, `bun --watch ...`) ตัวจัดการแพ็กเกจเริ่มต้นยังคงเป็น `pnpm` ซึ่งรองรับอย่างสมบูรณ์และใช้โดยเครื่องมือเอกสาร Bun ไม่สามารถใช้ `pnpm-lock.yaml` และจะเพิกเฉยต่อไฟล์นี้

## ติดตั้ง

* ### Install dependencies

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` ถูก gitignore ไว้ ดังนั้นจึงไม่มีความเปลี่ยนแปลงรบกวนใน repo หากต้องการข้ามการเขียน lockfile ทั้งหมด:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build and test

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## สคริปต์วงจรชีวิต

Bun บล็อกสคริปต์วงจรชีวิตของ dependency เว้นแต่จะถูกเชื่อถืออย่างชัดเจน สำหรับ repo นี้ สคริปต์ที่มักถูกบล็อกไม่จำเป็นต้องใช้:

  * `baileys` `preinstall` \-- ตรวจสอบ Node major >= 20 (OpenClaw ใช้ค่าเริ่มต้นเป็น Node 24 และยังรองรับ Node 22 LTS ซึ่งปัจจุบันคือ `22.16+`)
  * `protobufjs` `postinstall` \-- แสดงคำเตือนเกี่ยวกับรูปแบบเวอร์ชันที่เข้ากันไม่ได้ (ไม่มีอาร์ติแฟกต์จากการ build)


หากคุณพบปัญหารันไทม์ที่ต้องใช้สคริปต์เหล่านี้ ให้เชื่อถือสคริปต์เหล่านั้นอย่างชัดเจน:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## ข้อควรระวัง

สคริปต์บางรายการยังคง hardcode pnpm อยู่ (เช่น `docs:build`, `ui:*`, `protocol:check`) ให้รันรายการเหล่านั้นผ่าน pnpm ไปก่อนในตอนนี้

## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [Node.js](</th/install/node>)
  * [การอัปเดต](</th/install/updating>)


Was this useful?YesNo