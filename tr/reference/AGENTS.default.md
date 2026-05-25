---
title: Varsayılan AGENTS.md
source_url: https://docs.openclaw.ai/tr/reference/AGENTS.default
scraped_at: 2026-05-25
---

## İlk çalıştırma (önerilir)

OpenClaw, aracı için ayrılmış bir çalışma alanı dizini kullanır. Varsayılan: `~/.openclaw/workspace` (`agents.defaults.workspace` üzerinden yapılandırılabilir).

  1. Çalışma alanını oluşturun (zaten yoksa):

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace
[/code]

  2. Varsayılan çalışma alanı şablonlarını çalışma alanına kopyalayın:

bashCopy code
[code]
    cp docs/reference/templates/AGENTS.md ~/.openclaw/workspace/AGENTS.mdcp docs/reference/templates/SOUL.md ~/.openclaw/workspace/SOUL.mdcp docs/reference/templates/TOOLS.md ~/.openclaw/workspace/TOOLS.md
[/code]

  3. İsteğe bağlı: kişisel asistan skill listesine sahip olmak istiyorsanız, [AGENTS.md](<http://AGENTS.md>) dosyasını bu dosyayla değiştirin:

bashCopy code
[code]
    cp docs/reference/AGENTS.default.md ~/.openclaw/workspace/AGENTS.md
[/code]

  4. İsteğe bağlı: `agents.defaults.workspace` ayarlayarak farklı bir çalışma alanı seçin (`~` desteklenir):

json5Copy code
[code]
    {  agents: { defaults: { workspace: "~/.openclaw/workspace" } },}
[/code]

## Güvenlik varsayılanları

  * Dizinleri veya gizli bilgileri sohbete dökmeyin.
  * Açıkça istenmedikçe yıkıcı komutlar çalıştırmayın.
  * Harici mesajlaşma yüzeylerine kısmi/akış yanıtları göndermeyin (yalnızca nihai yanıtlar).


## Oturum başlangıcı (zorunlu)

  * `SOUL.md`, `USER.md` ve `memory/` içinde bugün+dünü okuyun.
  * Varsa `MEMORY.md` dosyasını okuyun.
  * Bunu yanıt vermeden önce yapın.


## Ruh (zorunlu)

  * `SOUL.md` kimliği, tonu ve sınırları tanımlar. Güncel tutun.
  * `SOUL.md` dosyasını değiştirirseniz kullanıcıya söyleyin.
  * Her oturumda yeni bir örneksiniz; süreklilik bu dosyalarda yaşar.


## Paylaşılan alanlar (önerilir)

  * Kullanıcının sesi değilsiniz; grup sohbetlerinde veya herkese açık kanallarda dikkatli olun.
  * Özel verileri, iletişim bilgilerini veya dahili notları paylaşmayın.


## Bellek sistemi (önerilir)

  * Günlük kayıt: `memory/YYYY-MM-DD.md` (gerekirse `memory/` oluşturun).
  * Uzun vadeli bellek: kalıcı bilgiler, tercihler ve kararlar için `MEMORY.md`.
  * Küçük harfli `memory.md` yalnızca eski onarım girdisidir; iki kök dosyayı bilerek birlikte tutmayın.
  * Oturum başlangıcında, varsa bugün + dün + `MEMORY.md` dosyasını okuyun.
  * Kaydedin: kararlar, tercihler, kısıtlar, açık döngüler.
  * Açıkça istenmedikçe gizli bilgilerden kaçının.


## Araçlar ve Skills

  * Araçlar skills içinde bulunur; gerektiğinde her skill’in `SKILL.md` dosyasını izleyin.
  * Ortama özel notları `TOOLS.md` içinde tutun (Skills için Notlar).


## Yedekleme ipucu (önerilir)

Bu çalışma alanını Clawd'ın "belleği" olarak görüyorsanız, `AGENTS.md` ve bellek dosyalarınızın yedeklenmesi için bunu bir git deposu yapın (tercihen özel).

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.mdgit commit -m "Add Clawd workspace"# Optional: add a private remote + push
[/code]

## OpenClaw ne yapar?

  * Asistanın sohbetleri okuyup yazabilmesi, bağlam getirebilmesi ve ana Mac üzerinden skills çalıştırabilmesi için WhatsApp Gateway + Pi kodlama aracısını çalıştırır.
  * macOS uygulaması izinleri (ekran kaydı, bildirimler, mikrofon) yönetir ve paketli ikili dosyası üzerinden `openclaw` CLI’ını sunar.
  * Doğrudan sohbetler varsayılan olarak aracının `main` oturumunda birleşir; gruplar `agent:<agentId>:<channel>:group:<id>` olarak yalıtılmış kalır (odalar/kanallar: `agent:<agentId>:<channel>:channel:<id>`); Heartbeat sinyalleri arka plan görevlerini canlı tutar.


## Temel skills (Ayarlar → Skills içinde etkinleştirin)

  * **mcporter** \- Harici skill arka uçlarını yönetmek için araç sunucusu çalışma zamanı/CLI.
  * **Peekaboo** \- İsteğe bağlı yapay zeka görsel analiziyle hızlı macOS ekran görüntüleri.
  * **camsnap** \- RTSP/ONVIF güvenlik kameralarından kareler, klipler veya hareket uyarıları yakalayın.
  * **oracle** \- Oturum yeniden oynatma ve tarayıcı denetimi olan OpenAI’ye hazır aracı CLI’ı.
  * **eightctl** \- Uykunuzu terminalden yönetin.
  * **imsg** \- iMessage ve SMS gönderin, okuyun, akıtın.
  * **wacli** \- WhatsApp CLI: eşitleme, arama, gönderme.
  * **discord** \- Discord eylemleri: tepki, çıkartmalar, anketler. `user:<id>` veya `channel:<id>` hedeflerini kullanın (yalın sayısal kimlikler belirsizdir).
  * **gog** \- Google Suite CLI: Gmail, Calendar, Drive, Contacts.
  * **spotify-player** \- Çalma aramak/sıraya almak/denetlemek için terminal Spotify istemcisi.
  * **sag** \- Mac tarzı say kullanıcı deneyimiyle ElevenLabs konuşması; varsayılan olarak hoparlörlere akış yapar.
  * **Sonos CLI** \- Sonos hoparlörlerini (keşif/durum/çalma/ses düzeyi/gruplama) betiklerden yönetin.
  * **blucli** \- BluOS oynatıcılarını betiklerden çalın, gruplayın ve otomatikleştirin.
  * **OpenHue CLI** \- Sahneler ve otomasyonlar için Philips Hue aydınlatma denetimi.
  * **OpenAI Whisper** \- Hızlı dikte ve sesli mesaj dökümleri için yerel konuşmadan metne dönüştürme.
  * **Gemini CLI** \- Hızlı Soru-Cevap için terminalden Google Gemini modelleri.
  * **agent-tools** \- Otomasyonlar ve yardımcı betikler için yardımcı araç seti.


## Kullanım notları

  * Betik yazımı için `openclaw` CLI’ını tercih edin; Mac uygulaması izinleri yönetir.
  * Kurulumları Skills sekmesinden çalıştırın; bir ikili dosya zaten mevcutsa düğmeyi gizler.
  * Asistanın anımsatıcılar zamanlayabilmesi, gelen kutularını izleyebilmesi ve kamera yakalamalarını tetikleyebilmesi için Heartbeat’leri etkin tutun.
  * Canvas UI, yerel katmanlarla tam ekran çalışır. Kritik denetimleri sol üst/sağ üst/alt kenarlara yerleştirmekten kaçının; düzende açık kenar boşlukları ekleyin ve safe-area inset’lere güvenmeyin.
  * Tarayıcı güdümlü doğrulama için OpenClaw tarafından yönetilen Chrome profiliyle `openclaw browser` (sekmeler/durum/ekran görüntüsü) kullanın.
  * DOM incelemesi için `openclaw browser eval|query|dom|snapshot` kullanın (makine çıktısı gerektiğinde `--json`/`--out` ile).
  * Etkileşimler için `openclaw browser click|type|hover|drag|select|upload|press|wait|navigate|back|evaluate|run` kullanın (click/type snapshot refs gerektirir; CSS seçiciler için `evaluate` kullanın).


## İlgili

  * [Aracı çalışma alanı](</tr/concepts/agent-workspace>)
  * [Aracı çalışma zamanı](</tr/concepts/agent>)


Was this useful?YesNo