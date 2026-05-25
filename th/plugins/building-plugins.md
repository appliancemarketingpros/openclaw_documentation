---
title: การสร้าง Plugin
source_url: https://docs.openclaw.ai/th/plugins/building-plugins
scraped_at: 2026-05-25
---

Plugin ต่าง ๆ ขยาย OpenClaw ด้วยความสามารถใหม่ ๆ ได้แก่ ช่องทาง, ผู้ให้บริการโมเดล, คำพูด, การถอดเสียงแบบเรียลไทม์, เสียงแบบเรียลไทม์, การทำความเข้าใจสื่อ, การสร้างภาพ, การสร้างวิดีโอ, การดึงข้อมูลเว็บ, การค้นหาเว็บ, เครื่องมือเอเจนต์ หรือการผสมผสานใด ๆ ของความสามารถเหล่านี้

คุณไม่จำเป็นต้องเพิ่ม Plugin ของคุณลงในรีโพซิทอรี OpenClaw เผยแพร่ไปยัง [ClawHub](</th/clawhub>) แล้วผู้ใช้จะติดตั้งด้วย `openclaw plugins install clawhub:<package-name>` สเป็กแพ็กเกจแบบเปล่ายังคง ติดตั้งจาก npm ระหว่างช่วงเปลี่ยนผ่านการเปิดตัว

## ข้อกำหนดเบื้องต้น

  * Node >= 22 และตัวจัดการแพ็กเกจ (npm หรือ pnpm)
  * คุ้นเคยกับ TypeScript (ESM)
  * สำหรับ Plugin ในรีโพ: โคลนรีโพซิทอรีและรัน `pnpm install` เรียบร้อยแล้ว การพัฒนา Plugin จากซอร์สเช็กเอาต์รองรับเฉพาะ pnpm เพราะ OpenClaw โหลด Plugin ที่บันเดิล จากแพ็กเกจเวิร์กสเปซ `extensions/*`


## Plugin แบบไหน?

[**Plugin ช่องทาง** เชื่อมต่อ OpenClaw กับแพลตฟอร์มรับส่งข้อความ (Discord, IRC และอื่น ๆ) ](</th/plugins/sdk-channel-plugins>) [**Plugin ผู้ให้บริการ** เพิ่มผู้ให้บริการโมเดล (LLM, พร็อกซี หรือเอนด์พอยต์แบบกำหนดเอง) ](</th/plugins/sdk-provider-plugins>) [**Plugin แบ็กเอนด์ CLI** แมป AI CLI ภายในเครื่องเข้ากับรันเนอร์สำรองแบบข้อความของ OpenClaw ](</th/plugins/cli-backend-plugins>) [**Plugin เครื่องมือ / hook** ลงทะเบียนเครื่องมือเอเจนต์, event hooks หรือบริการ - อ่านต่อด้านล่าง ](</th/plugins/hooks>)

สำหรับ Plugin ช่องทางที่ไม่รับประกันว่าจะติดตั้งอยู่เมื่อ onboarding/setup ทำงาน ให้ใช้ `createOptionalChannelSetupSurface(...)` จาก `openclaw/plugin-sdk/channel-setup` ซึ่งจะสร้างคู่ setup adapter + wizard ที่ประกาศข้อกำหนดการติดตั้งและปิดกั้นอย่างปลอดภัยเมื่อเขียน config จริง จนกว่า Plugin จะถูกติดตั้ง

## เริ่มต้นอย่างรวดเร็ว: Plugin เครื่องมือ

คู่มือนี้สร้าง Plugin ขั้นต่ำที่ลงทะเบียนเครื่องมือเอเจนต์ Plugin ช่องทาง และ Plugin ผู้ให้บริการมีคู่มือเฉพาะที่ลิงก์ไว้ด้านบน

* ### สร้างแพ็กเกจและ manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

ทุก Plugin ต้องมี manifest แม้ไม่มี config ก็ตาม เครื่องมือที่ลงทะเบียนในรันไทม์ ต้องระบุไว้ใน `contracts.tools` เพื่อให้ OpenClaw ค้นพบ Plugin เจ้าของ ได้โดยไม่ต้องโหลดรันไทม์ของทุก Plugin นอกจากนี้ Plugin ควรประกาศ `activation.onStartup` อย่างตั้งใจ ตัวอย่างนี้ตั้งค่าเป็น `true` ดู [Manifest](</th/plugins/manifest>) สำหรับสคีมาเต็ม สนิปเป็ตการเผยแพร่ ClawHub แบบมาตรฐานอยู่ใน `docs/snippets/plugin-publish/`

* ### เขียน entry point

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` ใช้สำหรับ Plugin ที่ไม่ใช่ช่องทาง สำหรับช่องทาง ให้ใช้ `defineChannelPluginEntry` \- ดู [Plugin ช่องทาง](</th/plugins/sdk-channel-plugins>) สำหรับตัวเลือก entry point ทั้งหมด ดู [Entry Points](</th/plugins/sdk-entrypoints>)

* ### ทดสอบและเผยแพร่

**Plugin ภายนอก:** ตรวจสอบความถูกต้องและเผยแพร่ด้วย ClawHub จากนั้นติดตั้ง:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

สเป็กแพ็กเกจแบบเปล่า เช่น `@myorg/openclaw-my-plugin` จะติดตั้งจาก npm ระหว่าง ช่วงเปลี่ยนผ่านการเปิดตัว ใช้ `clawhub:` เมื่อคุณต้องการให้ resolve ผ่าน ClawHub

**Plugin ในรีโพ:** วางไว้ใต้ทรีเวิร์กสเปซ Plugin ที่บันเดิล - ระบบจะค้นพบโดยอัตโนมัติ

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## ความสามารถของ Plugin

Plugin เดียวสามารถลงทะเบียนความสามารถจำนวนเท่าใดก็ได้ผ่านออบเจ็กต์ `api`:

ความสามารถ | เมธอดการลงทะเบียน | คู่มือโดยละเอียด  
---|---|---  
การอนุมานข้อความ (LLM) | `api.registerProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins>)  
แบ็กเอนด์การอนุมาน CLI | `api.registerCliBackend(...)` | [Plugin แบ็กเอนด์ CLI](</th/plugins/cli-backend-plugins>)  
ช่องทาง / การรับส่งข้อความ | `api.registerChannel(...)` | [Plugin ช่องทาง](</th/plugins/sdk-channel-plugins>)  
คำพูด (TTS/STT) | `api.registerSpeechProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
การถอดเสียงแบบเรียลไทม์ | `api.registerRealtimeTranscriptionProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
เสียงแบบเรียลไทม์ | `api.registerRealtimeVoiceProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
การทำความเข้าใจสื่อ | `api.registerMediaUnderstandingProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
การสร้างภาพ | `api.registerImageGenerationProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
การสร้างเพลง | `api.registerMusicGenerationProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
การสร้างวิดีโอ | `api.registerVideoGenerationProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
การดึงข้อมูลเว็บ | `api.registerWebFetchProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
การค้นหาเว็บ | `api.registerWebSearchProvider(...)` | [Plugin ผู้ให้บริการ](</th/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
มิดเดิลแวร์ผลลัพธ์เครื่องมือ | `api.registerAgentToolResultMiddleware(...)` | [ภาพรวม SDK](</th/plugins/sdk-overview#registration-api>)  
เครื่องมือเอเจนต์ | `api.registerTool(...)` | ด้านล่าง  
คำสั่งแบบกำหนดเอง | `api.registerCommand(...)` | [Entry Points](</th/plugins/sdk-entrypoints>)  
Plugin hooks | `api.on(...)` | [Plugin hooks](</th/plugins/hooks>)  
Internal event hooks | `api.registerHook(...)` | [Entry Points](</th/plugins/sdk-entrypoints>)  
เส้นทาง HTTP | `api.registerHttpRoute(...)` | [Internals](</th/plugins/architecture-internals#gateway-http-routes>)  
คำสั่งย่อย CLI | `api.registerCli(...)` | [Entry Points](</th/plugins/sdk-entrypoints>)  
  
สำหรับ API การลงทะเบียนทั้งหมด ดู [ภาพรวม SDK](</th/plugins/sdk-overview#registration-api>)

Plugin ที่บันเดิลสามารถใช้ `api.registerAgentToolResultMiddleware(...)` เมื่อ ต้องการเขียนผลลัพธ์เครื่องมือใหม่แบบ async ก่อนที่โมเดลจะเห็นเอาต์พุต ประกาศ รันไทม์เป้าหมายใน `contracts.agentToolResultMiddleware` เช่น `["pi", "codex"]` นี่เป็น seam สำหรับ Plugin ที่บันเดิลและเชื่อถือได้; Plugin ภายนอกควรเลือกใช้ OpenClaw plugin hooks ตามปกติ เว้นแต่ OpenClaw จะเพิ่ม นโยบายความเชื่อถือที่ชัดเจนสำหรับความสามารถนี้

หาก Plugin ของคุณลงทะเบียนเมธอด gateway RPC แบบกำหนดเอง ให้เก็บไว้บน คำนำหน้าที่เฉพาะกับ Plugin เนมสเปซผู้ดูแลหลัก (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) จะยังคงถูกสงวนไว้และ resolve ไปที่ `operator.admin` เสมอ แม้ว่า Plugin จะขอขอบเขตที่แคบกว่าก็ตาม

ความหมายของ hook guard ที่ควรทราบ:

  * `before_tool_call`: `{ block: true }` เป็นขั้นสุดท้ายและหยุดตัวจัดการที่มีลำดับความสำคัญต่ำกว่า
  * `before_tool_call`: `{ block: false }` ถือว่าไม่มีการตัดสินใจ
  * `before_tool_call`: `{ requireApproval: true }` จะหยุดการทำงานของเอเจนต์ชั่วคราวและขออนุมัติจากผู้ใช้ผ่าน exec approval overlay, ปุ่ม Telegram, การโต้ตอบ Discord หรือคำสั่ง `/approve` บนช่องทางใดก็ได้
  * `before_install`: `{ block: true }` เป็นขั้นสุดท้ายและหยุดตัวจัดการที่มีลำดับความสำคัญต่ำกว่า
  * `before_install`: `{ block: false }` ถือว่าไม่มีการตัดสินใจ
  * `message_sending`: `{ cancel: true }` เป็นขั้นสุดท้ายและหยุดตัวจัดการที่มีลำดับความสำคัญต่ำกว่า
  * `message_sending`: `{ cancel: false }` ถือว่าไม่มีการตัดสินใจ
  * `message_received`: ควรใช้ฟิลด์ typed `threadId` เมื่อคุณต้องกำหนดเส้นทาง thread/topic ขาเข้า เก็บ `metadata` ไว้สำหรับข้อมูลเพิ่มเติมเฉพาะช่องทาง
  * `message_sending`: ควรใช้ฟิลด์กำหนดเส้นทาง typed `replyToId` / `threadId` แทนคีย์ metadata เฉพาะช่องทาง


คำสั่ง `/approve` จัดการทั้ง exec และการอนุมัติของ Plugin พร้อม fallback แบบมีขอบเขต: เมื่อไม่พบ exec approval id, OpenClaw จะลอง id เดียวกันอีกครั้งผ่านการอนุมัติของ Plugin การส่งต่อการอนุมัติของ Plugin สามารถกำหนดค่าแยกต่างหากผ่าน `approvals.plugin` ใน config

หากระบบอนุมัติแบบกำหนดเองจำเป็นต้องตรวจจับกรณี fallback แบบมีขอบเขตเดียวกันนี้ ควรใช้ `isApprovalNotFoundError` จาก `openclaw/plugin-sdk/error-runtime` แทนการจับคู่สตริง approval-expiry ด้วยตนเอง

ดู [Plugin hooks](</th/plugins/hooks>) สำหรับตัวอย่างและข้อมูลอ้างอิง hook

## การลงทะเบียนเครื่องมือเอเจนต์

เครื่องมือคือฟังก์ชันที่มี type ซึ่ง LLM สามารถเรียกใช้ได้ เครื่องมืออาจเป็นแบบบังคับ (พร้อมใช้งานเสมอ) หรือแบบเลือกได้ (ผู้ใช้ opt-in):

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

แฟกทอรีเครื่องมือจะได้รับออบเจ็กต์บริบทที่รันไทม์จัดให้ ใช้ `ctx.activeModel` เมื่อเครื่องมือต้องบันทึก แสดงผล หรือปรับให้เข้ากับโมเดลที่ใช้งานอยู่ สำหรับรอบปัจจุบัน ออบเจ็กต์นี้อาจมี `provider`, `modelId` และ `modelRef` ให้มองว่าเป็นเมตาดาต้ารันไทม์เชิงข้อมูล ไม่ใช่ขอบเขตความปลอดภัย สำหรับป้องกันผู้ปฏิบัติการในเครื่อง โค้ด Plugin ที่ติดตั้งไว้ หรือรันไทม์ OpenClaw ที่ถูกแก้ไข สำหรับเครื่องมือภายในเครื่องที่อ่อนไหว ให้คงการยินยอมใช้งานอย่างชัดเจนจาก Plugin หรือผู้ปฏิบัติการ และปฏิเสธโดยปริยายเมื่อเมตาดาต้าโมเดลที่ใช้งานอยู่ขาดหายหรือไม่เหมาะสม

ทุกเครื่องมือที่ลงทะเบียนด้วย `api.registerTool(...)` ต้องประกาศไว้ใน manifest ของ Plugin ด้วย:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw จะจับและแคชตัวบรรยายที่ผ่านการตรวจสอบจากเครื่องมือที่ลงทะเบียนไว้ ดังนั้น Plugin จึงไม่ต้องทำซ้ำข้อมูล `description` หรือ schema ใน manifest สัญญาใน manifest เพียงประกาศความเป็นเจ้าของและการค้นพบเท่านั้น ส่วนการเรียกใช้ยังคงเรียก อิมพลีเมนเทชันเครื่องมือที่ลงทะเบียนสดอยู่ ตั้งค่า `toolMetadata.<tool>.optional: true` สำหรับเครื่องมือที่ลงทะเบียนด้วย `api.registerTool(..., { optional: true })` เพื่อให้ OpenClaw หลีกเลี่ยงการโหลด รันไทม์ของ Plugin นั้นจนกว่าเครื่องมือจะถูกเพิ่มใน allowlist อย่างชัดเจน

ผู้ใช้เปิดใช้เครื่องมือแบบไม่บังคับใน config:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * ชื่อเครื่องมือต้องไม่ชนกับเครื่องมือหลัก (ความขัดแย้งจะถูกข้าม)
  * เครื่องมือที่มีออบเจ็กต์การลงทะเบียนผิดรูป รวมถึงไม่มี `parameters` จะถูกข้ามและรายงานใน diagnostics ของ Plugin แทนที่จะทำให้การรัน agent ล้มเหลว
  * ใช้ `optional: true` สำหรับเครื่องมือที่มีผลข้างเคียงหรือต้องใช้ไบนารีเพิ่มเติม
  * ผู้ใช้สามารถเปิดใช้เครื่องมือทั้งหมดจาก Plugin ได้โดยเพิ่ม id ของ Plugin ลงใน `tools.allow`


## การลงทะเบียนคำสั่ง CLI

Plugin สามารถเพิ่มกลุ่มคำสั่งราก `openclaw` ด้วย `api.registerCli` ได้ ระบุ `descriptors` สำหรับรากคำสั่งระดับบนสุดทุกคำสั่ง เพื่อให้ OpenClaw แสดงและกำหนดเส้นทาง คำสั่งได้โดยไม่ต้องโหลดรันไทม์ของ Plugin ทุกตัวตั้งแต่ต้น

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

หลังติดตั้ง ให้ตรวจสอบการลงทะเบียนรันไทม์และเรียกใช้คำสั่ง:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## แบบแผนการนำเข้า

นำเข้าจากพาธ `openclaw/plugin-sdk/<subpath>` ที่เจาะจงเสมอ:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

สำหรับข้อมูลอ้างอิง subpath ทั้งหมด ดู [ภาพรวม SDK](</th/plugins/sdk-overview>)

ภายใน Plugin ของคุณ ให้ใช้ไฟล์ barrel ภายในเครื่อง (`api.ts`, `runtime-api.ts`) สำหรับ การนำเข้าภายใน - อย่านำเข้า Plugin ของคุณเองผ่านพาธ SDK ของมัน

สำหรับ provider Plugin ให้เก็บ helper เฉพาะ provider ไว้ใน barrel รากของแพ็กเกจเหล่านั้น เว้นแต่ว่า seam นั้นเป็นแบบทั่วไปอย่างแท้จริง ตัวอย่างที่รวมมาในปัจจุบัน:

  * Anthropic: wrapper สตรีม Claude และ helper `service_tier` / beta
  * OpenAI: builder ของ provider, helper โมเดลเริ่มต้น, provider แบบ realtime
  * OpenRouter: builder ของ provider พร้อม helper onboarding/config


หาก helper มีประโยชน์เฉพาะภายในแพ็กเกจ provider ที่รวมมาเพียงแพ็กเกจเดียว ให้เก็บไว้บน seam รากแพ็กเกจนั้นแทนการโปรโมตเข้าไปใน `openclaw/plugin-sdk/*`

seam helper `openclaw/plugin-sdk/<bundled-id>` บางส่วนที่สร้างขึ้นยังคงมีอยู่สำหรับ การบำรุงรักษา bundled Plugin เมื่อมีการใช้งานจากเจ้าของที่ติดตามไว้ ให้ถือว่าสิ่งเหล่านี้เป็น พื้นผิวที่สงวนไว้ ไม่ใช่รูปแบบเริ่มต้นสำหรับ Plugin ภายนอกรายใหม่

## เช็กลิสต์ก่อนส่ง

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** มีเมตาดาต้า `openclaw` ที่ถูกต้อง OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s มี manifest **openclaw.plugin.json** และถูกต้อง OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s entry point ใช้ `defineChannelPluginEntry` หรือ `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s การนำเข้าทั้งหมดใช้พาธ `plugin-sdk/<subpath>` ที่เจาะจง OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo