---
title: Skills
source_url: https://docs.openclaw.ai/uk/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

Переглядайте локальні Skills та встановлюйте/оновлюйте Skills із ClawHub.

Пов’язане:

  * Система Skills: [Skills](</uk/tools/skills>)
  * Конфігурація Skills: [Skills config](</uk/tools/skills-config>)
  * Встановлення з ClawHub: [ClawHub](</uk/clawhub/cli>)


## Команди

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` використовують ClawHub напряму та встановлюють у каталог `skills/` активного робочого простору. `list`/`info`/`check` і далі перевіряють локальні Skills, видимі для поточного робочого простору та конфігурації. Команди, що працюють із робочим простором, визначають цільовий робочий простір із `--agent <id>`, потім із поточного робочого каталогу, якщо він розташований у налаштованому робочому просторі агента, а потім з агента за замовчуванням.

Ця команда CLI `install` завантажує папки Skills із ClawHub. Встановлення залежностей Skills через Gateway, які запускаються під час онбордингу або з налаштувань Skills, натомість використовують окремий шлях запиту `skills.install`.

Примітки:

  * `search [query...]` приймає необов’язковий запит; пропустіть його, щоб переглядати стандартну стрічку пошуку ClawHub.
  * `search --limit <n>` обмежує кількість повернених результатів.
  * `install --force` перезаписує наявну папку Skills робочого простору для того самого slug.
  * `--agent <id>` націлюється на один налаштований робочий простір агента й перевизначає визначення за поточним робочим каталогом.
  * `update --all` оновлює лише відстежувані встановлення ClawHub в активному робочому просторі.
  * `check --agent <id>` перевіряє робочий простір вибраного агента й повідомляє, які готові Skills фактично видимі для промпта або командної поверхні цього агента.
  * `list` є дією за замовчуванням, коли підкоманду не вказано.
  * `list`, `info` і `check` записують свій відрендерений вивід у stdout. З `--json` це означає, що машиночитний payload залишається в stdout для каналів і скриптів.


## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Skills](</uk/tools/skills>)


Was this useful?YesNo