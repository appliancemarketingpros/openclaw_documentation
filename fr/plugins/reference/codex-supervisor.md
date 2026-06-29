---
title: Plugin superviseur Codex
source_url: https://docs.openclaw.ai/fr/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin superviseur Codex

Supervisez les sessions du serveur d’application Codex depuis OpenClaw.

## Distribution

  * Paquet : `@openclaw/codex-supervisor`
  * Chemin d’installation : inclus dans OpenClaw


## Surface

contrats : outils

## Liste des sessions

`codex_sessions_list` utilise par défaut uniquement les sessions Codex chargées. Définissez `include_stored` pour inclure l’historique stocké ; le plugin utilise le chemin de listage exclusivement fondé sur la base de données d’état du serveur d’application Codex et limite les résultats stockés à 200 par défaut. Transmettez `max_stored_sessions` pour abaisser ou augmenter cette limite, jusqu’à 1000.

Was this useful?YesNo

Open issue