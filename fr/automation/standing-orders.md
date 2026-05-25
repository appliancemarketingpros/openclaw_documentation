---
title: Consignes permanentes
source_url: https://docs.openclaw.ai/fr/automation/standing-orders
scraped_at: 2026-05-25
---

Les ordres permanents accordent à votre agent une **autorité opérationnelle permanente** pour des programmes définis. Au lieu de donner des instructions de tâche individuelles à chaque fois, vous définissez des programmes avec un périmètre, des déclencheurs et des règles d’escalade clairs - et l’agent s’exécute de manière autonome dans ces limites.

C’est la différence entre dire à votre assistant « envoie le rapport hebdomadaire » chaque vendredi et accorder une autorité permanente : « Tu es responsable du rapport hebdomadaire. Compile-le chaque vendredi, envoie-le, et n’escalade que si quelque chose semble anormal. »

## Pourquoi les ordres permanents

**Sans ordres permanents :**

  * Vous devez solliciter l’agent pour chaque tâche
  * L’agent reste inactif entre les demandes
  * Le travail routinier est oublié ou retardé
  * Vous devenez le goulot d’étranglement


**Avec des ordres permanents :**

  * L’agent s’exécute de manière autonome dans des limites définies
  * Le travail routinier se fait à l’heure prévue sans sollicitation
  * Vous n’intervenez que pour les exceptions et les validations
  * L’agent utilise les temps morts de façon productive


## Fonctionnement

Les ordres permanents sont définis dans les fichiers de votre [espace de travail de l’agent](</fr/concepts/agent-workspace>). L’approche recommandée consiste à les inclure directement dans `AGENTS.md` (qui est automatiquement injecté à chaque session) afin que l’agent les ait toujours en contexte. Pour les configurations plus importantes, vous pouvez aussi les placer dans un fichier dédié comme `standing-orders.md` et y faire référence depuis `AGENTS.md`.

Chaque programme précise :

  1. **Périmètre** \- ce que l’agent est autorisé à faire
  2. **Déclencheurs** \- quand l’exécuter (calendrier, événement ou condition)
  3. **Points de validation** \- ce qui nécessite une approbation humaine avant d’agir
  4. **Règles d’escalade** \- quand s’arrêter et demander de l’aide


L’agent charge ces instructions à chaque session via les fichiers d’amorçage de l’espace de travail (voir [Espace de travail de l’agent](</fr/concepts/agent-workspace>) pour la liste complète des fichiers automatiquement injectés) et les exécute, en combinaison avec des [tâches Cron](</fr/automation/cron-jobs>) pour l’application basée sur le temps.

## Anatomie d’un ordre permanent

markdownCopy code
[code]
    ## Program: Weekly Status Report **Authority:** Compile data, generate report, deliver to stakeholders**Trigger:** Every Friday at 4 PM (enforced via cron job)**Approval gate:** None for standard reports. Flag anomalies for human review.**Escalation:** If data source is unavailable or metrics look unusual (>2σ from norm) ### Execution steps 1. Pull metrics from configured sources2. Compare to prior week and targets3. Generate report in Reports/weekly/YYYY-MM-DD.md4. Deliver summary via configured channel5. Log completion to Agent/Logs/ ### What NOT to do - Do not send reports to external parties- Do not modify source data- Do not skip delivery if metrics look bad - report accurately
[/code]

## Ordres permanents plus tâches Cron

Les ordres permanents définissent **ce que** l’agent est autorisé à faire. Les [tâches Cron](</fr/automation/cron-jobs>) définissent **quand** cela se produit. Ils fonctionnent ensemble :

CodeCopy code
[code]
    Standing Order: "You own the daily inbox triage"    ↓Cron Job (8 AM daily): "Execute inbox triage per standing orders"    ↓Agent: Reads standing orders → executes steps → reports results
[/code]

L’invite de la tâche Cron doit faire référence à l’ordre permanent au lieu de le dupliquer :

bashCopy code
[code]
    openclaw cron add \  --name daily-inbox-triage \  --cron "0 8 * * 1-5" \  --tz America/New_York \  --timeout-seconds 300 \  --announce \  --channel imessage \  --to "+1XXXXXXXXXX" \  --message "Execute daily inbox triage per standing orders. Check mail for new alerts. Parse, categorize, and persist each item. Report summary to owner. Escalate unknowns."
[/code]

## Exemples

### Exemple 1 : contenu et réseaux sociaux (cycle hebdomadaire)

markdownCopy code
[code]
    ## Program: Content & Social Media **Authority:** Draft content, schedule posts, compile engagement reports**Approval gate:** All posts require owner review for first 30 days, then standing approval**Trigger:** Weekly cycle (Monday review → mid-week drafts → Friday brief) ### Weekly cycle - **Monday:** Review platform metrics and audience engagement- **Tuesday-Thursday:** Draft social posts, create blog content- **Friday:** Compile weekly marketing brief → deliver to owner ### Content rules - Voice must match the brand (see SOUL.md or brand voice guide)- Never identify as AI in public-facing content- Include metrics when available- Focus on value to audience, not self-promotion
[/code]

### Exemple 2 : opérations financières (déclenchées par événement)

