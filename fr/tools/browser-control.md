---
title: API de contrôle du navigateur
source_url: https://docs.openclaw.ai/fr/tools/browser-control
scraped_at: 2026-05-25
---

Pour l’installation, la configuration et le dépannage, consultez [Browser](</fr/tools/browser>). Cette page est la référence pour l’API HTTP de contrôle local, la CLI `openclaw browser` et les modèles de scripts (instantanés, refs, attentes, flux de débogage).

## API de contrôle (facultative)

Pour les intégrations locales uniquement, le Gateway expose une petite API HTTP loopback :

  * État/démarrage/arrêt : `GET /`, `POST /start`, `POST /stop`
  * Onglets : `GET /tabs`, `POST /tabs/open`, `POST /tabs/focus`, `DELETE /tabs/:targetId`
  * Instantané/capture d’écran : `GET /snapshot`, `POST /screenshot`
  * Actions : `POST /navigate`, `POST /act`
  * Hooks : `POST /hooks/file-chooser`, `POST /hooks/dialog`
  * Téléchargements : `POST /download`, `POST /wait/download`
  * Autorisations : `POST /permissions/grant`
  * Débogage : `GET /console`, `POST /pdf`
  * Débogage : `GET /errors`, `GET /requests`, `POST /trace/start`, `POST /trace/stop`, `POST /highlight`
  * Réseau : `POST /response/body`
  * État : `GET /cookies`, `POST /cookies/set`, `POST /cookies/clear`
  * État : `GET /storage/:kind`, `POST /storage/:kind/set`, `POST /storage/:kind/clear`
  * Paramètres : `POST /set/offline`, `POST /set/headers`, `POST /set/credentials`, `POST /set/geolocation`, `POST /set/media`, `POST /set/timezone`, `POST /set/locale`, `POST /set/device`


Tous les points de terminaison acceptent `?profile=<name>`. `POST /start?headless=true` demande un lancement headless local ponctuel pour les profils gérés localement sans modifier la configuration persistante du navigateur ; les profils attach-only, CDP distants et existing-session refusent cette surcharge, car OpenClaw ne lance pas ces processus de navigateur.

Si l’authentification du Gateway par secret partagé est configurée, les routes HTTP du navigateur exigent aussi une authentification :

  * `Authorization: Bearer <gateway token>`
  * `x-openclaw-password: <gateway password>` ou l’authentification HTTP Basic avec ce mot de passe


Notes :

  * Cette API de navigateur loopback autonome ne consomme **pas** les en-têtes d’identité trusted-proxy ou Tailscale Serve.
  * Si `gateway.auth.mode` vaut `none` ou `trusted-proxy`, ces routes de navigateur loopback n’héritent pas de ces modes porteurs d’identité ; gardez-les réservées au loopback.


### Contrat d’erreur de `/act`

`POST /act` utilise une réponse d’erreur structurée pour la validation au niveau de la route et les échecs de politique :

jsonCopy code
[code]
    { "error": "<message>", "code": "ACT_*" }
[/code]

Valeurs actuelles de `code` :

  * `ACT_KIND_REQUIRED` (HTTP 400) : `kind` est manquant ou non reconnu.
  * `ACT_INVALID_REQUEST` (HTTP 400) : la charge utile de l’action a échoué à la normalisation ou à la validation.
  * `ACT_SELECTOR_UNSUPPORTED` (HTTP 400) : `selector` a été utilisé avec un type d’action non pris en charge.
  * `ACT_EVALUATE_DISABLED` (HTTP 403) : `evaluate` (ou `wait --fn`) est désactivé par la configuration.
  * `ACT_TARGET_ID_MISMATCH` (HTTP 403) : le `targetId` de premier niveau ou groupé entre en conflit avec la cible de la requête.
  * `ACT_EXISTING_SESSION_UNSUPPORTED` (HTTP 501) : l’action n’est pas prise en charge pour les profils existing-session.


