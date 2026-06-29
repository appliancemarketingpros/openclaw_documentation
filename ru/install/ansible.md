---
title: Ansible
source_url: https://docs.openclaw.ai/ru/install/ansible
scraped_at: 2026-06-29
---

InstallContainers

Разверните OpenClaw на производственных серверах с **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- автоматическим установщиком с архитектурой, ориентированной на безопасность.

## Предварительные требования

Требование | Подробности  
---|---  
**ОС** | Debian 11+ или Ubuntu 20.04+  
**Доступ** | Права root или sudo  
**Сеть** | Подключение к Интернету для установки пакетов  
**Ansible** | 2.14+ (устанавливается автоматически скриптом быстрого старта)  
  
## Что вы получаете

  * **Безопасность с приоритетом межсетевого экрана** \-- изоляция UFW + Docker (доступны только SSH + Tailscale)
  * **Tailscale VPN** \-- безопасный удаленный доступ без публичного раскрытия сервисов
  * **Docker** \-- изолированные контейнеры-песочницы, привязки только к localhost
  * **Глубоко эшелонированная защита** \-- 4-уровневая архитектура безопасности
  * **Интеграция с systemd** \-- автозапуск при загрузке с усилением безопасности
  * **Настройка одной командой** \-- полное развертывание за минуты


## Быстрый старт

Установка одной командой:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Что устанавливается

Playbook Ansible устанавливает и настраивает:

  1. **Tailscale** \-- mesh VPN для безопасного удаленного доступа
  2. **Межсетевой экран UFW** \-- только порты SSH + Tailscale
  3. **Docker CE + Compose V2** \-- для стандартного backend песочницы агента
  4. **Node.js 24 + pnpm** \-- зависимости среды выполнения (Node 22 LTS, сейчас `22.19+`, остается поддерживаемым)
  5. **OpenClaw** \-- размещается на хосте, не контейнеризируется
  6. **Сервис systemd** \-- автозапуск с усилением безопасности


## Настройка после установки

* ### Переключитесь на пользователя openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Запустите мастер первичной настройки

Скрипт после установки проведет вас через настройку параметров OpenClaw.

* ### Подключите провайдеры сообщений

Войдите в WhatsApp, Telegram, Discord или Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Проверьте установку

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Подключитесь к Tailscale

Присоединитесь к вашей VPN mesh для безопасного удаленного доступа.

### Быстрые команды

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Архитектура безопасности

Развертывание использует 4-уровневую модель защиты:

  1. **Межсетевой экран (UFW)** \-- публично открыты только SSH (22) + Tailscale (41641/udp)
  2. **VPN (Tailscale)** \-- Gateway доступен только через VPN mesh
  3. **Изоляция Docker** \-- цепочка iptables DOCKER-USER предотвращает внешнее раскрытие портов
  4. **Усиление systemd** \-- NoNewPrivileges, PrivateTmp, непривилегированный пользователь


Чтобы проверить вашу внешнюю поверхность атаки:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Открыт должен быть только порт 22 (SSH). Все остальные сервисы (Gateway, Docker) заблокированы.

Docker устанавливается для песочниц агентов (изолированного выполнения инструментов), а не для запуска самого Gateway. Настройку песочницы см. в [Многоагентная песочница и инструменты](</ru/tools/multi-agent-sandbox-tools>).

## Ручная установка

Если вы предпочитаете ручной контроль вместо автоматизации:

* ### Установите предварительные зависимости

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Клонируйте репозиторий

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Установите коллекции Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Запустите playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Либо запустите напрямую, а затем вручную выполните скрипт настройки:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Обновление

Установщик Ansible настраивает OpenClaw для ручных обновлений. Стандартный процесс обновления см. в [Обновление](</ru/install/updating>).

Чтобы повторно запустить playbook Ansible (например, для изменений конфигурации):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Это идемпотентно и безопасно для многократного запуска.

## Устранение неполадок

Межсетевой экран блокирует мое подключение

  * Сначала убедитесь, что у вас есть доступ через Tailscale VPN
  * Доступ по SSH (порт 22) всегда разрешен
  * Gateway по проекту доступен только через Tailscale

Сервис не запускается bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Проблемы с песочницей Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Вход в провайдер не удается

Убедитесь, что вы запускаете команды от пользователя `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Расширенная конфигурация

Подробную архитектуру безопасности и устранение неполадок см. в репозитории openclaw-ansible:

  * [Архитектура безопасности](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Технические подробности](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Руководство по устранению неполадок](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Связанные материалы

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- полное руководство по развертыванию
  * [Docker](</ru/install/docker>) \-- настройка контейнеризированного Gateway
  * [Изоляция в песочнице](</ru/gateway/sandboxing>) \-- конфигурация песочницы агента
  * [Многоагентная песочница и инструменты](</ru/tools/multi-agent-sandbox-tools>) \-- изоляция для каждого агента


Was this useful?YesNo

Open issue