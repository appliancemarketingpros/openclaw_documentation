---
title: Reakcje
source_url: https://docs.openclaw.ai/pl/tools/reactions
scraped_at: 2026-05-25
---

Agent może dodawać i usuwać reakcje emoji na wiadomościach za pomocą narzędzia `message` z akcją `react`. Zachowanie reakcji różni się w zależności od kanału i transportu.

## Jak to działa

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * `emoji` jest wymagane podczas dodawania reakcji.
  * Ustaw `emoji` na pusty ciąg (`""`), aby usunąć reakcję/reakcje bota.
  * Ustaw `remove: true`, aby usunąć konkretne emoji (wymaga niepustego `emoji`).
  * W kanałach obsługujących reakcje statusu `trackToolCalls: true` w reakcji pozwala środowisku uruchomieniowemu używać tej wiadomości z reakcją do kolejnych reakcji postępu narzędzia w tej samej turze.


## Zachowanie kanałów

Discord and Slack

  * Puste `emoji` usuwa wszystkie reakcje bota na wiadomości.
  * `remove: true` usuwa tylko określone emoji.

Google Chat

  * Puste `emoji` usuwa reakcje aplikacji na wiadomości.
  * `remove: true` usuwa tylko określone emoji.

Telegram

  * Puste `emoji` usuwa reakcje bota.
  * `remove: true` również usuwa reakcje, ale nadal wymaga niepustego `emoji` do walidacji narzędzia.

WhatsApp

  * Puste `emoji` usuwa reakcję bota.
  * `remove: true` jest wewnętrznie mapowane na puste emoji (nadal wymaga `emoji` w wywołaniu narzędzia).

Zalo Personal (zalouser)

  * Wymaga niepustego `emoji`.
  * `remove: true` usuwa tę konkretną reakcję emoji.

Feishu/Lark

  * Użyj narzędzia `feishu_reaction` z akcjami `add`, `remove` i `list`.
  * Dodawanie/usuwanie wymaga `emoji_type`; usuwanie wymaga także `reaction_id`.

Signal

  * Powiadomienia o reakcjach przychodzących są kontrolowane przez `channels.signal.reactionNotifications`: `"off"` je wyłącza, `"own"` (domyślnie) emituje zdarzenia, gdy użytkownicy reagują na wiadomości bota, a `"all"` emituje zdarzenia dla wszystkich reakcji.

iMessage

  * Reakcje wychodzące to tapbacki iMessage (`love`, `like`, `dislike`, `laugh`, `emphasize` i `question`).
  * Powiadomienia o przychodzących tapbackach są kontrolowane przez `channels.imessage.reactionNotifications`: `"off"` je wyłącza, `"own"` (domyślnie) emituje zdarzenia, gdy użytkownicy reagują na wiadomości utworzone przez bota, a `"all"` emituje zdarzenia dla wszystkich tapbacków od autoryzowanych nadawców.


## Poziom reakcji

Konfiguracja `reactionLevel` dla poszczególnych kanałów kontroluje, jak szeroko agent używa reakcji. Wartości to zwykle `off`, `ack`, `minimal` lub `extensive`.

  * [Telegram reactionLevel](</pl/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</pl/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


Ustaw `reactionLevel` na poszczególnych kanałach, aby dostroić, jak aktywnie agent reaguje na wiadomości na każdej platformie.

## Powiązane

  * [Wysyłanie agenta](</pl/tools/agent-send>) — narzędzie `message`, które obejmuje `react`
  * [Kanały](</pl/channels>) — konfiguracja specyficzna dla kanału


Was this useful?YesNo