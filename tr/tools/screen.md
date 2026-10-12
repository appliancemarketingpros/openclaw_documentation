---
title: Ekran
source_url: https://docs.openclaw.ai/tr/tools/screen
scraped_at: 2026-10-12
---

CapabilitiesTools

`screen` aracı, bir ajanın tarayıcı tabanlı Control UI'ı düzenlemesini sağlar. Bu, ekran görüntüsü yakalama veya tarayıcı otomasyonu değil, türü belirlenmiş bir yerleşim ve gezinme yüzeyidir.

Araç yalnızca kaynak istemci `ui-commands` yeteneğini bildirdiğinde sunulur. Araç çalıştırılırken en az bir yetenekli Control UI'ın hâlâ bağlı olması gerekir; aksi takdirde Gateway, `UNAVAILABLE` döndürür.

## Eylemler

Eylem | Etki | İsteğe bağlı girdiler  
---|---|---  
`split_right` | Hedef oturum bölmesini sağa doğru böler | `sessionKey` (varsayılanı geçerli oturumdur)  
`split_down` | Hedef oturum bölmesini aşağı doğru böler | `sessionKey` (varsayılanı geçerli oturumdur)  
`close_pane` | Hedef oturum bölmesini kapatır | `sessionKey` (varsayılanı geçerli oturumdur)  
`focus` | Hedef oturum bölmesine odaklanır | `sessionKey` (varsayılanı geçerli oturumdur)  
`navigate` | Hedef oturumu açar | `sessionKey` (varsayılanı geçerli oturumdur)  
`sidebar_show` / `sidebar_hide` | Ana kenar çubuğunu gösterir veya gizler | -  
`terminal_show` / `terminal_hide` | Operatör terminal panelini gösterir veya gizler | Gösterirken `dock` (`bottom` veya `right`)  
`browser_show` / `browser_hide` | Tarayıcı panelini gösterir veya gizler | Gösterirken `dock` (`bottom` veya `right`)  
  
Başarılı bir komut, Gateway türü belirlenmiş `ui.command` olayını yayımladıktan sonra `{ "ok": true }` döndürür.

## Yönlendirme ve güvenlik

Protokol v1, komutu kasıtlı olarak `ui-commands` bildiren tüm bağlı Control UI'lara gönderir; belirli bir tarayıcı sekmesini hedeflemez. Aynı operatörün birden fazla açık panosu olduğunda bu önemlidir.

Gateway RPC, `operator.write` gerektirir. Araç yalnızca sunum durumunu değiştirebilir: pikselleri okuyamaz, ekran görüntüsü alamaz, rastgele sayfa içeriğine tıklayamaz veya seçilen oturum ve operatör panellerinin izinlerini atlayamaz.

## İlgili

  * [Control UI](</web/control-ui>)
  * [Gateway protokolü](</tr/gateway/protocol#method-families>)
  * [Tarayıcı aracı](</tr/tools/browser>)


Was this useful?YesNo

Open issue