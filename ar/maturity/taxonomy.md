---
title: تصنيف النضج
source_url: https://docs.openclaw.ai/ar/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# تصنيف النضج

النموذج خلف بطاقة النتائج

الأسطح > الفئات > القدرات > الأدلة.

50 سطحًا مجمعة في 4 عائلات، مع ربط كل فئة بالوثائق القانونية ومعرّفات تغطية ضمان الجودة.

تصفح مجالات المنتج / افتح التصنيف التفصيلي / [عرض النتائج](</ar/maturity/scorecard>)

## كيفية قراءة هذه الصفحة

السطح هو مجال منتج مثل وقت تشغيل Gateway، أو Discord، أو تطبيق macOS. يحتوي كل سطح على فئات، وتحتوي كل فئة على فحوصات على مستوى القدرات تغطيها سيناريوهات ضمان الجودة. استخدم بطاقة النتائج للحكم على مستوى الإصدار؛ واستخدم هذه الصفحة لفحص النموذج الكامن تحتها.

## مستويات النضج

M0مخططالاتجاه معروف، لكن لا يوجد مسار مستخدم مدعوم.الترقية: توجد مشكلة تصميم ومالك وسطح مستهدف.

M1تجريبيمنفذ مع تحفظات أو أعلام أو بنايات مصدرية أو تدفقات خاصة بالمشرفين فقط.الترقية: يستطيع المشرف تشغيل السيناريو من الفرع الرئيسي الحالي.

M2ألفايمكن للمستخدمين الحقيقيين تجربته، لكن التغييرات الكاسرة وتجربة المستخدم غير المكتملة متوقعة.الترقية: إعداد موثق، واختبارات أساسية، وتحفظات معروفة، ودليل واحد على الأقل من بيئة حقيقية.

M3بيتايوجد مسار عام وسير العمل الرئيسي قابل للاستخدام مع تحفظات محدودة.الترقية: وثائق تثبيت/تحديث، واختبارات انحدار، ودليل تشغيل للدعم، وإثبات سيناريو ناجح عبر البيئة المتوقعة.

M4مستقرالمسار الموصى به للمستخدمين العاديين. تُعامل الإخفاقات على أنها انحدارات.الترقية: بوابة إصدار، ومسار طبيب/استكشاف أخطاء وإصلاحها، ووثائق واسعة، وإثبات متكرر من العالم الحقيقي.

M5رائعمصقول، وممتع، ومزود بقياسات جيدة، ومنافس لأفضل سير عمل قابل للمقارنة.الترقية: مستوى مستقر بالإضافة إلى اجتياز بطاقة نتائج المستخدم عبر مستخدمين ممثلين.

## مجالات المنتج

### Core

CLI M4مستقر7 مجالات - مكتمل بنسبة 90% وقت تشغيل Gateway M4مستقر13 مجالًا - مكتمل بنسبة 89% وقت تشغيل الوكيل M3بيتا9 مجالات - مكتمل بنسبة 79% الجلسة والذاكرة ومحرك السياق M3بيتا9 مجالات - مكتمل بنسبة 79% إطار عمل القنوات M3بيتا8 مجالات - مكتمل بنسبة 79% قابلية المراقبة M3بيتا5 مجالات - مكتمل بنسبة 79% تطبيق ويب Gateway M3بيتا6 مجالات - مكتمل بنسبة 79% Plugins M3تجريبي9 مجالات - مكتمل بنسبة 79% الأمان، والمصادقة، والإقران، والأسرار M3تجريبي6 مجالات - مكتمل بنسبة 79% الأتمتة: Cron، والخطافات، والمهام، والاستقصاء M3تجريبي6 مجالات - مكتمل بنسبة 79% فهم الوسائط وتوليد الوسائط M2ألفا6 مجالات - مكتمل بنسبة 68% الصوت والمحادثة في الوقت الحقيقي M2ألفا6 مجالات - مكتمل بنسبة 68% TUI M2ألفا5 مجالات - مكتمل بنسبة 66% ClawHub M2ألفا4 مجالات - مكتمل بنسبة 62% حزمة SDK لتطبيق OpenClaw M2ألفا6 مجالات - مكتمل بنسبة 53%

### المنصة

مضيف Gateway على Linux M4مستقر5 مجالات - مكتمل بنسبة 89% مضيف Gateway على macOS M4مستقر7 مجالات - مكتمل بنسبة 88% استضافة Docker وPodman M3تجريبي4 مجالات - مكتمل بنسبة 79% Windows عبر WSL2 M3تجريبي6 مجالات - مكتمل بنسبة 79% Raspberry Pi وأجهزة Linux الصغيرة M3تجريبي4 مجالات - مكتمل بنسبة 79% تطبيق macOS المرافق M3تجريبي8 مجالات - مكتمل بنسبة 78% تطبيق Android M2ألفا7 مجالات - مكتمل بنسبة 66% Windows الأصلي M2ألفا4 مجالات - مكتمل بنسبة 66% استضافة Kubernetes M2ألفا4 مجالات - مكتمل بنسبة 61% تطبيق iOS M1تجريبي8 مجالات - مكتمل بنسبة 44% مسار تثبيت Nix M1تجريبي5 مجالات - مكتمل بنسبة 44% أسطح watchOS المرافقة M1تجريبي5 مجالات - مكتمل بنسبة 44% تطبيق Linux المرافق M0مخطط5 مجالات - مكتمل بنسبة 21% تطبيق Windows الأصلي المرافق M0مخطط5 مجالات - مكتمل بنسبة 21%

### القناة

Discord M4مستقر6 مجالات - مكتمل بنسبة 87% Telegram M3بيتا5 مجالات - مكتمل بنسبة 78% Slack M3بيتا5 مجالات - مكتمل بنسبة 78% iMessage وBlueBubbles M3بيتا5 مجالات - مكتمل بنسبة 78% WhatsApp M3بيتا5 مجالات - مكتمل بنسبة 78% Matrix M2ألفا6 مجالات - مكتمل بنسبة 67% Google Chat M2ألفا5 مجالات - مكتمل بنسبة 66% Microsoft Teams M2ألفا5 مجالات - مكتمل بنسبة 66% Signal M2ألفا5 مجالات - مكتمل بنسبة 66% Feishu، QQ Bot، WeChat، Yuanbao، Zalo، Zalo Personal، القنوات الإقليمية M2ألفا4 مجالات - مكتمل بنسبة 58% Mattermost، LINE، IRC، Nextcloud Talk، Nostr، Twitch، Tlon، Synology Chat M2ألفا4 مجالات - مكتمل بنسبة 54% قناة المكالمات الصوتية M1تجريبي5 مجالات - مكتمل بنسبة 44%

### المزوّد والأداة

أدوات أتمتة المتصفح وexec وبيئة العزل M3بيتا3 مجالات - مكتمل بنسبة 79% مسار مزوّد OpenAI وCodex M3بيتا5 مجالات - مكتمل بنسبة 79% أدوات بحث الويب M3بيتا4 مجالات - مكتمل بنسبة 79% مسار مزوّد Anthropic M3بيتا5 مجالات - مكتمل بنسبة 78% مسار مزوّد Google M3بيتا5 مجالات - مكتمل بنسبة 78% مسار مزوّد OpenRouter M3بيتا4 مجالات - مكتمل بنسبة 78% أدوات إنشاء الصور والفيديو والموسيقى M2ألفا5 مجالات - مكتمل بنسبة 68% مزوّدو النماذج المحلية: Ollama، vLLM، SGLang، LM Studio M2ألفا5 مجالات - مكتمل بنسبة 68% المزوّدون المستضافون ذوو الانتشار المحدود M2ألفا3 مجالات - مكتمل بنسبة 68%

## التفاصيل

### النواة

CLI - M4 مستقر - 7 مجالات

وُثّقت مسارات الإعداد والإصلاح العادية عبر وثائق التثبيت وCLI وGateway. تُتتبّع مسارات Windows الخاصة بالمنصات في صفّي Windows عبر WSL2 وWindows الأصلي.

التغطية تجريبية - 4%الجودة مستقرة - 83%الاكتمال مستقر - 90%جزئي - 6

إعداد CLI 6 إمكانات / مدعوم بإصدارات LTS

تجريبي17%

مستقر89%

مستقر90%

[الفهرس](</ar/install>), [المثبّت](</ar/install/installer>), [Node](</ar/install/node>), [التحديث](</ar/install/updating>)

الإعداد الأولي وإعداد المصادقة 5 إمكانات / مدعوم بإصدارات LTS

تجريبي0%

بيتا75%

مستقر89%

[الإعداد الأولي](</ar/cli/onboard>), [التهيئة](</ar/cli/configure>), [نظرة عامة على الإعداد الأولي](</ar/start/onboarding-overview>)

إعداد Plugin والقنوات 5 إمكانات

تجريبي0%

بيتا75%

مستقر89%

[الإعداد الأولي](</ar/cli/onboard>), [Plugins](</ar/cli/plugins>), [القنوات](</ar/cli/channels>)

إدارة خدمة Gateway 5 إمكانات / مدعوم بإصدارات LTS

تجريبي14%

مستقر87%

مستقر90%

[Gateway](</ar/cli/gateway>), [التحديث](</ar/install/updating>), [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)

قابلية المراقبة في CLI 5 إمكانات / مدعوم بإصدارات LTS

تجريبي0%

مستقر89%

مستقر90%

[الحالة](</ar/cli/status>), [الصحة](</ar/cli/health>), [السجلات](</ar/cli/logs>), [التشخيصات](</ar/gateway/diagnostics>)

الفحص 10 إمكانات / مدعوم بإصدارات LTS

تجريبي0%

مستقر89%

مستقر90%

[الفحص](</ar/cli/doctor>), [الفحص](</ar/gateway/doctor>), [الأسرار](</ar/gateway/secrets>), [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)

التحديثات والترقيات 5 إمكانات / مدعوم بإصدارات LTS

تجريبي0%

بيتا75%

مستقر89%

[التحديث](</ar/install/updating>), [التحديث](</ar/cli/update>), [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)

وقت تشغيل Gateway - M4 مستقر - 13 مجالًا

البنية الأساسية، والمصادقة، والإقران، ووثائق البروتوكول، ووثائق العفريت، وأدلة تشغيل CLI واسعة وحديثة.

التغطية تجريبية - 6%الجودة مستقرة - 81%الاكتمال مستقر - 89%جزئي - 12

الموافقات والتنفيذ عن بُعد 6 إمكانات / مدعومة بإصدار LTS

تجريبي0%

بيتا75%

مستقر89%

[البروتوكول](</ar/gateway/protocol>), [الفهرس](</ar/gateway/security>)

واجهات API عبر HTTP 4 إمكانات / مدعومة بإصدار LTS

تجريبي25%

مستقر90%

مستقر90%

[الفهرس](</ar/gateway>), [واجهة Openai Http Api](</ar/gateway/openai-http-api>), [واجهة Openresponses Http Api](</ar/gateway/openresponses-http-api>), [واجهة Tools Invoke Http Api](</ar/gateway/tools-invoke-http-api>), [الخطافات](</ar/automation/hooks>), [الفهرس](</ar/web>)

سطح الويب المستضاف 4 إمكانات / مدعومة بإصدار LTS

تجريبي0%

مستقر89%

مستقر90%

[الفهرس](</ar/gateway>), [البنية](</ar/concepts/architecture>), [واجهة التحكم](</ar/web/control-ui>), [دردشة الويب](</ar/web/webchat>), [Canvas](</ar/refactor/canvas>)

واجهات API وأحداث RPC في Gateway 20 إمكانية / مدعومة بإصدار LTS

تجريبي9%

مستقر90%

مستقر90%

[البروتوكول](</ar/gateway/protocol>), [الفهرس](</ar/gateway>), [البنية](</ar/concepts/architecture>)

مصادقة الجهاز والاقتران 10 إمكانات / مدعومة بإصدار LTS

تجريبي0%

بيتا75%

مستقر89%

[البروتوكول](</ar/gateway/protocol>), [الاقتران](</ar/gateway/pairing>), [الفهرس](</ar/gateway/security>)

الوصول إلى الشبكة والاكتشاف 6 إمكانات / مدعومة بإصدار LTS

تجريبي0%

بيتا75%

مستقر89%

[الفهرس](</ar/gateway>), [الاكتشاف](</ar/gateway/discovery>), [البروتوكول](</ar/gateway/protocol>)

Nodes والإمكانات عن بُعد 8 إمكانات

تجريبي0%

بيتا75%

مستقر89%

[البروتوكول](</ar/gateway/protocol>), [البنية](</ar/concepts/architecture>), [الفهرس](</ar/nodes>)

الصحة والتشخيص والإصلاح 7 إمكانات / مدعومة بإصدار LTS

تجريبي0%

بيتا75%

مستقر89%

[الفهرس](</ar/gateway>)، [التشخيصات](</ar/gateway/diagnostics>)، [Doctor](</ar/gateway/doctor>)

توافق البروتوكول 7 قدرات / مدعومة عبر LTS

تجريبي0%

بيتا75%

مستقر89%

[البروتوكول](</ar/gateway/protocol>)، [البنية](</ar/concepts/architecture>)، [Typebox](</ar/concepts/typebox>)، [بروتوكول الجسر](</ar/gateway/bridge-protocol>)

الأدوار والأذونات 5 قدرات / مدعومة عبر LTS

تجريبي0%

بيتا75%

مستقر89%

[البروتوكول](</ar/gateway/protocol>)، [الفهرس](</ar/gateway/security>)

