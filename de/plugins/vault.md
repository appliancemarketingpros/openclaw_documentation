---
title: Vault-SecretRefs
source_url: https://docs.openclaw.ai/de/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# Vault-SecretRefs

Das gebündelte Vault-Plugin ermöglicht OpenClaw, `exec`-SecretRefs beim Start des Gateways und beim Neuladen aus HashiCorp Vault aufzulösen. OpenClaw speichert Vault-Referenzen in der Konfiguration, hält aufgelöste Werte im In-Memory- Snapshot der Secrets und schreibt die aufgelösten API-Schlüssel nicht zurück in `openclaw.json`.

Verwenden Sie dies, wenn Sie Vault bereits betreiben oder die Schlüssel für Modell-Provider außerhalb der OpenClaw-Konfigurationsdateien speichern möchten. Informationen zum Laufzeitmodell für SecretRefs finden Sie unter [Secrets-Verwaltung](</de/gateway/secrets>).

## Bevor Sie beginnen

Sie benötigen:

  * OpenClaw mit verfügbarem gebündeltem `vault`-Plugin
  * einen erreichbaren Vault-Server
  * eine Vault-Authentifizierung, die ein Client-Token mit Lesezugriff auf die Secret-Pfade erzeugen kann, die OpenClaw auflösen soll
  * die Umgebung, die den Gateway startet, muss `VAULT_ADDR` und entweder `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` mit `VAULT_TOKEN_FILE` oder eine konfigurierte JWT-/Kubernetes-Anmeldung enthalten


Der Resolver kommuniziert von Node aus über HTTP mit Vault. Der Gateway benötigt die Vault-CLI nicht, um SecretRefs aufzulösen.

Aktivieren Sie das gebündelte Plugin, bevor Sie die `openclaw vault`-Befehle ausführen:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Einen Provider-Schlüssel in Vault speichern

OpenClaw verwendet standardmäßig KV v2, das unter `secret` eingehängt ist, wie in den Beispielen für den Vault-Entwicklungsserver. Legen Sie für eine Produktivumgebung von Vault `OPENCLAW_VAULT_KV_MOUNT` auf Ihren tatsächlichen KV-Einhängepfad fest, bevor Sie SecretRef-IDs erstellen. Mit den Standardeinstellungen von OpenClaw liest diese SecretRef-ID:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

dieses Vault-Feld:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Eine Möglichkeit, es mit der Vault-CLI zu erstellen, ist:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Verwenden Sie für OpenClaw ein auf den erforderlichen Umfang beschränktes Client-Token und kein Root-Token. Für das standardmäßige KV-v2-Layout sieht eine minimale Richtlinie für Schlüssel von Modell-Providern wie folgt aus:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Vault für den Gateway zugänglich machen

Exportieren Sie für einen lokalen Gateway ohne Container die Vault-Einstellungen in derselben Shell, in der OpenClaw gestartet wird. Die standardmäßige Authentifizierungsmethode liest ein Vault-Client-Token aus `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Wenn Vault Agent eine Token-Sink-Datei schreibt, verwenden Sie die Token-Datei-Authentifizierung:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Installieren Sie für einen Vault-Server, der von einer privaten CA signiert ist, entweder diese CA im Vertrauensspeicher des Hosts und aktivieren Sie den Systemvertrauensspeicher von Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Oder stellen Sie direkt ein PEM-Bundle bereit:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Diese Variablen müssen beim Start von OpenClaw vorhanden sein. Das Vault-Plugin leitet sie an seinen Resolver-Prozess weiter.

Verwenden Sie für die nicht interaktive JWT-Authentifizierung eine Workload-JWT-Datei und eine Vault-Rolle vom Typ `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

Die JWT-Datei sollte ein projiziertes Workload-Token sein, beispielsweise ein Kubernetes-Service-Account-Token mit einer Zielgruppe, die von der Vault-Rolle akzeptiert wird. Die interaktive OIDC-Anmeldung im Browser ist für Menschen nützlich, die Gateway-Laufzeit benötigt jedoch eine nicht interaktive JWT-Anmeldung oder eine Token-Datei.

Verwenden Sie für die Kubernetes-Authentifizierungsmethode von Vault `kubernetes`. Diese ist für Gateways vorgesehen, die als Pods ausgeführt werden; der standardmäßige Einhängepunkt ist `kubernetes`, und die standardmäßige JWT-Datei befindet sich unter dem üblichen Pfad für Service-Account-Token:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Legen Sie `OPENCLAW_VAULT_AUTH_MOUNT` nur fest, wenn die Kubernetes-Authentifizierung in Vault an einer anderen Stelle als `auth/kubernetes` eingehängt ist. Legen Sie `OPENCLAW_VAULT_JWT_FILE` nur fest, wenn das Service-Account-Token unter einem benutzerdefinierten Pfad projiziert wird.

Optionale Einstellungen:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Prüfen Sie, was für die aktuelle Shell sichtbar ist:

bashCopy code
[code]
    openclaw vault status
[/code]

