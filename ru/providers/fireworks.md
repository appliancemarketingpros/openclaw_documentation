---
title: Fireworks
source_url: https://docs.openclaw.ai/ru/providers/fireworks
scraped_at: 2026-06-29
---

ModelsProviders

[Fireworks](<https://fireworks.ai>) предоставляет open-weight и маршрутизируемые модели через API, совместимый с OpenAI. Установите официальный Plugin провайдера Fireworks, чтобы использовать две заранее каталогизированные модели Kimi и любой идентификатор модели или маршрутизатора Fireworks во время выполнения.

Свойство | Значение  
---|---  
Идентификатор провайдера | `fireworks` (псевдоним: `fireworks-ai`)  
Пакет | `@openclaw/fireworks-provider`  
Переменная окружения авторизации | `FIREWORKS_API_KEY`  
Флаг онбординга | `--auth-choice fireworks-api-key`  
Прямой флаг CLI | `--fireworks-api-key <key>`  
API | совместимый с OpenAI (`openai-completions`)  
Базовый URL | `https://api.fireworks.ai/inference/v1`  
Модель по умолчанию | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Псевдоним по умолчанию | `Kimi K2.5 Turbo`  
  
## Начало работы

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/fireworks-provider
[/code]

* ### Set the Fireworks API key

ОнбордингCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Прямой флагCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Только envCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Онбординг сохраняет ключ для провайдера `fireworks` в ваших профилях авторизации и устанавливает маршрутизатор **Fire Pass** Kimi K2.5 Turbo как модель по умолчанию.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

Список должен включать `Kimi K2.6` и `Kimi K2.5 Turbo (Fire Pass)`. Если `FIREWORKS_API_KEY` не разрешен, `openclaw models status --json` сообщает об отсутствующих учетных данных в `auth.unusableProfiles`.

## Неинтерактивная настройка

Для скриптовых установок или установок в CI передайте все параметры в командной строке:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Встроенный каталог

Ссылка на модель | Название | Ввод | Контекст | Макс. вывод | Размышление  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | текст + изображение | 262,144 | 262,144 | Принудительно выключено  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | текст + изображение | 256,000 | 256,000 | Принудительно выключено (по умолчанию)  
  
## Пользовательские идентификаторы моделей Fireworks

OpenClaw принимает любой идентификатор модели или маршрутизатора Fireworks во время выполнения. Используйте точный идентификатор, показанный Fireworks, и добавьте к нему префикс `fireworks/`. Динамическое разрешение клонирует шаблон Fire Pass (ввод текста + изображения, API, совместимый с OpenAI, стоимость по умолчанию ноль) и автоматически отключает thinking, когда идентификатор совпадает с шаблоном Kimi. Динамические идентификаторы GLM помечаются как поддерживающие только текст, если вы не настроите пользовательскую запись модели с вводом изображений.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

How model id prefixing works

Каждая ссылка на модель Fireworks в OpenClaw начинается с `fireworks/`, за которым следует точный идентификатор или путь маршрутизатора с платформы Fireworks. Например:

  * Модель маршрутизатора: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Прямая модель: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw удаляет префикс `fireworks/` при создании API-запроса и отправляет оставшийся путь в конечную точку Fireworks как совместимое с OpenAI поле `model`.

Why thinking is forced off for Kimi

Fireworks K2.6 возвращает 400, если запрос содержит параметры `reasoning_*`, хотя Kimi поддерживает thinking через собственный API Moonshot. Политика провайдера (`extensions/fireworks/thinking-policy.ts`) объявляет для идентификаторов моделей Kimi только уровень thinking `off`, поэтому ручные переключения `/think` и поверхности политик провайдера остаются согласованными с контрактом среды выполнения.

Чтобы использовать рассуждения Kimi от начала до конца, настройте [провайдера Moonshot](</ru/providers/moonshot>) и маршрутизируйте ту же модель через него.

Environment availability for the daemon

Если Gateway запускается как управляемая служба (launchd, systemd, Docker), ключ Fireworks должен быть виден этому процессу, а не только вашей интерактивной оболочке.

В macOS `openclaw gateway install` уже подключает `~/.openclaw/.env` к файлу окружения LaunchAgent. После ротации ключа повторно выполните установку (или `openclaw doctor --fix`).

## См. также

[**Model providers** Выбор провайдеров, ссылок на модели и поведения failover. ](</ru/concepts/model-providers>) [**Thinking modes** Уровни `/think`, политики провайдеров и маршрутизация моделей, поддерживающих рассуждения. ](</ru/tools/thinking>) [**Moonshot** Запускайте Kimi с нативным выводом thinking через собственный API Moonshot. ](</ru/providers/moonshot>) [**Troubleshooting** Общая диагностика и часто задаваемые вопросы. ](</ru/help/troubleshooting>)

Was this useful?YesNo

Open issue