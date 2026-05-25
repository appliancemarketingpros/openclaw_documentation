---
title: Wiki de mémoire
source_url: https://docs.openclaw.ai/fr/plugins/memory-wiki
scraped_at: 2026-05-25
---

`memory-wiki` est un plugin intégré qui transforme la mémoire durable en un coffre de connaissances compilé.

Il ne remplace **pas** le plugin de mémoire active. Le plugin de mémoire active reste responsable du rappel, de la promotion, de l’indexation et du dreaming. `memory-wiki` fonctionne à ses côtés et compile les connaissances durables dans un wiki navigable avec des pages déterministes, des affirmations structurées, la provenance, des tableaux de bord et des résumés lisibles par machine.

Utilisez-le lorsque vous voulez que la mémoire se comporte davantage comme une couche de connaissances maintenue que comme un ensemble de fichiers Markdown.

## Ce qu’il ajoute

  * Un coffre wiki dédié avec une mise en page déterministe des pages
  * Des métadonnées structurées d’affirmation et de preuve, pas seulement de la prose
  * Provenance, confiance, contradictions et questions ouvertes au niveau des pages
  * Des résumés compilés pour les consommateurs agent/runtime
  * Des outils wiki natifs de recherche/lecture/application/lint
  * Un mode passerelle facultatif qui importe les artefacts publics depuis le plugin de mémoire active
  * Un mode de rendu compatible Obsidian facultatif et une intégration CLI


## Comment il s’intègre à la mémoire

Pensez à la séparation ainsi :

Couche | Responsable  
---|---  
Plugin de mémoire active (`memory-core`, QMD, Honcho, etc.) | Rappel, recherche sémantique, promotion, dreaming, runtime mémoire  
`memory-wiki` | Pages wiki compilées, synthèses riches en provenance, tableaux de bord, recherche/lecture/application propres au wiki  
  
Si le plugin de mémoire active expose des artefacts de rappel partagés, OpenClaw peut rechercher dans les deux couches en une seule passe avec `memory_search corpus=all`.

Lorsque vous avez besoin d’un classement spécifique au wiki, de provenance ou d’un accès direct aux pages, utilisez plutôt les outils wiki natifs.

## Modèle hybride recommandé

Un bon choix par défaut pour les configurations locales-first est :

  * QMD comme backend de mémoire active pour le rappel et la recherche sémantique large
  * `memory-wiki` en mode `bridge` pour les pages de connaissances durables synthétisées


Cette séparation fonctionne bien, car chaque couche reste concentrée sur son rôle :

  * QMD garde les notes brutes, les exports de session et les collections supplémentaires consultables
  * `memory-wiki` compile les entités stables, les affirmations, les tableaux de bord et les pages sources


Règle pratique :

  * utilisez `memory_search` lorsque vous voulez une passe de rappel large sur la mémoire
  * utilisez `wiki_search` et `wiki_get` lorsque vous voulez des résultats wiki tenant compte de la provenance
  * utilisez `memory_search corpus=all` lorsque vous voulez que la recherche partagée couvre les deux couches


Si le mode passerelle signale zéro artefact exporté, le plugin de mémoire active n’expose pas encore d’entrées de passerelle publiques. Exécutez d’abord `openclaw wiki doctor`, puis confirmez que le plugin de mémoire active prend en charge les artefacts publics.

Lorsque le mode passerelle est actif et que `bridge.readMemoryArtifacts` est activé, `openclaw wiki status`, `openclaw wiki doctor` et `openclaw wiki bridge import` lisent via le Gateway en cours d’exécution. Cela garde les vérifications CLI de la passerelle alignées avec le contexte du plugin de mémoire runtime. Si la passerelle est désactivée ou si la lecture des artefacts est désactivée, ces commandes conservent leur comportement local/hors ligne.

## Modes de coffre

`memory-wiki` prend en charge trois modes de coffre :

### `isolated`

Coffre propre, sources propres, aucune dépendance à `memory-core`.

Utilisez ceci lorsque vous voulez que le wiki soit son propre magasin de connaissances organisé.

### `bridge`

Lit les artefacts mémoire publics et les événements mémoire depuis le plugin de mémoire active via les coutures publiques du SDK de plugin.

Utilisez ceci lorsque vous voulez que le wiki compile et organise les artefacts exportés par le plugin de mémoire sans accéder aux détails internes privés du plugin.

Le mode passerelle peut indexer :

  * les artefacts mémoire exportés
  * les rapports de rêve
  * les notes quotidiennes
  * les fichiers racine de mémoire
  * les journaux d’événements mémoire


### `unsafe-local`

Échappatoire explicite sur la même machine pour les chemins privés locaux.

