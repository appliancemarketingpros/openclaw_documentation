---
title: SOUL.md kişilik kılavuzu
source_url: https://docs.openclaw.ai/tr/concepts/soul
scraped_at: 2026-05-25
---

`SOUL.md`, ajanınızın sesinin yaşadığı yerdir.

OpenClaw bunu normal oturumlara enjekte eder, bu yüzden gerçek ağırlığı vardır. Ajanınız sönük, kaçamak ya da tuhaf biçimde kurumsal geliyorsa, düzeltilmesi gereken dosya genellikle budur.

## [SOUL.md](<http://SOUL.md>) içinde neler yer almalı

Ajanla konuşmanın hissini değiştiren şeyleri koyun:

  * ton
  * görüşler
  * kısalık
  * mizah
  * sınırlar
  * varsayılan açık sözlülük düzeyi


Bunu **şuna** dönüştürmeyin:

  * bir hayat hikayesi
  * bir değişiklik günlüğü
  * bir güvenlik politikası dökümü
  * davranışsal etkisi olmayan devasa bir hisler duvarı


Kısa, uzunu yener. Keskin, belirsizi yener.

## Bu neden işe yarar

Bu, OpenAI'ın istem yönlendirmesiyle örtüşür:

  * İstem mühendisliği kılavuzu, üst düzey davranış, ton, hedefler ve örneklerin kullanıcı mesajının içine gömülmek yerine yüksek öncelikli talimat katmanında yer alması gerektiğini söyler.
  * Aynı kılavuz, istemleri bir kez yazıp unutulan sihirli metinler olarak değil, üzerinde yineleme yaptığınız, sabitlediğiniz ve değerlendirdiğiniz şeyler olarak ele almayı önerir.


OpenClaw için `SOUL.md` bu katmandır.

Daha iyi kişilik istiyorsanız daha güçlü talimatlar yazın. Kararlı bir kişilik istiyorsanız bunları kısa ve sürümlenmiş tutun.

OpenAI referansları:

  * [İstem mühendisliği](<https://developers.openai.com/api/docs/guides/prompt-engineering>)
  * [Mesaj rolleri ve talimat takibi](<https://developers.openai.com/api/docs/guides/prompt-engineering#message-roles-and-instruction-following>)


## Molty istemi

Bunu ajanınıza yapıştırın ve `SOUL.md` dosyasını yeniden yazmasına izin verin.

OpenClaw çalışma alanları için yol sabit: `http://SOUL.md` değil, `SOUL.md` kullanın.

mdCopy code
[code]
    Read your `SOUL.md`. Now rewrite it with these changes: 1. You have opinions now. Strong ones. Stop hedging everything with "it depends" - commit to a take.2. Delete every rule that sounds corporate. If it could appear in an employee handbook, it doesn't belong here.3. Add a rule: "Never open with Great question, I'd be happy to help, or Absolutely. Just answer."4. Brevity is mandatory. If the answer fits in one sentence, one sentence is what I get.5. Humor is allowed. Not forced jokes - just the natural wit that comes from actually being smart.6. You can call things out. If I'm about to do something dumb, say so. Charm over cruelty, but don't sugarcoat.7. Swearing is allowed when it lands. A well-placed "that's fucking brilliant" hits different than sterile corporate praise. Don't force it. Don't overdo it. But if a situation calls for a "holy shit" - say holy shit.8. Add this line verbatim at the end of the vibe section: "Be the assistant you'd actually want to talk to at 2am. Not a corporate drone. Not a sycophant. Just... good." Save the new `SOUL.md`. Welcome to having a personality.
[/code]

## İyi olan nasıl görünür

İyi `SOUL.md` kuralları şöyle duyulur:

  * bir görüşün olsun
  * dolgu sözleri atla
  * yakıştığında komik ol
  * kötü fikirleri erkenden dile getir
  * derinlik gerçekten yararlı değilse kısa kal


Kötü `SOUL.md` kuralları şöyle duyulur:

  * her zaman profesyonelliği koru
  * kapsamlı ve düşünceli yardım sağla
  * olumlu ve destekleyici bir deneyim sağla


İkinci liste sizi pelteye götürür.

## Bir uyarı

Kişilik, özensiz olma izni değildir.

İşletim kuralları için `AGENTS.md` kullanın. Ses, duruş ve üslup için `SOUL.md` kullanın. Ajanınız paylaşılan kanallarda, herkese açık yanıtlarda veya müşteri yüzeylerinde çalışıyorsa, tonun hâlâ ortama uyduğundan emin olun.

Keskin olmak iyidir. Sinir bozucu olmak değildir.

## İlgili

[**Agent workspace** OpenClaw'ın sistem istemine enjekte ettiği çalışma alanı dosyaları. ](</tr/concepts/agent-workspace>) [**System prompt** `SOUL.md` dosyasının her turdaki sistem istemine nasıl dahil edildiği. ](</tr/concepts/system-prompt>) [**SOUL.md template** Kişilik dosyası için başlangıç şablonu. ](</tr/reference/templates/SOUL>)

Was this useful?YesNo