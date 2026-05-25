---
title: Railway
source_url: https://docs.openclaw.ai/nl/install/railway
scraped_at: 2026-05-25
---

# Railway

Implementeer OpenClaw op Railway met een one-click-template en open het via de web-Control UI. Dit is het eenvoudigste pad zonder terminal op de server: Railway voert de Gateway voor je uit.

## Snelle checklist (nieuwe gebruikers)

  1. Klik op **Deploy on Railway** (hieronder).
  2. Voeg een **Volume** toe dat is aangekoppeld op `/data`.
  3. Stel de vereiste **Variables** in (minimaal `OPENCLAW_GATEWAY_PORT` en `OPENCLAW_GATEWAY_TOKEN`).
  4. Schakel **HTTP Proxy** in op poort `8080`.
  5. Open `https://<your-railway-domain>/openclaw` en maak verbinding met het geconfigureerde gedeelde geheim. Deze template gebruikt standaard `OPENCLAW_GATEWAY_TOKEN`; als je dit vervangt door wachtwoordauthenticatie, gebruik dan in plaats daarvan dat wachtwoord.


## One-click-implementatie

[ Deploy on Railway ](<https://railway.com/deploy/clawdbot-railway-template>)

Zoek na de implementatie je openbare URL in **Railway → je service → Settings → Domains**.

Railway zal ofwel:

  * je een gegenereerd domein geven (vaak `https://<something>.up.railway.app`), of
  * je aangepaste domein gebruiken als je er een hebt gekoppeld.


Open daarna:

  * `https://<your-railway-domain>/openclaw` — Control UI


## Wat je krijgt

  * Gehoste OpenClaw Gateway + Control UI
  * Persistente opslag via Railway Volume (`/data`), zodat `openclaw.json`, `auth-profiles.json` per agent, kanaal-/providerstatus, sessies en workspace herimplementaties overleven


## Vereiste Railway-instellingen

### Openbaar netwerk

Schakel **HTTP Proxy** in voor de service.

  * Poort: `8080`


### Volume (vereist)

Koppel een volume aan op:

  * `/data`


### Variabelen

Stel deze variabelen in op de service:

  * `OPENCLAW_GATEWAY_PORT=8080` (vereist — moet overeenkomen met de poort in Openbaar netwerk)
  * `OPENCLAW_GATEWAY_TOKEN` (vereist; behandel als een beheerdersgeheim)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (aanbevolen)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (aanbevolen)


## Een kanaal verbinden

Gebruik de Control UI op `/openclaw` of voer `openclaw onboard` uit via de shell van Railway voor instructies voor kanaalconfiguratie:

  * [Telegram](</nl/channels/telegram>) (snelst — alleen een bottoken)
  * [Discord](</nl/channels/discord>)
  * [Alle kanalen](</nl/channels>)


## Back-ups en migratie

Exporteer je status, configuratie, auth-profielen en workspace:

bashCopy code
[code]
    openclaw backup create
[/code]

Dit maakt een draagbaar back-uparchief met OpenClaw-status plus elke geconfigureerde workspace. Zie [Back-up](</nl/cli/backup>) voor details.

## Volgende stappen

  * Stel berichtenkanalen in: [Kanalen](</nl/channels>)
  * Configureer de Gateway: [Gateway-configuratie](</nl/gateway/configuration>)
  * Houd OpenClaw up-to-date: [Bijwerken](</nl/install/updating>)


Was this useful?YesNo