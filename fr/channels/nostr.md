---
title: Nostr
source_url: https://docs.openclaw.ai/fr/channels/nostr
scraped_at: 2026-05-25
---

**État :** Plugin groupé facultatif (désactivé par défaut jusqu’à configuration).

Nostr est un protocole décentralisé de réseau social. Ce canal permet à OpenClaw de recevoir des messages directs (DM) chiffrés et d’y répondre via NIP-04.

## Plugin groupé

Les versions actuelles d’OpenClaw fournissent Nostr comme Plugin groupé ; les builds packagés normaux n’ont donc pas besoin d’une installation séparée.

### Installations anciennes/personnalisées

  * L’onboarding (`openclaw onboard`) et `openclaw channels add` présentent toujours Nostr depuis le catalogue de canaux partagé.
  * Si votre build exclut Nostr groupé, installez directement le package npm.

bashCopy code
[code]
    openclaw plugins install @openclaw/nostr
[/code]

Utilisez le package nu pour suivre le tag de publication officiel actuel. Épinglez une version exacte uniquement lorsque vous avez besoin d’une installation reproductible.

Utilisez un checkout local (workflows de développement) :

bashCopy code
[code]
    openclaw plugins install --link <path-to-local-nostr-plugin>
[/code]

Redémarrez le Gateway après avoir installé ou activé des plugins.

### Configuration non interactive

bashCopy code
[code]
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY" --relay-urls "wss://relay.damus.io,wss://relay.primal.net"
[/code]

Utilisez `--use-env` pour conserver `NOSTR_PRIVATE_KEY` dans l’environnement au lieu de stocker la clé dans la configuration.

## Configuration rapide

  1. Générez une paire de clés Nostr (si nécessaire) :

bashCopy code
[code]
    # Using naknak key generate
[/code]

  2. Ajoutez-la à la configuration :

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",    },  },}
[/code]

  3. Exportez la clé :

bashCopy code
[code]
    export NOSTR_PRIVATE_KEY="nsec1..."
[/code]

  4. Redémarrez le Gateway.


## Référence de configuration

Clé | Type | Par défaut | Description  
---|---|---|---  
`privateKey` | string | obligatoire | Clé privée au format `nsec` ou hex  
`relays` | string[] | `['wss://relay.damus.io', 'wss://nos.lol']` | URL de relais (WebSocket)  
`dmPolicy` | string | `pairing` | Politique d’accès aux DM  
`allowFrom` | string[] | `[]` | Pubkeys d’expéditeurs autorisées  
`enabled` | boolean | `true` | Activer/désactiver le canal  
`name` | string | - | Nom d’affichage  
`profile` | object | - | Métadonnées de profil NIP-01  
  
## Métadonnées de profil

Les données de profil sont publiées comme événement NIP-01 `kind:0`. Vous pouvez les gérer depuis l’interface de contrôle (Channels -> Nostr -> Profile) ou les définir directement dans la configuration.

Exemple :

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      profile: {        name: "openclaw",        displayName: "OpenClaw",        about: "Personal assistant DM bot",        picture: "https://example.com/avatar.png",        banner: "https://example.com/banner.png",        website: "https://example.com",        nip05: "openclaw@example.com",        lud16: "openclaw@example.com",      },    },  },}
[/code]

Remarques :

  * Les URL de profil doivent utiliser `https://`.
  * L’importation depuis des relais fusionne les champs et préserve les substitutions locales.


## Contrôle d’accès

### Politiques de DM

  * **pairing** (par défaut) : les expéditeurs inconnus reçoivent un code d’appairage.
  * **allowlist** : seules les pubkeys dans `allowFrom` peuvent envoyer des DM.
  * **open** : DM entrants publics (requiert `allowFrom: ["*"]`).
  * **disabled** : ignorer les DM entrants.


Remarques d’application :

  * Les signatures des événements entrants sont vérifiées avant la politique d’expéditeur et le déchiffrement NIP-04, ce qui permet de rejeter tôt les événements falsifiés.
  * Les réponses d’appairage sont envoyées sans traiter le corps du DM d’origine.
  * Les DM entrants sont limités en débit, et les charges utiles surdimensionnées sont supprimées avant le déchiffrement.


### Exemple d’allowlist

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      dmPolicy: "allowlist",      allowFrom: ["npub1abc...", "npub1xyz..."],    },  },}
[/code]

## Formats de clés

Formats acceptés :

  * **Clé privée :** `nsec...` ou hex de 64 caractères
  * **Pubkeys (`allowFrom`) :** `npub...` ou hex


## Relais

Valeurs par défaut : `relay.damus.io` et `nos.lol`.

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["wss://relay.damus.io", "wss://relay.primal.net", "wss://nostr.wine"],    },  },}
[/code]

Conseils :

  * Utilisez 2 à 3 relais pour la redondance.
  * Évitez un trop grand nombre de relais (latence, duplication).
  * Les relais payants peuvent améliorer la fiabilité.
  * Les relais locaux conviennent aux tests (`ws://localhost:7777`).


## Prise en charge du protocole

NIP | État | Description  
---|---|---  
NIP-01 | Pris en charge | Format d’événement de base + métadonnées profil  
NIP-04 | Pris en charge | DM chiffrés (`kind:4`)  
NIP-17 | Prévu | DM emballés  
NIP-44 | Prévu | Chiffrement versionné  
  
## Tests

### Relais local

bashCopy code
[code]
    # Start strfrydocker run -p 7777:7777 ghcr.io/hoytech/strfry
[/code]

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["ws://localhost:7777"],    },  },}
[/code]

### Test manuel

  1. Notez la pubkey du bot (npub) depuis les journaux.
  2. Ouvrez un client Nostr (Damus, Amethyst, etc.).
  3. Envoyez un DM à la pubkey du bot.
  4. Vérifiez la réponse.


## Dépannage

### Messages non reçus

  * Vérifiez que la clé privée est valide.
  * Assurez-vous que les URL de relais sont joignables et utilisent `wss://` (ou `ws://` en local).
  * Confirmez que `enabled` n’est pas `false`.
  * Consultez les journaux du Gateway pour les erreurs de connexion aux relais.


### Réponses non envoyées

  * Vérifiez que le relais accepte les écritures.
  * Vérifiez la connectivité sortante.
  * Surveillez les limites de débit des relais.


### Réponses en double

  * Attendu lors de l’utilisation de plusieurs relais.
  * Les messages sont dédupliqués par ID d’événement ; seule la première livraison déclenche une réponse.


## Sécurité

  * Ne commitez jamais de clés privées.
  * Utilisez des variables d’environnement pour les clés.
  * Envisagez `allowlist` pour les bots en production.
  * Les signatures sont vérifiées avant la politique d’expéditeur, et la politique d’expéditeur est appliquée avant le déchiffrement ; les événements falsifiés sont donc rejetés tôt et les expéditeurs inconnus ne peuvent pas forcer l’exécution complète du travail cryptographique.


## Limitations (MVP)

  * Messages directs uniquement (pas de conversations de groupe).
  * Pas de pièces jointes multimédias.
  * NIP-04 uniquement (emballage cadeau NIP-17 prévu).


## Connexe

  * [Vue d’ensemble des canaux](</fr/channels>) — tous les canaux pris en charge
  * [Appairage](</fr/channels/pairing>) — authentification DM et flux d’appairage
  * [Groupes](</fr/channels/groups>) — comportement des conversations de groupe et filtrage des mentions
  * [Routage des canaux](</fr/channels/channel-routing>) — routage de session pour les messages
  * [Sécurité](</fr/gateway/security>) — modèle d’accès et durcissement


Was this useful?YesNo