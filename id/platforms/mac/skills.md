---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/id/platforms/mac/skills
scraped_at: 2026-05-25
---

Aplikasi macOS menampilkan Skills OpenClaw melalui gateway; aplikasi ini tidak mem-parsing skill secara lokal.

## Sumber data

  * `skills.status` (gateway) mengembalikan semua skill beserta eligibility dan missing requirements (termasuk blok allowlist untuk skill bawaan).
  * Requirement diturunkan dari `metadata.openclaw.requires` di setiap `SKILL.md`.


## Aksi instalasi

  * `metadata.openclaw.install` menentukan opsi instalasi (brew/node/go/uv).
  * Aplikasi memanggil `skills.install` untuk menjalankan installer di host gateway.
  * Temuan `critical` dangerous-code bawaan memblokir `skills.install` secara default; temuan suspicious tetap hanya memberi peringatan. Override dangerous memang ada pada permintaan gateway, tetapi alur aplikasi default tetap fail-closed.
  * Jika setiap opsi instalasi adalah `download`, gateway menampilkan semua pilihan unduhan.
  * Jika tidak, gateway memilih satu installer yang diprioritaskan menggunakan preferensi instalasi saat ini dan binary host: Homebrew terlebih dahulu ketika `skills.install.preferBrew` diaktifkan dan `brew` ada, lalu `uv`, lalu node manager yang dikonfigurasi dari `skills.install.nodeManager`, lalu fallback berikutnya seperti `go` atau `download`.
  * Label instalasi Node mencerminkan node manager yang dikonfigurasi, termasuk `yarn`.


## Env/API key

  * Aplikasi menyimpan key di `~/.openclaw/openclaw.json` di bawah `skills.entries.<skillKey>`.
  * `skills.update` menambal `enabled`, `apiKey`, dan `env`.


## Mode remote

  * Instalasi + pembaruan konfigurasi terjadi di host gateway (bukan di Mac lokal).


## Terkait

  * [Skills](</id/tools/skills>)
  * [Aplikasi macOS](</id/platforms/macos>)


Was this useful?YesNo