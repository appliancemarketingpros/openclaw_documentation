---
title: Taksonomi kematangan
source_url: https://docs.openclaw.ai/id/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Taksonomi kematangan

model di balik kartu skor

Permukaan > kategori > kemampuan > bukti.

50 permukaan dikelompokkan ke dalam 4 keluarga, dengan setiap kategori ditautkan kembali ke dokumen kanonis dan ID cakupan QA.

Jelajahi area produk / Buka taksonomi terperinci / [Lihat skor](</id/maturity/scorecard>)

## Cara membaca halaman ini

Permukaan adalah area produk seperti runtime Gateway, Discord, atau aplikasi macOS. Setiap permukaan berisi kategori, dan setiap kategori berisi pemeriksaan tingkat kemampuan yang dicakup oleh skenario QA. Gunakan kartu skor untuk penilaian tingkat rilis; gunakan halaman ini untuk memeriksa model di baliknya.

## Tingkat kematangan

M0DirencanakanArahnya sudah diketahui, tetapi belum ada jalur pengguna yang didukung.Promosi: Isu desain, pemilik, dan permukaan target tersedia.

M1EksperimentalDiimplementasikan dengan catatan, flag, build sumber, atau alur khusus maintainer.Promosi: Maintainer dapat menjalankan skenario dari main saat ini.

M2AlphaPengguna nyata dapat mencobanya, tetapi perubahan yang merusak dan UX yang belum lengkap masih diperkirakan.Promosi: Penyiapan terdokumentasi, pengujian dasar, catatan yang diketahui, dan setidaknya satu bukti lingkungan nyata.

M3BetaJalur publik tersedia dan alur kerja utama dapat digunakan dengan catatan terbatas.Promosi: Dokumen instal/perbarui, pengujian regresi, runbook dukungan, dan bukti skenario yang berhasil di seluruh lingkungan yang diharapkan.

M4StabilJalur yang direkomendasikan untuk pengguna normal. Kegagalan diperlakukan sebagai regresi.Promosi: Gate rilis, jalur doctor/pemecahan masalah, dokumen luas, dan bukti dunia nyata yang berulang.

M5ClawesomeMatang, menyenangkan, terinstrumentasi dengan baik, dan kompetitif dengan alur kerja sebanding yang terbaik.Promosi: Stabil ditambah kelulusan kartu skor pengguna di seluruh pengguna representatif.

## Area produk

### Core

CLI M4Stabil7 area - 90% selesai Runtime Gateway M4Stabil13 area - 89% selesai Runtime Agen M3Beta9 area - 79% selesai Sesi, memori, dan mesin konteks M3Beta9 area - 79% selesai Kerangka kerja channel M3Beta8 area - 79% selesai Observabilitas M3Beta5 area - 79% selesai Aplikasi Web Gateway M3Beta6 area - 79% selesai Plugin M3Beta9 area - 79% selesai Keamanan, autentikasi, pemasangan, dan rahasia M3Beta6 area - 79% selesai Automasi: Cron, kait, tugas, polling M3Beta6 area - 79% selesai Pemahaman media dan pembuatan media M2Alfa6 area - 68% selesai Suara dan percakapan waktu nyata M2Alfa6 area - 68% selesai TUI M2Alfa5 area - 66% selesai ClawHub M2Alfa4 area - 62% selesai OpenClaw App SDK M2Alfa6 area - 53% selesai

### Platform

host Gateway Linux M4Stabil5 area - 89% selesai host Gateway macOS M4Stabil7 area - 88% selesai Hosting Docker dan Podman M3Beta4 area - 79% selesai Windows melalui WSL2 M3Beta6 area - 79% selesai Raspberry Pi dan perangkat Linux kecil M3Beta4 area - 79% selesai aplikasi pendamping macOS M3Beta8 area - 78% selesai aplikasi Android M2Alfa7 area - 66% selesai Windows Native M2Alfa4 area - 66% selesai Hosting Kubernetes M2Alfa4 area - 61% selesai Aplikasi iOS M1Eksperimental8 area - 44% selesai Jalur instalasi Nix M1Eksperimental5 area - 44% selesai Permukaan pendamping watchOS M1Eksperimental5 area - 44% selesai Aplikasi pendamping Linux M0Direncanakan5 area - 21% selesai Aplikasi pendamping Windows Native M0Direncanakan5 area - 21% selesai

### Kanal

Discord M4Stabil6 area - 87% selesai Telegram M3Beta5 area - 78% selesai Slack M3Beta5 area - 78% selesai iMessage dan BlueBubbles M3Beta5 area - 78% selesai WhatsApp M3Beta5 area - 78% selesai Matrix M2Alfa6 area - 67% selesai Google Chat M2Alfa5 area - 66% selesai Microsoft Teams M2Alfa5 area - 66% selesai Signal M2Alfa5 area - 66% selesai Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, kanal regional M2Alfa4 area - 58% selesai Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alfa4 area - 54% selesai Kanal Panggilan Suara M1Eksperimental5 area - 44% selesai

### Penyedia dan alat

Alat otomatisasi browser, exec, dan sandbox M3Beta3 area - 79% selesai Jalur penyedia OpenAI dan Codex M3Beta5 area - 79% selesai Alat pencarian web M3Beta4 area - 79% selesai Jalur penyedia Anthropic M3Beta5 area - 78% selesai Jalur penyedia Google M3Beta5 area - 78% selesai Jalur penyedia OpenRouter M3Beta4 area - 78% selesai Alat pembuatan gambar, video, dan musik M2Alfa5 area - 68% selesai Penyedia model lokal: Ollama, vLLM, SGLang, LM Studio M2Alfa5 area - 68% selesai Penyedia terhosting ekor panjang M2Alfa3 area - 68% selesai

## Detail

### Inti

CLI - M4 Stabil - 7 area

Jalur penyiapan dan perbaikan normal didokumentasikan di seluruh dokumentasi instalasi, CLI, dan Gateway. Jalur khusus platform Windows dilacak dalam baris Windows melalui WSL2 dan Windows Native.

Cakupan Eksperimental - 4%Kualitas Stabil - 83%Kelengkapan Stabil - 90%Parsial - 6

Penyiapan CLI 6 kapabilitas / didukung LTS

Eksperimental17%

Stabil89%

Stabil90%

[Indeks](</id/install>), [Penginstal](</id/install/installer>), [Node](</id/install/node>), [Memperbarui](</id/install/updating>)

Penyiapan Onboarding dan Autentikasi 5 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Onboard](</id/cli/onboard>), [Konfigurasi](</id/cli/configure>), [Ikhtisar Onboarding](</id/start/onboarding-overview>)

Penyiapan Plugin dan Kanal 5 kapabilitas

Eksperimental0%

Beta75%

Stabil89%

[Onboard](</id/cli/onboard>), [Plugin](</id/cli/plugins>), [Kanal](</id/cli/channels>)

Manajemen Layanan Gateway 5 kapabilitas / didukung LTS

Eksperimental14%

Stabil87%

Stabil90%

[Gateway](</id/cli/gateway>), [Memperbarui](</id/install/updating>), [Pemecahan Masalah](</id/gateway/troubleshooting>)

Observabilitas CLI 5 kapabilitas / didukung LTS

Eksperimental0%

Stabil89%

Stabil90%

[Status](</id/cli/status>), [Kesehatan](</id/cli/health>), [Log](</id/cli/logs>), [Diagnostik](</id/gateway/diagnostics>)

Doctor 10 kapabilitas / didukung LTS

Eksperimental0%

Stabil89%

Stabil90%

[Doctor](</id/cli/doctor>), [Doctor](</id/gateway/doctor>), [Rahasia](</id/gateway/secrets>), [Pemecahan Masalah](</id/gateway/troubleshooting>)

Pembaruan dan Peningkatan 5 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Memperbarui](</id/install/updating>), [Pembaruan](</id/cli/update>), [Pemecahan Masalah](</id/gateway/troubleshooting>)

Runtime Gateway - M4 Stabil - 13 area

Arsitektur inti, autentikasi, pemasangan, dokumen protokol, dokumen daemon, dan runbook CLI luas dan mutakhir.

Cakupan Eksperimental - 6%Kualitas Stabil - 81%Kelengkapan Stabil - 89%Sebagian - 12

Persetujuan dan Eksekusi Jarak Jauh 6 kemampuan / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Protokol](</id/gateway/protocol>), [Indeks](</id/gateway/security>)

API HTTP 4 kemampuan / didukung LTS

Eksperimental25%

Stabil90%

Stabil90%

[Indeks](</id/gateway>), [API HTTP Openai](</id/gateway/openai-http-api>), [API HTTP Openresponses](</id/gateway/openresponses-http-api>), [API HTTP Pemanggilan Tools](</id/gateway/tools-invoke-http-api>), [Hook](</id/automation/hooks>), [Indeks](</id/web>)

Permukaan Web yang Dihosting 4 kemampuan / didukung LTS

Eksperimental0%

Stabil89%

Stabil90%

[Indeks](</id/gateway>), [Arsitektur](</id/concepts/architecture>), [UI Kontrol](</id/web/control-ui>), [Webchat](</id/web/webchat>), [Canvas](</id/refactor/canvas>)

API RPC Gateway dan Peristiwa 20 kemampuan / didukung LTS

Eksperimental9%

Stabil90%

Stabil90%

[Protokol](</id/gateway/protocol>), [Indeks](</id/gateway>), [Arsitektur](</id/concepts/architecture>)

Autentikasi dan Penyandingan Perangkat 10 kemampuan / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Protokol](</id/gateway/protocol>), [Penyandingan](</id/gateway/pairing>), [Indeks](</id/gateway/security>)

Akses dan Penemuan Jaringan 6 kemampuan / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Indeks](</id/gateway>), [Penemuan](</id/gateway/discovery>), [Protokol](</id/gateway/protocol>)

Node dan Kemampuan Jarak Jauh 8 kemampuan

Eksperimental0%

Beta75%

Stabil89%

[Protokol](</id/gateway/protocol>), [Arsitektur](</id/concepts/architecture>), [Indeks](</id/nodes>)

Kesehatan, Diagnostik, dan Perbaikan 7 kemampuan / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Indeks](</id/gateway>), [Diagnostik](</id/gateway/diagnostics>), [Doctor](</id/gateway/doctor>)

Kompatibilitas Protokol 7 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Protokol](</id/gateway/protocol>), [Arsitektur](</id/concepts/architecture>), [Typebox](</id/concepts/typebox>), [Protokol Bridge](</id/gateway/bridge-protocol>)

Peran dan Izin 5 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Protokol](</id/gateway/protocol>), [Indeks](</id/gateway/security>)

Siklus Hidup Gateway 7 kapabilitas / didukung LTS

Eksperimental33%

Stabil90%

Stabil90%

[Indeks](</id/gateway>), [Arsitektur](</id/concepts/architecture>)

Kontrol Keamanan 6 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Indeks](</id/gateway/security>), [Protokol](</id/gateway/protocol>), [Penemuan](</id/gateway/discovery>)

Koneksi WebSocket 8 kapabilitas / didukung LTS

Eksperimental13%

Stabil90%

Stabil90%

[Protokol](</id/gateway/protocol>), [Arsitektur](</id/concepts/architecture>)

Runtime Agen - M3 Beta - 9 area

Loop utama, model, perutean penyedia, dan streaming alat adalah fitur kelas satu, tetapi perilaku penyedia berubah setiap minggu dan membutuhkan bukti skenario per rilis.

Cakupan Eksperimental - 33%Kualitas Beta - 78%Kelengkapan Beta - 79%Sebagian - 6

Eksekusi Giliran Agen 3 kapabilitas / didukung LTS

Eksperimental29%

Beta79%

Beta79%

[Loop Agen](</id/concepts/agent-loop>), [Agen](</id/cli/agent>), [Runtime Agen](</id/concepts/agent-runtimes>)

Runtime Eksternal dan Subagen 4 kapabilitas

Eksperimental30%

Beta79%

Beta79%

[Runtime Agen](</id/concepts/agent-runtimes>), [Anthropic](</id/providers/anthropic>), [Google](</id/providers/google>), [Subagen](</id/tools/subagents>)

Eksekusi Penyedia Terhosting 5 kapabilitas / didukung LTS

Eksperimental20%

Beta79%

Beta79%

[Openai](</id/providers/openai>), [Anthropic](</id/providers/anthropic>), [Google](</id/providers/google>), [Model](</id/concepts/models>)

Penyedia Lokal dan Dihosting Sendiri 5 kapabilitas

Eksperimental0%

Alpha68%

Beta79%

[Ollama](</id/providers/ollama>), [Model](</id/concepts/models>), [Agen](</id/cli/agent>)

Pemilihan Model dan Runtime 4 kapabilitas / didukung LTS

Eksperimental25%

Beta79%

Beta79%

[Model](</id/concepts/models>), [Model](</id/cli/models>), [Openai](</id/providers/openai>), [Runtime Agen](</id/concepts/agent-runtimes>)

Autentikasi Penyedia 10 kapabilitas / didukung LTS

Eksperimental24%

Beta79%

Beta79%

[Model](</id/concepts/models>), [Agen](</id/cli/agent>), [Model](</id/cli/models>), [Openai](</id/providers/openai>), [Anthropic](</id/providers/anthropic>), [Google](</id/providers/google>), [Subagen](</id/tools/subagents>)

Streaming dan Progres 2 kapabilitas

Alpha56%

Beta79%

Beta79%

[Streaming](</id/concepts/streaming>), [Loop Agen](</id/concepts/agent-loop>)

Panggilan Alat dan Penanganan Respons 3 kapabilitas / didukung LTS

Alpha65%

Beta79%

Beta79%

[Loop Agen](</id/concepts/agent-loop>), [Ollama](</id/providers/ollama>)

Kontrol Eksekusi Alat 6 kapabilitas / didukung LTS

Alfa50%

Beta79%

Beta79%

[Sandbox vs Kebijakan Alat vs Ditingkatkan](</id/gateway/sandbox-vs-tool-policy-vs-elevated>), [Loop Agen](</id/concepts/agent-loop>), [Subagen](</id/tools/subagents>)

Sesi, memori, dan mesin konteks - M3 Beta - 9 area

Dokumentasi kuat dan implementasi aktif. Kematangan bergantung pada ketahanan transkrip, kualitas Compaction, dan kesetaraan lintas klien.

Cakupan Eksperimental - 30%Kualitas Beta - 77%Kelengkapan Beta - 79%Sebagian - 6

Manajemen Sesi dan Transkrip CLI 2 kemampuan / didukung LTS

Eksperimental0%

Alfa68%

Beta79%

[Sesi](</id/concepts/session>), [Compaction Manajemen Sesi](</id/reference/session-management-compaction>), [Sesi](</id/cli/sessions>)

Manajemen Token 3 kemampuan / didukung LTS

Eksperimental20%

Beta79%

Beta79%

[Compaction](</id/concepts/compaction>), [Konteks](</id/concepts/context>), [Compaction Manajemen Sesi](</id/reference/session-management-compaction>)

Mesin Konteks 2 kemampuan / didukung LTS

Alfa57%

Beta79%

Beta79%

[Konteks](</id/concepts/context>), [Mesin Konteks](</id/concepts/context-engine>), [Harness Mesin Konteks Codex](</id/plan/codex-context-engine-harness>)

Riwayat Lintas Klien dan Kesetaraan Sesi 2 kemampuan

Eksperimental40%

Beta79%

Beta79%

[Webchat](</id/web/webchat>), [Android](</id/platforms/android>), [Perutean Saluran](</id/channels/channel-routing>)

Diagnostik, Pemeliharaan, dan Pemulihan 3 kemampuan

Eksperimental40%

Beta79%

Beta79%

[Diagnostik](</id/gateway/diagnostics>), [Compaction Manajemen Sesi](</id/reference/session-management-compaction>), [Flag](</id/diagnostics/flags>)

Prompt dan Konteks Inti 2 kemampuan / didukung LTS

Eksperimental38%

Beta79%

Beta79%

[Konteks](</id/concepts/context>), [Kebersihan Transkrip](</id/reference/transcript-hygiene>), [Discord](</id/channels/discord>)

Memori 5 kemampuan

Eksperimental46%

Beta79%

Beta79%

[Konfigurasi Memori](</id/reference/memory-config>), [Qmd Memori](</id/concepts/memory-qmd>), [Memori](</id/concepts/memory>), [Discord](</id/channels/discord>)

Perutean Sesi 2 kemampuan / didukung LTS

Eksperimental25%

Beta79%

Beta79%

[Sesi](</id/concepts/session>), [Perutean Saluran](</id/channels/channel-routing>), [Discord](</id/channels/discord>)

Persistensi Transkrip 2 kemampuan / didukung LTS

Eksperimental0%

Alfa68%

Beta79%

[Manajemen Sesi Compaction](</id/reference/session-management-compaction>), [Higiene Transkrip](</id/reference/transcript-hygiene>)

Kerangka kerja saluran - M3 Beta - 8 area

Banyak channel berbagi kontrak pengiriman dan perutean Gateway, tetapi perilaku channel bervariasi menurut API upstream dan batasan kebijakan akun.

Cakupan Eksperimental - 13%Kualitas Beta - 76%Kelengkapan Beta - 79%Parsial - 5

Perintah dan Persetujuan Tindakan Channel 5 kapabilitas

Eksperimental0%

Beta79%

Beta79%

[Grup](</id/channels/groups>), [Discord](</id/channels/discord>), [Google Chat](</id/channels/googlechat>), [Signal](</id/channels/signal>), [Matrix](</id/channels/matrix>)

Penyiapan Channel 5 kapabilitas / didukung LTS

Eksperimental14%

Beta79%

Beta79%

[Indeks](</id/channels>), [Penyandingan](</id/channels/pairing>), [Pemecahan Masalah](</id/channels/troubleshooting>), [Plugin Channel SDK](</id/plugins/sdk-channel-plugins>)

Perilaku Thread Grup dan Ruang Sekitar 5 kapabilitas

Eksperimental36%

Beta79%

Beta79%

[Grup](</id/channels/groups>), [Pesan Grup](</id/channels/group-messages>), [Peristiwa Ruang Sekitar](</id/channels/ambient-room-events>), [Grup Siaran](</id/channels/broadcast-groups>), [Discord](</id/channels/discord>)

Gerbang Akses Masuk dan Identitas 5 kapabilitas / didukung LTS

Eksperimental0%

Alpha68%

Beta79%

[Grup Akses](</id/channels/access-groups>), [Grup](</id/channels/groups>), [Discord](</id/channels/discord>), [LINE](</id/channels/line>)

Lampiran Media dan Data Channel Kaya 4 kapabilitas

Eksperimental0%

Alpha68%

Beta79%

[LINE](</id/channels/line>), [Signal](</id/channels/signal>), [Google Chat](</id/channels/googlechat>), [Matrix](</id/channels/matrix>), [Discord](</id/channels/discord>)

Pengiriman Keluar dan Pipeline Balasan 4 kapabilitas / didukung LTS

Eksperimental38%

Beta79%

Beta79%

[Grup](</id/channels/groups>), [Peristiwa Ruang Sekitar](</id/channels/ambient-room-events>), [Discord](</id/channels/discord>), [Matrix](</id/channels/matrix>), [Channel Konfigurasi](</id/gateway/config-channels>)

Perutean dan Pengiriman Percakapan 10 kapabilitas / didukung LTS

Eksperimental19%

Beta79%

Beta79%

[Perutean Channel](</id/channels/channel-routing>), [Grup](</id/channels/groups>), [Discord](</id/channels/discord>), [Matrix](</id/channels/matrix>), [Pemecahan Masalah](</id/channels/troubleshooting>), [Referensi Konfigurasi](</id/gateway/configuration-reference>)

Kesehatan Status dan Kontrol Operator 4 kapabilitas / didukung LTS

Eksperimental0%

Beta79%

Beta79%

[Kesehatan](</id/gateway/health>), [Referensi Konfigurasi](</id/gateway/configuration-reference>), [Pemecahan Masalah](</id/channels/troubleshooting>), [Discord](</id/channels/discord>)

Observabilitas - Beta M3 - 5 area

Dokumentasi OTel, Prometheus, pencatatan log, dan diagnostik sudah ada. Memerlukan peninjauan kematangan publik tentang "apa yang harus dilihat operator terlebih dahulu".

Cakupan Eksperimental - 18%Kualitas Beta - 75%Kelengkapan Beta - 79%Parsial - 3

Kesehatan dan Perbaikan 12 kemampuan / didukung LTS

Eksperimental28%

Beta79%

Beta79%

[Kesehatan](</id/gateway/health>), [Telegram](</id/channels/telegram>), [Doctor](</id/cli/doctor>), [Doctor](</id/gateway/doctor>), [Subpath Sdk](</id/plugins/sdk-subpaths>), [Kesehatan](</id/cli/health>), [Protokol](</id/gateway/protocol>)

Pencatatan log 5 kemampuan / didukung LTS

Eksperimental0%

Alpha68%

Beta79%

[Pencatatan log](</id/logging>), [Pencatatan log](</id/gateway/logging>), [Log](</id/cli/logs>)

Pengumpulan Diagnostik 8 kemampuan

Eksperimental30%

Beta79%

Beta79%

[Diagnostik](</id/gateway/diagnostics>), [Kesehatan](</id/gateway/health>), [Harness Codex](</id/plugins/codex-harness>), [Protokol](</id/gateway/protocol>)

Ekspor Telemetri 13 kemampuan

Eksperimental33%

Beta79%

Beta79%

[Hook](</id/plugins/hooks>), [Opentelemetry](</id/gateway/opentelemetry>), [Pencatatan log](</id/logging>), [Subpath Sdk](</id/plugins/sdk-subpaths>), [Diagnostics Otel](</id/plugins/reference/diagnostics-otel>), [Prometheus](</id/gateway/prometheus>), [Diagnostics Prometheus](</id/plugins/reference/diagnostics-prometheus>)

Diagnostik Sesi 4 kemampuan / didukung LTS

Eksperimental0%

Alpha68%

Beta79%

[Opentelemetry](</id/gateway/opentelemetry>), [Prometheus](</id/gateway/prometheus>), [Diagnostik](</id/gateway/diagnostics>), [Protokol](</id/gateway/protocol>)

Aplikasi Web Gateway - M3 Beta - 6 area

UI Web didokumentasikan dengan alur penyandingan, chat, PWA, Talk, push, dan Gateway jarak jauh. Promosikan setelah scorecard lintas browser dan PWA seluler.

Cakupan Eksperimental - 4%Kualitas Beta - 74%Kelengkapan Beta - 79%Tidak ada

Percakapan Realtime Browser 5 kapabilitas

Eksperimental0%

Alpha68%

Beta79%

[UI Kontrol](</id/web/control-ui>), [Protokol](</id/gateway/protocol>), [Percakapan](</id/nodes/talk>)

Akses dan Kepercayaan Browser 5 kapabilitas

Eksperimental0%

Alpha68%

Beta79%

[UI Kontrol](</id/web/control-ui>), [Dasbor](</id/web/dashboard>), [Tailscale](</id/gateway/tailscale>), [Jarak Jauh](</id/gateway/remote>)

Konfigurasi 5 kapabilitas

Eksperimental0%

Alpha68%

Beta79%

[UI Kontrol](</id/web/control-ui>), [Konfigurasi](</id/gateway/configuration>)

UI Browser 10 kapabilitas

Eksperimental8%

Beta79%

Beta79%

[UI Kontrol](</id/web/control-ui>), [Indeks](</id/web>), [Dasbor](</id/web/dashboard>), [Protokol](</id/gateway/protocol>)

Percakapan WebChat 15 kapabilitas

Eksperimental10%

Beta79%

Beta79%

[UI Kontrol](</id/web/control-ui>), [Webchat](</id/web/webchat>), [Memulai](</id/start/getting-started>), [Perutean Channel](</id/channels/channel-routing>), [Operasi File Aman](</id/gateway/security/secure-file-operations>)

Konsol Operator 10 kapabilitas

Eksperimental8%

Beta79%

Beta79%

[UI Kontrol](</id/web/control-ui>), [Kesehatan](</id/gateway/health>), [Protokol](</id/gateway/protocol>), [Dasbor](</id/web/dashboard>)

Plugin - M3 Beta - 9 area

Dokumentasi luas dan bukti runtime internal yang kuat tersedia di seluruh manifes, penemuan, pemuatan, arsitektur penyedia/alat, dan batas persetujuan. Pertahankan baris ini pada beta hingga bukti API/subpath SDK publik dan distribusi eksternal lebih kuat.

Cakupan Eksperimental - 12%Kualitas Beta - 72%Kelengkapan Beta - 79%Parsial - 7

Pembuatan dan Pengemasan Plugin 8 kapabilitas / didukung LTS

Eksperimental0%

Alfa68%

Beta79%

[Membangun Plugin](</id/plugins/building-plugins>), [Ikhtisar SDK](</id/plugins/sdk-overview>), [Titik Masuk SDK](</id/plugins/sdk-entrypoints>), [Subjalur SDK](</id/plugins/sdk-subpaths>), [Manifest](</id/plugins/manifest>), [Referensi](</id/plugins/reference>)

Plugin bawaan 5 kapabilitas / didukung LTS

Eksperimental0%

Alfa68%

Beta79%

[Inventaris Plugin](</id/plugins/plugin-inventory>), [Plugin](</id/cli/plugins>), [Internal Arsitektur](</id/plugins/architecture-internals>)

Plugin Canvas 6 kapabilitas

Eksperimental0%

Alfa68%

Beta79%

[Canvas](</id/plugins/reference/canvas>), [Canvas](</id/refactor/canvas>), [Referensi Konfigurasi](</id/gateway/configuration-reference>)

Menginstal dan menjalankan Plugin 6 kapabilitas / didukung LTS

Eksperimental35%

Beta79%

Beta79%

[Arsitektur](</id/plugins/architecture>), [Internal Arsitektur](</id/plugins/architecture-internals>), [Plugin](</id/cli/plugins>)

Plugin saluran 5 kapabilitas / didukung LTS

Eksperimental0%

Alfa68%

Beta79%

[Plugin Saluran SDK](</id/plugins/sdk-channel-plugins>), [Masuk Saluran SDK](</id/plugins/sdk-channel-inbound>), [Keluar Saluran SDK](</id/plugins/sdk-channel-outbound>)

Plugin penyedia dan alat 6 kapabilitas / didukung LTS

Eksperimental43%

Beta79%

Beta79%

[Plugin Penyedia SDK](</id/plugins/sdk-provider-plugins>), [Plugin Alat](</id/plugins/tool-plugins>), [Menambahkan Kapabilitas](</id/plugins/adding-capabilities>)

Persetujuan Plugin 6 kapabilitas / didukung LTS

Eksperimental0%

Alfa68%

Beta79%

[Permintaan Izin Plugin](</id/plugins/plugin-permission-requests>), [Persetujuan Exec](</id/tools/exec-approvals>), [Plugin Saluran SDK](</id/plugins/sdk-channel-plugins>)

Menerbitkan Plugin 6 kapabilitas / didukung LTS

Eksperimental0%

Alfa68%

Beta79%

[Plugin](</id/cli/plugins>), [Kompatibilitas](</id/plugins/compatibility>), [Penerbitan](</id/clawhub/publishing>)

Menguji Plugin 6 kemampuan

Eksperimental27%

Beta79%

Beta79%

[Pengujian SDK](</id/plugins/sdk-testing>), [Penyiapan SDK](</id/plugins/sdk-setup>), [Perangkat Uji Codex](</id/plugins/codex-harness>)

Keamanan, autentikasi, pairing, dan rahasia - M3 Beta - 6 area

Dokumentasi yang baik dan permukaan penguatan sudah tersedia. Promosikan setelah skenario peningkatan dan keamanan rutin membuktikan tidak ada regresi penyiapan.

Cakupan Eksperimental - 16%Kualitas Beta - 72%Kelengkapan Beta - 79%Parsial - 5

Kebijakan Persetujuan dan Perlindungan Alat 2 kemampuan / didukung LTS

Alpha50%

Beta79%

Beta79%

[Persetujuan Exec](</id/tools/exec-approvals>), [Persetujuan](</id/cli/approvals>), [Permintaan Izin Plugin](</id/plugins/plugin-permission-requests>), [Pemeriksaan Audit](</id/gateway/security/audit-checks>)

Autentikasi Gateway dan Akses Jarak Jauh 9 kemampuan / didukung LTS

Eksperimental0%

Alpha68%

Beta79%

[Indeks](</id/gateway/security>), [Runbook Eksposur](</id/gateway/security/exposure-runbook>), [Autentikasi Proksi Tepercaya](</id/gateway/trusted-proxy-auth>), [Tailscale](</id/gateway/tailscale>), [Jarak Jauh](</id/gateway/remote>), [Referensi Konfigurasi](</id/gateway/configuration-reference>), [Gateway](</id/cli/gateway>), [Doctor](</id/cli/doctor>), [UI Kontrol](</id/web/control-ui>), [Kontrol Browser](</id/tools/browser-control>), [Pemeriksaan Audit](</id/gateway/security/audit-checks>)

Kontrol Akses Kanal 3 kemampuan / didukung LTS

Eksperimental0%

Alpha68%

Beta79%

[Pairing](</id/channels/pairing>), [Telegram](</id/channels/telegram>), [Grup Akses](</id/channels/access-groups>), [Pemeriksaan Audit](</id/gateway/security/audit-checks>)

Pairing Perangkat dan Node 11 kemampuan / didukung LTS

Eksperimental0%

Alpha68%

Beta79%

[Protokol](</id/gateway/protocol>), [Perangkat](</id/cli/devices>), [Pairing](</id/channels/pairing>), [Pairing](</id/gateway/pairing>), [Cakupan Operator](</id/gateway/operator-scopes>), [UI Kontrol](</id/web/control-ui>), [Obrolan Web](</id/web/webchat>), [Persetujuan](</id/cli/approvals>)

Kepercayaan Plugin 2 kemampuan

Eksperimental0%

Alpha68%

Beta79%

[Manifest](</id/plugins/manifest>), [Permintaan Izin Plugin](</id/plugins/plugin-permission-requests>), [Kelola Plugin](</id/plugins/manage-plugins>), [Pemeriksaan Audit](</id/gateway/security/audit-checks>)

Kebersihan Kredensial dan Rahasia 5 kemampuan / didukung LTS

Eksperimental46%

Beta79%

Beta79%

[Autentikasi](</id/gateway/authentication>), [Model](</id/cli/models>), [Openai](</id/providers/openai>), [OAuth](</id/concepts/oauth>), [Rahasia](</id/gateway/secrets>), [Rahasia](</id/cli/secrets>), [Permukaan Kredensial Secretref](</id/reference/secretref-credential-surface>), [Pemeriksaan Audit](</id/gateway/security/audit-checks>)

Otomasi: cron, hook, tugas, polling - M3 Beta - 6 area

Terdokumentasi dan dapat digunakan, tetapi bukti skenario harus mencakup pengiriman tanpa pengawasan, percobaan ulang, dan visibilitas kegagalan.

Cakupan Eksperimental - 2%Kualitas Beta - 72%Kelengkapan Beta - 79%Tidak ada

Pekerjaan Cron 15 kemampuan

Eksperimental0%

Beta79%

Beta79%

[Pekerjaan Cron](</id/automation/cron-jobs>), [Cron](</id/cli/cron>), [Protokol](</id/gateway/protocol>), [Tugas](</id/automation/tasks>), [Discord](</id/channels/discord>)

Ingress Peristiwa 15 kemampuan

Eksperimental0%

Alpha68%

Beta79%

[Telegram](</id/channels/telegram>), [Zalo](</id/channels/zalo>), [Pemecahan Masalah](</id/channels/troubleshooting>), [iMessage dari Bluebubbles](</id/channels/imessage-from-bluebubbles>), [Integrasi Gmail Pubsub](</id/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</id/automation/cron-jobs>), [Webhook](</id/cli/webhooks>), [Webhook](</id/automation/cron-jobs#webhooks>), [Webhook](</id/automation/cron-jobs>)

Hook Otomatisasi 11 kemampuan

Eksperimental0%

Alpha68%

Beta79%

[Hook](</id/automation/hooks>), [Hook](</id/cli/hooks>), [Hook](</id/plugins/hooks>), [Permintaan Izin Plugin](</id/plugins/plugin-permission-requests>), [Subpath SDK](</id/plugins/sdk-subpaths>)

Tugas dan Alur Latar Belakang 10 kemampuan

Eksperimental0%

Alpha68%

Beta79%

[Tugas](</id/automation/tasks>), [Indeks](</id/automation>), [Tugas](</id/cli/tasks>), [TaskFlow](</id/automation/taskflow>), [Runtime SDK](</id/plugins/sdk-runtime>)

Heartbeat 5 kemampuan

Eksperimental14%

Beta79%

Beta79%

[Indeks](</id/automation>), [Heartbeat](</id/gateway/heartbeat>), [Komitmen](</id/concepts/commitments>)

Kontrol Polling 10 kemampuan

Eksperimental0%

Alpha68%

Beta79%

[Polling](</id/cli/message>), [Pesan](</id/cli/message>), [Telegram](</id/channels/telegram>), [Msteams](</id/channels/msteams>), [Proses Latar Belakang](</id/gateway/background-process>)

Pemahaman media dan pembuatan media - M2 Alpha - 6 area

Permukaan kemampuan yang luas sudah tersedia, tetapi variasi penyedia, batas file, dan paritas node/aplikasi membuatnya belum stabil.

Cakupan Eksperimental - 2%Kualitas Alpha - 64%Kelengkapan Alpha - 68%Tidak ada

Asupan dan Akses Media 8 kemampuan

Eksperimental0%

Alfa61%

Alfa68%

[Ikhtisar Media](</id/tools/media-overview>), [Pemahaman Media](</id/nodes/media-understanding>), [Operasi File Aman](</id/gateway/security/secure-file-operations>), [PDF](</id/tools/pdf>), [Pembuatan Gambar](</id/tools/image-generation>), [QR](</id/cli/qr>), [LINE](</id/channels/line>), [WhatsApp](</id/channels/whatsapp>)

Penanganan Media Kanal 5 kemampuan

Eksperimental0%

Alfa61%

Alfa68%

[Gambar](</id/nodes/images>), [Ikhtisar Media](</id/tools/media-overview>), [Discord](</id/channels/discord>)

Konfigurasi Media 1 kemampuan

Eksperimental0%

Alfa61%

Alfa68%

[Ikhtisar Media](</id/tools/media-overview>), [Pembuatan Gambar](</id/tools/image-generation>), [Manifest](</id/plugins/manifest>), [Harness Codex](</id/plugins/codex-harness>)

Pengiriman Teks-ke-Ucapan 2 kemampuan

Eksperimental0%

Alfa61%

Alfa68%

[TTS](</id/tools/tts>), [Ikhtisar Media](</id/tools/media-overview>), [Discord](</id/channels/discord>)

Pemahaman Media 12 kemampuan

Eksperimental7%

Alfa69%

Alfa69%

[Audio](</id/nodes/audio>), [Pemahaman Media](</id/nodes/media-understanding>), [Ikhtisar Media](</id/tools/media-overview>), [WhatsApp](</id/channels/whatsapp>), [Gambar](</id/nodes/images>), [Infer](</id/cli/infer>), [PDF](</id/tools/pdf>)

Pembuatan Media 17 kemampuan

Eksperimental5%

Alfa69%

Alfa69%

[Pembuatan Gambar](</id/tools/image-generation>), [Ikhtisar Media](</id/tools/media-overview>), [Skills](</id/tools/skills>), [Pembuatan Musik](</id/tools/music-generation>), [Pembuatan Video](</id/tools/video-generation>)

Suara dan percakapan waktu nyata - M2 Alfa - 6 area

Ada beberapa implementasi di Control UI, aplikasi, dan penyedia. Membutuhkan kartu skor latensi, mode kegagalan, dan penyiapan sebelum beta.

Cakupan Eksperimental - 0%Kualitas Alfa - 61%Kelengkapan Alfa - 68%Tidak ada

Penyedia Bicara 7 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Openai](</id/providers/openai>), [Google](</id/providers/google>), [Plugin Penyedia SDK](</id/plugins/sdk-provider-plugins>), [Bicara](</id/nodes/talk>), [UI Kontrol](</id/web/control-ui>)

Sesi Bicara Realtime 11 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Bicara](</id/nodes/talk>), [UI Kontrol](</id/web/control-ui>)

Ucapan dan Transkripsi 5 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Bicara](</id/nodes/talk>), [Openai](</id/providers/openai>), [Google](</id/providers/google>)

Bicara Aplikasi Native 4 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Bicara](</id/nodes/talk>), [Voicewake](</id/platforms/mac/voicewake>)

Bangunkan Suara dan Perutean 4 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Voicewake](</id/nodes/voicewake>), [Voicewake](</id/platforms/mac/voicewake>), [Hamparan Suara](</id/platforms/mac/voice-overlay>)

Observabilitas Bicara 5 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[UI Kontrol](</id/web/control-ui>), [Hamparan Suara](</id/platforms/mac/voice-overlay>), [Bicara](</id/nodes/talk>)

TUI - M2 Alpha - 5 area

Ada dalam dokumentasi dan sumber, tetapi kurang terlihat sebagai alur kerja pengguna utama. Memerlukan definisi skenario yang eksplisit.

Cakupan Eksperimental - 0%Kualitas Alpha - 59%Kelengkapan Alpha - 66%Tidak Ada

Mode Runtime 14 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[TUI](</id/cli/tui>), [TUI](</id/web/tui>), [Indeks](</id/cli>)

Input dan Perintah 8 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[TUI](</id/web/tui>)

Manajemen Sesi 3 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[TUI](</id/web/tui>), [Sesi](</id/cli/sessions>)

Eksekusi Shell Lokal 4 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[TUI](</id/web/tui>), [TUI](</id/cli/tui>)

Rendering dan Keamanan Output 4 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[TUI](</id/web/tui>), [QR](</id/cli/qr>), [Log](</id/cli/logs>), [Penyelesaian](</id/cli/completion>)

ClawHub - M2 Alfa - 4 area

Dokumentasi publik dan konsep ekosistem sudah ada. Membutuhkan kartu skor instalasi, kepercayaan, pembaruan, rollback, dan kompatibilitas.

Cakupan Eksperimental - 0%Kualitas Alfa - 58%Kelengkapan Alfa - 62%Tidak ada

Penerbitan 7 kapabilitas

Eksperimental0%

Alpha54%

Alpha55%

[Penerbitan](</id/clawhub/publishing>), [Membuat Skills](</id/tools/creating-skills>), [Komunitas](</id/plugins/community>)

Penemuan Katalog 5 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Plugin](</id/tools/plugin>), [Plugin](</id/cli/plugins>), [Skills](</id/cli/skills>), [Skills](</id/tools/skills>), [Komunitas](</id/plugins/community>)

Kompatibilitas dan Kepercayaan 12 kapabilitas

Eksperimental0%

Alpha55%

Alpha56%

[Plugin](</id/tools/plugin>), [Plugin](</id/cli/plugins>), [Kompatibilitas](</id/plugins/compatibility>), [Inventaris Plugin](</id/plugins/plugin-inventory>), [Penerbitan](</id/clawhub/publishing>), [Skills](</id/tools/skills>), [Konfigurasi Skills](</id/tools/skills-config>)

Siklus Hidup dan Kesehatan Plugin 26 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Plugin](</id/tools/plugin>), [Plugin](</id/cli/plugins>), [Skills](</id/cli/skills>), [Skills](</id/tools/skills>), [Protokol](</id/gateway/protocol>), [Bundel](</id/plugins/bundles>), [Resolusi Dependensi](</id/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 area

OpenClaw App SDK adalah kontrak aplikasi eksternal tersendiri yang terpisah dari runtime Gateway dan Plugin SDK. Penilaian saat ini menunjukkan jalur `@openclaw/sdk` yang nyata dengan celah seputar pemaketan publik, penemuan otomatis, persetujuan, helper, dan kompatibilitas.

Cakupan Eksperimental - 3%Kualitas Alpha - 54%Kelengkapan Alpha - 53%Tidak Ada

API Klien 4 kemampuan

Eksperimental0%

Alfa51%

Alfa50%

[SDK OpenClaw](</id/gateway/external-apps>), [Desain API SDK OpenClaw](</id/gateway/external-apps>)

Akses Gateway 5 kemampuan

Eksperimental0%

Alfa53%

Alfa54%

[SDK OpenClaw](</id/gateway/external-apps>), [Desain API SDK OpenClaw](</id/gateway/external-apps>), [Protokol](</id/gateway/protocol>), [Indeks](</id/gateway/security>)

Percakapan Agen 6 kemampuan

Eksperimental0%

Alfa52%

Alfa52%

[SDK OpenClaw](</id/gateway/external-apps>), [Desain API SDK OpenClaw](</id/gateway/external-apps>), [Protokol](</id/gateway/protocol>)

Peristiwa dan Persetujuan 5 kemampuan

Eksperimental0%

Alfa52%

Alfa52%

[SDK OpenClaw](</id/gateway/external-apps>), [Desain API SDK OpenClaw](</id/gateway/external-apps>), [Protokol](</id/gateway/protocol>)

Pembantu Sumber Daya 5 kemampuan

Eksperimental17%

Alfa62%

Alfa53%

[SDK OpenClaw](</id/gateway/external-apps>), [Desain API SDK OpenClaw](</id/gateway/external-apps>)

Kompatibilitas 5 kemampuan

Eksperimental0%

Alfa54%

Alfa55%

[Desain API SDK OpenClaw](</id/gateway/external-apps>), [Typebox](</id/concepts/typebox>), [Protokol](</id/gateway/protocol>)

### Platform

Linux Gateway host - M4 Stable - 5 areas

Runtime Node direkomendasikan, layanan pengguna systemd didokumentasikan, dan panduan VPS/kontainer bersifat luas.

Cakupan Eksperimental - 0%Kualitas Beta - 75%Kelengkapan Stabil - 89%Parsial - 4

Penyiapan dan Pembaruan Host 4 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Indeks](</id/install>), [Memperbarui](</id/install/updating>), [Linux](</id/platforms/linux>), [Indeks](</id/platforms>)

Runtime Gateway dan Kontrol Layanan 6 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Indeks](</id/gateway>), [Gateway](</id/cli/gateway>), [Linux](</id/platforms/linux>), [Vps](</id/vps>)

Akses Jarak Jauh dan Keamanan 6 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Jarak Jauh](</id/gateway/remote>), [Tailscale](</id/gateway/tailscale>), [Runbook Eksposur](</id/gateway/security/exposure-runbook>), [Autentikasi](</id/gateway/authentication>), [Rahasia](</id/gateway/secrets>)

Diagnostik dan Perbaikan 4 kapabilitas / didukung LTS

Eksperimental0%

Beta75%

Stabil89%

[Status](</id/cli/status>), [Log](</id/cli/logs>), [Doctor](</id/cli/doctor>), [Diagnostik](</id/gateway/diagnostics>), [Indeks](</id/gateway>)

Target Deployment 3 kapabilitas

Eksperimental0%

Beta75%

Stabil89%

[Vps](</id/vps>), [Docker](</id/install/docker>), [Hetzner](</id/install/hetzner>), [Digitalocean](</id/install/digitalocean>), [Kubernetes](</id/install/kubernetes>), [Podman](</id/install/podman>)

Host Gateway macOS - M4 Stabil - 7 area

Jalur layanan LaunchAgent, mode Gateway lokal/jarak jauh, instalasi CLI, dan integrasi aplikasi didokumentasikan.

Cakupan Eksperimental - 0%Kualitas Beta - 74%Kelengkapan Stabil - 88%Tidak ada

Penyiapan CLI 4 kemampuan

Eksperimental0%

Beta74%

Stabil88%

[Macos](</id/platforms/macos>), [Gateway Terbundel](</id/platforms/mac/bundled-gateway>), [Penginstal](</id/install/installer>), [Node](</id/install/node>)

Integrasi Gateway Lokal 9 kemampuan

Eksperimental0%

Beta74%

Stabil88%

[Macos](</id/platforms/macos>), [Gateway Terbundel](</id/platforms/mac/bundled-gateway>), [Jarak Jauh](</id/platforms/mac/remote>), [Indeks](</id/gateway>), [Gateway](</id/cli/gateway>), [Bonjour](</id/gateway/bonjour>)

Mode Gateway Jarak Jauh 5 kemampuan

Eksperimental0%

Beta74%

Stabil88%

[Jarak Jauh](</id/platforms/mac/remote>), [Jarak Jauh](</id/gateway/remote>), [Tailscale](</id/gateway/tailscale>)

Siklus Hidup Layanan Gateway 10 kemampuan

Eksperimental0%

Beta74%

Stabil88%

[Macos](</id/platforms/macos>), [Gateway Terbundel](</id/platforms/mac/bundled-gateway>), [Gateway](</id/cli/gateway>), [Indeks](</id/gateway>), [Pembaruan](</id/cli/update>), [Memperbarui](</id/install/updating>), [Hapus Instalasi](</id/install/uninstall>), [Pemecahan Masalah](</id/gateway/troubleshooting>)

Diagnostik dan Observabilitas 4 kemampuan

Eksperimental0%

Beta74%

Stabil88%

[Gateway Terbundel](</id/platforms/mac/bundled-gateway>), [Macos](</id/platforms/macos>), [Gateway](</id/cli/gateway>), [Dokter](</id/gateway/doctor>), [Pemecahan Masalah](</id/gateway/troubleshooting>)

Izin dan Kemampuan Bawaan 4 kemampuan

Eksperimental0%

Beta74%

Stabil88%

[Macos](</id/platforms/macos>), [Jarak Jauh](</id/platforms/mac/remote>)

Profil dan Isolasi 5 kemampuan

Eksperimental0%

Beta74%

Stabil88%

[Beberapa Gateway](</id/gateway/multiple-gateways>), [Indeks](</id/gateway>), [Gateway](</id/cli/gateway>)

Hosting Docker dan Podman - M3 Beta - 4 area

Dokumentasi instalasi tersedia dan merupakan jalur deployment yang umum. Promosikan setelah smoke rilis berulang menangkap perilaku pemutakhiran dan volume.

Cakupan Eksperimental - 7%Kualitas Beta - 71%Kelengkapan Beta - 79%Tidak ada

Penyiapan Kontainer 6 kapabilitas

Eksperimental0%

Alfa68%

Beta79%

[Docker](</id/install/docker>), [Podman](</id/install/podman>)

Operasi Kontainer 11 kapabilitas

Eksperimental0%

Alfa68%

Beta79%

[Podman](</id/install/podman>), [Runtime VM Docker](</id/install/docker-vm-runtime>), [Docker](</id/install/docker>), [Hetzner](</id/install/hetzner>), [Hostinger](</id/install/hostinger>)

Rilis dan Validasi Image 5 kapabilitas

Eksperimental29%

Beta79%

Beta79%

[Docker](</id/install/docker>), [Runtime VM Docker](</id/install/docker-vm-runtime>), [Validasi Rilis Lengkap](</id/reference/full-release-validation>)

