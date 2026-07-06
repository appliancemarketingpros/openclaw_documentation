---
title: إرفاق CLI
source_url: https://docs.openclaw.ai/ar/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` يشغّل Claude Code باستخدام إعداد MCP مؤقت صارم مرتبط بجلسة Gateway واحدة.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

الخيارات:

  * يربط `--session <key>` المنحة بجلسة Gateway. الافتراضي هو الجلسة الرئيسية.
  * يطلب `--ttl <ms>` مدة TTL موجبة للمنحة بالمللي ثانية. يطبّق Gateway حدّه الأقصى الخاص.
  * يحدد `--bin <path>` ملف Claude Code التنفيذي. الافتراضي هو `claude`.
  * يكتب `--print-config` ملف `.mcp.json` المؤقت، ويطبع أمر التشغيل والبيئة، ويُبقي المنحة نشطة حتى انتهاء TTL.


يُمرَّر رمز الحامل عبر متغيرات البيئة، وليس عبر argv. يشغّل OpenClaw Claude Code باستخدام `--strict-mcp-config --mcp-config <path>` حتى لا تنضم خوادم Claude MCP المحيطة إلى الجلسة المرفقة. تلغي عمليات التشغيل العادية المنحة عند خروج عملية Claude Code.

انظر أيضًا: [CLI Gateway](</ar/cli/gateway>)، و[CLI MCP](</ar/cli/mcp>)، و[CLI ACP](</ar/cli/acp>).

Was this useful?YesNo

Open issue