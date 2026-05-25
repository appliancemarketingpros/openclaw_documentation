---
title: Gizli bilgiler
source_url: https://docs.openclaw.ai/tr/cli/secrets
scraped_at: 2026-05-25
---

# `openclaw secrets`

SecretRef'leri yönetmek ve etkin çalışma zamanı anlık görüntüsünü sağlıklı tutmak için `openclaw secrets` kullanın.

Komut rolleri:

  * `reload`: ref'leri yeniden çözen ve çalışma zamanı anlık görüntüsünü yalnızca tam başarı durumunda değiştiren Gateway RPC'si (`secrets.reload`) (yapılandırma yazımı yok).
  * `audit`: düz metin, çözümlenmemiş ref'ler ve öncelik sapması için yapılandırma/kimlik doğrulama/oluşturulmuş model depolarını ve eski kalıntıları salt okunur tarar (`--allow-exec` ayarlanmadıkça exec ref'leri atlanır).
  * `configure`: sağlayıcı kurulumu, hedef eşleme ve ön kontrol için etkileşimli planlayıcı (TTY gerekir).
  * `apply`: kaydedilmiş bir planı yürütür (`--dry-run` yalnızca doğrulama içindir; dry-run varsayılan olarak exec denetimlerini atlar ve yazma modu `--allow-exec` ayarlanmadıkça exec içeren planları reddeder), ardından hedeflenen düz metin kalıntılarını temizler.


Önerilen operatör döngüsü:

bashCopy code
[code]
    openclaw secrets audit --checkopenclaw secrets configureopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-runopenclaw secrets apply --from /tmp/openclaw-secrets-plan.jsonopenclaw secrets audit --checkopenclaw secrets reload
[/code]

Planınız `exec` SecretRef'ler/sağlayıcılar içeriyorsa, hem dry-run hem de yazma apply komutlarında `--allow-exec` geçin.

CI/geçitler için çıkış kodu notu:

  * `audit --check`, bulgu varsa `1` döndürür.
  * çözümlenmemiş ref'ler `2` döndürür.


İlgili:

  * Gizli bilgiler kılavuzu: [Gizli Bilgi Yönetimi](</tr/gateway/secrets>)
  * Kimlik bilgisi yüzeyi: [SecretRef Credential Surface](</tr/reference/secretref-credential-surface>)
  * Güvenlik kılavuzu: [Güvenlik](</tr/gateway/security>)


## Çalışma zamanı anlık görüntüsünü yeniden yükleme

Gizli bilgi ref'lerini yeniden çözün ve çalışma zamanı anlık görüntüsünü atomik olarak değiştirin.

bashCopy code
[code]
    openclaw secrets reloadopenclaw secrets reload --jsonopenclaw secrets reload --url ws://127.0.0.1:18789 --token <token>
[/code]

Notlar:

  * Gateway RPC yöntemi `secrets.reload` kullanır.
  * Çözümleme başarısız olursa Gateway son bilinen iyi anlık görüntüyü korur ve hata döndürür (kısmi etkinleştirme yok).
  * JSON yanıtı `warningCount` içerir.


