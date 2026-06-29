---
title: Gizli Yer Tutucu Kuralları
source_url: https://docs.openclaw.ai/tr/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Gizli değer yer tutucu kuralları

İnsan tarafından okunabilir olan ancak gerçek gizli değerlere benzemeyen yer tutucular kullanın.

## Önerilen stil

  * `example-openai-key-not-real` veya `example-discord-bot-token` gibi açıklayıcı değerleri tercih edin.
  * Kabuk parçacıkları için satır içi token benzeri dizeler yerine `${OPENAI_API_KEY}` tercih edin.
  * Örnekleri açıkça sahte ve amaca göre kapsamlandırılmış tutun (sağlayıcı, kanal, kimlik doğrulama türü).


## Belgelerde bu kalıplardan kaçının

  * Değişmez PEM özel anahtar üst bilgisi veya alt bilgisi metni.
  * Canlı kimlik bilgilerine benzeyen önekler, örneğin `sk-...`, `xoxb-...`, `AKIA...`.
  * Çalışma zamanı günlüklerinden kopyalanmış gerçekçi görünen bearer token'lar.


## Örnek

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue