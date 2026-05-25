---
title: Pluginleri yönet
source_url: https://docs.openclaw.ai/tr/plugins/manage-plugins
scraped_at: 2026-05-25
---

Çoğu Plugin iş akışı birkaç komuttan oluşur: ara, yükle, Gateway'i yeniden başlat, doğrula ve Plugin'e artık ihtiyacın kalmadığında kaldır.

## Plugin'leri listeleme

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Betikler için `--json` kullanın. Plugin paketi `dependencies` veya `optionalDependencies` bildirdiğinde kayıt defteri tanılamalarını ve her Plugin'in statik `dependencyStatus` değerini içerir.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` soğuk bir envanter kontrolüdür. OpenClaw'ın config, manifestler ve Plugin kayıt defterinden neleri keşfedebildiğini gösterir; halihazırda çalışan bir Gateway sürecinin Plugin runtime'ını içe aktardığını kanıtlamaz.

## Plugin'leri yükleme

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Plugin kodunu yükledikten sonra kanallarınıza hizmet veren Gateway'i yeniden başlatın:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Plugin'in araçlar, hook'lar, servisler, Gateway yöntemleri veya Plugin'e ait CLI komutları gibi runtime yüzeylerini kaydettiğine dair kanıt gerektiğinde `inspect --runtime` kullanın.

## Plugin'leri güncelleme

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Bir Plugin `@beta` gibi bir npm dist-tag'den yüklendiyse sonraki `update <plugin-id>` çağrıları kaydedilmiş bu etiketi yeniden kullanır. Açık bir npm spec geçmek, izlenen yüklemeyi gelecekteki güncellemeler için bu spec'e geçirir.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

İkinci komut, daha önce kesin bir sürüme veya etikete sabitlenmiş bir Plugin'i kayıt defterinin varsayılan sürüm hattına geri taşır.

`openclaw update` beta kanalında çalıştığında, varsayılan hat npm ve ClawHub Plugin kayıtları önce eşleşen Plugin `@beta` sürümünü dener. Bu beta sürümü yoksa OpenClaw kaydedilmiş varsayılan/latest spec'e geri döner. npm Plugin'leri için, beta paketi mevcut olsa ancak yükleme doğrulaması başarısız olsa da OpenClaw geri döner. Kesin sürümler ve `@rc` veya `@beta` gibi açık etiketler korunur.

## Plugin'leri kaldırma

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

Kaldırma işlemi, Plugin'in config girişini, Plugin dizin kaydını, izin/ret listesi girişlerini ve geçerliyse bağlı yükleme yollarını kaldırır. Yönetilen yükleme dizinleri, `--keep-files` geçmediğiniz sürece kaldırılır.

Nix modunda (`OPENCLAW_NIX_MODE=1`), Plugin yükleme, güncelleme, kaldırma, etkinleştirme ve devre dışı bırakma komutları devre dışıdır. Bunun yerine bu seçimleri yükleme için Nix kaynağında yönetin; nix-openclaw için ajan öncelikli [Hızlı Başlangıç](<https://github.com/openclaw/nix-openclaw#quick-start>) bölümünü kullanın.

## Plugin'leri yayımlama

Harici Plugin'leri [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) veya her ikisine yayımlayabilirsiniz.

### ClawHub'a yayımlama

ClawHub, OpenClaw Plugin'leri için birincil herkese açık keşif yüzeyidir. Kullanıcılara yüklemeden önce aranabilir meta veriler, sürüm geçmişi ve kayıt defteri tarama sonuçları sağlar.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Kullanıcılar ClawHub'dan şu komutla yükler:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

Yalın biçim hâlâ önce ClawHub'ı kontrol eder.

### [npmjs.com](<http://npmjs.com>)'a yayımlama

Yerel npm Plugin'leri bir Plugin manifesti ve `package.json` OpenClaw giriş noktası meta verilerini içermelidir.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Kullanıcılar yalnızca npm'den şu komutlarla yükler:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Aynı paket ClawHub'da da mevcutsa `npm:` ClawHub aramasını atlar ve npm çözümlemesini zorlar.

## Kaynak seçimi

  * **ClawHub** : OpenClaw'a özgü keşif, tarama özetleri, sürümler ve yükleme ipuçları istediğinizde kullanın.
  * **[npmjs.com](<http://npmjs.com>)** : Zaten JavaScript paketleri yayımlıyorsanız veya npm dist-tag/private kayıt defteri iş akışlarına ihtiyacınız varsa kullanın.
  * **Git** : Doğrudan bir branch, tag veya commit'ten yüklemek istediğinizde kullanın.
  * **Yerel yol** : Aynı makinede bir Plugin geliştirirken veya test ederken kullanın.


## İlgili

  * [Plugin'ler](</tr/tools/plugin>) \- genel bakış ve sorun giderme
  * [`openclaw plugins`](</tr/cli/plugins>) \- tam CLI referansı
  * [ClawHub](</tr/clawhub/cli>) \- yayımlama ve kayıt defteri işlemleri
  * [Plugin oluşturma](</tr/plugins/building-plugins>) \- Plugin paketi oluşturma
  * [Plugin manifesti](</tr/plugins/manifest>) \- manifest ve paket meta verileri


Was this useful?YesNo