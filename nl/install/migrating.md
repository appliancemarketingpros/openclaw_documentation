---
title: Migratiegids
source_url: https://docs.openclaw.ai/nl/install/migrating
scraped_at: 2026-05-25
---

OpenClaw ondersteunt drie migratiepaden: importeren vanuit een ander agentsysteem, een bestaande installatie naar een nieuwe machine verplaatsen en een Plugin ter plekke upgraden.

## Importeren vanuit een ander agentsysteem

Gebruik de meegeleverde migratieproviders om instructies, MCP-servers, Skills, modelconfiguratie en (opt-in) API-sleutels naar OpenClaw te brengen. Plannen worden vooraf bekeken voordat er iets verandert, geheimen worden in rapporten geredigeerd en toepassen wordt ondersteund door een geverifieerde back-up.

[**Migreren vanuit Claude** Importeer de status van Claude Code en Claude Desktop, inclusief `CLAUDE.md`, MCP-servers, Skills en projectopdrachten. ](</nl/install/migrating-claude>) [**Migreren vanuit Hermes** Importeer Hermes-configuratie, providers, MCP-servers, geheugen, Skills en ondersteunde `.env`-sleutels. ](</nl/install/migrating-hermes>)

Het CLI-ingangspunt is [`openclaw migrate`](</nl/cli/migrate>). Onboarding kan ook migratie aanbieden wanneer het een bekende bron detecteert (`openclaw onboard --flow import`).

## OpenClaw naar een nieuwe machine verplaatsen

Kopieer de **statusdirectory** (standaard `~/.openclaw/`) en je **workspace** om het volgende te behouden:

  * **Configuratie** — `openclaw.json` en alle gateway-instellingen.
  * **Authenticatie** — `auth-profiles.json` per agent (API-sleutels plus OAuth), plus eventuele kanaal- of providerstatus onder `credentials/`.
  * **Sessies** — gespreksgeschiedenis en agentstatus.
  * **Kanaalstatus** — WhatsApp-login, Telegram-sessie en vergelijkbare gegevens.
  * **Workspace-bestanden** — `MEMORY.md`, `USER.md`, Skills en prompts.


### Migratiestappen

* ### Stop de Gateway en maak een back-up

Stop op de **oude** machine de Gateway zodat bestanden niet tijdens het kopiëren veranderen, en archiveer daarna:

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

Als je meerdere profielen gebruikt (bijvoorbeeld `~/.openclaw-work`), archiveer elk profiel afzonderlijk.

* ### Installeer OpenClaw op de nieuwe machine

[Installeer](</nl/install>) de CLI (en Node indien nodig) op de nieuwe machine. Het is prima als onboarding een nieuwe `~/.openclaw/` aanmaakt. Je overschrijft die hierna.

* ### Kopieer de statusdirectory en workspace

Zet het archief over via `scp`, `rsync -a` of een externe schijf, en pak het daarna uit:

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

Zorg dat verborgen directory's zijn meegenomen en dat het bestandseigendom overeenkomt met de gebruiker die de Gateway zal uitvoeren.

* ### Voer doctor uit en verifieer

Voer op de nieuwe machine [Doctor](</nl/gateway/doctor>) uit om configuratiemigraties toe te passen en services te repareren:

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

Als Telegram of Discord de standaard env-terugval gebruikt (`TELEGRAM_BOT_TOKEN` of `DISCORD_BOT_TOKEN`), controleer dan of de gemigreerde statusdirectory `.env` die sleutels bevat zonder de geheime waarden af te drukken:

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

`openclaw doctor` waarschuwt ook wanneer een ingeschakeld standaard Telegram- of Discord-account geen geconfigureerd token heeft en de overeenkomende env-variabele niet beschikbaar is voor het doctor-proces.

### Veelvoorkomende valkuilen

Profiel- of statusdirectory komt niet overeen

Als de oude Gateway `--profile` of `OPENCLAW_STATE_DIR` gebruikte en de nieuwe niet, lijken kanalen uitgelogd en zijn sessies leeg. Start de Gateway met hetzelfde profiel of dezelfde statusdirectory die je hebt gemigreerd, en voer daarna `openclaw doctor` opnieuw uit.

Alleen openclaw.json kopiëren

Het configuratiebestand alleen is niet genoeg. Modelauthenticatieprofielen staan onder `agents/<agentId>/agent/auth-profiles.json`, en kanaal- en providerstatus staat onder `credentials/`. Migreer altijd de **volledige** statusdirectory.

Machtigingen en eigendom

Als je als root hebt gekopieerd of van gebruiker bent gewisseld, kan de Gateway mogelijk geen inloggegevens lezen. Zorg dat de statusdirectory en workspace eigendom zijn van de gebruiker die de Gateway uitvoert.

Externe modus

Als je UI naar een **externe** Gateway verwijst, beheert de externe host de sessies en workspace. Migreer de Gateway-host zelf, niet je lokale laptop. Zie [FAQ](</nl/help/faq#where-things-live-on-disk>).

Geheimen in back-ups

De statusdirectory bevat authenticatieprofielen, kanaalinloggegevens en andere providerstatus. Sla back-ups versleuteld op, vermijd onveilige overdrachtskanalen en roteer sleutels als je blootstelling vermoedt.

### Verificatiechecklist

Bevestig op de nieuwe machine:

  * [ ] `openclaw status` toont dat de Gateway draait.
  * [ ] Kanalen zijn nog steeds verbonden (opnieuw koppelen is niet nodig).
  * [ ] Het dashboard opent en toont bestaande sessies.
  * [ ] Workspace-bestanden (geheugen, configuraties) zijn aanwezig.


## Een Plugin ter plekke upgraden

Ter plekke uitgevoerde Plugin-upgrades behouden dezelfde Plugin-id en configuratiesleutels, maar kunnen status op schijf naar de huidige indeling verplaatsen. Plugin-specifieke upgradehandleidingen staan naast hun kanalen:

  * [Matrix-migratie](</nl/channels/matrix-migration>): herstelbeperkingen voor versleutelde status, automatisch snapshotgedrag en handmatige herstelopdrachten.


## Gerelateerd

  * [`openclaw migrate`](</nl/cli/migrate>): CLI-referentie voor imports tussen systemen.
  * [Installatieoverzicht](</nl/install>): alle installatiemethoden.
  * [Doctor](</nl/gateway/doctor>): gezondheidscontrole na migratie.
  * [De-installeren](</nl/install/uninstall>): OpenClaw netjes verwijderen.


Was this useful?YesNo