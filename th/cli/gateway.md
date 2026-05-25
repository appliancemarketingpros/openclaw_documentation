---
title: Gateway
source_url: https://docs.openclaw.ai/th/cli/gateway
scraped_at: 2026-05-25
---

Gateway คือเซิร์ฟเวอร์ WebSocket ของ OpenClaw (ช่องทาง, Node, เซสชัน, hook) คำสั่งย่อยในหน้านี้อยู่ภายใต้ `openclaw gateway …`

[**การค้นพบ Bonjour** การตั้งค่า mDNS ภายในเครื่อง + DNS-SD แบบ wide-area ](</th/gateway/bonjour>) [**ภาพรวมการค้นพบ** วิธีที่ OpenClaw ประกาศและค้นหา Gateway ](</th/gateway/discovery>) [**การกำหนดค่า** คีย์การกำหนดค่า Gateway ระดับบนสุด ](</th/gateway/configuration>)

## เรียกใช้ Gateway

เรียกใช้กระบวนการ Gateway ภายในเครื่อง:

bashCopy code
[code]
    openclaw gateway
[/code]

นามแฝงสำหรับโหมด foreground:

bashCopy code
[code]
    openclaw gateway run
[/code]

ลักษณะการทำงานเมื่อเริ่มต้น

  * โดยค่าเริ่มต้น Gateway จะปฏิเสธการเริ่มทำงาน เว้นแต่จะตั้งค่า `gateway.mode=local` ไว้ใน `~/.openclaw/openclaw.json` ใช้ `--allow-unconfigured` สำหรับการรันเฉพาะกิจ/การพัฒนา
  * `openclaw onboard --mode local` และ `openclaw setup` ควรเขียนค่า `gateway.mode=local` หากไฟล์มีอยู่แต่ไม่มี `gateway.mode` ให้ถือว่าเป็นการกำหนดค่าที่เสียหรือถูกเขียนทับ และซ่อมแซมแทนการถือว่าเป็นโหมด local โดยนัย
  * หากไฟล์มีอยู่และไม่มี `gateway.mode` Gateway จะถือว่าเป็นความเสียหายของการกำหนดค่าที่น่าสงสัย และปฏิเสธที่จะ "เดา local" ให้คุณ
  * การ bind ออกนอก loopback โดยไม่มี auth จะถูกบล็อก (มาตรการป้องกันความปลอดภัย)
  * `SIGUSR1` จะทริกเกอร์การรีสตาร์ทภายในกระบวนการเมื่อได้รับอนุญาต (`commands.restart` เปิดใช้งานตามค่าเริ่มต้น; ตั้งค่า `commands.restart: false` เพื่อบล็อกการรีสตาร์ทด้วยตนเอง ขณะที่การ apply/update เครื่องมือ/การกำหนดค่า Gateway ยังอนุญาตอยู่)
  * handler ของ `SIGINT`/`SIGTERM` จะหยุดกระบวนการ Gateway แต่จะไม่กู้คืนสถานะเทอร์มินัลแบบกำหนดเองใด ๆ หากคุณครอบ CLI ด้วย TUI หรืออินพุต raw-mode ให้กู้คืนเทอร์มินัลก่อนออก


### ตัวเลือก

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> พอร์ต WebSocket (ค่าเริ่มต้นมาจาก config/env; โดยทั่วไปคือ `18789`)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> override token (ตั้งค่า `OPENCLAW_GATEWAY_TOKEN` ให้กระบวนการด้วย)

รีเซ็ตการกำหนดค่า serve/funnel ของ Tailscale เมื่อปิดการทำงาน

อนุญาตให้เริ่ม Gateway โดยไม่มี `gateway.mode=local` ในการกำหนดค่า ข้าม guard ตอนเริ่มต้นสำหรับการ bootstrap เฉพาะกิจ/การพัฒนาเท่านั้น; ไม่เขียนหรือซ่อมแซมไฟล์การกำหนดค่า