دورة حياة Gateway 7 قدرات / مدعومة عبر LTS

تجريبي33%

مستقر90%

مستقر90%

[الفهرس](</ar/gateway>)، [البنية](</ar/concepts/architecture>)

عناصر التحكم الأمنية 6 قدرات / مدعومة عبر LTS

تجريبي0%

بيتا75%

مستقر89%

[الفهرس](</ar/gateway/security>)، [البروتوكول](</ar/gateway/protocol>)، [الاكتشاف](</ar/gateway/discovery>)

اتصال WebSocket 8 قدرات / مدعومة عبر LTS

تجريبي13%

مستقر90%

مستقر90%

[البروتوكول](</ar/gateway/protocol>)، [البنية](</ar/concepts/architecture>)

وقت تشغيل الوكيل - M3 Beta - 9 مجالات

الحلقة الرئيسية والنماذج وتوجيه المزوّدين وبث الأدوات هي عناصر أساسية، لكن سلوك المزوّدين يتغيّر أسبوعيًا ويحتاج إلى إثبات بالسيناريو لكل إصدار.

التغطية تجريبية - 33%الجودة Beta - 78%الاكتمال Beta - 79%جزئي - 6

تنفيذ دورة الوكيل 3 قدرات / مدعوم بإصدار LTS

تجريبي29%

بيتا79%

بيتا79%

[حلقة الوكيل](</ar/concepts/agent-loop>)، [الوكيل](</ar/cli/agent>)، [بيئات تشغيل الوكيل](</ar/concepts/agent-runtimes>)

بيئات التشغيل الخارجية والوكلاء الفرعيون 4 قدرات

تجريبي30%

بيتا79%

بيتا79%

[بيئات تشغيل الوكيل](</ar/concepts/agent-runtimes>)، [Anthropic](</ar/providers/anthropic>)، [Google](</ar/providers/google>)، [الوكلاء الفرعيون](</ar/tools/subagents>)

تنفيذ المزوّد المستضاف 5 قدرات / مدعوم بإصدار LTS

تجريبي20%

بيتا79%

بيتا79%

[Openai](</ar/providers/openai>)، [Anthropic](</ar/providers/anthropic>)، [Google](</ar/providers/google>)، [النماذج](</ar/concepts/models>)

المزوّدون المحليون والمستضافون ذاتيًا 5 قدرات

تجريبي0%

ألفا68%

بيتا79%

[Ollama](</ar/providers/ollama>)، [النماذج](</ar/concepts/models>)، [الوكيل](</ar/cli/agent>)

اختيار النموذج وبيئة التشغيل 4 قدرات / مدعوم بإصدار LTS

تجريبي25%

بيتا79%

بيتا79%

[النماذج](</ar/concepts/models>)، [النماذج](</ar/cli/models>)، [Openai](</ar/providers/openai>)، [بيئات تشغيل الوكيل](</ar/concepts/agent-runtimes>)

مصادقة المزوّد 10 قدرات / مدعوم بإصدار LTS

تجريبي24%

بيتا79%

بيتا79%

[النماذج](</ar/concepts/models>)، [الوكيل](</ar/cli/agent>)، [النماذج](</ar/cli/models>)، [Openai](</ar/providers/openai>)، [Anthropic](</ar/providers/anthropic>)، [Google](</ar/providers/google>)، [الوكلاء الفرعيون](</ar/tools/subagents>)

البث والتقدم 2 قدرات

ألفا56%

بيتا79%

بيتا79%

[البث](</ar/concepts/streaming>)، [حلقة الوكيل](</ar/concepts/agent-loop>)

استدعاءات الأدوات ومعالجة الاستجابة 3 قدرات / مدعوم بإصدار LTS

ألفا65%

بيتا79%

بيتا79%

[حلقة الوكيل](</ar/concepts/agent-loop>)، [Ollama](</ar/providers/ollama>)

عناصر التحكم في تنفيذ الأدوات 6 إمكانات / مدعوم بإصدارات LTS

ألفا50%

بيتا79%

بيتا79%

[سياسة Sandbox مقابل سياسة الأدوات مقابل الصلاحيات المرتفعة](</ar/gateway/sandbox-vs-tool-policy-vs-elevated>)، [حلقة الوكيل](</ar/concepts/agent-loop>)، [الوكلاء الفرعيون](</ar/tools/subagents>)

جلسة العمل والذاكرة ومحرك السياق - M3 بيتا - 9 مجالات

توثيق قوي وتنفيذ نشط. يعتمد النضج على متانة النصوص المنسوخة، وجودة Compaction، والتكافؤ عبر العملاء.

التغطية تجريبية - 30%الجودة بيتا - 77%الاكتمال بيتا - 79%جزئي - 6

إدارة جلسات CLI والنصوص الحرفية قدرتان / مدعوم بإصدارات LTS

تجريبي0%

ألفا68%

بيتا79%

[الجلسة](</ar/concepts/session>), [Compaction لإدارة الجلسات](</ar/reference/session-management-compaction>), [الجلسات](</ar/cli/sessions>)

إدارة الرموز 3 قدرات / مدعوم بإصدارات LTS

تجريبي20%

بيتا79%

بيتا79%

[Compaction](</ar/concepts/compaction>), [السياق](</ar/concepts/context>), [Compaction لإدارة الجلسات](</ar/reference/session-management-compaction>)

محرك السياق قدرتان / مدعوم بإصدارات LTS

ألفا57%

بيتا79%

بيتا79%

[السياق](</ar/concepts/context>), [محرك السياق](</ar/concepts/context-engine>), [حزمة اختبار محرك سياق Codex](</ar/plan/codex-context-engine-harness>)

السجل عبر العملاء وتكافؤ الجلسات قدرتان

تجريبي40%

بيتا79%

بيتا79%

[الدردشة عبر الويب](</ar/web/webchat>), [Android](</ar/platforms/android>), [توجيه القنوات](</ar/channels/channel-routing>)

التشخيصات والصيانة والاسترداد 3 قدرات

تجريبي40%

بيتا79%

بيتا79%

[التشخيصات](</ar/gateway/diagnostics>), [Compaction لإدارة الجلسات](</ar/reference/session-management-compaction>), [العلامات](</ar/diagnostics/flags>)

المطالبات الأساسية والسياق قدرتان / مدعوم بإصدارات LTS

تجريبي38%

بيتا79%

بيتا79%

[السياق](</ar/concepts/context>), [نظافة النص الحرفي](</ar/reference/transcript-hygiene>), [Discord](</ar/channels/discord>)

الذاكرة 5 قدرات

تجريبي46%

بيتا79%

بيتا79%

[إعداد الذاكرة](</ar/reference/memory-config>), [ذاكرة Qmd](</ar/concepts/memory-qmd>), [الذاكرة](</ar/concepts/memory>), [Discord](</ar/channels/discord>)

توجيه الجلسات قدرتان / مدعوم بإصدارات LTS

تجريبي25%

بيتا79%

بيتا79%

[الجلسة](</ar/concepts/session>), [توجيه القنوات](</ar/channels/channel-routing>), [Discord](</ar/channels/discord>)

استبقاء النصوص التفريغية قدرتان / مدعوم ضمن LTS

تجريبي0%

ألفا68%

بيتا79%

[إدارة الجلسات وCompaction](</ar/reference/session-management-compaction>), [نظافة النصوص التفريغية](</ar/reference/transcript-hygiene>)

إطار عمل القنوات - M3 Beta - 8 مجالات

تشترك قنوات كثيرة في عقود التسليم والتوجيه الخاصة بـ Gateway، لكن سلوك القناة يختلف بحسب قيود واجهة API العليا وسياسة الحساب.

التغطية تجريبية - 13%الجودة Beta - 76%الاكتمال Beta - 79%جزئي - 5

أوامر إجراءات القنوات والموافقات 5 قدرات

تجريبي0%

بيتا79%

بيتا79%

[المجموعات](</ar/channels/groups>), [Discord](</ar/channels/discord>), [Googlechat](</ar/channels/googlechat>), [Signal](</ar/channels/signal>), [Matrix](</ar/channels/matrix>)

إعداد القناة 5 قدرات / مدعوم بإصدار LTS

تجريبي14%

بيتا79%

بيتا79%

[الفهرس](</ar/channels>), [الإقران](</ar/channels/pairing>), [استكشاف الأخطاء وإصلاحها](</ar/channels/troubleshooting>), [SDK Channel Plugins](</ar/plugins/sdk-channel-plugins>)

سلوك سلاسل المجموعة والغرفة المحيطة 5 قدرات

تجريبي36%

بيتا79%

بيتا79%

[المجموعات](</ar/channels/groups>), [رسائل المجموعة](</ar/channels/group-messages>), [أحداث الغرفة المحيطة](</ar/channels/ambient-room-events>), [مجموعات البث](</ar/channels/broadcast-groups>), [Discord](</ar/channels/discord>)

الوصول الوارد وبوابات الهوية 5 قدرات / مدعوم بإصدار LTS

تجريبي0%

ألفا68%

بيتا79%

[مجموعات الوصول](</ar/channels/access-groups>), [المجموعات](</ar/channels/groups>), [Discord](</ar/channels/discord>), [LINE](</ar/channels/line>)

مرفقات الوسائط وبيانات القنوات الغنية 4 قدرات

تجريبي0%

ألفا68%

بيتا79%

[LINE](</ar/channels/line>), [Signal](</ar/channels/signal>), [Googlechat](</ar/channels/googlechat>), [Matrix](</ar/channels/matrix>), [Discord](</ar/channels/discord>)

التسليم الصادر ومسار الردود 4 قدرات / مدعوم بإصدار LTS

تجريبي38%

بيتا79%

بيتا79%

[المجموعات](</ar/channels/groups>), [أحداث الغرفة المحيطة](</ar/channels/ambient-room-events>), [Discord](</ar/channels/discord>), [Matrix](</ar/channels/matrix>), [قنوات الإعدادات](</ar/gateway/config-channels>)

توجيه المحادثات وتسليمها 10 قدرات / مدعوم بإصدار LTS

تجريبي19%

بيتا79%

بيتا79%

[توجيه القنوات](</ar/channels/channel-routing>), [المجموعات](</ar/channels/groups>), [Discord](</ar/channels/discord>), [Matrix](</ar/channels/matrix>), [استكشاف الأخطاء وإصلاحها](</ar/channels/troubleshooting>), [مرجع التكوين](</ar/gateway/configuration-reference>)

صحة الحالة وعناصر تحكم المشغل 4 قدرات / مدعوم بإصدار LTS

تجريبي0%

بيتا79%

بيتا79%

[الصحة](</ar/gateway/health>), [مرجع التكوين](</ar/gateway/configuration-reference>), [استكشاف الأخطاء وإصلاحها](</ar/channels/troubleshooting>), [Discord](</ar/channels/discord>)

Observability - M3 Beta - 5 areas

توجد وثائق OTel وPrometheus والتسجيل والتشخيصات. تحتاج إلى تمريرة نضج عامة توضّح "ما الذي ينبغي للمشغّلين النظر إليه أولًا".

التغطية تجريبية - 18%الجودة Beta - 75%الاكتمال Beta - 79%جزئي - 3

الصحة والإصلاح 12 قدرة / مدعومة من LTS

تجريبية28%

Beta79%

Beta79%

[الصحة](</ar/gateway/health>)، [Telegram](</ar/channels/telegram>)، [Doctor](</ar/cli/doctor>)، [Doctor](</ar/gateway/doctor>)، [مسارات Sdk الفرعية](</ar/plugins/sdk-subpaths>)، [الصحة](</ar/cli/health>)، [البروتوكول](</ar/gateway/protocol>)

التسجيل 5 قدرات / مدعومة من LTS

تجريبية0%

Alpha68%

Beta79%

[التسجيل](</ar/logging>)، [التسجيل](</ar/gateway/logging>)، [السجلات](</ar/cli/logs>)

جمع التشخيصات 8 قدرات

تجريبية30%

Beta79%

Beta79%

[التشخيصات](</ar/gateway/diagnostics>)، [الصحة](</ar/gateway/health>)، [حزمة Codex Harness](</ar/plugins/codex-harness>)، [البروتوكول](</ar/gateway/protocol>)

تصدير القياسات عن بُعد 13 قدرة

تجريبية33%

Beta79%

Beta79%

[الخطافات](</ar/plugins/hooks>)، [Opentelemetry](</ar/gateway/opentelemetry>)، [التسجيل](</ar/logging>)، [مسارات Sdk الفرعية](</ar/plugins/sdk-subpaths>)، [Diagnostics Otel](</ar/plugins/reference/diagnostics-otel>)، [Prometheus](</ar/gateway/prometheus>)، [Diagnostics Prometheus](</ar/plugins/reference/diagnostics-prometheus>)

تشخيصات الجلسة 4 قدرات / مدعومة من LTS

تجريبية0%

Alpha68%

Beta79%

[Opentelemetry](</ar/gateway/opentelemetry>)، [Prometheus](</ar/gateway/prometheus>)، [التشخيصات](</ar/gateway/diagnostics>)، [البروتوكول](</ar/gateway/protocol>)

تطبيق الويب Gateway - M3 Beta - 6 مجالات

واجهة مستخدم الويب موثقة مع تدفقات الاقتران والدردشة وPWA وTalk والدفع وGateway البعيد. قم بالترقية بعد بطاقات تقييم المتصفحات المتعددة وPWA على الأجهزة المحمولة.

التغطية تجريبية - 4%الجودة Beta - 74%الاكتمال Beta - 79%لا شيء

المحادثة الفورية في المتصفح 5 قدرات

تجريبي0%

ألفا68%

بيتا79%

[واجهة التحكم](</ar/web/control-ui>), [Protocol](</ar/gateway/protocol>), [المحادثة](</ar/nodes/talk>)

وصول المتصفح والثقة 5 قدرات

تجريبي0%

ألفا68%

بيتا79%

[واجهة التحكم](</ar/web/control-ui>), [لوحة التحكم](</ar/web/dashboard>), [Tailscale](</ar/gateway/tailscale>), [بعيد](</ar/gateway/remote>)

التكوين 5 قدرات

تجريبي0%

ألفا68%

بيتا79%

[واجهة التحكم](</ar/web/control-ui>), [التكوين](</ar/gateway/configuration>)

واجهة مستخدم المتصفح 10 قدرات

تجريبي8%

بيتا79%

بيتا79%

[واجهة التحكم](</ar/web/control-ui>), [الفهرس](</ar/web>), [لوحة التحكم](</ar/web/dashboard>), [Protocol](</ar/gateway/protocol>)

محادثات WebChat 15 قدرة

تجريبي10%

بيتا79%

بيتا79%

[واجهة التحكم](</ar/web/control-ui>), [Webchat](</ar/web/webchat>), [بدء الاستخدام](</ar/start/getting-started>), [توجيه القنوات](</ar/channels/channel-routing>), [عمليات الملفات الآمنة](</ar/gateway/security/secure-file-operations>)

وحدة تحكم المشغل 10 قدرات

تجريبي8%

بيتا79%

بيتا79%

[واجهة التحكم](</ar/web/control-ui>), [الصحة](</ar/gateway/health>), [Protocol](</ar/gateway/protocol>), [لوحة التحكم](</ar/web/dashboard>)

Plugins - M3 Beta - 9 مناطق

توجد وثائق واسعة وأدلة قوية على وقت التشغيل الداخلي عبر البيانات الوصفية، والاكتشاف، والتحميل، وبنية المزود/الأداة، وحدود الموافقة. أبقِ الصف في مرحلة beta حتى تصبح إثباتات API/subpaths العامة لـ SDK والتوزيع الخارجي أقوى.

التغطية تجريبية - 12%الجودة Beta - 72%الاكتمال Beta - 79%جزئي - 7

تأليف Plugins وتحزيمها 8 إمكانات / مدعومة بـ LTS

تجريبي0%

ألفا68%

بيتا79%

[بناء Plugins](</ar/plugins/building-plugins>), [نظرة عامة على SDK](</ar/plugins/sdk-overview>), [نقاط دخول SDK](</ar/plugins/sdk-entrypoints>), [المسارات الفرعية لـ SDK](</ar/plugins/sdk-subpaths>), [البيان](</ar/plugins/manifest>), [المرجع](</ar/plugins/reference>)

Plugins المضمّنة 5 إمكانات / مدعومة بـ LTS

تجريبي0%

ألفا68%

بيتا79%

[مخزون Plugin](</ar/plugins/plugin-inventory>), [Plugins](</ar/cli/plugins>), [تفاصيل المعمارية الداخلية](</ar/plugins/architecture-internals>)

Plugin Canvas 6 إمكانات

تجريبي0%

ألفا68%

بيتا79%

[Canvas](</ar/plugins/reference/canvas>), [Canvas](</ar/refactor/canvas>), [مرجع التهيئة](</ar/gateway/configuration-reference>)

تثبيت Plugins وتشغيلها 6 إمكانات / مدعومة بـ LTS

تجريبي35%

بيتا79%

بيتا79%

[المعمارية](</ar/plugins/architecture>), [تفاصيل المعمارية الداخلية](</ar/plugins/architecture-internals>), [Plugins](</ar/cli/plugins>)

Plugins القنوات 5 إمكانات / مدعومة بـ LTS

تجريبي0%

ألفا68%

بيتا79%

[Plugins قنوات SDK](</ar/plugins/sdk-channel-plugins>), [الوارد عبر قنوات SDK](</ar/plugins/sdk-channel-inbound>), [الصادر عبر قنوات SDK](</ar/plugins/sdk-channel-outbound>)

Plugins المزوّدات والأدوات 6 إمكانات / مدعومة بـ LTS

تجريبي43%

بيتا79%

بيتا79%

[Plugins مزوّدي SDK](</ar/plugins/sdk-provider-plugins>), [Plugins الأدوات](</ar/plugins/tool-plugins>), [إضافة الإمكانات](</ar/plugins/adding-capabilities>)

موافقات Plugin 6 إمكانات / مدعومة بـ LTS

تجريبي0%

ألفا68%

بيتا79%

[طلبات أذونات Plugin](</ar/plugins/plugin-permission-requests>), [موافقات التنفيذ](</ar/tools/exec-approvals>), [Plugins قنوات SDK](</ar/plugins/sdk-channel-plugins>)

نشر Plugins 6 إمكانات / مدعومة بـ LTS

تجريبي0%

ألفا68%

إصدار تجريبي79%

[Plugins](</ar/cli/plugins>), [التوافق](</ar/plugins/compatibility>), [النشر](</ar/clawhub/publishing>)

اختبار Plugins 6 إمكانات

تجريبي27%

إصدار تجريبي79%

إصدار تجريبي79%

[اختبار Sdk](</ar/plugins/sdk-testing>), [إعداد Sdk](</ar/plugins/sdk-setup>), [مجموعة اختبار Codex](</ar/plugins/codex-harness>)

الأمان، والمصادقة، والإقران، والأسرار - M3 بيتا - 6 مجالات

توجد مستندات جيدة وأسطح تقوية. قم بالترقية بعد أن تثبت عمليات تشغيل سيناريوهات الترقية والأمان المنتظمة عدم وجود تراجعات في الإعداد.

التغطية تجريبية - 16%الجودة بيتا - 72%الاكتمال بيتا - 79%جزئي - 5

سياسة الموافقات وضمانات الأدوات إمكانيتان / مدعوم بواسطة LTS

ألفا50%

بيتا79%

بيتا79%

[موافقات التنفيذ](</ar/tools/exec-approvals>), [الموافقات](</ar/cli/approvals>), [طلبات أذونات Plugin](</ar/plugins/plugin-permission-requests>), [فحوصات التدقيق](</ar/gateway/security/audit-checks>)

مصادقة Gateway والوصول البعيد 9 إمكانات / مدعوم بواسطة LTS

تجريبي0%

ألفا68%

بيتا79%

[الفهرس](</ar/gateway/security>), [دليل تشغيل التعرض](</ar/gateway/security/exposure-runbook>), [مصادقة الوكيل الموثوق](</ar/gateway/trusted-proxy-auth>), [Tailscale](</ar/gateway/tailscale>), [بعيد](</ar/gateway/remote>), [مرجع الإعدادات](</ar/gateway/configuration-reference>), [Gateway](</ar/cli/gateway>), [Doctor](</ar/cli/doctor>), [واجهة التحكم](</ar/web/control-ui>), [التحكم بالمتصفح](</ar/tools/browser-control>), [فحوصات التدقيق](</ar/gateway/security/audit-checks>)

التحكم في الوصول إلى القنوات 3 إمكانات / مدعوم بواسطة LTS

تجريبي0%

ألفا68%

بيتا79%

[الإقران](</ar/channels/pairing>), [Telegram](</ar/channels/telegram>), [مجموعات الوصول](</ar/channels/access-groups>), [فحوصات التدقيق](</ar/gateway/security/audit-checks>)

إقران الأجهزة وNode 11 إمكانية / مدعوم بواسطة LTS

تجريبي0%

ألفا68%

بيتا79%

[البروتوكول](</ar/gateway/protocol>), [الأجهزة](</ar/cli/devices>), [الإقران](</ar/channels/pairing>), [الإقران](</ar/gateway/pairing>), [نطاقات المشغل](</ar/gateway/operator-scopes>), [واجهة التحكم](</ar/web/control-ui>), [دردشة الويب](</ar/web/webchat>), [الموافقات](</ar/cli/approvals>)

ثقة Plugin إمكانيتان

تجريبي0%

ألفا68%

بيتا79%

[البيان](</ar/plugins/manifest>), [طلبات أذونات Plugin](</ar/plugins/plugin-permission-requests>), [إدارة Plugins](</ar/plugins/manage-plugins>), [فحوصات التدقيق](</ar/gateway/security/audit-checks>)

سلامة بيانات الاعتماد والأسرار 5 إمكانات / مدعوم بواسطة LTS

تجريبي46%

بيتا79%

بيتا79%

[المصادقة](</ar/gateway/authentication>), [النماذج](</ar/cli/models>), [Openai](</ar/providers/openai>), [Oauth](</ar/concepts/oauth>), [الأسرار](</ar/gateway/secrets>), [الأسرار](</ar/cli/secrets>), [سطح بيانات اعتماد Secretref](</ar/reference/secretref-credential-surface>), [فحوصات التدقيق](</ar/gateway/security/audit-checks>)

الأتمتة: Cron، والخطافات، والمهام، والاستقصاء - M3 بيتا - 6 مجالات

موثق وقابل للاستخدام، لكن إثبات السيناريو يجب أن يغطي التسليم غير المراقب، وإعادة المحاولة، ووضوح الفشل.

التغطية تجريبية - 2%الجودة بيتا - 72%الاكتمال بيتا - 79%لا شيء

مهام Cron 15 إمكانية

تجريبي0%

بيتا79%

بيتا79%

[مهام Cron](</ar/automation/cron-jobs>), [Cron](</ar/cli/cron>), [البروتوكول](</ar/gateway/protocol>), [المهام](</ar/automation/tasks>), [Discord](</ar/channels/discord>)

إدخال الأحداث 15 إمكانية

تجريبي0%

ألفا68%

بيتا79%

