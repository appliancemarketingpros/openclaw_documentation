---
title: Tokenjuice
source_url: https://docs.openclaw.ai/tr/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice`, komut zaten çalıştırıldıktan sonra gürültülü `exec` ve `bash` araç sonuçlarını sıkıştıran isteğe bağlı paketlenmiş bir plugin'dir.

Komutun kendisini değil, döndürülen `tool_result` değerini değiştirir. Tokenjuice shell girdisini yeniden yazmaz, komutları yeniden çalıştırmaz ve çıkış kodlarını değiştirmez.

Bugün bu, PI gömülü çalıştırmalarına ve Codex app-server harness içindeki OpenClaw dinamik araçlarına uygulanır. Tokenjuice, OpenClaw'ın araç sonucu middleware'ine bağlanır ve çıktı etkin harness oturumuna geri gitmeden önce kırpar.

## Plugin'i etkinleştirin

Hızlı yol:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Eşdeğeri:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw plugin'i zaten paketlenmiş olarak sunar. Ayrı bir `plugins install` veya `tokenjuice install openclaw` adımı yoktur.

Yapılandırmayı doğrudan düzenlemeyi tercih ederseniz:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Tokenjuice'ın değiştirdiği şeyler

  * Gürültülü `exec` ve `bash` sonuçlarını oturuma geri beslenmeden önce sıkıştırır.
  * Özgün komut yürütmesini değiştirmeden bırakır.
  * Tam dosya içeriği okumalarını ve Tokenjuice'ın ham bırakması gereken diğer komutları korur.
  * İsteğe bağlı kalır: her yerde birebir çıktı istiyorsanız plugin'i devre dışı bırakın.


## Çalıştığını doğrulayın

  1. Plugin'i etkinleştirin.
  2. `exec` çağırabilen bir oturum başlatın.
  3. `git status` gibi gürültülü bir komut çalıştırın.
  4. Döndürülen araç sonucunun ham shell çıktısından daha kısa ve daha yapılandırılmış olduğunu kontrol edin.


## Plugin'i devre dışı bırakın

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Veya:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## İlgili

  * [Exec tool](</tr/tools/exec>)
  * [Thinking levels](</tr/tools/thinking>)
  * [Context engine](</tr/concepts/context-engine>)


Was this useful?YesNo