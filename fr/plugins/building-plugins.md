---
title: Créer des Plugins
source_url: https://docs.openclaw.ai/fr/plugins/building-plugins
scraped_at: 2026-05-25
---

Les plugins étendent OpenClaw avec de nouvelles capacités : canaux, fournisseurs de modèles, parole, transcription en temps réel, voix en temps réel, compréhension des médias, génération d’images, génération de vidéos, récupération web, recherche web, outils d’agent, ou toute combinaison.

Vous n’avez pas besoin d’ajouter votre plugin au dépôt OpenClaw. Publiez-le sur [ClawHub](</fr/clawhub>) et les utilisateurs l’installent avec `openclaw plugins install clawhub:<package-name>`. Les spécifications de paquet nues continuent de s’installer depuis npm pendant la transition de lancement.

## Prérequis

  * Node >= 22 et un gestionnaire de paquets (npm ou pnpm)
  * Familiarité avec TypeScript (ESM)
  * Pour les plugins dans le dépôt : dépôt cloné et `pnpm install` effectué. Le développement de plugins depuis un checkout source utilise uniquement pnpm, car OpenClaw charge les plugins groupés depuis les paquets d’espace de travail `extensions/*`.


## Quel type de plugin ?

[**Channel plugin** Connecter OpenClaw à une plateforme de messagerie (Discord, IRC, etc.) ](</fr/plugins/sdk-channel-plugins>) [**Provider plugin** Ajouter un fournisseur de modèles (LLM, proxy ou endpoint personnalisé) ](</fr/plugins/sdk-provider-plugins>) [**CLI backend plugin** Mapper une CLI IA locale vers le runner de repli textuel d’OpenClaw ](</fr/plugins/cli-backend-plugins>) [**Tool / hook plugin** Enregistrer des outils d’agent, des hooks d’événements ou des services - continuez ci-dessous ](</fr/plugins/hooks>)

Pour un plugin de canal qui n’est pas garanti d’être installé quand l’intégration/la configuration s’exécute, utilisez `createOptionalChannelSetupSurface(...)` depuis `openclaw/plugin-sdk/channel-setup`. Il produit une paire adaptateur de configuration + assistant qui annonce l’exigence d’installation et échoue de manière fermée lors des écritures de configuration réelles tant que le plugin n’est pas installé.

## Démarrage rapide : plugin d’outil

Ce guide crée un plugin minimal qui enregistre un outil d’agent. Les plugins de canal et de fournisseur ont des guides dédiés liés ci-dessus.

* ### Create the package and manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

Chaque plugin nécessite un manifeste, même sans configuration. Les outils enregistrés à l’exécution doivent être listés dans `contracts.tools` afin qu’OpenClaw puisse découvrir le plugin propriétaire sans charger chaque runtime de plugin. Les plugins doivent aussi déclarer `activation.onStartup` intentionnellement. Cet exemple le définit à `true`. Voir [Manifest](</fr/plugins/manifest>) pour le schéma complet. Les extraits canoniques de publication ClawHub se trouvent dans `docs/snippets/plugin-publish/`.

