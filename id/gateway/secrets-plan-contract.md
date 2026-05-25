---
title: Kontrak rencana penerapan Secrets
source_url: https://docs.openclaw.ai/id/gateway/secrets-plan-contract
scraped_at: 2026-05-25
---

Halaman ini mendefinisikan kontrak ketat yang ditegakkan oleh `openclaw secrets apply`.

Jika sebuah target tidak cocok dengan aturan ini, apply gagal sebelum memutasi konfigurasi.

## Bentuk file plan

`openclaw secrets apply --from <plan.json>` mengharapkan array `targets` berisi target plan:

json5Copy code
[code]
    {  version: 1,  protocolVersion: 1,  targets: [    {      type: "models.providers.apiKey",      path: "models.providers.openai.apiKey",      pathSegments: ["models", "providers", "openai", "apiKey"],      providerId: "openai",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },    {      type: "auth-profiles.api_key.key",      path: "profiles.openai:default.key",      pathSegments: ["profiles", "openai:default", "key"],      agentId: "main",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },  ],}
[/code]

## Cakupan target yang didukung

Target plan diterima untuk path kredensial yang didukung di:

  * [Permukaan Kredensial SecretRef](</id/reference/secretref-credential-surface>)


## Perilaku jenis target

Aturan umum:

  * `target.type` harus dikenali dan harus cocok dengan bentuk `target.path` yang dinormalisasi.


Alias kompatibilitas tetap diterima untuk plan yang sudah ada:

  * `models.providers.apiKey`
  * `skills.entries.apiKey`
  * `channels.googlechat.serviceAccount`


## Aturan validasi path

Setiap target divalidasi dengan semua hal berikut:

  * `type` harus berupa jenis target yang dikenali.
  * `path` harus berupa dot path yang tidak kosong.
  * `pathSegments` boleh dihilangkan. Jika diberikan, nilainya harus dinormalisasi ke path yang persis sama dengan `path`.
  * Segmen terlarang ditolak: `__proto__`, `prototype`, `constructor`.
  * Path yang dinormalisasi harus cocok dengan bentuk path terdaftar untuk jenis target tersebut.
  * Jika `providerId` atau `accountId` diatur, nilainya harus cocok dengan id yang dienkode di path.
  * Target `auth-profiles.json` memerlukan `agentId`.
  * Saat membuat pemetaan `auth-profiles.json` baru, sertakan `authProfileProvider`.


## Perilaku kegagalan

Jika sebuah target gagal validasi, apply keluar dengan error seperti:

textCopy code
[code]
    Invalid plan target path for models.providers.apiKey: models.providers.openai.baseUrl
[/code]

Tidak ada penulisan yang dikomit untuk plan yang tidak valid.

## Perilaku persetujuan provider exec

  * `--dry-run` melewati pemeriksaan SecretRef exec secara default.
  * Plan yang berisi SecretRef/provider exec ditolak dalam mode tulis kecuali `--allow-exec` diatur.
  * Saat memvalidasi/menerapkan plan yang berisi exec, berikan `--allow-exec` pada perintah dry-run maupun perintah tulis.


## Catatan cakupan runtime dan audit

  * Entri `auth-profiles.json` ref-only (`keyRef`/`tokenRef`) disertakan dalam resolusi runtime dan cakupan audit.
  * `secrets apply` menulis target `openclaw.json` yang didukung, target `auth-profiles.json` yang didukung, dan target scrub opsional.


## Pemeriksaan operator

bashCopy code
[code]
    # Validasi plan tanpa penulisanopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run # Lalu terapkan sungguhanopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json # Untuk plan yang berisi exec, pilih masuk secara eksplisit di kedua modeopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
[/code]

Jika apply gagal dengan pesan invalid target path, buat ulang plan dengan `openclaw secrets configure` atau perbaiki path target ke bentuk yang didukung di atas.

## Dokumen terkait

  * [Manajemen Secrets](</id/gateway/secrets>)
  * [CLI `secrets`](</id/cli/secrets>)
  * [Permukaan Kredensial SecretRef](</id/reference/secretref-credential-surface>)
  * [Referensi Konfigurasi](</id/gateway/configuration-reference>)


Was this useful?YesNo