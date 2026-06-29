---
title: npm shrinkwrap
source_url: https://docs.openclaw.ai/fr/gateway/security/shrinkwrap
scraped_at: 2026-06-29
---

Gateway & OpsGateway

Les checkouts source OpenClaw utilisent `pnpm-lock.yaml`. Les packages npm OpenClaw publiés utilisent `npm-shrinkwrap.json`, le fichier de verrouillage des dépendances publiable de npm, afin que les installations de packages utilisent le graphe de dépendances vérifié pendant la publication.

## La version simple

Shrinkwrap est un reçu pour l’arborescence des dépendances livrée avec un package npm. Il indique à npm quelles versions exactes des packages transitifs installer.

Pour les versions OpenClaw, cela signifie que :

  * le package publié ne demande pas à npm d’inventer un nouveau graphe de dépendances au moment de l’installation ;
  * les changements de dépendances deviennent plus faciles à vérifier, car ils apparaissent dans un fichier de verrouillage ;
  * la validation de publication peut tester le même graphe que les utilisateurs installeront ;
  * les surprises liées à la taille du package ou aux dépendances natives sont plus faciles à repérer avant la publication.


Shrinkwrap n’est pas un bac à sable. Il ne rend pas une dépendance sûre à lui seul, et il ne remplace pas l’isolation de l’hôte, `openclaw security audit`, la provenance des packages ni les tests de validation rapide d’installation.

Le modèle mental court :

Fichier | Où il compte | Ce qu’il signifie  
---|---|---  
`pnpm-lock.yaml` | Checkout source OpenClaw | Graphe de dépendances mainteneur  
`npm-shrinkwrap.json` | Package npm publié | Graphe d’installation npm pour les utilisateurs  
`package-lock.json` | Apps npm locales | Pas le contrat de publication OpenClaw  
  
## Pourquoi OpenClaw l’utilise

OpenClaw est un Gateway, un hôte de Plugin, un routeur de modèles et un runtime d’agent. Une installation par défaut peut affecter le temps de démarrage, l’utilisation du disque, les téléchargements de packages natifs et l’exposition à la chaîne d’approvisionnement.

Shrinkwrap donne à la vérification de publication une frontière stable :

  * les relecteurs peuvent voir les mouvements de dépendances transitives ;
  * les validateurs de packages peuvent rejeter une dérive inattendue du fichier de verrouillage ;
  * l’acceptation des packages peut tester les installations avec le graphe qui sera livré ;
  * les packages de Plugin peuvent porter leur propre graphe de dépendances verrouillé au lieu de dépendre du package racine pour posséder les dépendances propres au Plugin.


L’objectif n’est pas « plus de fichiers de verrouillage ». L’objectif est d’obtenir des installations de publication reproductibles avec une propriété claire.

## Détails techniques

Le package npm racine `openclaw` et les packages npm de Plugin appartenant à OpenClaw incluent `npm-shrinkwrap.json` lors de leur publication. Les packages de Plugin appropriés appartenant à OpenClaw peuvent aussi être publiés avec des `bundledDependencies` explicites, afin que leurs fichiers de dépendances runtime soient transportés dans l’archive tar du Plugin au lieu de dépendre uniquement de la résolution au moment de l’installation.

Maintenez la frontière comme ceci :

bashCopy code
[code]
    pnpm deps:shrinkwrap:generatepnpm deps:shrinkwrap:check
[/code]

Le générateur résout le format de verrouillage publiable de npm, mais rejette les versions de packages générées qui ne sont pas déjà présentes dans `pnpm-lock.yaml`. Cela garde intacte la frontière d’âge des dépendances pnpm, des overrides et de vérification des correctifs.

Utilisez les commandes racine uniquement lorsque vous actualisez intentionnellement le package racine sans toucher aux packages de Plugin :

bashCopy code
[code]
    pnpm deps:shrinkwrap:root:generatepnpm deps:shrinkwrap:root:check
[/code]

Vérifiez ces fichiers comme sensibles à la sécurité :

  * `pnpm-lock.yaml`
  * `npm-shrinkwrap.json`
  * les charges utiles de dépendances des Plugins groupés
  * tout diff de `package-lock.json`


Les validateurs de packages OpenClaw exigent shrinkwrap dans les nouvelles archives tar du package racine. Le chemin de publication npm des Plugins vérifie le shrinkwrap local au Plugin, installe les dépendances groupées locales au package, puis empaquette ou publie. Les validateurs de packages rejettent `package-lock.json` pour les packages OpenClaw publiés.

Pour inspecter un package racine publié :

bashCopy code
[code]
    npm pack openclaw@<version> --json --pack-destination /tmp/openclaw-packtar -tf /tmp/openclaw-pack/openclaw-<version>.tgz | grep '^package/npm-shrinkwrap.json$'
[/code]

Pour inspecter un package de Plugin appartenant à OpenClaw :

bashCopy code
[code]
    npm pack @openclaw/discord@<version> --json --pack-destination /tmp/openclaw-plugin-packtar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/npm-shrinkwrap.json$'tar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/node_modules/'
[/code]

Contexte : [npm-shrinkwrap.json](<https://docs.npmjs.com/cli/v11/configuring-npm/npm-shrinkwrap-json>).

Was this useful?YesNo

Open issue