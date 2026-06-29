---
title: Olgunluk taksonomisi
source_url: https://docs.openclaw.ai/tr/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Olgunluk taksonomisi

puan kartının arkasındaki model

Yüzeyler > kategoriler > yetenekler > kanıt.

50 yüzey 4 ailede gruplandırılır; her kategori standart belgelere ve QA kapsam kimliklerine bağlanır.

Ürün alanlarına göz at / Ayrıntılı taksonomiyi aç / [Puanları görüntüle](</tr/maturity/scorecard>)

## Bu sayfa nasıl okunur?

Yüzey, Gateway çalışma zamanı, Discord veya macOS uygulaması gibi bir ürün alanıdır. Her yüzey kategoriler içerir ve her kategori QA senaryolarının kapsadığı yetenek düzeyindeki denetimleri içerir. Sürüm düzeyinde değerlendirme için puan kartını kullanın; bu sayfayı ise onun altındaki modeli incelemek için kullanın.

## Olgunluk düzeyleri

M0PlanlandıYön biliniyor, ancak desteklenen bir kullanıcı yolu yok.Yükseltme: Tasarım konusu, sahip ve hedef yüzey mevcut.

M1DeneyselUyarılar, bayraklar, kaynak derlemeleri veya yalnızca bakımcı akışları arkasında uygulanmıştır.Yükseltme: Bakımcı senaryoyu mevcut main üzerinden çalıştırabilir.

M2AlfaGerçek kullanıcılar deneyebilir, ancak kırıcı değişiklikler ve eksik kullanıcı deneyimi beklenir.Yükseltme: Belgelenmiş kurulum, temel testler, bilinen uyarılar ve en az bir gerçek ortam kanıtı.

M3BetaHerkese açık yol mevcuttur ve ana iş akışı sınırlı uyarılarla kullanılabilir.Yükseltme: Kurulum/güncelleme belgeleri, regresyon testleri, destek runbook'u ve beklenen ortam genelinde başarılı senaryo kanıtı.

M4KararlıNormal kullanıcılar için önerilen yol. Hatalar regresyon olarak ele alınır.Yükseltme: Sürüm kapısı, doctor/sorun giderme yolu, kapsamlı belgeler ve tekrarlanan gerçek dünya kanıtı.

M5Clawesomeİyi cilalanmış, keyifli, iyi enstrümante edilmiş ve en iyi karşılaştırılabilir iş akışıyla rekabet edebilir.Yükseltme: Stable artı temsili kullanıcılar genelinde kullanıcı puan kartı geçişi.

## Ürün alanları

### Çekirdek

CLI M4Kararlı7 alan - %90 tamamlandı Gateway çalışma zamanı M4Kararlı13 alan - %89 tamamlandı Agent Çalışma Zamanı M3Beta9 alan - %79 tamamlandı Oturum, bellek ve bağlam motoru M3Beta9 alan - %79 tamamlandı Kanal çatısı M3Beta8 alan - %79 tamamlandı Gözlemlenebilirlik M3Beta5 alan - %79 tamamlandı Gateway Web Uygulaması M3Beta6 alan - %79 tamamlandı Plugins M3Beta9 alan - %79 tamamlandı Güvenlik, kimlik doğrulama, eşleştirme ve gizli bilgiler M3Beta6 alan - %79 tamamlandı Otomasyon: cron, kancalar, görevler, yoklama M3Beta6 alan - %79 tamamlandı Medya anlama ve medya üretimi M2Alpha6 alan - %68 tamamlandı Ses ve gerçek zamanlı konuşma M2Alpha6 alan - %68 tamamlandı TUI M2Alpha5 alan - %66 tamamlandı ClawHub M2Alpha4 alan - %62 tamamlandı OpenClaw App SDK M2Alpha6 alan - %53 tamamlandı

### Platform

Linux Gateway ana makinesi M4Kararlı5 alan - %89 tamamlandı macOS Gateway ana makinesi M4Kararlı7 alan - %88 tamamlandı Docker ve Podman barındırma M3Beta4 alan - %79 tamamlandı WSL2 üzerinden Windows M3Beta6 alan - %79 tamamlandı Raspberry Pi ve küçük Linux cihazları M3Beta4 alan - %79 tamamlandı macOS yardımcı uygulaması M3Beta8 alan - %78 tamamlandı Android uygulaması M2Alpha7 alan - %66 tamamlandı Yerel Windows M2Alpha4 alan - %66 tamamlandı Kubernetes barındırma M2Alpha4 alan - %61 tamamlandı iOS uygulaması M1Deneysel8 alan - %44 tamamlandı Nix kurulum yolu M1Deneysel5 alan - %44 tamamlandı watchOS eşlikçi yüzeyleri M1Deneysel5 alan - %44 tamamlandı Linux eşlikçi uygulaması M0Planlandı5 alan - %21 tamamlandı Yerel Windows eşlikçi uygulaması M0Planlandı5 alan - %21 tamamlandı

### Kanal

Discord M4Kararlı6 alan - %87 tamamlandı Telegram M3Beta5 alan - %78 tamamlandı Slack M3Beta5 alan - %78 tamamlandı iMessage ve BlueBubbles M3Beta5 alan - %78 tamamlandı WhatsApp M3Beta5 alan - %78 tamamlandı Matrix M2Alpha6 alan - %67 tamamlandı Google Chat M2Alpha5 alan - %66 tamamlandı Microsoft Teams M2Alpha5 alan - %66 tamamlandı Signal M2Alpha5 alan - %66 tamamlandı Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, bölgesel kanallar M2Alpha4 alan - %58 tamamlandı Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 alan - %54 tamamlandı Sesli Arama kanalı M1Deneysel5 alan - %44 tamamlandı

### Sağlayıcı ve araç

Tarayıcı otomasyonu, exec ve sandbox araçları M3Beta3 alan - %79 tamamlandı OpenAI ve Codex sağlayıcı yolu M3Beta5 alan - %79 tamamlandı Web arama araçları M3Beta4 alan - %79 tamamlandı Anthropic sağlayıcı yolu M3Beta5 alan - %78 tamamlandı Google sağlayıcı yolu M3Beta5 alan - %78 tamamlandı OpenRouter sağlayıcı yolu M3Beta4 alan - %78 tamamlandı Görüntü, video ve müzik üretme araçları M2Alpha5 alan - %68 tamamlandı Yerel model sağlayıcıları: Ollama, vLLM, SGLang, LM Studio M2Alpha5 alan - %68 tamamlandı Uzun kuyruklu barındırılan sağlayıcılar M2Alpha3 alan - %68 tamamlandı

## Ayrıntılar

### Çekirdek

CLI - M4 Kararlı - 7 alan

Normal kurulum ve onarım yolları kurulum, CLI ve gateway belgeleri genelinde belgelenmiştir. Platforma özgü Windows yolları WSL2 üzerinden Windows ve Yerel Windows satırlarında izlenir.

Kapsam Deneysel - %4Kalite Kararlı - %83Tamlık Kararlı - %90Kısmi - 6

CLI Kurulumu 6 yetenek / LTS destekli

Deneysel17%

Kararlı89%

Kararlı90%

[Dizin](</tr/install>), [Yükleyici](</tr/install/installer>), [Node](</tr/install/node>), [Güncelleme](</tr/install/updating>)

İlk Katılım ve Kimlik Doğrulama Kurulumu 5 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[İlk Katılım](</tr/cli/onboard>), [Yapılandırma](</tr/cli/configure>), [İlk Katılım Genel Bakışı](</tr/start/onboarding-overview>)

Plugin ve Kanal Kurulumu 5 yetenek

Deneysel0%

Beta75%

Kararlı89%

[İlk Katılım](</tr/cli/onboard>), [Plugins](</tr/cli/plugins>), [Kanallar](</tr/cli/channels>)

Gateway Hizmet Yönetimi 5 yetenek / LTS destekli

Deneysel14%

Kararlı87%

Kararlı90%

[Gateway](</tr/cli/gateway>), [Güncelleme](</tr/install/updating>), [Sorun Giderme](</tr/gateway/troubleshooting>)

CLI Gözlemlenebilirliği 5 yetenek / LTS destekli

Deneysel0%

Kararlı89%

Kararlı90%

[Durum](</tr/cli/status>), [Sağlık](</tr/cli/health>), [Günlükler](</tr/cli/logs>), [Tanılama](</tr/gateway/diagnostics>)

Doctor 10 yetenek / LTS destekli

Deneysel0%

Kararlı89%

Kararlı90%

[Doctor](</tr/cli/doctor>), [Doctor](</tr/gateway/doctor>), [Gizli Bilgiler](</tr/gateway/secrets>), [Sorun Giderme](</tr/gateway/troubleshooting>)

Güncellemeler ve Yükseltmeler 5 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Güncelleme](</tr/install/updating>), [Güncelle](</tr/cli/update>), [Sorun Giderme](</tr/gateway/troubleshooting>)

Gateway çalışma zamanı - M4 Kararlı - 13 alan

Temel mimari, kimlik doğrulama, eşleştirme, protokol belgeleri, arka plan programı belgeleri ve CLI çalışma kılavuzları kapsamlı ve günceldir.

Kapsam Deneysel - 6%Kalite Kararlı - 81%Tamamlanmışlık Kararlı - 89%Kısmi - 12

Onaylar ve Uzak Yürütme 6 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Protokol](</tr/gateway/protocol>), [Dizin](</tr/gateway/security>)

HTTP API'leri 4 yetenek / LTS destekli

Deneysel25%

Kararlı90%

Kararlı90%

[Dizin](</tr/gateway>), [Openai HTTP API'si](</tr/gateway/openai-http-api>), [Openresponses HTTP API'si](</tr/gateway/openresponses-http-api>), [Tools Invoke HTTP API'si](</tr/gateway/tools-invoke-http-api>), [Kancalar](</tr/automation/hooks>), [Dizin](</tr/web>)

Barındırılan Web Yüzeyi 4 yetenek / LTS destekli

Deneysel0%

Kararlı89%

Kararlı90%

[Dizin](</tr/gateway>), [Mimari](</tr/concepts/architecture>), [Denetim Kullanıcı Arayüzü](</tr/web/control-ui>), [Web Sohbeti](</tr/web/webchat>), [Tuval](</tr/refactor/canvas>)

Gateway RPC API'leri ve Olaylar 20 yetenek / LTS destekli

Deneysel9%

Kararlı90%

Kararlı90%

[Protokol](</tr/gateway/protocol>), [Dizin](</tr/gateway>), [Mimari](</tr/concepts/architecture>)

Cihaz Kimlik Doğrulaması ve Eşleştirme 10 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Protokol](</tr/gateway/protocol>), [Eşleştirme](</tr/gateway/pairing>), [Dizin](</tr/gateway/security>)

Ağ Erişimi ve Keşif 6 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Dizin](</tr/gateway>), [Keşif](</tr/gateway/discovery>), [Protokol](</tr/gateway/protocol>)

Node'lar ve Uzak Yetenekler 8 yetenek

Deneysel0%

Beta75%

Kararlı89%

[Protokol](</tr/gateway/protocol>), [Mimari](</tr/concepts/architecture>), [Dizin](</tr/nodes>)

Sağlık, Tanılama ve Onarım 7 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Dizin](</tr/gateway>), [Tanılama](</tr/gateway/diagnostics>), [Doktor](</tr/gateway/doctor>)

Protokol Uyumluluğu 7 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Protokol](</tr/gateway/protocol>), [Mimari](</tr/concepts/architecture>), [Typebox](</tr/concepts/typebox>), [Köprü Protokolü](</tr/gateway/bridge-protocol>)

Roller ve İzinler 5 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Protokol](</tr/gateway/protocol>), [Dizin](</tr/gateway/security>)

Gateway Yaşam Döngüsü 7 yetenek / LTS destekli

Deneysel33%

Kararlı90%

Kararlı90%

[Dizin](</tr/gateway>), [Mimari](</tr/concepts/architecture>)

Güvenlik Kontrolleri 6 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Dizin](</tr/gateway/security>), [Protokol](</tr/gateway/protocol>), [Keşif](</tr/gateway/discovery>)

WebSocket Bağlantısı 8 yetenek / LTS destekli

Deneysel13%

Kararlı90%

Kararlı90%

[Protokol](</tr/gateway/protocol>), [Mimari](</tr/concepts/architecture>)

Aracı Çalışma Zamanı - M3 Beta - 9 alan

Ana döngü, modeller, sağlayıcı yönlendirmesi ve araç akışı birinci sınıf özelliklerdir, ancak sağlayıcı davranışı haftalık olarak değişir ve her sürüm için senaryo kanıtı gerektirir.

Kapsam Deneysel - 33%Kalite Beta - 78%Tamamlanmışlık Beta - 79%Kısmi - 6

Agent Sırası Yürütme 3 yetenek / LTS destekli

Deneysel29%

Beta79%

Beta79%

[Agent Döngüsü](</tr/concepts/agent-loop>), [Agent](</tr/cli/agent>), [Agent Çalışma Zamanları](</tr/concepts/agent-runtimes>)

Harici Çalışma Zamanları ve Alt Agent'lar 4 yetenek

Deneysel30%

Beta79%

Beta79%

[Agent Çalışma Zamanları](</tr/concepts/agent-runtimes>), [Anthropic](</tr/providers/anthropic>), [Google](</tr/providers/google>), [Alt Agent'lar](</tr/tools/subagents>)

Barındırılan Sağlayıcı Yürütme 5 yetenek / LTS destekli

Deneysel20%

Beta79%

Beta79%

[Openai](</tr/providers/openai>), [Anthropic](</tr/providers/anthropic>), [Google](</tr/providers/google>), [Modeller](</tr/concepts/models>)

Yerel ve Kendi Barındırılan Sağlayıcılar 5 yetenek

Deneysel0%

Alpha68%

Beta79%

[Ollama](</tr/providers/ollama>), [Modeller](</tr/concepts/models>), [Agent](</tr/cli/agent>)

Model ve Çalışma Zamanı Seçimi 4 yetenek / LTS destekli

Deneysel25%

Beta79%

Beta79%

[Modeller](</tr/concepts/models>), [Modeller](</tr/cli/models>), [Openai](</tr/providers/openai>), [Agent Çalışma Zamanları](</tr/concepts/agent-runtimes>)

Sağlayıcı Kimlik Doğrulaması 10 yetenek / LTS destekli

Deneysel24%

Beta79%

Beta79%

[Modeller](</tr/concepts/models>), [Agent](</tr/cli/agent>), [Modeller](</tr/cli/models>), [Openai](</tr/providers/openai>), [Anthropic](</tr/providers/anthropic>), [Google](</tr/providers/google>), [Alt Agent'lar](</tr/tools/subagents>)

Akış ve İlerleme 2 yetenek

Alpha56%

Beta79%

Beta79%

[Akış](</tr/concepts/streaming>), [Agent Döngüsü](</tr/concepts/agent-loop>)

Araç Çağrıları ve Yanıt İşleme 3 yetenek / LTS destekli

Alpha65%

Beta79%

Beta79%

[Agent Döngüsü](</tr/concepts/agent-loop>), [Ollama](</tr/providers/ollama>)

Araç Yürütme Denetimleri 6 yetenek / LTS destekli

Alpha50%

Beta79%

Beta79%

[Sandbox Vs Araç Politikası Vs Yükseltilmiş](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>), [Ajan Döngüsü](</tr/concepts/agent-loop>), [Alt Ajanlar](</tr/tools/subagents>)

Oturum, bellek ve bağlam motoru - M3 Beta - 9 alan

Güçlü dokümantasyon ve aktif uygulama. Olgunluk; transkript dayanıklılığına, Compaction kalitesine ve istemciler arası eşdeğerliğe bağlıdır.

Kapsam Deneysel - 30%Kalite Beta - 77%Tamamlanma Beta - 79%Kısmi - 6

CLI Oturum ve Transkript Yönetimi 2 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Oturum](</tr/concepts/session>), [Oturum Yönetimi Compaction](</tr/reference/session-management-compaction>), [Oturumlar](</tr/cli/sessions>)

Token Yönetimi 3 yetenek / LTS destekli

Deneysel20%

Beta79%

Beta79%

[Compaction](</tr/concepts/compaction>), [Bağlam](</tr/concepts/context>), [Oturum Yönetimi Compaction](</tr/reference/session-management-compaction>)

Bağlam Motoru 2 yetenek / LTS destekli

Alfa57%

Beta79%

Beta79%

[Bağlam](</tr/concepts/context>), [Bağlam Motoru](</tr/concepts/context-engine>), [Codex Bağlam Motoru Test Düzeneği](</tr/plan/codex-context-engine-harness>)

İstemciler Arası Geçmiş ve Oturum Eşdeğerliği 2 yetenek

Deneysel40%

Beta79%

Beta79%

[Web sohbet](</tr/web/webchat>), [Android](</tr/platforms/android>), [Kanal Yönlendirme](</tr/channels/channel-routing>)

Tanılama, Bakım ve Kurtarma 3 yetenek

Deneysel40%

Beta79%

Beta79%

[Tanılama](</tr/gateway/diagnostics>), [Oturum Yönetimi Compaction](</tr/reference/session-management-compaction>), [Bayraklar](</tr/diagnostics/flags>)

Çekirdek Komut İstemleri ve Bağlam 2 yetenek / LTS destekli

Deneysel38%

Beta79%

Beta79%

[Bağlam](</tr/concepts/context>), [Transkript Hijyeni](</tr/reference/transcript-hygiene>), [Discord](</tr/channels/discord>)

Bellek 5 yetenek

Deneysel46%

Beta79%

Beta79%

[Bellek Yapılandırması](</tr/reference/memory-config>), [Bellek Qmd](</tr/concepts/memory-qmd>), [Bellek](</tr/concepts/memory>), [Discord](</tr/channels/discord>)

Oturum Yönlendirme 2 yetenek / LTS destekli

Deneysel25%

Beta79%

Beta79%

[Oturum](</tr/concepts/session>), [Kanal Yönlendirme](</tr/channels/channel-routing>), [Discord](</tr/channels/discord>)

Transkript Kalıcılığı 2 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Oturum Yönetimi Compaction](</tr/reference/session-management-compaction>), [Transkript Hijyeni](</tr/reference/transcript-hygiene>)

Kanal çatısı - M3 Beta - 8 alan

Birçok kanal Gateway teslim ve yönlendirme sözleşmelerini paylaşır, ancak kanal davranışı yukarı akış API'sine ve hesap ilkesi kısıtlamalarına göre değişir.

Kapsam Deneysel - 13%Kalite Beta - 76%Tamlık Beta - 79%Kısmi - 5

Kanal Eylemleri, Komutları ve Onayları 5 yetenek

Deneysel0%

Beta79%

Beta79%

[Gruplar](</tr/channels/groups>), [Discord](</tr/channels/discord>), [Googlechat](</tr/channels/googlechat>), [Signal](</tr/channels/signal>), [Matrix](</tr/channels/matrix>)

Kanal Kurulumu 5 yetenek / LTS destekli

Deneysel14%

Beta79%

Beta79%

[Dizin](</tr/channels>), [Eşleştirme](</tr/channels/pairing>), [Sorun Giderme](</tr/channels/troubleshooting>), [SDK Kanal Plugin'leri](</tr/plugins/sdk-channel-plugins>)

Grup İş Parçacığı ve Ortam Odası Davranışı 5 yetenek

Deneysel36%

Beta79%

Beta79%

[Gruplar](</tr/channels/groups>), [Grup Mesajları](</tr/channels/group-messages>), [Ortam Odası Olayları](</tr/channels/ambient-room-events>), [Yayın Grupları](</tr/channels/broadcast-groups>), [Discord](</tr/channels/discord>)

Gelen Erişim ve Kimlik Kapıları 5 yetenek / LTS destekli

Deneysel0%

Alpha68%

Beta79%

[Erişim Grupları](</tr/channels/access-groups>), [Gruplar](</tr/channels/groups>), [Discord](</tr/channels/discord>), [LINE](</tr/channels/line>)

Medya Ekleri ve Zengin Kanal Verileri 4 yetenek

Deneysel0%

Alpha68%

Beta79%

[LINE](</tr/channels/line>), [Signal](</tr/channels/signal>), [Googlechat](</tr/channels/googlechat>), [Matrix](</tr/channels/matrix>), [Discord](</tr/channels/discord>)

Giden Teslimat ve Yanıt İş Hattı 4 yetenek / LTS destekli

Deneysel38%

Beta79%

Beta79%

[Gruplar](</tr/channels/groups>), [Ortam Odası Olayları](</tr/channels/ambient-room-events>), [Discord](</tr/channels/discord>), [Matrix](</tr/channels/matrix>), [Yapılandırma Kanalları](</tr/gateway/config-channels>)

Konuşma Yönlendirme ve Teslimat 10 yetenek / LTS destekli

Deneysel19%

Beta79%

Beta79%

[Kanal Yönlendirme](</tr/channels/channel-routing>), [Gruplar](</tr/channels/groups>), [Discord](</tr/channels/discord>), [Matrix](</tr/channels/matrix>), [Sorun Giderme](</tr/channels/troubleshooting>), [Yapılandırma Başvurusu](</tr/gateway/configuration-reference>)

Durum Sağlığı ve Operatör Denetimleri 4 yetenek / LTS destekli

Deneysel0%

Beta79%

Beta79%

[Sağlık](</tr/gateway/health>), [Yapılandırma Referansı](</tr/gateway/configuration-reference>), [Sorun Giderme](</tr/channels/troubleshooting>), [Discord](</tr/channels/discord>)

Observability - M3 Beta - 5 areas

OTel, Prometheus, günlükleme ve tanılama belgeleri mevcut. Herkese açık bir "operatörlerin önce neye bakması gerektiği" olgunluk gözden geçirmesine ihtiyaç var.

Kapsam Deneysel - 18%Kalite Beta - 75%Tamamlanma Beta - 79%Kısmi - 3

Sağlık ve Onarım 12 yetenek / LTS destekli

Deneysel28%

Beta79%

Beta79%

[Sağlık](</tr/gateway/health>), [Telegram](</tr/channels/telegram>), [Doktor](</tr/cli/doctor>), [Doktor](</tr/gateway/doctor>), [SDK Alt Yolları](</tr/plugins/sdk-subpaths>), [Sağlık](</tr/cli/health>), [Protokol](</tr/gateway/protocol>)

Günlükleme 5 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Günlükleme](</tr/logging>), [Günlükleme](</tr/gateway/logging>), [Günlükler](</tr/cli/logs>)

Tanılama Toplama 8 yetenek

Deneysel30%

Beta79%

Beta79%

[Tanılamalar](</tr/gateway/diagnostics>), [Sağlık](</tr/gateway/health>), [Codex Koşumu](</tr/plugins/codex-harness>), [Protokol](</tr/gateway/protocol>)

Telemetri Dışa Aktarma 13 yetenek

Deneysel33%

Beta79%

Beta79%

[Kancalar](</tr/plugins/hooks>), [Opentelemetry](</tr/gateway/opentelemetry>), [Günlükleme](</tr/logging>), [SDK Alt Yolları](</tr/plugins/sdk-subpaths>), [Tanılama Otel](</tr/plugins/reference/diagnostics-otel>), [Prometheus](</tr/gateway/prometheus>), [Tanılama Prometheus](</tr/plugins/reference/diagnostics-prometheus>)

Oturum Tanılamaları 4 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Opentelemetry](</tr/gateway/opentelemetry>), [Prometheus](</tr/gateway/prometheus>), [Tanılamalar](</tr/gateway/diagnostics>), [Protokol](</tr/gateway/protocol>)

Gateway Web Uygulaması - M3 Beta - 6 alan

Web arayüzü eşleme, sohbet, PWA, Talk, anlık bildirim ve uzak Gateway akışlarıyla belgelenmiştir. Tarayıcılar arası ve mobil PWA puan kartlarından sonra yükseltin.

Kapsam Deneysel - 4%Kalite Beta - 74%Tamamlanma Beta - 79%Yok

Tarayıcı Gerçek Zamanlı Konuşma 5 yetenek

Deneysel0%

Alfa68%

Beta79%

[Denetim Arayüzü](</tr/web/control-ui>), [Protokol](</tr/gateway/protocol>), [Konuşma](</tr/nodes/talk>)

Tarayıcı Erişimi ve Güven 5 yetenek

Deneysel0%

Alfa68%

Beta79%

[Denetim Arayüzü](</tr/web/control-ui>), [Pano](</tr/web/dashboard>), [Tailscale](</tr/gateway/tailscale>), [Uzak](</tr/gateway/remote>)

Yapılandırma 5 yetenek

Deneysel0%

Alfa68%

Beta79%

[Denetim Arayüzü](</tr/web/control-ui>), [Yapılandırma](</tr/gateway/configuration>)

Tarayıcı Kullanıcı Arayüzü 10 yetenek

Deneysel8%

Beta79%

Beta79%

[Denetim Arayüzü](</tr/web/control-ui>), [Dizin](</tr/web>), [Pano](</tr/web/dashboard>), [Protokol](</tr/gateway/protocol>)

WebChat Sohbetleri 15 yetenek

Deneysel10%

Beta79%

Beta79%

[Denetim Arayüzü](</tr/web/control-ui>), [Webchat](</tr/web/webchat>), [Başlarken](</tr/start/getting-started>), [Kanal Yönlendirme](</tr/channels/channel-routing>), [Güvenli Dosya İşlemleri](</tr/gateway/security/secure-file-operations>)

Operatör Konsolu 10 yetenek

Deneysel8%

Beta79%

Beta79%

[Denetim Arayüzü](</tr/web/control-ui>), [Sağlık](</tr/gateway/health>), [Protokol](</tr/gateway/protocol>), [Pano](</tr/web/dashboard>)

Pluginler - M3 Beta - 9 alan

Manifestolar, keşif, yükleme, sağlayıcı/araç mimarisi ve onay sınırları genelinde geniş belgeler ve güçlü dahili çalışma zamanı kanıtı mevcut. Herkese açık SDK API/alt yolları ve dış dağıtım kanıtı güçlenene kadar satırı beta düzeyinde tutun.

Kapsam Deneysel - 12%Kalite Beta - 72%Tamamlanma Beta - 79%Kısmi - 7

Plugin yazma ve paketleme 8 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Plugin Oluşturma](</tr/plugins/building-plugins>), [Sdk Genel Bakış](</tr/plugins/sdk-overview>), [Sdk Giriş Noktaları](</tr/plugins/sdk-entrypoints>), [Sdk Alt Yolları](</tr/plugins/sdk-subpaths>), [Manifest](</tr/plugins/manifest>), [Başvuru](</tr/plugins/reference>)

Birlikte gelen Plugin'ler 5 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Plugin Envanteri](</tr/plugins/plugin-inventory>), [Plugin'ler](</tr/cli/plugins>), [Mimari İç Yapısı](</tr/plugins/architecture-internals>)

Canvas Plugin'i 6 yetenek

Deneysel0%

Alfa68%

Beta79%

[Canvas](</tr/plugins/reference/canvas>), [Canvas](</tr/refactor/canvas>), [Yapılandırma Başvurusu](</tr/gateway/configuration-reference>)

Plugin'leri yükleme ve çalıştırma 6 yetenek / LTS destekli

Deneysel35%

Beta79%

Beta79%

[Mimari](</tr/plugins/architecture>), [Mimari İç Yapısı](</tr/plugins/architecture-internals>), [Plugin'ler](</tr/cli/plugins>)

Kanal Plugin'leri 5 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Sdk Kanal Plugin'leri](</tr/plugins/sdk-channel-plugins>), [Sdk Kanal Gelen](</tr/plugins/sdk-channel-inbound>), [Sdk Kanal Giden](</tr/plugins/sdk-channel-outbound>)

Sağlayıcı ve araç Plugin'leri 6 yetenek / LTS destekli

Deneysel43%

Beta79%

Beta79%

[Sdk Sağlayıcı Plugin'leri](</tr/plugins/sdk-provider-plugins>), [Araç Plugin'leri](</tr/plugins/tool-plugins>), [Yetenek Ekleme](</tr/plugins/adding-capabilities>)

Plugin onayları 6 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Plugin İzin İstekleri](</tr/plugins/plugin-permission-requests>), [Exec Onayları](</tr/tools/exec-approvals>), [Sdk Kanal Plugin'leri](</tr/plugins/sdk-channel-plugins>)

Plugin yayımlama 6 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Plugin'ler](</tr/cli/plugins>), [Uyumluluk](</tr/plugins/compatibility>), [Yayınlama](</tr/clawhub/publishing>)

Plugin testleri 6 yetenek

Deneysel27%

Beta79%

Beta79%

[SDK Testi](</tr/plugins/sdk-testing>), [SDK Kurulumu](</tr/plugins/sdk-setup>), [Codex Test Koşumu](</tr/plugins/codex-harness>)

Güvenlik, kimlik doğrulama, eşleştirme ve gizli bilgiler - M3 Beta - 6 alan

İyi belgeler ve sertleştirme yüzeyleri mevcut. Düzenli yükseltme/güvenlik senaryo çalıştırmaları kurulum regresyonu olmadığını kanıtladıktan sonra yükseltin.

Kapsam Experimental - 16%Kalite Beta - 72%Tamlık Beta - 79%Kısmi - 5

Onay Politikası ve Araç Koruma Önlemleri 2 yetenek / LTS destekli

Alpha50%

Beta79%

Beta79%

[Exec Onayları](</tr/tools/exec-approvals>), [Onaylar](</tr/cli/approvals>), [Plugin İzin İstekleri](</tr/plugins/plugin-permission-requests>), [Denetim Kontrolleri](</tr/gateway/security/audit-checks>)

Gateway Kimlik Doğrulaması ve Uzaktan Erişim 9 yetenek / LTS destekli

Experimental0%

Alpha68%

Beta79%

[Dizin](</tr/gateway/security>), [Açığa Çıkarma Runbook'u](</tr/gateway/security/exposure-runbook>), [Güvenilir Proxy Kimlik Doğrulaması](</tr/gateway/trusted-proxy-auth>), [Tailscale](</tr/gateway/tailscale>), [Uzak](</tr/gateway/remote>), [Yapılandırma Referansı](</tr/gateway/configuration-reference>), [Gateway](</tr/cli/gateway>), [Doctor](</tr/cli/doctor>), [Denetim Arayüzü](</tr/web/control-ui>), [Tarayıcı Denetimi](</tr/tools/browser-control>), [Denetim Kontrolleri](</tr/gateway/security/audit-checks>)

Kanal Erişim Denetimi 3 yetenek / LTS destekli

Experimental0%

Alpha68%

Beta79%

[Eşleştirme](</tr/channels/pairing>), [Telegram](</tr/channels/telegram>), [Erişim Grupları](</tr/channels/access-groups>), [Denetim Kontrolleri](</tr/gateway/security/audit-checks>)

Cihaz ve Node Eşleştirmesi 11 yetenek / LTS destekli

Experimental0%

Alpha68%

Beta79%

[Protokol](</tr/gateway/protocol>), [Cihazlar](</tr/cli/devices>), [Eşleştirme](</tr/channels/pairing>), [Eşleştirme](</tr/gateway/pairing>), [Operatör Kapsamları](</tr/gateway/operator-scopes>), [Denetim Arayüzü](</tr/web/control-ui>), [Web Sohbeti](</tr/web/webchat>), [Onaylar](</tr/cli/approvals>)

Plugin Güveni 2 yetenek

Experimental0%

Alpha68%

Beta79%

[Manifest](</tr/plugins/manifest>), [Plugin İzin İstekleri](</tr/plugins/plugin-permission-requests>), [Plugin'leri Yönet](</tr/plugins/manage-plugins>), [Denetim Kontrolleri](</tr/gateway/security/audit-checks>)

Kimlik Bilgisi ve Gizli Bilgi Hijyeni 5 yetenek / LTS destekli

Experimental46%

Beta79%

Beta79%

[Kimlik Doğrulama](</tr/gateway/authentication>), [Modeller](</tr/cli/models>), [Openai](</tr/providers/openai>), [Oauth](</tr/concepts/oauth>), [Gizli Bilgiler](</tr/gateway/secrets>), [Gizli Bilgiler](</tr/cli/secrets>), [Secretref Kimlik Bilgisi Yüzeyi](</tr/reference/secretref-credential-surface>), [Denetim Kontrolleri](</tr/gateway/security/audit-checks>)

Otomasyon: Cron, hook'lar, görevler, yoklama - M3 Beta - 6 alan

Belgelenmiş ve kullanılabilir, ancak senaryo kanıtı gözetimsiz teslimi, yeniden denemeleri ve hata görünürlüğünü kapsamalıdır.

Kapsam Experimental - 2%Kalite Beta - 72%Tamlık Beta - 79%Yok

Cron İşleri 15 yetenek

Deneysel0%

Beta79%

Beta79%

[Cron İşleri](</tr/automation/cron-jobs>), [Cron](</tr/cli/cron>), [Protokol](</tr/gateway/protocol>), [Görevler](</tr/automation/tasks>), [Discord](</tr/channels/discord>)

Olay Girişi 15 yetenek

Deneysel0%

Alpha68%

Beta79%

[Telegram](</tr/channels/telegram>), [Zalo](</tr/channels/zalo>), [Sorun Giderme](</tr/channels/troubleshooting>), [Bluebubbles'tan Imessage](</tr/channels/imessage-from-bluebubbles>), [Gmail Pubsub Entegrasyonu](</tr/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</tr/automation/cron-jobs>), [Webhook'lar](</tr/cli/webhooks>), [Webhook'lar](</tr/automation/cron-jobs#webhooks>), [Webhook](</tr/automation/cron-jobs>)

Otomasyon Kancaları 11 yetenek

Deneysel0%

Alpha68%

Beta79%

[Kancalar](</tr/automation/hooks>), [Kancalar](</tr/cli/hooks>), [Kancalar](</tr/plugins/hooks>), [Plugin İzin İstekleri](</tr/plugins/plugin-permission-requests>), [SDK Alt Yolları](</tr/plugins/sdk-subpaths>)

Arka Plan Görevleri ve Akışları 10 yetenek

Deneysel0%

Alpha68%

Beta79%

[Görevler](</tr/automation/tasks>), [Dizin](</tr/automation>), [Görevler](</tr/cli/tasks>), [TaskFlow](</tr/automation/taskflow>), [SDK Çalışma Zamanı](</tr/plugins/sdk-runtime>)

Heartbeat 5 yetenek

Deneysel14%

Beta79%

Beta79%

[Dizin](</tr/automation>), [Heartbeat](</tr/gateway/heartbeat>), [Taahhütler](</tr/concepts/commitments>)

Yoklama Kontrolleri 10 yetenek

Deneysel0%

Alpha68%

Beta79%

[Yoklama](</tr/cli/message>), [Mesaj](</tr/cli/message>), [Telegram](</tr/channels/telegram>), [Msteams](</tr/channels/msteams>), [Arka Plan Süreci](</tr/gateway/background-process>)

Medya anlama ve medya üretimi - M2 Alpha - 6 alan

Geniş bir yetenek yüzeyi mevcut, ancak sağlayıcı farklılıkları, dosya sınırları ve Node/uygulama eşdeğerliği bunu henüz kararlı yapmıyor.

Kapsam Deneysel - 2%Kalite Alpha - 64%Tamlık Alpha - 68%Yok

Medya Alımı ve Erişimi 8 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Medya Genel Bakışı](</tr/tools/media-overview>), [Medya Anlama](</tr/nodes/media-understanding>), [Güvenli Dosya İşlemleri](</tr/gateway/security/secure-file-operations>), [PDF](</tr/tools/pdf>), [Görsel Oluşturma](</tr/tools/image-generation>), [QR](</tr/cli/qr>), [LINE](</tr/channels/line>), [WhatsApp](</tr/channels/whatsapp>)

Kanal Medyası İşleme 5 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Görseller](</tr/nodes/images>), [Medya Genel Bakışı](</tr/tools/media-overview>), [Discord](</tr/channels/discord>)

Medya Yapılandırması 1 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Medya Genel Bakışı](</tr/tools/media-overview>), [Görsel Oluşturma](</tr/tools/image-generation>), [Manifest](</tr/plugins/manifest>), [Codex Harness](</tr/plugins/codex-harness>)

Metinden Konuşmaya İletim 2 yetenek

Deneysel0%

Alfa61%

Alfa68%

[TTS](</tr/tools/tts>), [Medya Genel Bakışı](</tr/tools/media-overview>), [Discord](</tr/channels/discord>)

Medya Anlama 12 yetenek

Deneysel7%

Alfa69%

Alfa69%

[Ses](</tr/nodes/audio>), [Medya Anlama](</tr/nodes/media-understanding>), [Medya Genel Bakışı](</tr/tools/media-overview>), [WhatsApp](</tr/channels/whatsapp>), [Görseller](</tr/nodes/images>), [Infer](</tr/cli/infer>), [PDF](</tr/tools/pdf>)

Medya Oluşturma 17 yetenek

Deneysel5%

Alfa69%

Alfa69%

[Görsel Oluşturma](</tr/tools/image-generation>), [Medya Genel Bakışı](</tr/tools/media-overview>), [Skills](</tr/tools/skills>), [Müzik Oluşturma](</tr/tools/music-generation>), [Video Oluşturma](</tr/tools/video-generation>)

Ses ve gerçek zamanlı konuşma - M2 Alfa - 6 alan

Control UI, uygulamalar ve sağlayıcılar genelinde birden fazla uygulama mevcut. Beta öncesinde gecikme, hata modu ve kurulum puan kartları gerekiyor.

Kapsam Deneysel - 0%Kalite Alfa - 61%Tamamlanmışlık Alfa - 68%Yok

Konuşma Sağlayıcıları 7 yetenek

Deneysel0%

Alpha61%

Alpha68%

[Openai](</tr/providers/openai>), [Google](</tr/providers/google>), [Sdk Sağlayıcı Plugin’leri](</tr/plugins/sdk-provider-plugins>), [Konuşma](</tr/nodes/talk>), [Kontrol UI](</tr/web/control-ui>)

Gerçek Zamanlı Konuşma Oturumları 11 yetenek

Deneysel0%

Alpha61%

Alpha68%

[Konuşma](</tr/nodes/talk>), [Kontrol UI](</tr/web/control-ui>)

Konuşma ve Transkripsiyon 5 yetenek

Deneysel0%

Alpha61%

Alpha68%

[Konuşma](</tr/nodes/talk>), [Openai](</tr/providers/openai>), [Google](</tr/providers/google>)

Yerel Uygulama Konuşması 4 yetenek

Deneysel0%

Alpha61%

Alpha68%

[Konuşma](</tr/nodes/talk>), [Voicewake](</tr/platforms/mac/voicewake>)

Sesle Uyandırma ve Yönlendirme 4 yetenek

Deneysel0%

Alpha61%

Alpha68%

[Voicewake](</tr/nodes/voicewake>), [Voicewake](</tr/platforms/mac/voicewake>), [Ses Katmanı](</tr/platforms/mac/voice-overlay>)

Konuşma Gözlemlenebilirliği 5 yetenek

Deneysel0%

Alpha61%

Alpha68%

[Kontrol UI](</tr/web/control-ui>), [Ses Katmanı](</tr/platforms/mac/voice-overlay>), [Konuşma](</tr/nodes/talk>)

TUI - M2 Alpha - 5 alan

Dokümanlarda ve kaynakta mevcut, ancak birincil kullanıcı iş akışı olarak daha az görünür. Açık senaryo tanımı gerektirir.

Kapsam Deneysel - 0%Kalite Alpha - 59%Tamlık Alpha - 66%Yok

Çalışma Zamanı Modları 14 yetenek

Deneysel0%

Alpha59%

Alpha66%

[TUI](</tr/cli/tui>), [TUI](</tr/web/tui>), [Dizin](</tr/cli>)

Girdi ve Komutlar 8 yetenek

Deneysel0%

Alpha59%

Alpha66%

[TUI](</tr/web/tui>)

Oturum Yönetimi 3 yetenek

Deneysel0%

Alpha59%

Alpha66%

[TUI](</tr/web/tui>), [Oturumlar](</tr/cli/sessions>)

Yerel Kabuk Yürütme 4 yetenek

Deneysel0%

Alpha59%

Alpha66%

[TUI](</tr/web/tui>), [TUI](</tr/cli/tui>)

İşleme ve Çıktı Güvenliği 4 yetenek

Deneysel0%

Alpha59%

Alpha66%

[TUI](</tr/web/tui>), [QR](</tr/cli/qr>), [Günlükler](</tr/cli/logs>), [Tamamlama](</tr/cli/completion>)

ClawHub - M2 Alpha - 4 alan

Genel belgeler ve ekosistem kavramı mevcut. Kurulum, güven, güncelleme, geri alma ve uyumluluk puan kartlarına ihtiyaç var.

Kapsam Deneysel - 0%Kalite Alpha - 58%Tamamlanmışlık Alpha - 62%Yok

Yayınlama 7 yetenek

Deneysel0%

Alfa54%

Alfa55%

[Yayınlama](</tr/clawhub/publishing>), [Skills Oluşturma](</tr/tools/creating-skills>), [Topluluk](</tr/plugins/community>)

Katalog Keşfi 5 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Plugin](</tr/tools/plugin>), [Pluginler](</tr/cli/plugins>), [Skills](</tr/cli/skills>), [Skills](</tr/tools/skills>), [Topluluk](</tr/plugins/community>)

