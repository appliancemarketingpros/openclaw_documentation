---
title: Nix
source_url: https://docs.openclaw.ai/uk/install/nix
scraped_at: 2026-05-25
---

Встановіть OpenClaw декларативно за допомогою **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** \- офіційного, повністю укомплектованого модуля Home Manager.

## Що ви отримуєте

  * Gateway + застосунок macOS + інструменти (whisper, spotify, cameras) -- усе зафіксовано
  * Сервіс launchd, який зберігається після перезавантажень
  * Система Plugin із декларативною конфігурацією
  * Миттєве відкочування: `home-manager switch --rollback`


## Швидкий старт

* ### Встановіть Determinate Nix

Якщо Nix ще не встановлено, дотримуйтеся інструкцій [інсталятора Determinate Nix](<https://github.com/DeterminateSystems/nix-installer>).

* ### Створіть локальний flake

Використайте шаблон agent-first із репозиторію nix-openclaw:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### Налаштуйте секрети

Налаштуйте токен бота для обміну повідомленнями та API-ключ постачальника моделі. Звичайні файли в `~/.secrets/` цілком підходять.

* ### Заповніть заповнювачі шаблону й перемкніться

bashCopy code
[code]
    home-manager switch
[/code]

* ### Перевірте

Переконайтеся, що сервіс launchd працює, а ваш бот відповідає на повідомлення.

Повні параметри модуля та приклади див. у [README nix-openclaw](<https://github.com/openclaw/nix-openclaw>).

## Поведінка середовища виконання в режимі Nix

Коли встановлено `OPENCLAW_NIX_MODE=1` (автоматично з nix-openclaw), OpenClaw переходить у детермінований режим для встановлень, керованих Nix. Інші пакети Nix можуть встановлювати той самий режим; nix-openclaw є офіційною референсною реалізацією.

Ви також можете встановити його вручну:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

У macOS GUI-застосунок не успадковує автоматично змінні середовища оболонки. Натомість увімкніть режим Nix через defaults:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Що змінюється в режимі Nix

  * Потоки автоматичного встановлення та самомодифікації вимкнено
  * `openclaw.json` вважається незмінним. Типові значення, отримані під час запуску, залишаються лише в середовищі виконання, а засоби запису конфігурації, як-от setup, onboarding, мутаційний `openclaw update`, встановлення/оновлення/видалення/увімкнення Plugin, `doctor --fix`, `doctor --generate-gateway-token` і `openclaw config set`, відмовляються редагувати файл.
  * Натомість агенти мають редагувати джерело Nix. Для nix-openclaw скористайтеся agent-first [Швидким стартом](<https://github.com/openclaw/nix-openclaw#quick-start>) і задайте конфігурацію в `programs.openclaw.config` або `instances.<name>.config`.
  * Відсутні залежності показують повідомлення з інструкціями для Nix
  * UI показує банер режиму Nix лише для читання


### Шляхи конфігурації та стану

OpenClaw читає конфігурацію JSON5 з `OPENCLAW_CONFIG_PATH` і зберігає змінювані дані в `OPENCLAW_STATE_DIR`. Під час роботи під Nix задавайте їх явно як розташування, керовані Nix, щоб стан середовища виконання та конфігурація залишалися поза незмінним сховищем.

Змінна | Типове значення  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### Виявлення PATH сервісу

Сервіс Gateway launchd/systemd автоматично виявляє бінарні файли Nix-профілю, щоб plugins та інструменти, які запускають виконувані файли, встановлені через `nix`, працювали без ручного налаштування PATH:

  * Коли `NIX_PROFILES` встановлено, кожен запис додається до PATH сервісу з пріоритетом справа наліво (відповідає пріоритету оболонки Nix - перемагає найправіший).
  * Коли `NIX_PROFILES` не встановлено, `~/.nix-profile/bin` додається як резервний варіант.


Це застосовується до середовищ сервісів macOS launchd і Linux systemd.

## Пов’язане

[**nix-openclaw** Джерело істини для модуля Home Manager і повний посібник із налаштування. ](<https://github.com/openclaw/nix-openclaw>) [**Майстер налаштування** Покрокове налаштування CLI без Nix. ](</uk/start/wizard>) [**Docker** Контейнеризоване налаштування як альтернатива без Nix. ](</uk/install/docker>) [**Оновлення** Оновлення встановлень, керованих Home Manager, разом із пакетом. ](</uk/install/updating>)

Was this useful?YesNo