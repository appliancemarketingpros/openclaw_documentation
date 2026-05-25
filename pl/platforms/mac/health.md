---
title: Health checks (macOS)
source_url: https://docs.openclaw.ai/pl/platforms/mac/health
scraped_at: 2026-05-25
---

# Health Checks na macOS

Jak sprawdzić w aplikacji paska menu, czy powiązany kanał jest zdrowy.

## Pasek menu

  * Kropka statusu odzwierciedla teraz health Baileys: 
    * Zielona: połączony + socket został niedawno otwarty.
    * Pomarańczowa: trwa łączenie/ponawianie.
    * Czerwona: wylogowano albo probe zakończył się błędem.
  * Druga linia pokazuje „linked · auth 12m” albo wyświetla powód błędu.
  * Pozycja menu „Run Health Check” uruchamia probe na żądanie.


## Ustawienia

  * Karta General zyskuje kartę Health pokazującą: wiek powiązanego auth, ścieżkę/liczbę wpisów magazynu sesji, czas ostatniej kontroli, ostatni błąd/kod statusu oraz przyciski Run Health Check / Reveal Logs.
  * Używa cache'owanego snapshotu, więc UI ładuje się natychmiast i działa z łagodnym fallbackiem offline.
  * **Karta Channels** pokazuje status kanałów + kontrolki dla WhatsApp/Telegram (QR logowania, wylogowanie, probe, ostatnie rozłączenie/błąd).


## Jak działa probe

  * Aplikacja uruchamia `openclaw health --json` przez `ShellExecutor` co około 60 s i na żądanie. Probe ładuje poświadczenia i raportuje status bez wysyłania wiadomości.
  * Cache'uj osobno ostatni dobry snapshot i ostatni błąd, aby uniknąć migotania; pokazuj znacznik czasu każdego z nich.


## Gdy masz wątpliwości

  * Nadal możesz używać przepływu CLI opisanego w [health Gateway](</pl/gateway/health>) (`openclaw status`, `openclaw status --deep`, `openclaw health --json`) i śledzić `/tmp/openclaw/openclaw-*.log` pod kątem `web-heartbeat` / `web-reconnect`.


## Powiązane

  * [Health Gateway](</pl/gateway/health>)
  * [Aplikacja macOS](</pl/platforms/macos>)


Was this useful?YesNo