Uyumluluk ve Güven 12 yetenek

Deneysel0%

Alfa55%

Alfa56%

[Plugin](</tr/tools/plugin>), [Pluginler](</tr/cli/plugins>), [Uyumluluk](</tr/plugins/compatibility>), [Plugin Envanteri](</tr/plugins/plugin-inventory>), [Yayınlama](</tr/clawhub/publishing>), [Skills](</tr/tools/skills>), [Skills Yapılandırması](</tr/tools/skills-config>)

Plugin Yaşam Döngüsü ve Sağlığı 26 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Plugin](</tr/tools/plugin>), [Pluginler](</tr/cli/plugins>), [Skills](</tr/cli/skills>), [Skills](</tr/tools/skills>), [Protokol](</tr/gateway/protocol>), [Paketler](</tr/plugins/bundles>), [Bağımlılık Çözümleme](</tr/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 areas

OpenClaw App SDK, Gateway çalışma zamanı ve Plugin SDK'dan ayrı, farklı bir harici uygulama sözleşmesidir. Mevcut puanlama; herkese açık paketleme, otomatik keşif, onaylar, yardımcılar ve uyumluluk alanlarında boşlukları olan gerçek bir `@openclaw/sdk` yolu gösteriyor.

Kapsam Deneysel - 3%Kalite Alfa - 54%Tamamlanma Alfa - 53%Yok

İstemci API'si 4 yetenek

Deneysel0%

Alpha51%

Alpha50%

[OpenClaw SDK](</tr/gateway/external-apps>), [OpenClaw SDK API Tasarımı](</tr/gateway/external-apps>)

Gateway Erişimi 5 yetenek

Deneysel0%

Alpha53%

Alpha54%

[OpenClaw SDK](</tr/gateway/external-apps>), [OpenClaw SDK API Tasarımı](</tr/gateway/external-apps>), [Protokol](</tr/gateway/protocol>), [Dizin](</tr/gateway/security>)

Ajan Konuşmaları 6 yetenek

Deneysel0%

Alpha52%

Alpha52%

[OpenClaw SDK](</tr/gateway/external-apps>), [OpenClaw SDK API Tasarımı](</tr/gateway/external-apps>), [Protokol](</tr/gateway/protocol>)

Olaylar ve Onaylar 5 yetenek

Deneysel0%

Alpha52%

Alpha52%

[OpenClaw SDK](</tr/gateway/external-apps>), [OpenClaw SDK API Tasarımı](</tr/gateway/external-apps>), [Protokol](</tr/gateway/protocol>)

Kaynak Yardımcıları 5 yetenek

Deneysel17%

Alpha62%

Alpha53%

[OpenClaw SDK](</tr/gateway/external-apps>), [OpenClaw SDK API Tasarımı](</tr/gateway/external-apps>)

Uyumluluk 5 yetenek

Deneysel0%

Alpha54%

Alpha55%

[OpenClaw SDK API Tasarımı](</tr/gateway/external-apps>), [Typebox](</tr/concepts/typebox>), [Protokol](</tr/gateway/protocol>)

### Platform

Linux Gateway ana makinesi - M4 Kararlı - 5 alan

Node çalışma zamanı önerilir, systemd kullanıcı hizmeti belgelenmiştir ve VPS/konteyner rehberliği kapsamlıdır.

Kapsam Deneysel - 0%Kalite Beta - 75%Tamamlanma Kararlı - 89%Kısmi - 4

Ana Makine Kurulumu ve Güncellemeler 4 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Dizin](</tr/install>), [Güncelleme](</tr/install/updating>), [Linux](</tr/platforms/linux>), [Dizin](</tr/platforms>)

Gateway Çalışma Zamanı ve Hizmet Denetimi 6 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Dizin](</tr/gateway>), [Gateway](</tr/cli/gateway>), [Linux](</tr/platforms/linux>), [Vps](</tr/vps>)

Uzaktan Erişim ve Güvenlik 6 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Uzaktan](</tr/gateway/remote>), [Tailscale](</tr/gateway/tailscale>), [Maruz Kalma Runbook'u](</tr/gateway/security/exposure-runbook>), [Kimlik Doğrulama](</tr/gateway/authentication>), [Gizli Bilgiler](</tr/gateway/secrets>)

Tanılama ve Onarım 4 yetenek / LTS destekli

Deneysel0%

Beta75%

Kararlı89%

[Durum](</tr/cli/status>), [Günlükler](</tr/cli/logs>), [Doctor](</tr/cli/doctor>), [Tanılama](</tr/gateway/diagnostics>), [Dizin](</tr/gateway>)

Dağıtım Hedefleri 3 yetenek

Deneysel0%

Beta75%

Kararlı89%

[Vps](</tr/vps>), [Docker](</tr/install/docker>), [Hetzner](</tr/install/hetzner>), [Digitalocean](</tr/install/digitalocean>), [Kubernetes](</tr/install/kubernetes>), [Podman](</tr/install/podman>)

macOS Gateway ana makinesi - M4 Kararlı - 7 alan

LaunchAgent hizmet yolu, yerel/uzak Gateway modları, CLI kurulumu ve uygulama entegrasyonu belgelenmiştir.

Kapsam Deneysel - 0%Kalite Beta - 74%Tamamlanmışlık Kararlı - 88%Yok

CLI Kurulumu 4 yetenek

Deneysel0%

Beta74%

Kararlı88%

[Macos](</tr/platforms/macos>), [Paketlenmiş Gateway](</tr/platforms/mac/bundled-gateway>), [Yükleyici](</tr/install/installer>), [Node](</tr/install/node>)

Yerel Gateway Entegrasyonu 9 yetenek

Deneysel0%

Beta74%

Kararlı88%

[Macos](</tr/platforms/macos>), [Paketlenmiş Gateway](</tr/platforms/mac/bundled-gateway>), [Uzak](</tr/platforms/mac/remote>), [Dizin](</tr/gateway>), [Gateway](</tr/cli/gateway>), [Bonjour](</tr/gateway/bonjour>)

Uzak Gateway Modu 5 yetenek

Deneysel0%

Beta74%

Kararlı88%

[Uzak](</tr/platforms/mac/remote>), [Uzak](</tr/gateway/remote>), [Tailscale](</tr/gateway/tailscale>)

Gateway Hizmeti Yaşam Döngüsü 10 yetenek

Deneysel0%

Beta74%

Kararlı88%

[Macos](</tr/platforms/macos>), [Paketlenmiş Gateway](</tr/platforms/mac/bundled-gateway>), [Gateway](</tr/cli/gateway>), [Dizin](</tr/gateway>), [Güncelleme](</tr/cli/update>), [Güncelleme](</tr/install/updating>), [Kaldırma](</tr/install/uninstall>), [Sorun Giderme](</tr/gateway/troubleshooting>)

Tanılama ve Gözlemlenebilirlik 4 yetenek

Deneysel0%

Beta74%

Kararlı88%

[Paketlenmiş Gateway](</tr/platforms/mac/bundled-gateway>), [Macos](</tr/platforms/macos>), [Gateway](</tr/cli/gateway>), [Doctor](</tr/gateway/doctor>), [Sorun Giderme](</tr/gateway/troubleshooting>)

İzinler ve Yerel Yetenekler 4 yetenek

Deneysel0%

Beta74%

Kararlı88%

[Macos](</tr/platforms/macos>), [Uzak](</tr/platforms/mac/remote>)

Profiller ve Yalıtım 5 yetenek

Deneysel0%

Beta74%

Kararlı88%

[Birden Çok Gateway](</tr/gateway/multiple-gateways>), [Dizin](</tr/gateway>), [Gateway](</tr/cli/gateway>)

Docker ve Podman barındırma - M3 Beta - 4 alan

Kurulum belgeleri mevcut ve yaygın dağıtım yollarıdır. Yinelenen sürüm smoke testleri yükseltme ve birim davranışını kaydettikten sonra yükseltin.

Kapsam Deneysel - 7%Kalite Beta - 71%Tamlık Beta - 79%Yok

Konteyner Kurulumu 6 yetenek

Deneysel0%

Alfa68%

Beta79%

[Docker](</tr/install/docker>), [Podman](</tr/install/podman>)

Konteyner İşlemleri 11 yetenek

Deneysel0%

Alfa68%

Beta79%

[Podman](</tr/install/podman>), [Docker Vm Runtime](</tr/install/docker-vm-runtime>), [Docker](</tr/install/docker>), [Hetzner](</tr/install/hetzner>), [Hostinger](</tr/install/hostinger>)

İmaj Yayını ve Doğrulama 5 yetenek

Deneysel29%

Beta79%

Beta79%

[Docker](</tr/install/docker>), [Docker Vm Runtime](</tr/install/docker-vm-runtime>), [Tam Sürüm Doğrulaması](</tr/reference/full-release-validation>)

Ajan Sandbox'ı ve Araçları 3 yetenek

Deneysel0%

Alfa68%

Beta79%

[Docker](</tr/install/docker>), [Docker Vm Runtime](</tr/install/docker-vm-runtime>)

WSL2 üzerinden Windows - M3 Beta - 6 alan

systemd/kullanıcı hizmeti rehberliği ve önyükleme zinciri belgeleriyle önerilen Windows yolu. Yinelenen kurulum/güncelleme puan kartlarından sonra yükseltin.

Kapsam Deneysel - 6%Kalite Alfa - 69%Tamlık Beta - 79%Kısmi - 5

WSL Kurulumu 6 yetenek / LTS destekli

Deneysel0%

Alfa67%

Beta79%

[Windows](</tr/platforms/windows>), [Başlarken](</tr/start/getting-started>)

CLI 8 yetenek / LTS destekli

Deneysel0%

Alfa67%

Beta79%

[Windows](</tr/platforms/windows>), [Başlarken](</tr/start/getting-started>), [Güncelleme](</tr/install/updating>), [Onboard](</tr/cli/onboard>), [Doctor](</tr/cli/doctor>), [Durum](</tr/cli/status>), [Günlükler](</tr/cli/logs>)

Gateway Hizmet Yaşam Döngüsü 10 yetenek / LTS destekli

Deneysel0%

Alfa67%

Beta79%

[Windows](</tr/platforms/windows>), [Dizin](</tr/gateway>), [Doctor](</tr/gateway/doctor>)

Gateway Erişimi ve Dışa Açılması 11 yetenek / LTS destekli

Deneysel0%

Alfa67%

Beta79%

[Kimlik Doğrulama](</tr/gateway/authentication>), [Gizli Bilgiler](</tr/gateway/secrets>), [Uzaktan](</tr/gateway/remote>), [Dışa Açma Runbook'u](</tr/gateway/security/exposure-runbook>), [Windows](</tr/platforms/windows>)

Tanılama ve Onarım 6 yetenek / LTS destekli

Deneysel38%

Beta79%

Beta79%

[Windows](</tr/platforms/windows>), [Durum](</tr/cli/status>), [Günlükler](</tr/cli/logs>), [Doctor](</tr/cli/doctor>), [Doctor](</tr/gateway/doctor>)

Tarayıcı ve Denetim UI 6 yetenek

Deneysel0%

Alfa67%

Beta79%

[Tarayıcı Wsl2 Windows Uzak Cdp Sorun Giderme](</tr/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Tarayıcı](</tr/tools/browser>), [Denetim UI](</tr/web/control-ui>)

Raspberry Pi ve küçük Linux cihazlar - M3 Beta - 4 alan

Platform belgeleri mevcut ve Gateway yolu Linux tabanlıdır. Daha yükseğe çıkmak için donanıma özgü sürüm smoke kanıtı gerekir.

Kapsam Deneysel - 0%Kalite Alfa - 67%Tamlık Beta - 79%Yok

Kurulum ve Uyumluluk 12 yetenek

Deneysel0%

Alpha67%

Beta79%

[Raspberry Pi](</tr/install/raspberry-pi>), [Dizin](</tr/install>), [İlk Çalıştırma SSS](</tr/help/faq-first-run>), [SSS](</tr/help/faq>), [Linux](</tr/platforms/linux>), [Yükleyici](</tr/install/installer>)

Uzaktan Erişim ve Kimlik Doğrulama 9 yetenek

Deneysel0%

Alpha67%

Beta79%

[Raspberry Pi](</tr/install/raspberry-pi>), [Kimlik Doğrulama](</tr/gateway/authentication>), [Gizli Bilgiler](</tr/gateway/secrets>), [Eşleştirme](</tr/gateway/pairing>), [Cihazlar](</tr/cli/devices>), [Uzak](</tr/gateway/remote>), [Tailscale](</tr/gateway/tailscale>)

Gateway Çalışma Zamanı 10 yetenek

Deneysel0%

Alpha67%

Beta79%

[Dizin](</tr/gateway>), [Gateway](</tr/cli/gateway>), [Raspberry Pi](</tr/install/raspberry-pi>), [Linux](</tr/platforms/linux>), [Vps](</tr/vps>)

Performans ve Tanılama 5 yetenek

Deneysel0%

Alpha67%

Beta79%

[Raspberry Pi](</tr/install/raspberry-pi>), [Linux](</tr/platforms/linux>), [Sağlık](</tr/gateway/health>), [Tanılama](</tr/gateway/diagnostics>)

macOS companion app - M3 Beta - 8 alan

Zengin menü çubuğu uygulaması, izinler, node modu, Canvas, sesle uyandırma, WebChat ve uzak mod mevcut. Stable seviyesinden kaçınacak kadar hâlâ hızlı değişiyor.

Kapsam Deneysel - 0%Kalite Alpha - 66%Tamlık Beta - 78%Yok

Tuval 4 yetenek

Deneysel0%

Alfa66%

Beta78%

[Tuval](</tr/platforms/mac/canvas>), [Macos](</tr/platforms/macos>), [Webchat](</tr/web/webchat>)

Yerel Kurulum 7 yetenek

Deneysel0%

Alfa66%

Beta78%

[Paketlenmiş Gateway](</tr/platforms/mac/bundled-gateway>), [Macos](</tr/platforms/macos>), [Alt Süreç](</tr/platforms/mac/child-process>), [Geliştirme Kurulumu](</tr/platforms/mac/dev-setup>)

Durum ve Ayarlar 5 yetenek

Deneysel0%

Alfa66%

Beta78%

[Menü Çubuğu](</tr/platforms/mac/menu-bar>), [Simge](</tr/platforms/mac/icon>), [Macos](</tr/platforms/macos>), [Sağlık](</tr/platforms/mac/health>), [Günlükleme](</tr/platforms/mac/logging>), [Uzak](</tr/platforms/mac/remote>)

Yerel Yetenekler 5 yetenek

Deneysel0%

Alfa66%

Beta78%

[Macos](</tr/platforms/macos>), [Xpc](</tr/platforms/mac/xpc>), [İzinler](</tr/platforms/mac/permissions>), [İmzalama](</tr/platforms/mac/signing>), [Peekaboo](</tr/platforms/mac/peekaboo>)

Uzak Bağlantılar 3 yetenek

Deneysel0%

Alfa66%

Beta78%

[Uzak](</tr/platforms/mac/remote>), [Macos](</tr/platforms/macos>), [Uzak](</tr/gateway/remote>)

Ses ve Konuşma 3 yetenek

Deneysel0%

Alfa66%

Beta78%

[Voicewake](</tr/platforms/mac/voicewake>), [Ses Katmanı](</tr/platforms/mac/voice-overlay>), [Konuşma](</tr/nodes/talk>), [Macos](</tr/platforms/macos>)

WebChat 3 yetenek

Deneysel0%

Alfa66%

Beta78%

[Webchat](</tr/platforms/mac/webchat>), [Macos](</tr/platforms/macos>), [Webchat](</tr/web/webchat>)

Uzak WebChat 5 yetenek

Deneysel0%

Alfa66%

Beta78%

[Webchat](</tr/platforms/mac/webchat>), [Uzak](</tr/gateway/remote>), [Uzak](</tr/platforms/mac/remote>)

Android uygulaması - M2 Alfa - 7 alan

Herkese açık Google Play yolu mevcut, ancak uygulama belgeleri yeniden derlemeyi hâlâ son derece alfa olarak tanımlıyor ve sürüm sağlamlaştırma çalışmasına dikkat çekiyor.

Kapsam Deneysel - 0%Kalite Alfa - 59%Tamamlanma Alfa - 66%Yok

Medya Yakalama 1 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Android](</tr/platforms/android>), [Kamera](</tr/nodes/camera>)

Mobil Sohbet 1 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Android](</tr/platforms/android>)

Bağlantı Kurulumu 1 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Android](</tr/platforms/android>), [Bonjour](</tr/gateway/bonjour>), [Eşleştirme](</tr/gateway/pairing>)

Dağıtım 3 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Android](</tr/platforms/android>)

Ayarlar 1 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Android](</tr/platforms/android>)

Ses 1 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Android](</tr/platforms/android>), [Konuşma](</tr/nodes/talk>)

Cihaz Çalışma Zamanı 2 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Android](</tr/platforms/android>), [Sorun Giderme](</tr/nodes/troubleshooting>), [Protokol](</tr/gateway/protocol>)

Yerel Windows - M2 Alpha - 4 alan

Temel CLI/Gateway akışları çalışır, ancak belgeler tam deneyim için hâlâ WSL2 önerir ve yerel kullanıma özgü uyarıları listeler.

Kapsam Deneysel - 0%Kalite Alpha - 58%Tamamlanma Alpha - 66%Kısmi - 1

CLI 9 yetenek / LTS destekli

Deneysel0%

Alfa54%

Alfa64%

[Dizin](</tr/install>), [Yükleyici](</tr/install/installer>), [Windows](</tr/platforms/windows>), [Başlarken](</tr/start/getting-started>), [Onboard](</tr/cli/onboard>)

Gateway Yönetimi 11 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Windows](</tr/platforms/windows>), [Dizin](</tr/gateway>), [Gateway](</tr/cli/gateway>), [Doctor](</tr/cli/doctor>)

Ağ 4 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Windows](</tr/platforms/windows>), [Dizin](</tr/gateway>), [Gateway](</tr/cli/gateway>)

Güncellemeler 4 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Güncelleme](</tr/install/updating>), [Ci](</tr/ci>)

Kubernetes barındırma - M2 Alfa - 4 alan

Kubernetes barındırma, Kustomize tabanlı ayrı bir küme dağıtım yoludur. Mevcut puanlama, Kubernetes'e özgü CI, ingress/TLS/NetworkPolicy paketleme, yedekleme/geri yükleme ve üretim ortamına açma sağlamlaştırması konularındaki eksiklerle birlikte gerçek bir asgari dağıtım yolu olduğunu gösteriyor.

Kapsam Deneysel - 0%Kalite Alfa - 55%Eksiksizlik Alfa - 61%Yok

Dağıtım Kurulumu 5 yetenek

Deneysel0%

Alfa55%

Alfa61%

[Kubernetes](</tr/install/kubernetes>), [Dizin](</tr/install>)

Yapılandırma ve Gizli Bilgiler 5 yetenek

Deneysel0%

Alfa55%

Alfa61%

[Kubernetes](</tr/install/kubernetes>), [Gizli Bilgiler](</tr/gateway/secrets>), [Ortam](</tr/help/environment>)

Erişim ve Açığa Çıkarma 5 yetenek

Deneysel0%

Alfa55%

Alfa61%

[Kubernetes](</tr/install/kubernetes>), [Kimlik Doğrulama](</tr/gateway/authentication>), [Uzak](</tr/gateway/remote>), [Açığa Çıkarma Çalıştırma Rehberi](</tr/gateway/security/exposure-runbook>)

Küme Yaşam Döngüsü 5 yetenek

Deneysel0%

Alfa55%

Alfa61%

[Kubernetes](</tr/install/kubernetes>), [Dizin](</tr/gateway>)

iOS uygulaması - M1 Deneysel - 8 alan

Dahili önizleme / süper-alfa. TestFlight ve aktarıcı destekli anlık bildirim akışları mevcut, ancak henüz herkese açık dağıtım yok.

Kapsam Deneysel - 0%Kalite Deneysel - 41%Tamamlanmışlık Deneysel - 44%Yok

Medya ve Paylaşım 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>), [Kamera](</tr/nodes/camera>)

Canvas ve Ekran 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>), [Canvas](</tr/plugins/reference/canvas>)

Sohbet ve Oturumlar 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>), [Webchat](</tr/web/webchat>), [Protokol](</tr/gateway/protocol>)

Gateway Kurulumu ve Tanılama 7 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>), [Eşleştirme](</tr/channels/pairing>)

Dağıtım 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>)

Cihaz Komutları 2 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>), [Protokol](</tr/gateway/protocol>)

Bildirimler ve Arka Plan 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>), [Yapılandırma](</tr/gateway/configuration>)

Ses 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>), [Konuşma](</tr/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

İsteğe bağlı kurulum akışı. Alfa/beta aşamasına yükseltmeden önce daha net bir destek taahhüdü gerekiyor.

Kapsam Deneysel - %0Kalite Deneysel - %41Tamamlanmışlık Deneysel - %44Yok

Kurulum Devri 4 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Nix](</tr/install/nix>), [Dizin](</tr/install>), [Dokümanlar Dizini](</tr/start/docs-directory>)

Plugin Yaşam Döngüsü 4 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Plugin'leri Yönet](</tr/plugins/manage-plugins>), [Plugin](</tr/tools/plugin>), [Nix](</tr/install/nix>)

Etkinleştirme ve Uygulama UX'i 7 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Nix](</tr/install/nix>)

Yapılandırma ve Durum 7 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Nix](</tr/install/nix>), [Kurulum](</tr/cli/setup>), [Ortam](</tr/help/environment>)

