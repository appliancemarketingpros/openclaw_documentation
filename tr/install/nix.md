---
title: Nix
source_url: https://docs.openclaw.ai/tr/install/nix
scraped_at: 2026-05-25
---

OpenClaw'u **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** ile bildirimsel olarak kurun - birinci taraf, kapsamlı Home Manager modülü.

## Ne elde edersiniz

  * Gateway + macOS uygulaması + araçlar (whisper, spotify, kameralar) -- hepsi sabitlenmiş
  * Yeniden başlatmalardan sonra çalışmaya devam eden launchd servisi
  * Bildirimsel yapılandırmaya sahip Plugin sistemi
  * Anında geri alma: `home-manager switch --rollback`


## Hızlı başlangıç

* ### Determinate Nix'i kurun

Nix zaten kurulu değilse [Determinate Nix installer](<https://github.com/DeterminateSystems/nix-installer>) talimatlarını izleyin.

* ### Yerel bir flake oluşturun

nix-openclaw reposundaki agent-first şablonunu kullanın:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### Gizli bilgileri yapılandırın

Mesajlaşma botu token'ınızı ve model sağlayıcısı API anahtarınızı ayarlayın. `~/.secrets/` altındaki düz dosyalar yeterlidir.

* ### Şablon yer tutucularını doldurun ve geçiş yapın

bashCopy code
[code]
    home-manager switch
[/code]

* ### Doğrulayın

launchd servisinin çalıştığını ve botunuzun mesajlara yanıt verdiğini doğrulayın.

Tam modül seçenekleri ve örnekler için [nix-openclaw README](<https://github.com/openclaw/nix-openclaw>) dosyasına bakın.

## Nix modu çalışma zamanı davranışı

`OPENCLAW_NIX_MODE=1` ayarlandığında (nix-openclaw ile otomatik), OpenClaw Nix tarafından yönetilen kurulumlar için deterministik bir moda girer. Diğer Nix paketleri de aynı modu ayarlayabilir; nix-openclaw birinci taraf referanstır.

Bunu manuel olarak da ayarlayabilirsiniz:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

macOS'te GUI uygulaması kabuk ortam değişkenlerini otomatik olarak devralmaz. Bunun yerine Nix modunu defaults üzerinden etkinleştirin:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Nix modunda neler değişir

  * Otomatik kurulum ve kendi kendini değiştirme akışları devre dışı bırakılır
  * `openclaw.json` değişmez kabul edilir. Başlangıçtan türetilen varsayılanlar yalnızca çalışma zamanında kalır; setup, onboarding, değişiklik yapan `openclaw update`, Plugin install/update/uninstall/enable, `doctor --fix`, `doctor --generate-gateway-token` ve `openclaw config set` gibi yapılandırma yazıcıları dosyayı düzenlemeyi reddeder.
  * Aracılar bunun yerine Nix kaynağını düzenlemelidir. nix-openclaw için agent-first [Hızlı Başlangıç](<https://github.com/openclaw/nix-openclaw#quick-start>) bölümünü kullanın ve yapılandırmayı `programs.openclaw.config` veya `instances.<name>.config` altında ayarlayın.
  * Eksik bağımlılıklar Nix'e özgü düzeltme mesajları gösterir
  * UI, salt okunur Nix modu banner'ı gösterir


### Yapılandırma ve durum yolları

OpenClaw JSON5 yapılandırmasını `OPENCLAW_CONFIG_PATH` üzerinden okur ve değiştirilebilir verileri `OPENCLAW_STATE_DIR` içinde saklar. Nix altında çalışırken, çalışma zamanı durumu ve yapılandırmanın değişmez store dışında kalması için bunları açıkça Nix tarafından yönetilen konumlara ayarlayın.

Değişken | Varsayılan  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### Servis PATH keşfi

launchd/systemd gateway servisi, `nix` ile kurulan çalıştırılabilirleri kabuk üzerinden çağıran Plugin'lerin ve araçların manuel PATH kurulumu olmadan çalışması için Nix-profile ikili dosyalarını otomatik keşfeder:

  * `NIX_PROFILES` ayarlandığında, her giriş sağdan sola öncelikle servis PATH'ine eklenir (Nix kabuk önceliğiyle eşleşir - en sağdaki kazanır).
  * `NIX_PROFILES` ayarlı olmadığında, `~/.nix-profile/bin` yedek olarak eklenir.


Bu, hem macOS launchd hem de Linux systemd servis ortamları için geçerlidir.

## İlgili

[**nix-openclaw** Doğruluk kaynağı Home Manager modülü ve tam kurulum kılavuzu. ](<https://github.com/openclaw/nix-openclaw>) [**Kurulum sihirbazı** Nix dışı CLI kurulum adımları. ](</tr/start/wizard>) [**Docker** Nix dışı alternatif olarak konteynerleştirilmiş kurulum. ](</tr/install/docker>) [**Güncelleme** Home Manager tarafından yönetilen kurulumları paketle birlikte güncelleme. ](</tr/install/updating>)

Was this useful?YesNo