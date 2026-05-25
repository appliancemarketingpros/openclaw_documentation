---
title: outil apply_patch
source_url: https://docs.openclaw.ai/fr/tools/apply-patch
scraped_at: 2026-05-25
---

Appliquez des modifications de fichiers à l’aide d’un format de patch structuré. C’est idéal pour les modifications portant sur plusieurs fichiers ou plusieurs hunks, où un seul appel `edit` serait fragile.

L’outil accepte une seule chaîne `input` qui enveloppe une ou plusieurs opérations sur des fichiers :

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Paramètres

  * `input` (obligatoire) : contenu complet du patch, y compris `*** Begin Patch` et `*** End Patch`.


## Notes

  * Les chemins de patch prennent en charge les chemins relatifs (depuis le répertoire de l’espace de travail) et les chemins absolus.
  * `tools.exec.applyPatch.workspaceOnly` vaut `true` par défaut (contenu dans l’espace de travail). Définissez-le sur `false` uniquement si vous souhaitez intentionnellement que `apply_patch` écrive/supprime en dehors du répertoire de l’espace de travail.
  * Utilisez `*** Move to:` dans un hunk `*** Update File:` pour renommer des fichiers.
  * `*** End of File` marque une insertion uniquement en fin de fichier lorsque nécessaire.
  * Disponible par défaut pour les modèles OpenAI et OpenAI Codex. Définissez `tools.exec.applyPatch.enabled: false` pour le désactiver.
  * Vous pouvez éventuellement restreindre l’accès par modèle via `tools.exec.applyPatch.allowModels`.
  * La configuration se trouve uniquement sous `tools.exec`.


## Exemple

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Liens connexes

[**Diffs** Visionneuse de diff en lecture seule pour présenter les changements. ](</fr/tools/diffs>) [**Outil exec** Exécution de commandes shell depuis l’agent. ](</fr/tools/exec>) [**Exécution de code** Analyse Python distante en bac à sable avec xAI. ](</fr/tools/code-execution>)

Was this useful?YesNo