---
title: Inicjalizacja agenta
source_url: https://docs.openclaw.ai/pl/start/bootstrapping
scraped_at: 2026-05-25
---

Inicjalizacja to procedura **pierwszego uruchomienia** , która przygotowuje obszar roboczy agenta i zbiera dane tożsamości. Dzieje się po wdrożeniu, gdy agent uruchamia się po raz pierwszy.

## Co robi inicjalizacja

Podczas pierwszego uruchomienia agenta OpenClaw inicjalizuje obszar roboczy (domyślnie `~/.openclaw/workspace`):

  * Dodaje początkowe pliki `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Uruchamia krótką procedurę pytań i odpowiedzi (po jednym pytaniu naraz).
  * Zapisuje tożsamość i preferencje w `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Po zakończeniu usuwa `BOOTSTRAP.md`, aby procedura uruchomiła się tylko raz.


W przypadku uruchomień osadzonych/lokalnych modeli OpenClaw utrzymuje `BOOTSTRAP.md` poza uprzywilejowanym kontekstem systemowym. Podczas głównego interaktywnego pierwszego uruchomienia nadal przekazuje zawartość pliku w prompcie użytkownika, aby modele, które nie wywołują niezawodnie narzędzia `read`, mogły ukończyć procedurę. Jeśli bieżące uruchomienie nie może bezpiecznie uzyskać dostępu do obszaru roboczego, agent otrzymuje ograniczoną notatkę inicjalizacyjną zamiast ogólnego powitania.

## Pomijanie inicjalizacji

Aby pominąć to w przypadku wstępnie przygotowanego obszaru roboczego, uruchom `openclaw onboard --skip-bootstrap`.

## Gdzie działa

Inicjalizacja zawsze działa na **hoście Gateway**. Jeśli aplikacja macOS łączy się ze zdalnym Gateway, obszar roboczy i pliki inicjalizacji znajdują się na tej zdalnej maszynie.

## Powiązana dokumentacja

  * Wdrożenie aplikacji macOS: [Wdrożenie](</pl/start/onboarding>)
  * Układ obszaru roboczego: [Obszar roboczy agenta](</pl/concepts/agent-workspace>)


Was this useful?YesNo