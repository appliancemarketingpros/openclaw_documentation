---
title: LLM görevi
source_url: https://docs.openclaw.ai/tr/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task`, JSON-only bir LLM görevi çalıştıran ve yapılandırılmış çıktı döndüren (isteğe bağlı olarak JSON Schema ile doğrulanan) **isteğe bağlı bir Plugin aracıdır**.

Bu, Lobster gibi iş akışı motorları için idealdir: her iş akışı için özel OpenClaw kodu yazmadan tek bir LLM adımı ekleyebilirsiniz.

## Plugin'i etkinleştirin

  1. Plugin'i etkinleştirin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. İsteğe bağlı araca izin verin:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

`tools.allow` öğesini yalnızca kısıtlayıcı izin listesi modunu istediğinizde kullanın.

## Yapılandırma (isteğe bağlı)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels`, `provider/model` dizelerinden oluşan bir izin listesidir. Ayarlanırsa, listenin dışındaki tüm istekler reddedilir.

## Araç parametreleri

  * `prompt` (dize, zorunlu)
  * `input` (herhangi bir değer, isteğe bağlı)
  * `schema` (nesne, isteğe bağlı JSON Schema)
  * `provider` (dize, isteğe bağlı)
  * `model` (dize, isteğe bağlı)
  * `thinking` (dize, isteğe bağlı)
  * `authProfileId` (dize, isteğe bağlı)
  * `temperature` (sayı, isteğe bağlı)
  * `maxTokens` (sayı, isteğe bağlı)
  * `timeoutMs` (sayı, isteğe bağlı)


`thinking`, `low` veya `medium` gibi standart OpenClaw muhakeme ön ayarlarını kabul eder.

## Çıktı

Ayrıştırılmış JSON'u içeren `details.json` döndürür (ve sağlandığında `schema` ile doğrular).

## Örnek: Lobster iş akışı adımı

### Önemli sınırlama

Aşağıdaki örnek, **bağımsız Lobster CLI** 'nin `openclaw.invoke` için doğru gateway URL'sinin/kimlik doğrulama bağlamının zaten bulunduğu bir ortamda çalıştığını varsayar.

OpenClaw içindeki paketlenmiş **gömülü** Lobster çalıştırıcısı için bu iç içe CLI deseni **şu anda güvenilir değildir** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Gömülü Lobster bu akış için desteklenen bir köprüye sahip olana kadar şunlardan birini tercih edin:

  * Lobster dışında doğrudan `llm-task` araç çağrıları veya
  * iç içe `openclaw.invoke` çağrılarına dayanmayan Lobster adımları.


Bağımsız Lobster CLI örneği:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Güvenlik notları

  * Araç **yalnızca JSON** kullanır ve modele yalnızca JSON çıktısı üretmesini söyler (kod blokları yok, yorum yok).
  * Bu çalıştırma için modele hiçbir araç sunulmaz.
  * `schema` ile doğrulamadığınız sürece çıktıyı güvenilmeyen kabul edin.
  * Yan etkisi olan herhangi bir adımdan (gönder, yayınla, yürüt) önce onayları yerleştirin.


## İlgili

  * [Düşünme düzeyleri](</tr/tools/thinking>)
  * [Alt ajanlar](</tr/tools/subagents>)
  * [Slash komutları](</tr/tools/slash-commands>)


Was this useful?YesNo