---
title: Publikowanie
source_url: https://docs.openclaw.ai/pl/clawhub/publishing
scraped_at: 2026-05-25
---

# Publikowanie

Publikowanie w ClawHub ma zakres właściciela: każda publikacja wskazuje wydawcę, a serwer decyduje, czy zalogowany użytkownik ma prawo tam publikować.

## Właściciele

Właściciel to identyfikator wydawcy w ClawHub, taki jak `@alice` lub `@openclaw`. Właściciele osobowi są tworzeni dla użytkowników. Właściciele organizacyjni mogą mieć wielu członków.

Podczas publikowania używasz swojego właściciela osobowego albo wybierasz właściciela organizacyjnego, u którego masz dostęp wydawcy.

## Skills

Skills publikuje się z folderu skill. Strona publiczna to:

textCopy code
[code]
    https://clawhub.ai/<owner>/<slug>
[/code]

Przykład:

textCopy code
[code]
    https://clawhub.ai/alice/review-helper
[/code]

Żądanie publikacji obejmuje wybranego właściciela, slug, wersję, dziennik zmian i pliki. Serwer sprawdza, czy aktor może publikować jako ten właściciel, zanim utworzy wydanie.

Aby przenieść istniejący skill do innego właściciela podczas publikowania nowej wersji, wybierz nowego właściciela i jawnie potwierdź przeniesienie własności. W CLI/API przekaż docelowego właściciela oraz zgodę na migrację:

shCopy code
[code]
    clawhub skill publish ./review-helper --owner openclaw --migrate-owner --version 1.2.0
[/code]

Migracja właściciela skill wymaga dostępu administratora lub właściciela zarówno u bieżącego właściciela, jak i u właściciela docelowego. Zachowuje skill, historię wersji, statystyki, komentarze, forki, aliasy i ścieżkę audytu; adresy URL starego właściciela nadal działają przez ścieżkę aliasu/przekierowania.

## Pluginy

Pluginy używają nazw pakietów w stylu npm. Nazwy pakietów z zakresem zawierają właściciela w pierwszej części nazwy:

textCopy code
[code]
    @owner/package-name
[/code]

Zakres musi odpowiadać wybranemu właścicielowi publikacji. Jeśli pakiet nazywa się `@openclaw/dronzer`, można go opublikować tylko jako `@openclaw`. Jeśli publikujesz jako `@vintageayu`, zmień nazwę pakietu na `@vintageayu/dronzer`.

Zapobiega to sytuacji, w której pakiet rości sobie prawo do przestrzeni nazw organizacji, której wydawca nie kontroluje.

## Przebieg wydania

  1. Interfejs użytkownika, CLI lub workflow GitHub zbiera metadane pakietu i pliki.
  2. Żądanie publikacji jest wysyłane do ClawHub z wybranym właścicielem.
  3. Serwer weryfikuje uprawnienia właściciela, zakres pakietu, nazwę pakietu, wersję, limity plików i metadane źródła.
  4. ClawHub zapisuje wydanie i uruchamia automatyczne kontrole bezpieczeństwa.
  5. Nowe wydania są ukryte przed standardowymi powierzchniami instalacji/pobierania do czasu zakończenia przeglądu i weryfikacji.


Jeśli weryfikacja nie powiedzie się, wydanie nie zostanie utworzone.

## FAQ

### Zakres pakietu musi odpowiadać wybranemu właścicielowi

Jeśli zakres pakietu i wybrany właściciel nie pasują do siebie, ClawHub odrzuca publikację:

textCopy code
[code]
    Package scope "@openclaw" must match selected owner "@vintageayu".Publish as "@openclaw" or rename this package to "@vintageayu/dronzer".
[/code]

Aby to naprawić, wybierz właściciela wskazanego przez zakres pakietu albo zmień nazwę pakietu tak, aby zakres odpowiadał właścicielowi, jako którego możesz publikować.

Jeśli nazwa pakietu ma już właściwy zakres, ale pakiet należy do niewłaściwego wydawcy, zamiast tego przenieś własność:

shCopy code
[code]
    clawhub package transfer @opik/opik-openclaw --to opik
[/code]

Używaj transferu pakietu lub skill tylko wtedy, gdy masz dostęp administratora zarówno do bieżącego właściciela, jak i wydawcy docelowego. Transfer pakietu nie pozwala publikować w zakresie, którego nie możesz zarządzać.

Chroni to przestrzenie nazw organizacji. Pakiet o nazwie `@openclaw/dronzer` rości sobie prawo do przestrzeni nazw `@openclaw`, więc publikować go mogą tylko wydawcy z dostępem do właściciela `@openclaw`.

Was this useful?YesNo