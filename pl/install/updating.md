---
title: Aktualizowanie
source_url: https://docs.openclaw.ai/pl/install/updating
scraped_at: 2026-05-25
---

Dbaj, aby OpenClaw był aktualny.

## Zalecane: `openclaw update`

Najszybszy sposób aktualizacji. Wykrywa typ instalacji (npm lub git), pobiera najnowszą wersję, uruchamia `openclaw doctor` i restartuje Gateway.

bashCopy code
[code]
    openclaw update
[/code]

Aby przełączać kanały lub wskazać konkretną wersję:

bashCopy code
[code]
    openclaw update --channel betaopenclaw update --channel devopenclaw update --tag mainopenclaw update --dry-run   # preview without applying
[/code]

`openclaw update` nie przyjmuje `--verbose`. Do diagnostyki aktualizacji użyj `--dry-run`, aby podejrzeć planowane działania, `--json` dla wyników strukturalnych albo `openclaw update status --json`, aby sprawdzić kanał i stan dostępności. Instalator ma własną flagę `--verbose`, ale ta flaga nie jest częścią `openclaw update`.

`--channel beta` preferuje wersję beta, ale środowisko uruchomieniowe wraca do stable/latest, gdy tag beta jest niedostępny albo starszy niż najnowsze stabilne wydanie. Użyj `--tag beta`, jeśli chcesz surowy npm beta dist-tag do jednorazowej aktualizacji pakietu.

W przypadku zarządzanych pluginów fallback kanału beta jest ostrzeżeniem: aktualizacja core może nadal się powieść, podczas gdy plugin użyje swojego zapisanego domyślnego/najnowszego wydania, ponieważ nie jest dostępna żadna beta pluginu.

Zobacz [Kanały deweloperskie](</pl/install/development-channels>), aby poznać semantykę kanałów.

## Przełączanie między instalacjami npm i git

Używaj kanałów, gdy chcesz zmienić typ instalacji. Aktualizator zachowuje Twój stan, konfigurację, poświadczenia i workspace w `~/.openclaw`; zmienia tylko to, której instalacji kodu OpenClaw używają CLI i Gateway.

bashCopy code
[code]
    # npm package install -> editable git checkoutopenclaw update --channel dev # git checkout -> npm package installopenclaw update --channel stable
[/code]

Najpierw uruchom z `--dry-run`, aby podejrzeć dokładne przełączenie trybu instalacji:

bashCopy code
[code]
    openclaw update --channel dev --dry-runopenclaw update --channel stable --dry-run
[/code]

Kanał `dev` zapewnia checkout git, buduje go i instaluje globalne CLI z tego checkoutu. Kanały `stable` i `beta` używają instalacji pakietowych. Jeśli Gateway jest już zainstalowany, `openclaw update` odświeża metadane usługi i restartuje ją, chyba że przekażesz `--no-restart`.

## Alternatywnie: ponownie uruchom instalator

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

Dodaj `--no-onboard`, aby pominąć onboarding. Aby wymusić konkretny typ instalacji przez instalator, przekaż `--install-method git --no-onboard` albo `--install-method npm --no-onboard`.

Jeśli `openclaw update` nie powiedzie się po fazie instalacji pakietu npm, ponownie uruchom instalator. Instalator nie wywołuje starego aktualizatora; uruchamia globalną instalację pakietu bezpośrednio i może odzyskać częściowo zaktualizowaną instalację npm.

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm
[/code]

Aby przypiąć odzyskiwanie do konkretnej wersji lub dist-tag, dodaj `--version`:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm --version <version-or-dist-tag>
[/code]

## Alternatywnie: ręcznie przez npm, pnpm lub bun

bashCopy code
[code]
    npm i -g openclaw@latest
[/code]

Preferuj `openclaw update` dla instalacji nadzorowanych, ponieważ może koordynować podmianę pakietu z działającą usługą Gateway. Jeśli aktualizujesz ręcznie, gdy zarządzany Gateway działa, zrestartuj Gateway natychmiast po zakończeniu przez menedżera pakietów, aby stary proces nie obsługiwał dalej z podmienionych plików pakietu.

Gdy `openclaw update` zarządza globalną instalacją npm, najpierw instaluje cel w tymczasowym prefiksie npm, weryfikuje spakowany inwentarz `dist`, a następnie podmienia czyste drzewo pakietu do rzeczywistego globalnego prefiksu. Zapobiega to nakładaniu przez npm nowego pakietu na przestarzałe pliki ze starego pakietu. Jeśli polecenie instalacji się nie powiedzie, OpenClaw ponawia próbę raz z `--omit=optional`. Ta próba pomaga hostom, na których natywne opcjonalne zależności nie mogą się skompilować, jednocześnie zachowując widoczność pierwotnego błędu, jeśli fallback również się nie powiedzie.

bashCopy code
[code]
    pnpm add -g openclaw@latest
[/code]

bashCopy code
[code]
    bun add -g openclaw@latest
[/code]

### Zaawansowane tematy instalacji npm

Read-only package tree

