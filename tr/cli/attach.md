---
title: CLI'yi bağla
source_url: https://docs.openclaw.ai/tr/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach`, tek bir Gateway oturumuna bağlı katı bir geçici MCP yapılandırmasıyla Claude Code'u başlatır.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Seçenekler:

  * `--session <key>` izni bir Gateway oturumuna bağlar. Varsayılan olarak ana oturumu kullanır.
  * `--ttl <ms>` milisaniye cinsinden pozitif bir izin TTL'si ister. Gateway kendi üst sınırını uygular.
  * `--bin <path>` Claude Code ikilisini seçer. Varsayılan değer `claude` şeklindedir.
  * `--print-config` geçici `.mcp.json` dosyasını yazar, başlatma komutunu ve env değerlerini yazdırır ve izni TTL süresi dolana kadar etkin bırakır.


Taşıyıcı token, argv üzerinden değil ortam değişkenleri üzerinden aktarılır. OpenClaw, Claude Code'u `--strict-mcp-config --mcp-config <path>` ile başlatır; böylece ortamdaki Claude MCP sunucuları ekli oturuma katılmaz. Normal başlatmalar, Claude Code süreci çıktığında izni iptal eder.

Ayrıca bkz.: [Gateway CLI](</tr/cli/gateway>), [MCP CLI](</tr/cli/mcp>) ve [ACP CLI](</tr/cli/acp>).

Was this useful?YesNo

Open issue