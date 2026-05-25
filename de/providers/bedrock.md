---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/de/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw kann **Amazon Bedrock** -Modelle über den **Bedrock Converse** \- Streaming-Provider von pi-ai verwenden. Die Bedrock-Authentifizierung verwendet die **Standard-Anmeldeinformationskette des AWS SDK** , keinen API-Schlüssel.

Eigenschaft | Wert  
---|---  
Provider | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Auth | AWS-Anmeldeinformationen (Umgebungsvariablen, gemeinsame Konfiguration oder Instanzrolle)  
Region | `AWS_REGION` oder `AWS_DEFAULT_REGION` (Standard: `us-east-1`)  
  
## Erste Schritte

Wählen Sie Ihre bevorzugte Authentifizierungsmethode und folgen Sie den Einrichtungsschritten.

### Zugriffsschlüssel / Umgebungsvariablen

**Am besten geeignet für:** Entwicklungsrechner, CI oder Hosts, auf denen Sie AWS-Anmeldeinformationen direkt verwalten.

* ### AWS-Anmeldeinformationen auf dem Gateway-Host festlegen

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Einen Bedrock-Provider und ein Modell zu Ihrer Konfiguration hinzufügen

Es ist kein `apiKey` erforderlich. Konfigurieren Sie den Provider mit `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Prüfen, ob Modelle verfügbar sind

bashCopy code
[code]
    openclaw models list
[/code]

### EC2-Instanzrollen (IMDS)

**Am besten geeignet für:** EC2-Instanzen mit angehängter IAM-Rolle, die den Instanzmetadatendienst für die Authentifizierung verwenden.

* ### Erkennung explizit aktivieren

Bei Verwendung von IMDS kann OpenClaw AWS-Authentifizierung nicht allein anhand von Umgebungsmarkern erkennen, daher müssen Sie sich explizit dafür entscheiden:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Optional einen Umgebungsmarker für den Automatikmodus hinzufügen

Wenn Sie auch möchten, dass der Pfad zur automatischen Erkennung über Umgebungsmarker funktioniert (zum Beispiel für `openclaw status`-Oberflächen):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

Sie benötigen **keinen** gefälschten API-Schlüssel.

* ### Prüfen, ob Modelle erkannt werden

bashCopy code
[code]
    openclaw models list
[/code]

## Automatische Modellerkennung

OpenClaw kann Bedrock-Modelle, die **Streaming** und **Textausgabe** unterstützen, automatisch erkennen. Die Erkennung verwendet `bedrock:ListFoundationModels` und `bedrock:ListInferenceProfiles`, und Ergebnisse werden zwischengespeichert (Standard: 1 Stunde).

So wird der implizite Provider aktiviert:

  * Wenn `plugins.entries.amazon-bedrock.config.discovery.enabled` auf `true` gesetzt ist, versucht OpenClaw die Erkennung auch dann, wenn kein AWS-Umgebungsmarker vorhanden ist.
  * Wenn `plugins.entries.amazon-bedrock.config.discovery.enabled` nicht gesetzt ist, fügt OpenClaw den impliziten Bedrock-Provider nur automatisch hinzu, wenn einer dieser AWS-Authentifizierungsmarker gefunden wird: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY` oder `AWS_PROFILE`.
  * Der tatsächliche Authentifizierungspfad der Bedrock-Laufzeit verwendet weiterhin die Standardkette des AWS SDK, sodass gemeinsame Konfiguration, SSO und Authentifizierung über IMDS-Instanzrollen auch dann funktionieren können, wenn die Erkennung `enabled: true` zum Opt-in erforderte.


Konfigurationsoptionen für die Erkennung

Konfigurationsoptionen befinden sich unter `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Option | Standard | Beschreibung  
---|---|---  
`enabled` | auto | Im Automatikmodus aktiviert OpenClaw den impliziten Bedrock-Provider nur, wenn ein unterstützter AWS-Umgebungsmarker gefunden wird. Setzen Sie `true`, um die Erkennung zu erzwingen.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | AWS-Region, die für API-Aufrufe zur Erkennung verwendet wird.  
`providerFilter` | (alle) | Entspricht Bedrock-Provider-Namen (zum Beispiel `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Cache-Dauer in Sekunden. Setzen Sie den Wert auf `0`, um Caching zu deaktivieren.  
`defaultContextWindow` | `32000` | Kontextfenster, das für erkannte Modelle verwendet wird (überschreiben Sie den Wert, wenn Sie die Grenzen Ihres Modells kennen).  
`defaultMaxTokens` | `4096` | Maximale Ausgabetokens, die für erkannte Modelle verwendet werden (überschreiben Sie den Wert, wenn Sie die Grenzen Ihres Modells kennen).  
  
## Schnelle Einrichtung (AWS-Pfad)

Diese Anleitung erstellt eine IAM-Rolle, hängt Bedrock-Berechtigungen an, verknüpft das Instanzprofil und aktiviert die OpenClaw-Erkennung auf dem EC2-Host.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Erweiterte Konfiguration

Inferenzprofile

OpenClaw erkennt **regionale und globale Inferenzprofile** zusätzlich zu Foundation Models. Wenn ein Profil einem bekannten Foundation Model zugeordnet ist, übernimmt das Profil die Fähigkeiten dieses Modells (Kontextfenster, maximale Tokens, Reasoning, Vision), und die richtige Bedrock-Anfrageregion wird automatisch eingefügt. Dadurch funktionieren regionsübergreifende Claude-Profile ohne manuelle Provider-Overrides.

IDs von Inferenzprofilen sehen aus wie `us.anthropic.claude-opus-4-6-v1:0` (regional) oder `anthropic.claude-opus-4-6-v1:0` (global). Wenn das zugrunde liegende Modell bereits in den Erkennungsergebnissen enthalten ist, übernimmt das Profil seinen vollständigen Fähigkeitssatz; andernfalls gelten sichere Standardwerte.

Es ist keine zusätzliche Konfiguration erforderlich. Solange die Erkennung aktiviert ist und der IAM- Prinzipal `bedrock:ListInferenceProfiles` besitzt, erscheinen Profile neben Foundation Models in `openclaw models list`.

Dienststufe

Einige Bedrock-Modelle unterstützen einen `service_tier`-Parameter, um Kosten oder Latenz zu optimieren. Die folgenden Stufen sind verfügbar:

Stufe | Beschreibung  
---|---  
`default` | Standard-Bedrock-Stufe  
`flex` | Vergünstigte Verarbeitung für Workloads, die längere Latenz tolerieren können  
`priority` | Priorisierte Verarbeitung für latenzempfindliche Workloads  
`reserved` | Reservierte Kapazität für Workloads im Dauerbetrieb  
  
Setzen Sie `serviceTier` (oder `service_tier`) über `agents.defaults.params` für Bedrock-Modellanfragen oder pro Modell in `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

Gültige Werte sind `default`, `flex`, `priority` und `reserved`. Nicht alle Modelle unterstützen alle Stufen. Wenn eine nicht unterstützte Stufe angefordert wird, gibt Bedrock einen Validierungsfehler zurück. Hinweis: Die Fehlermeldung ist etwas irreführend; sie kann „The provided model identifier is invalid“ sagen, statt auf eine nicht unterstützte Dienststufe hinzuweisen. Wenn Sie diesen Fehler sehen, prüfen Sie, ob das Modell die angeforderte Stufe unterstützt.

Claude Opus 4.7-Temperatur

Bedrock lehnt den `temperature`-Parameter für Claude Opus 4.7 ab. OpenClaw lässt `temperature` automatisch für jede Opus 4.7-Bedrock-Referenz weg, einschließlich Foundation-Model-IDs, benannter Inferenzprofile, Anwendungs-Inferenzprofile, deren zugrunde liegendes Modell über `bedrock:GetInferenceProfile` zu Opus 4.7 aufgelöst wird, sowie gepunkteter `opus-4.7`-Varianten mit optionalen Regionspräfixen (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). Es ist kein Konfigurationsschalter erforderlich, und die Auslassung gilt sowohl für das Anfrageoptionsobjekt als auch für das `inferenceConfig`-Payload-Feld.

Guardrails

Sie können [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) auf alle Bedrock-Modellaufrufe anwenden, indem Sie der Plugin-Konfiguration `amazon-bedrock` ein `guardrail`-Objekt hinzufügen. Mit Guardrails können Sie Inhaltsfilterung, Themenablehnung, Wortfilter, Filter für vertrauliche Informationen und Prüfungen der kontextuellen Fundierung erzwingen.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Option | Erforderlich | Beschreibung  
---|---|---  
`guardrailIdentifier` | Ja | Guardrail-ID (z. B. `abc123`) oder vollständige ARN (z. B. `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Ja | Veröffentlichte Versionsnummer oder `"DRAFT"` für den Arbeitsentwurf.  
`streamProcessingMode` | Nein | `"sync"` oder `"async"` für die Guardrail-Auswertung während des Streamings. Wenn ausgelassen, verwendet Bedrock seine Standardeinstellung.  
`trace` | Nein | `"enabled"` oder `"enabled_full"` zum Debugging; für Produktion auslassen oder auf `"disabled"` setzen.  
Embeddings für Memory-Suche

Bedrock kann auch als Embedding-Provider für die [Memory-Suche](</de/concepts/memory-search>) dienen. Dies wird getrennt vom Inferenz-Provider konfiguriert: Setzen Sie `agents.defaults.memorySearch.provider` auf `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Bedrock-Embeddings verwenden dieselbe AWS-SDK-Anmeldeinformationskette wie die Inferenz (Instanzrollen, SSO, Zugriffsschlüssel, gemeinsame Konfiguration und Webidentität). Es wird kein API-Schlüssel benötigt. Wenn `provider` `"auto"` ist, wird Bedrock automatisch erkannt, wenn diese Anmeldeinformationskette erfolgreich aufgelöst wird.

Unterstützte Embedding-Modelle umfassen Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) und TwelveLabs Marengo. Siehe [Memory-Konfigurationsreferenz -- Bedrock](</de/reference/memory-config#bedrock-embedding-config>) für die vollständige Modellliste und Dimensionsoptionen.

Hinweise und Einschränkungen

  * Bedrock erfordert aktivierten **Modellzugriff** in Ihrem AWS-Konto/Ihrer AWS-Region.
  * Automatische Erkennung benötigt die Berechtigungen `bedrock:ListFoundationModels` und `bedrock:ListInferenceProfiles`.
  * Wenn Sie sich auf den Auto-Modus verlassen, setzen Sie einen der unterstützten AWS-Auth-Env-Marker auf dem Gateway-Host. Wenn Sie IMDS-/Shared-Config-Auth ohne Env-Marker bevorzugen, setzen Sie `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * OpenClaw zeigt die Anmeldeinformationsquelle in dieser Reihenfolge an: `AWS_BEARER_TOKEN_BEDROCK`, dann `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, dann `AWS_PROFILE`, dann die standardmäßige AWS-SDK-Kette.
  * Reasoning-Unterstützung hängt vom Modell ab; prüfen Sie die Bedrock-Modellkarte auf aktuelle Fähigkeiten.
  * Wenn Sie einen verwalteten Schlüsselfluss bevorzugen, können Sie auch einen OpenAI-kompatiblen Proxy vor Bedrock platzieren und ihn stattdessen als OpenAI-Provider konfigurieren.


## Verwandt

[**Modellauswahl** Provider, Modell-Refs und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Memory-Suche** Bedrock-Embeddings für die Memory-Suchkonfiguration. ](</de/concepts/memory-search>) [**Memory-Konfigurationsreferenz** Vollständige Liste der Bedrock-Embedding-Modelle und Dimensionsoptionen. ](</de/reference/memory-config#bedrock-embedding-config>) [**Fehlerbehebung** Allgemeine Fehlerbehebung und FAQ. ](</de/help/troubleshooting>)

Was this useful?YesNo