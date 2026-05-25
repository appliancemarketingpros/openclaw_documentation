---
title: ایجاد Skills
source_url: https://docs.openclaw.ai/fa/tools/creating-skills
scraped_at: 2026-05-25
---

Skills به عامل می‌آموزد چگونه و چه زمانی از ابزارها استفاده کند. هر مهارت یک دایرکتوری است که شامل یک فایل `SKILL.md` با فرانت‌متر YAML و دستورالعمل‌های markdown است.

برای نحوه بارگذاری و اولویت‌بندی مهارت‌ها، [Skills](</fa/tools/skills>) را ببینید.

## نخستین مهارت خود را بسازید

* ### Create the skill directory

Skills در فضای کاری شما قرار دارد. یک پوشه جدید بسازید:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Write SKILL.md

در آن دایرکتوری `SKILL.md` بسازید. فرانت‌متر، فراداده را تعریف می‌کند، و بدنه markdown شامل دستورالعمل‌هایی برای عامل است.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

برای `name` مهارت، از قالب خط‌تیره‌ای با حروف کوچک، رقم‌ها و خط‌تیره‌ها استفاده کنید. نام پوشه و `name` در فرانت‌متر را هماهنگ نگه دارید.

* ### Add tools (optional)

می‌توانید طرح‌واره‌های ابزار سفارشی را در فرانت‌متر تعریف کنید یا به عامل دستور دهید از ابزارهای سیستمی موجود (مانند `exec` یا `browser`) استفاده کند. Skills همچنین می‌تواند داخل plugins و همراه ابزارهایی که مستند می‌کند ارائه شود.

* ### Load the skill

یک نشست جدید شروع کنید تا OpenClaw مهارت را شناسایی کند:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

بررسی کنید که مهارت بارگذاری شده باشد:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Test it

پیامی بفرستید که باید مهارت را فعال کند:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

یا فقط با عامل گفت‌وگو کنید و درخواست یک احوال‌پرسی بدهید.

## مرجع فراداده مهارت

فرانت‌متر YAML از این فیلدها پشتیبانی می‌کند:

فیلد | الزامی | توضیح  
---|---|---  
`name` | بله | شناسه یکتا با استفاده از حروف کوچک، رقم‌ها و خط‌تیره‌ها  
`description` | بله | توضیح یک‌خطی که به عامل نشان داده می‌شود  
`metadata.openclaw.os` | خیر | فیلتر سیستم‌عامل (`["darwin"]`، `["linux"]` و غیره)  
`metadata.openclaw.requires.bins` | خیر | باینری‌های لازم در PATH  
`metadata.openclaw.requires.config` | خیر | کلیدهای پیکربندی لازم  
  
## بهترین روش‌ها

  * **مختصر باشید** — به مدل بگویید _چه کاری_ انجام دهد، نه اینکه چگونه یک هوش مصنوعی باشد
  * **اول ایمنی** — اگر مهارت شما از `exec` استفاده می‌کند، مطمئن شوید پرامپت‌ها اجازه تزریق فرمان دلخواه از ورودی نامعتبر را نمی‌دهند
  * **محلی آزمایش کنید** — پیش از اشتراک‌گذاری، با `openclaw agent --message "..."` آزمایش کنید
  * **از ClawHub استفاده کنید** — مهارت‌ها را در [ClawHub](<https://clawhub.ai>) مرور کنید و مشارکت داشته باشید


## محل قرارگیری مهارت‌ها

مکان | اولویت | دامنه  
---|---|---  
`\<workspace\>/skills/` | بالاترین | برای هر عامل  
`\<workspace\>/.agents/skills/` | بالا | عاملِ هر فضای کاری  
`~/.agents/skills/` | متوسط | پروفایل عامل مشترک  
`~/.openclaw/skills/` | متوسط | مشترک (همه عامل‌ها)  
همراه بسته (ارائه‌شده با OpenClaw) | پایین | سراسری  
`skills.load.extraDirs` | پایین‌ترین | پوشه‌های مشترک سفارشی  
  
## مرتبط

  * [مرجع Skills](</fa/tools/skills>) — قواعد بارگذاری، اولویت و دروازه‌گذاری
  * [پیکربندی Skills](</fa/tools/skills-config>) — طرح‌واره پیکربندی `skills.*`
  * [ClawHub](</fa/clawhub>) — رجیستری عمومی مهارت‌ها
  * [ساخت Plugins](</fa/plugins/building-plugins>) — plugins می‌توانند Skills ارائه کنند


Was this useful?YesNo