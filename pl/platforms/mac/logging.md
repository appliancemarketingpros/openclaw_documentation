---
title: Rejestrowanie w macOS
source_url: https://docs.openclaw.ai/pl/platforms/mac/logging
scraped_at: 2026-05-25
---

# Rejestrowanie (macOS)

## Rotujący plik dziennika diagnostycznego (panel debugowania)

OpenClaw kieruje logi aplikacji macOS przez swift-log (domyślnie ujednolicone rejestrowanie) i może zapisywać lokalny, rotujący plik dziennika na dysku, gdy potrzebujesz trwałego zapisu.

  * Szczegółowość: **Panel debugowania → Logi → Rejestrowanie aplikacji → Szczegółowość**
  * Włącz: **Panel debugowania → Logi → Rejestrowanie aplikacji → „Zapisuj rotujący dziennik diagnostyczny (JSONL)”**
  * Lokalizacja: `~/Library/Logs/OpenClaw/diagnostics.jsonl` (rotuje automatycznie; stare pliki otrzymują sufiksy `.1`, `.2`, …)
  * Wyczyść: **Panel debugowania → Logi → Rejestrowanie aplikacji → „Wyczyść”**


Uwagi:

  * Jest to **domyślnie wyłączone**. Włączaj tylko podczas aktywnego debugowania.
  * Traktuj plik jako poufny; nie udostępniaj go bez wcześniejszego sprawdzenia.


## Prywatne dane w ujednoliconym rejestrowaniu na macOS

Ujednolicone rejestrowanie redaguje większość danych, chyba że podsystem włączy `privacy -off`. Zgodnie z opisem Petera dotyczącym [zawiłości prywatności logowania](<https://steipete.me/posts/2025/logging-privacy-shenanigans>) na macOS (2025), steruje tym plik plist w `/Library/Preferences/Logging/Subsystems/`, którego kluczem jest nazwa podsystemu. Tylko nowe wpisy dziennika uwzględnią tę flagę, więc włącz ją przed odtworzeniem problemu.

## Włącz dla OpenClaw (`ai.openclaw`)

  * Najpierw zapisz plist do pliku tymczasowego, a następnie zainstaluj go atomowo jako root:

bashCopy code
[code]
    cat <<'EOF' >/tmp/ai.openclaw.plist<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>DEFAULT-OPTIONS</key>    <dict>        <key>Enable-Private-Data</key>        <true/>    </dict></dict></plist>EOFsudo install -m 644 -o root -g wheel /tmp/ai.openclaw.plist /Library/Preferences/Logging/Subsystems/ai.openclaw.plist
[/code]

  * Ponowne uruchomienie nie jest wymagane; logd szybko zauważa plik, ale tylko nowe wiersze dziennika będą zawierać prywatne dane.
  * Wyświetl bogatsze dane wyjściowe za pomocą istniejącego pomocnika, np. `./scripts/clawlog.sh --category WebChat --last 5m`.


## Wyłącz po debugowaniu

  * Usuń nadpisanie: `sudo rm /Library/Preferences/Logging/Subsystems/ai.openclaw.plist`.
  * Opcjonalnie uruchom `sudo log config --reload`, aby wymusić natychmiastowe usunięcie nadpisania przez logd.
  * Pamiętaj, że ta powierzchnia może zawierać numery telefonów i treści wiadomości; pozostawiaj plist na miejscu tylko wtedy, gdy aktywnie potrzebujesz dodatkowych szczegółów.


## Powiązane

  * [Aplikacja macOS](</pl/platforms/macos>)
  * [Rejestrowanie Gateway](</pl/gateway/logging>)


Was this useful?YesNo