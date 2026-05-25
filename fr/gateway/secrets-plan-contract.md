---
title: Contrat du plan d’application des secrets
source_url: https://docs.openclaw.ai/fr/gateway/secrets-plan-contract
scraped_at: 2026-05-25
---

Cette page définit le contrat strict appliqué par `openclaw secrets apply`.

Si une cible ne correspond pas à ces règles, l’application échoue avant toute mutation de la configuration.

## Forme du fichier de plan

`openclaw secrets apply --from <plan.json>` attend un tableau `targets` de cibles de plan :

json5Copy code
[code]
    {  version: 1,  protocolVersion: 1,  targets: [    {      type: "models.providers.apiKey",      path: "models.providers.openai.apiKey",      pathSegments: ["models", "providers", "openai", "apiKey"],      providerId: "openai",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },    {      type: "auth-profiles.api_key.key",      path: "profiles.openai:default.key",      pathSegments: ["profiles", "openai:default", "key"],      agentId: "main",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },  ],}
[/code]

## Portée des cibles prises en charge

Les cibles de plan sont acceptées pour les chemins d’identifiants pris en charge dans :

  * [Surface d’identifiants SecretRef](</fr/reference/secretref-credential-surface>)


## Comportement du type de cible

Règle générale :

  * `target.type` doit être reconnu et doit correspondre à la forme normalisée de `target.path`.


Les alias de compatibilité restent acceptés pour les plans existants :

  * `models.providers.apiKey`
  * `skills.entries.apiKey`
  * `channels.googlechat.serviceAccount`


## Règles de validation des chemins

Chaque cible est validée avec l’ensemble des règles suivantes :

  * `type` doit être un type de cible reconnu.
  * `path` doit être un chemin pointé non vide.
  * `pathSegments` peut être omis. S’il est fourni, il doit se normaliser exactement vers le même chemin que `path`.
  * Les segments interdits sont rejetés : `__proto__`, `prototype`, `constructor`.
  * Le chemin normalisé doit correspondre à la forme de chemin enregistrée pour le type de cible.
  * Si `providerId` ou `accountId` est défini, il doit correspondre à l’identifiant encodé dans le chemin.
  * Les cibles `auth-profiles.json` exigent `agentId`.
  * Lors de la création d’un nouveau mappage `auth-profiles.json`, incluez `authProfileProvider`.


## Comportement en cas d’échec

Si une cible échoue à la validation, l’application se termine avec une erreur du type :

textCopy code
[code]
    Invalid plan target path for models.providers.apiKey: models.providers.openai.baseUrl
[/code]

Aucune écriture n’est validée pour un plan invalide.

## Comportement de consentement du fournisseur Exec

  * `--dry-run` ignore par défaut les vérifications SecretRef exec.
  * Les plans contenant des SecretRefs/fournisseurs exec sont rejetés en mode écriture sauf si `--allow-exec` est défini.
  * Lors de la validation/de l’application de plans contenant exec, transmettez `--allow-exec` dans les commandes dry-run et écriture.


## Remarques sur la portée d’exécution et d’audit

  * Les entrées `auth-profiles.json` uniquement par ref (`keyRef`/`tokenRef`) sont incluses dans la résolution d’exécution et dans la couverture d’audit.
  * `secrets apply` écrit les cibles `openclaw.json` prises en charge, les cibles `auth-profiles.json` prises en charge et les cibles facultatives de nettoyage.


## Vérifications opérateur

bashCopy code
[code]
    # Validate plan without writesopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run # Then apply for realopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json # For exec-containing plans, opt in explicitly in both modesopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
[/code]

Si l’application échoue avec un message de chemin de cible invalide, régénérez le plan avec `openclaw secrets configure` ou corrigez le chemin de cible vers une forme prise en charge ci-dessus.

## Documentation associée

  * [Gestion des secrets](</fr/gateway/secrets>)
  * [CLI `secrets`](</fr/cli/secrets>)
  * [Surface d’identifiants SecretRef](</fr/reference/secretref-credential-surface>)
  * [Référence de configuration](</fr/gateway/configuration-reference>)


Was this useful?YesNo