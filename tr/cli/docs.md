---
title: Belgeler
source_url: https://docs.openclaw.ai/tr/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

Canlı OpenClaw docs dizininde terminalden arama yapın. Komut, `https://docs.openclaw.ai/mcp.SearchOpenClaw` adresindeki herkese açık, Mintlify üzerinde barındırılan docs MCP arama uç noktasına shell üzerinden çağrı yapar ve sonuçları terminalinizde gösterir.

## Kullanım

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

Argümanlar:

Argüman | Açıklama  
---|---  
`[query...]` | Serbest biçimli arama sorgusu. Çok kelimeli sorgular boşluklarla birleştirilip tek sorgu olarak gönderilir.  
  
## Örnekler

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

Sorgu olmadan, `openclaw docs` arama çalıştırmak yerine docs giriş noktası URL'sini ve örnek bir arama komutunu yazdırır.

## Nasıl çalışır

`openclaw docs`, docs arama MCP aracını çağırmak için `mcporter` CLI'ını çalıştırır, ardından araç çıktısındaki `Title: / Link: / Content:` bloklarını bir sonuç listesine ayrıştırır.

`mcporter`'ı çözümlemek için OpenClaw sırayla şunları kontrol eder:

  1. `PATH` üzerindeki `mcporter` (varsa doğrudan kullanılır).
  2. `pnpm` yüklüyse `pnpm dlx mcporter ...`.
  3. `npx` yüklüyse `npx -y mcporter ...`.


Hiçbiri yoksa komut, `pnpm` yükleme ipucuyla (`npm install -g pnpm`) başarısız olur.

Arama çağrısı sabit 30 saniyelik zaman aşımı kullanır. Sonuç alıntıları giriş başına yaklaşık 220 karaktere kısaltılır.

## Çıktı

Zengin (TTY) bir terminalde sonuçlar, bir başlığın ardından madde işaretli liste olarak gösterilir. Her madde sayfa başlığını, bağlantılı docs URL'sini ve sonraki satırda kısa bir alıntıyı gösterir. Boş sonuçlar "Sonuç yok." yazdırır.

Zengin olmayan çıktıda (pipe ile aktarılmış çıktı, `--no-color`, betikler), aynı veri Markdown olarak gösterilir:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## Çıkış kodları

Kod | Anlam  
---|---  
`0` | Arama başarılı oldu (sıfır sonuçlu yanıtlar dahil).  
`1` | MCP araç çağrısı başarısız oldu; stderr satır içinde yazdırılır.  
  
## İlgili

  * [CLI referansı](</tr/cli>)
  * [Canlı docs](<https://docs.openclaw.ai>)


Was this useful?YesNo