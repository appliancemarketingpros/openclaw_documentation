---
title: Adapter RPC
source_url: https://docs.openclaw.ai/id/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw mengintegrasikan CLI eksternal melalui JSON-RPC. Dua pola digunakan saat ini.

## Pola A: daemon HTTP (signal-cli)

  * `signal-cli` berjalan sebagai daemon dengan JSON-RPC melalui HTTP.
  * Aliran peristiwa adalah SSE (`/api/v1/events`).
  * Probe kesehatan: `/api/v1/check`.
  * OpenClaw mengelola siklus hidup saat `channels.signal.autoStart=true`.


Lihat [Signal](</id/channels/signal>) untuk penyiapan dan endpoint.

## Pola B: proses anak stdio (imsg)

  * OpenClaw menjalankan `imsg rpc` sebagai proses anak untuk [iMessage](</id/channels/imessage>).
  * JSON-RPC dibatasi baris melalui stdin/stdout (satu objek JSON per baris).
  * Tidak ada port TCP, tidak diperlukan daemon.


Metode inti yang digunakan:

  * `watch.subscribe` → notifikasi (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (probe/diagnostik)


Lihat [iMessage](</id/channels/imessage>) untuk penyiapan legacy dan pengalamatan (`chat_id` lebih disukai).

## Panduan adapter

  * Gateway mengelola proses (start/stop terkait dengan siklus hidup provider).
  * Jaga agar klien RPC tetap tangguh: timeout, mulai ulang saat keluar.
  * Lebih pilih ID stabil (misalnya, `chat_id`) daripada string tampilan.


## Terkait

  * [Protokol Gateway](</id/gateway/protocol>)


Was this useful?YesNo