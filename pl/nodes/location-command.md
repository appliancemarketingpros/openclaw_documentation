---
title: Polecenie lokalizacji
source_url: https://docs.openclaw.ai/pl/nodes/location-command
scraped_at: 2026-05-25
---

## W skrócie

  * `location.get` jest poleceniem Node (przez `node.invoke`).
  * Domyślnie wyłączone.
  * Ustawienia aplikacji Android używają selektora: Wyłączone / Podczas używania.
  * Osobny przełącznik: Dokładna lokalizacja.


## Dlaczego selektor (a nie tylko przełącznik)

Uprawnienia systemu operacyjnego mają wiele poziomów. Możemy udostępnić selektor w aplikacji, ale o faktycznym przyznaniu dostępu nadal decyduje system operacyjny.

  * iOS/macOS mogą pokazywać **Podczas używania** lub **Zawsze** w monitach systemowych/Ustawieniach.
  * Aplikacja Android obecnie obsługuje tylko lokalizację na pierwszym planie.
  * Dokładna lokalizacja jest osobnym uprawnieniem (iOS 14+ „Dokładna”, Android „fine” kontra „coarse”).


Selektor w UI steruje żądanym przez nas trybem; faktycznie przyznane uprawnienie znajduje się w ustawieniach systemu operacyjnego.

## Model ustawień

Dla każdego urządzenia Node:

  * `location.enabledMode`: `off | whileUsing`
  * `location.preciseEnabled`: bool


Zachowanie UI:

  * Wybranie `whileUsing` żąda uprawnienia do lokalizacji na pierwszym planie.
  * Jeśli system operacyjny odmówi żądanego poziomu, przywróć najwyższy przyznany poziom i pokaż status.


## Mapowanie uprawnień (node.permissions)

Opcjonalne. Node macOS zgłasza `location` przez mapę uprawnień; iOS/Android mogą ją pominąć.

## Polecenie: `location.get`

Wywoływane przez `node.invoke`.

Parametry (sugerowane):

jsonCopy code
[code]
    {  "timeoutMs": 10000,  "maxAgeMs": 15000,  "desiredAccuracy": "coarse|balanced|precise"}
[/code]

Ładunek odpowiedzi:

jsonCopy code
[code]
    {  "lat": 48.20849,  "lon": 16.37208,  "accuracyMeters": 12.5,  "altitudeMeters": 182.0,  "speedMps": 0.0,  "headingDeg": 270.0,  "timestamp": "2026-01-03T12:34:56.000Z",  "isPrecise": true,  "source": "gps|wifi|cell|unknown"}
[/code]

Błędy (stabilne kody):

  * `LOCATION_DISABLED`: selektor jest wyłączony.
  * `LOCATION_PERMISSION_REQUIRED`: brakuje uprawnienia dla żądanego trybu.
  * `LOCATION_BACKGROUND_UNAVAILABLE`: aplikacja działa w tle, ale dozwolone jest tylko Podczas używania.
  * `LOCATION_TIMEOUT`: brak ustalenia pozycji w czasie.
  * `LOCATION_UNAVAILABLE`: awaria systemu / brak dostawców.


## Zachowanie w tle

  * Aplikacja Android odmawia `location.get`, gdy działa w tle.
  * Pozostaw OpenClaw otwarte podczas żądania lokalizacji na Androidzie.
  * Inne platformy Node mogą się różnić.


## Integracja z modelem/narzędziami

  * Powierzchnia narzędzia: narzędzie `nodes` dodaje akcję `location_get` (wymagany Node).
  * CLI: `openclaw nodes location get --node <id>`.
  * Wytyczne dla agenta: wywołuj tylko wtedy, gdy użytkownik włączył lokalizację i rozumie zakres.


## Tekst UX (sugerowany)

  * Wyłączone: „Udostępnianie lokalizacji jest wyłączone.”
  * Podczas używania: „Tylko gdy OpenClaw jest otwarte.”
  * Dokładna: „Używaj dokładnej lokalizacji GPS. Wyłącz przełącznik, aby udostępniać przybliżoną lokalizację.”


## Powiązane

  * [Parsowanie lokalizacji kanału](</pl/channels/location>)
  * [Przechwytywanie obrazu z kamery](</pl/nodes/camera>)
  * [Tryb rozmowy](</pl/nodes/talk>)


Was this useful?YesNo