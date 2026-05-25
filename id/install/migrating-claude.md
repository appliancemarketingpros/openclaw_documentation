---
title: Bermigrasi dari Claude
source_url: https://docs.openclaw.ai/id/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw mengimpor state Claude lokal melalui penyedia migrasi Claude bawaan. Penyedia menampilkan pratinjau setiap item sebelum mengubah state, menyamarkan rahasia dalam rencana dan laporan, serta membuat cadangan terverifikasi sebelum diterapkan.

## Dua cara untuk mengimpor

### Wizard onboarding

Wizard menawarkan Claude saat mendeteksi state Claude lokal.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Atau arahkan ke sumber tertentu:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Gunakan `openclaw migrate` untuk eksekusi berskrip atau berulang. Lihat [`openclaw migrate`](</id/cli/migrate>) untuk referensi lengkap.

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Tambahkan `--from <path>` untuk mengimpor home Claude Code atau root proyek tertentu.

## Apa yang diimpor

Instruksi dan memori

  * Konten proyek `CLAUDE.md` dan `.claude/CLAUDE.md` disalin atau ditambahkan ke `AGENTS.md` ruang kerja agen OpenClaw.
  * Konten pengguna `~/.claude/CLAUDE.md` ditambahkan ke `USER.md` ruang kerja.

Server MCP

Definisi server MCP diimpor dari `.mcp.json` proyek, Claude Code `~/.claude.json`, dan Claude Desktop `claude_desktop_config.json` jika ada.

Skills dan perintah

  * Skills Claude dengan file `SKILL.md` disalin ke direktori Skills ruang kerja OpenClaw.
  * File Markdown perintah Claude di bawah `.claude/commands/` atau `~/.claude/commands/` dikonversi menjadi Skills OpenClaw dengan `disable-model-invocation: true`.


## Apa yang tetap hanya arsip

Penyedia menyalin ini ke laporan migrasi untuk peninjauan manual, tetapi **tidak** memuatnya ke konfigurasi OpenClaw aktif:

  * Hook Claude
  * Izin Claude dan allowlist alat yang luas
  * Default lingkungan Claude
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Subagen Claude di bawah `.claude/agents/` atau `~/.claude/agents/`
  * Cache, rencana, dan direktori riwayat proyek Claude Code
  * Ekstensi Claude Desktop dan kredensial yang disimpan OS


OpenClaw menolak menjalankan hook, memercayai allowlist izin, atau mendekode state kredensial OAuth dan Desktop yang buram secara otomatis. Pindahkan yang Anda perlukan secara manual setelah meninjau arsip.

## Pemilihan sumber

Tanpa `--from`, OpenClaw memeriksa home Claude Code default di `~/.claude`, file state Claude Code `~/.claude.json` yang disampel, dan konfigurasi MCP Claude Desktop di macOS.

Saat `--from` menunjuk ke root proyek, OpenClaw hanya mengimpor file Claude proyek tersebut seperti `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/`, dan `.mcp.json`. Itu tidak membaca home Claude global Anda selama impor root proyek.

## Alur yang direkomendasikan

* ### Pratinjau rencana

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

Rencana mencantumkan semua yang akan berubah, termasuk konflik, item yang dilewati, dan nilai sensitif yang disamarkan dari field MCP `env` atau `headers` bersarang.

* ### Terapkan dengan cadangan

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw membuat dan memverifikasi cadangan sebelum menerapkan.

* ### Jalankan doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</id/gateway/doctor>) memeriksa masalah konfigurasi atau state setelah impor.

* ### Mulai ulang dan verifikasi

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Pastikan Gateway sehat dan instruksi, server MCP, serta Skills yang diimpor sudah dimuat.

## Penanganan konflik

Penerapan menolak melanjutkan saat rencana melaporkan konflik (file atau nilai konfigurasi sudah ada di target).

Untuk instalasi OpenClaw baru, konflik jarang terjadi. Konflik biasanya muncul saat Anda menjalankan ulang impor pada penyiapan yang sudah memiliki editan pengguna.

## Output JSON untuk otomatisasi

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

Dengan `--json` dan tanpa `--yes`, penerapan mencetak rencana dan tidak mengubah state. Ini adalah mode paling aman untuk CI dan skrip bersama.

## Pemecahan masalah

State Claude berada di luar ~/.claude

Teruskan `--from /actual/path` (CLI) atau `--import-source /actual/path` (onboarding).

Onboarding menolak mengimpor pada penyiapan yang sudah ada

Impor onboarding memerlukan penyiapan baru. Reset state lalu onboarding ulang, atau gunakan `openclaw migrate apply claude` secara langsung, yang mendukung `--overwrite` dan kontrol cadangan eksplisit.

Server MCP dari Claude Desktop tidak terimpor

Claude Desktop membaca `claude_desktop_config.json` dari path khusus platform. Arahkan `--from` ke direktori file tersebut jika OpenClaw tidak mendeteksinya secara otomatis.

Perintah Claude menjadi Skills dengan pemanggilan model dinonaktifkan

Ini sesuai desain. Perintah Claude dipicu pengguna, jadi OpenClaw mengimpornya sebagai Skills dengan `disable-model-invocation: true`. Edit frontmatter setiap Skill jika Anda ingin agen memanggilnya secara otomatis.

## Terkait

  * [`openclaw migrate`](</id/cli/migrate>): referensi CLI lengkap, kontrak Plugin, dan bentuk JSON.
  * [Panduan migrasi](</id/install/migrating>): semua jalur migrasi.
  * [Bermigrasi dari Hermes](</id/install/migrating-hermes>): jalur impor lintas sistem lainnya.
  * [Onboarding](</id/cli/onboard>): alur wizard dan flag noninteraktif.
  * [Doctor](</id/gateway/doctor>): pemeriksaan kesehatan pascamigrasi.
  * [Ruang kerja agen](</id/concepts/agent-workspace>): tempat `AGENTS.md`, `USER.md`, dan Skills berada.


Was this useful?YesNo