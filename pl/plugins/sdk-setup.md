---
title: Konfiguracja i ustawienia Plugin
source_url: https://docs.openclaw.ai/pl/plugins/sdk-setup
scraped_at: 2026-05-25
---

Dokumentacja referencyjna dotycząca pakowania Plugin (`package.json` metadata), manifestów (`openclaw.plugin.json`), wpisów konfiguracji początkowej i schematów konfiguracji.

## Metadane pakietu

Twój `package.json` wymaga pola `openclaw`, które informuje system Plugin, co udostępnia Twój Plugin:

### Plugin kanału

jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-channel",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "channel": {      "id": "my-channel",      "label": "My Channel",      "blurb": "Short description of the channel."    }  }}
[/code]

### Plugin dostawcy / bazowy ClawHub

openclaw-clawhub-package.jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  }}
[/code]

### Pola `openclaw`

Pliki punktów wejścia (względem katalogu głównego pakietu).

Lekki wpis wyłącznie do konfiguracji początkowej (opcjonalny).

Metadane katalogowe kanału dla powierzchni konfiguracji początkowej, selektora, szybkiego startu i statusu.

Identyfikatory dostawców rejestrowane przez ten Plugin.

Wskazówki instalacji: `npmSpec`, `localPath`, `defaultChoice`, `minHostVersion`, `expectedIntegrity`, `allowInvalidConfigRecovery`.

Flagi zachowania podczas uruchamiania.

### `openclaw.channel`

`openclaw.channel` to lekkie metadane pakietu służące do wykrywania kanałów i powierzchni konfiguracji początkowej przed załadowaniem środowiska uruchomieniowego.

Pole | Typ | Znaczenie  
---|---|---  
`id` | `string` | Kanoniczny identyfikator kanału.  
`label` | `string` | Główna etykieta kanału.  
`selectionLabel` | `string` | Etykieta selektora/konfiguracji początkowej, gdy powinna różnić się od `label`.  
`detailLabel` | `string` | Dodatkowa etykieta szczegółowa dla bogatszych katalogów kanałów i powierzchni statusu.  
`docsPath` | `string` | Ścieżka dokumentacji dla linków konfiguracji początkowej i wyboru.  
`docsLabel` | `string` | Zastępcza etykieta używana dla linków do dokumentacji, gdy powinna różnić się od identyfikatora kanału.  
`blurb` | `string` | Krótki opis onboardingowy/katalogowy.  
`order` | `number` | Kolejność sortowania w katalogach kanałów.  
`aliases` | `string[]` | Dodatkowe aliasy wyszukiwania dla wyboru kanału.  
`preferOver` | `string[]` | Identyfikatory Plugin/kanałów o niższym priorytecie, które ten kanał powinien wyprzedzać.  
`systemImage` | `string` | Opcjonalna nazwa ikony/obrazu systemowego dla katalogów UI kanałów.  
`selectionDocsPrefix` | `string` | Tekst prefiksu przed linkami do dokumentacji w powierzchniach wyboru.  
`selectionDocsOmitLabel` | `boolean` | Pokazuj ścieżkę dokumentacji bezpośrednio zamiast etykietowanego linku do dokumentacji w tekście wyboru.  
`selectionExtras` | `string[]` | Dodatkowe krótkie ciągi dołączane w tekście wyboru.  
`markdownCapable` | `boolean` | Oznacza kanał jako obsługujący markdown dla decyzji o formatowaniu wychodzącym.  
`exposure` | `object` | Kontrolki widoczności kanału dla konfiguracji początkowej, list skonfigurowanych i powierzchni dokumentacji.  
`quickstartAllowFrom` | `boolean` | Włącza ten kanał do standardowego przepływu szybkiego startu `allowFrom`.  
`forceAccountBinding` | `boolean` | Wymaga jawnego powiązania konta nawet wtedy, gdy istnieje tylko jedno konto.  
`preferSessionLookupForAnnounceTarget` | `boolean` | Preferuj wyszukiwanie sesji podczas rozwiązywania celów ogłoszeń dla tego kanału.  
  
Przykład:

