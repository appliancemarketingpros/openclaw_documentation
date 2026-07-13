---
title: Kluis-SecretRefs
source_url: https://docs.openclaw.ai/nl/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# Vault-SecretRefs

Met de gebundelde Vault-Plugin kan OpenClaw bij het opstarten en opnieuw laden van de Gateway `exec`-SecretRefs ophalen uit HashiCorp Vault. OpenClaw slaat Vault-verwijzingen op in de configuratie, bewaart opgehaalde waarden in de geheugensnapshot met geheimen en schrijft de opgehaalde API-sleutels niet terug naar `openclaw.json`.

Gebruik dit wanneer je Vault al gebruikt of sleutels van modelproviders buiten de OpenClaw-configuratiebestanden wilt bewaren. Zie [Geheimenbeheer](</nl/gateway/secrets>) voor het runtimemodel van SecretRef.

## Voordat je begint

Je hebt het volgende nodig:

  * OpenClaw met de gebundelde `vault`-Plugin beschikbaar
  * een bereikbare Vault-server
  * Vault-verificatie die een clienttoken kan verstrekken met leestoegang tot de geheime paden die OpenClaw moet ophalen
  * de omgeving die de Gateway start, moet `VAULT_ADDR` bevatten en daarnaast `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` met `VAULT_TOKEN_FILE`, of een geconfigureerde JWT-/Kubernetes-aanmelding


De resolver communiceert vanuit Node via HTTP met Vault. De Gateway heeft de Vault-CLI niet nodig om SecretRefs op te halen.

Schakel de gebundelde Plugin in voordat je de `openclaw vault`-opdrachten uitvoert:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Een providersleutel opslaan in Vault

OpenClaw gebruikt standaard KV v2, gekoppeld op `secret`, overeenkomstig de voorbeelden voor de ontwikkelserver van Vault. Stel voor een productieomgeving van Vault `OPENCLAW_VAULT_KV_MOUNT` in op het daadwerkelijke KV-koppelpad voordat je SecretRef-id's maakt. Met de standaardinstellingen van OpenClaw leest deze SecretRef-id:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

dit Vault-veld:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Je kunt dit bijvoorbeeld met de Vault-CLI maken:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Gebruik voor OpenClaw een clienttoken met een beperkt bereik, geen roottoken. Voor de standaardindeling van KV v2 ziet een minimaal beleid voor sleutels van modelproviders er als volgt uit:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Vault zichtbaar maken voor de Gateway

Exporteer voor een lokale Gateway zonder container de Vault-instellingen in dezelfde shell waarin OpenClaw wordt gestart. De standaardverificatiemethode leest een Vault-clienttoken uit `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Als Vault Agent een tokenbestand wegschrijft, gebruik je verificatie via een tokenbestand:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Voor een Vault-server die is ondertekend door een privé-CA installeer je die CA in het vertrouwensarchief van de host en schakel je het systeemvertrouwen van Node in:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Of geef je rechtstreeks een PEM-bundel op:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Deze variabelen moeten aanwezig zijn wanneer OpenClaw wordt gestart. De Vault-Plugin geeft ze door aan het resolverproces.

Gebruik voor niet-interactieve JWT-verificatie een JWT-bestand van de werklast en een Vault-rol van het type `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

Het JWT-bestand moet een geprojecteerd werklasttoken zijn, zoals een token voor een Kubernetes-serviceaccount met een doelgroep die door de Vault-rol wordt geaccepteerd. Interactieve OIDC-aanmelding via de browser is nuttig voor mensen, maar de Gateway-runtime vereist niet-interactieve JWT-aanmelding of een tokenbestand.

Gebruik `kubernetes` voor de Kubernetes-verificatiemethode van Vault. Dit is bedoeld voor Gateways die als Pods worden uitgevoerd; het standaardkoppelpunt is `kubernetes` en het standaard-JWT-bestand is het gebruikelijke tokenpad van het serviceaccount:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Stel `OPENCLAW_VAULT_AUTH_MOUNT` alleen in wanneer Kubernetes-verificatie in Vault ergens anders dan op `auth/kubernetes` is gekoppeld. Stel `OPENCLAW_VAULT_JWT_FILE` alleen in wanneer het token van het serviceaccount naar een aangepast pad wordt geprojecteerd.

Optionele instellingen:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Controleer wat de huidige shell kan zien:

bashCopy code
[code]
    openclaw vault status
[/code]

Wanneer meer dan één door Vault ondersteunde geheimenprovider is geconfigureerd, selecteer je er een op alias:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` geeft `VAULT_TOKEN` nooit weer; de opdracht meldt alleen of het token, het tokenbestand en het JWT-bestand zijn ingesteld.

## Een SecretRef-plan genereren en toepassen

Maak een plan dat de API-sleutel van de modelprovider OpenRouter aan Vault koppelt:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Pas het plan toe en verifieer het:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Gebruik `--allow-exec`, omdat de Vault-Plugin geheimen ophaalt via een door OpenClaw beheerde `exec`-SecretRef-provider.

Als de Gateway nog niet actief is, start je deze na het toepassen van het plan op de normale manier in plaats van `openclaw secrets reload` uit te voeren.

## Meer providersleutels configureren

Ingebouwde snelkoppelingen:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Meerdere providersleutels in één plan:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Gebruik `--provider-key` voor gebundelde providers zonder snelkoppelingen of voor reeds geconfigureerde OpenAI-compatibele en aangepaste modelproviders:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Elke `--provider-key <provider=id>` schrijft een SecretRef naar `models.providers.<provider>.apiKey`. Voor aangepaste providers worden de instellingen `baseUrl`, `api` en `models` van de provider niet gemaakt; configureer die eerst.

Gebruik `--target <path=id>` voor elk bekend SecretRef-doelpad:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Doelpaden zonder voorvoegsel zijn van toepassing op `openclaw.json`. Gebruik `auth-profiles:<agentId>:<path>` voor bestaande doelen in `auth-profiles.json`. Het doelpad moet een geregistreerd OpenClaw-SecretRef-doel zijn. De installatieopdracht maakt geen willekeurige benoemde geheimen in OpenClaw; Vault blijft de opslagplaats voor geheimen en OpenClaw slaat SecretRefs alleen op in ondersteunde configuratievelden.

## Indeling van SecretRef-id's

Vault-SecretRef-id's gebruiken deze conventie:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Voorbeelden:

SecretRef-id | Standaard Vault-leespad voor KV v2 | Geretourneerd veld  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Het geretourneerde Vault-veld moet een tekenreeks zijn.

Stel voor KV v1 het volgende in:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Vervolgens leest `providers/openrouter/apiKey`:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Wat OpenClaw opslaat

Bij het toepassen van een Vault-installatieplan wordt een door de Plugin beheerde provider opgeslagen:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Referentievelden verwijzen naar die provider:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

De opgehaalde waarde bevindt zich alleen in de actieve runtimesnapshot met geheimen.

## Containers en beheerde implementaties

Gateways in containers gebruiken nog steeds dezelfde Plugin- en SecretRef-configuratie. De container moet het volgende ontvangen:

  * `VAULT_ADDR`
  * één verificatiebron: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` plus `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` plus `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` en `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` plus `OPENCLAW_VAULT_AUTH_ROLE`; overschrijf desgewenst `OPENCLAW_VAULT_AUTH_MOUNT` of `OPENCLAW_VAULT_JWT_FILE`
  * optioneel `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` en `OPENCLAW_VAULT_KV_VERSION`


Geef bij gebruik van Kubernetes de voorkeur aan `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` wanneer Kubernetes-verificatie voor het cluster in Vault is geconfigureerd. Gebruik `OPENCLAW_VAULT_AUTH_METHOD=jwt` alleen wanneer Vault is geconfigureerd om het cluster als een algemene JWT-/OIDC-uitgever te behandelen. Beide opties zijn beter dan een langlevend Vault-token in een Kubernetes Secret. Implementaties met een Vault Agent-sidecar of -injector kunnen in plaats daarvan `token_file` gebruiken.

Houd voor Vault-configuraties met meerdere tenants de tenantroutering in het Vault-beleid en de implementatieconfiguratie. OpenClaw vereist geen vast koppelpunt, vaste rol of vast pad: elke Gateway-omgeving kan een eigen `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` en eigen SecretRef-id's instellen. Als één gedeelde Gateway tegelijkertijd geheimen voor verschillende Vault-gebruikers moet ophalen, gebruik je handmatig geconfigureerde `exec`-providers die afzonderlijke verificatieomgevingen omvatten, of verdeel je tenants over Gateway-omgevingen met afzonderlijke Vault-omgevingsvariabelen.

## Gerelateerd

  * [Geheimenbeheer](</nl/gateway/secrets>)
  * [`openclaw secrets`](</nl/cli/secrets>)
  * [Plugin-inventaris](</nl/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue