---
title: Zalo kişisel Plugin
source_url: https://docs.openclaw.ai/tr/plugins/zalouser
scraped_at: 2026-05-25
---

OpenClaw için Zalo Personal desteği, normal bir Zalo kullanıcı hesabını otomatikleştirmek üzere yerel `zca-js` kullanan bir Plugin aracılığıyla sağlanır.

## Adlandırma

Kanal kimliği, bunun **kişisel Zalo kullanıcı hesabını** otomatikleştirdiğini açıkça göstermek için `zalouser` şeklindedir (resmi değildir). `zalo` değerini gelecekteki olası resmi Zalo API entegrasyonu için ayrılmış tutuyoruz.

## Nerede çalışır

Bu Plugin **Gateway süreci içinde** çalışır.

Uzak bir Gateway kullanıyorsanız bunu **Gateway’in çalıştığı makinede** kurun/yapılandırın, ardından Gateway’i yeniden başlatın.

Harici bir `zca`/`openzca` CLI ikilisi gerekmez.

## Kurulum

### Seçenek A: npm’den kurma

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Geçerli resmi yayın etiketini takip etmek için yalın paketi kullanın. Tam bir sürümü yalnızca yeniden üretilebilir bir kurulum gerektiğinde sabitleyin.

Ardından Gateway’i yeniden başlatın.

### Seçenek B: yerel klasörden kurma (geliştirme)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Ardından Gateway’i yeniden başlatın.

## Yapılandırma

Kanal yapılandırması `channels.zalouser` altında bulunur (`plugins.entries.*` altında değil):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Aracı aracı

Araç adı: `zalouser`

Eylemler: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Kanal mesaj eylemleri, mesaj tepkileri için `react` desteği de sunar.

## İlgili

  * [Plugin oluşturma](</tr/plugins/building-plugins>)
  * [ClawHub](</tr/clawhub>)


Was this useful?YesNo