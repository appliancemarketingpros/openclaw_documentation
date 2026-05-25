---
title: Webabruf
source_url: https://docs.openclaw.ai/de/tools/web-fetch
scraped_at: 2026-05-25
---

Das Tool `web_fetch` führt ein einfaches HTTP GET aus und extrahiert lesbare Inhalte (HTML zu Markdown oder Text). Es führt **kein** JavaScript aus.

Für JS-lastige Websites oder zugriffsgeschützte Seiten verwenden Sie stattdessen den [Webbrowser](</de/tools/browser>).

## Schnellstart

`web_fetch` ist **standardmäßig aktiviert** \-- keine Konfiguration erforderlich. Der Agent kann es sofort aufrufen:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Tool-Parameter

Abzurufende URL. Nur `http(s)`.

Ausgabeformat nach der Extraktion des Hauptinhalts.

Ausgabe auf diese Anzahl von Zeichen kürzen.

## Funktionsweise

* ### Fetch

Sendet ein HTTP GET mit einem Chrome-ähnlichen User-Agent und einem `Accept-Language`\- Header. Blockiert private/interne Hostnamen und prüft Weiterleitungen erneut.

* ### Extract

Führt Readability (Extraktion des Hauptinhalts) auf der HTML-Antwort aus.

* ### Fallback (optional)

Wenn Readability fehlschlägt und Firecrawl konfiguriert ist, wird über die Firecrawl-API mit Bot-Umgehungsmodus erneut versucht.

* ### Cache

Ergebnisse werden 15 Minuten lang zwischengespeichert (konfigurierbar), um wiederholte Abrufe derselben URL zu reduzieren.

## Konfiguration

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Firecrawl-Fallback

Wenn die Readability-Extraktion fehlschlägt, kann `web_fetch` als Fallback [Firecrawl](</de/tools/firecrawl>) für Bot-Umgehung und bessere Extraktion verwenden:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` unterstützt SecretRef-Objekte. Legacy-Konfiguration unter `tools.web.fetch.firecrawl.*` wird von `openclaw doctor --fix` automatisch migriert.

Aktuelles Laufzeitverhalten:

  * `tools.web.fetch.provider` wählt den Fetch-Fallback-Provider explizit aus.
  * Wenn `provider` weggelassen wird, erkennt OpenClaw automatisch den ersten bereiten Web-Fetch- Provider aus den verfügbaren Anmeldedaten. Nicht sandboxed `web_fetch` kann installierte Plugins verwenden, die `contracts.webFetchProviders` deklarieren und zur Laufzeit einen passenden Provider registrieren. Der heute gebündelte Provider ist Firecrawl.
  * Sandboxed `web_fetch`-Aufrufe bleiben auf gebündelte Provider beschränkt.
  * Wenn Readability deaktiviert ist, springt `web_fetch` direkt zum ausgewählten Provider-Fallback. Wenn kein Provider verfügbar ist, schlägt es geschlossen fehl.


## Vertrauenswürdiger Umgebungs-Proxy

Wenn Ihre Bereitstellung erfordert, dass `web_fetch` über einen vertrauenswürdigen ausgehenden HTTP(S)-Proxy läuft, setzen Sie `tools.web.fetch.useTrustedEnvProxy: true`.

In diesem Modus wendet OpenClaw weiterhin hostnamenbasierte SSRF-Prüfungen an, bevor die Anfrage gesendet wird, lässt aber den Proxy DNS auflösen, statt lokales DNS- Pinning durchzuführen. Aktivieren Sie dies nur, wenn der Proxy vom Betreiber kontrolliert wird und nach der DNS-Auflösung eine ausgehende Richtlinie durchsetzt.

## Limits und Sicherheit

  * `maxChars` wird auf `tools.web.fetch.maxCharsCap` begrenzt
  * Der Antwortkörper wird vor dem Parsen auf `maxResponseBytes` begrenzt; übergroße Antworten werden mit einer Warnung gekürzt
  * Private/interne Hostnamen werden blockiert
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` und `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` sind enge Opt-ins für vertrauenswürdige Fake-IP-Proxy-Stacks; lassen Sie sie ungesetzt, sofern Ihr Proxy diese synthetischen Bereiche nicht besitzt und seine eigene Zielrichtlinie durchsetzt
  * Weiterleitungen werden geprüft und durch `maxRedirects` begrenzt
  * `useTrustedEnvProxy` ist ein explizites Opt-in und sollte nur für betreiberkontrollierte Proxys aktiviert werden, die nach der DNS- Auflösung weiterhin eine ausgehende Richtlinie durchsetzen
  * `web_fetch` arbeitet nach Best Effort -- einige Websites benötigen den [Webbrowser](</de/tools/browser>)


## Tool-Profile

Wenn Sie Tool-Profile oder Allowlisten verwenden, fügen Sie `web_fetch` oder `group:web` hinzu:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## Verwandte Themen

  * [Websuche](</de/tools/web>) \-- das Web mit mehreren Providern durchsuchen
  * [Webbrowser](</de/tools/browser>) \-- vollständige Browser-Automatisierung für JS-lastige Websites
  * [Firecrawl](</de/tools/firecrawl>) \-- Firecrawl-Such- und Scrape-Tools


Was this useful?YesNo