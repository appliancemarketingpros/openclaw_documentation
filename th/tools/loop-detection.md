---
title: การตรวจจับลูปของเครื่องมือ
source_url: https://docs.openclaw.ai/th/tools/loop-detection
scraped_at: 2026-05-25
---

OpenClaw มี guardrails สองแบบที่ทำงานร่วมกันสำหรับรูปแบบการเรียกใช้เครื่องมือซ้ำ ๆ:

  1. **การตรวจจับลูป** (`tools.loopDetection.enabled`) — ปิดใช้งานโดยค่าเริ่มต้น เฝ้าดูประวัติการเรียกใช้เครื่องมือแบบเลื่อนหน้าต่างเพื่อหารูปแบบที่เกิดซ้ำและการลองใหม่กับเครื่องมือที่ไม่รู้จัก
  2. **Guard หลัง Compaction** (`tools.loopDetection.postCompactionGuard`) — เปิดใช้งานโดยค่าเริ่มต้น เว้นแต่ `tools.loopDetection.enabled` จะเป็น `false` อย่างชัดเจน จะทำงานหลังการลองใหม่หลัง Compaction ทุกครั้ง และยุติการรันเมื่อเอเจนต์ส่งทริปเปิล `(tool, args, result)` เดิมภายในหน้าต่าง


ทั้งสองอย่างกำหนดค่าอยู่ใต้บล็อก `tools.loopDetection` เดียวกัน แต่ Guard หลัง Compaction จะทำงานเสมอเมื่อสวิตช์หลักไม่ได้ถูกปิดอย่างชัดเจน ตั้งค่า `tools.loopDetection.enabled: false` เพื่อปิดทั้งสองส่วน

## เหตุผลที่มีสิ่งนี้

  * ตรวจจับลำดับที่เกิดซ้ำซึ่งไม่ทำให้เกิดความคืบหน้า
  * ตรวจจับลูปที่ไม่มีผลลัพธ์ด้วยความถี่สูง (เครื่องมือเดียวกัน อินพุตเดียวกัน ข้อผิดพลาดซ้ำ)
  * ตรวจจับรูปแบบการเรียกซ้ำเฉพาะสำหรับเครื่องมือ polling ที่รู้จัก
  * ป้องกันวงจรบริบทล้น จากนั้นทำ Compaction แล้วกลับเข้าสู่ลูปเดิมไม่ให้รันไปเรื่อย ๆ


## บล็อกการกำหนดค่า

ค่าเริ่มต้นส่วนกลาง พร้อมแสดงทุกฟิลด์ที่มีเอกสารกำกับ:

json5Copy code
[code]
    {  tools: {    loopDetection: {      enabled: false, // master switch for the rolling-history detectors      historySize: 30,      warningThreshold: 10,      criticalThreshold: 20,      unknownToolThreshold: 10,      globalCircuitBreakerThreshold: 30,      detectors: {        genericRepeat: true,        knownPollNoProgress: true,        pingPong: true,      },      postCompactionGuard: {        windowSize: 3, // armed after compaction-retry; runs unless enabled is explicitly false      },    },  },}
[/code]

การเขียนทับรายเอเจนต์ (ไม่บังคับ):

json5Copy code
[code]
    {  agents: {    list: [      {        id: "safe-runner",        tools: {          loopDetection: {            enabled: true,            warningThreshold: 8,            criticalThreshold: 16,          },        },      },    ],  },}
[/code]

### พฤติกรรมของฟิลด์

ฟิลด์ | ค่าเริ่มต้น | ผล  
---|---|---  
`enabled` | `false` | สวิตช์หลักสำหรับตัวตรวจจับประวัติแบบเลื่อนหน้าต่าง การตั้งค่าเป็น `false` จะปิด Guard หลัง Compaction ด้วย  
`historySize` | `30` | จำนวนการเรียกใช้เครื่องมือล่าสุดที่เก็บไว้เพื่อวิเคราะห์  
`warningThreshold` | `10` | เกณฑ์ก่อนที่รูปแบบจะถูกจัดประเภทเป็นเพียงคำเตือน  
`criticalThreshold` | `20` | เกณฑ์สำหรับบล็อกรูปแบบลูปที่เกิดซ้ำและไม่มีความคืบหน้า  
`unknownToolThreshold` | `10` | บล็อกการเรียกซ้ำไปยังเครื่องมือเดิมที่ไม่พร้อมใช้งานหลังจากพลาดครบจำนวนนี้  
`globalCircuitBreakerThreshold` | `30` | เกณฑ์ breaker ส่วนกลางสำหรับกรณีไม่มีความคืบหน้าข้ามตัวตรวจจับทั้งหมด  
`detectors.genericRepeat` | `true` | เตือนเมื่อพบรูปแบบเครื่องมือเดิม + พารามิเตอร์เดิมซ้ำ และบล็อกเมื่อการเรียกเดิมยังให้ผลลัพธ์เหมือนกันด้วย  
`detectors.knownPollNoProgress` | `true` | ตรวจจับรูปแบบที่คล้าย polling ซึ่งรู้จักและไม่มีการเปลี่ยนสถานะ  
`detectors.pingPong` | `true` | ตรวจจับรูปแบบ ping-pong สลับไปมา  
`postCompactionGuard.windowSize` | `3` | จำนวนการเรียกใช้เครื่องมือหลัง Compaction ที่ Guard ยังคงทำงานอยู่ และจำนวนทริปเปิลที่เหมือนกันซึ่งจะยุติการรัน  
  
สำหรับ `exec` การตรวจสอบว่าไม่มีความคืบหน้าจะเปรียบเทียบผลลัพธ์คำสั่งที่เสถียร และละเว้นเมทาดาทารันไทม์ที่เปลี่ยนแปลงได้ เช่น ระยะเวลา, PID, session ID และไดเรกทอรีทำงาน เมื่อมี run id ประวัติการเรียกใช้เครื่องมือล่าสุดจะถูกประเมินเฉพาะภายในรันนั้น เพื่อให้รอบ Heartbeat ที่กำหนดเวลาไว้และรันใหม่ไม่สืบทอดจำนวนลูปค้างจากรันก่อนหน้า

## การตั้งค่าที่แนะนำ

  * สำหรับโมเดลขนาดเล็ก ให้ตั้ง `enabled: true` และปล่อยเกณฑ์ต่าง ๆ ไว้ตามค่าเริ่มต้น โมเดลระดับเรือธงมักไม่จำเป็นต้องใช้การตรวจจับประวัติแบบเลื่อนหน้าต่าง และสามารถปล่อยสวิตช์หลักไว้ที่ `false` ขณะยังได้ประโยชน์จาก Guard หลัง Compaction
  * รักษาลำดับเกณฑ์เป็น `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold`
  * หากเกิด false positive: 
    * เพิ่ม `warningThreshold` และ/หรือ `criticalThreshold`
    * อาจเพิ่ม `globalCircuitBreakerThreshold`
    * ปิดเฉพาะตัวตรวจจับที่ทำให้เกิดปัญหา (`detectors.<name>: false`)
    * ลด `historySize` เพื่อให้บริบทเชิงประวัติเข้มงวดน้อยลง
  * หากต้องการปิดทุกอย่าง (รวมถึง Guard หลัง Compaction) ให้ตั้ง `tools.loopDetection.enabled: false` อย่างชัดเจน


## Guard หลัง Compaction

เมื่อ runner ทำการลองใหม่หลัง Compaction เสร็จหลังจากบริบทล้น มันจะเปิด Guard แบบหน้าต่างสั้นที่เฝ้าดูการเรียกใช้เครื่องมือสองสามครั้งถัดไป หากเอเจนต์ส่งทริปเปิล `(toolName, argsHash, resultHash)` เดิมหลายครั้งภายในหน้าต่าง Guard จะสรุปว่า Compaction ไม่ได้ทำให้หลุดจากลูป และยุติการรันด้วยข้อผิดพลาด `compaction_loop_persisted`

Guard ถูกควบคุมโดยแฟล็กหลัก `tools.loopDetection.enabled` โดยมีเงื่อนไขพิเศษหนึ่งอย่าง: Guard จะยัง **เปิดใช้งานเมื่อไม่ได้ตั้งค่าแฟล็กหรือเป็น`true`** และจะปิดเฉพาะเมื่อแฟล็กเป็น `false` อย่างชัดเจน นี่เป็นพฤติกรรมตั้งใจ Guard นี้มีไว้เพื่อหนีจากลูป Compaction ที่ไม่เช่นนั้นจะเผาผลาญโทเค็นอย่างไม่จำกัด ดังนั้นผู้ใช้ที่ไม่ได้ตั้งค่าใด ๆ ก็ยังได้รับการป้องกัน

json5Copy code
[code]
    {  tools: {    loopDetection: {      // master switch; set false to disable the guard along with the rolling detectors      enabled: true,      postCompactionGuard: {        windowSize: 3, // default      },    },  },}
[/code]

  * `windowSize` ต่ำกว่าจะเข้มงวดกว่า (พยายามได้น้อยครั้งก่อนยุติ)
  * `windowSize` สูงกว่าจะให้เอเจนต์มีโอกาสกู้คืนมากขึ้น
  * Guard จะไม่ยุติการทำงานเมื่อผลลัพธ์กำลังเปลี่ยนแปลง จะยุติเฉพาะเมื่อผลลัพธ์เหมือนกันระดับไบต์ตลอดหน้าต่าง
  * Guard นี้ถูกตั้งใจให้มีขอบเขตแคบ: ทำงานเฉพาะทันทีหลังการลองใหม่หลัง Compaction


## บันทึกและพฤติกรรมที่คาดหวัง

เมื่อตรวจพบลูป OpenClaw จะรายงานเหตุการณ์ลูป และจะลดทอนหรือบล็อกรอบการใช้เครื่องมือถัดไปตามระดับความรุนแรง วิธีนี้ช่วยปกป้องผู้ใช้จากการใช้โทเค็น runaway และการค้าง ขณะยังคงรักษาการเข้าถึงเครื่องมือตามปกติ

  * คำเตือนจะมาก่อน
  * การระงับจะตามมาเมื่อรูปแบบยังคงอยู่เกินเกณฑ์คำเตือน
  * เกณฑ์วิกฤติจะบล็อกรอบการใช้เครื่องมือถัดไป และแสดงเหตุผลการตรวจจับลูปที่ชัดเจนในบันทึกรัน
  * Guard หลัง Compaction จะส่งข้อผิดพลาด `compaction_loop_persisted` พร้อมชื่อเครื่องมือที่เป็นปัญหาและจำนวนการเรียกที่เหมือนกัน


## ที่เกี่ยวข้อง

[**การอนุมัติ Exec** นโยบายอนุญาต/ปฏิเสธสำหรับการเรียกใช้เชลล์ ](</th/tools/exec-approvals>) [**ระดับการคิด** ระดับความพยายามในการใช้เหตุผลและการทำงานร่วมกับนโยบายของผู้ให้บริการ ](</th/tools/thinking>) [**เอเจนต์ย่อย** การสร้างเอเจนต์แยกเพื่อจำกัดพฤติกรรม runaway ](</th/tools/subagents>) [**เอกสารอ้างอิงการกำหนดค่า** สคีมา `tools.loopDetection` แบบเต็มและ semantics การผสาน ](</th/gateway/configuration-reference>)

Was this useful?YesNo