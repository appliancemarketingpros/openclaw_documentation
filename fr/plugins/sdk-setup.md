---
title: Installation et configuration du Plugin
source_url: https://docs.openclaw.ai/fr/plugins/sdk-setup
scraped_at: 2026-05-25
---

Référence pour l’empaquetage des plugins (métadonnées `package.json`), les manifestes (`openclaw.plugin.json`), les entrées de configuration et les schémas de configuration.

## Métadonnées du package

Votre `package.json` doit contenir un champ `openclaw` qui indique au système de plugins ce que fournit votre plugin :

### Plugin de canal

jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-channel",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "channel": {      "id": "my-channel",      "label": "My Channel",      "blurb": "Short description of the channel."    }  }}
[/code]

### Plugin de fournisseur / référence ClawHub

openclaw-clawhub-package.jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  }}
[/code]

### Champs `openclaw`

Fichiers de point d’entrée (relatifs à la racine du package).

Entrée légère réservée à la configuration (facultatif).

Métadonnées du catalogue de canaux pour les surfaces de configuration, de sélection, de démarrage rapide et d’état.

ID de fournisseurs enregistrés par ce plugin.

Indications d’installation : `npmSpec`, `localPath`, `defaultChoice`, `minHostVersion`, `expectedIntegrity`, `allowInvalidConfigRecovery`.

Indicateurs de comportement au démarrage.

### `openclaw.channel`

`openclaw.channel` est une métadonnée de package légère pour la découverte des canaux et les surfaces de configuration avant le chargement de l’exécution.

Champ | Type | Signification  
---|---|---  
`id` | `string` | ID canonique du canal.  
`label` | `string` | Libellé principal du canal.  
`selectionLabel` | `string` | Libellé du sélecteur/de la configuration lorsqu’il doit différer de `label`.  
`detailLabel` | `string` | Libellé de détail secondaire pour les catalogues de canaux et les surfaces d’état plus riches.  
`docsPath` | `string` | Chemin de documentation pour les liens de configuration et de sélection.  
`docsLabel` | `string` | Libellé de remplacement utilisé pour les liens de documentation lorsqu’il doit différer de l’ID du canal.  
`blurb` | `string` | Courte description d’intégration/de catalogue.  
`order` | `number` | Ordre de tri dans les catalogues de canaux.  
`aliases` | `string[]` | Alias de recherche supplémentaires pour la sélection de canal.  
`preferOver` | `string[]` | ID de plugins/canaux de priorité inférieure que ce canal doit devancer.  
`systemImage` | `string` | Nom facultatif d’icône/d’image système pour les catalogues d’interface de canal.  
`selectionDocsPrefix` | `string` | Texte de préfixe avant les liens de documentation dans les surfaces de sélection.  
`selectionDocsOmitLabel` | `boolean` | Afficher directement le chemin de documentation au lieu d’un lien de documentation libellé dans le texte de sélection.  
`selectionExtras` | `string[]` | Courtes chaînes supplémentaires ajoutées au texte de sélection.  
`markdownCapable` | `boolean` | Marque le canal comme compatible avec Markdown pour les décisions de mise en forme sortante.  
`exposure` | `object` | Contrôles de visibilité du canal pour la configuration, les listes configurées et les surfaces de documentation.  
`quickstartAllowFrom` | `boolean` | Inclure ce canal dans le flux de configuration standard de démarrage rapide `allowFrom`.  
`forceAccountBinding` | `boolean` | Exiger une liaison explicite du compte même lorsqu’un seul compte existe.  
`preferSessionLookupForAnnounceTarget` | `boolean` | Préférer la recherche de session lors de la résolution des cibles d’annonce pour ce canal.  
  
Exemple :

jsonCopy code
[code]
    {  "openclaw": {    "channel": {      "id": "my-channel",      "label": "My Channel",      "selectionLabel": "My Channel (self-hosted)",      "detailLabel": "My Channel Bot",      "docsPath": "/channels/my-channel",      "docsLabel": "my-channel",      "blurb": "Webhook-based self-hosted chat integration.",      "order": 80,      "aliases": ["mc"],      "preferOver": ["my-channel-legacy"],      "selectionDocsPrefix": "Guide:",      "selectionExtras": ["Markdown"],      "markdownCapable": true,      "exposure": {        "configured": true,        "setup": true,        "docs": true      },      "quickstartAllowFrom": true    }  }}
[/code]

`exposure` prend en charge :

  * `configured` : inclure le canal dans les surfaces de type liste configurée/état
  * `setup` : inclure le canal dans les sélecteurs interactifs de configuration
  * `docs` : marquer le canal comme public dans les surfaces de documentation/navigation


### `openclaw.install`

`openclaw.install` est une métadonnée de package, pas une métadonnée de manifeste.

Champ | Type | Signification  
---|---|---  
`clawhubSpec` | `string` | Spécification ClawHub canonique pour les flux d’installation/mise à jour et d’installation à la demande lors de l’intégration.  
`npmSpec` | `string` | Spécification npm canonique pour les flux de secours d’installation/mise à jour.  
`localPath` | `string` | Chemin d’installation local de développement ou groupé.  
`defaultChoice` | `"clawhub"` | `"npm"` | `"local"` | Source d’installation préférée lorsque plusieurs sources sont disponibles.  
`minHostVersion` | `string` | Version minimale prise en charge d’OpenClaw sous la forme `>=x.y.z` ou `>=x.y.z-prerelease`.  
`expectedIntegrity` | `string` | Chaîne d’intégrité npm dist attendue, généralement `sha512-...`, pour les installations épinglées.  
`allowInvalidConfigRecovery` | `boolean` | Permet aux flux de réinstallation de plugins groupés de récupérer certaines défaillances de configuration obsolète.  
  
Comportement d’intégration

L’intégration interactive utilise également `openclaw.install` pour les surfaces d’installation à la demande. Si votre plugin expose des choix d’authentification de fournisseur ou des métadonnées de configuration/catalogue de canal avant le chargement de l’exécution, l’intégration peut afficher ce choix, demander une installation via ClawHub, npm ou locale, installer ou activer le plugin, puis poursuivre le flux sélectionné. Les choix d’intégration ClawHub utilisent `clawhubSpec` et sont préférés lorsqu’ils sont présents ; les choix npm exigent des métadonnées de catalogue fiables avec un `npmSpec` de registre ; les versions exactes et `expectedIntegrity` sont des épinglages npm facultatifs. Si `expectedIntegrity` est présent, les flux d’installation/mise à jour l’appliquent pour npm. Conservez les métadonnées « quoi afficher » dans `openclaw.plugin.json` et les métadonnées « comment l’installer » dans `package.json`.

Application de minHostVersion

Si `minHostVersion` est défini, l’installation et le chargement du registre de manifestes non groupé l’appliquent tous deux. Les hôtes plus anciens ignorent les plugins externes ; les chaînes de version invalides sont rejetées. Les plugins source groupés sont supposés être dans la même version que l’extraction de l’hôte.

Installations npm épinglées

Pour les installations npm épinglées, conservez la version exacte dans `npmSpec` et ajoutez l’intégrité attendue de l’artefact :

jsonCopy code
[code]
    {  "openclaw": {    "install": {      "npmSpec": "@wecom/wecom-openclaw-plugin@1.2.3",      "expectedIntegrity": "sha512-REPLACE_WITH_NPM_DIST_INTEGRITY",      "defaultChoice": "npm"    }  }}
[/code]

Portée de allowInvalidConfigRecovery

`allowInvalidConfigRecovery` n’est pas un contournement général pour les configurations défectueuses. Il est réservé à la récupération étroite de plugins groupés, afin que la réinstallation/configuration puisse réparer des restes de mise à niveau connus, comme un chemin de plugin groupé manquant ou une entrée `channels.<id>` obsolète pour ce même plugin. Si la configuration est rompue pour des raisons non liées, l’installation échoue toujours de manière fermée et indique à l’opérateur d’exécuter `openclaw doctor --fix`.

### Chargement complet différé

Les plugins de canal peuvent opter pour le chargement différé avec :

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "startup": {      "deferConfiguredChannelFullLoadUntilAfterListen": true    }  }}
[/code]

Lorsqu’il est activé, OpenClaw ne charge que `setupEntry` pendant la phase de démarrage avant écoute, même pour les canaux déjà configurés. L’entrée complète se charge après que le gateway commence à écouter.

Si votre entrée de configuration/complète enregistre des méthodes RPC de gateway, conservez-les sous un préfixe propre au plugin. Les espaces de noms d’administration réservés du cœur (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) restent détenus par le cœur et se résolvent toujours vers `operator.admin`.

## Manifeste de plugin

Chaque plugin natif doit fournir un `openclaw.plugin.json` à la racine du package. OpenClaw l’utilise pour valider la configuration sans exécuter le code du plugin.

jsonCopy code
[code]
    {  "id": "my-plugin",  "name": "My Plugin",  "description": "Adds My Plugin capabilities to OpenClaw",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {      "webhookSecret": {        "type": "string",        "description": "Webhook verification secret"      }    }  }}
[/code]

Pour les plugins de canal, ajoutez `kind` et `channels` :

jsonCopy code
[code]
    {  "id": "my-channel",  "kind": "channel",  "channels": ["my-channel"],  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  }}
[/code]

Même les plugins sans configuration doivent fournir un schéma. Un schéma vide est valide :

jsonCopy code
[code]
    {  "id": "my-plugin",  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

Consultez [Manifeste de plugin](</fr/plugins/manifest>) pour la référence complète du schéma.

## Publication ClawHub

Pour les packages de plugins, utilisez la commande ClawHub propre au package :

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

## Entrée de configuration

Le fichier `setup-entry.ts` est une alternative légère à `index.ts` qu’OpenClaw charge lorsqu’il n’a besoin que des surfaces de configuration (intégration initiale, réparation de configuration, inspection des canaux désactivés).

typescriptCopy code
[code]
    // setup-entry.ts  export default defineSetupPluginEntry(myChannelPlugin);
[/code]

Cela évite de charger du code d’exécution lourd (bibliothèques de cryptographie, enregistrements CLI, services d’arrière-plan) pendant les flux de configuration.

Les canaux de l’espace de travail intégré qui conservent des exports compatibles avec la configuration dans des modules sidecar peuvent utiliser `defineBundledChannelSetupEntry(...)` depuis `openclaw/plugin-sdk/channel-entry-contract` au lieu de `defineSetupPluginEntry(...)`. Ce contrat intégré prend aussi en charge un export `runtime` facultatif afin que le câblage d’exécution au moment de la configuration reste léger et explicite.

Quand OpenClaw utilise setupEntry au lieu de l’entrée complète

  * Le canal est désactivé mais nécessite des surfaces de configuration/intégration initiale.
  * Le canal est activé mais non configuré.
  * Le chargement différé est activé (`deferConfiguredChannelFullLoadUntilAfterListen`).

Ce que setupEntry doit enregistrer

  * L’objet Plugin de canal (via `defineSetupPluginEntry`).
  * Toutes les routes HTTP requises avant l’écoute du Gateway.
  * Toutes les méthodes du Gateway nécessaires au démarrage.


Ces méthodes du Gateway au démarrage doivent toujours éviter les espaces de noms d’administration réservés au cœur, tels que `config.*` ou `update.*`.

Ce que setupEntry ne doit PAS inclure

  * Les enregistrements CLI.
  * Les services d’arrière-plan.
  * Les imports d’exécution lourds (cryptographie, SDK).
  * Les méthodes du Gateway nécessaires uniquement après le démarrage.


### Imports étroits des assistants de configuration

Pour les chemins actifs uniquement liés à la configuration, préférez les coutures étroites d’assistants de configuration à l’interface plus large `plugin-sdk/setup` lorsque vous n’avez besoin que d’une partie de la surface de configuration :

Chemin d’import | À utiliser pour | Exports clés  
---|---|---  
`plugin-sdk/setup-runtime` | assistants d’exécution au moment de la configuration qui restent disponibles dans `setupEntry` / démarrage différé du canal | `createPatchedAccountSetupAdapter`, `createEnvPatchedAccountSetupAdapter`, `createSetupInputPresenceValidator`, `noteChannelLookupFailure`, `noteChannelLookupSummary`, `promptResolvedAllowFrom`, `splitSetupEntries`, `createAllowlistSetupWizardProxy`, `createDelegatedSetupWizardProxy`  
`plugin-sdk/setup-adapter-runtime` | alias de compatibilité obsolète ; utilisez `plugin-sdk/setup-runtime` | `createEnvPatchedAccountSetupAdapter`  
`plugin-sdk/setup-tools` | assistants CLI/archive/docs pour configuration/installation | `formatCliCommand`, `detectBinary`, `extractArchive`, `resolveBrewExecutable`, `formatDocsLink`, `CONFIG_DIR`  
  
Utilisez la couture plus large `plugin-sdk/setup` lorsque vous voulez toute la boîte à outils de configuration partagée, y compris les assistants de correctif de configuration tels que `moveSingleAccountChannelSectionToDefaultAccount(...)`.

Les adaptateurs de correctif de configuration restent sûrs à importer sur les chemins actifs. Leur recherche de surface de contrat intégrée pour la promotion de compte unique est paresseuse, donc l’import de `plugin-sdk/setup-runtime` ne charge pas immédiatement la découverte de surface de contrat intégrée avant l’utilisation réelle de l’adaptateur.

### Promotion de compte unique détenue par le canal

Lorsqu’un canal passe d’une configuration de premier niveau à compte unique à `channels.<id>.accounts.*`, le comportement partagé par défaut consiste à déplacer les valeurs promues propres au compte dans `accounts.default`.

Les canaux intégrés peuvent restreindre ou remplacer cette promotion via leur surface de contrat de configuration :

  * `singleAccountKeysToMove` : clés de premier niveau supplémentaires qui doivent être déplacées dans le compte promu
  * `namedAccountPromotionKeys` : lorsque des comptes nommés existent déjà, seules ces clés sont déplacées dans le compte promu ; les clés partagées de politique/livraison restent à la racine du canal
  * `resolveSingleAccountPromotionTarget(...)` : choisir quel compte existant reçoit les valeurs promues


## Schéma de configuration

La configuration du Plugin est validée par rapport au JSON Schema de votre manifeste. Les utilisateurs configurent les plugins via :

json5Copy code
[code]
    {  plugins: {    entries: {      "my-plugin": {        config: {          webhookSecret: "abc123",        },      },    },  },}
[/code]

Votre Plugin reçoit cette configuration sous forme de `api.pluginConfig` pendant l’enregistrement.

Pour une configuration propre à un canal, utilisez plutôt la section de configuration du canal :

json5Copy code
[code]
    {  channels: {    "my-channel": {      token: "bot-token",      allowFrom: ["user1", "user2"],    },  },}
[/code]

### Créer des schémas de configuration de canal

Utilisez `buildChannelConfigSchema` pour convertir un schéma Zod dans l’enveloppe `ChannelConfigSchema` utilisée par les artefacts de configuration détenus par le Plugin :

typescriptCopy code
[code]
      const accountSchema = z.object({  token: z.string().optional(),  allowFrom: z.array(z.string()).optional(),  accounts: z.object({}).catchall(z.any()).optional(),  defaultAccount: z.string().optional(),}); const configSchema = buildChannelConfigSchema(accountSchema);
[/code]

Si vous rédigez déjà le contrat en JSON Schema ou TypeBox, utilisez l’assistant direct afin qu’OpenClaw puisse éviter la conversion Zod vers JSON Schema sur les chemins de métadonnées :

typescriptCopy code
[code]
      const configSchema = buildJsonChannelConfigSchema(  Type.Object({    token: Type.Optional(Type.String()),    allowFrom: Type.Optional(Type.Array(Type.String())),  }),);
[/code]

Pour les plugins tiers, le contrat de chemin froid reste le manifeste du Plugin : reflétez le JSON Schema généré dans `openclaw.plugin.json#channelConfigs` afin que le schéma de configuration, la configuration et les surfaces UI puissent inspecter `channels.<id>` sans charger le code d’exécution.

## Assistants de configuration

Les Plugins de canal peuvent fournir des assistants de configuration interactifs pour `openclaw onboard`. L’assistant est un objet `ChannelSetupWizard` sur le `ChannelPlugin` :

typescriptCopy code
[code]
     const setupWizard: ChannelSetupWizard = {  channel: "my-channel",  status: {    configuredLabel: "Connected",    unconfiguredLabel: "Not configured",    resolveConfigured: ({ cfg }) => Boolean((cfg.channels as any)?.["my-channel"]?.token),  },  credentials: [    {      inputKey: "token",      providerHint: "my-channel",      credentialLabel: "Bot token",      preferredEnvVar: "MY_CHANNEL_BOT_TOKEN",      envPrompt: "Use MY_CHANNEL_BOT_TOKEN from environment?",      keepPrompt: "Keep current token?",      inputPrompt: "Enter your bot token:",      inspect: ({ cfg, accountId }) => {        const token = (cfg.channels as any)?.["my-channel"]?.token;        return {          accountConfigured: Boolean(token),          hasConfiguredValue: Boolean(token),        };      },    },  ],};
[/code]

Le type `ChannelSetupWizard` prend en charge `credentials`, `textInputs`, `dmPolicy`, `allowFrom`, `groupAccess`, `prepare`, `finalize`, et plus encore. Consultez les paquets de Plugins intégrés (par exemple le Plugin Discord `src/channel.setup.ts`) pour des exemples complets.

Invites allowFrom partagées

Pour les invites de liste d’autorisation DM qui n’ont besoin que du flux standard `note -> prompt -> parse -> merge -> patch`, préférez les assistants de configuration partagés de `openclaw/plugin-sdk/setup` : `createPromptParsedAllowFromForAccount(...)`, `createTopLevelChannelParsedAllowFromPrompt(...)` et `createNestedChannelParsedAllowFromPrompt(...)`.

État standard de configuration de canal

Pour les blocs d’état de configuration de canal qui ne varient que par les libellés, scores et lignes supplémentaires facultatives, préférez `createStandardChannelSetupStatus(...)` depuis `openclaw/plugin-sdk/setup` au lieu de recréer manuellement le même objet `status` dans chaque Plugin.

Surface de configuration de canal facultative

Pour les surfaces de configuration facultatives qui ne doivent apparaître que dans certains contextes, utilisez `createOptionalChannelSetupSurface` depuis `openclaw/plugin-sdk/channel-setup` :

typescriptCopy code
[code]
    import { createOptionalChannelSetupSurface } from "openclaw/plugin-sdk/channel-setup"; const setupSurface = createOptionalChannelSetupSurface({  channel: "my-channel",  label: "My Channel",  npmSpec: "@myorg/openclaw-my-channel",  docsPath: "/channels/my-channel",});// Returns { setupAdapter, setupWizard }
[/code]

`plugin-sdk/channel-setup` expose aussi les constructeurs de plus bas niveau `createOptionalChannelSetupAdapter(...)` et `createOptionalChannelSetupWizard(...)` lorsque vous n’avez besoin que d’une moitié de cette surface d’installation facultative.

L’adaptateur et l’assistant facultatifs générés échouent de façon fermée lors de véritables écritures de configuration. Ils réutilisent un même message d’installation requise dans `validateInput`, `applyAccountConfig` et `finalize`, et ajoutent un lien vers la documentation lorsque `docsPath` est défini.

Assistants de configuration adossés à un binaire

Pour les UI de configuration adossées à un binaire, préférez les assistants délégués partagés au lieu de copier la même colle binaire/état dans chaque canal :

  * `createDetectedBinaryStatus(...)` pour les blocs d’état qui ne varient que par les libellés, indices, scores et la détection du binaire
  * `createCliPathTextInput(...)` pour les champs texte adossés à un chemin
  * `createDelegatedSetupWizardStatusResolvers(...)`, `createDelegatedPrepare(...)`, `createDelegatedFinalize(...)` et `createDelegatedResolveConfigured(...)` lorsque `setupEntry` doit transmettre paresseusement à un assistant complet plus lourd
  * `createDelegatedTextInputShouldPrompt(...)` lorsque `setupEntry` doit seulement déléguer une décision `textInputs[*].shouldPrompt`


## Publication et installation

**Plugins externes :** publiez sur [ClawHub](</fr/clawhub>), puis installez :

### npm

bashCopy code
[code]
    openclaw plugins install @myorg/openclaw-my-plugin
[/code]

Les spécifications de paquet nues s’installent depuis npm pendant la transition de lancement.

### ClawHub uniquement

bashCopy code
[code]
    openclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

### Spécification de paquet npm

Utilisez npm lorsqu’un paquet n’a pas encore été déplacé vers ClawHub, ou lorsque vous avez besoin d’un chemin d’installation npm direct pendant la migration :

bashCopy code
[code]
    openclaw plugins install npm:@myorg/openclaw-my-plugin
[/code]

**Plugins dans le dépôt :** placez-les sous l’arborescence de l’espace de travail des Plugins groupés, et ils sont automatiquement découverts pendant la compilation.

**Les utilisateurs peuvent installer :**

bashCopy code
[code]
    openclaw plugins install <package-name>
[/code]

Les métadonnées des packages groupés sont explicites, et non déduites du JavaScript compilé au démarrage du gateway. Les dépendances d’exécution appartiennent au package du Plugin qui les possède ; le démarrage d’OpenClaw packagé ne répare ni ne met jamais en miroir les dépendances des Plugins.

## Associés

  * [Créer des Plugins](</fr/plugins/building-plugins>) — guide de démarrage étape par étape
  * [Manifeste de Plugin](</fr/plugins/manifest>) — référence complète du schéma de manifeste
  * [Points d’entrée du SDK](</fr/plugins/sdk-entrypoints>) — `definePluginEntry` et `defineChannelPluginEntry`


Was this useful?YesNo