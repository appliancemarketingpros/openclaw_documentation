---
title: Journalisation macOS
source_url: https://docs.openclaw.ai/fr/platforms/mac/logging
scraped_at: 2026-05-25
---

# Journalisation (macOS)

## Journal de diagnostic rotatif sur fichier (volet Débogage)

OpenClaw achemine les journaux de l’app macOS via swift-log (journalisation unifiée par défaut) et peut écrire sur disque un journal local rotatif lorsque vous avez besoin d’une capture durable.

  * Niveau de détail : **volet Débogage → Journaux → Journalisation de l’app → Niveau de détail**
  * Activer : **volet Débogage → Journaux → Journalisation de l’app → « Écrire le journal de diagnostic rotatif (JSONL) »**
  * Emplacement : `~/Library/Logs/OpenClaw/diagnostics.jsonl` (rotation automatique ; les anciens fichiers reçoivent un suffixe `.1`, `.2`, …)
  * Effacer : **volet Débogage → Journaux → Journalisation de l’app → « Effacer »**


Remarques :

  * Cette option est **désactivée par défaut**. Activez-la uniquement pendant un débogage actif.
  * Traitez le fichier comme sensible ; ne le partagez pas sans vérification.


## Données privées de la journalisation unifiée sur macOS

La journalisation unifiée masque la plupart des charges utiles, sauf si un sous-système active `privacy -off`. D’après l’article de Peter sur les [étrangetés de confidentialité de la journalisation macOS](<https://steipete.me/posts/2025/logging-privacy-shenanigans>) (2025), ce comportement est contrôlé par un plist dans `/Library/Preferences/Logging/Subsystems/`, indexé par le nom du sous-système. Seules les nouvelles entrées de journal prennent en compte l’indicateur ; activez-le donc avant de reproduire un problème.

## Activer pour OpenClaw (`ai.openclaw`)

  * Écrivez d’abord le plist dans un fichier temporaire, puis installez-le atomiquement en tant que root :

bashCopy code
[code]
    cat <<'EOF' >/tmp/ai.openclaw.plist<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>DEFAULT-OPTIONS</key>    <dict>        <key>Enable-Private-Data</key>        <true/>    </dict></dict></plist>EOFsudo install -m 644 -o root -g wheel /tmp/ai.openclaw.plist /Library/Preferences/Logging/Subsystems/ai.openclaw.plist
[/code]

  * Aucun redémarrage n’est nécessaire ; logd détecte le fichier rapidement, mais seules les nouvelles lignes de journal incluront les charges utiles privées.
  * Affichez la sortie plus riche avec l’assistant existant, par exemple `./scripts/clawlog.sh --category WebChat --last 5m`.


## Désactiver après le débogage

  * Supprimez la surcharge : `sudo rm /Library/Preferences/Logging/Subsystems/ai.openclaw.plist`.
  * Vous pouvez aussi exécuter `sudo log config --reload` pour forcer logd à abandonner immédiatement la surcharge.
  * N’oubliez pas que cette surface peut inclure des numéros de téléphone et le contenu de messages ; gardez le plist en place uniquement pendant que vous avez activement besoin de ces détails supplémentaires.


## Connexe

  * [App macOS](</fr/platforms/macos>)
  * [Journalisation du Gateway](</fr/gateway/logging>)


Was this useful?YesNo