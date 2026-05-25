---
title: การตรวจสอบสิทธิ์พร็อกซีที่เชื่อถือได้
source_url: https://docs.openclaw.ai/th/gateway/trusted-proxy-auth
scraped_at: 2026-05-25
---

## ควรใช้เมื่อใด

ใช้โหมดการตรวจสอบสิทธิ์ `trusted-proxy` เมื่อ:

  * คุณรัน OpenClaw อยู่หลัง **identity-aware proxy** (Pomerium, Caddy + OAuth, nginx + oauth2-proxy, Traefik + forward auth)
  * Proxy ของคุณจัดการการตรวจสอบสิทธิ์ทั้งหมดและส่งผ่านตัวตนผู้ใช้ผ่าน headers
  * คุณอยู่ในสภาพแวดล้อม Kubernetes หรือ container ที่ proxy เป็นเส้นทางเดียวไปยัง Gateway
  * คุณพบข้อผิดพลาด WebSocket `1008 unauthorized` เพราะเบราว์เซอร์ไม่สามารถส่ง tokens ใน WS payloads ได้


## ไม่ควรใช้เมื่อใด

  * หาก proxy ของคุณไม่ได้ตรวจสอบสิทธิ์ผู้ใช้ (เป็นเพียง TLS terminator หรือ load balancer)
  * หากมีเส้นทางใดก็ตามไปยัง Gateway ที่ข้าม proxy (ช่องโหว่ firewall, การเข้าถึงเครือข่ายภายใน)
  * หากคุณไม่แน่ใจว่า proxy ของคุณลบหรือเขียนทับ forwarded headers อย่างถูกต้องหรือไม่
  * หากคุณต้องการเพียงการเข้าถึงแบบผู้ใช้เดียวส่วนตัว (พิจารณา Tailscale Serve + loopback เพื่อการตั้งค่าที่ง่ายกว่า)


## วิธีทำงาน

* ### Proxy ตรวจสอบสิทธิ์ผู้ใช้

reverse proxy ของคุณตรวจสอบสิทธิ์ผู้ใช้ (OAuth, OIDC, SAML เป็นต้น)

* ### Proxy เพิ่ม identity header

Proxy เพิ่ม header ที่มีตัวตนผู้ใช้ที่ผ่านการตรวจสอบสิทธิ์แล้ว (เช่น `x-forwarded-user: nick@example.com`)

* ### Gateway ตรวจสอบแหล่งที่เชื่อถือได้

OpenClaw ตรวจสอบว่าคำขอมาจาก **IP ของ proxy ที่เชื่อถือได้** (กำหนดค่าใน `gateway.trustedProxies`)

* ### Gateway ดึงตัวตน

OpenClaw ดึงตัวตนผู้ใช้จาก header ที่กำหนดค่าไว้

* ### อนุญาต

หากทุกอย่างตรวจสอบผ่าน คำขอจะได้รับอนุญาต

## พฤติกรรมการจับคู่ Control UI

เมื่อ `gateway.auth.mode = "trusted-proxy"` ทำงานอยู่และคำขอผ่านการตรวจสอบ trusted-proxy แล้ว เซสชัน WebSocket ของ Control UI สามารถเชื่อมต่อได้โดยไม่ต้องมีตัวตนจากการจับคู่อุปกรณ์

ผลที่ตามมา:

  * การจับคู่จะไม่ใช่ด่านหลักสำหรับการเข้าถึง Control UI ในโหมดนี้อีกต่อไป
  * นโยบายการตรวจสอบสิทธิ์ของ reverse proxy และ `allowUsers` จะกลายเป็นการควบคุมการเข้าถึงที่มีผลจริง
  * จำกัด gateway ingress ให้เฉพาะ IP ของ proxy ที่เชื่อถือได้เท่านั้น (`gateway.trustedProxies` \+ firewall)


## การกำหนดค่า

json5Copy code
[code]
    {  gateway: {    // Trusted-proxy auth expects requests from a non-loopback trusted proxy source by default    bind: "lan",     // CRITICAL: Only add your proxy's IP(s) here    trustedProxies: ["10.0.0.1", "172.17.0.1"],     auth: {      mode: "trusted-proxy",      trustedProxy: {        // Header containing authenticated user identity (required)        userHeader: "x-forwarded-user",         // Optional: headers that MUST be present (proxy verification)        requiredHeaders: ["x-forwarded-proto", "x-forwarded-host"],         // Optional: restrict to specific users (empty = allow all)        allowUsers: ["nick@example.com", "admin@company.org"],         // Optional: allow a same-host loopback proxy after explicit opt-in        allowLoopback: false,      },    },  },}
[/code]

### ข้อมูลอ้างอิงการกำหนดค่า

อาร์เรย์ของที่อยู่ IP ของ proxy ที่เชื่อถือได้ คำขอจาก IP อื่นจะถูกปฏิเสธ

ต้องเป็น `"trusted-proxy"`

ชื่อ header ที่มีตัวตนผู้ใช้ที่ผ่านการตรวจสอบสิทธิ์

headers เพิ่มเติมที่ต้องมีเพื่อให้คำขอได้รับความเชื่อถือ

allowlist ของตัวตนผู้ใช้ ค่าว่างหมายถึงอนุญาตผู้ใช้ที่ผ่านการตรวจสอบสิทธิ์ทั้งหมด

การรองรับแบบ opt-in สำหรับ same-host loopback reverse proxies ค่าเริ่มต้นคือ `false`

## TLS termination และ HSTS

ใช้จุด TLS termination เพียงจุดเดียวและใช้ HSTS ที่จุดนั้น

### Proxy TLS termination (แนะนำ)

เมื่อ reverse proxy ของคุณจัดการ HTTPS สำหรับ `https://control.example.com` ให้ตั้งค่า `Strict-Transport-Security` ที่ proxy สำหรับโดเมนนั้น

  * เหมาะกับการปรับใช้ที่เปิดสู่อินเทอร์เน็ต
  * เก็บนโยบาย certificate + HTTP hardening ไว้ในที่เดียว
  * OpenClaw สามารถคงอยู่บน HTTP แบบ loopback หลัง proxy ได้


ค่าตัวอย่างของ header:

textCopy code
[code]
    Strict-Transport-Security: max-age=31536000; includeSubDomains
[/code]

### Gateway TLS termination

หาก OpenClaw ให้บริการ HTTPS โดยตรงเอง (ไม่มี proxy ที่ทำ TLS termination) ให้ตั้งค่า:

json5Copy code
[code]
    {  gateway: {    tls: { enabled: true },    http: {      securityHeaders: {        strictTransportSecurity: "max-age=31536000; includeSubDomains",      },    },  },}
[/code]

`strictTransportSecurity` รับค่า header แบบ string หรือ `false` เพื่อปิดใช้งานอย่างชัดเจน

### แนวทางการ rollout

  * เริ่มด้วย max age สั้น ๆ ก่อน (เช่น `max-age=300`) ระหว่างตรวจสอบ traffic
  * เพิ่มเป็นค่าที่มีอายุยาว (เช่น `max-age=31536000`) เฉพาะหลังจากมีความมั่นใจสูงแล้ว
  * เพิ่ม `includeSubDomains` เฉพาะเมื่อทุก subdomain พร้อมใช้ HTTPS
  * ใช้ preload เฉพาะเมื่อคุณตั้งใจทำตามข้อกำหนด preload สำหรับชุดโดเมนทั้งหมดของคุณ
  * การพัฒนาภายในเครื่องแบบ loopback-only ไม่ได้รับประโยชน์จาก HSTS


## ตัวอย่างการตั้งค่า Proxy

Pomerium

Pomerium ส่งผ่านตัวตนใน `x-pomerium-claim-email` (หรือ claim headers อื่น) และ JWT ใน `x-pomerium-jwt-assertion`

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Pomerium's IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-pomerium-claim-email",        requiredHeaders: ["x-pomerium-jwt-assertion"],      },    },  },}
[/code]

ตัวอย่างส่วนกำหนดค่า Pomerium:

yamlCopy code
[code]
    routes:  - from: https://openclaw.example.com    to: http://openclaw-gateway:18789    policy:      - allow:          or:            - email:                is: nick@example.com    pass_identity_headers: true
[/code]

Caddy พร้อม OAuth

Caddy พร้อม Plugin `caddy-security` สามารถตรวจสอบสิทธิ์ผู้ใช้และส่งผ่าน identity headers ได้

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Caddy/sidecar proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

ตัวอย่างส่วน Caddyfile:

CodeCopy code
[code]
    openclaw.example.com {    authenticate with oauth2_provider    authorize with policy1     reverse_proxy openclaw:18789 {        header_up X-Forwarded-User {http.auth.user.email}    }}
[/code]

nginx + oauth2-proxy

oauth2-proxy ตรวจสอบสิทธิ์ผู้ใช้และส่งผ่านตัวตนใน `x-auth-request-email`

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // nginx/oauth2-proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-auth-request-email",      },    },  },}
[/code]

ตัวอย่างส่วนกำหนดค่า nginx:

nginxCopy code
[code]
    location / {    auth_request /oauth2/auth;    auth_request_set $user $upstream_http_x_auth_request_email;     proxy_pass http://openclaw:18789;    proxy_set_header X-Auth-Request-Email $user;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
[/code]

Traefik พร้อม forward auth json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["172.17.0.1"], // Traefik container IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

## การกำหนดค่า token แบบผสม

OpenClaw ปฏิเสธการกำหนดค่าที่กำกวมเมื่อทั้ง `gateway.auth.token` (หรือ `OPENCLAW_GATEWAY_TOKEN`) และโหมด `trusted-proxy` ทำงานพร้อมกัน การกำหนดค่า token แบบผสมอาจทำให้คำขอ loopback ตรวจสอบสิทธิ์แบบเงียบ ๆ บนเส้นทางการตรวจสอบสิทธิ์ที่ผิด

หากคุณเห็นข้อผิดพลาด `mixed_trusted_proxy_token` ตอนเริ่มต้น:

  * ลบ shared token เมื่อใช้โหมด trusted-proxy หรือ
  * เปลี่ยน `gateway.auth.mode` เป็น `"token"` หากคุณตั้งใจใช้การตรวจสอบสิทธิ์แบบ token-based


identity headers ของ trusted-proxy บน loopback ยังคง fail closed: ผู้เรียกจากโฮสต์เดียวกันจะไม่ถูกตรวจสอบสิทธิ์แบบเงียบ ๆ เป็นผู้ใช้ proxy ผู้เรียก OpenClaw ภายในที่ข้าม proxy อาจตรวจสอบสิทธิ์ด้วย `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD` แทน token fallback ยังคงไม่รองรับโดยตั้งใจในโหมด trusted-proxy

## Operator scopes header

การตรวจสอบสิทธิ์แบบ trusted-proxy เป็นโหมด HTTP ที่ **มีตัวตนประกอบ** ดังนั้นผู้เรียกอาจประกาศ operator scopes ด้วย `x-openclaw-scopes` ได้ตามต้องการ

ตัวอย่าง:

  * `x-openclaw-scopes: operator.read`
  * `x-openclaw-scopes: operator.read,operator.write`
  * `x-openclaw-scopes: operator.admin,operator.write`


พฤติกรรม:

  * เมื่อมี header อยู่ OpenClaw จะเคารพชุด scope ที่ประกาศไว้
  * เมื่อมี header อยู่แต่ค่าว่าง คำขอจะประกาศว่า **ไม่มี** operator scopes
  * เมื่อไม่มี header อยู่ API HTTP แบบมีตัวตนประกอบตามปกติจะ fallback ไปยังชุด scope เริ่มต้นมาตรฐานของ operator
  * **เส้นทาง HTTP ของ Plugin** แบบ Gateway-auth จะแคบกว่าโดยค่าเริ่มต้น: เมื่อไม่มี `x-openclaw-scopes` runtime scope ของเส้นทางเหล่านั้นจะ fallback ไปที่ `operator.write`
  * คำขอ HTTP จาก browser-origin ยังคงต้องผ่าน `gateway.controlUi.allowedOrigins` (หรือโหมด Host-header fallback ที่ตั้งใจใช้) แม้หลังจากการตรวจสอบสิทธิ์แบบ trusted-proxy สำเร็จแล้ว


กฎเชิงปฏิบัติ: ส่ง `x-openclaw-scopes` อย่างชัดเจนเมื่อคุณต้องการให้คำขอ trusted-proxy แคบกว่าค่าเริ่มต้น หรือเมื่อเส้นทาง Plugin แบบ gateway-auth ต้องการสิ่งที่แข็งแรงกว่า write scope

## รายการตรวจสอบความปลอดภัย

ก่อนเปิดใช้การยืนยันตัวตนแบบ trusted-proxy ให้ตรวจสอบว่า:

  * [ ] **พร็อกซีเป็นเส้นทางเดียวเท่านั้น** : พอร์ต Gateway ถูกไฟร์วอลล์จากทุกอย่าง ยกเว้นพร็อกซีของคุณ
  * [ ] **trustedProxies มีรายการน้อยที่สุด** : มีเฉพาะ IP พร็อกซีจริงของคุณ ไม่ใช่ทั้งซับเน็ต
  * [ ] **แหล่งที่มาของพร็อกซีแบบ loopback เป็นความตั้งใจ** : การยืนยันตัวตนแบบ trusted-proxy จะปิดกั้นคำขอจากแหล่งที่มาแบบ loopback โดยค่าเริ่มต้น เว้นแต่จะเปิดใช้ `gateway.auth.trustedProxy.allowLoopback` อย่างชัดเจนสำหรับพร็อกซีบนโฮสต์เดียวกัน
  * [ ] **พร็อกซีล้างส่วนหัว** : พร็อกซีของคุณเขียนทับ (ไม่ใช่ต่อท้าย) ส่วนหัว `x-forwarded-*` จากไคลเอนต์
  * [ ] **การสิ้นสุด TLS** : พร็อกซีของคุณจัดการ TLS; ผู้ใช้เชื่อมต่อผ่าน HTTPS
  * [ ] **allowedOrigins ระบุอย่างชัดเจน** : Control UI ที่ไม่ใช่ loopback ใช้ `gateway.controlUi.allowedOrigins` ที่ระบุอย่างชัดเจน
  * [ ] **ตั้งค่า allowUsers แล้ว** (แนะนำ): จำกัดไว้เฉพาะผู้ใช้ที่รู้จัก แทนที่จะอนุญาตทุกคนที่ยืนยันตัวตนแล้ว
  * [ ] **ไม่มีการกำหนดค่า token แบบผสม** : อย่าตั้งค่าทั้ง `gateway.auth.token` และ `gateway.auth.mode: "trusted-proxy"`
  * [ ] **รหัสผ่านสำรองในเครื่องเป็นส่วนตัว** : หากคุณกำหนดค่า `gateway.auth.password` สำหรับผู้เรียกโดยตรงภายใน ให้ไฟร์วอลล์พอร์ต Gateway ไว้เพื่อไม่ให้ไคลเอนต์ระยะไกลที่ไม่ผ่านพร็อกซีเข้าถึงได้โดยตรง


## การตรวจสอบความปลอดภัย

`openclaw security audit` จะทำเครื่องหมายการยืนยันตัวตนแบบ trusted-proxy เป็นรายการความรุนแรงระดับ **วิกฤต** นี่เป็นความตั้งใจ — เป็นการเตือนว่าคุณกำลังมอบหมายความปลอดภัยให้กับการตั้งค่าพร็อกซีของคุณ

การตรวจสอบจะตรวจหา:

  * คำเตือน/คำเตือนวิกฤตพื้นฐาน `gateway.trusted_proxy_auth`
  * การกำหนดค่า `trustedProxies` ที่ขาดหายไป
  * การกำหนดค่า `userHeader` ที่ขาดหายไป
  * `allowUsers` ว่างเปล่า (อนุญาตผู้ใช้ที่ยืนยันตัวตนแล้วทุกคน)
  * เปิดใช้ `allowLoopback` สำหรับแหล่งที่มาของพร็อกซีบนโฮสต์เดียวกัน
  * นโยบาย browser-origin แบบ wildcard หรือขาดหายไปบนพื้นผิว Control UI ที่เปิดเผย


## การแก้ไขปัญหา

trusted_proxy_untrusted_source

คำขอไม่ได้มาจาก IP ใน `gateway.trustedProxies` ตรวจสอบว่า:

  * IP ของพร็อกซีถูกต้องหรือไม่? (IP ของคอนเทนเนอร์ Docker อาจเปลี่ยนได้)
  * มี load balancer อยู่หน้าพร็อกซีของคุณหรือไม่?
  * ใช้ `docker inspect` หรือ `kubectl get pods -o wide` เพื่อหา IP จริง

trusted_proxy_loopback_source

OpenClaw ปฏิเสธคำขอ trusted-proxy จากแหล่งที่มาแบบ loopback

ตรวจสอบว่า:

  * พร็อกซีกำลังเชื่อมต่อจาก `127.0.0.1` / `::1` หรือไม่?
  * คุณกำลังพยายามใช้การยืนยันตัวตนแบบ trusted-proxy กับ reverse proxy แบบ loopback บนโฮสต์เดียวกันหรือไม่?


วิธีแก้ไข:

  * ควรใช้การยืนยันตัวตนแบบ token/password สำหรับไคลเอนต์ภายในบนโฮสต์เดียวกันที่ไม่ได้ผ่านพร็อกซี หรือ
  * กำหนดเส้นทางผ่านที่อยู่พร็อกซีที่เชื่อถือได้ซึ่งไม่ใช่ loopback และเก็บ IP นั้นไว้ใน `gateway.trustedProxies` หรือ
  * สำหรับ reverse proxy บนโฮสต์เดียวกันที่ตั้งใจใช้ ให้ตั้งค่า `gateway.auth.trustedProxy.allowLoopback = true` เก็บที่อยู่ loopback ไว้ใน `gateway.trustedProxies` และตรวจสอบให้แน่ใจว่าพร็อกซีล้างหรือเขียนทับส่วนหัวระบุตัวตน

trusted_proxy_user_missing

ส่วนหัวผู้ใช้ว่างเปล่าหรือขาดหายไป ตรวจสอบว่า:

  * พร็อกซีของคุณกำหนดค่าให้ส่งต่อส่วนหัวระบุตัวตนหรือไม่?
  * ชื่อส่วนหัวถูกต้องหรือไม่? (ไม่สนตัวพิมพ์เล็กใหญ่ แต่การสะกดต้องถูกต้อง)
  * ผู้ใช้ยืนยันตัวตนที่พร็อกซีแล้วจริงหรือไม่?

trusted_proxy_missing_header_*

ไม่มีส่วนหัวที่จำเป็น ตรวจสอบว่า:

  * การกำหนดค่าพร็อกซีของคุณสำหรับส่วนหัวเฉพาะเหล่านั้น
  * ส่วนหัวถูกล้างที่ใดที่หนึ่งในห่วงโซ่หรือไม่

trusted_proxy_user_not_allowed

ผู้ใช้ยืนยันตัวตนแล้วแต่ไม่ได้อยู่ใน `allowUsers` ให้เพิ่มผู้ใช้รายนั้นหรือลบ allowlist

trusted_proxy_origin_not_allowed

การยืนยันตัวตนแบบ trusted-proxy สำเร็จแล้ว แต่ส่วนหัว `Origin` ของเบราว์เซอร์ไม่ผ่านการตรวจสอบ origin ของ Control UI

ตรวจสอบว่า:

  * `gateway.controlUi.allowedOrigins` มี origin ของเบราว์เซอร์ที่ตรงกันทุกประการ
  * คุณไม่ได้พึ่งพา wildcard origins เว้นแต่คุณตั้งใจต้องการพฤติกรรมอนุญาตทั้งหมด
  * หากคุณตั้งใจใช้โหมดสำรองจากส่วนหัว Host ให้ตั้งค่า `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` อย่างตั้งใจ

WebSocket still failing

ตรวจสอบให้แน่ใจว่าพร็อกซีของคุณ:

  * รองรับการอัปเกรด WebSocket (`Upgrade: websocket`, `Connection: upgrade`)
  * ส่งต่อส่วนหัวระบุตัวตนในคำขออัปเกรด WebSocket (ไม่ใช่เฉพาะ HTTP)
  * ไม่มีเส้นทางการยืนยันตัวตนแยกต่างหากสำหรับการเชื่อมต่อ WebSocket


## การย้ายจากการยืนยันตัวตนแบบ token

หากคุณกำลังย้ายจากการยืนยันตัวตนแบบ token ไปเป็น trusted-proxy:

* ### Configure the proxy

กำหนดค่าพร็อกซีของคุณให้ยืนยันตัวตนผู้ใช้และส่งต่อส่วนหัว

* ### Test the proxy independently

ทดสอบการตั้งค่าพร็อกซีแยกต่างหาก (curl พร้อมส่วนหัว)

* ### Update OpenClaw config

อัปเดตการกำหนดค่า OpenClaw ด้วยการยืนยันตัวตนแบบ trusted-proxy

* ### Restart the Gateway

รีสตาร์ท Gateway

* ### Test WebSocket

ทดสอบการเชื่อมต่อ WebSocket จาก Control UI

* ### Audit

รัน `openclaw security audit` และตรวจทานผลการตรวจสอบ

## ที่เกี่ยวข้อง

  * [การกำหนดค่า](</th/gateway/configuration>) — ข้อมูลอ้างอิงการกำหนดค่า
  * [การเข้าถึงระยะไกล](</th/gateway/remote>) — รูปแบบการเข้าถึงระยะไกลอื่นๆ
  * [ความปลอดภัย](</th/gateway/security>) — คู่มือความปลอดภัยฉบับเต็ม
  * [Tailscale](</th/gateway/tailscale>) — ทางเลือกที่ง่ายกว่าสำหรับการเข้าถึงเฉพาะ tailnet


Was this useful?YesNo