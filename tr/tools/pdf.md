---
title: PDF aracı
source_url: https://docs.openclaw.ai/tr/tools/pdf
scraped_at: 2026-05-25
---

`pdf`, bir veya daha fazla PDF belgesini analiz eder ve metin döndürür.

Hızlı davranış:

  * Anthropic ve Google model sağlayıcıları için yerel sağlayıcı modu.
  * Diğer sağlayıcılar için çıkarma geri dönüş modu (önce metni, gerektiğinde sayfa görsellerini çıkarır).
  * Tekli (`pdf`) veya çoklu (`pdfs`) girdiyi destekler; çağrı başına en fazla 10 PDF.


## Kullanılabilirlik

Araç yalnızca OpenClaw, ajan için PDF özellikli bir model yapılandırmasını çözümleyebildiğinde kaydedilir:

  1. `agents.defaults.pdfModel`
  2. `agents.defaults.imageModel` değerine geri dönüş
  3. ajanın çözümlenen oturum/varsayılan modeline geri dönüş
  4. yerel-PDF sağlayıcıları kimlik doğrulama destekliyse, genel görsel geri dönüş adaylarından önce onları tercih et


Kullanılabilir bir model çözümlenemezse `pdf` aracı gösterilmez.

Kullanılabilirlik notları:

  * Geri dönüş zinciri kimlik doğrulama farkındadır. Yapılandırılmış bir `provider/model` yalnızca OpenClaw ajan için o sağlayıcıda gerçekten kimlik doğrulayabiliyorsa geçerli sayılır.
  * Yerel PDF sağlayıcıları şu anda **Anthropic** ve **Google**.
  * Çözümlenen oturum/varsayılan sağlayıcının zaten yapılandırılmış bir görsel/PDF modeli varsa PDF aracı, kimlik doğrulama destekli diğer sağlayıcılara geri dönmeden önce bunu yeniden kullanır.


## Girdi referansı

Bir PDF yolu veya URL.

En fazla toplam 10 adet olmak üzere birden fazla PDF yolu veya URL.

Analiz istemi.

`1-5` veya `1,3,7-9` gibi sayfa filtresi.

`provider/model` biçiminde isteğe bağlı model geçersiz kılması.

PDF başına MB cinsinden boyut sınırı. Varsayılan olarak `agents.defaults.pdfMaxBytesMb` veya `10`.

Girdi notları:

  * `pdf` ve `pdfs`, yüklemeden önce birleştirilir ve tekilleştirilir.
  * PDF girdisi sağlanmazsa araç hata verir.
  * `pages`, 1 tabanlı sayfa numaraları olarak ayrıştırılır, tekilleştirilir, sıralanır ve yapılandırılmış en fazla sayfa sayısına sınırlandırılır.
  * `maxBytesMb` varsayılan olarak `agents.defaults.pdfMaxBytesMb` veya `10` olur.


## Desteklenen PDF referansları

  * yerel dosya yolu (`~` genişletmesi dahil)
  * `file://` URL
  * `http://` ve `https://` URL
  * `media://inbound/<id>` gibi OpenClaw tarafından yönetilen gelen referanslar


Referans notları:

  * Diğer URI şemaları (örneğin `ftp://`) `unsupported_pdf_reference` ile reddedilir.
  * Korumalı alan modunda uzak `http(s)` URL'leri reddedilir.
  * Yalnızca çalışma alanı dosya ilkesi etkinken, izin verilen köklerin dışındaki yerel dosya yolları reddedilir.
  * Yönetilen gelen referanslara ve OpenClaw'ın gelen medya deposu altındaki yeniden oynatılan yollara, yalnızca çalışma alanı dosya ilkesiyle izin verilir.


## Yürütme modları

### Yerel sağlayıcı modu

Yerel mod, `anthropic` ve `google` sağlayıcıları için kullanılır. Araç ham PDF baytlarını doğrudan sağlayıcı API'lerine gönderir.

