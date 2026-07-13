---
title: Recherche de sessions
source_url: https://docs.openclaw.ai/fr/concepts/session-search
scraped_at: 2026-07-13
---

AgentsSessions and memory

# Recherche dans les sessions

`sessions_search` recherche le texte de l’utilisateur et de l’assistant dans vos propres sessions passées. Chaque résultat comprend une `sessionKey`, un horodatage, un rôle et un court extrait correspondant. Transmettez la `sessionKey` renvoyée à `sessions_history` lorsque vous avez besoin du contexte de la conversation.

## Visibilité et sortie

La recherche utilise les mêmes règles de visibilité des sessions que `sessions_history`. Les résultats situés en dehors de l’arborescence de sessions visible par l’appelant sont supprimés avant l’application des limites de résultats. Les agents en bac à sable restent limités aux sessions qu’ils ont créées lorsque la visibilité des sessions créées est activée.

Les extraits sont expurgés avant d’être renvoyés au modèle. Les résultats sont également limités par leur nombre, la longueur des extraits et la taille totale de la réponse.

## Cycle de vie de l’index

OpenClaw stocke un index de recherche en texte intégral à côté des lignes de transcription dans la base de données SQLite de chaque agent. Les nouveaux messages de l’utilisateur et de l’assistant sont indexés dans la même transaction que celle qui les enregistre, afin que l’index ne soit jamais en retard sur les conversations en cours ; les résultats d’outils, les blocs de raisonnement et les images sont exclus. Seule la branche active de la transcription peut faire l’objet d’une recherche.

Les transcriptions antérieures à l’index (par exemple, les sessions importées par `openclaw doctor`) et les sessions dont la branche active a été rétablie à un état antérieur sont réindexées par une réconciliation en arrière-plan qui démarre lors de la recherche suivante. Une réponse contenant `indexing: true` peut donc être incomplète ; réessayez une fois l’indexation terminée. La suppression d’une session supprime ses entrées d’index dans la même transaction.

La recherche utilise actuellement le segmenteur de mots Unicode de SQLite avec suppression des signes diacritiques. La tokenisation par trigrammes pour la recherche de sous-chaînes en CJK constitue une amélioration future.

## Recherche dans les sessions ou recherche en mémoire

Utilisez `sessions_search` pour rechercher des mots ou des expressions exacts dans les transcriptions brutes des sessions. Utilisez [`memory_search`](</fr/concepts/memory-search>) pour les fichiers de mémoire persistante et le rappel sémantique. Le corpus expérimental de mémoire des sessions constitue le complément sémantique de cette recherche exacte dans les transcriptions.

Was this useful?YesNo

Open issue