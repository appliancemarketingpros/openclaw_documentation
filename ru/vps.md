---
title: Linux-сервер
source_url: https://docs.openclaw.ai/ru/vps
scraped_at: 2026-06-29
---

InstallHosting

Запускайте OpenClaw Gateway на любом Linux-сервере или облачном VPS. Эта страница помогает выбрать провайдера, объясняет, как работают облачные развертывания, и описывает общую настройку Linux, применимую везде.

## Выберите провайдера

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / бесплатный уровень)** также хорошо подходит. Видеоинструкция от сообщества доступна по адресу [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) (ресурс сообщества -- может стать недоступен). Как работают облачные установки

  * **Gateway работает на VPS** и владеет состоянием + рабочей областью.
  * Вы подключаетесь с ноутбука или телефона через **интерфейс управления** или **Tailscale/SSH**.
  * Считайте VPS источником истины и регулярно **создавайте резервные копии** состояния + рабочей области.
  * Безопасный вариант по умолчанию: держите Gateway на петлевом интерфейсе и получайте к нему доступ через SSH-туннель или Tailscale Serve. Если вы привязываетесь к `lan` или `tailnet`, требуйте `gateway.auth.token` или `gateway.auth.password`.

Связанные страницы: [удаленный доступ к Gateway](</ru/gateway/remote>), [центр платформ](</ru/platforms>). Сначала защитите административный доступ Перед установкой OpenClaw на публичный VPS решите, как вы хотите администрировать саму машину.

  * Если вам нужен административный доступ только через Tailnet, сначала установите Tailscale, подключите VPS к своему tailnet, проверьте второй SSH-сеанс через Tailscale IP или имя MagicDNS, затем ограничьте публичный SSH.
  * Если вы не используете Tailscale, примените эквивалентное усиление защиты для вашего SSH- пути перед публикацией дополнительных сервисов.
  * Это отдельно от доступа к Gateway. Вы по-прежнему можете оставить OpenClaw привязанным к петлевому интерфейсу и использовать SSH-туннель или Tailscale Serve для панели управления.

Параметры Gateway, относящиеся к Tailscale, находятся в разделе [Tailscale](</ru/gateway/tailscale>). Общий агент компании на VPS Запуск одного агента для команды является допустимой схемой, когда все пользователи находятся в одной границе доверия, а агент используется только для рабочих задач.

  * Держите его в выделенной среде выполнения (VPS/ВМ/контейнер + выделенный пользователь/учетные записи ОС).
  * Не входите в этой среде выполнения в личные учетные записи Apple/Google или личные профили браузера/менеджера паролей.
  * Если пользователи не доверяют друг другу, разделите их по Gateway/хосту/пользователю ОС.

Подробности модели безопасности: [безопасность](</ru/gateway/security>). Использование узлов с VPS Вы можете оставить Gateway в облаке и подключить **узлы** на своих локальных устройствах (Mac/iOS/Android/безголовых). Узлы предоставляют локальные возможности экрана/камеры/холста и `system.run`, пока Gateway остается в облаке. Документация: [узлы](</ru/nodes>), [CLI узлов](</ru/cli/nodes>). Настройка запуска для небольших ВМ и ARM-хостов Если CLI-команды выполняются медленно на маломощных ВМ (или ARM-хостах), включите кэш компиляции модулей Node: bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` ускоряет повторный запуск команд.
  * `OPENCLAW_NO_RESPAWN=1` удерживает обычные перезапуски Gateway внутри процесса, что избегает дополнительных передач между процессами и упрощает отслеживание PID на небольших хостах.
  * Первый запуск команды прогревает кэш; последующие запуски быстрее.
  * Особенности Raspberry Pi см. в разделе [Raspberry Pi](</ru/install/raspberry-pi>).

Контрольный список настройки systemd (необязательно) Для ВМ-хостов, использующих `systemd`, рассмотрите следующее:

  * Добавьте переменные окружения сервиса для стабильного пути запуска: 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * Сделайте поведение перезапуска явным: 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * Предпочитайте диски на базе SSD для путей состояния/кэша, чтобы снизить штрафы холодного старта из-за случайного ввода-вывода.

Для стандартного пути `openclaw onboard --install-daemon` отредактируйте пользовательский unit: bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Если вместо этого вы намеренно установили системный unit, отредактируйте `openclaw-gateway.service` через `sudo systemctl edit openclaw-gateway.service`. Как политики `Restart=` помогают автоматическому восстановлению: [systemd может автоматизировать восстановление сервиса](<https://www.redhat.com/en/blog/systemd-automate-recovery>). О поведении Linux при OOM, выборе дочернего процесса-жертвы и диагностике `exit 137` см. [давление на память Linux и завершения OOM](</ru/platforms/linux#memory-pressure-and-oom-kills>). Связанные материалы

  * [Обзор установки](</ru/install>)
  * [DigitalOcean](</ru/install/digitalocean>)
  * [Fly.io](</ru/install/fly>)
  * [Hetzner](</ru/install/hetzner>)

](</ru/install/raspberry-pi>) Was this useful?YesNoOpen issue ](</ru/install/exe-dev>)](</ru/install/azure>)](</ru/install/gcp>)](</ru/install/hostinger>)](</ru/install/hetzner>)](</ru/install/fly>)](</ru/install/oracle>)](</ru/install/digitalocean>)](</ru/install/northflank>)](</ru/install/railway>)