Yerel mod sınırları:

  * `pages` desteklenmez. Ayarlanırsa araç bir hata döndürür.
  * Çoklu PDF girdisi desteklenir; her PDF istemden önce yerel belge bloğu / satır içi PDF parçası olarak gönderilir.


### Çıkarma geri dönüş modu

Geri dönüş modu, yerel olmayan sağlayıcılar için kullanılır.

Akış:

  1. Seçilen sayfalardan metin çıkar (`agents.defaults.pdfMaxPages` değerine kadar, varsayılan `20`).
  2. Çıkarılan metin uzunluğu `200` karakterin altındaysa, seçilen sayfaları PNG görsellerine dönüştür ve dahil et.
  3. Çıkarılan içeriği ve istemi seçilen modele gönder.


Geri dönüş ayrıntıları:

  * Sayfa görseli çıkarma `4,000,000` piksel bütçesi kullanır.
  * Hedef model görsel girdiyi desteklemiyorsa ve çıkarılabilir metin yoksa araç hata verir.
  * Metin çıkarma başarılı olursa ancak görsel çıkarma, yalnızca metin destekleyen bir modelde görsel yeteneği gerektirirse OpenClaw işlenen görselleri çıkarır ve çıkarılan metinle devam eder.
  * Çıkarma geri dönüşü, paketlenmiş `document-extract` Plugin'ini kullanır. Plugin, `pdfjs-dist` sahibidir; `@napi-rs/canvas` yalnızca görsel işleme geri dönüşü kullanılabilir olduğunda kullanılır.


## Yapılandırma

json5Copy code
[code]
    {  agents: {    defaults: {      pdfModel: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["openai/gpt-5.4-mini"],      },      pdfMaxBytesMb: 10,      pdfMaxPages: 20,    },  },}
[/code]

Tüm alan ayrıntıları için [Yapılandırma Referansı](</tr/gateway/configuration-reference>) bölümüne bakın.

## Çıktı ayrıntıları

Araç metni `content[0].text` içinde, yapılandırılmış meta verileri ise `details` içinde döndürür.

Yaygın `details` alanları:

  * `model`: çözümlenen model referansı (`provider/model`)
  * `native`: yerel sağlayıcı modu için `true`, geri dönüş için `false`
  * `attempts`: başarıdan önce başarısız olan geri dönüş denemeleri


Yol alanları:

  * tek PDF girdisi: `details.pdf`
  * birden fazla PDF girdisi: `pdf` girdileriyle `details.pdfs[]`
  * korumalı alan yol yeniden yazma meta verileri (geçerli olduğunda): `rewrittenFrom`


## Hata davranışı

  * Eksik PDF girdisi: `pdf required: provide a path or URL to a PDF document` fırlatır
  * Çok fazla PDF: `details.error = "too_many_pdfs"` içinde yapılandırılmış hata döndürür
  * Desteklenmeyen referans şeması: `details.error = "unsupported_pdf_reference"` döndürür
  * `pages` ile yerel mod: net bir `pages is not supported with native PDF providers` hatası fırlatır


## Örnekler

Tek PDF:

jsonCopy code
[code]
    {  "pdf": "/tmp/report.pdf",  "prompt": "Summarize this report in 5 bullets"}
[/code]

Birden fazla PDF:

jsonCopy code
[code]
    {  "pdfs": ["/tmp/q1.pdf", "/tmp/q2.pdf"],  "prompt": "Compare risks and timeline changes across both documents"}
[/code]

Sayfa filtreli geri dönüş modeli:

jsonCopy code
[code]
    {  "pdf": "https://example.com/report.pdf",  "pages": "1-3,7",  "model": "openai/gpt-5.4-mini",  "prompt": "Extract only customer-impacting incidents"}
[/code]

## İlgili

  * [Araçlara Genel Bakış](</tr/tools>) \- kullanılabilir tüm ajan araçları
  * [Yapılandırma Referansı](</tr/gateway/config-agents#agent-defaults>) \- pdfMaxBytesMb ve pdfMaxPages yapılandırması


Was this useful?YesNo