---
title: Pengesampingan instalasi Plugin
source_url: https://docs.openclaw.ai/id/plugins/install-overrides
scraped_at: 2026-05-25
---

Override instalasi Plugin memungkinkan pemelihara menguji instalasi Plugin saat penyiapan terhadap paket npm tertentu atau tarball npm-pack lokal. Override ini hanya untuk validasi E2E dan paket. Pengguna biasa sebaiknya memasang Plugin dengan [`openclaw plugins install`](</id/cli/plugins>).

## Lingkungan

Override dinonaktifkan kecuali kedua variabel ditetapkan:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

Peta override adalah JSON yang dikunci berdasarkan id Plugin. Nilai mendukung:

  * `npm:<registry-spec>` untuk paket registry dan versi atau tag eksak
  * `npm-pack:<path.tgz>` untuk tarball lokal yang dibuat oleh `npm pack`


Jalur `npm-pack:` relatif diresolve dari direktori kerja saat ini.

## Perilaku

Ketika alur saat penyiapan meminta untuk memasang Plugin yang id-nya muncul di peta, OpenClaw menggunakan sumber override alih-alih sumber npm dari katalog, bawaan, atau default. Ini berlaku untuk onboarding dan alur lain yang menggunakan penginstal Plugin saat penyiapan bersama.

Override tetap memberlakukan id Plugin yang diharapkan. Tarball yang dipetakan ke `codex` harus memasang Plugin yang id manifestnya adalah `codex`.

Override tidak mewarisi status sumber tepercaya resmi. Bahkan ketika entri katalog biasanya merepresentasikan paket milik OpenClaw, override diperlakukan sebagai input uji yang disediakan operator.

File `.env` workspace tidak dapat mengaktifkan override instalasi. Tetapkan variabel ini di shell tepercaya, job CI, atau perintah uji jarak jauh yang meluncurkan OpenClaw.

## E2E Paket

Gunakan direktori keadaan terisolasi agar instalasi paket dan catatan instalasi tidak menyentuh keadaan OpenClaw normal Anda:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Verifikasi paket yang terpasang di bawah direktori keadaan:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Untuk E2E provider live, muat kunci API nyata dari shell tepercaya atau secret CI sebelum meluncurkan perintah uji. Jangan cetak kunci; laporkan hanya sumber dan apakah kunci tersedia.

Was this useful?YesNo