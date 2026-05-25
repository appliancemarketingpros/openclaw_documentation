---
title: Ollama-Websuche
source_url: https://docs.openclaw.ai/de/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt **Ollama Web Search** als gebündelten `web_search`-Provider. Er verwendet die Websuche-API von Ollama und gibt strukturierte Ergebnisse mit Titeln, URLs und Snippets zurück.

Für lokales oder selbst gehostetes Ollama benötigt diese Einrichtung standardmäßig keinen API-Schlüssel. Erforderlich sind:

  * ein Ollama-Host, der von OpenClaw aus erreichbar ist
  * `ollama signin`


Für direkte gehostete Suche setzen Sie die Basis-URL des Ollama-Providers auf `https://ollama.com` und stellen Sie einen echten `OLLAMA_API_KEY` bereit.

## Einrichtung

* ### Ollama starten

Stellen Sie sicher, dass Ollama installiert ist und ausgeführt wird.

* ### Anmelden

Führen Sie aus:

bashCopy code
[code]
    ollama signin
[/code]

* ### Ollama Web Search auswählen

Führen Sie aus:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Wählen Sie anschließend **Ollama Web Search** als Provider aus.

Wenn Sie Ollama bereits für Modelle verwenden, nutzt Ollama Web Search denselben konfigurierten Host erneut.

## Konfiguration

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Optionales Überschreiben des Ollama-Hosts:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Wenn Sie Ollama bereits als Modell-Provider konfigurieren, kann der Websuche-Provider stattdessen diesen Host erneut verwenden:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Der Ollama-Modell-Provider verwendet `baseUrl` als kanonischen Schlüssel. Der Websuche-Provider berücksichtigt außerdem `baseURL` unter `models.providers.ollama`, um mit Konfigurationsbeispielen im Stil des OpenAI SDK kompatibel zu sein.

Wenn keine explizite Ollama-Basis-URL festgelegt ist, verwendet OpenClaw `http://127.0.0.1:11434`.

Wenn Ihr Ollama-Host Bearer-Authentifizierung erwartet, verwendet OpenClaw `models.providers.ollama.apiKey` (oder die passende umgebungsvariablenbasierte Provider-Authentifizierung) für Anfragen an diesen konfigurierten Host erneut.

Direkte gehostete Ollama Web Search:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Hinweise

  * Für diesen Provider ist kein API-Schlüsselfeld speziell für die Websuche erforderlich.
  * Wenn der Ollama-Host durch Authentifizierung geschützt ist, verwendet OpenClaw den normalen Ollama- Provider-API-Schlüssel erneut, sofern vorhanden.
  * Wenn `baseUrl` `https://ollama.com` ist, ruft OpenClaw `https://ollama.com/api/web_search` direkt auf und sendet den konfigurierten Ollama- API-Schlüssel als Bearer-Authentifizierung.
  * Wenn der konfigurierte Host keine Websuche bereitstellt und `OLLAMA_API_KEY` gesetzt ist, kann OpenClaw auf `https://ollama.com/api/web_search` zurückfallen, ohne diesen Umgebungsschlüssel an den lokalen Host zu senden.
  * OpenClaw warnt während der Einrichtung, wenn Ollama nicht erreichbar oder nicht angemeldet ist, blockiert die Auswahl jedoch nicht.
  * Die Laufzeit-Autoerkennung kann auf Ollama Web Search zurückfallen, wenn kein höher priorisierter Provider mit Anmeldedaten konfiguriert ist.
  * Lokale Hosts des Ollama-Daemons verwenden den lokalen Proxy-Endpunkt `/api/experimental/web_search`, der signiert und an Ollama Cloud weiterleitet.
  * `https://ollama.com`-Hosts verwenden den öffentlichen gehosteten Endpunkt `/api/web_search` direkt mit Bearer-API-Schlüssel-Authentifizierung.


## Verwandt

  * [Überblick zur Websuche](</de/tools/web>) \-- alle Provider und Autoerkennung
  * [Ollama](</de/providers/ollama>) \-- Ollama-Modelleinrichtung und Cloud-/lokale Modi


Was this useful?YesNo