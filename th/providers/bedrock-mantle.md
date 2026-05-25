---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/th/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw มีผู้ให้บริการ **Amazon Bedrock Mantle** ที่บันเดิลมาให้ ซึ่งเชื่อมต่อกับ ปลายทาง Mantle ที่เข้ากันได้กับ OpenAI Mantle โฮสต์โมเดลโอเพนซอร์สและ โมเดลจากบุคคลที่สาม (GPT-OSS, Qwen, Kimi, GLM และโมเดลที่คล้ายกัน) ผ่านพื้นผิวมาตรฐาน `/v1/chat/completions` ที่รองรับด้วยโครงสร้างพื้นฐานของ Bedrock

คุณสมบัติ | ค่า  
---|---  
ID ผู้ให้บริการ | `amazon-bedrock-mantle`  
API | `openai-completions` (เข้ากันได้กับ OpenAI) หรือ `anthropic-messages` (เส้นทาง Anthropic Messages)  
การยืนยันตัวตน | `AWS_BEARER_TOKEN_BEDROCK` แบบชัดเจน หรือการสร้าง bearer-token จากเชนข้อมูลรับรอง IAM  
รีเจียนเริ่มต้น | `us-east-1` (เขียนทับด้วย `AWS_REGION` หรือ `AWS_DEFAULT_REGION`)  
  
## เริ่มต้นใช้งาน

เลือกวิธีการยืนยันตัวตนที่ต้องการและทำตามขั้นตอนการตั้งค่า

### Explicit bearer token

**เหมาะที่สุดสำหรับ:** สภาพแวดล้อมที่คุณมี Mantle bearer token อยู่แล้ว

* ### Set the bearer token on the gateway host

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

ตั้งค่ารีเจียนเพิ่มเติมได้ตามต้องการ (ค่าเริ่มต้นคือ `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

โมเดลที่ค้นพบจะแสดงอยู่ภายใต้ผู้ให้บริการ `amazon-bedrock-mantle` ไม่ต้องมี การกำหนดค่าเพิ่มเติม เว้นแต่ว่าคุณต้องการเขียนทับค่าเริ่มต้น

### IAM credentials

**เหมาะที่สุดสำหรับ:** การใช้ข้อมูลรับรองที่เข้ากันได้กับ AWS SDK (การกำหนดค่าที่แชร์, SSO, web identity, instance role หรือ task role)

* ### Configure AWS credentials on the gateway host

แหล่งการยืนยันตัวตนใด ๆ ที่เข้ากันได้กับ AWS SDK ใช้งานได้:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw สร้าง Mantle bearer token จากเชนข้อมูลรับรองโดยอัตโนมัติ

## การค้นพบโมเดลอัตโนมัติ

เมื่อตั้งค่า `AWS_BEARER_TOKEN_BEDROCK` แล้ว OpenClaw จะใช้ค่านั้นโดยตรง มิฉะนั้น OpenClaw จะพยายามสร้าง Mantle bearer token จากเชนข้อมูลรับรองเริ่มต้นของ AWS จากนั้นจึงค้นพบโมเดล Mantle ที่พร้อมใช้งานโดยค้นหาที่ปลายทาง `/v1/models` ของรีเจียน

พฤติกรรม | รายละเอียด  
---|---  
แคชการค้นพบ | แคชผลลัพธ์ไว้ 1 ชั่วโมง  
การรีเฟรชโทเคน IAM | ทุกชั่วโมง  
  
หากต้องการเปิดใช้งาน Plugin ของ Mantle ไว้ แต่ระงับการค้นพบอัตโนมัติและการสร้าง IAM bearer-token ให้ปิดสวิตช์การค้นพบที่ Plugin เป็นเจ้าของ:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### รีเจียนที่รองรับ

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## การกำหนดค่าด้วยตนเอง

หากคุณต้องการกำหนดค่าอย่างชัดเจนแทนการค้นพบอัตโนมัติ:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## การกำหนดค่าขั้นสูง

Reasoning support

รองรับการใช้เหตุผลโดยอนุมานจาก ID โมเดลที่มีรูปแบบอย่างเช่น `thinking`, `reasoner` หรือ `gpt-oss-120b` OpenClaw จะตั้งค่า `reasoning: true` โดยอัตโนมัติสำหรับโมเดลที่ตรงกันระหว่างการค้นพบ

Endpoint unavailability

หากปลายทาง Mantle ไม่พร้อมใช้งานหรือไม่ส่งคืนโมเดล ผู้ให้บริการจะถูก ข้ามไปอย่างเงียบ ๆ OpenClaw จะไม่แจ้งข้อผิดพลาด ผู้ให้บริการอื่นที่กำหนดค่าไว้ จะยังทำงานได้ตามปกติ

Claude Opus 4.7 via the Anthropic Messages route

Mantle ยังเปิดเผยเส้นทาง Anthropic Messages ที่นำโมเดล Claude ผ่านเส้นทางสตรีมมิงที่ยืนยันตัวตนด้วย bearer เดียวกัน Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) เรียกผ่านเส้นทางนี้ได้ด้วยสตรีมมิงที่ผู้ให้บริการเป็นเจ้าของ ดังนั้น AWS bearer token จึงไม่ถูกปฏิบัติเหมือนคีย์ Anthropic API

เมื่อคุณปักหมุดโมเดล Anthropic Messages บนผู้ให้บริการ Mantle OpenClaw จะใช้พื้นผิว API `anthropic-messages` แทน `openai-completions` สำหรับโมเดลนั้น การยืนยันตัวตนยังคงมาจาก `AWS_BEARER_TOKEN_BEDROCK` (หรือ IAM bearer token ที่ออกให้)

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relationship to Amazon Bedrock provider

Bedrock Mantle เป็นผู้ให้บริการแยกจากผู้ให้บริการ [Amazon Bedrock](</th/providers/bedrock>) มาตรฐาน Mantle ใช้พื้นผิว `/v1` ที่เข้ากันได้กับ OpenAI ในขณะที่ผู้ให้บริการ Bedrock มาตรฐานใช้ Bedrock API แบบเนทีฟ

ผู้ให้บริการทั้งสองแชร์ข้อมูลรับรอง `AWS_BEARER_TOKEN_BEDROCK` เดียวกันเมื่อ มีข้อมูลนี้อยู่

## ที่เกี่ยวข้อง

[**Amazon Bedrock** ผู้ให้บริการ Bedrock แบบเนทีฟสำหรับ Anthropic Claude, Titan และโมเดลอื่น ๆ ](</th/providers/bedrock>) [**Model selection** การเลือกผู้ให้บริการ, model refs และพฤติกรรมการสลับไปใช้ตัวสำรอง ](</th/concepts/model-providers>) [**OAuth and auth** รายละเอียดการยืนยันตัวตนและกฎการใช้ข้อมูลรับรองซ้ำ ](</th/gateway/authentication>) [**Troubleshooting** ปัญหาทั่วไปและวิธีแก้ไข ](</th/help/troubleshooting>)

Was this useful?YesNo