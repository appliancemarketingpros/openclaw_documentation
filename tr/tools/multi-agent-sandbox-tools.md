---
title: Çok ajanlı korumalı alan ve araçlar
source_url: https://docs.openclaw.ai/tr/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Çok ajanlı bir kurulumda her ajan, genel korumalı alan ve araç ilkesini geçersiz kılabilir. Bu sayfa ajan başına yapılandırmayı, öncelik kurallarını ve örnekleri kapsar.

[**Korumalı alan kullanımı** Arka uçlar ve modlar — tam korumalı alan başvurusu. ](</tr/gateway/sandboxing>) [**Korumalı alan ile araç ilkesi ile yükseltilmiş** "Bu neden engellendi?" hata ayıklaması ](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Yükseltilmiş mod** Güvenilen göndericiler için yükseltilmiş exec. ](</tr/tools/elevated>)

* * *

## Yapılandırma örnekleri

Örnek 1: Kişisel + kısıtlı aile ajanı jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Sonuç:**

  * `main` ajanı: ana makinede çalışır, tam araç erişimine sahiptir.
  * `family` ajanı: Docker içinde çalışır (ajan başına bir kapsayıcı), yalnızca `read` ve geçerli konuşmaya ileti gönderimleri.

Örnek 2: Paylaşılan korumalı alana sahip iş ajanı jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Örnek 2b: Genel kodlama profili + yalnızca mesajlaşma ajanı jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Sonuç:**

  * varsayılan ajanlar kodlama araçlarını alır.
  * `support` ajanı yalnızca mesajlaşma içindir (+ Slack aracı).

Örnek 3: Ajan başına farklı korumalı alan modları jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Yapılandırma önceliği

Hem genel (`agents.defaults.*`) hem de ajana özgü (`agents.list[].*`) yapılandırmalar mevcut olduğunda:

### Korumalı alan yapılandırması

Ajana özgü ayarlar geneli geçersiz kılar:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Araç kısıtlamaları

Filtreleme sırası şudur:

* ### Araç profili

`tools.profile` veya `agents.list[].tools.profile`.

* ### Sağlayıcı araç profili

`tools.byProvider[provider].profile` veya `agents.list[].tools.byProvider[provider].profile`.

* ### Genel araç ilkesi

`tools.allow` / `tools.deny`.

* ### Sağlayıcı araç ilkesi

`tools.byProvider[provider].allow/deny`.

* ### Ajana özgü araç ilkesi

`agents.list[].tools.allow/deny`.

* ### Ajan sağlayıcı ilkesi

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Korumalı alan araç ilkesi

`tools.sandbox.tools` veya `agents.list[].tools.sandbox.tools`.

* ### Alt ajan araç ilkesi

Geçerliyse `tools.subagents.tools`.

Öncelik kuralları

  * Her seviye araçları daha da kısıtlayabilir, ancak önceki seviyelerde reddedilen araçları geri veremez.
  * `agents.list[].tools.sandbox.tools` ayarlanmışsa, o ajan için `tools.sandbox.tools` değerinin yerini alır.
  * `agents.list[].tools.profile` ayarlanmışsa, o ajan için `tools.profile` değerini geçersiz kılar.
  * Sağlayıcı araç anahtarları `provider` (ör. `google-antigravity`) veya `provider/model` (ör. `openai/gpt-5.4`) kabul eder.

Boş izin listesi davranışı

Bu zincirdeki açık izin listelerinden herhangi biri çalıştırmada çağrılabilir araç bırakmazsa, OpenClaw istemi modele göndermeden önce durur. Bu kasıtlıdır: `agents.list[].tools.allow: ["query_db"]` gibi eksik bir araçla yapılandırılmış bir ajan, `query_db` kaydını yapan Plugin etkinleştirilene kadar açık şekilde başarısız olmalıdır; yalnızca metin ajanı olarak devam etmemelidir.

Araç ilkeleri, birden çok araca genişleyen `group:*` kısaltmalarını destekler. Tam liste için [Araç grupları](</tr/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) bölümüne bakın.

Ajan başına yükseltilmiş geçersiz kılmalar (`agents.list[].tools.elevated`), belirli ajanlar için yükseltilmiş exec'i daha da kısıtlayabilir. Ayrıntılar için [Yükseltilmiş mod](</tr/tools/elevated>) bölümüne bakın.

* * *

## Tek ajandan geçiş

### Önce (tek ajan)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Sonra (çok ajanlı)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Araç kısıtlama örnekleri

### Salt okunur ajan

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Dosya sistemi araçları devre dışıyken kabuk yürütme

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Yalnızca iletişim

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

Bu profildeki `sessions_history`, ham bir transkript dökümü yerine hâlâ sınırlı ve temizlenmiş bir hatırlama görünümü döndürür. Asistan hatırlaması; düşünme etiketlerini, `<relevant-memories>` iskeletini, düz metin araç çağrısı XML yüklerini (`<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` ve kısaltılmış araç çağrısı blokları dahil), derecesi düşürülmüş araç çağrısı iskeletini, sızmış ASCII/tam genişlikli model denetim belirteçlerini ve hatalı biçimlendirilmiş MiniMax araç çağrısı XML'ini redaksiyon/kısaltma öncesinde ayıklar.

* * *

## Yaygın tuzak: "non-main"

* * *

## Test

Çok ajanlı sandbox ve araçları yapılandırdıktan sonra:

* ### Ajan çözümlemesini denetleyin

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Sandbox kapsayıcılarını doğrulayın

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Araç kısıtlamalarını test edin

  * Kısıtlı araçlar gerektiren bir ileti gönderin.
  * Ajanın reddedilen araçları kullanamadığını doğrulayın.


* ### Günlükleri izleyin

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Sorun giderme

`mode: 'all'` olmasına rağmen ajan sandbox içinde değil

  * Bunu geçersiz kılan genel bir `agents.defaults.sandbox.mode` olup olmadığını denetleyin.
  * Ajana özel yapılandırma önceliklidir; bu nedenle `agents.list[].sandbox.mode: "all"` ayarını yapın.

Reddetme listesine rağmen araçlar hâlâ kullanılabilir

  * Araç filtreleme sırasını denetleyin: genel → ajan → sandbox → alt ajan.
  * Her düzey yalnızca daha fazla kısıtlayabilir, tekrar izin veremez.
  * Günlüklerle doğrulayın: `[tools] filtering tools for agent:${agentId}`.

Kapsayıcı ajan başına yalıtılmamış

  * Ajana özel sandbox yapılandırmasında `scope: "agent"` ayarını yapın.
  * Varsayılan değer, oturum başına bir kapsayıcı oluşturan `"session"` değeridir.


* * *

## İlgili

  * [Yükseltilmiş mod](</tr/tools/elevated>)
  * [Çoklu ajan yönlendirme](</tr/concepts/multi-agent>)
  * [Sandbox yapılandırması](</tr/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox, araç ilkesi ve yükseltilmiş mod karşılaştırması](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>) — "bu neden engelleniyor?" hatalarını ayıklama
  * [Sandboxing](</tr/gateway/sandboxing>) — tam sandbox başvurusu (modlar, kapsamlar, arka uçlar, imajlar)
  * [Oturum yönetimi](</tr/concepts/session>)


Was this useful?YesNo