D’autres échecs d’exécution peuvent encore renvoyer `{ "error": "<message>" }` sans champ `code`.

### Exigence Playwright

Certaines fonctionnalités (navigate/act/instantané IA/instantané de rôle, captures d’écran d’éléments, PDF) nécessitent Playwright. Si Playwright n’est pas installé, ces points de terminaison renvoient une erreur 501 claire.

Ce qui fonctionne encore sans Playwright :

  * Instantanés ARIA
  * Instantanés d’accessibilité de style rôle (`--interactive`, `--compact`, `--depth`, `--efficient`) lorsqu’un WebSocket CDP par onglet est disponible. Il s’agit d’un repli pour l’inspection et la découverte de refs ; Playwright reste le moteur d’action principal.
  * Captures d’écran de page pour le navigateur `openclaw` géré lorsqu’un WebSocket CDP par onglet est disponible
  * Captures d’écran de page pour les profils `existing-session` / Chrome MCP
  * Captures d’écran basées sur des refs `existing-session` (`--ref`) depuis la sortie d’instantané


Ce qui nécessite encore Playwright :

  * `navigate`
  * `act`
  * Les instantanés IA qui dépendent du format d’instantané IA natif de Playwright
  * Les captures d’écran d’éléments par sélecteur CSS (`--element`)
  * l’export PDF complet du navigateur


Les captures d’écran d’éléments refusent aussi `--full-page` ; la route renvoie `fullPage is not supported for element screenshots`.

Si vous voyez `Playwright is not available in this gateway build`, il manque au Gateway empaqueté la dépendance d’exécution principale du navigateur. Réinstallez ou mettez à jour OpenClaw, puis redémarrez le gateway. Pour Docker, installez aussi les binaires du navigateur Chromium comme indiqué ci-dessous.

#### Installation Docker de Playwright

Si votre Gateway s’exécute dans Docker, évitez `npx playwright` (conflits de surcharge npm). Pour les images personnalisées, intégrez Chromium à l’image :

bashCopy code
[code]
    OPENCLAW_INSTALL_BROWSER=1 ./scripts/docker/setup.sh
[/code]

Pour une image existante, installez-le plutôt via la CLI fournie :

bashCopy code
[code]
    docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

Pour persister les téléchargements de navigateurs, définissez `PLAYWRIGHT_BROWSERS_PATH` (par exemple, `/home/node/.cache/ms-playwright`) et assurez-vous que `/home/node` est persisté via `OPENCLAW_HOME_VOLUME` ou un montage bind. OpenClaw détecte automatiquement le Chromium persisté sous Linux. Consultez [Docker](</fr/install/docker>).

## Fonctionnement (interne)

Un petit serveur de contrôle loopback accepte les requêtes HTTP et se connecte aux navigateurs basés sur Chromium via CDP. Les actions avancées (click/type/snapshot/PDF) passent par Playwright au-dessus de CDP ; lorsque Playwright est absent, seules les opérations qui ne dépendent pas de Playwright sont disponibles. L’agent voit une interface stable unique tandis que les navigateurs et profils locaux/distants peuvent être remplacés librement en dessous.

## Référence rapide de la CLI

Toutes les commandes acceptent `--browser-profile <name>` pour cibler un profil spécifique, et `--json` pour une sortie lisible par machine.

Basics: status, tabs, open/focus/close bashCopy code
[code]
    openclaw browser statusopenclaw browser startopenclaw browser start --headless # one-shot local managed headless launchopenclaw browser stop            # also clears emulation on attach-only/remote CDPopenclaw browser tabsopenclaw browser tab             # shortcut for current tabopenclaw browser tab newopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://example.comopenclaw browser focus abcd1234openclaw browser close abcd1234
[/code]

