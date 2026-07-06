---
title: Lampirkan CLI
source_url: https://docs.openclaw.ai/id/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` meluncurkan Claude Code dengan konfigurasi MCP sementara yang ketat dan terikat ke satu sesi Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Opsi:

  * `--session <key>` mengikat grant ke sesi Gateway. Default-nya adalah sesi utama.
  * `--ttl <ms>` meminta TTL grant positif dalam milidetik. Gateway menerapkan batas atasnya sendiri.
  * `--bin <path>` memilih binary Claude Code. Default-nya adalah `claude`.
  * `--print-config` menulis `.mcp.json` sementara, mencetak perintah peluncuran dan env, serta membiarkan grant tetap aktif hingga TTL berakhir.


Token bearer diteruskan melalui variabel lingkungan, bukan argv. OpenClaw meluncurkan Claude Code dengan `--strict-mcp-config --mcp-config <path>` sehingga server Claude MCP ambient tidak bergabung ke sesi yang dilampirkan. Peluncuran normal mencabut grant saat proses Claude Code keluar.

Lihat juga: [CLI Gateway](</id/cli/gateway>), [CLI MCP](</id/cli/mcp>), dan [CLI ACP](</id/cli/acp>).

Was this useful?YesNo

Open issue