---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/id/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin Codex Supervisor

Awasi sesi app-server Codex dari OpenClaw.

## Distribusi

  * Paket: `@openclaw/codex-supervisor`
  * Rute instalasi: disertakan dalam OpenClaw


## Permukaan

contracts: tools

## Daftar Sesi

`codex_sessions_list` secara default hanya menampilkan sesi Codex yang dimuat. Atur `include_stored` untuk menyertakan riwayat tersimpan; Plugin menggunakan jalur daftar khusus state-DB dari app-server Codex dan membatasi hasil tersimpan hingga 200 secara default. Berikan `max_stored_sessions` untuk menurunkan atau menaikkan batas tersebut, hingga 1000.

Was this useful?YesNo

Open issue