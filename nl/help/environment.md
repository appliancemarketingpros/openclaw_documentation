---
title: Omgevingsvariabelen
source_url: https://docs.openclaw.ai/nl/help/environment
scraped_at: 2026-05-25
---

OpenClaw haalt omgevingsvariabelen op uit meerdere bronnen. De regel is: **bestaande waarden nooit overschrijven**.

## Prioriteit (hoogste → laagste)

  1. **Procesomgeving** (wat het Gateway-proces al heeft van de bovenliggende shell/daemon).
  2. **`.env` in de huidige werkmap** (dotenv-standaard; overschrijft niet).
  3. **Globale`.env`** op `~/.openclaw/.env` (ook bekend als `$OPENCLAW_STATE_DIR/.env`; overschrijft niet).
  4. **Configuratie-`env`-blok** in `~/.openclaw/openclaw.json` (alleen toegepast als het ontbreekt).
  5. **Optionele login-shell-import** (`env.shellEnv.enabled` of `OPENCLAW_LOAD_SHELL_ENV=1`), alleen toegepast voor ontbrekende verwachte sleutels.


Op nieuwe Ubuntu-installaties die de standaard statusmap gebruiken, behandelt OpenClaw ook `~/.config/openclaw/gateway.env` als compatibiliteitsfallback na de globale `.env`. Als beide bestanden bestaan en niet overeenkomen, behoudt OpenClaw `~/.openclaw/.env` en toont het een waarschuwing.

Als het configuratiebestand volledig ontbreekt, wordt stap 4 overgeslagen; shell-import wordt nog steeds uitgevoerd als die is ingeschakeld.

## Configuratie-`env`-blok

Twee gelijkwaardige manieren om inline omgevingsvariabelen in te stellen (beide overschrijven niet):

json5Copy code
[code]
    {  env: {    OPENROUTER_API_KEY: "sk-or-...",    vars: {      GROQ_API_KEY: "gsk-...",    },  },}
[/code]

## Shell-omgevingsimport

`env.shellEnv` voert je login-shell uit en importeert alleen **ontbrekende** verwachte sleutels:

json5Copy code
[code]
    {  env: {    shellEnv: {      enabled: true,      timeoutMs: 15000,    },  },}
[/code]

Equivalenten als omgevingsvariabelen:

  * `OPENCLAW_LOAD_SHELL_ENV=1`
  * `OPENCLAW_SHELL_ENV_TIMEOUT_MS=15000`


## Door runtime geïnjecteerde omgevingsvariabelen

OpenClaw injecteert ook contextmarkeringen in gespawnde onderliggende processen:

  * `OPENCLAW_SHELL=exec`: ingesteld voor opdrachten die via de `exec`-tool worden uitgevoerd.
  * `OPENCLAW_SHELL=acp`: ingesteld voor proces-spawns van de ACP-runtimebackend (bijvoorbeeld `acpx`).
  * `OPENCLAW_SHELL=acp-client`: ingesteld voor `openclaw acp client` wanneer dit het ACP-bridgeproces spawnt.
  * `OPENCLAW_SHELL=tui-local`: ingesteld voor lokale TUI-`!`-shellopdrachten.


Dit zijn runtimemarkeringen (geen vereiste gebruikersconfiguratie). Ze kunnen worden gebruikt in shell-/profiellogica om contextspecifieke regels toe te passen.

## Omgevingsvariabelen voor UI

  * `OPENCLAW_THEME=light`: forceer het lichte TUI-palet wanneer je terminal een lichte achtergrond heeft.
  * `OPENCLAW_THEME=dark`: forceer het donkere TUI-palet.
  * `COLORFGBG`: als je terminal dit exporteert, gebruikt OpenClaw de hint voor de achtergrondkleur om automatisch het TUI-palet te kiezen.


## Vervanging van omgevingsvariabelen in configuratie

Je kunt rechtstreeks naar omgevingsvariabelen verwijzen in stringwaarden van de configuratie met de syntaxis `${VAR_NAME}`:

json5Copy code
[code]
    {  models: {    providers: {      "vercel-gateway": {        apiKey: "${VERCEL_GATEWAY_API_KEY}",      },    },  },}
[/code]

Zie [Configuratie: vervanging van omgevingsvariabelen](</nl/gateway/configuration-reference#env-var-substitution>) voor alle details.

## Secret refs versus `${ENV}`-strings

OpenClaw ondersteunt twee patronen op basis van omgevingsvariabelen:

  * `${VAR}`-stringvervanging in configuratiewaarden.
  * SecretRef-objecten (`{ source: "env", provider: "default", id: "VAR" }`) voor velden die verwijzingen naar geheimen ondersteunen.


Beide worden tijdens activering opgelost vanuit de procesomgeving. Details over SecretRef zijn gedocumenteerd in [Beheer van geheimen](</nl/gateway/secrets>).

## Padgerelateerde omgevingsvariabelen

Variabele | Doel  
---|---  
`OPENCLAW_HOME` | Overschrijf de thuismap die wordt gebruikt voor alle interne padresolutie (`~/.openclaw/`, agentmappen, sessies, referenties). Nuttig wanneer OpenClaw als een toegewezen servicegebruiker draait.  
`OPENCLAW_STATE_DIR` | Overschrijf de statusmap (standaard `~/.openclaw`).  
`OPENCLAW_CONFIG_PATH` | Overschrijf het pad naar het configuratiebestand (standaard `~/.openclaw/openclaw.json`).  
`OPENCLAW_INCLUDE_ROOTS` | Padlijst van mappen waarin `$include`-directieven bestanden buiten de configuratiemap mogen oplossen (standaard: geen — `$include` is beperkt tot de configuratiemap). Tilde wordt uitgebreid.  
  
## Logboekregistratie

Variabele | Doel  
---|---  
`OPENCLAW_LOG_LEVEL` | Overschrijf het logniveau voor zowel bestand als console (bijv. `debug`, `trace`). Heeft voorrang op `logging.level` en `logging.consoleLevel` in de configuratie. Ongeldige waarden worden genegeerd met een waarschuwing.  
`OPENCLAW_DEBUG_MODEL_TRANSPORT` | Geef gerichte timingdiagnostiek voor modelverzoeken/-reacties uit op `info`-niveau zonder globale debuglogs in te schakelen.  
`OPENCLAW_DEBUG_MODEL_PAYLOAD` | Diagnostiek voor modelpayloads: `summary`, `tools` of `full-redacted`. `full-redacted` is begrensd en geredigeerd, maar kan prompt-/berichttekst bevatten.  
`OPENCLAW_DEBUG_SSE` | Streamingdiagnostiek: `events` voor timing van eerste/klaar, `peek` om de eerste vijf geredigeerde SSE-events op te nemen.  
`OPENCLAW_DEBUG_CODE_MODE` | Diagnostiek voor het modeloppervlak in code-modus, inclusief verbergen van provider-tools en afdwingen van alleen exec/wait.  
  
### `OPENCLAW_HOME`

Wanneer ingesteld, vervangt `OPENCLAW_HOME` de systeemthuismap (`$HOME` / `os.homedir()`) voor alle interne padresolutie. Dit maakt volledige bestandssysteemisolatie mogelijk voor headless serviceaccounts.

**Prioriteit:** `OPENCLAW_HOME` > `$HOME` > `USERPROFILE` > `os.homedir()`

**Voorbeeld** (macOS LaunchDaemon):

xmlCopy code
[code]
    <key>EnvironmentVariables</key><dict>  <key>OPENCLAW_HOME</key>  <string>/Users/user</string></dict>
[/code]

`OPENCLAW_HOME` kan ook worden ingesteld op een tilde-pad (bijv. `~/svc`), dat vóór gebruik wordt uitgebreid met `$HOME`.

## nvm-gebruikers: TLS-fouten met web_fetch

Als Node.js via **nvm** is geïnstalleerd (niet via de systeempackagebeheerder), gebruikt de ingebouwde `fetch()` de gebundelde CA-store van nvm, waarin moderne root-CA's kunnen ontbreken (ISRG Root X1/X2 voor Let's Encrypt, DigiCert Global Root G2, enz.). Hierdoor mislukt `web_fetch` met `"fetch failed"` op de meeste HTTPS-sites.

Op Linux detecteert OpenClaw nvm automatisch en past het de oplossing toe in de daadwerkelijke opstartomgeving:

  * `openclaw gateway install` schrijft `NODE_EXTRA_CA_CERTS` naar de systemd-serviceomgeving
  * het `openclaw` CLI-entrypoint voert zichzelf opnieuw uit met `NODE_EXTRA_CA_CERTS` ingesteld vóór het opstarten van Node


**Handmatige oplossing (voor oudere versies of directe`node ...`-starts):**

Exporteer de variabele voordat je OpenClaw start:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crtopenclaw gateway run
[/code]

Vertrouw er niet op dat je voor deze variabele alleen naar `~/.openclaw/.env` schrijft; Node leest `NODE_EXTRA_CA_CERTS` bij het opstarten van het proces.

## Verouderde omgevingsvariabelen

OpenClaw leest alleen `OPENCLAW_*`-omgevingsvariabelen. De verouderde voorvoegsels `CLAWDBOT_*` en `MOLTBOT_*` uit eerdere releases worden stilzwijgend genegeerd.

Als er bij het opstarten nog een van deze variabelen is ingesteld op het Gateway-proces, geeft OpenClaw een enkele Node-deprecationwaarschuwing (`OPENCLAW_LEGACY_ENV_VARS`) weer met de gedetecteerde voorvoegsels en het totale aantal. Hernoem elke waarde door het verouderde voorvoegsel te vervangen door `OPENCLAW_` (bijvoorbeeld `CLAWDBOT_GATEWAY_TOKEN` → `OPENCLAW_GATEWAY_TOKEN`); de oude namen hebben geen effect.

## Gerelateerd

  * [Gateway-configuratie](</nl/gateway/configuration>)
  * [FAQ: omgevingsvariabelen en .env-laden](</nl/help/faq#env-vars-and-env-loading>)
  * [Modellenoverzicht](</nl/concepts/models>)


Was this useful?YesNo