[Telegram](</ar/channels/telegram>), [Zalo](</ar/channels/zalo>), [استكشاف الأخطاء وإصلاحها](</ar/channels/troubleshooting>), [iMessage من BlueBubbles](</ar/channels/imessage-from-bluebubbles>), [تكامل Gmail Pub/Sub](</ar/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pub/Sub](</ar/automation/cron-jobs>), [Webhooks](</ar/cli/webhooks>), [Webhooks](</ar/automation/cron-jobs#webhooks>), [Webhook](</ar/automation/cron-jobs>)

خطافات الأتمتة 11 إمكانية

تجريبي0%

ألفا68%

بيتا79%

[الخطافات](</ar/automation/hooks>), [الخطافات](</ar/cli/hooks>), [الخطافات](</ar/plugins/hooks>), [طلبات أذونات Plugin](</ar/plugins/plugin-permission-requests>), [مسارات SDK الفرعية](</ar/plugins/sdk-subpaths>)

المهام والتدفقات في الخلفية 10 إمكانات

تجريبي0%

ألفا68%

بيتا79%

[المهام](</ar/automation/tasks>), [الفهرس](</ar/automation>), [المهام](</ar/cli/tasks>), [TaskFlow](</ar/automation/taskflow>), [وقت تشغيل SDK](</ar/plugins/sdk-runtime>)

Heartbeat 5 إمكانات

تجريبي14%

بيتا79%

بيتا79%

[الفهرس](</ar/automation>), [Heartbeat](</ar/gateway/heartbeat>), [الالتزامات](</ar/concepts/commitments>)

عناصر التحكم في الاستطلاع الدوري 10 إمكانات

تجريبي0%

ألفا68%

بيتا79%

[الاستطلاع الدوري](</ar/cli/message>), [رسالة](</ar/cli/message>), [Telegram](</ar/channels/telegram>), [Microsoft Teams](</ar/channels/msteams>), [عملية الخلفية](</ar/gateway/background-process>)

فهم الوسائط وتوليد الوسائط - M2 ألفا - 6 مجالات

يوجد سطح إمكانات واسع، لكن اختلاف المزوّدين وحدود الملفات والتكافؤ بين Node والتطبيق تجعل هذا غير مستقر بعد.

التغطية تجريبي - 2%الجودة ألفا - 64%الاكتمال ألفا - 68%لا شيء

استيعاب الوسائط والوصول إليها 8 قدرات

تجريبي0%

ألفا61%

ألفا68%

[نظرة عامة على الوسائط](</ar/tools/media-overview>), [فهم الوسائط](</ar/nodes/media-understanding>), [عمليات الملفات الآمنة](</ar/gateway/security/secure-file-operations>), [PDF](</ar/tools/pdf>), [توليد الصور](</ar/tools/image-generation>), [رمز QR](</ar/cli/qr>), [LINE](</ar/channels/line>), [WhatsApp](</ar/channels/whatsapp>)

معالجة وسائط القنوات 5 قدرات

تجريبي0%

ألفا61%

ألفا68%

[الصور](</ar/nodes/images>), [نظرة عامة على الوسائط](</ar/tools/media-overview>), [Discord](</ar/channels/discord>)

تكوين الوسائط 1 قدرات

تجريبي0%

ألفا61%

ألفا68%

[نظرة عامة على الوسائط](</ar/tools/media-overview>), [توليد الصور](</ar/tools/image-generation>), [البيان](</ar/plugins/manifest>), [بيئة Codex الاختبارية](</ar/plugins/codex-harness>)

تسليم تحويل النص إلى كلام 2 قدرات

تجريبي0%

ألفا61%

ألفا68%

[TTS](</ar/tools/tts>), [نظرة عامة على الوسائط](</ar/tools/media-overview>), [Discord](</ar/channels/discord>)

فهم الوسائط 12 قدرة

تجريبي7%

ألفا69%

ألفا69%

[الصوت](</ar/nodes/audio>), [فهم الوسائط](</ar/nodes/media-understanding>), [نظرة عامة على الوسائط](</ar/tools/media-overview>), [WhatsApp](</ar/channels/whatsapp>), [الصور](</ar/nodes/images>), [الاستنتاج](</ar/cli/infer>), [PDF](</ar/tools/pdf>)

توليد الوسائط 17 قدرة

تجريبي5%

ألفا69%

ألفا69%

[توليد الصور](</ar/tools/image-generation>), [نظرة عامة على الوسائط](</ar/tools/media-overview>), [Skills](</ar/tools/skills>), [توليد الموسيقى](</ar/tools/music-generation>), [توليد الفيديو](</ar/tools/video-generation>)

الصوت والمحادثة في الوقت الفعلي - M2 ألفا - 6 مناطق

توجد تطبيقات متعددة عبر واجهة التحكم والتطبيقات والمزوّدين. يحتاج إلى بطاقات تقييم للكمون وأوضاع الفشل والإعداد قبل الإصدار التجريبي.

التغطية تجريبية - 0%الجودة ألفا - 61%الاكتمال ألفا - 68%لا شيء

موفرو المحادثة 7 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[Openai](</ar/providers/openai>)، [Google](</ar/providers/google>)، [إضافات موفري SDK](</ar/plugins/sdk-provider-plugins>)، [المحادثة](</ar/nodes/talk>)، [واجهة التحكم](</ar/web/control-ui>)

جلسات المحادثة في الوقت الفعلي 11 إمكانية

تجريبي0%

ألفا61%

ألفا68%

[المحادثة](</ar/nodes/talk>)، [واجهة التحكم](</ar/web/control-ui>)

الكلام والتفريغ 5 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[المحادثة](</ar/nodes/talk>)، [Openai](</ar/providers/openai>)، [Google](</ar/providers/google>)

محادثة التطبيق الأصلي 4 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[المحادثة](</ar/nodes/talk>)، [Voicewake](</ar/platforms/mac/voicewake>)

التنبيه الصوتي والتوجيه 4 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[Voicewake](</ar/nodes/voicewake>)، [Voicewake](</ar/platforms/mac/voicewake>)، [تراكب الصوت](</ar/platforms/mac/voice-overlay>)

قابلية مراقبة المحادثة 5 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[واجهة التحكم](</ar/web/control-ui>)، [تراكب الصوت](</ar/platforms/mac/voice-overlay>)، [المحادثة](</ar/nodes/talk>)

TUI - ألفا M2 - 5 مجالات

موجود في المستندات والمصدر، لكنه أقل ظهورًا كسير عمل أساسي للمستخدم. يحتاج إلى تعريف صريح للسيناريو.

التغطية تجريبية - 0%الجودة ألفا - 59%الاكتمال ألفا - 66%لا شيء

أوضاع وقت التشغيل 14 قدرة

تجريبي0%

ألفا59%

ألفا66%

[TUI](</ar/cli/tui>), [TUI](</ar/web/tui>), [الفهرس](</ar/cli>)

الإدخال والأوامر 8 قدرات

تجريبي0%

ألفا59%

ألفا66%

[TUI](</ar/web/tui>)

إدارة الجلسات 3 قدرات

تجريبي0%

ألفا59%

ألفا66%

[TUI](</ar/web/tui>), [الجلسات](</ar/cli/sessions>)

تنفيذ الصدفة المحلية 4 قدرات

تجريبي0%

ألفا59%

ألفا66%

[TUI](</ar/web/tui>), [TUI](</ar/cli/tui>)

العرض وسلامة الإخراج 4 قدرات

تجريبي0%

ألفا59%

ألفا66%

[TUI](</ar/web/tui>), [QR](</ar/cli/qr>), [السجلات](</ar/cli/logs>), [الإكمال](</ar/cli/completion>)

ClawHub - M2 Alpha - 4 areas

توجد وثائق عامة ومفهوم للنظام البيئي. يحتاج إلى بطاقات تقييم للتثبيت والثقة والتحديث والتراجع والتوافق.

التغطية تجريبية - 0%الجودة ألفا - 58%الاكتمال ألفا - 62%لا يوجد

النشر 7 إمكانات

تجريبي0%

ألفا54%

ألفا55%

[النشر](</ar/clawhub/publishing>), [إنشاء Skills](</ar/tools/creating-skills>), [المجتمع](</ar/plugins/community>)

اكتشاف الكتالوج 5 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[Plugin](</ar/tools/plugin>), [Plugins](</ar/cli/plugins>), [Skills](</ar/cli/skills>), [Skills](</ar/tools/skills>), [المجتمع](</ar/plugins/community>)

التوافق والثقة 12 إمكانية

تجريبي0%

ألفا55%

ألفا56%

[Plugin](</ar/tools/plugin>), [Plugins](</ar/cli/plugins>), [التوافق](</ar/plugins/compatibility>), [جرد Plugin](</ar/plugins/plugin-inventory>), [النشر](</ar/clawhub/publishing>), [Skills](</ar/tools/skills>), [إعدادات Skills](</ar/tools/skills-config>)

دورة حياة Plugin وصحته 26 إمكانية

تجريبي0%

ألفا61%

ألفا68%

[Plugin](</ar/tools/plugin>), [Plugins](</ar/cli/plugins>), [Skills](</ar/cli/skills>), [Skills](</ar/tools/skills>), [البروتوكول](</ar/gateway/protocol>), [الحزم](</ar/plugins/bundles>), [حل التبعيات](</ar/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 areas

يُعد SDK تطبيق OpenClaw عقد تطبيق خارجيًا مستقلًا ومنفصلًا عن تشغيل Gateway وPlugin SDK. يُظهر التقييم الحالي مسار `@openclaw/sdk` حقيقيًا، مع فجوات حول التغليف العام، والاكتشاف التلقائي، والموافقات، والمساعدات، والتوافق.

التغطية تجريبية - 3%الجودة ألفا - 54%الاكتمال ألفا - 53%لا شيء

واجهة API للعميل 4 إمكانات

تجريبي0%

Alpha51%

Alpha50%

[Openclaw Sdk](</ar/gateway/external-apps>)، [تصميم Openclaw Sdk Api](</ar/gateway/external-apps>)

الوصول إلى Gateway 5 إمكانات

تجريبي0%

Alpha53%

Alpha54%

[Openclaw Sdk](</ar/gateway/external-apps>)، [تصميم Openclaw Sdk Api](</ar/gateway/external-apps>)، [البروتوكول](</ar/gateway/protocol>)، [الفهرس](</ar/gateway/security>)

محادثات الوكيل 6 إمكانات

تجريبي0%

Alpha52%

Alpha52%

[Openclaw Sdk](</ar/gateway/external-apps>)، [تصميم Openclaw Sdk Api](</ar/gateway/external-apps>)، [البروتوكول](</ar/gateway/protocol>)

الأحداث والموافقات 5 إمكانات

تجريبي0%

Alpha52%

Alpha52%

[Openclaw Sdk](</ar/gateway/external-apps>)، [تصميم Openclaw Sdk Api](</ar/gateway/external-apps>)، [البروتوكول](</ar/gateway/protocol>)

مساعدات الموارد 5 إمكانات

تجريبي17%

Alpha62%

Alpha53%

[Openclaw Sdk](</ar/gateway/external-apps>)، [تصميم Openclaw Sdk Api](</ar/gateway/external-apps>)

التوافق 5 إمكانات

تجريبي0%

Alpha54%

Alpha55%

[تصميم Openclaw Sdk Api](</ar/gateway/external-apps>)، [Typebox](</ar/concepts/typebox>)، [البروتوكول](</ar/gateway/protocol>)

### المنصة

مضيف Linux Gateway - M4 Stable - 5 مجالات

يُوصى ببيئة تشغيل Node، وتم توثيق خدمة مستخدم systemd، وإرشادات VPS/الحاويات واسعة.

التغطية تجريبية - 0%الجودة Beta - 75%الاكتمال مستقر - 89%جزئي - 4

إعداد المضيف والتحديثات 4 قدرات / مدعومة بإصدارات LTS

تجريبي0%

بيتا75%

مستقر89%

[الفهرس](</ar/install>), [التحديث](</ar/install/updating>), [Linux](</ar/platforms/linux>), [الفهرس](</ar/platforms>)

تشغيل Gateway والتحكم في الخدمة 6 قدرات / مدعومة بإصدارات LTS

تجريبي0%

بيتا75%

مستقر89%

[الفهرس](</ar/gateway>), [Gateway](</ar/cli/gateway>), [Linux](</ar/platforms/linux>), [VPS](</ar/vps>)

الوصول البعيد والأمان 6 قدرات / مدعومة بإصدارات LTS

تجريبي0%

بيتا75%

مستقر89%

[البعيد](</ar/gateway/remote>), [Tailscale](</ar/gateway/tailscale>), [دليل تشغيل التعرض](</ar/gateway/security/exposure-runbook>), [المصادقة](</ar/gateway/authentication>), [الأسرار](</ar/gateway/secrets>)

التشخيص والإصلاح 4 قدرات / مدعومة بإصدارات LTS

تجريبي0%

بيتا75%

مستقر89%

[الحالة](</ar/cli/status>), [السجلات](</ar/cli/logs>), [الفحص](</ar/cli/doctor>), [التشخيصات](</ar/gateway/diagnostics>), [الفهرس](</ar/gateway>)

أهداف النشر 3 قدرات

تجريبي0%

بيتا75%

مستقر89%

[VPS](</ar/vps>), [Docker](</ar/install/docker>), [Hetzner](</ar/install/hetzner>), [Digitalocean](</ar/install/digitalocean>), [Kubernetes](</ar/install/kubernetes>), [Podman](</ar/install/podman>)

مضيف Gateway على macOS - M4 مستقر - 7 مجالات

تم توثيق مسار خدمة LaunchAgent، وأوضاع Gateway المحلية/البعيدة، وتثبيت CLI، وتكامل التطبيق.

التغطية تجريبية - 0%الجودة بيتا - 74%الاكتمال مستقر - 88%لا شيء

إعداد CLI 4 إمكانات

تجريبي0%

بيتا74%

مستقر88%

[Macos](</ar/platforms/macos>), [Gateway المضمّن](</ar/platforms/mac/bundled-gateway>), [المثبّت](</ar/install/installer>), [Node](</ar/install/node>)

تكامل Gateway المحلي 9 إمكانات

تجريبي0%

بيتا74%

مستقر88%

[Macos](</ar/platforms/macos>), [Gateway المضمّن](</ar/platforms/mac/bundled-gateway>), [عن بُعد](</ar/platforms/mac/remote>), [الفهرس](</ar/gateway>), [Gateway](</ar/cli/gateway>), [Bonjour](</ar/gateway/bonjour>)

وضع Gateway عن بُعد 5 إمكانات

تجريبي0%

بيتا74%

مستقر88%

[عن بُعد](</ar/platforms/mac/remote>), [عن بُعد](</ar/gateway/remote>), [Tailscale](</ar/gateway/tailscale>)

دورة حياة خدمة Gateway 10 إمكانات

تجريبي0%

بيتا74%

مستقر88%

[Macos](</ar/platforms/macos>), [Gateway المضمّن](</ar/platforms/mac/bundled-gateway>), [Gateway](</ar/cli/gateway>), [الفهرس](</ar/gateway>), [التحديث](</ar/cli/update>), [التحديث](</ar/install/updating>), [إلغاء التثبيت](</ar/install/uninstall>), [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)

التشخيصات وقابلية المراقبة 4 إمكانات

تجريبي0%

بيتا74%

مستقر88%

[Gateway المضمّن](</ar/platforms/mac/bundled-gateway>), [Macos](</ar/platforms/macos>), [Gateway](</ar/cli/gateway>), [الفحص](</ar/gateway/doctor>), [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)

الأذونات والإمكانات الأصلية 4 إمكانات

تجريبي0%

بيتا74%

مستقر88%

[Macos](</ar/platforms/macos>), [عن بُعد](</ar/platforms/mac/remote>)

الملفات الشخصية والعزل 5 إمكانات

تجريبي0%

بيتا74%

مستقر88%

[Gateways متعددة](</ar/gateway/multiple-gateways>), [الفهرس](</ar/gateway>), [Gateway](</ar/cli/gateway>)

استضافة Docker وPodman - M3 بيتا - 4 مجالات

توجد وثائق التثبيت وهي مسارات نشر شائعة. قم بالترقية بعد أن تلتقط اختبارات دخان الإصدار المتكررة سلوك الترقية ووحدات التخزين.

التغطية تجريبي - 7%الجودة بيتا - 71%الاكتمال بيتا - 79%لا شيء

إعداد الحاوية 6 قدرات

تجريبي0%

ألفا68%

بيتا79%

[Docker](</ar/install/docker>), [Podman](</ar/install/podman>)

عمليات الحاويات 11 قدرة

تجريبي0%

ألفا68%

بيتا79%

[Podman](</ar/install/podman>), [Docker Vm Runtime](</ar/install/docker-vm-runtime>), [Docker](</ar/install/docker>), [Hetzner](</ar/install/hetzner>), [Hostinger](</ar/install/hostinger>)

إصدار الصور والتحقق منها 5 قدرات

تجريبي29%

بيتا79%

بيتا79%

[Docker](</ar/install/docker>), [Docker Vm Runtime](</ar/install/docker-vm-runtime>), [التحقق الكامل من الإصدار](</ar/reference/full-release-validation>)

صندوق عزل الوكيل والأدوات 3 قدرات

تجريبي0%

ألفا68%

بيتا79%

[Docker](</ar/install/docker>), [Docker Vm Runtime](</ar/install/docker-vm-runtime>)

Windows عبر WSL2 - M3 Beta - 6 مجالات

مسار Windows الموصى به مع إرشادات systemd/خدمة المستخدم ومستندات سلسلة التمهيد. روّج بعد بطاقات تقييم التثبيت/التحديث المتكررة.

التغطية تجريبي - 6%الجودة ألفا - 69%الاكتمال بيتا - 79%جزئي - 5

إعداد WSL 6 قدرات / مدعوم بإصدارات LTS

تجريبي0%

ألفا67%

بيتا79%

[Windows](</ar/platforms/windows>)، [بدء الاستخدام](</ar/start/getting-started>)

CLI 8 قدرات / مدعوم بإصدارات LTS

تجريبي0%

ألفا67%

بيتا79%

[Windows](</ar/platforms/windows>)، [بدء الاستخدام](</ar/start/getting-started>)، [التحديث](</ar/install/updating>)، [الإعداد الأولي](</ar/cli/onboard>)، [التشخيص](</ar/cli/doctor>)، [الحالة](</ar/cli/status>)، [السجلات](</ar/cli/logs>)

دورة حياة خدمة Gateway 10 قدرات / مدعوم بإصدارات LTS

تجريبي0%

ألفا67%

بيتا79%

[Windows](</ar/platforms/windows>)، [الفهرس](</ar/gateway>)، [التشخيص](</ar/gateway/doctor>)

الوصول إلى Gateway وتعريضه 11 قدرة / مدعوم بإصدارات LTS

تجريبي0%

ألفا67%

بيتا79%

[المصادقة](</ar/gateway/authentication>)، [الأسرار](</ar/gateway/secrets>)، [الوصول البعيد](</ar/gateway/remote>)، [دليل تشغيل التعريض](</ar/gateway/security/exposure-runbook>)، [Windows](</ar/platforms/windows>)

التشخيص والإصلاح 6 قدرات / مدعوم بإصدارات LTS

تجريبي38%

بيتا79%

بيتا79%

[Windows](</ar/platforms/windows>)، [الحالة](</ar/cli/status>)، [السجلات](</ar/cli/logs>)، [التشخيص](</ar/cli/doctor>)، [التشخيص](</ar/gateway/doctor>)

المتصفح وواجهة التحكم 6 قدرات

تجريبي0%

ألفا67%

بيتا79%

[استكشاف أخطاء CDP البعيد للمتصفح على WSL2 في Windows وإصلاحها](</ar/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)، [المتصفح](</ar/tools/browser>)، [واجهة التحكم](</ar/web/control-ui>)

Raspberry Pi وأجهزة Linux الصغيرة - M3 بيتا - 4 مجالات

توجد مستندات المنصة ومسار Gateway قائم على Linux. يحتاج إلى إثبات اختبار إصدار دخاني خاص بالعتاد للانتقال إلى مستوى أعلى.

التغطية تجريبي - 0%الجودة ألفا - 67%الاكتمال بيتا - 79%لا شيء

الإعداد والتوافق 12 قدرة

تجريبي0%

ألفا67%

بيتا79%

[Raspberry Pi](</ar/install/raspberry-pi>), [الفهرس](</ar/install>), [الأسئلة الشائعة للتشغيل الأول](</ar/help/faq-first-run>), [الأسئلة الشائعة](</ar/help/faq>), [Linux](</ar/platforms/linux>), [المثبّت](</ar/install/installer>)

الوصول عن بُعد والمصادقة 9 قدرات

تجريبي0%

ألفا67%

بيتا79%

[Raspberry Pi](</ar/install/raspberry-pi>), [المصادقة](</ar/gateway/authentication>), [الأسرار](</ar/gateway/secrets>), [الإقران](</ar/gateway/pairing>), [الأجهزة](</ar/cli/devices>), [عن بُعد](</ar/gateway/remote>), [Tailscale](</ar/gateway/tailscale>)

وقت تشغيل Gateway 10 قدرات

تجريبي0%

ألفا67%

بيتا79%

[الفهرس](</ar/gateway>), [Gateway](</ar/cli/gateway>), [Raspberry Pi](</ar/install/raspberry-pi>), [Linux](</ar/platforms/linux>), [VPS](</ar/vps>)

الأداء والتشخيصات 5 قدرات

تجريبي0%

ألفا67%

بيتا79%

[Raspberry Pi](</ar/install/raspberry-pi>), [Linux](</ar/platforms/linux>), [الصحة](</ar/gateway/health>), [التشخيصات](</ar/gateway/diagnostics>)

تطبيق macOS المرافق - M3 بيتا - 8 مجالات

يتوفر تطبيق غني لشريط القوائم، والأذونات، ووضع Node، وCanvas، والتنبيه الصوتي، وWebChat، ووضع التشغيل عن بُعد. لا يزال سريع التغير بما يكفي لتجنب مستوى مستقر.

التغطية تجريبي - 0%الجودة ألفا - 66%الاكتمال بيتا - 78%لا شيء

لوحة الرسم 4 قدرات

تجريبي0%

ألفا66%

بيتا78%

[لوحة الرسم](</ar/platforms/mac/canvas>), [macOS](</ar/platforms/macos>), [دردشة الويب](</ar/web/webchat>)

الإعداد المحلي 7 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Gateway المضمّن](</ar/platforms/mac/bundled-gateway>), [macOS](</ar/platforms/macos>), [العملية الفرعية](</ar/platforms/mac/child-process>), [إعداد التطوير](</ar/platforms/mac/dev-setup>)

الحالة والإعدادات 5 قدرات

تجريبي0%

ألفا66%

بيتا78%

[شريط القوائم](</ar/platforms/mac/menu-bar>), [الأيقونة](</ar/platforms/mac/icon>), [macOS](</ar/platforms/macos>), [الصحة](</ar/platforms/mac/health>), [التسجيل](</ar/platforms/mac/logging>), [عن بُعد](</ar/platforms/mac/remote>)

القدرات الأصلية 5 قدرات

تجريبي0%

ألفا66%

بيتا78%

[macOS](</ar/platforms/macos>), [Xpc](</ar/platforms/mac/xpc>), [الأذونات](</ar/platforms/mac/permissions>), [التوقيع](</ar/platforms/mac/signing>), [Peekaboo](</ar/platforms/mac/peekaboo>)

الاتصالات البعيدة 3 قدرات

تجريبي0%

ألفا66%

بيتا78%

[عن بُعد](</ar/platforms/mac/remote>), [macOS](</ar/platforms/macos>), [عن بُعد](</ar/gateway/remote>)

الصوت والتحدث 3 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Voicewake](</ar/platforms/mac/voicewake>), [تراكب الصوت](</ar/platforms/mac/voice-overlay>), [التحدث](</ar/nodes/talk>), [macOS](</ar/platforms/macos>)

