---
title: Azure Speech
source_url: https://docs.openclaw.ai/th/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech เป็นผู้ให้บริการแปลงข้อความเป็นเสียงของ Azure AI Speech ใน OpenClaw ระบบจะใช้สังเคราะห์เสียงคำตอบขาออกเป็น MP3 โดยค่าเริ่มต้น, เป็น Ogg/Opus แบบดั้งเดิมสำหรับ voice notes และเป็นเสียง mulaw 8 kHz สำหรับช่องทางโทรศัพท์ เช่น Voice Call

OpenClaw ใช้ Azure Speech REST API โดยตรงร่วมกับ SSML และส่ง รูปแบบเอาต์พุตที่ผู้ให้บริการกำหนดผ่าน `X-Microsoft-OutputFormat`

Detail | Value  
---|---  
เว็บไซต์ | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
เอกสาร | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
การยืนยันตัวตน | `AZURE_SPEECH_KEY` plus `AZURE_SPEECH_REGION`  
เสียงเริ่มต้น | `en-US-JennyNeural`  
เอาต์พุตไฟล์เริ่มต้น | `audio-24khz-48kbitrate-mono-mp3`  
ไฟล์ voice note เริ่มต้น | `ogg-24khz-16bit-mono-opus`  
  
## เริ่มต้นใช้งาน

* ### สร้างทรัพยากร Azure Speech

ใน Azure portal ให้สร้างทรัพยากร Speech คัดลอก **KEY 1** จาก Resource Management > Keys and Endpoint และคัดลอกตำแหน่งของทรัพยากร เช่น `eastus`

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### เลือก Azure Speech ใน messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### ส่งข้อความ

ส่งคำตอบผ่านช่องทางที่เชื่อมต่อไว้ช่องทางใดก็ได้ OpenClaw จะสังเคราะห์เสียง ด้วย Azure Speech และส่งเป็น MP3 สำหรับเสียงมาตรฐาน หรือเป็น Ogg/Opus เมื่อ ช่องทางนั้นคาดหวัง voice note

## ตัวเลือกการกำหนดค่า

Option | Path | Description  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | คีย์ทรัพยากร Azure Speech หากไม่มีจะ fallback ไปใช้ `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` หรือ `SPEECH_KEY`  
`region` | `messages.tts.providers.azure-speech.region` | region ของทรัพยากร Azure Speech หากไม่มีจะ fallback ไปใช้ `AZURE_SPEECH_REGION` หรือ `SPEECH_REGION`  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | ตัวเลือก override สำหรับ endpoint/base URL ของ Azure Speech  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | ตัวเลือก override สำหรับ base URL ของ Azure Speech  
`voice` | `messages.tts.providers.azure-speech.voice` | Azure voice ShortName (ค่าเริ่มต้น `en-US-JennyNeural`)  
`lang` | `messages.tts.providers.azure-speech.lang` | รหัสภาษา SSML (ค่าเริ่มต้น `en-US`)  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | รูปแบบเอาต์พุตไฟล์เสียง (ค่าเริ่มต้น `audio-24khz-48kbitrate-mono-mp3`)  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | รูปแบบเอาต์พุต voice note (ค่าเริ่มต้น `ogg-24khz-16bit-mono-opus`)  
  
## หมายเหตุ

การยืนยันตัวตน

Azure Speech ใช้คีย์ทรัพยากร Speech ไม่ใช่คีย์ Azure OpenAI โดยคีย์ จะถูกส่งเป็น `Ocp-Apim-Subscription-Key`; OpenClaw จะสร้าง `https://<region>.tts.speech.microsoft.com` จาก `region` เว้นแต่คุณ จะระบุ `endpoint` หรือ `baseUrl`

ชื่อเสียง

ใช้ค่า `ShortName` ของเสียง Azure Speech เช่น `en-US-JennyNeural` ผู้ให้บริการที่มาพร้อมกันสามารถแสดงรายการเสียงผ่าน ทรัพยากร Speech เดียวกัน และจะกรองเสียงที่ถูกทำเครื่องหมายว่า deprecated หรือ retired ออก

เอาต์พุตเสียง

Azure รองรับรูปแบบเอาต์พุต เช่น `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus` และ `riff-24khz-16bit-mono-pcm` OpenClaw จะขอ Ogg/Opus สำหรับเป้าหมาย `voice-note` เพื่อให้ช่องทางต่าง ๆ สามารถส่ง voice bubble แบบดั้งเดิมได้โดยไม่ต้องแปลงจาก MP3 เพิ่มเติม

Alias

`azure` ยอมรับเป็น alias ของผู้ให้บริการได้สำหรับ PR ที่มีอยู่และ config ของผู้ใช้ แต่ config ใหม่ควรใช้ `azure-speech` เพื่อหลีกเลี่ยงความสับสนกับ ผู้ให้บริการโมเดล Azure OpenAI

## ที่เกี่ยวข้อง

[**การแปลงข้อความเป็นเสียง** ภาพรวม TTS, ผู้ให้บริการ และ config `messages.tts` ](</th/tools/tts>) [**การกำหนดค่า** เอกสารอ้างอิงการกำหนดค่าแบบเต็ม รวมถึงการตั้งค่า `messages.tts` ](</th/gateway/configuration>) [**Providers** Providers ทั้งหมดของ OpenClaw ที่มาพร้อมกัน ](</th/providers>) [**การแก้ปัญหา** ปัญหาที่พบบ่อยและขั้นตอนการดีบัก ](</th/help/troubleshooting>)

Was this useful?YesNo