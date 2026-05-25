---
title: OpenClaw
source_url: https://docs.openclaw.ai/fr
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"EXFOLIEZ ! EXFOLIEZ !"_ — Un homard de l’espace, probablement

**Gateway pour n’importe quel OS destiné aux agents IA sur Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, et plus encore.**

Envoyez un message, recevez une réponse d’agent depuis votre poche. Exécutez un Gateway unique avec les canaux intégrés, les plugins de canaux groupés, WebChat et les nœuds mobiles.

[**Premiers pas** Installez OpenClaw et lancez le Gateway en quelques minutes. ](</fr/start/getting-started>) [**Exécuter l’intégration** Configuration guidée avec `openclaw onboard` et des flux d’appairage. ](</fr/start/wizard>) [**Ouvrir l’interface de contrôle** Lancez le tableau de bord du navigateur pour la discussion, la configuration et les sessions. ](</fr/web/control-ui>)

## Qu’est-ce qu’OpenClaw ?

OpenClaw est un **gateway auto-hébergé** qui connecte vos applications de discussion et surfaces de canaux favorites — canaux intégrés, ainsi que plugins de canaux groupés ou externes comme Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, et plus encore — à des agents de codage IA comme Pi. Vous exécutez un seul processus Gateway sur votre propre machine (ou un serveur), et il devient le pont entre vos applications de messagerie et un assistant IA toujours disponible.

**À qui s’adresse-t-il ?** Aux développeurs et utilisateurs avancés qui veulent un assistant IA personnel auquel ils peuvent envoyer des messages depuis n’importe où — sans abandonner le contrôle de leurs données ni dépendre d’un service hébergé.

**Qu’est-ce qui le rend différent ?**

  * **Auto-hébergé** : fonctionne sur votre matériel, selon vos règles
  * **Multicanal** : un Gateway dessert simultanément les canaux intégrés et les plugins de canaux groupés ou externes
  * **Natif pour les agents** : conçu pour les agents de codage avec utilisation d’outils, sessions, mémoire et routage multi-agents
  * **Open source** : sous licence MIT, porté par la communauté


**De quoi avez-vous besoin ?** Node 24 (recommandé), ou Node 22 LTS (`22.16+`) pour la compatibilité, une clé API du fournisseur choisi et 5 minutes. Pour une qualité et une sécurité optimales, utilisez le modèle de dernière génération le plus puissant disponible.

## Fonctionnement
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Le Gateway est la source unique de vérité pour les sessions, le routage et les connexions de canaux.

## Capacités clés

[**Gateway multicanal** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, et plus encore avec un seul processus Gateway. ](</fr/channels>) [**Canaux de Plugin** Les plugins groupés ajoutent Matrix, Nostr, Twitch, Zalo, et plus encore dans les versions courantes normales. ](</fr/tools/plugin>) [**Routage multi-agents** Sessions isolées par agent, espace de travail ou expéditeur. ](</fr/concepts/multi-agent>) [**Prise en charge des médias** Envoyez et recevez des images, de l’audio et des documents. ](</fr/nodes/images>) [**Interface de contrôle Web** Tableau de bord navigateur pour la discussion, la configuration, les sessions et les nœuds. ](</fr/web/control-ui>) [**Nœuds mobiles** Appairez des nœuds iOS et Android pour Canvas, la caméra et les flux de travail avec voix activée. ](</fr/nodes>)

## Démarrage rapide

* ### Installer OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Intégrer et installer le service

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Discuter

Ouvrez l’interface de contrôle dans votre navigateur et envoyez un message :

bashCopy code
[code]
    openclaw dashboard
[/code]

Ou connectez un canal ([Telegram](</fr/channels/telegram>) est le plus rapide) et discutez depuis votre téléphone.

Besoin de l’installation complète et de la configuration de développement ? Consultez [Premiers pas](</fr/start/getting-started>).

## Tableau de bord

Ouvrez l’interface de contrôle du navigateur après le démarrage du Gateway.

  * Valeur locale par défaut : <http://127.0.0.1:18789/>
  * Accès à distance : [Surfaces Web](</fr/web>) et [Tailscale](</fr/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Configuration (facultatif)

La configuration se trouve dans `~/.openclaw/openclaw.json`.

  * Si vous **ne faites rien** , OpenClaw utilise le binaire Pi groupé en mode RPC avec des sessions par expéditeur.
  * Si vous voulez le verrouiller, commencez par `channels.whatsapp.allowFrom` et (pour les groupes) les règles de mention.


Exemple :

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Commencez ici

[**Hubs de documentation** Toute la documentation et tous les guides, organisés par cas d’utilisation. ](</fr/start/hubs>) [**Configuration** Paramètres principaux du Gateway, jetons et configuration des fournisseurs. ](</fr/gateway/configuration>) [**Accès à distance** Modèles d’accès SSH et tailnet. ](</fr/gateway/remote>) [**Canaux** Configuration propre à chaque canal pour Feishu, Microsoft Teams, WhatsApp, Telegram, Discord, et plus encore. ](</fr/channels/telegram>) [**Nœuds** Nœuds iOS et Android avec appairage, Canvas, caméra et actions d’appareil. ](</fr/nodes>) [**Aide** Point d’entrée pour les correctifs courants et le dépannage. ](</fr/help>)

## En savoir plus

[**Liste complète des fonctionnalités** Capacités complètes de canaux, de routage et de médias. ](</fr/concepts/features>) [**Routage multi-agents** Isolation des espaces de travail et sessions par agent. ](</fr/concepts/multi-agent>) [**Sécurité** Jetons, listes d’autorisation et contrôles de sécurité. ](</fr/gateway/security>) [**Dépannage** Diagnostics du Gateway et erreurs courantes. ](</fr/gateway/troubleshooting>) [**À propos et crédits** Origines du projet, contributeurs et licence. ](</fr/reference/credits>)

Was this useful?YesNo