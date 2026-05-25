---
title: Inisialisasi agen
source_url: https://docs.openclaw.ai/id/start/bootstrapping
scraped_at: 2026-05-25
---

Inisialisasi awal adalah ritual **eksekusi pertama** yang menyiapkan ruang kerja agen dan mengumpulkan detail identitas. Ini terjadi setelah orientasi awal, saat agen dimulai untuk pertama kalinya.

## Apa yang dilakukan inisialisasi awal

Pada eksekusi agen pertama, OpenClaw menginisialisasi ruang kerja (default `~/.openclaw/workspace`):

  * Mengisi `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Menjalankan ritual tanya jawab singkat (satu pertanyaan setiap kali).
  * Menulis identitas + preferensi ke `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Menghapus `BOOTSTRAP.md` setelah selesai sehingga hanya berjalan sekali.


Untuk eksekusi model tersemat/lokal, OpenClaw menjaga `BOOTSTRAP.md` tetap di luar konteks sistem yang diberi hak istimewa. Pada eksekusi pertama interaktif utama, OpenClaw tetap meneruskan isi file dalam prompt pengguna agar model yang tidak selalu memanggil alat `read` dapat menyelesaikan ritual. Jika eksekusi saat ini tidak dapat mengakses ruang kerja dengan aman, agen menerima catatan inisialisasi awal terbatas alih-alih sapaan generik.

## Melewati inisialisasi awal

Untuk melewati ini bagi ruang kerja yang sudah diisi sebelumnya, jalankan `openclaw onboard --skip-bootstrap`.

## Tempat ini dijalankan

Inisialisasi awal selalu berjalan di **host gateway**. Jika aplikasi macOS terhubung ke Gateway jarak jauh, ruang kerja dan file inisialisasi awal berada di mesin jarak jauh tersebut.

## Dokumen terkait

  * Orientasi awal aplikasi macOS: [Orientasi awal](</id/start/onboarding>)
  * Tata letak ruang kerja: [Ruang kerja agen](</id/concepts/agent-workspace>)


Was this useful?YesNo