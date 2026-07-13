---
title: SecretRefs du coffre-fort
source_url: https://docs.openclaw.ai/fr/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# SecretRefs Vault

Le plugin Vault intégré permet à OpenClaw de résoudre les SecretRefs `exec` depuis HashiCorp Vault au démarrage du Gateway et lors des rechargements. OpenClaw stocke les références Vault dans la configuration, conserve les valeurs résolues dans l’instantané des secrets en mémoire et ne réécrit pas les clés API résolues dans `openclaw.json`.

Utilisez cette fonctionnalité si vous exécutez déjà Vault ou souhaitez conserver les clés des fournisseurs de modèles hors des fichiers de configuration d’OpenClaw. Pour le modèle d’exécution des SecretRefs, consultez [Gestion des secrets](</fr/gateway/secrets>).

## Avant de commencer

Vous avez besoin des éléments suivants :

  * OpenClaw avec le plugin `vault` intégré disponible
  * un serveur Vault accessible
  * une authentification Vault capable de produire un jeton client disposant d’un accès en lecture aux chemins de secrets qu’OpenClaw doit résoudre
  * l’environnement qui démarre le Gateway doit inclure `VAULT_ADDR` et soit `VAULT_TOKEN`, soit `OPENCLAW_VAULT_AUTH_METHOD=token_file` avec `VAULT_TOKEN_FILE`, soit une connexion JWT/Kubernetes configurée


Le résolveur communique avec Vault par HTTP depuis Node. Le Gateway n’a pas besoin de la CLI Vault pour résoudre les SecretRefs.

Activez le plugin intégré avant d’exécuter les commandes `openclaw vault` :

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Stocker une clé de fournisseur dans Vault

Par défaut, OpenClaw utilise KV v2 monté sur `secret`, conformément aux exemples du serveur de développement Vault. Pour un environnement Vault de production, définissez `OPENCLAW_VAULT_KV_MOUNT` sur le chemin de montage KV réel avant de créer des identifiants SecretRef. Avec les valeurs par défaut d’OpenClaw, cet identifiant SecretRef :

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

lit ce champ Vault :

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Vous pouvez notamment le créer avec la CLI Vault comme suit :

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Utilisez pour OpenClaw un jeton client à portée limitée, et non un jeton racine. Pour l’organisation KV v2 par défaut, une stratégie minimale destinée aux clés des fournisseurs de modèles ressemble à ceci :

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Rendre Vault accessible au Gateway

Pour un Gateway local non conteneurisé, exportez les paramètres Vault dans le même interpréteur de commandes que celui qui démarre OpenClaw. La méthode d’authentification par défaut lit un jeton client Vault depuis `VAULT_TOKEN` :

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Si Vault Agent écrit un fichier récepteur de jeton, utilisez l’authentification par fichier de jeton :

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Pour un serveur Vault signé par une autorité de certification privée, installez cette autorité dans le magasin de certificats de confiance de l’hôte et activez la confiance système de Node :

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Vous pouvez également fournir directement un ensemble de certificats PEM :

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Ces variables doivent être présentes au démarrage d’OpenClaw. Le plugin Vault les transmet à son processus de résolution.

Pour une authentification JWT non interactive, utilisez un fichier JWT de charge de travail et un rôle Vault de type `jwt` :

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

Le fichier JWT doit contenir un jeton de charge de travail projeté, par exemple un jeton de compte de service Kubernetes dont l’audience est acceptée par le rôle Vault. La connexion OIDC interactive par navigateur est utile aux personnes, mais l’exécution du Gateway nécessite une connexion JWT non interactive ou un fichier de jeton.

Pour la méthode d’authentification Kubernetes de Vault, utilisez `kubernetes`. Elle est destinée aux Gateways exécutés sous forme de Pods ; le montage par défaut est `kubernetes` et le fichier JWT par défaut correspond au chemin standard du jeton du compte de service :

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Définissez `OPENCLAW_VAULT_AUTH_MOUNT` uniquement lorsque l’authentification Kubernetes est montée dans Vault ailleurs que sous `auth/kubernetes`. Définissez `OPENCLAW_VAULT_JWT_FILE` uniquement lorsque le jeton du compte de service est projeté dans un chemin personnalisé.

Paramètres facultatifs :

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Vérifiez ce qui est accessible depuis l’interpréteur de commandes actuel :

bashCopy code
[code]
    openclaw vault status
[/code]

Lorsque plusieurs fournisseurs de secrets adossés à Vault sont configurés, sélectionnez-en un par alias :

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` n’affiche jamais `VAULT_TOKEN` ; la commande indique uniquement si le jeton, le fichier de jeton et le fichier JWT sont définis.

## Générer et appliquer un plan SecretRef

Créez un plan qui associe à Vault la clé API du fournisseur de modèles OpenRouter :

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Appliquez et vérifiez le plan :

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Utilisez `--allow-exec`, car le plugin Vault effectue la résolution par l’intermédiaire d’un fournisseur SecretRef exec géré par OpenClaw.

Si le Gateway n’est pas encore en cours d’exécution, démarrez-le normalement après avoir appliqué le plan au lieu d’exécuter `openclaw secrets reload`.

## Configurer davantage de clés de fournisseurs

Raccourcis intégrés :

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Plusieurs clés de fournisseurs dans un même plan :

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Pour les fournisseurs intégrés dépourvus de raccourcis, ainsi que les fournisseurs de modèles personnalisés ou compatibles avec OpenAI déjà configurés, utilisez `--provider-key` :

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Chaque option `--provider-key <provider=id>` écrit une SecretRef dans `models.providers.<provider>.apiKey`. Pour les fournisseurs personnalisés, elle ne crée pas les paramètres `baseUrl`, `api` ou `models` du fournisseur ; configurez-les d’abord.

Utilisez `--target <path=id>` pour tout chemin cible SecretRef connu :

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Les chemins cibles sans préfixe s’appliquent à `openclaw.json`. Utilisez `auth-profiles:<agentId>:<path>` pour les cibles existantes dans `auth-profiles.json`. Le chemin cible doit être une cible SecretRef enregistrée dans OpenClaw. La commande de configuration ne crée pas de secrets nommés arbitraires dans OpenClaw ; Vault reste le magasin de secrets et OpenClaw stocke les SecretRefs uniquement dans les champs de configuration pris en charge.

## Format des identifiants SecretRef

Les identifiants SecretRef Vault suivent cette convention :

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Exemples :

Identifiant SecretRef | Lecture Vault KV v2 par défaut | Champ renvoyé  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Le champ Vault renvoyé doit être une chaîne de caractères.

Pour KV v1, définissez :

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

`providers/openrouter/apiKey` lit alors :

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Ce qu’OpenClaw stocke

L’application d’un plan de configuration Vault stocke un fournisseur géré par le plugin :

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Les champs d’identifiants pointent vers ce fournisseur :

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

La valeur résolue réside uniquement dans l’instantané actif des secrets de l’exécution.

## Conteneurs et déploiements gérés

Les Gateways conteneurisés utilisent toujours le même plugin et la même configuration SecretRef. Le conteneur doit recevoir :

  * `VAULT_ADDR`
  * une source d’authentification : 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` avec `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` avec `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` et `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` avec `OPENCLAW_VAULT_AUTH_ROLE` ; vous pouvez éventuellement remplacer `OPENCLAW_VAULT_AUTH_MOUNT` ou `OPENCLAW_VAULT_JWT_FILE`
  * les paramètres facultatifs `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` et `OPENCLAW_VAULT_KV_VERSION`


Avec Kubernetes, privilégiez `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` lorsque l’authentification Kubernetes de Vault est configurée pour le cluster. Utilisez `OPENCLAW_VAULT_AUTH_METHOD=jwt` uniquement lorsque Vault est configuré pour traiter le cluster comme un émetteur JWT/OIDC générique. Les deux options sont préférables à un jeton Vault à longue durée de vie dans un Secret Kubernetes. Les déploiements avec conteneur compagnon ou injecteur Vault Agent peuvent utiliser `token_file` à la place.

Pour les configurations Vault mutualisées, conservez le routage des locataires dans la stratégie Vault et la configuration du déploiement. OpenClaw n’impose aucun montage, rôle ou chemin fixe : chaque environnement Gateway peut définir ses propres valeurs `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` et identifiants SecretRef. Si un Gateway partagé doit résoudre simultanément différents utilisateurs Vault, utilisez des fournisseurs exec configurés manuellement qui encapsulent des environnements d’authentification distincts, ou répartissez les locataires entre plusieurs environnements Gateway dotés d’environnements Vault séparés.

## Ressources connexes

  * [Gestion des secrets](</fr/gateway/secrets>)
  * [`openclaw secrets`](</fr/cli/secrets>)
  * [Inventaire des plugins](</fr/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue