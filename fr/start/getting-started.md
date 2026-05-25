---
title: Premiers pas
source_url: https://docs.openclaw.ai/fr/start/getting-started
scraped_at: 2026-05-25
---

Installez OpenClaw, exécutez l’onboarding et discutez avec votre assistant IA — le tout en environ 5 minutes. À la fin, vous aurez un Gateway en cours d’exécution, une authentification configurée et une session de chat fonctionnelle.

## Ce dont vous avez besoin

  * **Node.js** — Node 24 recommandé (Node 22.16+ également pris en charge)
  * **Une clé API** d’un fournisseur de modèles (Anthropic, OpenAI, Google, etc.) — l’onboarding vous la demandera


## Configuration rapide

* ### Installer OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Processus du script d’installation](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

L’assistant vous guide dans le choix d’un fournisseur de modèles, la définition d’une clé API et la configuration du Gateway. Cela prend environ 2 minutes.

Consultez [Onboarding (CLI)](</fr/start/wizard>) pour la référence complète.

* ### Vérifier que le Gateway est en cours d’exécution

bashCopy code
[code]
    openclaw gateway status
[/code]

Vous devriez voir le Gateway à l’écoute sur le port 18789.

* ### Ouvrir le tableau de bord

bashCopy code
[code]
    openclaw dashboard
[/code]

Cela ouvre l’interface de contrôle dans votre navigateur. Si elle se charge, tout fonctionne.

* ### Envoyer votre premier message

Saisissez un message dans le chat de l’interface de contrôle et vous devriez recevoir une réponse de l’IA.

Vous voulez plutôt discuter depuis votre téléphone ? Le canal le plus rapide à configurer est [Telegram](</fr/channels/telegram>) (juste un jeton de bot). Consultez [Canaux](</fr/channels>) pour toutes les options.

Avancé : monter une version personnalisée de l’interface de contrôle

Si vous maintenez une version localisée ou personnalisée du tableau de bord, faites pointer `gateway.controlUi.root` vers un répertoire contenant vos ressources statiques générées et `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Définissez ensuite :

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Redémarrez le Gateway et rouvrez le tableau de bord :

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Que faire ensuite

[**Connecter un canal** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, et plus encore. ](</fr/channels>) [**Appairage et sécurité** Contrôlez qui peut envoyer des messages à votre agent. ](</fr/channels/pairing>) [**Configurer le Gateway** Modèles, outils, bac à sable et paramètres avancés. ](</fr/gateway/configuration>) [**Parcourir les outils** Navigateur, exec, recherche web, Skills et plugins. ](</fr/tools>)

Avancé : variables d’environnement

Si vous exécutez OpenClaw avec un compte de service ou si vous voulez des chemins personnalisés :

  * `OPENCLAW_HOME` — répertoire personnel pour la résolution des chemins internes
  * `OPENCLAW_STATE_DIR` — remplace le répertoire d’état
  * `OPENCLAW_CONFIG_PATH` — remplace le chemin du fichier de configuration


Référence complète : [Variables d’environnement](</fr/help/environment>).

## Associés

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Vue d’ensemble des canaux](</fr/channels>)
  * [Configuration](</fr/start/setup>)


Was this useful?YesNo