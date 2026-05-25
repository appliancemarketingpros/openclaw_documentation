---
title: Kelola Plugin
source_url: https://docs.openclaw.ai/id/plugins/manage-plugins
scraped_at: 2026-05-25
---

Sebagian besar alur kerja plugin hanya terdiri dari beberapa perintah: cari, instal, mulai ulang Gateway, verifikasi, dan hapus instalasi saat Anda tidak lagi memerlukan plugin tersebut.

## Cantumkan plugin

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Gunakan `--json` untuk skrip. Ini menyertakan diagnostik registri dan `dependencyStatus` statis setiap plugin saat paket plugin mendeklarasikan `dependencies` atau `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` adalah pemeriksaan inventaris dingin. Ini menampilkan apa yang dapat ditemukan OpenClaw dari konfigurasi, manifes, dan registri plugin; ini tidak membuktikan bahwa proses Gateway yang sudah berjalan telah mengimpor runtime plugin.

## Instal plugin

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Setelah menginstal kode plugin, mulai ulang Gateway yang melayani saluran Anda:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Gunakan `inspect --runtime` saat Anda memerlukan bukti bahwa plugin mendaftarkan permukaan runtime seperti alat, hook, layanan, metode Gateway, atau perintah CLI milik plugin.

## Perbarui plugin

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Jika sebuah plugin diinstal dari dist-tag npm seperti `@beta`, pemanggilan `update <plugin-id>` berikutnya menggunakan kembali tag yang tercatat tersebut. Meneruskan spec npm eksplisit mengalihkan instalasi yang dilacak ke spec tersebut untuk pembaruan mendatang.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

Perintah kedua memindahkan plugin kembali ke jalur rilis default registri saat sebelumnya dipin ke versi atau tag yang tepat.

Saat `openclaw update` berjalan pada saluran beta, catatan plugin npm dan ClawHub jalur default mencoba rilis plugin `@beta` yang cocok terlebih dahulu. Jika rilis beta tersebut tidak ada, OpenClaw beralih ke spec default/latest yang tercatat. Untuk plugin npm, OpenClaw juga beralih saat paket beta ada tetapi gagal validasi instalasi. Versi tepat dan tag eksplisit seperti `@rc` atau `@beta` dipertahankan.

## Hapus instalasi plugin

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

Penghapusan instalasi menghapus entri konfigurasi plugin, catatan indeks plugin, entri daftar izinkan/tolak, dan jalur pemuatan tertaut bila berlaku. Direktori instalasi terkelola dihapus kecuali Anda meneruskan `--keep-files`.

Dalam mode Nix (`OPENCLAW_NIX_MODE=1`), perintah instal, perbarui, hapus instalasi, aktifkan, dan nonaktifkan plugin dinonaktifkan. Kelola pilihan tersebut di sumber Nix untuk instalasi sebagai gantinya; untuk nix-openclaw, gunakan [Mulai Cepat](<https://github.com/openclaw/nix-openclaw#quick-start>) yang mengutamakan agen.

## Publikasikan plugin

Anda dapat memublikasikan plugin eksternal ke [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>), atau keduanya.

### Publikasikan ke ClawHub

ClawHub adalah permukaan penemuan publik utama untuk plugin OpenClaw. Ini memberi pengguna metadata yang dapat dicari, riwayat versi, dan hasil pemindaian registri sebelum instalasi.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Pengguna menginstal dari ClawHub dengan:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

Bentuk polos tetap memeriksa ClawHub terlebih dahulu.

### Publikasikan ke [npmjs.com](<http://npmjs.com>)

Plugin npm native harus menyertakan manifes plugin dan metadata entrypoint OpenClaw `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Pengguna menginstal hanya-npm dengan:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Jika paket yang sama juga tersedia di ClawHub, `npm:` melewati pencarian ClawHub dan memaksa resolusi npm.

## Pilihan sumber

  * **ClawHub** : gunakan saat Anda menginginkan penemuan native OpenClaw, ringkasan pemindaian, versi, dan petunjuk instalasi.
  * **[npmjs.com](<http://npmjs.com>)** : gunakan saat Anda sudah mengirimkan paket JavaScript atau memerlukan alur kerja dist-tag npm/registri privat.
  * **Git** : gunakan saat Anda ingin menginstal langsung dari branch, tag, atau commit.
  * **Jalur lokal** : gunakan saat Anda mengembangkan atau menguji plugin di mesin yang sama.


## Terkait

  * [Plugin](</id/tools/plugin>) \- ikhtisar dan pemecahan masalah
  * [`openclaw plugins`](</id/cli/plugins>) \- referensi CLI lengkap
  * [ClawHub](</id/clawhub/cli>) \- publikasi dan operasi registri
  * [Membangun plugin](</id/plugins/building-plugins>) \- buat paket plugin
  * [Manifes plugin](</id/plugins/manifest>) \- metadata manifes dan paket


Was this useful?YesNo