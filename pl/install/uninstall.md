---
title: Odinstalowanie
source_url: https://docs.openclaw.ai/pl/install/uninstall
scraped_at: 2026-05-25
---

Dwie ścieżki:

  * **Łatwa ścieżka** , jeśli `openclaw` jest nadal zainstalowany.
  * **Ręczne usunięcie usługi** , jeśli CLI już nie ma, ale usługa nadal działa.


## Łatwa ścieżka (CLI nadal zainstalowane)

Zalecane: użyj wbudowanego deinstalatora:

bashCopy code
[code]
    openclaw uninstall
[/code]

Tryb nieinteraktywny (automatyzacja / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Kroki ręczne (ten sam rezultat):

  1. Zatrzymaj usługę gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Odinstaluj usługę gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Usuń stan + konfigurację:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Jeśli ustawiłeś `OPENCLAW_CONFIG_PATH` na niestandardową lokalizację poza katalogiem stanu, usuń również ten plik.

  4. Usuń obszar roboczy (opcjonalnie, usuwa pliki agenta):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Usuń instalację CLI (wybierz tę, której użyłeś):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Jeśli zainstalowałeś aplikację macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Uwagi:

  * Jeśli używałeś profili (`--profile` / `OPENCLAW_PROFILE`), powtórz krok 3 dla każdego katalogu stanu (domyślnie są to `~/.openclaw-<profile>`).
  * W trybie zdalnym katalog stanu znajduje się na **hoście gateway** , więc uruchom tam również kroki 1-4.


## Ręczne usunięcie usługi (CLI nie jest zainstalowane)

Użyj tej ścieżki, jeśli usługa gateway nadal działa, ale `openclaw` nie istnieje.

### macOS (launchd)

Domyślna etykieta to `ai.openclaw.gateway` (albo `ai.openclaw.<profile>`; starsze `com.openclaw.*` mogą nadal istnieć):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Jeśli używałeś profilu, zastąp etykietę i nazwę plist przez `ai.openclaw.<profile>`. Usuń też wszelkie starsze pliki plist `com.openclaw.*`, jeśli istnieją.

### Linux (jednostka użytkownika systemd)

Domyślna nazwa jednostki to `openclaw-gateway.service` (albo `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

Domyślna nazwa zadania to `OpenClaw Gateway` (albo `OpenClaw Gateway (<profile>)`). Skrypt zadania znajduje się w katalogu stanu.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Jeśli używałeś profilu, usuń pasującą nazwę zadania i `~\.openclaw-<profile>\gateway.cmd`.

## Zwykła instalacja vs checkout ze źródła

### Zwykła instalacja (`install.sh` / npm / pnpm / bun)

Jeśli użyłeś `https://openclaw.ai/install.sh` albo `install.ps1`, CLI zostało zainstalowane przez `npm install -g openclaw@latest`. Usuń je przez `npm rm -g openclaw` (albo `pnpm remove -g` / `bun remove -g`, jeśli instalowałeś w ten sposób).

### Checkout ze źródła (`git clone`)

Jeśli uruchamiasz z checkoutu repo (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Odinstaluj usługę gateway **przed** usunięciem repo (użyj łatwej ścieżki powyżej albo ręcznego usunięcia usługi).
  2. Usuń katalog repo.
  3. Usuń stan + obszar roboczy, jak pokazano wyżej.


## Powiązane

  * [Install overview](</pl/install>)
  * [Migration guide](</pl/install/migrating>)


Was this useful?YesNo