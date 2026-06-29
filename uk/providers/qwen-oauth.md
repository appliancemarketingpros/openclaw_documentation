---
title: Qwen OAuth / Портал
source_url: https://docs.openclaw.ai/uk/providers/qwen-oauth
scraped_at: 2026-06-29
---

ModelsProviders

`qwen-oauth` — це ідентифікатор провайдера Qwen Portal. Він спрямований на кінцеву точку Qwen Portal і зберігає старіші налаштування Qwen OAuth / portal доступними через окремий ідентифікатор провайдера.

Використовуйте цього провайдера, коли у вас саме є чинний токен Qwen Portal для `https://portal.qwen.ai/v1`, або коли ви мігруєте старіше налаштування Qwen Portal / Qwen CLI і хочете тримати ці облікові дані окремо від канонічного провайдера Qwen Cloud. Це не рекомендований перший вибір для нових користувачів Qwen.

Для нових налаштувань Qwen Cloud віддавайте перевагу [Qwen](</uk/providers/qwen>) зі стандартною кінцевою точкою ModelStudio, якщо у вас немає саме чинного токена Qwen Portal.

## Налаштування

Надайте свій токен порталу через початкове налаштування:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

Або встановіть:

bashCopy code
[code]
    export QWEN_API_KEY="<your-qwen-portal-token>" # pragma: allowlist secret
[/code]

## Типові значення

  * Провайдер: `qwen-oauth`
  * Псевдоніми: `qwen-portal`, `qwen-cli`
  * Базова URL-адреса: `https://portal.qwen.ai/v1`
  * Змінна середовища: `QWEN_API_KEY`
  * Стиль API: сумісний з OpenAI
  * Типова модель: `qwen-oauth/qwen3.5-plus`


## Чим це відрізняється від Qwen

OpenClaw має два ідентифікатори провайдерів для Qwen:

Провайдер | Сімейство кінцевих точок | Найкраще для  
---|---|---  
`qwen` | Кінцеві точки Qwen Cloud / Alibaba DashScope і Coding Plan | Нові налаштування API-ключа, Standard з оплатою за фактичне використання, Coding Plan, мультимодальні функції DashScope  
`qwen-oauth` | Кінцева точка Qwen Portal на `portal.qwen.ai/v1` | Наявні токени Qwen Portal і застарілі налаштування Qwen OAuth / CLI  
  
Обидва провайдери використовують сумісні з OpenAI форми запитів, але це окремі поверхні автентифікації. Токен, збережений для `qwen-oauth`, не слід трактувати як ключ DashScope або ModelStudio, а новий ключ DashScope має натомість використовувати канонічного провайдера `qwen`.

## Коли вибирати Qwen OAuth / Portal

  * У вас уже є робочий токен Qwen Portal.
  * Ви зберігаєте застарілий робочий процес Qwen OAuth або Qwen CLI під час переходу на модель провайдерів OpenClaw.
  * Вам потрібно перевірити сумісність саме з кінцевою точкою Qwen Portal.


Вибирайте [Qwen](</uk/providers/qwen>) для нового налаштування, ширшого вибору кінцевих точок, Standard ModelStudio, Coding Plan і повного каталогу Plugin Qwen.

## Моделі

Каталог Plugin Qwen додає типове значення Qwen Portal:

  * `qwen-oauth/qwen3.5-plus`


Доступність залежить від поточного облікового запису й токена Qwen Portal. Якщо ваш обліковий запис натомість використовує API-ключі ModelStudio / DashScope, налаштуйте канонічного провайдера `qwen`:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-keyopenclaw models set qwen/qwen3-coder-plus
[/code]

## Міграція

Застарілі OAuth-профілі Qwen Portal можуть не підтримувати оновлення. Якщо профіль порталу перестає працювати, повторно автентифікуйтеся з чинним токеном або перейдіть на стандартного провайдера Qwen:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Стандартний глобальний ModelStudio використовує:

textCopy code
[code]
    https://dashscope-intl.aliyuncs.com/compatible-mode/v1
[/code]

## Усунення несправностей

  * Збої оновлення Portal OAuth: застарілі OAuth-профілі Qwen Portal можуть не підтримувати оновлення. Повторно запустіть початкове налаштування з чинним токеном.
  * Помилки неправильної кінцевої точки: переконайтеся, що посилання на модель починається з `qwen-oauth/`, коли використовується токен порталу. Використовуйте посилання `qwen/` лише для канонічного провайдера Qwen.
  * Плутанина з `QWEN_API_KEY`: обидві сторінки Qwen згадують цю змінну середовища, але початкове налаштування зберігає облікові дані під вибраним ідентифікатором провайдера. Віддавайте перевагу початковому налаштуванню, коли ви тримаєте і `qwen`, і `qwen-oauth` доступними на одній машині.


## Пов’язане

  * [Qwen](</uk/providers/qwen>)
  * [Alibaba Model Studio](</uk/providers/alibaba>)
  * [Провайдери моделей](</uk/concepts/model-providers>)
  * [Усі провайдери](</uk/providers>)


Was this useful?YesNo

Open issue