دردشة الويب 3 قدرات

تجريبي0%

ألفا66%

بيتا78%

[دردشة الويب](</ar/platforms/mac/webchat>), [macOS](</ar/platforms/macos>), [دردشة الويب](</ar/web/webchat>)

دردشة الويب البعيدة 5 قدرات

تجريبي0%

ألفا66%

بيتا78%

[دردشة الويب](</ar/platforms/mac/webchat>), [عن بُعد](</ar/gateway/remote>), [عن بُعد](</ar/platforms/mac/remote>)

تطبيق Android - M2 ألفا - 7 مجالات

مسار Google Play العام موجود، لكن وثائق التطبيق ما زالت تصف إعادة البناء بأنها في مرحلة ألفا شديدة جدًا وتشير إلى أعمال تقوية الإصدار.

التغطية تجريبية - 0%الجودة ألفا - 59%الاكتمال ألفا - 66%لا شيء

التقاط الوسائط إمكان واحد

تجريبي0%

ألفا59%

ألفا66%

[Android](</ar/platforms/android>)، [الكاميرا](</ar/nodes/camera>)

دردشة الهاتف المحمول إمكان واحد

تجريبي0%

ألفا59%

ألفا66%

[Android](</ar/platforms/android>)

إعداد الاتصال إمكان واحد

تجريبي0%

ألفا59%

ألفا66%

[Android](</ar/platforms/android>)، [Bonjour](</ar/gateway/bonjour>)، [الإقران](</ar/gateway/pairing>)

التوزيع 3 إمكانات

تجريبي0%

ألفا59%

ألفا66%

[Android](</ar/platforms/android>)

الإعدادات إمكان واحد

تجريبي0%

ألفا59%

ألفا66%

[Android](</ar/platforms/android>)

الصوت إمكان واحد

تجريبي0%

ألفا59%

ألفا66%

[Android](</ar/platforms/android>)، [التحدث](</ar/nodes/talk>)

وقت تشغيل الجهاز 2 إمكانات

تجريبي0%

ألفا59%

ألفا66%

[Android](</ar/platforms/android>)، [استكشاف الأخطاء وإصلاحها](</ar/nodes/troubleshooting>)، [البروتوكول](</ar/gateway/protocol>)

Windows الأصلي - M2 ألفا - 4 مجالات

تعمل تدفقات CLI/Gateway الأساسية، لكن المستندات ما زالت توصي باستخدام WSL2 للتجربة الكاملة وتذكر محاذير التشغيل الأصلي.

التغطية تجريبي - 0%الجودة ألفا - 58%الاكتمال ألفا - 66%جزئي - 1

CLI 9 قدرات / مدعوم بإصدارات LTS

تجريبي0%

ألفا54%

ألفا64%

[الفهرس](</ar/install>), [المثبّت](</ar/install/installer>), [Windows](</ar/platforms/windows>), [بدء الاستخدام](</ar/start/getting-started>), [الإعداد الأولي](</ar/cli/onboard>)

إدارة Gateway 11 قدرة

تجريبي0%

ألفا59%

ألفا66%

[Windows](</ar/platforms/windows>), [الفهرس](</ar/gateway>), [Gateway](</ar/cli/gateway>), [Doctor](</ar/cli/doctor>)

الشبكات 4 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Windows](</ar/platforms/windows>), [الفهرس](</ar/gateway>), [Gateway](</ar/cli/gateway>)

التحديثات 4 قدرات

تجريبي0%

ألفا59%

ألفا66%

[التحديث](</ar/install/updating>), [CI](</ar/ci>)

استضافة Kubernetes - M2 ألفا - 4 مجالات

استضافة Kubernetes هي مسار نشر عنقودي متميز قائم على Kustomize. يُظهر التقييم الحالي مسار نشر حقيقيًا بالحد الأدنى مع فجوات حول CI الخاص بـ Kubernetes، وحزم ingress/TLS/NetworkPolicy، والنسخ الاحتياطي/الاستعادة، وتقوية التعرض للإنتاج.

التغطية تجريبية - 0%الجودة ألفا - 55%الاكتمال ألفا - 61%لا شيء

إعداد النشر 5 قدرات

تجريبي0%

ألفا55%

ألفا61%

[Kubernetes](</ar/install/kubernetes>), [الفهرس](</ar/install>)

التكوين والأسرار 5 قدرات

تجريبي0%

ألفا55%

ألفا61%

[Kubernetes](</ar/install/kubernetes>), [الأسرار](</ar/gateway/secrets>), [البيئة](</ar/help/environment>)

الوصول والتعريض 5 قدرات

تجريبي0%

ألفا55%

ألفا61%

[Kubernetes](</ar/install/kubernetes>), [المصادقة](</ar/gateway/authentication>), [عن بُعد](</ar/gateway/remote>), [دليل تشغيل التعريض](</ar/gateway/security/exposure-runbook>)

دورة حياة المجموعة 5 قدرات

تجريبي0%

ألفا55%

ألفا61%

[Kubernetes](</ar/install/kubernetes>), [الفهرس](</ar/gateway>)

تطبيق iOS - M1 تجريبي - 8 مجالات

معاينة داخلية / ألفا مبكرة جدًا. توجد تدفقات دفع مدعومة بالترحيل عبر TestFlight، لكن لا يوجد توزيع عام بعد.

التغطية تجريبية - 0%الجودة تجريبية - 41%الاكتمال تجريبي - 44%لا شيء

الوسائط والمشاركة قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>), [الكاميرا](</ar/nodes/camera>)

اللوحة والشاشة قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>), [اللوحة](</ar/plugins/reference/canvas>)

الدردشة والجلسات قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>), [دردشة الويب](</ar/web/webchat>), [البروتوكول](</ar/gateway/protocol>)

إعداد Gateway وتشخيصه 7 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>), [الاقتران](</ar/channels/pairing>)

التوزيع قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>)

أوامر الجهاز قدرتان

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>), [البروتوكول](</ar/gateway/protocol>)

الإشعارات والخلفية قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>), [التهيئة](</ar/gateway/configuration>)

الصوت قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[Ios](</ar/platforms/ios>), [التحدث](</ar/nodes/talk>)

مسار تثبيت Nix - M1 تجريبي - 5 مجالات

مسار تثبيت اختياري. يحتاج إلى وعد دعم أوضح قبل الترقية إلى ألفا/بيتا.

التغطية تجريبية - 0%الجودة تجريبية - 41%الاكتمال تجريبي - 44%لا شيء

تسليم التثبيت 4 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[Nix](</ar/install/nix>)، [الفهرس](</ar/install>)، [دليل الوثائق](</ar/start/docs-directory>)

دورة حياة Plugin 4 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[إدارة Plugins](</ar/plugins/manage-plugins>)، [Plugin](</ar/tools/plugin>)، [Nix](</ar/install/nix>)

التفعيل وتجربة مستخدم التطبيق 7 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[Nix](</ar/install/nix>)

الإعداد والحالة 7 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[Nix](</ar/install/nix>)، [الإعداد](</ar/cli/setup>)، [البيئة](</ar/help/environment>)

وقت تشغيل الخدمة والحواجز الوقائية 8 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[Nix](</ar/install/nix>)، [الإعداد](</ar/cli/setup>)، [Doctor](</ar/cli/doctor>)، [التحديث](</ar/cli/update>)

أسطح مرافق watchOS - M1 تجريبي - 5 مجالات

يحتوي المصدر على أسطح تطبيق/امتداد Watch؛ ولا تعرض الوثائق العامة هذا بعد كميزة للمستخدم.

التغطية تجريبية - 0%الجودة تجريبية - 41%الاكتمال تجريبي - 44%لا شيء

التسليم والاسترداد 7 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[iOS](</ar/platforms/ios>)

موافقات التنفيذ 3 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[موافقات التنفيذ](</ar/tools/exec-approvals>), [iOS](</ar/platforms/ios>)

التوزيع والدعم 6 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[iOS](</ar/platforms/ios>)

الإشعارات والردود 7 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[iOS](</ar/platforms/ios>)

واجهة مستخدم تطبيق الساعة 3 قدرات

تجريبي0%

تجريبي41%

تجريبي44%

[iOS](</ar/platforms/ios>)

تطبيق Linux المصاحب - M0 مخطط له - 5 مجالات

تذكر الوثائق أن تطبيقات Linux المصاحبة الأصلية مخطط لها؛ أما Gateway فهو مسار Linux المدعوم اليوم.

التغطية تجريبية - 0%الجودة تجريبية - 19%الاكتمال تجريبي - 21%لا شيء

توزيع التطبيق 3 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Linux](</ar/platforms/linux>)، [الفهرس](</ar/platforms>)، [الفهرس](</ar/install>)

اتصال Gateway 4 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Linux](</ar/platforms/linux>)، [الفهرس](</ar/gateway>)، [الاقتران](</ar/gateway/pairing>)، [عن بُعد](</ar/gateway/remote>)

الدردشة والجلسات 3 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Linux](</ar/platforms/linux>)، [البروتوكول](</ar/gateway/protocol>)، [دردشة الويب](</ar/web/webchat>)

قدرات سطح المكتب 9 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Linux](</ar/platforms/linux>)، [موافقات التنفيذ](</ar/tools/exec-approvals>)، [الأسرار](</ar/gateway/secrets>)، [الفهرس](</ar/nodes>)، [التنفيذ](</ar/tools/exec>)، [التحدث](</ar/nodes/talk>)، [الكاميرا](</ar/nodes/camera>)

الحالة والتشخيصات 7 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Linux](</ar/platforms/linux>)، [OpenClaw](</ar/start/openclaw>)، [الفحص](</ar/gateway/doctor>)

Native Windows companion app - M0 Planned - 5 areas

مخطط فقط.

التغطية تجريبية - 0%الجودة تجريبية - 19%الاكتمال تجريبي - 21%لا شيء

التثبيت والتحديثات 4 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Windows](</ar/platforms/windows>)، [الفهرس](</ar/install>)

اتصال Gateway 3 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Windows](</ar/platforms/windows>)، [الفهرس](</ar/gateway>)، [الإقران](</ar/gateway/pairing>)، [البعيد](</ar/gateway/remote>)

جلسات الدردشة قدرتان

تجريبي0%

تجريبي19%

تجريبي21%

[Windows](</ar/platforms/windows>)، [البروتوكول](</ar/gateway/protocol>)

الحالة والإصلاح 5 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Windows](</ar/platforms/windows>)، [Doctor](</ar/gateway/doctor>)، [الفهرس](</ar/gateway>)

أدوات سطح المكتب والأذونات 10 قدرات

تجريبي0%

تجريبي19%

تجريبي21%

[Windows](</ar/platforms/windows>)، [الفهرس](</ar/nodes>)، [Exec](</ar/tools/exec>)، [موافقات Exec](</ar/tools/exec-approvals>)، [الفهرس](</ar/gateway/security>)

### القناة

Discord - M4 مستقر - 6 مجالات

مستندات معمقة وتغطية واسعة للميزات. ينبغي أن تظل مسارات الصوت/التفويض مصنفة بشكل منفصل كبيتا/ألفا.

التغطية تجريبي - 0%الجودة بيتا - 73%الاكتمال مستقر - 87%جزئي - 4

إعداد القنوات وتشغيلها 10 قدرات / مدعوم بإصدارات LTS

تجريبي0%

بيتا73%

مستقر87%

[Discord](</ar/channels/discord>), [Discord](</ar/plugins/reference/discord>), [Fly](</ar/install/fly>), [أوامر الشرطة المائلة](</ar/tools/slash-commands>), [الصحة](</ar/gateway/health>), [القنوات](</ar/cli/channels>), [قنوات التكوين](</ar/gateway/config-channels>)

الوصول والهوية 6 قدرات / مدعوم بإصدارات LTS

تجريبي0%

بيتا73%

مستقر87%

[Discord](</ar/channels/discord>), [الاقتران](</ar/channels/pairing>), [مجموعات الوصول](</ar/channels/access-groups>), [المجموعات](</ar/channels/groups>)

توجيه المحادثات وتسليمها 12 قدرة / مدعوم بإصدارات LTS

تجريبي0%

بيتا73%

مستقر87%

[Discord](</ar/channels/discord>), [توجيه القنوات](</ar/channels/channel-routing>), [المجموعات](</ar/channels/groups>), [مجموعات الوصول](</ar/channels/access-groups>), [وكلاء ACP](</ar/tools/acp-agents>), [الوكلاء الفرعيون](</ar/tools/subagents>)

الوسائط والمحتوى الغني 1 قدرة / مدعوم بإصدارات LTS

تجريبي0%

بيتا73%

مستقر87%

[Discord](</ar/channels/discord>)

عناصر التحكم الأصلية والموافقات 5 قدرات

تجريبي0%

بيتا73%

مستقر87%

[Discord](</ar/channels/discord>), [أوامر الشرطة المائلة](</ar/tools/slash-commands>)

الصوت والمكالمات في الوقت الفعلي 5 قدرات

تجريبي0%

بيتا73%

مستقر87%

[Discord](</ar/channels/discord>), [Openai](</ar/providers/openai>), [Elevenlabs](</ar/providers/elevenlabs>), [أتمتة QA E2E](</ar/concepts/qa-e2e-automation>), [قنوات التكوين](</ar/gateway/config-channels>)

Telegram - M3 Beta - 5 areas

القناة الأساسية ناضجة بما يكفي للاستخدام المنتظم، لكن تجربة المستخدم عالية التباين وحالات الوسائط الطرفية تحتاج إلى إثبات سيناريو متكرر.

التغطية تجريبية - 0%الجودة ألفا - 68%الاكتمال بيتا - 78%كامل - 5

إعداد القنوات وعملياتها 10 قدرات / مدعوم بإصدار LTS

تجريبي0%

ألفا66%

بيتا78%

[Telegram](</ar/channels/telegram>)، [قنوات الإعدادات](</ar/gateway/config-channels>)، [القنوات](</ar/cli/channels>)

الوصول والهوية 10 قدرات / مدعوم بإصدار LTS

تجريبي0%

ألفا66%

بيتا78%

[Telegram](</ar/channels/telegram>)، [الإقران](</ar/channels/pairing>)، [مجموعات الوصول](</ar/channels/access-groups>)، [المجموعات](</ar/channels/groups>)، [الوكلاء المتعددون](</ar/concepts/multi-agent>)

توجيه المحادثات وتسليمها 1 قدرة / مدعوم بإصدار LTS

تجريبي0%

ألفا66%

بيتا78%

[Telegram](</ar/channels/telegram>)، [المجموعات](</ar/channels/groups>)، [الوكلاء المتعددون](</ar/concepts/multi-agent>)

الوسائط والمحتوى المنسق 1 قدرة / مدعوم بإصدار LTS

تجريبي0%

ألفا66%

بيتا78%

[Telegram](</ar/channels/telegram>)، [الموقع](</ar/channels/location>)

عناصر التحكم الأصلية والموافقات 9 قدرات / مدعوم بإصدار LTS

تجريبي0%

بيتا77%

بيتا79%

[Telegram](</ar/channels/telegram>)، [موافقات التنفيذ](</ar/tools/exec-approvals>)، [التفاعلات](</ar/tools/reactions>)

Slack - M3 بيتا - 5 مجالات

وثائق قناة وسطح توجيه من الدرجة الأولى. يحتاج إلى بطاقات تقييم لسيناريو تثبيت مساحة العمل وإدارتها.

التغطية تجريبي - 0%الجودة ألفا - 66%الاكتمال بيتا - 78%كامل - 5

إعداد القناة وعملياتها 10 قدرات / مدعومة بإصدارات LTS

تجريبي0%

ألفا66%

بيتا78%

[Slack](</ar/channels/slack>)، [Slack](</ar/plugins/reference/slack>)، [الأسرار](</ar/gateway/secrets>)، [أتمتة ضمان الجودة من طرف إلى طرف](</ar/concepts/qa-e2e-automation>)، [استكشاف الأخطاء وإصلاحها](</ar/channels/troubleshooting>)

الوصول والهوية 1 قدرة / مدعومة بإصدارات LTS

تجريبي0%

ألفا66%

بيتا78%

[Slack](</ar/channels/slack>)، [الإقران](</ar/channels/pairing>)

توجيه المحادثات وتسليمها 5 قدرات / مدعومة بإصدارات LTS

تجريبي0%

ألفا66%

بيتا78%

[Slack](</ar/channels/slack>)، [الحماية من حلقة البوت](</ar/channels/bot-loop-protection>)، [الإقران](</ar/channels/pairing>)

الوسائط والمحتوى الغني 1 قدرة / مدعومة بإصدارات LTS

تجريبي0%

ألفا66%

بيتا78%

[Slack](</ar/channels/slack>)، [أتمتة ضمان الجودة من طرف إلى طرف](</ar/concepts/qa-e2e-automation>)

عناصر التحكم الأصلية والموافقات 8 قدرات / مدعومة بإصدارات LTS

تجريبي0%

ألفا66%

بيتا78%

[Slack](</ar/channels/slack>)، [أوامر الشرطة المائلة](</ar/tools/slash-commands>)، [موافقات Exec](</ar/tools/exec-approvals>)

iMessage وBlueBubbles - M3 بيتا - 5 مجالات

يعمل iMessage المدعوم عبر imsg على مضيف macOS Messages مسجّل الدخول؛ وتتطلب إعدادات BlueBubbles القديمة ترحيلاً. أبقِ أذونات macOS، وغلاف SSH، وSIP/واجهة API الخاصة، ومحاذير الترحيل واضحة.

التغطية تجريبية - 0%الجودة ألفا - 66%الاكتمال بيتا - 78%لا شيء

إعداد القنوات وعملياتها 11 قدرة

تجريبي0%

ألفا66%

بيتا78%

[Bluebubbles Imessage](</ar/announcements/bluebubbles-imessage>), [Imessage من Bluebubbles](</ar/channels/imessage-from-bluebubbles>), [تهيئة القنوات](</ar/gateway/config-channels>), [Imessage](</ar/channels/imessage>)

الوصول والهوية 6 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Imessage](</ar/channels/imessage>), [Imessage من Bluebubbles](</ar/channels/imessage-from-bluebubbles>), [تهيئة القنوات](</ar/gateway/config-channels>)

توجيه المحادثات وتسليمها 4 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Imessage](</ar/channels/imessage>)

الوسائط والمحتوى الغني 7 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Imessage](</ar/channels/imessage>), [Imessage من Bluebubbles](</ar/channels/imessage-from-bluebubbles>), [تهيئة القنوات](</ar/gateway/config-channels>)

عناصر التحكم والموافقات الأصلية 3 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Imessage](</ar/channels/imessage>)

WhatsApp - M3 بيتا - 5 مجالات

المسار الأساسي مهم وموثق؛ وتبقيه تقلبات Baileys/الجلسات في المنبع دون Stable.

التغطية تجريبي - 0%الجودة ألفا - 66%الاكتمال بيتا - 78%لا شيء

إعداد القنوات وعملياتها 5 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[WhatsApp](</ar/channels/whatsapp>), [قنوات التهيئة](</ar/gateway/config-channels>), [WhatsApp](</ar/plugins/reference/whatsapp>), [أتمتة QA E2E](</ar/concepts/qa-e2e-automation>), [Doctor](</ar/gateway/doctor>)

الوصول والهوية 7 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[WhatsApp](</ar/channels/whatsapp>), [قنوات التهيئة](</ar/gateway/config-channels>), [أتمتة QA E2E](</ar/concepts/qa-e2e-automation>), [الاقتران](</ar/channels/pairing>)

توجيه المحادثات وتسليمها 4 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[WhatsApp](</ar/channels/whatsapp>), [رسائل المجموعات](</ar/channels/group-messages>)

الوسائط والمحتوى الغني 2 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[WhatsApp](</ar/channels/whatsapp>)

عناصر التحكم والموافقات الأصلية 2 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[WhatsApp](</ar/channels/whatsapp>)

Matrix - M2 Alpha - 6 مجالات

مدعوم عبر Plugin مرفق. يحتاج إلى بطاقات تقييم للجسر والمصادقة ودورة حياة الغرفة.

التغطية تجريبي - 0%الجودة ألفا - 60%الاكتمال ألفا - 67%لا شيء

إعداد القنوات وعملياتها 5 قدرات

تجريبي0%

ألفا60%

ألفا67%

[Matrix](</ar/channels/matrix>)، [ترحيل Matrix](</ar/channels/matrix-migration>)

الوصول والهوية 7 قدرات

تجريبي0%

ألفا60%

ألفا67%

[Matrix](</ar/channels/matrix>)، [المجموعات](</ar/channels/groups>)، [الحماية من حلقات البوت](</ar/channels/bot-loop-protection>)

توجيه المحادثات وتسليمها 1 قدرة

تجريبي0%

ألفا60%

ألفا67%

[Matrix](</ar/channels/matrix>)

الوسائط والمحتوى الغني 1 قدرة

تجريبي0%

ألفا60%

ألفا67%

[Matrix](</ar/channels/matrix>)

عناصر التحكم الأصلية والموافقات 6 قدرات

تجريبي0%

ألفا60%

ألفا67%

[Matrix](</ar/channels/matrix>)

التشفير والتحقق 3 قدرات

تجريبي0%

ألفا60%

ألفا67%

[Matrix](</ar/channels/matrix>)، [ترحيل Matrix](</ar/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 areas

قناة موثقة، لكن إعداد المؤسسة/المسؤول يزيد مخاطر النضج.

التغطية تجريبية - 0%الجودة ألفا - 59%الاكتمال ألفا - 66%لا شيء

إعداد القنوات وعملياتها 16 قدرة

تجريبي0%

Alpha59%

Alpha66%

[Googlechat](</ar/channels/googlechat>), [Googlechat](</ar/plugins/reference/googlechat>), [قنوات الإعداد](</ar/gateway/config-channels>), [مرجع CLI للمعالج](</ar/start/wizard-cli-reference>), [الأسرار](</ar/gateway/secrets>), [سطح بيانات اعتماد Secretref](</ar/reference/secretref-credential-surface>), [الصحة](</ar/gateway/health>), [جرد Plugins](</ar/plugins/plugin-inventory>), [الفهرس](</ar/channels>)

الوصول والهوية 11 قدرة

تجريبي0%

Alpha59%

Alpha66%

[Googlechat](</ar/channels/googlechat>), [الإقران](</ar/channels/pairing>), [مجموعات الوصول](</ar/channels/access-groups>), [قنوات الإعداد](</ar/gateway/config-channels>), [الحماية من حلقة البوت](</ar/channels/bot-loop-protection>), [توجيه القنوات](</ar/channels/channel-routing>)

توجيه المحادثات وتسليمها 1 قدرة

تجريبي0%

Alpha59%

Alpha66%

[Googlechat](</ar/channels/googlechat>), [الحماية من حلقة البوت](</ar/channels/bot-loop-protection>), [مجموعات الوصول](</ar/channels/access-groups>), [توجيه القنوات](</ar/channels/channel-routing>)

الوسائط والمحتوى الغني 1 قدرة

تجريبي0%

Alpha59%

Alpha66%

[Googlechat](</ar/channels/googlechat>), [الرسالة](</ar/cli/message>), [فهم الوسائط](</ar/nodes/media-understanding>), [سطح بيانات اعتماد Secretref](</ar/reference/secretref-credential-surface>)

عناصر التحكم والموافقات الأصلية 16 قدرة

تجريبي0%

Alpha59%

Alpha66%

[Googlechat](</ar/channels/googlechat>), [الرسالة](</ar/cli/message>), [فهم الوسائط](</ar/nodes/media-understanding>), [سطح بيانات اعتماد Secretref](</ar/reference/secretref-credential-surface>), [التفاعلات](</ar/tools/reactions>), [أوامر Slash](</ar/tools/slash-commands>), [إعداد الوكلاء](</ar/gateway/config-agents>), [إعادة هيكلة دورة حياة الرسائل](</ar/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 مجالات

تحتاج تدفقات مصادقة/إدارة المؤسسة إلى إثبات سيناريو صريح.

التغطية تجريبي - 0%الجودة Alpha - 59%الاكتمال Alpha - 66%لا شيء

إعداد القنوات وتشغيلها 9 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Msteams](</ar/channels/msteams>)، [Msteams](</ar/plugins/reference/msteams>)، [قنوات التكوين](</ar/gateway/config-channels>)، [الصحة](</ar/gateway/health>)

الوصول والهوية 9 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Msteams](</ar/channels/msteams>)، [الاقتران](</ar/channels/pairing>)، [مجموعات الوصول](</ar/channels/access-groups>)

توجيه المحادثات وتسليمها 5 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Msteams](</ar/channels/msteams>)، [المجموعات](</ar/channels/groups>)، [توجيه القنوات](</ar/channels/channel-routing>)

الوسائط والمحتوى الغني 5 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Msteams](</ar/channels/msteams>)

عناصر التحكم والموافقات الأصلية 5 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Msteams](</ar/channels/msteams>)، [موافقات التنفيذ المتقدمة](</ar/tools/exec-approvals-advanced>)

Signal - M2 ألفا - 5 مجالات

توجد وثائق قناة مدعومة؛ وتحتاج إلى إثبات أقوى للتثبيت وإعادة الاتصال.

التغطية تجريبية - 0%الجودة ألفا - 59%الاكتمال ألفا - 66%لا شيء

إعداد القنوات والعمليات 7 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Signal](</ar/channels/signal>)، [Signal](</ar/plugins/reference/signal>)

الوصول والهوية 6 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Signal](</ar/channels/signal>)

توجيه المحادثات وتسليمها 1 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Signal](</ar/channels/signal>)

الوسائط والمحتوى الغني 7 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Signal](</ar/channels/signal>)

عناصر التحكم والموافقات الأصلية 3 قدرات

تجريبي0%

ألفا59%

ألفا66%

[Signal](</ar/channels/signal>)

Feishu، QQ Bot، WeChat، Yuanbao، Zalo، Zalo Personal، القنوات الإقليمية - M2 ألفا - 4 مجالات

تغطية إقليمية مهمة، لكن يجب معايرة مستوى الدعم العام حسب نوع الحساب وموافقة المصدر upstream وإثبات المشرف.

التغطية تجريبي - 0%الجودة ألفا - 55%الاكتمال ألفا - 58%لا شيء

إعداد القنوات وعملياتها 6 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[الفهرس](</ar/channels>)، [الاقتران](</ar/channels/pairing>)، [Feishu](</ar/plugins/reference/feishu>)، [البنية الداخلية للمعمارية](</ar/plugins/architecture-internals>)

الوصول والهوية إمكانية واحدة

تجريبي0%

ألفا53%

ألفا54%

لا توجد مستندات مرتبطة

توجيه المحادثات وتسليمها إمكانية واحدة

تجريبي0%

ألفا53%

ألفا54%

لا توجد مستندات مرتبطة

الوسائط والمحتوى الغني إمكانية واحدة

تجريبي0%

ألفا53%

ألفا54%

لا توجد مستندات مرتبطة

Mattermost وLINE وIRC وNextcloud Talk وNostr وTwitch وTlon وSynology Chat - M2 ألفا - 4 مجالات

توجد أسطح مدعومة، لكن من المرجح أن يختلف النضج حسب التغطية من المصدر العلوي والمشرفين. قيّم كل واحد على حدة لاحقًا.

التغطية تجريبية - 0%الجودة ألفا - 53%الاكتمال ألفا - 54%لا شيء

إعداد القناة وعملياتها إمكانية واحدة

تجريبي0%

ألفا53%

ألفا54%

لا توجد مستندات مرتبطة

الوصول والهوية إمكانية واحدة

تجريبي0%

ألفا53%

ألفا54%

لا توجد مستندات مرتبطة

توجيه المحادثات وتسليمها إمكانية واحدة

تجريبي0%

ألفا53%

ألفا54%

لا توجد مستندات مرتبطة

الوسائط والمحتوى الغني إمكانية واحدة

تجريبي0%

ألفا53%

ألفا54%

لا توجد مستندات مرتبطة

قناة المكالمات الصوتية - M1 تجريبي - 5 مجالات

مسار اختياري/Plugin بسلوك معقد في الوقت الفعلي. يحتاج إلى بطاقة قياس للسيناريوهات قبل الإصدار التجريبي العام.

التغطية تجريبية - 0%الجودة تجريبية - 41%الاكتمال تجريبي - 44%لا شيء

إعداد القنوات وتشغيلها قدرتان

تجريبي0%

تجريبي41%

تجريبي44%

[المكالمة الصوتية](</ar/cli/voicecall>), [المكالمة الصوتية](</ar/plugins/voice-call>), [البروتوكول](</ar/gateway/protocol>)

الوصول والهوية قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[المكالمة الصوتية](</ar/plugins/voice-call>), [المكالمة الصوتية](</ar/cli/voicecall>)

توجيه المحادثات وتسليمها قدرة واحدة

تجريبي0%

تجريبي41%

تجريبي44%

[المكالمة الصوتية](</ar/plugins/voice-call>)

الوسائط والمحتوى الغني قدرتان

تجريبي0%

تجريبي41%

تجريبي44%

[المكالمة الصوتية](</ar/plugins/voice-call>), [مخزون Plugin](</ar/plugins/plugin-inventory>)

الصوت والمكالمات في الوقت الحقيقي قدرتان

تجريبي0%

تجريبي41%

تجريبي44%

[المكالمة الصوتية](</ar/plugins/voice-call>)

### الموفر والأداة

أتمتة المتصفح، والتنفيذ، وأدوات صندوق العزل - M3 بيتا - 3 مجالات

أدوات النواة موثقة، لكن ينبغي أن تظل تجربة مستخدم أمان المضيف والأذونات قيد مراجعة نشطة في بطاقة النقاط.

التغطية تجريبية - 21%الجودة بيتا - 75%الاكتمال بيتا - 79%جزئي - 2

أتمتة المتصفح 8 إمكانات

تجريبي13%

بيتا79%

بيتا79%

[التحكم في المتصفح](</ar/tools/browser-control>), [الاختبار](</ar/help/testing>), [المتصفح](</ar/tools/browser>), [الفهرس](</ar/gateway/security>), [فحوصات التدقيق](</ar/gateway/security/audit-checks>)

استدعاء الأدوات وتنفيذها 6 إمكانات / مدعوم من LTS

ألفا50%

بيتا79%

بيتا79%

[التنفيذ](</ar/tools/exec>), [عملية الخلفية](</ar/gateway/background-process>), [API HTTP لاستدعاء الأدوات](</ar/gateway/tools-invoke-http-api>), [نطاقات المشغّل](</ar/gateway/operator-scopes>), [البروتوكول](</ar/gateway/protocol>), [موافقات التنفيذ](</ar/tools/exec-approvals>), [موافقات التنفيذ المتقدمة](</ar/tools/exec-approvals-advanced>), [مرفّع](</ar/tools/elevated>)

صندوق العزل وسياسة الأدوات 6 إمكانات / مدعوم من LTS

تجريبي0%

ألفا68%

بيتا79%

[العزل في صندوق](</ar/gateway/sandboxing>), [صندوق العزل مقابل سياسة الأدوات مقابل المرفّع](</ar/gateway/sandbox-vs-tool-policy-vs-elevated>), [أدوات صندوق العزل متعددة الوكلاء](</ar/tools/multi-agent-sandbox-tools>), [مرجع مشغّل Codex](</ar/plugins/codex-harness-reference>), [أدوات التكوين](</ar/gateway/config-tools>)

مسار موفّر OpenAI وCodex - M3 بيتا - 5 مجالات

مستندات معمّقة، ومسار OAuth/الاشتراك، والصوت الفوري، والصورة، وسلوك التوافق. يبقي تغيّر الموفّر المتكرر هذا المسار دون مستوى مستقر من دون إثبات بطاقة نتائج الإصدار.

التغطية تجريبية - 26%الجودة بيتا - 74%الاكتمال بيتا - 79%جزئي - 3

النموذج والمصادقة 6 إمكانات / مدعوم من LTS

تجريبي44%

Beta79%

Beta79%

[Openai](</ar/providers/openai>), [عدة Codex](</ar/plugins/codex-harness>), [النماذج](</ar/concepts/models>), [Oauth](</ar/concepts/oauth>), [مرجع عدة Codex](</ar/plugins/codex-harness-reference>), [مراقبة المصادقة](</ar/gateway/authentication>)

توافق الاستجابات والأدوات 4 إمكانات / مدعوم من LTS

تجريبي40%

Beta79%

Beta79%

[Openai](</ar/providers/openai>), [واجهة Openresponses Http Api](</ar/gateway/openresponses-http-api>), [واجهة Openai Http Api](</ar/gateway/openai-http-api>), [Plugins أصلية لـ Codex](</ar/plugins/codex-native-plugins>)

عدة Codex الأصلية إمكانتان / مدعوم من LTS

تجريبي44%

Beta79%

Beta79%

[عدة Codex](</ar/plugins/codex-harness>), [وقت تشغيل عدة Codex](</ar/plugins/codex-harness-runtime>), [مرجع عدة Codex](</ar/plugins/codex-harness-reference>), [Plugins أصلية لـ Codex](</ar/plugins/codex-native-plugins>)

إدخال الصور والمتعدد الوسائط إمكانتان

تجريبي0%

Alpha67%

Beta79%

[Openai](</ar/providers/openai>), [توليد الصور](</ar/tools/image-generation>), [الصور](</ar/nodes/images>)

الصوت والصوت الفوري إمكانتان

تجريبي0%

Alpha67%

Beta79%

[Openai](</ar/providers/openai>), [Discord](</ar/channels/discord>), [مكالمة صوتية](</ar/plugins/voice-call>)

أدوات بحث الويب - M3 Beta - 4 مجالات

توجد عدة مزودين ووثائق. يحتاج إلى إثبات الحصة/الخطأ/SSRF لكل عائلة مزودين.

التغطية تجريبية - 9%الجودة Beta - 74%الاكتمال Beta - 79%لا شيء

موفرو البحث 19 قدرة

تجريبي11%

بيتا79%

بيتا79%

[الويب](</ar/tools/web>), [بحث Brave](</ar/tools/brave-search>), [Tavily](</ar/tools/tavily>), [بحث Exa](</ar/tools/exa-search>), [Firecrawl](</ar/tools/firecrawl>), [بحث Perplexity](</ar/tools/perplexity-search>), [بحث Duckduckgo](</ar/tools/duckduckgo-search>), [بحث Searxng](</ar/tools/searxng-search>), [بحث Gemini](</ar/tools/gemini-search>), [بحث Grok](</ar/tools/grok-search>), [بحث Kimi](</ar/tools/kimi-search>), [بحث Minimax](</ar/tools/minimax-search>), [بحث Ollama](</ar/tools/ollama-search>), [مسارات SDK الفرعية](</ar/plugins/sdk-subpaths>), [نظرة عامة على SDK](</ar/plugins/sdk-overview>), [البيان](</ar/plugins/manifest>)

الإعداد والتشخيصات 9 قدرات

تجريبي0%

ألفا68%

بيتا79%

[الويب](</ar/tools/web>), [جلب الويب](</ar/tools/web-fetch>), [الأسئلة الشائعة](</ar/help/faq>), [تكاليف استخدام API](</ar/reference/api-usage-costs>), [بحث Brave](</ar/tools/brave-search>), [بحث Perplexity](</ar/tools/perplexity-search>), [Tavily](</ar/tools/tavily>), [Firecrawl](</ar/tools/firecrawl>)

سلامة الشبكة 4 قدرات

تجريبي0%

ألفا68%

بيتا79%

[الويب](</ar/tools/web>), [جلب الويب](</ar/tools/web-fetch>), [Firecrawl](</ar/tools/firecrawl>), [بحث Searxng](</ar/tools/searxng-search>)

توفر الأدوات والجلب 11 قدرة

تجريبي25%

بيتا79%

بيتا79%

[أدوات التكوين](</ar/gateway/config-tools>), [جلب الويب](</ar/tools/web-fetch>), [الويب](</ar/tools/web>), [الأسئلة الشائعة](</ar/help/faq>)

Anthropic provider path - M3 Beta - 5 areas

موفر نماذج من الدرجة الأولى. يحتاج إلى إثبات متكرر لسيناريوهات المصادقة والفهرس واستدعاء الأدوات.

التغطية تجريبي - 0%الجودة بيتا - 71%الاكتمال بيتا - 78%لا شيء

مصادقة المزوّد والاسترداد 9 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Anthropic](</ar/providers/anthropic>)، [Doctor](</ar/gateway/doctor>)، [أمثلة التكوين](</ar/gateway/configuration-examples>)، [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)، [تخزين المطالبات مؤقتًا](</ar/reference/prompt-caching>)

اختيار النموذج وبيئة التشغيل 10 قدرات

تجريبي0%

بيتا78%

بيتا79%

[Anthropic](</ar/providers/anthropic>)، [وكلاء التكوين](</ar/gateway/config-agents>)، [النماذج](</ar/concepts/models>)، [واجهات CLI الخلفية](</ar/gateway/cli-backends>)

نقل الطلبات ودلالات الدور 10 قدرات

تجريبي0%

بيتا77%

بيتا79%

[Anthropic](</ar/providers/anthropic>)، [تخزين المطالبات مؤقتًا](</ar/reference/prompt-caching>)، [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)، [واجهات CLI الخلفية](</ar/gateway/cli-backends>)، [مزوّدو النماذج](</ar/concepts/model-providers>)

ذاكرة التخزين المؤقت للمطالبات والسياق 5 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Anthropic](</ar/providers/anthropic>)، [تخزين المطالبات مؤقتًا](</ar/reference/prompt-caching>)، [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>)، [Heartbeat](</ar/gateway/heartbeat>)

مدخلات الوسائط 4 قدرات

تجريبي0%

ألفا66%

بيتا78%

[Anthropic](</ar/providers/anthropic>)، [وكلاء التكوين](</ar/gateway/config-agents>)

مسار مزوّد Google - M3 بيتا - 5 مجالات

مزوّد من الدرجة الأولى مع واجهات للنماذج والزمن الحقيقي. يحتاج إلى تقييم منفصل لـ Live/Talk.

التغطية تجريبي - 0%الجودة ألفا - 66%الاكتمال بيتا - 78%لا شيء

إعداد الموفر وبيانات الاعتماد 10 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[Google](</ar/providers/google>), [موفرو النماذج](</ar/concepts/model-providers>)

توجيه النماذج ونقاط النهاية 10 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[Google](</ar/providers/google>), [موفرو النماذج](</ar/concepts/model-providers>), [Google](</ar/plugins/reference/google>), [بحث Gemini](</ar/tools/gemini-search>)

وقت تشغيل Gemini المباشر 9 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[Google](</ar/providers/google>), [موفرو النماذج](</ar/concepts/model-providers>), [الأسئلة الشائعة حول النماذج](</ar/help/faq-models>), [الاختبار المباشر](</ar/help/testing-live>)

الوسائط والبحث والوقت الفعلي 10 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[Google](</ar/plugins/reference/google>), [Google](</ar/providers/google>)

التخزين المؤقت للمطالبات 5 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[التخزين المؤقت للمطالبات](</ar/reference/prompt-caching>), [Google](</ar/providers/google>), [موفرو النماذج](</ar/concepts/model-providers>), [استخدام الرموز](</ar/reference/token-use>)

مسار موفر OpenRouter - M3 بيتا - 4 مجالات

مسار الموفر الموحّد موثّق وقيّم، لكن السلوك الخاص بالنماذج يختلف.

التغطية تجريبي - 0%الجودة ألفا - 66%الاكتمال بيتا - 78%لا يوجد

إعداد المزوّد والمصادقة 14 إمكانية

تجريبي0%

ألفا66%

بيتا78%

[Openrouter](</ar/providers/openrouter>)، [موفّرو النماذج](</ar/concepts/model-providers>)، [التكوين](</ar/cli/configure>)، [المصادقة](</ar/gateway/authentication>)، [البيئة](</ar/help/environment>)، [النماذج](</ar/cli/models>)، [النماذج](</ar/concepts/models>)

تشغيل الدردشة والتطبيع 15 إمكانية

تجريبي0%

ألفا66%

بيتا78%

[Openrouter](</ar/providers/openrouter>)، [موفّرو النماذج](</ar/concepts/model-providers>)، [تخزين الموجّهات مؤقتًا](</ar/reference/prompt-caching>)

استرداد المزوّد والتشخيصات 5 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[تجاوز فشل النماذج](</ar/concepts/model-failover>)، [Openrouter](</ar/providers/openrouter>)، [النماذج](</ar/cli/models>)

توليد الوسائط والكلام 7 إمكانات

تجريبي0%

ألفا66%

بيتا78%

[Openrouter](</ar/providers/openrouter>)، [توليد الصور](</ar/tools/image-generation>)، [توليد الموسيقى](</ar/tools/music-generation>)، [نظرة عامة على الوسائط](</ar/tools/media-overview>)، [توليد الفيديو](</ar/tools/video-generation>)، [تحويل النص إلى كلام](</ar/tools/tts>)

أدوات توليد الصور والفيديو والموسيقى - M2 ألفا - 5 مجالات

توجد الإمكانية عبر المزوّدين، لكن الجودة وزمن الاستجابة وتوافق المعلمات تختلف بدرجة كبيرة جدًا تجعل الوصول إلى بيتا غير مناسب دون إثبات لكل مزوّد.

التغطية تجريبي - 0%الجودة ألفا - 61%الاكتمال ألفا - 68%لا شيء

توجيه الوسائط واكتشافها 4 قدرات

تجريبي0%

ألفا61%

ألفا68%

[وكلاء التكوين](</ar/gateway/config-agents>)، [إنشاء الصور](</ar/tools/image-generation>)، [إنشاء الفيديو](</ar/tools/video-generation>)، [إنشاء الموسيقى](</ar/tools/music-generation>)

دورة حياة المهام وتسليمها 12 قدرة

تجريبي0%

ألفا61%

ألفا68%

[نظرة عامة على الوسائط](</ar/tools/media-overview>)، [إنشاء الصور](</ar/tools/image-generation>)، [إنشاء الفيديو](</ar/tools/video-generation>)، [إنشاء الموسيقى](</ar/tools/music-generation>)

إنشاء الصور 9 قدرات

تجريبي0%

ألفا61%

ألفا68%

[إنشاء الصور](</ar/tools/image-generation>)، [Infer](</ar/cli/infer>)، [نظرة عامة على الوسائط](</ar/tools/media-overview>)

إنشاء الفيديو 11 قدرة

تجريبي0%

ألفا61%

ألفا68%

[إنشاء الفيديو](</ar/tools/video-generation>)، [Runway](</ar/providers/runway>)، [Pixverse](</ar/providers/pixverse>)، [Fal](</ar/providers/fal>)، [Openrouter](</ar/providers/openrouter>)

إنشاء الموسيقى 6 قدرات

تجريبي0%

ألفا61%

ألفا68%

[إنشاء الموسيقى](</ar/tools/music-generation>)

موفرو النماذج المحلية: Ollama وvLLM وSGLang وLM Studio - M2 ألفا - 5 مجالات

مفيد وموثق، لكن تفاوت البيئة مرتفع.

التغطية تجريبية - 0%الجودة ألفا - 61%الاكتمال ألفا - 68%لا شيء

إعداد المزوّد، ودورة الحياة، والتشخيصات 12 قدرة

تجريبي0%

Alpha61%

Alpha68%

[النماذج المحلية](</ar/gateway/local-models>), [Lmstudio](</ar/providers/lmstudio>), [Ollama](</ar/providers/ollama>), [Vllm](</ar/providers/vllm>), [خدمات النماذج المحلية](</ar/gateway/local-model-services>), [وكلاء الإعدادات](</ar/gateway/config-agents>), [استكشاف الأخطاء وإصلاحها](</ar/gateway/troubleshooting>), [Doctor](</ar/gateway/doctor>)

Plugins المزوّدين الأصلية 10 قدرات

تجريبي0%

Alpha61%

Alpha68%

[Ollama](</ar/providers/ollama>), [Lmstudio](</ar/providers/lmstudio>)

توافق وقت التشغيل المتوافق مع OpenAI 8 قدرات

تجريبي0%

Alpha61%

Alpha68%

[Vllm](</ar/providers/vllm>), [Sglang](</ar/providers/sglang>), [النماذج المحلية](</ar/gateway/local-models>), [Lmstudio](</ar/providers/lmstudio>)

الذاكرة المحلية والتضمينات 5 قدرات

تجريبي0%

Alpha61%

Alpha68%

[الذاكرة](</ar/concepts/memory>), [Doctor](</ar/gateway/doctor>)

سلامة الشبكة وعناصر التحكم في المطالبة قدرتان

تجريبي0%

Alpha61%

Alpha68%

[الفهرس](</ar/gateway/security>), [أدوات الإعدادات](</ar/gateway/config-tools>), [النماذج المحلية](</ar/gateway/local-models>)

المزوّدون المستضافون طويلو الذيل - M2 Alpha - 3 مجالات

توجد العديد من صفحات المستندات/المرجع؛ ينبغي توليد الدرجة من بيانات تعريف المزوّدين بالإضافة إلى تغطية اختبار smoke المباشر.

التغطية تجريبية - 0%الجودة ألفا - 61%الاكتمال ألفا - 68%لا يوجد

موفرو LLM المستضافون 12 إمكانية

تجريبي0%

ألفا61%

ألفا68%

[الفهرس](</ar/providers>), [موفرو النماذج](</ar/concepts/model-providers>), [الاختبار المباشر](</ar/help/testing-live>), [الإعداد الأولي](</ar/cli/onboard>)

موفرو الوسائط المستضافون 8 إمكانات

تجريبي0%

ألفا61%

ألفا68%

[البيان](</ar/plugins/manifest>), [الاختبار المباشر](</ar/help/testing-live>), [الفهرس](</ar/providers>)

عمليات المزوّدين 12 إمكانية

تجريبي0%

ألفا61%

ألفا68%

[الفهرس](</ar/providers>), [موفرو النماذج](</ar/concepts/model-providers>), [البيان](</ar/plugins/manifest>), [الاختبار المباشر](</ar/help/testing-live>), [النماذج](</ar/cli/models>)

Was this useful?YesNo

Open issue