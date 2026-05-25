---
title: Introductie (CLI)
source_url: https://docs.openclaw.ai/nl/start/wizard
scraped_at: 2026-05-25
---

CLI-onboarding is de **aanbevolen** manier om OpenClaw in te stellen op macOS, Linux of Windows (via WSL2; sterk aanbevolen). Het configureert een lokale Gateway of een externe Gateway-verbinding, plus kanalen, skills en standaardinstellingen voor de werkruimte in één begeleide flow.

bashCopy code
[code]
    openclaw onboard
[/code]

Om later opnieuw te configureren:

bashCopy code
[code]
    openclaw configureopenclaw agents add <name>
[/code]

## QuickStart versus Geavanceerd

Onboarding begint met **QuickStart** (standaardinstellingen) versus **Geavanceerd** (volledige controle).

### QuickStart (standaardinstellingen)

  * Lokale Gateway (loopback)
  * Standaardwerkruimte (of bestaande werkruimte)
  * Gateway-poort **18789**
  * Gateway-auth **Token** (automatisch gegenereerd, zelfs op loopback)
  * Standaard toolbeleid voor nieuwe lokale installaties: `tools.profile: "coding"` (bestaand expliciet profiel blijft behouden)
  * Standaard DM-isolatie: lokale onboarding schrijft `session.dmScope: "per-channel-peer"` wanneer niet ingesteld. Details: [CLI-installatiereferentie](</nl/start/wizard-cli-reference#outputs-and-internals>)
  * Tailscale-blootstelling **Uit**
  * Telegram- en WhatsApp-DM's staan standaard op **allowlist** (je wordt om je telefoonnummer gevraagd)


### Geavanceerd (volledige controle)

  * Toont elke stap (modus, werkruimte, Gateway, kanalen, daemon, skills).


## Wat onboarding configureert

**Lokale modus (standaard)** leidt je door deze stappen:

  1. **Model/Auth** — kies een ondersteunde provider/auth-flow (API-sleutel, OAuth of providerspecifieke handmatige auth), inclusief Custom Provider (OpenAI-compatibel, Anthropic-compatibel of Unknown automatische detectie). Kies een standaardmodel. Beveiligingsopmerking: als deze agent tools gaat uitvoeren of webhook-/hooks-inhoud gaat verwerken, geef dan de voorkeur aan het sterkste beschikbare model van de nieuwste generatie en houd het toolbeleid strikt. Zwakkere/oudere niveaus zijn makkelijker te prompt-injecteren. Voor niet-interactieve runs slaat `--secret-input-mode ref` door env ondersteunde refs op in auth-profielen in plaats van platte API-sleutelwaarden. In niet-interactieve `ref`-modus moet de provider-env-var zijn ingesteld; inline sleutelvlaggen doorgeven zonder die env-var faalt direct. In interactieve runs kun je met de modus voor geheime referenties verwijzen naar een omgevingsvariabele of een geconfigureerde provider-ref (`file` of `exec`), met snelle preflightvalidatie vóór het opslaan. Voor Anthropic biedt interactieve onboarding/configuratie **Anthropic Claude CLI** als het voorkeurs lokale pad en **Anthropic API key** als het aanbevolen productiepad. Anthropic setup-token blijft ook beschikbaar als ondersteund token-auth-pad.
  2. **Werkruimte** — locatie voor agentbestanden (standaard `~/.openclaw/workspace`). Plaatst bootstrap-bestanden.
  3. **Gateway** — poort, bind-adres, auth-modus, Tailscale-blootstelling. Kies in interactieve tokenmodus de standaard opslag van tokens in platte tekst of kies voor SecretRef. Niet-interactief token-SecretRef-pad: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  4. **Kanalen** — ingebouwde en gebundelde chatkanalen zoals iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, QQ Bot, Signal, Slack, Telegram, WhatsApp en meer.
  5. **Daemon** — installeert een LaunchAgent (macOS), systemd-gebruikerseenheid (Linux/WSL2) of native Windows Scheduled Task met per-gebruiker Startup-mapfallback. Als token-auth een token vereist en `gateway.auth.token` door SecretRef wordt beheerd, valideert daemoninstallatie dit, maar blijft het opgeloste token niet bewaard in metadata van de supervisorserviceomgeving. Als token-auth een token vereist en de geconfigureerde token-SecretRef niet kan worden opgelost, wordt daemoninstallatie geblokkeerd met bruikbare begeleiding. Als zowel `gateway.auth.token` als `gateway.auth.password` zijn geconfigureerd en `gateway.auth.mode` niet is ingesteld, wordt daemoninstallatie geblokkeerd totdat de modus expliciet is ingesteld.
  6. **Health check** — start de Gateway en controleert of deze actief is.
  7. **Skills** — installeert aanbevolen skills en optionele afhankelijkheden.


**Externe modus** configureert alleen de lokale client om verbinding te maken met een Gateway elders. Het installeert of wijzigt **niets** op de externe host.

## Nog een agent toevoegen

Gebruik `openclaw agents add <name>` om een afzonderlijke agent te maken met een eigen werkruimte, sessies en auth-profielen. Uitvoeren zonder `--workspace` start onboarding.

Wat het instelt:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Opmerkingen:

  * Standaardwerkruimten volgen `~/.openclaw/workspace-<agentId>`.
  * Voeg `bindings` toe om inkomende berichten te routeren (onboarding kan dit doen).
  * Niet-interactieve vlaggen: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Volledige referentie

Zie voor gedetailleerde stapsgewijze uitsplitsingen en configuratie-uitvoer [CLI-installatiereferentie](</nl/start/wizard-cli-reference>). Zie voor niet-interactieve voorbeelden [CLI-automatisering](</nl/start/wizard-cli-automation>). Zie voor de diepere technische referentie, inclusief RPC-details, [Onboardingreferentie](</nl/reference/wizard>).

## Gerelateerde docs

  * CLI-opdrachtreferentie: [`openclaw onboard`](</nl/cli/onboard>)
  * Onboarding-overzicht: [Onboarding-overzicht](</nl/start/onboarding-overview>)
  * macOS-app-onboarding: [Onboarding](</nl/start/onboarding>)
  * Eerste-runritueel voor agent: [Agent Bootstrapping](</nl/start/bootstrapping>)


Was this useful?YesNo