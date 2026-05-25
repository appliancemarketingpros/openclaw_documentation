---
title: Secret
source_url: https://docs.openclaw.ai/id/cli/secrets
scraped_at: 2026-05-25
---

# `openclaw secrets`

Gunakan `openclaw secrets` untuk mengelola SecretRef dan menjaga snapshot runtime aktif tetap sehat.

Peran perintah:

  * `reload`: RPC gateway (`secrets.reload`) yang me-resolve ulang ref dan menukar snapshot runtime hanya jika seluruh proses berhasil (tanpa penulisan config).
  * `audit`: pemindaian read-only terhadap store config/auth/model yang dihasilkan dan residu lama untuk plaintext, ref yang tidak ter-resolve, dan drift prioritas (ref exec dilewati kecuali `--allow-exec` diatur).
  * `configure`: planner interaktif untuk penyiapan provider, pemetaan target, dan preflight (memerlukan TTY).
  * `apply`: jalankan rencana yang disimpan (`--dry-run` hanya untuk validasi; dry-run melewati pemeriksaan exec secara default, dan mode tulis menolak rencana yang berisi exec kecuali `--allow-exec` diatur), lalu scrub residu plaintext yang ditargetkan.


Loop operator yang direkomendasikan:

bashCopy code
[code]
    openclaw secrets audit --checkopenclaw secrets configureopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-runopenclaw secrets apply --from /tmp/openclaw-secrets-plan.jsonopenclaw secrets audit --checkopenclaw secrets reload
[/code]

Jika rencana Anda mencakup SecretRef/provider `exec`, berikan `--allow-exec` pada perintah apply dry-run maupun write.

Catatan exit code untuk CI/gate:

  * `audit --check` mengembalikan `1` jika ada temuan.
  * ref yang tidak ter-resolve mengembalikan `2`.


Terkait:

  * Panduan secret: [Manajemen Secret](</id/gateway/secrets>)
  * Surface kredensial: [Surface Kredensial SecretRef](</id/reference/secretref-credential-surface>)
  * Panduan keamanan: [Keamanan](</id/gateway/security>)


## Muat ulang snapshot runtime

Me-resolve ulang ref secret dan menukar snapshot runtime secara atomik.

bashCopy code
[code]
    openclaw secrets reloadopenclaw secrets reload --jsonopenclaw secrets reload --url ws://127.0.0.1:18789 --token <token>
[/code]

Catatan:

  * Menggunakan metode RPC gateway `secrets.reload`.
  * Jika resolusi gagal, gateway mempertahankan snapshot terakhir yang diketahui baik dan mengembalikan error (tanpa aktivasi parsial).
  * Respons JSON mencakup `warningCount`.


Opsi:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--json`


## Audit

Pindai state OpenClaw untuk:

  * penyimpanan secret plaintext
  * ref yang tidak ter-resolve
  * drift prioritas (kredensial `auth-profiles.json` yang membayangi ref `openclaw.json`)
  * residu `agents/*/agent/models.json` yang dihasilkan (nilai provider `apiKey` dan header provider sensitif)
  * residu lama (entri store auth lama, pengingat OAuth)


Catatan residu header:

  * Deteksi header provider sensitif berbasis heuristik nama (nama header auth/kredensial umum dan fragmen seperti `authorization`, `x-api-key`, `token`, `secret`, `password`, dan `credential`).

bashCopy code
[code]
    openclaw secrets auditopenclaw secrets audit --checkopenclaw secrets audit --jsonopenclaw secrets audit --allow-exec
[/code]

Perilaku exit:

  * `--check` keluar non-zero jika ada temuan.
  * ref yang tidak ter-resolve keluar dengan kode non-zero prioritas lebih tinggi.


Sorotan bentuk laporan:

  * `status`: `clean | findings | unresolved`
  * `resolution`: `refsChecked`, `skippedExecRefs`, `resolvabilityComplete`
  * `summary`: `plaintextCount`, `unresolvedRefCount`, `shadowedRefCount`, `legacyResidueCount`
  * kode temuan: 
    * `PLAINTEXT_FOUND`
    * `REF_UNRESOLVED`
    * `REF_SHADOWED`
    * `LEGACY_RESIDUE`


## Configure (helper interaktif)

Bangun perubahan provider dan SecretRef secara interaktif, jalankan preflight, dan secara opsional terapkan:

bashCopy code
[code]
    openclaw secrets configureopenclaw secrets configure --plan-out /tmp/openclaw-secrets-plan.jsonopenclaw secrets configure --apply --yesopenclaw secrets configure --providers-onlyopenclaw secrets configure --skip-provider-setupopenclaw secrets configure --agent opsopenclaw secrets configure --json
[/code]

Alur:

  * Penyiapan provider terlebih dahulu (`add/edit/remove` untuk alias `secrets.providers`).
  * Pemetaan kredensial kedua (pilih field dan tetapkan ref `{source, provider, id}`).
  * Preflight dan apply opsional terakhir.


Flag:

  * `--providers-only`: konfigurasikan hanya `secrets.providers`, lewati pemetaan kredensial.
  * `--skip-provider-setup`: lewati penyiapan provider dan petakan kredensial ke provider yang ada.
  * `--agent <id>`: cakup penemuan target `auth-profiles.json` dan penulisan ke satu store agen.
  * `--allow-exec`: izinkan pemeriksaan SecretRef exec selama preflight/apply (dapat mengeksekusi perintah provider).


Catatan:

  * Memerlukan TTY interaktif.
  * Anda tidak dapat menggabungkan `--providers-only` dengan `--skip-provider-setup`.
  * `configure` menargetkan field yang mengandung secret di `openclaw.json` plus `auth-profiles.json` untuk cakupan agen yang dipilih.
  * `configure` mendukung pembuatan pemetaan `auth-profiles.json` baru secara langsung di alur picker.
  * Surface kanonis yang didukung: [Surface Kredensial SecretRef](</id/reference/secretref-credential-surface>).
  * Perintah ini menjalankan resolusi preflight sebelum apply.
  * Jika preflight/apply mencakup ref exec, biarkan `--allow-exec` tetap aktif pada kedua langkah.
  * Rencana yang dihasilkan secara default menggunakan opsi scrub (`scrubEnv`, `scrubAuthProfilesForProviderTargets`, `scrubLegacyAuthJson` semuanya aktif).
  * Jalur apply bersifat satu arah untuk nilai plaintext yang telah discrub.
  * Tanpa `--apply`, CLI tetap menampilkan prompt `Apply this plan now?` setelah preflight.
  * Dengan `--apply` (dan tanpa `--yes`), CLI menampilkan konfirmasi tambahan yang tidak dapat dibatalkan.
  * `--json` mencetak rencana + laporan preflight, tetapi perintah ini tetap memerlukan TTY interaktif.


Catatan keamanan provider exec:

  * Instalasi Homebrew sering mengekspos binary symlink di bawah `/opt/homebrew/bin/*`.
  * Atur `allowSymlinkCommand: true` hanya jika diperlukan untuk path package manager tepercaya, dan pasangkan dengan `trustedDirs` (misalnya `["/opt/homebrew"]`).
  * Di Windows, jika verifikasi ACL tidak tersedia untuk path provider, OpenClaw gagal tertutup. Hanya untuk path tepercaya, atur `allowInsecurePath: true` pada provider tersebut untuk melewati pemeriksaan keamanan path.


## Terapkan rencana yang disimpan

Terapkan atau preflight rencana yang sebelumnya telah dibuat:

bashCopy code
[code]
    openclaw secrets apply --from /tmp/openclaw-secrets-plan.jsonopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-runopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --json
[/code]

Perilaku exec:

  * `--dry-run` memvalidasi preflight tanpa menulis file.
  * Pemeriksaan SecretRef exec dilewati secara default dalam dry-run.
  * Mode tulis menolak rencana yang berisi SecretRef/provider exec kecuali `--allow-exec` diatur.
  * Gunakan `--allow-exec` untuk ikut serta dalam pemeriksaan/eksekusi provider exec pada salah satu mode.


Detail kontrak rencana (path target yang diizinkan, aturan validasi, dan semantik kegagalan):

  * [Kontrak Rencana Apply Secret](</id/gateway/secrets-plan-contract>)


Yang dapat diperbarui oleh `apply`:

  * `openclaw.json` (target SecretRef + upsert/delete provider)
  * `auth-profiles.json` (scrub target provider)
  * residu `auth.json` lama
  * kunci secret yang dikenal di `~/.openclaw/.env` yang nilainya telah dimigrasikan


## Mengapa tidak ada backup rollback

`secrets apply` sengaja tidak menulis backup rollback yang berisi nilai plaintext lama.

Keamanan berasal dari preflight yang ketat + apply yang hampir atomik dengan pemulihan in-memory best-effort saat gagal.

## Contoh

bashCopy code
[code]
    openclaw secrets audit --checkopenclaw secrets configureopenclaw secrets audit --check
[/code]

Jika `audit --check` masih melaporkan temuan plaintext, perbarui path target yang masih dilaporkan dan jalankan ulang audit.

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Manajemen secret](</id/gateway/secrets>)


Was this useful?YesNo