Seçenekler:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--json`


## Denetim

OpenClaw durumunu şunlar için tarar:

  * düz metin gizli bilgi depolama
  * çözümlenmemiş ref'ler
  * öncelik sapması (`auth-profiles.json` kimlik bilgilerinin `openclaw.json` ref'lerini gölgelemesi)
  * oluşturulmuş `agents/*/agent/models.json` kalıntıları (sağlayıcı `apiKey` değerleri ve hassas sağlayıcı üst bilgileri)
  * eski kalıntılar (eski kimlik doğrulama deposu girdileri, OAuth hatırlatmaları)


Üst bilgi kalıntısı notu:

  * Hassas sağlayıcı üst bilgi algılama ad-sezgisel temellidir (yaygın kimlik doğrulama/kimlik bilgisi üst bilgi adları ve `authorization`, `x-api-key`, `token`, `secret`, `password` ve `credential` gibi parçalar).

bashCopy code
[code]
    openclaw secrets auditopenclaw secrets audit --checkopenclaw secrets audit --jsonopenclaw secrets audit --allow-exec
[/code]

Çıkış davranışı:

  * `--check`, bulgu varsa sıfır olmayan kodla çıkar.
  * çözümlenmemiş ref'ler daha yüksek öncelikli sıfır olmayan çıkış koduyla çıkar.


Rapor biçimi öne çıkanlar:

  * `status`: `clean | findings | unresolved`
  * `resolution`: `refsChecked`, `skippedExecRefs`, `resolvabilityComplete`
  * `summary`: `plaintextCount`, `unresolvedRefCount`, `shadowedRefCount`, `legacyResidueCount`
  * bulgu kodları: 
    * `PLAINTEXT_FOUND`
    * `REF_UNRESOLVED`
    * `REF_SHADOWED`
    * `LEGACY_RESIDUE`


## Configure (etkileşimli yardımcı)

Sağlayıcı ve SecretRef değişikliklerini etkileşimli olarak oluşturun, ön kontrol çalıştırın ve isteğe bağlı olarak uygulayın:

bashCopy code
[code]
    openclaw secrets configureopenclaw secrets configure --plan-out /tmp/openclaw-secrets-plan.jsonopenclaw secrets configure --apply --yesopenclaw secrets configure --providers-onlyopenclaw secrets configure --skip-provider-setupopenclaw secrets configure --agent opsopenclaw secrets configure --json
[/code]

Akış:

  * Önce sağlayıcı kurulumu (`secrets.providers` takma adları için `add/edit/remove`).
  * Sonra kimlik bilgisi eşleme (alanları seçin ve `{source, provider, id}` ref'leri atayın).
  * En son ön kontrol ve isteğe bağlı uygulama.


Bayraklar:

  * `--providers-only`: yalnızca `secrets.providers` yapılandırın, kimlik bilgisi eşlemeyi atlayın.
  * `--skip-provider-setup`: sağlayıcı kurulumunu atlayın ve kimlik bilgilerini mevcut sağlayıcılara eşleyin.
  * `--agent <id>`: `auth-profiles.json` hedef bulma ve yazmaları tek bir aracı deposuyla sınırlar.
  * `--allow-exec`: ön kontrol/uygulama sırasında exec SecretRef denetimlerine izin verir (sağlayıcı komutlarını çalıştırabilir).


Notlar:

  * Etkileşimli bir TTY gerektirir.
  * `--providers-only` ile `--skip-provider-setup` birlikte kullanılamaz.
  * `configure`, seçilen aracı kapsamı için `openclaw.json` içindeki gizli bilgi taşıyan alanları ve `auth-profiles.json` dosyasını hedefler.
  * `configure`, seçici akışı içinde doğrudan yeni `auth-profiles.json` eşlemeleri oluşturmayı destekler.
  * Kanonik desteklenen yüzey: [SecretRef Credential Surface](</tr/reference/secretref-credential-surface>).
  * Uygulamadan önce ön kontrol çözümlemesi yapar.
  * Ön kontrol/uygulama exec ref'ler içeriyorsa, her iki adım için de `--allow-exec` ayarlı tutun.
  * Oluşturulan planlar varsayılan olarak temizleme seçeneklerini kullanır (`scrubEnv`, `scrubAuthProfilesForProviderTargets`, `scrubLegacyAuthJson` hepsi etkin).
  * Uygulama yolu, temizlenen düz metin değerler için tek yönlüdür.
  * `--apply` olmadan bile CLI ön kontrolden sonra `Apply this plan now?` sorusunu sorar.
  * `--apply` ile (`--yes` olmadan), CLI ek bir geri alınamaz onay ister.
  * `--json`, planı + ön kontrol raporunu yazdırır, ancak komut yine de etkileşimli bir TTY gerektirir.


Exec sağlayıcı güvenlik notu:

  * Homebrew kurulumları genellikle `/opt/homebrew/bin/*` altında sembolik bağlantılı ikili dosyalar sunar.
  * `allowSymlinkCommand: true` ayarını yalnızca güvenilen paket yöneticisi yolları için gerektiğinde yapın ve bunu `trustedDirs` ile eşleyin (örneğin `["/opt/homebrew"]`).
  * Windows'ta, bir sağlayıcı yolu için ACL doğrulaması kullanılamıyorsa OpenClaw kapalı güvenli olarak başarısız olur. Yalnızca güvenilen yollar için, yol güvenlik denetimlerini atlamak üzere o sağlayıcıda `allowInsecurePath: true` ayarlayın.


## Kaydedilmiş planı uygulama

Önceden oluşturulmuş bir planı uygulayın veya ön kontrolünü yapın:

bashCopy code
[code]
    openclaw secrets apply --from /tmp/openclaw-secrets-plan.jsonopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-runopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --json
[/code]

Exec davranışı:

  * `--dry-run`, dosya yazmadan ön kontrolü doğrular.
  * exec SecretRef denetimleri dry-run içinde varsayılan olarak atlanır.
  * yazma modu, `--allow-exec` ayarlanmadıkça exec SecretRef'ler/sağlayıcılar içeren planları reddeder.
  * Her iki modda da exec sağlayıcı denetimlerine/yürütümüne katılmak için `--allow-exec` kullanın.


Plan sözleşmesi ayrıntıları (izin verilen hedef yollar, doğrulama kuralları ve başarısızlık anlamları):

  * [Secrets Apply Plan Contract](</tr/gateway/secrets-plan-contract>)


`apply`'ın güncelleyebilecekleri:

  * `openclaw.json` (SecretRef hedefleri + sağlayıcı ekleme/güncelleme/silmeleri)
  * `auth-profiles.json` (sağlayıcı hedef temizleme)
  * eski `auth.json` kalıntıları
  * değeri taşınmış olan `~/.openclaw/.env` içindeki bilinen gizli bilgi anahtarları


## Neden geri alma yedekleri yok

`secrets apply`, eski düz metin değerleri içeren geri alma yedeklerini bilerek yazmaz.

Güvenlik, sıkı ön kontrol + başarısızlık durumunda en iyi çabayla bellek içi geri yükleme ile neredeyse atomik uygulamadan gelir.

## Örnek

bashCopy code
[code]
    openclaw secrets audit --checkopenclaw secrets configureopenclaw secrets audit --check
[/code]

`audit --check` hâlâ düz metin bulguları bildiriyorsa, bildirilen kalan hedef yolları güncelleyin ve denetimi yeniden çalıştırın.

## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Gizli bilgi yönetimi](</tr/gateway/secrets>)


Was this useful?YesNo