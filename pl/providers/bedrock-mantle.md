---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/pl/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw zawiera dołączonego dostawcę **Amazon Bedrock Mantle** , który łączy się z punktem końcowym Mantle zgodnym z OpenAI. Mantle hostuje modele open source i modele innych firm (GPT-OSS, Qwen, Kimi, GLM i podobne) przez standardową powierzchnię `/v1/chat/completions` opartą na infrastrukturze Bedrock.

Właściwość | Wartość  
---|---  
ID dostawcy | `amazon-bedrock-mantle`  
API | `openai-completions` (zgodne z OpenAI) lub `anthropic-messages` (trasa Anthropic Messages)  
Uwierzytelnianie | Jawne `AWS_BEARER_TOKEN_BEDROCK` lub generowanie tokena bearer z łańcucha poświadczeń IAM  
Domyślny region | `us-east-1` (nadpisz za pomocą `AWS_REGION` lub `AWS_DEFAULT_REGION`)  
  
## Pierwsze kroki

Wybierz preferowaną metodę uwierzytelniania i wykonaj kroki konfiguracji.

### Jawny token bearer

**Najlepsze dla:** środowisk, w których masz już token bearer Mantle.

* ### Ustaw token bearer na hoście Gateway

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Opcjonalnie ustaw region (domyślnie `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Zweryfikuj, że modele zostały wykryte

bashCopy code
[code]
    openclaw models list
[/code]

Wykryte modele pojawią się pod dostawcą `amazon-bedrock-mantle`. Nie jest wymagana dodatkowa konfiguracja, chyba że chcesz nadpisać wartości domyślne.

### Poświadczenia IAM

**Najlepsze dla:** używania poświadczeń zgodnych z AWS SDK (wspólna konfiguracja, SSO, tożsamość web identity, role instancji lub zadań).

* ### Skonfiguruj poświadczenia AWS na hoście Gateway

Działa każde źródło uwierzytelniania zgodne z AWS SDK:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Zweryfikuj, że modele zostały wykryte

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw automatycznie generuje token bearer Mantle z łańcucha poświadczeń.

## Automatyczne wykrywanie modeli

Gdy `AWS_BEARER_TOKEN_BEDROCK` jest ustawione, OpenClaw używa go bezpośrednio. W przeciwnym razie OpenClaw próbuje wygenerować token bearer Mantle z domyślnego łańcucha poświadczeń AWS. Następnie wykrywa dostępne modele Mantle, odpytując regionalny punkt końcowy `/v1/models`.

Zachowanie | Szczegół  
---|---  
Pamięć podręczna wykrywania | Wyniki buforowane przez 1 godzinę  
Odświeżanie tokena IAM | Co godzinę  
  
Aby pozostawić Plugin Mantle włączony, ale wyłączyć automatyczne wykrywanie i generowanie tokenu bearer IAM, wyłącz przełącznik wykrywania należący do Plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Obsługiwane regiony

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Konfiguracja ręczna

Jeśli wolisz jawną konfigurację zamiast automatycznego wykrywania:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Konfiguracja zaawansowana

Obsługa rozumowania

Obsługa rozumowania jest wnioskowana z identyfikatorów modeli zawierających wzorce takie jak `thinking`, `reasoner` lub `gpt-oss-120b`. OpenClaw ustawia `reasoning: true` automatycznie dla pasujących modeli podczas wykrywania.

Niedostępność punktu końcowego

Jeśli punkt końcowy Mantle jest niedostępny lub nie zwraca żadnych modeli, dostawca jest pomijany bez komunikatu. OpenClaw nie zgłasza błędu; inni skonfigurowani dostawcy nadal działają normalnie.

Claude Opus 4.7 przez trasę Anthropic Messages

Mantle udostępnia także trasę Anthropic Messages, która przenosi modele Claude przez tę samą ścieżkę strumieniowania uwierzytelnianą tokenem bearer. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) można wywołać przez tę trasę ze strumieniowaniem należącym do dostawcy, więc tokeny bearer AWS nie są traktowane jak klucze API Anthropic.

Gdy przypniesz model Anthropic Messages u dostawcy Mantle, OpenClaw używa powierzchni API `anthropic-messages` zamiast `openai-completions` dla tego modelu. Uwierzytelnianie nadal pochodzi z `AWS_BEARER_TOKEN_BEDROCK` (lub z utworzonego tokena bearer IAM).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relacja z dostawcą Amazon Bedrock

Bedrock Mantle jest osobnym dostawcą względem standardowego dostawcy [Amazon Bedrock](</pl/providers/bedrock>). Mantle używa powierzchni `/v1` zgodnej z OpenAI, podczas gdy standardowy dostawca Bedrock używa natywnego API Bedrock.

Obaj dostawcy współdzielą to samo poświadczenie `AWS_BEARER_TOKEN_BEDROCK`, gdy jest obecne.

## Powiązane

[**Amazon Bedrock** Natywny dostawca Bedrock dla Anthropic Claude, Titan i innych modeli. ](</pl/providers/bedrock>) [**Wybór modelu** Wybieranie dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**OAuth i uwierzytelnianie** Szczegóły uwierzytelniania i reguły ponownego użycia poświadczeń. ](</pl/gateway/authentication>) [**Rozwiązywanie problemów** Typowe problemy i sposoby ich rozwiązywania. ](</pl/help/troubleshooting>)

Was this useful?YesNo