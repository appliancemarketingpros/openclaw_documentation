---
title: Isolasi kotak pasir
source_url: https://docs.openclaw.ai/id/gateway/sandboxing
scraped_at: 2026-05-25
---

OpenClaw dapat menjalankan **alat di dalam backend sandbox** untuk mengurangi jangkauan dampak. Ini **opsional** dan dikontrol oleh konfigurasi (`agents.defaults.sandbox` atau `agents.list[].sandbox`). Jika sandboxing nonaktif, alat berjalan di host. Gateway tetap berada di host; eksekusi alat berjalan di sandbox terisolasi saat diaktifkan.

## Apa yang dimasukkan ke sandbox

  * Eksekusi alat (`exec`, `read`, `write`, `edit`, `apply_patch`, `process`, dll.).
  * Peramban opsional dalam sandbox (`agents.defaults.sandbox.browser`).


Detail peramban dalam sandbox

  * Secara default, peramban sandbox otomatis dimulai (memastikan CDP dapat dijangkau) saat alat peramban membutuhkannya. Konfigurasikan melalui `agents.defaults.sandbox.browser.autoStart` dan `agents.defaults.sandbox.browser.autoStartTimeoutMs`.
  * Secara default, kontainer peramban sandbox menggunakan jaringan Docker khusus (`openclaw-sandbox-browser`) alih-alih jaringan global `bridge`. Konfigurasikan dengan `agents.defaults.sandbox.browser.network`.
  * `agents.defaults.sandbox.browser.cdpSourceRange` opsional membatasi ingress CDP di tepi kontainer dengan allowlist CIDR (misalnya `172.21.0.1/32`).
  * Akses pengamat noVNC dilindungi kata sandi secara default; OpenClaw menerbitkan URL token berumur pendek yang menyajikan halaman bootstrap lokal dan membuka noVNC dengan kata sandi di fragmen URL (bukan log kueri/header).
  * `agents.defaults.sandbox.browser.allowHostControl` memungkinkan sesi dalam sandbox menargetkan peramban host secara eksplisit.
  * Allowlist opsional membatasi `target: "custom"`: `allowedControlUrls`, `allowedControlHosts`, `allowedControlPorts`.


Tidak dimasukkan ke sandbox:

  * Proses Gateway itu sendiri.
  * Alat apa pun yang secara eksplisit diizinkan berjalan di luar sandbox (mis. `tools.elevated`). 
    * **Elevated exec melewati sandboxing dan menggunakan jalur escape yang dikonfigurasi (`gateway` secara default, atau `node` saat target exec adalah `node`).**
    * Jika sandboxing nonaktif, `tools.elevated` tidak mengubah eksekusi (sudah berada di host). Lihat [Mode Elevated](</id/tools/elevated>).


## Mode

`agents.defaults.sandbox.mode` mengontrol **kapan** sandboxing digunakan:

### off

Tidak ada sandboxing.

### non-main

Sandbox hanya sesi **non-main** (default jika Anda ingin obrolan normal berada di host).

`"non-main"` didasarkan pada `session.mainKey` (default `"main"`), bukan id agen. Sesi grup/channel menggunakan kuncinya sendiri, sehingga dihitung sebagai non-main dan akan dimasukkan ke sandbox.

### all

Setiap sesi berjalan di sandbox.

## Cakupan

`agents.defaults.sandbox.scope` mengontrol **berapa banyak kontainer** yang dibuat:

  * `"agent"` (default): satu kontainer per agen.
  * `"session"`: satu kontainer per sesi.
  * `"shared"`: satu kontainer yang dibagikan oleh semua sesi dalam sandbox.


## Backend

`agents.defaults.sandbox.backend` mengontrol **runtime mana** yang menyediakan sandbox:

  * `"docker"` (default saat sandboxing diaktifkan): runtime sandbox lokal berbasis Docker.
  * `"ssh"`: runtime sandbox jarak jauh generik berbasis SSH.
  * `"openshell"`: runtime sandbox berbasis OpenShell.


Konfigurasi khusus SSH berada di bawah `agents.defaults.sandbox.ssh`. Konfigurasi khusus OpenShell berada di bawah `plugins.entries.openshell.config`.

