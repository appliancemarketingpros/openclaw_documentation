---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/nl/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot is de AI-codeerassistent van GitHub. Het biedt toegang tot Copilot -modellen voor je GitHub-account en -abonnement. OpenClaw kan Copilot op twee verschillende manieren als modelprovider gebruiken.

## Twee manieren om Copilot in OpenClaw te gebruiken

### Ingebouwde provider (github-copilot)

Gebruik de native device-login-stroom om een GitHub-token te verkrijgen en wissel dit vervolgens in voor Copilot-API-tokens wanneer OpenClaw wordt uitgevoerd. Dit is het **standaard** en eenvoudigste pad, omdat VS Code niet vereist is.

* ### Voer de login-opdracht uit

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Je wordt gevraagd een URL te bezoeken en een eenmalige code in te voeren. Houd de terminal open totdat dit is voltooid.

* ### Stel een standaardmodel in

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Of in de configuratie:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Copilot Proxy-Plugin (copilot-proxy)

Gebruik de VS Code-extensie **Copilot Proxy** als lokale brug. OpenClaw communiceert met het `/v1`-endpoint van de proxy en gebruikt de modellenlijst die je daar configureert.

## Optionele vlaggen

Vlag | Beschrijving  
---|---  
`--yes` | Sla de bevestigingsprompt over  
`--set-default` | Pas ook het aanbevolen standaardmodel van de provider toe  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Niet-interactieve onboarding

Als je al een GitHub OAuth-toegangstoken voor Copilot hebt, importeer je dit tijdens headless installatie met `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Je kunt `--auth-choice` ook weglaten; het doorgeven van `--github-copilot-token` leidt de auth-keuze voor de GitHub Copilot-provider af. Als de vlag wordt weggelaten, valt onboarding terug op `COPILOT_GITHUB_TOKEN`, `GH_TOKEN` en daarna `GITHUB_TOKEN`. Gebruik `--secret-input-mode ref` met `COPILOT_GITHUB_TOKEN` ingesteld om een door de omgeving ondersteunde `tokenRef` op te slaan in plaats van platte tekst in `auth-profiles.json`.

Interactieve TTY vereist

De device-login-stroom vereist een interactieve TTY. Voer deze rechtstreeks uit in een terminal, niet in een niet-interactief script of CI-pipeline.

Modelbeschikbaarheid hangt af van je abonnement

De beschikbaarheid van Copilot-modellen hangt af van je GitHub-abonnement. Als een model wordt geweigerd, probeer dan een andere ID (bijvoorbeeld `github-copilot/gpt-4.1`).

Live catalogusverversing vanuit de Copilot-API

Zodra het auth-pad via device-login (of env-var) een GitHub-token heeft opgelost, ververst OpenClaw de modelcatalogus op aanvraag vanuit `${baseUrl}/models` (hetzelfde endpoint dat VS Code Copilot gebruikt), zodat de runtime per-account rechten en accurate contextvensters volgt zonder manifestwijzigingen. Nieuw gepubliceerde Copilot-modellen worden zichtbaar zonder OpenClaw-upgrade, en contextvensters weerspiegelen de echte limieten per model (bijv. 400k voor de gpt-5.x-serie, 1M voor de interne `claude-opus-*-1m`-varianten).

De meegeleverde statische catalogus blijft de zichtbare fallback wanneer discovery is uitgeschakeld, de gebruiker geen GitHub-authprofiel heeft, de tokenuitwisseling mislukt, of de HTTPS-aanroep naar `/models` een fout geeft. Om je af te melden en volledig te vertrouwen op de statische manifestcatalogus (offline / air-gapped scenario's):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Transportselectie

Claude-model-ID's gebruiken automatisch het Anthropic Messages-transport. GPT-, o-series- en Gemini-modellen blijven het OpenAI Responses-transport gebruiken. OpenClaw selecteert het juiste transport op basis van de modelreferentie.

Aanvraagcompatibiliteit

OpenClaw verzendt Copilot IDE-achtige aanvraagheaders op Copilot-transports, inclusief ingebouwde compaction, tool-result en vervolgrondes voor afbeeldingen. Het schakelt provider-level Responses-continuation voor Copilot niet in, tenzij dat gedrag is geverifieerd tegen de API van Copilot.

Volgorde voor het oplossen van omgevingsvariabelen

OpenClaw lost Copilot-auth op uit omgevingsvariabelen in de volgende prioriteitsvolgorde:

Prioriteit | Variabele | Opmerkingen  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Hoogste prioriteit, Copilot-specifiek  
2 | `GH_TOKEN` | GitHub CLI-token (fallback)  
3 | `GITHUB_TOKEN` | Standaard GitHub-token (laagste)  
  
Wanneer meerdere variabelen zijn ingesteld, gebruikt OpenClaw de variabele met de hoogste prioriteit. De device-login-stroom (`openclaw models auth login-github-copilot`) slaat zijn token op in de auth-profielopslag en heeft voorrang op alle omgevingsvariabelen.

Tokenopslag

De login slaat een GitHub-token op in de auth-profielopslag en wisselt dit in voor een Copilot-API-token wanneer OpenClaw wordt uitgevoerd. Je hoeft het token niet handmatig te beheren.

## Embeddings voor geheugenzoekopdrachten

GitHub Copilot kan ook dienen als embeddingprovider voor [geheugenzoekopdrachten](</nl/concepts/memory-search>). Als je een Copilot-abonnement hebt en bent ingelogd, kan OpenClaw dit gebruiken voor embeddings zonder aparte API-sleutel.

### Automatische detectie

Wanneer `memorySearch.provider` `"auto"` is (de standaard), wordt GitHub Copilot geprobeerd met prioriteit 15 -- na lokale embeddings maar vóór OpenAI en andere betaalde providers. Als er een GitHub-token beschikbaar is, ontdekt OpenClaw beschikbare embeddingmodellen vanuit de Copilot-API en kiest automatisch het beste model.

### Expliciete configuratie

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Hoe het werkt

  1. OpenClaw lost je GitHub-token op (uit env-vars of auth-profiel).
  2. Wisselt dit in voor een kortlevend Copilot-API-token.
  3. Bevraagt het Copilot-`/models`-endpoint om beschikbare embeddingmodellen te ontdekken.
  4. Kiest het beste model (geeft de voorkeur aan `text-embedding-3-small`).
  5. Verzendt embeddingaanvragen naar het Copilot-`/embeddings`-endpoint.


Modelbeschikbaarheid hangt af van je GitHub-abonnement. Als er geen embeddingmodellen beschikbaar zijn, slaat OpenClaw Copilot over en probeert de volgende provider.

## Gerelateerd

[**Modelselectie** Providers, modelreferenties en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**OAuth en auth** Auth-details en regels voor hergebruik van referenties. ](</nl/gateway/authentication>)

Was this useful?YesNo