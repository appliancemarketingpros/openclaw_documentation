---
title: Ajanlar
source_url: https://docs.openclaw.ai/tr/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

Yalıtılmış ajanları yönetin (çalışma alanları + kimlik doğrulama + yönlendirme).

İlgili:

  * [Çok ajanlı yönlendirme](</tr/concepts/multi-agent>)
  * [Ajan çalışma alanı](</tr/concepts/agent-workspace>)
  * [Skills yapılandırması](</tr/tools/skills-config>): skill görünürlüğü yapılandırması.


## Örnekler

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## Yönlendirme bağlamaları

Gelen kanal trafiğini belirli bir ajana sabitlemek için yönlendirme bağlamalarını kullanın.

Ayrıca ajan başına farklı görünür skills istiyorsanız, `openclaw.json` içinde `agents.defaults.skills` ve `agents.list[].skills` yapılandırın. [Skills yapılandırması](</tr/tools/skills-config>) ve [Yapılandırma başvurusu](</tr/gateway/config-agents#agents-defaults-skills>) bölümlerine bakın.

Bağlamaları listeleyin:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

Bağlamalar ekleyin:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

`accountId` öğesini atlarsanız (`--bind <channel>`), OpenClaw mümkün olduğunda bunu kanal varsayılanlarından ve plugin kurulum kancalarından çözer.

`bind` veya `unbind` için `--agent` öğesini atlarsanız, OpenClaw geçerli varsayılan ajanı hedefler.

### Bağlama kapsamı davranışı

  * `accountId` içermeyen bir bağlama yalnızca kanalın varsayılan hesabıyla eşleşir.
  * `accountId: "*"` kanal genelinde yedektir (tüm hesaplar) ve açık bir hesap bağlamasından daha az özeldir.
  * Aynı ajanın zaten `accountId` olmadan eşleşen bir kanal bağlaması varsa ve daha sonra açık veya çözümlenmiş bir `accountId` ile bağlama yaparsanız, OpenClaw yinelenen eklemek yerine mevcut bağlamayı yerinde yükseltir.


Örnek:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

Yükseltmeden sonra, bu bağlama için yönlendirme `telegram:ops` kapsamına alınır. Varsayılan hesap yönlendirmesini de istiyorsanız, bunu açıkça ekleyin (örneğin `--bind telegram:default`).

Bağlamaları kaldırın:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind`, `--all` ya da bir veya daha fazla `--bind` değeri kabul eder; ikisini birlikte kabul etmez.

## Komut yüzeyi

### `agents`

Alt komut olmadan `openclaw agents` çalıştırmak, `openclaw agents list` ile eşdeğerdir.

### `agents list`

Seçenekler:

  * `--json`
  * `--bindings`: yalnızca ajan başına sayıları/özetleri değil, tam yönlendirme kurallarını dahil et


### `agents add [name]`

Seçenekler:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (tekrarlanabilir)
  * `--non-interactive`
  * `--json`


Notlar:

  * Herhangi bir açık ekleme bayrağı geçirmek, komutu etkileşimsiz yola geçirir.
  * Etkileşimsiz mod hem ajan adı hem de `--workspace` gerektirir.
  * `main` ayrılmıştır ve yeni ajan kimliği olarak kullanılamaz.
  * Etkileşimli modda kimlik doğrulama tohumlama yalnızca taşınabilir statik profilleri kopyalar (varsayılan olarak `api_key` ve statik `token`). OAuth yenileme belirteci profilleri yalnızca gerçek `main` ajan deposundan okuma yoluyla kalıtım üzerinden kullanılabilir kalır. Yapılandırılmış varsayılan ajan `main` değilse, yeni ajandaki OAuth profilleri için ayrı oturum açın.


### `agents bindings`

Seçenekler:

  * `--agent <id>`
  * `--json`


### `agents bind`

Seçenekler:

  * `--agent <id>` (varsayılan olarak geçerli varsayılan ajan)
  * `--bind <channel[:accountId]>` (tekrarlanabilir)
  * `--json`


### `agents unbind`

Seçenekler:

  * `--agent <id>` (varsayılan olarak geçerli varsayılan ajan)
  * `--bind <channel[:accountId]>` (tekrarlanabilir)
  * `--all`
  * `--json`


### `agents delete <id>`

Seçenekler:

  * `--force`
  * `--json`


Notlar:

  * `main` silinemez.
  * `--force` olmadan etkileşimli onay gerekir.
  * Çalışma alanı, ajan durumu ve oturum dökümü dizinleri kalıcı olarak silinmez; Çöp Kutusu'na taşınır.
  * Gateway erişilebilir olduğunda silme işlemi Gateway üzerinden gönderilir; böylece yapılandırma ve oturum deposu temizliği, çalışma zamanı trafiğiyle aynı yazıcıyı paylaşır. Gateway'e ulaşılamazsa CLI çevrimdışı yerel yola geri döner.
  * Başka bir ajanın çalışma alanı aynı yolsa, bu çalışma alanının içindeyse veya bu çalışma alanını içeriyorsa, çalışma alanı korunur ve `--json` `workspaceRetained`, `workspaceRetainedReason` ve `workspaceSharedWith` bildirir.


## Kimlik dosyaları

Her ajan çalışma alanı, çalışma alanı kökünde bir `IDENTITY.md` içerebilir:

  * Örnek yol: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity`, çalışma alanı kökünden (veya açık bir `--identity-file` değerinden) okur


Avatar yolları çalışma alanı köküne göre çözümlenir.

## Kimlik ayarla

`set-identity`, alanları `agents.list[].identity` içine yazar:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (çalışma alanına göreli yol, http(s) URL'si veya veri URI'si)


Seçenekler:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


Notlar:

  * Hedef ajanı seçmek için `--agent` veya `--workspace` kullanılabilir.
  * `--workspace` kullanıyorsanız ve birden fazla ajan bu çalışma alanını paylaşıyorsa, komut başarısız olur ve `--agent` geçirmenizi ister.
  * Açık kimlik alanları sağlanmadığında komut kimlik verilerini `IDENTITY.md` dosyasından okur.


`IDENTITY.md` dosyasından yükleyin:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

Alanları açıkça geçersiz kılın:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

Yapılandırma örneği:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Çok ajanlı yönlendirme](</tr/concepts/multi-agent>)
  * [Ajan çalışma alanı](</tr/concepts/agent-workspace>)


Was this useful?YesNo