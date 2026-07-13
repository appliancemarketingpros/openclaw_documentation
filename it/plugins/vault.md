---
title: SecretRef del vault
source_url: https://docs.openclaw.ai/it/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# SecretRef di Vault

Il Plugin Vault incluso consente a OpenClaw di risolvere le SecretRef `exec` da HashiCorp Vault all'avvio del Gateway e durante il ricaricamento. OpenClaw memorizza i riferimenti a Vault nella configurazione, mantiene i valori risolti nell'istantanea dei segreti in memoria e non riscrive le chiavi API risolte in `openclaw.json`.

Usa questa soluzione se utilizzi già Vault o vuoi conservare le chiavi dei provider di modelli al di fuori dei file di configurazione di OpenClaw. Per il modello di runtime delle SecretRef, consulta [Gestione dei segreti](</it/gateway/secrets>).

## Prima di iniziare

Sono necessari:

  * OpenClaw con il plugin `vault` incluso disponibile
  * un server Vault raggiungibile
  * un'autenticazione Vault in grado di generare un token client con accesso in lettura ai percorsi dei segreti che OpenClaw deve risolvere
  * l'ambiente che avvia il Gateway deve includere `VAULT_ADDR` e uno tra `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` con `VAULT_TOKEN_FILE` oppure un accesso JWT/Kubernetes configurato


Il resolver comunica con Vault tramite HTTP da Node. Il Gateway non richiede la CLI di Vault per risolvere le SecretRef.

Abilita il plugin incluso prima di eseguire i comandi `openclaw vault`:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Archiviare una chiave di provider in Vault

Per impostazione predefinita, OpenClaw usa KV v2 montato in `secret`, in linea con gli esempi del server di sviluppo Vault. Per Vault in produzione, imposta `OPENCLAW_VAULT_KV_MOUNT` sul percorso di montaggio KV effettivo prima di creare gli ID SecretRef. Con le impostazioni predefinite di OpenClaw, questo ID SecretRef:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

legge questo campo Vault:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Un modo per crearlo con la CLI di Vault è:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Usa per OpenClaw un token client con ambito limitato, non un token root. Per la struttura KV v2 predefinita, una policy minima per le chiavi dei provider di modelli è simile alla seguente:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Rendere Vault visibile al Gateway

Per un Gateway locale non containerizzato, esporta le impostazioni di Vault nella stessa shell che avvia OpenClaw. Il metodo di autenticazione predefinito legge un token client Vault da `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Se Vault Agent scrive un file sink del token, usa l'autenticazione tramite file del token:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Per un server Vault firmato da una CA privata, installa la CA nell'archivio di attendibilità dell'host e abilita l'attendibilità di sistema di Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Oppure fornisci direttamente un bundle PEM:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Queste variabili devono essere presenti all'avvio di OpenClaw. Il Plugin Vault le inoltra al proprio processo resolver.

Per l'autenticazione JWT non interattiva, usa un file JWT del carico di lavoro e un ruolo Vault di tipo `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

Il file JWT dovrebbe essere un token del carico di lavoro proiettato, ad esempio un token dell'account di servizio Kubernetes con un destinatario accettato dal ruolo Vault. L'accesso interattivo OIDC tramite browser è utile per gli utenti, ma il runtime del Gateway richiede un accesso JWT non interattivo o un file del token.

Per il metodo di autenticazione Kubernetes di Vault, usa `kubernetes`. È destinato ai Gateway eseguiti come Pod; il montaggio predefinito è `kubernetes` e il file JWT predefinito è il percorso standard del token dell'account di servizio:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Imposta `OPENCLAW_VAULT_AUTH_MOUNT` solo quando Vault ha montato l'autenticazione Kubernetes in un percorso diverso da `auth/kubernetes`. Imposta `OPENCLAW_VAULT_JWT_FILE` solo quando il token dell'account di servizio è proiettato in un percorso personalizzato.

Impostazioni facoltative:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Verifica cosa può vedere la shell corrente:

bashCopy code
[code]
    openclaw vault status
[/code]

Quando è configurato più di un provider di segreti basato su Vault, selezionane uno tramite alias:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` non stampa mai `VAULT_TOKEN`; indica soltanto se il token, il file del token e il file JWT sono impostati.

## Generare e applicare un piano SecretRef

Crea un piano che associ la chiave API del provider di modelli OpenRouter a Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Applica e verifica il piano:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Usa `--allow-exec` perché il Plugin Vault esegue la risoluzione tramite un provider SecretRef exec gestito da OpenClaw.

Se il Gateway non è ancora in esecuzione, avvialo normalmente dopo aver applicato il piano, anziché eseguire `openclaw secrets reload`.

## Configurare altre chiavi dei provider

Scorciatoie integrate:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Più chiavi di provider in un unico piano:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

I provider inclusi senza scorciatoie, oppure i provider di modelli compatibili con OpenAI e personalizzati già configurati, usano `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Ogni `--provider-key <provider=id>` scrive una SecretRef in `models.providers.<provider>.apiKey`. Per i provider personalizzati, non crea le impostazioni `baseUrl`, `api` o `models` del provider; configurale prima.

Usa `--target <path=id>` per qualsiasi percorso di destinazione SecretRef noto:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

I percorsi di destinazione semplici si applicano a `openclaw.json`. Usa `auth-profiles:<agentId>:<path>` per le destinazioni esistenti in `auth-profiles.json`. Il percorso di destinazione deve essere una destinazione SecretRef registrata di OpenClaw. Il comando di configurazione non crea segreti denominati arbitrariamente in OpenClaw; Vault rimane l'archivio dei segreti e OpenClaw memorizza le SecretRef solo nei campi di configurazione supportati.

## Formato degli ID SecretRef

Gli ID SecretRef di Vault usano questa convenzione:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Esempi:

ID SecretRef | Lettura Vault KV v2 predefinita | Campo restituito  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Il campo Vault restituito deve essere una stringa.

Per KV v1, imposta:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Quindi `providers/openrouter/apiKey` legge:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Cosa memorizza OpenClaw

L'applicazione di un piano di configurazione Vault memorizza un provider gestito dal plugin:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

I campi delle credenziali puntano a tale provider:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

Il valore risolto risiede soltanto nell'istantanea attiva dei segreti di runtime.

## Container e distribuzioni gestite

I Gateway containerizzati usano comunque lo stesso Plugin e la stessa configurazione SecretRef. Il container deve ricevere:

  * `VAULT_ADDR`
  * una fonte di autenticazione: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` più `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` più `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` e `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` più `OPENCLAW_VAULT_AUTH_ROLE`; facoltativamente sostituisci `OPENCLAW_VAULT_AUTH_MOUNT` o `OPENCLAW_VAULT_JWT_FILE`
  * facoltativamente `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` e `OPENCLAW_VAULT_KV_VERSION`


Quando usi Kubernetes, preferisci `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` se Vault dispone dell'autenticazione Kubernetes configurata per il cluster. Usa `OPENCLAW_VAULT_AUTH_METHOD=jwt` solo quando Vault è configurato per trattare il cluster come emittente JWT/OIDC generico. Entrambe le opzioni sono preferibili a un token Vault a lunga durata in un Secret Kubernetes. Le distribuzioni con sidecar o injector Vault Agent possono usare invece `token_file`.

Per le configurazioni Vault multi-tenant, mantieni l'instradamento dei tenant nella policy Vault e nella configurazione della distribuzione. OpenClaw non richiede un montaggio, un ruolo o un percorso fisso: ciascun ambiente Gateway può impostare i propri `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` e ID SecretRef. Se un unico Gateway condiviso deve risolvere contemporaneamente diversi utenti Vault, usa provider exec configurati manualmente che racchiudano ambienti di autenticazione distinti, oppure suddividi i tenant tra ambienti Gateway con ambienti Vault separati.

## Contenuti correlati

  * [Gestione dei segreti](</it/gateway/secrets>)
  * [`openclaw secrets`](</it/cli/secrets>)
  * [Inventario dei Plugin](</it/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue