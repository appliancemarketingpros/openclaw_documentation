---
title: Bermigrasi dari Hermes
source_url: https://docs.openclaw.ai/id/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw mengimpor state Hermes melalui penyedia migrasi bawaan. Penyedia ini meninjau semuanya sebelum mengubah state, menyamarkan secret dalam rencana dan laporan, serta membuat backup terverifikasi sebelum apply.

## Dua cara untuk mengimpor

### Wizard onboarding

Jalur tercepat. Wizard mendeteksi Hermes di `~/.hermes` dan menampilkan pratinjau sebelum menerapkan.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Atau arahkan ke sumber tertentu:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Gunakan `openclaw migrate` untuk eksekusi berskrip atau berulang. Lihat [`openclaw migrate`](</id/cli/migrate>) untuk referensi lengkap.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Tambahkan `--from <path>` saat Hermes berada di luar `~/.hermes`.

## Apa yang diimpor

Konfigurasi model

  * Pilihan model default dari Hermes `config.yaml`.
  * Penyedia model yang dikonfigurasi dan endpoint kustom yang kompatibel dengan OpenAI dari `providers` dan `custom_providers`.

Server MCP

Definisi server MCP dari `mcp_servers` atau `mcp.servers`.

File workspace

  * `SOUL.md` dan `AGENTS.md` disalin ke workspace agen OpenClaw.
  * `memories/MEMORY.md` dan `memories/USER.md` **ditambahkan** ke file memori OpenClaw yang sesuai, bukan menimpanya.

Konfigurasi memori

Default config memori untuk memori file OpenClaw. Penyedia memori eksternal seperti Honcho dicatat sebagai item arsip atau tinjauan manual agar Anda dapat memindahkannya secara sengaja.

Skills

Skills dengan file `SKILL.md` di bawah `skills/<name>/` disalin, bersama dengan nilai config per skill dari `skills.config`.

Kunci API (ikut serta)

Atur `--include-secrets` untuk mengimpor kunci `.env` yang didukung: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Tanpa flag tersebut, secret tidak pernah disalin.

## Yang tetap hanya diarsipkan

Penyedia menyalin ini ke direktori laporan migrasi untuk tinjauan manual, tetapi **tidak** memuatnya ke config atau credentials OpenClaw live:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw menolak mengeksekusi atau memercayai state ini secara otomatis karena format dan asumsi kepercayaan dapat bergeser antar sistem. Pindahkan yang Anda butuhkan secara manual setelah meninjau arsip.

## Alur yang direkomendasikan

* ### Tinjau rencana

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Rencana mencantumkan semua hal yang akan berubah, termasuk konflik, item yang dilewati, dan item sensitif apa pun. Output rencana menyamarkan kunci bertingkat yang tampak seperti secret.

* ### Terapkan dengan backup

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw membuat dan memverifikasi backup sebelum menerapkan. Jika Anda perlu mengimpor kunci API, tambahkan `--include-secrets`.

* ### Jalankan doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</id/gateway/doctor>) menerapkan ulang migrasi config yang tertunda dan memeriksa masalah yang muncul selama impor.

* ### Restart dan verifikasi

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Pastikan Gateway sehat dan model, memori, serta skills yang diimpor sudah dimuat.

## Penanganan konflik

Apply menolak melanjutkan saat rencana melaporkan konflik (file atau nilai config sudah ada di target).

Untuk instalasi OpenClaw baru, konflik jarang terjadi. Konflik biasanya muncul saat Anda menjalankan ulang impor pada setup yang sudah memiliki editan pengguna.

Jika konflik muncul di tengah apply (misalnya, race tak terduga pada file config), Hermes menandai item config dependen yang tersisa sebagai `skipped` dengan alasan `blocked by earlier apply conflict`, bukan menulisnya sebagian. Laporan migrasi mencatat setiap item yang diblokir agar Anda dapat menyelesaikan konflik asal dan menjalankan ulang impor.

## Secret

Secret tidak pernah diimpor secara default.

  * Jalankan `openclaw migrate apply hermes --yes` terlebih dahulu untuk mengimpor state non-secret.
  * Jika Anda juga ingin kunci `.env` yang didukung disalin, jalankan ulang dengan `--include-secrets`.
  * Untuk credentials yang dikelola SecretRef, konfigurasikan sumber SecretRef setelah impor selesai.


## Output JSON untuk otomasi

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Dengan `--json` dan tanpa `--yes`, apply mencetak rencana dan tidak mengubah state. Ini adalah mode paling aman untuk CI dan skrip bersama.

## Pemecahan masalah

Apply menolak dengan konflik

Periksa output rencana. Setiap konflik mengidentifikasi path sumber dan target yang sudah ada. Putuskan per item apakah akan melewati, mengedit target, atau menjalankan ulang dengan `--overwrite`.

Hermes berada di luar ~/.hermes

Berikan `--from /actual/path` (CLI) atau `--import-source /actual/path` (onboarding).

Onboarding menolak mengimpor pada setup yang sudah ada

Impor onboarding memerlukan setup baru. Reset state dan lakukan onboarding ulang, atau gunakan `openclaw migrate apply hermes` secara langsung, yang mendukung `--overwrite` dan kontrol backup eksplisit.

Kunci API tidak terimpor

`--include-secrets` wajib digunakan, dan hanya kunci yang tercantum di atas yang dikenali. Variabel lain di `.env` diabaikan.

## Terkait

  * [`openclaw migrate`](</id/cli/migrate>): referensi CLI lengkap, kontrak Plugin, dan bentuk JSON.
  * [Onboarding](</id/cli/onboard>): alur wizard dan flag non-interaktif.
  * [Migrasi](</id/install/migrating>): memindahkan instalasi OpenClaw antar mesin.
  * [Doctor](</id/gateway/doctor>): pemeriksaan kesehatan pascamigrasi.
  * [Workspace agen](</id/concepts/agent-workspace>): tempat `SOUL.md`, `AGENTS.md`, dan file memori berada.


Was this useful?YesNo