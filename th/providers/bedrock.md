---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/th/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw สามารถใช้โมเดล **Amazon Bedrock** ผ่านผู้ให้บริการสตรีมมิง **Bedrock Converse** ของ pi-ai ได้ การยืนยันตัวตนของ Bedrock ใช้ **AWS SDK default credential chain** ไม่ใช่ API key

คุณสมบัติ | ค่า  
---|---  
ผู้ให้บริการ | `amazon-bedrock`  
API | `bedrock-converse-stream`  
การยืนยันตัวตน | ข้อมูลรับรอง AWS (ตัวแปรสภาพแวดล้อม, shared config, หรือ instance role)  
Region | `AWS_REGION` หรือ `AWS_DEFAULT_REGION` (ค่าเริ่มต้น: `us-east-1`)  
  
## เริ่มต้นใช้งาน

เลือกวิธียืนยันตัวตนที่คุณต้องการ แล้วทำตามขั้นตอนการตั้งค่า

### Access keys / ตัวแปรสภาพแวดล้อม

**เหมาะที่สุดสำหรับ:** เครื่องของนักพัฒนา, CI, หรือโฮสต์ที่คุณจัดการข้อมูลรับรอง AWS โดยตรง

* ### ตั้งค่าข้อมูลรับรอง AWS บนโฮสต์ Gateway

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### เพิ่มผู้ให้บริการและโมเดล Bedrock ลงใน config ของคุณ

ไม่จำเป็นต้องมี `apiKey` กำหนดค่าผู้ให้บริการด้วย `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### ตรวจสอบว่ามีโมเดลพร้อมใช้งาน

bashCopy code
[code]
    openclaw models list
[/code]

### EC2 instance roles (IMDS)

**เหมาะที่สุดสำหรับ:** อินสแตนซ์ EC2 ที่มี IAM role แนบอยู่ โดยใช้ instance metadata service สำหรับการยืนยันตัวตน

* ### เปิดใช้งานการค้นพบอย่างชัดเจน

เมื่อใช้ IMDS OpenClaw ไม่สามารถตรวจจับการยืนยันตัวตน AWS จาก env markers เพียงอย่างเดียวได้ ดังนั้นคุณต้องเลือกเปิดใช้:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### เลือกเพิ่ม env marker สำหรับโหมดอัตโนมัติ

หากคุณต้องการให้เส้นทางการตรวจจับอัตโนมัติแบบ env-marker ทำงานด้วย (เช่น สำหรับพื้นผิว `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

คุณ **ไม่** จำเป็นต้องมี API key ปลอม

* ### ตรวจสอบว่าค้นพบโมเดลแล้ว

bashCopy code
[code]
    openclaw models list
[/code]

## การค้นพบโมเดลอัตโนมัติ

OpenClaw สามารถค้นพบโมเดล Bedrock ที่รองรับ **สตรีมมิง** และ **เอาต์พุตข้อความ** ได้โดยอัตโนมัติ การค้นพบใช้ `bedrock:ListFoundationModels` และ `bedrock:ListInferenceProfiles` และผลลัพธ์จะถูกแคชไว้ (ค่าเริ่มต้น: 1 ชั่วโมง)

วิธีเปิดใช้งานผู้ให้บริการแบบแฝง:

  * หาก `plugins.entries.amazon-bedrock.config.discovery.enabled` เป็น `true` OpenClaw จะพยายามค้นพบแม้ไม่มี AWS env marker อยู่
  * หากไม่ได้ตั้งค่า `plugins.entries.amazon-bedrock.config.discovery.enabled` OpenClaw จะเพิ่มผู้ให้บริการ Bedrock แบบแฝงโดยอัตโนมัติเฉพาะเมื่อเห็นหนึ่งใน AWS auth markers เหล่านี้: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, หรือ `AWS_PROFILE`
  * เส้นทางการยืนยันตัวตน runtime ของ Bedrock จริงยังคงใช้ AWS SDK default chain ดังนั้น shared config, SSO, และการยืนยันตัวตนด้วย IMDS instance-role จึงทำงานได้แม้เมื่อการค้นพบ ต้องใช้ `enabled: true` เพื่อเลือกเปิดใช้


ตัวเลือก config สำหรับการค้นพบ

