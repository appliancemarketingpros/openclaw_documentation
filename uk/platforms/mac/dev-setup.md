---
title: Налаштування середовища розробки macOS
source_url: https://docs.openclaw.ai/uk/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# Налаштування розробника macOS

Зберіть і запустіть застосунок OpenClaw для macOS із вихідного коду.

## Передумови

Перед збиранням застосунку переконайтеся, що у вас установлено:

  1. **Xcode 26.2+** : потрібен для розробки на Swift.
  2. **Node.js 24 і pnpm** : рекомендовано для Gateway, CLI та скриптів пакування. Node 22 LTS, наразі `22.16+`, залишається підтримуваним для сумісності.


## 1\. Встановіть залежності

Встановіть залежності для всього проєкту:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. Зберіть і запакуйте застосунок

Щоб зібрати застосунок macOS і запакувати його в `dist/OpenClaw.app`, виконайте:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Якщо у вас немає сертифіката Apple Developer ID, скрипт автоматично використає **ad-hoc signing** (`-`).

Про режими запуску для розробки, прапорці підписування та усунення проблем із Team ID див. README застосунку macOS: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Примітка** : застосунки з ad-hoc підписом можуть викликати запити безпеки. Якщо застосунок одразу аварійно завершується з "Abort trap 6", див. розділ Усунення несправностей.

## 3\. Встановіть CLI

Застосунок macOS очікує глобальне встановлення CLI `openclaw` для керування фоновими завданнями.

**Щоб встановити його (рекомендовано):**

  1. Відкрийте застосунок OpenClaw.
  2. Перейдіть на вкладку налаштувань **General**.
  3. Натисніть **"Install CLI"**.


Або встановіть його вручну:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` і `bun add -g openclaw@<version>` також працюють. Для середовища виконання Gateway рекомендованим шляхом залишається Node.

## Усунення несправностей

### Збирання не вдається: невідповідність toolchain або SDK

Збирання застосунку macOS очікує найновіший macOS SDK і toolchain Swift 6.2.

**Системні залежності (обов’язково):**

  * **Найновіша версія macOS, доступна в Software Update** (потрібна для SDK Xcode 26.2)
  * **Xcode 26.2** (toolchain Swift 6.2)


**Перевірки:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

Якщо версії не збігаються, оновіть macOS/Xcode і повторно запустіть збирання.

### Застосунок аварійно завершується під час надання дозволу

Якщо застосунок аварійно завершується, коли ви намагаєтеся дозволити доступ до **Speech Recognition** або **Microphone** , це може бути спричинено пошкодженим кешем TCC або невідповідністю підпису.

**Виправлення:**

  1. Скиньте дозволи TCC:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. Якщо це не допомогло, тимчасово змініть `BUNDLE_ID` у [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>), щоб змусити macOS почати з "чистого аркуша".


### Gateway нескінченно показує "Starting..."

Якщо статус Gateway залишається "Starting...", перевірте, чи не утримує порт zombie-процес:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

Якщо порт утримує ручний запуск, зупиніть цей процес (Ctrl+C). У крайньому разі завершіть PID, який ви знайшли вище.

## Пов’язане

  * [Застосунок macOS](</uk/platforms/macos>)
  * [Огляд встановлення](</uk/install>)


Was this useful?YesNo