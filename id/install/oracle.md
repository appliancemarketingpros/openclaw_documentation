---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/id/install/oracle
scraped_at: 2026-05-25
---

Jalankan OpenClaw Gateway persisten di tier ARM **Always Free** Oracle Cloud (hingga 4 OCPU, RAM 24 GB, penyimpanan 200 GB) tanpa biaya.

## Prasyarat

  * Akun Oracle Cloud ([daftar](<https://www.oracle.com/cloud/free/>)) -- lihat [panduan pendaftaran komunitas](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>) jika mengalami masalah
  * Akun Tailscale (gratis di [tailscale.com](<https://tailscale.com>))
  * Sepasang kunci SSH
  * Sekitar 30 menit


## Penyiapan

* ### Buat instance OCI

  1. Masuk ke [Oracle Cloud Console](<https://cloud.oracle.com/>).
  2. Buka **Compute > Instances > Create Instance**.
  3. Konfigurasikan: 
     * **Nama:** `openclaw`
     * **Image:** Ubuntu 24.04 (aarch64)
     * **Shape:** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPU:** 2 (atau hingga 4)
     * **Memori:** 12 GB (atau hingga 24 GB)
     * **Volume boot:** 50 GB (gratis hingga 200 GB)
     * **Kunci SSH:** Tambahkan kunci publik Anda
  4. Klik **Create** dan catat alamat IP publiknya.


* ### Hubungkan dan perbarui sistem

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

`build-essential` diperlukan untuk kompilasi ARM pada beberapa dependensi.

* ### Konfigurasikan pengguna dan hostname

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

Mengaktifkan linger membuat layanan pengguna tetap berjalan setelah logout.

* ### Instal Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

Mulai sekarang, hubungkan melalui Tailscale: `ssh ubuntu@openclaw`.

* ### Instal OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

Saat diminta "How do you want to hatch your bot?", pilih **Lakukan nanti**.

* ### Konfigurasikan Gateway

Gunakan autentikasi token dengan Tailscale Serve untuk akses jarak jauh yang aman.

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` di sini hanya untuk penanganan forwarded-IP/klien-lokal dari proksi Tailscale Serve lokal. Ini **bukan** `gateway.auth.mode: "trusted-proxy"`. Rute penampil diff tetap mempertahankan perilaku fail-closed dalam penyiapan ini: permintaan penampil `127.0.0.1` mentah tanpa header proksi terusan dapat mengembalikan `Diff not found`. Gunakan `mode=file` / `mode=both` untuk lampiran, atau aktifkan penampil jarak jauh secara sengaja dan tetapkan `plugins.entries.diffs.config.viewerBaseUrl` (atau berikan `baseUrl` proksi) jika Anda memerlukan tautan penampil yang dapat dibagikan.

* ### Kunci keamanan VCN

Blokir semua lalu lintas kecuali Tailscale di tepi jaringan:

  1. Buka **Networking > Virtual Cloud Networks** di OCI Console.
  2. Klik VCN Anda, lalu **Security Lists > Default Security List**.
  3. **Hapus** semua aturan ingress kecuali `0.0.0.0/0 UDP 41641` (Tailscale).
  4. Pertahankan aturan egress default (izinkan semua lalu lintas keluar).


Ini memblokir SSH pada port 22, HTTP, HTTPS, dan semua yang lain di tepi jaringan. Mulai titik ini, Anda hanya dapat terhubung melalui Tailscale.

* ### Verifikasi

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

Akses UI Kontrol dari perangkat apa pun di tailnet Anda:

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

Ganti `<tailnet-name>` dengan nama tailnet Anda (terlihat di `tailscale status`).

## Verifikasi postur keamanan

Dengan VCN terkunci (hanya UDP 41641 terbuka) dan Gateway terikat ke loopback, lalu lintas publik diblokir di tepi jaringan dan akses admin hanya melalui tailnet. Ini menghilangkan kebutuhan atas beberapa langkah hardening VPS tradisional:

Langkah tradisional | Diperlukan? | Alasan  
---|---|---  
Firewall UFW | Tidak | VCN memblokir lalu lintas sebelum mencapai instance.  
fail2ban | Tidak | Port 22 diblokir di VCN; tidak ada permukaan brute-force.  
Hardening sshd | Tidak | SSH Tailscale tidak menggunakan sshd.  
Nonaktifkan login root | Tidak | Tailscale mengautentikasi berdasarkan identitas tailnet, bukan pengguna sistem.  
Autentikasi khusus kunci SSH | Tidak | Sama — identitas tailnet menggantikan kunci SSH sistem.  
Hardening IPv6 | Biasanya tidak | Bergantung pada pengaturan VCN/subnet; verifikasi apa yang benar-benar ditetapkan/terekspos.  
  
Tetap direkomendasikan:

  * `chmod 700 ~/.openclaw` untuk membatasi izin file kredensial.
  * `openclaw security audit` untuk pemeriksaan postur khusus OpenClaw.
  * `sudo apt update && sudo apt upgrade` secara berkala untuk patch OS.
  * Tinjau perangkat di [konsol admin Tailscale](<https://login.tailscale.com/admin>) secara berkala.


Perintah verifikasi cepat:

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## Catatan ARM

Tier Always Free menggunakan ARM (`aarch64`). Sebagian besar fitur OpenClaw berfungsi dengan baik; sejumlah kecil biner native memerlukan build ARM:

  * Node.js, Telegram, WhatsApp (Baileys): JavaScript murni, tidak ada masalah.
  * Sebagian besar paket npm dengan kode native: artefak `linux-arm64` pre-built tersedia.
  * Pembantu CLI opsional (mis. biner Go/Rust yang dikirim oleh Skills): periksa apakah ada rilis `aarch64` / `linux-arm64` sebelum menginstal.


Verifikasi arsitektur dengan `uname -m` (seharusnya mencetak `aarch64`). Untuk biner tanpa build ARM, instal dari sumber atau lewati.

## Persistensi dan cadangan

State OpenClaw berada di bawah:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` per agen, state saluran/penyedia, dan data sesi.
  * `~/.openclaw/workspace/` — workspace agen ([SOUL.md](<http://SOUL.md>), memori, artefak).


Ini tetap ada setelah reboot. Untuk mengambil snapshot portabel:

bashCopy code
[code]
    openclaw backup create
[/code]

## Fallback: tunnel SSH

Jika Tailscale Serve tidak berfungsi, gunakan tunnel SSH dari mesin lokal Anda:

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

Lalu buka `http://localhost:18789`.

## Pemecahan masalah

**Pembuatan instance gagal ("Out of capacity")** \-- Instance ARM tier gratis populer. Coba domain ketersediaan lain atau coba lagi saat jam sepi.

**Tailscale tidak mau terhubung** \-- Jalankan `sudo tailscale up --ssh --hostname=openclaw --reset` untuk mengautentikasi ulang.

**Gateway tidak mau mulai** \-- Jalankan `openclaw doctor --non-interactive` dan periksa log dengan `journalctl --user -u openclaw-gateway.service -n 50`.

**Masalah biner ARM** \-- Sebagian besar paket npm berfungsi di ARM64. Untuk biner native, cari rilis `linux-arm64` atau `aarch64`. Verifikasi arsitektur dengan `uname -m`.

## Langkah berikutnya

  * [Saluran](</id/channels>) \-- hubungkan Telegram, WhatsApp, Discord, dan lainnya
  * [Konfigurasi Gateway](</id/gateway/configuration>) \-- semua opsi konfigurasi
  * [Memperbarui](</id/install/updating>) \-- jaga OpenClaw tetap mutakhir


## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [GCP](</id/install/gcp>)
  * [Hosting VPS](</id/vps>)


Was this useful?YesNo