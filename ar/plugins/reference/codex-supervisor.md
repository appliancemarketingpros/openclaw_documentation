---
title: Plugin مشرف Codex
source_url: https://docs.openclaw.ai/ar/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin مشرف Codex

أشرف على جلسات خادم تطبيق Codex من OpenClaw.

## التوزيع

  * الحزمة: `@openclaw/codex-supervisor`
  * مسار التثبيت: مضمّن في OpenClaw


## السطح

العقود: الأدوات

## سرد الجلسات

يقتصر `codex_sessions_list` افتراضيًا على جلسات Codex المحمّلة فقط. اضبط `include_stored` لتضمين السجل المخزّن؛ يستخدم الPlugin مسار السرد المعتمد فقط على قاعدة بيانات الحالة في خادم تطبيق Codex ويحدّ النتائج المخزّنة عند 200 افتراضيًا. مرّر `max_stored_sessions` لخفض ذلك الحد أو رفعه، حتى 1000.

Was this useful?YesNo

Open issue