---
title: Kanvas
source_url: https://docs.openclaw.ai/id/platforms/mac/canvas
scraped_at: 2026-05-25
---

Aplikasi macOS menyematkan **panel Canvas** yang dikendalikan agen menggunakan `WKWebView`. Ini adalah ruang kerja visual ringan untuk HTML/CSS/JS, A2UI, dan permukaan UI interaktif kecil.

## Lokasi Canvas

Status Canvas disimpan di bawah Application Support:

  * `~/Library/Application Support/OpenClaw/canvas/<session>/...`


Panel Canvas menyajikan file tersebut melalui **skema URL kustom** :

  * `openclaw-canvas://<session>/<path>`


Contoh:

  * `openclaw-canvas://main/` → `<canvasRoot>/main/index.html`
  * `openclaw-canvas://main/assets/app.css` → `<canvasRoot>/main/assets/app.css`
  * `openclaw-canvas://main/widgets/todo/` → `<canvasRoot>/main/widgets/todo/index.html`


Jika tidak ada `index.html` di root, aplikasi menampilkan **halaman scaffold bawaan**.

## Perilaku panel

  * Panel tanpa bingkai yang dapat diubah ukurannya, ditambatkan di dekat bilah menu (atau kursor tetikus).
  * Mengingat ukuran/posisi per sesi.
  * Memuat ulang otomatis saat file canvas lokal berubah.
  * Hanya satu panel Canvas yang terlihat pada satu waktu (sesi dialihkan sesuai kebutuhan).


Canvas dapat dinonaktifkan dari Pengaturan → **Izinkan Canvas**. Saat dinonaktifkan, perintah node canvas mengembalikan `CANVAS_DISABLED`.

## Permukaan API agen

Canvas diekspos melalui **Gateway WebSocket** , sehingga agen dapat:

  * menampilkan/menyembunyikan panel
  * bernavigasi ke path atau URL
  * mengevaluasi JavaScript
  * menangkap gambar snapshot


Contoh CLI:

bashCopy code
[code]
    openclaw nodes canvas present --node <id>openclaw nodes canvas navigate --node <id> --url "/"openclaw nodes canvas eval --node <id> --js "document.title"openclaw nodes canvas snapshot --node <id>
[/code]

Catatan:

  * `canvas.navigate` menerima **path canvas lokal** , URL `http(s)`, dan URL `file://`.
  * Jika Anda meneruskan `"/"`, Canvas menampilkan scaffold lokal atau `index.html`.


## A2UI di Canvas

A2UI di-host oleh host canvas Gateway dan dirender di dalam panel Canvas. Saat Gateway mengiklankan host Canvas, aplikasi macOS otomatis bernavigasi ke halaman host A2UI pada pembukaan pertama.

URL host A2UI default:

CodeCopy code
[code]
    http://<gateway-host>:18789/__openclaw__/a2ui/
[/code]

### Perintah A2UI (v0.8)

Canvas saat ini menerima pesan server→klien **A2UI v0.8** :

  * `beginRendering`
  * `surfaceUpdate`
  * `dataModelUpdate`
  * `deleteSurface`


`createSurface` (v0.9) tidak didukung.

Contoh CLI:

bashCopy code
[code]
    cat > /tmp/a2ui-v0.8.jsonl <<'EOFA2'{"surfaceUpdate":{"surfaceId":"main","components":[{"id":"root","component":{"Column":{"children":{"explicitList":["title","content"]}}}},{"id":"title","component":{"Text":{"text":{"literalString":"Canvas (A2UI v0.8)"},"usageHint":"h1"}}},{"id":"content","component":{"Text":{"text":{"literalString":"If you can read this, A2UI push works."},"usageHint":"body"}}}]}}{"beginRendering":{"surfaceId":"main","root":"root"}}EOFA2 openclaw nodes canvas a2ui push --jsonl /tmp/a2ui-v0.8.jsonl --node <id>
[/code]

Smoke cepat:

bashCopy code
[code]
    openclaw nodes canvas a2ui push --node <id> --text "Hello from A2UI"
[/code]

## Memicu run agen dari Canvas

Canvas dapat memicu run agen baru melalui deep link:

  * `openclaw://agent?...`


Contoh (dalam JS):

jsCopy code
[code]
    window.location.href = "openclaw://agent?message=Review%20this%20design";
[/code]

Aplikasi meminta konfirmasi kecuali kunci yang valid disediakan.

## Catatan keamanan

  * Skema Canvas memblokir traversal direktori; file harus berada di bawah root sesi.
  * Konten Canvas lokal menggunakan skema kustom (tidak memerlukan server loopback).
  * URL `http(s)` eksternal hanya diizinkan saat dinavigasikan secara eksplisit.


## Terkait

  * [aplikasi macOS](</id/platforms/macos>)
  * [WebChat](</id/web/webchat>)


Was this useful?YesNo