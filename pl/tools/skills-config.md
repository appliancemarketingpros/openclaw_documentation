---
title: Konfiguracja Skills
source_url: https://docs.openclaw.ai/pl/tools/skills-config
scraped_at: 2026-05-25
---

Większość konfiguracji ładowania/instalacji Skills znajduje się pod `skills` w `~/.openclaw/openclaw.json`. Widoczność Skills specyficzna dla agenta znajduje się pod `agents.defaults.skills` i `agents.list[].skills`.

json5Copy code
[code]
    {  skills: {    allowBundled: ["gemini", "peekaboo"],    load: {      extraDirs: ["~/Projects/agent-scripts/skills", "~/Projects/oss/some-skill-pack/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],      watch: true,      watchDebounceMs: 250,    },    install: {      preferBrew: true,      nodeManager: "npm", // npm | pnpm | yarn | bun (Gateway runtime still Node; bun not recommended)      allowUploadedArchives: false,    },    entries: {      "image-lab": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" }, // or plaintext string        env: {          GEMINI_API_KEY: "GEMINI_KEY_HERE",        },      },      peekaboo: { enabled: true },      sag: { enabled: false },    },  },}
[/code]

W przypadku wbudowanego generowania/edycji obrazów preferuj `agents.defaults.imageGenerationModel` oraz podstawowe narzędzie `image_generate`. `skills.entries.*` służy tylko do niestandardowych lub zewnętrznych przepływów pracy Skills.

Jeśli wybierzesz konkretnego dostawcę/model obrazu, skonfiguruj także uwierzytelnianie/klucz API tego dostawcy. Typowe przykłady: `GEMINI_API_KEY` lub `GOOGLE_API_KEY` dla `google/*`, `OPENAI_API_KEY` dla `openai/*` oraz `FAL_KEY` dla `fal/*`.

Przykłady:

  * Natywna konfiguracja w stylu Nano Banana Pro: `agents.defaults.imageGenerationModel.primary: "google/gemini-3-pro-image-preview"`
  * Natywna konfiguracja fal: `agents.defaults.imageGenerationModel.primary: "fal/fal-ai/flux/dev"`


## Listy dozwolonych Skills agenta

Użyj konfiguracji agenta, gdy chcesz mieć te same główne katalogi Skills maszyny/przestrzeni roboczej, ale inny widoczny zestaw Skills dla każdego agenta.

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"],    },    list: [      { id: "writer" }, // inherits defaults -> github, weather      { id: "docs", skills: ["docs-search"] }, // replaces defaults      { id: "locked-down", skills: [] }, // no skills    ],  },}
[/code]

Zasady:

  * `agents.defaults.skills`: współdzielona bazowa lista dozwolonych Skills dla agentów, które pomijają `agents.list[].skills`.
  * Pomiń `agents.defaults.skills`, aby domyślnie pozostawić Skills bez ograniczeń.
  * `agents.list[].skills`: jawny końcowy zestaw Skills dla tego agenta; nie jest scalany z wartościami domyślnymi.
  * `agents.list[].skills: []`: nie udostępniaj żadnych Skills temu agentowi.


## Pola

  * Wbudowane główne katalogi Skills zawsze obejmują `~/.openclaw/skills`, `~/.agents/skills`, `<workspace>/.agents/skills` oraz `<workspace>/skills`.
  * `allowBundled`: opcjonalna lista dozwolonych tylko dla **dołączonych** Skills. Gdy jest ustawiona, kwalifikują się tylko dołączone Skills z listy (zarządzane Skills oraz Skills agenta i przestrzeni roboczej pozostają bez zmian).
  * `load.extraDirs`: dodatkowe katalogi Skills do skanowania (najniższy priorytet).
  * `load.allowSymlinkTargets`: zaufane rzeczywiste katalogi docelowe, do których mogą rozwiązywać się dowiązane symbolicznie foldery Skills, nawet gdy dowiązanie symboliczne znajduje się poza tym katalogiem głównym celu. Użyj tego dla zamierzonych układów równoległych repozytoriów, takich jak `~/.agents/skills/manager -> ~/Projects/manager/skills`.
  * `load.watch`: obserwuj foldery Skills i odświeżaj migawkę Skills (domyślnie: true).
  * `load.watchDebounceMs`: opóźnienie debounce dla zdarzeń obserwatora Skills w milisekundach (domyślnie: 250).
  * `install.preferBrew`: preferuj instalatory brew, gdy są dostępne (domyślnie: true).
  * `install.nodeManager`: preferencja instalatora node (`npm` | `pnpm` | `yarn` | `bun`, domyślnie: npm). Dotyczy to tylko **instalacji Skills** ; środowisko wykonawcze Gateway nadal powinno być Node (Bun nie jest zalecany dla WhatsApp/Telegram). 
    * `openclaw setup --node-manager` ma węższy zakres i obecnie akceptuje `npm`, `pnpm` lub `bun`. Ustaw ręcznie `skills.install.nodeManager: "yarn"`, jeśli chcesz instalacje Skills oparte na Yarn.
  * `install.allowUploadedArchives`: zezwól zaufanym klientom Gateway `operator.admin` na instalowanie prywatnych archiwów zip przygotowanych przez `skills.upload.*` (domyślnie: false). Włącza to tylko ścieżkę przesłanych archiwów; zwykłe instalacje ClawHub jej nie wymagają.
  * `entries.<skillKey>`: nadpisania dla poszczególnych Skills.
  * `agents.defaults.skills`: opcjonalna domyślna lista dozwolonych Skills dziedziczona przez agentów, którzy pomijają `agents.list[].skills`.
  * `agents.list[].skills`: opcjonalna końcowa lista dozwolonych Skills dla poszczególnych agentów; jawne listy zastępują odziedziczone wartości domyślne zamiast je scalać.


## Dowiązane symbolicznie równoległe repozytoria

Domyślnie każdy główny katalog Skills jest granicą zawierania. Jeśli folder Skills pod `~/.agents/skills` jest dowiązaniem symbolicznym, które rozwiązuje się poza `~/.agents/skills`, OpenClaw pomija go i loguje `Skipping escaped skill path outside its configured root`.

Zachowaj układ dowiązań symbolicznych i zezwól tylko na zaufany katalog główny celu:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/manager/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],    },  },}
[/code]

