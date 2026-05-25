---
title: Interne werking van Plugin
source_url: https://docs.openclaw.ai/nl/plugins/architecture
scraped_at: 2026-05-25
---

Dit is de **uitgebreide architectuurreferentie** voor het OpenClaw-pluginsysteem. Begin voor praktische gidsen met een van de gerichte pagina's hieronder.

[**Plugins installeren en gebruiken** Eindgebruikersgids voor het toevoegen, inschakelen en oplossen van problemen met plugins. ](</nl/tools/plugin>) [**Plugins bouwen** Tutorial voor een eerste plugin met het kleinste werkende manifest. ](</nl/plugins/building-plugins>) [**Kanaalplugins** Bouw een plugin voor een berichtenkanaal. ](</nl/plugins/sdk-channel-plugins>) [**Providerplugins** Bouw een plugin voor een modelprovider. ](</nl/plugins/sdk-provider-plugins>) [**SDK-overzicht** Referentie voor importmap en registratie-API. ](</nl/plugins/sdk-overview>)

## Publiek capaciteitsmodel

Capaciteiten zijn het publieke **native plugin** -model binnen OpenClaw. Elke native OpenClaw-plugin registreert zich voor een of meer capaciteitstypen:

Capaciteit | Registratiemethode | Voorbeeldplugins  
---|---|---  
Tekstinferentie | `api.registerProvider(...)` | `openai`, `anthropic`  
CLI-inferentiebackend | `api.registerCliBackend(...)` | `openai`, `anthropic`  
Spraak | `api.registerSpeechProvider(...)` | `elevenlabs`, `microsoft`  
Realtime transcriptie | `api.registerRealtimeTranscriptionProvider(...)` | `openai`  
Realtime stem | `api.registerRealtimeVoiceProvider(...)` | `openai`  
Mediabegrip | `api.registerMediaUnderstandingProvider(...)` | `openai`, `google`  
Afbeeldingsgeneratie | `api.registerImageGenerationProvider(...)` | `openai`, `google`, `fal`, `minimax`  
Muziekgeneratie | `api.registerMusicGenerationProvider(...)` | `google`, `minimax`  
Videogeneratie | `api.registerVideoGenerationProvider(...)` | `qwen`  
Web ophalen | `api.registerWebFetchProvider(...)` | `firecrawl`  
Web zoeken | `api.registerWebSearchProvider(...)` | `google`  
Kanaal / berichten | `api.registerChannel(...)` | `msteams`, `matrix`  
Gateway-detectie | `api.registerGatewayDiscoveryService(...)` | `bonjour`  
  
### Standpunt over externe compatibiliteit

Het capaciteitsmodel is in core geland en wordt vandaag gebruikt door gebundelde/native plugins, maar compatibiliteit voor externe plugins heeft nog een strengere lat nodig dan "het is geëxporteerd, dus het is bevroren."

Pluginsituatie | Richtlijn  
---|---  
Bestaande externe plugins | Houd hookgebaseerde integraties werkend; dit is de compatibiliteitsbasis.  
Nieuwe gebundelde/native plugins | Geef de voorkeur aan expliciete capaciteitsregistratie boven leveranciersspecifieke reach-ins of nieuwe hook-only ontwerpen.  
Externe plugins die capaciteitsregistratie gebruiken | Toegestaan, maar behandel capaciteitsspecifieke hulpinterfaces als in ontwikkeling, tenzij docs ze als stabiel markeren.  
  
Capaciteitsregistratie is de beoogde richting. Verouderde hooks blijven tijdens de overgang het veiligste pad zonder breuken voor externe plugins. Geëxporteerde hulpsubpaden zijn niet allemaal gelijk — geef de voorkeur aan smalle gedocumenteerde contracten boven incidentele helperexports.

### Plugin-vormen

OpenClaw classificeert elke geladen plugin in een vorm op basis van het daadwerkelijke registratiegedrag ervan (niet alleen statische metadata):

plain-capability

Registreert exact één capaciteitstype (bijvoorbeeld een provider-only plugin zoals `mistral`).

hybrid-capability

Registreert meerdere capaciteitstypen (bijvoorbeeld `openai` bezit tekstinferentie, spraak, mediabegrip en afbeeldingsgeneratie).

hook-only

Registreert alleen hooks (getypeerd of aangepast), geen capaciteiten, tools, opdrachten of services.

non-capability

Registreert tools, opdrachten, services of routes, maar geen capaciteiten.

Gebruik `openclaw plugins inspect <id>` om de vorm en capaciteitsuitsplitsing van een plugin te bekijken. Zie [CLI-referentie](</nl/cli/plugins#inspect>) voor details.

### Verouderde hooks

De hook `before_agent_start` blijft ondersteund als compatibiliteitspad voor hook-only plugins. Verouderde echte plugins zijn er nog steeds van afhankelijk.

Richting:

  * houd het werkend
  * documenteer het als verouderd
  * geef de voorkeur aan `before_model_resolve` voor werk rond model-/provideroverrides
  * geef de voorkeur aan `before_prompt_build` voor werk rond promptmutatie
  * verwijder het pas nadat echt gebruik is afgenomen en fixturedekking bewijst dat migratie veilig is


### Compatibiliteitssignalen

Wanneer je `openclaw doctor` of `openclaw plugins inspect <id>` uitvoert, kun je een van deze labels zien:

Signaal | Betekenis  
---|---  
**config valid** | Configuratie wordt correct geparseerd en plugins worden opgelost  
**compatibility advisory** | Plugin gebruikt een ondersteund maar ouder patroon (bijv. `hook-only`)  
**legacy warning** | Plugin gebruikt `before_agent_start`, wat verouderd is  
**hard error** | Configuratie is ongeldig of plugin kon niet worden geladen  
  
Noch `hook-only` noch `before_agent_start` breekt je plugin vandaag: `hook-only` is adviserend, en `before_agent_start` geeft alleen een waarschuwing. Deze signalen verschijnen ook in `openclaw status --all` en `openclaw plugins doctor`.

## Architectuuroverzicht

Het pluginsysteem van OpenClaw heeft vier lagen:

* ### Manifest + detectie

OpenClaw vindt kandidaatplugins via geconfigureerde paden, werkruimteroots, globale pluginroots en gebundelde plugins. Detectie leest eerst native `openclaw.plugin.json`-manifesten plus ondersteunde bundlemanifesten.

* ### Inschakeling + validatie

Core bepaalt of een gevonden plugin ingeschakeld, uitgeschakeld, geblokkeerd of geselecteerd is voor een exclusieve sleuf zoals geheugen.

* ### Runtime laden

Native OpenClaw-plugins worden in-process geladen en registreren capaciteiten in een centraal register. Verpakte JavaScript laadt via native `require`; TypeScript van lokale broncode van derden is de noodfallback via Jiti. Compatibele bundles worden genormaliseerd tot registerrecords zonder runtimecode te importeren.

* ### Gebruik door oppervlakken

De rest van OpenClaw leest het register om tools, kanalen, providerconfiguratie, hooks, HTTP-routes, CLI-opdrachten en services bloot te stellen.

Voor de plugin-CLI specifiek is rootopdrachtdetectie opgesplitst in twee fasen:

  * metadata tijdens het parsen komt uit `registerCli(..., { descriptors: [...] })`
  * de echte plugin-CLI-module kan lazy blijven en registreren bij de eerste aanroep


Daardoor blijft plugin-eigen CLI-code binnen de plugin, terwijl OpenClaw toch rootopdrachtnamen kan reserveren vóór het parsen.

De belangrijke ontwerpgrens:

  * manifest-/configvalidatie moet werken vanuit **manifest-/schemametadata** zonder plugincode uit te voeren
  * native capaciteitsdetectie mag vertrouwde plugin-entrycode laden om een niet-activerende registersnapshot te bouwen
  * native runtimegedrag komt uit het pad `register(api)` van de pluginmodule met `api.registrationMode === "full"`


Die splitsing laat OpenClaw configuratie valideren, ontbrekende/uitgeschakelde plugins uitleggen en UI-/schemahints bouwen voordat de volledige runtime actief is.

### Snapshot van pluginmetadata en opzoektabel

Bij het opstarten van de Gateway wordt één `PluginMetadataSnapshot` gebouwd voor de huidige configuratiesnapshot. De snapshot bevat alleen metadata: hij bewaart de geïnstalleerde pluginindex, het manifestregister, manifestdiagnostiek, eigenaarkaarten, een normalizer voor plugin-id's en manifestrecords. Hij bevat geen geladen pluginmodules, provider-SDK's, pakketinhoud of runtimeexports.

Pluginbewuste configvalidatie, automatisch inschakelen bij opstarten en de Gateway-pluginbootstrap gebruiken die snapshot in plaats van manifest-/indexmetadata onafhankelijk opnieuw op te bouwen. `PluginLookUpTable` wordt afgeleid van dezelfde snapshot en voegt het opstartpluginplan toe voor de huidige runtimeconfiguratie.

Na het opstarten bewaart Gateway de huidige metadatasnapshot als een vervangbaar runtimeproduct. Herhaalde runtime-providerdetectie kan die snapshot lenen in plaats van voor elke provider-cataloguspass de geïnstalleerde index en het manifestregister opnieuw te reconstrueren. De snapshot wordt gewist of vervangen bij afsluiten van de Gateway, wijzigingen in configuratie/plugininventaris en schrijfacties naar de geïnstalleerde index; callers vallen terug op het koude manifest-/indexpad wanneer er geen compatibele huidige snapshot bestaat. Compatibiliteitscontroles moeten plugin-detectieroots bevatten zoals `plugins.load.paths` en de standaard agentwerkruimte, omdat werkruimteplugins deel uitmaken van de metadatascope.

De snapshot en opzoektabel houden herhaalde opstartbeslissingen op het snelle pad:

  * kanaaleigenaarschap
  * uitgestelde kanaalstart
  * opstartplugin-id's
  * eigenaarschap van provider- en CLI-backends
  * eigenaarschap van setup-provider, opdrachtalias, modelcatalogusprovider en manifestcontract
  * validatie van pluginconfigschema en kanaalconfigschema
  * beslissingen voor automatisch inschakelen bij opstarten


De veiligheidsgrens is vervanging van snapshots, niet mutatie. Bouw de snapshot opnieuw wanneer configuratie, plugininventaris, installatierecords of bewaard indexbeleid verandert. Behandel hem niet als een breed muteerbaar globaal register, en bewaar geen onbeperkte historische snapshots. Runtime laden van plugins blijft gescheiden van metadatasnapshots zodat verouderde runtimestatus niet achter een metadatacache kan worden verborgen.

De cacheregel is gedocumenteerd in [Interne pluginarchitectuur](</nl/plugins/architecture-internals#plugin-cache-boundary>): manifest- en detectiemetadata zijn vers, tenzij een caller een expliciete snapshot, opzoektabel of manifestregister voor de huidige flow vasthoudt. Verborgen metadatacaches en TTL's op basis van de klok maken geen deel uit van pluginladen. Alleen runtime-loader-, module- en afhankelijkheidsartefactcaches mogen blijven bestaan nadat code of geïnstalleerde artefacten daadwerkelijk zijn geladen.

Sommige callers op het koude pad reconstrueren manifestregisters nog steeds rechtstreeks vanuit de bewaarde geïnstalleerde pluginindex in plaats van een Gateway `PluginLookUpTable` te ontvangen. Dat pad reconstrueert het register nu op aanvraag; geef liever de huidige opzoektabel of een expliciet manifestregister door runtimeflows wanneer een caller er al een heeft.

### Activeringsplanning

Activeringsplanning maakt deel uit van het control plane. Callers kunnen vragen welke plugins relevant zijn voor een concrete opdracht, provider, kanaal, route, agentharnas of capaciteit voordat bredere runtimeregisters worden geladen.

De planner houdt huidig manifestgedrag compatibel:

  * velden `activation.*` zijn expliciete plannerhints
  * `providers`, `channels`, `commandAliases`, `setup.providers`, `contracts.tools` en hooks blijven manifest-eigenaarschapfallback
  * de ids-only planner-API blijft beschikbaar voor bestaande callers
  * de plan-API rapporteert redenlabels zodat diagnostiek expliciete hints kan onderscheiden van eigenaarschapfallback


### Kanaalplugins en de gedeelde berichttool

Kanaalplugins hoeven geen aparte tool voor verzenden/bewerken/reageren te registreren voor normale chatacties. OpenClaw bewaart één gedeelde `message`-tool in core, en kanaalplugins zijn eigenaar van de kanaalspecifieke ontdekking en uitvoering daarachter.

De huidige grens is:

  * core is eigenaar van de gedeelde host van de `message`-tool, prompt-bedrading, sessie-/threadboekhouding en uitvoeringsdispatch
  * kanaalplugins zijn eigenaar van gescopete actiediscovery, capability-discovery en eventuele kanaalspecifieke schemafragmenten
  * kanaalplugins zijn eigenaar van providerspecifieke grammatica voor sessiegesprekken, zoals hoe gespreks-id's thread-id's coderen of overerven van bovenliggende gesprekken
  * kanaalplugins voeren de uiteindelijke actie uit via hun action-adapter


Voor kanaalplugins is het SDK-oppervlak `ChannelMessageActionAdapter.describeMessageTool(...)`. Die uniforme discovery-call laat een plugin zijn zichtbare acties, capabilities en schemabijdragen samen teruggeven, zodat die onderdelen niet uit elkaar gaan lopen.

Wanneer een kanaalspecifieke message-tool-param een mediabron bevat, zoals een lokaal pad of een externe media-URL, moet de plugin ook `mediaSourceParams` teruggeven vanuit `describeMessageTool(...)`. Core gebruikt die expliciete lijst om sandbox-padnormalisatie en hints voor uitgaande mediatoegang toe te passen zonder plugin-eigen param-namen hard te coderen. Geef daar de voorkeur aan actiegescopete maps, niet aan één kanaalbrede platte lijst, zodat een media-param die alleen voor profielen geldt niet wordt genormaliseerd bij niet-gerelateerde acties zoals `send`.

Core geeft runtime-scope door aan die discoverystap. Belangrijke velden zijn onder andere:

  * `accountId`
  * `currentChannelId`
  * `currentThreadTs`
  * `currentMessageId`
  * `sessionKey`
  * `sessionId`
  * `agentId`
  * vertrouwde inkomende `requesterSenderId`


Dat is belangrijk voor contextgevoelige plugins. Een kanaal kan berichtacties verbergen of tonen op basis van het actieve account, de huidige room/thread/bericht of de vertrouwde identiteit van de aanvrager, zonder kanaalspecifieke vertakkingen hard te coderen in de core-`message`-tool.

Daarom blijven routeringswijzigingen voor embedded-runners pluginwerk: de runner is verantwoordelijk voor het doorsturen van de huidige chat-/sessie-identiteit naar de plugin-discoverygrens, zodat de gedeelde `message`-tool het juiste kanaaleigen oppervlak voor de huidige beurt toont.

Voor kanaaleigen uitvoeringshelpers moeten gebundelde plugins de uitvoeringsruntime binnen hun eigen extension-modules houden. Core is niet langer eigenaar van de Discord-, Slack-, Telegram- of WhatsApp-message-action-runtimes onder `src/agents/tools`. We publiceren geen aparte `plugin-sdk/*-action-runtime`-subpaden, en gebundelde plugins moeten hun eigen lokale runtimecode rechtstreeks importeren uit hun extension-eigen modules.

Dezelfde grens geldt in het algemeen voor provider-genoemde SDK-seams: core mag geen kanaalspecifieke convenience barrels importeren voor Slack, Discord, Signal, WhatsApp of vergelijkbare extensions. Als core gedrag nodig heeft, consumeer dan ofwel de eigen `api.ts`\- / `runtime-api.ts`-barrel van de gebundelde plugin, of promoveer de behoefte naar een smalle generieke capability in de gedeelde SDK.

Gebundelde plugins volgen dezelfde regel. De `runtime-api.ts` van een gebundelde plugin mag zijn eigen gemerkte `openclaw/plugin-sdk/<plugin-id>`-facade niet opnieuw exporteren. Die gemerkte facades blijven compatibiliteitsshims voor externe plugins en oudere consumenten, maar gebundelde plugins moeten lokale exports gebruiken plus smalle generieke SDK-subpaden zoals `openclaw/plugin-sdk/channel-policy`, `openclaw/plugin-sdk/runtime-store` of `openclaw/plugin-sdk/webhook-ingress`. Nieuwe code mag geen plugin-id-specifieke SDK-facades toevoegen, tenzij de compatibiliteitsgrens voor een bestaand extern ecosysteem dat vereist.

Specifiek voor polls zijn er twee uitvoeringspaden:

  * `outbound.sendPoll` is de gedeelde basis voor kanalen die passen binnen het algemene pollmodel
  * `actions.handleAction("poll")` is het voorkeurs-pad voor kanaalspecifieke pollsemantiek of extra pollparameters


Core stelt gedeelde pollparsing nu uit tot nadat plugin-polldispatch de actie weigert, zodat plugin-eigen pollhandlers kanaalspecifieke pollvelden kunnen accepteren zonder eerst door de generieke pollparser te worden geblokkeerd.

Zie [Interne pluginarchitectuur](</nl/plugins/architecture-internals>) voor de volledige opstartvolgorde.

## Capability-eigendomsmodel

OpenClaw behandelt een native plugin als de eigendomsgrens voor een **bedrijf** of een **feature** , niet als een verzameling losstaande integraties.

Dat betekent:

  * een bedrijfsplugin moet meestal eigenaar zijn van alle OpenClaw-gerichte oppervlakken van dat bedrijf
  * een featureplugin moet meestal eigenaar zijn van het volledige feature-oppervlak dat hij introduceert
  * kanalen moeten gedeelde core-capabilities gebruiken in plaats van provider-gedrag ad hoc opnieuw te implementeren


Vendor multi-capability

`openai` is eigenaar van tekstinferentie, spraak, realtime stem, mediabegrip en beeldgeneratie. `google` is eigenaar van tekstinferentie plus mediabegrip, beeldgeneratie en webzoeken. `qwen` is eigenaar van tekstinferentie plus mediabegrip en videogeneratie.

Vendor single-capability

`elevenlabs` en `microsoft` zijn eigenaar van spraak; `firecrawl` is eigenaar van web-fetch; `minimax` / `mistral` / `moonshot` / `zai` zijn eigenaar van mediabegrip-backends.

Feature plugin

`voice-call` is eigenaar van call-transport, tools, CLI, routes en Twilio media-stream-bridging, maar gebruikt gedeelde capabilities voor spraak, realtime transcriptie en realtime stem in plaats van vendorplugins rechtstreeks te importeren.

De beoogde eindtoestand is:

  * OpenAI leeft in één plugin, zelfs als die tekstmodellen, spraak, afbeeldingen en toekomstige video omvat
  * een andere vendor kan hetzelfde doen voor zijn eigen oppervlak
  * kanalen hoeven niet te weten welke vendorplugin eigenaar is van de provider; ze consumeren het gedeelde capability-contract dat door core wordt blootgesteld


Dit is het belangrijkste onderscheid:

  * **plugin** = eigendomsgrens
  * **capability** = core-contract dat meerdere plugins kunnen implementeren of consumeren


Dus als OpenClaw een nieuw domein toevoegt, zoals video, is de eerste vraag niet "welke provider moet videobehandeling hard coderen?" De eerste vraag is "wat is het core video-capability-contract?" Zodra dat contract bestaat, kunnen vendorplugins zich ertegen registreren en kunnen kanaal-/featureplugins het consumeren.

Als de capability nog niet bestaat, is de juiste stap meestal:

* ### Define the capability

Definieer de ontbrekende capability in core.

* ### Expose through the SDK

Stel die op een getypeerde manier beschikbaar via de plugin-API/runtime.

* ### Wire consumers

Sluit kanalen/features aan op die capability.

* ### Vendor implementations

Laat vendorplugins implementaties registreren.

Dit houdt eigendom expliciet en vermijdt tegelijk core-gedrag dat afhankelijk is van één vendor of een eenmalig plugin-specifiek codepad.

### Capability-lagen

Gebruik dit mentale model wanneer je beslist waar code thuishoort:

### Core capability layer

Gedeelde orkestratie, beleid, fallback, config-samenvoegregels, leveringssemantiek en getypeerde contracten.

### Vendor plugin layer

Vendorspecifieke API's, auth, modelcatalogi, spraaksynthese, beeldgeneratie, toekomstige video-backends, usage-endpoints.

### Channel/feature plugin layer

Slack-/Discord-/voice-call-/enzovoort-integratie die core-capabilities consumeert en ze op een oppervlak presenteert.

TTS volgt bijvoorbeeld deze vorm:

  * core is eigenaar van TTS-beleid op antwoordtijd, fallbackvolgorde, voorkeuren en kanaallevering
  * `openai`, `elevenlabs` en `microsoft` zijn eigenaar van synthese-implementaties
  * `voice-call` consumeert de telephony TTS-runtimehelper


Datzelfde patroon verdient de voorkeur voor toekomstige capabilities.

### Voorbeeld van bedrijfsplugin met meerdere capabilities

Een bedrijfsplugin moet van buitenaf coherent aanvoelen. Als OpenClaw gedeelde contracten heeft voor modellen, spraak, realtime transcriptie, realtime stem, mediabegrip, beeldgeneratie, videogeneratie, web-fetch en webzoeken, kan een vendor al zijn oppervlakken op één plek bezitten:

tsCopy code
[code]
        describeImageWithModel,  transcribeOpenAiCompatibleAudio,} from "openclaw/plugin-sdk/media-understanding"; const plugin: OpenClawPluginDefinition = {  id: "exampleai",  name: "ExampleAI",  register(api) {    api.registerProvider({      id: "exampleai",      // auth/model catalog/runtime hooks    });     api.registerSpeechProvider({      id: "exampleai",      // vendor speech config — implement the SpeechProviderPlugin interface directly    });     api.registerMediaUnderstandingProvider({      id: "exampleai",      capabilities: ["image", "audio", "video"],      async describeImage(req) {        return describeImageWithModel({          provider: "exampleai",          model: req.model,          input: req.input,        });      },      async transcribeAudio(req) {        return transcribeOpenAiCompatibleAudio({          provider: "exampleai",          model: req.model,          input: req.input,        });      },    });     api.registerWebSearchProvider(      createPluginBackedWebSearchProvider({        id: "exampleai-search",        // credential + fetch logic      }),    );  },}; export default plugin;
[/code]

Wat telt, zijn niet de exacte helpernamen. De vorm telt:

  * één plugin is eigenaar van het vendoroppervlak
  * core blijft eigenaar van de capability-contracten
  * kanalen en featureplugins consumeren `api.runtime.*`-helpers, geen vendorcode
  * contracttests kunnen bevestigen dat de plugin de capabilities heeft geregistreerd waarvan hij zegt eigenaar te zijn


### Capability-voorbeeld: videobegrip

OpenClaw behandelt beeld-/audio-/videobegrip al als één gedeelde capability. Hetzelfde eigendomsmodel geldt daar:

* ### Core defines the contract

Core definieert het mediabegrip-contract.

* ### Vendor plugins register

Vendorplugins registreren `describeImage`, `transcribeAudio` en `describeVideo` waar van toepassing.

* ### Consumers use the shared behavior

Kanalen en featureplugins consumeren het gedeelde core-gedrag in plaats van rechtstreeks naar vendorcode te bedraden.

Dat voorkomt dat de videoaannames van één provider in core worden ingebakken. De plugin is eigenaar van het vendoroppervlak; core is eigenaar van het capability-contract en fallbackgedrag.

Videogeneratie gebruikt al dezelfde volgorde: core is eigenaar van het getypeerde capability-contract en de runtimehelper, en vendorplugins registreren `api.registerVideoGenerationProvider(...)`-implementaties ertegen.

Een concrete rollout-checklist nodig? Zie [Capability Cookbook](</nl/plugins/architecture>).

## Contracten en handhaving

Het plugin-API-oppervlak is bewust getypeerd en gecentraliseerd in `OpenClawPluginApi`. Dat contract definieert de ondersteunde registratiepunten en de runtimehelpers waarop een plugin mag vertrouwen.

Waarom dit belangrijk is:

  * pluginauteurs krijgen één stabiele interne standaard
  * core kan dubbel eigendom weigeren, zoals twee plugins die dezelfde provider-id registreren
  * startup kan bruikbare diagnostiek tonen voor misvormde registratie
  * contracttests kunnen eigendom van gebundelde plugins afdwingen en stille drift voorkomen


Er zijn twee handhavingslagen:

Afdwinging van runtimeregistratie

Het Plugin-register valideert registraties terwijl plugins worden geladen. Voorbeelden: dubbele provider-id's, dubbele spraakprovider-id's en ongeldige registraties leveren Plugin-diagnostiek op in plaats van ongedefinieerd gedrag.

Contracttests

Gebundelde plugins worden tijdens testruns vastgelegd in contractregisters zodat OpenClaw eigenaarschap expliciet kan bevestigen. Tegenwoordig wordt dit gebruikt voor modelproviders, spraakproviders, webzoekproviders en eigenaarschap van gebundelde registraties.

Het praktische effect is dat OpenClaw vooraf weet welke Plugin eigenaar is van welk oppervlak. Daardoor kunnen core en kanalen naadloos samenwerken, omdat eigenaarschap gedeclareerd, getypeerd en testbaar is in plaats van impliciet.

### Wat hoort in een contract

### Goede contracten

  * getypeerd
  * klein
  * capaciteitsspecifiek
  * eigendom van core
  * herbruikbaar door meerdere plugins
  * te gebruiken door kanalen/functies zonder kennis van leveranciers


### Slechte contracten

  * leveranciersspecifiek beleid dat verborgen zit in core
  * eenmalige Plugin-ontsnappingsroutes die het register omzeilen
  * kanaalcode die rechtstreeks in een leveranciersimplementatie grijpt
  * ad-hocruntimeobjecten die geen onderdeel zijn van `OpenClawPluginApi` of `api.runtime`


Bij twijfel, verhoog het abstractieniveau: definieer eerst de capaciteit en laat plugins er daarna op aansluiten.

## Uitvoeringsmodel

Native OpenClaw-plugins draaien **in-process** met de Gateway. Ze zijn niet gesandboxed. Een geladen native Plugin heeft dezelfde vertrouwensgrens op procesniveau als corecode.

Compatibele bundels zijn standaard veiliger omdat OpenClaw ze momenteel behandelt als metadata-/contentpakketten. In huidige releases betekent dat vooral gebundelde Skills.

Gebruik allowlists en expliciete installatie-/laadpaden voor niet-gebundelde plugins. Behandel workspace-plugins als code voor ontwikkeltijd, niet als productie-standaardinstellingen.

Houd voor gebundelde workspace-pakketnamen de Plugin-id verankerd in de npm-naam: standaard `@openclaw/<id>`, of een goedgekeurd getypeerd achtervoegsel zoals `-provider`, `-plugin`, `-speech`, `-sandbox` of `-media-understanding` wanneer het pakket bewust een smallere Plugin-rol beschikbaar stelt.

## Exportgrens

OpenClaw exporteert capaciteiten, geen implementatiegemak.

Houd capaciteitsregistratie openbaar. Snoei helperexports die geen contract zijn:

  * helper-subpaden specifiek voor gebundelde plugins
  * runtime-plumbing-subpaden die niet bedoeld zijn als publieke API
  * leveranciersspecifieke gemakhelpers
  * setup-/onboardinghelpers die implementatiedetails zijn


Gereserveerde helper-subpaden voor gebundelde plugins zijn verwijderd uit de gegenereerde SDK-exportmap. Houd eigenaarspecifieke helpers binnen het eigen Plugin-pakket; promoveer alleen herbruikbaar hostgedrag naar generieke SDK-contracten zoals `plugin-sdk/gateway-runtime`, `plugin-sdk/security-runtime` en `plugin-sdk/plugin-config-runtime`.

## Internals en referentie

Zie [Plugin-architectuurinternals](</nl/plugins/architecture-internals>) voor de laadpipeline, het registermodel, provider-runtimehooks, Gateway-HTTP-routes, schemas voor berichtentools, resolutie van kanaaldoelen, providercatalogi, contextengine-plugins en de handleiding voor het toevoegen van een nieuwe capaciteit.

## Gerelateerd

  * [Plugins bouwen](</nl/plugins/building-plugins>)
  * [Plugin-manifest](</nl/plugins/manifest>)
  * [Plugin SDK-installatie](</nl/plugins/sdk-setup>)


Was this useful?YesNo