---
title: การบันทึกล็อกของ macOS
source_url: https://docs.openclaw.ai/th/platforms/mac/logging
scraped_at: 2026-05-25
---

# การบันทึก (macOS)

## บันทึกไฟล์วินิจฉัยแบบหมุนเวียน (แผง Debug)

OpenClaw ส่งบันทึกของแอป macOS ผ่าน swift-log (ค่าเริ่มต้นคือการบันทึกแบบรวมศูนย์) และสามารถเขียนบันทึกไฟล์ภายในเครื่องแบบหมุนเวียนลงดิสก์ได้เมื่อคุณต้องการการจับข้อมูลที่คงอยู่

  * ระดับรายละเอียด: **แผง Debug → บันทึก → การบันทึกของแอป → ระดับรายละเอียด**
  * เปิดใช้: **แผง Debug → บันทึก → การบันทึกของแอป → "เขียนบันทึกวินิจฉัยแบบหมุนเวียน (JSONL)"**
  * ตำแหน่ง: `~/Library/Logs/OpenClaw/diagnostics.jsonl` (หมุนเวียนโดยอัตโนมัติ; ไฟล์เก่าจะมีส่วนต่อท้ายเป็น `.1`, `.2`, …)
  * ล้าง: **แผง Debug → บันทึก → การบันทึกของแอป → "ล้าง"**


หมายเหตุ:

  * สิ่งนี้**ปิดอยู่โดยค่าเริ่มต้น** เปิดใช้เฉพาะขณะกำลังดีบักเท่านั้น
  * ถือว่าไฟล์นี้มีข้อมูลละเอียดอ่อน อย่าแชร์โดยไม่ได้ตรวจสอบก่อน


## ข้อมูลส่วนตัวใน unified logging บน macOS

Unified logging จะปกปิด payload ส่วนใหญ่ เว้นแต่ subsystem จะเลือกใช้ `privacy -off` ตามบทความของ Peter เกี่ยวกับ [ประเด็นความเป็นส่วนตัวของการบันทึกบน macOS](<https://steipete.me/posts/2025/logging-privacy-shenanigans>) (2025) สิ่งนี้ควบคุมด้วย plist ใน `/Library/Preferences/Logging/Subsystems/` ที่ใช้ชื่อ subsystem เป็นคีย์ มีเพียงรายการบันทึกใหม่เท่านั้นที่จะรับค่าแฟล็กนี้ ดังนั้นให้เปิดใช้ก่อนทำให้ปัญหาเกิดซ้ำ

## เปิดใช้สำหรับ OpenClaw (`ai.openclaw`)

  * เขียน plist ไปยังไฟล์ชั่วคราวก่อน แล้วติดตั้งแบบ atomic ในฐานะ root:

bashCopy code
[code]
    cat <<'EOF' >/tmp/ai.openclaw.plist<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>DEFAULT-OPTIONS</key>    <dict>        <key>Enable-Private-Data</key>        <true/>    </dict></dict></plist>EOFsudo install -m 644 -o root -g wheel /tmp/ai.openclaw.plist /Library/Preferences/Logging/Subsystems/ai.openclaw.plist
[/code]

  * ไม่จำเป็นต้องรีบูต; logd จะตรวจพบไฟล์อย่างรวดเร็ว แต่เฉพาะบรรทัดบันทึกใหม่เท่านั้นที่จะรวม payload ส่วนตัว
  * ดูเอาต์พุตที่มีรายละเอียดมากขึ้นด้วยตัวช่วยที่มีอยู่ เช่น `./scripts/clawlog.sh --category WebChat --last 5m`


## ปิดใช้หลังจากดีบัก

  * ลบ override: `sudo rm /Library/Preferences/Logging/Subsystems/ai.openclaw.plist`
  * เลือกเรียกใช้ `sudo log config --reload` เพื่อบังคับให้ logd ยกเลิก override ทันที
  * จำไว้ว่าพื้นที่นี้อาจรวมหมายเลขโทรศัพท์และเนื้อหาข้อความไว้ด้วย ให้เก็บ plist ไว้เฉพาะขณะที่คุณต้องการรายละเอียดเพิ่มเติมนี้จริง ๆ เท่านั้น


## ที่เกี่ยวข้อง

  * [แอป macOS](</th/platforms/macos>)
  * [การบันทึกของ Gateway](</th/gateway/logging>)


Was this useful?YesNo