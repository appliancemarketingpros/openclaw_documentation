---
title: Ansible
source_url: https://docs.openclaw.ai/id/install/ansible
scraped_at: 2026-05-25
---

Deploy OpenClaw ke server produksi dengan **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- installer otomatis dengan arsitektur yang mengutamakan keamanan.

## Prasyarat

Persyaratan | Detail  
---|---  
**OS** | Debian 11+ atau Ubuntu 20.04+  
**Akses** | Hak akses root atau sudo  
**Jaringan** | Koneksi internet untuk instalasi paket  
**Ansible** | 2.14+ (diinstal otomatis oleh skrip quick-start)  
  
## Yang Anda dapatkan

  * **Keamanan berbasis firewall** \-- isolasi UFW + Docker (hanya SSH + Tailscale yang dapat diakses)
  * **VPN Tailscale** \-- akses jarak jauh yang aman tanpa mengekspos layanan secara publik
  * **Docker** \-- kontainer sandbox terisolasi, binding hanya localhost
  * **Pertahanan berlapis** \-- arsitektur keamanan 4 lapis
  * **Integrasi Systemd** \-- mulai otomatis saat boot dengan hardening
  * **Setup satu perintah** \-- deployment lengkap dalam hitungan menit


## Mulai cepat

Instalasi satu perintah:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Yang diinstal

Playbook Ansible menginstal dan mengonfigurasi:

  1. **Tailscale** \-- VPN mesh untuk akses jarak jauh yang aman
  2. **Firewall UFW** \-- hanya port SSH + Tailscale
  3. **Docker CE + Compose V2** \-- untuk backend sandbox agent default
  4. **Node.js 24 + pnpm** \-- dependensi runtime (Node 22 LTS, saat ini `22.16+`, tetap didukung)
  5. **OpenClaw** \-- berbasis host, tidak dikontainerisasi
  6. **Layanan Systemd** \-- mulai otomatis dengan hardening keamanan


## Setup Pasca-Instalasi

* ### Beralih ke pengguna openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Jalankan wizard onboarding

Skrip pasca-instalasi memandu Anda dalam mengonfigurasi pengaturan OpenClaw.

* ### Hubungkan penyedia pesan

Masuk ke WhatsApp, Telegram, Discord, atau Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Verifikasi instalasi

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Hubungkan ke Tailscale

Bergabunglah dengan mesh VPN Anda untuk akses jarak jauh yang aman.

### Perintah cepat

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Arsitektur keamanan

Deployment menggunakan model pertahanan 4 lapis:

  1. **Firewall (UFW)** \-- hanya SSH (22) + Tailscale (41641/udp) yang terekspos secara publik
  2. **VPN (Tailscale)** \-- Gateway hanya dapat diakses melalui mesh VPN
  3. **Isolasi Docker** \-- chain iptables DOCKER-USER mencegah eksposur port eksternal
  4. **Hardening Systemd** \-- NoNewPrivileges, PrivateTmp, pengguna tanpa hak istimewa


Untuk memverifikasi permukaan serangan eksternal Anda:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Hanya port 22 (SSH) yang seharusnya terbuka. Semua layanan lain (Gateway, Docker) dikunci.

Docker diinstal untuk sandbox agent (eksekusi tool terisolasi), bukan untuk menjalankan Gateway itu sendiri. Lihat [Multi-Agent Sandbox and Tools](</id/tools/multi-agent-sandbox-tools>) untuk konfigurasi sandbox.

## Instalasi manual

Jika Anda lebih memilih kontrol manual daripada otomatisasi:

* ### Instal prasyarat

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Clone repositori

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Instal koleksi Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Jalankan playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Atau, jalankan langsung lalu eksekusi skrip setup secara manual setelahnya:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Memperbarui

Installer Ansible menyiapkan OpenClaw untuk pembaruan manual. Lihat [Memperbarui](</id/install/updating>) untuk alur pembaruan standar.

Untuk menjalankan ulang playbook Ansible (misalnya, untuk perubahan konfigurasi):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Ini bersifat idempoten dan aman dijalankan berkali-kali.

## Pemecahan masalah

Firewall memblokir koneksi saya

  * Pastikan Anda dapat mengakses melalui VPN Tailscale terlebih dahulu
  * Akses SSH (port 22) selalu diizinkan
  * Gateway memang hanya dapat diakses melalui Tailscale sesuai desain

Layanan tidak dapat dimulai bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Masalah sandbox Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Login penyedia gagal

Pastikan Anda menjalankannya sebagai pengguna `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Konfigurasi lanjutan

Untuk arsitektur keamanan dan pemecahan masalah yang detail, lihat repo openclaw-ansible:

  * [Arsitektur Keamanan](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Detail Teknis](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Panduan Pemecahan Masalah](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Terkait

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- panduan deployment lengkap
  * [Docker](</id/install/docker>) \-- setup Gateway terkointainerisasi
  * [Sandboxing](</id/gateway/sandboxing>) \-- konfigurasi sandbox agent
  * [Multi-Agent Sandbox and Tools](</id/tools/multi-agent-sandbox-tools>) \-- isolasi per-agent


Was this useful?YesNo