markdownCopy code
[code]
    ## Program: Financial Processing **Authority:** Process transaction data, generate reports, send summaries**Approval gate:** None for analysis. Recommendations require owner approval.**Trigger:** New data file detected OR scheduled monthly cycle ### When new data arrives 1. Detect new file in designated input directory2. Parse and categorize all transactions3. Compare against budget targets4. Flag: unusual items, threshold breaches, new recurring charges5. Generate report in designated output directory6. Deliver summary to owner via configured channel ### Escalation rules - Single item > $500: immediate alert- Category > budget by 20%: flag in report- Unrecognizable transaction: ask owner for categorization- Failed processing after 2 retries: report failure, do not guess
[/code]

### Exemple 3 : surveillance et alertes (continu)

markdownCopy code
[code]
    ## Program: System Monitoring **Authority:** Check system health, restart services, send alerts**Approval gate:** Restart services automatically. Escalate if restart fails twice.**Trigger:** Every heartbeat cycle ### Checks - Service health endpoints responding- Disk space above threshold- Pending tasks not stale (>24 hours)- Delivery channels operational ### Response matrix | Condition        | Action                   | Escalate?                || ---------------- | ------------------------ | ------------------------ || Service down     | Restart automatically    | Only if restart fails 2x || Disk space < 10% | Alert owner              | Yes                      || Stale task > 24h | Remind owner             | No                       || Channel offline  | Log and retry next cycle | If offline > 2 hours     |
[/code]

## Modèle exécuter-vérifier-rendre compte

Les ordres permanents fonctionnent mieux lorsqu’ils sont associés à une discipline d’exécution stricte. Chaque tâche d’un ordre permanent doit suivre cette boucle :

  1. **Exécuter** \- Faire le travail réel (ne pas se contenter d’accuser réception de l’instruction)
  2. **Vérifier** \- Confirmer que le résultat est correct (fichier existant, message livré, données analysées)
  3. **Rendre compte** \- Dire au propriétaire ce qui a été fait et ce qui a été vérifié

markdownCopy code
[code]
    ### Execution rules - Every task follows Execute-Verify-Report. No exceptions.- "I'll do that" is not execution. Do it, then report.- "Done" without verification is not acceptable. Prove it.- If execution fails: retry once with adjusted approach.- If still fails: report failure with diagnosis. Never silently fail.- Never retry indefinitely - 3 attempts max, then escalate.
[/code]

Ce modèle évite le mode d’échec le plus courant des agents : accuser réception d’une tâche sans l’accomplir.

## Architecture multiprogramme

Pour les agents qui gèrent plusieurs domaines, organisez les ordres permanents sous forme de programmes séparés avec des limites claires :

markdownCopy code
[code]
    ## Program 1: [Domain A] (Weekly) ... ## Program 2: [Domain B] (Monthly + On-Demand) ... ## Program 3: [Domain C] (As-Needed) ... ## Escalation Rules (All Programs) - [Common escalation criteria]- [Approval gates that apply across programs]
[/code]

Chaque programme doit avoir :

  * Sa propre **cadence de déclenchement** (hebdomadaire, mensuelle, événementielle, continue)
  * Ses propres **points de validation** (certains programmes nécessitent plus de supervision que d’autres)
  * Des **limites** claires (l’agent doit savoir où un programme se termine et où un autre commence)


## Bonnes pratiques

### À faire

  * Commencer avec une autorité limitée et l’élargir à mesure que la confiance se construit
  * Définir des points de validation explicites pour les actions à haut risque
  * Inclure des sections « Ce qu’il ne faut PAS faire » - les limites comptent autant que les autorisations
  * Combiner avec des tâches Cron pour une exécution fiable basée sur le temps
  * Examiner les journaux de l’agent chaque semaine pour vérifier que les ordres permanents sont respectés
  * Mettre à jour les ordres permanents à mesure que vos besoins évoluent - ce sont des documents vivants


### À éviter

  * Accorder une autorité large dès le premier jour (« fais ce que tu penses être le mieux »)
  * Omettre les règles d’escalade - chaque programme a besoin d’une clause « quand s’arrêter et demander »
  * Supposer que l’agent se souviendra des instructions verbales - mettez tout dans le fichier
  * Mélanger les sujets dans un seul programme - programmes séparés pour domaines séparés
  * Oublier l’application par des tâches Cron - les ordres permanents sans déclencheurs deviennent des suggestions


## Connexe

  * [Automatisation](</fr/automation>) : tous les mécanismes d’automatisation en un coup d’œil.
  * [Tâches Cron](</fr/automation/cron-jobs>) : application du calendrier pour les ordres permanents.
  * [Hooks](</fr/automation/hooks>) : scripts événementiels pour les événements du cycle de vie de l’agent.
  * [Webhooks](</fr/automation/cron-jobs#webhooks>) : déclencheurs d’événements HTTP entrants.
  * [Espace de travail de l’agent](</fr/concepts/agent-workspace>) : où résident les ordres permanents, y compris la liste complète des fichiers d’amorçage automatiquement injectés (`AGENTS.md`, `SOUL.md`, etc.).


Was this useful?YesNo