Przy tej konfiguracji dowiązanie symboliczne takie jak `~/.agents/skills/manager -> ~/Projects/manager/skills` jest akceptowane po rozwiązaniu realpath. `extraDirs` skanuje także równoległe repozytorium bezpośrednio, natomiast `allowSymlinkTargets` zachowuje ścieżkę dowiązaną symbolicznie dla istniejących układów Skills agenta. Utrzymuj wpisy docelowe wąskie; nie wskazuj szerokich katalogów głównych, takich jak `~` lub `~/Projects`, chyba że każde drzewo Skills pod tym katalogiem głównym jest zaufane.

Pola dla poszczególnych Skills:

  * `enabled`: ustaw `false`, aby wyłączyć Skills, nawet jeśli są dołączone/zainstalowane.
  * `env`: zmienne środowiskowe wstrzykiwane dla uruchomienia agenta (tylko jeśli nie są już ustawione).
  * `apiKey`: opcjonalne ułatwienie dla Skills, które deklarują podstawową zmienną env. Obsługuje zwykły ciąg tekstowy lub obiekt SecretRef (`{ source, provider, id }`).


## Uwagi

  * Klucze pod `entries` domyślnie mapują się na nazwę Skills. Jeśli Skills definiują `metadata.openclaw.skillKey`, użyj tego klucza zamiast niej.
  * Priorytet ładowania to `<workspace>/skills` → `<workspace>/.agents/skills` → `~/.agents/skills` → `~/.openclaw/skills` → dołączone Skills → `skills.load.extraDirs`.
  * Zmiany w Skills są wychwytywane w następnej turze agenta, gdy obserwator jest włączony.


### Skills w piaskownicy i zmienne env

Gdy sesja jest **w piaskownicy** , procesy Skills działają wewnątrz skonfigurowanego backendu piaskownicy. Piaskownica **nie** dziedziczy hostowego `process.env`.

Użyj jednej z opcji:

  * `agents.defaults.sandbox.docker.env` dla backendu Docker (lub `agents.list[].sandbox.docker.env` dla poszczególnych agentów).
  * Wypal env w niestandardowym obrazie piaskownicy lub zdalnym środowisku piaskownicy.


## Powiązane

[**Skills** Czym są Skills i jak są ładowane. ](</pl/tools/skills>) [**Creating skills** Tworzenie niestandardowych pakietów Skills. ](</pl/tools/creating-skills>) [**Slash commands** Natywny katalog poleceń i dyrektywy czatu. ](</pl/tools/slash-commands>) [**Configuration reference** Pełny schemat `skills` i `agents.skills`. ](</pl/gateway/configuration-reference>)

Was this useful?YesNo