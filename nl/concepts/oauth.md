---
title: OAuth
source_url: https://docs.openclaw.ai/nl/concepts/oauth
scraped_at: 2026-05-25
---

OpenClaw ondersteunt "abonnementsauthenticatie" via OAuth voor providers die dit aanbieden (met name **OpenAI Codex (ChatGPT OAuth)**). Voor Anthropic is de praktische verdeling nu:

  * **Anthropic API-sleutel** : normale facturering voor de Anthropic API
  * **Anthropic Claude CLI / abonnementsauthenticatie binnen OpenClaw** : Anthropic-medewerkers hebben ons verteld dat dit gebruik weer is toegestaan


OpenAI Codex OAuth wordt expliciet ondersteund voor gebruik in externe tools zoals OpenClaw. Deze pagina legt uit:

Voor Anthropic in productie is authenticatie met API-sleutel de veiligere aanbevolen route.

  * hoe de OAuth-**tokenuitwisseling** werkt (PKCE)
  * waar tokens worden **opgeslagen** (en waarom)
  * hoe je **meerdere accounts** afhandelt (profielen + overschrijvingen per sessie)


OpenClaw ondersteunt ook **provider-plugins** die hun eigen OAuth- of API-sleutel- flows meeleveren. Voer ze uit via:

bashCopy code
[code]
    openclaw models auth login --provider <id>
[/code]

## De tokenopvang (waarom die bestaat)

OAuth-providers maken vaak een **nieuw vernieuwingstoken** aan tijdens login- of vernieuwingsflows. Sommige providers (of OAuth-clients) kunnen oudere vernieuwingstokens ongeldig maken wanneer er een nieuw token voor dezelfde gebruiker/app wordt uitgegeven.

Praktisch symptoom:

  * je logt in via OpenClaw _en_ via Claude Code / Codex CLI → een van beide wordt later willekeurig "uitgelogd"


Om dat te verminderen behandelt OpenClaw `auth-profiles.json` als een **tokenopvang** :

  * de runtime leest referenties vanaf **één plek**
  * we kunnen meerdere profielen behouden en ze deterministisch routeren
  * hergebruik van externe CLI is providerspecifiek: Codex CLI kan een leeg `openai-codex:default`-profiel initialiseren, maar zodra OpenClaw een lokaal OAuth-profiel heeft, is het lokale vernieuwingstoken canoniek; andere integraties kunnen extern beheerd blijven en hun CLI-authenticatieopslag opnieuw lezen
  * status- en opstartpaden die de geconfigureerde providerset al kennen, beperken externe CLI-detectie tot die set, zodat een niet-gerelateerde CLI-loginopslag niet wordt onderzocht voor een setup met één provider


## Opslag (waar tokens staan)

Geheimen worden opgeslagen in authenticatieopslag van agents:

  * Authenticatieprofielen (OAuth + API-sleutels + optionele refs op waardeniveau): `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * Compatibiliteitsbestand voor legacy: `~/.openclaw/agents/<agentId>/agent/auth.json` (statische `api_key`-items worden opgeschoond wanneer ze worden gevonden)


Legacy-bestand alleen voor import (nog steeds ondersteund, maar niet de hoofdopslag):

  * `~/.openclaw/credentials/oauth.json` (bij eerste gebruik geïmporteerd in `auth-profiles.json`)


Al het bovenstaande respecteert ook `$OPENCLAW_STATE_DIR` (overschrijving van de statusmap). Volledige referentie: [/gateway/configuration](</nl/gateway/configuration-reference#auth-storage>)

Zie [Geheimenbeheer](</nl/gateway/secrets>) voor statische geheime refs en activeringsgedrag van runtimesnapshots.

Wanneer een secundaire agent geen lokaal authenticatieprofiel heeft, gebruikt OpenClaw read-through overerving vanuit de standaard-/hoofdagentopslag. Het kloont de `auth-profiles.json` van de hoofdagent niet bij het lezen. OAuth-vernieuwingstokens zijn extra gevoelig: normale kopieerflows slaan ze standaard over omdat sommige providers vernieuwingstokens na gebruik roteren of ongeldig maken. Configureer een aparte OAuth-login voor een agent wanneer die een onafhankelijk account nodig heeft.

## Compatibiliteit met Anthropic legacy-tokens

OpenClaw stelt Anthropic setup-token ook beschikbaar als ondersteund token-authenticatiepad, maar geeft nu de voorkeur aan hergebruik van Claude CLI en `claude -p` wanneer beschikbaar.

## Migratie naar Anthropic Claude CLI

OpenClaw ondersteunt hergebruik van Anthropic Claude CLI weer. Als je al een lokale Claude-login op de host hebt, kan onboarding/configuratie die direct hergebruiken.

## OAuth-uitwisseling (hoe login werkt)

OpenClaw's interactieve loginflows zijn geïmplementeerd in `@earendil-works/pi-ai` en gekoppeld aan de wizards/commando's.

### Anthropic setup-token

Flowvorm:

  1. start Anthropic setup-token of paste-token vanuit OpenClaw
  2. OpenClaw slaat de resulterende Anthropic-referentie op in een authenticatieprofiel
  3. modelselectie blijft op `anthropic/...`
  4. bestaande Anthropic-authenticatieprofielen blijven beschikbaar voor rollback-/volgordebeheer


### OpenAI Codex (ChatGPT OAuth)

OpenAI Codex OAuth wordt expliciet ondersteund voor gebruik buiten de Codex CLI, inclusief OpenClaw-workflows.

Flowvorm (PKCE):

  1. genereer PKCE verifier/challenge + willekeurige `state`
  2. open `https://auth.openai.com/oauth/authorize?...`
  3. probeer de callback op te vangen op `http://127.0.0.1:1455/auth/callback`
  4. als callback niet kan binden (of je werkt remote/headless), plak dan de redirect-URL/code
  5. wissel uit bij `https://auth.openai.com/oauth/token`
  6. extraheer `accountId` uit het toegangstoken en sla `{ access, refresh, expires, accountId }` op


Wizardpad is `openclaw onboard` → authenticatiekeuze `openai-codex`.

## Vernieuwen + verlopen

Profielen slaan een `expires`-tijdstempel op.

Tijdens runtime:

  * als `expires` in de toekomst ligt → gebruik het opgeslagen toegangstoken
  * als het verlopen is → vernieuw (onder een bestandslock) en overschrijf de opgeslagen referenties
  * als een secundaire agent een overgeërfd OAuth-profiel van de hoofdagent leest, schrijft vernieuwen terug naar de hoofdagentopslag in plaats van het vernieuwingstoken naar de opslag van de secundaire agent te kopiëren
  * uitzondering: sommige externe CLI-referenties blijven extern beheerd; OpenClaw leest die CLI-authenticatieopslagen opnieuw in plaats van gekopieerde vernieuwingstokens te verbruiken. Codex CLI-bootstrap is bewust smaller: die seedt een leeg `openai-codex:default`-profiel, waarna door OpenClaw beheerde vernieuwingen het lokale profiel canoniek houden.


De vernieuwingsflow is automatisch; meestal hoef je tokens niet handmatig te beheren.

## Meerdere accounts (profielen) + routering

Twee patronen:

### 1) Aanbevolen: aparte agents

Als je wilt dat "persoonlijk" en "werk" nooit met elkaar interacteren, gebruik dan geïsoleerde agents (aparte sessies + referenties + workspace):

bashCopy code
[code]
    openclaw agents add workopenclaw agents add personal
[/code]

Configureer daarna authenticatie per agent (wizard) en routeer chats naar de juiste agent.

### 2) Geavanceerd: meerdere profielen in één agent

`auth-profiles.json` ondersteunt meerdere profiel-ID's voor dezelfde provider.

Kies welk profiel wordt gebruikt:

  * globaal via configuratievolgorde (`auth.order`)
  * per sessie via `/model ...@<profileId>`


Voorbeeld (sessie-overschrijving):

  * `/model Opus@anthropic:work`


Hoe je ziet welke profiel-ID's bestaan:

  * `openclaw channels list --json` (toont `auth[]`)


Gerelateerde documentatie:

  * [Modelfailover](</nl/concepts/model-failover>) (rotatie- en cooldownregels)
  * [Slash-commando's](</nl/tools/slash-commands>) (commandosurface)


## Gerelateerd

  * [Authenticatie](</nl/gateway/authentication>) \- overzicht van authenticatie voor modelproviders
  * [Geheimen](</nl/gateway/secrets>) \- opslag van referenties en SecretRef
  * [Configuratiereferentie](</nl/gateway/configuration-reference#auth-storage>) \- authenticatieconfiguratiesleutels


Was this useful?YesNo