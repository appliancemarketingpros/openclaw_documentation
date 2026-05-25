---
title: Node + tsx mengalami kegagalan
source_url: https://docs.openclaw.ai/id/debug/node-issue
scraped_at: 2026-05-25
---

# Kegagalan Node + tsx "__name is not a function"

## Ringkasan

Menjalankan OpenClaw melalui Node dengan `tsx` gagal saat startup dengan:

CodeCopy code
[code]
    [openclaw] Failed to start CLI: TypeError: __name is not a function    at createSubsystemLogger (.../src/logging/subsystem.ts:203:25)    at .../src/agents/auth-profiles/constants.ts:25:20
[/code]

Ini mulai terjadi setelah skrip dev dialihkan dari Bun ke `tsx` (commit `2871657e`, 2026-01-06). Jalur runtime yang sama berfungsi dengan Bun.

## Lingkungan

  * Node: v25.x (diamati pada v25.3.0)
  * tsx: 4.21.0
  * OS: macOS (repro juga kemungkinan terjadi pada platform lain yang menjalankan Node 25)


## Repro (hanya Node)

bashCopy code
[code]
    # in repo rootnode --versionpnpm installnode --import tsx src/entry.ts status
[/code]

## Repro minimal di repo

bashCopy code
[code]
    node --import tsx scripts/repro/tsx-name-repro.ts
[/code]

## Pemeriksaan versi Node

  * Node 25.3.0: gagal
  * Node 22.22.0 (Homebrew `node@22`): gagal
  * Node 24: belum terpasang di sini; perlu verifikasi


## Catatan / hipotesis

  * `tsx` menggunakan esbuild untuk mentransformasi TS/ESM. `keepNames` milik esbuild menghasilkan helper `__name` dan membungkus definisi fungsi dengan `__name(...)`.
  * Kegagalan menunjukkan `__name` ada tetapi bukan fungsi saat runtime, yang menyiratkan helper hilang atau ditimpa untuk modul ini dalam jalur loader Node 25.
  * Masalah helper `__name` serupa telah dilaporkan pada konsumen esbuild lain ketika helper hilang atau ditulis ulang.


## Riwayat regresi

  * `2871657e` (2026-01-06): skrip diubah dari Bun ke tsx agar Bun bersifat opsional.
  * Sebelumnya (jalur Bun), `openclaw status` dan `gateway:watch` berfungsi.


## Solusi sementara

  * Gunakan Bun untuk skrip dev (revert sementara saat ini).

  * Gunakan `tsgo` untuk pemeriksaan tipe repo, lalu jalankan output hasil build:

bashCopy code
[code]pnpm tsgonode openclaw.mjs status
[/code]

  * Catatan historis: `tsc` digunakan di sini saat men-debug masalah Node/tsx ini, tetapi lane pemeriksaan tipe repo sekarang menggunakan `tsgo`.

  * Nonaktifkan esbuild keepNames di loader TS jika memungkinkan (mencegah penyisipan helper `__name`); tsx saat ini tidak mengekspos ini.

  * Uji Node LTS (22/24) dengan `tsx` untuk melihat apakah masalah ini spesifik Node 25.


## Referensi

  * <https://opennext.js.org/cloudflare/howtos/keep_names>
  * <https://esbuild.github.io/api/#keep-names>
  * <https://github.com/evanw/esbuild/issues/1031>


## Langkah berikutnya

  * Repro pada Node 22/24 untuk mengonfirmasi regresi Node 25.
  * Uji `tsx` nightly atau pin ke versi sebelumnya jika ada regresi yang diketahui.
  * Jika tereproduksi pada Node LTS, ajukan repro minimal ke upstream dengan stack trace `__name`.


## Terkait

  * [Instal Node.js](</id/install/node>)
  * [Pemecahan masalah Gateway](</id/gateway/troubleshooting>)


Was this useful?YesNo