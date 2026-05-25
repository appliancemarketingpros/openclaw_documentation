---
title: Створення Skills
source_url: https://docs.openclaw.ai/uk/tools/creating-skills
scraped_at: 2026-05-25
---

Skills навчають агента, як і коли використовувати інструменти. Кожна навичка — це каталог, що містить файл `SKILL.md` із YAML frontmatter та інструкціями markdown.

Про те, як навички завантажуються та пріоритезуються, див. [Skills](</uk/tools/skills>).

## Створіть свою першу навичку

* ### Створіть каталог навички

Навички розміщуються у вашому робочому просторі. Створіть нову папку:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Напишіть SKILL.md

Створіть `SKILL.md` у цьому каталозі. Frontmatter визначає метадані, а тіло markdown містить інструкції для агента.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Використовуйте hyphen-case з малими літерами, цифрами та дефісами для `name` навички. Узгоджуйте назву папки та `name` у frontmatter.

* ### Додайте інструменти (необов’язково)

Ви можете визначити власні схеми інструментів у frontmatter або доручити агенту використовувати наявні системні інструменти (наприклад, `exec` або `browser`). Навички також можуть постачатися всередині plugins разом з інструментами, які вони документують.

* ### Завантажте навичку

Запустіть новий сеанс, щоб OpenClaw підхопив навичку:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Перевірте, що навичку завантажено:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Протестуйте її

Надішліть повідомлення, яке має активувати навичку:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Або просто поспілкуйтеся з агентом і попросіть привітання.

## Довідник метаданих навички

YAML frontmatter підтримує такі поля:

Поле | Обов’язково | Опис  
---|---|---  
`name` | Так | Унікальний ідентифікатор із малих літер, цифр і дефісів  
`description` | Так | Однорядковий опис, показаний агенту  
`metadata.openclaw.os` | Ні | Фільтр ОС (`["darwin"]`, `["linux"]` тощо)  
`metadata.openclaw.requires.bins` | Ні | Обов’язкові бінарні файли в PATH  
`metadata.openclaw.requires.config` | Ні | Обов’язкові ключі конфігурації  
  
## Найкращі практики

  * **Будьте лаконічні** — інструктуйте модель, _що_ робити, а не як бути ШІ
  * **Безпека передусім** — якщо ваша навичка використовує `exec`, переконайтеся, що підказки не дозволяють довільне впровадження команд із недовіреного вводу
  * **Тестуйте локально** — використовуйте `openclaw agent --message "..."` для тестування перед поширенням
  * **Використовуйте ClawHub** — переглядайте навички та долучайтеся до них на [ClawHub](<https://clawhub.ai>)


## Де розміщуються навички

Розташування | Пріоритет | Область застосування  
---|---|---  
`\<workspace\>/skills/` | Найвищий | Для окремого агента  
`\<workspace\>/.agents/skills/` | Високий | Для агента робочого простору  
`~/.agents/skills/` | Середній | Спільний профіль агента  
`~/.openclaw/skills/` | Середній | Спільно (усі агенти)  
Вбудовані (постачаються з OpenClaw) | Низький | Глобальна  
`skills.load.extraDirs` | Найнижчий | Власні спільні папки  
  
## Пов’язане

  * [Довідник Skills](</uk/tools/skills>) — правила завантаження, пріоритету та gating
  * [Конфігурація Skills](</uk/tools/skills-config>) — схема конфігурації `skills.*`
  * [ClawHub](</uk/clawhub>) — публічний реєстр навичок
  * [Створення Plugins](</uk/plugins/building-plugins>) — plugins можуть постачати навички


Was this useful?YesNo