---
title: openclaw status
source_url: https://docs.openclaw.ai/tr/cli/status
scraped_at: 2026-05-25
---

Kanallar + oturumlar için tanılamalar.

bashCopy code
[code]
    openclaw statusopenclaw status --allopenclaw status --deepopenclaw status --usage
[/code]

Notlar:

  * `--deep` canlı sondalar çalıştırır (WhatsApp Web + Telegram + Discord + Slack + Signal).
  * Düz `openclaw status`, hızlı salt okunur yolda kalır ve bellek incelemesini atladığında belleği kullanılamaz yerine `not checked` olarak işaretler. Ağır güvenlik denetimi, Plugin uyumluluğu ve bellek vektörü sondaları `openclaw status --all`, `openclaw status --deep`, `openclaw security audit` ve `openclaw memory status --deep` komutlarına bırakılır.
  * `status --json --all`, `plugins.slots.memory` tarafından seçilen etkin bellek Plugin runtime'ından bellek ayrıntılarını bildirir. Özel bellek Pluginleri, yerleşik `agents.defaults.memorySearch.enabled` ayarını devre dışı bırakıp yine de kendi dosya, parça, vektör ve FTS durumlarını bildirebilir.
  * `--usage`, normalleştirilmiş sağlayıcı kullanım pencerelerini `X% left` olarak yazdırır.
  * Oturum durumu çıktısı `Execution:` ile `Runtime:` değerlerini ayırır. `Execution` sandbox yoludur (`direct`, `docker/*`), `Runtime` ise oturumun `OpenClaw Pi Default`, `OpenAI Codex`, bir CLI arka ucu veya `codex (acp/acpx)` gibi bir ACP arka ucu kullanıp kullanmadığını söyler. Sağlayıcı/model/runtime ayrımı için bkz. [Aracı runtime'ları](</tr/concepts/agent-runtimes>).
  * MiniMax'in ham `usage_percent` / `usagePercent` alanları kalan kotadır; bu nedenle OpenClaw bunları görüntülemeden önce tersine çevirir; mevcut olduğunda sayım tabanlı alanlar önceliklidir. `model_remains` yanıtları sohbet modeli girdisini tercih eder, gerektiğinde pencere etiketini zaman damgalarından türetir ve plan etiketine model adını dahil eder.
  * Geçerli oturum anlık görüntüsü seyrek olduğunda, `/status` belirteç ve önbellek sayaçlarını en son transkript kullanım günlüğünden tamamlayabilir. Mevcut sıfır olmayan canlı değerler, transkript yedek değerlerine göre yine önceliklidir.
  * `/status`, kompakt Gateway süreç çalışma süresini ve ana makine sistem çalışma süresini içerir.
  * Transkript yedeği, canlı oturum girdisinde eksik olduğunda etkin runtime model etiketini de kurtarabilir. Bu transkript modeli seçilen modelden farklıysa, durum bağlam penceresini seçilen model yerine kurtarılan runtime modeline göre çözer.
  * İstem boyutu muhasebesi için, oturum meta verileri eksik veya daha küçük olduğunda transkript yedeği daha büyük istem odaklı toplamı tercih eder; böylece özel sağlayıcı oturumları `0` belirteç gösterimlerine düşmez.
  * Birden fazla aracı yapılandırıldığında çıktı aracı başına oturum depolarını içerir.
  * Genel bakış, mevcut olduğunda Gateway + düğüm ana makine hizmeti kurulum/runtime durumunu içerir.
  * Genel bakış, güncelleme kanalını + git SHA'sını (kaynak checkout'ları için) içerir.
  * Güncelleme bilgisi Genel Bakış'ta gösterilir; bir güncelleme varsa, durum `openclaw update` çalıştırmaya yönelik bir ipucu yazdırır (bkz. [Güncelleme](</tr/install/updating>)).
  * Model fiyatlandırması yenileme hataları isteğe bağlı fiyatlandırma uyarıları olarak gösterilir. Bunlar Gateway'in veya kanalların sağlıksız olduğu anlamına gelmez.
  * Salt okunur durum yüzeyleri (`status`, `status --json`, `status --all`) mümkün olduğunda hedeflenen yapılandırma yolları için desteklenen SecretRefs değerlerini çözer.
  * Desteklenen bir kanal SecretRef yapılandırılmış ancak geçerli komut yolunda kullanılamıyorsa, durum salt okunur kalır ve çökmek yerine bozulmuş çıktı bildirir. İnsan çıktısı "configured token unavailable in this command path" gibi uyarılar gösterir ve JSON çıktısı `secretDiagnostics` içerir.
  * Komuta yerel SecretRef çözümlemesi başarılı olduğunda, durum çözümlenmiş anlık görüntüyü tercih eder ve nihai çıktıdan geçici "secret unavailable" kanal işaretleyicilerini temizler.
  * `status --all`, rapor oluşturmayı durdurmadan gizli anahtar tanılamalarını özetleyen (okunabilirlik için kısaltılmış) bir Gizli Anahtarlar genel bakış satırı ve tanılama bölümü içerir.


## İlgili

  * [CLI referansı](</tr/cli>)
  * [Doctor](</tr/gateway/doctor>)


Was this useful?YesNo