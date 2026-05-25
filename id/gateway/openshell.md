---
title: OpenShell
source_url: https://docs.openclaw.ai/id/gateway/openshell
scraped_at: 2026-05-25
---

OpenShell adalah backend sandbox terkelola untuk OpenClaw. Alih-alih menjalankan kontainer Docker secara lokal, OpenClaw mendelegasikan siklus hidup sandbox ke CLI `openshell`, yang menyediakan lingkungan jarak jauh dengan eksekusi perintah berbasis SSH.

Plugin OpenShell menggunakan kembali transport SSH inti dan bridge sistem berkas jarak jauh yang sama seperti [backend SSH](</id/gateway/sandboxing#ssh-backend>) generik. Plugin ini menambahkan siklus hidup khusus OpenShell (`sandbox create/get/delete`, `sandbox ssh-config`) dan mode workspace `mirror` opsional.

## Prasyarat

  * CLI `openshell` terinstal dan ada di `PATH` (atau tetapkan jalur kustom melalui `plugins.entries.openshell.config.command`)
  * Akun OpenShell dengan akses sandbox
  * OpenClaw Gateway berjalan di host


## Mulai cepat

  1. Aktifkan Plugin dan tetapkan backend sandbox:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "session",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote",        },      },    },  },}
[/code]

  2. Mulai ulang Gateway. Pada giliran agen berikutnya, OpenClaw membuat sandbox OpenShell dan merutekan eksekusi alat melaluinya.

  3. Verifikasi:


bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox explain
[/code]

## Mode workspace

Ini adalah keputusan paling penting saat menggunakan OpenShell.

### `mirror`

Gunakan `plugins.entries.openshell.config.mode: "mirror"` saat Anda ingin **workspace lokal tetap menjadi kanonik**.

Perilaku:

  * Sebelum `exec`, OpenClaw menyinkronkan workspace lokal ke sandbox OpenShell.
  * Setelah `exec`, OpenClaw menyinkronkan workspace jarak jauh kembali ke workspace lokal.
  * Alat berkas tetap beroperasi melalui bridge sandbox, tetapi workspace lokal tetap menjadi sumber kebenaran antar giliran.


Paling sesuai untuk:

  * Anda mengedit berkas secara lokal di luar OpenClaw dan ingin perubahan tersebut terlihat di sandbox secara otomatis.
  * Anda ingin sandbox OpenShell berperilaku semirip mungkin dengan backend Docker.
  * Anda ingin workspace host mencerminkan penulisan sandbox setelah setiap giliran exec.


Konsekuensi: biaya sinkronisasi tambahan sebelum dan setelah setiap exec.

### `remote`

Gunakan `plugins.entries.openshell.config.mode: "remote"` saat Anda ingin **workspace OpenShell menjadi kanonik**.

Perilaku:

  * Saat sandbox pertama kali dibuat, OpenClaw mengisi workspace jarak jauh dari workspace lokal satu kali.
  * Setelah itu, `exec`, `read`, `write`, `edit`, dan `apply_patch` beroperasi langsung terhadap workspace OpenShell jarak jauh.
  * OpenClaw **tidak** menyinkronkan perubahan jarak jauh kembali ke workspace lokal.
  * Pembacaan media saat prompt tetap berfungsi karena alat berkas dan media membaca melalui bridge sandbox.


Paling sesuai untuk:

  * Sandbox seharusnya terutama berada di sisi jarak jauh.
  * Anda menginginkan overhead sinkronisasi per giliran yang lebih rendah.
  * Anda tidak ingin pengeditan lokal host diam-diam menimpa status sandbox jarak jauh.


### Memilih mode

| `mirror` | `remote`  
---|---|---  
**Workspace kanonik** | Host lokal | OpenShell jarak jauh  
**Arah sinkronisasi** | Dua arah (setiap exec) | Pengisian satu kali  
**Overhead per giliran** | Lebih tinggi (unggah + unduh) | Lebih rendah (operasi langsung jarak jauh)  
**Edit lokal terlihat?** | Ya, pada exec berikutnya | Tidak, hingga dibuat ulang  
**Paling sesuai untuk** | Alur kerja pengembangan | Agen jangka panjang, CI  
  
## Referensi konfigurasi

Semua konfigurasi OpenShell berada di bawah `plugins.entries.openshell.config`:

Kunci | Tipe | Default | Deskripsi  
---|---|---|---  
`mode` | `"mirror"` or `"remote"` | `"mirror"` | Mode sinkronisasi workspace  
`command` | `string` | `"openshell"` | Jalur atau nama CLI `openshell`  
`from` | `string` | `"openclaw"` | Sumber sandbox untuk pembuatan pertama kali  
`gateway` | `string` | — | Nama Gateway OpenShell (`--gateway`)  
`gatewayEndpoint` | `string` | — | URL endpoint Gateway OpenShell (`--gateway-endpoint`)  
`policy` | `string` | — | ID kebijakan OpenShell untuk pembuatan sandbox  
`providers` | `string[]` | `[]` | Nama penyedia yang dilampirkan saat sandbox dibuat  
`gpu` | `boolean` | `false` | Meminta sumber daya GPU  
`autoProviders` | `boolean` | `true` | Meneruskan `--auto-providers` selama pembuatan sandbox  
`remoteWorkspaceDir` | `string` | `"/sandbox"` | Workspace utama yang dapat ditulis di dalam sandbox  
`remoteAgentWorkspaceDir` | `string` | `"/agent"` | Jalur mount workspace agen (untuk akses baca-saja)  
`timeoutSeconds` | `number` | `120` | Timeout untuk operasi CLI `openshell`  
  
Pengaturan tingkat sandbox (`mode`, `scope`, `workspaceAccess`) dikonfigurasi di bawah `agents.defaults.sandbox` seperti backend lainnya. Lihat [Sandboxing](</id/gateway/sandboxing>) untuk matriks lengkap.

## Contoh

### Penyiapan jarak jauh minimal

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote",        },      },    },  },}
[/code]

### Mode mirror dengan GPU

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "agent",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "mirror",          gpu: true,          providers: ["openai"],          timeoutSeconds: 180,        },      },    },  },}
[/code]

