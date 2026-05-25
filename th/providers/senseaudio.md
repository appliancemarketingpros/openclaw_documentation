---
title: SenseAudio
source_url: https://docs.openclaw.ai/th/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio สามารถถอดเสียงจากเสียงขาเข้าและไฟล์แนบโน้ตเสียงผ่านไปป์ไลน์ `tools.media.audio` ที่ใช้ร่วมกันของ OpenClaw ได้ OpenClaw จะโพสต์เสียงแบบ multipart ไปยัง endpoint การถอดเสียงที่เข้ากันได้กับ OpenAI และฉีดข้อความที่ส่งกลับมาเป็น `{{Transcript}}` พร้อมบล็อก `[Audio]`

คุณสมบัติ | ค่า  
---|---  
รหัสผู้ให้บริการ | `senseaudio`  
Plugin | รวมมาให้, `enabledByDefault: true`  
Contract | `mediaUnderstandingProviders` (เสียง)  
ตัวแปร env สำหรับการยืนยันตัวตน | `SENSEAUDIO_API_KEY`  
โมเดลเริ่มต้น | `senseaudio-asr-pro-1.5-260319`  
URL เริ่มต้น | `https://api.senseaudio.cn/v1`  
เว็บไซต์ | [senseaudio.cn](<https://senseaudio.cn>)  
เอกสาร | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## เริ่มต้นใช้งาน

* ### ตั้งค่า API key ของคุณ

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### เปิดใช้ผู้ให้บริการเสียง

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### ส่งโน้ตเสียง

ส่งข้อความเสียงผ่านช่องทางที่เชื่อมต่ออยู่ใดก็ได้ OpenClaw จะอัปโหลด เสียงไปยัง SenseAudio และใช้ถอดเสียงในไปป์ไลน์การตอบกลับ

## ตัวเลือก

ตัวเลือก | พาธ | คำอธิบาย  
---|---|---  
`model` | `tools.media.audio.models[].model` | รหัสโมเดล ASR ของ SenseAudio  
`language` | `tools.media.audio.models[].language` | คำใบ้ภาษาแบบไม่บังคับ  
`prompt` | `tools.media.audio.prompt` | prompt การถอดเสียงแบบไม่บังคับ  
`baseUrl` | `tools.media.audio.baseUrl` หรือโมเดล | แทนที่ base ที่เข้ากันได้กับ OpenAI  
`headers` | `tools.media.audio.request.headers` | ส่วนหัวคำขอเพิ่มเติม  
  
## ที่เกี่ยวข้อง

  * [การทำความเข้าใจสื่อ (เสียง)](</th/nodes/audio>)
  * [ผู้ให้บริการโมเดล](</th/concepts/model-providers>)


Was this useful?YesNo