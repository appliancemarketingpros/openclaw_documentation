---
title: Web
source_url: https://docs.openclaw.ai/tr/web
scraped_at: 2026-05-25
---

Gateway, Gateway WebSocket ile aynı porttan küçük bir **tarayıcı Kontrol Arayüzü** (Vite + Lit) sunar:

  * varsayılan: `http://<host>:18789/`
  * `gateway.tls.enabled: true` ile: `https://<host>:18789/`
  * isteğe bağlı önek: `gateway.controlUi.basePath` ayarlayın (örn. `/openclaw`)


Yetenekler [Kontrol Arayüzü](</tr/web/control-ui>) içinde yer alır. Bu sayfanın geri kalanı bağlama modlarına, güvenliğe ve web'e açık yüzeylere odaklanır.

## Webhook'lar

`hooks.enabled=true` olduğunda Gateway, aynı HTTP sunucusunda küçük bir Webhook uç noktası da açar. Kimlik doğrulama + yükler için [Gateway yapılandırması](</tr/gateway/configuration>) → `hooks` bölümüne bakın.

## Yapılandırma (varsayılan olarak açık)

Varlıklar mevcut olduğunda (`dist/control-ui`) Kontrol Arayüzü **varsayılan olarak etkindir**. Bunu yapılandırma üzerinden kontrol edebilirsiniz:

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath isteğe bağlıdır  },}
[/code]

## Tailscale erişimi

### Entegre Serve (önerilir)

Gateway'i loopback üzerinde tutun ve Tailscale Serve'ün onu proxy'lemesine izin verin:

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

Ardından gateway'i başlatın:

bashCopy code
[code]
    openclaw gateway
[/code]

Açın:

  * `https://<magicdns>/` (veya yapılandırdığınız `gateway.controlUi.basePath`)


### Tailnet bağlama + token

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

Ardından gateway'i başlatın (bu loopback olmayan örnek, paylaşılan gizli token kimlik doğrulaması kullanır):

bashCopy code
[code]
    openclaw gateway
[/code]

Açın:

  * `http://<tailscale-ip>:18789/` (veya yapılandırdığınız `gateway.controlUi.basePath`)


### Genel internet (Funnel)

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // veya OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## Güvenlik notları

  * Gateway kimlik doğrulaması varsayılan olarak gereklidir (etkinleştirildiğinde token, parola, trusted-proxy veya Tailscale Serve kimlik başlıkları).
  * Loopback olmayan bağlamalar yine de gateway kimlik doğrulamasını **gerektirir**. Pratikte bu, token/parola kimlik doğrulaması veya `gateway.auth.mode: "trusted-proxy"` kullanan kimlik farkındalığına sahip bir ters proxy anlamına gelir.
  * Sihirbaz varsayılan olarak paylaşılan gizli kimlik doğrulaması oluşturur ve genellikle bir gateway token'ı üretir (loopback üzerinde bile).
  * Paylaşılan gizli modda UI, `connect.params.auth.token` veya `connect.params.auth.password` gönderir.
  * `gateway.tls.enabled: true` olduğunda, yerel pano ve durum yardımcıları `https://` pano URL'leri ve `wss://` WebSocket URL'leri oluşturur.
  * Tailscale Serve veya `trusted-proxy` gibi kimlik taşıyan modlarda, WebSocket kimlik doğrulama denetimi bunun yerine istek başlıklarından karşılanır.
  * Loopback olmayan Kontrol Arayüzü dağıtımları için `gateway.controlUi.allowedOrigins` değerini açıkça ayarlayın (tam origin'ler). Bu olmadan, gateway başlatılması varsayılan olarak reddedilir.
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true`, Host-header origin yedek modunu etkinleştirir, ancak bu tehlikeli bir güvenlik düşürmesidir.
  * Serve ile, `gateway.auth.allowTailscale` `true` olduğunda Tailscale kimlik başlıkları Kontrol Arayüzü/WebSocket kimlik doğrulamasını karşılayabilir (token/parola gerekmez). HTTP API uç noktaları bu Tailscale kimlik başlıklarını kullanmaz; bunun yerine gateway'in normal HTTP kimlik doğrulama modunu izler. Açık kimlik bilgileri gerektirmek için `gateway.auth.allowTailscale: false` ayarlayın. Bkz. [Tailscale](</tr/gateway/tailscale>) ve [Güvenlik](</tr/gateway/security>). Bu token'sız akış, gateway ana makinesinin güvenilir olduğunu varsayar.
  * `gateway.tailscale.mode: "funnel"`, `gateway.auth.mode: "password"` (paylaşılan parola) gerektirir.


## UI'yi oluşturma

Gateway statik dosyaları `dist/control-ui` konumundan sunar. Bunları şu komutla oluşturun:

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo