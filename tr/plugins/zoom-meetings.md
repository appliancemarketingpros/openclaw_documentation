---
title: Zoom toplantıları Plugin'i
source_url: https://docs.openclaw.ai/tr/plugins/zoom-meetings
scraped_at: 2026-10-12
---

CapabilitiesPlugin guides

`zoom-meetings` plugin'i, OpenClaw Chrome profilindeki Zoom Web App üzerinden Zoom toplantı bağlantılarına konuk olarak katılır. `zoom.us/j/...` altındaki toplantı bağlantılarını ve `example.zoom.us/j/...` gibi hesap alt alan adlarını kabul eder. Toplantı oluşturmaz, telefonla bağlanmaz, Zoom Meeting SDK'yı kullanmaz veya ses/video kaydı almaz.

## Kurulum

Sesli yanıt özelliği, [Google Meet plugin'i](</tr/plugins/google-meet>) ile aynı yerel ses ön koşullarını kullanır: macOS, `BlackHole 2ch` sanal ses aygıtı ve SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Plugin varsayılan olarak dahildir ve etkindir. Yalnızca özelleştirmek için bir giriş ekleyin, ardından kurulumu kontrol edin:

json5Copy code
[code]
    {  plugins: {    entries: {      "zoom-meetings": {        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

Plugin'in etkin olmasını istemiyorsanız `openclaw plugins disable zoom-meetings` komutunu çalıştırın.

bashCopy code
[code]
    openclaw zoommeetings setupopenclaw zoommeetings join 'https://zoom.us/j/1234567890'
[/code]

Chrome, BlackHole ve SoX'u eşleştirilmiş bir macOS node'unda çalıştırmak için `chromeNode.node` kullanın. Node, `zoommeetings.chrome` ve `browser.proxy` işlemlerine izin vermelidir.

## Modlar

Mod | Davranış  
---|---  
`agent` | Gerçek zamanlı transkripsiyon, yapılandırılmış OpenClaw aracısına danışır; TTS ile yanıt verir.  
`bidi` | Gerçek zamanlı bir ses modeli doğrudan dinler ve yanıt verir.  
`transcribe` | Canlı altyazı transkript anlık görüntüleriyle yalnızca gözlem amaçlı katılım.  
  
Zoom canlı altyazıları, OpenClaw'ın toplantı notlarını kalıcı olarak saklayabilmesi için her modda toplantıya kabul edildikten sonra etkinleştirilir. `transcript` eylemi yine yalnızca `transcribe` oturumları için sınırlandırılmış canlı arabelleği döndürür. Toplantıdan ayrılırken OpenClaw, kalıcı transkripti ve bundan türetilen özeti paylaşılan durum veritabanında saklar; bunları [`openclaw transcripts`](</tr/cli/transcripts>) ile listeleyin veya dışa aktarın.

Otomatik notlar varsayılan olarak etkindir. Kalıcı notları genel olarak devre dışı bırakmak için `transcripts.enabled: false` ayarını kullanın; açıkça belirtilen `transcribe` modu yine yalnızca kendi sınırlandırılmış canlı son bölümünü sunar.

## Konuk katılımı sınırlamaları

Tarayıcı bağdaştırıcısı **Join from browser** seçeneğini belirler, konuk adını doldurur, kamerayı kapatır, mikrofonu seçilen moda göre yapılandırır ve **Join** düğmesine tıklar. Zoom Web App, `app.zoom.us` altında çalışır; plugin, gezinmeden önce bu kaynağa mikrofon ve hoparlör seçimi izinlerini verir. Görüşme sırasındaki durum için Zoom'un Leave denetimi kullanılır. Lobi, oturum açma, geçiş kodu, CAPTCHA ve aygıt izni durumları, açıkça belirtilmiş manuel işlem gerekçeleri döndürür.

Zoom ana bilgisayar ve hesap politikası, tarayıcıdan katılımı devre dışı bırakabilir; kimlik doğrulaması veya e-posta doğrulaması isteyebilir; CAPTCHA gösterebilir ya da ana bilgisayarın kabulünü gerektirebilir. Bu adımı OpenClaw Chrome profilinde tamamlayın, ardından durum veya konuşma işlemini yeniden deneyin. Plugin, Zoom politikasını atlamaz.

Zoom Web App; uygulama geçiş ekranı, iframe'de konuk adı girişi, katılım öncesi mikrofon ve kamera denetimleri, katılım, tarayıcı ve macOS medya izinleri, görüşme algılama, canlı altyazı etkinleştirme ve ana bilgisayarın sonlandırdığını algılama açısından resmi bir Zoom test toplantısıyla canlı olarak doğrulanmıştır. Lobi ve kimlik doğrulama durumları, ana bilgisayar politikasına bağlıdır ve kararlı bir DOM tanımlayıcısı bulunmadığında metin tabanlı geri dönüşleri korur.

## Araç ve Gateway yüzeyi

`zoom_meetings` aracı; `join`, `leave`, `status`, `transcript` ve `speak` işlemlerini destekler. Gateway yöntemleri `zoommeetings.*` önekini kullanır. Node komutu `zoommeetings.chrome` şeklindedir.

## İlgili

  * [Toplantı plugin'lerine genel bakış](</tr/plugins/meeting-plugins>)


Was this useful?YesNo

Open issue