Sandbox dan Perkakas Agen 3 kapabilitas

Eksperimental0%

Alfa68%

Beta79%

[Docker](</id/install/docker>), [Runtime VM Docker](</id/install/docker-vm-runtime>)

Windows melalui WSL2 - M3 Beta - 6 area

Jalur Windows yang direkomendasikan dengan panduan systemd/layanan pengguna dan dokumentasi rantai boot. Promosikan setelah scorecard instalasi/pembaruan berulang.

Cakupan Eksperimental - 6%Kualitas Alfa - 69%Kelengkapan Beta - 79%Parsial - 5

Penyiapan WSL 6 kemampuan / didukung LTS

Eksperimental0%

Alfa67%

Beta79%

[Windows](</id/platforms/windows>), [Memulai](</id/start/getting-started>)

CLI 8 kemampuan / didukung LTS

Eksperimental0%

Alfa67%

Beta79%

[Windows](</id/platforms/windows>), [Memulai](</id/start/getting-started>), [Memperbarui](</id/install/updating>), [Onboard](</id/cli/onboard>), [Doctor](</id/cli/doctor>), [Status](</id/cli/status>), [Log](</id/cli/logs>)

Siklus Hidup Layanan Gateway 10 kemampuan / didukung LTS

Eksperimental0%

Alfa67%

Beta79%

[Windows](</id/platforms/windows>), [Indeks](</id/gateway>), [Doctor](</id/gateway/doctor>)

Akses dan Paparan Gateway 11 kemampuan / didukung LTS

Eksperimental0%

Alfa67%

Beta79%

[Autentikasi](</id/gateway/authentication>), [Rahasia](</id/gateway/secrets>), [Jarak Jauh](</id/gateway/remote>), [Runbook Paparan](</id/gateway/security/exposure-runbook>), [Windows](</id/platforms/windows>)

Diagnostik dan Perbaikan 6 kemampuan / didukung LTS

Eksperimental38%

Beta79%

Beta79%

[Windows](</id/platforms/windows>), [Status](</id/cli/status>), [Log](</id/cli/logs>), [Doctor](</id/cli/doctor>), [Doctor](</id/gateway/doctor>)

Browser dan UI Kontrol 6 kemampuan

Eksperimental0%

Alfa67%

Beta79%

[Pemecahan Masalah Cdp Jarak Jauh Windows Wsl2 Browser](</id/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Browser](</id/tools/browser>), [Ui Kontrol](</id/web/control-ui>)

Raspberry Pi dan perangkat Linux kecil - M3 Beta - 4 area

Dokumentasi platform tersedia dan jalur Gateway berbasis Linux. Perlu bukti smoke rilis khusus perangkat keras untuk naik ke tingkat lebih tinggi.

Cakupan Eksperimental - 0%Kualitas Alfa - 67%Kelengkapan Beta - 79%Tidak ada

Penyiapan dan Kompatibilitas 12 kemampuan

Eksperimental0%

Alfa67%

Beta79%

[Raspberry Pi](</id/install/raspberry-pi>), [Indeks](</id/install>), [FAQ Menjalankan Pertama Kali](</id/help/faq-first-run>), [FAQ](</id/help/faq>), [Linux](</id/platforms/linux>), [Pemasang](</id/install/installer>)

Akses Jarak Jauh dan Autentikasi 9 kemampuan

Eksperimental0%

Alfa67%

Beta79%

[Raspberry Pi](</id/install/raspberry-pi>), [Autentikasi](</id/gateway/authentication>), [Rahasia](</id/gateway/secrets>), [Penyandingan](</id/gateway/pairing>), [Perangkat](</id/cli/devices>), [Jarak Jauh](</id/gateway/remote>), [Tailscale](</id/gateway/tailscale>)

Runtime Gateway 10 kemampuan

Eksperimental0%

Alfa67%

Beta79%

[Indeks](</id/gateway>), [Gateway](</id/cli/gateway>), [Raspberry Pi](</id/install/raspberry-pi>), [Linux](</id/platforms/linux>), [VPS](</id/vps>)

Performa dan Diagnostik 5 kemampuan

Eksperimental0%

Alfa67%

Beta79%

[Raspberry Pi](</id/install/raspberry-pi>), [Linux](</id/platforms/linux>), [Kesehatan](</id/gateway/health>), [Diagnostik](</id/gateway/diagnostics>)

aplikasi pendamping macOS - M3 Beta - 8 area

Aplikasi menu bar yang lengkap, izin, mode Node, Canvas, aktivasi suara, WebChat, dan mode jarak jauh sudah tersedia. Masih cukup cepat berubah sehingga belum Stabil.

Cakupan Eksperimental - 0%Kualitas Alfa - 66%Kelengkapan Beta - 78%Tidak ada

Kanvas 4 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Kanvas](</id/platforms/mac/canvas>), [Macos](</id/platforms/macos>), [Webchat](</id/web/webchat>)

Penyiapan Lokal 7 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Gateway Terbundel](</id/platforms/mac/bundled-gateway>), [Macos](</id/platforms/macos>), [Proses Anak](</id/platforms/mac/child-process>), [Penyiapan Pengembangan](</id/platforms/mac/dev-setup>)

Status dan Pengaturan 5 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Bilah Menu](</id/platforms/mac/menu-bar>), [Ikon](</id/platforms/mac/icon>), [Macos](</id/platforms/macos>), [Kesehatan](</id/platforms/mac/health>), [Pencatatan Log](</id/platforms/mac/logging>), [Jarak Jauh](</id/platforms/mac/remote>)

Kemampuan Native 5 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Macos](</id/platforms/macos>), [Xpc](</id/platforms/mac/xpc>), [Izin](</id/platforms/mac/permissions>), [Penandatanganan](</id/platforms/mac/signing>), [Peekaboo](</id/platforms/mac/peekaboo>)

Koneksi Jarak Jauh 3 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Jarak Jauh](</id/platforms/mac/remote>), [Macos](</id/platforms/macos>), [Jarak Jauh](</id/gateway/remote>)

Suara dan Bicara 3 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Voicewake](</id/platforms/mac/voicewake>), [Overlay Suara](</id/platforms/mac/voice-overlay>), [Bicara](</id/nodes/talk>), [Macos](</id/platforms/macos>)

WebChat 3 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Webchat](</id/platforms/mac/webchat>), [Macos](</id/platforms/macos>), [Webchat](</id/web/webchat>)

WebChat Jarak Jauh 5 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Webchat](</id/platforms/mac/webchat>), [Jarak Jauh](</id/gateway/remote>), [Jarak Jauh](</id/platforms/mac/remote>)

Aplikasi Android - M2 Alpha - 7 area

Jalur Google Play publik sudah tersedia, tetapi dokumentasi aplikasi masih menggambarkan pembangunan ulang ini sebagai sangat alfa dan menyebutkan pekerjaan pengerasan rilis.

Cakupan Eksperimental - 0%Kualitas Alfa - 59%Kelengkapan Alfa - 66%Tidak ada

Pengambilan Media 1 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Android](</id/platforms/android>), [Kamera](</id/nodes/camera>)

Obrolan Seluler 1 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Android](</id/platforms/android>)

Penyiapan Koneksi 1 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Android](</id/platforms/android>), [Bonjour](</id/gateway/bonjour>), [Penyandingan](</id/gateway/pairing>)

Distribusi 3 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Android](</id/platforms/android>)

Pengaturan 1 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Android](</id/platforms/android>)

Suara 1 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Android](</id/platforms/android>), [Bicara](</id/nodes/talk>)

Runtime Perangkat 2 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Android](</id/platforms/android>), [Pemecahan Masalah](</id/nodes/troubleshooting>), [Protokol](</id/gateway/protocol>)

Windows Native - M2 Alpha - 4 area

Alur CLI/Gateway inti berfungsi, tetapi dokumentasi masih merekomendasikan WSL2 untuk pengalaman lengkap dan mencantumkan catatan khusus native.

Cakupan Eksperimental - 0%Kualitas Alpha - 58%Kelengkapan Alpha - 66%Sebagian - 1

CLI 9 kapabilitas / didukung LTS

Eksperimental0%

Alfa54%

Alfa64%

[Indeks](</id/install>), [Penginstal](</id/install/installer>), [Windows](</id/platforms/windows>), [Memulai](</id/start/getting-started>), [Orientasi](</id/cli/onboard>)

Manajemen Gateway 11 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[Windows](</id/platforms/windows>), [Indeks](</id/gateway>), [Gateway](</id/cli/gateway>), [Dokter](</id/cli/doctor>)

Jaringan 4 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[Windows](</id/platforms/windows>), [Indeks](</id/gateway>), [Gateway](</id/cli/gateway>)

Pembaruan 4 kapabilitas

Eksperimental0%

Alfa59%

Alfa66%

[Memperbarui](</id/install/updating>), [CI](</id/ci>)

Hosting Kubernetes - M2 Alfa - 4 area

Hosting Kubernetes adalah jalur deployment klaster berbasis Kustomize yang terpisah. Penilaian saat ini menunjukkan jalur deployment minimal yang nyata dengan celah seputar CI khusus Kubernetes, pengemasan ingress/TLS/NetworkPolicy, pencadangan/pemulihan, dan penguatan paparan produksi.

Cakupan Eksperimental - 0%Kualitas Alpha - 55%Kelengkapan Alpha - 61%Tidak Ada

Penyiapan Deployment 5 kapabilitas

Eksperimental0%

Alpha55%

Alpha61%

[Kubernetes](</id/install/kubernetes>), [Indeks](</id/install>)

Konfigurasi dan Rahasia 5 kapabilitas

Eksperimental0%

Alpha55%

Alpha61%

[Kubernetes](</id/install/kubernetes>), [Rahasia](</id/gateway/secrets>), [Lingkungan](</id/help/environment>)

Akses dan Eksposur 5 kapabilitas

Eksperimental0%

Alpha55%

Alpha61%

[Kubernetes](</id/install/kubernetes>), [Autentikasi](</id/gateway/authentication>), [Jarak Jauh](</id/gateway/remote>), [Runbook Eksposur](</id/gateway/security/exposure-runbook>)

Siklus Hidup Klaster 5 kapabilitas

Eksperimental0%

Alpha55%

Alpha61%

[Kubernetes](</id/install/kubernetes>), [Indeks](</id/gateway>)

Aplikasi iOS - M1 Eksperimental - 8 area

Pratinjau internal / super-alpha. Alur push berbasis TestFlight dan relay sudah ada, tetapi belum ada distribusi publik.

Cakupan Eksperimental - 0%Kualitas Eksperimental - 41%Kelengkapan Eksperimental - 44%Tidak ada

Media dan Berbagi 1 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>), [Kamera](</id/nodes/camera>)

Kanvas dan Layar 1 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>), [Canvas](</id/plugins/reference/canvas>)

Obrolan dan Sesi 1 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>), [Webchat](</id/web/webchat>), [Protokol](</id/gateway/protocol>)

Penyiapan dan Diagnostik Gateway 7 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>), [Penyandingan](</id/channels/pairing>)

Distribusi 1 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>)

Perintah Perangkat 2 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>), [Protokol](</id/gateway/protocol>)

Notifikasi dan Latar Belakang 1 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>), [Konfigurasi](</id/gateway/configuration>)

Suara 1 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>), [Bicara](</id/nodes/talk>)

Jalur pemasangan Nix - M1 Eksperimental - 5 area

Alur pemasangan opsional. Memerlukan janji dukungan yang lebih jelas sebelum promosi alpha/beta.

Cakupan Eksperimental - 0%Kualitas Eksperimental - 41%Kelengkapan Eksperimental - 44%Tidak ada

Serah Terima Instalasi 4 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Nix](</id/install/nix>), [Indeks](</id/install>), [Direktori Dokumentasi](</id/start/docs-directory>)

Siklus Hidup Plugin 4 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Kelola Plugin](</id/plugins/manage-plugins>), [Plugin](</id/tools/plugin>), [Nix](</id/install/nix>)

Aktivasi dan UX Aplikasi 7 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Nix](</id/install/nix>)

Konfigurasi dan Status 7 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Nix](</id/install/nix>), [Penyiapan](</id/cli/setup>), [Lingkungan](</id/help/environment>)

Runtime Layanan dan Guard 8 kapabilitas

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Nix](</id/install/nix>), [Penyiapan](</id/cli/setup>), [Doctor](</id/cli/doctor>), [Pembaruan](</id/cli/update>)

Permukaan pendamping watchOS - M1 Eksperimental - 5 area

Sumber memiliki permukaan aplikasi/ekstensi Watch; dokumentasi publik belum menyajikan ini sebagai fitur pengguna.

Cakupan Eksperimental - 0%Kualitas Eksperimental - 41%Kelengkapan Eksperimental - 44%Tidak Ada

Pengiriman dan Pemulihan 7 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>)

Persetujuan Eksekusi 3 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Persetujuan Eksekusi](</id/tools/exec-approvals>), [Ios](</id/platforms/ios>)

Distribusi dan Dukungan 6 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>)

Notifikasi dan Balasan 7 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>)

UI Aplikasi Watch 3 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Ios](</id/platforms/ios>)

Aplikasi pendamping Linux - M0 Direncanakan - 5 area

Dokumentasi menyebutkan bahwa aplikasi pendamping Linux native direncanakan; Gateway adalah jalur Linux yang didukung saat ini.

Cakupan Eksperimental - 0%Kualitas Eksperimental - 19%Kelengkapan Eksperimental - 21%Tidak ada

Distribusi Aplikasi 3 kapabilitas

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Linux](</id/platforms/linux>), [Indeks](</id/platforms>), [Indeks](</id/install>)

Konektivitas Gateway 4 kapabilitas

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Linux](</id/platforms/linux>), [Indeks](</id/gateway>), [Pemasangan](</id/gateway/pairing>), [Jarak Jauh](</id/gateway/remote>)

Chat dan Sesi 3 kapabilitas

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Linux](</id/platforms/linux>), [Protokol](</id/gateway/protocol>), [Webchat](</id/web/webchat>)

Kapabilitas Desktop 9 kapabilitas

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Linux](</id/platforms/linux>), [Persetujuan Exec](</id/tools/exec-approvals>), [Rahasia](</id/gateway/secrets>), [Indeks](</id/nodes>), [Exec](</id/tools/exec>), [Bicara](</id/nodes/talk>), [Kamera](</id/nodes/camera>)

Status dan Diagnostik 7 kapabilitas

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Linux](</id/platforms/linux>), [Openclaw](</id/start/openclaw>), [Doctor](</id/gateway/doctor>)

Aplikasi pendamping Windows native - M0 Direncanakan - 5 area

Hanya direncanakan.

Cakupan Eksperimental - 0%Kualitas Eksperimental - 19%Kelengkapan Eksperimental - 21%Tidak Ada

Instalasi dan Pembaruan 4 kemampuan

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Windows](</id/platforms/windows>), [Indeks](</id/install>)

Koneksi Gateway 3 kemampuan

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Windows](</id/platforms/windows>), [Indeks](</id/gateway>), [Penyandingan](</id/gateway/pairing>), [Jarak Jauh](</id/gateway/remote>)

Sesi Obrolan 2 kemampuan

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Windows](</id/platforms/windows>), [Protokol](</id/gateway/protocol>)

Status dan Perbaikan 5 kemampuan

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Windows](</id/platforms/windows>), [Dokter](</id/gateway/doctor>), [Indeks](</id/gateway>)

Alat Desktop dan Izin 10 kemampuan

Eksperimental0%

Eksperimental19%

Eksperimental21%

[Windows](</id/platforms/windows>), [Indeks](</id/nodes>), [Exec](</id/tools/exec>), [Persetujuan Exec](</id/tools/exec-approvals>), [Indeks](</id/gateway/security>)

### Kanal

Discord - M4 Stabil - 6 area

Dokumentasi mendalam dan cakupan fitur yang luas. Jalur suara/delegasi sebaiknya tetap dinilai terpisah sebagai beta/alfa.

Cakupan Eksperimental - 0%Kualitas Beta - 73%Kelengkapan Stabil - 87%Parsial - 4

Penyiapan dan Operasi Channel 10 kapabilitas / didukung LTS

Eksperimental0%

Beta73%

Stabil87%

[Discord](</id/channels/discord>), [Discord](</id/plugins/reference/discord>), [Fly](</id/install/fly>), [Perintah Slash](</id/tools/slash-commands>), [Kesehatan](</id/gateway/health>), [Channel](</id/cli/channels>), [Channel Konfigurasi](</id/gateway/config-channels>)

Akses dan Identitas 6 kapabilitas / didukung LTS

Eksperimental0%

Beta73%

Stabil87%

[Discord](</id/channels/discord>), [Pemasangan](</id/channels/pairing>), [Grup Akses](</id/channels/access-groups>), [Grup](</id/channels/groups>)

Perutean dan Pengiriman Percakapan 12 kapabilitas / didukung LTS

Eksperimental0%

Beta73%

Stabil87%

[Discord](</id/channels/discord>), [Perutean Channel](</id/channels/channel-routing>), [Grup](</id/channels/groups>), [Grup Akses](</id/channels/access-groups>), [Agen Acp](</id/tools/acp-agents>), [Subagen](</id/tools/subagents>)

Media dan Konten Kaya 1 kapabilitas / didukung LTS

Eksperimental0%

Beta73%

Stabil87%

[Discord](</id/channels/discord>)

Kontrol Native dan Persetujuan 5 kapabilitas

Eksperimental0%

Beta73%

Stabil87%

[Discord](</id/channels/discord>), [Perintah Slash](</id/tools/slash-commands>)

Suara dan Panggilan Realtime 5 kapabilitas

Eksperimental0%

Beta73%

Stabil87%

[Discord](</id/channels/discord>), [Openai](</id/providers/openai>), [Elevenlabs](</id/providers/elevenlabs>), [Otomatisasi Qa E2e](</id/concepts/qa-e2e-automation>), [Channel Konfigurasi](</id/gateway/config-channels>)

Telegram - M3 Beta - 5 area

Channel inti sudah cukup matang untuk penggunaan reguler, tetapi UX dengan variasi tinggi dan kasus tepi media memerlukan bukti skenario berulang.

Cakupan Eksperimental - 0%Kualitas Alfa - 68%Kelengkapan Beta - 78%Penuh - 5

Penyiapan dan Operasi Channel 10 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Telegram](</id/channels/telegram>), [Konfigurasi Channel](</id/gateway/config-channels>), [Channel](</id/cli/channels>)

Akses dan Identitas 10 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Telegram](</id/channels/telegram>), [Pemasangan](</id/channels/pairing>), [Grup Akses](</id/channels/access-groups>), [Grup](</id/channels/groups>), [Multi Agent](</id/concepts/multi-agent>)

Perutean dan Pengiriman Percakapan 1 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Telegram](</id/channels/telegram>), [Grup](</id/channels/groups>), [Multi Agent](</id/concepts/multi-agent>)

Media dan Konten Kaya 1 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Telegram](</id/channels/telegram>), [Lokasi](</id/channels/location>)

Kontrol dan Persetujuan Native 9 kapabilitas / didukung LTS

Eksperimental0%

Beta77%

Beta79%

[Telegram](</id/channels/telegram>), [Persetujuan Exec](</id/tools/exec-approvals>), [Reaksi](</id/tools/reactions>)

Slack - M3 Beta - 5 area

Dokumentasi channel kelas utama dan permukaan perutean. Membutuhkan kartu skor skenario instalasi/admin workspace.

Cakupan Eksperimental - 0%Kualitas Alpha - 66%Kelengkapan Beta - 78%Penuh - 5

Penyiapan dan Operasi Channel 10 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Slack](</id/channels/slack>), [Slack](</id/plugins/reference/slack>), [Rahasia](</id/gateway/secrets>), [Otomatisasi QA E2E](</id/concepts/qa-e2e-automation>), [Pemecahan Masalah](</id/channels/troubleshooting>)

Akses dan Identitas 1 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Slack](</id/channels/slack>), [Pemasangan](</id/channels/pairing>)

Perutean dan Pengiriman Percakapan 5 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Slack](</id/channels/slack>), [Perlindungan Bot Loop](</id/channels/bot-loop-protection>), [Pemasangan](</id/channels/pairing>)

Media dan Konten Kaya 1 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Slack](</id/channels/slack>), [Otomatisasi QA E2E](</id/concepts/qa-e2e-automation>)

Kontrol dan Persetujuan Native 8 kapabilitas / didukung LTS

Eksperimental0%

Alpha66%

Beta78%

[Slack](</id/channels/slack>), [Perintah Slash](</id/tools/slash-commands>), [Persetujuan Exec](</id/tools/exec-approvals>)

iMessage dan BlueBubbles - M3 Beta - 5 area

iMessage yang didukung berjalan melalui imsg pada host macOS Messages yang sudah masuk; konfigurasi BlueBubbles lama memerlukan migrasi. Tetap tampilkan izin macOS, pembungkus SSH, API SIP/privat, dan catatan migrasi.

Cakupan Eksperimental - 0%Kualitas Alpha - 66%Kelengkapan Beta - 78%Tidak Ada

Penyiapan dan Operasi Channel 11 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</id/announcements/bluebubbles-imessage>), [Imessage Dari Bluebubbles](</id/channels/imessage-from-bluebubbles>), [Konfigurasi Channel](</id/gateway/config-channels>), [Imessage](</id/channels/imessage>)

Akses dan Identitas 6 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Imessage](</id/channels/imessage>), [Imessage Dari Bluebubbles](</id/channels/imessage-from-bluebubbles>), [Konfigurasi Channel](</id/gateway/config-channels>)

Perutean dan Pengiriman Percakapan 4 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Imessage](</id/channels/imessage>)

Media dan Konten Kaya 7 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Imessage](</id/channels/imessage>), [Imessage Dari Bluebubbles](</id/channels/imessage-from-bluebubbles>), [Konfigurasi Channel](</id/gateway/config-channels>)

Kontrol Native dan Persetujuan 3 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Imessage](</id/channels/imessage>)

WhatsApp - M3 Beta - 5 area

Jalur inti penting dan terdokumentasi; volatilitas Baileys/sesi upstream membuatnya tetap di bawah Stabil.

Cakupan Eksperimental - 0%Kualitas Alpha - 66%Kelengkapan Beta - 78%Tidak ada

Penyiapan dan Operasi Channel 5 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[WhatsApp](</id/channels/whatsapp>), [Konfigurasi Channel](</id/gateway/config-channels>), [WhatsApp](</id/plugins/reference/whatsapp>), [Otomasi QA E2E](</id/concepts/qa-e2e-automation>), [Doctor](</id/gateway/doctor>)

Akses dan Identitas 7 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[WhatsApp](</id/channels/whatsapp>), [Konfigurasi Channel](</id/gateway/config-channels>), [Otomasi QA E2E](</id/concepts/qa-e2e-automation>), [Penyandingan](</id/channels/pairing>)

Perutean dan Pengiriman Percakapan 4 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[WhatsApp](</id/channels/whatsapp>), [Pesan Grup](</id/channels/group-messages>)

Media dan Konten Kaya 2 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[WhatsApp](</id/channels/whatsapp>)

Kontrol dan Persetujuan Native 2 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[WhatsApp](</id/channels/whatsapp>)

Matrix - M2 Alfa - 6 area

Didukung melalui Plugin terbundel. Membutuhkan kartu skor bridge, auth, dan siklus hidup ruang.

Cakupan Eksperimental - 0%Kualitas Alfa - 60%Kelengkapan Alfa - 67%Tidak ada

Penyiapan dan Operasi Channel 5 kemampuan

Eksperimental0%

Alpha60%

Alpha67%

[Matrix](</id/channels/matrix>), [Migrasi Matrix](</id/channels/matrix-migration>)

Akses dan Identitas 7 kemampuan

Eksperimental0%

Alpha60%

Alpha67%

[Matrix](</id/channels/matrix>), [Grup](</id/channels/groups>), [Perlindungan Loop Bot](</id/channels/bot-loop-protection>)

Perutean dan Pengiriman Percakapan 1 kemampuan

Eksperimental0%

Alpha60%

Alpha67%

[Matrix](</id/channels/matrix>)

Media dan Konten Kaya 1 kemampuan

Eksperimental0%

Alpha60%

Alpha67%

[Matrix](</id/channels/matrix>)

Kontrol dan Persetujuan Native 6 kemampuan

Eksperimental0%

Alpha60%

Alpha67%

[Matrix](</id/channels/matrix>)

Enkripsi dan Verifikasi 3 kemampuan

Eksperimental0%

Alpha60%

Alpha67%

[Matrix](</id/channels/matrix>), [Migrasi Matrix](</id/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 area

Channel terdokumentasi, tetapi penyiapan perusahaan/admin meningkatkan risiko kematangan.

Cakupan Eksperimental - 0%Kualitas Alpha - 59%Kelengkapan Alpha - 66%Tidak ada

Penyiapan dan Operasi Channel 16 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Google Chat](</id/channels/googlechat>), [Google Chat](</id/plugins/reference/googlechat>), [Konfigurasi Channel](</id/gateway/config-channels>), [Referensi CLI Wizard](</id/start/wizard-cli-reference>), [Rahasia](</id/gateway/secrets>), [Permukaan Kredensial Secretref](</id/reference/secretref-credential-surface>), [Kesehatan](</id/gateway/health>), [Inventaris Plugin](</id/plugins/plugin-inventory>), [Indeks](</id/channels>)

Akses dan Identitas 11 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Google Chat](</id/channels/googlechat>), [Pemasangan](</id/channels/pairing>), [Grup Akses](</id/channels/access-groups>), [Konfigurasi Channel](</id/gateway/config-channels>), [Perlindungan Loop Bot](</id/channels/bot-loop-protection>), [Perutean Channel](</id/channels/channel-routing>)

Perutean dan Pengiriman Percakapan 1 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Google Chat](</id/channels/googlechat>), [Perlindungan Loop Bot](</id/channels/bot-loop-protection>), [Grup Akses](</id/channels/access-groups>), [Perutean Channel](</id/channels/channel-routing>)

Media dan Konten Kaya 1 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Google Chat](</id/channels/googlechat>), [Pesan](</id/cli/message>), [Pemahaman Media](</id/nodes/media-understanding>), [Permukaan Kredensial Secretref](</id/reference/secretref-credential-surface>)

Kontrol dan Persetujuan Native 16 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Google Chat](</id/channels/googlechat>), [Pesan](</id/cli/message>), [Pemahaman Media](</id/nodes/media-understanding>), [Permukaan Kredensial Secretref](</id/reference/secretref-credential-surface>), [Reaksi](</id/tools/reactions>), [Perintah Slash](</id/tools/slash-commands>), [Konfigurasi Agen](</id/gateway/config-agents>), [Refaktor Siklus Hidup Pesan](</id/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 area

Alur auth/admin perusahaan memerlukan bukti skenario eksplisit.

Cakupan Eksperimental - 0%Kualitas Alpha - 59%Kelengkapan Alpha - 66%Tidak Ada

Penyiapan dan Operasi Channel 9 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Msteams](</id/channels/msteams>), [Msteams](</id/plugins/reference/msteams>), [Konfigurasi Channel](</id/gateway/config-channels>), [Kesehatan](</id/gateway/health>)

Akses dan Identitas 9 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Msteams](</id/channels/msteams>), [Pemasangan](</id/channels/pairing>), [Grup Akses](</id/channels/access-groups>)

Perutean dan Pengiriman Percakapan 5 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Msteams](</id/channels/msteams>), [Grup](</id/channels/groups>), [Perutean Channel](</id/channels/channel-routing>)

Media dan Konten Kaya 5 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Msteams](</id/channels/msteams>)

Kontrol Native dan Persetujuan 5 kapabilitas

Eksperimental0%

Alpha59%

Alpha66%

[Msteams](</id/channels/msteams>), [Persetujuan Exec Lanjutan](</id/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 area

Dokumentasi channel yang didukung tersedia; membutuhkan bukti instalasi dan penyambungan ulang yang lebih kuat.

Cakupan Eksperimental - 0%Kualitas Alpha - 59%Kelengkapan Alpha - 66%Tidak ada

Penyiapan dan Operasi Saluran 7 kemampuan

Eksperimental0%

Alpha59%

Alpha66%

[Signal](</id/channels/signal>), [Signal](</id/plugins/reference/signal>)

Akses dan Identitas 6 kemampuan

Eksperimental0%

Alpha59%

Alpha66%

[Signal](</id/channels/signal>)

Perutean dan Pengiriman Percakapan 1 kemampuan

Eksperimental0%

Alpha59%

Alpha66%

[Signal](</id/channels/signal>)

Media dan Konten Kaya 7 kemampuan

Eksperimental0%

Alpha59%

Alpha66%

[Signal](</id/channels/signal>)

Kontrol Bawaan dan Persetujuan 3 kemampuan

Eksperimental0%

Alpha59%

Alpha66%

[Signal](</id/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, saluran regional - M2 Alpha - 4 area

Cakupan regional yang penting, tetapi tingkat dukungan publik harus dikalibrasi berdasarkan jenis akun, persetujuan upstream, dan bukti maintainer.

Cakupan Eksperimental - 0%Kualitas Alpha - 55%Kelengkapan Alpha - 58%Tidak ada

Penyiapan dan Operasi Channel 6 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Indeks](</id/channels>), [Pemasangan](</id/channels/pairing>), [Feishu](</id/plugins/reference/feishu>), [Internal Arsitektur](</id/plugins/architecture-internals>)

Akses dan Identitas 1 kapabilitas

Eksperimental0%

Alpha53%

Alpha54%

Tidak ada dokumentasi tertaut

Perutean dan Pengiriman Percakapan 1 kapabilitas

Eksperimental0%

Alpha53%

Alpha54%

Tidak ada dokumentasi tertaut

Media dan Konten Kaya 1 kapabilitas

Eksperimental0%

Alpha53%

Alpha54%

Tidak ada dokumentasi tertaut

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 areas

Surface yang didukung tersedia, tetapi tingkat kematangan kemungkinan bervariasi menurut cakupan upstream dan maintainer. Nilai satu per satu nanti.

Cakupan Eksperimental - 0%Kualitas Alpha - 53%Kelengkapan Alpha - 54%Tidak ada

Penyiapan dan Operasi Channel 1 kemampuan

Eksperimental0%

Alpha53%

Alpha54%

Tidak ada dokumentasi tertaut

Akses dan Identitas 1 kemampuan

Eksperimental0%

Alpha53%

Alpha54%

Tidak ada dokumentasi tertaut

Perutean dan Pengiriman Percakapan 1 kemampuan

Eksperimental0%

Alpha53%

Alpha54%

Tidak ada dokumentasi tertaut

Media dan Konten Kaya 1 kemampuan

Eksperimental0%

Alpha53%

Alpha54%

Tidak ada dokumentasi tertaut

Channel Panggilan Suara - M1 Eksperimental - 5 area

Jalur opsional/plugin dengan perilaku realtime yang kompleks. Membutuhkan kartu skor skenario sebelum beta publik.

Cakupan Eksperimental - 0%Kualitas Eksperimental - 41%Kelengkapan Eksperimental - 44%Tidak ada

Penyiapan dan Operasi Saluran 2 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Panggilan Suara](</id/cli/voicecall>), [Panggilan Suara](</id/plugins/voice-call>), [Protokol](</id/gateway/protocol>)

Akses dan Identitas 1 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Panggilan Suara](</id/plugins/voice-call>), [Panggilan Suara](</id/cli/voicecall>)

Perutean dan Pengiriman Percakapan 1 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Panggilan Suara](</id/plugins/voice-call>)

Media dan Konten Kaya 2 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Panggilan Suara](</id/plugins/voice-call>), [Inventaris Plugin](</id/plugins/plugin-inventory>)

Suara dan Panggilan Real-time 2 kemampuan

Eksperimental0%

Eksperimental41%

Eksperimental44%

[Panggilan Suara](</id/plugins/voice-call>)

### Penyedia dan alat

Automasi browser, exec, dan alat sandbox - M3 Beta - 3 area

Alat inti didokumentasikan, tetapi keamanan host dan UX izin harus tetap berada dalam peninjauan kartu skor aktif.

Cakupan Eksperimental - 21%Kualitas Beta - 75%Kelengkapan Beta - 79%Parsial - 2

Otomatisasi Browser 8 kapabilitas

Eksperimental13%

Beta79%

Beta79%

[Kontrol Browser](</id/tools/browser-control>), [Pengujian](</id/help/testing>), [Browser](</id/tools/browser>), [Indeks](</id/gateway/security>), [Pemeriksaan Audit](</id/gateway/security/audit-checks>)

Pemanggilan dan Eksekusi Alat 6 kapabilitas / didukung LTS

Alpha50%

Beta79%

Beta79%

[Exec](</id/tools/exec>), [Proses Latar Belakang](</id/gateway/background-process>), [API HTTP Pemanggilan Alat](</id/gateway/tools-invoke-http-api>), [Cakupan Operator](</id/gateway/operator-scopes>), [Protokol](</id/gateway/protocol>), [Persetujuan Exec](</id/tools/exec-approvals>), [Persetujuan Exec Lanjutan](</id/tools/exec-approvals-advanced>), [Elevated](</id/tools/elevated>)

Kebijakan Sandbox dan Alat 6 kapabilitas / didukung LTS

Eksperimental0%

Alpha68%

Beta79%

[Sandboxing](</id/gateway/sandboxing>), [Sandbox Vs Kebijakan Alat Vs Elevated](</id/gateway/sandbox-vs-tool-policy-vs-elevated>), [Alat Sandbox Multi-Agen](</id/tools/multi-agent-sandbox-tools>), [Referensi Harness Codex](</id/plugins/codex-harness-reference>), [Alat Konfigurasi](</id/gateway/config-tools>)

Jalur penyedia OpenAI dan Codex - M3 Beta - 5 area

Dokumentasi mendalam, jalur OAuth/langganan, suara realtime, gambar, dan perilaku kompatibilitas. Perubahan cepat pada penyedia mencegah ini menjadi Stabil tanpa bukti scorecard rilis.

Cakupan Eksperimental - 26%Kualitas Beta - 74%Kelengkapan Beta - 79%Parsial - 3

Model dan Auth 6 kapabilitas / didukung LTS

Eksperimental44%

Beta79%

Beta79%

[Openai](</id/providers/openai>), [Codex Harness](</id/plugins/codex-harness>), [Model](</id/concepts/models>), [OAuth](</id/concepts/oauth>), [Referensi Codex Harness](</id/plugins/codex-harness-reference>), [Pemantauan Auth](</id/gateway/authentication>)

Kompatibilitas Respons dan Alat 4 kapabilitas / didukung LTS

Eksperimental40%

Beta79%

Beta79%

[Openai](</id/providers/openai>), [Openresponses HTTP API](</id/gateway/openresponses-http-api>), [Openai HTTP API](</id/gateway/openai-http-api>), [Plugin Native Codex](</id/plugins/codex-native-plugins>)

Codex Harness Native 2 kapabilitas / didukung LTS

Eksperimental44%

Beta79%

Beta79%

[Codex Harness](</id/plugins/codex-harness>), [Runtime Codex Harness](</id/plugins/codex-harness-runtime>), [Referensi Codex Harness](</id/plugins/codex-harness-reference>), [Plugin Native Codex](</id/plugins/codex-native-plugins>)

Input Gambar dan Multimodal 2 kapabilitas

Eksperimental0%

