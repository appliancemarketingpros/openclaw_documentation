---
title: Fuseaux horaires
source_url: https://docs.openclaw.ai/fr/concepts/timezone
scraped_at: 2026-05-25
---

OpenClaw standardise les horodatages afin que le modèle voie une **seule heure de référence** au lieu d’un mélange d’horloges locales aux fournisseurs. Les fuseaux horaires apparaissent sur trois surfaces, chacune ayant son propre objectif :

## Trois surfaces de fuseaux horaires

Surface | Ce qu’elle affiche | Valeur par défaut | Configuré via  
---|---|---|---  
Enveloppes de messages | Encapsule les messages de canal entrants : `[Signal +1555 2026-01-18 00:19 PST] bonjour` | Locale à l’hôte | `agents.defaults.envelopeTimezone`  
Charges utiles des outils | Les outils de type `readMessages` du canal renvoient l’heure brute du fournisseur + les champs normalisés `timestampMs` / `timestampUtc` | Champs UTC toujours présents | Non configurable — conserve les horodatages natifs du fournisseur  
Invite système | Un petit bloc `Current Date & Time` avec le **fuseau horaire uniquement** (sans valeur d’horloge, pour la stabilité du cache) | Fuseau horaire de l’hôte si `userTimezone` n’est pas défini | `agents.defaults.userTimezone`  
  
L’invite système omet délibérément l’horloge en direct afin de garder la mise en cache des invites stable entre les tours. Lorsque l’agent a besoin de l’heure actuelle, il appelle `session_status`.

## Définir le fuseau horaire de l’utilisateur

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",    },  },}
[/code]

Si `userTimezone` n’est pas défini, OpenClaw résout le fuseau horaire de l’hôte à l’exécution (sans écriture de configuration). `agents.defaults.timeFormat` (`auto` | `12` | `24`) contrôle le rendu 12 h/24 h dans les enveloppes et les surfaces en aval, pas dans la section de l’invite système.

## Quand remplacer la valeur

  * **Utilisez des enveloppes UTC** (`envelopeTimezone: "utc"`) lorsque vous voulez des horodatages stables entre des hôtes situés dans différentes régions, ou lorsque vous voulez que les journaux alignés sur UTC correspondent à la sortie de diagnostic.
  * **Utilisez une zone IANA fixe** (par ex. `"Europe/Vienna"`) lorsque l’hôte du Gateway se trouve dans une zone, mais que l’utilisateur se trouve dans une autre, et que vous voulez que les enveloppes soient lues dans la zone de l’utilisateur indépendamment de la migration de l’hôte.
  * **Définissez`envelopeTimestamp: "off"`** pour des enveloppes consommant peu de jetons lorsque le contexte d’horodatage n’est pas utile à la conversation.


Pour la référence complète du comportement, des exemples par fournisseur et la mise en forme du temps écoulé, consultez [Date et heure](</fr/date-time>).

## Associé

  * [Date et heure](</fr/date-time>) — comportement complet des enveloppes, outils et invites, avec exemples.
  * [Heartbeat](</fr/gateway/heartbeat>) — les heures actives utilisent le fuseau horaire pour la planification.
  * [Tâches Cron](</fr/automation/cron-jobs>) — les expressions cron utilisent le fuseau horaire pour la planification.


Was this useful?YesNo