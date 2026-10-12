---
title: Microsoft Teams toplantıları Plugin'i
source_url: https://docs.openclaw.ai/tr/plugins/teams-meetings
scraped_at: 2026-10-12
---

CapabilitiesPlugin guides

`teams-meetings` Plugin, OpenClaw Chrome profilinde Microsoft Teams bağlantılarına konuk olarak katılır. `teams.microsoft.com/l/meetup-join/...` altındaki iş bağlantılarını ve `teams.live.com/meet/...` altındaki tüketici bağlantılarını kabul eder. Toplantı oluşturmaz, telefonla bağlanmaz, Microsoft Graph'i çağırmaz veya ses/video kaydı almaz.

## Kurulum

Sesli yanıt, [Google Meet Plugin](</tr/plugins/google-meet>) ile aynı yerel ses ön koşullarını kullanır: macOS, `BlackHole 2ch` sanal ses aygıtı ve SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Plugin varsayılan olarak dâhildir ve etkindir. Yalnızca özelleştirmek için bir girdi ekleyin, ardından kurulumu denetleyin:

json5Copy code
[code]
    {  plugins: {    entries: {      "teams-meetings": {        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

Plugin'in etkin olmasını istemiyorsanız `openclaw plugins disable teams-meetings` komutunu çalıştırın.

bashCopy code
[code]
    openclaw teamsmeetings setupopenclaw teamsmeetings join 'https://teams.microsoft.com/l/meetup-join/...'
[/code]

Chrome, BlackHole ve SoX'u eşleştirilmiş bir macOS Node üzerinde çalıştırmak için `chromeNode.node` kullanın. Node, `teamsmeetings.chrome` ve `browser.proxy` işlemlerine izin vermelidir.

## Modlar

Mod | Davranış  
---|---  
`agent` | Gerçek zamanlı transkripsiyon, yapılandırılmış OpenClaw aracısına danışır; TTS yanıt verir.  
`bidi` | Gerçek zamanlı bir ses modeli doğrudan dinler ve yanıt verir.  
`transcribe` | Canlı altyazı transkript anlık görüntüleriyle yalnızca gözlem amaçlı katılım.  
  
OpenClaw'ın konuşmacılara göre ilişkilendirilmiş notları kalıcı hâle getirebilmesi için her modda toplantıya kabul edildikten sonra Teams canlı altyazıları etkinleştirilir. `transcript` eylemi, yalnızca `transcribe` oturumları için sınırlı canlı arabelleği döndürmeye devam eder. Ayrılma sırasında OpenClaw, kalıcı transkripti ve türetilmiş özeti paylaşılan durum veritabanında depolar; bunları [`openclaw transcripts`](</tr/cli/transcripts>) ile listeleyin veya dışa aktarın.

Otomatik notlar varsayılan olarak etkindir. Kalıcı notları genel olarak devre dışı bırakmak için `transcripts.enabled: false` olarak ayarlayın; açıkça belirtilen `transcribe` modu yine yalnızca sınırlı canlı son bölümünü sunar.

## Konuk katılımı sınırları

Tarayıcı bağdaştırıcısı uygulama ara ekranını kapatır, konuk adını doldurur, kamerayı kapatır, mikrofonu seçilen moda göre yapılandırır ve katıl düğmesine tıklar. Görüşme içi durumda görüşmeyi sonlandırma denetimi kullanılır; lobi, kiracı oturum açma ve aygıt izni durumları, açıkça belirtilmiş manuel işlem nedenleri döndürür. Tüketici toplantısı başlatıcısının yönlendirmeleri ve Chrome tarafından gösterilen `BlackHole 2ch (Virtual)` etiketleri desteklenir.

Teams kiracı ilkesi oturum açmayı, e-posta doğrulamasını veya düzenleyicinin kabulünü zorunlu kılabilir. Bu adımı OpenClaw Chrome profilinde tamamlayın, ardından durumu veya konuşmayı yeniden deneyin. Plugin, kiracı ilkesini atlamaz.

Tüketici Teams web istemcisi; uygulama ara ekranı, konuk adı girişi, katılım öncesi mikrofon/kamera geçişleri, katılım, lobi kabulü, medya izinleri, görüşme içi durum algılama, canlı altyazılar, BlackHole giriş/çıkış yönlendirmesi, ayrılma ve görüşme sonrası algılama için canlı ortamda doğrulanmıştır. İş kiracıları farklı oturum açma, e-posta doğrulama, kabul ve ayrılma onayı ilkeleri uygulayabilir; bildirilen tüm manuel işlemleri OpenClaw Chrome profilinde tamamlayın.

## Araç ve Gateway yüzeyi

`teams_meetings` aracı; `join`, `leave`, `status`, `transcript` ve `speak` işlemlerini destekler. Gateway yöntemleri `teamsmeetings.*` ön ekini kullanır. Node komutu `teamsmeetings.chrome` şeklindedir.

## İlgili

  * [Toplantı Plugin'lerine genel bakış](</tr/plugins/meeting-plugins>)
  * [Microsoft Teams kanalı](</tr/channels/msteams>)


Was this useful?YesNo

Open issue