Wenn mehr als ein Vault-gestützter Secret-Provider konfiguriert ist, wählen Sie einen anhand seines Alias aus:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` gibt `VAULT_TOKEN` niemals aus; der Befehl meldet lediglich, ob das Token, die Token-Datei und die JWT-Datei festgelegt sind.

## SecretRef-Plan erstellen und anwenden

Erstellen Sie einen Plan, der den API-Schlüssel des Modell-Providers OpenRouter Vault zuordnet:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Wenden Sie den Plan an und überprüfen Sie ihn:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Verwenden Sie `--allow-exec`, da das Vault-Plugin die Auflösung über einen von OpenClaw verwalteten exec-SecretRef-Provider durchführt.

Wenn der Gateway noch nicht ausgeführt wird, starten Sie ihn nach dem Anwenden des Plans wie gewohnt, anstatt `openclaw secrets reload` auszuführen.

## Weitere Provider-Schlüssel konfigurieren

Integrierte Kurzformen:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Mehrere Provider-Schlüssel in einem Plan:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Verwenden Sie für gebündelte Provider ohne Kurzformen oder bereits konfigurierte OpenAI-kompatible und benutzerdefinierte Modell-Provider `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Jede Angabe von `--provider-key <provider=id>` schreibt eine SecretRef nach `models.providers.<provider>.apiKey`. Bei benutzerdefinierten Providern werden dadurch die Einstellungen `baseUrl`, `api` oder `models` des Providers nicht erstellt; konfigurieren Sie diese zuerst.

Verwenden Sie `--target <path=id>` für jeden bekannten SecretRef-Zielpfad:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Reine Zielpfade gelten für `openclaw.json`. Verwenden Sie `auth-profiles:<agentId>:<path>` für vorhandene Ziele in `auth-profiles.json`. Der Zielpfad muss ein registriertes OpenClaw-SecretRef-Ziel sein. Der Einrichtungsbefehl erstellt keine beliebig benannten Geheimnisse in OpenClaw; Vault bleibt der Geheimnisspeicher, und OpenClaw speichert SecretRefs nur in unterstützten Konfigurationsfeldern.

## Format der SecretRef-ID

Vault-SecretRef-IDs verwenden diese Konvention:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Beispiele:

SecretRef-ID | Standardmäßiger KV-v2-Lesezugriff in Vault | Zurückgegebenes Feld  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Das zurückgegebene Vault-Feld muss eine Zeichenfolge sein.

Legen Sie für KV v1 Folgendes fest:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Dann liest `providers/openrouter/apiKey` Folgendes:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Was OpenClaw speichert

Beim Anwenden eines Vault-Einrichtungsplans wird ein vom Plugin verwalteter Provider gespeichert:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Anmeldedatenfelder verweisen auf diesen Provider:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

Der aufgelöste Wert ist nur im aktiven Laufzeit-Snapshot der Geheimnisse enthalten.

## Container und verwaltete Bereitstellungen

Containerisierte Gateways verwenden weiterhin dieselbe Plugin- und SecretRef-Konfiguration. Der Container muss Folgendes erhalten:

  * `VAULT_ADDR`
  * eine Authentifizierungsquelle: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` zusammen mit `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` zusammen mit `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` und `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` zusammen mit `OPENCLAW_VAULT_AUTH_ROLE`; optional können `OPENCLAW_VAULT_AUTH_MOUNT` oder `OPENCLAW_VAULT_JWT_FILE` überschrieben werden
  * optional `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` und `OPENCLAW_VAULT_KV_VERSION`


Bevorzugen Sie bei der Verwendung von Kubernetes `OPENCLAW_VAULT_AUTH_METHOD=kubernetes`, wenn in Vault die Kubernetes-Authentifizierung für den Cluster konfiguriert ist. Verwenden Sie `OPENCLAW_VAULT_AUTH_METHOD=jwt` nur, wenn Vault so konfiguriert ist, dass der Cluster als generischer JWT-/OIDC-Aussteller behandelt wird. Beide Optionen sind besser als ein langlebiges Vault- Token in einem Kubernetes-Secret. Bereitstellungen mit Vault-Agent-Sidecar oder -Injector können stattdessen `token_file` verwenden.

Behalten Sie bei mandantenfähigen Vault-Konfigurationen die Mandantenweiterleitung in der Vault-Richtlinie und der Bereitstellungskonfiguration bei. OpenClaw erfordert keinen festen Mount, keine feste Rolle und keinen festen Pfad: Jede Gateway-Umgebung kann eigene Werte für `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` und eigene SecretRef-IDs festlegen. Wenn ein gemeinsam genutzter Gateway gleichzeitig Geheimnisse für verschiedene Vault-Benutzer auflösen muss, verwenden Sie manuell konfigurierte exec-Provider, die unterschiedliche Authentifizierungsumgebungen kapseln, oder verteilen Sie die Mandanten auf Gateway- Umgebungen mit separaten Vault-Umgebungsvariablen.

## Verwandte Themen

  * [Verwaltung von Geheimnissen](</de/gateway/secrets>)
  * [`openclaw secrets`](</de/cli/secrets>)
  * [Plugin-Inventar](</de/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue