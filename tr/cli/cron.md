---
title: Cron
source_url: https://docs.openclaw.ai/tr/cli/cron
scraped_at: 2026-05-25
---

# `openclaw cron`

Gateway zamanlayıcısı için Cron işlerini yönetin.

## Oturumlar

`--session`, `main`, `isolated`, `current` veya `session:<id>` kabul eder.

Oturum anahtarları

  * `main`, aracının ana oturumuna bağlanır.
  * `isolated`, her çalıştırma için yeni bir transcript ve oturum kimliği oluşturur.
  * `current`, oluşturma anındaki etkin oturuma bağlanır.
  * `session:<id>`, açık bir kalıcı oturum anahtarına sabitler.

Yalıtılmış oturum semantiği

Yalıtılmış çalıştırmalar ortam konuşma bağlamını sıfırlar. Kanal ve grup yönlendirmesi, gönderme/kuyruğa alma ilkesi, yükseltme, kaynak ve ACP çalışma zamanı bağlaması yeni çalıştırma için sıfırlanır. Güvenli tercihler ve kullanıcının açıkça seçtiği model veya auth geçersiz kılmaları çalıştırmalar arasında taşınabilir.

## Teslim

`openclaw cron list` ve `openclaw cron show <job-id>` çözümlenen teslim rotasının önizlemesini gösterir. `channel: "last"` için önizleme, rotanın ana oturumdan mı yoksa geçerli oturumdan mı çözümlendiğini ya da kapalı şekilde başarısız olacağını gösterir.

Provider önekli hedefler, çözümlenmemiş duyuru kanallarındaki belirsizliği giderebilir. Örneğin `to: "telegram:123"`, `delivery.channel` atlandığında veya `last` olduğunda Telegram seçer. Yalnızca yüklenen plugin tarafından ilan edilen önekler provider seçicileridir. `delivery.channel` açıkça belirtilmişse, önek o kanalla eşleşmelidir; `channel: "whatsapp"` ile `to: "telegram:123"` reddedilir. `imessage:` ve `sms:` gibi servis önekleri kanalın sahip olduğu hedef sözdizimi olarak kalır.

### Teslim sahipliği

Yalıtılmış Cron sohbet teslimi aracı ile runner arasında paylaşılır:

  * Aracı, bir sohbet rotası kullanılabilir olduğunda `message` aracını kullanarak doğrudan gönderebilir.
  * `announce`, yalnızca aracı çözümlenen hedefe doğrudan göndermediyse son yanıtı yedek olarak teslim eder.
  * `webhook`, tamamlanan payload'u bir URL'ye gönderir.
  * `none`, runner yedek teslimini devre dışı bırakır.


`--announce`, son yanıt için runner yedek teslimidir. `--no-deliver`, bu yedeği devre dışı bırakır ancak bir sohbet rotası kullanılabilir olduğunda aracının `message` aracını kaldırmaz.

Etkin bir sohbetten oluşturulan hatırlatıcılar, yedek duyuru teslimi için canlı sohbet teslim hedefini korur. Dahili oturum anahtarları küçük harf olabilir; bunları Matrix oda kimlikleri gibi büyük/küçük harfe duyarlı provider kimlikleri için doğruluk kaynağı olarak kullanmayın.

### Hata teslimi

Hata bildirimleri şu sırayla çözümlenir:

  1. İşteki `delivery.failureDestination`.
  2. Genel `cron.failureDestination`.
  3. İşin birincil duyuru hedefi (açık bir hata hedefi ayarlanmadığında).


Not: yalıtılmış Cron çalıştırmaları, yanıt payload'u üretilmese bile çalıştırma düzeyindeki aracı hatalarını iş hataları olarak ele alır; böylece model/provider hataları yine hata sayaçlarını artırır ve hata bildirimlerini tetikler.

Yalıtılmış bir çalıştırma ilk model isteğinden önce zaman aşımına uğrarsa, `openclaw cron show` ve `openclaw cron runs`, `setup timed out before runner start` veya `stalled before first model call (last phase: context-engine)` gibi aşamaya özgü bir hata içerir. CLI destekli provider'lar için, model öncesi watchdog dış CLI turu başlayana kadar etkin kalır; bu nedenle oturum arama, hook, auth, prompt ve CLI kurulum takılmaları model öncesi Cron hataları olarak raporlanır.

## Zamanlama

### Tek seferlik işler

`--at <datetime>`, tek seferlik bir çalıştırma zamanlar. Offset içermeyen datetime değerleri, `--tz <iana>` da geçmediğiniz sürece UTC olarak ele alınır; bu seçenek, duvar saati zamanını verilen saat diliminde yorumlar.

### Yinelenen işler

Yinelenen işler, ardışık hatalardan sonra üstel yeniden deneme backoff'u kullanır: 30s, 1m, 5m, 15m, 60m. Bir sonraki başarılı çalıştırmadan sonra zamanlama normale döner.

Atlanan çalıştırmalar, yürütme hatalarından ayrı izlenir. Yeniden deneme backoff'unu etkilemezler, ancak `openclaw cron edit <job-id> --failure-alert-include-skipped`, hata uyarılarını yinelenen atlanmış çalıştırma bildirimlerine dahil edebilir.

Yerel yapılandırılmış bir model provider'ı hedefleyen yalıtılmış işler için Cron, aracı turunu başlatmadan önce hafif bir provider preflight çalıştırır. Loopback, private-network ve `.local` `api: "ollama"` provider'ları `/api/tags` üzerinde yoklanır; vLLM, SGLang ve LM Studio gibi yerel OpenAI uyumlu provider'lar `/models` üzerinde yoklanır. Endpoint erişilemezse, çalıştırma `skipped` olarak kaydedilir ve daha sonraki bir zamanlamada yeniden denenir; eşleşen ölü endpoint'ler, birçok işin aynı yerel sunucuya yük bindirmesini önlemek için 5 dakika önbelleğe alınır.

Not: Cron iş tanımları `jobs.json` içinde yaşarken, bekleyen çalışma zamanı durumu `jobs-state.json` içinde yaşar. `jobs.json` harici olarak düzenlenirse, Gateway değişen zamanlamaları yeniden yükler ve eski bekleyen slotları temizler; yalnızca biçimlendirme amaçlı yeniden yazımlar bekleyen slotu temizlemez.

### Manuel çalıştırmalar

`openclaw cron run`, manuel çalıştırma kuyruğa alınır alınmaz döner. Başarılı yanıtlar `{ ok: true, enqueued: true, runId }` içerir. Sonucu izlemek için `openclaw cron runs --id <job-id>` kullanın.

## Modeller

`cron add|edit --model <ref>`, iş için izin verilen bir model seçer.

Cron `--model`, bir sohbet oturumu `/model` geçersiz kılması değil, **iş birinciliğidir**. Bunun anlamı:

  * Seçilen iş modeli başarısız olduğunda yapılandırılmış model fallback'leri hâlâ uygulanır.
  * İş başına payload `fallbacks` mevcut olduğunda yapılandırılmış fallback listesinin yerini alır.
  * Boş bir iş başına fallback listesi (iş payload/API içinde `fallbacks: []`), Cron çalıştırmasını katı hale getirir.
  * Bir işte `--model` varsa ancak fallback listesi yapılandırılmamışsa, OpenClaw açık bir boş fallback geçersiz kılması geçirir; böylece aracı birinciliği gizli yeniden deneme hedefi olarak eklenmez.


### Yalıtılmış Cron model önceliği

Yalıtılmış Cron etkin modeli şu sırayla çözümler:

  1. Gmail-hook geçersiz kılması.
  2. İş başına `--model`.
  3. Saklanan Cron oturumu model geçersiz kılması (kullanıcı bir tane seçtiğinde).
  4. Aracı veya varsayılan model seçimi.


### Hızlı mod

Yalıtılmış Cron hızlı modu, çözümlenen canlı model seçimini izler. Model yapılandırması `params.fastMode` varsayılan olarak uygulanır, ancak saklanan oturum `fastMode` geçersiz kılması yapılandırmaya göre yine önceliklidir.

### Canlı model değiştirme yeniden denemeleri

Yalıtılmış bir çalıştırma `LiveSessionModelSwitchError` fırlatırsa, Cron yeniden denemeden önce etkin çalıştırma için değiştirilen provider ve modeli (ve mevcut olduğunda değiştirilen auth profil geçersiz kılmasını) kalıcı hale getirir. Dış yeniden deneme döngüsü, ilk denemeden sonra iki switch yeniden denemesiyle sınırlıdır; ardından sonsuza kadar döngüye girmek yerine iptal eder.

## Çalıştırma çıktısı ve retler

### Eski onay bastırma

Yalıtılmış Cron turları, eski yalnızca onay niteliğindeki yanıtları bastırır. İlk sonuç yalnızca geçici bir durum güncellemesiyse ve nihai yanıttan sorumlu bir alt aracı çalıştırması yoksa, Cron teslimden önce gerçek sonuç için bir kez yeniden prompt gönderir.

### Sessiz token bastırma

Yalıtılmış bir Cron çalıştırması yalnızca sessiz token (`NO_REPLY` veya `no_reply`) döndürürse, Cron hem doğrudan giden teslimi hem de yedek kuyruğa alınmış özet yolunu bastırır; böylece sohbete hiçbir şey gönderilmez.

### Yapılandırılmış retler

Yalıtılmış Cron çalıştırmaları, gömülü çalıştırmadan gelen yapılandırılmış yürütme reddi metadata'sını tercih eder; ardından `SYSTEM_RUN_DENIED`, `INVALID_REQUEST` ve onay bağlama reddi ifadeleri gibi son çıktıda bilinen ret işaretçilerine geri döner.

`cron list` ve çalıştırma geçmişi, engellenen bir komutu `ok` olarak bildirmek yerine ret nedenini gösterir.

## Saklama

Saklama ve budama yapılandırmada kontrol edilir:

  * `cron.sessionRetention` (varsayılan `24h`), tamamlanmış yalıtılmış çalıştırma oturumlarını budar.
  * `cron.runLog.maxBytes` ve `cron.runLog.keepLines`, `~/.openclaw/cron/runs/<jobId>.jsonl` dosyasını budar.


## Eski işleri taşıma

## Yaygın düzenlemeler

Mesajı değiştirmeden teslim ayarlarını güncelleyin:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "123456789"
[/code]

Yalıtılmış bir iş için teslimi devre dışı bırakın:

bashCopy code
[code]
    openclaw cron edit <job-id> --no-deliver
[/code]

Yalıtılmış bir iş için hafif bootstrap bağlamını etkinleştirin:

bashCopy code
[code]
    openclaw cron edit <job-id> --light-context
[/code]

Belirli bir kanala duyuru yapın:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"
[/code]

Bir Telegram forum konusuna duyuru yapın:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "-1001234567890" --thread-id 42
[/code]

Hafif bootstrap bağlamıyla yalıtılmış bir iş oluşturun:

bashCopy code
[code]
    openclaw cron add \  --name "Lightweight morning brief" \  --cron "0 7 * * *" \  --session isolated \  --message "Summarize overnight updates." \  --light-context \  --no-deliver
[/code]

`--light-context`, yalnızca yalıtılmış aracı turu işlerine uygulanır. Cron çalıştırmaları için hafif mod, tam workspace bootstrap kümesini enjekte etmek yerine bootstrap bağlamını boş tutar.

## Yaygın yönetici komutları

Manuel çalıştırma ve inceleme:

bashCopy code
[code]
    openclaw cron listopenclaw cron list --agent opsopenclaw cron get <job-id>openclaw cron show <job-id>openclaw cron run <job-id>openclaw cron run <job-id> --dueopenclaw cron runs --id <job-id> --limit 50
[/code]

`openclaw cron list`, varsayılan olarak eşleşen tüm işleri gösterir. Yalnızca etkili normalleştirilmiş aracı kimliği eşleşen işleri göstermek için `--agent <id>` geçin; saklanan aracı kimliği olmayan işler yapılandırılmış varsayılan aracı olarak sayılır.

`openclaw cron get <job-id>`, saklanan iş JSON'unu doğrudan döndürür. Teslim rotası önizlemesiyle insan tarafından okunabilir görünümü istediğinizde `cron show <job-id>` kullanın.

`cron list --json` ve `cron show <job-id> --json`, her işte üst düzey bir `status` alanı içerir; bu alan `enabled`, `state.runningAtMs` ve `state.lastRunStatus` üzerinden hesaplanır. Değerler: `disabled`, `running`, `ok`, `error`, `skipped` veya `idle`. Bu, insan tarafından okunabilir durum sütununu yansıtır; böylece harici araçlar iş durumunu yeniden türetmeden okuyabilir.

`cron runs` girdileri, hedeflenen Cron hedefi, çözümlenen hedef, message-tool gönderimleri, fallback kullanımı ve teslim edilmiş durumla birlikte teslim tanılamalarını içerir.

Aracı ve oturum yeniden hedefleme:

bashCopy code
[code]
    openclaw cron edit <job-id> --agent opsopenclaw cron edit <job-id> --clear-agentopenclaw cron edit <job-id> --session currentopenclaw cron edit <job-id> --session "session:daily-brief"
[/code]

`openclaw cron add`, aracı turu işlerinde `--agent` atlandığında uyarır ve varsayılan aracıya (`main`) geri döner. Belirli bir aracı sabitlemek için oluşturma sırasında `--agent <id>` geçin.

Teslim ayarlamaları:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"openclaw cron edit <job-id> --best-effort-deliveropenclaw cron edit <job-id> --no-best-effort-deliveropenclaw cron edit <job-id> --no-deliver
[/code]

## İlgili

  * [CLI referansı](</tr/cli>)
  * [Zamanlanmış görevler](</tr/automation/cron-jobs>)


Was this useful?YesNo