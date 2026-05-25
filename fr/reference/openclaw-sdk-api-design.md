---
title: Conception de l’API du SDK d’application OpenClaw
source_url: https://docs.openclaw.ai/fr/reference/openclaw-sdk-api-design
scraped_at: 2026-05-25
---

Cette page est la conception de référence API détaillée du [SDK d’application OpenClaw](</fr/concepts/openclaw-sdk>) public. Elle est volontairement séparée du [Plugin SDK](</fr/plugins/sdk-overview>).

Le SDK d’application public doit être construit en deux couches :

  1. Un client Gateway généré de bas niveau.
  2. Un wrapper ergonomique de haut niveau avec des objets `OpenClaw`, `Agent`, `Session`, `Run`, `Task`, `Artifact`, `Approval` et `Environment`.


## Conception des espaces de noms

Les espaces de noms de bas niveau doivent suivre de près les ressources Gateway :

typescriptCopy code
[code]
    oc.agents.list();oc.agents.get("main");oc.agents.create(...);oc.agents.update(...); oc.sessions.list();oc.sessions.create(...);oc.sessions.resolve(...);oc.sessions.send(...);oc.sessions.messages(...);oc.sessions.fork(...);oc.sessions.compact(...);oc.sessions.abort(...); oc.runs.create(...);oc.runs.get(runId);oc.runs.events(runId, { after });oc.runs.wait(runId);oc.runs.cancel(runId); oc.tasks.list({ status: "running" });oc.tasks.get(taskId);oc.tasks.cancel(taskId, { reason });oc.tasks.events(taskId, { after }); // future API oc.models.list();oc.models.status(); // Gateway models.authStatus oc.tools.list();oc.tools.invoke("tool-name", { sessionKey, idempotencyKey }); oc.artifacts.list({ runId });oc.artifacts.get(artifactId, { runId });oc.artifacts.download(artifactId, { runId }); oc.approvals.list();oc.approvals.respond(approvalId, ...); oc.environments.list();oc.environments.create(...); // future API: current SDK throws unsupportedoc.environments.status(environmentId);oc.environments.delete(environmentId); // future API: current SDK throws unsupported
[/code]

Les wrappers de haut niveau doivent retourner des objets qui rendent les flux courants agréables :