jsonCopy code
[code]
    {  "openclaw": {    "channel": {      "id": "my-channel",      "label": "My Channel",      "selectionLabel": "My Channel (self-hosted)",      "detailLabel": "My Channel Bot",      "docsPath": "/channels/my-channel",      "docsLabel": "my-channel",      "blurb": "Webhook-based self-hosted chat integration.",      "order": 80,      "aliases": ["mc"],      "preferOver": ["my-channel-legacy"],      "selectionDocsPrefix": "Guide:",      "selectionExtras": ["Markdown"],      "markdownCapable": true,      "exposure": {        "configured": true,        "setup": true,        "docs": true      },      "quickstartAllowFrom": true    }  }}
[/code]

`exposure` obsługuje:

  * `configured`: uwzględnij kanał w skonfigurowanych powierzchniach listowania w stylu statusu
  * `setup`: uwzględnij kanał w interaktywnych selektorach konfiguracji początkowej/konfiguracji
  * `docs`: oznacz kanał jako publiczny w powierzchniach dokumentacji/nawigacji


### `openclaw.install`

`openclaw.install` to metadane pakietu, a nie metadane manifestu.

Pole | Typ | Znaczenie  
---|---|---  
`clawhubSpec` | `string` | Kanoniczna specyfikacja ClawHub dla instalacji/aktualizacji oraz przepływów onboardingowych instalacji na żądanie.  
`npmSpec` | `string` | Kanoniczna specyfikacja npm dla zapasowych przepływów instalacji/aktualizacji.  
`localPath` | `string` | Lokalna ścieżka deweloperska lub ścieżka instalacji dołączonej.  
`defaultChoice` | `"clawhub"` | `"npm"` | `"local"` | Preferowane źródło instalacji, gdy dostępnych jest wiele źródeł.  
`minHostVersion` | `string` | Minimalna obsługiwana wersja OpenClaw w formie `>=x.y.z` lub `>=x.y.z-prerelease`.  
`expectedIntegrity` | `string` | Oczekiwany ciąg integralności npm dist, zwykle `sha512-...`, dla instalacji przypiętych.  
`allowInvalidConfigRecovery` | `boolean` | Pozwala przepływom ponownej instalacji dołączonego Plugin odzyskiwać się po określonych awariach nieaktualnej konfiguracji.  
  
Zachowanie onboardingu

Interaktywny onboarding używa również `openclaw.install` dla powierzchni instalacji na żądanie. Jeśli Twój Plugin udostępnia opcje uwierzytelniania dostawcy lub metadane konfiguracji początkowej/katalogu kanału przed załadowaniem środowiska uruchomieniowego, onboarding może pokazać ten wybór, poprosić o instalację z ClawHub, npm lub lokalną, zainstalować albo włączyć Plugin, a następnie kontynuować wybrany przepływ. Opcje onboardingu ClawHub używają `clawhubSpec` i są preferowane, gdy są obecne; opcje npm wymagają zaufanych metadanych katalogu ze specyfikacją rejestru `npmSpec`; dokładne wersje i `expectedIntegrity` są opcjonalnymi przypięciami npm. Jeśli `expectedIntegrity` jest obecne, przepływy instalacji/aktualizacji egzekwują je dla npm. Metadane „co pokazać” trzymaj w `openclaw.plugin.json`, a metadane „jak to zainstalować” w `package.json`.

Egzekwowanie minHostVersion

Jeśli ustawiono `minHostVersion`, egzekwują je zarówno instalacja, jak i ładowanie rejestru manifestów dla niedołączonych Plugin. Starsze hosty pomijają zewnętrzne Plugin; nieprawidłowe ciągi wersji są odrzucane. Zakłada się, że dołączone źródłowe Plugin mają tę samą wersję co checkout hosta.

Przypięte instalacje npm

Dla przypiętych instalacji npm zachowaj dokładną wersję w `npmSpec` i dodaj oczekiwaną integralność artefaktu:

jsonCopy code
[code]
    {  "openclaw": {    "install": {      "npmSpec": "@wecom/wecom-openclaw-plugin@1.2.3",      "expectedIntegrity": "sha512-REPLACE_WITH_NPM_DIST_INTEGRITY",      "defaultChoice": "npm"    }  }}
[/code]

Zakres allowInvalidConfigRecovery

`allowInvalidConfigRecovery` nie jest ogólnym obejściem dla uszkodzonych konfiguracji. Służy wyłącznie do wąskiego odzyskiwania dołączonego Plugin, aby ponowna instalacja/konfiguracja początkowa mogła naprawić znane pozostałości po aktualizacji, takie jak brakująca ścieżka dołączonego Plugin lub nieaktualny wpis `channels.<id>` dla tego samego Plugin. Jeśli konfiguracja jest uszkodzona z niezwiązanych powodów, instalacja nadal kończy się niepowodzeniem w trybie zamkniętym i informuje operatora, aby uruchomił `openclaw doctor --fix`.

### Odroczone pełne ładowanie

Plugin kanału mogą włączyć odroczone ładowanie za pomocą:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "startup": {      "deferConfiguredChannelFullLoadUntilAfterListen": true    }  }}
[/code]

Po włączeniu OpenClaw ładuje tylko `setupEntry` w fazie uruchamiania przed nasłuchiwaniem, nawet dla już skonfigurowanych kanałów. Pełny wpis ładuje się po rozpoczęciu nasłuchiwania przez Gateway.

Jeśli Twój wpis konfiguracji początkowej/pełny wpis rejestruje metody RPC Gateway, trzymaj je pod prefiksem specyficznym dla Plugin. Zarezerwowane podstawowe przestrzenie nazw administracyjnych (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) pozostają własnością core i zawsze rozwiązują się do `operator.admin`.

## Manifest Plugin

Każdy natywny Plugin musi dostarczać `openclaw.plugin.json` w katalogu głównym pakietu. OpenClaw używa go do walidacji konfiguracji bez wykonywania kodu Plugin.

jsonCopy code
[code]
    {  "id": "my-plugin",  "name": "My Plugin",  "description": "Adds My Plugin capabilities to OpenClaw",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {      "webhookSecret": {        "type": "string",        "description": "Webhook verification secret"      }    }  }}
[/code]

Dla Plugin kanału dodaj `kind` i `channels`:

jsonCopy code
[code]
    {  "id": "my-channel",  "kind": "channel",  "channels": ["my-channel"],  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  }}
[/code]

Nawet Plugin bez konfiguracji muszą dostarczać schemat. Pusty schemat jest prawidłowy:

jsonCopy code
[code]
    {  "id": "my-plugin",  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

Zobacz [Manifest Plugin](</pl/plugins/manifest>), aby uzyskać pełną dokumentację referencyjną schematu.

## Publikowanie w ClawHub

Dla pakietów Plugin użyj polecenia ClawHub specyficznego dla pakietu:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

## Wpis konfiguracji

Plik `setup-entry.ts` jest lekką alternatywą dla `index.ts`, którą OpenClaw ładuje, gdy potrzebuje tylko powierzchni konfiguracji (onboarding, naprawa konfiguracji, inspekcja wyłączonego kanału).

typescriptCopy code
[code]
    // setup-entry.ts  export default defineSetupPluginEntry(myChannelPlugin);
[/code]

Pozwala to uniknąć ładowania ciężkiego kodu wykonawczego (bibliotek kryptograficznych, rejestracji CLI, usług działających w tle) podczas przepływów konfiguracji.

Kanały dołączone w obszarze roboczym, które utrzymują bezpieczne dla konfiguracji eksporty w modułach bocznych, mogą używać `defineBundledChannelSetupEntry(...)` z `openclaw/plugin-sdk/channel-entry-contract` zamiast `defineSetupPluginEntry(...)`. Ten dołączony kontrakt obsługuje również opcjonalny eksport `runtime`, dzięki czemu okablowanie runtime podczas konfiguracji może pozostać lekkie i jawne.

When OpenClaw uses setupEntry instead of the full entry

  * Kanał jest wyłączony, ale potrzebuje powierzchni konfiguracji/onboardingu.
  * Kanał jest włączony, ale nieskonfigurowany.
  * Włączone jest odroczone ładowanie (`deferConfiguredChannelFullLoadUntilAfterListen`).

What setupEntry must register

  * Obiekt Plugin kanału (przez `defineSetupPluginEntry`).
  * Wszelkie trasy HTTP wymagane przed nasłuchem Gateway.
  * Wszelkie metody Gateway potrzebne podczas uruchamiania.


Te metody Gateway uruchamiane na starcie nadal powinny unikać zarezerwowanych głównych przestrzeni nazw administracyjnych, takich jak `config.*` lub `update.*`.

What setupEntry should NOT include

  * Rejestracje CLI.
  * Usługi działające w tle.
  * Ciężkie importy runtime (kryptografia, SDK).
  * Metody Gateway potrzebne dopiero po uruchomieniu.


### Wąskie importy pomocników konfiguracji

Dla gorących ścieżek przeznaczonych tylko do konfiguracji preferuj wąskie seams pomocników konfiguracji zamiast szerszego parasola `plugin-sdk/setup`, gdy potrzebujesz tylko części powierzchni konfiguracji:

Ścieżka importu | Do czego służy | Kluczowe eksporty  
---|---|---  
`plugin-sdk/setup-runtime` | pomocnicy runtime czasu konfiguracji, którzy pozostają dostępni w `setupEntry` / odroczonym uruchamianiu kanału | `createPatchedAccountSetupAdapter`, `createEnvPatchedAccountSetupAdapter`, `createSetupInputPresenceValidator`, `noteChannelLookupFailure`, `noteChannelLookupSummary`, `promptResolvedAllowFrom`, `splitSetupEntries`, `createAllowlistSetupWizardProxy`, `createDelegatedSetupWizardProxy`  
`plugin-sdk/setup-adapter-runtime` | przestarzały alias zgodności; użyj `plugin-sdk/setup-runtime` | `createEnvPatchedAccountSetupAdapter`  
`plugin-sdk/setup-tools` | pomocnicy konfiguracji/instalacji CLI/archiwów/dokumentacji | `formatCliCommand`, `detectBinary`, `extractArchive`, `resolveBrewExecutable`, `formatDocsLink`, `CONFIG_DIR`  
  
Użyj szerszego seam `plugin-sdk/setup`, gdy chcesz pełny współdzielony zestaw narzędzi konfiguracji, w tym pomocniki łatek konfiguracji, takie jak `moveSingleAccountChannelSectionToDefaultAccount(...)`.

Adaptery łatek konfiguracji pozostają bezpieczne dla gorącej ścieżki przy imporcie. Ich dołączone wyszukiwanie powierzchni kontraktu promocji pojedynczego konta jest leniwe, więc importowanie `plugin-sdk/setup-runtime` nie ładuje z wyprzedzeniem wykrywania dołączonej powierzchni kontraktu, zanim adapter zostanie faktycznie użyty.

### Promocja pojedynczego konta zarządzana przez kanał

Gdy kanał aktualizuje się z konfiguracji najwyższego poziomu dla pojedynczego konta do `channels.<id>.accounts.*`, domyślne współdzielone zachowanie polega na przeniesieniu promowanych wartości o zakresie konta do `accounts.default`.

Dołączone kanały mogą zawęzić lub nadpisać tę promocję przez swoją powierzchnię kontraktu konfiguracji:

  * `singleAccountKeysToMove`: dodatkowe klucze najwyższego poziomu, które powinny zostać przeniesione do promowanego konta
  * `namedAccountPromotionKeys`: gdy konta nazwane już istnieją, tylko te klucze trafiają do promowanego konta; współdzielone klucze polityki/dostarczania pozostają w katalogu głównym kanału
  * `resolveSingleAccountPromotionTarget(...)`: wybiera, które istniejące konto otrzyma promowane wartości


## Schemat konfiguracji

Konfiguracja Plugin jest walidowana względem JSON Schema w manifeście. Użytkownicy konfigurują Pluginy przez:

json5Copy code
[code]
    {  plugins: {    entries: {      "my-plugin": {        config: {          webhookSecret: "abc123",        },      },    },  },}
[/code]

Twój Plugin otrzymuje tę konfigurację jako `api.pluginConfig` podczas rejestracji.

Dla konfiguracji specyficznej dla kanału użyj zamiast tego sekcji konfiguracji kanału:

json5Copy code
[code]
    {  channels: {    "my-channel": {      token: "bot-token",      allowFrom: ["user1", "user2"],    },  },}
[/code]

### Budowanie schematów konfiguracji kanału

Użyj `buildChannelConfigSchema`, aby przekonwertować schemat Zod na opakowanie `ChannelConfigSchema` używane przez artefakty konfiguracji należące do Plugin:

typescriptCopy code
[code]
      const accountSchema = z.object({  token: z.string().optional(),  allowFrom: z.array(z.string()).optional(),  accounts: z.object({}).catchall(z.any()).optional(),  defaultAccount: z.string().optional(),}); const configSchema = buildChannelConfigSchema(accountSchema);
[/code]

Jeśli już tworzysz kontrakt jako JSON Schema lub TypeBox, użyj bezpośredniego pomocnika, aby OpenClaw mógł pominąć konwersję Zod-do-JSON-Schema na ścieżkach metadanych:

typescriptCopy code
[code]
      const configSchema = buildJsonChannelConfigSchema(  Type.Object({    token: Type.Optional(Type.String()),    allowFrom: Type.Optional(Type.Array(Type.String())),  }),);
[/code]

W przypadku Pluginów zewnętrznych kontraktem zimnej ścieżki nadal jest manifest Plugin: odzwierciedl wygenerowany JSON Schema w `openclaw.plugin.json#channelConfigs`, aby schemat konfiguracji, konfiguracja i powierzchnie UI mogły sprawdzać `channels.<id>` bez ładowania kodu runtime.

## Kreatory konfiguracji

Pluginy kanałów mogą udostępniać interaktywne kreatory konfiguracji dla `openclaw onboard`. Kreator jest obiektem `ChannelSetupWizard` w `ChannelPlugin`:

typescriptCopy code
[code]
     const setupWizard: ChannelSetupWizard = {  channel: "my-channel",  status: {    configuredLabel: "Connected",    unconfiguredLabel: "Not configured",    resolveConfigured: ({ cfg }) => Boolean((cfg.channels as any)?.["my-channel"]?.token),  },  credentials: [    {      inputKey: "token",      providerHint: "my-channel",      credentialLabel: "Bot token",      preferredEnvVar: "MY_CHANNEL_BOT_TOKEN",      envPrompt: "Use MY_CHANNEL_BOT_TOKEN from environment?",      keepPrompt: "Keep current token?",      inputPrompt: "Enter your bot token:",      inspect: ({ cfg, accountId }) => {        const token = (cfg.channels as any)?.["my-channel"]?.token;        return {          accountConfigured: Boolean(token),          hasConfiguredValue: Boolean(token),        };      },    },  ],};
[/code]

Typ `ChannelSetupWizard` obsługuje `credentials`, `textInputs`, `dmPolicy`, `allowFrom`, `groupAccess`, `prepare`, `finalize` i więcej. Pełne przykłady znajdziesz w pakietach dołączonych Pluginów (na przykład Plugin Discord `src/channel.setup.ts`).

Shared allowFrom prompts

W przypadku monitów listy dozwolonych DM, które potrzebują tylko standardowego przepływu `note -> prompt -> parse -> merge -> patch`, preferuj współdzielone pomocniki konfiguracji z `openclaw/plugin-sdk/setup`: `createPromptParsedAllowFromForAccount(...)`, `createTopLevelChannelParsedAllowFromPrompt(...)` i `createNestedChannelParsedAllowFromPrompt(...)`.

Standard channel setup status

W przypadku bloków statusu konfiguracji kanału, które różnią się tylko etykietami, wynikami i opcjonalnymi dodatkowymi wierszami, preferuj `createStandardChannelSetupStatus(...)` z `openclaw/plugin-sdk/setup` zamiast ręcznie tworzyć ten sam obiekt `status` w każdym Plugin.

Optional channel setup surface

W przypadku opcjonalnych powierzchni konfiguracji, które powinny pojawiać się tylko w określonych kontekstach, użyj `createOptionalChannelSetupSurface` z `openclaw/plugin-sdk/channel-setup`:

typescriptCopy code
[code]
    import { createOptionalChannelSetupSurface } from "openclaw/plugin-sdk/channel-setup"; const setupSurface = createOptionalChannelSetupSurface({  channel: "my-channel",  label: "My Channel",  npmSpec: "@myorg/openclaw-my-channel",  docsPath: "/channels/my-channel",});// Returns { setupAdapter, setupWizard }
[/code]

`plugin-sdk/channel-setup` udostępnia również niższopoziomowe konstruktory `createOptionalChannelSetupAdapter(...)` i `createOptionalChannelSetupWizard(...)`, gdy potrzebujesz tylko jednej połowy tej opcjonalnej powierzchni instalacji.

Wygenerowany opcjonalny adapter/kreator bezpiecznie odmawia rzeczywistych zapisów konfiguracji. Ponownie używa jednego komunikatu o wymaganej instalacji w `validateInput`, `applyAccountConfig` i `finalize` oraz dołącza link do dokumentacji, gdy ustawione jest `docsPath`.

Binary-backed setup helpers

W przypadku UI konfiguracji wspieranych przez pliki binarne preferuj współdzielone delegowane pomocniki zamiast kopiować to samo połączenie binarne/statusu do każdego kanału:

  * `createDetectedBinaryStatus(...)` dla bloków statusu, które różnią się tylko etykietami, wskazówkami, wynikami i wykrywaniem pliku binarnego
  * `createCliPathTextInput(...)` dla wejść tekstowych opartych na ścieżce
  * `createDelegatedSetupWizardStatusResolvers(...)`, `createDelegatedPrepare(...)`, `createDelegatedFinalize(...)` i `createDelegatedResolveConfigured(...)`, gdy `setupEntry` musi leniwie przekazać obsługę do cięższego pełnego kreatora
  * `createDelegatedTextInputShouldPrompt(...)`, gdy `setupEntry` musi tylko delegować decyzję `textInputs[*].shouldPrompt`


## Publikowanie i instalowanie

**Zewnętrzne Pluginy:** opublikuj w [ClawHub](</pl/clawhub>), a następnie zainstaluj:

### npm

bashCopy code
[code]
    openclaw plugins install @myorg/openclaw-my-plugin
[/code]

Gołe specyfikacje pakietów są instalowane z npm podczas przełączenia uruchomieniowego.

### ClawHub only

bashCopy code
[code]
    openclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

### npm package spec

Użyj npm, gdy pakiet nie został jeszcze przeniesiony do ClawHub albo gdy potrzebujesz bezpośredniej ścieżki instalacji npm podczas migracji:

bashCopy code
[code]
    openclaw plugins install npm:@myorg/openclaw-my-plugin
[/code]

**Pluginy w repozytorium:** umieść je w dołączonym drzewie obszaru roboczego Pluginów, a zostaną automatycznie wykryte podczas kompilacji.

**Użytkownicy mogą instalować:**

bashCopy code
[code]
    openclaw plugins install <package-name>
[/code]

Metadane dołączonego pakietu są jawne, a nie wywnioskowane ze skompilowanego JavaScriptu podczas uruchamiania gateway. Zależności uruchomieniowe należą do pakietu Pluginu, który jest ich właścicielem; uruchomienie spakowanego OpenClaw nigdy nie naprawia ani nie odzwierciedla zależności Pluginów.

## Powiązane

  * [Tworzenie Pluginów](</pl/plugins/building-plugins>) — przewodnik krok po kroku ułatwiający rozpoczęcie pracy
  * [Manifest Pluginu](</pl/plugins/manifest>) — pełna dokumentacja schematu manifestu
  * [Punkty wejścia SDK](</pl/plugins/sdk-entrypoints>) — `definePluginEntry` i `defineChannelPluginEntry`


Was this useful?YesNo