---
title: Skills
source_url: https://docs.openclaw.ai/id/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

Periksa Skills lokal dan instal/perbarui Skills dari ClawHub.

Terkait:

  * Sistem Skills: [Skills](</id/tools/skills>)
  * Konfigurasi Skills: [Konfigurasi Skills](</id/tools/skills-config>)
  * Instalasi ClawHub: [ClawHub](</id/clawhub/cli>)


## Perintah

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` menggunakan ClawHub secara langsung dan menginstal ke direktori `skills/` ruang kerja aktif. `list`/`info`/`check` tetap memeriksa Skills lokal yang terlihat oleh ruang kerja dan konfigurasi saat ini. Perintah berbasis ruang kerja menyelesaikan ruang kerja target dari `--agent <id>`, lalu direktori kerja saat ini jika berada di dalam ruang kerja agen yang dikonfigurasi, lalu agen default.

Perintah CLI `install` ini mengunduh folder Skills dari ClawHub. Instalasi dependensi Skills berbasis Gateway yang dipicu dari orientasi awal atau pengaturan Skills menggunakan jalur permintaan `skills.install` yang terpisah.

Catatan:

  * `search [query...]` menerima kueri opsional; hilangkan untuk menelusuri feed pencarian ClawHub default.
  * `search --limit <n>` membatasi hasil yang dikembalikan.
  * `install --force` menimpa folder Skills ruang kerja yang ada untuk slug yang sama.
  * `--agent <id>` menargetkan satu ruang kerja agen yang dikonfigurasi dan mengesampingkan inferensi direktori kerja saat ini.
  * `update --all` hanya memperbarui instalasi ClawHub terlacak di ruang kerja aktif.
  * `check --agent <id>` memeriksa ruang kerja agen yang dipilih dan melaporkan Skills siap mana yang benar-benar terlihat oleh prompt atau permukaan perintah agen tersebut.
  * `list` adalah tindakan default ketika tidak ada subperintah yang diberikan.
  * `list`, `info`, dan `check` menulis keluaran yang dirender ke stdout. Dengan `--json`, ini berarti payload yang dapat dibaca mesin tetap berada di stdout untuk pipe dan skrip.


## Terkait

  * [Referensi CLI](</id/cli>)
  * [Skills](</id/tools/skills>)


Was this useful?YesNo