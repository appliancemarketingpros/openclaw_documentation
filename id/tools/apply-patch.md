---
title: alat apply_patch
source_url: https://docs.openclaw.ai/id/tools/apply-patch
scraped_at: 2026-05-25
---

Terapkan perubahan berkas menggunakan format patch terstruktur. Ini ideal untuk edit multi-berkas atau multi-segmen ketika satu pemanggilan `edit` akan rapuh.

Alat ini menerima satu string `input` yang membungkus satu atau beberapa operasi berkas:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parameter

  * `input` (wajib): Isi patch lengkap termasuk `*** Begin Patch` dan `*** End Patch`.


## Catatan

  * Jalur patch mendukung jalur relatif (dari direktori workspace) dan jalur absolut.
  * `tools.exec.applyPatch.workspaceOnly` default-nya adalah `true` (terbatas dalam workspace). Atur ke `false` hanya jika Anda sengaja ingin `apply_patch` menulis/menghapus di luar direktori workspace.
  * Gunakan `*** Move to:` di dalam segmen `*** Update File:` untuk mengganti nama berkas.
  * `*** End of File` menandai penyisipan khusus EOF bila diperlukan.
  * Tersedia secara default untuk model OpenAI dan OpenAI Codex. Atur `tools.exec.applyPatch.enabled: false` untuk menonaktifkannya.
  * Secara opsional, batasi berdasarkan model melalui `tools.exec.applyPatch.allowModels`.
  * Konfigurasi hanya berada di bawah `tools.exec`.


## Contoh

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Terkait

[**Diff** Penampil diff hanya-baca untuk penyajian perubahan. ](</id/tools/diffs>) [**Alat exec** Eksekusi perintah shell dari agen. ](</id/tools/exec>) [**Eksekusi kode** Analisis Python jarak jauh dalam sandbox dengan xAI. ](</id/tools/code-execution>)

Was this useful?YesNo