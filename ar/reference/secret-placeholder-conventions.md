---
title: اصطلاحات العناصر النائبة للأسرار
source_url: https://docs.openclaw.ai/ar/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# اصطلاحات العناصر النائبة للأسرار

استخدم عناصر نائبة قابلة للقراءة البشرية لكنها لا تشبه الأسرار الحقيقية.

## النمط الموصى به

  * فضّل القيم الوصفية مثل `example-openai-key-not-real` أو `example-discord-bot-token`.
  * في مقتطفات shell، فضّل `${OPENAI_API_KEY}` على السلاسل المضمنة التي تشبه الرموز المميزة.
  * اجعل الأمثلة مزيفة بوضوح ومحددة النطاق بحسب الغرض (المزوّد، القناة، نوع المصادقة).


## تجنب هذه الأنماط في الوثائق

  * نص ترويسة أو تذييل مفتاح خاص PEM حرفي.
  * البادئات التي تشبه بيانات اعتماد حية، مثل `sk-...` و`xoxb-...` و`AKIA...`.
  * رموز bearer تبدو واقعية ومنسوخة من سجلات وقت التشغيل.


## مثال

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue