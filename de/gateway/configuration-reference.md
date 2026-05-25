---
title: Konfigurationsreferenz
source_url: https://docs.openclaw.ai/de/gateway/configuration-reference
scraped_at: 2026-05-25
---

Kernkonfigurationsreferenz für `~/.openclaw/openclaw.json`. Eine aufgabenorientierte Übersicht finden Sie unter [Konfiguration](</de/gateway/configuration>).

Behandelt die wichtigsten OpenClaw-Konfigurationsbereiche und verlinkt weiter, wenn ein Subsystem eine eigene, detailliertere Referenz hat. Kanal- und Plugin-eigene Befehlskataloge sowie tiefgehende Speicher-/QMD-Schalter befinden sich auf eigenen Seiten statt auf dieser.

Code-Wahrheit:

  * `openclaw config schema` gibt das Live-JSON-Schema aus, das für Validierung und Control UI verwendet wird, mit zusammengeführten gebündelten/Plugin-/Kanal-Metadaten, sofern verfügbar
  * `config.schema.lookup` gibt einen pfadbezogenen Schemaknoten für Drill-down-Werkzeuge zurück
  * `pnpm config:docs:check` / `pnpm config:docs:gen` validieren den Baseline-Hash der Konfigurationsdokumentation gegen die aktuelle Schemaoberfläche


Agent-Nachschlagepfad: Verwenden Sie die `gateway`-Toolaktion `config.schema.lookup` für exakte feldbezogene Dokumentation und Einschränkungen vor Änderungen. Verwenden Sie [Konfiguration](</de/gateway/configuration>) für aufgabenorientierte Anleitung und diese Seite für die breitere Feldübersicht, Standardwerte und Links zu Subsystemreferenzen.

Dedizierte Detailreferenzen:

  * [Referenz zur Speicherkonfiguration](</de/reference/memory-config>) für `agents.defaults.memorySearch.*`, `memory.qmd.*`, `memory.citations` und Dreaming-Konfiguration unter `plugins.entries.memory-core.config.dreaming`
  * [Slash-Befehle](</de/tools/slash-commands>) für den aktuellen integrierten + gebündelten Befehlskatalog
  * zuständige Kanal-/Plugin-Seiten für kanalspezifische Befehlsoberflächen


Das Konfigurationsformat ist **JSON5** (Kommentare + nachgestellte Kommas erlaubt). Alle Felder sind optional - OpenClaw verwendet sichere Standardwerte, wenn sie ausgelassen werden.

* * *

## Kanäle

Kanalspezifische Konfigurationsschlüssel wurden auf eine dedizierte Seite verschoben - siehe [Konfiguration - Kanäle](</de/gateway/config-channels>) für `channels.*`, einschließlich Slack, Discord, Telegram, WhatsApp, Matrix, iMessage und anderer gebündelter Kanäle (Authentifizierung, Zugriffskontrolle, mehrere Konten, Erwähnungs-Gating).

## Agent-Standardwerte, Multi-Agent, Sitzungen und Nachrichten

Auf eine dedizierte Seite verschoben - siehe [Konfiguration - Agents](</de/gateway/config-agents>) für:

  * `agents.defaults.*` (Arbeitsbereich, Modell, Denken, Heartbeat, Speicher, Medien, Skills, Sandbox)
  * `multiAgent.*` (Multi-Agent-Routing und Bindungen)
  * `session.*` (Sitzungslebenszyklus, Compaction, Pruning)
  * `messages.*` (Nachrichtenzustellung, TTS, Markdown-Rendering)
  * `talk.*` (Talk-Modus) 
    * `talk.consultThinkingLevel`: Override der Denkstufe für den vollständigen OpenClaw-Agent-Lauf hinter Control UI Talk-Echtzeitkonsultationen
    * `talk.consultFastMode`: einmaliger Fast-Mode-Override für Control UI Talk-Echtzeitkonsultationen
    * `talk.speechLocale`: optionale BCP-47-Locale-ID für Talk-Spracherkennung unter iOS/macOS
    * `talk.silenceTimeoutMs`: wenn nicht gesetzt, behält Talk das plattformseitige Standard-Pausenfenster vor dem Senden des Transkripts bei (`700 ms on macOS and Android, 900 ms on iOS`)


## Tools und benutzerdefinierte Provider

Tool-Richtlinie, experimentelle Schalter, Provider-gestützte Tool-Konfiguration und Einrichtung benutzerdefinierter Provider / Basis-URLs wurden auf eine dedizierte Seite verschoben - siehe [Konfiguration - Tools und benutzerdefinierte Provider](</de/gateway/config-tools>).

## Modelle

Provider-Definitionen, Modell-Allowlists und die Einrichtung benutzerdefinierter Provider befinden sich in [Konfiguration - Tools und benutzerdefinierte Provider](</de/gateway/config-tools#custom-providers-and-base-urls>). Die `models`-Wurzel besitzt außerdem globales Modellkatalogverhalten.

json5Copy code
[code]
    {  models: {    // Optional. Default: true. Requires a Gateway restart when changed.    pricing: { enabled: false },  },}
[/code]

  * `models.mode`: Provider-Katalogverhalten (`merge` oder `replace`).
  * `models.providers`: Zuordnung benutzerdefinierter Provider, geschlüsselt nach Provider-ID.
  * `models.providers.*.localService`: optionaler On-Demand-Prozessmanager für lokale Modellserver. OpenClaw prüft den konfigurierten Health-Endpunkt, startet bei Bedarf den absoluten `command`, wartet auf Bereitschaft und sendet dann die Modellanfrage. Siehe [Lokale Modelldienste](</de/gateway/local-model-services>).
  * `models.pricing.enabled`: steuert den Hintergrund-Preis-Bootstrap, der startet, nachdem Sidecars und Kanäle den Gateway-Bereit-Pfad erreicht haben. Wenn `false`, überspringt der Gateway OpenRouter- und LiteLLM-Preiskatalogabrufe; konfigurierte `models.providers.*.models[].cost`-Werte funktionieren weiterhin für lokale Kostenschätzungen.


## MCP

Von OpenClaw verwaltete MCP-Serverdefinitionen befinden sich unter `mcp.servers` und werden von eingebettetem Pi und anderen Runtime-Adaptern genutzt. Die Befehle `openclaw mcp list`, `show`, `set` und `unset` verwalten diesen Block, ohne während Konfigurationsänderungen eine Verbindung zum Zielserver herzustellen.

json5Copy code
[code]
    {  mcp: {    // Optional. Default: 600000 ms (10 minutes). Set 0 to disable idle eviction.    sessionIdleTtlMs: 600000,    servers: {      docs: {        command: "npx",        args: ["-y", "@modelcontextprotocol/server-fetch"],      },      remote: {        url: "https://example.com/mcp",        transport: "streamable-http", // streamable-http | sse        headers: {          Authorization: "Bearer ${MCP_REMOTE_TOKEN}",        },      },    },  },}
[/code]

  * `mcp.servers`: benannte stdio- oder Remote-MCP-Serverdefinitionen für Runtimes, die konfigurierte MCP-Tools bereitstellen. Remote-Einträge verwenden `transport: "streamable-http"` oder `transport: "sse"`; `type: "http"` ist ein CLI-nativer Alias, den `openclaw mcp set` und `openclaw doctor --fix` in das kanonische Feld `transport` normalisieren.
  * `mcp.sessionIdleTtlMs`: Leerlauf-TTL für sitzungsbezogene gebündelte MCP-Runtimes. Einmalige eingebettete Läufe fordern Bereinigung am Laufende an; diese TTL ist die Rückfallebene für langlebige Sitzungen und zukünftige Aufrufer.
  * Änderungen unter `mcp.*` werden durch Entsorgen zwischengespeicherter Sitzungs-MCP-Runtimes direkt angewendet. Die nächste Tool-Erkennung/-Nutzung erstellt sie aus der neuen Konfiguration neu, sodass entfernte `mcp.servers`-Einträge sofort bereinigt werden, statt auf die Leerlauf-TTL zu warten.


Siehe [MCP](</de/cli/mcp#openclaw-as-an-mcp-client-registry>) und [CLI-Backends](</de/gateway/cli-backends#bundle-mcp-overlays>) für Runtime-Verhalten.

## Skills

json5Copy code
[code]
    {  skills: {    allowBundled: ["gemini", "peekaboo"],    load: {      extraDirs: ["~/Projects/agent-scripts/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],    },    install: {      preferBrew: true,      nodeManager: "npm", // npm | pnpm | yarn | bun      allowUploadedArchives: false,    },    entries: {      "image-lab": {        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" }, // or plaintext string        env: { GEMINI_API_KEY: "GEMINI_KEY_HERE" },      },      peekaboo: { enabled: true },      sag: { enabled: false },    },  },}
[/code]

  * `allowBundled`: optionale Allowlist nur für gebündelte Skills (verwaltete/Arbeitsbereich-Skills nicht betroffen).
  * `load.extraDirs`: zusätzliche gemeinsame Skill-Wurzeln (niedrigste Priorität).
  * `load.allowSymlinkTargets`: vertrauenswürdige echte Zielwurzeln, in die Skill-Symlinks auflösen dürfen, wenn sich der Link außerhalb seiner konfigurierten Quellwurzel befindet.
  * `install.preferBrew`: wenn true, Homebrew-Installer bevorzugen, sofern `brew` verfügbar ist, bevor auf andere Installer-Arten zurückgefallen wird.
  * `install.nodeManager`: Node-Installer-Präferenz für `metadata.openclaw.install`\- Spezifikationen (`npm` | `pnpm` | `yarn` | `bun`).
  * `install.allowUploadedArchives`: vertrauenswürdigen `operator.admin`-Gateway- Clients erlauben, private ZIP-Archive zu installieren, die über `skills.upload.*` bereitgestellt wurden (Standard: false). Dies aktiviert nur den Pfad für hochgeladene Archive; normale ClawHub- Installationen benötigen dies nicht.
  * `entries.<skillKey>.enabled: false` deaktiviert einen Skill, selbst wenn er gebündelt/installiert ist.
  * `entries.<skillKey>.apiKey`: Komfortfeld für Skills, die eine primäre Umgebungsvariable deklarieren (Klartextzeichenfolge oder SecretRef-Objekt).


* * *

## Plugins

json5Copy code
[code]
    {  plugins: {    enabled: true,    allow: ["voice-call"],    bundledDiscovery: "allowlist",    deny: [],    load: {      paths: ["~/Projects/oss/voice-call-plugin"],    },    entries: {      "voice-call": {        enabled: true,        hooks: {          allowPromptInjection: false,        },        config: { provider: "twilio" },      },    },  },}
[/code]

  * Geladen aus `~/.openclaw/extensions`, `<workspace>/.openclaw/extensions` sowie `plugins.load.paths`.
  * Die Erkennung akzeptiert native OpenClaw-Plugins sowie kompatible Codex-Bundles und Claude-Bundles, einschließlich manifestloser Claude-Bundles im Standardlayout.
  * **Konfigurationsänderungen erfordern einen Gateway-Neustart.**
  * `allow`: optionale Allowlist (nur aufgeführte Plugins werden geladen). `deny` hat Vorrang.
  * `bundledDiscovery`: standardmäßig `"allowlist"` für neue Konfigurationen, sodass eine nicht leere `plugins.allow` auch gebündelte Provider-Plugins einschließt, einschließlich Websuche- Runtime-Providern. Doctor schreibt `"compat"` für migrierte Legacy-Allowlist- Konfigurationen, um bestehendes Verhalten gebündelter Provider beizubehalten, bis Sie sich dafür entscheiden.
  * `plugins.entries.<id>.apiKey`: Komfortfeld für API-Schlüssel auf Plugin-Ebene (wenn vom Plugin unterstützt).
  * `plugins.entries.<id>.env`: Plugin-spezifische Zuordnung von Umgebungsvariablen.
  * `plugins.entries.<id>.hooks.allowPromptInjection`: wenn `false`, blockiert Core `before_prompt_build` und ignoriert Prompt-mutierende Felder aus Legacy-`before_agent_start`, während Legacy-`modelOverride` und `providerOverride` beibehalten werden. Gilt für native Plugin-Hooks und unterstützte, von Bundles bereitgestellte Hook-Verzeichnisse.
  * `plugins.entries.<id>.hooks.allowConversationAccess`: wenn `true`, dürfen vertrauenswürdige nicht gebündelte Plugins rohe Konversationsinhalte aus typisierten Hooks wie `llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize` und `agent_end` lesen.
  * `plugins.entries.<id>.subagent.allowModelOverride`: diesem Plugin ausdrücklich vertrauen, pro Lauf `provider`\- und `model`-Overrides für Hintergrund-Subagent-Läufe anzufordern.
  * `plugins.entries.<id>.subagent.allowedModels`: optionale Allowlist kanonischer `provider/model`-Ziele für vertrauenswürdige Subagent-Overrides. Verwenden Sie `"*"` nur, wenn Sie bewusst jedes Modell zulassen möchten.
  * `plugins.entries.<id>.llm.allowModelOverride`: diesem Plugin ausdrücklich vertrauen, Modell-Overrides für `api.runtime.llm.complete` anzufordern.
  * `plugins.entries.<id>.llm.allowedModels`: optionale Allowlist kanonischer `provider/model`-Ziele für vertrauenswürdige Plugin-LLM-Completion-Overrides. Verwenden Sie `"*"` nur, wenn Sie bewusst jedes Modell zulassen möchten.
  * `plugins.entries.<id>.llm.allowAgentIdOverride`: diesem Plugin ausdrücklich vertrauen, `api.runtime.llm.complete` gegen eine nicht standardmäßige Agent-ID auszuführen.
  * `plugins.entries.<id>.config`: vom Plugin definiertes Konfigurationsobjekt (validiert durch natives OpenClaw-Plugin-Schema, sofern verfügbar).
  * Konto-/Runtime-Einstellungen von Kanal-Plugins befinden sich unter `channels.<id>` und sollten durch die Manifest-Metadaten `channelConfigs` des zuständigen Plugins beschrieben werden, nicht durch eine zentrale OpenClaw-Optionsregistrierung.


### Codex-Harness-Plugin-Konfiguration

Das gebündelte `codex`-Plugin besitzt native Codex-App-Server-Harness-Einstellungen unter `plugins.entries.codex.config`. Siehe [Codex-Harness-Referenz](</de/plugins/codex-harness-reference>) für die vollständige Konfigurationsoberfläche und [Codex-Harness](</de/plugins/codex-harness>) für das Runtime-Modell.

`codexPlugins` gilt nur für Sitzungen, die den nativen Codex-Harness auswählen. Es aktiviert keine Codex-Plugins für Pi, normale OpenAI-Provider-Läufe, ACP- Konversationsbindungen oder einen beliebigen Nicht-Codex-Harness.

json5Copy code
[code]
    {  plugins: {    entries: {      codex: {        enabled: true,        config: {          codexPlugins: {            enabled: true,            allow_destructive_actions: true,            plugins: {              "google-calendar": {                enabled: true,                marketplaceName: "openai-curated",                pluginName: "google-calendar",                allow_destructive_actions: false,              },            },          },        },      },    },  },}
[/code]

  * `plugins.entries.codex.config.codexPlugins.enabled`: aktiviert native Codex Plugin-/App-Unterstützung für das Codex-Harness. Standard: `false`.
  * `plugins.entries.codex.config.codexPlugins.allow_destructive_actions`: standardmäßige Richtlinie für destruktive Aktionen bei migrierten Plugin-App-Elicitations. Standard: `true`.
  * `plugins.entries.codex.config.codexPlugins.plugins.<key>.enabled`: aktiviert einen migrierten Plugin-Eintrag, wenn global `codexPlugins.enabled` ebenfalls true ist. Standard: `true` für explizite Einträge.
  * `plugins.entries.codex.config.codexPlugins.plugins.<key>.marketplaceName`: stabile Marketplace-Identität. V1 unterstützt nur `"openai-curated"`.
  * `plugins.entries.codex.config.codexPlugins.plugins.<key>.pluginName`: stabile Codex-Plugin-Identität aus der Migration, zum Beispiel `"google-calendar"`.
  * `plugins.entries.codex.config.codexPlugins.plugins.<key>.allow_destructive_actions`: Plugin-spezifische Überschreibung für destruktive Aktionen. Wenn ausgelassen, wird der globale Wert `allow_destructive_actions` verwendet.


`codexPlugins.enabled` ist die globale Aktivierungsdirektive. Explizite Plugin- Einträge, die durch die Migration geschrieben werden, sind die dauerhafte Menge für Installations- und Reparaturberechtigung. `plugins["*"]` wird nicht unterstützt, es gibt keinen `install`-Schalter, und lokale `marketplacePath`-Werte sind absichtlich keine Konfigurationsfelder, da sie hostspezifisch sind.

`app/list`-Bereitschaftsprüfungen werden für eine Stunde zwischengespeichert und bei Veraltung asynchron aktualisiert. Die App-Konfiguration des Codex-Threads wird beim Aufbau der Codex-Harness- Sitzung berechnet, nicht bei jedem Turn; verwenden Sie `/new`, `/reset` oder einen Gateway- Neustart, nachdem Sie die native Plugin-Konfiguration geändert haben.

  * `plugins.entries.firecrawl.config.webFetch`: Firecrawl-Web-Fetch-Provider-Einstellungen. 
    * `apiKey`: Firecrawl-API-Schlüssel (akzeptiert SecretRef). Fällt zurück auf `plugins.entries.firecrawl.config.webSearch.apiKey`, das Legacy-`tools.web.fetch.firecrawl.apiKey` oder die Env-Var `FIRECRAWL_API_KEY`.
    * `baseUrl`: Firecrawl-API-Basis-URL (Standard: `https://api.firecrawl.dev`; selbst gehostete Überschreibungen müssen auf private/interne Endpunkte zielen).
    * `onlyMainContent`: nur den Hauptinhalt aus Seiten extrahieren (Standard: `true`).
    * `maxAgeMs`: maximales Cache-Alter in Millisekunden (Standard: `172800000` / 2 Tage).
    * `timeoutSeconds`: Timeout für Scrape-Anfragen in Sekunden (Standard: `60`).
  * `plugins.entries.xai.config.xSearch`: Einstellungen für xAI X Search (Grok-Websuche). 
    * `enabled`: den X-Search-Provider aktivieren.
    * `model`: Grok-Modell, das für die Suche verwendet werden soll (z. B. `"grok-4-1-fast"`).
  * `plugins.entries.memory-core.config.dreaming`: Einstellungen für Memory-Dreaming. Siehe [Dreaming](</de/concepts/dreaming>) für Phasen und Schwellenwerte. 
    * `enabled`: Hauptschalter für Dreaming (Standard `false`).
    * `frequency`: Cron-Takt für jeden vollständigen Dreaming-Durchlauf (standardmäßig `"0 3 * * *"`).
    * `model`: optionale Modellüberschreibung für den Dream-Diary-Subagenten. Erfordert `plugins.entries.memory-core.subagent.allowModelOverride: true`; kombinieren Sie dies mit `allowedModels`, um Ziele einzuschränken. Fehler wegen nicht verfügbarer Modelle werden einmal mit dem Standardmodell der Sitzung erneut versucht; Trust- oder Allowlist-Fehler fallen nicht stillschweigend zurück.
    * Phasenrichtlinie und Schwellenwerte sind Implementierungsdetails (keine benutzerseitigen Konfigurationsschlüssel).
  * Die vollständige Memory-Konfiguration befindet sich in der [Memory-Konfigurationsreferenz](</de/reference/memory-config>): 
    * `agents.defaults.memorySearch.*`
    * `memory.backend`
    * `memory.citations`
    * `memory.qmd.*`
    * `plugins.entries.memory-core.config.dreaming`
  * Aktivierte Claude-Bundle-Plugins können außerdem eingebettete Pi-Standardwerte aus `settings.json` beisteuern; OpenClaw wendet diese als bereinigte Agent-Einstellungen an, nicht als rohe OpenClaw-Konfigurationspatches.
  * `plugins.slots.memory`: wählen Sie die aktive Memory-Plugin-ID oder `"none"`, um Memory-Plugins zu deaktivieren.
  * `plugins.slots.contextEngine`: wählen Sie die aktive Kontext-Engine-Plugin-ID; standardmäßig `"legacy"`, sofern Sie keine andere Engine installieren und auswählen.


Siehe [Plugins](</de/tools/plugin>).

* * *

## Zusagen

`commitments` steuert abgeleitete Nachfass-Memory: OpenClaw kann Check-ins aus Gesprächs-Turns erkennen und sie über Heartbeat-Läufe ausliefern.

  * `commitments.enabled`: aktiviert versteckte LLM-Extraktion, Speicherung und Heartbeat-Auslieferung für abgeleitete Nachfasszusagen. Standard: `false`.
  * `commitments.maxPerDay`: maximale Anzahl abgeleiteter Nachfasszusagen, die pro Agent-Sitzung innerhalb eines rollierenden Tages ausgeliefert werden. Standard: `3`.


Siehe [Abgeleitete Zusagen](</de/concepts/commitments>).

* * *

## Browser

json5Copy code
[code]
    {  browser: {    enabled: true,    evaluateEnabled: true,    defaultProfile: "user",    ssrfPolicy: {      // dangerouslyAllowPrivateNetwork: true, // opt in only for trusted private-network access      // allowPrivateNetwork: true, // legacy alias      // hostnameAllowlist: ["*.example.com", "example.com"],      // allowedHostnames: ["localhost"],    },    tabCleanup: {      enabled: true,      idleMinutes: 120,      maxTabsPerSession: 8,      sweepMinutes: 5,    },    profiles: {      openclaw: { cdpPort: 18800, color: "#FF4500" },      work: {        cdpPort: 18801,        color: "#0066CC",        executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",      },      user: { driver: "existing-session", attachOnly: true, color: "#00AA00" },      brave: {        driver: "existing-session",        attachOnly: true,        userDataDir: "~/Library/Application Support/BraveSoftware/Brave-Browser",        color: "#FB542B",      },      remote: { cdpUrl: "http://10.0.0.42:9222", color: "#00AA00" },    },    color: "#FF4500",    // headless: false,    // noSandbox: false,    // extraArgs: [],    // executablePath: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",    // attachOnly: false,  },}
[/code]

  * `evaluateEnabled: false` deaktiviert `act:evaluate` und `wait --fn`.
  * `tabCleanup` gibt verfolgte Tabs des primären Agenten nach Leerlaufzeit oder wenn eine Sitzung ihr Limit überschreitet wieder frei. Setzen Sie `idleMinutes: 0` oder `maxTabsPerSession: 0`, um diese einzelnen Bereinigungsmodi zu deaktivieren.
  * `ssrfPolicy.dangerouslyAllowPrivateNetwork` ist deaktiviert, wenn nicht gesetzt, sodass Browser-Navigation standardmäßig strikt bleibt.
  * Setzen Sie `ssrfPolicy.dangerouslyAllowPrivateNetwork: true` nur, wenn Sie Browser-Navigation in privaten Netzwerken absichtlich vertrauen.
  * Im strikten Modus unterliegen Remote-CDP-Profilendpunkte (`profiles.*.cdpUrl`) bei Erreichbarkeits-/Erkennungsprüfungen derselben Blockierung privater Netzwerke.
  * `ssrfPolicy.allowPrivateNetwork` bleibt als Legacy-Alias unterstützt.
  * Verwenden Sie im strikten Modus `ssrfPolicy.hostnameAllowlist` und `ssrfPolicy.allowedHostnames` für explizite Ausnahmen.
  * Remote-Profile sind nur zum Anhängen vorgesehen (Start/Stopp/Reset deaktiviert).
  * `profiles.*.cdpUrl` akzeptiert `http://`, `https://`, `ws://` und `wss://`. Verwenden Sie HTTP(S), wenn OpenClaw `/json/version` ermitteln soll; verwenden Sie WS(S), wenn Ihr Provider Ihnen eine direkte DevTools-WebSocket-URL bereitstellt.
  * `remoteCdpTimeoutMs` und `remoteCdpHandshakeTimeoutMs` gelten für Remote- und `attachOnly`-CDP-Erreichbarkeit sowie Tab-Öffnungsanfragen. Verwaltete loopback- Profile behalten lokale CDP-Standardwerte.
  * Wenn ein extern verwalteter CDP-Dienst über loopback erreichbar ist, setzen Sie für dieses Profil `attachOnly: true`; andernfalls behandelt OpenClaw den loopback-Port als lokal verwaltetes Browser-Profil und kann lokale Portbesitzfehler melden.
  * `existing-session`-Profile verwenden Chrome MCP statt CDP und können auf dem ausgewählten Host oder über einen verbundenen Browser-Knoten anhängen.
  * `existing-session`-Profile können `userDataDir` setzen, um ein bestimmtes Chromium-basiertes Browser-Profil wie Brave oder Edge anzusteuern.
  * `existing-session`-Profile behalten die aktuellen Chrome-MCP-Routenlimits: snapshot-/ref-gesteuerte Aktionen statt CSS-Selektor-Targeting, Ein-Datei-Upload- Hooks, keine Dialog-Timeout-Überschreibungen, kein `wait --load networkidle` und kein `responsebody`, PDF-Export, Download-Interception oder Batch-Aktionen.
  * Lokal verwaltete `openclaw`-Profile weisen `cdpPort` und `cdpUrl` automatisch zu; setzen Sie `cdpUrl` nur explizit für Remote-CDP.
  * Lokal verwaltete Profile können `executablePath` setzen, um das globale `browser.executablePath` für dieses Profil zu überschreiben. Verwenden Sie dies, um ein Profil in Chrome und ein anderes in Brave auszuführen.
  * Lokal verwaltete Profile verwenden `browser.localLaunchTimeoutMs` für die HTTP- Erkennung von Chrome CDP nach dem Prozessstart und `browser.localCdpReadyTimeoutMs` für die CDP-WebSocket-Bereitschaft nach dem Start. Erhöhen Sie diese Werte auf langsameren Hosts, bei denen Chrome erfolgreich startet, Bereitschaftsprüfungen aber mit dem Start konkurrieren. Beide Werte müssen positive Ganzzahlen bis `120000` ms sein; ungültige Konfigurationswerte werden abgelehnt.
  * Reihenfolge der automatischen Erkennung: Standardbrowser, wenn Chromium-basiert → Chrome → Brave → Edge → Chromium → Chrome Canary.
  * `browser.executablePath` und `browser.profiles.<name>.executablePath` akzeptieren beide `~` und `~/...` für Ihr OS-Home-Verzeichnis vor dem Chromium-Start. Profilbezogenes `userDataDir` in `existing-session`-Profilen wird ebenfalls mit Tilde expandiert.
  * Steuerdienst: nur loopback (Port abgeleitet aus `gateway.port`, Standard `18791`).
  * `extraArgs` hängt zusätzliche Start-Flags an den lokalen Chromium-Start an (zum Beispiel `--disable-gpu`, Fenstergrößen oder Debug-Flags).


* * *

## UI

json5Copy code
[code]
    {  ui: {    seamColor: "#FF4500",    assistant: {      name: "OpenClaw",      avatar: "CB", // emoji, short text, image URL, or data URI    },  },}
[/code]

  * `seamColor`: Akzentfarbe für die Chrome-Elemente der nativen App-UI (Talk-Mode-Bubble-Färbung usw.).
  * `assistant`: Überschreibung der Control-UI-Identität. Fällt auf die aktive Agent-Identität zurück.


* * *

## Gateway

json5Copy code
[code]
    {  gateway: {    mode: "local", // local | remote    port: 18789,    bind: "loopback",    auth: {      mode: "token", // none | token | password | trusted-proxy      token: "your-token",      // password: "your-password", // or OPENCLAW_GATEWAY_PASSWORD      // trustedProxy: { userHeader: "x-forwarded-user" }, // for mode=trusted-proxy; see /gateway/trusted-proxy-auth      allowTailscale: true,      rateLimit: {        maxAttempts: 10,        windowMs: 60000,        lockoutMs: 300000,        exemptLoopback: true,      },    },    tailscale: {      mode: "off", // off | serve | funnel      resetOnExit: false,    },    controlUi: {      enabled: true,      basePath: "/openclaw",      // root: "dist/control-ui",      // embedSandbox: "scripts", // strict | scripts | trusted      // allowExternalEmbedUrls: false, // dangerous: allow absolute external http(s) embed URLs      // chatMessageMaxWidth: "min(1280px, 82%)", // optional grouped chat message max-width      // allowedOrigins: ["https://control.example.com"], // required for non-loopback Control UI      // dangerouslyAllowHostHeaderOriginFallback: false, // dangerous Host-header origin fallback mode      // allowInsecureAuth: false,      // dangerouslyDisableDeviceAuth: false,    },    remote: {      url: "ws://gateway.tailnet:18789",      transport: "ssh", // ssh | direct      token: "your-token",      // password: "your-password",    },    trustedProxies: ["10.0.0.1"],    // Optional. Default false.    allowRealIpFallback: false,    nodes: {      pairing: {        // Optional. Default unset/disabled.        autoApproveCidrs: ["192.168.1.0/24", "fd00:1234:5678::/64"],      },      allowCommands: ["canvas.navigate"],      denyCommands: ["system.run"],    },    tools: {      // Additional /tools/invoke HTTP denies      deny: ["browser"],      // Remove tools from the default HTTP deny list      allow: ["gateway"],    },    push: {      apns: {        relay: {          baseUrl: "https://relay.example.com",          timeoutMs: 10000,        },      },    },  },}
[/code]

Gateway field details

  * `mode`: `local` (Gateway ausführen) oder `remote` (mit Remote-Gateway verbinden). Gateway verweigert den Start, sofern nicht `local` festgelegt ist.
  * `port`: einzelner multiplexter Port für WS + HTTP. Priorität: `--port` > `OPENCLAW_GATEWAY_PORT` > `gateway.port` > `18789`.
  * `bind`: `auto`, `loopback` (Standard), `lan` (`0.0.0.0`), `tailnet` (nur Tailscale-IP) oder `custom`.
  * **Legacy-Bind-Aliasse** : Verwenden Sie Bind-Modus-Werte in `gateway.bind` (`auto`, `loopback`, `lan`, `tailnet`, `custom`), nicht Host-Aliasse (`0.0.0.0`, `127.0.0.1`, `localhost`, `::`, `::1`).
  * **Docker-Hinweis** : Das standardmäßige `loopback`-Binding lauscht im Container auf `127.0.0.1`. Bei Docker-Bridge-Networking (`-p 18789:18789`) kommt Traffic auf `eth0` an, daher ist das Gateway nicht erreichbar. Verwenden Sie `--network host`, oder setzen Sie `bind: "lan"` (oder `bind: "custom"` mit `customBindHost: "0.0.0.0"`), um auf allen Interfaces zu lauschen.
  * **Authentifizierung** : standardmäßig erforderlich. Nicht-Loopback-Bindings erfordern Gateway-Authentifizierung. Praktisch bedeutet das ein gemeinsames Token/Passwort oder einen identitätsbewussten Reverse Proxy mit `gateway.auth.mode: "trusted-proxy"`. Der Onboarding-Assistent erzeugt standardmäßig ein Token.
  * Wenn sowohl `gateway.auth.token` als auch `gateway.auth.password` konfiguriert sind (einschließlich SecretRefs), setzen Sie `gateway.auth.mode` explizit auf `token` oder `password`. Start- und Service-Installations-/Reparaturflüsse schlagen fehl, wenn beide konfiguriert sind und kein Modus gesetzt ist.
  * `gateway.auth.mode: "none"`: expliziter Modus ohne Authentifizierung. Nur für vertrauenswürdige lokale local loopback-Setups verwenden; dies wird absichtlich nicht in Onboarding-Eingabeaufforderungen angeboten.
  * `gateway.auth.mode: "trusted-proxy"`: Browser-/Benutzerauthentifizierung an einen identitätsbewussten Reverse Proxy delegieren und Identitäts-Header von `gateway.trustedProxies` vertrauen (siehe [Trusted-Proxy-Authentifizierung](</de/gateway/trusted-proxy-auth>)). Dieser Modus erwartet standardmäßig eine **Nicht-Loopback** -Proxy-Quelle; same-host local loopback-Reverse-Proxys erfordern explizit `gateway.auth.trustedProxy.allowLoopback = true`. Interne same-host-Aufrufer können `gateway.auth.password` als lokalen direkten Fallback verwenden; `gateway.auth.token` bleibt mit dem Trusted-Proxy-Modus gegenseitig ausgeschlossen.
  * `gateway.auth.allowTailscale`: Wenn `true`, können Tailscale Serve-Identitäts-Header die Control-UI-/WebSocket-Authentifizierung erfüllen (verifiziert über `tailscale whois`). HTTP-API-Endpunkte verwenden diese Tailscale-Header-Authentifizierung **nicht** ; sie folgen stattdessen dem normalen HTTP-Authentifizierungsmodus des Gateways. Dieser tokenlose Flow geht davon aus, dass der Gateway-Host vertrauenswürdig ist. Standard ist `true`, wenn `tailscale.mode = "serve"`.
  * `gateway.auth.rateLimit`: optionaler Limiter für fehlgeschlagene Authentifizierung. Gilt pro Client-IP und pro Authentifizierungsbereich (shared-secret und device-token werden unabhängig verfolgt). Blockierte Versuche geben `429` \+ `Retry-After` zurück.
  * Im asynchronen Tailscale-Serve-Control-UI-Pfad werden fehlgeschlagene Versuche für dasselbe `{scope, clientIp}` vor dem Schreiben des Fehlers serialisiert. Gleichzeitige fehlerhafte Versuche desselben Clients können den Limiter daher bei der zweiten Anfrage auslösen, statt beide als einfache Fehlübereinstimmungen durchlaufen zu lassen.
  * `gateway.auth.rateLimit.exemptLoopback` ist standardmäßig `true`; setzen Sie `false`, wenn Sie localhost-Traffic absichtlich ebenfalls rate-limitieren möchten (für Test-Setups oder strikte Proxy-Deployments).
  * Browser-Origin-WS-Authentifizierungsversuche werden immer gedrosselt, wobei die Loopback-Ausnahme deaktiviert ist (Defense-in-Depth gegen browserbasierte localhost-Brute-Force-Angriffe).
  * Bei local loopback werden diese browserbezogenen Sperren pro normalisiertem `Origin`-Wert isoliert, sodass wiederholte Fehlschläge von einem localhost-Origin nicht automatisch einen anderen Origin sperren.
  * `tailscale.mode`: `serve` (nur Tailnet, local loopback-Bind) oder `funnel` (öffentlich, erfordert Authentifizierung).
  * `tailscale.preserveFunnel`: Wenn `true` und `tailscale.mode = "serve"`, prüft OpenClaw `tailscale funnel status`, bevor Serve beim Start erneut angewendet wird, und überspringt dies, wenn eine extern konfigurierte Funnel-Route bereits den Gateway-Port abdeckt. Standard `false`.
  * `controlUi.allowedOrigins`: explizite Browser-Origin-Allowlist für Gateway-WebSocket-Verbindungen. Erforderlich, wenn Browser-Clients von Nicht-Loopback-Origins erwartet werden.
  * `controlUi.chatMessageMaxWidth`: optionale maximale Breite für gruppierte Control-UI-Chatnachrichten. Akzeptiert eingeschränkte CSS-Breitenwerte wie `960px`, `82%`, `min(1280px, 82%)` und `calc(100% - 2rem)`.
  * `controlUi.dangerouslyAllowHostHeaderOriginFallback`: gefährlicher Modus, der den Host-Header-Origin-Fallback für Deployments aktiviert, die absichtlich auf Host-Header-Origin-Policy setzen.
  * `remote.transport`: `ssh` (Standard) oder `direct` (ws/wss). Für `direct` muss `remote.url` `ws://` oder `wss://` sein.
  * `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1`: clientseitiger Prozessumgebungs-Break-Glass-Override, der Klartext-`ws://` zu vertrauenswürdigen Private-Network-IPs erlaubt; Standard bleibt Klartext nur für local loopback. Es gibt kein `openclaw.json`-Äquivalent, und Browser-Private-Network-Konfiguration wie `browser.ssrfPolicy.dangerouslyAllowPrivateNetwork` wirkt sich nicht auf Gateway-WebSocket-Clients aus.
  * `gateway.remote.token` / `.password` sind Zugangsdatenfelder für Remote-Clients. Sie konfigurieren die Gateway-Authentifizierung nicht selbst.
  * `gateway.push.apns.relay.baseUrl`: Basis-HTTPS-URL für das externe APNs-Relay, das von offiziellen/TestFlight-iOS-Builds verwendet wird, nachdem sie relaygestützte Registrierungen im Gateway veröffentlicht haben. Diese URL muss mit der in den iOS-Build einkompilierten Relay-URL übereinstimmen.
  * `gateway.push.apns.relay.timeoutMs`: Sende-Timeout vom Gateway zum Relay in Millisekunden. Standard ist `10000`.
  * Relaygestützte Registrierungen werden an eine bestimmte Gateway-Identität delegiert. Die gekoppelte iOS-App ruft `gateway.identity.get` ab, fügt diese Identität in die Relay-Registrierung ein und leitet eine registrierungsbezogene Sendeberechtigung an das Gateway weiter. Ein anderes Gateway kann diese gespeicherte Registrierung nicht wiederverwenden.
  * `OPENCLAW_APNS_RELAY_BASE_URL` / `OPENCLAW_APNS_RELAY_TIMEOUT_MS`: temporäre Env-Overrides für die obige Relay-Konfiguration.
  * `OPENCLAW_APNS_RELAY_ALLOW_HTTP=true`: nur für Entwicklung vorgesehene Ausweichoption für local loopback-HTTP-Relay-URLs. Produktions-Relay-URLs sollten bei HTTPS bleiben.
  * `gateway.handshakeTimeoutMs`: Pre-Auth-Gateway-WebSocket-Handshake-Timeout in Millisekunden. Standard: `15000`. `OPENCLAW_HANDSHAKE_TIMEOUT_MS` hat Vorrang, wenn gesetzt. Erhöhen Sie diesen Wert auf ausgelasteten oder leistungsschwachen Hosts, bei denen lokale Clients verbinden können, während sich das Startup-Warmup noch stabilisiert.
  * `gateway.channelHealthCheckMinutes`: Intervall des Channel-Health-Monitors in Minuten. Setzen Sie `0`, um Health-Monitor-Neustarts global zu deaktivieren. Standard: `5`.
  * `gateway.channelStaleEventThresholdMinutes`: Schwellenwert für veraltete Sockets in Minuten. Halten Sie diesen größer oder gleich `gateway.channelHealthCheckMinutes`. Standard: `30`.
  * `gateway.channelMaxRestartsPerHour`: maximale Health-Monitor-Neustarts pro Channel/Konto in einer gleitenden Stunde. Standard: `10`.
  * `channels.<provider>.healthMonitor.enabled`: Opt-out pro Channel für Health-Monitor-Neustarts, während der globale Monitor aktiviert bleibt.
  * `channels.<provider>.accounts.<accountId>.healthMonitor.enabled`: Override pro Konto für Multi-Account-Channels. Wenn gesetzt, hat er Vorrang vor dem Channel-Level-Override.
  * Lokale Gateway-Aufrufpfade können `gateway.remote.*` nur als Fallback verwenden, wenn `gateway.auth.*` nicht gesetzt ist.
  * Wenn `gateway.auth.token` / `gateway.auth.password` explizit über SecretRef konfiguriert und nicht auflösbar ist, schlägt die Auflösung geschlossen fehl (keine Maskierung durch Remote-Fallback).
  * `trustedProxies`: Reverse-Proxy-IPs, die TLS terminieren oder Forwarded-Client-Header injizieren. Listen Sie nur Proxys auf, die Sie kontrollieren. Loopback-Einträge sind weiterhin gültig für same-host Proxy-/Local-Detection-Setups (zum Beispiel Tailscale Serve oder ein lokaler Reverse Proxy), machen local loopback-Anfragen jedoch **nicht** für `gateway.auth.mode: "trusted-proxy"` zulässig.
  * `allowRealIpFallback`: Wenn `true`, akzeptiert das Gateway `X-Real-IP`, falls `X-Forwarded-For` fehlt. Standard `false` für Fail-Closed-Verhalten.
  * `gateway.nodes.pairing.autoApproveCidrs`: optionale CIDR/IP-Allowlist für die automatische Genehmigung erstmaliger Node-Device-Kopplung ohne angeforderte Scopes. Sie ist deaktiviert, wenn nicht gesetzt. Dies genehmigt keine Operator-/Browser-/Control-UI-/WebChat-Kopplung automatisch und genehmigt auch keine Rollen-, Scope-, Metadaten- oder Public-Key-Upgrades automatisch.
  * `gateway.nodes.allowCommands` / `gateway.nodes.denyCommands`: globale Allow-/Deny-Formung für deklarierte Node-Befehle nach Kopplung und Plattform-Allowlist-Auswertung. Verwenden Sie `allowCommands`, um gefährliche Node-Befehle wie `camera.snap`, `camera.clip` und `screen.record` explizit zuzulassen; `denyCommands` entfernt einen Befehl, selbst wenn ein Plattformstandard oder eine explizite Zulassung ihn sonst einschließen würde. Nachdem ein Node seine deklarierte Befehlsliste geändert hat, lehnen Sie diese Gerätekopplung ab und genehmigen Sie sie erneut, damit das Gateway den aktualisierten Befehls-Snapshot speichert.
  * `gateway.tools.deny`: zusätzliche Tool-Namen, die für HTTP `POST /tools/invoke` blockiert sind (erweitert die Standard-Deny-Liste).
  * `gateway.tools.allow`: Tool-Namen aus der Standard-HTTP-Deny-Liste entfernen.


### OpenAI-kompatible Endpunkte

  * Chat Completions: standardmäßig deaktiviert. Aktivieren mit `gateway.http.endpoints.chatCompletions.enabled: true`.
  * Responses API: `gateway.http.endpoints.responses.enabled`.
  * Responses-URL-Eingabehärtung: 
    * `gateway.http.endpoints.responses.maxUrlParts`
    * `gateway.http.endpoints.responses.files.urlAllowlist`
    * `gateway.http.endpoints.responses.images.urlAllowlist` Leere Allowlists werden als nicht gesetzt behandelt; verwenden Sie `gateway.http.endpoints.responses.files.allowUrl=false` und/oder `gateway.http.endpoints.responses.images.allowUrl=false`, um URL-Abrufe zu deaktivieren.
  * Optionaler Response-Härtungs-Header: 
    * `gateway.http.securityHeaders.strictTransportSecurity` (nur für HTTPS-Origins setzen, die Sie kontrollieren; siehe [Trusted-Proxy-Authentifizierung](</de/gateway/trusted-proxy-auth#tls-termination-and-hsts>))


### Multi-Instanz-Isolierung

Führen Sie mehrere Gateways auf einem Host mit eindeutigen Ports und State-Verzeichnissen aus:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json \OPENCLAW_STATE_DIR=~/.openclaw-a \openclaw gateway --port 19001
[/code]

Komfort-Flags: `--dev` (verwendet `~/.openclaw-dev` \+ Port `19001`), `--profile <name>` (verwendet `~/.openclaw-<name>`).

Siehe [Mehrere Gateways](</de/gateway/multiple-gateways>).

### `gateway.tls`

json5Copy code
[code]
    {  gateway: {    tls: {      enabled: false,      autoGenerate: false,      certPath: "/etc/openclaw/tls/server.crt",      keyPath: "/etc/openclaw/tls/server.key",      caPath: "/etc/openclaw/tls/ca-bundle.crt",    },  },}
[/code]

  * `enabled`: aktiviert TLS-Terminierung am Gateway-Listener (HTTPS/WSS) (Standard: `false`).
  * `autoGenerate`: erzeugt automatisch ein lokales selbstsigniertes Zertifikat/Schlüsselpaar, wenn keine expliziten Dateien konfiguriert sind; nur für lokale/Dev-Nutzung.
  * `certPath`: Dateisystempfad zur TLS-Zertifikatsdatei.
  * `keyPath`: Dateisystempfad zur privaten TLS-Schlüsseldatei; Berechtigungen restriktiv halten.
  * `caPath`: optionaler CA-Bundle-Pfad für Client-Verifizierung oder benutzerdefinierte Trust Chains.


### `gateway.reload`

json5Copy code
[code]
    {  gateway: {    reload: {      mode: "hybrid", // off | restart | hot | hybrid      debounceMs: 500,      deferralTimeoutMs: 300000,    },  },}
[/code]

  * `mode`: steuert, wie Konfigurationsänderungen zur Laufzeit angewendet werden. 
    * `"off"`: Live-Änderungen ignorieren; Änderungen erfordern einen expliziten Neustart.
    * `"restart"`: Gateway-Prozess bei Konfigurationsänderung immer neu starten.
    * `"hot"`: Änderungen im Prozess ohne Neustart anwenden.
    * `"hybrid"` (Standard): zuerst Hot Reload versuchen; bei Bedarf auf Neustart zurückfallen.
  * `debounceMs`: Debounce-Fenster in ms, bevor Konfigurationsänderungen angewendet werden (nichtnegative ganze Zahl).
  * `deferralTimeoutMs`: optionale maximale Wartezeit in ms für laufende Operationen, bevor ein Neustart oder Channel-Hot-Reload erzwungen wird. Weglassen, um die standardmäßige begrenzte Wartezeit (`300000`) zu verwenden; auf `0` setzen, um unbegrenzt zu warten und regelmäßig Warnungen zu noch ausstehenden Vorgängen zu protokollieren.


* * *

## Hooks

json5Copy code
[code]
    {  hooks: {    enabled: true,    token: "shared-secret",    path: "/hooks",    maxBodyBytes: 262144,    defaultSessionKey: "hook:ingress",    allowRequestSessionKey: true,    allowedSessionKeyPrefixes: ["hook:", "hook:gmail:"],    allowedAgentIds: ["hooks", "main"],    presets: ["gmail"],    transformsDir: "~/.openclaw/hooks/transforms",    mappings: [      {        match: { path: "gmail" },        action: "agent",        agentId: "hooks",        wakeMode: "now",        name: "Gmail",        sessionKey: "hook:gmail:{{messages[0].id}}",        messageTemplate: "From: {{messages[0].from}}\nSubject: {{messages[0].subject}}\n{{messages[0].snippet}}",        deliver: true,        channel: "last",        model: "openai/gpt-5.4-mini",      },    ],  },}
[/code]

Authentifizierung: `Authorization: Bearer <token>` oder `x-openclaw-token: <token>`. Hook-Tokens in Query-Strings werden abgelehnt.

Validierungs- und Sicherheitshinweise:

  * `hooks.enabled=true` erfordert ein nicht leeres `hooks.token`.
  * `hooks.token` muss sich von `gateway.auth.token` **unterscheiden** ; die Wiederverwendung des Gateway-Tokens wird abgelehnt.
  * `hooks.path` darf nicht `/` sein; verwenden Sie einen dedizierten Unterpfad wie `/hooks`.
  * Wenn `hooks.allowRequestSessionKey=true` ist, beschränken Sie `hooks.allowedSessionKeyPrefixes` (zum Beispiel `["hook:"]`).
  * Wenn eine Zuordnung oder Voreinstellung einen vorlagenbasierten `sessionKey` verwendet, setzen Sie `hooks.allowedSessionKeyPrefixes` und `hooks.allowRequestSessionKey=true`. Statische Zuordnungsschlüssel erfordern diese Aktivierung nicht.


**Endpunkte:**

  * `POST /hooks/wake` → `{ text, mode?: "now"|"next-heartbeat" }`
  * `POST /hooks/agent` → `{ message, name?, agentId?, sessionKey?, wakeMode?, deliver?, channel?, to?, model?, thinking?, timeoutSeconds? }`
    * `sessionKey` aus der Anfrage-Payload wird nur akzeptiert, wenn `hooks.allowRequestSessionKey=true` ist (Standard: `false`).
  * `POST /hooks/<name>` → wird über `hooks.mappings` aufgelöst 
    * Durch Vorlagen gerenderte Zuordnungswerte für `sessionKey` werden als extern bereitgestellt behandelt und erfordern ebenfalls `hooks.allowRequestSessionKey=true`.

Zuordnungsdetails

  * `match.path` entspricht dem Unterpfad nach `/hooks` (z. B. `/hooks/gmail` → `gmail`).
  * `match.source` entspricht einem Payload-Feld für generische Pfade.
  * Vorlagen wie `{{messages[0].subject}}` lesen aus der Payload.
  * `transform` kann auf ein JS/TS-Modul verweisen, das eine Hook-Aktion zurückgibt.
  * `transform.module` muss ein relativer Pfad sein und innerhalb von `hooks.transformsDir` bleiben (absolute Pfade und Traversal werden abgelehnt).
  * Behalten Sie `hooks.transformsDir` unter `~/.openclaw/hooks/transforms`; Workspace-Skills-Verzeichnisse werden abgelehnt. Wenn `openclaw doctor` diesen Pfad als ungültig meldet, verschieben Sie das Transform-Modul in das Hooks-Transform-Verzeichnis oder entfernen Sie `hooks.transformsDir`.
  * `agentId` leitet an einen bestimmten Agenten weiter; unbekannte IDs fallen auf den Standard zurück.
  * `allowedAgentIds`: beschränkt explizites Routing (`*` oder ausgelassen = alle erlauben, `[]` = alle verweigern).
  * `defaultSessionKey`: optionaler fester Sitzungsschlüssel für Hook-Agent-Ausführungen ohne expliziten `sessionKey`.
  * `allowRequestSessionKey`: erlaubt Aufrufern von `/hooks/agent` und vorlagengesteuerten Zuordnungssitzungsschlüsseln, `sessionKey` zu setzen (Standard: `false`).
  * `allowedSessionKeyPrefixes`: optionale Präfix-Allowlist für explizite `sessionKey`-Werte (Anfrage + Zuordnung), z. B. `["hook:"]`. Sie wird erforderlich, wenn eine Zuordnung oder Voreinstellung einen vorlagenbasierten `sessionKey` verwendet.
  * `deliver: true` sendet die finale Antwort an einen Kanal; `channel` ist standardmäßig `last`.
  * `model` überschreibt das LLM für diese Hook-Ausführung (muss erlaubt sein, wenn der Modellkatalog gesetzt ist).


### Gmail-Integration

  * Die integrierte Gmail-Voreinstellung verwendet `sessionKey: "hook:gmail:{{messages[0].id}}"`.
  * Wenn Sie dieses Routing pro Nachricht beibehalten, setzen Sie `hooks.allowRequestSessionKey: true` und beschränken Sie `hooks.allowedSessionKeyPrefixes` so, dass es zum Gmail-Namespace passt, zum Beispiel `["hook:", "hook:gmail:"]`.
  * Wenn Sie `hooks.allowRequestSessionKey: false` benötigen, überschreiben Sie die Voreinstellung mit einem statischen `sessionKey` statt mit dem vorlagenbasierten Standard.

json5Copy code
[code]
    {  hooks: {    gmail: {      account: "openclaw@gmail.com",      topic: "projects/<project-id>/topics/gog-gmail-watch",      subscription: "gog-gmail-watch-push",      pushToken: "shared-push-token",      hookUrl: "http://127.0.0.1:18789/hooks/gmail",      includeBody: true,      maxBytes: 20000,      renewEveryMinutes: 720,      serve: { bind: "127.0.0.1", port: 8788, path: "/" },      tailscale: { mode: "funnel", path: "/gmail-pubsub" },      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",      thinking: "off",    },  },}
[/code]

  * Gateway startet beim Booten automatisch `gog gmail watch serve`, wenn es konfiguriert ist. Setzen Sie `OPENCLAW_SKIP_GMAIL_WATCHER=1`, um dies zu deaktivieren.
  * Führen Sie kein separates `gog gmail watch serve` parallel zum Gateway aus.


* * *

## Canvas-Plugin-Host

json5Copy code
[code]
    {  plugins: {    entries: {      canvas: {        config: {          host: {            root: "~/.openclaw/workspace/canvas",            liveReload: true,            // enabled: false, // or OPENCLAW_SKIP_CANVAS_HOST=1          },        },      },    },  },}
[/code]

  * Stellt agentenbearbeitbares HTML/CSS/JS und A2UI per HTTP unter dem Gateway-Port bereit: 
    * `http://<gateway-host>:<gateway.port>/__openclaw__/canvas/`
    * `http://<gateway-host>:<gateway.port>/__openclaw__/a2ui/`
  * Nur lokal: Behalten Sie `gateway.bind: "loopback"` bei (Standard).
  * Nicht-Loopback-Bindings: Canvas-Routen erfordern Gateway-Authentifizierung (Token/Passwort/vertrauenswürdiger Proxy), genau wie andere Gateway-HTTP-Oberflächen.
  * Node-WebViews senden in der Regel keine Auth-Header; nachdem ein Node gekoppelt und verbunden ist, gibt der Gateway node-spezifische Capability-URLs für den Canvas-/A2UI-Zugriff bekannt.
  * Capability-URLs sind an die aktive Node-WS-Sitzung gebunden und laufen schnell ab. IP-basierter Fallback wird nicht verwendet.
  * Fügt den bereitgestellten HTML-Dateien einen Live-Reload-Client hinzu.
  * Erstellt automatisch eine Starterdatei `index.html`, wenn das Verzeichnis leer ist.
  * Stellt A2UI außerdem unter `/__openclaw__/a2ui/` bereit.
  * Änderungen erfordern einen Neustart des Gateway.
  * Deaktivieren Sie Live-Reload für große Verzeichnisse oder bei `EMFILE`-Fehlern.


* * *

## Discovery

### mDNS (Bonjour)

json5Copy code
[code]
    {  discovery: {    mdns: {      mode: "minimal", // minimal | full | off    },  },}
[/code]

  * `minimal` (Standard, wenn das gebündelte `bonjour`-Plugin aktiviert ist): lässt `cliPath` \+ `sshPort` aus TXT-Records weg.
  * `full`: schließt `cliPath` \+ `sshPort` ein; LAN-Multicast-Ankündigung erfordert weiterhin, dass das gebündelte `bonjour`-Plugin aktiviert ist.
  * `off`: unterdrückt LAN-Multicast-Ankündigung, ohne die Plugin-Aktivierung zu ändern.
  * Das gebündelte `bonjour`-Plugin startet automatisch auf macOS-Hosts und ist auf Linux, Windows und containerisierten Gateway-Bereitstellungen optional aktivierbar.
  * Der Hostname ist standardmäßig der System-Hostname, wenn er ein gültiges DNS-Label ist; andernfalls wird `openclaw` verwendet. Überschreiben Sie ihn mit `OPENCLAW_MDNS_HOSTNAME`.


### Weitbereich (DNS-SD)

json5Copy code
[code]
    {  discovery: {    wideArea: { enabled: true },  },}
[/code]

Schreibt eine Unicast-DNS-SD-Zone unter `~/.openclaw/dns/`. Für netzwerkübergreifende Discovery kombinieren Sie dies mit einem DNS-Server (CoreDNS empfohlen) + Tailscale Split-DNS.

Einrichtung: `openclaw dns setup --apply`.

* * *

## Umgebung

### `env` (Inline-Umgebungsvariablen)

json5Copy code
[code]
    {  env: {    OPENROUTER_API_KEY: "sk-or-...",    vars: {      GROQ_API_KEY: "gsk-...",    },    shellEnv: {      enabled: true,      timeoutMs: 15000,    },  },}
[/code]

  * Inline-Umgebungsvariablen werden nur angewendet, wenn in der Prozessumgebung der Schlüssel fehlt.
  * `.env`-Dateien: CWD `.env` \+ `~/.openclaw/.env` (keine davon überschreibt vorhandene Variablen).
  * `shellEnv`: importiert fehlende erwartete Schlüssel aus Ihrem Login-Shell-Profil.
  * Vollständige Vorrangregeln finden Sie unter [Umgebung](</de/help/environment>).


### Umgebungsvariablen-Ersetzung

Referenzieren Sie Umgebungsvariablen in beliebigen Konfigurationszeichenfolgen mit `${VAR_NAME}`:

json5Copy code
[code]
    {  gateway: {    auth: { token: "${OPENCLAW_GATEWAY_TOKEN}" },  },}
[/code]

  * Nur Namen in Großbuchstaben werden abgeglichen: `[A-Z_][A-Z0-9_]*`.
  * Fehlende/leere Variablen lösen beim Laden der Konfiguration einen Fehler aus.
  * Mit `$${VAR}` für ein literales `${VAR}` escapen.
  * Funktioniert mit `$include`.


* * *

## Secrets

Secret-Referenzen sind additiv: Klartextwerte funktionieren weiterhin.

### `SecretRef`

Verwenden Sie eine Objektform:

json5Copy code
[code]
    { source: "env" | "file" | "exec", provider: "default", id: "..." }
[/code]

Validierung:

  * `provider`-Muster: `^[a-z][a-z0-9_-]{0,63}$`
  * `source: "env"`-`id`-Muster: `^[A-Z][A-Z0-9_]{0,127}$`
  * `source: "file"`-`id`: absoluter JSON-Pointer (zum Beispiel `"/providers/openai/apiKey"`)
  * `source: "exec"`-`id`-Muster: `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$`
  * `source: "exec"`-`id`s dürfen keine durch Schrägstriche getrennten Pfadsegmente `.` oder `..` enthalten (zum Beispiel wird `a/../b` abgelehnt)


### Unterstützte Zugangsdatenoberfläche

  * Kanonische Matrix: [SecretRef-Zugangsdatenoberfläche](</de/reference/secretref-credential-surface>)
  * `secrets apply` zielt auf unterstützte `openclaw.json`-Zugangsdatenpfade ab.
  * `auth-profiles.json`-Referenzen sind in Runtime-Auflösung und Audit-Abdeckung enthalten.


### Konfiguration der Secret-Provider

json5Copy code
[code]
    {  secrets: {    providers: {      default: { source: "env" }, // optional explicit env provider      filemain: {        source: "file",        path: "~/.openclaw/secrets.json",        mode: "json",        timeoutMs: 5000,      },      vault: {        source: "exec",        command: "/usr/local/bin/openclaw-vault-resolver",        passEnv: ["PATH", "VAULT_ADDR"],      },    },    defaults: {      env: "default",      file: "filemain",      exec: "vault",    },  },}
[/code]

Hinweise:

  * Der `file`-Provider unterstützt `mode: "json"` und `mode: "singleValue"` (`id` muss im singleValue-Modus `"value"` sein).
  * Datei- und exec-Provider-Pfade schlagen geschlossen fehl, wenn die Windows-ACL-Verifizierung nicht verfügbar ist. Setzen Sie `allowInsecurePath: true` nur für vertrauenswürdige Pfade, die nicht verifiziert werden können.
  * Der `exec`-Provider erfordert einen absoluten `command`-Pfad und verwendet Protokoll-Payloads über stdin/stdout.
  * Standardmäßig werden Symlink-Befehlspfade abgelehnt. Setzen Sie `allowSymlinkCommand: true`, um Symlink-Pfade zuzulassen, während der aufgelöste Zielpfad validiert wird.
  * Wenn `trustedDirs` konfiguriert ist, wird die Prüfung vertrauenswürdiger Verzeichnisse auf den aufgelösten Zielpfad angewendet.
  * Die `exec`-Kindumgebung ist standardmäßig minimal; übergeben Sie erforderliche Variablen explizit mit `passEnv`.
  * Secret-Referenzen werden zur Aktivierungszeit in einen In-Memory-Snapshot aufgelöst; anschließend lesen Anfragepfade nur den Snapshot.
  * Während der Aktivierung wird eine Filterung aktiver Oberflächen angewendet: Nicht aufgelöste Referenzen auf aktivierten Oberflächen lassen Start/Neuladen fehlschlagen, während inaktive Oberflächen mit Diagnosen übersprungen werden.


* * *

## Auth-Speicher

json5Copy code
[code]
    {  auth: {    profiles: {      "anthropic:default": { provider: "anthropic", mode: "api_key" },      "anthropic:work": { provider: "anthropic", mode: "api_key" },      "openai-codex:personal": { provider: "openai-codex", mode: "oauth" },    },    order: {      anthropic: ["anthropic:default", "anthropic:work"],      "openai-codex": ["openai-codex:personal"],    },  },}
[/code]

  * Agent-spezifische Profile werden unter `<agentDir>/auth-profiles.json` gespeichert.
  * `auth-profiles.json` unterstützt Referenzen auf Wertebene (`keyRef` für `api_key`, `tokenRef` für `token`) für statische Zugangsdatenmodi.
  * Legacy-flache `auth-profiles.json`-Maps wie `{ "provider": { "apiKey": "..." } }` sind kein Runtime-Format; `openclaw doctor --fix` schreibt sie mit einem `.legacy-flat.*.bak`-Backup in kanonische `provider:default`-API-Schlüsselprofile um.
  * OAuth-Modus-Profile (`auth.profiles.<id>.mode = "oauth"`) unterstützen keine SecretRef-gestützten Auth-Profil-Zugangsdaten.
  * Statische Runtime-Zugangsdaten stammen aus im Arbeitsspeicher aufgelösten Snapshots; alte statische `auth.json`-Einträge werden bereinigt, wenn sie gefunden werden.
  * Legacy-OAuth-Importe aus `~/.openclaw/credentials/oauth.json`.
  * Siehe [OAuth](</de/concepts/oauth>).
  * Secrets-Runtime-Verhalten und `audit/configure/apply`-Werkzeuge: [Secrets-Verwaltung](</de/gateway/secrets>).


### `auth.cooldowns`

json5Copy code
[code]
    {  auth: {    cooldowns: {      billingBackoffHours: 5,      billingBackoffHoursByProvider: { anthropic: 3, openai: 8 },      billingMaxHours: 24,      authPermanentBackoffMinutes: 10,      authPermanentMaxMinutes: 60,      failureWindowHours: 24,      overloadedProfileRotations: 1,      overloadedBackoffMs: 0,      rateLimitedProfileRotations: 1,    },  },}
[/code]

  * `billingBackoffHours`: Basis-Backoff in Stunden, wenn ein Profil aufgrund echter Abrechnungs-/Guthaben-nicht-ausreichend-Fehler fehlschlägt (Standard: `5`). Expliziter Abrechnungstext kann auch bei `401`-/`403`-Antworten hier landen, aber Provider-spezifische Text- Matcher bleiben auf den Provider beschränkt, dem sie gehören (zum Beispiel OpenRouter `Key limit exceeded`). Wiederholbare HTTP-`402`-Meldungen zum Nutzungsfenster oder zu Ausgabenlimits für Organisation/Workspace bleiben stattdessen im `rate_limit`-Pfad.
  * `billingBackoffHoursByProvider`: optionale Overrides pro Provider für Abrechnungs-Backoff-Stunden.
  * `billingMaxHours`: Obergrenze in Stunden für das exponentielle Wachstum des Abrechnungs-Backoffs (Standard: `24`).
  * `authPermanentBackoffMinutes`: Basis-Backoff in Minuten für hochverlässliche `auth_permanent`-Fehler (Standard: `10`).
  * `authPermanentMaxMinutes`: Obergrenze in Minuten für das `auth_permanent`-Backoff-Wachstum (Standard: `60`).
  * `failureWindowHours`: rollierendes Zeitfenster in Stunden, das für Backoff-Zähler verwendet wird (Standard: `24`).
  * `overloadedProfileRotations`: maximale Rotationen von Auth-Profilen desselben Providers bei Überlastungsfehlern, bevor auf Modell-Fallback gewechselt wird (Standard: `1`). Provider-Auslastungsformen wie `ModelNotReadyException` landen hier.
  * `overloadedBackoffMs`: feste Verzögerung vor dem erneuten Versuch einer Rotation für überlasteten Provider/überlastetes Profil (Standard: `0`).
  * `rateLimitedProfileRotations`: maximale Rotationen von Auth-Profilen desselben Providers bei Rate-Limit-Fehlern, bevor auf Modell-Fallback gewechselt wird (Standard: `1`). Dieser Rate-Limit-Bucket umfasst Provider-geprägten Text wie `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached`, `workers_ai ... quota limit exceeded` und `resource exhausted`.


* * *

## Protokollierung

json5Copy code
[code]
    {  logging: {    level: "info",    file: "/tmp/openclaw/openclaw.log",    consoleLevel: "info",    consoleStyle: "pretty", // pretty | compact | json    redactSensitive: "tools", // off | tools    redactPatterns: ["\\bTOKEN\\b\\s*[=:]\\s*([\"']?)([^\\s\"']+)\\1"],  },}
[/code]

  * Standard-Logdatei: `/tmp/openclaw/openclaw-YYYY-MM-DD.log`.
  * Setzen Sie `logging.file` für einen stabilen Pfad.
  * `consoleLevel` wird bei `--verbose` auf `debug` angehoben.
  * `maxFileBytes`: maximale Größe der aktiven Logdatei in Byte vor der Rotation (positive Ganzzahl; Standard: `104857600` = 100 MB). OpenClaw behält bis zu fünf nummerierte Archive neben der aktiven Datei.
  * `redactSensitive` / `redactPatterns`: Best-Effort-Maskierung für Konsolenausgabe, Datei-Logs, OTLP-Logdatensätze und persistierten Sitzungstranskripttext. `redactSensitive: "off"` deaktiviert nur diese allgemeine Log-/Transkript-Richtlinie; UI-/Tool-/Diagnose-Sicherheitsflächen redigieren Geheimnisse weiterhin vor der Ausgabe.


* * *

## Diagnose

json5Copy code
[code]
    {  diagnostics: {    enabled: true,    flags: ["telegram.*"],    stuckSessionWarnMs: 30000,    stuckSessionAbortMs: 600000,     otel: {      enabled: false,      endpoint: "https://otel-collector.example.com:4318",      tracesEndpoint: "https://traces.example.com/v1/traces",      metricsEndpoint: "https://metrics.example.com/v1/metrics",      logsEndpoint: "https://logs.example.com/v1/logs",      protocol: "http/protobuf", // http/protobuf | grpc      headers: { "x-tenant-id": "my-org" },      serviceName: "openclaw-gateway",      traces: true,      metrics: true,      logs: false,      sampleRate: 1.0,      flushIntervalMs: 5000,      captureContent: {        enabled: false,        inputMessages: false,        outputMessages: false,        toolInputs: false,        toolOutputs: false,        systemPrompt: false,      },    },     cacheTrace: {      enabled: false,      filePath: "~/.openclaw/logs/cache-trace.jsonl",      includeMessages: true,      includePrompt: true,      includeSystem: true,    },  },}
[/code]

  * `enabled`: Hauptschalter für Instrumentierungsausgabe (Standard: `true`).
  * `flags`: Array von Flag-Strings, die gezielte Logausgabe aktivieren (unterstützt Wildcards wie `"telegram.*"` oder `"*"`).
  * `stuckSessionWarnMs`: Altersschwelle ohne Fortschritt in ms, um lang laufende Verarbeitungssitzungen als `session.long_running`, `session.stalled` oder `session.stuck` zu klassifizieren. Antwort, Tool, Status, Block und ACP-Fortschritt setzen den Timer zurück; wiederholte `session.stuck`-Diagnosen verwenden Backoff, solange unverändert.
  * `stuckSessionAbortMs`: Altersschwelle ohne Fortschritt in ms, bevor geeignete angehaltene aktive Arbeit zur Wiederherstellung abbruch-entleert werden darf. Wenn nicht gesetzt, verwendet OpenClaw das sicherere erweiterte Fenster für eingebettete Ausführung von mindestens 10 Minuten und 5x `stuckSessionWarnMs`.
  * `otel.enabled`: aktiviert die OpenTelemetry-Export-Pipeline (Standard: `false`). Die vollständige Konfiguration, den Signalkatalog und das Datenschutzmodell finden Sie unter [OpenTelemetry-Export](</de/gateway/opentelemetry>).
  * `otel.endpoint`: Collector-URL für OTel-Export.
  * `otel.tracesEndpoint` / `otel.metricsEndpoint` / `otel.logsEndpoint`: optionale signalspezifische OTLP-Endpunkte. Wenn gesetzt, überschreiben sie `otel.endpoint` nur für dieses Signal.
  * `otel.protocol`: `"http/protobuf"` (Standard) oder `"grpc"`.
  * `otel.headers`: zusätzliche HTTP-/gRPC-Metadaten-Header, die mit OTel-Exportanforderungen gesendet werden.
  * `otel.serviceName`: Dienstname für Ressourcenattribute.
  * `otel.traces` / `otel.metrics` / `otel.logs`: Trace-, Metrik- oder Logexport aktivieren.
  * `otel.sampleRate`: Trace-Sampling-Rate `0`-`1`.
  * `otel.flushIntervalMs`: periodisches Telemetrie-Flush-Intervall in ms.
  * `otel.captureContent`: Opt-in-Erfassung von Rohinhalten für OTEL-Span-Attribute. Standardmäßig deaktiviert. Boolesches `true` erfasst Nicht-System-Nachrichten-/Tool-Inhalte; die Objektform lässt Sie `inputMessages`, `outputMessages`, `toolInputs`, `toolOutputs` und `systemPrompt` explizit aktivieren.
  * `OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental`: Umgebungsumschalter für neueste experimentelle GenAI-Span-Provider-Attribute. Standardmäßig behalten Spans aus Kompatibilitätsgründen das Legacy-Attribut `gen_ai.system`; GenAI-Metriken verwenden begrenzte semantische Attribute.
  * `OPENCLAW_OTEL_PRELOADED=1`: Umgebungsumschalter für Hosts, die bereits ein globales OpenTelemetry-SDK registriert haben. OpenClaw überspringt dann Start/Shutdown des Plugin-eigenen SDK, während Diagnose-Listener aktiv bleiben.
  * `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`, `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` und `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`: signalspezifische Endpunkt-Umgebungsvariablen, die verwendet werden, wenn der passende Konfigurationsschlüssel nicht gesetzt ist.
  * `cacheTrace.enabled`: Cache-Trace-Snapshots für eingebettete Ausführungen protokollieren (Standard: `false`).
  * `cacheTrace.filePath`: Ausgabepfad für Cache-Trace-JSONL (Standard: `$OPENCLAW_STATE_DIR/logs/cache-trace.jsonl`).
  * `cacheTrace.includeMessages` / `includePrompt` / `includeSystem`: steuern, was in der Cache-Trace-Ausgabe enthalten ist (alle Standard: `true`).


* * *

## Update

json5Copy code
[code]
    {  update: {    channel: "stable", // stable | beta | dev    checkOnStart: true,     auto: {      enabled: false,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

  * `channel`: Release-Kanal für npm-/git-Installationen - `"stable"`, `"beta"` oder `"dev"`.
  * `checkOnStart`: beim Start des Gateways auf npm-Updates prüfen (Standard: `true`).
  * `auto.enabled`: automatische Hintergrundaktualisierung für Paketinstallationen aktivieren (Standard: `false`).
  * `auto.stableDelayHours`: Mindestverzögerung in Stunden vor automatischer Anwendung im Stable-Kanal (Standard: `6`; Maximum: `168`).
  * `auto.stableJitterHours`: zusätzliches Ausrollfenster für den Stable-Kanal in Stunden (Standard: `12`; Maximum: `168`).
  * `auto.betaCheckIntervalHours`: wie oft Prüfungen im Beta-Kanal in Stunden ausgeführt werden (Standard: `1`; Maximum: `24`).


* * *

## ACP

json5Copy code
[code]
    {  acp: {    enabled: true,    dispatch: { enabled: true },    backend: "acpx",    defaultAgent: "main",    allowedAgents: ["main", "ops"],    maxConcurrentSessions: 10,     stream: {      coalesceIdleMs: 50,      maxChunkChars: 1000,      repeatSuppression: true,      deliveryMode: "live", // live | final_only      hiddenBoundarySeparator: "paragraph", // none | space | newline | paragraph      maxOutputChars: 50000,      maxSessionUpdateChars: 500,    },     runtime: {      ttlMinutes: 30,    },  },}
[/code]

  * `enabled`: globales ACP-Feature-Gate (Standard: `true`; setzen Sie `false`, um ACP-Dispatch- und Spawn-Bedienelemente auszublenden).
  * `dispatch.enabled`: unabhängiges Gate für ACP-Sitzungs-Turn-Dispatch (Standard: `true`). Setzen Sie `false`, um ACP-Befehle verfügbar zu halten, aber die Ausführung zu blockieren.
  * `backend`: Standard-ACP-Runtime-Backend-ID (muss mit einem registrierten ACP-Runtime-Plugin übereinstimmen). Installieren Sie zuerst das Backend-Plugin, und wenn `plugins.allow` gesetzt ist, nehmen Sie die Backend-Plugin-ID auf (zum Beispiel `acpx`), sonst wird das ACP-Backend nicht geladen.
  * `defaultAgent`: Fallback-ACP-Ziel-Agent-ID, wenn Spawns kein explizites Ziel angeben.
  * `allowedAgents`: Allowlist von Agent-IDs, die für ACP-Runtime-Sitzungen zulässig sind; leer bedeutet keine zusätzliche Einschränkung.
  * `maxConcurrentSessions`: maximale Anzahl gleichzeitig aktiver ACP-Sitzungen.
  * `stream.coalesceIdleMs`: Idle-Flush-Fenster in ms für gestreamten Text.
  * `stream.maxChunkChars`: maximale Chunk-Größe vor dem Aufteilen der gestreamten Blockprojektion.
  * `stream.repeatSuppression`: wiederholte Status-/Tool-Zeilen pro Turn unterdrücken (Standard: `true`).
  * `stream.deliveryMode`: `"live"` streamt inkrementell; `"final_only"` puffert bis zu terminalen Turn-Ereignissen.
  * `stream.hiddenBoundarySeparator`: Trennzeichen vor sichtbarem Text nach verborgenen Tool-Ereignissen (Standard: `"paragraph"`).
  * `stream.maxOutputChars`: maximale Zeichenanzahl der Assistentenausgabe, die pro ACP-Turn projiziert wird.
  * `stream.maxSessionUpdateChars`: maximale Zeichenanzahl für projizierte ACP-Status-/Update-Zeilen.
  * `stream.tagVisibility`: Datensatz von Tag-Namen zu booleschen Sichtbarkeits-Overrides für gestreamte Ereignisse.
  * `runtime.ttlMinutes`: Idle-TTL in Minuten für ACP-Sitzungs-Worker vor möglicher Bereinigung.
  * `runtime.installCommand`: optionaler Installationsbefehl, der beim Bootstrapping einer ACP-Runtime-Umgebung ausgeführt wird.


* * *

## CLI

json5Copy code
[code]
    {  cli: {    banner: {      taglineMode: "off", // random | default | off    },  },}
[/code]

  * `cli.banner.taglineMode` steuert den Stil der Banner-Tagline: 
    * `"random"` (Standard): rotierende humorvolle/saisonale Taglines.
    * `"default"`: feste neutrale Tagline (`All your chats, one OpenClaw.`).
    * `"off"`: kein Tagline-Text (Banner-Titel/-Version werden weiterhin angezeigt).
  * Um das gesamte Banner auszublenden (nicht nur Taglines), setzen Sie die Umgebungsvariable `OPENCLAW_HIDE_BANNER=1`.


* * *

## Assistent

Metadaten, die von CLI-geführten Einrichtungsabläufen geschrieben werden (`onboard`, `configure`, `doctor`):

json5Copy code
[code]
    {  wizard: {    lastRunAt: "2026-01-01T00:00:00.000Z",    lastRunVersion: "2026.1.4",    lastRunCommit: "abc1234",    lastRunCommand: "configure",    lastRunMode: "local",  },}
[/code]

* * *

## Identität

Siehe `agents.list`-Identitätsfelder unter [Agent-Standardwerte](</de/gateway/config-agents#agent-defaults>).

* * *

## Bridge (Legacy, entfernt)

Aktuelle Builds enthalten die TCP-Bridge nicht mehr. Nodes verbinden sich über den Gateway-WebSocket. `bridge.*`-Schlüssel sind nicht mehr Teil des Konfigurationsschemas (Validierung schlägt fehl, bis sie entfernt werden; `openclaw doctor --fix` kann unbekannte Schlüssel entfernen).

Legacy-Bridge-Konfiguration (historische Referenz) jsonCopy code
[code]
    {"bridge": {  "enabled": true,  "port": 18790,  "bind": "tailnet",  "tls": {    "enabled": true,    "autoGenerate": true  }}}
[/code]

* * *

## Cron

json5Copy code
[code]
    {  cron: {    enabled: true,    maxConcurrentRuns: 2, // cron dispatch + isolated cron agent-turn execution    webhook: "https://example.invalid/legacy", // deprecated fallback for stored notify:true jobs    webhookToken: "replace-with-dedicated-token", // optional bearer token for outbound webhook auth    sessionRetention: "24h", // duration string or false    runLog: {      maxBytes: "2mb", // default 2_000_000 bytes      keepLines: 2000, // default 2000    },  },}
[/code]

  * `sessionRetention`: wie lange abgeschlossene isolierte Cron-Laufsitzungen aufbewahrt werden, bevor sie aus `sessions.json` entfernt werden. Steuert auch die Bereinigung archivierter gelöschter Cron-Transkripte. Standard: `24h`; auf `false` setzen, um dies zu deaktivieren.
  * `runLog.maxBytes`: maximale Größe pro Laufprotokolldatei (`cron/runs/<jobId>.jsonl`) vor dem Entfernen. Standard: `2_000_000` Byte.
  * `runLog.keepLines`: neueste Zeilen, die beibehalten werden, wenn das Entfernen des Laufprotokolls ausgelöst wird. Standard: `2000`.
  * `webhookToken`: Bearer-Token, der für die Cron-Webhook-POST-Zustellung (`delivery.mode = "webhook"`) verwendet wird; wenn er ausgelassen wird, wird kein Auth-Header gesendet.
  * `webhook`: veraltete Legacy-Fallback-Webhook-URL (http/https), die nur für gespeicherte Jobs verwendet wird, die noch `notify: true` haben.


### `cron.retry`

json5Copy code
[code]
    {  cron: {    retry: {      maxAttempts: 3,      backoffMs: [30000, 60000, 300000],      retryOn: ["rate_limit", "overloaded", "network", "timeout", "server_error"],    },  },}
[/code]

  * `maxAttempts`: maximale Wiederholungen für einmalige Jobs bei transienten Fehlern (Standard: `3`; Bereich: `0`-`10`).
  * `backoffMs`: Array von Backoff-Verzögerungen in ms für jeden Wiederholungsversuch (Standard: `[30000, 60000, 300000]`; 1-10 Einträge).
  * `retryOn`: Fehlertypen, die Wiederholungen auslösen - `"rate_limit"`, `"overloaded"`, `"network"`, `"timeout"`, `"server_error"`. Weglassen, um alle transienten Typen zu wiederholen.


Gilt nur für einmalige Cron-Jobs. Wiederkehrende Jobs verwenden eine separate Fehlerbehandlung.

### `cron.failureAlert`

json5Copy code
[code]
    {  cron: {    failureAlert: {      enabled: false,      after: 3,      cooldownMs: 3600000,      includeSkipped: false,      mode: "announce",      accountId: "main",    },  },}
[/code]

  * `enabled`: Fehleralarme für Cron-Jobs aktivieren (Standard: `false`).
  * `after`: aufeinanderfolgende Fehler, bevor ein Alarm ausgelöst wird (positive Ganzzahl, min.: `1`).
  * `cooldownMs`: Mindestanzahl von Millisekunden zwischen wiederholten Alarmen für denselben Job (nicht negative Ganzzahl).
  * `includeSkipped`: aufeinanderfolgende übersprungene Läufe auf den Alarmschwellenwert anrechnen (Standard: `false`). Übersprungene Läufe werden separat verfolgt und beeinflussen den Backoff bei Ausführungsfehlern nicht.
  * `mode`: Zustellmodus - `"announce"` sendet über eine Kanalnachricht; `"webhook"` postet an den konfigurierten Webhook.
  * `accountId`: optionale Konto- oder Kanal-ID zur Eingrenzung der Alarmzustellung.


### `cron.failureDestination`

json5Copy code
[code]
    {  cron: {    failureDestination: {      mode: "announce",      channel: "last",      to: "channel:C1234567890",      accountId: "main",    },  },}
[/code]

  * Standardziel für Cron-Fehlerbenachrichtigungen über alle Jobs hinweg.
  * `mode`: `"announce"` oder `"webhook"`; standardmäßig `"announce"`, wenn genügend Zieldaten vorhanden sind.
  * `channel`: Kanalüberschreibung für die Announce-Zustellung. `"last"` verwendet den zuletzt bekannten Zustellkanal wieder.
  * `to`: explizites Announce-Ziel oder Webhook-URL. Für den Webhook-Modus erforderlich.
  * `accountId`: optionale Kontoüberschreibung für die Zustellung.
  * `delivery.failureDestination` pro Job überschreibt diesen globalen Standard.
  * Wenn weder ein globales noch ein jobspezifisches Fehlerziel festgelegt ist, fallen Jobs, die bereits über `announce` zustellen, bei Fehlern auf dieses primäre Announce-Ziel zurück.
  * `delivery.failureDestination` wird nur für Jobs mit `sessionTarget="isolated"` unterstützt, es sei denn, das primäre `delivery.mode` des Jobs ist `"webhook"`.


Siehe [Cron-Jobs](</de/automation/cron-jobs>). Isolierte Cron-Ausführungen werden als [Hintergrundaufgaben](</de/automation/tasks>) verfolgt.

* * *

## Medienmodell-Template-Variablen

Template-Platzhalter, die in `tools.media.models[].args` erweitert werden:

Variable | Beschreibung  
---|---  
`{{Body}}` | Vollständiger eingehender Nachrichtentext  
`{{RawBody}}` | Rohtext (ohne Verlaufs-/Absender-Wrapper)  
`{{BodyStripped}}` | Text mit entfernten Gruppenerwähnungen  
`{{From}}` | Absenderkennung  
`{{To}}` | Zielkennung  
`{{MessageSid}}` | Kanalnachrichten-ID  
`{{SessionId}}` | Aktuelle Sitzungs-UUID  
`{{IsNewSession}}` | `"true"`, wenn eine neue Sitzung erstellt wurde  
`{{MediaUrl}}` | Eingehende Medien-Pseudo-URL  
`{{MediaPath}}` | Lokaler Medienpfad  
`{{MediaType}}` | Medientyp (Bild/Audio/Dokument/…)  
`{{Transcript}}` | Audiotranskript  
`{{Prompt}}` | Aufgelöster Medien-Prompt für CLI-Einträge  
`{{MaxChars}}` | Aufgelöste maximale Ausgabezeichen für CLI-Einträge  
`{{ChatType}}` | `"direct"` oder `"group"`  
`{{GroupSubject}}` | Gruppenthema (nach bestem Bemühen)  
`{{GroupMembers}}` | Vorschau der Gruppenmitglieder (nach bestem Bemühen)  
`{{SenderName}}` | Anzeigename des Absenders (nach bestem Bemühen)  
`{{SenderE164}}` | Telefonnummer des Absenders (nach bestem Bemühen)  
`{{Provider}}` | Provider-Hinweis (whatsapp, telegram, discord usw.)  
  
* * *

## Config-Includes (`$include`)

Config auf mehrere Dateien aufteilen:

json5Copy code
[code]
    // ~/.openclaw/openclaw.json{  gateway: { port: 18789 },  agents: { $include: "./agents.json5" },  broadcast: {    $include: ["./clients/mueller.json5", "./clients/schmidt.json5"],  },}
[/code]

**Merge-Verhalten:**

  * Einzelne Datei: ersetzt das enthaltende Objekt.
  * Array von Dateien: wird in der Reihenfolge tief zusammengeführt (spätere überschreiben frühere).
  * Geschwisterschlüssel: werden nach Includes zusammengeführt (überschreiben enthaltene Werte).
  * Verschachtelte Includes: bis zu 10 Ebenen tief.
  * Pfade: werden relativ zur einschließenden Datei aufgelöst, müssen aber innerhalb des obersten Config-Verzeichnisses (`dirname` von `openclaw.json`) bleiben. Absolute/`../`-Formen sind nur erlaubt, wenn sie weiterhin innerhalb dieser Grenze aufgelöst werden.
  * Schreibvorgänge im Besitz von OpenClaw, die nur einen obersten Abschnitt ändern, der durch ein Single-File-Include gestützt wird, schreiben in diese eingeschlossene Datei durch. Beispielsweise aktualisiert `plugins install` `plugins: { $include: "./plugins.json5" }` in `plugins.json5` und lässt `openclaw.json` unverändert.
  * Root-Includes, Include-Arrays und Includes mit Geschwisterüberschreibungen sind für Schreibvorgänge im Besitz von OpenClaw schreibgeschützt; diese Schreibvorgänge schlagen geschlossen fehl, statt die Config zu verflachen.
  * Fehler: klare Meldungen für fehlende Dateien, Parse-Fehler und zirkuläre Includes.


* * *

_Verwandt:[Konfiguration](</de/gateway/configuration>) · [Konfigurationsbeispiele](</de/gateway/configuration-examples>) · [Doctor](</de/gateway/doctor>)_

## Verwandt

  * [Konfiguration](</de/gateway/configuration>)
  * [Konfigurationsbeispiele](</de/gateway/configuration-examples>)


Was this useful?YesNo