---
title: macOS IPC
source_url: https://docs.openclaw.ai/tr/platforms/mac/xpc
scraped_at: 2026-05-25
---

# OpenClaw macOS IPC mimarisi

**Geçerli model:** yerel bir Unix socket, **Node host servisinin** **macOS uygulamasına** bağlanmasını sağlar; bu exec onayları + `system.run` içindir. Keşif/bağlantı kontrolleri için bir `openclaw-mac` debug CLI vardır; ajan eylemleri yine de Gateway WebSocket ve `node.invoke` üzerinden akar. UI otomasyonu PeekabooBridge kullanır.

## Hedefler

  * TCC ile ilgili tüm işleri (bildirimler, ekran kaydı, mikrofon, konuşma, AppleScript) sahiplenen tek GUI uygulama örneği.
  * Otomasyon için küçük bir yüzey: Gateway + Node komutları ve UI otomasyonu için PeekabooBridge.
  * Öngörülebilir izinler: her zaman aynı imzalı bundle ID, launchd tarafından başlatılır; böylece TCC izinleri kalıcı olur.


## Nasıl çalışır

### Gateway + Node taşıması

  * Uygulama Gateway'i çalıştırır (yerel mod) ve ona bir Node olarak bağlanır.
  * Ajan eylemleri `node.invoke` ile gerçekleştirilir (örn. `system.run`, `system.notify`, `canvas.*`).


### Node servisi + uygulama IPC

  * Headless bir Node host servisi Gateway WebSocket'e bağlanır.
  * `system.run` istekleri yerel bir Unix socket üzerinden macOS uygulamasına iletilir.
  * Uygulama exec işlemini UI bağlamında gerçekleştirir, gerekirse istem gösterir ve çıktıyı döndürür.


Diyagram (SCI):

CodeCopy code
[code]
    Agent -> Gateway -> Node Service (WS)                      |  IPC (UDS + token + HMAC + TTL)                      v                  Mac App (UI + TCC + system.run)
[/code]

### PeekabooBridge (UI otomasyonu)

  * UI otomasyonu, `bridge.sock` adlı ayrı bir UNIX socket ve PeekabooBridge JSON protokolünü kullanır.
  * Host tercih sırası (istemci tarafı): Peekaboo.app → Claude.app → OpenClaw.app → yerel yürütme.
  * Güvenlik: bridge host'ları izin verilen bir TeamID gerektirir; DEBUG-only aynı UID kaçış kapısı `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` ile korunur (Peekaboo sözleşmesi).
  * Ayrıntılar için bkz.: [PeekabooBridge kullanımı](</tr/platforms/mac/peekaboo>).


## Operasyonel akışlar

  * Yeniden başlatma/yeniden derleme: `SIGN_IDENTITY="Apple Development: &lt;Developer Name&gt; (&lt;TEAMID&gt;)" scripts/restart-mac.sh`
    * Mevcut örnekleri sonlandırır
    * Swift derleme + paketleme yapar
    * LaunchAgent'i yazar/bootstrap eder/kickstart eder
  * Tek örnek: aynı bundle ID ile başka bir örnek çalışıyorsa uygulama erkenden çıkar.


## Sağlamlaştırma notları

  * Tüm ayrıcalıklı yüzeylerde TeamID eşleşmesini zorunlu kılmayı tercih edin.
  * PeekabooBridge: `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (yalnızca DEBUG), yerel geliştirme için aynı UID çağıranlarına izin verebilir.
  * Tüm iletişim yalnızca yerel kalır; hiçbir ağ socket'i açığa çıkarılmaz.
  * TCC istemleri yalnızca GUI uygulama bundle'ından gelir; yeniden derlemeler arasında imzalı bundle ID'yi kararlı tutun.
  * IPC sağlamlaştırma: socket modu `0600`, token, peer-UID kontrolleri, HMAC challenge/response, kısa TTL.


## İlgili

  * [macOS uygulaması](</tr/platforms/macos>)
  * [macOS IPC akışı (Yürütme onayları)](</tr/tools/exec-approvals-advanced#macos-ipc-flow>)


Was this useful?YesNo