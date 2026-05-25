---
title: Uprawnienia macOS
source_url: https://docs.openclaw.ai/pl/platforms/mac/permissions
scraped_at: 2026-05-25
---

Uprawnienia macOS są delikatne. TCC wiąże przyznanie uprawnienia z podpisem kodu aplikacji, identyfikatorem bundle i ścieżką na dysku. Jeśli którakolwiek z tych rzeczy się zmieni, macOS traktuje aplikację jako nową i może usunąć lub ukryć prompty.

## Wymagania dla stabilnych uprawnień

  * Ta sama ścieżka: uruchamiaj aplikację z ustalonej lokalizacji (dla OpenClaw `dist/OpenClaw.app`).
  * Ten sam identyfikator bundle: zmiana bundle ID tworzy nową tożsamość uprawnień.
  * Podpisana aplikacja: niepodpisane albo podpisane ad-hoc buildy nie utrwalają uprawnień.
  * Spójny podpis: używaj prawdziwego certyfikatu Apple Development albo Developer ID, aby podpis pozostawał stabilny między przebudowaniami.


Podpisy ad-hoc generują nową tożsamość przy każdym buildzie. macOS zapomni wcześniejsze przyznania, a prompty mogą całkowicie zniknąć, dopóki nie zostaną wyczyszczone stare wpisy.

## Lista kontrolna odzyskiwania, gdy prompty znikają

  1. Zamknij aplikację.
  2. Usuń wpis aplikacji w System Settings -> Privacy & Security.
  3. Uruchom ponownie aplikację z tej samej ścieżki i ponownie przyznaj uprawnienia.
  4. Jeśli prompt nadal się nie pojawia, zresetuj wpisy TCC przez `tccutil` i spróbuj ponownie.
  5. Niektóre uprawnienia pojawiają się ponownie dopiero po pełnym restarcie macOS.


Przykładowe resety (w razie potrzeby zastąp bundle ID):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## Uprawnienia do plików i folderów (Desktop/Documents/Downloads)

macOS może także blokować Desktop, Documents i Downloads dla procesów terminalowych/tła. Jeśli odczyty plików albo listowania katalogów zawieszają się, przyznaj dostęp temu samemu kontekstowi procesu, który wykonuje operacje na plikach (na przykład Terminal/iTerm, aplikacja uruchamiana przez LaunchAgent albo proces SSH).

Obejście: przenieś pliki do obszaru roboczego OpenClaw (`~/.openclaw/workspace`), jeśli chcesz uniknąć przyznań per folder.

Jeśli testujesz uprawnienia, zawsze podpisuj prawdziwym certyfikatem. Buildy ad-hoc są akceptowalne tylko do szybkich lokalnych uruchomień, gdzie uprawnienia nie mają znaczenia.

## Powiązane

  * [macOS app](</pl/platforms/macos>)
  * [macOS signing](</pl/platforms/mac/signing>)


Was this useful?YesNo