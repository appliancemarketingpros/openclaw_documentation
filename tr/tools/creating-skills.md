---
title: Skills oluşturma
source_url: https://docs.openclaw.ai/tr/tools/creating-skills
scraped_at: 2026-05-25
---

Skills, ajana araçları nasıl ve ne zaman kullanacağını öğretir. Her beceri, YAML frontmatter ve markdown talimatları içeren bir `SKILL.md` dosyası bulunan bir dizindir.

Skills'in nasıl yüklendiği ve önceliklendirildiği için bkz. [Skills](</tr/tools/skills>).

## İlk becerinizi oluşturun

* ### Beceri dizinini oluşturun

Skills çalışma alanınızda bulunur. Yeni bir klasör oluşturun:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### SKILL.md yazın

Bu dizinin içinde `SKILL.md` oluşturun. Frontmatter meta verileri tanımlar, markdown gövdesi ise ajan için talimatları içerir.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Beceri `name` değeri için küçük harfler, rakamlar ve kısa çizgilerle hyphen-case kullanın. Klasör adı ile frontmatter `name` değerini uyumlu tutun.

* ### Araçlar ekleyin (isteğe bağlı)

Frontmatter içinde özel araç şemaları tanımlayabilir veya ajana mevcut sistem araçlarını (`exec` ya da `browser` gibi) kullanmasını söyleyebilirsiniz. Skills, belgeledikleri araçlarla birlikte Plugin'lerin içinde de sunulabilir.

* ### Beceriyi yükleyin

OpenClaw'ın beceriyi algılaması için yeni bir oturum başlatın:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Becerinin yüklendiğini doğrulayın:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Test edin

Beceriyi tetiklemesi gereken bir mesaj gönderin:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Ya da ajanla sohbet edip bir selamlama isteyin.

## Beceri meta verileri referansı

YAML frontmatter şu alanları destekler:

Alan | Zorunlu | Açıklama  
---|---|---  
`name` | Evet | Küçük harfler, rakamlar ve kısa çizgiler kullanan benzersiz tanımlayıcı  
`description` | Evet | Ajana gösterilen tek satırlık açıklama  
`metadata.openclaw.os` | Hayır | İşletim sistemi filtresi (`["darwin"]`, `["linux"]` vb.)  
`metadata.openclaw.requires.bins` | Hayır | PATH üzerinde gerekli ikili dosyalar  
`metadata.openclaw.requires.config` | Hayır | Gerekli yapılandırma anahtarları  
  
## En iyi uygulamalar

  * **Kısa ve öz olun** — modele bir yapay zeka nasıl olacağını değil, _ne_ yapacağını söyleyin
  * **Önce güvenlik** — beceriniz `exec` kullanıyorsa, istemlerin güvenilmeyen girdiden rastgele komut enjeksiyonuna izin vermediğinden emin olun
  * **Yerelde test edin** — paylaşmadan önce test etmek için `openclaw agent --message "..."` kullanın
  * **ClawHub kullanın** — [ClawHub](<https://clawhub.ai>) üzerinde becerilere göz atın ve katkıda bulunun


## Becerilerin bulunduğu yerler

Konum | Öncelik | Kapsam  
---|---|---  
`\<workspace\>/skills/` | En yüksek | Ajan başına  
`\<workspace\>/.agents/skills/` | Yüksek | Çalışma alanı ajanı başına  
`~/.agents/skills/` | Orta | Paylaşılan ajan profili  
`~/.openclaw/skills/` | Orta | Paylaşılan (tüm ajanlar)  
Paketlenmiş (OpenClaw ile gönderilir) | Düşük | Küresel  
`skills.load.extraDirs` | En düşük | Özel paylaşılan klasörler  
  
## İlgili

  * [Skills referansı](</tr/tools/skills>) — yükleme, öncelik ve geçit kuralları
  * [Skills yapılandırması](</tr/tools/skills-config>) — `skills.*` yapılandırma şeması
  * [ClawHub](</tr/clawhub>) — herkese açık beceri kayıt yeri
  * [Plugin Oluşturma](</tr/plugins/building-plugins>) — Plugin'ler becerilerle birlikte sunulabilir


Was this useful?YesNo