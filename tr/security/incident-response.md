---
title: Olay müdahalesi
source_url: https://docs.openclaw.ai/tr/security/incident-response
scraped_at: 2026-08-31
---

Baslangic

## 1\. Tespit ve önceliklendirme

Güvenlik sinyalleri şu kaynaklardan gelir:

  * GitHub Security Advisories (GHSA) ve özel güvenlik açığı bildirimleri.
  * Bildirimlerin hassas olmadığı durumlarda herkese açık GitHub sorunları/tartışmaları.
  * Otomatik sinyaller: Dependabot, CodeQL, npm güvenlik bildirimleri, gizli bilgi taraması.


İlk önceliklendirme:

  1. Etkilenen bileşeni, sürümü ve güven sınırı üzerindeki etkiyi doğrulayın.
  2. `SECURITY.md` kapsam ve kapsam dışı kurallarını kullanarak durumu bir güvenlik sorunu ya da sağlamlaştırma/işlem gerektirmeyen durum olarak sınıflandırın.
  3. Olay sorumlusu buna uygun şekilde yanıt verir.


## 2\. Önem derecesi

Önem derecesi | Tanım  
---|---  
Kritik | Paket/sürüm/depo güvenliğinin ihlal edilmesi, aktif istismar veya yüksek etkili denetim ya da veri ifşasıyla sonuçlanan, kimlik doğrulaması gerektirmeyen güven sınırı atlatması.  
Yüksek | Sınırlı ön koşullar gerektiren doğrulanmış güven sınırı atlatması (örneğin, kimliği doğrulanmış ancak yetkisiz yüksek etkili bir işlem) veya OpenClaw'a ait hassas kimlik bilgilerinin ifşa olması.  
Orta | Pratik etkisi bulunan ancak istismar edilebilirliği kısıtlı veya önemli ön koşullar gerektiren ciddi bir güvenlik zayıflığı.  
Düşük | Derinlemesine savunma bulguları, dar kapsamlı hizmet reddi veya kanıtlanmış bir güven sınırı atlatması bulunmayan sağlamlaştırma/eş değerlik eksiklikleri.  
  
## 3\. Müdahale

  1. Bildirimi aldığınızı bildiren kişiye teyit edin (hassas olduğunda özel olarak).
  2. Desteklenen sürümlerde ve en son `main` üzerinde yeniden oluşturun, ardından gerileme kapsamıyla birlikte bir yama uygulayıp doğrulayın.
  3. Kritik/yüksek: yamalı sürümleri uygulanabilir olduğu ölçüde hızlı hazırlayın.
  4. Orta/düşük: normal sürüm akışında yamalayın ve risk azaltma yönergelerini belgeleyin.


## 4\. İletişim ve açıklama

Etkilenen depodaki GitHub Security Advisories, düzeltilmiş sürümlerin sürüm notları/değişiklik günlüğü girdileri ve durum ile çözüm hakkında bildirim sahibine doğrudan geri dönüş yoluyla iletişim kurun.

Kritik/yüksek önem dereceli olaylar, uygun olduğunda CVE yayımlanmasıyla birlikte koordineli olarak açıklanır. Düşük riskli sağlamlaştırma bulguları, etkiye ve kullanıcıların maruz kalma düzeyine bağlı olarak CVE olmadan sürüm notlarında veya güvenlik bildirimlerinde belgelenebilir.

## 5\. Kurtarma ve takip

Düzeltme yayımlandıktan sonra:

  1. Düzeltmeleri CI'da ve sürüm yapıtlarında doğrulayın.
  2. Kısa bir olay sonrası inceleme gerçekleştirin: zaman çizelgesi, temel neden, tespit eksikliği, önleme planı.
  3. Takip niteliğinde sağlamlaştırma/test/dokümantasyon görevleri ekleyin ve tamamlanana kadar izleyin.


## İlgili

  * [Güvenlik politikası](<https://github.com/openclaw/openclaw/blob/main/SECURITY.md>) — bildirim kapsamı ve güven modeli.
  * [Tehdit modeli](</tr/security/THREAT-MODEL-ATLAS>)


Was this useful?YesNo

Open issue