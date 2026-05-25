---
title: Amorçage de l’agent
source_url: https://docs.openclaw.ai/fr/start/bootstrapping
scraped_at: 2026-05-25
---

L’amorçage est le rituel de **première exécution** qui prépare un espace de travail d’agent et collecte les détails d’identité. Il a lieu après l’intégration, lorsque l’agent démarre pour la première fois.

## Ce que fait l’amorçage

Lors de la première exécution de l’agent, OpenClaw amorce l’espace de travail (par défaut `~/.openclaw/workspace`) :

  * Initialise `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Exécute un court rituel de questions-réponses (une question à la fois).
  * Écrit l’identité et les préférences dans `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Supprime `BOOTSTRAP.md` une fois terminé afin qu’il ne s’exécute qu’une seule fois.


Pour les exécutions de modèles intégrés/locaux, OpenClaw garde `BOOTSTRAP.md` hors du contexte système privilégié. Lors de la première exécution interactive principale, il transmet tout de même le contenu du fichier dans le prompt utilisateur afin que les modèles qui n’appellent pas de manière fiable l’outil `read` puissent terminer le rituel. Si l’exécution actuelle ne peut pas accéder en toute sécurité à l’espace de travail, l’agent reçoit une note d’amorçage limitée au lieu d’un message de salutation générique.

## Ignorer l’amorçage

Pour l’ignorer avec un espace de travail préinitialisé, exécutez `openclaw onboard --skip-bootstrap`.

## Où il s’exécute

L’amorçage s’exécute toujours sur l’**hôte Gateway**. Si l’application macOS se connecte à un Gateway distant, l’espace de travail et les fichiers d’amorçage résident sur cette machine distante.

## Documentation associée

  * Intégration de l’application macOS : [Intégration](</fr/start/onboarding>)
  * Organisation de l’espace de travail : [Espace de travail de l’agent](</fr/concepts/agent-workspace>)


Was this useful?YesNo