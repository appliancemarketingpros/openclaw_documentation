---
title: CLI Kotak Pasir
source_url: https://docs.openclaw.ai/id/cli/sandbox
scraped_at: 2026-05-25
---

Kelola runtime sandbox untuk eksekusi agen yang terisolasi.

## Ringkasan

OpenClaw dapat menjalankan agen dalam runtime sandbox terisolasi untuk keamanan. Perintah `sandbox` membantu Anda memeriksa dan membuat ulang runtime tersebut setelah pembaruan atau perubahan konfigurasi.

Saat ini biasanya berarti:

  * Kontainer sandbox Docker
  * Runtime sandbox SSH saat `agents.defaults.sandbox.backend = "ssh"`
  * Runtime sandbox OpenShell saat `agents.defaults.sandbox.backend = "openshell"`


Untuk `ssh` dan OpenShell `remote`, pembuatan ulang lebih penting dibandingkan dengan Docker:

  * workspace jarak jauh menjadi kanonis setelah seed awal
  * `openclaw sandbox recreate` menghapus workspace jarak jauh kanonis tersebut untuk cakupan yang dipilih
  * penggunaan berikutnya melakukan seed ulang dari workspace lokal saat ini


## Perintah

### `openclaw sandbox explain`

Periksa mode/cakupan/akses workspace sandbox **efektif** , kebijakan tool sandbox, dan gate yang ditinggikan (dengan jalur kunci konfigurasi untuk perbaikan).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Cantumkan semua runtime sandbox beserta status dan konfigurasinya.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**Output mencakup:**

  * Nama dan status runtime
  * Backend (`docker`, `openshell`, dll.)
  * Label konfigurasi dan apakah cocok dengan konfigurasi saat ini
  * Usia (waktu sejak dibuat)
  * Waktu menganggur (waktu sejak terakhir digunakan)
  * Sesi/agen terkait


### `openclaw sandbox recreate`

Hapus runtime sandbox untuk memaksa pembuatan ulang dengan konfigurasi yang diperbarui.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Opsi:**

  * `--all`: Buat ulang semua kontainer sandbox
  * `--session <key>`: Buat ulang kontainer untuk sesi tertentu
  * `--agent <id>`: Buat ulang kontainer untuk agen tertentu
  * `--browser`: Hanya buat ulang kontainer browser
  * `--force`: Lewati prompt konfirmasi


## Kasus penggunaan

### Setelah memperbarui image Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### Setelah mengubah konfigurasi sandbox

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### Setelah mengubah target SSH atau materi auth SSH

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Untuk backend inti `ssh`, pembuatan ulang menghapus root workspace jarak jauh per cakupan pada target SSH. Run berikutnya melakukan seed ulang dari workspace lokal.

### Setelah mengubah sumber, kebijakan, atau mode OpenShell

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

Untuk mode OpenShell `remote`, pembuatan ulang menghapus workspace jarak jauh kanonis untuk cakupan tersebut. Run berikutnya melakukan seed ulang dari workspace lokal.

### Setelah mengubah setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Hanya untuk agen tertentu

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Mengapa ini diperlukan

Saat Anda memperbarui konfigurasi sandbox:

  * Runtime yang ada tetap berjalan dengan pengaturan lama.
  * Runtime hanya dipangkas setelah 24 jam tidak aktif.
  * Agen yang digunakan secara rutin mempertahankan runtime lama tanpa batas.


Gunakan `openclaw sandbox recreate` untuk memaksa penghapusan runtime lama. Runtime tersebut dibuat ulang secara otomatis dengan pengaturan saat ini saat berikutnya dibutuhkan.

## Migrasi registry

OpenClaw menyimpan metadata runtime sandbox sebagai satu shard JSON per entri kontainer/browser di bawah direktori status sandbox. Instalasi lama mungkin masih memiliki file legacy monolitik:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


Pembacaan runtime sandbox reguler tidak menulis ulang file tersebut. Jalankan `openclaw doctor --fix` untuk memigrasikan entri legacy yang valid ke direktori registry bershard. File legacy yang tidak valid dikarantina sehingga satu registry lama yang buruk tidak dapat menyembunyikan entri runtime saat ini.

## Konfigurasi

Pengaturan sandbox berada di `~/.openclaw/openclaw.json` di bawah `agents.defaults.sandbox` (override per agen berada di `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Sandboxing](</id/gateway/sandboxing>)
  * [Workspace agen](</id/concepts/agent-workspace>)
  * [Doctor](</id/gateway/doctor>): memeriksa setup sandbox.


Was this useful?YesNo