Hizmet Çalışma Zamanı ve Korumalar 8 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Nix](</tr/install/nix>), [Kurulum](</tr/cli/setup>), [Tanı](</tr/cli/doctor>), [Güncelleme](</tr/cli/update>)

watchOS eşlikçi yüzeyleri - M1 Deneysel - 5 alan

Kaynakta Watch uygulaması/uzantısı yüzeyleri bulunur; genel dokümanlar bunu henüz bir kullanıcı özelliği olarak sunmaz.

Kapsam Deneysel - 0%Kalite Deneysel - 41%Tamlık Deneysel - 44%Yok

Teslim ve Kurtarma 7 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>)

Exec Onayları 3 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Exec Onayları](</tr/tools/exec-approvals>), [Ios](</tr/platforms/ios>)

Dağıtım ve Destek 6 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>)

Bildirimler ve Yanıtlar 7 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>)

Watch Uygulaması Kullanıcı Arayüzü 3 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Ios](</tr/platforms/ios>)

Linux companion uygulaması - M0 Planlandı - 5 alan

Dokümanlar, yerel Linux companion uygulamalarının planlandığını söylüyor; Gateway bugün desteklenen Linux yoludur.

Kapsam Deneysel - 0%Kalite Deneysel - 19%Tamlık Deneysel - 21%Yok

Uygulama Dağıtımı 3 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Linux](</tr/platforms/linux>), [Dizin](</tr/platforms>), [Dizin](</tr/install>)

Gateway Bağlantısı 4 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Linux](</tr/platforms/linux>), [Dizin](</tr/gateway>), [Eşleştirme](</tr/gateway/pairing>), [Uzak](</tr/gateway/remote>)

Sohbet ve Oturumlar 3 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Linux](</tr/platforms/linux>), [Protokol](</tr/gateway/protocol>), [Webchat](</tr/web/webchat>)

Masaüstü Yetenekleri 9 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Linux](</tr/platforms/linux>), [Exec Onayları](</tr/tools/exec-approvals>), [Gizli Bilgiler](</tr/gateway/secrets>), [Dizin](</tr/nodes>), [Exec](</tr/tools/exec>), [Konuşma](</tr/nodes/talk>), [Kamera](</tr/nodes/camera>)

Durum ve Tanılama 7 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Linux](</tr/platforms/linux>), [Openclaw](</tr/start/openclaw>), [Doctor](</tr/gateway/doctor>)

Yerel Windows yardımcı uygulaması - M0 Planlandı - 5 alan

Yalnızca planlandı.

Kapsam Deneysel - 0%Kalite Deneysel - 19%Tamlık Deneysel - 21%Yok

Kurulum ve Güncellemeler 4 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Windows](</tr/platforms/windows>), [Dizin](</tr/install>)

Gateway Bağlantısı 3 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Windows](</tr/platforms/windows>), [Dizin](</tr/gateway>), [Eşleştirme](</tr/gateway/pairing>), [Uzak](</tr/gateway/remote>)

Sohbet Oturumları 2 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Windows](</tr/platforms/windows>), [Protokol](</tr/gateway/protocol>)

Durum ve Onarım 5 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Windows](</tr/platforms/windows>), [Doctor](</tr/gateway/doctor>), [Dizin](</tr/gateway>)

Masaüstü Araçları ve İzinler 10 yetenek

Deneysel0%

Deneysel19%

Deneysel21%

[Windows](</tr/platforms/windows>), [Dizin](</tr/nodes>), [Exec](</tr/tools/exec>), [Exec Onayları](</tr/tools/exec-approvals>), [Dizin](</tr/gateway/security>)

### Kanal

Discord - M4 Kararlı - 6 alan

Derin dokümanlar ve geniş özellik kapsamı. Ses/delegasyon yolları ayrı olarak beta/alfa şeklinde puanlanmaya devam etmelidir.

Kapsam Deneysel - 0%Kalite Beta - 73%Tamlık Kararlı - 87%Kısmi - 4

Kanal Kurulumu ve Operasyonlar 10 yetenek / LTS destekli

Deneysel0%

Beta73%

Kararlı87%

[Discord](</tr/channels/discord>), [Discord](</tr/plugins/reference/discord>), [Fly](</tr/install/fly>), [Eğik Çizgi Komutları](</tr/tools/slash-commands>), [Sağlık](</tr/gateway/health>), [Kanallar](</tr/cli/channels>), [Yapılandırma Kanalları](</tr/gateway/config-channels>)

Erişim ve Kimlik 6 yetenek / LTS destekli

Deneysel0%

Beta73%

Kararlı87%

[Discord](</tr/channels/discord>), [Eşleştirme](</tr/channels/pairing>), [Erişim Grupları](</tr/channels/access-groups>), [Gruplar](</tr/channels/groups>)

Konuşma Yönlendirme ve Teslim 12 yetenek / LTS destekli

Deneysel0%

Beta73%

Kararlı87%

[Discord](</tr/channels/discord>), [Kanal Yönlendirme](</tr/channels/channel-routing>), [Gruplar](</tr/channels/groups>), [Erişim Grupları](</tr/channels/access-groups>), [ACP Aracıları](</tr/tools/acp-agents>), [Alt aracılar](</tr/tools/subagents>)

Medya ve Zengin İçerik 1 yetenek / LTS destekli

Deneysel0%

Beta73%

Kararlı87%

[Discord](</tr/channels/discord>)

Yerel Kontroller ve Onaylar 5 yetenek

Deneysel0%

Beta73%

Kararlı87%

[Discord](</tr/channels/discord>), [Eğik Çizgi Komutları](</tr/tools/slash-commands>)

Gerçek Zamanlı Ses ve Aramalar 5 yetenek

Deneysel0%

Beta73%

Kararlı87%

[Discord](</tr/channels/discord>), [Openai](</tr/providers/openai>), [Elevenlabs](</tr/providers/elevenlabs>), [QA E2E Otomasyonu](</tr/concepts/qa-e2e-automation>), [Yapılandırma Kanalları](</tr/gateway/config-channels>)

Telegram - M3 Beta - 5 alan

Çekirdek kanal düzenli kullanım için yeterince olgun, ancak yüksek değişkenlik gösteren UX ve medya uç durumları yinelenen senaryo kanıtı gerektirir.

Kapsam Deneysel - 0%Kalite Alfa - 68%Tamlık Beta - 78%Tam - 5

Kanal Kurulumu ve İşlemleri 10 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Telegram](</tr/channels/telegram>), [Yapılandırma Kanalları](</tr/gateway/config-channels>), [Kanallar](</tr/cli/channels>)

Erişim ve Kimlik 10 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Telegram](</tr/channels/telegram>), [Eşleştirme](</tr/channels/pairing>), [Erişim Grupları](</tr/channels/access-groups>), [Gruplar](</tr/channels/groups>), [Çoklu Ajan](</tr/concepts/multi-agent>)

Konuşma Yönlendirme ve Teslim 1 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Telegram](</tr/channels/telegram>), [Gruplar](</tr/channels/groups>), [Çoklu Ajan](</tr/concepts/multi-agent>)

Medya ve Zengin İçerik 1 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Telegram](</tr/channels/telegram>), [Konum](</tr/channels/location>)

Yerel Kontroller ve Onaylar 9 yetenek / LTS destekli

Deneysel0%

Beta77%

Beta79%

[Telegram](</tr/channels/telegram>), [Exec Onayları](</tr/tools/exec-approvals>), [Tepkiler](</tr/tools/reactions>)

Slack - M3 Beta - 5 alan

Birinci sınıf kanal dokümanları ve yönlendirme yüzeyi. Çalışma alanı kurulum/yönetici senaryosu puan kartları gerekiyor.

Kapsam Deneysel - 0%Kalite Alfa - 66%Tamlık Beta - 78%Tam - 5

Kanal Kurulumu ve Operasyonları 10 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Slack](</tr/channels/slack>), [Slack](</tr/plugins/reference/slack>), [Gizli Bilgiler](</tr/gateway/secrets>), [QA E2E Otomasyonu](</tr/concepts/qa-e2e-automation>), [Sorun Giderme](</tr/channels/troubleshooting>)

Erişim ve Kimlik 1 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Slack](</tr/channels/slack>), [Eşleştirme](</tr/channels/pairing>)

Konuşma Yönlendirme ve Teslim 5 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Slack](</tr/channels/slack>), [Bot Döngüsü Koruması](</tr/channels/bot-loop-protection>), [Eşleştirme](</tr/channels/pairing>)

Medya ve Zengin İçerik 1 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Slack](</tr/channels/slack>), [QA E2E Otomasyonu](</tr/concepts/qa-e2e-automation>)

Yerel Denetimler ve Onaylar 8 yetenek / LTS destekli

Deneysel0%

Alfa66%

Beta78%

[Slack](</tr/channels/slack>), [Eğik Çizgi Komutları](</tr/tools/slash-commands>), [Çalıştırma Onayları](</tr/tools/exec-approvals>)

iMessage ve BlueBubbles - M3 Beta - 5 alan

Desteklenen iMessage, oturum açılmış bir macOS Messages ana makinesinde imsg üzerinden çalışır; eski BlueBubbles yapılandırmaları geçiş gerektirir. macOS izinlerini, SSH sarmalayıcısını, SIP/özel API'yi ve geçiş uyarılarını görünür tutun.

Kapsam Deneysel - 0%Kalite Alfa - 66%Tamlık Beta - 78%Yok

Kanal Kurulumu ve Operasyonları 11 yetenek

Deneysel0%

Alfa66%

Beta78%

[Bluebubbles iMessage](</tr/announcements/bluebubbles-imessage>), [Bluebubbles'tan iMessage](</tr/channels/imessage-from-bluebubbles>), [Kanalları Yapılandırma](</tr/gateway/config-channels>), [iMessage](</tr/channels/imessage>)

Erişim ve Kimlik 6 yetenek

Deneysel0%

Alfa66%

Beta78%

[iMessage](</tr/channels/imessage>), [Bluebubbles'tan iMessage](</tr/channels/imessage-from-bluebubbles>), [Kanalları Yapılandırma](</tr/gateway/config-channels>)

Konuşma Yönlendirme ve Teslimat 4 yetenek

Deneysel0%

Alfa66%

Beta78%

[iMessage](</tr/channels/imessage>)

Medya ve Zengin İçerik 7 yetenek

Deneysel0%

Alfa66%

Beta78%

[iMessage](</tr/channels/imessage>), [Bluebubbles'tan iMessage](</tr/channels/imessage-from-bluebubbles>), [Kanalları Yapılandırma](</tr/gateway/config-channels>)

Yerel Denetimler ve Onaylar 3 yetenek

Deneysel0%

Alfa66%

Beta78%

[iMessage](</tr/channels/imessage>)

WhatsApp - M3 Beta - 5 alan

Çekirdek yol önemlidir ve belgelenmiştir; upstream Baileys/oturum değişkenliği onu Stable seviyesinin altında tutar.

Kapsam Deneysel - 0%Kalite Alfa - 66%Tamamlanmışlık Beta - 78%Yok

Kanal Kurulumu ve Operasyonları 5 yetenek

Deneysel0%

Alfa66%

Beta78%

[WhatsApp](</tr/channels/whatsapp>), [Kanalları Yapılandırma](</tr/gateway/config-channels>), [WhatsApp](</tr/plugins/reference/whatsapp>), [QA E2E Otomasyonu](</tr/concepts/qa-e2e-automation>), [Doctor](</tr/gateway/doctor>)

Erişim ve Kimlik 7 yetenek

Deneysel0%

Alfa66%

Beta78%

[WhatsApp](</tr/channels/whatsapp>), [Kanalları Yapılandırma](</tr/gateway/config-channels>), [QA E2E Otomasyonu](</tr/concepts/qa-e2e-automation>), [Eşleştirme](</tr/channels/pairing>)

Konuşma Yönlendirme ve Teslim 4 yetenek

Deneysel0%

Alfa66%

Beta78%

[WhatsApp](</tr/channels/whatsapp>), [Grup Mesajları](</tr/channels/group-messages>)

Medya ve Zengin İçerik 2 yetenek

Deneysel0%

Alfa66%

Beta78%

[WhatsApp](</tr/channels/whatsapp>)

Yerel Kontroller ve Onaylar 2 yetenek

Deneysel0%

Alfa66%

Beta78%

[WhatsApp](</tr/channels/whatsapp>)

Matrix - M2 Alpha - 6 alan

Paketle gelen plugin üzerinden desteklenir. Köprü, kimlik doğrulama ve oda yaşam döngüsü puan kartları gerekir.

Kapsam Deneysel - %0Kalite Alpha - %60Tamlık Alpha - %67Yok

Kanal Kurulumu ve Operasyonları 5 yetenek

Deneysel0%

Alfa60%

Alfa67%

[Matrix](</tr/channels/matrix>), [Matrix Geçişi](</tr/channels/matrix-migration>)

Erişim ve Kimlik 7 yetenek

Deneysel0%

Alfa60%

Alfa67%

[Matrix](</tr/channels/matrix>), [Gruplar](</tr/channels/groups>), [Bot Döngüsü Koruması](</tr/channels/bot-loop-protection>)

Konuşma Yönlendirme ve Teslim 1 yetenek

Deneysel0%

Alfa60%

Alfa67%

[Matrix](</tr/channels/matrix>)

Medya ve Zengin İçerik 1 yetenek

Deneysel0%

Alfa60%

Alfa67%

[Matrix](</tr/channels/matrix>)

Yerel Denetimler ve Onaylar 6 yetenek

Deneysel0%

Alfa60%

Alfa67%

[Matrix](</tr/channels/matrix>)

Şifreleme ve Doğrulama 3 yetenek

Deneysel0%

Alfa60%

Alfa67%

[Matrix](</tr/channels/matrix>), [Matrix Geçişi](</tr/channels/matrix-migration>)

Google Chat - M2 Alfa - 5 alan

Belgelenmiş kanal, ancak kurumsal/yönetici kurulumu olgunluk riskini artırır.

Kapsam Deneysel - 0%Kalite Alfa - 59%Tamlık Alfa - 66%Yok

Kanal Kurulumu ve Operasyonları 16 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Google Chat](</tr/channels/googlechat>), [Google Chat](</tr/plugins/reference/googlechat>), [Yapılandırma Kanalları](</tr/gateway/config-channels>), [Sihirbaz CLI Başvurusu](</tr/start/wizard-cli-reference>), [Gizli Değerler](</tr/gateway/secrets>), [Secretref Kimlik Bilgisi Yüzeyi](</tr/reference/secretref-credential-surface>), [Sağlık](</tr/gateway/health>), [Plugin Envanteri](</tr/plugins/plugin-inventory>), [Dizin](</tr/channels>)

Erişim ve Kimlik 11 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Google Chat](</tr/channels/googlechat>), [Eşleştirme](</tr/channels/pairing>), [Erişim Grupları](</tr/channels/access-groups>), [Yapılandırma Kanalları](</tr/gateway/config-channels>), [Bot Döngüsü Koruması](</tr/channels/bot-loop-protection>), [Kanal Yönlendirme](</tr/channels/channel-routing>)

Konuşma Yönlendirme ve Teslim 1 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Google Chat](</tr/channels/googlechat>), [Bot Döngüsü Koruması](</tr/channels/bot-loop-protection>), [Erişim Grupları](</tr/channels/access-groups>), [Kanal Yönlendirme](</tr/channels/channel-routing>)

Medya ve Zengin İçerik 1 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Google Chat](</tr/channels/googlechat>), [Mesaj](</tr/cli/message>), [Medya Anlama](</tr/nodes/media-understanding>), [Secretref Kimlik Bilgisi Yüzeyi](</tr/reference/secretref-credential-surface>)

Yerel Denetimler ve Onaylar 16 yetenek

Deneysel0%

Alpha59%

Alpha66%

[Google Chat](</tr/channels/googlechat>), [Mesaj](</tr/cli/message>), [Medya Anlama](</tr/nodes/media-understanding>), [Secretref Kimlik Bilgisi Yüzeyi](</tr/reference/secretref-credential-surface>), [Tepkiler](</tr/tools/reactions>), [Slash Komutları](</tr/tools/slash-commands>), [Yapılandırma Aracıları](</tr/gateway/config-agents>), [Mesaj Yaşam Döngüsü Refaktörü](</tr/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 alan

Kurumsal kimlik doğrulama/yönetici akışları açık senaryo kanıtı gerektirir.

Kapsam Deneysel - 0%Kalite Alpha - 59%Tamlık Alpha - 66%Yok

Kanal Kurulumu ve İşlemleri 9 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Msteams](</tr/channels/msteams>), [Msteams](</tr/plugins/reference/msteams>), [Yapılandırma Kanalları](</tr/gateway/config-channels>), [Sağlık](</tr/gateway/health>)

Erişim ve Kimlik 9 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Msteams](</tr/channels/msteams>), [Eşleştirme](</tr/channels/pairing>), [Erişim Grupları](</tr/channels/access-groups>)

Konuşma Yönlendirme ve Teslim 5 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Msteams](</tr/channels/msteams>), [Gruplar](</tr/channels/groups>), [Kanal Yönlendirme](</tr/channels/channel-routing>)

Medya ve Zengin İçerik 5 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Msteams](</tr/channels/msteams>)

Yerel Denetimler ve Onaylar 5 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Msteams](</tr/channels/msteams>), [Gelişmiş Exec Onayları](</tr/tools/exec-approvals-advanced>)

Signal - M2 Alfa - 5 alan

Desteklenen kanal dokümanları mevcut; daha güçlü kurulum ve yeniden bağlanma kanıtı gerekiyor.

Kapsam Deneysel - 0%Kalite Alfa - 59%Tamlık Alfa - 66%Yok

Kanal Kurulumu ve İşlemleri 7 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Signal](</tr/channels/signal>), [Signal](</tr/plugins/reference/signal>)

Erişim ve Kimlik 6 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Signal](</tr/channels/signal>)

Konuşma Yönlendirme ve Teslimi 1 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Signal](</tr/channels/signal>)

Medya ve Zengin İçerik 7 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Signal](</tr/channels/signal>)

Yerel Denetimler ve Onaylar 3 yetenek

Deneysel0%

Alfa59%

Alfa66%

[Signal](</tr/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, bölgesel kanallar - M2 Alfa - 4 alan

Önemli bölgesel kapsam, ancak genel destek düzeyi hesap türüne, üst kaynak onayına ve bakımcı kanıtına göre ayarlanmalıdır.

Kapsam Deneysel - 0%Kalite Alfa - 55%Tamlık Alfa - 58%Yok

Kanal Kurulumu ve Operasyonları 6 yetenek

Deneysel0%

Alpha61%

Alpha68%

[Dizin](</tr/channels>), [Eşleştirme](</tr/channels/pairing>), [Feishu](</tr/plugins/reference/feishu>), [Mimari İç Yapıları](</tr/plugins/architecture-internals>)

Erişim ve Kimlik 1 yetenek

Deneysel0%

Alpha53%

Alpha54%

Bağlantılı belge yok

Konuşma Yönlendirme ve Teslimi 1 yetenek

Deneysel0%

Alpha53%

Alpha54%

Bağlantılı belge yok

Medya ve Zengin İçerik 1 yetenek

Deneysel0%

Alpha53%

Alpha54%

Bağlantılı belge yok

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 alan

Desteklenen yüzeyler mevcut, ancak olgunluk muhtemelen upstream ve bakımcı kapsamına göre değişir. Daha sonra tek tek puanlayın.

Kapsam Deneysel - 0%Kalite Alpha - 53%Tamamlanmışlık Alpha - 54%Yok

Kanal Kurulumu ve Operasyonları 1 yetenek

Deneysel0%

Alpha53%

Alpha54%

Bağlantılı belge yok

Erişim ve Kimlik 1 yetenek

Deneysel0%

Alpha53%

Alpha54%

Bağlantılı belge yok

Konuşma Yönlendirme ve Teslimat 1 yetenek

Deneysel0%

Alpha53%

Alpha54%

Bağlantılı belge yok

Medya ve Zengin İçerik 1 yetenek

Deneysel0%

Alpha53%

Alpha54%

Bağlantılı belge yok

Sesli Arama kanalı - M1 Deneysel - 5 alan

Karmaşık gerçek zamanlı davranışa sahip isteğe bağlı/Plugin yolu. Herkese açık beta öncesinde senaryo puan kartı gerekiyor.

Kapsam Deneysel - 0%Kalite Deneysel - 41%Tamlık Deneysel - 44%Yok

Kanal Kurulumu ve Operasyonları 2 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Sesli Arama](</tr/cli/voicecall>), [Sesli Arama](</tr/plugins/voice-call>), [Protokol](</tr/gateway/protocol>)

Erişim ve Kimlik 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Sesli Arama](</tr/plugins/voice-call>), [Sesli Arama](</tr/cli/voicecall>)

Konuşma Yönlendirme ve Teslim 1 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Sesli Arama](</tr/plugins/voice-call>)

Medya ve Zengin İçerik 2 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Sesli Arama](</tr/plugins/voice-call>), [Plugin Envanteri](</tr/plugins/plugin-inventory>)

Gerçek Zamanlı Ses ve Aramalar 2 yetenek

Deneysel0%

Deneysel41%

Deneysel44%

[Sesli Arama](</tr/plugins/voice-call>)

### Sağlayıcı ve araç

Tarayıcı otomasyonu, exec ve sandbox araçları - M3 Beta - 3 alan

Temel araçlar belgelendirilmiştir, ancak ana makine güvenliği ve izin kullanıcı deneyimi etkin puan kartı incelemesi altında kalmalıdır.

Kapsam Deneysel - 21%Kalite Beta - 75%Tamamlanma Beta - 79%Kısmi - 2

Tarayıcı Otomasyonu 8 yetenek

Deneysel13%

Beta79%

Beta79%

[Tarayıcı Denetimi](</tr/tools/browser-control>), [Test](</tr/help/testing>), [Tarayıcı](</tr/tools/browser>), [Dizin](</tr/gateway/security>), [Denetim Kontrolleri](</tr/gateway/security/audit-checks>)

Araç Çağırma ve Yürütme 6 yetenek / LTS destekli

Alfa50%

Beta79%

Beta79%

