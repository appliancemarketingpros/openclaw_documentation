---
title: Vérifications de santé (macOS)
source_url: https://docs.openclaw.ai/fr/platforms/mac/health
scraped_at: 2026-05-25
---

# Vérifications de santé sur macOS

Comment voir depuis l’application de barre de menus si le canal lié est sain.

## Barre de menus

  * Le point d’état reflète maintenant la santé de Baileys : 
    * Vert : lié + socket ouvert récemment.
    * Orange : connexion/reconnexion en cours.
    * Rouge : déconnecté ou échec de la sonde.
  * La ligne secondaire affiche « linked · auth 12m » ou montre la raison de l’échec.
  * L’élément de menu « Run Health Check » déclenche une sonde à la demande.


## Réglages

  * L’onglet Général gagne une carte Health affichant : âge de l’authentification liée, chemin/nombre du magasin de sessions, heure de la dernière vérification, dernier code d’erreur/statut, et des boutons pour Run Health Check / Reveal Logs.
  * Utilise un instantané en cache afin que l’interface se charge instantanément et revienne proprement à un mode dégradé hors ligne.
  * L’**onglet Channels** affiche l’état du canal + des contrôles pour WhatsApp/Telegram (QR de connexion, déconnexion, sonde, dernière déconnexion/erreur).


## Fonctionnement de la sonde

  * L’application exécute `openclaw health --json` via `ShellExecutor` toutes les ~60 s et à la demande. La sonde charge les identifiants et signale l’état sans envoyer de messages.
  * Mettre en cache séparément le dernier instantané sain et la dernière erreur pour éviter les scintillements ; afficher l’horodatage de chacun.


## En cas de doute

  * Vous pouvez toujours utiliser le flux CLI de [Santé du Gateway](</fr/gateway/health>) (`openclaw status`, `openclaw status --deep`, `openclaw health --json`) et suivre `/tmp/openclaw/openclaw-*.log` pour `web-heartbeat` / `web-reconnect`.


## Lié

  * [Santé du Gateway](</fr/gateway/health>)
  * [App macOS](</fr/platforms/macos>)


Was this useful?YesNo