Ce mode est volontairement expérimental et non portable. Utilisez-le seulement si vous comprenez la frontière de confiance et avez spécifiquement besoin d’un accès au système de fichiers local que le mode passerelle ne peut pas fournir.

## Disposition du coffre

Le plugin initialise un coffre comme ceci :

textCopy code
[code]
    <vault>/  AGENTS.md  WIKI.md  index.md  inbox.md  entities/  concepts/  syntheses/  sources/  reports/  _attachments/  _views/  .openclaw-wiki/
[/code]

Le contenu géré reste dans des blocs générés. Les blocs de notes humaines sont préservés.

Les principaux groupes de pages sont :

  * `sources/` pour le matériau brut importé et les pages soutenues par la passerelle
  * `entities/` pour les éléments, personnes, systèmes, projets et objets durables
  * `concepts/` pour les idées, abstractions, modèles et politiques
  * `syntheses/` pour les résumés compilés et les regroupements maintenus
  * `reports/` pour les tableaux de bord générés


## Affirmations structurées et preuves

Les pages peuvent contenir du frontmatter `claims` structuré, pas seulement du texte libre.

Chaque affirmation peut inclure :

  * `id`
  * `text`
  * `status`
  * `confidence`
  * `evidence[]`
  * `updatedAt`


Les entrées de preuve peuvent inclure :

  * `kind`
  * `sourceId`
  * `path`
  * `lines`
  * `weight`
  * `confidence`
  * `privacyTier`
  * `note`
  * `updatedAt`


C’est ce qui fait que le wiki agit davantage comme une couche de croyances que comme un dépôt passif de notes. Les affirmations peuvent être suivies, notées, contestées et résolues jusqu’aux sources.

## Métadonnées d’entité destinées aux agents

Les pages d’entité peuvent aussi contenir des métadonnées de routage destinées aux agents. Il s’agit de frontmatter générique, donc cela fonctionne pour les personnes, équipes, systèmes, projets ou tout autre type d’entité.

Les champs courants incluent :

  * `entityType` : par exemple `person`, `team`, `system` ou `project`
  * `canonicalId` : clé d’identité stable utilisée entre les alias et les imports
  * `aliases` : noms, identifiants ou libellés qui doivent résoudre vers la même page
  * `privacyTier` : `public`, `local-private`, `sensitive` ou `confirm-before-use`
  * `bestUsedFor` / `notEnoughFor` : indices de routage compacts
  * `lastRefreshedAt` : horodatage de rafraîchissement des sources distinct du moment de modification de la page
  * `personCard` : carte de routage facultative propre à une personne avec identifiants, réseaux sociaux, e-mails, fuseau horaire, voie, à demander, à éviter de demander, confiance et confidentialité
  * `relationships` : arêtes typées vers des pages liées avec cible, type, poids, confiance, type de preuve, niveau de confidentialité et note


Pour un wiki de personnes, l’agent devrait généralement commencer par `reports/person-agent-directory.md`, puis ouvrir la page de la personne avec `wiki_get` avant d’utiliser des coordonnées ou des faits inférés.

Exemple :

yamlCopy code
[code]
    pageType: entityentityType: personid: entity.brad-grouxcanonicalId: maintainer.brad-grouxaliases:  - Brad  - bgrouxprivacyTier: local-privatebestUsedFor:  - Microsoft Teams and Azure routingnotEnoughFor:  - legal approvallastRefreshedAt: "2026-04-29T00:00:00.000Z"personCard:  handles:    - "@bgroux"  socials:    - "https://x.example/bgroux"  emails:    - brad@example.com  timezone: America/Chicago  lane: Microsoft ecosystem  askFor:    - Teams rollout questions  avoidAskingFor:    - unrelated billing decisions  confidence: 0.8  privacyTier: confirm-before-userelationships:  - targetId: entity.alice    targetTitle: Alice    kind: collaborates-with    confidence: 0.7    evidenceKind: discrawl-statclaims:  - id: claim.brad.teams    text: Brad is useful for Microsoft Teams routing.    status: supported    confidence: 0.9    evidence:      - kind: maintainer-whois        sourceId: source.maintainers        privacyTier: local-private
[/code]

## Pipeline de compilation

L’étape de compilation lit les pages wiki, normalise les résumés et émet des artefacts stables destinés aux machines sous :

  * `.openclaw-wiki/cache/agent-digest.json`
  * `.openclaw-wiki/cache/claims.jsonl`


Ces résumés existent pour que les agents et le code runtime n’aient pas à extraire le contenu des pages Markdown.

La sortie compilée alimente aussi :

  * l’indexation wiki de première passe pour les flux de recherche/lecture
  * la recherche d’identifiants d’affirmation vers les pages propriétaires
  * les suppléments d’invite compacts
  * la génération de rapports/tableaux de bord


