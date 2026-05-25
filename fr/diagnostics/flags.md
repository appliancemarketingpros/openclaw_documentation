---
title: Options de diagnostic
source_url: https://docs.openclaw.ai/fr/diagnostics/flags
scraped_at: 2026-05-25
---

Les indicateurs de diagnostic vous permettent d’activer des journaux de débogage ciblés sans activer la journalisation détaillée partout. Les indicateurs sont opt-in et n’ont aucun effet sauf si un sous-système les vérifie.

## Fonctionnement

  * Les indicateurs sont des chaînes de caractères (insensibles à la casse).
  * Vous pouvez activer des indicateurs dans la configuration ou via un remplacement par variable d’environnement.
  * Les caractères génériques sont pris en charge : 
    * `telegram.*` correspond à `telegram.http`
    * `*` active tous les indicateurs


## Activer via la configuration

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Plusieurs indicateurs :

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Redémarrez le Gateway après avoir modifié les indicateurs.

## Remplacement par variable d’environnement (ponctuel)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Désactiver tous les indicateurs :

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Artefacts de chronologie

L’indicateur `timeline` écrit des événements structurés de démarrage et de synchronisation d’exécution pour les harnais de QA externes :

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Vous pouvez aussi l’activer dans la configuration :

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Le chemin du fichier de chronologie provient toujours de `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Lorsque `timeline` est activé uniquement depuis la configuration, les premiers segments de chargement de la configuration ne sont pas émis, car OpenClaw n’a pas encore lu la configuration ; les segments de démarrage suivants utilisent l’indicateur de configuration.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` et `OPENCLAW_DIAGNOSTICS=*` activent aussi la chronologie, car ils activent tous les indicateurs de diagnostic. Préférez `timeline` lorsque vous voulez uniquement l’artefact de synchronisation JSONL.

Les enregistrements de chronologie utilisent l’enveloppe `openclaw.diagnostics.v1`. Les événements peuvent inclure des identifiants de processus, des noms de phase, des noms de segment, des durées, des identifiants de plugin, des nombres de dépendances, des échantillons de délai de boucle d’événements, des noms d’opérations de fournisseur, l’état de sortie de processus enfants, ainsi que des noms/messages d’erreurs de démarrage. Traitez les fichiers de chronologie comme des artefacts de diagnostic locaux ; examinez-les avant de les partager en dehors de votre machine.

## Emplacement des journaux

Les indicateurs émettent des journaux dans le fichier de journaux de diagnostic standard. Par défaut :

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Si vous définissez `logging.file`, utilisez plutôt ce chemin. Les journaux sont au format JSONL (un objet JSON par ligne). La rédaction s’applique toujours selon `logging.redactSensitive`.

## Extraire les journaux

Choisir le fichier journal le plus récent :

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Filtrer les diagnostics HTTP de Telegram :

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Filtrer les diagnostics HTTP de Brave Search :

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Ou suivre les journaux pendant la reproduction :

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Pour les Gateways distants, vous pouvez aussi utiliser `openclaw logs --follow` (voir [/cli/logs](</fr/cli/logs>)).

## Remarques

  * Si `logging.level` est défini à une valeur supérieure à `warn`, ces journaux peuvent être supprimés. La valeur par défaut `info` convient.
  * `brave.http` journalise les URL/paramètres de requête des demandes Brave Search, l’état/le temps de réponse et les événements de réussite/échec/écriture du cache. Il ne journalise pas les clés d’API ni les corps de réponse, mais les requêtes de recherche peuvent être sensibles.
  * Les indicateurs peuvent rester activés sans risque ; ils n’affectent que le volume de journaux du sous-système spécifique.
  * Utilisez [/logging](</fr/logging>) pour modifier les destinations, les niveaux et la rédaction des journaux.


## Connexe

  * [Diagnostics du Gateway](</fr/gateway/diagnostics>)
  * [Dépannage du Gateway](</fr/gateway/troubleshooting>)


Was this useful?YesNo