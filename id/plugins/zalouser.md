---
title: Plugin pribadi Zalo
source_url: https://docs.openclaw.ai/id/plugins/zalouser
scraped_at: 2026-05-25
---

Dukungan Zalo Personal untuk OpenClaw melalui sebuah Plugin, menggunakan `zca-js` native untuk mengotomatiskan akun pengguna Zalo biasa.

## Penamaan

ID channel adalah `zalouser` untuk memperjelas bahwa ini mengotomatiskan **akun pengguna Zalo personal** (tidak resmi). Kami mempertahankan `zalo` untuk kemungkinan integrasi API resmi Zalo di masa mendatang.

## Tempat menjalankannya

Plugin ini berjalan **di dalam proses Gateway**.

Jika Anda menggunakan Gateway jarak jauh, instal/konfigurasikan di **mesin yang menjalankan Gateway** , lalu mulai ulang Gateway.

Tidak diperlukan biner CLI eksternal `zca`/`openzca`.

## Instalasi

### Opsi A: instal dari npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Gunakan paket polos untuk mengikuti tag rilis resmi saat ini. Sematkan versi yang persis hanya saat Anda membutuhkan instalasi yang dapat direproduksi.

Mulai ulang Gateway setelahnya.

### Opsi B: instal dari folder lokal (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Mulai ulang Gateway setelahnya.

## Konfigurasi

Konfigurasi channel berada di bawah `channels.zalouser` (bukan `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Alat agen

Nama alat: `zalouser`

Tindakan: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Tindakan pesan channel juga mendukung `react` untuk reaksi pesan.

## Terkait

  * [Membangun Plugin](</id/plugins/building-plugins>)
  * [ClawHub](</id/clawhub>)


Was this useful?YesNo