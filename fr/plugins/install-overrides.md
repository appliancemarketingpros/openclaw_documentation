---
title: Remplacements d’installation de Plugin
source_url: https://docs.openclaw.ai/fr/plugins/install-overrides
scraped_at: 2026-05-25
---

Les remplacements d’installation de plugins permettent aux mainteneurs de tester les installations de plugins au moment de la configuration avec un package npm spécifique ou une archive tar locale produite par npm pack. Ils sont réservés à l’E2E et à la validation de packages. Les utilisateurs normaux doivent installer les plugins avec [`openclaw plugins install`](</fr/cli/plugins>).

## Environnement

Les remplacements sont désactivés sauf si les deux variables sont définies :

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

La carte de remplacement est du JSON indexé par identifiant de plugin. Les valeurs prennent en charge :

  * `npm:<registry-spec>` pour les packages de registre et les versions exactes ou les balises
  * `npm-pack:<path.tgz>` pour les archives tar locales produites par `npm pack`


Les chemins relatifs `npm-pack:` sont résolus depuis le répertoire de travail actuel.

## Comportement

Lorsqu’un flux de configuration demande l’installation d’un plugin dont l’identifiant apparaît dans la carte, OpenClaw utilise la source de remplacement au lieu de la source npm du catalogue, groupée ou par défaut. Cela s’applique à l’onboarding et aux autres flux qui utilisent l’installateur de plugins partagé au moment de la configuration.

Les remplacements continuent d’imposer l’identifiant de plugin attendu. Une archive tar mappée à `codex` doit installer un plugin dont l’identifiant de manifeste est `codex`.

Les remplacements n’héritent pas du statut officiel de source fiable. Même lorsque l’entrée de catalogue représente normalement un package appartenant à OpenClaw, un remplacement est traité comme une entrée de test fournie par l’opérateur.

Les fichiers `.env` de l’espace de travail ne peuvent pas activer les remplacements d’installation. Définissez ces variables dans le shell fiable, la tâche CI ou la commande de test distante qui lance OpenClaw.

## E2E de package

Utilisez un répertoire d’état isolé afin que les installations de packages et les enregistrements d’installation ne touchent pas votre état OpenClaw normal :

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Vérifiez le package installé sous le répertoire d’état :

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Pour l’E2E avec fournisseur en direct, sourcez la vraie clé API depuis un shell fiable ou un secret CI avant de lancer la commande de test. N’affichez pas les clés ; indiquez uniquement la source et si la clé était présente.

Was this useful?YesNo