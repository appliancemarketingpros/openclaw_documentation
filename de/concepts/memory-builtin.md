---
title: Integrierte Speicher-Engine
source_url: https://docs.openclaw.ai/de/concepts/memory-builtin
scraped_at: 2026-05-25
---

Die integrierte Engine ist das standardmäßige Speicher-Backend. Sie speichert Ihren Speicherindex in einer SQLite-Datenbank pro Agent und benötigt für den Einstieg keine zusätzlichen Abhängigkeiten.

## Was sie bietet

  * **Schlüsselwortsuche** über FTS5-Volltextindexierung (BM25-Scoring).
  * **Vektorsuche** über Embeddings von jedem unterstützten Provider.
  * **Hybridsuche** , die beides kombiniert, um die besten Ergebnisse zu erzielen.
  * **CJK-Unterstützung** über Trigramm-Tokenisierung für Chinesisch, Japanisch und Koreanisch.
  * **sqlite-vec-Beschleunigung** für Vektorabfragen in der Datenbank (optional).


## Erste Schritte

Wenn Sie einen API-Schlüssel für OpenAI, Gemini, Voyage, Mistral oder DeepInfra haben, erkennt die integrierte Engine ihn automatisch und aktiviert die Vektorsuche. Keine Konfiguration erforderlich.

So legen Sie einen Provider explizit fest:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",      },    },  },}
[/code]

Ohne Embedding-Provider ist nur die Schlüsselwortsuche verfügbar.

Um den integrierten lokalen Embedding-Provider zu erzwingen, installieren Sie das optionale Laufzeitpaket `node-llama-cpp` neben OpenClaw und verweisen Sie dann `local.modelPath` auf eine GGUF-Datei:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        fallback: "none",        local: {          modelPath: "~/.node-llama-cpp/models/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

## Unterstützte Embedding-Provider

Provider | ID | Automatisch erkannt | Hinweise  
---|---|---|---  
OpenAI | `openai` | Ja | Standard: `text-embedding-3-small`  
Gemini | `gemini` | Ja | Unterstützt multimodal (Bild + Audio)  
Voyage | `voyage` | Ja |   
Mistral | `mistral` | Ja |   
DeepInfra | `deepinfra` | Ja | Standard: `BAAI/bge-m3`  
Ollama | `ollama` | Nein | Lokal, explizit festlegen  
Lokal | `local` | Ja (zuerst) | Optionale `node-llama-cpp`-Laufzeit  
  
Die automatische Erkennung wählt den ersten Provider aus, dessen API-Schlüssel aufgelöst werden kann, in der angezeigten Reihenfolge. Legen Sie `memorySearch.provider` fest, um dies zu überschreiben.

## Wie die Indexierung funktioniert

OpenClaw indexiert `MEMORY.md` und `memory/*.md` in Chunks (~400 Tokens mit 80-Token-Überlappung) und speichert sie in einer SQLite-Datenbank pro Agent.

  * **Indexspeicherort:** `~/.openclaw/memory/<agentId>.sqlite`
  * **Speicherwartung:** SQLite-WAL-Begleitdateien werden durch regelmäßige und Shutdown-Checkpoints begrenzt.
  * **Dateiüberwachung:** Änderungen an Speicherdateien lösen eine entprellte Neuindexierung aus (1,5 s).
  * **Automatische Neuindexierung:** Wenn sich der Embedding-Provider, das Modell oder die Chunking-Konfiguration ändert, wird der gesamte Index automatisch neu aufgebaut.
  * **Neuindexierung bei Bedarf:** `openclaw memory index --force`


## Wann verwenden

Die integrierte Engine ist für die meisten Nutzer die richtige Wahl:

  * Funktioniert ohne zusätzliche Abhängigkeiten sofort.
  * Verarbeitet Schlüsselwort- und Vektorsuche zuverlässig.
  * Unterstützt alle Embedding-Provider.
  * Die Hybridsuche kombiniert das Beste aus beiden Retrieval-Ansätzen.


Erwägen Sie den Wechsel zu [QMD](</de/concepts/memory-qmd>), wenn Sie Reranking, Abfrageerweiterung benötigen oder Verzeichnisse außerhalb des Workspace indexieren möchten.

Erwägen Sie [Honcho](</de/concepts/memory-honcho>), wenn Sie sitzungsübergreifenden Speicher mit automatischer Nutzermodellierung wünschen.

## Fehlerbehebung

**Speichersuche deaktiviert?** Prüfen Sie `openclaw memory status`. Wenn kein Provider erkannt wird, legen Sie einen explizit fest oder fügen Sie einen API-Schlüssel hinzu.

**Lokaler Provider nicht erkannt?** Stellen Sie sicher, dass der lokale Pfad vorhanden ist, und führen Sie Folgendes aus:

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

Sowohl eigenständige CLI-Befehle als auch der Gateway verwenden dieselbe `local`-Provider-ID. Wenn der Provider auf `auto` gesetzt ist, werden lokale Embeddings nur dann zuerst berücksichtigt, wenn `memorySearch.local.modelPath` auf eine vorhandene lokale Datei verweist.

**Veraltete Ergebnisse?** Führen Sie `openclaw memory index --force` aus, um den Index neu aufzubauen. Der Watcher kann Änderungen in seltenen Randfällen übersehen.

**sqlite-vec wird nicht geladen?** OpenClaw fällt automatisch auf In-Process-Kosinusähnlichkeit zurück. `openclaw memory status --deep` meldet den lokalen Vektorspeicher separat vom Embedding-Provider, sodass `Vector store: unavailable` auf das Laden von sqlite-vec hinweist, während `Embeddings: unavailable` auf Provider-/Authentifizierungsprobleme oder Modellbereitschaft hinweist. Prüfen Sie die Logs auf den konkreten Ladefehler.

## Konfiguration

Informationen zur Einrichtung des Embedding-Providers, zur Abstimmung der Hybridsuche (Gewichtungen, MMR, zeitlicher Abfall), Batch-Indexierung, multimodalem Speicher, sqlite-vec, zusätzlichen Pfaden und allen weiteren Konfigurationsoptionen finden Sie in der [Speicherkonfigurationsreferenz](</de/reference/memory-config>).

## Verwandt

  * [Speicherübersicht](</de/concepts/memory>)
  * [Speichersuche](</de/concepts/memory-search>)
  * [Active Memory](</de/concepts/active-memory>)


Was this useful?YesNo