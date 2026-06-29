---
title: OpenCode
source_url: https://docs.openclaw.ai/ru/providers/opencode
scraped_at: 2026-06-29
---

ModelsProviders

OpenCode предоставляет два размещенных каталога в OpenClaw:

Каталог | Префикс | Провайдер среды выполнения  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Оба каталога используют один и тот же API-ключ OpenCode. OpenClaw оставляет идентификаторы провайдеров среды выполнения разделенными, чтобы вышестоящая маршрутизация по моделям оставалась корректной, но первичная настройка и документация рассматривают их как единую настройку OpenCode.

## Начало работы

### Каталог Zen

**Лучше всего для:** курируемого мультимодельного прокси OpenCode (Claude, GPT, Gemini, GLM).

* ### Запустите первичную настройку

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Или передайте ключ напрямую:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Задайте модель Zen по умолчанию

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Проверьте, что модели доступны

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Каталог Go

**Лучше всего для:** размещенной в OpenCode линейки Kimi, GLM и MiniMax.

* ### Запустите первичную настройку

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Или передайте ключ напрямую:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Задайте модель Go по умолчанию

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Проверьте, что модели доступны

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Пример конфигурации

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Встроенные каталоги

### Zen

Свойство | Значение  
---|---  
Провайдер среды выполнения | `opencode`  
Примеры моделей | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3.1-pro`, `opencode/glm-5.2`  
  
### Go

Свойство | Значение  
---|---  
Провайдер среды выполнения | `opencode-go`  
Примеры моделей | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Расширенная конфигурация

Псевдонимы API-ключа

`OPENCODE_ZEN_API_KEY` также поддерживается как псевдоним для `OPENCODE_API_KEY`.

Общие учетные данные

Ввод одного ключа OpenCode во время настройки сохраняет учетные данные для обоих провайдеров среды выполнения. Вам не нужно отдельно выполнять первичную настройку каждого каталога.

Биллинг и панель управления

Вы входите в OpenCode, добавляете платежные данные и копируете свой API-ключ. Биллинг и доступность каталога управляются из панели управления OpenCode.

Поведение воспроизведения Gemini

Ссылки OpenCode на базе Gemini остаются на пути proxy-Gemini, поэтому OpenClaw сохраняет там очистку сигнатур размышлений Gemini, не включая нативную проверку воспроизведения Gemini или перезаписи начальной загрузки.

Поведение воспроизведения не-Gemini

Ссылки OpenCode не-Gemini сохраняют минимальную OpenAI-совместимую политику воспроизведения.

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Справочник конфигурации** Полный справочник конфигурации для агентов, моделей и провайдеров. ](</ru/gateway/configuration-reference>)

Was this useful?YesNo

Open issue