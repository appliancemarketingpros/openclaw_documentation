---
title: Керування Plugin
source_url: https://docs.openclaw.ai/uk/plugins/manage-plugins
scraped_at: 2026-05-25
---

Найпоширеніші робочі процеси Plugin складаються з кількох команд: пошук, установлення, перезапуск Gateway, перевірка та видалення, коли Plugin більше не потрібен.

## Список Plugins

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Використовуйте `--json` для скриптів. Він містить діагностику реєстру та статичний `dependencyStatus` кожного Plugin, коли пакет Plugin оголошує `dependencies` або `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` — це холодна перевірка інвентарю. Вона показує, що OpenClaw може виявити з конфігурації, маніфестів і реєстру Plugin; вона не доводить, що вже запущений процес Gateway імпортував runtime Plugin.

## Установлення Plugins

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Після встановлення коду Plugin перезапустіть Gateway, який обслуговує ваші канали:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Використовуйте `inspect --runtime`, коли вам потрібен доказ, що Plugin зареєстрував runtime-поверхні, як-от інструменти, hooks, сервіси, методи Gateway або команди CLI, що належать Plugin.

## Оновлення Plugins

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Якщо Plugin було встановлено з npm dist-tag, такого як `@beta`, подальші виклики `update <plugin-id>` повторно використовують цей записаний тег. Передавання явної npm-специфікації перемикає відстежуване встановлення на цю специфікацію для майбутніх оновлень.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

Друга команда повертає Plugin до стандартної лінії випусків реєстру, якщо раніше він був закріплений за точною версією або тегом.

Коли `openclaw update` виконується на beta-каналі, записи Plugin npm і ClawHub зі стандартної лінії спочатку пробують відповідний випуск Plugin `@beta`. Якщо такого beta-випуску не існує, OpenClaw повертається до записаної специфікації default/latest. Для npm Plugins OpenClaw також повертається назад, коли beta-пакет існує, але не проходить перевірку встановлення. Точні версії та явні теги, як-от `@rc` або `@beta`, зберігаються.

## Видалення Plugins

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

Видалення прибирає конфігураційний запис Plugin, запис індексу Plugin, записи списків дозволу/заборони та пов’язані шляхи завантаження, коли це застосовно. Керовані каталоги встановлення видаляються, якщо не передано `--keep-files`.

У режимі Nix (`OPENCLAW_NIX_MODE=1`) команди встановлення, оновлення, видалення, увімкнення та вимкнення Plugin вимкнені. Натомість керуйте цими виборами у джерелі Nix для встановлення; для nix-openclaw використовуйте agent-first [Швидкий старт](<https://github.com/openclaw/nix-openclaw#quick-start>).

## Публікація Plugins

Ви можете публікувати зовнішні Plugins у [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) або в обох місцях.

### Публікація в ClawHub

ClawHub є основною публічною поверхнею виявлення для OpenClaw Plugins. Він надає користувачам метадані з пошуком, історію версій і результати сканування реєстру перед встановленням.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Користувачі встановлюють із ClawHub так:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

Коротка форма все одно спочатку перевіряє ClawHub.

### Публікація в [npmjs.com](<http://npmjs.com>)

Нативні npm Plugins повинні містити маніфест Plugin і метадані entrypoint OpenClaw у `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Користувачі встановлюють лише з npm так:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Якщо той самий пакет також доступний у ClawHub, `npm:` пропускає пошук у ClawHub і примусово використовує розв’язання через npm.

## Вибір джерела

  * **ClawHub** : використовуйте, коли вам потрібні нативне для OpenClaw виявлення, підсумки сканування, версії та підказки щодо встановлення.
  * **[npmjs.com](<http://npmjs.com>)** : використовуйте, коли ви вже постачаєте JavaScript-пакети або потребуєте npm dist-tags/робочих процесів приватного реєстру.
  * **Git** : використовуйте, коли потрібно встановити безпосередньо з гілки, тегу або коміту.
  * **Локальний шлях** : використовуйте, коли розробляєте або тестуєте Plugin на тій самій машині.


## Пов’язане

  * [Plugins](</uk/tools/plugin>) \- огляд і усунення несправностей
  * [`openclaw plugins`](</uk/cli/plugins>) \- повна довідка CLI
  * [ClawHub](</uk/clawhub/cli>) \- публікація та операції реєстру
  * [Створення Plugins](</uk/plugins/building-plugins>) \- створення пакета Plugin
  * [Маніфест Plugin](</uk/plugins/manifest>) \- маніфест і метадані пакета


Was this useful?YesNo