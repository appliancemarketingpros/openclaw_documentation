---
title: IPC في macOS
source_url: https://docs.openclaw.ai/ar/platforms/mac/xpc
scraped_at: 2026-05-25
---

# بنية IPC في macOS الخاصة بـ OpenClaw

**النموذج الحالي:** يربط Unix socket محلي **خدمة node host** بـ **تطبيق macOS** من أجل موافقات exec + `system.run`. وتوجد أداة CLI للتصحيح باسم `openclaw-mac` من أجل فحوصات الاكتشاف/الاتصال؛ لكن إجراءات الوكيل لا تزال تتدفق عبر Gateway WebSocket و`node.invoke`. وتستخدم أتمتة واجهة المستخدم PeekabooBridge.

## الأهداف

  * نسخة واحدة من تطبيق GUI تملك جميع الأعمال المواجهة لـ TCC ‏(الإشعارات، وتسجيل الشاشة، والميكروفون، والكلام، وAppleScript).
  * سطح صغير للأتمتة: Gateway + أوامر node، بالإضافة إلى PeekabooBridge لأتمتة واجهة المستخدم.
  * أذونات قابلة للتنبؤ: المعرّف نفسه للحزمة الموقّعة دائمًا، ويتم تشغيله بواسطة launchd، بحيث تبقى منح TCC ثابتة.


## كيف يعمل

### نقل Gateway + node

  * يشغّل التطبيق Gateway ‏(الوضع المحلي) ويتصل بها باعتباره node.
  * تُنفَّذ إجراءات الوكيل عبر `node.invoke` ‏(مثل `system.run` و`system.notify` و`canvas.*`).


### خدمة Node + IPC الخاصة بالتطبيق

  * تتصل خدمة node host بلا واجهة بـ Gateway WebSocket.
  * تُعاد توجيه طلبات `system.run` إلى تطبيق macOS عبر Unix socket محلي.
  * ينفّذ التطبيق الأمر في سياق واجهة المستخدم، ويطلب الموافقة إذا لزم الأمر، ويعيد المخرجات.


مخطط (SCI):

CodeCopy code
[code]
    Agent -> Gateway -> Node Service (WS)                      |  IPC (UDS + token + HMAC + TTL)                      v                  Mac App (UI + TCC + system.run)
[/code]

### PeekabooBridge ‏(أتمتة واجهة المستخدم)

  * تستخدم أتمتة واجهة المستخدم UNIX socket منفصلة باسم `bridge.sock` وبروتوكول JSON الخاص بـ PeekabooBridge.
  * ترتيب تفضيل المضيف (من جهة العميل): ‏Peekaboo.app → Claude.app → OpenClaw.app → التنفيذ المحلي.
  * الأمان: تتطلب مضيفات الجسر TeamID مسموحًا به؛ ويكون مسار الهروب same-UID في وضع DEBUG فقط محميًا بواسطة `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` ‏(وفق اصطلاح Peekaboo).
  * راجع: [استخدام PeekabooBridge](</ar/platforms/mac/peekaboo>) للتفاصيل.


## التدفقات التشغيلية

  * إعادة التشغيل/إعادة البناء: `SIGN_IDENTITY="Apple Development: &lt;Developer Name&gt; (&lt;TEAMID&gt;)" scripts/restart-mac.sh`
    * يقتل النسخ الموجودة
    * بناء Swift + الحزمة
    * يكتب LaunchAgent ويهيئها ويعيد تشغيلها
  * نسخة واحدة: يخرج التطبيق مبكرًا إذا كانت نسخة أخرى تحمل معرّف الحزمة نفسه قيد التشغيل.


## ملاحظات التقوية

  * يُفضّل طلب تطابق TeamID لجميع الأسطح ذات الامتيازات.
  * PeekabooBridge: قد تسمح `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` ‏(في وضع DEBUG فقط) للمتصلين من same-UID من أجل التطوير المحلي.
  * تبقى جميع الاتصالات محلية فقط؛ ولا يتم كشف أي network sockets.
  * تصدر مطالبات TCC من حزمة تطبيق GUI فقط؛ أبقِ معرّف الحزمة الموقّعة ثابتًا عبر عمليات إعادة البناء.
  * تقوية IPC: نمط socket ‏`0600`، ورمز، وفحوصات peer-UID، وتحدي/استجابة HMAC، وTTL قصيرة.


## ذو صلة

  * [تطبيق macOS](</ar/platforms/macos>)
  * [تدفق IPC في macOS ‏(موافقات Exec)](</ar/tools/exec-approvals-advanced#macos-ipc-flow>)


Was this useful?YesNo