* ### Write the entry point

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` concerne les plugins qui ne sont pas des canaux. Pour les canaux, utilisez `defineChannelPluginEntry` \- voir [Plugins de canal](</fr/plugins/sdk-channel-plugins>). Pour les options complètes du point d’entrée, voir [Points d’entrée](</fr/plugins/sdk-entrypoints>).

* ### Test and publish

**Plugins externes :** validez et publiez avec ClawHub, puis installez :

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

Les spécifications de paquet nues comme `@myorg/openclaw-my-plugin` s’installent depuis npm pendant la transition de lancement. Utilisez `clawhub:` lorsque vous voulez la résolution ClawHub.

**Plugins dans le dépôt :** placez-les sous l’arborescence d’espace de travail des plugins groupés - ils sont découverts automatiquement.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Capacités des plugins

Un seul plugin peut enregistrer autant de capacités que nécessaire via l’objet `api` :

Capacité | Méthode d’enregistrement | Guide détaillé  
---|---|---  
Inférence textuelle (LLM) | `api.registerProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins>)  
Backend d’inférence CLI | `api.registerCliBackend(...)` | [Plugins de backend CLI](</fr/plugins/cli-backend-plugins>)  
Canal / messagerie | `api.registerChannel(...)` | [Plugins de canal](</fr/plugins/sdk-channel-plugins>)  
Parole (TTS/STT) | `api.registerSpeechProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Transcription en temps réel | `api.registerRealtimeTranscriptionProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Voix en temps réel | `api.registerRealtimeVoiceProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Compréhension des médias | `api.registerMediaUnderstandingProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Génération d’images | `api.registerImageGenerationProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Génération de musique | `api.registerMusicGenerationProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Génération de vidéos | `api.registerVideoGenerationProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Récupération web | `api.registerWebFetchProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Recherche web | `api.registerWebSearchProvider(...)` | [Plugins de fournisseur](</fr/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Middleware de résultat d’outil | `api.registerAgentToolResultMiddleware(...)` | [Vue d’ensemble du SDK](</fr/plugins/sdk-overview#registration-api>)  
Outils d’agent | `api.registerTool(...)` | Ci-dessous  
Commandes personnalisées | `api.registerCommand(...)` | [Points d’entrée](</fr/plugins/sdk-entrypoints>)  
Hooks de plugin | `api.on(...)` | [Hooks de plugin](</fr/plugins/hooks>)  
Hooks d’événements internes | `api.registerHook(...)` | [Points d’entrée](</fr/plugins/sdk-entrypoints>)  
Routes HTTP | `api.registerHttpRoute(...)` | [Internes](</fr/plugins/architecture-internals#gateway-http-routes>)  
Sous-commandes CLI | `api.registerCli(...)` | [Points d’entrée](</fr/plugins/sdk-entrypoints>)  
  
Pour l’API d’enregistrement complète, voir [Vue d’ensemble du SDK](</fr/plugins/sdk-overview#registration-api>).

Les plugins groupés peuvent utiliser `api.registerAgentToolResultMiddleware(...)` lorsqu’ils ont besoin d’une réécriture asynchrone des résultats d’outils avant que le modèle voie la sortie. Déclarez les runtimes ciblés dans `contracts.agentToolResultMiddleware`, par exemple `["pi", "codex"]`. Il s’agit d’un seam de plugin groupé de confiance ; les plugins externes devraient préférer les hooks de plugin OpenClaw ordinaires, sauf si OpenClaw ajoute une politique de confiance explicite pour cette capacité.

Si votre plugin enregistre des méthodes RPC de gateway personnalisées, gardez-les sous un préfixe propre au plugin. Les espaces de noms d’administration du cœur (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) restent réservés et se résolvent toujours vers `operator.admin`, même si un plugin demande une portée plus étroite.

Sémantique des garde-fous de hook à garder en tête :

  * `before_tool_call` : `{ block: true }` est terminal et arrête les gestionnaires de priorité inférieure.
  * `before_tool_call` : `{ block: false }` est traité comme une absence de décision.
  * `before_tool_call` : `{ requireApproval: true }` met en pause l’exécution de l’agent et demande l’approbation de l’utilisateur via la superposition d’approbation exec, les boutons Telegram, les interactions Discord ou la commande `/approve` sur n’importe quel canal.
  * `before_install` : `{ block: true }` est terminal et arrête les gestionnaires de priorité inférieure.
  * `before_install` : `{ block: false }` est traité comme une absence de décision.
  * `message_sending` : `{ cancel: true }` est terminal et arrête les gestionnaires de priorité inférieure.
  * `message_sending` : `{ cancel: false }` est traité comme une absence de décision.
  * `message_received` : préférez le champ typé `threadId` lorsque vous avez besoin du routage entrant de fil/sujet. Gardez `metadata` pour les extras propres au canal.
  * `message_sending` : préférez les champs de routage typés `replyToId` / `threadId` aux clés de métadonnées propres au canal.


La commande `/approve` gère à la fois les approbations exec et plugin avec un repli borné : lorsqu’un identifiant d’approbation exec est introuvable, OpenClaw réessaie le même identifiant via les approbations plugin. Le transfert des approbations plugin peut être configuré indépendamment via `approvals.plugin` dans la configuration.

Si une plomberie d’approbation personnalisée doit détecter ce même cas de repli borné, préférez `isApprovalNotFoundError` depuis `openclaw/plugin-sdk/error-runtime` au lieu de faire correspondre manuellement les chaînes d’expiration d’approbation.

Voir [Hooks de plugin](</fr/plugins/hooks>) pour des exemples et la référence des hooks.

## Enregistrement des outils d’agent

Les outils sont des fonctions typées que le LLM peut appeler. Ils peuvent être requis (toujours disponibles) ou optionnels (activation par l’utilisateur) :

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Les fabriques d’outils reçoivent un objet de contexte fourni par le runtime. Utilisez `ctx.activeModel` lorsqu’un outil doit journaliser, afficher ou s’adapter au modèle actif pour le tour actuel. L’objet peut inclure `provider`, `modelId` et `modelRef`. Traitez-le comme des métadonnées de runtime informatives, et non comme une frontière de sécurité contre l’opérateur local, le code de plugin installé ou un runtime OpenClaw modifié. Pour les outils locaux sensibles, conservez une activation explicite par le plugin ou l’opérateur et échouez de manière fermée lorsque les métadonnées du modèle actif sont absentes ou inadaptées.

Chaque outil enregistré avec `api.registerTool(...)` doit également être déclaré dans le manifeste du plugin :

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw capture et met en cache le descripteur validé de l’outil enregistré, afin que les plugins ne dupliquent pas les données `description` ou de schéma dans le manifeste. Le contrat de manifeste déclare uniquement la propriété et la découverte ; l’exécution appelle toujours l’implémentation vivante de l’outil enregistré. Définissez `toolMetadata.<tool>.optional: true` pour les outils enregistrés avec `api.registerTool(..., { optional: true })` afin qu’OpenClaw puisse éviter de charger ce runtime de plugin tant que l’outil n’est pas explicitement placé dans la liste d’autorisation.

Les utilisateurs activent les outils optionnels dans la configuration :

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * Les noms d’outils ne doivent pas entrer en conflit avec les outils du cœur (les conflits sont ignorés)
  * Les outils dont les objets d’enregistrement sont mal formés, y compris ceux auxquels il manque `parameters`, sont ignorés et signalés dans les diagnostics de plugin au lieu d’interrompre les exécutions d’agent
  * Utilisez `optional: true` pour les outils avec des effets de bord ou des exigences binaires supplémentaires
  * Les utilisateurs peuvent activer tous les outils d’un plugin en ajoutant l’identifiant du plugin à `tools.allow`


## Enregistrement de commandes CLI

Les plugins peuvent ajouter des groupes de commandes racine `openclaw` avec `api.registerCli`. Fournissez des `descriptors` pour chaque racine de commande de premier niveau afin qu’OpenClaw puisse afficher et router la commande sans charger avidement chaque runtime de plugin.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

Après l’installation, vérifiez l’enregistrement du runtime et exécutez la commande :

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## Conventions d’importation

Importez toujours depuis les chemins ciblés `openclaw/plugin-sdk/<subpath>` :

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

Pour la référence complète des sous-chemins, consultez [Vue d’ensemble du SDK](</fr/plugins/sdk-overview>).

Dans votre plugin, utilisez des fichiers barrel locaux (`api.ts`, `runtime-api.ts`) pour les imports internes - n’importez jamais votre propre plugin via son chemin SDK.

Pour les plugins de fournisseur, conservez les helpers propres au fournisseur dans ces barrels à la racine du paquet, sauf si la jonction est réellement générique. Exemples intégrés actuels :

  * Anthropic : wrappers de flux Claude et helpers `service_tier` / bêta
  * OpenAI : constructeurs de fournisseur, helpers de modèle par défaut, fournisseurs temps réel
  * OpenRouter : constructeur de fournisseur et helpers d’onboarding/configuration


Si un helper n’est utile qu’à l’intérieur d’un seul paquet de fournisseur intégré, conservez-le sur cette jonction à la racine du paquet au lieu de le promouvoir dans `openclaw/plugin-sdk/*`.

Certaines jonctions de helpers générées `openclaw/plugin-sdk/<bundled-id>` existent encore pour la maintenance des plugins intégrés lorsqu’elles ont un usage propriétaire suivi. Traitez-les comme des surfaces réservées, et non comme le modèle par défaut pour les nouveaux plugins tiers.

## Liste de vérification avant soumission

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** contient les métadonnées `openclaw` correctes OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Le manifeste **openclaw.plugin.json** est présent et valide OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Le point d’entrée utilise `defineChannelPluginEntry` ou `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Tous les imports utilisent des chemins ciblés `plugin-sdk/<subpath>` OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo