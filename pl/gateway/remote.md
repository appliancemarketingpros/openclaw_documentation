---
title: Dostęp zdalny
source_url: https://docs.openclaw.ai/pl/gateway/remote
scraped_at: 2026-05-25
---

To repo obsługuje „remote over SSH”, utrzymując pojedynczy Gateway (master) uruchomiony na dedykowanym hoście (desktop/serwer) i podłączając do niego klientów.

  * Dla **operatorów (Ty / aplikacja macOS)** : tunelowanie SSH jest uniwersalnym rozwiązaniem awaryjnym.
  * Dla **węzłów (iOS/Android i przyszłe urządzenia)** : łącz się z **WebSocket** Gateway (LAN/tailnet lub tunel SSH w razie potrzeby).


## Główna idea

  * WebSocket Gateway wiąże się z **loopback** na skonfigurowanym porcie (domyślnie 18789).
  * Do użycia zdalnego przekierowujesz ten port loopback przez SSH (albo używasz tailnet/VPN i tunelujesz mniej).


## Typowe konfiguracje VPN i tailnet

Pomyśl o **hoście Gateway** jako o miejscu, w którym działa agent. To on posiada sesje, profile uwierzytelniania, kanały i stan. Twój laptop, desktop i węzły łączą się z tym hostem.

### Zawsze włączony Gateway w tailnet

Uruchom Gateway na trwałym hoście (VPS lub serwer domowy) i uzyskuj do niego dostęp przez **Tailscale** lub SSH.

  * **Najlepsze UX:** pozostaw `gateway.bind: "loopback"` i użyj **Tailscale Serve** dla Control UI.
  * **Rozwiązanie awaryjne:** pozostaw loopback plus tunel SSH z dowolnej maszyny, która potrzebuje dostępu.
  * **Przykłady:** [exe.dev](</pl/install/exe-dev>) (łatwa VM) lub [Hetzner](</pl/install/hetzner>) (produkcyjny VPS).


Idealne, gdy laptop często usypia, ale chcesz, aby agent był zawsze włączony.

### Domowy desktop uruchamia Gateway

Laptop **nie** uruchamia agenta. Łączy się zdalnie:

  * Użyj trybu **Remote over SSH** w aplikacji macOS (Settings → General → OpenClaw runs).
  * Aplikacja otwiera tunel i nim zarządza, więc WebChat oraz kontrole zdrowia po prostu działają.


Runbook: [zdalny dostęp macOS](</pl/platforms/mac/remote>).

### Laptop uruchamia Gateway

Zachowaj Gateway lokalnie, ale udostępnij go bezpiecznie:

  * Tunel SSH do laptopa z innych maszyn albo
  * Tailscale Serve dla Control UI i utrzymanie Gateway wyłącznie na loopback.


Przewodniki: [Tailscale](</pl/gateway/tailscale>) i [omówienie Web](</pl/web>).

## Przepływ poleceń (co działa gdzie)

Jedna usługa gateway jest właścicielem stanu + kanałów. Węzły są urządzeniami peryferyjnymi.

Przykład przepływu (Telegram → węzeł):

  * Wiadomość Telegram trafia do **Gateway**.
  * Gateway uruchamia **agenta** i decyduje, czy wywołać narzędzie węzła.
  * Gateway wywołuje **węzeł** przez WebSocket Gateway (`node.*` RPC).
  * Węzeł zwraca wynik; Gateway odpowiada z powrotem do Telegram.


Uwagi:

  * **Węzły nie uruchamiają usługi gateway.** Na host powinien działać tylko jeden gateway, chyba że celowo uruchamiasz izolowane profile (zobacz [Wiele gatewayów](</pl/gateway/multiple-gateways>)).
  * „Tryb węzła” aplikacji macOS to po prostu klient węzła przez WebSocket Gateway.


## Tunel SSH (CLI + narzędzia)

Utwórz lokalny tunel do zdalnego Gateway WS:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Gdy tunel działa:

  * `openclaw health` i `openclaw status --deep` docierają teraz do zdalnego gateway przez `ws://127.0.0.1:18789`.
  * `openclaw gateway status`, `openclaw gateway health`, `openclaw gateway probe` i `openclaw gateway call` mogą także kierować na przekierowany URL przez `--url`, gdy jest to potrzebne.


## Zdalne wartości domyślne CLI

Możesz utrwalić zdalny cel, aby polecenia CLI używały go domyślnie:

json5Copy code
[code]
    {  gateway: {    mode: "remote",    remote: {      url: "ws://127.0.0.1:18789",      token: "your-token",    },  },}
[/code]

Gdy gateway działa tylko na loopback, pozostaw URL jako `ws://127.0.0.1:18789` i najpierw otwórz tunel SSH. W transporcie tunelu SSH aplikacji macOS wykryte nazwy hostów gateway należą do `gateway.remote.sshTarget`; `gateway.remote.url` pozostaje lokalnym URL-em tunelu.

## Priorytet poświadczeń

Rozwiązywanie poświadczeń Gateway stosuje jeden wspólny kontrakt w ścieżkach call/probe/status oraz monitorowaniu zatwierdzeń wykonania Discord. Node-host używa tego samego kontraktu bazowego z jednym wyjątkiem trybu lokalnego (celowo ignoruje `gateway.remote.*`):

  * Jawne poświadczenia (`--token`, `--password` lub narzędziowe `gatewayToken`) zawsze wygrywają na ścieżkach wywołań, które akceptują jawne uwierzytelnianie.
  * Bezpieczeństwo nadpisania URL: 
    * Nadpisania URL w CLI (`--url`) nigdy nie używają ponownie niejawnych poświadczeń z konfiguracji/środowiska.
    * Nadpisania URL przez env (`OPENCLAW_GATEWAY_URL`) mogą używać tylko poświadczeń env (`OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`).
  * Domyślne wartości trybu lokalnego: 
    * token: `OPENCLAW_GATEWAY_TOKEN` -> `gateway.auth.token` -> `gateway.remote.token` (zdalne rozwiązanie awaryjne ma zastosowanie tylko wtedy, gdy lokalne wejście tokena auth jest nieustawione)
    * password: `OPENCLAW_GATEWAY_PASSWORD` -> `gateway.auth.password` -> `gateway.remote.password` (zdalne rozwiązanie awaryjne ma zastosowanie tylko wtedy, gdy lokalne wejście hasła auth jest nieustawione)
  * Domyślne wartości trybu zdalnego: 
    * token: `gateway.remote.token` -> `OPENCLAW_GATEWAY_TOKEN` -> `gateway.auth.token`
    * password: `OPENCLAW_GATEWAY_PASSWORD` -> `gateway.remote.password` -> `gateway.auth.password`
  * Wyjątek trybu lokalnego Node-host: `gateway.remote.token` / `gateway.remote.password` są ignorowane.
  * Zdalne kontrole tokenów probe/status są domyślnie ścisłe: używają tylko `gateway.remote.token` (bez lokalnego rozwiązania awaryjnego tokena), gdy celują w tryb zdalny.
  * Nadpisania env Gateway używają tylko `OPENCLAW_GATEWAY_*`.


## Chat UI przez SSH

WebChat nie używa już osobnego portu HTTP. Chat UI SwiftUI łączy się bezpośrednio z WebSocket Gateway.

  * Przekieruj `18789` przez SSH (zobacz wyżej), a następnie połącz klientów z `ws://127.0.0.1:18789`.
  * Na macOS preferuj tryb „Remote over SSH” aplikacji, który automatycznie zarządza tunelem.


## Aplikacja macOS Remote over SSH

Aplikacja paska menu macOS może obsłużyć tę samą konfigurację od początku do końca (zdalne kontrole statusu, WebChat i przekazywanie Voice Wake).

Runbook: [zdalny dostęp macOS](</pl/platforms/mac/remote>).

## Reguły bezpieczeństwa (remote/VPN)

