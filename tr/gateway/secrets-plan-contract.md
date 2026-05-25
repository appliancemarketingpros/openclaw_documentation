---
title: Secrets apply plan sözleşmesi
source_url: https://docs.openclaw.ai/tr/gateway/secrets-plan-contract
scraped_at: 2026-05-25
---

Bu sayfa, `openclaw secrets apply` tarafından zorunlu tutulan katı sözleşmeyi tanımlar.

Bir hedef bu kurallarla eşleşmezse, apply yapılandırmayı değiştirmeden önce başarısız olur.

## Plan dosyası şekli

`openclaw secrets apply --from <plan.json>`, plan hedeflerinden oluşan bir `targets` dizisi bekler:

json5Copy code
[code]
    {  version: 1,  protocolVersion: 1,  targets: [    {      type: "models.providers.apiKey",      path: "models.providers.openai.apiKey",      pathSegments: ["models", "providers", "openai", "apiKey"],      providerId: "openai",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },    {      type: "auth-profiles.api_key.key",      path: "profiles.openai:default.key",      pathSegments: ["profiles", "openai:default", "key"],      agentId: "main",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },  ],}
[/code]

## Desteklenen hedef kapsamı

Plan hedefleri, şu konumlardaki desteklenen kimlik bilgisi yolları için kabul edilir:

  * [SecretRef Credential Surface](</tr/reference/secretref-credential-surface>)


## Hedef türü davranışı

Genel kural:

  * `target.type` tanınmalıdır ve normalize edilmiş `target.path` şekliyle eşleşmelidir.


Uyumluluk takma adları mevcut planlar için kabul edilmeye devam eder:

  * `models.providers.apiKey`
  * `skills.entries.apiKey`
  * `channels.googlechat.serviceAccount`


## Yol doğrulama kuralları

Her hedef aşağıdakilerin tümüyle doğrulanır:

  * `type` tanınan bir hedef türü olmalıdır.
  * `path` boş olmayan bir noktalı yol olmalıdır.
  * `pathSegments` atlanabilir. Verilirse, `path` ile tam olarak aynı yola normalize edilmelidir.
  * Yasaklı segmentler reddedilir: `__proto__`, `prototype`, `constructor`.
  * Normalize edilmiş yol, hedef türü için kaydedilmiş yol şekliyle eşleşmelidir.
  * `providerId` veya `accountId` ayarlıysa, yolda kodlanmış kimlikle eşleşmelidir.
  * `auth-profiles.json` hedefleri `agentId` gerektirir.
  * Yeni bir `auth-profiles.json` eşlemesi oluştururken `authProfileProvider` ekleyin.


## Başarısızlık davranışı

Bir hedef doğrulamayı geçemezse, apply şu şekilde bir hatayla çıkar:

textCopy code
[code]
    Invalid plan target path for models.providers.apiKey: models.providers.openai.baseUrl
[/code]

Geçersiz bir plan için hiçbir yazma işlemi işlenmez.

## Exec sağlayıcı onay davranışı

  * `--dry-run`, varsayılan olarak exec SecretRef denetimlerini atlar.
  * Exec SecretRef/sağlayıcı içeren planlar, `--allow-exec` ayarlanmadıkça yazma modunda reddedilir.
  * Exec içeren planları doğrularken/uygularken hem dry-run hem de yazma komutlarında `--allow-exec` geçin.


## Çalışma zamanı ve denetim kapsamı notları

  * Yalnızca ref içeren `auth-profiles.json` girdileri (`keyRef`/`tokenRef`), çalışma zamanı çözümlemesine ve denetim kapsamına dahildir.
  * `secrets apply`, desteklenen `openclaw.json` hedeflerini, desteklenen `auth-profiles.json` hedeflerini ve isteğe bağlı scrub hedeflerini yazar.


## Operatör denetimleri

bashCopy code
[code]
    # Yazma işlemi olmadan planı doğrulaopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run # Sonra gerçekten uygulaopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json # Exec içeren planlar için, her iki modda da açıkça dahil olunopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
[/code]

Apply geçersiz hedef yolu iletisiyle başarısız olursa, planı `openclaw secrets configure` ile yeniden oluşturun veya hedef yolunu yukarıdaki desteklenen bir şekle düzeltin.

## İlgili belgeler

  * [Secrets Management](</tr/gateway/secrets>)
  * [CLI `secrets`](</tr/cli/secrets>)
  * [SecretRef Credential Surface](</tr/reference/secretref-credential-surface>)
  * [Yapılandırma Başvurusu](</tr/gateway/configuration-reference>)


Was this useful?YesNo