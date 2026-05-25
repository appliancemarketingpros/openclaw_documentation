---
title: Matris sunum meta verileri
source_url: https://docs.openclaw.ai/tr/channels/matrix-presentation
scraped_at: 2026-05-25
---

OpenClaw, giden Matrix `m.room.message` olaylarına `com.openclaw.presentation` altında normalleştirilmiş `MessagePresentation` meta verileri ekleyebilir.

Standart Matrix istemcileri düz metin `body` alanını işlemeye devam eder. OpenClaw uyumlu istemciler yapılandırılmış meta verileri okuyabilir ve düğmeler, seçimler, bağlam satırları ve ayırıcılar gibi yerel kullanıcı arayüzlerini işleyebilir.

## Olay içeriği

Meta veriler Matrix olay içeriğinde saklanır:

jsonCopy code
[code]
    {  "msgtype": "m.text",  "body": "Select model\n\n- DeepSeek: /model deepseek/deepseek-chat",  "com.openclaw.presentation": {    "version": 1,    "type": "message.presentation",    "title": "Select model",    "tone": "info",    "blocks": [      {        "type": "select",        "placeholder": "Choose model",        "options": [          {            "label": "DeepSeek",            "value": "/model deepseek/deepseek-chat"          }        ]      }    ]  }}
[/code]

`version`, Matrix sunum meta verileri şema sürümüdür. `type`, OpenClaw uyumlu istemciler için kararlı bir ayırıcıdır. İstemciler bilinmeyen `type` değerlerini, güvenli biçimde yorumlayamadıkları bilinmeyen sürümleri ve bilinmeyen blok türlerini yok saymalıdır.

## Yedek davranış

OpenClaw her zaman `body` içine okunabilir bir düz metin yedeği işler. Yapılandırılmış meta veriler ek niteliğindedir ve temel Matrix birlikte çalışabilirliği için zorunlu olmamalıdır.

Desteklenmeyen istemciler yedek metni göstermeye devam etmelidir. OpenClaw uyumlu istemciler görüntüleme için yapılandırılmış meta verileri tercih edebilir; ancak kopyalama, arama, bildirimler ve erişilebilirlik için yedek metni korumalıdır.

## Desteklenen bloklar

Matrix giden bağdaştırıcısı şu destekleri bildirir:

  * `buttons`
  * `select`
  * `context`
  * `divider`


İstemciler bu blokları en iyi çaba esaslı sunum ipuçları olarak değerlendirmelidir. Bilinmeyen alanlar ve bilinmeyen blok türleri, iletinin tamamının işlenememesine neden olmak yerine yok sayılmalıdır.

## Etkileşimler

Bu meta veriler Matrix geri çağırma semantiği eklemez. Düğme ve seçim seçeneği değerleri yedek etkileşim yükleridir; genellikle eğik çizgi komutları veya metin komutlarıdır. Etkileşim desteği sunmak isteyen bir Matrix istemcisi, seçilen değeri normal bir ileti olarak odaya geri gönderebilir.

Örneğin, `/model deepseek/deepseek-chat` değerine sahip bir düğme, bu değerin aynı odada şifrelenmiş bir Matrix metin iletisi olarak gönderilmesiyle işlenebilir.

## Onay meta verileriyle ilişkisi

`com.openclaw.presentation`, genel zengin ileti sunumu içindir.

Onay istemleri özel `com.openclaw.approval` meta verilerini kullanır; çünkü onaylar güvenlik açısından hassas durum, kararlar ve yürütme/Plugin ayrıntıları taşır. Aynı olayda her iki meta veri anahtarı da varsa istemciler özel onay işleyicisini tercih etmelidir.

## Medya iletileri

Bir yanıt birden fazla medya URL'si içerdiğinde OpenClaw, her medya URL'si için bir Matrix olayı gönderir. Sunum meta verileri yalnızca ilk medya olayına eklenir; böylece istemcilerin tek bir kararlı yapılandırılmış yükü olur ve yinelenen işleyicilerden kaçınılır.

Sunum meta verilerini kompakt tutun. Kullanıcıya görünür büyük metinler `body` içinde kalmalı ve normal Matrix metin parçalama yolunu kullanmalıdır.

Was this useful?YesNo