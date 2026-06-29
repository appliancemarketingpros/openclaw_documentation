---
title: Çalışma Panosu CLI
source_url: https://docs.openclaw.ai/tr/cli/workboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

`openclaw workboard`, paketle gelen [Workboard Plugin'i](</tr/plugins/workboard>) için terminal yüzeyidir. Bir operatörün kartları listelemesini, kart oluşturmasını, tek bir kartı incelemesini ve çalışan Gateway'den hazır işi alt ajan worker çalıştırmalarına dağıtmasını sağlar.

Komutu kullanmadan önce Plugin'i etkinleştirin:

bashCopy code
[code]
    openclaw plugins enable workboardopenclaw gateway restart
[/code]

## Kullanım

bashCopy code
[code]
    openclaw workboard list [--board <id>] [--status <status>] [--include-archived] [--json]openclaw workboard create <title...> [--notes <text>] [--status <status>] [--priority <priority>] [--agent <id>] [--board <id>] [--labels <items>] [--json]openclaw workboard show <id> [--json]openclaw workboard dispatch [--url <url>] [--token <token>] [--timeout <ms>] [--json]
[/code]

Komut, dashboard ve Workboard ajan araçları tarafından kullanılan aynı Plugin'e ait SQLite veritabanını okur ve yazar. Kart kimlikleri, bir komut kart kimliği kabul ettiğinde tam kimlik olarak veya belirsiz olmayan bir önekle geçirilebilir.

## `list`

bashCopy code
[code]
    openclaw workboard listopenclaw workboard list --board default --status readyopenclaw workboard list --json
[/code]

Metin çıktısı kompakt olur:

textCopy code
[code]
    7f4a2c10  ready     high    default agent-a  Fix stale worker heartbeat
[/code]

Sütunlar kimlik öneki, durum, öncelik, pano kimliği, isteğe bağlı ajan kimliği ve başlıktır.

Bayraklar:

Bayrak | Amaç  
---|---  
`--board <id>` | Sonuçları tek bir pano ad alanıyla sınırla  
`--status <status>` | Sonuçları tek bir Workboard durumuyla sınırla  
`--include-archived` | Arşivlenmiş kartları kompakt metin çıktısına dahil et  
`--json` | Tam kart listesini makine JSON'u olarak yazdır  
  
Kompakt metin çıktısı, CLI'nin `/workboard list` komutuyla eşleşmesi için arşivlenmiş kartları varsayılan olarak gizler. Bunları göstermek için `--include-archived` geçirin. JSON çıktısı, mevcut otomasyon için arşivlenmiş kartlar dahil tam kart listesini korur.

## `create`

bashCopy code
[code]
    openclaw workboard create "Fix stale worker heartbeat" --priority high --labels bug,workboardopenclaw workboard create "Write Workboard docs" --status ready --agent docs-agent --board docs --notes "Cover CLI, slash command, dispatch, and SQLite state."
[/code]

Bayraklar:

Bayrak | Amaç  
---|---  
`--notes <text>` | İlk kart notları  
`--status <status>` | İlk durum, varsayılan `todo`  
`--priority <priority>` | Öncelik, varsayılan `normal`  
`--agent <id>` | Kartı bir ajana veya sahip kimliğine ata  
`--board <id>` | Kartı bir pano ad alanında sakla  
`--labels <items>` | Virgülle ayrılmış etiketler  
`--json` | Oluşturulan kartı makine JSON'u olarak yazdır  
  
`create`, doğrudan Workboard SQLite durumuna yazar. Kart, Control UI Workboard sekmesinde ve Workboard araçlarında hemen görünür olur.

## `show`

bashCopy code
[code]
    openclaw workboard show 7f4a2c10openclaw workboard show 7f4a2c10 --json
[/code]

Metin çıktısı, kompakt kart satırını ve notları yazdırır. JSON çıktısı; yürütme metadatası, denemeler, yorumlar, bağlantılar, kanıt, artifact'ler, worker günlükleri, protokol durumu, tanılamalar ve otomasyon metadatası dahil olmak üzere tam kart kaydını döndürür.

## `dispatch`

bashCopy code
[code]
    openclaw workboard dispatchopenclaw workboard dispatch --jsonopenclaw workboard dispatch --url http://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

`dispatch` önce çalışan Gateway RPC yöntemi `workboard.cards.dispatch`'i çağırır. Bu yol, dashboard dağıtım eylemiyle aynı alt ajan runtime'ını kullanır; böylece hazır kartlar, bağlı oturum anahtarlarına sahip görev izlemeli worker çalıştırmalarına dönüşür. Atanmış ajanı olan kartlar, ajan kapsamlı alt ajan oturum anahtarlarını kullanır; atanmamış kartlar ise Gateway'in yapılandırılmış varsayılan ajanının korunması için kapsamsız bir alt ajan anahtarını korur.

Dağıtım döngüsü:

  1. Bağımlılığı hazır olan çocukları `ready` durumuna yükseltir.
  2. Süresi dolmuş talepleri veya zaman aşımına uğramış worker çalıştırmalarını engeller.
  3. Hazır kartlara dağıtım metadatası kaydeder.
  4. Talep edilmemiş hazır kartlardan küçük bir toplu seçim yapar.
  5. Seçilen her kartı dağıtıcı veya atanmış ajan için talep eder.
  6. Sınırlı kart bağlamı ve kart talep token'ı ile bir alt ajan worker çalıştırması başlatır.
  7. Worker çalıştırma kimliğini, oturum anahtarını, Gateway görev defteri bildirdiğinde görev bağlantısını, yürütme durumunu ve worker günlüğünü kartta saklar.


Seçim bilinçli olarak muhafazakardır. Bir dağıtım varsayılan olarak en fazla üç worker başlatır, arşivlenmiş veya zaten talep edilmiş kartları atlar ve tek bir geçişte sahip veya ajan başına yalnızca bir kart başlatır. Etkin çalışan veya inceleme işi tarafından zaten sahiplenilmiş kartlar daha sonraki bir dağıtıma bırakılır.

Bir kart talep edildikten sonra worker başlatma başarısız olursa Workboard o kartı engeller, talebi temizler ve hatayı kart yürütme ve worker günlüğü metadatasına kaydeder. Bu, başarısız başlatmaların kartı sessizce kuyruğa döndürmek yerine görünür kalmasını sağlar.

Açık bir Gateway hedefi sağlanmadıysa ve yerel Gateway kullanılamıyorsa veya henüz Workboard dağıtım yöntemini sunmuyorsa, CLI yerel Workboard durumuna karşı yalnızca veri dağıtımına geri döner. Yalnızca veri dağıtımı yine de bağımlılıkları yükseltebilir, bayat talepleri temizleyebilir ve zaman aşımına uğramış çalıştırmaları engelleyebilir, ancak worker başlatmaz. Kimlik doğrulama, izin, doğrulama hataları ve açık bir `--url` veya `--token` hedefi için hatalar doğrudan bildirilir.

Metin çıktısı worker başlatmalarını bildirir:

textCopy code
[code]
    dispatch complete: started=2 failures=0
[/code]

Geri dönüş çıktısı açıktır:

textCopy code
[code]
    gateway unavailable; data dispatch only: promoted=1 blocked=0
[/code]

JSON çıktısı dağıtım sonucunu içerir. Gateway destekli dağıtım `started` ve `startFailures` içerebilir; yalnızca veri geri dönüşü `gatewayUnavailable: true` içerir. Talep token'ları kart JSON çıktısından redakte edilir.

Dashboard'da aynı dağıtım sonucu kısa bir özet olarak gösterilir; böylece bir operatör kart ayrıntılarını açmadan kaç kartın başlatıldığını, yükseltildiğini, engellendiğini, geri talep edildiğini veya başarısız olduğunu görebilir.

## Slash Komut Eşliği

Komut kullanabilen kanallar eşleşen slash komutunu kullanabilir:

textCopy code
[code]
    /workboard list/workboard show 7f4a2c10/workboard create Fix stale worker heartbeat/workboard dispatch
[/code]

Slash komut dağıtımı da Gateway alt ajan runtime'ını kullanır; bu nedenle dashboard ve CLI Gateway yoluyla aynı talep, worker başlatma ve hata davranışını izler.

`/workboard list` ve `/workboard show`, yetkili komut gönderenler için okuma komutlarıdır. `/workboard create` ve `/workboard dispatch` pano durumunu değiştirir ve sohbet yüzeylerinde sahip durumu veya `operator.write` ya da `operator.admin` yetkisine sahip bir Gateway istemcisi gerektirir.

## İzinler

CLI dağıtım yolu, `operator.read` ve `operator.write` kapsamlarıyla Gateway RPC'yi çağırır. Salt okunur bir Gateway token'ı Workboard verilerini okuma yöntemleriyle inceleyebilir, ancak kart oluşturamaz veya worker dağıtamaz.

Yerel `list`, `create` ve `show` komutları, geçerli profil tarafından kullanılan yerel OpenClaw durum dizininde çalışır. Farklı bir durum kökü gerektiğinde üst düzey `openclaw` komutunda `--dev` veya `--profile <name>` kullanın.

## Sorun Giderme

### Hiç Kart Görünmüyor

Plugin'in aynı profil ve durum kökü için etkin olduğunu doğrulayın:

bashCopy code
[code]
    openclaw plugins inspect workboard --runtime --json
[/code]

Dashboard kartları gösteriyor ancak CLI göstermiyorsa, iki komutun da aynı `--dev` veya `--profile` ayarını kullandığını kontrol edin.

### Dispatch Yalnızca Veri Diyor

Gateway'i başlatın veya yeniden başlatın:

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway status --deep
[/code]

Ardından `openclaw workboard dispatch` komutunu yeniden deneyin. Yalnızca veri geri dönüşü yerel durum temizliği için kullanışlıdır, ancak worker çalıştırmaları canlı bir Gateway gerektirir.

### Dispatch Hiçbir Şey Başlatmıyor

Etkin talebi olmayan en az bir `ready` kart olduğunu kontrol edin:

bashCopy code
[code]
    openclaw workboard list --status ready
[/code]

Aynı sahipte zaten çalışan veya inceleme işi olduğunda kartlar da atlanabilir. Tamamlanan işi `done` durumuna taşıyın, bayat talepleri Workboard araçlarıyla serbest bırakın veya etkin worker bittikten sonra dağıtımı yeniden çalıştırın.

## İlgili

  * [Workboard Plugin'i](</tr/plugins/workboard>)
  * [CLI başvurusu](</tr/cli>)
  * [Slash komutları](</tr/tools/slash-commands>)
  * [Control UI](</tr/web/control-ui>)


Was this useful?YesNo

Open issue