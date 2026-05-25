---
title: Logowanie w przeglądarce
source_url: https://docs.openclaw.ai/pl/tools/browser-login
scraped_at: 2026-05-25
---

## Logowanie ręczne (zalecane)

Gdy witryna wymaga logowania, **zaloguj się ręcznie** w profilu przeglądarki **hosta** (przeglądarce openclaw).

**Nie** przekazuj modelowi swoich poświadczeń. Automatyczne logowania często uruchamiają zabezpieczenia antybotowe i mogą zablokować konto.

Powrót do głównej dokumentacji przeglądarki: [Przeglądarka](</pl/tools/browser>).

## Który profil Chrome jest używany?

OpenClaw kontroluje **dedykowany profil Chrome** (o nazwie `openclaw`, z pomarańczowym odcieniem interfejsu). Jest on oddzielony od Twojego codziennego profilu przeglądarki.

W przypadku wywołań narzędzia przeglądarki przez agenta:

  * Domyślny wybór: agent powinien używać swojej odizolowanej przeglądarki `openclaw`.
  * Używaj `profile="user"` tylko wtedy, gdy znaczenie mają istniejące zalogowane sesje, a użytkownik jest przy komputerze, aby kliknąć/zatwierdzić ewentualny monit o dołączenie.
  * Jeśli masz wiele profili przeglądarki użytkownika, określ profil jawnie zamiast zgadywać.


Dwa proste sposoby dostępu:

  1. **Poproś agenta o otwarcie przeglądarki** , a następnie zaloguj się samodzielnie.
  2. **Otwórz ją przez CLI** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Jeśli masz wiele profili, przekaż `--browser-profile <name>` (domyślnie jest to `openclaw`).

## X/Twitter: zalecany przepływ

  * **Czytanie/wyszukiwanie/wątki:** używaj przeglądarki **hosta** (logowanie ręczne).
  * **Publikowanie aktualizacji:** używaj przeglądarki **hosta** (logowanie ręczne).


## Piaskownica + dostęp do przeglądarki hosta

Sesje przeglądarki w piaskownicy **częściej** uruchamiają wykrywanie botów. W przypadku X/Twitter (i innych restrykcyjnych witryn) preferuj przeglądarkę **hosta**.

Jeśli agent działa w piaskownicy, narzędzie przeglądarki domyślnie używa piaskownicy. Aby zezwolić na sterowanie hostem:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Następnie samodzielnie otwórz przeglądarkę hosta (wywołania CLI zawsze działają na przeglądarce hosta):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

Wywołania narzędzia `browser` agenta mogą wtedy wskazywać hosta po ustawieniu `sandbox.browser.allowHostControl: true`. Alternatywnie wyłącz piaskownicę dla agenta, który publikuje aktualizacje.

## Powiązane

  * [Przeglądarka](</pl/tools/browser>)
  * [Rozwiązywanie problemów z przeglądarką w systemie Linux](</pl/tools/browser-linux-troubleshooting>)
  * [Rozwiązywanie problemów z przeglądarką w WSL2](</pl/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo