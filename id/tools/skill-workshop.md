---
title: Lokakarya Keterampilan
source_url: https://docs.openclaw.ai/id/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skill Workshop adalah jalur tata kelola OpenClaw untuk membuat dan memperbarui skill workspace.

Agen dan operator tidak menulis file `SKILL.md` aktif secara langsung melalui jalur ini. Mereka membuat **proposal** terlebih dahulu. Proposal adalah draf tertunda yang berisi konten skill yang diusulkan, pengikatan target, status pemindai, hash, metadata file pendukung, dan metadata rollback. Proposal menjadi skill aktif hanya ketika diterapkan.

Skill Workshop hanya menulis skill workspace. Ini tidak mengubah skill bawaan, plugin, ClawHub, root tambahan, terkelola, agen pribadi, atau sistem.

## Cara kerjanya

  * **Proposal terlebih dahulu:** konten skill yang dihasilkan disimpan sebagai `PROPOSAL.md`, bukan `SKILL.md`.
  * **Apply adalah satu-satunya penulisan aktif:** buat, perbarui, dan revisi tidak mengubah skill aktif.
  * **Dicakup ke workspace:** pembuatan menargetkan root `skills/` workspace. Pembaruan hanya diizinkan untuk skill workspace yang dapat ditulis.
  * **Tidak menimpa:** pembuatan gagal jika skill target sudah ada.
  * **Terikat hash:** proposal pembaruan terikat ke hash target saat ini dan menjadi kedaluwarsa jika skill aktif berubah sebelum apply.
  * **Dibatasi pemindai:** apply menjalankan ulang pemindaian sebelum menulis.
  * **Dapat dipulihkan:** apply menulis metadata rollback sebelum mengubah file aktif.
  * **Permukaan konsisten:** chat, CLI, dan Gateway semuanya memanggil layanan Skill Workshop yang sama.


## Siklus hidup

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

Hanya proposal `pending` yang dapat direvisi, diterapkan, ditolak, atau dikarantina.

## Chat

Minta skill yang Anda inginkan kepada agen. Agen memanggil `skill_workshop` dan mengembalikan id proposal.

Buat:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

Perbarui skill workspace yang sudah ada:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

Iterasikan pada proposal tertunda:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

Secara default, `apply`, `reject`, dan `quarantine` yang dimulai oleh agen menampilkan prompt persetujuan sebelum dijalankan. Atur `skills.workshop.approvalPolicy` ke `"auto"` untuk melewati prompt di lingkungan tepercaya.

## CLI

Buat proposal skill baru:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

Buat proposal pembaruan untuk skill workspace yang sudah ada:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

Daftar dan periksa:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

Revisi sebelum persetujuan:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

Tutup proposal:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Konten proposal

Saat tertunda, proposal disimpan sebagai `PROPOSAL.md` dengan frontmatter khusus proposal:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

Saat apply, Skill Workshop menulis `SKILL.md` aktif dan menghapus field khusus proposal: `status`, `version` proposal, dan `date` proposal.

## File pendukung

Gunakan `--proposal-dir` ketika skill yang diusulkan memerlukan file di samping `PROPOSAL.md`:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

Direktori harus berisi `PROPOSAL.md`. File pendukung harus berada di bawah:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


Skill Workshop memindai, membuat hash, dan menyimpan file pendukung bersama proposal. File tersebut ditulis di samping `SKILL.md` aktif hanya saat apply.

Path file pendukung yang ditolak mencakup path absolut, segmen path tersembunyi, traversal path, path yang tumpang tindih, file executable dari direktori proposal, teks non-UTF-8, byte null, dan file di luar folder pendukung standar.

## Alat agen

Model menggunakan `skill_workshop`:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

Agen harus menggunakan `skill_workshop` untuk pekerjaan skill yang dihasilkan. Mereka tidak boleh membuat atau mengubah file proposal melalui `write`, `edit`, `exec`, perintah shell, atau operasi filesystem langsung.

## Persetujuan dan otonomi

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: mengizinkan OpenClaw membuat proposal tertunda dari sinyal percakapan yang tahan lama setelah giliran berhasil. Default: `false`.
  * `allowSymlinkTargetWrites`: mengizinkan apply menulis melalui symlink skill workspace yang target aslinya tercantum dalam `skills.load.allowSymlinkTargets`. Default: `false`.
  * `approvalPolicy: "pending"`: memerlukan prompt persetujuan sebelum `apply`, `reject`, atau `quarantine` yang dimulai oleh agen.
  * `approvalPolicy: "auto"`: melewati prompt persetujuan tersebut. Agen tetap harus memanggil tindakan.
  * `maxPending`: membatasi proposal tertunda dan dikarantina per workspace.
  * `maxSkillBytes`: membatasi ukuran isi proposal. Default: `40000`.


Deskripsi proposal selalu dibatasi hingga 160 byte.

## Metode Gateway

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

Metode hanya-baca memerlukan `operator.read`. Metode yang mengubah memerlukan `operator.admin`.

## Penyimpanan

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

Direktori status default: `~/.openclaw`.

  * `proposal.json`: rekaman proposal kanonis.
  * `proposals.json`: indeks daftar cepat, dapat dibangun ulang dari folder proposal.
  * `PROPOSAL.md`: proposal skill tertunda.
  * `rollback.json`: metadata pemulihan yang ditulis sebelum apply mengubah file aktif.


## Batas

  * Deskripsi: 160 byte.
  * Isi proposal: `skills.workshop.maxSkillBytes` (default 40.000).
  * File pendukung: 64 per proposal.
  * Ukuran file pendukung: masing-masing 256 KB, total 2 MB.
  * Proposal tertunda dan dikarantina: `skills.workshop.maxPending` per workspace (default 50).


## Pemecahan masalah

Masalah | Resolusi  
---|---  
`Skill proposal description is too large` | Persingkat `description` menjadi 160 byte atau kurang.  
`Skill proposal content is too large` | Persingkat isi proposal atau naikkan `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | Revisi proposal terhadap target saat ini, atau buat proposal baru.  
`Proposal scan failed` | Periksa temuan pemindai, lalu revisi atau karantina proposal.  
`untrusted symlink target` | Konfigurasikan `skills.load.allowSymlinkTargets` dan aktifkan `skills.workshop.allowSymlinkTargetWrites` hanya untuk root skill bersama yang disengaja.  
`Support file paths must be under one of...` | Pindahkan file pendukung ke bawah `assets/`, `examples/`, `references/`, `scripts/`, atau `templates/`.  
Proposal tidak muncul dalam daftar | Periksa workspace `--agent` yang dipilih dan `OPENCLAW_STATE_DIR`.  
Agen tidak dapat memanggil `skill_workshop` | Periksa kebijakan alat aktif dan mode jalan. `coding` menyertakan alat ini; kebijakan `tools.allow` yang restriktif harus mencantumkannya secara eksplisit, dan proses sandbox harus menggunakan sesi agen sisi host normal atau CLI.  
  
## Terkait

  * [Skills](</id/tools/skills>) untuk urutan pemuatan, presedensi, dan visibilitas
  * [Membuat skill](</id/tools/creating-skills>) untuk dasar-dasar `SKILL.md` yang ditulis tangan
  * [Konfigurasi Skills](</id/tools/skills-config>) untuk skema lengkap `skills.workshop`
  * [CLI Skills](</id/cli/skills>) untuk perintah `openclaw skills`


Was this useful?YesNo

Open issue