### OpenShell per agen dengan Gateway kustom

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: { mode: "off" },    },    list: [      {        id: "researcher",        sandbox: {          mode: "all",          backend: "openshell",          scope: "agent",          workspaceAccess: "rw",        },      },    ],  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote",          gateway: "lab",          gatewayEndpoint: "https://lab.example",          policy: "strict",        },      },    },  },}
[/code]

## Manajemen siklus hidup

Sandbox OpenShell dikelola melalui CLI sandbox normal:

bashCopy code
[code]
    # List all sandbox runtimes (Docker + OpenShell)openclaw sandbox list # Inspect effective policyopenclaw sandbox explain # Recreate (deletes remote workspace, re-seeds on next use)openclaw sandbox recreate --all
[/code]

Untuk mode `remote`, **pembuatan ulang sangat penting** : tindakan ini menghapus workspace jarak jauh kanonik untuk cakupan tersebut. Penggunaan berikutnya mengisi workspace jarak jauh baru dari workspace lokal.

Untuk mode `mirror`, pembuatan ulang terutama mereset lingkungan eksekusi jarak jauh karena workspace lokal tetap kanonik.

### Kapan membuat ulang

Buat ulang setelah mengubah salah satu dari ini:

  * `agents.defaults.sandbox.backend`
  * `plugins.entries.openshell.config.from`
  * `plugins.entries.openshell.config.mode`
  * `plugins.entries.openshell.config.policy`

bashCopy code
[code]
    openclaw sandbox recreate --all
[/code]

## Penguatan keamanan

OpenShell mem-pin fd root workspace dan memeriksa ulang identitas sandbox sebelum setiap pembacaan, sehingga penukaran symlink atau workspace yang di-mount ulang tidak dapat mengalihkan pembacaan keluar dari workspace jarak jauh yang dimaksud.

## Batasan saat ini

  * Browser sandbox tidak didukung pada backend OpenShell.
  * `sandbox.docker.binds` tidak berlaku untuk OpenShell.
  * Kenop runtime khusus Docker di bawah `sandbox.docker.*` hanya berlaku untuk backend Docker.


## Cara kerjanya

  1. OpenClaw memanggil `openshell sandbox create` (dengan flag `--from`, `--gateway`, `--policy`, `--providers`, `--gpu` sebagaimana dikonfigurasi).
  2. OpenClaw memanggil `openshell sandbox ssh-config <name>` untuk mendapatkan detail koneksi SSH untuk sandbox.
  3. Core menulis konfigurasi SSH ke berkas temp dan membuka sesi SSH menggunakan bridge sistem berkas jarak jauh yang sama seperti backend SSH generik.
  4. Dalam mode `mirror`: sinkronkan lokal ke jarak jauh sebelum exec, jalankan, lalu sinkronkan kembali setelah exec.
  5. Dalam mode `remote`: isi satu kali saat dibuat, lalu beroperasi langsung pada workspace jarak jauh.


## Terkait

  * [Sandboxing](</id/gateway/sandboxing>) \-- mode, cakupan, dan perbandingan backend
  * [Sandbox vs Tool Policy vs Elevated](</id/gateway/sandbox-vs-tool-policy-vs-elevated>) \-- men-debug alat yang diblokir
  * [Sandbox Multi-Agen dan Alat](</id/tools/multi-agent-sandbox-tools>) \-- override per agen
  * [CLI Sandbox](</id/cli/sandbox>) \-- perintah `openclaw sandbox`


Was this useful?YesNo