## Tableaux de bord et rapports de santé

Lorsque `render.createDashboards` est activé, la compilation maintient des tableaux de bord sous `reports/`.

Les rapports intégrés incluent :

  * `reports/open-questions.md`
  * `reports/contradictions.md`
  * `reports/low-confidence.md`
  * `reports/claim-health.md`
  * `reports/stale-pages.md`
  * `reports/person-agent-directory.md`
  * `reports/relationship-graph.md`
  * `reports/provenance-coverage.md`
  * `reports/privacy-review.md`


Ces rapports suivent des éléments comme :

  * les groupes de notes contradictoires
  * les groupes d’affirmations concurrentes
  * les affirmations sans preuve structurée
  * les pages et affirmations à faible confiance
  * la fraîcheur obsolète ou inconnue
  * les pages avec des questions non résolues
  * les cartes de routage personne/entité
  * les arêtes de relation structurées
  * la couverture des classes de preuve
  * les niveaux de confidentialité non publics qui nécessitent un examen avant utilisation


## Recherche et récupération

`memory-wiki` prend en charge deux backends de recherche :

  * `shared` : utiliser le flux de recherche mémoire partagé lorsqu’il est disponible
  * `local` : rechercher localement dans le wiki


Il prend aussi en charge trois corpus :

  * `wiki`
  * `memory`
  * `all`


Comportement important :

  * `wiki_search` et `wiki_get` utilisent les résumés compilés comme première passe lorsque c’est possible
  * les identifiants d’affirmation peuvent résoudre vers la page propriétaire
  * les affirmations contestées/obsolètes/fraîches influencent le classement
  * les libellés de provenance peuvent persister dans les résultats
  * le mode de recherche peut orienter le classement pour la recherche de personne, le routage de questions, les preuves sources ou les affirmations brutes


Règle pratique :

  * utilisez `memory_search corpus=all` pour une passe de rappel large
  * utilisez `wiki_search` \+ `wiki_get` lorsque le classement propre au wiki, la provenance ou la structure de croyance au niveau des pages vous importe


Modes de recherche :

  * `auto` : valeur par défaut équilibrée
  * `find-person` : renforce les entités de type personne, les alias, les identifiants, les réseaux sociaux et les identifiants canoniques
  * `route-question` : renforce les cartes d’agent, les indices à demander, les indices d’usage recommandé et le contexte de relation
  * `source-evidence` : renforce les pages sources et les métadonnées de preuve structurées
  * `raw-claim` : renforce les affirmations structurées correspondantes et renvoie les métadonnées d’affirmation/preuve dans les résultats


Lorsqu’un résultat correspond à une affirmation structurée, `wiki_search` peut renvoyer `matchedClaimId`, `matchedClaimStatus`, `matchedClaimConfidence`, `evidenceKinds` et `evidenceSourceIds` dans sa charge utile de détails. La sortie texte inclut aussi des lignes compactes `Claim:` et `Evidence:` lorsqu’elles sont disponibles.

## Outils d’agent

Le plugin enregistre ces outils :

  * `wiki_status`
  * `wiki_search`
  * `wiki_get`
  * `wiki_apply`
  * `wiki_lint`


Ce qu’ils font :

  * `wiki_status` : mode de coffre actuel, santé, disponibilité de la CLI Obsidian
  * `wiki_search` : recherche dans les pages wiki et, lorsque configuré, les corpus mémoire partagés ; accepte `mode` pour la recherche de personne, le routage de questions, les preuves sources ou l’exploration d’affirmations brutes
  * `wiki_get` : lit une page wiki par id/chemin ou bascule vers le corpus mémoire partagé
  * `wiki_apply` : mutations ciblées de synthèse/métadonnées sans chirurgie libre des pages
  * `wiki_lint` : vérifications structurelles, lacunes de provenance, contradictions, questions ouvertes


Le plugin enregistre aussi un supplément de corpus mémoire non exclusif, afin que les recherches partagées `memory_search` et `memory_get` puissent atteindre le wiki lorsque le plugin de mémoire active prend en charge la sélection de corpus.

## Comportement des invites et du contexte

Lorsque `context.includeCompiledDigestPrompt` est activé, les sections d’invite mémoire ajoutent un instantané compilé compact depuis `agent-digest.json`.

Cet instantané est volontairement petit et à fort signal :

  * seulement les principales pages
  * seulement les principales affirmations
  * nombre de contradictions
  * nombre de questions
  * qualificatifs de confiance/fraîcheur


C’est optionnel, car cela change la forme des invites et se révèle surtout utile pour les moteurs de contexte ou les assemblages d’invites hérités qui consomment explicitement des suppléments mémoire.

## Configuration

