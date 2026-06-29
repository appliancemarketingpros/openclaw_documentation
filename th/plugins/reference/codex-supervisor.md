---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/th/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin ผู้ดูแล Codex

ดูแลเซสชัน app-server ของ Codex จาก OpenClaw

## การแจกจ่าย

  * แพ็กเกจ: `@openclaw/codex-supervisor`
  * เส้นทางการติดตั้ง: รวมอยู่ใน OpenClaw


## พื้นผิว

contracts: tools

## รายการเซสชัน

`codex_sessions_list` มีค่าเริ่มต้นเป็นเฉพาะเซสชัน Codex ที่โหลดแล้ว ตั้งค่า `include_stored` เพื่อรวมประวัติที่จัดเก็บไว้; plugin ใช้เส้นทางการแสดงรายการแบบ state-DB-only ของ app-server ของ Codex และจำกัดผลลัพธ์ที่จัดเก็บไว้ที่ 200 โดยค่าเริ่มต้น ส่ง `max_stored_sessions` เพื่อลดหรือเพิ่มขีดจำกัดนั้นได้สูงสุดถึง 1000

Was this useful?YesNo

Open issue