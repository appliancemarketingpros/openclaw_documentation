---
title: Tarayıcıyla oturum açma
source_url: https://docs.openclaw.ai/tr/tools/browser-login
scraped_at: 2026-05-25
---

## Manuel giriş (önerilir)

Bir site giriş yapmayı gerektiriyorsa, **ana makine** tarayıcı profilinde (openclaw tarayıcısı) **manuel olarak oturum açın**.

Modele kimlik bilgilerinizi **vermeyin**. Otomatik girişler genellikle bot karşıtı savunmaları tetikler ve hesabın kilitlenmesine neden olabilir.

Ana tarayıcı belgelerine dönün: [Tarayıcı](</tr/tools/browser>).

## Hangi Chrome profili kullanılır?

OpenClaw, **ayrılmış bir Chrome profilini** denetler (`openclaw` adlı, turuncu tonlu UI). Bu, günlük tarayıcı profilinizden ayrıdır.

Aracı tarayıcı aracı çağrıları için:

  * Varsayılan seçim: aracı, yalıtılmış `openclaw` tarayıcısını kullanmalıdır.
  * `profile="user"` seçeneğini yalnızca mevcut oturum açılmış oturumlar önemli olduğunda ve kullanıcı herhangi bir ekleme istemine tıklamak/onaylamak için bilgisayar başındaysa kullanın.
  * Birden fazla kullanıcı tarayıcı profiliniz varsa, tahmin etmek yerine profili açıkça belirtin.


Erişmenin iki kolay yolu:

  1. **Aracıdan tarayıcıyı açmasını isteyin** ve ardından kendiniz giriş yapın.
  2. **CLI üzerinden açın** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Birden fazla profiliniz varsa, `--browser-profile <name>` iletin (varsayılan `openclaw` değeridir).

## X/Twitter: önerilen akış

  * **Okuma/arama/konular:** **ana makine** tarayıcısını kullanın (manuel giriş).
  * **Güncellemeler yayımlama:** **ana makine** tarayıcısını kullanın (manuel giriş).


## Sandbox + ana makine tarayıcı erişimi

Sandbox içindeki tarayıcı oturumlarının bot algılamayı tetikleme olasılığı **daha yüksektir**. X/Twitter (ve diğer katı siteler) için **ana makine** tarayıcısını tercih edin.

Aracı sandbox içindeyse, tarayıcı aracı varsayılan olarak sandbox'ı kullanır. Ana makine denetimine izin vermek için:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Ardından ana makine tarayıcısını kendiniz açın (CLI çağrıları her zaman ana makine tarayıcısına karşı çalışır):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

Aracının `browser` aracı çağrıları, `sandbox.browser.allowHostControl: true` ayarlandıktan sonra ana makineyi hedefleyebilir. Alternatif olarak, güncellemeleri yayımlayan aracı için sandbox'ı devre dışı bırakın.

## İlgili

  * [Tarayıcı](</tr/tools/browser>)
  * [Tarayıcı Linux sorun giderme](</tr/tools/browser-linux-troubleshooting>)
  * [Tarayıcı WSL2 sorun giderme](</tr/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo