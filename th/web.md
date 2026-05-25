---
title: เว็บ
source_url: https://docs.openclaw.ai/th/web
scraped_at: 2026-05-25
---

Gateway ให้บริการ **Control UI บนเบราว์เซอร์** ขนาดเล็ก (Vite + Lit) จากพอร์ตเดียวกับ Gateway WebSocket:

  * ค่าเริ่มต้น: `http://<host>:18789/`
  * เมื่อใช้ `gateway.tls.enabled: true`: `https://<host>:18789/`
  * คำนำหน้าแบบไม่บังคับ: ตั้งค่า `gateway.controlUi.basePath` (เช่น `/openclaw`)


ความสามารถต่างๆ อยู่ใน [Control UI](</th/web/control-ui>) ส่วนที่เหลือของหน้านี้มุ่งเน้นที่โหมดการ bind, ความปลอดภัย และพื้นผิวที่เปิดต่อเว็บ

## Webhook

เมื่อ `hooks.enabled=true` Gateway จะเปิดเผย endpoint webhook ขนาดเล็กบนเซิร์ฟเวอร์ HTTP เดียวกันด้วย ดู [การกำหนดค่า Gateway](</th/gateway/configuration>) → `hooks` สำหรับ auth + payload

## การกำหนดค่า (เปิดตามค่าเริ่มต้น)

Control UI **เปิดใช้งานตามค่าเริ่มต้น** เมื่อมี assets อยู่ (`dist/control-ui`) คุณสามารถควบคุมได้ผ่านการกำหนดค่า:

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath optional  },}
[/code]

## การเข้าถึงผ่าน Tailscale

### Serve แบบรวมในตัว (แนะนำ)

ให้ Gateway อยู่บน loopback และให้ Tailscale Serve ทำหน้าที่ proxy:

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

จากนั้นเริ่ม gateway:

bashCopy code
[code]
    openclaw gateway
[/code]

เปิด:

  * `https://<magicdns>/` (หรือ `gateway.controlUi.basePath` ที่คุณกำหนดค่าไว้)


### Bind กับ tailnet + token

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

จากนั้นเริ่ม gateway (ตัวอย่างแบบ non-loopback นี้ใช้ shared-secret token auth):

bashCopy code
[code]
    openclaw gateway
[/code]

เปิด:

  * `http://<tailscale-ip>:18789/` (หรือ `gateway.controlUi.basePath` ที่คุณกำหนดค่าไว้)


### อินเทอร์เน็ตสาธารณะ (Funnel)

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // or OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## หมายเหตุด้านความปลอดภัย

  * Gateway auth เป็นสิ่งจำเป็นตามค่าเริ่มต้น (token, password, trusted-proxy หรือ Tailscale Serve identity headers เมื่อเปิดใช้งาน)
  * การ bind แบบ non-loopback ยัง **ต้องใช้** gateway auth ในทางปฏิบัติหมายถึง token/password auth หรือ reverse proxy ที่รับรู้ตัวตนพร้อม `gateway.auth.mode: "trusted-proxy"`
  * wizard จะสร้าง shared-secret auth ตามค่าเริ่มต้น และโดยปกติจะสร้าง gateway token (แม้บน loopback)
  * ในโหมด shared-secret UI จะส่ง `connect.params.auth.token` หรือ `connect.params.auth.password`
  * เมื่อ `gateway.tls.enabled: true` ตัวช่วย dashboard และสถานะในเครื่องจะแสดง URL dashboard แบบ `https://` และ URL WebSocket แบบ `wss://`
  * ในโหมดที่มี identity เช่น Tailscale Serve หรือ `trusted-proxy` การตรวจสอบ WebSocket auth จะผ่านจาก request headers แทน
  * สำหรับการนำ Control UI ไปใช้แบบ non-loopback ให้ตั้งค่า `gateway.controlUi.allowedOrigins` อย่างชัดเจน (origin แบบเต็ม) หากไม่มีค่านี้ การเริ่มต้น gateway จะถูกปฏิเสธตามค่าเริ่มต้น
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` เปิดใช้งาน โหมด fallback ของ origin จาก Host-header แต่เป็นการลดระดับความปลอดภัยที่อันตราย
  * เมื่อใช้ Serve, Tailscale identity headers สามารถตอบสนอง Control UI/WebSocket auth ได้เมื่อ `gateway.auth.allowTailscale` เป็น `true` (ไม่ต้องใช้ token/password) endpoint ของ HTTP API ไม่ใช้ Tailscale identity headers เหล่านั้น แต่จะทำตาม โหมด HTTP auth ปกติของ gateway แทน ตั้งค่า `gateway.auth.allowTailscale: false` เพื่อบังคับให้ใช้ credentials อย่างชัดเจน ดู [Tailscale](</th/gateway/tailscale>) และ [ความปลอดภัย](</th/gateway/security>) โฟลว์แบบไม่ใช้ token นี้ถือว่าโฮสต์ gateway เชื่อถือได้
  * `gateway.tailscale.mode: "funnel"` ต้องใช้ `gateway.auth.mode: "password"` (shared password)


## การ build UI

Gateway ให้บริการไฟล์ static จาก `dist/control-ui` build ไฟล์เหล่านี้ด้วย:

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo