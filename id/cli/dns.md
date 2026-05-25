---
title: DNS
source_url: https://docs.openclaw.ai/id/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Pembantu DNS untuk penemuan area luas (Tailscale + CoreDNS). Saat ini berfokus pada macOS + Homebrew CoreDNS.

Terkait:

  * Penemuan Gateway: [Discovery](</id/gateway/discovery>)
  * Konfigurasi penemuan area luas: [Configuration](</id/gateway/configuration>)


## Penyiapan

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Rencanakan atau terapkan penyiapan CoreDNS untuk penemuan DNS-SD unicast.

Opsi:

  * `--domain <domain>`: domain penemuan area luas (misalnya `openclaw.internal`)
  * `--apply`: instal atau perbarui konfigurasi CoreDNS dan mulai ulang layanan (memerlukan sudo; hanya macOS)


Yang ditampilkan:

  * domain penemuan yang di-resolve
  * jalur berkas zona
  * IP tailnet saat ini
  * konfigurasi penemuan `openclaw.json` yang direkomendasikan
  * nilai nameserver/domain Tailscale Split DNS yang perlu diatur


Catatan:

  * Tanpa `--apply`, perintah ini hanya menjadi pembantu perencanaan dan mencetak penyiapan yang direkomendasikan.
  * Jika `--domain` dihilangkan, OpenClaw menggunakan `discovery.wideArea.domain` dari konfigurasi.
  * `--apply` saat ini hanya mendukung macOS dan mengharapkan Homebrew CoreDNS.
  * `--apply` melakukan bootstrap berkas zona jika diperlukan, memastikan stanza impor CoreDNS ada, dan memulai ulang layanan brew `coredns`.


## Terkait

  * [Referensi CLI](</id/cli>)
  * [Discovery](</id/gateway/discovery>)


Was this useful?YesNo