Alpha67%

Beta79%

[Openai](</id/providers/openai>), [Pembuatan Gambar](</id/tools/image-generation>), [Gambar](</id/nodes/images>)

Suara dan Audio Realtime 2 kapabilitas

Eksperimental0%

Alpha67%

Beta79%

[Openai](</id/providers/openai>), [Discord](</id/channels/discord>), [Panggilan Suara](</id/plugins/voice-call>)

Alat pencarian web - M3 Beta - 4 area

Tersedia beberapa penyedia dan dokumentasi. Memerlukan bukti kuota/error/SSRF per keluarga penyedia.

Cakupan Eksperimental - 9%Kualitas Beta - 74%Kelengkapan Beta - 79%Tidak ada

Penyedia Pencarian 19 kemampuan

Eksperimental11%

Beta79%

Beta79%

[Web](</id/tools/web>), [Brave Search](</id/tools/brave-search>), [Tavily](</id/tools/tavily>), [Exa Search](</id/tools/exa-search>), [Firecrawl](</id/tools/firecrawl>), [Perplexity Search](</id/tools/perplexity-search>), [Duckduckgo Search](</id/tools/duckduckgo-search>), [Searxng Search](</id/tools/searxng-search>), [Gemini Search](</id/tools/gemini-search>), [Grok Search](</id/tools/grok-search>), [Kimi Search](</id/tools/kimi-search>), [Minimax Search](</id/tools/minimax-search>), [Ollama Search](</id/tools/ollama-search>), [Subpath SDK](</id/plugins/sdk-subpaths>), [Ikhtisar SDK](</id/plugins/sdk-overview>), [Manifest](</id/plugins/manifest>)

Penyiapan dan Diagnostik 9 kemampuan

Eksperimental0%

Alfa68%

Beta79%

[Web](</id/tools/web>), [Web Fetch](</id/tools/web-fetch>), [FAQ](</id/help/faq>), [Biaya Penggunaan API](</id/reference/api-usage-costs>), [Brave Search](</id/tools/brave-search>), [Perplexity Search](</id/tools/perplexity-search>), [Tavily](</id/tools/tavily>), [Firecrawl](</id/tools/firecrawl>)

Keamanan Jaringan 4 kemampuan

Eksperimental0%

Alfa68%

Beta79%

[Web](</id/tools/web>), [Web Fetch](</id/tools/web-fetch>), [Firecrawl](</id/tools/firecrawl>), [Searxng Search](</id/tools/searxng-search>)

Ketersediaan Tool dan Fetch 11 kemampuan

Eksperimental25%

Beta79%

Beta79%

[Config Tools](</id/gateway/config-tools>), [Web Fetch](</id/tools/web-fetch>), [Web](</id/tools/web>), [FAQ](</id/help/faq>)

Jalur penyedia Anthropic - M3 Beta - 5 area

Penyedia model kelas utama. Memerlukan bukti skenario auth/catalog/tool-call berulang.

Cakupan Eksperimental - 0%Kualitas Beta - 71%Kelengkapan Beta - 78%Tidak ada

Autentikasi dan Pemulihan Penyedia 9 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Anthropic](</id/providers/anthropic>), [Dokter](</id/gateway/doctor>), [Contoh Konfigurasi](</id/gateway/configuration-examples>), [Pemecahan Masalah](</id/gateway/troubleshooting>), [Cache Prompt](</id/reference/prompt-caching>)

Pemilihan Model dan Runtime 10 kemampuan

Eksperimental0%

Beta78%

Beta79%

[Anthropic](</id/providers/anthropic>), [Agen Konfigurasi](</id/gateway/config-agents>), [Model](</id/concepts/models>), [Backend CLI](</id/gateway/cli-backends>)

Transport Permintaan dan Semantik Giliran 10 kemampuan

Eksperimental0%

Beta77%

Beta79%

[Anthropic](</id/providers/anthropic>), [Cache Prompt](</id/reference/prompt-caching>), [Pemecahan Masalah](</id/gateway/troubleshooting>), [Backend CLI](</id/gateway/cli-backends>), [Penyedia Model](</id/concepts/model-providers>)

Cache Prompt dan Konteks 5 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Anthropic](</id/providers/anthropic>), [Cache Prompt](</id/reference/prompt-caching>), [Pemecahan Masalah](</id/gateway/troubleshooting>), [Heartbeat](</id/gateway/heartbeat>)

Input Media 4 kemampuan

Eksperimental0%

Alfa66%

Beta78%

[Anthropic](</id/providers/anthropic>), [Agen Konfigurasi](</id/gateway/config-agents>)

Google provider path - M3 Beta - 5 areas

Penyedia kelas utama dengan antarmuka model dan realtime. Memerlukan penilaian Live/Talk terpisah.

Cakupan Eksperimental - 0%Kualitas Alfa - 66%Kelengkapan Beta - 78%Tidak ada

Penyiapan Penyedia dan Kredensial 10 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[Google](</id/providers/google>), [Penyedia Model](</id/concepts/model-providers>)

Perutean Model dan Titik Akhir 10 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[Google](</id/providers/google>), [Penyedia Model](</id/concepts/model-providers>), [Google](</id/plugins/reference/google>), [Pencarian Gemini](</id/tools/gemini-search>)

Runtime Gemini Langsung 9 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[Google](</id/providers/google>), [Penyedia Model](</id/concepts/model-providers>), [FAQ Model](</id/help/faq-models>), [Pengujian Langsung](</id/help/testing-live>)

Media, Pencarian, dan Realtime 10 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[Google](</id/plugins/reference/google>), [Google](</id/providers/google>)

Caching Prompt 5 kapabilitas

Eksperimental0%

Alfa66%

Beta78%

[Caching Prompt](</id/reference/prompt-caching>), [Google](</id/providers/google>), [Penyedia Model](</id/concepts/model-providers>), [Penggunaan Token](</id/reference/token-use>)

Jalur penyedia OpenRouter - M3 Beta - 4 area

Jalur penyedia terpadu didokumentasikan dan bernilai, tetapi perilaku khusus model bervariasi.

Cakupan Eksperimental - 0%Kualitas Alfa - 66%Kelengkapan Beta - 78%Tidak ada

Penyiapan dan Autentikasi Provider 14 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Openrouter](</id/providers/openrouter>), [Provider Model](</id/concepts/model-providers>), [Konfigurasi](</id/cli/configure>), [Autentikasi](</id/gateway/authentication>), [Lingkungan](</id/help/environment>), [Model](</id/cli/models>), [Model](</id/concepts/models>)

Runtime Chat dan Normalisasi 15 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Openrouter](</id/providers/openrouter>), [Provider Model](</id/concepts/model-providers>), [Caching Prompt](</id/reference/prompt-caching>)

Pemulihan dan Diagnostik Provider 5 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Failover Model](</id/concepts/model-failover>), [Openrouter](</id/providers/openrouter>), [Model](</id/cli/models>)

Pembuatan Media dan Ucapan 7 kapabilitas

Eksperimental0%

Alpha66%

Beta78%

[Openrouter](</id/providers/openrouter>), [Pembuatan Gambar](</id/tools/image-generation>), [Pembuatan Musik](</id/tools/music-generation>), [Ringkasan Media](</id/tools/media-overview>), [Pembuatan Video](</id/tools/video-generation>), [Tts](</id/tools/tts>)

Alat pembuatan gambar, video, dan musik - M2 Alpha - 5 area

Kapabilitas tersedia di berbagai provider, tetapi kualitas, latensi, dan kompatibilitas parameter terlalu bervariasi untuk beta tanpa bukti per provider.

Cakupan Eksperimental - 0%Kualitas Alpha - 61%Kelengkapan Alpha - 68%Tidak ada

Perutean dan Penemuan Media 4 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Agen Konfigurasi](</id/gateway/config-agents>), [Pembuatan Gambar](</id/tools/image-generation>), [Pembuatan Video](</id/tools/video-generation>), [Pembuatan Musik](</id/tools/music-generation>)

Siklus Hidup dan Pengiriman Tugas 12 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Ikhtisar Media](</id/tools/media-overview>), [Pembuatan Gambar](</id/tools/image-generation>), [Pembuatan Video](</id/tools/video-generation>), [Pembuatan Musik](</id/tools/music-generation>)

Pembuatan Gambar 9 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Pembuatan Gambar](</id/tools/image-generation>), [Infer](</id/cli/infer>), [Ikhtisar Media](</id/tools/media-overview>)

Pembuatan Video 11 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Pembuatan Video](</id/tools/video-generation>), [Runway](</id/providers/runway>), [Pixverse](</id/providers/pixverse>), [Fal](</id/providers/fal>), [Openrouter](</id/providers/openrouter>)

Pembuatan Musik 6 kapabilitas

Eksperimental0%

Alpha61%

Alpha68%

[Pembuatan Musik](</id/tools/music-generation>)

Penyedia model lokal: Ollama, vLLM, SGLang, LM Studio - M2 Alpha - 5 area

Berguna dan terdokumentasi, tetapi variasi lingkungan tinggi.

Cakupan Eksperimental - 0%Kualitas Alpha - 61%Kelengkapan Alpha - 68%Tidak Ada

Penyiapan, Siklus Hidup, dan Diagnostik Penyedia 12 kapabilitas

Eksperimental0%

Alfa61%

Alfa68%

[Model Lokal](</id/gateway/local-models>), [Lmstudio](</id/providers/lmstudio>), [Ollama](</id/providers/ollama>), [Vllm](</id/providers/vllm>), [Layanan Model Lokal](</id/gateway/local-model-services>), [Agen Konfigurasi](</id/gateway/config-agents>), [Pemecahan Masalah](</id/gateway/troubleshooting>), [Doctor](</id/gateway/doctor>)

Plugin Penyedia Asli 10 kapabilitas

Eksperimental0%

Alfa61%

Alfa68%

[Ollama](</id/providers/ollama>), [Lmstudio](</id/providers/lmstudio>)

Kompatibilitas Runtime yang Kompatibel dengan OpenAI 8 kapabilitas

Eksperimental0%

Alfa61%

Alfa68%

[Vllm](</id/providers/vllm>), [Sglang](</id/providers/sglang>), [Model Lokal](</id/gateway/local-models>), [Lmstudio](</id/providers/lmstudio>)

Memori Lokal dan Embedding 5 kapabilitas

Eksperimental0%

Alfa61%

Alfa68%

[Memori](</id/concepts/memory>), [Doctor](</id/gateway/doctor>)

Keamanan Jaringan dan Kontrol Prompt 2 kapabilitas

Eksperimental0%

Alfa61%

Alfa68%

[Indeks](</id/gateway/security>), [Alat Konfigurasi](</id/gateway/config-tools>), [Model Lokal](</id/gateway/local-models>)

Penyedia terhosting berekor panjang - M2 Alfa - 3 area

Banyak halaman dokumentasi/referensi sudah ada; skor harus dihasilkan dari metadata penyedia plus cakupan smoke langsung.

Cakupan Eksperimental - 0%Kualitas Alpha - 61%Kelengkapan Alpha - 68%Tidak Ada

Penyedia LLM Terhosting 12 kemampuan

Eksperimental0%

Alpha61%

Alpha68%

[Indeks](</id/providers>), [Penyedia Model](</id/concepts/model-providers>), [Pengujian Langsung](</id/help/testing-live>), [Onboard](</id/cli/onboard>)

Penyedia Media Terhosting 8 kemampuan

Eksperimental0%

Alpha61%

Alpha68%

[Manifest](</id/plugins/manifest>), [Pengujian Langsung](</id/help/testing-live>), [Indeks](</id/providers>)

Operasi Penyedia 12 kemampuan

Eksperimental0%

Alpha61%

Alpha68%

[Indeks](</id/providers>), [Penyedia Model](</id/concepts/model-providers>), [Manifest](</id/plugins/manifest>), [Pengujian Langsung](</id/help/testing-live>), [Model](</id/cli/models>)

Was this useful?YesNo

Open issue