Krótka wersja: **utrzymuj Gateway wyłącznie na loopback** , chyba że masz pewność, że potrzebujesz wiązania.

  * **Loopback + SSH/Tailscale Serve** to najbezpieczniejsza wartość domyślna (brak publicznej ekspozycji).
  * Zwykły tekst `ws://` jest domyślnie tylko dla loopback. Dla zaufanych sieci prywatnych ustaw `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` w procesie klienta jako awaryjne obejście. Nie ma odpowiednika w `openclaw.json`; musi to być środowisko procesu klienta nawiązującego połączenie WebSocket.
  * **Wiązania inne niż loopback** (`lan`/`tailnet`/`custom` albo `auto`, gdy loopback jest niedostępny) muszą używać uwierzytelniania gateway: tokena, hasła lub reverse proxy świadomego tożsamości z `gateway.auth.mode: "trusted-proxy"`.
  * `gateway.remote.token` / `.password` są źródłami poświadczeń klienta. Same **nie** konfigurują uwierzytelniania serwera.
  * Lokalne ścieżki wywołań mogą używać `gateway.remote.*` jako rozwiązania awaryjnego tylko wtedy, gdy `gateway.auth.*` jest nieustawione.
  * Jeśli `gateway.auth.token` / `gateway.auth.password` jest jawnie skonfigurowane przez SecretRef i nierozwiązane, rozwiązywanie kończy się zamknięciem dostępu (bez maskowania przez zdalne rozwiązanie awaryjne).
  * `gateway.remote.tlsFingerprint` przypina zdalny certyfikat TLS przy użyciu `wss://`.
  * **Tailscale Serve** może uwierzytelniać ruch Control UI/WebSocket przez nagłówki tożsamości, gdy `gateway.auth.allowTailscale: true`; punkty końcowe HTTP API nie używają tego uwierzytelniania nagłówkiem Tailscale i zamiast tego stosują normalny tryb uwierzytelniania HTTP gateway. Ten przepływ bez tokena zakłada, że host gateway jest zaufany. Ustaw go na `false`, jeśli chcesz wszędzie używać uwierzytelniania współdzielonym sekretem.
  * Uwierzytelnianie **Trusted-proxy** domyślnie oczekuje konfiguracji proxy świadomego tożsamości poza loopback. Reverse proxy na tym samym hoście przez loopback wymagają jawnego `gateway.auth.trustedProxy.allowLoopback = true`.
  * Traktuj kontrolę z przeglądarki jak dostęp operatora: tylko tailnet + celowe parowanie węzłów.


Szczegóły: [Bezpieczeństwo](</pl/gateway/security>).

### macOS: trwały tunel SSH przez LaunchAgent

Dla klientów macOS łączących się ze zdalnym gateway najprostsza trwała konfiguracja używa wpisu SSH `LocalForward` oraz LaunchAgent, aby utrzymać tunel przy życiu po restartach i awariach.

#### Krok 1: dodaj konfigurację SSH

Edytuj `~/.ssh/config`:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;    User &lt;REMOTE_USER&gt;    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Zastąp `&lt;REMOTE_IP&gt;` i `&lt;REMOTE_USER&gt;` swoimi wartościami.

#### Krok 2: skopiuj klucz SSH (jednorazowo)

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

#### Krok 3: skonfiguruj token gateway

Zapisz token w konfiguracji, aby przetrwał restarty:

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

#### Krok 4: utwórz LaunchAgent

Zapisz to jako `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

#### Krok 5: załaduj LaunchAgent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Tunel uruchomi się automatycznie przy logowaniu, zrestartuje po awarii i utrzyma przekierowany port jako aktywny.

#### Rozwiązywanie problemów

Sprawdź, czy tunel działa:

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

Zrestartuj tunel:

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

Zatrzymaj tunel:

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

Wpis konfiguracji | Co robi  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Przekierowuje lokalny port 18789 na zdalny port 18789  
`ssh -N` | SSH bez wykonywania zdalnych poleceń (tylko przekierowanie portów)  
`KeepAlive` | Automatycznie restartuje tunel, jeśli ulegnie awarii  
`RunAtLoad` | Uruchamia tunel, gdy LaunchAgent ładuje się przy logowaniu  
  
## Powiązane

  * [Tailscale](</pl/gateway/tailscale>)
  * [Uwierzytelnianie](</pl/gateway/authentication>)
  * [Konfiguracja zdalnego gateway](</pl/gateway/remote-gateway-readme>)


Was this useful?YesNo