ตัวเลือก config อยู่ใต้ `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

ตัวเลือก | ค่าเริ่มต้น | คำอธิบาย  
---|---|---  
`enabled` | auto | ในโหมดอัตโนมัติ OpenClaw จะเปิดใช้ผู้ให้บริการ Bedrock แบบแฝงเฉพาะเมื่อเห็น AWS env marker ที่รองรับ ตั้งค่าเป็น `true` เพื่อบังคับการค้นพบ  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | AWS region ที่ใช้สำหรับการเรียก API การค้นพบ  
`providerFilter` | (ทั้งหมด) | จับคู่ชื่อผู้ให้บริการ Bedrock (เช่น `anthropic`, `amazon`)  
`refreshInterval` | `3600` | ระยะเวลาแคชเป็นวินาที ตั้งค่าเป็น `0` เพื่อปิดใช้งานการแคช  
`defaultContextWindow` | `32000` | หน้าต่างบริบทที่ใช้สำหรับโมเดลที่ค้นพบ (override หากคุณทราบขีดจำกัดของโมเดล)  
`defaultMaxTokens` | `4096` | จำนวนโทเค็นเอาต์พุตสูงสุดที่ใช้สำหรับโมเดลที่ค้นพบ (override หากคุณทราบขีดจำกัดของโมเดล)  
  
## การตั้งค่าอย่างรวดเร็ว (เส้นทาง AWS)

คำแนะนำนี้จะสร้าง IAM role, แนบสิทธิ์ Bedrock, เชื่อมโยง instance profile, และเปิดใช้งานการค้นพบของ OpenClaw บนโฮสต์ EC2

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## การกำหนดค่าขั้นสูง

Inference profiles

OpenClaw ค้นพบ **regional และ global inference profiles** ควบคู่ไปกับ foundation models เมื่อ profile แมปกับ foundation model ที่รู้จัก profile จะสืบทอดความสามารถของโมเดลนั้น (หน้าต่างบริบท, โทเค็นสูงสุด, reasoning, vision) และจะ inject region คำขอ Bedrock ที่ถูกต้อง โดยอัตโนมัติ ซึ่งหมายความว่าโปรไฟล์ Claude ข้าม region ทำงานได้โดยไม่ต้อง override ผู้ให้บริการด้วยตนเอง

ID ของ inference profile จะมีรูปแบบเช่น `us.anthropic.claude-opus-4-6-v1:0` (regional) หรือ `anthropic.claude-opus-4-6-v1:0` (global) หากโมเดลที่รองรับมีอยู่แล้ว ในผลลัพธ์การค้นพบ profile จะสืบทอดชุดความสามารถทั้งหมดของโมเดลนั้น มิฉะนั้นจะใช้ค่าเริ่มต้นที่ปลอดภัย

ไม่จำเป็นต้องมีการกำหนดค่าเพิ่มเติม ตราบใดที่เปิดใช้งานการค้นพบและ IAM principal มี `bedrock:ListInferenceProfiles` profiles จะปรากฏควบคู่กับ foundation models ใน `openclaw models list`

Service tier

โมเดล Bedrock บางรุ่นรองรับพารามิเตอร์ `service_tier` เพื่อเพิ่มประสิทธิภาพด้านต้นทุน หรือ latency มี tier ต่อไปนี้พร้อมใช้งาน:

Tier | คำอธิบาย  
---|---  
`default` | tier มาตรฐานของ Bedrock  
`flex` | การประมวลผลแบบมีส่วนลดสำหรับ workload ที่ทนต่อ latency ที่ยาวขึ้นได้  
`priority` | การประมวลผลแบบจัดลำดับความสำคัญสำหรับ workload ที่ไวต่อ latency  
`reserved` | ความจุที่จองไว้สำหรับ workload แบบ steady-state  
  
ตั้งค่า `serviceTier` (หรือ `service_tier`) ผ่าน `agents.defaults.params` สำหรับ คำขอโมเดล Bedrock หรือกำหนดต่อโมเดลใน `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

ค่าที่ใช้ได้คือ `default`, `flex`, `priority`, และ `reserved` ไม่ใช่ทุก โมเดลจะรองรับทุก tier หากขอ tier ที่ไม่รองรับ Bedrock จะ คืนข้อผิดพลาดการตรวจสอบความถูกต้อง หมายเหตุ: ข้อความข้อผิดพลาดค่อนข้างทำให้เข้าใจผิด อาจระบุว่า "The provided model identifier is invalid" แทนที่จะชี้ว่า service tier ไม่รองรับ หากคุณเห็นข้อผิดพลาดนี้ ให้ตรวจสอบว่าโมเดล รองรับ tier ที่ร้องขอหรือไม่

Claude Opus 4.7 temperature

Bedrock ปฏิเสธพารามิเตอร์ `temperature` สำหรับ Claude Opus 4.7 OpenClaw จะละเว้น `temperature` โดยอัตโนมัติสำหรับ Bedrock ref ของ Opus 4.7 ใด ๆ รวมถึง ID ของ foundation model, inference profiles ที่มีชื่อ, application inference profiles ที่โมเดลเบื้องหลัง resolve เป็น Opus 4.7 ผ่าน `bedrock:GetInferenceProfile`, และตัวแปร `opus-4.7` แบบมีจุดพร้อม คำนำหน้า region ที่เลือกใช้ได้ (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`) ไม่จำเป็นต้องมีปุ่ม config และการละเว้นนี้มีผลกับทั้ง อ็อบเจ็กต์ตัวเลือกคำขอและฟิลด์ payload `inferenceConfig`

Guardrails

คุณสามารถใช้ [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) กับการเรียกใช้โมเดล Bedrock ทั้งหมดได้โดยเพิ่มออบเจ็กต์ `guardrail` ลงในการกำหนดค่า Plugin `amazon-bedrock` Guardrails ช่วยให้คุณบังคับใช้การกรองเนื้อหา, การปฏิเสธหัวข้อ, ตัวกรองคำ, ตัวกรองข้อมูลที่ละเอียดอ่อน และการตรวจสอบ การยึดโยงตามบริบทได้

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

ตัวเลือก | จำเป็น | คำอธิบาย  
---|---|---  
`guardrailIdentifier` | ใช่ | ID ของ Guardrail (เช่น `abc123`) หรือ ARN แบบเต็ม (เช่น `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`)  
`guardrailVersion` | ใช่ | หมายเลขเวอร์ชันที่เผยแพร่แล้ว หรือ `"DRAFT"` สำหรับฉบับร่างที่กำลังทำงาน  
`streamProcessingMode` | ไม่ | `"sync"` หรือ `"async"` สำหรับการประเมิน Guardrail ระหว่างการสตรีม หากละไว้ Bedrock จะใช้ค่าเริ่มต้นของตัวเอง  
`trace` | ไม่ | `"enabled"` หรือ `"enabled_full"` สำหรับการดีบัก; ละไว้หรือตั้งเป็น `"disabled"` สำหรับการใช้งานจริง  
Embeddings for memory search

Bedrock ยังสามารถทำหน้าที่เป็นผู้ให้บริการ embedding สำหรับ [การค้นหาหน่วยความจำ](</th/concepts/memory-search>) ได้ด้วย การตั้งค่านี้แยกจาก ผู้ให้บริการ inference โดยตั้งค่า `agents.defaults.memorySearch.provider` เป็น `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Embedding ของ Bedrock ใช้ลำดับข้อมูลรับรองของ AWS SDK เดียวกับ inference (บทบาทของอินสแตนซ์, SSO, access keys, shared config และ web identity) ไม่ต้องใช้ API key เมื่อ `provider` เป็น `"auto"` Bedrock จะถูกตรวจพบโดยอัตโนมัติหาก ลำดับข้อมูลรับรองนั้น resolve สำเร็จ

โมเดล embedding ที่รองรับรวมถึง Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) และ TwelveLabs Marengo ดู [ข้อมูลอ้างอิงการกำหนดค่าหน่วยความจำ -- Bedrock](</th/reference/memory-config#bedrock-embedding-config>) สำหรับรายการโมเดลทั้งหมดและตัวเลือกมิติ

Notes and caveats

  * Bedrock ต้องเปิดใช้ **model access** ในบัญชี/ภูมิภาค AWS ของคุณ
  * การค้นพบอัตโนมัติต้องมีสิทธิ์ `bedrock:ListFoundationModels` และ `bedrock:ListInferenceProfiles`
  * หากคุณพึ่งพาโหมดอัตโนมัติ ให้ตั้งค่าเครื่องหมาย env สำหรับการยืนยันตัวตน AWS ที่รองรับอย่างใดอย่างหนึ่งบน โฮสต์ Gateway หากคุณต้องการการยืนยันตัวตนแบบ IMDS/shared-config โดยไม่มีเครื่องหมาย env ให้ตั้งค่า `plugins.entries.amazon-bedrock.config.discovery.enabled: true`
  * OpenClaw แสดงแหล่งที่มาของข้อมูลรับรองตามลำดับนี้: `AWS_BEARER_TOKEN_BEDROCK`, จากนั้น `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, จากนั้น `AWS_PROFILE`, จากนั้น ลำดับ AWS SDK เริ่มต้น
  * การรองรับ reasoning ขึ้นอยู่กับโมเดล; ตรวจสอบการ์ดโมเดล Bedrock สำหรับ ความสามารถปัจจุบัน
  * หากคุณต้องการโฟลว์คีย์ที่มีการจัดการ คุณยังสามารถวางพร็อกซีที่เข้ากันได้กับ OpenAI ไว้หน้า Bedrock แล้วกำหนดค่าเป็นผู้ให้บริการ OpenAI แทนได้


## ที่เกี่ยวข้อง

[**Model selection** การเลือกผู้ให้บริการ, model refs และพฤติกรรม failover ](</th/concepts/model-providers>) [**Memory search** Embedding ของ Bedrock สำหรับการกำหนดค่าการค้นหาหน่วยความจำ ](</th/concepts/memory-search>) [**Memory config reference** รายการโมเดล embedding ของ Bedrock ทั้งหมดและตัวเลือกมิติ ](</th/reference/memory-config#bedrock-embedding-config>) [**Troubleshooting** การแก้ไขปัญหาทั่วไปและคำถามที่พบบ่อย ](</th/help/troubleshooting>)

Was this useful?YesNo