### Memilih backend

| Docker | SSH | OpenShell  
---|---|---|---  
**Tempat berjalan** | Kontainer lokal | Host apa pun yang dapat diakses SSH | Sandbox terkelola OpenShell  
**Penyiapan** | `scripts/sandbox-setup.sh` | Kunci SSH + host target | Plugin OpenShell diaktifkan  
**Model workspace** | Bind-mount atau salin | Remote-canonical (seed sekali) | `mirror` atau `remote`  
**Kontrol jaringan** | `docker.network` (default: none) | Bergantung pada host jarak jauh | Bergantung pada OpenShell  
**Sandbox peramban** | Didukung | Tidak didukung | Belum didukung  
**Bind mount** | `docker.binds` | N/A | N/A  
**Paling cocok untuk** | Dev lokal, isolasi penuh | Memindahkan beban ke mesin jarak jauh | Sandbox jarak jauh terkelola dengan sinkronisasi dua arah opsional  
  
### Backend Docker

Sandboxing nonaktif secara default. Jika Anda mengaktifkan sandboxing dan tidak memilih backend, OpenClaw menggunakan backend Docker. Backend ini mengeksekusi alat dan peramban sandbox secara lokal melalui socket daemon Docker (`/var/run/docker.sock`). Isolasi kontainer sandbox ditentukan oleh namespace Docker.

Untuk mengekspos GPU host ke sandbox Docker, atur `agents.defaults.sandbox.docker.gpus` atau override per agen `agents.list[].sandbox.docker.gpus`. Nilainya diteruskan ke flag `--gpus` milik Docker sebagai argumen terpisah, misalnya `"all"` atau `"device=GPU-uuid"`, dan memerlukan runtime host yang kompatibel seperti NVIDIA Container Toolkit.

### Backend SSH

Gunakan `backend: "ssh"` saat Anda ingin OpenClaw memasukkan `exec`, alat file, dan pembacaan media ke sandbox pada mesin arbitrer yang dapat diakses SSH.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "ssh",        scope: "session",        workspaceAccess: "rw",        ssh: {          target: "user@gateway-host:22",          workspaceRoot: "/tmp/openclaw-sandboxes",          strictHostKeyChecking: true,          updateHostKeys: true,          identityFile: "~/.ssh/id_ed25519",          certificateFile: "~/.ssh/id_ed25519-cert.pub",          knownHostsFile: "~/.ssh/known_hosts",          // Or use SecretRefs / inline contents instead of local files:          // identityData: { source: "env", provider: "default", id: "SSH_IDENTITY" },          // certificateData: { source: "env", provider: "default", id: "SSH_CERTIFICATE" },          // knownHostsData: { source: "env", provider: "default", id: "SSH_KNOWN_HOSTS" },        },      },    },  },}
[/code]

Cara kerjanya

  * OpenClaw membuat root jarak jauh per cakupan di bawah `sandbox.ssh.workspaceRoot`.
  * Pada penggunaan pertama setelah pembuatan atau pembuatan ulang, OpenClaw melakukan seed workspace jarak jauh itu dari workspace lokal sekali.
  * Setelah itu, `exec`, `read`, `write`, `edit`, `apply_patch`, pembacaan media prompt, dan staging media masuk berjalan langsung terhadap workspace jarak jauh melalui SSH.
  * OpenClaw tidak menyinkronkan perubahan jarak jauh kembali ke workspace lokal secara otomatis.

Materi autentikasi

  * `identityFile`, `certificateFile`, `knownHostsFile`: gunakan file lokal yang sudah ada dan teruskan melalui konfigurasi OpenSSH.
  * `identityData`, `certificateData`, `knownHostsData`: gunakan string inline atau SecretRefs. OpenClaw menyelesaikannya melalui snapshot runtime secret normal, menulisnya ke file temp dengan `0600`, dan menghapusnya saat sesi SSH berakhir.
  * Jika `*File` dan `*Data` sama-sama diatur untuk item yang sama, `*Data` menang untuk sesi SSH tersebut.

Konsekuensi remote-canonical

Ini adalah model **remote-canonical**. Workspace SSH jarak jauh menjadi status sandbox sebenarnya setelah seed awal.

  * Edit lokal host yang dibuat di luar OpenClaw setelah langkah seed tidak terlihat dari jarak jauh sampai Anda membuat ulang sandbox.
  * `openclaw sandbox recreate` menghapus root jarak jauh per cakupan dan melakukan seed lagi dari lokal pada penggunaan berikutnya.
  * Sandboxing peramban tidak didukung pada backend SSH.
  * Pengaturan `sandbox.docker.*` tidak berlaku untuk backend SSH.


### Backend OpenShell

Gunakan `backend: "openshell"` saat Anda ingin OpenClaw memasukkan alat ke sandbox di lingkungan jarak jauh yang dikelola OpenShell. Untuk panduan penyiapan lengkap, referensi konfigurasi, dan perbandingan mode workspace, lihat [halaman OpenShell](</id/gateway/openshell>) khusus.

OpenShell menggunakan ulang transport SSH inti dan bridge filesystem jarak jauh yang sama dengan backend SSH generik, serta menambahkan lifecycle khusus OpenShell (`sandbox create/get/delete`, `sandbox ssh-config`) plus mode workspace `mirror` opsional.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "session",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote", // mirror | remote          remoteWorkspaceDir: "/sandbox",          remoteAgentWorkspaceDir: "/agent",        },      },    },  },}
[/code]

Mode OpenShell:

  * `mirror` (default): workspace lokal tetap canonical. OpenClaw menyinkronkan file lokal ke OpenShell sebelum exec dan menyinkronkan workspace jarak jauh kembali setelah exec.
  * `remote`: workspace OpenShell menjadi canonical setelah sandbox dibuat. OpenClaw melakukan seed workspace jarak jauh sekali dari workspace lokal, lalu alat file dan exec berjalan langsung terhadap sandbox jarak jauh tanpa menyinkronkan perubahan kembali.


Detail transport jarak jauh

  * OpenClaw meminta konfigurasi SSH khusus sandbox dari OpenShell melalui `openshell sandbox ssh-config <name>`.
  * Core menulis konfigurasi SSH itu ke file temp, membuka sesi SSH, dan menggunakan ulang bridge filesystem jarak jauh yang sama dengan yang digunakan oleh `backend: "ssh"`.
  * Dalam mode `mirror`, hanya lifecycle yang berbeda: sinkronkan lokal ke jarak jauh sebelum exec, lalu sinkronkan kembali setelah exec.

Batasan OpenShell saat ini

  * peramban sandbox belum didukung
  * `sandbox.docker.binds` tidak didukung pada backend OpenShell
  * knob runtime khusus Docker di bawah `sandbox.docker.*` tetap hanya berlaku untuk backend Docker


#### Mode workspace

OpenShell memiliki dua model workspace. Inilah bagian yang paling penting dalam praktik.

### mirror (local canonical)

Gunakan `plugins.entries.openshell.config.mode: "mirror"` saat Anda ingin **workspace lokal tetap canonical**.

Perilaku:

  * Sebelum `exec`, OpenClaw menyinkronkan workspace lokal ke dalam sandbox OpenShell.
  * Setelah `exec`, OpenClaw menyinkronkan workspace remote kembali ke workspace lokal.
  * Tool file tetap beroperasi melalui bridge sandbox, tetapi workspace lokal tetap menjadi sumber kebenaran antar giliran.


Gunakan ini ketika:

  * Anda mengedit file secara lokal di luar OpenClaw dan ingin perubahan tersebut muncul otomatis di sandbox
  * Anda ingin sandbox OpenShell berperilaku semirip mungkin dengan backend Docker
  * Anda ingin workspace host mencerminkan penulisan sandbox setelah setiap giliran exec


Tradeoff: biaya sinkronisasi tambahan sebelum dan sesudah exec.

### remote (OpenShell canonical)

Gunakan `plugins.entries.openshell.config.mode: "remote"` ketika Anda ingin **workspace OpenShell menjadi kanonis**.

Perilaku:

  * Ketika sandbox pertama kali dibuat, OpenClaw mengisi workspace remote dari workspace lokal satu kali.
  * Setelah itu, `exec`, `read`, `write`, `edit`, dan `apply_patch` beroperasi langsung terhadap workspace OpenShell remote.
  * OpenClaw **tidak** menyinkronkan perubahan remote kembali ke workspace lokal setelah exec.
  * Pembacaan media pada waktu prompt tetap berfungsi karena tool file dan media membaca melalui bridge sandbox alih-alih mengasumsikan path host lokal.
  * Transport menggunakan SSH ke sandbox OpenShell yang dikembalikan oleh `openshell sandbox ssh-config`.


Konsekuensi penting:

  * Jika Anda mengedit file pada host di luar OpenClaw setelah langkah seed, sandbox remote **tidak** akan melihat perubahan tersebut secara otomatis.
  * Jika sandbox dibuat ulang, workspace remote diisi lagi dari workspace lokal.
  * Dengan `scope: "agent"` atau `scope: "shared"`, workspace remote tersebut dibagikan pada cakupan yang sama.


Gunakan ini ketika:

  * sandbox seharusnya terutama berada di sisi OpenShell remote
  * Anda ingin overhead sinkronisasi per giliran yang lebih rendah
  * Anda tidak ingin edit lokal host menimpa status sandbox remote secara diam-diam


Pilih `mirror` jika Anda menganggap sandbox sebagai lingkungan eksekusi sementara. Pilih `remote` jika Anda menganggap sandbox sebagai workspace yang sebenarnya.

#### Siklus hidup OpenShell

Sandbox OpenShell tetap dikelola melalui siklus hidup sandbox normal:

  * `openclaw sandbox list` menampilkan runtime OpenShell sekaligus runtime Docker
  * `openclaw sandbox recreate` menghapus runtime saat ini dan membiarkan OpenClaw membuatnya ulang pada penggunaan berikutnya
  * logika prune juga sadar backend


Untuk mode `remote`, pembuatan ulang sangat penting:

  * recreate menghapus workspace remote kanonis untuk cakupan tersebut
  * penggunaan berikutnya mengisi workspace remote baru dari workspace lokal


Untuk mode `mirror`, recreate terutama mereset lingkungan eksekusi remote karena workspace lokal tetap kanonis.

## Akses workspace

`agents.defaults.sandbox.workspaceAccess` mengontrol **apa yang dapat dilihat sandbox** :

### none (default)

Tool melihat workspace sandbox di bawah `~/.openclaw/sandboxes`.

### ro

Memasang workspace agen hanya-baca di `/agent` (menonaktifkan `write`/`edit`/`apply_patch`).

### rw

Memasang workspace agen baca/tulis di `/workspace`.

Dengan backend OpenShell:

  * mode `mirror` tetap menggunakan workspace lokal sebagai sumber kanonis antar giliran exec
  * mode `remote` menggunakan workspace OpenShell remote sebagai sumber kanonis setelah seed awal
  * `workspaceAccess: "ro"` dan `"none"` tetap membatasi perilaku penulisan dengan cara yang sama


Media masuk disalin ke workspace sandbox aktif (`media/inbound/*`).

## Bind mount kustom

`agents.defaults.sandbox.docker.binds` memasang direktori host tambahan ke dalam kontainer. Format: `host:container:mode` (misalnya, `"/home/user/source:/source:rw"`).

Bind global dan per agen **digabungkan** (bukan diganti). Di bawah `scope: "shared"`, bind per agen diabaikan.

`agents.defaults.sandbox.browser.binds` memasang direktori host tambahan hanya ke dalam kontainer **browser sandbox**.

  * Ketika ditetapkan (termasuk `[]`), ini menggantikan `agents.defaults.sandbox.docker.binds` untuk kontainer browser.
  * Ketika dihilangkan, kontainer browser menggunakan fallback ke `agents.defaults.sandbox.docker.binds` (kompatibel mundur).


Contoh (source hanya-baca + direktori data tambahan):

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"],        },      },    },    list: [      {        id: "build",        sandbox: {          docker: {            binds: ["/mnt/cache:/cache:rw"],          },        },      },    ],  },}
[/code]

## Image dan penyiapan

Image Docker default: `openclaw-sandbox:bookworm-slim`

* ### Build the default image

Dari checkout source:

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

Dari instalasi npm (checkout source tidak diperlukan):

bashCopy code
[code]
    docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'FROM debian:bookworm-slimENV DEBIAN_FRONTEND=noninteractiveRUN apt-get update && apt-get install -y --no-install-recommends \  bash ca-certificates curl git jq python3 ripgrep \  && rm -rf /var/lib/apt/lists/*RUN useradd --create-home --shell /bin/bash sandboxUSER sandboxWORKDIR /home/sandboxCMD ["sleep", "infinity"]DOCKERFILE
[/code]

Image default **tidak** menyertakan Node. Jika sebuah skill membutuhkan Node (atau runtime lain), bake image kustom atau instal melalui `sandbox.docker.setupCommand` (membutuhkan egress jaringan + root yang dapat ditulis + pengguna root).

OpenClaw tidak secara diam-diam mengganti dengan `debian:bookworm-slim` biasa ketika `openclaw-sandbox:bookworm-slim` tidak ada. Run sandbox yang menargetkan image default gagal cepat dengan instruksi build sampai Anda membangunnya, karena image bawaan membawa `python3` untuk helper tulis/edit sandbox.

* ### Optional: build the common image

Untuk image sandbox yang lebih fungsional dengan tooling umum (misalnya `curl`, `jq`, `nodejs`, `python3`, `git`):

Dari checkout source:

bashCopy code
[code]
    scripts/sandbox-common-setup.sh
[/code]

Dari instalasi npm, bangun image default terlebih dahulu (lihat di atas), lalu bangun image umum di atasnya menggunakan [`scripts/docker/sandbox/Dockerfile.common`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.common>) dari repositori.

Lalu tetapkan `agents.defaults.sandbox.docker.image` ke `openclaw-sandbox-common:bookworm-slim`.

* ### Optional: build the sandbox browser image

Dari checkout source:

bashCopy code
[code]
    scripts/sandbox-browser-setup.sh
[/code]

Dari instalasi npm, bangun menggunakan [`scripts/docker/sandbox/Dockerfile.browser`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.browser>) dari repositori.

Secara default, kontainer sandbox Docker berjalan dengan **tanpa jaringan**. Ganti dengan `agents.defaults.sandbox.docker.network`.

Sandbox browser Chromium defaults

Image browser sandbox bawaan juga menerapkan default startup Chromium yang konservatif untuk workload dalam kontainer. Default kontainer saat ini mencakup:

  * `--remote-debugging-address=127.0.0.1`
  * `--remote-debugging-port=<derived from OPENCLAW_BROWSER_CDP_PORT>`
  * `--user-data-dir=${HOME}/.chrome`
  * `--no-first-run`
  * `--no-default-browser-check`
  * `--disable-3d-apis`
  * `--disable-gpu`
  * `--disable-dev-shm-usage`
  * `--disable-background-networking`
  * `--disable-extensions`
  * `--disable-features=TranslateUI`
  * `--disable-breakpad`
  * `--disable-crash-reporter`
  * `--disable-software-rasterizer`
  * `--no-zygote`
  * `--metrics-recording-only`
  * `--renderer-process-limit=2`
  * `--no-sandbox` ketika `noSandbox` diaktifkan.
  * Tiga flag pengerasan grafis (`--disable-3d-apis`, `--disable-software-rasterizer`, `--disable-gpu`) bersifat opsional dan berguna ketika kontainer tidak memiliki dukungan GPU. Tetapkan `OPENCLAW_BROWSER_DISABLE_GRAPHICS_FLAGS=0` jika workload Anda membutuhkan WebGL atau fitur 3D/browser lainnya.
  * `--disable-extensions` diaktifkan secara default dan dapat dinonaktifkan dengan `OPENCLAW_BROWSER_DISABLE_EXTENSIONS=0` untuk alur yang bergantung pada ekstensi.
  * `--renderer-process-limit=2` dikontrol oleh `OPENCLAW_BROWSER_RENDERER_PROCESS_LIMIT=&lt;N&gt;`, dengan `0` mempertahankan default Chromium.


Jika Anda membutuhkan profil runtime yang berbeda, gunakan image browser kustom dan sediakan entrypoint Anda sendiri. Untuk profil Chromium lokal (non-kontainer), gunakan `browser.extraArgs` untuk menambahkan flag startup tambahan.

Network security defaults

  * `network: "host"` diblokir.
  * `network: "container:<id>"` diblokir secara default (risiko bypass join namespace).
  * Override break-glass: `agents.defaults.sandbox.docker.dangerouslyAllowContainerNamespaceJoin: true`.


Instalasi Docker dan gateway dalam kontainer berada di sini: [Docker](</id/install/docker>)

Untuk deployment gateway Docker, `scripts/docker/setup.sh` dapat melakukan bootstrap konfigurasi sandbox. Tetapkan `OPENCLAW_SANDBOX=1` (atau `true`/`yes`/`on`) untuk mengaktifkan path tersebut. Anda dapat mengganti lokasi socket dengan `OPENCLAW_DOCKER_SOCKET`. Referensi penyiapan lengkap dan env: [Docker](</id/install/docker#agent-sandbox>).

## setupCommand (penyiapan kontainer satu kali)

`setupCommand` berjalan **sekali** setelah kontainer sandbox dibuat (bukan pada setiap run). Ini dieksekusi di dalam kontainer melalui `sh -lc`.

Path:

  * Global: `agents.defaults.sandbox.docker.setupCommand`
  * Per agen: `agents.list[].sandbox.docker.setupCommand`


Kendala umum

  * Default `docker.network` adalah `"none"` (tanpa egress), sehingga instalasi paket akan gagal.
  * `docker.network: "container:<id>"` memerlukan `dangerouslyAllowContainerNamespaceJoin: true` dan hanya untuk kondisi darurat.
  * `readOnlyRoot: true` mencegah penulisan; tetapkan `readOnlyRoot: false` atau buat image kustom.
  * `user` harus root untuk instalasi paket (hilangkan `user` atau tetapkan `user: "0:0"`).
  * Exec sandbox **tidak** mewarisi `process.env` host. Gunakan `agents.defaults.sandbox.docker.env` (atau image kustom) untuk kunci API skill.


## Kebijakan tool dan jalur keluar

Kebijakan izinkan/tolak tool tetap berlaku sebelum aturan sandbox. Jika sebuah tool ditolak secara global atau per-agent, sandboxing tidak mengaktifkannya kembali.

`tools.elevated` adalah jalur keluar eksplisit yang menjalankan `exec` di luar sandbox (`gateway` secara default, atau `node` ketika target exec adalah `node`). Direktif `/exec` hanya berlaku untuk pengirim yang diotorisasi dan bertahan per sesi; untuk menonaktifkan `exec` secara tegas, gunakan penolakan kebijakan tool (lihat [Sandbox vs Tool Policy vs Elevated](</id/gateway/sandbox-vs-tool-policy-vs-elevated>)).

Debugging:

  * Gunakan `openclaw sandbox explain` untuk memeriksa mode sandbox efektif, kebijakan tool, dan kunci konfigurasi perbaikan.
  * Lihat [Sandbox vs Tool Policy vs Elevated](</id/gateway/sandbox-vs-tool-policy-vs-elevated>) untuk model mental "mengapa ini diblokir?".


Jaga tetap terkunci.

## Override multi-agent

Setiap agent dapat meng-override sandbox + tools: `agents.list[].sandbox` dan `agents.list[].tools` (ditambah `agents.list[].tools.sandbox.tools` untuk kebijakan tool sandbox). Lihat [Multi-Agent Sandbox & Tools](</id/tools/multi-agent-sandbox-tools>) untuk presedensi.

## Contoh aktivasi minimal

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        scope: "session",        workspaceAccess: "none",      },    },  },}
[/code]

## Terkait

  * [Multi-Agent Sandbox & Tools](</id/tools/multi-agent-sandbox-tools>) — override per-agent dan presedensi
  * [OpenShell](</id/gateway/openshell>) — penyiapan backend sandbox terkelola, mode workspace, dan referensi konfigurasi
  * [Konfigurasi sandbox](</id/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox vs Tool Policy vs Elevated](</id/gateway/sandbox-vs-tool-policy-vs-elevated>) — debugging "mengapa ini diblokir?"
  * [Keamanan](</id/gateway/security>)


Was this useful?YesNo