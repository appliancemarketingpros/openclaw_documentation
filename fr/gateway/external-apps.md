---
title: Intégrations Gateway pour les applications externes
source_url: https://docs.openclaw.ai/fr/gateway/external-apps
scraped_at: 2026-06-29
---

ReferenceRPC and API

Les applications externes doivent communiquer avec OpenClaw via le protocole Gateway aujourd’hui. Utilisez le WebSocket Gateway et les méthodes RPC lorsqu’un script, un tableau de bord, une tâche CI, une extension IDE ou un autre processus veut démarrer des exécutions d’agents, diffuser des événements, attendre des résultats, annuler un travail ou inspecter les ressources Gateway.

## Ce qui est disponible aujourd’hui

Surface | État | À utiliser pour  
---|---|---  
[Protocole Gateway](</fr/gateway/protocol>) | Prêt | Transport WebSocket, poignée de main de connexion, portées d’authentification, versionnage du protocole et événements.  
[Référence RPC Gateway](</fr/reference/rpc>) | Prêt | Méthodes Gateway actuelles pour les agents, sessions, tâches, modèles, outils, artefacts et approbations.  
[`openclaw agent`](</fr/cli/agent>) | Prêt | Intégration de script ponctuelle lorsque l’appel au CLI via le shell suffit.  
[`openclaw message`](</fr/cli/message>) | Prêt | Envoi de messages ou d’actions de canal depuis des scripts.  
  
L’arborescence source contient des travaux de package internes pour une future bibliothèque cliente, mais ce n’est pas une surface d’installation publique. Traitez-la comme un détail d’implémentation en aperçu jusqu’à ce que les packages soient publiés et versionnés.

## Parcours recommandé

  1. Exécutez ou découvrez un Gateway.
  2. Connectez-vous via le [protocole Gateway](</fr/gateway/protocol>).
  3. Appelez les méthodes RPC documentées depuis la [référence RPC Gateway](</fr/reference/rpc>).
  4. Épinglez la version d’OpenClaw que vous testez.
  5. Revérifiez la référence RPC lors de la mise à niveau d’OpenClaw.


Pour les exécutions d’agents, commencez par le RPC `agent` et associez-le à `agent.wait` lorsque vous avez besoin d’un résultat terminal. Pour un état de conversation durable, utilisez les méthodes `sessions.*`. Pour les intégrations d’interface utilisateur, abonnez-vous aux événements Gateway et affichez uniquement les familles d’événements que votre application comprend.

## Code d’application et code de Plugin

Utilisez le RPC Gateway lorsque le code vit en dehors d’OpenClaw :

  * Scripts Node qui démarrent ou observent des exécutions d’agents
  * Tâches CI qui appellent un Gateway
  * tableaux de bord et panneaux d’administration
  * extensions IDE
  * ponts externes qui n’ont pas besoin de devenir des Plugins de canal
  * tests d’intégration avec des transports Gateway factices ou réels


Utilisez le SDK Plugin lorsque le code s’exécute dans OpenClaw :

  * Plugins de fournisseur
  * Plugins de canal
  * hooks d’outil ou de cycle de vie
  * Plugins de harnais d’agent
  * assistants d’exécution approuvés


Les applications externes ne doivent pas importer `openclaw/plugin-sdk/*` ; ces sous-chemins sont destinés aux Plugins chargés par OpenClaw.

## Associés

  * [Protocole Gateway](</fr/gateway/protocol>)
  * [Référence RPC Gateway](</fr/reference/rpc>)
  * [Commande CLI agent](</fr/cli/agent>)
  * [Commande CLI message](</fr/cli/message>)
  * [Boucle d’agent](</fr/concepts/agent-loop>)
  * [Environnements d’exécution d’agent](</fr/concepts/agent-runtimes>)
  * [Sessions](</fr/concepts/session>)
  * [Tâches en arrière-plan](</fr/automation/tasks>)
  * [Agents ACP](</fr/tools/acp-agents>)
  * [Vue d’ensemble du SDK Plugin](</fr/plugins/sdk-overview>)


Was this useful?YesNo

Open issue