---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/pl/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw może używać modeli **Amazon Bedrock** za pośrednictwem dostawcy strumieniowania **Bedrock Converse** pi-ai. Uwierzytelnianie Bedrock używa **domyślnego łańcucha poświadczeń AWS SDK** , a nie klucza API.

Właściwość | Wartość  
---|---  
Dostawca | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Auth | Poświadczenia AWS (zmienne env, konfiguracja współdzielona lub rola instancji)  
Region | `AWS_REGION` lub `AWS_DEFAULT_REGION` (domyślnie: `us-east-1`)  
  
## Pierwsze kroki

Wybierz preferowaną metodę uwierzytelniania i wykonaj kroki konfiguracji.

### Klucze dostępu / zmienne env

**Najlepsze dla:** maszyn deweloperskich, CI lub hostów, na których zarządzasz poświadczeniami AWS bezpośrednio.

* ### Ustaw poświadczenia AWS na hoście Gateway

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Opcjonalnie:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Opcjonalnie (klucz API/token bearer Bedrock):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Dodaj dostawcę Bedrock i model do swojej konfiguracji

`apiKey` nie jest wymagany. Skonfiguruj dostawcę z `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list
[/code]

### Role instancji EC2 (IMDS)

**Najlepsze dla:** instancji EC2 z przypisaną rolą IAM, używających usługi metadanych instancji do uwierzytelniania.

* ### Włącz wykrywanie jawnie

Podczas używania IMDS OpenClaw nie może wykryć uwierzytelniania AWS wyłącznie na podstawie znaczników env, więc musisz włączyć tę opcję:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Opcjonalnie dodaj znacznik env dla trybu automatycznego

Jeśli chcesz też, aby ścieżka automatycznego wykrywania znaczników env działała (na przykład dla powierzchni `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

**Nie** potrzebujesz fałszywego klucza API.

* ### Sprawdź, czy modele zostały wykryte

bashCopy code
[code]
    openclaw models list
[/code]

## Automatyczne wykrywanie modeli

OpenClaw może automatycznie wykrywać modele Bedrock obsługujące **strumieniowanie** i **wyjście tekstowe**. Wykrywanie używa `bedrock:ListFoundationModels` i `bedrock:ListInferenceProfiles`, a wyniki są buforowane (domyślnie: 1 godzina).

Jak włączany jest niejawny dostawca:

  * Jeśli `plugins.entries.amazon-bedrock.config.discovery.enabled` ma wartość `true`, OpenClaw spróbuje wykrywania nawet wtedy, gdy nie ma znacznika env AWS.
  * Jeśli `plugins.entries.amazon-bedrock.config.discovery.enabled` nie jest ustawione, OpenClaw automatycznie dodaje niejawnego dostawcę Bedrock tylko wtedy, gdy zobaczy jeden z tych znaczników uwierzytelniania AWS: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY` lub `AWS_PROFILE`.
  * Rzeczywista ścieżka uwierzytelniania środowiska uruchomieniowego Bedrock nadal używa domyślnego łańcucha AWS SDK, więc konfiguracja współdzielona, SSO i uwierzytelnianie rolą instancji IMDS mogą działać nawet wtedy, gdy wykrywanie wymagało `enabled: true`, aby zostać włączone.


Opcje konfiguracji wykrywania

Opcje konfiguracji znajdują się pod `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Opcja | Domyślnie | Opis  
---|---|---  
`enabled` | auto | W trybie automatycznym OpenClaw włącza niejawnego dostawcę Bedrock tylko wtedy, gdy zobaczy obsługiwany znacznik env AWS. Ustaw `true`, aby wymusić wykrywanie.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | Region AWS używany do wywołań API wykrywania.  
`providerFilter` | (wszystkie) | Dopasowuje nazwy dostawców Bedrock (na przykład `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Czas trwania bufora w sekundach. Ustaw `0`, aby wyłączyć buforowanie.  
`defaultContextWindow` | `32000` | Okno kontekstu używane dla wykrytych modeli (nadpisz, jeśli znasz limity swojego modelu).  
`defaultMaxTokens` | `4096` | Maksymalna liczba tokenów wyjściowych używana dla wykrytych modeli (nadpisz, jeśli znasz limity swojego modelu).  
  
## Szybka konfiguracja (ścieżka AWS)

Ten przewodnik tworzy rolę IAM, przypisuje uprawnienia Bedrock, kojarzy profil instancji i włącza wykrywanie OpenClaw na hoście EC2.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Konfiguracja zaawansowana

Profile wnioskowania

OpenClaw wykrywa **regionalne i globalne profile wnioskowania** obok modeli bazowych. Gdy profil mapuje się na znany model bazowy, profil dziedziczy możliwości tego modelu (okno kontekstu, maksymalną liczbę tokenów, rozumowanie, wizję), a poprawny region żądania Bedrock jest wstrzykiwany automatycznie. Oznacza to, że międzyregionalne profile Claude działają bez ręcznych nadpisań dostawcy.

Identyfikatory profili wnioskowania wyglądają jak `us.anthropic.claude-opus-4-6-v1:0` (regionalny) lub `anthropic.claude-opus-4-6-v1:0` (globalny). Jeśli model bazowy jest już w wynikach wykrywania, profil dziedziczy pełny zestaw jego możliwości; w przeciwnym razie stosowane są bezpieczne wartości domyślne.

Nie jest potrzebna żadna dodatkowa konfiguracja. Dopóki wykrywanie jest włączone, a podmiot IAM ma `bedrock:ListInferenceProfiles`, profile pojawiają się obok modeli bazowych w `openclaw models list`.

Poziom usługi

Niektóre modele Bedrock obsługują parametr `service_tier`, aby optymalizować koszt lub opóźnienie. Dostępne są następujące poziomy:

Poziom | Opis  
---|---  
`default` | Standardowy poziom Bedrock  
`flex` | Przetwarzanie ze zniżką dla obciążeń, które mogą tolerować większe opóźnienia  
`priority` | Przetwarzanie priorytetowe dla obciążeń wrażliwych na opóźnienia  
`reserved` | Zarezerwowana pojemność dla obciążeń o stałym charakterze  
  
Ustaw `serviceTier` (lub `service_tier`) przez `agents.defaults.params` dla żądań modeli Bedrock albo dla konkretnego modelu w `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

Prawidłowe wartości to `default`, `flex`, `priority` i `reserved`. Nie wszystkie modele obsługują wszystkie poziomy — jeśli zażądany zostanie nieobsługiwany poziom, Bedrock zwróci błąd walidacji. Uwaga: komunikat o błędzie jest nieco mylący; może brzmieć „The provided model identifier is invalid” zamiast wskazywać nieobsługiwany poziom usługi. Jeśli zobaczysz ten błąd, sprawdź, czy model obsługuje żądany poziom.

Temperatura Claude Opus 4.7

Bedrock odrzuca parametr `temperature` dla Claude Opus 4.7. OpenClaw automatycznie pomija `temperature` dla każdego odwołania Bedrock do Opus 4.7, w tym identyfikatorów modeli bazowych, nazwanych profili wnioskowania, aplikacyjnych profili wnioskowania, których model bazowy rozwiązuje się do Opus 4.7 przez `bedrock:GetInferenceProfile`, oraz wariantów z kropką `opus-4.7` z opcjonalnymi prefiksami regionu (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). Nie jest wymagane żadne pokrętło konfiguracyjne, a pominięcie dotyczy zarówno obiektu opcji żądania, jak i pola payloadu `inferenceConfig`.

Mechanizmy ochronne

Możesz zastosować [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) do wszystkich wywołań modeli Bedrock, dodając obiekt `guardrail` do konfiguracji Pluginu `amazon-bedrock`. Mechanizmy ochronne pozwalają wymuszać filtrowanie treści, blokowanie tematów, filtry słów, filtry informacji wrażliwych oraz kontrole ugruntowania kontekstowego.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Opcja | Wymagane | Opis  
---|---|---  
`guardrailIdentifier` | Tak | Identyfikator mechanizmu ochronnego (np. `abc123`) lub pełny ARN (np. `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Tak | Numer opublikowanej wersji albo `"DRAFT"` dla roboczej wersji roboczej.  
`streamProcessingMode` | Nie | `"sync"` lub `"async"` dla oceny mechanizmu ochronnego podczas strumieniowania. Jeśli pominięto, Bedrock używa wartości domyślnej.  
`trace` | Nie | `"enabled"` lub `"enabled_full"` do debugowania; pomiń albo ustaw `"disabled"` dla produkcji.  
Osadzenia do wyszukiwania w pamięci

Bedrock może również działać jako dostawca osadzeń dla [wyszukiwania w pamięci](</pl/concepts/memory-search>). Konfiguruje się to oddzielnie od dostawcy inferencji -- ustaw `agents.defaults.memorySearch.provider` na `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Osadzenia Bedrock używają tego samego łańcucha poświadczeń AWS SDK co inferencja (role instancji, SSO, klucze dostępu, współdzielona konfiguracja i tożsamość webowa). Klucz API nie jest potrzebny. Gdy `provider` ma wartość `"auto"`, Bedrock jest automatycznie wykrywany, jeśli ten łańcuch poświadczeń zostanie pomyślnie rozwiązany.

Obsługiwane modele osadzeń obejmują Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) i TwelveLabs Marengo. Zobacz [odniesienie do konfiguracji pamięci -- Bedrock](</pl/reference/memory-config#bedrock-embedding-config>), aby uzyskać pełną listę modeli i opcje wymiarów.

Uwagi i zastrzeżenia

  * Bedrock wymaga włączenia **dostępu do modelu** na Twoim koncie/regionie AWS.
  * Automatyczne wykrywanie wymaga uprawnień `bedrock:ListFoundationModels` i `bedrock:ListInferenceProfiles`.
  * Jeśli polegasz na trybie automatycznym, ustaw jeden z obsługiwanych znaczników zmiennych środowiskowych uwierzytelniania AWS na hoście Gateway. Jeśli wolisz uwierzytelnianie IMDS/współdzielonej konfiguracji bez znaczników zmiennych środowiskowych, ustaw `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * OpenClaw pokazuje źródło poświadczeń w tej kolejności: `AWS_BEARER_TOKEN_BEDROCK`, następnie `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, następnie `AWS_PROFILE`, a potem domyślny łańcuch AWS SDK.
  * Obsługa rozumowania zależy od modelu; sprawdź kartę modelu Bedrock, aby poznać aktualne możliwości.
  * Jeśli wolisz przepływ z zarządzanym kluczem, możesz również umieścić zgodne z OpenAI proxy przed Bedrock i skonfigurować je zamiast tego jako dostawcę OpenAI.


## Powiązane

[**Wybór modelu** Wybieranie dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Wyszukiwanie w pamięci** Konfiguracja osadzeń Bedrock do wyszukiwania w pamięci. ](</pl/concepts/memory-search>) [**Odniesienie do konfiguracji pamięci** Pełna lista modeli osadzeń Bedrock i opcje wymiarów. ](</pl/reference/memory-config#bedrock-embedding-config>) [**Rozwiązywanie problemów** Ogólne rozwiązywanie problemów i często zadawane pytania. ](</pl/help/troubleshooting>)

Was this useful?YesNo