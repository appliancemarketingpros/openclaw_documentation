---
title: API masuk saluran
source_url: https://docs.openclaw.ai/id/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Plugin kanal harus memodelkan jalur penerimaan dengan nomina masuk dan pesan:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

Gunakan `openclaw/plugin-sdk/channel-inbound` untuk normalisasi event masuk, pemformatan, root, dan orkestrasi. Gunakan `openclaw/plugin-sdk/channel-outbound` untuk perilaku pengiriman native, tanda terima, pengiriman persisten, dan pratinjau langsung.

## Helper Inti

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: proyeksikan fakta kanal yang telah dinormalisasi ke dalam konteks prompt/sesi. Gunakan `channelContext` untuk meneruskan metadata pengirim/percakapan milik kanal ke hook Plugin `ctx.channelContext`; perluas `PluginHookChannelSenderContext` atau `PluginHookChannelChatContext` dari subjalur ini untuk field khusus kanal.
  * `runChannelInboundEvent(...)`: jalankan ingest, klasifikasi, preflight, resolve, perekaman, dispatch, dan finalisasi untuk satu event platform masuk.
  * `dispatchChannelInboundReply(...)`: rekam dan dispatch balasan masuk yang sudah dirakit dengan adapter pengiriman.


Runtime Plugin yang diinjeksi mengekspos helper tingkat tinggi yang sama di bawah `runtime.channel.inbound.*` untuk kanal bawaan/native yang sudah menerima objek runtime.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

Dispatcher kompatibilitas harus merakit input `dispatchChannelInboundReply(...)` dan mempertahankan pengiriman platform di dalam adapter pengiriman. Jalur pengiriman baru harus mengutamakan adapter pesan dan helper pesan persisten.

## Migrasi

Alias runtime lama `runtime.channel.turn.*` telah dihapus. Gunakan:

  * `runtime.channel.inbound.run(...)` untuk event masuk mentah.
  * `runtime.channel.inbound.dispatchReply(...)` untuk konteks balasan yang sudah dirakit.
  * `runtime.channel.inbound.buildContext(...)` untuk payload konteks masuk.
  * `runtime.channel.inbound.runPreparedReply(...)` hanya untuk jalur dispatch siap pakai milik kanal yang sudah merakit closure dispatch mereka sendiri.


Kode Plugin baru tidak boleh memperkenalkan API kanal bernama `turn`. Pertahankan kosakata giliran model atau agen di dalam kode agen/provider; Plugin kanal menggunakan istilah masuk, pesan, pengiriman, dan balasan.

Was this useful?YesNo

Open issue