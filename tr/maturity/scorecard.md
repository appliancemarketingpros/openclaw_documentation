---
title: Olgunluk puan kartı
source_url: https://docs.openclaw.ai/tr/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Olgunluk puan kartı

yayın hazırlığı - taksonomi + QA kanıtlarından oluşturuldu

Neyin hazır, neyin kanıtlanmış ve neyin hâlâ çalışma gerektirdiğine dair pratik bir görünüm.

50 yüzey - 281 yetenek alanı - deterministik kapsam artı insan incelemesinden geçmiş kalite ve eksiksizlik.

Yüzeylere göz at / QA kanıtını incele / [Taksonomiyi oku](</tr/maturity/taxonomy>)

## Bu sayfa ne için kullanılır?

Bu sayfayı tek bir soruya yanıt vermek için kullanın: hangi OpenClaw yüzeyleri bir yayın için güvenilir seçeneklerdir ve bu yargıyı hangi kanıt destekler? Kapsam deterministik QA kanıtlarından gelir; kalite ve eksiksizlik, incelenmiş olgunluk puanları olarak korunur.

## Bir bakışta

67% Olgunluk puanı

Alfa Kalite + eksiksizlik Kapsam Deneysel - %4 Kalite Alfa - %63 Eksiksizlik Beta - %70

Kapsam bilinçli olarak kanıt odaklıdır: bir alan yalnızca uygulama mevcut olduğu için "hazır" hale gelmez. Olgunluk puanı için bir girdi değildir, ancak OpenClaw zaman içinde olgun Kararlı veya daha iyi özellikler için uçtan uca kapsamı %90'ın üzerinde tutmayı hedefler.

## Puan bantları

Deneysel0-50%

Alfa50-70%

Beta70-80%

Kararlı80-95%

Clawesome95-100%

## Yüzey gezgini

Yüzeyler olgunluk düzeyine, eksiksizliğe ve kaliteye göre sıralanır. Yayına hazır seçeneklerin kolayca karşılaştırılabilmesi için LTS desteği her satırın yanında gösterilir.

### Tüm yüzeyler

[CLIM4Kararlı7 alan](</tr/maturity/taxonomy#cli>)

KapsamDeneysel4%

KaliteKararlı83%

TamamlanmaKararlı90%

Kısmi - 6

[Gateway çalışma zamanıM4Kararlı13 alan](</tr/maturity/taxonomy#gateway-runtime>)

KapsamDeneysel6%

KaliteKararlı81%

TamamlanmaKararlı89%

Kısmi - 12

[Linux Gateway ana makinesiM4Kararlı5 alan](</tr/maturity/taxonomy#linux-gateway-host>)

KapsamDeneysel0%

KaliteBeta75%

TamamlanmaKararlı89%

Kısmi - 4

[macOS Gateway ana makinesiM4Kararlı7 alan](</tr/maturity/taxonomy#macos-gateway-host>)

KapsamDeneysel0%

KaliteBeta74%

TamamlanmaKararlı88%

Yok

[DiscordM4Kararlı6 alan](</tr/maturity/taxonomy#discord>)

KapsamDeneysel0%

KaliteBeta73%

TamamlanmaKararlı87%

Kısmi - 4

[Ajan Çalışma ZamanıM3Beta9 alan](</tr/maturity/taxonomy#agent-runtime>)

KapsamDeneysel33%

KaliteBeta78%

TamamlanmaBeta79%

Kısmi - 6

[Oturum, bellek ve bağlam motoruM3Beta9 alan](</tr/maturity/taxonomy#session-memory-and-context-engine>)

KapsamDeneysel30%

KaliteBeta77%

EksiksizlikBeta79%

Kısmi - 6

[Kanal çerçevesiM3Beta8 alan](</tr/maturity/taxonomy#channel-framework>)

KapsamDeneysel13%

KaliteBeta76%

EksiksizlikBeta79%

Kısmi - 5

[Tarayıcı otomasyonu, yürütme ve korumalı alan araçlarıM3Beta3 alan](</tr/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

KapsamDeneysel21%

KaliteBeta75%

EksiksizlikBeta79%

Kısmi - 2

[GözlemlenebilirlikM3Beta5 alan](</tr/maturity/taxonomy#observability>)

KapsamDeneysel18%

KaliteBeta75%

EksiksizlikBeta79%

Kısmi - 3

[OpenAI ve Codex sağlayıcı yoluM3Beta5 alan](</tr/maturity/taxonomy#openai-and-codex-provider-path>)

KapsamDeneysel26%

KaliteBeta74%

EksiksizlikBeta79%

Kısmi - 3

[Gateway Web UygulamasıM3Beta6 alan](</tr/maturity/taxonomy#gateway-web-app>)

KapsamDeneysel4%

KaliteBeta74%

EksiksizlikBeta79%

Yok

[Web arama araçlarıM3Beta4 alan](</tr/maturity/taxonomy#web-search-tools>)

KapsamDeneysel9%

KaliteBeta74%

TamamlanmaBeta79%

Yok

[PluginlerM3Beta9 alan](</tr/maturity/taxonomy#plugins>)

KapsamDeneysel12%

KaliteBeta72%

TamamlanmaBeta79%

Kısmi - 7

[Güvenlik, kimlik doğrulama, eşleştirme ve gizli bilgilerM3Beta6 alan](</tr/maturity/taxonomy#security-auth-pairing-and-secrets>)

KapsamDeneysel16%

KaliteBeta72%

TamamlanmaBeta79%

Kısmi - 5

[Otomasyon: Cron, kancalar, görevler, yoklamaM3Beta6 alan](</tr/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

KapsamDeneysel2%

KaliteBeta72%

TamamlanmaBeta79%

Yok

[Docker ve Podman barındırmaM3Beta4 alan](</tr/maturity/taxonomy#docker-and-podman-hosting>)

KapsamDeneysel7%

KaliteBeta71%

TamamlanmaBeta79%

Yok

[WSL2 üzerinden WindowsM3Beta6 alan](</tr/maturity/taxonomy#windows-via-wsl2>)

KapsamDeneysel6%

KaliteAlfa69%

TamamlanmaBeta79%

Kısmi - 5

[Raspberry Pi ve küçük Linux cihazlarıM3Beta4 alan](</tr/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

KapsamDeneysel0%

KaliteAlfa67%

TamamlanmaBeta79%

Yok

[Anthropic sağlayıcı yoluM3Beta5 alan](</tr/maturity/taxonomy#anthropic-provider-path>)

KapsamDeneysel0%

KaliteBeta71%

TamamlanmaBeta78%

Yok

[TelegramM3Beta5 alan](</tr/maturity/taxonomy#telegram>)

KapsamDeneysel0%

KaliteAlfa68%

TamamlanmaBeta78%

Tam - 5

[SlackM3Beta5 alan](</tr/maturity/taxonomy#slack>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmaBeta78%

Tam - 5

[Google sağlayıcı yoluM3Beta5 alan](</tr/maturity/taxonomy#google-provider-path>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmaBeta78%

Yok

[iMessage ve BlueBubblesM3Beta5 alan](</tr/maturity/taxonomy#imessage-and-bluebubbles>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmaBeta78%

Yok

[macOS eşlikçi uygulamasıM3Beta8 alan](</tr/maturity/taxonomy#macos-companion-app>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmışlıkBeta78%

Yok

[OpenRouter sağlayıcı yoluM3Beta4 alan](</tr/maturity/taxonomy#openrouter-provider-path>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmışlıkBeta78%

Yok

[WhatsAppM3Beta5 alan](</tr/maturity/taxonomy#whatsapp>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmışlıkBeta78%

Yok

[Medya anlama ve medya üretimiM2Alfa6 alan](</tr/maturity/taxonomy#media-understanding-and-media-generation>)

KapsamDeneysel2%

KaliteAlfa64%

TamamlanmışlıkAlfa68%

Yok

[Görüntü, video ve müzik üretim araçlarıM2Alfa5 alan](</tr/maturity/taxonomy#image-video-and-music-generation-tools>)

KapsamDeneysel0%

KaliteAlfa61%

TamamlanmışlıkAlfa68%

Yok

[Yerel model sağlayıcıları: Ollama, vLLM, SGLang, LM StudioM2Alfa5 alan](</tr/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

KapsamDeneysel0%

KaliteAlfa61%

TamamlanmışlıkAlfa68%

Yok

[Uzun kuyruk barındırılan sağlayıcılarM2Alfa3 alan](</tr/maturity/taxonomy#long-tail-hosted-providers>)

KapsamDeneysel0%

KaliteAlfa61%

TamamlanmışlıkAlfa68%

Yok

[Ses ve gerçek zamanlı konuşmaM2Alfa6 alan](</tr/maturity/taxonomy#voice-and-realtime-talk>)

KapsamDeneysel0%

KaliteAlfa61%

TamamlanmaAlfa68%

Yok

[MatrixM2Alfa6 alan](</tr/maturity/taxonomy#matrix>)

KapsamDeneysel0%

KaliteAlfa60%

TamamlanmaAlfa67%

Yok

[Android uygulamasıM2Alfa7 alan](</tr/maturity/taxonomy#android-app>)

KapsamDeneysel0%

KaliteAlfa59%

TamamlanmaAlfa66%

Yok

[Google ChatM2Alfa5 alan](</tr/maturity/taxonomy#google-chat>)

KapsamDeneysel0%

KaliteAlfa59%

TamamlanmaAlfa66%

Yok

[Microsoft TeamsM2Alfa5 alan](</tr/maturity/taxonomy#microsoft-teams>)

KapsamDeneysel0%

KaliteAlfa59%

TamamlanmaAlfa66%

Yok

[SignalM2Alfa5 alan](</tr/maturity/taxonomy#signal>)

KapsamDeneysel0%

KaliteAlfa59%

TamamlanmaAlfa66%

Yok

[TUIM2Alfa5 alan](</tr/maturity/taxonomy#tui>)

KapsamDeneysel0%

KaliteAlfa59%

EksiksizlikAlfa66%

Yok

[Yerel WindowsM2Alfa4 alan](</tr/maturity/taxonomy#native-windows>)

KapsamDeneysel0%

KaliteAlfa58%

EksiksizlikAlfa66%

Kısmi - 1

[ClawHubM2Alfa4 alan](</tr/maturity/taxonomy#clawhub>)

KapsamDeneysel0%

KaliteAlfa58%

EksiksizlikAlfa62%

Yok

[Kubernetes barındırmaM2Alfa4 alan](</tr/maturity/taxonomy#kubernetes-hosting>)

KapsamDeneysel0%

KaliteAlfa55%

EksiksizlikAlfa61%

Yok

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, bölgesel kanallarM2Alfa4 alan](</tr/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

KapsamDeneysel0%

KaliteAlfa55%

EksiksizlikAlfa58%

Yok

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alfa4 alan](</tr/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

KapsamDeneysel0%

KaliteAlfa53%

EksiksizlikAlfa54%

Yok

[OpenClaw Uygulama SDK'sıM2Alfa6 alan](</tr/maturity/taxonomy#openclaw-app-sdk>)

KapsamDeneysel3%

KaliteAlfa54%

TamamlanmışlıkAlfa53%

Yok

[iOS uygulamasıM1Deneysel8 alan](</tr/maturity/taxonomy#ios-app>)

KapsamDeneysel0%

KaliteDeneysel41%

TamamlanmışlıkDeneysel44%

Yok

[Nix kurulum yoluM1Deneysel5 alan](</tr/maturity/taxonomy#nix-install-path>)

KapsamDeneysel0%

KaliteDeneysel41%

TamamlanmışlıkDeneysel44%

Yok

[Sesli Arama kanalıM1Deneysel5 alan](</tr/maturity/taxonomy#voice-call-channel>)

KapsamDeneysel0%

KaliteDeneysel41%

TamamlanmışlıkDeneysel44%

Yok

[watchOS eşlikçi yüzeyleriM1Deneysel5 alan](</tr/maturity/taxonomy#watchos-companion-surfaces>)

KapsamDeneysel0%

KaliteDeneysel41%

TamamlanmışlıkDeneysel44%

Yok

[Linux eşlikçi uygulamasıM0Planlanan5 alan](</tr/maturity/taxonomy#linux-companion-app>)

KapsamDeneysel0%

KaliteDeneysel19%

TamamlanmışlıkDeneysel21%

Yok

[Yerel Windows eşlikçi uygulamasıM0Planlanan5 alan](</tr/maturity/taxonomy#native-windows-companion-app>)

KapsamDeneysel0%

KaliteDeneysel19%

TamamlanmaDeneysel21%

Yok

### Core

[CLIM4Kararlı7 alan](</tr/maturity/taxonomy#cli>)

KapsamDeneysel4%

KaliteKararlı83%

TamamlanmaKararlı90%

Kısmi - 6

[Gateway çalışma zamanıM4Kararlı13 alan](</tr/maturity/taxonomy#gateway-runtime>)

KapsamDeneysel6%

KaliteKararlı81%

TamamlanmaKararlı89%

Kısmi - 12

[Ajan Çalışma ZamanıM3Beta9 alan](</tr/maturity/taxonomy#agent-runtime>)

KapsamDeneysel33%

KaliteBeta78%

TamamlanmaBeta79%

Kısmi - 6

[Oturum, bellek ve bağlam motoruM3Beta9 alan](</tr/maturity/taxonomy#session-memory-and-context-engine>)

KapsamDeneysel30%

KaliteBeta77%

TamamlanmaBeta79%

Kısmi - 6

[Kanal çerçevesiM3Beta8 alan](</tr/maturity/taxonomy#channel-framework>)

KapsamDeneysel13%

KaliteBeta76%

TamamlanmaBeta79%

Kısmi - 5

[GözlemlenebilirlikM3Beta5 alan](</tr/maturity/taxonomy#observability>)

KapsamDeneysel18%

KaliteBeta75%

TamamlanmışlıkBeta79%

Kısmi - 3

[Gateway Web UygulamasıM3Beta6 alan](</tr/maturity/taxonomy#gateway-web-app>)

KapsamDeneysel4%

KaliteBeta74%

TamamlanmışlıkBeta79%

Yok

[PluginlerM3Beta9 alan](</tr/maturity/taxonomy#plugins>)

KapsamDeneysel12%

KaliteBeta72%

TamamlanmışlıkBeta79%

Kısmi - 7

[Güvenlik, kimlik doğrulama, eşleştirme ve sırlarM3Beta6 alan](</tr/maturity/taxonomy#security-auth-pairing-and-secrets>)

KapsamDeneysel16%

KaliteBeta72%

TamamlanmışlıkBeta79%

Kısmi - 5

[Otomasyon: Cron, kancalar, görevler, yoklamaM3Beta6 alan](</tr/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

KapsamDeneysel2%

KaliteBeta72%

TamamlanmışlıkBeta79%

Yok

[Medya anlama ve medya üretimiM2Alfa6 alan](</tr/maturity/taxonomy#media-understanding-and-media-generation>)

KapsamDeneysel2%

KaliteAlfa64%

TamamlanmışlıkAlfa68%

Yok

[Ses ve gerçek zamanlı konuşmaM2Alfa6 alan](</tr/maturity/taxonomy#voice-and-realtime-talk>)

KapsamDeneysel0%

KaliteAlfa61%

TamamlanmışlıkAlfa68%

Yok

[TUIM2Alfa5 alan](</tr/maturity/taxonomy#tui>)

KapsamDeneysel0%

KaliteAlfa59%

TamlıkAlfa66%

Yok

[ClawHubM2Alfa4 alan](</tr/maturity/taxonomy#clawhub>)

KapsamDeneysel0%

KaliteAlfa58%

TamlıkAlfa62%

Yok

[OpenClaw Uygulama SDK'sıM2Alfa6 alan](</tr/maturity/taxonomy#openclaw-app-sdk>)

KapsamDeneysel3%

KaliteAlfa54%

TamlıkAlfa53%

Yok

### Platform

[Linux Gateway ana makinesiM4Kararlı5 alan](</tr/maturity/taxonomy#linux-gateway-host>)

KapsamDeneysel0%

KaliteBeta75%

TamlıkKararlı89%

Kısmi - 4

[macOS Gateway ana makinesiM4Kararlı7 alan](</tr/maturity/taxonomy#macos-gateway-host>)

KapsamDeneysel0%

KaliteBeta74%

TamlıkKararlı88%

Yok

[Docker ve Podman barındırmaM3Beta4 alan](</tr/maturity/taxonomy#docker-and-podman-hosting>)

KapsamDeneysel7%

KaliteBeta71%

TamlıkBeta79%

Yok

[WSL2 üzerinden WindowsM3Beta6 alan](</tr/maturity/taxonomy#windows-via-wsl2>)

KapsamDeneysel6%

KaliteAlfa69%

TamamlanmaBeta79%

Kısmi - 5

[Raspberry Pi ve küçük Linux cihazlarıM3Beta4 alan](</tr/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

KapsamDeneysel0%

KaliteAlfa67%

TamamlanmaBeta79%

Yok

[macOS eşlikçi uygulamasıM3Beta8 alan](</tr/maturity/taxonomy#macos-companion-app>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmaBeta78%

Yok

[Android uygulamasıM2Alfa7 alan](</tr/maturity/taxonomy#android-app>)

KapsamDeneysel0%

KaliteAlfa59%

TamamlanmaAlfa66%

Yok

[Yerel WindowsM2Alfa4 alan](</tr/maturity/taxonomy#native-windows>)

KapsamDeneysel0%

KaliteAlfa58%

TamamlanmaAlfa66%

Kısmi - 1

[Kubernetes barındırmaM2Alfa4 alan](</tr/maturity/taxonomy#kubernetes-hosting>)

KapsamDeneysel0%

KaliteAlfa55%

TamamlanmaAlfa61%

Yok

[iOS uygulamasıM1Deneysel8 alan](</tr/maturity/taxonomy#ios-app>)

KapsamDeneysel0%

KaliteDeneysel41%

TamamlanmaDeneysel44%

Yok

[Nix kurulum yoluM1Deneysel5 alan](</tr/maturity/taxonomy#nix-install-path>)

KapsamDeneysel0%

KaliteDeneysel41%

TamamlanmaDeneysel44%

Yok

[watchOS eşlikçi yüzeyleriM1Deneysel5 alan](</tr/maturity/taxonomy#watchos-companion-surfaces>)

KapsamDeneysel0%

KaliteDeneysel41%

TamamlanmaDeneysel44%

Yok

[Linux eşlikçi uygulamasıM0Planlandı5 alan](</tr/maturity/taxonomy#linux-companion-app>)

KapsamDeneysel0%

KaliteDeneysel19%

TamamlanmaDeneysel21%

Yok

[Yerel Windows eşlikçi uygulamasıM0Planlandı5 alan](</tr/maturity/taxonomy#native-windows-companion-app>)

KapsamDeneysel0%

KaliteDeneysel19%

TamamlanmaDeneysel21%

Yok

### Kanal

[DiscordM4Kararlı6 alan](</tr/maturity/taxonomy#discord>)

KapsamDeneysel0%

KaliteBeta73%

TamamlanmaKararlı87%

Kısmi - 4

[TelegramM3Beta5 alan](</tr/maturity/taxonomy#telegram>)

KapsamDeneysel0%

KaliteAlfa68%

TamamlanmışlıkBeta78%

Tam - 5

[SlackM3Beta5 alan](</tr/maturity/taxonomy#slack>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmışlıkBeta78%

Tam - 5

[iMessage ve BlueBubblesM3Beta5 alan](</tr/maturity/taxonomy#imessage-and-bluebubbles>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmışlıkBeta78%

Yok

[WhatsAppM3Beta5 alan](</tr/maturity/taxonomy#whatsapp>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmışlıkBeta78%

Yok

[MatrixM2Alfa6 alan](</tr/maturity/taxonomy#matrix>)

KapsamDeneysel0%

KaliteAlfa60%

TamamlanmışlıkAlfa67%

Yok

[Google ChatM2Alfa5 alan](</tr/maturity/taxonomy#google-chat>)

KapsamDeneysel0%

KaliteAlfa59%

TamamlanmışlıkAlfa66%

Yok

[Microsoft TeamsM2Alfa5 alan](</tr/maturity/taxonomy#microsoft-teams>)

KapsamDeneysel0%

KaliteAlfa59%

TamlıkAlpha66%

Yok

[SignalM2Alpha5 alan](</tr/maturity/taxonomy#signal>)

KapsamDeneysel0%

KaliteAlpha59%

TamlıkAlpha66%

Yok

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, bölgesel kanallarM2Alpha4 alan](</tr/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

KapsamDeneysel0%

KaliteAlpha55%

TamlıkAlpha58%

Yok

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 alan](</tr/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

KapsamDeneysel0%

KaliteAlpha53%

TamlıkAlpha54%

Yok

[Sesli Arama kanalıM1Deneysel5 alan](</tr/maturity/taxonomy#voice-call-channel>)

KapsamDeneysel0%

KaliteDeneysel41%

TamlıkDeneysel44%

Yok

### Sağlayıcı ve araç

[Tarayıcı otomasyonu, exec ve sandbox araçlarıM3Beta3 alan](</tr/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

KapsamDeneysel21%

KaliteBeta75%

TamlıkBeta79%

Kısmi - 2

[OpenAI ve Codex sağlayıcı yoluM3Beta5 alan](</tr/maturity/taxonomy#openai-and-codex-provider-path>)

KapsamDeneysel26%

KaliteBeta74%

TamamlanmaBeta79%

Kısmi - 3

[Web arama araçlarıM3Beta4 alan](</tr/maturity/taxonomy#web-search-tools>)

KapsamDeneysel9%

KaliteBeta74%

TamamlanmaBeta79%

Yok

[Anthropic sağlayıcı yoluM3Beta5 alan](</tr/maturity/taxonomy#anthropic-provider-path>)

KapsamDeneysel0%

KaliteBeta71%

TamamlanmaBeta78%

Yok

[Google sağlayıcı yoluM3Beta5 alan](</tr/maturity/taxonomy#google-provider-path>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmaBeta78%

Yok

[OpenRouter sağlayıcı yoluM3Beta4 alan](</tr/maturity/taxonomy#openrouter-provider-path>)

KapsamDeneysel0%

KaliteAlfa66%

TamamlanmaBeta78%

Yok

[Görüntü, video ve müzik üretme araçlarıM2Alfa5 alan](</tr/maturity/taxonomy#image-video-and-music-generation-tools>)

KapsamDeneysel0%

KaliteAlfa61%

TamamlanmaAlfa68%

Yok

[Yerel model sağlayıcıları: Ollama, vLLM, SGLang, LM StudioM2Alfa5 alan](</tr/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

KapsamDeneysel0%

KaliteAlfa61%

TamamlanmaAlfa68%

Yok

[Uzun kuyruklu barındırılan sağlayıcılarM2Alfa3 alan](</tr/maturity/taxonomy#long-tail-hosted-providers>)

KapsamDeneysel0%

KaliteAlfa61%

TamlıkAlfa68%

Yok

## QA kanıt özeti

Aşağıdaki kontroller, QA profil kanıtlarıyla hangi puan kartı alanlarının çalıştırıldığını gösterir.

Tam taksonomi doğrulaması 2026-06-23T07:24:36.128Z 96 kontrol - 94 geçti, 2 engellendi 281 alanın 0'ı (0%) - 1675 özelliğin 20'si (1.2%) - 1665 kapsam kimliğinin 77'si (4.6%)

### Alana göre hazır olma durumu

Her kategorinin kanıt durumunu incelemek için bir yüzey açın. Liste daraltılmış kalır, böylece sayfa ilk bakışta kullanışlı olmaya devam eder.

Ajan Çalışma Zamanı - 9 alan

8 kısmen gözden geçirildi / 1 gözden geçirilmeli

Ajan Tur Yürütmesi Kısmen gözden geçirildi - Tam taksonomi doğrulaması

3'ün 0'ı (0%) / 24'ün 7'si (29.2%) 17 yetenek boşluğu

Harici Çalışma Zamanları ve Alt Ajanlar Kısmen gözden geçirildi - Tam taksonomi doğrulaması

4'ün 0'ı (0%) / 10'un 3'ü (30%) 7 yetenek boşluğu

Barındırılan Sağlayıcı Yürütmesi Kısmen gözden geçirildi - Tam taksonomi doğrulaması

5'in 1'i (20%) / 5'in 1'i (20%) 4 yetenek boşluğu

Yerel ve Kendi Barındırılan Sağlayıcılar Gözden geçirilmeli - Tam taksonomi doğrulaması

5'in 0'ı (0%) / 5'in 0'ı (0%) 5 yetenek boşluğu

Model ve Çalışma Zamanı Seçimi Kısmen gözden geçirildi - Tam taksonomi doğrulaması

4'ün 0'ı (0%) / 8'in 2'si (25%) 6 yetenek boşluğu

Sağlayıcı Kimlik Doğrulaması Kısmen gözden geçirildi - Tam taksonomi doğrulaması

10'un 0'ı (0%) / 17'nin 4'ü (23.5%) 13 yetenek boşluğu

Akış ve İlerleme Kısmen gözden geçirildi - Tam taksonomi doğrulaması

2'nin 0'ı (0%) / 9'un 5'i (55.6%) 4 yetenek boşluğu

Araç Çağrıları ve Yanıt İşleme Kısmen gözden geçirildi - Tam taksonomi doğrulaması

3'ün 0'ı (0%) / 23'ün 15'i (65.2%) 8 yetenek boşluğu

Araç Yürütme Denetimleri Kısmen gözden geçirildi - Tam taksonomi doğrulaması

6'nın 0'ı (0%) / 12'nin 6'sı (50%) 6 yetenek boşluğu

Android uygulaması - 7 alan

7 gözden geçirilmeli

Bağlantı Kurulumu Gözden geçirilmeli - Tam taksonomi doğrulaması

1'in 0'ı (0%) / 1'in 0'ı (0%) 1 yetenek boşluğu

Cihaz Çalışma Zamanı Gözden geçirilmeli - Tam taksonomi doğrulaması

2'nin 0'ı (0%) / 2'nin 0'ı (0%) 2 yetenek boşluğu

Dağıtım Gözden geçirilmeli - Tam taksonomi doğrulaması

3'ün 0'ı (0%) / 3'ün 0'ı (0%) 3 yetenek boşluğu

Medya Yakalama Gözden geçirilmeli - Tam taksonomi doğrulaması

1'in 0'ı (0%) / 1'in 0'ı (0%) 1 yetenek boşluğu

Mobil Sohbet Gözden geçirilmeli - Tam taksonomi doğrulaması

1'in 0'ı (0%) / 1'in 0'ı (0%) 1 yetenek boşluğu

Ayarlar Gözden geçirilmeli - Tam taksonomi doğrulaması

1'in 0'ı (0%) / 1'in 0'ı (0%) 1 yetenek boşluğu

Ses Gözden geçirilmeli - Tam taksonomi doğrulaması

1'in 0'ı (0%) / 1'in 0'ı (0%) 1 yetenek boşluğu

Anthropic sağlayıcı yolu - 5 alan

5 gözden geçirilmeli

Medya Girdileri Gözden geçirilmeli - Tam taksonomi doğrulaması

4'ün 0'ı (0%) / 4'ün 0'ı (0%) 4 yetenek boşluğu

Model ve Çalışma Zamanı Seçimi Gözden geçirilmeli - Tam taksonomi doğrulaması

10'un 0'ı (0%) / 12'nin 0'ı (0%) 12 yetenek boşluğu

İstem Önbelleği ve Bağlam Gözden geçirilmeli - Tam taksonomi doğrulaması

5'in 0'ı (0%) / 5'in 0'ı (0%) 5 yetenek boşluğu

Sağlayıcı Kimlik Doğrulaması ve Kurtarma Gözden geçirilmeli - Tam taksonomi doğrulaması

9'un 0'ı (0%) / 9'un 0'ı (0%) 9 yetenek boşluğu

İstek Aktarımı ve Tur Semantiği Gözden geçirilmeli - Tam taksonomi doğrulaması

10'un 0'ı (0%) / 10'un 0'ı (0%) 10 yetenek boşluğu

Otomasyon: Cron, kancalar, görevler, yoklama - 6 alan

5 inceleme gerekli / 1 kısmen incelendi

Otomasyon Kancaları İnceleme gerekli - Tam taksonomi doğrulaması

11 üzerinden 0 (%0) / 11 üzerinden 0 (%0) 11 yetenek boşluğu

Arka Plan Görevleri ve Akışları İnceleme gerekli - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek boşluğu

Cron İşleri İnceleme gerekli - Tam taksonomi doğrulaması

15 üzerinden 0 (%0) / 15 üzerinden 0 (%0) 15 yetenek boşluğu

Olay Girişi İnceleme gerekli - Tam taksonomi doğrulaması

15 üzerinden 0 (%0) / 15 üzerinden 0 (%0) 15 yetenek boşluğu

Heartbeat Kısmen incelendi - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 7 üzerinden 1 (%14,3) 6 yetenek boşluğu

Yoklama Denetimleri İnceleme gerekli - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek boşluğu

Tarayıcı otomasyonu, yürütme ve korumalı alan araçları - 3 alan

2 kısmen incelendi / 1 inceleme gerekli

Tarayıcı Otomasyonu Kısmen incelendi - Tam taksonomi doğrulaması

8 üzerinden 1 (%12,5) / 8 üzerinden 1 (%12,5) 7 yetenek boşluğu

Korumalı Alan ve Araç Politikası İnceleme gerekli - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek boşluğu

Araç Çağırma ve Yürütme Kısmen incelendi - Tam taksonomi doğrulaması

6 üzerinden 2 (%33,3) / 8 üzerinden 4 (%50) 4 yetenek boşluğu

Gateway Web Uygulaması - 6 alan

3 inceleme gerekli / 3 kısmen incelendi

Tarayıcı Erişimi ve Güven İnceleme gerekli - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Tarayıcı Gerçek Zamanlı Konuşması İnceleme gerekli - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Tarayıcı Arayüzü Kısmen incelendi - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 12 üzerinden 1 (%8,3) 11 yetenek boşluğu

Yapılandırma İnceleme gerekli - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Operatör Konsolu Kısmen incelendi - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 12 üzerinden 1 (%8,3) 11 yetenek boşluğu

WebChat Konuşmaları Kısmen incelendi - Tam taksonomi doğrulaması

15 üzerinden 0 (%0) / 20 üzerinden 2 (%10) 18 yetenek boşluğu

Kanal çerçevesi - 8 alan

4 inceleme gerekli / 4 kısmen incelendi

Kanal Eylemleri, Komutları ve Onayları İnceleme gerekli - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Kanal Kurulumu Kısmen incelendi - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 7 üzerinden 1 (%14,3) 6 yetenek boşluğu

Konuşma Yönlendirme ve Teslim Kısmen incelendi - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 27 üzerinden 5 (%18,5) 22 yetenek boşluğu

Grup Dizisi ve Ortam Odası Davranışı Kısmen incelendi - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 11 üzerinden 4 (%36,4) 7 yetenek boşluğu

Gelen Erişim ve Kimlik Kapıları İnceleme gerekli - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Medya Ekleri ve Zengin Kanal Verileri İnceleme gerekli - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek boşluğu

Giden Teslim ve Yanıt İşlem Hattı Kısmen incelendi - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 21 üzerinden 8 (%38,1) 13 yetenek boşluğu

Durum Sağlığı ve Operatör Denetimleri İnceleme gerekli - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek boşluğu

ClawHub - 4 alan

4 inceleme gerekiyor

Katalog Keşfi İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 5 üzerinden 0 (0%) 5 yetenek açığı

Uyumluluk ve Güven İnceleme gerekiyor - Tam taksonomi doğrulaması

12 üzerinden 0 (0%) / 12 üzerinden 0 (0%) 12 yetenek açığı

Plugin Yaşam Döngüsü ve Sağlığı İnceleme gerekiyor - Tam taksonomi doğrulaması

26 üzerinden 0 (0%) / 26 üzerinden 0 (0%) 26 yetenek açığı

Yayınlama İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (0%) / 7 üzerinden 0 (0%) 7 yetenek açığı

CLI - 7 alan

5 inceleme gerekiyor / 2 kısmen incelendi

CLI Gözlemlenebilirliği İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 5 üzerinden 0 (0%) 5 yetenek açığı

CLI Kurulumu Kısmen incelendi - Tam taksonomi doğrulaması

6 üzerinden 1 (16.7%) / 6 üzerinden 1 (16.7%) 5 yetenek açığı

Doctor İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (0%) / 10 üzerinden 0 (0%) 10 yetenek açığı

Gateway Hizmet Yönetimi Kısmen incelendi - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 7 üzerinden 1 (14.3%) 6 yetenek açığı

Başlangıç Yapılandırması ve Kimlik Doğrulama Kurulumu İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 5 üzerinden 0 (0%) 5 yetenek açığı

Plugin ve Kanal Kurulumu İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 5 üzerinden 0 (0%) 5 yetenek açığı

Güncellemeler ve Yükseltmeler İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 5 üzerinden 0 (0%) 5 yetenek açığı

Discord - 6 alan

6 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (0%) / 6 üzerinden 0 (0%) 6 yetenek açığı

Kanal Kurulumu ve Operasyonlar İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (0%) / 10 üzerinden 0 (0%) 10 yetenek açığı

Konuşma Yönlendirme ve Teslimat İnceleme gerekiyor - Tam taksonomi doğrulaması

12 üzerinden 0 (0%) / 12 üzerinden 0 (0%) 12 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (0%) / 1 üzerinden 0 (0%) 1 yetenek açığı

Yerel Denetimler ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 5 üzerinden 0 (0%) 5 yetenek açığı

Gerçek Zamanlı Ses ve Çağrılar İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (0%) / 5 üzerinden 0 (0%) 5 yetenek açığı

Docker ve Podman barındırma - 4 alan

3 inceleme gerekiyor / 1 kısmen incelendi

Ajan Sandbox'ı ve Araçlar İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (0%) / 3 üzerinden 0 (0%) 3 yetenek açığı

Konteyner Operasyonları İnceleme gerekiyor - Tam taksonomi doğrulaması

11 üzerinden 0 (0%) / 11 üzerinden 0 (0%) 11 yetenek açığı

Konteyner Kurulumu İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (0%) / 6 üzerinden 0 (0%) 6 yetenek açığı

İmaj Sürümü ve Doğrulama Kısmen incelendi - Tam taksonomi doğrulaması

5 üzerinden 1 (20%) / 7 üzerinden 2 (28.6%) 5 yetenek açığı

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, bölgesel kanallar - 4 alan

4 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Kanal Kurulumu ve Operasyonları İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Konuşma Yönlendirme ve Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Gateway çalışma zamanı - 13 alan

9 inceleme gerekiyor / 4 kısmen incelendi

Onaylar ve Uzaktan Yürütme İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Cihaz Kimlik Doğrulaması ve Eşleştirme İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek açığı

Gateway Yaşam Döngüsü Kısmen incelendi - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 12 üzerinden 4 (%33,3) 8 yetenek açığı

Gateway RPC API'leri ve Olayları Kısmen incelendi - Tam taksonomi doğrulaması

20 üzerinden 0 (%0) / 22 üzerinden 2 (%9,1) 20 yetenek açığı

Sağlık, Tanılama ve Onarım İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Barındırılan Web Yüzeyi İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

HTTP API'leri Kısmen incelendi - Tam taksonomi doğrulaması

4 üzerinden 1 (%25) / 4 üzerinden 1 (%25) 3 yetenek açığı

Ağ Erişimi ve Keşif İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Node'lar ve Uzak Yetenekler İnceleme gerekiyor - Tam taksonomi doğrulaması

8 üzerinden 0 (%0) / 8 üzerinden 0 (%0) 8 yetenek açığı

Protokol Uyumluluğu İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Roller ve İzinler İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Güvenlik Denetimleri İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

WebSocket Bağlantısı Kısmen incelendi - Tam taksonomi doğrulaması

8 üzerinden 1 (%12,5) / 8 üzerinden 1 (%12,5) 7 yetenek açığı

Google Chat - 5 alan

5 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

11 üzerinden 0 (%0) / 11 üzerinden 0 (%0) 11 yetenek açığı

Kanal Kurulumu ve Operasyonları İnceleme gerekiyor - Tam taksonomi doğrulaması

16 üzerinden 0 (%0) / 16 üzerinden 0 (%0) 16 yetenek açığı

Konuşma Yönlendirme ve Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Yerel Denetimler ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

16 üzerinden 0 (%0) / 16 üzerinden 0 (%0) 16 yetenek açığı

Google sağlayıcı yolu - 5 alan

5 için inceleme gerekiyor

Doğrudan Gemini Çalışma Zamanı İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Medya, Arama ve Gerçek Zamanlı İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek açığı

Model Yönlendirme ve Uç Noktalar İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek açığı

İstem Önbelleğe Alma İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Sağlayıcı Kurulumu ve Kimlik Bilgileri İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek açığı

Görsel, video ve müzik oluşturma araçları - 5 alan

5 için inceleme gerekiyor

Görsel Oluşturma İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Medya Yönlendirme ve Keşif İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Müzik Oluşturma İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Görev Yaşam Döngüsü ve Teslimi İnceleme gerekiyor - Tam taksonomi doğrulaması

12 üzerinden 0 (%0) / 12 üzerinden 0 (%0) 12 yetenek açığı

Video Oluşturma İnceleme gerekiyor - Tam taksonomi doğrulaması

11 üzerinden 0 (%0) / 11 üzerinden 0 (%0) 11 yetenek açığı

iMessage ve BlueBubbles - 5 alan

5 için inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Kanal Kurulumu ve Operasyonlar İnceleme gerekiyor - Tam taksonomi doğrulaması

11 üzerinden 0 (%0) / 11 üzerinden 0 (%0) 11 yetenek açığı

Konuşma Yönlendirme ve Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Yerel Kontroller ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

iOS uygulaması - 8 alan

8 için inceleme gerekiyor

Tuval ve Ekran İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Sohbet ve Oturumlar İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Cihaz Komutları İnceleme gerekiyor - Tam taksonomi doğrulaması

2 üzerinden 0 (%0) / 2 üzerinden 0 (%0) 2 yetenek açığı

Dağıtım İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Gateway Kurulumu ve Tanılama İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Medya ve Paylaşım İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Bildirimler ve Arka Plan İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Ses İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Kubernetes barındırma - 4 alan

4 inceleme gerekiyor

Erişim ve Maruz Bırakma İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Küme Yaşam Döngüsü İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Yapılandırma ve Gizli Bilgiler İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Dağıtım Kurulumu İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Linux eşlikçi uygulaması - 5 alan

5 inceleme gerekiyor

Uygulama Dağıtımı İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek boşluğu

Sohbet ve Oturumlar İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek boşluğu

Masaüstü Yetenekleri İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek boşluğu

Gateway Bağlantısı İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek boşluğu

Durum ve Tanılama İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek boşluğu

Linux Gateway ana makinesi - 5 alan

5 inceleme gerekiyor

Dağıtım Hedefleri İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek boşluğu

Tanılama ve Onarım İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek boşluğu

Gateway Çalışma Zamanı ve Hizmet Denetimi İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek boşluğu

Ana Makine Kurulumu ve Güncellemeler İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek boşluğu

Uzaktan Erişim ve Güvenlik İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek boşluğu

Yerel model sağlayıcıları: Ollama, vLLM, SGLang, LM Studio - 5 alan

5 inceleme gerekiyor

Yerel Bellek ve Embedding'ler İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek boşluğu

Yerel Sağlayıcı Plugin'leri İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek boşluğu

Ağ Güvenliği ve İstem Denetimleri İnceleme gerekiyor - Tam taksonomi doğrulaması

2 üzerinden 0 (%0) / 2 üzerinden 0 (%0) 2 yetenek boşluğu

OpenAI Uyumlu Çalışma Zamanı Uyumluluğu İnceleme gerekiyor - Tam taksonomi doğrulaması

8 üzerinden 0 (%0) / 8 üzerinden 0 (%0) 8 yetenek boşluğu

Sağlayıcı Kurulumu, Yaşam Döngüsü ve Tanılama İnceleme gerekiyor - Tam taksonomi doğrulaması

12 üzerinden 0 (%0) / 12 üzerinden 0 (%0) 12 yetenek boşluğu

Uzun kuyruklu barındırılan sağlayıcılar - 3 alan

3 inceleme gerekiyor

Barındırılan LLM Sağlayıcıları İnceleme gerekiyor - Tam taksonomi doğrulaması

12 üzerinden 0 (%0) / 12 üzerinden 0 (%0) 12 yetenek boşluğu

Barındırılan Medya Sağlayıcıları İnceleme gerekiyor - Tam taksonomi doğrulaması

8 üzerinden 0 (%0) / 8 üzerinden 0 (%0) 8 yetenek boşluğu

Sağlayıcı Operasyonları İnceleme gerekiyor - Tam taksonomi doğrulaması

12 üzerinden 0 (%0) / 12 üzerinden 0 (%0) 12 yetenek boşluğu

macOS yardımcı uygulaması - 8 alan

8 inceleme gerekiyor

Tuval İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Yerel Kurulum İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Yerel Yetenekler İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Uzak Bağlantılar İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

Uzak Web Sohbeti İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Durum ve Ayarlar İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Ses ve Konuşma İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

Web Sohbeti İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

macOS Gateway ana makinesi - 7 alan

7 inceleme gerekiyor

CLI Kurulumu İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Tanılama ve Gözlemlenebilirlik İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Gateway Hizmet Yaşam Döngüsü İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek açığı

Yerel Gateway Entegrasyonu İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

İzinler ve Yerel Yetenekler İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Profiller ve Yalıtım İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Uzak Gateway Modu İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Matrix - 6 alan

6 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Kanal Kurulumu ve İşlemleri İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Konuşma Yönlendirme ve Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Şifreleme ve Doğrulama İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Yerel Kontroller ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 alan

4 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Kanal Kurulumu ve Operasyonları İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Konuşma Yönlendirme ve Teslimi İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Medya anlama ve medya üretimi - 6 alan

4 inceleme gerekiyor / 2 kısmen incelendi

Kanal Medyası İşleme İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Medya Yapılandırması İnceleme gerekiyor - Tam taksonomi doğrulaması

1 üzerinden 0 (%0) / 1 üzerinden 0 (%0) 1 yetenek açığı

Medya Üretimi Kısmen incelendi - Tam taksonomi doğrulaması

17 üzerinden 1 (%5.9) / 19 üzerinden 1 (%5.3) 18 yetenek açığı

Medya Alımı ve Erişimi İnceleme gerekiyor - Tam taksonomi doğrulaması

8 üzerinden 0 (%0) / 8 üzerinden 0 (%0) 8 yetenek açığı

Medya Anlama Kısmen incelendi - Tam taksonomi doğrulaması

12 üzerinden 0 (%0) / 14 üzerinden 1 (%7.1) 13 yetenek açığı

Metinden Konuşmaya Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

2 üzerinden 0 (%0) / 2 üzerinden 0 (%0) 2 yetenek açığı

Microsoft Teams - 5 alan

5 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Kanal Kurulumu ve Operasyonları İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Konuşma Yönlendirme ve Teslimi İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Yerel Kontroller ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Yerel Windows - 4 alan

4 inceleme gerekiyor

CLI İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Gateway Yönetimi İnceleme gerekiyor - Tam taksonomi doğrulaması

11 üzerinden 0 (%0) / 11 üzerinden 0 (%0) 11 yetenek açığı

Ağ İletişimi İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Güncellemeler İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Yerel Windows eşlikçi uygulaması - 5 alan

5 inceleme gerekiyor

Sohbet Oturumları İnceleme gerekiyor - Tam taksonomi doğrulaması

2'de 0 (%0) / 2'de 0 (%0) 2 yetenek boşluğu

Masaüstü Araçları ve İzinler İnceleme gerekiyor - Tam taksonomi doğrulaması

10'da 0 (%0) / 10'da 0 (%0) 10 yetenek boşluğu

Gateway Bağlantısı İnceleme gerekiyor - Tam taksonomi doğrulaması

3'te 0 (%0) / 3'te 0 (%0) 3 yetenek boşluğu

Kurulum ve Güncellemeler İnceleme gerekiyor - Tam taksonomi doğrulaması

4'te 0 (%0) / 4'te 0 (%0) 4 yetenek boşluğu

Durum ve Onarım İnceleme gerekiyor - Tam taksonomi doğrulaması

5'te 0 (%0) / 5'te 0 (%0) 5 yetenek boşluğu

Nix kurulum yolu - 5 alan

5 inceleme gerekiyor

Etkinleştirme ve Uygulama UX'i İnceleme gerekiyor - Tam taksonomi doğrulaması

7'de 0 (%0) / 7'de 0 (%0) 7 yetenek boşluğu

Yapılandırma ve Durum İnceleme gerekiyor - Tam taksonomi doğrulaması

7'de 0 (%0) / 7'de 0 (%0) 7 yetenek boşluğu

Kurulum Devri İnceleme gerekiyor - Tam taksonomi doğrulaması

4'te 0 (%0) / 4'te 0 (%0) 4 yetenek boşluğu

Plugin Yaşam Döngüsü İnceleme gerekiyor - Tam taksonomi doğrulaması

4'te 0 (%0) / 4'te 0 (%0) 4 yetenek boşluğu

Hizmet Çalışma Zamanı ve Korumalar İnceleme gerekiyor - Tam taksonomi doğrulaması

8'de 0 (%0) / 8'de 0 (%0) 8 yetenek boşluğu

OpenAI ve Codex sağlayıcı yolu - 5 alan

2 inceleme gerekiyor / 3 kısmen incelendi

Görüntü ve Çok Modlu Girdi İnceleme gerekiyor - Tam taksonomi doğrulaması

2'de 0 (%0) / 2'de 0 (%0) 2 yetenek boşluğu

Model ve Kimlik Doğrulama Kısmen incelendi - Tam taksonomi doğrulaması

6'da 1 (%16,7) / 9'da 4 (%44,4) 5 yetenek boşluğu

Yerel Codex Harness Kısmen incelendi - Tam taksonomi doğrulaması

2'de 0 (%0) / 9'da 4 (%44,4) 5 yetenek boşluğu

Yanıtlar ve Araç Uyumluluğu Kısmen incelendi - Tam taksonomi doğrulaması

4'te 1 (%25) / 5'te 2 (%40) 3 yetenek boşluğu

Ses ve Gerçek Zamanlı Ses İnceleme gerekiyor - Tam taksonomi doğrulaması

2'de 0 (%0) / 2'de 0 (%0) 2 yetenek boşluğu

OpenClaw Uygulama SDK'sı - 6 alan

5 inceleme gerekiyor / 1 kısmen incelendi

Ajan Konuşmaları İnceleme gerekiyor - Tam taksonomi doğrulaması

6'da 0 (%0) / 6'da 0 (%0) 6 yetenek boşluğu

İstemci API'si İnceleme gerekiyor - Tam taksonomi doğrulaması

4'te 0 (%0) / 4'te 0 (%0) 4 yetenek boşluğu

Uyumluluk İnceleme gerekiyor - Tam taksonomi doğrulaması

5'te 0 (%0) / 5'te 0 (%0) 5 yetenek boşluğu

Olaylar ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

5'te 0 (%0) / 5'te 0 (%0) 5 yetenek boşluğu

Gateway Erişimi İnceleme gerekiyor - Tam taksonomi doğrulaması

5'te 0 (%0) / 5'te 0 (%0) 5 yetenek boşluğu

Kaynak Yardımcıları Kısmen incelendi - Tam taksonomi doğrulaması

5'te 0 (%0) / 6'da 1 (%16,7) 5 yetenek boşluğu

OpenRouter sağlayıcı yolu - 4 alan

4 için inceleme gerekiyor

Sohbet Çalışma Zamanı ve Normalleştirme İnceleme gerekiyor - Tam taksonomi doğrulaması

15 üzerinden 0 (%0) / 15 üzerinden 0 (%0) 15 yetenek açığı

Medya Oluşturma ve Konuşma İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Sağlayıcı Kurtarma ve Tanılama İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Sağlayıcı Kurulumu ve Kimlik Doğrulama İnceleme gerekiyor - Tam taksonomi doğrulaması

14 üzerinden 0 (%0) / 14 üzerinden 0 (%0) 14 yetenek açığı

Plugin'ler - 9 alan

6 için inceleme gerekiyor / 3 kısmen incelendi

Plugin yazma ve paketleme İnceleme gerekiyor - Tam taksonomi doğrulaması

8 üzerinden 0 (%0) / 8 üzerinden 0 (%0) 8 yetenek açığı

Paketle gelen Plugin'ler İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Canvas Plugin'i İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Kanal Plugin'leri İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Plugin'leri kurma ve çalıştırma Kısmen incelendi - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 20 üzerinden 7 (%35) 13 yetenek açığı

Plugin onayları İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Sağlayıcı ve araç Plugin'leri Kısmen incelendi - Tam taksonomi doğrulaması

6 üzerinden 1 (%16,7) / 21 üzerinden 9 (%42,9) 12 yetenek açığı

Plugin'leri yayımlama İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Plugin'leri test etme Kısmen incelendi - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 11 üzerinden 3 (%27,3) 8 yetenek açığı

Raspberry Pi ve küçük Linux cihazları - 4 alan

4 için inceleme gerekiyor

Gateway Çalışma Zamanı İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek açığı

Performans ve Tanılama İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Uzaktan Erişim ve Kimlik Doğrulama İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Kurulum ve Uyumluluk İnceleme gerekiyor - Tam taksonomi doğrulaması

12 üzerinden 0 (%0) / 12 üzerinden 0 (%0) 12 yetenek açığı

Güvenlik, kimlik doğrulama, eşleştirme ve sırlar - 6 alan

2 kısmen incelendi / 4 için inceleme gerekiyor

Onay Politikası ve Araç Güvenceleri Kısmen incelendi - Tam taksonomi doğrulaması

2 üzerinden 0 (%0) / 6 üzerinden 3 (%50) 3 yetenek açığı

Kanal Erişim Denetimi İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

Kimlik Bilgisi ve Sır Hijyeni Kısmen incelendi - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 11 üzerinden 5 (%45,5) 6 yetenek açığı

Cihaz ve Node Eşleştirme İnceleme gerekiyor - Tam taksonomi doğrulaması

11 üzerinden 0 (%0) / 11 üzerinden 0 (%0) 11 yetenek açığı

Gateway Kimlik Doğrulaması ve Uzaktan Erişim İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Plugin Güveni İnceleme gerekiyor - Tam taksonomi doğrulaması

2 üzerinden 0 (%0) / 2 üzerinden 0 (%0) 2 yetenek açığı

Oturum, bellek ve bağlam motoru - 9 alan

2 inceleme gerekiyor / 7 kısmen incelendi

CLI Oturum ve Döküm Yönetimi İnceleme gerekiyor - Tam taksonomi doğrulaması

2'den 0 (%0) / 2'den 0 (%0) 2 yetenek açığı

Bağlam Motoru Kısmen incelendi - Tam taksonomi doğrulaması

2'den 0 (%0) / 7'den 4 (%57,1) 3 yetenek açığı

Çekirdek İstemler ve Bağlam Kısmen incelendi - Tam taksonomi doğrulaması

2'den 0 (%0) / 8'den 3 (%37,5) 5 yetenek açığı

Çapraz İstemci Geçmişi ve Oturum Eşdeğerliği Kısmen incelendi - Tam taksonomi doğrulaması

2'den 0 (%0) / 5'ten 2 (%40) 3 yetenek açığı

Tanılama, Bakım ve Kurtarma Kısmen incelendi - Tam taksonomi doğrulaması

3'ten 0 (%0) / 10'dan 4 (%40) 6 yetenek açığı

Bellek Kısmen incelendi - Tam taksonomi doğrulaması

5'ten 0 (%0) / 13'ten 6 (%46,2) 7 yetenek açığı

Oturum Yönlendirme Kısmen incelendi - Tam taksonomi doğrulaması

2'den 0 (%0) / 4'ten 1 (%25) 3 yetenek açığı

Token Yönetimi Kısmen incelendi - Tam taksonomi doğrulaması

3'ten 0 (%0) / 10'dan 2 (%20) 8 yetenek açığı

Döküm Kalıcılığı İnceleme gerekiyor - Tam taksonomi doğrulaması

2'den 0 (%0) / 2'den 0 (%0) 2 yetenek açığı

Signal - 5 alan

5 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

6'dan 0 (%0) / 6'dan 0 (%0) 6 yetenek açığı

Kanal Kurulumu ve İşlemleri İnceleme gerekiyor - Tam taksonomi doğrulaması

7'den 0 (%0) / 7'den 0 (%0) 7 yetenek açığı

Konuşma Yönlendirme ve Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

1'den 0 (%0) / 1'den 0 (%0) 1 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

7'den 0 (%0) / 7'den 0 (%0) 7 yetenek açığı

Yerel Denetimler ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

3'ten 0 (%0) / 3'ten 0 (%0) 3 yetenek açığı

Slack - 5 alan

5 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

1'den 0 (%0) / 1'den 0 (%0) 1 yetenek açığı

Kanal Kurulumu ve İşlemleri İnceleme gerekiyor - Tam taksonomi doğrulaması

10'dan 0 (%0) / 10'dan 0 (%0) 10 yetenek açığı

Konuşma Yönlendirme ve Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

5'ten 0 (%0) / 5'ten 0 (%0) 5 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

1'den 0 (%0) / 1'den 0 (%0) 1 yetenek açığı

Yerel Denetimler ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

8'den 0 (%0) / 8'den 0 (%0) 8 yetenek açığı

Telegram - 5 alan

5 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

10'dan 0 (%0) / 10'dan 0 (%0) 10 yetenek açığı

Kanal Kurulumu ve İşlemleri İnceleme gerekiyor - Tam taksonomi doğrulaması

10'dan 0 (%0) / 10'dan 0 (%0) 10 yetenek açığı

Konuşma Yönlendirme ve Teslim İnceleme gerekiyor - Tam taksonomi doğrulaması

1'den 0 (%0) / 1'den 0 (%0) 1 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

1'den 0 (%0) / 1'den 0 (%0) 1 yetenek açığı

Yerel Denetimler ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

9'dan 0 (%0) / 9'dan 0 (%0) 9 yetenek açığı

Gözlemlenebilirlik - 5 alan

3 kısmen incelendi / 2 inceleme gerekli

Tanılama Verilerini Toplama Kısmen incelendi - Tam taksonomi doğrulaması

8'de 1 (12.5%) / 10'da 3 (30%) 7 yetkinlik boşluğu

Sağlık ve Onarım Kısmen incelendi - Tam taksonomi doğrulaması

12'de 1 (8.3%) / 18'de 5 (27.8%) 13 yetkinlik boşluğu

Günlükleme İnceleme gerekli - Tam taksonomi doğrulaması

5'te 0 (0%) / 5'te 0 (0%) 5 yetkinlik boşluğu

Oturum Tanılaması İnceleme gerekli - Tam taksonomi doğrulaması

4'te 0 (0%) / 4'te 0 (0%) 4 yetkinlik boşluğu

Telemetri Dışa Aktarımı Kısmen incelendi - Tam taksonomi doğrulaması

13'te 1 (7.7%) / 21'de 7 (33.3%) 14 yetkinlik boşluğu

TUI - 5 alan

5 inceleme gerekli

Girdi ve Komutlar İnceleme gerekli - Tam taksonomi doğrulaması

8'de 0 (0%) / 8'de 0 (0%) 8 yetkinlik boşluğu

Yerel Kabuk Yürütme İnceleme gerekli - Tam taksonomi doğrulaması

4'te 0 (0%) / 4'te 0 (0%) 4 yetkinlik boşluğu

İşleme ve Çıktı Güvenliği İnceleme gerekli - Tam taksonomi doğrulaması

4'te 0 (0%) / 4'te 0 (0%) 4 yetkinlik boşluğu

Çalışma Zamanı Modları İnceleme gerekli - Tam taksonomi doğrulaması

14'te 0 (0%) / 14'te 0 (0%) 14 yetkinlik boşluğu

Oturum Yönetimi İnceleme gerekli - Tam taksonomi doğrulaması

3'te 0 (0%) / 3'te 0 (0%) 3 yetkinlik boşluğu

Ses ve gerçek zamanlı konuşma - 6 alan

6 inceleme gerekli

Yerel Uygulama Konuşması İnceleme gerekli - Tam taksonomi doğrulaması

4'te 0 (0%) / 4'te 0 (0%) 4 yetkinlik boşluğu

Gerçek Zamanlı Konuşma Oturumları İnceleme gerekli - Tam taksonomi doğrulaması

11'de 0 (0%) / 11'de 0 (0%) 11 yetkinlik boşluğu

Konuşma ve Transkripsiyon İnceleme gerekli - Tam taksonomi doğrulaması

5'te 0 (0%) / 5'te 0 (0%) 5 yetkinlik boşluğu

Konuşma Gözlemlenebilirliği İnceleme gerekli - Tam taksonomi doğrulaması

5'te 0 (0%) / 5'te 0 (0%) 5 yetkinlik boşluğu

Konuşma Sağlayıcıları İnceleme gerekli - Tam taksonomi doğrulaması

7'de 0 (0%) / 7'de 0 (0%) 7 yetkinlik boşluğu

Sesle Uyandırma ve Yönlendirme İnceleme gerekli - Tam taksonomi doğrulaması

4'te 0 (0%) / 4'te 0 (0%) 4 yetkinlik boşluğu

Sesli Arama kanalı - 5 alan

5 inceleme gerekli

Erişim ve Kimlik İnceleme gerekli - Tam taksonomi doğrulaması

1'de 0 (0%) / 1'de 0 (0%) 1 yetkinlik boşluğu

Kanal Kurulumu ve İşlemler İnceleme gerekli - Tam taksonomi doğrulaması

2'de 0 (0%) / 2'de 0 (0%) 2 yetkinlik boşluğu

Konuşma Yönlendirme ve Teslim İnceleme gerekli - Tam taksonomi doğrulaması

1'de 0 (0%) / 1'de 0 (0%) 1 yetkinlik boşluğu

Medya ve Zengin İçerik İnceleme gerekli - Tam taksonomi doğrulaması

2'de 0 (0%) / 2'de 0 (0%) 2 yetkinlik boşluğu

Gerçek Zamanlı Ses ve Aramalar İnceleme gerekli - Tam taksonomi doğrulaması

2'de 0 (0%) / 2'de 0 (0%) 2 yetkinlik boşluğu

watchOS yardımcı yüzeyleri - 5 alan

5 inceleme gerekiyor

İletim ve Kurtarma İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Dağıtım ve Destek İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

Yürütme Onayları İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

Bildirimler ve Yanıtlar İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Watch Uygulaması Kullanıcı Arayüzü İnceleme gerekiyor - Tam taksonomi doğrulaması

3 üzerinden 0 (%0) / 3 üzerinden 0 (%0) 3 yetenek açığı

Web arama araçları - 4 alan

2 inceleme gerekiyor / 2 kısmen incelendi

Ağ Güvenliği İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Arama Sağlayıcıları Kısmen incelendi - Tam taksonomi doğrulaması

19 üzerinden 2 (%10,5) / 19 üzerinden 2 (%10,5) 17 yetenek açığı

Kurulum ve Tanılama İnceleme gerekiyor - Tam taksonomi doğrulaması

9 üzerinden 0 (%0) / 9 üzerinden 0 (%0) 9 yetenek açığı

Araç Kullanılabilirliği ve Getirme Kısmen incelendi - Tam taksonomi doğrulaması

11 üzerinden 2 (%18,2) / 12 üzerinden 3 (%25) 9 yetenek açığı

WhatsApp - 5 alan

5 inceleme gerekiyor

Erişim ve Kimlik İnceleme gerekiyor - Tam taksonomi doğrulaması

7 üzerinden 0 (%0) / 7 üzerinden 0 (%0) 7 yetenek açığı

Kanal Kurulumu ve Operasyonları İnceleme gerekiyor - Tam taksonomi doğrulaması

5 üzerinden 0 (%0) / 5 üzerinden 0 (%0) 5 yetenek açığı

Konuşma Yönlendirme ve İletim İnceleme gerekiyor - Tam taksonomi doğrulaması

4 üzerinden 0 (%0) / 4 üzerinden 0 (%0) 4 yetenek açığı

Medya ve Zengin İçerik İnceleme gerekiyor - Tam taksonomi doğrulaması

2 üzerinden 0 (%0) / 2 üzerinden 0 (%0) 2 yetenek açığı

Yerel Denetimler ve Onaylar İnceleme gerekiyor - Tam taksonomi doğrulaması

2 üzerinden 0 (%0) / 2 üzerinden 0 (%0) 2 yetenek açığı

WSL2 üzerinden Windows - 6 alan

5 inceleme gerekiyor / 1 kısmen incelendi

Tarayıcı ve Kontrol Kullanıcı Arayüzü İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

CLI İnceleme gerekiyor - Tam taksonomi doğrulaması

8 üzerinden 0 (%0) / 8 üzerinden 0 (%0) 8 yetenek açığı

Tanılama ve Onarım Kısmen incelendi - Tam taksonomi doğrulaması

6 üzerinden 1 (%16,7) / 8 üzerinden 3 (%37,5) 5 yetenek açığı

Gateway Erişimi ve Dışa Açılımı İnceleme gerekiyor - Tam taksonomi doğrulaması

11 üzerinden 0 (%0) / 11 üzerinden 0 (%0) 11 yetenek açığı

Gateway Hizmeti Yaşam Döngüsü İnceleme gerekiyor - Tam taksonomi doğrulaması

10 üzerinden 0 (%0) / 10 üzerinden 0 (%0) 10 yetenek açığı

WSL Kurulumu İnceleme gerekiyor - Tam taksonomi doğrulaması

6 üzerinden 0 (%0) / 6 üzerinden 0 (%0) 6 yetenek açığı

> Son güncelleme: 2026-06-22

Was this useful?YesNo

Open issue