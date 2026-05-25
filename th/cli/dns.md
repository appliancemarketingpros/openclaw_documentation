---
title: DNS
source_url: https://docs.openclaw.ai/th/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

ตัวช่วย DNS สำหรับการค้นพบแบบพื้นที่กว้าง (Tailscale + CoreDNS) ปัจจุบันมุ่งเน้นที่ macOS + Homebrew CoreDNS

ที่เกี่ยวข้อง:

  * การค้นพบ Gateway: [การค้นพบ](</th/gateway/discovery>)
  * การกำหนดค่าการค้นพบแบบพื้นที่กว้าง: [การกำหนดค่า](</th/gateway/configuration>)


## การตั้งค่า

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

วางแผนหรือนำการตั้งค่า CoreDNS ไปใช้สำหรับการค้นพบ DNS-SD แบบ unicast

ตัวเลือก:

  * `--domain <domain>`: โดเมนการค้นพบแบบพื้นที่กว้าง (เช่น `openclaw.internal`)
  * `--apply`: ติดตั้งหรืออัปเดตการกำหนดค่า CoreDNS แล้วรีสตาร์ทบริการ (ต้องใช้ sudo; เฉพาะ macOS)


สิ่งที่แสดง:

  * โดเมนการค้นพบที่แก้ค่าแล้ว
  * เส้นทางไฟล์โซน
  * IP ของ tailnet ปัจจุบัน
  * การกำหนดค่า discovery ของ `openclaw.json` ที่แนะนำ
  * ค่า nameserver/domain ของ Tailscale Split DNS ที่ต้องตั้งค่า


หมายเหตุ:

  * หากไม่มี `--apply` คำสั่งนี้เป็นเพียงตัวช่วยวางแผนและพิมพ์การตั้งค่าที่แนะนำ
  * หากละ `--domain` ไว้ OpenClaw จะใช้ `discovery.wideArea.domain` จากการกำหนดค่า
  * ปัจจุบัน `--apply` รองรับเฉพาะ macOS และคาดว่าจะใช้ Homebrew CoreDNS
  * `--apply` จะเริ่มต้นไฟล์โซนหากจำเป็น ตรวจให้แน่ใจว่ามี stanza สำหรับ import ของ CoreDNS อยู่ และรีสตาร์ทบริการ brew `coredns`


## ที่เกี่ยวข้อง

  * [อ้างอิง CLI](</th/cli>)
  * [การค้นพบ](</th/gateway/discovery>)


Was this useful?YesNo