[Yürütme](</tr/tools/exec>), [Arka Plan Süreci](</tr/gateway/background-process>), [Araç Çağırma HTTP API'si](</tr/gateway/tools-invoke-http-api>), [Operatör Kapsamları](</tr/gateway/operator-scopes>), [Protokol](</tr/gateway/protocol>), [Yürütme Onayları](</tr/tools/exec-approvals>), [Gelişmiş Yürütme Onayları](</tr/tools/exec-approvals-advanced>), [Yükseltilmiş](</tr/tools/elevated>)

Korumalı Alan ve Araç Politikası 6 yetenek / LTS destekli

Deneysel0%

Alfa68%

Beta79%

[Korumalı Alan Kullanımı](</tr/gateway/sandboxing>), [Korumalı Alan ile Araç Politikası ile Yükseltilmiş Karşılaştırması](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>), [Çok Aracılı Korumalı Alan Araçları](</tr/tools/multi-agent-sandbox-tools>), [Codex Çalıştırma Düzeneği Başvurusu](</tr/plugins/codex-harness-reference>), [Yapılandırma Araçları](</tr/gateway/config-tools>)

OpenAI ve Codex sağlayıcı yolu - M3 Beta - 5 alan

Derinlemesine belgeler, OAuth/abonelik yolu, gerçek zamanlı ses, görüntü ve uyumluluk davranışı. Sağlayıcı değişkenliği, yayın puan kartı kanıtı olmadan bunun Stable olmasını engeller.

Kapsam Deneysel - 26%Kalite Beta - 74%Tamlık Beta - 79%Kısmi - 3

Model ve Kimlik Doğrulama 6 yetenek / LTS destekli

Deneysel44%

Beta79%

Beta79%

[Openai](</tr/providers/openai>), [Codex Harness](</tr/plugins/codex-harness>), [Modeller](</tr/concepts/models>), [Oauth](</tr/concepts/oauth>), [Codex Harness Referansı](</tr/plugins/codex-harness-reference>), [Kimlik Doğrulama İzleme](</tr/gateway/authentication>)

Yanıtlar ve Araç Uyumluluğu 4 yetenek / LTS destekli

Deneysel40%

Beta79%

Beta79%

[Openai](</tr/providers/openai>), [Openresponses Http Api](</tr/gateway/openresponses-http-api>), [Openai Http Api](</tr/gateway/openai-http-api>), [Codex Yerel Plugin'leri](</tr/plugins/codex-native-plugins>)

Yerel Codex Harness 2 yetenek / LTS destekli

Deneysel44%

Beta79%

Beta79%

[Codex Harness](</tr/plugins/codex-harness>), [Codex Harness Çalışma Zamanı](</tr/plugins/codex-harness-runtime>), [Codex Harness Referansı](</tr/plugins/codex-harness-reference>), [Codex Yerel Plugin'leri](</tr/plugins/codex-native-plugins>)

Görüntü ve Çok Modlu Girdi 2 yetenek

Deneysel0%

Alfa67%

Beta79%

[Openai](</tr/providers/openai>), [Görüntü Oluşturma](</tr/tools/image-generation>), [Görüntüler](</tr/nodes/images>)

Ses ve Gerçek Zamanlı Ses 2 yetenek

Deneysel0%

Alfa67%

Beta79%

[Openai](</tr/providers/openai>), [Discord](</tr/channels/discord>), [Sesli Arama](</tr/plugins/voice-call>)

Web arama araçları - M3 Beta - 4 alan

Birden çok sağlayıcı ve belge mevcut. Sağlayıcı ailesi başına kota/hata/SSRF kanıtı gerekir.

Kapsam Deneysel - 9%Kalite Beta - 74%Tamlık Beta - 79%Yok

Arama Sağlayıcıları 19 yetenek

Deneysel11%

Beta79%

Beta79%

[Web](</tr/tools/web>), [Brave Search](</tr/tools/brave-search>), [Tavily](</tr/tools/tavily>), [Exa Search](</tr/tools/exa-search>), [Firecrawl](</tr/tools/firecrawl>), [Perplexity Search](</tr/tools/perplexity-search>), [Duckduckgo Search](</tr/tools/duckduckgo-search>), [Searxng Search](</tr/tools/searxng-search>), [Gemini Search](</tr/tools/gemini-search>), [Grok Search](</tr/tools/grok-search>), [Kimi Search](</tr/tools/kimi-search>), [Minimax Search](</tr/tools/minimax-search>), [Ollama Search](</tr/tools/ollama-search>), [SDK Alt Yolları](</tr/plugins/sdk-subpaths>), [SDK Genel Bakışı](</tr/plugins/sdk-overview>), [Manifest](</tr/plugins/manifest>)

Kurulum ve Tanılama 9 yetenek

Deneysel0%

Alfa68%

Beta79%

[Web](</tr/tools/web>), [Web Fetch](</tr/tools/web-fetch>), [SSS](</tr/help/faq>), [API Kullanım Maliyetleri](</tr/reference/api-usage-costs>), [Brave Search](</tr/tools/brave-search>), [Perplexity Search](</tr/tools/perplexity-search>), [Tavily](</tr/tools/tavily>), [Firecrawl](</tr/tools/firecrawl>)

Ağ Güvenliği 4 yetenek

Deneysel0%

Alfa68%

Beta79%

[Web](</tr/tools/web>), [Web Fetch](</tr/tools/web-fetch>), [Firecrawl](</tr/tools/firecrawl>), [Searxng Search](</tr/tools/searxng-search>)

Araç Kullanılabilirliği ve Getirme 11 yetenek

Deneysel25%

Beta79%

Beta79%

[Yapılandırma Araçları](</tr/gateway/config-tools>), [Web Fetch](</tr/tools/web-fetch>), [Web](</tr/tools/web>), [SSS](</tr/help/faq>)

Anthropic provider path - M3 Beta - 5 areas

Birinci sınıf model sağlayıcısı. Yinelenen kimlik doğrulama/katalog/araç çağrısı senaryo kanıtı gerekir.

Kapsam Deneysel - 0%Kalite Beta - 71%Tamlık Beta - 78%Yok

Sağlayıcı Kimlik Doğrulaması ve Kurtarma 9 yetenek

Deneysel0%

Alpha66%

Beta78%

[Anthropic](</tr/providers/anthropic>), [Doctor](</tr/gateway/doctor>), [Yapılandırma Örnekleri](</tr/gateway/configuration-examples>), [Sorun Giderme](</tr/gateway/troubleshooting>), [Prompt Önbelleğe Alma](</tr/reference/prompt-caching>)

Model ve Çalışma Zamanı Seçimi 10 yetenek

Deneysel0%

Beta78%

Beta79%

[Anthropic](</tr/providers/anthropic>), [Ajanları Yapılandırma](</tr/gateway/config-agents>), [Modeller](</tr/concepts/models>), [CLI Arka Uçları](</tr/gateway/cli-backends>)

İstek Taşıması ve Tur Semantiği 10 yetenek

Deneysel0%

Beta77%

Beta79%

[Anthropic](</tr/providers/anthropic>), [Prompt Önbelleğe Alma](</tr/reference/prompt-caching>), [Sorun Giderme](</tr/gateway/troubleshooting>), [CLI Arka Uçları](</tr/gateway/cli-backends>), [Model Sağlayıcıları](</tr/concepts/model-providers>)

Prompt Önbelleği ve Bağlam 5 yetenek

Deneysel0%

Alpha66%

Beta78%

[Anthropic](</tr/providers/anthropic>), [Prompt Önbelleğe Alma](</tr/reference/prompt-caching>), [Sorun Giderme](</tr/gateway/troubleshooting>), [Heartbeat](</tr/gateway/heartbeat>)

Medya Girdileri 4 yetenek

Deneysel0%

Alpha66%

Beta78%

[Anthropic](</tr/providers/anthropic>), [Ajanları Yapılandırma](</tr/gateway/config-agents>)

Google sağlayıcı yolu - M3 Beta - 5 alan

Model ve gerçek zamanlı yüzeylere sahip birinci sınıf sağlayıcı. Ayrı Live/Talk puanlaması gerektirir.

Kapsam Deneysel - 0%Kalite Alpha - 66%Tamlık Beta - 78%Yok

Sağlayıcı Kurulumu ve Kimlik Bilgileri 10 yetenek

Deneysel0%

Alfa66%

Beta78%

[Google](</tr/providers/google>), [Model Sağlayıcıları](</tr/concepts/model-providers>)

Model Yönlendirme ve Uç Noktalar 10 yetenek

Deneysel0%

Alfa66%

Beta78%

[Google](</tr/providers/google>), [Model Sağlayıcıları](</tr/concepts/model-providers>), [Google](</tr/plugins/reference/google>), [Gemini Search](</tr/tools/gemini-search>)

Doğrudan Gemini Çalışma Zamanı 9 yetenek

Deneysel0%

Alfa66%

Beta78%

[Google](</tr/providers/google>), [Model Sağlayıcıları](</tr/concepts/model-providers>), [Model SSS](</tr/help/faq-models>), [Canlı Test](</tr/help/testing-live>)

Medya, Arama ve Gerçek Zamanlı 10 yetenek

Deneysel0%

Alfa66%

Beta78%

[Google](</tr/plugins/reference/google>), [Google](</tr/providers/google>)

İstem Önbelleğe Alma 5 yetenek

Deneysel0%

Alfa66%

Beta78%

[İstem Önbelleğe Alma](</tr/reference/prompt-caching>), [Google](</tr/providers/google>), [Model Sağlayıcıları](</tr/concepts/model-providers>), [Token Kullanımı](</tr/reference/token-use>)

OpenRouter sağlayıcı yolu - M3 Beta - 4 alan

Birleşik sağlayıcı yolu belgelenmiştir ve değerlidir, ancak modele özgü davranış değişiklik gösterir.

Kapsam Deneysel - 0%Kalite Alfa - 66%Tamlık Beta - 78%Yok

Sağlayıcı Kurulumu ve Kimlik Doğrulama 14 yetenek

Deneysel0%

Alfa66%

Beta78%

[Openrouter](</tr/providers/openrouter>), [Model Sağlayıcıları](</tr/concepts/model-providers>), [Yapılandırma](</tr/cli/configure>), [Kimlik Doğrulama](</tr/gateway/authentication>), [Ortam](</tr/help/environment>), [Modeller](</tr/cli/models>), [Modeller](</tr/concepts/models>)

Sohbet Çalışma Zamanı ve Normalleştirme 15 yetenek

Deneysel0%

Alfa66%

Beta78%

[Openrouter](</tr/providers/openrouter>), [Model Sağlayıcıları](</tr/concepts/model-providers>), [İstem Önbelleğe Alma](</tr/reference/prompt-caching>)

Sağlayıcı Kurtarma ve Tanılama 5 yetenek

Deneysel0%

Alfa66%

Beta78%

[Model Yük Devretme](</tr/concepts/model-failover>), [Openrouter](</tr/providers/openrouter>), [Modeller](</tr/cli/models>)

Medya Üretimi ve Konuşma 7 yetenek

Deneysel0%

Alfa66%

Beta78%

[Openrouter](</tr/providers/openrouter>), [Görsel Üretimi](</tr/tools/image-generation>), [Müzik Üretimi](</tr/tools/music-generation>), [Medyaya Genel Bakış](</tr/tools/media-overview>), [Video Üretimi](</tr/tools/video-generation>), [Metinden Konuşmaya](</tr/tools/tts>)

Görsel, video ve müzik üretim araçları - M2 Alfa - 5 alan

Yetenek sağlayıcılar genelinde mevcuttur, ancak kalite, gecikme ve parametre uyumluluğu sağlayıcı başına kanıt olmadan beta için fazla değişkendir.

Kapsam Deneysel - 0%Kalite Alfa - 61%Tamamlanmışlık Alfa - 68%Yok

Medya Yönlendirme ve Keşif 4 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Yapılandırma Aracıları](</tr/gateway/config-agents>), [Görsel Oluşturma](</tr/tools/image-generation>), [Video Oluşturma](</tr/tools/video-generation>), [Müzik Oluşturma](</tr/tools/music-generation>)

Görev Yaşam Döngüsü ve Teslim 12 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Medya Genel Bakışı](</tr/tools/media-overview>), [Görsel Oluşturma](</tr/tools/image-generation>), [Video Oluşturma](</tr/tools/video-generation>), [Müzik Oluşturma](</tr/tools/music-generation>)

Görsel Oluşturma 9 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Görsel Oluşturma](</tr/tools/image-generation>), [Infer](</tr/cli/infer>), [Medya Genel Bakışı](</tr/tools/media-overview>)

Video Oluşturma 11 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Video Oluşturma](</tr/tools/video-generation>), [Runway](</tr/providers/runway>), [Pixverse](</tr/providers/pixverse>), [Fal](</tr/providers/fal>), [Openrouter](</tr/providers/openrouter>)

Müzik Oluşturma 6 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Müzik Oluşturma](</tr/tools/music-generation>)

Yerel model sağlayıcıları: Ollama, vLLM, SGLang, LM Studio - M2 Alfa - 5 alan

Kullanışlı ve belgelenmiş, ancak ortam değişkenliği yüksek.

Kapsam Deneysel - 0%Kalite Alfa - 61%Tamamlanmışlık Alfa - 68%Yok

Sağlayıcı Kurulumu, Yaşam Döngüsü ve Tanılama 12 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Yerel Modeller](</tr/gateway/local-models>), [Lmstudio](</tr/providers/lmstudio>), [Ollama](</tr/providers/ollama>), [Vllm](</tr/providers/vllm>), [Yerel Model Hizmetleri](</tr/gateway/local-model-services>), [Yapılandırma Aracıları](</tr/gateway/config-agents>), [Sorun Giderme](</tr/gateway/troubleshooting>), [Doctor](</tr/gateway/doctor>)

Yerel Sağlayıcı Pluginleri 10 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Ollama](</tr/providers/ollama>), [Lmstudio](</tr/providers/lmstudio>)

OpenAI Uyumlu Çalışma Zamanı Uyumluluğu 8 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Vllm](</tr/providers/vllm>), [Sglang](</tr/providers/sglang>), [Yerel Modeller](</tr/gateway/local-models>), [Lmstudio](</tr/providers/lmstudio>)

Yerel Bellek ve Gömme Vektörleri 5 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Bellek](</tr/concepts/memory>), [Doctor](</tr/gateway/doctor>)

Ağ Güvenliği ve Prompt Denetimleri 2 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Dizin](</tr/gateway/security>), [Yapılandırma Araçları](</tr/gateway/config-tools>), [Yerel Modeller](</tr/gateway/local-models>)

Uzun kuyruklu barındırılan sağlayıcılar - M2 Alfa - 3 alan

Birçok doküman/referans sayfası var; puan, sağlayıcı meta verilerinden ve canlı smoke kapsamından üretilmelidir.

Kapsam Deneysel - 0%Kalite Alfa - 61%Tamamlanmışlık Alfa - 68%Yok

Barındırılan LLM Sağlayıcıları 12 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Dizin](</tr/providers>), [Model Sağlayıcıları](</tr/concepts/model-providers>), [Canlı Test](</tr/help/testing-live>), [İlk Kurulum](</tr/cli/onboard>)

Barındırılan Medya Sağlayıcıları 8 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Manifest](</tr/plugins/manifest>), [Canlı Test](</tr/help/testing-live>), [Dizin](</tr/providers>)

Sağlayıcı İşlemleri 12 yetenek

Deneysel0%

Alfa61%

Alfa68%

[Dizin](</tr/providers>), [Model Sağlayıcıları](</tr/concepts/model-providers>), [Manifest](</tr/plugins/manifest>), [Canlı Test](</tr/help/testing-live>), [Modeller](</tr/cli/models>)

Was this useful?YesNo

Open issue