Inspection: screenshot, snapshot, console, errors, requests bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref 12        # or --ref e12openclaw browser screenshot --labelsopenclaw browser snapshotopenclaw browser snapshot --format aria --limit 200openclaw browser snapshot --interactive --compact --depth 6openclaw browser snapshot --efficientopenclaw browser snapshot --labelsopenclaw browser snapshot --urlsopenclaw browser snapshot --selector "#main" --interactiveopenclaw browser snapshot --frame "iframe#main" --interactiveopenclaw browser console --level erroropenclaw browser errors --clearopenclaw browser requests --filter api --clearopenclaw browser pdfopenclaw browser responsebody "**/api" --max-chars 5000
[/code]

Actions: navigate, click, type, drag, wait, evaluate bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser resize 1280 720openclaw browser click 12 --double           # or e12 for role refsopenclaw browser click-coords 120 340        # viewport coordinatesopenclaw browser type 23 "hello" --submitopenclaw browser press Enteropenclaw browser hover 44openclaw browser scrollintoview e12openclaw browser drag 10 11openclaw browser select 9 OptionA OptionBopenclaw browser download e12 report.pdfopenclaw browser waitfordownload report.pdfopenclaw browser upload /tmp/openclaw/uploads/file.pdfopenclaw browser fill --fields '[{"ref":"1","type":"text","value":"Ada"}]'openclaw browser dialog --acceptopenclaw browser wait --text "Done"openclaw browser wait "#main" --url "**/dash" --load networkidle --fn "window.ready===true"openclaw browser evaluate --fn '(el) => el.textContent' --ref 7openclaw browser highlight e12openclaw browser trace startopenclaw browser trace stop
[/code]

State: cookies, storage, offline, headers, geo, device bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url "https://example.com"openclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set theme darkopenclaw browser storage session clearopenclaw browser set offline onopenclaw browser set headers --headers-json '{"X-Debug":"1"}'openclaw browser set credentials user pass            # --clear to removeopenclaw browser set geo 37.7749 -122.4194 --origin "https://example.com"openclaw browser set media darkopenclaw browser set timezone America/New_Yorkopenclaw browser set locale en-USopenclaw browser set device "iPhone 14"
[/code]

Notes :

  * `upload` et `dialog` sont des appels d’**armement** ; exécutez-les avant le clic/la pression qui déclenche le sélecteur/la boîte de dialogue.
  * `click`/`type`/etc nécessitent une `ref` provenant de `snapshot` (`12` numérique, ref de rôle `e12` ou ref ARIA actionnable `ax12`). Les sélecteurs CSS ne sont volontairement pas pris en charge pour les actions. Utilisez `click-coords` lorsque la position visible dans la fenêtre d’affichage est la seule cible fiable.
  * Les chemins de téléchargement, trace et upload sont limités aux racines temporaires OpenClaw : `/tmp/openclaw{,/downloads,/uploads}` (repli : `${os.tmpdir()}/openclaw/...`).
  * `upload` peut aussi définir directement les entrées de fichier via `--input-ref` ou `--element`.


Les identifiants et libellés d’onglets stables survivent au remplacement de cible brute Chromium lorsque OpenClaw peut prouver l’onglet de remplacement, par exemple avec la même URL ou lorsqu’un seul ancien onglet devient un seul nouvel onglet après l’envoi d’un formulaire. Les identifiants de cible bruts restent volatils ; préférez `suggestedTargetId` depuis `tabs` dans les scripts.

Aperçu des indicateurs d’instantané :

  * `--format ai` (par défaut avec Playwright) : instantané IA avec refs numériques (`aria-ref="<n>"`).
  * `--format aria` : arbre d’accessibilité avec refs `axN`. Lorsque Playwright est disponible, OpenClaw lie les refs avec des identifiants DOM backend à la page en direct afin que les actions suivantes puissent les utiliser ; sinon, considérez la sortie comme réservée à l’inspection.
  * `--efficient` (ou `--mode efficient`) : préréglage compact d’instantané de rôle. Définissez `browser.snapshotDefaults.mode: "efficient"` pour en faire la valeur par défaut (voir [configuration du Gateway](</fr/gateway/configuration-reference#browser>)).
  * `--interactive`, `--compact`, `--depth`, `--selector` forcent un instantané de rôle avec des refs `ref=e12`. `--frame "<iframe>"` limite les instantanés de rôle à une iframe.
  * `--labels` ajoute une capture d’écran limitée à la fenêtre d’affichage avec des libellés de refs superposés (affiche `MEDIA:<path>`).
  * `--urls` ajoute les destinations de liens découvertes aux instantanés IA.


## Instantanés et refs

OpenClaw prend en charge deux styles d’« instantané » :

  * **Instantané IA (refs numériques)** : `openclaw browser snapshot` (par défaut ; `--format ai`)

    * Sortie : un instantané texte qui inclut des refs numériques.
    * Actions : `openclaw browser click 12`, `openclaw browser type 23 "hello"`.
    * En interne, la ref est résolue via `aria-ref` de Playwright.
  * **Instantané de rôle (refs de rôle comme`e12`)** : `openclaw browser snapshot --interactive` (ou `--compact`, `--depth`, `--selector`, `--frame`)

    * Sortie : une liste/arborescence basée sur les rôles avec `[ref=e12]` (et `[nth=1]` facultatif).
    * Actions : `openclaw browser click e12`, `openclaw browser highlight e12`.
    * En interne, la ref est résolue via `getByRole(...)` (plus `nth()` pour les doublons).
    * Ajoutez `--labels` pour inclure une capture d’écran de la fenêtre d’affichage avec des libellés `e12` superposés.
    * Ajoutez `--urls` lorsque le texte du lien est ambigu et que l’agent a besoin de cibles de navigation concrètes.
  * **Instantané ARIA (réfs ARIA comme`ax12`)** : `openclaw browser snapshot --format aria`

    * Sortie : l’arbre d’accessibilité sous forme de nœuds structurés.
    * Actions : `openclaw browser click ax12` fonctionne lorsque le chemin de l’instantané peut lier la réf via les ids DOM du backend Playwright et Chrome.
  * Si Playwright n’est pas disponible, les instantanés ARIA peuvent tout de même être utiles pour l’inspection, mais les réfs peuvent ne pas être utilisables pour des actions. Reprenez un instantané avec `--format ai` ou `--interactive` lorsque vous avez besoin de réfs d’action.

  * Preuve Docker pour le chemin de repli raw-CDP : `pnpm test:docker:browser-cdp-snapshot` démarre Chromium avec CDP, exécute `browser doctor --deep`, et vérifie que les instantanés de rôles incluent les URL de liens, les éléments cliquables promus par le curseur, et les métadonnées d’iframe.


Comportement des réfs :

  * Les réfs ne sont **pas stables entre les navigations** ; si quelque chose échoue, relancez `snapshot` et utilisez une réf fraîche.
  * `/act` renvoie le `targetId` brut actuel après un remplacement déclenché par une action lorsqu’il peut prouver l’onglet de remplacement. Continuez à utiliser des ids/étiquettes d’onglet stables pour les commandes de suivi.
  * Si l’instantané de rôles a été pris avec `--frame`, les réfs de rôles sont limitées à cet iframe jusqu’au prochain instantané de rôles.
  * Les réfs `axN` inconnues ou obsolètes échouent rapidement au lieu de retomber sur le sélecteur `aria-ref` de Playwright. Exécutez un nouvel instantané sur le même onglet lorsque cela se produit.


## Capacités d’attente avancées

Vous pouvez attendre plus que simplement du temps/texte :

  * Attendre une URL (globs pris en charge par Playwright) : 
    * `openclaw browser wait --url "**/dash"`
  * Attendre l’état de chargement : 
    * `openclaw browser wait --load networkidle`
  * Attendre un prédicat JS : 
    * `openclaw browser wait --fn "window.ready===true"`
  * Attendre qu’un sélecteur devienne visible : 
    * `openclaw browser wait "#main"`


Ces options peuvent être combinées :

bashCopy code
[code]
    openclaw browser wait "#main" \  --url "**/dash" \  --load networkidle \  --fn "window.ready===true" \  --timeout-ms 15000
[/code]

## Flux de débogage

Lorsqu’une action échoue (par exemple « non visible », « violation du mode strict », « recouvert ») :

  1. `openclaw browser snapshot --interactive`
  2. Utilisez `click <ref>` / `type <ref>` (privilégiez les réfs de rôles en mode interactif)
  3. Si l’échec persiste : `openclaw browser highlight <ref>` pour voir ce que Playwright cible
  4. Si la page se comporte étrangement : 
     * `openclaw browser errors --clear`
     * `openclaw browser requests --filter api --clear`
  5. Pour un débogage approfondi : enregistrez une trace : 
     * `openclaw browser trace start`
     * reproduisez le problème
     * `openclaw browser trace stop` (affiche `TRACE:<path>`)


## Sortie JSON

`--json` est destiné aux scripts et aux outils structurés.

Exemples :

bashCopy code
[code]
    openclaw browser status --jsonopenclaw browser snapshot --interactive --jsonopenclaw browser requests --filter api --jsonopenclaw browser cookies --json
[/code]

Les instantanés de rôles en JSON incluent `refs` ainsi qu’un petit bloc `stats` (lines/chars/refs/interactive) afin que les outils puissent raisonner sur la taille et la densité de la charge utile.

## Options d’état et d’environnement

Elles sont utiles pour les flux « faire en sorte que le site se comporte comme X » :

  * Cookies : `cookies`, `cookies set`, `cookies clear`
  * Stockage : `storage local|session get|set|clear`
  * Hors ligne : `set offline on|off`
  * En-têtes : `set headers --headers-json '{"X-Debug":"1"}'` (l’ancien `set headers --json '{"X-Debug":"1"}'` reste pris en charge)
  * Authentification HTTP basic : `set credentials user pass` (ou `--clear`)
  * Géolocalisation : `set geo <lat> <lon> --origin "https://example.com"` (ou `--clear`)
  * Média : `set media dark|light|no-preference|none`
  * Fuseau horaire / locale : `set timezone ...`, `set locale ...`
  * Appareil / zone d’affichage : 
    * `set device "iPhone 14"` (préréglages d’appareils Playwright)
    * `set viewport 1280 720`


## Sécurité et confidentialité

  * Le profil de navigateur openclaw peut contenir des sessions connectées ; traitez-le comme sensible.
  * `browser act kind=evaluate` / `openclaw browser evaluate` et `wait --fn` exécutent du JavaScript arbitraire dans le contexte de la page. L’injection de prompt peut orienter cela. Désactivez-le avec `browser.evaluateEnabled=false` si vous n’en avez pas besoin.
  * Pour les connexions et les notes anti-bot (X/Twitter, etc.), consultez [Connexion navigateur + publication X/Twitter](</fr/tools/browser-login>).
  * Gardez l’hôte Gateway/Node privé (loopback ou tailnet-only).
  * Les points de terminaison CDP distants sont puissants ; tunnelisez-les et protégez-les.


Exemple de mode strict (bloquer les destinations privées/internes par défaut) :

json5Copy code
[code]
    {  browser: {    ssrfPolicy: {      dangerouslyAllowPrivateNetwork: false,      hostnameAllowlist: ["*.example.com", "example.com"],      allowedHostnames: ["localhost"], // optional exact allow    },  },}
[/code]

## Connexe

  * [Navigateur](</fr/tools/browser>) \- vue d’ensemble, configuration, profils, sécurité
  * [Connexion navigateur](</fr/tools/browser-login>) \- connexion à des sites
  * [Dépannage navigateur Linux](</fr/tools/browser-linux-troubleshooting>)
  * [Dépannage navigateur WSL2](</fr/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo