---
title: Oturum budama
source_url: https://docs.openclaw.ai/tr/concepts/session-pruning
scraped_at: 2026-05-25
---

Oturum budama, her LLM çağrısından önce bağlamdan **eski araç sonuçlarını** budar. Normal konuşma metnini yeniden yazmadan, birikmiş araç çıktılarından (exec sonuçları, dosya okumaları, arama sonuçları) kaynaklanan bağlam şişmesini azaltır.

## Neden önemlidir

Uzun oturumlar, bağlam penceresini şişiren araç çıktıları biriktirir. Bu, maliyeti artırır ve [Compaction](</tr/concepts/compaction>) işlemini gerekenden daha erken zorlayabilir.

Budama özellikle **Anthropic istem önbelleklemesi** için değerlidir. Önbellek TTL süresi dolduktan sonra, sonraki istek tüm istemi yeniden önbelleğe alır. Budama önbelleğe yazma boyutunu azaltır ve maliyeti doğrudan düşürür.

## Nasıl çalışır

  1. Önbellek TTL süresinin dolmasını bekler (varsayılan 5 dakika).
  2. Normal budama için eski araç sonuçlarını bulur (konuşma metni olduğu gibi bırakılır).
  3. Aşırı büyük sonuçları **hafifçe budar** \-- başı ve sonu tutar, araya `...` ekler.
  4. Kalanları **sert şekilde temizler** \-- bir yer tutucuyla değiştirir.
  5. Takip eden isteklerin yeni önbelleği yeniden kullanması için TTL'yi sıfırlar.


## Eski görsel temizliği

OpenClaw ayrıca oturum geçmişinde ham görsel blokları veya istem-hidrasyon medya işaretçileri kalıcı olarak saklayan oturumlar için ayrı bir idempotent yeniden oynatma görünümü oluşturur.

  * Son **3 tamamlanmış turu** bayt düzeyinde korur; böylece son takip istekleri için istem önbelleği önekleri sabit kalır.
  * Yeniden oynatma görünümünde, `user` veya `toolResult` geçmişindeki daha eski, zaten işlenmiş görsel blokları `[image data removed - already processed by model]` ile değiştirilebilir.
  * `[media attached: ...]`, `[Image: source: ...]` ve `media://inbound/...` gibi daha eski metinsel medya referansları `[media reference removed - already processed by model]` ile değiştirilebilir. Geçerli turdaki ek işaretçileri bozulmadan kalır; böylece görsel modeller yeni görselleri yine hidrate edebilir.
  * Ham oturum dökümü yeniden yazılmaz; bu nedenle geçmiş görüntüleyicileri özgün mesaj girdilerini ve bunların görsellerini yine işleyebilir.
  * Bu, normal önbellek-TTL budamasından ayrıdır. Sonraki turlarda tekrarlanan görsel yüklerinin veya eski medya referanslarının istem önbelleklerini bozmasını engellemek için vardır.


## Akıllı varsayılanlar

OpenClaw, Anthropic profilleri için budamayı otomatik etkinleştirir:

Profil türü | Budama etkin | Heartbeat  
---|---|---  
Anthropic OAuth/token kimlik doğrulaması (Claude CLI yeniden kullanımı dahil) | Evet | 1 saat  
API anahtarı | Evet | 30 dk  
  
Açık değerler ayarlarsanız, OpenClaw bunları geçersiz kılmaz.

## Etkinleştirme veya devre dışı bırakma

Anthropic dışı sağlayıcılar için budama varsayılan olarak kapalıdır. Etkinleştirmek için:

json5Copy code
[code]
    {  agents: {    defaults: {      contextPruning: { mode: "cache-ttl", ttl: "5m" },    },  },}
[/code]

Devre dışı bırakmak için: `mode: "off"` ayarlayın.

## Budama ve Compaction

| Budama | Compaction  
---|---|---  
**Ne** | Araç sonuçlarını budar | Konuşmayı özetler  
**Kaydedilir mi?** | Hayır (istek başına) | Evet (dökümde)  
**Kapsam** | Yalnızca araç sonuçları | Tüm konuşma  
  
Birbirlerini tamamlarlar -- budama, Compaction döngüleri arasında araç çıktısını yalın tutar.

## Daha fazla okuma

  * [Compaction](</tr/concepts/compaction>) \-- özetleme tabanlı bağlam azaltma
  * [Gateway yapılandırması](</tr/gateway/configuration>) \-- tüm budama yapılandırma seçenekleri (`contextPruning.*`)


## İlgili

  * [Oturum yönetimi](</tr/concepts/session>)
  * [Oturum araçları](</tr/concepts/session-tool>)
  * [Bağlam motoru](</tr/concepts/context-engine>)


Was this useful?YesNo