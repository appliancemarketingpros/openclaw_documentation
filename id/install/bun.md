---
title: Bun (eksperimental)
source_url: https://docs.openclaw.ai/id/install/bun
scraped_at: 2026-05-25
---

Bun adalah runtime lokal opsional untuk menjalankan TypeScript secara langsung (`bun run ...`, `bun --watch ...`). Manajer paket bawaan tetap `pnpm`, yang didukung penuh dan digunakan oleh tooling docs. Bun tidak dapat menggunakan `pnpm-lock.yaml` dan akan mengabaikannya.

## Instal

* ### Instal dependensi

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` diabaikan oleh git, sehingga tidak ada churn repo. Untuk sepenuhnya melewati penulisan lockfile:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build dan uji

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Skrip siklus hidup

Bun memblokir skrip siklus hidup dependensi kecuali dipercaya secara eksplisit. Untuk repo ini, skrip yang umum diblokir tidak diperlukan:

  * `baileys` `preinstall` \-- memeriksa versi mayor Node >= 20 (OpenClaw secara bawaan menggunakan Node 24 dan masih mendukung Node 22 LTS, saat ini `22.16+`)
  * `protobufjs` `postinstall` \-- mengeluarkan peringatan tentang skema versi yang tidak kompatibel (tidak ada artefak build)


Jika Anda mengalami masalah runtime yang memerlukan skrip ini, percayai secara eksplisit:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Catatan

Beberapa skrip masih meng-hardcode pnpm (misalnya `docs:build`, `ui:*`, `protocol:check`). Jalankan skrip tersebut melalui pnpm untuk saat ini.

## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Node.js](</id/install/node>)
  * [Memperbarui](</id/install/updating>)


Was this useful?YesNo