สร้างการกำหนดค่า + workspace สำหรับการพัฒนาหากไม่มีอยู่ (ข้าม [BOOTSTRAP.md](<http://BOOTSTRAP.md>))

รีเซ็ตการกำหนดค่าสำหรับการพัฒนา + credentials + เซสชัน + workspace (ต้องใช้ `--dev`)

kill listener ที่มีอยู่บนพอร์ตที่เลือกก่อนเริ่มต้น

log แบบละเอียด

แสดงเฉพาะ log ของแบ็กเอนด์ CLI ในคอนโซล (และเปิดใช้ stdout/stderr)

นามแฝงสำหรับ `--ws-log compact`

บันทึกเหตุการณ์สตรีมโมเดลดิบเป็น jsonl

## รีสตาร์ท Gateway

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` ขอให้ Gateway ที่กำลังทำงาน preflight งาน OpenClaw ที่ active ก่อนรีสตาร์ท หากมีการดำเนินการในคิว, การส่งคำตอบ, การรันแบบฝัง, หรือการรัน task ที่ active อยู่ Gateway จะรายงานตัวบล็อก, รวมคำขอรีสตาร์ทแบบ safe ที่ซ้ำกัน, และรีสตาร์ทเมื่อ active work ระบายหมดแล้ว `restart` แบบธรรมดายังคงลักษณะการทำงานของ service-manager เดิมเพื่อความเข้ากันได้ ใช้ `--force` เฉพาะเมื่อคุณต้องการเส้นทาง override ทันทีอย่างชัดเจน

`openclaw gateway restart --safe --skip-deferral` รันการรีสตาร์ทแบบประสานงานที่รับรู้ OpenClaw เหมือนกับ `--safe` แต่ข้าม gate การเลื่อนเพราะ active-work เพื่อให้ Gateway ส่งการรีสตาร์ททันทีแม้ว่าจะมีการรายงานตัวบล็อก ใช้เป็นทางออกฉุกเฉินสำหรับผู้ปฏิบัติการเมื่อการเลื่อนถูกตรึงไว้โดยการรัน task ที่ค้าง และ `--safe` เพียงอย่างเดียวจะรอไม่มีกำหนด `--skip-deferral` ต้องใช้ `--safe`

### การทำโปรไฟล์เมื่อเริ่มต้น

  * ตั้งค่า `OPENCLAW_GATEWAY_STARTUP_TRACE=1` เพื่อบันทึกเวลาของ phase ระหว่างการเริ่มต้น Gateway รวมถึง delay ของ `eventLoopMax` ต่อ phase และเวลาของตารางค้นหา Plugin สำหรับ installed-index, manifest registry, startup planning, และงาน owner-map
  * ตั้งค่า `OPENCLAW_DIAGNOSTICS=timeline` พร้อม `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>` เพื่อเขียน timeline diagnostics ตอนเริ่มต้นแบบ JSONL best-effort สำหรับ harness QA ภายนอก คุณยังสามารถเปิดใช้ flag ด้วย `diagnostics.flags: ["timeline"]` ในการกำหนดค่า; path ยังคงมาจาก env เพิ่ม `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` เพื่อรวมตัวอย่าง event-loop
  * รัน `pnpm test:startup:gateway -- --runs 5 --warmup 1` เพื่อ benchmark การเริ่มต้น Gateway benchmark จะบันทึกเอาต์พุตแรกของกระบวนการ, `/healthz`, `/readyz`, เวลาของ startup trace, delay ของ event-loop, และรายละเอียดเวลาในตารางค้นหา Plugin


## สอบถาม Gateway ที่กำลังทำงาน

คำสั่ง query ทั้งหมดใช้ WebSocket RPC

### โหมดเอาต์พุต

  * ค่าเริ่มต้น: อ่านได้สำหรับมนุษย์ (มีสีใน TTY)
  * `--json`: JSON ที่เครื่องอ่านได้ (ไม่มี styling/spinner)
  * `--no-color` (หรือ `NO_COLOR=1`): ปิด ANSI ขณะที่ยังคง layout สำหรับมนุษย์ไว้


### ตัวเลือกที่ใช้ร่วมกัน

  * `--url <url>`: URL WebSocket ของ Gateway
  * `--token <token>`: token ของ Gateway
  * `--password <password>`: รหัสผ่าน Gateway
  * `--timeout <ms>`: timeout/budget (แตกต่างกันไปตามคำสั่ง)
  * `--expect-final`: รอการตอบกลับแบบ "final" (การเรียก agent)


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

endpoint HTTP `/healthz` เป็น liveness probe: จะตอบกลับเมื่อเซิร์ฟเวอร์สามารถตอบ HTTP ได้ endpoint HTTP `/readyz` เข้มงวดกว่าและจะยังคงเป็นสีแดงขณะที่ sidecar ของ Plugin ตอนเริ่มต้น, ช่องทาง, หรือ hook ที่กำหนดค่าไว้ยังคงกำลัง settle การตอบกลับ readiness แบบละเอียดภายในเครื่องหรือที่ authenticated แล้วจะรวมบล็อก diagnostics `eventLoop` ซึ่งมี delay ของ event-loop, การใช้ประโยชน์ event-loop, อัตราส่วนคอร์ CPU, และ flag `degraded`

### `gateway usage-cost`

ดึงสรุป usage-cost จาก log ของเซสชัน

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

ดึง diagnostic stability recorder ล่าสุดจาก Gateway ที่กำลังทำงาน

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> จำนวนเหตุการณ์ล่าสุดสูงสุดที่จะรวม (สูงสุด `1000`)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> กรองตามประเภทเหตุการณ์ diagnostics เช่น `payload.large` หรือ `diagnostic.memory.pressure`

อ่าน stability bundle ที่บันทึกไว้แทนการเรียก Gateway ที่กำลังทำงาน ใช้ `--bundle latest` (หรือแค่ `--bundle`) สำหรับ bundle ใหม่ที่สุดภายใต้ไดเรกทอรี state หรือส่ง path JSON ของ bundle โดยตรง

เขียน zip diagnostics สำหรับ support ที่แชร์ได้ แทนการพิมพ์รายละเอียด stability

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> path เอาต์พุตสำหรับ `--export`

ความเป็นส่วนตัวและลักษณะการทำงานของ bundle

  * records เก็บ metadata ด้านปฏิบัติการ: ชื่อเหตุการณ์, จำนวน, ขนาด byte, ค่าหน่วยความจำ, สถานะคิว/เซสชัน, ชื่อช่องทาง/Plugin, และสรุปเซสชันที่ redact แล้ว โดยไม่เก็บข้อความแชท, body ของ Webhook, เอาต์พุตของเครื่องมือ, body คำขอหรือคำตอบดิบ, token, cookie, ค่าลับ, hostname, หรือ session id ดิบ ตั้งค่า `diagnostics.enabled: false` เพื่อปิด recorder ทั้งหมด
  * เมื่อ Gateway ออกแบบ fatal, shutdown timeout, และ restart startup failure, OpenClaw จะเขียน snapshot diagnostics เดียวกันไปที่ `~/.openclaw/logs/stability/openclaw-stability-*.json` เมื่อ recorder มีเหตุการณ์ ตรวจสอบ bundle ใหม่ที่สุดด้วย `openclaw gateway stability --bundle latest`; `--limit`, `--type`, และ `--since-seq` ใช้กับเอาต์พุต bundle ด้วย


### `gateway diagnostics export`

เขียน zip diagnostics ภายในเครื่องที่ออกแบบมาเพื่อแนบกับรายงาน bug สำหรับโมเดลความเป็นส่วนตัวและเนื้อหา bundle ดู [การส่งออก diagnostics](</th/gateway/diagnostics>)

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

ข้ามการค้นหา stability bundle ที่บันทึกไว้

พิมพ์ path ที่เขียน, ขนาด, และ manifest เป็น JSON

export มี manifest, สรุป Markdown, รูปแบบการกำหนดค่า, รายละเอียดการกำหนดค่าที่ sanitize แล้ว, สรุป log ที่ sanitize แล้ว, snapshot status/health ของ Gateway ที่ sanitize แล้ว, และ stability bundle ใหม่ที่สุดเมื่อมีอยู่

สิ่งนี้มีไว้สำหรับแชร์ โดยเก็บรายละเอียดด้านปฏิบัติการที่ช่วย debug เช่น field ของ log OpenClaw ที่ปลอดภัย, ชื่อ subsystem, status code, duration, โหมดที่กำหนดค่าไว้, พอร์ต, รหัส Plugin, รหัส provider, การตั้งค่า feature ที่ไม่ใช่ความลับ, และข้อความ log ด้านปฏิบัติการที่ redact แล้ว โดยละเว้นหรือ redact ข้อความแชท, body ของ Webhook, เอาต์พุตของเครื่องมือ, credentials, cookie, ตัวระบุบัญชี/ข้อความ, ข้อความ prompt/instruction, hostname, และค่าลับ เมื่อข้อความรูปแบบ LogTape ดูเหมือนข้อความ payload ของผู้ใช้/แชท/เครื่องมือ export จะเก็บเฉพาะว่ามีข้อความถูกละเว้น พร้อมจำนวน byte ของข้อความนั้น

### `gateway status`

`gateway status` แสดงบริการ Gateway (launchd/systemd/schtasks) พร้อม probe ทางเลือกสำหรับความสามารถ connectivity/auth

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

ข้าม connectivity probe (มุมมองเฉพาะ service)

สแกน service ระดับระบบด้วย

ยกระดับ connectivity probe เริ่มต้นเป็น read probe และออกด้วยค่าที่ไม่ใช่ศูนย์เมื่อ read probe นั้นล้มเหลว ไม่สามารถใช้ร่วมกับ `--no-probe` ได้

Status semantics

  * `gateway status` ยังคงใช้ได้สำหรับการวินิจฉัย แม้เมื่อ config ของ CLI ภายในเครื่องหายไปหรือไม่ถูกต้อง
  * `gateway status` ค่าเริ่มต้นพิสูจน์สถานะ service, การเชื่อมต่อ WebSocket และความสามารถด้าน auth ที่เห็นได้ในช่วง handshake โดยไม่ได้พิสูจน์การดำเนินการ read/write/admin
  * Diagnostic probe ไม่เปลี่ยนแปลงข้อมูลสำหรับ auth ของอุปกรณ์ครั้งแรก: จะใช้ device token ที่ cache ไว้เดิมเมื่อมีอยู่ แต่จะไม่สร้างตัวตนอุปกรณ์ CLI ใหม่หรือระเบียนการจับคู่อุปกรณ์แบบ read-only ใหม่เพียงเพื่อตรวจสอบสถานะ
  * `gateway status` จะ resolve auth SecretRefs ที่กำหนดค่าไว้สำหรับ probe auth เมื่อทำได้
  * หาก auth SecretRef ที่จำเป็นยัง resolve ไม่ได้ในเส้นทางคำสั่งนี้ `gateway status --json` จะรายงาน `rpc.authWarning` เมื่อ probe connectivity/auth ล้มเหลว; ส่ง `--token`/`--password` อย่างชัดเจน หรือ resolve แหล่ง secret ก่อน
  * หาก probe สำเร็จ คำเตือน auth-ref ที่ยัง resolve ไม่ได้จะถูกซ่อนเพื่อหลีกเลี่ยง false positive
  * ใช้ `--require-rpc` ในสคริปต์และ automation เมื่อ service ที่กำลัง listen อยู่ยังไม่เพียงพอ และคุณต้องการให้การเรียก RPC แบบ read-scope มีสถานะดีด้วย
  * `--deep` เพิ่มการสแกนแบบ best-effort สำหรับการติดตั้ง launchd/systemd/schtasks เพิ่มเติม เมื่อพบ service ที่คล้าย Gateway หลายรายการ เอาต์พุตสำหรับมนุษย์จะพิมพ์คำแนะนำการล้างข้อมูลและเตือนว่าการตั้งค่าส่วนใหญ่ควรรัน Gateway หนึ่งรายการต่อเครื่อง
  * `--deep` ยังรายงานการส่งต่อการ restart ล่าสุดของ Gateway supervisor เมื่อ process ของ service ออกอย่างสะอาดเพื่อให้ supervisor ภายนอก restart
  * `--deep` รันการตรวจสอบ config ในโหมดที่รับรู้ Plugin (`pluginValidation: "full"`) และแสดงคำเตือน manifest ของ Plugin ที่กำหนดค่าไว้ (เช่น metadata ของ channel config ที่หายไป) เพื่อให้ smoke check สำหรับการติดตั้งและอัปเดตตรวจจับได้ `gateway status` ค่าเริ่มต้นยังคงใช้เส้นทาง read-only ที่รวดเร็วซึ่งข้ามการตรวจสอบ Plugin
  * เอาต์พุตสำหรับมนุษย์รวม path ของ log file ที่ resolve แล้ว พร้อม snapshot ของ path/ความถูกต้องของ config ระหว่าง CLI กับ service เพื่อช่วยวินิจฉัย profile หรือ state-dir drift

Linux systemd auth-drift checks

  * บนการติดตั้ง Linux systemd การตรวจ auth drift ของ service จะอ่านค่าทั้ง `Environment=` และ `EnvironmentFile=` จาก unit (รวมถึง `%h`, path ที่ quote ไว้, ไฟล์หลายไฟล์ และไฟล์ optional ที่ขึ้นต้นด้วย `-`)
  * การตรวจ drift จะ resolve `gateway.auth.token` SecretRefs โดยใช้ runtime env ที่ merge แล้ว (env ของคำสั่ง service ก่อน จากนั้น fallback เป็น process env)
  * หาก token auth ไม่ได้ active อย่างมีผลจริง (`gateway.auth.mode` แบบชัดเจนเป็น `password`/`none`/`trusted-proxy` หรือไม่ได้ตั้ง mode โดยที่ password อาจชนะได้และไม่มี token candidate ใดชนะได้) การตรวจ token-drift จะข้ามการ resolve config token


### `gateway probe`

`gateway probe` คือคำสั่ง "debug everything" โดยจะ probe เสมอ:

  * Gateway remote ที่คุณกำหนดค่าไว้ (หากตั้งไว้), และ
  * localhost (loopback) **แม้จะกำหนด remote ไว้ก็ตาม**


หากคุณส่ง `--url` เป้าหมายที่ระบุชัดเจนนั้นจะถูกเพิ่มไว้ก่อนทั้งสองรายการ เอาต์พุตสำหรับมนุษย์ติดป้ายเป้าหมายเป็น:

  * `URL (ระบุชัดเจน)`
  * `Remote (กำหนดค่าไว้)` หรือ `Remote (กำหนดค่าไว้, ไม่ active)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

Interpretation

  * `Reachable: yes` หมายถึงมีเป้าหมายอย่างน้อยหนึ่งรายการที่ยอมรับการเชื่อมต่อ WebSocket
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` รายงานสิ่งที่ probe พิสูจน์ได้เกี่ยวกับ auth ซึ่งแยกจาก reachability
  * `Read probe: ok` หมายถึงการเรียก RPC รายละเอียดแบบ read-scope (`health`/`status`/`system-presence`/`config.get`) สำเร็จด้วย
  * `Read probe: limited - missing scope: operator.read` หมายถึงเชื่อมต่อสำเร็จ แต่ RPC แบบ read-scope ถูกจำกัด รายงานเป็น reachability แบบ **degraded** ไม่ใช่ความล้มเหลวทั้งหมด
  * `Read probe: failed` หลัง `Connect: ok` หมายถึง Gateway ยอมรับการเชื่อมต่อ WebSocket แล้ว แต่การวินิจฉัย read ที่ตามมาหมดเวลาหรือล้มเหลว ซึ่งเป็น reachability แบบ **degraded** เช่นกัน ไม่ใช่ Gateway ที่เข้าถึงไม่ได้
  * เช่นเดียวกับ `gateway status` probe จะใช้ auth ของอุปกรณ์ที่ cache ไว้เดิม แต่จะไม่สร้างตัวตนอุปกรณ์หรือสถานะการจับคู่ครั้งแรก
  * Exit code จะไม่ใช่ศูนย์เฉพาะเมื่อไม่มีเป้าหมายที่ probe แล้วเข้าถึงได้

JSON output

ระดับบนสุด:

  * `ok`: มีเป้าหมายอย่างน้อยหนึ่งรายการที่เข้าถึงได้
  * `degraded`: มีเป้าหมายอย่างน้อยหนึ่งรายการที่ยอมรับการเชื่อมต่อ แต่ไม่ได้ทำการวินิจฉัย RPC รายละเอียดอย่างครบถ้วน
  * `capability`: ความสามารถที่ดีที่สุดที่พบในเป้าหมายที่เข้าถึงได้ (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope` หรือ `unknown`)
  * `primaryTargetId`: เป้าหมายที่ดีที่สุดให้ถือเป็นผู้ชนะที่ active ตามลำดับนี้: URL ที่ระบุชัดเจน, SSH tunnel, remote ที่กำหนดค่าไว้, จากนั้น local loopback
  * `warnings[]`: ระเบียนคำเตือนแบบ best-effort ที่มี `code`, `message` และ `targetIds` แบบ optional
  * `network`: hint URL ของ local loopback/tailnet ที่ได้จาก config ปัจจุบันและระบบเครือข่ายของ host
  * `discovery.timeoutMs` และ `discovery.count`: budget/result count ของ discovery จริงที่ใช้สำหรับรอบ probe นี้


ต่อเป้าหมาย (`targets[].connect`):

  * `ok`: reachability หลัง connect + การจัดประเภท degraded
  * `rpcOk`: RPC รายละเอียดเต็มสำเร็จ
  * `scopeLimited`: RPC รายละเอียดล้มเหลวเนื่องจากขาด operator scope


ต่อเป้าหมาย (`targets[].auth`):

  * `role`: บทบาท auth ที่รายงานใน `hello-ok` เมื่อมี
  * `scopes`: scope ที่ได้รับซึ่งรายงานใน `hello-ok` เมื่อมี
  * `capability`: การจัดประเภทความสามารถ auth ที่แสดงสำหรับเป้าหมายนั้น

Common warning codes

  * `ssh_tunnel_failed`: การตั้งค่า SSH tunnel ล้มเหลว; คำสั่ง fallback ไปใช้ direct probe
  * `multiple_gateways`: มีเป้าหมายมากกว่าหนึ่งรายการที่เข้าถึงได้; เป็นกรณีไม่ปกติ เว้นแต่คุณตั้งใจรัน profile ที่แยกกัน เช่น bot สำหรับกู้คืน
  * `auth_secretref_unresolved`: auth SecretRef ที่กำหนดค่าไว้ไม่สามารถ resolve ได้สำหรับเป้าหมายที่ล้มเหลว
  * `probe_scope_limited`: การเชื่อมต่อ WebSocket สำเร็จ แต่ read probe ถูกจำกัดเนื่องจากขาด `operator.read`


#### Remote ผ่าน SSH (ความเทียบเท่ากับแอป Mac)

โหมด "Remote over SSH" ของแอป macOS ใช้ local port-forward เพื่อให้ Gateway remote (ซึ่งอาจ bind กับ loopback เท่านั้น) เข้าถึงได้ที่ `ws://127.0.0.1:<port>`

CLI ที่เทียบเท่า:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` หรือ `user@host:port` (port มีค่าเริ่มต้นเป็น `22`)

เลือก host ของ Gateway รายการแรกที่ค้นพบเป็นเป้าหมาย SSH จาก endpoint ของ discovery ที่ resolve แล้ว (`local.` บวกกับโดเมน wide-area ที่กำหนดค่าไว้ หากมี) hint แบบ TXT-only จะถูกละเว้น

Config (optional, ใช้เป็นค่าเริ่มต้น):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

ตัวช่วย RPC ระดับต่ำ

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

ส่วนใหญ่สำหรับ RPC แบบ agent-style ที่ stream event ขั้นกลางก่อน payload สุดท้าย

เอาต์พุต JSON ที่อ่านได้โดยเครื่อง

## จัดการ service ของ Gateway

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### ติดตั้งด้วย wrapper

ใช้ `--wrapper` เมื่อ service ที่จัดการอยู่ต้องเริ่มผ่าน executable อื่น เช่น shim ของ secrets manager หรือ helper สำหรับ run-as wrapper จะได้รับ args ปกติของ Gateway และ รับผิดชอบในการ exec `openclaw` หรือ Node พร้อม args เหล่านั้นในท้ายที่สุด

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

คุณยังสามารถตั้งค่า wrapper ผ่าน environment ได้ `gateway install` จะตรวจสอบว่า path เป็น ไฟล์ executable, เขียน wrapper ลงใน service `ProgramArguments` และบันทึก `OPENCLAW_WRAPPER` ไว้ใน environment ของ service สำหรับการ reinstall, update และการซ่อมแซมด้วย doctor แบบบังคับในภายหลัง

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

หากต้องการลบ wrapper ที่บันทึกไว้ ให้ล้าง `OPENCLAW_WRAPPER` ระหว่าง reinstall:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Command options

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

พฤติกรรมวงจรชีวิต

  * ใช้ `gateway restart` เพื่อรีสตาร์ตบริการที่จัดการอยู่ อย่าต่อคำสั่ง `gateway stop` และ `gateway start` เพื่อใช้แทนการรีสตาร์ต
  * บน macOS, `gateway stop` ใช้ `launchctl bootout` เป็นค่าเริ่มต้น ซึ่งลบ LaunchAgent ออกจากเซสชันการบูตปัจจุบันโดยไม่คงการปิดใช้งานไว้ — การกู้คืนอัตโนมัติของ KeepAlive ยังคงเปิดใช้งานสำหรับการขัดข้องในอนาคต และ `gateway start` เปิดใช้งานใหม่ได้อย่างสะอาดโดยไม่ต้องสั่ง `launchctl enable` ด้วยตนเอง ส่ง `--disable` เพื่อระงับ KeepAlive และ RunAtLoad แบบถาวร เพื่อไม่ให้ gateway เริ่มทำงานใหม่จนกว่าจะสั่ง `gateway start` อย่างชัดเจนครั้งถัดไป ใช้ตัวเลือกนี้เมื่อการหยุดด้วยตนเองควรคงอยู่หลังการรีบูตหรือการรีสตาร์ตระบบ
  * `gateway restart --safe` ขอให้ Gateway ที่กำลังทำงานอยู่ตรวจล่วงหน้างาน OpenClaw ที่ยังทำงานอยู่ และเลื่อนการรีสตาร์ตจนกว่าการส่งคำตอบ การรันแบบฝัง และการรันงานจะระบายหมด `--safe` ใช้ร่วมกับ `--force` หรือ `--wait` ไม่ได้
  * `gateway restart --wait 30s` เขียนทับงบเวลาระบายงานก่อนรีสตาร์ตที่กำหนดค่าไว้สำหรับการรีสตาร์ตครั้งนั้น ตัวเลขล้วนเป็นมิลลิวินาที ยอมรับหน่วยอย่าง `s`, `m` และ `h` ได้ `--wait 0` จะรอไม่มีกำหนด
  * `gateway restart --safe --skip-deferral` รันการรีสตาร์ตอย่างปลอดภัยที่รับรู้งาน OpenClaw แต่ข้ามด่านการเลื่อนเวลา เพื่อให้ Gateway ส่งสัญญาณรีสตาร์ตทันทีแม้มีรายงานตัวบล็อกอยู่ เป็นทางออกฉุกเฉินสำหรับผู้ปฏิบัติงานเมื่อการเลื่อนเวลาจากงานที่ค้างอยู่หยุดชะงัก ต้องใช้ `--safe`
  * `gateway restart --force` ข้ามการระบายงานที่ยังทำงานอยู่และรีสตาร์ตทันที ใช้เมื่่อผู้ปฏิบัติงานตรวจสอบตัวบล็อกงานที่แสดงไว้แล้วและต้องการให้ gateway กลับมาทันที
  * คำสั่งวงจรชีวิตรองรับ `--json` สำหรับการเขียนสคริปต์

Auth และ SecretRefs ขณะติดตั้ง

  * เมื่อ token auth ต้องใช้โทเค็นและ `gateway.auth.token` จัดการโดย SecretRef, `gateway install` จะตรวจสอบว่า SecretRef แก้ค่าได้ แต่จะไม่คงโทเค็นที่แก้ค่าแล้วไว้ในข้อมูลเมตาสภาพแวดล้อมของบริการ
  * หาก token auth ต้องใช้โทเค็นและ SecretRef ของโทเค็นที่กำหนดค่าไว้แก้ค่าไม่ได้ การติดตั้งจะล้มเหลวแบบปิดแทนที่จะคง fallback plaintext ไว้
  * สำหรับ password auth บน `gateway run` ควรใช้ `OPENCLAW_GATEWAY_PASSWORD`, `--password-file` หรือ `gateway.auth.password` ที่มี SecretRef รองรับ แทน `--password` แบบอินไลน์
  * ในโหมด auth ที่อนุมานได้ `OPENCLAW_GATEWAY_PASSWORD` ที่มีเฉพาะใน shell จะไม่ผ่อนปรนข้อกำหนดโทเค็นสำหรับการติดตั้ง ใช้การกำหนดค่าที่คงทน (`gateway.auth.password` หรือ config `env`) เมื่อติดตั้งบริการที่จัดการอยู่
  * หากกำหนดค่าทั้ง `gateway.auth.token` และ `gateway.auth.password` และไม่ได้ตั้งค่า `gateway.auth.mode` การติดตั้งจะถูกบล็อกจนกว่าจะตั้งค่าโหมดอย่างชัดเจน


## ค้นหา gateway (Bonjour)

`gateway discover` สแกนหา beacon ของ Gateway (`_openclaw-gw._tcp`)

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): เลือกโดเมนหนึ่ง (ตัวอย่าง: `openclaw.internal.`) และตั้งค่า split DNS + เซิร์ฟเวอร์ DNS ดู [Bonjour](</th/gateway/bonjour>)


เฉพาะ gateway ที่เปิดใช้งานการค้นหา Bonjour (ค่าเริ่มต้น) เท่านั้นที่จะประกาศ beacon

เรคคอร์ดการค้นหาแบบ wide-area สามารถมีคำใบ้ TXT เหล่านี้ได้:

  * `role` (คำใบ้บทบาท gateway)
  * `transport` (คำใบ้ transport เช่น `gateway`)
  * `gatewayPort` (พอร์ต WebSocket โดยปกติคือ `18789`)
  * `sshPort` (เฉพาะโหมดการค้นหาแบบเต็มเท่านั้น; ไคลเอนต์จะใช้เป้าหมาย SSH เริ่มต้นเป็น `22` เมื่อไม่มีค่านี้)
  * `tailnetDns` (ชื่อโฮสต์ MagicDNS เมื่อมี)
  * `gatewayTls` / `gatewayTlsSha256` (เปิดใช้งาน TLS + ลายนิ้วมือใบรับรอง)
  * `cliPath` (เฉพาะโหมดการค้นหาแบบเต็มเท่านั้น)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

เอาต์พุตที่เครื่องอ่านได้ (และปิดใช้งานการจัดสไตล์/สปินเนอร์ด้วย)

ตัวอย่าง:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## ที่เกี่ยวข้อง

  * [ข้อมูลอ้างอิง CLI](</th/cli>)
  * [Runbook ของ Gateway](</th/gateway>)


Was this useful?YesNo