typescriptCopy code
[code]
    const run = await agent.run(inputOrParams);await run.cancel();await run.wait(); for await (const event of run.events()) {  // normalized event stream} const artifacts = await run.artifacts.list();const session = await run.session();
[/code]

## Contrat d’événement

Le SDK public doit exposer des événements versionnés, rejouables et normalisés.

typescriptCopy code
[code]
    type OpenClawEvent = {  version: 1;  id: string;  ts: number;  type: OpenClawEventType;  runId?: string;  sessionId?: string;  sessionKey?: string;  taskId?: string;  agentId?: string;  data: unknown;  raw?: unknown;};
[/code]

`id` est un curseur de relecture. Les consommateurs doivent pouvoir se reconnecter avec `events({ after: id })` et recevoir les événements manqués lorsque la rétention le permet.

Familles d’événements normalisés recommandées :

Événement | Signification  
---|---  
`run.created` | Exécution acceptée.  
`run.queued` | L’exécution attend une voie de session, un runtime ou un environnement.  
`run.started` | Le runtime a démarré l’exécution.  
`run.completed` | L’exécution s’est terminée avec succès.  
`run.failed` | L’exécution s’est terminée avec une erreur.  
`run.cancelled` | L’exécution a été annulée.  
`run.timed_out` | L’exécution a dépassé son délai d’expiration.  
`assistant.delta` | Delta de texte de l’assistant.  
`assistant.message` | Message complet de l’assistant ou remplacement.  
`thinking.delta` | Delta de raisonnement ou de plan, lorsque la politique autorise l’exposition.  
`tool.call.started` | L’appel d’outil a commencé.  
`tool.call.delta` | L’appel d’outil a diffusé une progression ou une sortie partielle.  
`tool.call.completed` | L’appel d’outil a réussi.  
`tool.call.failed` | L’appel d’outil a échoué.  
`approval.requested` | Une exécution ou un outil nécessite une approbation.  
`approval.resolved` | L’approbation a été accordée, refusée, a expiré ou a été annulée.  
`question.requested` | Le runtime demande une saisie à l’utilisateur ou à l’application hôte.  
`question.answered` | L’application hôte a fourni une réponse.  
`artifact.created` | Nouvel artefact disponible.  
`artifact.updated` | Un artefact existant a changé.  
`session.created` | Session créée.  
`session.updated` | Les métadonnées de session ont changé.  
`session.compacted` | La Compaction de session a eu lieu.  
`task.updated` | L’état de la tâche en arrière-plan a changé.  
`git.branch` | Le runtime a observé ou modifié l’état de branche.  
`git.diff` | Le runtime a produit ou modifié un diff.  
`git.pr` | Le runtime a ouvert, mis à jour ou lié une pull request.  
  
Les payloads natifs du runtime doivent être disponibles via `raw`, mais les applications ne doivent pas avoir à analyser `raw` pour l’interface utilisateur normale.

## Contrat de résultat

`Run.wait()` doit retourner une enveloppe de résultat stable :

typescriptCopy code
[code]
    type RunResult = {  runId: string;  status: "accepted" | "completed" | "failed" | "cancelled" | "timed_out";  sessionId?: string;  sessionKey?: string;  taskId?: string;  startedAt?: string | number;  endedAt?: string | number;  output?: {    text?: string;    messages?: SDKMessage[];  };  usage?: {    inputTokens?: number;    outputTokens?: number;    totalTokens?: number;    costUsd?: number;  };  artifacts?: ArtifactSummary[];  error?: SDKError;};
[/code]

Le résultat doit être simple et stable. Les valeurs d’horodatage préservent la forme du Gateway, de sorte que les exécutions actuelles adossées au cycle de vie signalent généralement des nombres en millisecondes depuis l’époque, tandis que les adaptateurs peuvent encore exposer des chaînes ISO. L’interface utilisateur riche, les traces d’outils et les détails natifs du runtime appartiennent aux événements et aux artefacts.

`accepted` est un résultat d’attente non terminal : il signifie que l’échéance d’attente du Gateway a expiré avant que l’exécution ne produise une fin/erreur de cycle de vie. Il ne doit pas être traité comme `timed_out` ; `timed_out` est réservé à une exécution qui a dépassé son propre délai d’expiration du runtime.

## Approbations et questions

Les approbations doivent être des entités de premier ordre, car les agents de codage franchissent constamment des limites de sécurité.

typescriptCopy code
[code]
    run.onApproval(async (request) => {  if (request.kind === "tool" && request.toolName === "exec") {    return request.approveOnce({ reason: "CI command allowed by policy" });  }   return request.askUser();});
[/code]

Les événements d’approbation doivent transporter :

  * l’identifiant d’approbation
  * l’identifiant d’exécution et l’identifiant de session
  * le type de demande
  * le résumé de l’action demandée
  * le nom de l’outil ou l’action d’environnement
  * le niveau de risque
  * les décisions disponibles
  * l’expiration
  * si la décision peut être réutilisée


Les questions sont distinctes des approbations. Une question demande des informations à l’utilisateur ou à l’application hôte. Une approbation demande l’autorisation d’effectuer une action.

## Modèle ToolSpace

Les applications doivent comprendre la surface d’outils sans importer les éléments internes des Plugins.

typescriptCopy code
[code]
    const tools = await run.toolSpace(); for (const tool of tools.list()) {  console.log(tool.name, tool.source, tool.requiresApproval);}
[/code]

Le SDK doit exposer :

  * des métadonnées d’outil normalisées
  * la source : OpenClaw, MCP, Plugin, canal, runtime ou application
  * un résumé du schéma
  * la politique d’approbation
  * la compatibilité runtime
  * si un outil est masqué, en lecture seule, capable d’écrire ou capable côté hôte


L’invocation d’outils via le SDK doit être explicite et limitée au périmètre. La plupart des applications doivent exécuter des agents, et non appeler directement des outils arbitraires.

## Modèle d’artefact

Les artefacts doivent couvrir plus que des fichiers.

typescriptCopy code
[code]
    type ArtifactSummary = {  id: string;  runId?: string;  sessionId?: string;  type:    | "file"    | "patch"    | "diff"    | "log"    | "media"    | "screenshot"    | "trajectory"    | "pull_request"    | "workspace";  title?: string;  mimeType?: string;  sizeBytes?: number;  createdAt: string;  expiresAt?: string;};
[/code]

Exemples courants :

  * modifications de fichiers et fichiers générés
  * lots de patchs
  * diffs VCS
  * captures d’écran et sorties média
  * journaux et lots de traces
  * liens de pull request
  * trajectoires du runtime
  * instantanés d’espaces de travail d’environnement géré


L’accès aux artefacts doit prendre en charge la rédaction, la rétention et les URL de téléchargement sans supposer que chaque artefact est un fichier local normal.

## Modèle de sécurité

Le SDK d’application doit être explicite concernant l’autorité.

Portées de jeton recommandées :

Portée | Autorise  
---|---  
`agent.read` | Lister et inspecter les agents.  
`agent.run` | Démarrer des exécutions.  
`session.read` | Lire les métadonnées et les messages de session.  
`session.write` | Créer, envoyer vers, dupliquer, compacter et interrompre des sessions.  
`task.read` | Lire l’état des tâches en arrière-plan.  
`task.write` | Annuler ou modifier la politique de notification des tâches.  
`approval.respond` | Approuver ou refuser des demandes.  
`tools.invoke` | Invoquer directement les outils exposés.  
`artifacts.read` | Lister et télécharger des artefacts.  
`environment.write` | Créer ou détruire des environnements gérés.  
`admin` | Opérations administratives.  
  
Valeurs par défaut :

  * aucun transfert de secrets par défaut
  * aucun relais illimité de variables d’environnement
  * références de secrets au lieu des valeurs de secrets
  * politique explicite de bac à sable et de réseau
  * rétention explicite des environnements distants
  * approbations pour l’exécution hôte, sauf si la politique prouve le contraire
  * événements bruts du runtime expurgés avant de quitter le Gateway, sauf si l’appelant dispose d’une portée de diagnostic plus forte


## Fournisseur d’environnement géré

Les agents gérés doivent être implémentés comme des fournisseurs d’environnement.

typescriptCopy code
[code]
    type EnvironmentProvider = {  id: string;  capabilities: {    checkout?: boolean;    sandbox?: boolean;    networkPolicy?: boolean;    secrets?: boolean;    artifacts?: boolean;    logs?: boolean;    pullRequests?: boolean;    longRunning?: boolean;  };};
[/code]

La première implémentation n’a pas besoin d’être un SaaS hébergé. Elle peut cibler des hôtes Node existants, des espaces de travail éphémères, des runners de style CI ou des environnements de style Testbox. Le contrat important est :

  1. préparer l’espace de travail
  2. lier un environnement sûr et des secrets
  3. démarrer l’exécution
  4. diffuser les événements
  5. collecter les artefacts
  6. nettoyer ou conserver selon la politique


Une fois cela stable, un service cloud hébergé peut implémenter le même contrat de fournisseur.

## Structure des paquets

Paquets recommandés :

Paquet | Objectif  
---|---  
`@openclaw/sdk` | SDK public de haut niveau et client Gateway généré de bas niveau.  
`@openclaw/sdk-react` | Hooks React optionnels pour tableaux de bord et créateurs d’applications.  
`@openclaw/sdk-testing` | Assistants de test et faux serveur Gateway pour intégrations d’applications.  
  
Le dépôt dispose déjà de `openclaw/plugin-sdk/*` pour les Plugins. Gardez cet espace de noms séparé afin d’éviter de confondre les auteurs de Plugins avec les développeurs d’applications.

## Stratégie de client généré

Le client de bas niveau doit être généré à partir de schémas de protocole Gateway versionnés, puis enveloppé par des classes ergonomiques écrites à la main.

Couches :

  1. Source de vérité du schéma Gateway.
  2. Client TypeScript bas niveau généré.
  3. Validateurs d’exécution pour les entrées externes et les charges utiles d’événements.
  4. Wrappers de haut niveau `OpenClaw`, `Agent`, `Session`, `Run`, `Task` et `Artifact`.
  5. Exemples pratiques et tests d’intégration.


Avantages :

  * la dérive du protocole est visible
  * les tests peuvent comparer les méthodes générées avec les exports Gateway
  * le SDK d’application reste indépendant des détails internes du SDK Plugin
  * les consommateurs bas niveau conservent un accès complet au protocole
  * les consommateurs haut niveau obtiennent la petite API produit


## Connexe

  * [SDK d’application OpenClaw](</fr/concepts/openclaw-sdk>)
  * [Référence RPC Gateway](</fr/reference/rpc>)
  * [Boucle d’agent](</fr/concepts/agent-loop>)
  * [Environnements d’exécution d’agent](</fr/concepts/agent-runtimes>)
  * [Tâches en arrière-plan](</fr/automation/tasks>)
  * [Agents ACP](</fr/tools/acp-agents>)
  * [Présentation du SDK Plugin](</fr/plugins/sdk-overview>)


Was this useful?YesNo