Placez la configuration sous `plugins.entries.memory-wiki.config` :

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-wiki": {        enabled: true,        config: {          vaultMode: "isolated",          vault: {            path: "~/.openclaw/wiki/main",            renderMode: "obsidian",          },          obsidian: {            enabled: true,            useOfficialCli: true,            vaultName: "OpenClaw Wiki",            openAfterWrites: false,          },          bridge: {            enabled: false,            readMemoryArtifacts: true,            indexDreamReports: true,            indexDailyNotes: true,            indexMemoryRoot: true,            followMemoryEvents: true,          },          ingest: {            autoCompile: true,            maxConcurrentJobs: 1,            allowUrlIngest: true,          },          search: {            backend: "shared",            corpus: "wiki",          },          context: {            includeCompiledDigestPrompt: false,          },          render: {            preserveHumanBlocks: true,            createBacklinks: true,            createDashboards: true,          },        },      },    },  },}
[/code]

Bascules clés :

  * `vaultMode` : `isolated`, `bridge`, `unsafe-local`
  * `vault.renderMode` : `native` ou `obsidian`
  * `bridge.readMemoryArtifacts` : importer les artefacts publics du Plugin de mémoire active
  * `bridge.followMemoryEvents` : inclure les journaux d’événements en mode bridge
  * `search.backend` : `shared` ou `local`
  * `search.corpus` : `wiki`, `memory` ou `all`
  * `context.includeCompiledDigestPrompt` : ajouter l’instantané de résumé compact aux sections d’invite de mémoire
  * `render.createBacklinks` : générer des blocs associés déterministes
  * `render.createDashboards` : générer des pages de tableau de bord


### Exemple : QMD + mode bridge

Utilisez ceci lorsque vous voulez QMD pour le rappel et `memory-wiki` pour une couche de connaissances maintenue :

json5Copy code
[code]
    {  memory: {    backend: "qmd",  },  plugins: {    entries: {      "memory-wiki": {        enabled: true,        config: {          vaultMode: "bridge",          bridge: {            enabled: true,            readMemoryArtifacts: true,            indexDreamReports: true,            indexDailyNotes: true,            indexMemoryRoot: true,            followMemoryEvents: true,          },          search: {            backend: "shared",            corpus: "all",          },          context: {            includeCompiledDigestPrompt: false,          },        },      },    },  },}
[/code]

Cela conserve :

  * QMD responsable du rappel de la mémoire active
  * `memory-wiki` concentré sur les pages compilées et les tableaux de bord
  * la forme de l’invite inchangée jusqu’à ce que vous activiez intentionnellement les invites de résumé compilé


## CLI

`memory-wiki` expose également une surface CLI de premier niveau :

bashCopy code
[code]
    openclaw wiki statusopenclaw wiki doctoropenclaw wiki initopenclaw wiki ingest ./notes/alpha.mdopenclaw wiki compileopenclaw wiki lintopenclaw wiki search "alpha"openclaw wiki get entity.alphaopenclaw wiki apply synthesis "Alpha Summary" --body "..." --source-id source.alphaopenclaw wiki bridge importopenclaw wiki obsidian status
[/code]

Consultez [CLI : wiki](</fr/cli/wiki>) pour la référence complète des commandes.

## Prise en charge d’Obsidian

Lorsque `vault.renderMode` vaut `obsidian`, le Plugin écrit du Markdown compatible avec Obsidian et peut éventuellement utiliser la CLI officielle `obsidian`.

Les workflows pris en charge incluent :

  * la vérification de l’état
  * la recherche dans le coffre
  * l’ouverture d’une page
  * l’appel d’une commande Obsidian
  * l’accès direct à la note quotidienne


C’est facultatif. Le wiki fonctionne toujours en mode natif sans Obsidian.

## Workflow recommandé

  1. Conservez votre Plugin de mémoire active pour le rappel, la promotion et la rêverie.
  2. Activez `memory-wiki`.
  3. Commencez par le mode `isolated`, sauf si vous souhaitez explicitement le mode bridge.
  4. Utilisez `wiki_search` / `wiki_get` lorsque la provenance est importante.
  5. Utilisez `wiki_apply` pour des synthèses limitées ou des mises à jour de métadonnées.
  6. Exécutez `wiki_lint` après des modifications significatives.
  7. Activez les tableaux de bord si vous voulez de la visibilité sur les contenus obsolètes ou les contradictions.


## Docs connexes

  * [Vue d’ensemble de la mémoire](</fr/concepts/memory>)
  * [CLI : mémoire](</fr/cli/memory>)
  * [CLI : wiki](</fr/cli/wiki>)
  * [Présentation du Plugin SDK](</fr/plugins/sdk-overview>)


Was this useful?YesNo