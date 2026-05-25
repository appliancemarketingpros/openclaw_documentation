---
title: Webhook Plugin
source_url: https://docs.openclaw.ai/tr/plugins/webhooks
scraped_at: 2026-05-25
---

Webhooks Plugin'i, dış otomasyonu OpenClaw TaskFlow'larına bağlayan kimliği doğrulanmış HTTP rotaları ekler.

Önce özel bir Plugin yazmadan Zapier, n8n, bir CI işi veya dahili bir servis gibi güvenilir bir sistemin yönetilen TaskFlow'lar oluşturmasını ve yürütmesini istediğinizde kullanın.

## Nerede çalışır

Webhooks Plugin'i Gateway işleminin içinde çalışır.

Gateway'iniz başka bir makinede çalışıyorsa Plugin'i o Gateway ana makinesine kurup yapılandırın, ardından Gateway'i yeniden başlatın.

## Rotaları yapılandırma

Yapılandırmayı `plugins.entries.webhooks.config` altında ayarlayın:

json5Copy code
[code]
    {  plugins: {    entries: {      webhooks: {        enabled: true,        config: {          routes: {            zapier: {              path: "/plugins/webhooks/zapier",              sessionKey: "agent:main:main",              secret: {                source: "env",                provider: "default",                id: "OPENCLAW_WEBHOOK_SECRET",              },              controllerId: "webhooks/zapier",              description: "Zapier TaskFlow köprüsü",            },          },        },      },    },  },}
[/code]

Rota alanları:

  * `enabled`: isteğe bağlıdır, varsayılanı `true`
  * `path`: isteğe bağlıdır, varsayılanı `/plugins/webhooks/<routeId>`
  * `sessionKey`: bağlı TaskFlow'ların sahibi olan gerekli oturum
  * `secret`: gerekli paylaşılan gizli anahtar veya SecretRef
  * `controllerId`: oluşturulan yönetilen akışlar için isteğe bağlı denetleyici kimliği
  * `description`: isteğe bağlı operatör notu


Desteklenen `secret` girdileri:

  * Düz metin dizesi
  * `source: "env" | "file" | "exec"` ile SecretRef


Gizli anahtar destekli bir rota başlangıçta gizli anahtarını çözemezse Plugin, bozuk bir uç noktayı açığa çıkarmak yerine o rotayı atlar ve bir uyarı günlüğe kaydeder.

## Güvenlik modeli

Her rotaya, yapılandırılmış `sessionKey` değerinin TaskFlow yetkisiyle hareket etmesi için güvenilir.

Bu, rotanın söz konusu oturumun sahibi olduğu TaskFlow'ları inceleyip değiştirebileceği anlamına gelir; bu nedenle şunları yapmalısınız:

  * Her rota için güçlü ve benzersiz bir gizli anahtar kullanın
  * Satır içi düz metin gizli anahtarlar yerine gizli anahtar başvurularını tercih edin
  * Rotaları iş akışına uyan en dar oturuma bağlayın
  * Yalnızca ihtiyacınız olan belirli Webhook yolunu açığa çıkarın


Plugin şunları uygular:

  * Paylaşılan gizli anahtar kimlik doğrulaması
  * İstek gövdesi boyutu ve zaman aşımı korumaları
  * Sabit pencereli hız sınırlama
  * Devam eden istek sınırlama
  * `api.runtime.tasks.managedFlows.bindSession(...)` üzerinden sahip bağlı TaskFlow erişimi


## İstek biçimi

`POST` isteklerini şunlarla gönderin:

  * `Content-Type: application/json`
  * `Authorization: Bearer <secret>` veya `x-openclaw-webhook-secret: <secret>`


Örnek:

bashCopy code
[code]
    curl -X POST https://gateway.example.com/plugins/webhooks/zapier \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_SHARED_SECRET' \  -d '{"action":"create_flow","goal":"Review inbound queue"}'
[/code]

## Desteklenen eylemler

Plugin şu anda bu JSON `action` değerlerini kabul eder:

  * `create_flow`
  * `get_flow`
  * `list_flows`
  * `find_latest_flow`
  * `resolve_flow`
  * `get_task_summary`
  * `set_waiting`
  * `resume_flow`
  * `finish_flow`
  * `fail_flow`
  * `request_cancel`
  * `cancel_flow`
  * `run_task`


### `create_flow`

Rotanın bağlı oturumu için yönetilen bir TaskFlow oluşturur.

Örnek:

jsonCopy code
[code]
    {  "action": "create_flow",  "goal": "Review inbound queue",  "status": "queued",  "notifyPolicy": "done_only"}
[/code]

### `run_task`

Mevcut bir yönetilen TaskFlow içinde yönetilen bir alt görev oluşturur.

İzin verilen çalışma zamanları şunlardır:

  * `subagent`
  * `acp`


Örnek:

jsonCopy code
[code]
    {  "action": "run_task",  "flowId": "flow_123",  "runtime": "acp",  "childSessionKey": "agent:main:acp:worker",  "task": "Inspect the next message batch"}
[/code]

## Yanıt biçimi

Başarılı yanıtlar şunu döndürür:

jsonCopy code
[code]
    {  "ok": true,  "routeId": "zapier",  "result": {}}
[/code]

Reddedilen istekler şunu döndürür:

jsonCopy code
[code]
    {  "ok": false,  "routeId": "zapier",  "code": "not_found",  "error": "TaskFlow not found.",  "result": {}}
[/code]

Plugin, Webhook yanıtlarından sahip/oturum meta verilerini bilinçli olarak temizler.

## İlgili belgeler

  * [Plugin çalışma zamanı SDK'sı](</tr/plugins/sdk-runtime>)
  * [Hook'lar ve Webhook'lara genel bakış](</tr/automation/hooks>)
  * [CLI Webhook'ları](</tr/cli/webhooks>)


Was this useful?YesNo