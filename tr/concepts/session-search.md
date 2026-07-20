---
title: Oturum araması
source_url: https://docs.openclaw.ai/tr/concepts/session-search
scraped_at: 2026-07-20
---

AgentsSessions and memory

# Oturum araması

`sessions_search`, kendi geçmiş oturumlarınızdaki kullanıcı ve asistan metinlerinde arama yapar. Her sonuç bir `sessionKey`, zaman damgası, rol ve eşleşen kısa bir alıntı içerir. Çevresindeki konuşmaya ihtiyaç duyduğunuzda döndürülen `sessionKey` değerini `sessions_history` öğesine iletin.

## Görünürlük ve çıktı

Arama, `sessions_history` ile aynı oturum görünürlüğü kurallarını kullanır. Çağıranın görünür oturum ağacının dışındaki sonuçlar, sonuç sınırları uygulanmadan önce kaldırılır. Korumalı alan aracıları, oluşturulan oturum görünürlüğü etkinleştirildiğinde oluşturdukları oturumlarla sınırlı kalır.

Alıntılar modele döndürülmeden önce hassas bilgilerden arındırılır. Sonuçlar ayrıca sayı, alıntı uzunluğu ve toplam yanıt boyutuyla sınırlandırılır.

## Dizin yaşam döngüsü

OpenClaw, her aracının SQLite veritabanındaki transkript satırlarının yanında bir tam metin dizini depolar. Yeni kullanıcı ve asistan mesajları, bunları kalıcılaştıran aynı işlemde dizine eklenir; böylece dizin hiçbir zaman canlı konuşmaların gerisinde kalmaz. Araç sonuçları, akıl yürütme blokları ve görseller hariç tutulur. Yalnızca transkriptin etkin dalında arama yapılabilir.

Dizinden önce oluşturulan transkriptler (örneğin, `openclaw doctor` tarafından içe aktarılan oturumlar) ve etkin dalı geri alınmış oturumlar, bir sonraki aramayla başlayan arka plan uzlaştırması tarafından yeniden dizine eklenir. Bu nedenle `indexing: true` içeren bir yanıt eksik olabilir; dizine ekleme tamamlandıktan sonra yeniden deneyin. Bir oturum silindiğinde, dizin girdileri aynı işlemde kaldırılır.

Arama şu anda SQLite'ın aksan işaretlerini kaldıran Unicode sözcük belirteçleyicisini kullanır. CJK alt dize eşleştirmesi için trigram belirteçleme gelecekte yapılacak bir iyileştirmedir.

## Oturum araması ve bellek araması

Ham oturum transkriptlerindeki tam sözcükler veya ifadeler için `sessions_search` kullanın. Kalıcı bellek dosyaları ve anlamsal hatırlama için [`memory_search`](</tr/concepts/memory-search>) kullanın. Deneysel oturum belleği külliyatı, bu tam transkript aramasının anlamsal tamamlayıcısıdır.

Was this useful?YesNo

Open issue