OpenClaw traktuje spakowane instalacje globalne jako tylko do odczytu w czasie działania, nawet gdy globalny katalog pakietu jest zapisywalny dla bieżącego użytkownika. Instalacje pakietów Plugin znajdują się w należących do OpenClaw korzeniach npm/git pod katalogiem konfiguracji użytkownika, a uruchomienie Gateway nie modyfikuje drzewa pakietu OpenClaw.

Niektóre konfiguracje npm w systemie Linux instalują pakiety globalne pod katalogami należącymi do root, takimi jak `/usr/lib/node_modules/openclaw`. OpenClaw obsługuje ten układ, ponieważ polecenia instalacji/aktualizacji pluginów zapisują poza tym globalnym katalogiem pakietu.

Hardened systemd units

Przyznaj OpenClaw dostęp do zapisu w jego korzeniach konfiguracji/stanu, aby jawne instalacje pluginów, aktualizacje pluginów i czyszczenie przez doctor mogły utrwalać swoje zmiany:

iniCopy code
[code]
    ReadWritePaths=/var/lib/openclaw /home/openclaw/.openclaw /tmp
[/code]

Disk-space preflight

Przed aktualizacjami pakietów i jawnymi instalacjami pluginów OpenClaw próbuje wykonać best-effort sprawdzenie miejsca na dysku dla woluminu docelowego. Mała ilość miejsca generuje ostrzeżenie ze sprawdzoną ścieżką, ale nie blokuje aktualizacji, ponieważ limity systemu plików, migawki i woluminy sieciowe mogą zmienić się po sprawdzeniu. Rzeczywista instalacja przez menedżera pakietów i weryfikacja poinstalacyjna pozostają autorytatywne.

## Automatyczny aktualizator

Automatyczny aktualizator jest domyślnie wyłączony. Włącz go w `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  update: {    channel: "stable",    auto: {      enabled: true,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

Kanał | Zachowanie  
---|---  
`stable` | Czeka `stableDelayHours`, a następnie stosuje z deterministycznym jitterem w ramach `stableJitterHours` (rozłożone wdrażanie).  
`beta` | Sprawdza co `betaCheckIntervalHours` (domyślnie: co godzinę) i stosuje natychmiast.  
`dev` | Brak automatycznego stosowania. Użyj `openclaw update` ręcznie.  
  
Gateway rejestruje też podpowiedź aktualizacji przy starcie (wyłącz przez `update.checkOnStart: false`). W celu downgrade'u lub odzyskiwania po incydencie ustaw `OPENCLAW_NO_AUTO_UPDATE=1` w środowisku Gateway, aby zablokować automatyczne stosowanie nawet wtedy, gdy skonfigurowano `update.auto.enabled`. Podpowiedzi aktualizacji przy starcie nadal mogą działać, chyba że wyłączono też `update.checkOnStart`.

Aktualizacje przez menedżera pakietów żądane przez aktywny handler płaszczyzny sterowania Gateway wymuszają restart aktualizacji bez odroczenia i bez cooldownu po podmianie pakietu. Pozwala to uniknąć pozostawienia starego procesu w pamięci na tyle długo, by leniwie ładował fragmenty z drzewa pakietu, które zostało już zastąpione. Powłokowe `openclaw update` pozostaje preferowaną ścieżką dla instalacji nadzorowanych, ponieważ może zatrzymać i ponownie uruchomić usługę wokół aktualizacji.

## Po aktualizacji

### Uruchom doctor

bashCopy code
[code]
    openclaw doctor
[/code]

Migruje konfigurację, audytuje zasady DM i sprawdza kondycję Gateway. Szczegóły: [Doctor](</pl/gateway/doctor>)

### Zrestartuj Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Zweryfikuj

bashCopy code
[code]
    openclaw health
[/code]

## Rollback

### Przypnij wersję (npm)

bashCopy code
[code]
    npm i -g openclaw@<version>openclaw doctoropenclaw gateway restart
[/code]

### Przypnij commit (źródło)

bashCopy code
[code]
    git fetch origingit checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"pnpm install && pnpm buildopenclaw gateway restart
[/code]

Aby wrócić do najnowszej wersji: `git checkout main && git pull`.

## Jeśli utkniesz

  * Ponownie uruchom `openclaw doctor` i uważnie przeczytaj wynik.
  * W przypadku `openclaw update --channel dev` na checkoutach źródłowych aktualizator automatycznie bootstrapuje `pnpm`, gdy jest to potrzebne. Jeśli zobaczysz błąd bootstrapu pnpm/corepack, zainstaluj `pnpm` ręcznie (albo ponownie włącz `corepack`) i uruchom aktualizację ponownie.
  * Sprawdź: [Rozwiązywanie problemów](</pl/gateway/troubleshooting>)
  * Zapytaj na Discord: <https://discord.gg/clawd>


## Powiązane

  * [Przegląd instalacji](</pl/install>): wszystkie metody instalacji.
  * [Doctor](</pl/gateway/doctor>): kontrole kondycji po aktualizacjach.
  * [Migracja](</pl/install/migrating>): przewodniki migracji wersji głównych.


Was this useful?YesNo