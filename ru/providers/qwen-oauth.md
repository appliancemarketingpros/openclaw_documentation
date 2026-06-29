---
title: Qwen OAuth / Портал
source_url: https://docs.openclaw.ai/ru/providers/qwen-oauth
scraped_at: 2026-06-29
---

ModelsProviders

`qwen-oauth` — это идентификатор провайдера Qwen Portal. Он предназначен для конечной точки Qwen Portal и сохраняет адресуемость старых настроек Qwen OAuth / portal через отдельный идентификатор провайдера.

Используйте этого провайдера, когда у вас есть актуальный токен Qwen Portal для `https://portal.qwen.ai/v1`, или когда вы переносите старую настройку Qwen Portal / Qwen CLI и хотите держать эти учетные данные отдельно от канонического провайдера Qwen Cloud. Это не рекомендуемый первый выбор для новых пользователей Qwen.

Для новых настроек Qwen Cloud предпочитайте [Qwen](</ru/providers/qwen>) со стандартной конечной точкой ModelStudio, если только у вас нет актуального токена Qwen Portal.

## Настройка

Передайте токен portal через onboarding:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

Или задайте:

bashCopy code
[code]
    export QWEN_API_KEY="<your-qwen-portal-token>" # pragma: allowlist secret
[/code]

## Значения по умолчанию

  * Провайдер: `qwen-oauth`
  * Псевдонимы: `qwen-portal`, `qwen-cli`
  * Базовый URL: `https://portal.qwen.ai/v1`
  * Переменная окружения: `QWEN_API_KEY`
  * Стиль API: совместимый с OpenAI
  * Модель по умолчанию: `qwen-oauth/qwen3.5-plus`


## Чем это отличается от Qwen

В OpenClaw есть два идентификатора провайдера для Qwen:

Провайдер | Семейство конечных точек | Лучше всего подходит для  
---|---|---  
`qwen` | Конечные точки Qwen Cloud / Alibaba DashScope и Coding Plan | Новых настроек с API-ключом, Standard pay-as-you-go, Coding Plan, мультимодальных возможностей DashScope  
`qwen-oauth` | Конечная точка Qwen Portal на `portal.qwen.ai/v1` | Существующих токенов Qwen Portal и устаревших настроек Qwen OAuth / CLI  
  
Оба провайдера используют формы запросов, совместимые с OpenAI, но это отдельные поверхности аутентификации. Токен, сохраненный для `qwen-oauth`, не следует считать ключом DashScope или ModelStudio, а новый ключ DashScope должен вместо этого использовать канонического провайдера `qwen`.

## Когда выбирать Qwen OAuth / Portal

  * У вас уже есть рабочий токен Qwen Portal.
  * Вы сохраняете устаревший рабочий процесс Qwen OAuth или Qwen CLI при переходе на модель провайдеров OpenClaw.
  * Вам нужно проверить совместимость именно с конечной точкой Qwen Portal.


Выбирайте [Qwen](</ru/providers/qwen>) для новой настройки, более широкого выбора конечных точек, Standard ModelStudio, Coding Plan и полного каталога Plugin Qwen.

## Модели

Каталог Plugin Qwen задает значение Qwen Portal по умолчанию:

  * `qwen-oauth/qwen3.5-plus`


Доступность зависит от текущей учетной записи Qwen Portal и токена. Если ваша учетная запись вместо этого использует API-ключи ModelStudio / DashScope, настройте канонического провайдера `qwen`:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-keyopenclaw models set qwen/qwen3-coder-plus
[/code]

## Миграция

Устаревшие OAuth-профили Qwen Portal могут не поддерживать обновление. Если профиль portal перестал работать, выполните повторную аутентификацию с актуальным токеном или переключитесь на стандартного провайдера Qwen:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Глобальный Standard ModelStudio использует:

textCopy code
[code]
    https://dashscope-intl.aliyuncs.com/compatible-mode/v1
[/code]

## Устранение неполадок

  * Сбои обновления Portal OAuth: устаревшие OAuth-профили Qwen Portal могут не поддерживать обновление. Повторно запустите onboarding с актуальным токеном.
  * Ошибки неправильной конечной точки: убедитесь, что ссылка на модель начинается с `qwen-oauth/` при использовании токена portal. Используйте ссылки `qwen/` только для канонического провайдера Qwen.
  * Путаница с `QWEN_API_KEY`: обе страницы Qwen упоминают эту переменную окружения, но onboarding сохраняет учетные данные под выбранным идентификатором провайдера. Предпочитайте onboarding, когда держите и `qwen`, и `qwen-oauth` доступными на одной машине.


## Связанные материалы

  * [Qwen](</ru/providers/qwen>)
  * [Alibaba Model Studio](</ru/providers/alibaba>)
  * [Провайдеры моделей](</ru/concepts/model-providers>)
  * [Все провайдеры](</ru/providers>)


Was this useful?YesNo

Open issue