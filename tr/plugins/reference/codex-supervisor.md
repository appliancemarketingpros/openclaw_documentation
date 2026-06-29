---
title: Codex Supervisor Plugin
source_url: https://docs.openclaw.ai/tr/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor Plugin

OpenClaw'dan Codex app-server oturumlarını denetleyin.

## Dağıtım

  * Paket: `@openclaw/codex-supervisor`
  * Kurulum yolu: OpenClaw'a dahil


## Yüzey

sözleşmeler: araçlar

## Oturum Listeleme

`codex_sessions_list` varsayılan olarak yalnızca yüklenmiş Codex oturumlarını listeler. Saklanan geçmişi dahil etmek için `include_stored` değerini ayarlayın; Plugin, Codex app-server'ın yalnızca durum DB'si listeleme yolunu kullanır ve saklanan sonuçları varsayılan olarak 200 ile sınırlar. Bu sınırı 1000'e kadar düşürmek veya yükseltmek için `max_stored_sessions` iletin.

Was this useful?YesNo

Open issue