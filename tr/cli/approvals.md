---
title: Onaylar
source_url: https://docs.openclaw.ai/tr/cli/approvals
scraped_at: 2026-05-25
---

# `openclaw approvals`

**Yerel ana bilgisayar** , **Gateway ana bilgisayarı** veya bir **Node ana bilgisayarı** için exec onaylarını yönetin. Varsayılan olarak komutlar diskteki yerel onaylar dosyasını hedefler. Gateway'i hedeflemek için `--gateway`, belirli bir Node'u hedeflemek için `--node` kullanın.

Takma ad: `openclaw exec-approvals`

İlgili:

  * Exec onayları: [Exec approvals](</tr/tools/exec-approvals>)
  * Node'lar: [Nodes](</tr/nodes>)


## `openclaw exec-policy`

`openclaw exec-policy`, istenen `tools.exec.*` yapılandırmasını ve yerel ana bilgisayar onayları dosyasını tek adımda uyumlu tutmak için kullanılan yerel kolaylık komutudur.

Bunu şu durumlarda kullanın:

  * yerel istenen ilkeyi, ana bilgisayar onayları dosyasını ve etkin birleştirmeyi incelemek
  * YOLO veya deny-all gibi yerel bir ön ayarı uygulamak
  * yerel `tools.exec.*` ile yerel `~/.openclaw/exec-approvals.json` dosyasını eşzamanlamak


Örnekler:

bashCopy code
[code]
    openclaw exec-policy showopenclaw exec-policy show --json openclaw exec-policy preset yoloopenclaw exec-policy preset cautious --json openclaw exec-policy set --host gateway --security full --ask off --ask-fallback full
[/code]

Çıktı kipleri:

  * `--json` yok: insan tarafından okunabilir tablo görünümünü yazdırır
  * `--json`: makine tarafından okunabilir yapılandırılmış çıktı yazdırır


Geçerli kapsam:

  * `exec-policy` **yalnızca yereldir**
  * yerel yapılandırma dosyasını ve yerel onaylar dosyasını birlikte günceller
  * ilkeyi Gateway ana bilgisayarına veya bir Node ana bilgisayarına **göndermez**
  * `--host node` bu komutta reddedilir çünkü Node exec onayları çalışma zamanında Node'dan alınır ve bunun yerine Node hedefli onay komutlarıyla yönetilmelidir
  * `openclaw exec-policy show`, yerel onaylar dosyasından etkin bir ilke türetmek yerine `host=node` kapsamlarını çalışma zamanında Node tarafından yönetilen olarak işaretler


Uzak ana bilgisayar onaylarını doğrudan düzenlemeniz gerekiyorsa `openclaw approvals set --gateway` veya `openclaw approvals set --node <id|name|ip>` kullanmaya devam edin.

## Yaygın komutlar

bashCopy code
[code]
    openclaw approvals getopenclaw approvals get --node <id|name|ip>openclaw approvals get --gateway
[/code]

`openclaw approvals get` artık yerel, Gateway ve Node hedefleri için etkin exec ilkesini gösterir:

  * istenen `tools.exec` ilkesi
  * ana bilgisayar onayları dosyası ilkesi
  * öncelik kuralları uygulandıktan sonraki etkin sonuç


Öncelik kasıtlıdır:

  * ana bilgisayar onayları dosyası uygulanabilir doğruluk kaynağıdır
  * istenen `tools.exec` ilkesi niyeti daraltabilir veya genişletebilir, ancak etkin sonuç yine de ana bilgisayar kurallarından türetilir
  * `--node`, Node ana bilgisayarı onayları dosyasını Gateway `tools.exec` ilkesiyle birleştirir, çünkü her ikisi de çalışma zamanında hâlâ uygulanır
  * Gateway yapılandırması kullanılamıyorsa CLI, Node onayları anlık görüntüsüne geri düşer ve son çalışma zamanı ilkesinin hesaplanamadığını belirtir


## Bir dosyadan onayları değiştirin

bashCopy code
[code]
    openclaw approvals set --file ./exec-approvals.jsonopenclaw approvals set --stdin <<'EOF'{ version: 1, defaults: { security: "full", ask: "off" } }EOFopenclaw approvals set --node <id|name|ip> --file ./exec-approvals.jsonopenclaw approvals set --gateway --file ./exec-approvals.json
[/code]

`set`, yalnızca katı JSON değil, JSON5 kabul eder. `--file` veya `--stdin` kullanın, ikisini birden değil.

## "Asla sorma" / YOLO örneği

Exec onaylarında asla durmaması gereken bir ana bilgisayar için, ana bilgisayar onayları varsayılanlarını `full` \+ `off` olarak ayarlayın:

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Node sürümü:

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Bu yalnızca **ana bilgisayar onayları dosyasını** değiştirir. İstenen OpenClaw ilkesini uyumlu tutmak için ayrıca şunları da ayarlayın:

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask off
[/code]

Bu örnekte neden `tools.exec.host=gateway` kullanılıyor:

  * `host=auto` hâlâ "varsa sandbox, aksi takdirde Gateway" anlamına gelir.
  * YOLO, yönlendirmeyle değil onaylarla ilgilidir.
  * Bir sandbox yapılandırılmış olsa bile ana bilgisayarda exec istiyorsanız ana bilgisayar seçimini `gateway` veya `/exec host=gateway` ile açıkça belirtin.


Bu, mevcut ana bilgisayar varsayılanı YOLO davranışıyla eşleşir. Onaylar istiyorsanız bunu sıkılaştırın.

Yerel kısayol:

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

Bu yerel kısayol, istenen yerel `tools.exec.*` yapılandırmasını ve yerel onay varsayılanlarını birlikte günceller. Niyet olarak yukarıdaki el ile iki adımlı kuruluma denktir, ancak yalnızca yerel makine için geçerlidir.

## İzin listesi yardımcıları

bashCopy code
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"openclaw approvals allowlist add --agent "*" "/usr/bin/uname" openclaw approvals allowlist remove "~/Projects/**/bin/rg"
[/code]

## Yaygın seçenekler

`get`, `set` ve `allowlist add|remove` komutlarının tümü şunları destekler:

  * `--node <id|name|ip>`
  * `--gateway`
  * paylaşılan Node RPC seçenekleri: `--url`, `--token`, `--timeout`, `--json`


Hedefleme notları:

  * hedef bayrağı yoksa diskteki yerel onaylar dosyası hedeflenir
  * `--gateway`, Gateway ana bilgisayarı onayları dosyasını hedefler
  * `--node`, kimlik, ad, IP veya kimlik öneki çözümlendikten sonra bir Node ana bilgisayarını hedefler


`allowlist add|remove` ayrıca şunları da destekler:

  * `--agent <id>` (varsayılan `*`)


## Notlar

  * `--node`, `openclaw nodes` ile aynı çözümleyiciyi kullanır (kimlik, ad, ip veya kimlik öneki).
  * `--agent` varsayılan olarak `"*"` değerini kullanır; bu tüm ajanlara uygulanır.
  * Node ana bilgisayarı `system.execApprovals.get/set` özelliğini ilan etmelidir (macOS uygulaması veya headless Node ana bilgisayarı).
  * Onay dosyaları ana bilgisayar başına `~/.openclaw/exec-approvals.json` konumunda saklanır.


## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Exec approvals](</tr/tools/exec-approvals>)


Was this useful?YesNo