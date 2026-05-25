---
title: Platform
source_url: https://docs.openclaw.ai/id/platforms
scraped_at: 2026-05-25
---

OpenClaw inti ditulis dalam TypeScript. **Node adalah runtime yang direkomendasikan**. Bun tidak direkomendasikan untuk Gateway — ada masalah yang diketahui dengan kanal WhatsApp dan Telegram; lihat [Bun (eksperimental)](</id/install/bun>) untuk detail.

Aplikasi pendamping tersedia untuk macOS (aplikasi bilah menu) dan node seluler (iOS/Android). Aplikasi pendamping Windows dan Linux direncanakan, tetapi Gateway sudah didukung sepenuhnya saat ini. Aplikasi pendamping native untuk Windows juga direncanakan; Gateway direkomendasikan melalui WSL2.

## Pilih OS Anda

  * macOS: [macOS](</id/platforms/macos>)
  * iOS: [iOS](</id/platforms/ios>)
  * Android: [Android](</id/platforms/android>)
  * Windows: [Windows](</id/platforms/windows>)
  * Linux: [Linux](</id/platforms/linux>)


## VPS dan hosting

  * Hub VPS: [Hosting VPS](</id/vps>)
  * [Fly.io](<http://Fly.io>): [Fly.io](</id/install/fly>)
  * Hetzner (Docker): [Hetzner](</id/install/hetzner>)
  * GCP (Compute Engine): [GCP](</id/install/gcp>)
  * Azure (Linux VM): [Azure](</id/install/azure>)
  * exe.dev (VM + proxy HTTPS): [exe.dev](</id/install/exe-dev>)


## Tautan umum

  * Panduan instalasi: [Memulai](</id/start/getting-started>)
  * Runbook Gateway: [Gateway](</id/gateway>)
  * Konfigurasi Gateway: [Konfigurasi](</id/gateway/configuration>)
  * Status layanan: `openclaw gateway status`


## Instalasi layanan Gateway (CLI)

Gunakan salah satu dari ini (semuanya didukung):

  * Wizard (direkomendasikan): `openclaw onboard --install-daemon`
  * Langsung: `openclaw gateway install`
  * Alur konfigurasi: `openclaw configure` → pilih **Layanan Gateway**
  * Perbaiki/migrasikan: `openclaw doctor` (menawarkan untuk menginstal atau memperbaiki layanan)


Target layanan bergantung pada OS:

  * macOS: LaunchAgent (`ai.openclaw.gateway` atau `ai.openclaw.<profile>`; legacy `com.openclaw.*`)
  * Linux/WSL2: layanan pengguna systemd (`openclaw-gateway[-<profile>].service`)
  * Windows native: Scheduled Task (`OpenClaw Gateway` atau `OpenClaw Gateway (<profile>)`), dengan fallback item login folder Startup per pengguna jika pembuatan tugas ditolak


## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Aplikasi macOS](</id/platforms/macos>)
  * [Aplikasi iOS](</id/platforms/ios>)


Was this useful?YesNo