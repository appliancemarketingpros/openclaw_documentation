---
title: Jaringan
source_url: https://docs.openclaw.ai/id/network
scraped_at: 2026-05-25
---

Hub ini menautkan dokumentasi inti tentang cara OpenClaw menghubungkan, memasangkan, dan mengamankan perangkat di localhost, LAN, dan tailnet.

## Model inti

Sebagian besar operasi mengalir melalui Gateway (`openclaw gateway`), satu proses berjalan lama yang mengelola koneksi channel dan control plane WebSocket.

  * **Loopback lebih dulu** : Gateway WS secara default menggunakan `ws://127.0.0.1:18789`. Bind non-loopback memerlukan jalur autentikasi gateway yang valid: autentikasi token/kata sandi shared-secret, atau deployment `trusted-proxy` non-loopback yang dikonfigurasi dengan benar.
  * **Satu Gateway per host** direkomendasikan. Untuk isolasi, jalankan beberapa gateway dengan profil dan port terisolasi ([Beberapa Gateway](</id/gateway/multiple-gateways>)).
  * **Host canvas** disajikan pada port yang sama dengan Gateway (`/__openclaw__/canvas/`, `/__openclaw__/a2ui/`), dilindungi oleh autentikasi Gateway saat di-bind di luar loopback.
  * **Akses jarak jauh** biasanya menggunakan tunnel SSH atau VPN Tailscale ([Akses Jarak Jauh](</id/gateway/remote>)).


Referensi utama:

  * [Arsitektur Gateway](</id/concepts/architecture>)
  * [Protokol Gateway](</id/gateway/protocol>)
  * [Runbook Gateway](</id/gateway>)
  * [Permukaan web + mode bind](</id/web>)


## Pairing + identitas

  * [Ringkasan pairing (DM + node)](</id/channels/pairing>)
  * [Pairing node yang dikelola Gateway](</id/gateway/pairing>)
  * [CLI perangkat (pairing + rotasi token)](</id/cli/devices>)
  * [CLI pairing (persetujuan DM)](</id/cli/pairing>)


Kepercayaan lokal:

  * Koneksi local loopback langsung dapat disetujui otomatis untuk pairing agar UX pada host yang sama tetap lancar.
  * OpenClaw juga memiliki jalur self-connect backend/container-lokal yang sempit untuk alur helper shared-secret tepercaya.
  * Klien tailnet dan LAN, termasuk bind tailnet pada host yang sama, tetap memerlukan persetujuan pairing eksplisit.


## Discovery + transport

  * [Discovery dan transport](</id/gateway/discovery>)
  * [Bonjour / mDNS](</id/gateway/bonjour>)
  * [Akses jarak jauh (SSH)](</id/gateway/remote>)
  * [Tailscale](</id/gateway/tailscale>)


## Node + transport

  * [Ringkasan node](</id/nodes>)
  * [Protokol bridge (node legacy, historis)](</id/gateway/bridge-protocol>)
  * [Runbook node: iOS](</id/platforms/ios>)
  * [Runbook node: Android](</id/platforms/android>)


## Keamanan

  * [Ringkasan keamanan](</id/gateway/security>)
  * [Referensi konfigurasi Gateway](</id/gateway/configuration>)
  * [Pemecahan masalah](</id/gateway/troubleshooting>)
  * [Doctor](</id/gateway/doctor>)


## Terkait

  * [Runbook Gateway](</id/gateway>)
  * [Akses jarak jauh](</id/gateway/remote>)


Was this useful?YesNo