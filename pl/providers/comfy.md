---
title: ComfyUI
source_url: https://docs.openclaw.ai/pl/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw dostarcza wbudowany plugin `comfy` do uruchamiania ComfyUI sterowanego workflow. Plugin jest w pełni sterowany przez workflow, więc OpenClaw nie próbuje mapować ogólnych ustawień `size`, `aspectRatio`, `resolution`, `durationSeconds` ani kontrolek w stylu TTS na Twój graf.

Właściwość | Szczegóły  
---|---  
Dostawca | `comfy`  
Modele | `comfy/workflow`  
Współdzielone powierzchnie | `image_generate`, `video_generate`, `music_generate`  
Auth | Brak dla lokalnego ComfyUI; `COMFY_API_KEY` lub `COMFY_CLOUD_API_KEY` dla Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` oraz Comfy Cloud `/api/*`  
  
## Co jest obsługiwane

  * Generowanie obrazów z workflow JSON
  * Edycja obrazów z 1 przesłanym obrazem referencyjnym
  * Generowanie wideo z workflow JSON
  * Generowanie wideo z 1 przesłanym obrazem referencyjnym
  * Generowanie muzyki lub audio przez współdzielone narzędzie `music_generate`
  * Pobieranie wyjścia ze skonfigurowanego node albo ze wszystkich pasujących node wyjściowych


## Pierwsze kroki

Wybierz między uruchamianiem ComfyUI na własnej maszynie a używaniem Comfy Cloud.

### Lokalnie

**Najlepsze do:** uruchamiania własnej instancji ComfyUI na swojej maszynie lub w sieci LAN.

* ### Uruchom ComfyUI lokalnie

Upewnij się, że lokalna instancja ComfyUI działa (domyślnie pod `http://127.0.0.1:8188`).

* ### Przygotuj workflow JSON

Wyeksportuj lub utwórz plik workflow JSON ComfyUI. Zanotuj identyfikatory node dla node wejścia promptu i node wyjścia, z którego OpenClaw ma odczytywać dane.

* ### Skonfiguruj dostawcę

Ustaw `mode: "local"` i wskaż plik workflow. Oto minimalny przykład dla obrazu:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Ustaw model domyślny

Skieruj OpenClaw na model `comfy/workflow` dla skonfigurowanej capability:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Zweryfikuj

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Najlepsze do:** uruchamiania workflow w Comfy Cloud bez zarządzania lokalnymi zasobami GPU.

* ### Pobierz klucz API

Zarejestruj się na [comfy.org](<https://comfy.org>) i wygeneruj klucz API w panelu swojego konta.

* ### Ustaw klucz API

Przekaż klucz jedną z tych metod:

bashCopy code
[code]
    # Zmienna środowiskowa (zalecane)export COMFY_API_KEY="your-key" # Alternatywna zmienna środowiskowaexport COMFY_CLOUD_API_KEY="your-key" # Albo bezpośrednio w konfiguracjiopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Przygotuj workflow JSON

Wyeksportuj lub utwórz plik workflow JSON ComfyUI. Zanotuj identyfikatory node dla node wejścia promptu i node wyjścia.

* ### Skonfiguruj dostawcę

Ustaw `mode: "cloud"` i wskaż plik workflow:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Zweryfikuj

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Konfiguracja

Comfy obsługuje współdzielone ustawienia połączenia najwyższego poziomu oraz sekcje workflow dla poszczególnych capability (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Współdzielone klucze

Klucz | Typ | Opis  
---|---|---  
`mode` | `"local"` or `"cloud"` | Tryb połączenia.  
`baseUrl` | string | Domyślnie `http://127.0.0.1:8188` lokalnie lub `https://cloud.comfy.org` w chmurze.  
`apiKey` | string | Opcjonalny klucz w konfiguracji, alternatywa dla zmiennych środowiskowych `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Zezwala na prywatny/LAN `baseUrl` w trybie cloud.  
  
### Klucze dla poszczególnych capability

Te klucze obowiązują w sekcjach `image`, `video` lub `music`:

Klucz | Wymagane | Domyślnie | Opis  
---|---|---|---  
`workflow` or `workflowPath` | Tak | \-- | Ścieżka do pliku workflow JSON ComfyUI.  
`promptNodeId` | Tak | \-- | Identyfikator node, który otrzymuje prompt tekstowy.  
`promptInputName` | Nie | `"text"` | Nazwa wejścia w node promptu.  
`outputNodeId` | Nie | \-- | Identyfikator node, z którego odczytywane jest wyjście. Jeśli pominięty, używane są wszystkie pasujące node wyjściowe.  
`pollIntervalMs` | Nie | \-- | Interwał odpytywania w milisekundach dla zakończenia zadania.  
`timeoutMs` | Nie | \-- | Limit czasu w milisekundach dla uruchomienia workflow.  
  
Sekcje `image` i `video` obsługują także:

Klucz | Wymagane | Domyślnie | Opis  
---|---|---|---  
`inputImageNodeId` | Tak (przy przekazywaniu obrazu referencyjnego) | \-- | Identyfikator node, który otrzymuje przesłany obraz referencyjny.  
`inputImageInputName` | Nie | `"image"` | Nazwa wejścia w node obrazu.  
  
## Szczegóły workflow

Workflow obrazów

Ustaw domyślny model obrazu na `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Przykład edycji z obrazem referencyjnym:**

Aby włączyć edycję obrazu z przesłanym obrazem referencyjnym, dodaj `inputImageNodeId` do konfiguracji obrazu:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Workflow wideo

Ustaw domyślny model wideo na `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Workflow wideo Comfy obsługują text-to-video i image-to-video przez skonfigurowany graf.

Workflow muzyki

Wbudowany plugin rejestruje dostawcę generowania muzyki dla wyjść audio lub muzyki zdefiniowanych przez workflow, udostępnianych przez współdzielone narzędzie `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Użyj sekcji konfiguracji `music`, aby wskazać workflow JSON audio i node wyjścia.

Zgodność wsteczna

Dotychczasowa konfiguracja obrazu najwyższego poziomu (bez zagnieżdżonej sekcji `image`) nadal działa:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw traktuje ten starszy kształt jako konfigurację workflow obrazu. Nie musisz migrować od razu, ale w nowych konfiguracjach zalecane są zagnieżdżone sekcje `image` / `video` / `music`.

Testy live

Dla wbudowanego pluginu istnieje opcjonalny zakres testów live:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Test live pomija poszczególne przypadki obrazów, wideo lub muzyki, chyba że skonfigurowano odpowiadającą sekcję workflow Comfy.

## Powiązane

[**Generowanie obrazów** Konfiguracja i użycie narzędzia do generowania obrazów. ](</pl/tools/image-generation>) [**Generowanie wideo** Konfiguracja i użycie narzędzia do generowania wideo. ](</pl/tools/video-generation>) [**Generowanie muzyki** Konfiguracja narzędzia do generowania muzyki i audio. ](</pl/tools/music-generation>) [**Katalog dostawców** Przegląd wszystkich dostawców i odwołań do modeli. ](</pl/providers>) [**Dokumentacja konfiguracji** Pełna dokumentacja konfiguracji, w tym ustawień domyślnych agentów. ](</pl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo