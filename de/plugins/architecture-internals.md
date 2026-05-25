---
title: Interna der Plugin-Architektur
source_url: https://docs.openclaw.ai/de/plugins/architecture-internals
scraped_at: 2026-05-25
---

For das öffentliche Capability-Modell, Plugin-Formen und Ownership-/Ausführungs- verträge siehe [Plugin-Architektur](</de/plugins/architecture>). Diese Seite ist die Referenz für die internen Mechaniken: Lade-Pipeline, Registry, Runtime-Hooks, Gateway-HTTP-Routen, Importpfade und Schematabellen.

## Lade-Pipeline

Beim Start führt OpenClaw ungefähr Folgendes aus:

  1. Kandidaten für Plugin-Wurzeln entdecken
  2. native oder kompatible Bundle-Manifeste und Paketmetadaten lesen
  3. unsichere Kandidaten ablehnen
  4. Plugin-Konfiguration normalisieren (`plugins.enabled`, `allow`, `deny`, `entries`, `slots`, `load.paths`)
  5. Aktivierung für jeden Kandidaten entscheiden
  6. aktivierte native Module laden: gebaute gebündelte Module verwenden einen nativen Loader; lokaler TypeScript-Quellcode von Drittanbietern verwendet den Notfall-Jiti-Fallback
  7. native `register(api)`-Hooks aufrufen und Registrierungen in der Plugin-Registry sammeln
  8. die Registry für Befehle/Runtime-Oberflächen bereitstellen


Die Sicherheitsprüfungen erfolgen **vor** der Runtime-Ausführung. Kandidaten werden blockiert, wenn der Einstiegspunkt die Plugin-Wurzel verlässt, der Pfad weltweit beschreibbar ist oder die Pfad-Ownership für nicht gebündelte Plugins verdächtig wirkt.

Blockierte Kandidaten bleiben für Diagnosen mit ihrer Plugin-ID verknüpft. Wenn die Konfiguration diese ID weiterhin referenziert, meldet die Validierung das Plugin als vorhanden, aber blockiert, und verweist auf die Pfadsicherheitswarnung, statt den Konfigurationseintrag als veraltet zu behandeln.

### Manifest-zuerst-Verhalten

Das Manifest ist die Source of Truth der Control Plane. OpenClaw verwendet es, um:

  * das Plugin zu identifizieren
  * deklarierte Channels/Skills/Konfigurationsschemata oder Bundle-Capabilities zu entdecken
  * `plugins.entries.<id>.config` zu validieren
  * Beschriftungen/Platzhalter der Control UI zu ergänzen
  * Installations-/Katalogmetadaten anzuzeigen
  * günstige Aktivierungs- und Setup-Deskriptoren zu bewahren, ohne die Plugin-Runtime zu laden


Für native Plugins ist das Runtime-Modul der Data-Plane-Teil. Es registriert tatsächliches Verhalten wie Hooks, Tools, Befehle oder Provider-Flows.

Optionale Manifest-Blöcke `activation` und `setup` bleiben auf der Control Plane. Sie sind reine Metadaten-Deskriptoren für Aktivierungsplanung und Setup-Erkennung; sie ersetzen weder Runtime-Registrierung, `register(...)` noch `setupEntry`. Die ersten Live-Aktivierungskonsumenten verwenden jetzt Manifest-Hinweise zu Befehlen, Channels und Providern, um das Laden von Plugins vor einer breiteren Registry-Materialisierung einzugrenzen:

  * CLI-Ladevorgänge werden auf Plugins eingegrenzt, die den angeforderten primären Befehl besitzen
  * Channel-Setup/Plugin-Auflösung wird auf Plugins eingegrenzt, die die angeforderte Channel-ID besitzen
  * explizite Provider-Setup-/Runtime-Auflösung wird auf Plugins eingegrenzt, die die angeforderte Provider-ID besitzen
  * Gateway-Startplanung verwendet `activation.onStartup` für explizite Start-Imports und Start-Opt-outs; Plugins ohne Startmetadaten laden nur über engere Aktivierungsauslöser


Request-Time-Runtime-Preloads, die den breiten `all`-Scope anfordern, leiten weiterhin eine explizite effektive Plugin-ID-Menge aus Konfiguration, Startplanung, konfigurierten Channels, Slots und Auto-Enable-Regeln ab. Wenn diese abgeleitete Menge leer ist, lädt OpenClaw eine leere Runtime-Registry, statt auf jedes auffindbare Plugin zu erweitern.

Der Aktivierungsplaner stellt sowohl eine reine IDs-API für vorhandene Aufrufer als auch eine Plan-API für neue Diagnosen bereit. Planeinträge melden, warum ein Plugin ausgewählt wurde, und trennen explizite `activation.*`-Planerhinweise von Manifest-Ownership- Fallbacks wie `providers`, `channels`, `commandAliases`, `setup.providers`, `contracts.tools` und Hooks. Diese Trennung der Gründe ist die Kompatibilitätsgrenze: vorhandene Plugin-Metadaten funktionieren weiter, während neuer Code breite Hinweise oder Fallback-Verhalten erkennen kann, ohne die Runtime-Ladesemantik zu ändern.

Die Setup-Erkennung bevorzugt jetzt deskriptoreigene IDs wie `setup.providers` und `setup.cliBackends`, um Kandidaten-Plugins einzugrenzen, bevor sie auf `setup-api` für Plugins zurückfällt, die weiterhin Setup-Time-Runtime-Hooks benötigen. Provider- Setup-Listen verwenden Manifest-`providerAuthChoices`, aus Deskriptoren abgeleitete Setup- Auswahlen und Installationskatalog-Metadaten, ohne die Provider-Runtime zu laden. Explizites `setup.requiresRuntime: false` ist eine reine Deskriptor-Grenze; ein ausgelassenes `requiresRuntime` behält aus Kompatibilitätsgründen den Legacy-`setup-api`-Fallback bei. Wenn mehr als ein entdecktes Plugin dieselbe normalisierte Setup-Provider- oder CLI- Backend-ID beansprucht, verweigert die Setup-Suche den mehrdeutigen Owner, statt sich auf die Entdeckungsreihenfolge zu verlassen. Wenn Setup-Runtime ausgeführt wird, melden Registry-Diagnosen Abweichungen zwischen `setup.providers` / `setup.cliBackends` und den Providern oder CLI- Backends, die von setup-api registriert wurden, ohne Legacy-Plugins zu blockieren.

### Plugin-Cache-Grenze

OpenClaw cached Plugin-Erkennungsergebnisse oder direkte Manifest-Registry- Daten nicht hinter Wall-Clock-Fenstern. Installationen, Manifest-Bearbeitungen und Änderungen an Ladepfaden müssen beim nächsten expliziten Metadaten-Lesen oder Snapshot-Neuaufbau sichtbar werden. Der Manifest-Dateiparser darf einen begrenzten Dateisignatur-Cache behalten, der nach dem geöffneten Manifestpfad, Inode, Größe und Zeitstempeln geschlüsselt ist; dieser Cache vermeidet nur das erneute Parsen unveränderter Bytes und darf keine Erkennungs-, Registry-, Owner- oder Policy-Antworten cachen.

Der sichere schnelle Metadatenpfad ist explizite Objekt-Ownership, kein versteckter Cache. Gateway-Start-Hot-Paths sollten den aktuellen `PluginMetadataSnapshot`, die abgeleitete `PluginLookUpTable` oder eine explizite Manifest-Registry durch die Aufrufkette reichen. Konfigurationsvalidierung, Start-Auto-Enable, Plugin-Bootstrap und Provider- Auswahl können diese Objekte wiederverwenden, solange sie die aktuelle Konfiguration und das Plugin-Inventar repräsentieren. Die Setup-Suche rekonstruiert Manifest-Metadaten weiterhin bei Bedarf, sofern der spezifische Setup-Pfad keine explizite Manifest-Registry erhält; behalten Sie dies als Cold-Path-Fallback bei, statt versteckte Lookup-Caches hinzuzufügen. Wenn sich die Eingabe ändert, erstellen Sie den Snapshot neu und ersetzen ihn, statt ihn zu mutieren oder historische Kopien zu behalten. Views über die aktive Plugin-Registry und gebündelte Channel-Bootstrap-Helfer sollten aus der aktuellen Registry/Wurzel neu berechnet werden. Kurzlebige Maps sind innerhalb eines Aufrufs in Ordnung, um Arbeit zu deduplizieren oder Wiedereintritt zu schützen; sie dürfen nicht zu Prozess- Metadaten-Caches werden.

Für das Laden von Plugins ist die persistente Cache-Schicht das Runtime-Laden. Sie darf Loader-Zustand wiederverwenden, wenn Code oder installierte Artefakte tatsächlich geladen werden, etwa:

  * `PluginLoaderCacheState` und kompatible aktive Runtime-Registries
  * jiti-/Modul-Caches und Public-Surface-Loader-Caches, die verwendet werden, um wiederholtes Importieren derselben Runtime-Oberfläche zu vermeiden
  * Dateisystem-Caches für installierte Plugin-Artefakte
  * kurzlebige Maps pro Aufruf für Pfadnormalisierung oder Duplikatauflösung


Diese Caches sind Data-Plane-Implementierungsdetails. Sie dürfen keine Control-Plane-Fragen beantworten, wie etwa „welches Plugin besitzt diesen Provider?“, sofern der Aufrufer nicht ausdrücklich Runtime-Laden angefordert hat.

Fügen Sie keine persistenten oder Wall-Clock-Caches hinzu für:

  * Erkennungsergebnisse
  * direkte Manifest-Registries
  * Manifest-Registries, die aus dem installierten Plugin-Index rekonstruiert wurden
  * Provider-Owner-Lookup, Modellunterdrückung, Provider-Policy oder Public-Artifact- Metadaten
  * jede andere aus dem Manifest abgeleitete Antwort, bei der ein geändertes Manifest, ein installierter Index oder Ladepfad beim nächsten Metadaten-Lesen sichtbar sein sollte


Aufrufer, die Manifest-Metadaten aus dem persistierten installierten Plugin- Index neu aufbauen, rekonstruieren diese Registry bei Bedarf. Der installierte Index ist dauerhafter Source-Plane-Zustand; er ist kein versteckter In-Process-Metadaten-Cache.

## Registry-Modell

Geladene Plugins mutieren keine beliebigen Core-Globals direkt. Sie registrieren sich in einer zentralen Plugin-Registry.

Die Registry verfolgt:

  * Plugin-Einträge (Identität, Quelle, Ursprung, Status, Diagnosen)
  * Tools
  * Legacy-Hooks und typisierte Hooks
  * Channels
  * Provider
  * Gateway-RPC-Handler
  * HTTP-Routen
  * CLI-Registrare
  * Hintergrunddienste
  * Plugin-eigene Befehle


Core-Funktionen lesen dann aus dieser Registry, statt direkt mit Plugin-Modulen zu kommunizieren. Dadurch bleibt das Laden einseitig:

  * Plugin-Modul -> Registry-Registrierung
  * Core-Runtime -> Registry-Nutzung


Diese Trennung ist wichtig für die Wartbarkeit. Sie bedeutet, dass die meisten Core-Oberflächen nur einen Integrationspunkt benötigen: „die Registry lesen“, nicht „jedes Plugin-Modul speziell behandeln“.

## Conversation-Binding-Callbacks

Plugins, die eine Konversation binden, können reagieren, wenn eine Genehmigung aufgelöst wird.

Verwenden Sie `api.onConversationBindingResolved(...)`, um einen Callback zu erhalten, nachdem eine Bind- Anfrage genehmigt oder abgelehnt wurde:

tsCopy code
[code]
    export default {  id: "my-plugin",  register(api) {    api.onConversationBindingResolved(async (event) => {      if (event.status === "approved") {        // A binding now exists for this plugin + conversation.        console.log(event.binding?.conversationId);        return;      }       // The request was denied; clear any local pending state.      console.log(event.request.conversation.conversationId);    });  },};
[/code]

Callback-Payload-Felder:

  * `status`: `"approved"` oder `"denied"`
  * `decision`: `"allow-once"`, `"allow-always"` oder `"deny"`
  * `binding`: das aufgelöste Binding für genehmigte Anfragen
  * `request`: die ursprüngliche Anfragezusammenfassung, Detach-Hinweis, Sender-ID und Konversationsmetadaten


Dieser Callback dient nur der Benachrichtigung. Er ändert nicht, wer eine Konversation binden darf, und wird ausgeführt, nachdem die Core-Genehmigungsbehandlung abgeschlossen ist.

## Provider-Runtime-Hooks

Provider-Plugins haben drei Schichten:

  * **Manifest-Metadaten** für günstige Pre-Runtime-Lookups: `setup.providers[].envVars`, veraltete Kompatibilität `providerAuthEnvVars`, `providerAuthAliases`, `providerAuthChoices` und `channelEnvVars`.
  * **Config-Time-Hooks** : `catalog` (Legacy `discovery`) plus `applyConfigDefaults`.
  * **Runtime-Hooks** : mehr als 40 optionale Hooks für Authentifizierung, Modellauflösung, Stream-Wrapping, Denkstufen, Replay-Policy und Nutzungsendpunkte. Siehe die vollständige Liste unter Hook-Reihenfolge und Verwendung.


OpenClaw besitzt weiterhin den generischen Agent-Loop, Failover, Transcript-Behandlung und Tool-Policy. Diese Hooks sind die Erweiterungsoberfläche für Provider-spezifisches Verhalten, ohne einen vollständig eigenen Inferenztransport zu benötigen.

Verwenden Sie Manifest-`setup.providers[].envVars`, wenn der Provider env-basierte Anmeldeinformationen hat, die generische Auth-/Status-/Model-Picker-Pfade sehen sollten, ohne die Plugin-Runtime zu laden. Das veraltete `providerAuthEnvVars` wird während des Deprecation-Fensters weiterhin vom Kompatibilitätsadapter gelesen, und nicht gebündelte Plugins, die es verwenden, erhalten eine Manifest-Diagnose. Verwenden Sie Manifest-`providerAuthAliases`, wenn eine Provider-ID die env vars, Auth-Profile, konfigurationsgestützte Authentifizierung und API-Key-Onboarding-Auswahl einer anderen Provider-ID wiederverwenden sollte. Verwenden Sie Manifest- `providerAuthChoices`, wenn Onboarding-/Auth-Choice-CLI-Oberflächen die Choice-ID, Gruppenbeschriftungen und einfache One-Flag-Auth-Verdrahtung des Providers kennen sollten, ohne die Provider-Runtime zu laden. Behalten Sie Provider-Runtime- `envVars` für operatorbezogene Hinweise wie Onboarding-Beschriftungen oder OAuth- Client-ID-/Client-Secret-Setup-Variablen.

Verwenden Sie Manifest-`channelEnvVars`, wenn ein Channel env-gesteuerte Authentifizierung oder Setup hat, das generische Shell-Env-Fallbacks, Konfigurations-/Statusprüfungen oder Setup-Prompts sehen sollten, ohne die Channel-Runtime zu laden.

### Hook-Reihenfolge und Verwendung

Für Modell-/Provider-Plugins ruft OpenClaw Hooks ungefähr in dieser Reihenfolge auf. Die Spalte „Wann verwenden“ ist die schnelle Entscheidungshilfe. Kompatibilitäts-only-Provider-Felder, die OpenClaw nicht mehr aufruft, wie `ProviderPlugin.capabilities` und `suppressBuiltInModel`, werden hier absichtlich nicht aufgeführt.

# | Hook | Funktion | Wann verwenden  
---|---|---|---  
1 | `catalog` | Provider-Konfiguration während der `models.json`-Generierung in `models.providers` veröffentlichen | Provider besitzt einen Katalog oder Standardwerte für die Basis-URL  
2 | `applyConfigDefaults` | Provider-eigene globale Konfigurationsstandardwerte während der Konfigurationsmaterialisierung anwenden | Standardwerte hängen vom Auth-Modus, der Umgebung oder der Modellfamilien-Semantik des Providers ab  
\-- | _(integrierte Modellauflösung)_ | OpenClaw versucht zuerst den normalen Registry-/Katalogpfad | _(kein Plugin-Hook)_  
3 | `normalizeModelId` | Legacy- oder Preview-Modell-ID-Aliasse vor der Auflösung normalisieren | Provider ist für die Alias-Bereinigung vor der kanonischen Modellauflösung zuständig  
4 | `normalizeTransport` | Provider-Familien-`api` / `baseUrl` vor der generischen Modellassemblierung normalisieren | Provider ist für die Transport-Bereinigung für benutzerdefinierte Provider-IDs in derselben Transportfamilie zuständig  
5 | `normalizeConfig` | `models.providers.<id>` vor der Runtime-/Provider-Auflösung normalisieren | Provider benötigt Konfigurationsbereinigung, die beim Plugin liegen sollte; gebündelte Google-Familien-Helfer stützen außerdem unterstützte Google-Konfigurationseinträge ab  
6 | `applyNativeStreamingUsageCompat` | Native Kompatibilitätsumschreibungen für Streaming-Nutzungsdaten auf Konfigurations-Provider anwenden | Provider benötigt endpoint-gesteuerte Korrekturen für native Streaming-Nutzungsmetadaten  
7 | `resolveConfigApiKey` | Env-Marker-Authentifizierung für Konfigurations-Provider vor dem Laden der Runtime-Authentifizierung auflösen | Provider hat Provider-eigene Env-Marker-API-Schlüsselauflösung; `amazon-bedrock` hat hier außerdem einen integrierten AWS-Env-Marker-Resolver  
8 | `resolveSyntheticAuth` | Lokale/selbst gehostete oder konfigurationsgestützte Authentifizierung ohne Persistierung von Klartext offenlegen | Provider kann mit einem synthetischen/lokalen Zugangsdaten-Marker arbeiten  
9 | `resolveExternalAuthProfiles` | Provider-eigene externe Auth-Profile überlagern; Standard-`persistence` ist `runtime-only` für CLI-/App-eigene Zugangsdaten | Provider verwendet externe Auth-Zugangsdaten wieder, ohne kopierte Refresh-Token zu persistieren; `contracts.externalAuthProviders` im Manifest deklarieren  
10 | `shouldDeferSyntheticProfileAuth` | Gespeicherte synthetische Profil-Platzhalter hinter umgebungs-/konfigurationsgestützte Authentifizierung herabstufen | Provider speichert synthetische Platzhalterprofile, die keinen Vorrang erhalten sollen  
11 | `resolveDynamicModel` | Synchroner Fallback für Provider-eigene Modell-IDs, die noch nicht in der lokalen Registry sind | Provider akzeptiert beliebige Upstream-Modell-IDs  
12 | `prepareDynamicModel` | Asynchrones Warm-up, danach wird `resolveDynamicModel` erneut ausgeführt | Provider benötigt Netzwerkmetadaten, bevor unbekannte IDs aufgelöst werden  
13 | `normalizeResolvedModel` | Abschließende Umschreibung, bevor der eingebettete Runner das aufgelöste Modell verwendet | Provider benötigt Transport-Umschreibungen, verwendet aber weiterhin einen Kern-Transport  
14 | `contributeResolvedModelCompat` | Kompatibilitätsflags für Vendor-Modelle hinter einem anderen kompatiblen Transport beitragen | Provider erkennt eigene Modelle auf Proxy-Transporten, ohne den Provider zu übernehmen  
15 | `normalizeToolSchemas` | Tool-Schemas normalisieren, bevor der eingebettete Runner sie sieht | Provider benötigt Schema-Bereinigung für die Transportfamilie  
16 | `inspectToolSchemas` | Provider-eigene Schema-Diagnosen nach der Normalisierung offenlegen | Provider möchte Keyword-Warnungen, ohne dem Kern Provider-spezifische Regeln beizubringen  
17 | `resolveReasoningOutputMode` | Vertrag für native oder getaggte Reasoning-Ausgabe auswählen | Provider benötigt getaggte Reasoning-/finale Ausgabe statt nativer Felder  
18 | `prepareExtraParams` | Request-Parameter-Normalisierung vor generischen Stream-Options-Wrappern | Provider benötigt Standard-Request-Parameter oder Parameterbereinigung pro Provider  
19 | `createStreamFn` | Den normalen Stream-Pfad vollständig durch einen benutzerdefinierten Transport ersetzen | Provider benötigt ein benutzerdefiniertes Wire-Protokoll, nicht nur einen Wrapper  
20 | `wrapStreamFn` | Stream-Wrapper, nachdem generische Wrapper angewendet wurden | Provider benötigt Request-Header-/Body-/Modell-Kompatibilitätswrapper ohne benutzerdefinierten Transport  
21 | `resolveTransportTurnState` | Native Transport-Header oder Metadaten pro Turn anhängen | Provider möchte, dass generische Transporte Provider-native Turn-Identität senden  
22 | `resolveWebSocketSessionPolicy` | Native WebSocket-Header oder Session-Cool-down-Richtlinie anhängen | Provider möchte generische WS-Transporte für Session-Header oder Fallback-Richtlinien abstimmen  
23 | `formatApiKey` | Auth-Profil-Formatierer: gespeichertes Profil wird zur Runtime-`apiKey`-Zeichenfolge | Provider speichert zusätzliche Auth-Metadaten und benötigt eine benutzerdefinierte Runtime-Token-Form  
24 | `refreshOAuth` | OAuth-Refresh-Override für benutzerdefinierte Refresh-Endpunkte oder Richtlinien bei Refresh-Fehlern | Provider passt nicht zu den gemeinsamen `pi-ai`-Refreshern  
25 | `buildAuthDoctorHint` | Reparaturhinweis, der angehängt wird, wenn OAuth-Refresh fehlschlägt | Provider benötigt Provider-eigene Anleitung zur Auth-Reparatur nach Refresh-Fehler  
26 | `matchesContextOverflowError` | Provider-eigener Matcher für Kontextfenster-Überlauf | Provider hat rohe Überlauffehler, die generische Heuristiken übersehen würden  
27 | `classifyFailoverReason` | Provider-eigene Klassifizierung des Failover-Grunds | Provider kann rohe API-/Transportfehler auf Rate-Limit/Überlastung/usw. abbilden  
28 | `isCacheTtlEligible` | Prompt-Cache-Richtlinie für Proxy-/Backhaul-Provider | Provider benötigt Proxy-spezifisches Cache-TTL-Gating  
29 | `buildMissingAuthMessage` | Ersatz für die generische Wiederherstellungsnachricht bei fehlender Authentifizierung | Provider benötigt einen Provider-spezifischen Wiederherstellungshinweis bei fehlender Authentifizierung  
30 | `augmentModelCatalog` | Synthetische/abschließende Katalogzeilen, die nach der Discovery angehängt werden | Provider benötigt synthetische Forward-Compat-Zeilen in `models list` und Auswahloberflächen  
31 | `resolveThinkingProfile` | Modellspezifische `/think`-Stufengruppe, Anzeigelabels und Standardwert | Provider stellt für ausgewählte Modelle eine benutzerdefinierte Thinking-Leiter oder ein binäres Label bereit  
32 | `isBinaryThinking` | Kompatibilitäts-Hook für den Ein-/Aus-Schalter für Reasoning | Provider stellt Thinking nur binär ein/aus bereit  
33 | `supportsXHighThinking` | Kompatibilitäts-Hook für `xhigh`-Reasoning-Unterstützung | Provider möchte `xhigh` nur für eine Teilmenge von Modellen  
34 | `resolveDefaultThinkingLevel` | Kompatibilitäts-Hook für die standardmäßige `/think`-Stufe | Provider besitzt die standardmäßige `/think`-Richtlinie für eine Modellfamilie  
35 | `isModernModelRef` | Modern-Model-Matcher für Live-Profilfilter und Smoke-Auswahl | Provider besitzt das bevorzugte Live-/Smoke-Modell-Matching  
36 | `prepareRuntimeAuth` | Konfigurierte Zugangsdaten direkt vor der Inferenz in das eigentliche Runtime-Token/den eigentlichen Runtime-Schlüssel austauschen | Provider benötigt einen Token-Austausch oder kurzlebige Request-Zugangsdaten  
37 | `resolveUsageAuth` | Nutzungs-/Abrechnungszugangsdaten für `/usage` und verwandte Statusoberflächen auflösen | Provider benötigt benutzerdefinierte Analyse von Nutzungs-/Kontingent-Token oder andere Nutzungszugangsdaten  
38 | `fetchUsageSnapshot` | Provider-spezifische Nutzungs-/Kontingent-Snapshots abrufen und normalisieren, nachdem die Authentifizierung aufgelöst wurde | Provider benötigt einen Provider-spezifischen Nutzungsendpunkt oder Payload-Parser  
39 | `createEmbeddingProvider` | Einen Provider-eigenen Embedding-Adapter für Speicher/Suche erstellen | Das Verhalten von Speicher-Embeddings gehört in das Provider-Plugin  
40 | `buildReplayPolicy` | Eine Replay-Richtlinie zurückgeben, die die Transkriptverarbeitung für den Provider steuert | Provider benötigt eine benutzerdefinierte Transkriptrichtlinie (zum Beispiel Entfernen von Denkblöcken)  
41 | `sanitizeReplayHistory` | Replay-Verlauf nach generischer Transkriptbereinigung umschreiben | Provider benötigt Provider-spezifische Replay-Umschreibungen über gemeinsame Compaction-Hilfsfunktionen hinaus  
42 | `validateReplayTurns` | Abschließende Validierung oder Umformung von Replay-Turns vor dem eingebetteten Runner | Provider-Transport benötigt nach generischer Bereinigung strengere Turn-Validierung  
43 | `onModelSelected` | Provider-eigene Nebeneffekte nach der Auswahl ausführen | Provider benötigt Telemetrie oder Provider-eigenen Zustand, wenn ein Modell aktiv wird  
  
`normalizeModelId`, `normalizeTransport` und `normalizeConfig` prüfen zuerst das übereinstimmende Provider-Plugin und fallen dann auf andere Hook-fähige Provider-Plugins zurück, bis eines die Modell-ID oder den Transport/die Konfiguration tatsächlich ändert. Dadurch funktionieren Alias-/Kompatibilitäts- Provider-Shims weiter, ohne dass der Aufrufer wissen muss, welches mitgelieferte Plugin die Umschreibung besitzt. Wenn kein Provider-Hook einen unterstützten Konfigurationseintrag der Google-Familie umschreibt, wendet der mitgelieferte Google-Konfigurationsnormalisierer diese Kompatibilitätsbereinigung weiterhin an.

Wenn der Provider ein vollständig eigenes Wire-Protokoll oder einen eigenen Request Executor benötigt, ist das eine andere Klasse von Erweiterung. Diese Hooks sind für Provider-Verhalten gedacht, das weiterhin in der normalen Inferenzschleife von OpenClaw läuft.

### Provider-Beispiel

tsCopy code
[code]
    api.registerProvider({  id: "example-proxy",  label: "Example Proxy",  auth: [],  catalog: {    order: "simple",    run: async (ctx) => {      const apiKey = ctx.resolveProviderApiKey("example-proxy").apiKey;      if (!apiKey) {        return null;      }      return {        provider: {          baseUrl: "https://proxy.example.com/v1",          apiKey,          api: "openai-completions",          models: [{ id: "auto", name: "Auto" }],        },      };    },  },  resolveDynamicModel: (ctx) => ({    id: ctx.modelId,    name: ctx.modelId,    provider: "example-proxy",    api: "openai-completions",    baseUrl: "https://proxy.example.com/v1",    reasoning: false,    input: ["text"],    cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },    contextWindow: 128000,    maxTokens: 8192,  }),  prepareRuntimeAuth: async (ctx) => {    const exchanged = await exchangeToken(ctx.apiKey);    return {      apiKey: exchanged.token,      baseUrl: exchanged.baseUrl,      expiresAt: exchanged.expiresAt,    };  },  resolveUsageAuth: async (ctx) => {    const auth = await ctx.resolveOAuthToken();    return auth ? { token: auth.token } : null;  },  fetchUsageSnapshot: async (ctx) => {    return await fetchExampleProxyUsage(ctx.token, ctx.timeoutMs, ctx.fetchFn);  },});
[/code]

### Integrierte Beispiele

Mitgelieferte Provider-Plugins kombinieren die obigen Hooks, um Katalog-, Authentifizierungs-, Denk-, Replay- und Nutzungsanforderungen der jeweiligen Anbieter abzubilden. Der maßgebliche Hook-Satz liegt bei jedem Plugin unter `extensions/`; diese Seite veranschaulicht die Formen, statt die Liste zu spiegeln.

Pass-through catalog providers

OpenRouter, Kilocode, [Z.AI](<http://Z.AI>) und xAI registrieren `catalog` plus `resolveDynamicModel` / `prepareDynamicModel`, damit sie Upstream- Modell-IDs vor dem statischen Katalog von OpenClaw verfügbar machen können.

OAuth and usage endpoint providers

GitHub Copilot, Gemini CLI, ChatGPT Codex, MiniMax, Xiaomi und [z.ai](<http://z.ai>) kombinieren `prepareRuntimeAuth` oder `formatApiKey` mit `resolveUsageAuth` \+ `fetchUsageSnapshot`, um Token-Austausch und `/usage`-Integration zu besitzen.

Replay and transcript cleanup families

Gemeinsame benannte Familien (`google-gemini`, `passthrough-gemini`, `anthropic-by-model`, `hybrid-anthropic-openai`) lassen Provider über `buildReplayPolicy` in Transkript-Richtlinien einsteigen, statt dass jedes Plugin die Bereinigung erneut implementiert.

Catalog-only providers

`byteplus`, `cloudflare-ai-gateway`, `huggingface`, `kimi-coding`, `nvidia`, `qianfan`, `synthetic`, `together`, `venice`, `vercel-ai-gateway` und `volcengine` registrieren nur `catalog` und nutzen die gemeinsame Inferenzschleife.

Anthropic-specific stream helpers

Beta-Header, `/fast` / `serviceTier` und `context1m` leben in der öffentlichen `api.ts`-/`contract-api.ts`-Schnittstelle des Anthropic-Plugins (`wrapAnthropicProviderStream`, `resolveAnthropicBetas`, `resolveAnthropicFastMode`, `resolveAnthropicServiceTier`) statt im generischen SDK.

## Runtime-Helfer

Plugins können über `api.runtime` auf ausgewählte Core-Helfer zugreifen. Für TTS:

tsCopy code
[code]
    const clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); const result = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); const voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Hinweise:

  * `textToSpeech` gibt die normale Core-TTS-Ausgabepayload für Datei-/Sprachnotiz-Oberflächen zurück.
  * Verwendet die Core-Konfiguration `messages.tts` und die Provider-Auswahl.
  * Gibt PCM-Audiopuffer + Abtastrate zurück. Plugins müssen für Provider resamplen/codieren.
  * `listVoices` ist je Provider optional. Verwenden Sie es für anbieterverwaltete Stimmauswahlen oder Einrichtungsabläufe.
  * Stimmlisten können reichere Metadaten wie Spracheinstellung, Geschlecht und Persönlichkeits-Tags für Provider-bewusste Auswahlen enthalten.
  * OpenAI und ElevenLabs unterstützen heute Telefonie. Microsoft nicht.


Plugins können auch Speech-Provider über `api.registerSpeechProvider(...)` registrieren.

tsCopy code
[code]
    api.registerSpeechProvider({  id: "acme-speech",  label: "Acme Speech",  isConfigured: ({ config }) => Boolean(config.messages?.tts),  synthesize: async (req) => {    return {      audioBuffer: Buffer.from([]),      outputFormat: "mp3",      fileExtension: ".mp3",      voiceCompatible: false,    };  },});
[/code]

Hinweise:

  * Belassen Sie TTS-Richtlinie, Fallback und Antwortzustellung im Core.
  * Verwenden Sie Speech-Provider für anbieterverwaltetes Syntheseverhalten.
  * Die ältere Microsoft-`edge`-Eingabe wird auf die Provider-ID `microsoft` normalisiert.
  * Das bevorzugte Besitzmodell ist unternehmensorientiert: Ein Anbieter-Plugin kann Text-, Speech-, Bild- und zukünftige Medien-Provider besitzen, wenn OpenClaw diese Fähigkeitsverträge hinzufügt.


Für Bild-/Audio-/Videoverstehen registrieren Plugins einen typisierten Medienverständnis-Provider statt einer generischen Key/Value-Bag:

tsCopy code
[code]
    api.registerMediaUnderstandingProvider({  id: "google",  capabilities: ["image", "audio", "video"],  describeImage: async (req) => ({ text: "..." }),  transcribeAudio: async (req) => ({ text: "..." }),  describeVideo: async (req) => ({ text: "..." }),});
[/code]

Hinweise:

  * Belassen Sie Orchestrierung, Fallback, Konfiguration und Channel-Verdrahtung im Core.
  * Belassen Sie Anbieterverhalten im Provider-Plugin.
  * Additive Erweiterung sollte typisiert bleiben: neue optionale Methoden, neue optionale Ergebnisfelder, neue optionale Fähigkeiten.
  * Videogenerierung folgt bereits demselben Muster: 
    * Core besitzt den Fähigkeitsvertrag und den Runtime-Helfer
    * Anbieter-Plugins registrieren `api.registerVideoGenerationProvider(...)`
    * Feature-/Channel-Plugins nutzen `api.runtime.videoGeneration.*`


Für Medienverständnis-Runtime-Helfer können Plugins Folgendes aufrufen:

tsCopy code
[code]
    const image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); const video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); const extraction = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Use the printed fields as the source of truth." },  ],  instructions: "Return entities and searchable tags.",  schemaName: "example.evidence",  jsonSchema: {    type: "object",    properties: {      entities: { type: "array", items: { type: "string" } },      tags: { type: "array", items: { type: "string" } },    },  },  cfg: api.config,});
[/code]

Für Audiotranskription können Plugins entweder die Medienverständnis-Runtime oder den älteren STT-Alias verwenden:

tsCopy code
[code]
    const { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  // Optional when MIME cannot be inferred reliably:  mime: "audio/ogg",});
[/code]

Hinweise:

  * `api.runtime.mediaUnderstanding.*` ist die bevorzugte gemeinsame Oberfläche für Bild-/Audio-/Videoverstehen.
  * `extractStructuredWithModel(...)` ist die Plugin-seitige Schnittstelle für begrenzte, Provider-eigene, bildzentrierte Extraktion. Fügen Sie mindestens eine Bildeingabe hinzu; Texteingaben sind ergänzender Kontext. Produkt-Plugins besitzen ihre Routen und Schemas, während OpenClaw die Provider-/Runtime-Grenze besitzt.
  * Verwendet die Core-Audiokonfiguration für Medienverständnis (`tools.media.audio`) und die Provider-Fallback-Reihenfolge.
  * Gibt `{ text: undefined }` zurück, wenn keine Transkriptionsausgabe erzeugt wird (zum Beispiel bei übersprungener/nicht unterstützter Eingabe).
  * `api.runtime.stt.transcribeAudioFile(...)` bleibt als Kompatibilitätsalias erhalten.


Plugins können Hintergrund-Subagent-Läufe auch über `api.runtime.subagent` starten:

tsCopy code
[code]
    const result = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai",  model: "gpt-4.1-mini",  deliver: false,});
[/code]

Hinweise:

  * `provider` und `model` sind optionale Overrides pro Lauf, keine dauerhaften Sitzungsänderungen.
  * OpenClaw berücksichtigt diese Override-Felder nur für vertrauenswürdige Aufrufer.
  * Für Plugin-eigene Fallback-Läufe müssen Operatoren mit `plugins.entries.<id>.subagent.allowModelOverride: true` zustimmen.
  * Verwenden Sie `plugins.entries.<id>.subagent.allowedModels`, um vertrauenswürdige Plugins auf bestimmte kanonische `provider/model`-Ziele zu beschränken, oder `"*"`, um jedes Ziel ausdrücklich zu erlauben.
  * Subagent-Läufe nicht vertrauenswürdiger Plugins funktionieren weiterhin, aber Override-Anforderungen werden abgelehnt, statt stillschweigend zurückzufallen.
  * Von Plugins erstellte Subagent-Sitzungen werden mit der erstellenden Plugin-ID markiert. Der Fallback `api.runtime.subagent.deleteSession(...)` darf nur diese eigenen Sitzungen löschen; beliebiges Löschen von Sitzungen erfordert weiterhin eine administrativ begrenzte Gateway-Anforderung.


Für Websuche können Plugins den gemeinsamen Runtime-Helfer verwenden, statt in die Agent-Tool-Verdrahtung zu greifen:

tsCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({  config: api.config,}); const result = await api.runtime.webSearch.search({  config: api.config,  args: {    query: "OpenClaw plugin runtime helpers",    count: 5,  },});
[/code]

Plugins können auch Websuche-Provider über `api.registerWebSearchProvider(...)` registrieren.

Hinweise:

  * Belassen Sie Provider-Auswahl, Auflösung von Zugangsdaten und gemeinsame Anfragesemantik im Core.
  * Verwenden Sie Websuche-Provider für anbieterspezifische Suchtransporte.
  * `api.runtime.webSearch.*` ist die bevorzugte gemeinsame Oberfläche für Feature-/Channel-Plugins, die Suchverhalten benötigen, ohne vom Agent-Tool-Wrapper abzuhängen.


### `api.runtime.imageGeneration`

tsCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  config: api.config,  args: { prompt: "A friendly lobster mascot", size: "1024x1024" },}); const providers = api.runtime.imageGeneration.listProviders({  config: api.config,});
[/code]

  * `generate(...)`: generiert ein Bild mithilfe der konfigurierten Bildgenerierungs-Provider-Kette.
  * `listProviders(...)`: listet verfügbare Bildgenerierungs-Provider und ihre Fähigkeiten auf.


## Gateway-HTTP-Routen

Plugins können HTTP-Endpunkte mit `api.registerHttpRoute(...)` bereitstellen.

tsCopy code
[code]
    api.registerHttpRoute({  path: "/acme/webhook",  auth: "plugin",  match: "exact",  handler: async (_req, res) => {    res.statusCode = 200;    res.end("ok");    return true;  },});
[/code]

Routenfelder:

  * `path`: Routenpfad unter dem Gateway-HTTP-Server.
  * `auth`: erforderlich. Verwenden Sie `"gateway"`, um normale Gateway-Authentifizierung zu verlangen, oder `"plugin"` für Plugin-verwaltete Authentifizierung/Webhook-Verifizierung.
  * `match`: optional. `"exact"` (Standard) oder `"prefix"`.
  * `replaceExisting`: optional. Ermöglicht demselben Plugin, seine eigene vorhandene Routenregistrierung zu ersetzen.
  * `handler`: gibt `true` zurück, wenn die Route die Anfrage verarbeitet hat.


Hinweise:

  * `api.registerHttpHandler(...)` wurde entfernt und verursacht einen Fehler beim Laden des Plugins. Verwenden Sie stattdessen `api.registerHttpRoute(...)`.
  * Plugin-Routen müssen `auth` explizit deklarieren.
  * Exakte `path + match`-Konflikte werden abgelehnt, sofern nicht `replaceExisting: true` gesetzt ist, und ein Plugin kann nicht die Route eines anderen Plugins ersetzen.
  * Überlappende Routen mit unterschiedlichen `auth`-Stufen werden abgelehnt. Halten Sie `exact`-/`prefix`-Fallthrough-Ketten nur auf derselben Authentifizierungsstufe.
  * `auth: "plugin"`-Routen erhalten Operator-Laufzeit-Scopes **nicht** automatisch. Sie sind für Plugin-verwaltete Webhooks/Signaturprüfung gedacht, nicht für privilegierte Gateway-Hilfsaufrufe.
  * `auth: "gateway"`-Routen laufen innerhalb eines Gateway-Anforderungs-Laufzeit-Scopes, aber dieser Scope ist absichtlich konservativ: 
    * Shared-Secret-Bearer-Authentifizierung (`gateway.auth.mode = "token"` / `"password"`) fixiert die Laufzeit-Scopes von Plugin-Routen auf `operator.write`, selbst wenn der Aufrufer `x-openclaw-scopes` sendet
    * vertrauenswürdige identitätstragende HTTP-Modi (zum Beispiel `trusted-proxy` oder `gateway.auth.mode = "none"` an einem privaten Ingress) berücksichtigen `x-openclaw-scopes` nur, wenn der Header explizit vorhanden ist
    * wenn `x-openclaw-scopes` bei solchen identitätstragenden Plugin-Routen-Anforderungen fehlt, fällt der Laufzeit-Scope auf `operator.write` zurück
  * Praktische Regel: Gehen Sie nicht davon aus, dass eine Gateway-authentifizierte Plugin-Route implizit eine Admin-Oberfläche ist. Wenn Ihre Route Admin-exklusives Verhalten benötigt, verlangen Sie einen identitätstragenden Authentifizierungsmodus und dokumentieren Sie den expliziten Header-Vertrag für `x-openclaw-scopes`.


## Plugin-SDK-Importpfade

Verwenden Sie beim Erstellen neuer Plugins schmale SDK-Unterpfade statt des monolithischen Root-Barrels `openclaw/plugin-sdk`. Zentrale Unterpfade:

Unterpfad | Zweck  
---|---  
`openclaw/plugin-sdk/plugin-entry` | Primitive für die Plugin-Registrierung  
`openclaw/plugin-sdk/channel-core` | Channel-Einstiegs-/Build-Helfer  
`openclaw/plugin-sdk/core` | Generische gemeinsame Helfer und Rahmenvertrag  
`openclaw/plugin-sdk/config-schema` | Zod-Schema für Root-`openclaw.json` (`OpenClawSchema`)  
  
Channel-Plugins wählen aus einer Familie schmaler Schnittstellen: `channel-setup`, `setup-runtime`, `setup-tools`, `channel-pairing`, `channel-contract`, `channel-feedback`, `channel-inbound`, `channel-lifecycle`, `channel-reply-pipeline`, `command-auth`, `secret-input`, `webhook-ingress`, `channel-targets` und `channel-actions`. Genehmigungsverhalten sollte auf einen einzigen `approvalCapability`-Vertrag konsolidiert werden, statt unzusammenhängende Plugin-Felder zu mischen. Siehe [Channel-Plugins](</de/plugins/sdk-channel-plugins>).

Laufzeit- und Konfigurationshelfer befinden sich unter passenden fokussierten `*-runtime`-Unterpfaden (`approval-runtime`, `agent-runtime`, `lazy-runtime`, `directory-runtime`, `text-runtime`, `runtime-store`, `system-event-runtime`, `heartbeat-runtime`, `channel-activity-runtime` usw.). Bevorzugen Sie `config-contracts`, `plugin-config-runtime`, `runtime-config-snapshot` und `config-mutation` statt des breiten Kompatibilitäts-Barrels `config-runtime`.

Repo-interne Einstiegspunkte (je gebündeltem Plugin-Paket-Root):

  * `index.js` — Einstieg für gebündelte Plugins
  * `api.js` — Barrel für Helfer/Typen
  * `runtime-api.js` — nur Laufzeit-Barrel
  * `setup-entry.js` — Einstieg für Setup-Plugin


Externe Plugins sollten nur `openclaw/plugin-sdk/*`-Unterpfade importieren. Importieren Sie niemals `src/*` eines anderen Plugin-Pakets aus dem Core oder aus einem anderen Plugin. Per Fassade geladene Einstiegspunkte bevorzugen den aktiven Laufzeit-Konfigurations-Snapshot, wenn einer existiert, und fallen dann auf die aufgelöste Konfigurationsdatei auf der Festplatte zurück.

Capability-spezifische Unterpfade wie `image-generation`, `media-understanding` und `speech` existieren, weil gebündelte Plugins sie heute verwenden. Sie sind nicht automatisch langfristig eingefrorene externe Verträge. Prüfen Sie die relevante SDK- Referenzseite, wenn Sie sich auf sie verlassen.

## Message-Tool-Schemas

Plugins sollten Channel-spezifische `describeMessageTool(...)`-Schema- Beiträge für Nicht-Nachrichten-Primitive wie Reaktionen, Lesebestätigungen und Umfragen besitzen. Gemeinsame Sende-Darstellung sollte den generischen `MessagePresentation`-Vertrag statt Provider-nativer Button-, Komponenten-, Block- oder Kartenfelder verwenden. Siehe [Message Presentation](</de/plugins/message-presentation>) für den Vertrag, Fallback-Regeln, Provider-Zuordnung und die Checkliste für Plugin-Autoren.

Sendefähige Plugins deklarieren über Nachrichten-Capabilities, was sie rendern können:

  * `presentation` für semantische Darstellungsblöcke (`text`, `context`, `divider`, `buttons`, `select`)
  * `delivery-pin` für angepinnte Zustellungsanforderungen


Core entscheidet, ob die Darstellung nativ gerendert oder zu Text herabgestuft wird. Legen Sie keine Provider-nativen UI-Ausweichpfade über das generische Message-Tool offen. Veraltete SDK-Helfer für ältere native Schemas bleiben für bestehende Drittanbieter-Plugins exportiert, aber neue Plugins sollten sie nicht verwenden.

## Channel-Zielauflösung

Channel-Plugins sollten Channel-spezifische Zielsemantik besitzen. Halten Sie den gemeinsamen Outbound-Host generisch und verwenden Sie die Messaging-Adapter-Oberfläche für Provider-Regeln:

  * `messaging.inferTargetChatType({ to })` entscheidet, ob ein normalisiertes Ziel vor der Verzeichnissuche als `direct`, `group` oder `channel` behandelt werden soll.
  * `messaging.targetResolver.looksLikeId(raw, normalized)` teilt dem Core mit, ob eine Eingabe direkt zur ID-artigen Auflösung springen soll, statt die Verzeichnissuche zu verwenden.
  * `messaging.targetResolver.resolveTarget(...)` ist der Plugin-Fallback, wenn der Core nach der Normalisierung oder nach einem Verzeichnisfehlschlag eine abschließende Provider-eigene Auflösung benötigt.
  * `messaging.resolveOutboundSessionRoute(...)` übernimmt die Provider-spezifische Session- Routenerstellung, sobald ein Ziel aufgelöst ist.


Empfohlene Aufteilung:

  * Verwenden Sie `inferTargetChatType` für Kategorieentscheidungen, die vor dem Suchen von Peers/Gruppen stattfinden sollen.
  * Verwenden Sie `looksLikeId` für Prüfungen vom Typ „dies als explizite/native Ziel-ID behandeln“.
  * Verwenden Sie `resolveTarget` für Provider-spezifischen Normalisierungs-Fallback, nicht für breite Verzeichnissuche.
  * Halten Sie Provider-native IDs wie Chat-IDs, Thread-IDs, JIDs, Handles und Room- IDs innerhalb von `target`-Werten oder Provider-spezifischen Parametern, nicht in generischen SDK- Feldern.


## Konfigurationsgestützte Verzeichnisse

Plugins, die Verzeichniseinträge aus der Konfiguration ableiten, sollten diese Logik im Plugin behalten und die gemeinsamen Helfer aus `openclaw/plugin-sdk/directory-runtime` wiederverwenden.

Verwenden Sie dies, wenn ein Channel konfigurationsgestützte Peers/Gruppen benötigt, etwa:

  * durch Allowlist gesteuerte DM-Peers
  * konfigurierte Channel-/Gruppen-Zuordnungen
  * kontoabhängige statische Verzeichnis-Fallbacks


Die gemeinsamen Helfer in `directory-runtime` behandeln nur generische Operationen:

  * Abfragefilterung
  * Anwendung von Limits
  * Deduplizierungs-/Normalisierungshelfer
  * Erstellen von `ChannelDirectoryEntry[]`


Channel-spezifische Kontoinspektion und ID-Normalisierung sollten in der Plugin-Implementierung bleiben.

## Provider-Kataloge

Provider-Plugins können Modellkataloge für Inferenz mit `registerProvider({ catalog: { run(...) { ... } } })` definieren.

`catalog.run(...)` gibt dieselbe Form zurück, die OpenClaw in `models.providers` schreibt:

  * `{ provider }` für einen Provider-Eintrag
  * `{ providers }` für mehrere Provider-Einträge


Verwenden Sie `catalog`, wenn das Plugin Provider-spezifische Modell-IDs, Basis-URL- Voreinstellungen oder authentifizierungsgeschützte Modellmetadaten besitzt.

`catalog.order` steuert, wann der Katalog eines Plugins relativ zu den eingebauten impliziten Providern von OpenClaw zusammengeführt wird:

  * `simple`: einfache API-Key- oder umgebungsgetriebene Provider
  * `profile`: Provider, die erscheinen, wenn Authentifizierungsprofile existieren
  * `paired`: Provider, die mehrere zusammengehörige Provider-Einträge synthetisieren
  * `late`: letzter Durchlauf, nach anderen impliziten Providern


Spätere Provider gewinnen bei Schlüsselkonflikten, sodass Plugins einen eingebauten Provider-Eintrag mit derselben Provider-ID absichtlich überschreiben können.

Plugins können außerdem schreibgeschützte Modellzeilen über `api.registerModelCatalogProvider({ provider, kinds, staticCatalog, liveCatalog })` veröffentlichen. Dies ist der zukünftige Pfad für Listen-/Hilfe-/Picker-Oberflächen und unterstützt Zeilen für `text`, `image_generation`, `video_generation` und `music_generation`. Provider-Plugins besitzen weiterhin Live-Endpunktaufrufe, Token-Austausch und Vendor- Response-Mapping; Core besitzt die gemeinsame Zeilenform, Quelllabels und die Hilfeformatierung für Media-Tools. Registrierungen für Media-Generation-Provider synthetisieren statische Katalogzeilen automatisch aus `defaultModel`, `models` und `capabilities`.

Kompatibilität:

  * `discovery` funktioniert weiterhin als Legacy-Alias, gibt aber eine Veraltungswarnung aus
  * wenn sowohl `catalog` als auch `discovery` registriert sind, verwendet OpenClaw `catalog`
  * `augmentModelCatalog` ist veraltet; gebündelte Provider sollten zusätzliche Zeilen über `registerModelCatalogProvider` veröffentlichen


## Schreibgeschützte Channel-Inspektion

Wenn Ihr Plugin einen Channel registriert, sollten Sie vorzugsweise `plugin.config.inspectAccount(cfg, accountId)` neben `resolveAccount(...)` implementieren.

Warum:

  * `resolveAccount(...)` ist der Laufzeitpfad. Er darf annehmen, dass Anmeldedaten vollständig materialisiert sind, und kann schnell fehlschlagen, wenn erforderliche Secrets fehlen.
  * Schreibgeschützte Befehlspfade wie `openclaw status`, `openclaw status --all`, `openclaw channels status`, `openclaw channels resolve` sowie Doctor-/Konfigurations- Reparaturabläufe sollten keine Laufzeit-Anmeldedaten materialisieren müssen, nur um Konfiguration zu beschreiben.


Empfohlenes Verhalten von `inspectAccount(...)`:

  * Geben Sie nur beschreibenden Kontostatus zurück.
  * Bewahren Sie `enabled` und `configured` bei.
  * Fügen Sie bei Relevanz Felder für Quelle/Status der Anmeldedaten ein, etwa: 
    * `tokenSource`, `tokenStatus`
    * `botTokenSource`, `botTokenStatus`
    * `appTokenSource`, `appTokenStatus`
    * `signingSecretSource`, `signingSecretStatus`
  * Sie müssen keine rohen Token-Werte zurückgeben, nur um schreibgeschützte Verfügbarkeit zu melden. `tokenStatus: "available"` zurückzugeben (und das passende Quellfeld) reicht für Status-artige Befehle aus.
  * Verwenden Sie `configured_unavailable`, wenn Anmeldedaten über SecretRef konfiguriert, aber im aktuellen Befehlspfad nicht verfügbar sind.


Dadurch können schreibgeschützte Befehle „konfiguriert, aber in diesem Befehlspfad nicht verfügbar“ melden, statt abzustürzen oder das Konto fälschlich als nicht konfiguriert zu melden.

## Paket-Packs

Ein Plugin-Verzeichnis kann eine `package.json` mit `openclaw.extensions` enthalten:

jsonCopy code
[code]
    {  "name": "my-pack",  "openclaw": {    "extensions": ["./src/safety.ts", "./src/tools.ts"],    "setupEntry": "./src/setup-entry.ts"  }}
[/code]

Jeder Eintrag wird zu einem Plugin. Wenn das Pack mehrere Erweiterungen auflistet, wird die Plugin-ID zu `name/<fileBase>`.

Wenn Ihr Plugin npm-Abhängigkeiten importiert, installieren Sie sie in diesem Verzeichnis, sodass `node_modules` verfügbar ist (`npm install` / `pnpm install`).

Sicherheitsleitplanke: Jeder `openclaw.extensions`-Eintrag muss nach der Symlink-Auflösung innerhalb des Plugin- Verzeichnisses bleiben. Einträge, die aus dem Paketverzeichnis ausbrechen, werden abgelehnt.

Sicherheitshinweis: `openclaw plugins install` installiert Plugin-Abhängigkeiten mit einem projektlokalen `npm install --omit=dev --ignore-scripts` (keine Lifecycle-Skripte, keine Entwicklungsabhängigkeiten zur Laufzeit) und ignoriert geerbte globale npm-Installations-Einstellungen. Halten Sie Plugin-Abhängigkeitsbäume „pure JS/TS“ und vermeiden Sie Pakete, die `postinstall`-Builds erfordern.

Optional: `openclaw.setupEntry` kann auf ein schlankes, nur für Setup bestimmtes Modul zeigen. Wenn OpenClaw Setup-Oberflächen für ein deaktiviertes Channel-Plugin benötigt oder wenn ein Channel-Plugin aktiviert, aber noch nicht konfiguriert ist, lädt es `setupEntry` statt des vollständigen Plugin-Einstiegs. Das hält Start und Setup leichter, wenn Ihr Haupt-Plugin-Einstieg auch Tools, Hooks oder anderen nur zur Laufzeit benötigten Code verdrahtet.

Optional: `openclaw.startup.deferConfiguredChannelFullLoadUntilAfterListen` kann ein Channel-Plugin während der Pre-Listen-Startphase des Gateways in denselben `setupEntry`-Pfad optieren lassen, selbst wenn der Channel bereits konfiguriert ist.

Verwenden Sie dies nur, wenn `setupEntry` die Startoberfläche vollständig abdeckt, die vorhanden sein muss, bevor der Gateway zu lauschen beginnt. In der Praxis bedeutet das, dass der Setup-Eintrag jede kanal-eigene Fähigkeit registrieren muss, von der der Start abhängt, zum Beispiel:

  * die Kanalregistrierung selbst
  * alle HTTP-Routen, die verfügbar sein müssen, bevor der Gateway zu lauschen beginnt
  * alle Gateway-Methoden, Tools oder Dienste, die in demselben Zeitfenster vorhanden sein müssen


Wenn Ihr vollständiger Eintrag weiterhin eine erforderliche Startfähigkeit besitzt, aktivieren Sie dieses Flag nicht. Belassen Sie das Plugin beim Standardverhalten und lassen Sie OpenClaw den vollständigen Eintrag während des Starts laden.

Gebündelte Kanäle können außerdem reine Setup-Helfer für Vertragsoberflächen veröffentlichen, die der Core abfragen kann, bevor die vollständige Kanallaufzeit geladen wird. Die aktuelle Oberfläche für Setup-Hochstufungen ist:

  * `singleAccountKeysToMove`
  * `namedAccountPromotionKeys`
  * `resolveSingleAccountPromotionTarget(...)`


Der Core verwendet diese Oberfläche, wenn er eine ältere Einzelkonto-Kanalkonfiguration in `channels.<id>.accounts.*` hochstufen muss, ohne den vollständigen Plugin-Eintrag zu laden. Matrix ist das aktuelle gebündelte Beispiel: Es verschiebt nur Authentifizierungs-/Bootstrap-Schlüssel in ein benanntes hochgestuftes Konto, wenn benannte Konten bereits vorhanden sind, und kann einen konfigurierten nicht-kanonischen Standardkonto-Schlüssel beibehalten, anstatt immer `accounts.default` zu erstellen.

Diese Setup-Patch-Adapter halten die Erkennung gebündelter Vertragsoberflächen lazy. Die Importzeit bleibt leichtgewichtig; die Hochstufungsoberfläche wird erst bei der ersten Verwendung geladen, statt beim Modulimport erneut in den Start des gebündelten Kanals einzutreten.

Wenn diese Startoberflächen Gateway-RPC-Methoden enthalten, behalten Sie sie unter einem Plugin-spezifischen Präfix. Core-Admin-Namensräume (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) bleiben reserviert und werden immer zu `operator.admin` aufgelöst, selbst wenn ein Plugin einen engeren Scope anfordert.

Beispiel:

jsonCopy code
[code]
    {  "name": "@scope/my-channel",  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "startup": {      "deferConfiguredChannelFullLoadUntilAfterListen": true    }  }}
[/code]

### Kanalkatalog-Metadaten

Kanal-Plugins können Setup-/Erkennungsmetadaten über `openclaw.channel` und Installationshinweise über `openclaw.install` veröffentlichen. Dadurch bleibt der Core-Katalog datenfrei.

Beispiel:

jsonCopy code
[code]
    {  "name": "@openclaw/nextcloud-talk",  "openclaw": {    "extensions": ["./index.ts"],    "channel": {      "id": "nextcloud-talk",      "label": "Nextcloud Talk",      "selectionLabel": "Nextcloud Talk (self-hosted)",      "docsPath": "/channels/nextcloud-talk",      "docsLabel": "nextcloud-talk",      "blurb": "Self-hosted chat via Nextcloud Talk webhook bots.",      "order": 65,      "aliases": ["nc-talk", "nc"]    },    "install": {      "npmSpec": "@openclaw/nextcloud-talk",      "localPath": "<bundled-plugin-local-path>",      "defaultChoice": "npm"    }  }}
[/code]

Nützliche `openclaw.channel`-Felder über das minimale Beispiel hinaus:

  * `detailLabel`: sekundäres Label für reichhaltigere Katalog-/Statusoberflächen
  * `docsLabel`: Linktext für den Docs-Link überschreiben
  * `preferOver`: Plugin-/Kanal-IDs mit niedrigerer Priorität, die dieser Katalogeintrag übertreffen soll
  * `selectionDocsPrefix`, `selectionDocsOmitLabel`, `selectionExtras`: Kopiesteuerungen für Auswahloberflächen
  * `markdownCapable`: markiert den Kanal als Markdown-fähig für Entscheidungen zur ausgehenden Formatierung
  * `exposure.configured`: blendet den Kanal auf Oberflächen für konfigurierte Kanallisten aus, wenn auf `false` gesetzt
  * `exposure.setup`: blendet den Kanal in interaktiven Setup-/Konfigurationsauswahlen aus, wenn auf `false` gesetzt
  * `exposure.docs`: markiert den Kanal für Docs-Navigationsoberflächen als intern/privat
  * `showConfigured` / `showInSetup`: ältere Aliasse, die aus Kompatibilitätsgründen weiterhin akzeptiert werden; bevorzugen Sie `exposure`
  * `quickstartAllowFrom`: nimmt den Kanal in den standardmäßigen Quickstart-`allowFrom`-Flow auf
  * `forceAccountBinding`: erfordert eine explizite Kontobindung, auch wenn nur ein Konto vorhanden ist
  * `preferSessionLookupForAnnounceTarget`: bevorzugt Session-Lookup beim Auflösen von Ankündigungszielen


OpenClaw kann außerdem **externe Kanalkataloge** zusammenführen, zum Beispiel einen MPM- Registry-Export. Legen Sie eine JSON-Datei an einem der folgenden Orte ab:

  * `~/.openclaw/mpm/plugins.json`
  * `~/.openclaw/mpm/catalog.json`
  * `~/.openclaw/plugins/catalog.json`


Oder verweisen Sie mit `OPENCLAW_PLUGIN_CATALOG_PATHS` (oder `OPENCLAW_MPM_CATALOG_PATHS`) auf eine oder mehrere JSON-Dateien (durch Komma/Semikolon/`PATH` getrennt). Jede Datei sollte `{ "entries": [ { "name": "@scope/pkg", "openclaw": { "channel": {...}, "install": {...} } } ] }` enthalten. Der Parser akzeptiert auch `"packages"` oder `"plugins"` als ältere Aliasse für den Schlüssel `"entries"`.

Generierte Kanalkatalogeinträge und Provider-Installationskatalogeinträge stellen normalisierte Installationsquellen-Fakten neben dem rohen `openclaw.install`-Block bereit. Die normalisierten Fakten identifizieren, ob die npm-Spezifikation eine exakte Version oder ein gleitender Selektor ist, ob erwartete Integritätsmetadaten vorhanden sind und ob zusätzlich ein lokaler Quellpfad verfügbar ist. Wenn die Katalog-/Paketidentität bekannt ist, warnen die normalisierten Fakten, falls der geparste npm-Paketname von dieser Identität abweicht. Sie warnen auch, wenn `defaultChoice` ungültig ist oder auf eine Quelle verweist, die nicht verfügbar ist, sowie wenn npm-Integritätsmetadaten ohne gültige npm- Quelle vorhanden sind. Verbraucher sollten `installSource` als additives optionales Feld behandeln, damit von Hand erstellte Einträge und Katalog-Shims es nicht synthetisieren müssen. Dadurch können Onboarding und Diagnosen den Zustand der Quellenebene erklären, ohne Plugin-Laufzeit zu importieren.

Offizielle externe npm-Einträge sollten eine exakte `npmSpec` plus `expectedIntegrity` bevorzugen. Reine Paketnamen und dist-tags funktionieren aus Kompatibilitätsgründen weiterhin, erzeugen jedoch Warnungen auf der Quellenebene, damit sich der Katalog in Richtung gepinnter, integritätsgeprüfter Installationen bewegen kann, ohne bestehende Plugins zu beschädigen. Wenn das Onboarding aus einem lokalen Katalogpfad installiert, zeichnet es einen verwalteten Plugin- Plugin-Indexeintrag mit `source: "path"` und nach Möglichkeit einem workspace-relativen `sourcePath` auf. Der absolute operative Ladepfad bleibt in `plugins.load.paths`; der Installationsdatensatz vermeidet es, lokale Workstation- Pfade in langlebige Konfiguration zu duplizieren. Dadurch bleiben lokale Entwicklungsinstallationen für Quellenebenen-Diagnosen sichtbar, ohne eine zweite rohe Offenlegungsoberfläche für Dateisystempfade hinzuzufügen. Der persistierte Plugin-Index `plugins/installs.json` ist die Installationsquelle der Wahrheit und kann aktualisiert werden, ohne Plugin-Laufzeitmodule zu laden. Seine `installRecords`-Map ist dauerhaft, auch wenn ein Plugin-Manifest fehlt oder ungültig ist; sein `plugins`-Array ist eine neu aufbaubare Manifestansicht.

## Kontext-Engine-Plugins

Kontext-Engine-Plugins besitzen die Orchestrierung des Session-Kontexts für Ingest, Assembly und Compaction. Registrieren Sie sie aus Ihrem Plugin mit `api.registerContextEngine(id, factory)`, und wählen Sie dann die aktive Engine mit `plugins.slots.contextEngine` aus.

Verwenden Sie dies, wenn Ihr Plugin die Standard-Kontextpipeline ersetzen oder erweitern muss, statt nur Memory-Suche oder Hooks hinzuzufügen.

tsCopy code
[code]
     export default function (api) {  api.registerContextEngine("lossless-claw", (ctx) => ({    info: { id: "lossless-claw", name: "Lossless Claw", ownsCompaction: true },    async ingest() {      return { ingested: true };    },    async assemble({ messages, availableTools, citationsMode }) {      return {        messages,        estimatedTokens: 0,        systemPromptAddition: buildMemorySystemPromptAddition({          availableTools: availableTools ?? new Set(),          citationsMode,        }),      };    },    async compact() {      return { ok: true, compacted: false };    },  }));}
[/code]

Die Factory `ctx` stellt optionale Werte `config`, `agentDir` und `workspaceDir` für die Initialisierung zur Konstruktionszeit bereit.

Wenn Ihre Engine den Compaction-Algorithmus **nicht** besitzt, behalten Sie `compact()` implementiert und delegieren Sie explizit:

tsCopy code
[code]
       buildMemorySystemPromptAddition,  delegateCompactionToRuntime,} from "openclaw/plugin-sdk/core"; export default function (api) {  api.registerContextEngine("my-memory-engine", (ctx) => ({    info: {      id: "my-memory-engine",      name: "My Memory Engine",      ownsCompaction: false,    },    async ingest() {      return { ingested: true };    },    async assemble({ messages, availableTools, citationsMode }) {      return {        messages,        estimatedTokens: 0,        systemPromptAddition: buildMemorySystemPromptAddition({          availableTools: availableTools ?? new Set(),          citationsMode,        }),      };    },    async compact(params) {      return await delegateCompactionToRuntime(params);    },  }));}
[/code]

## Eine neue Fähigkeit hinzufügen

Wenn ein Plugin Verhalten benötigt, das nicht zur aktuellen API passt, umgehen Sie das Plugin-System nicht mit einem privaten Zugriff. Fügen Sie die fehlende Fähigkeit hinzu.

Empfohlene Reihenfolge:

  1. Core-Vertrag definieren Entscheiden Sie, welches gemeinsame Verhalten der Core besitzen soll: Policy, Fallback, Konfigurationszusammenführung, Lebenszyklus, kanalbezogene Semantik und Form des Laufzeithelfers.
  2. typisierte Plugin-Registrierungs-/Laufzeitoberflächen hinzufügen Erweitern Sie `OpenClawPluginApi` und/oder `api.runtime` um die kleinste nützliche typisierte Fähigkeitsoberfläche.
  3. Core und Kanal-/Feature-Verbraucher verdrahten Kanäle und Feature-Plugins sollten die neue Fähigkeit über den Core konsumieren, nicht durch direkten Import einer Herstellerimplementierung.
  4. Herstellerimplementierungen registrieren Hersteller-Plugins registrieren ihre Backends dann gegen die Fähigkeit.
  5. Vertragsabdeckung hinzufügen Fügen Sie Tests hinzu, damit Besitz und Registrierungsform im Laufe der Zeit explizit bleiben.


So bleibt OpenClaw meinungsstark, ohne hart auf die Weltsicht eines einzelnen Providers codiert zu werden. Siehe das [Fähigkeiten-Kochbuch](</de/plugins/adding-capabilities>) für eine konkrete Datei-Checkliste und ein ausgearbeitetes Beispiel.

### Fähigkeiten-Checkliste

Wenn Sie eine neue Fähigkeit hinzufügen, sollte die Implementierung diese Oberflächen in der Regel gemeinsam berühren:

  * Core-Vertragstypen in `src/<capability>/types.ts`
  * Core-Runner-/Laufzeithelfer in `src/<capability>/runtime.ts`
  * Plugin-API-Registrierungsoberfläche in `src/plugins/types.ts`
  * Plugin-Registry-Verdrahtung in `src/plugins/registry.ts`
  * Plugin-Laufzeitfreigabe in `src/plugins/runtime/*`, wenn Feature-/Kanal- Plugins sie konsumieren müssen
  * Capture-/Testhelfer in `src/test-utils/plugin-registration.ts`
  * Besitz-/Vertragsassertionen in `src/plugins/contracts/registry.ts`
  * Operator-/Plugin-Docs in `docs/`


Wenn eine dieser Oberflächen fehlt, ist das normalerweise ein Zeichen dafür, dass die Fähigkeit noch nicht vollständig integriert ist.

### Fähigkeiten-Vorlage

Minimales Muster:

tsCopy code
[code]
    // core contractexport type VideoGenerationProviderPlugin = {  id: string;  label: string;  generateVideo: (req: VideoGenerationRequest) => Promise&lt;VideoGenerationResult&gt;;}; // plugin APIapi.registerVideoGenerationProvider({  id: "openai",  label: "OpenAI",  async generateVideo(req) {    return await generateOpenAiVideo(req);  },}); // shared runtime helper for feature/channel pluginsconst clip = await api.runtime.videoGeneration.generate({  prompt: "Show the robot walking through the lab.",  cfg,});
[/code]

Vertragstest-Muster:

tsCopy code
[code]
    expect(findVideoGenerationProviderIdsForPlugin("openai")).toEqual(["openai"]);
[/code]

Das hält die Regel einfach:

  * der Core besitzt den Fähigkeitsvertrag und die Orchestrierung
  * Hersteller-Plugins besitzen Herstellerimplementierungen
  * Feature-/Kanal-Plugins konsumieren Laufzeithelfer
  * Vertragstests halten den Besitz explizit


## Verwandte Themen

  * [Plugin-Architektur](</de/plugins/architecture>) — öffentliches Fähigkeitsmodell und Formen
  * [Plugin-SDK-Unterpfade](</de/plugins/sdk-subpaths>)
  * [Plugin-SDK-Setup](</de/plugins/sdk-setup>)
  * [Plugins erstellen](</de/plugins/building-plugins>)


Was this useful?YesNo