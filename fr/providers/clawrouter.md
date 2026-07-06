---
title: ClawRouter
source_url: https://docs.openclaw.ai/fr/providers/clawrouter
scraped_at: 2026-07-06
---

ModelsProviders

ClawRouter donne à OpenClaw une clé à portée de politique pour plusieurs fournisseurs de modèles en amont. Le plugin intégré découvre uniquement les modèles autorisés pour cette clé, achemine chaque modèle via son protocole déclaré et signale le budget de la clé ainsi que l’utilisation agrégée sur les surfaces d’utilisation d’OpenClaw.

Vous n’installez ni n’authentifiez chaque plugin de fournisseur en amont sur l’hôte OpenClaw. Les identifiants en amont et le transfert propre à chaque fournisseur restent dans ClawRouter. OpenClaw n’a besoin que du plugin intégré `@openclaw/clawrouter` et d’un identifiant ClawRouter émis.

Propriété | Valeur  
---|---  
Fournisseur | `clawrouter`  
Paquet | `@openclaw/clawrouter`  
Authentification | `CLAWROUTER_API_KEY`  
URL par défaut | `https://clawrouter.openclaw.ai`  
Catalogue modèles | À portée d’identifiant via `/v1/catalog`  
Quotas | Budget mensuel et utilisation via `/v1/usage`  
  
## Bien démarrer

* ### Obtenir un identifiant à portée limitée

Demandez à votre administrateur ClawRouter un identifiant dont la politique inclut les fournisseurs, les modèles et le budget mensuel que vous devez utiliser. Les identifiants sont révélés une seule fois lors de leur émission.

* ### Configurer OpenClaw

bashCopy code
[code]
    export CLAWROUTER_API_KEY="..."openclaw onboard --auth-choice clawrouter-api-keyopenclaw plugins enable clawrouter
[/code]

Le plugin est intégré à OpenClaw. Si votre configuration définit `plugins.allow`, ajoutez `clawrouter` à cette liste avant de l’activer. Pour un déploiement personnalisé, définissez `models.providers.clawrouter.baseUrl` sur l’origine ClawRouter ; la valeur par défaut est `https://clawrouter.openclaw.ai`.

* ### Lister les modèles accordés

bashCopy code
[code]
    openclaw models list --all --provider clawrouter
[/code]

Utilisez les références de modèle retournées exactement comme indiqué. Elles conservent l’espace de noms en amont, comme `clawrouter/openai/...`, `clawrouter/anthropic/...` ou `clawrouter/google/...`. Si `agents.defaults.models` est une liste d’autorisation dans votre configuration, ajoutez-y chaque référence ClawRouter sélectionnée.

* ### Sélectionner un modèle

bashCopy code
[code]
    openclaw models set clawrouter/<provider>/<model>
[/code]

Vous pouvez également sélectionner un modèle retourné pour une exécution avec `openclaw agent --model clawrouter/<provider>/<model> --message "..."`.

## Découverte des modèles

`GET /v1/catalog` est la source de vérité. OpenClaw ne fournit pas une seconde liste fixe de modèles ClawRouter. Un modèle configuré dans ClawRouter apparaît lorsque :

  * la politique de l’identifiant accorde son fournisseur ;
  * la connexion du fournisseur est activée et prête ;
  * le modèle du catalogue annonce une capacité LLM prise en charge ; et
  * le catalogue expose un contrat de transport pris en charge par le plugin.


Ajouter un autre modèle à un fournisseur ClawRouter pris en charge ne nécessite donc pas de version OpenClaw ni un autre plugin de fournisseur. Le prochain rafraîchissement du catalogue le découvre. Un modèle qui nécessite un nouveau protocole filaire requiert une prise en charge dans le plugin ClawRouter avant qu’OpenClaw ne l’annonce.

## Protocole et plugins de fournisseurs

Vous n’avez pas besoin d’installer le plugin d’authentification de chaque entreprise en amont. ClawRouter possède les identifiants en amont ; son catalogue indique à OpenClaw quel transport utiliser. Le plugin prend en charge :

Route du catalogue | Transport OpenClaw  
---|---  
Chat compatible OpenAI | `openai-completions`  
Responses compatible OpenAI | `openai-responses`  
Messages Anthropic natifs | `anthropic-messages`  
Streaming Google Gemini natif | `google-generative-ai`  
  
Le plugin applique également les politiques de rejeu et de schéma d’outils correspondantes pour ces familles. Les lignes du catalogue utilisant un autre format de requête/flux ne sont intentionnellement pas annoncées comme modèles texte OpenClaw. Normalisez ces fournisseurs vers l’un des contrats pris en charge dans ClawRouter plutôt que d’envoyer une charge utile incompatible.

## Quotas et utilisation

La réponse `/v1/usage` de ClawRouter alimente les surfaces normales d’utilisation des fournisseurs d’OpenClaw. `/status` et les états de tableau de bord associés affichent la fenêtre de budget mensuel lorsque la clé a une limite, ainsi que les totaux de requêtes, de tokens et de dépenses. Les clés sans compteur affichent tout de même l’utilisation agrégée sans fenêtre de pourcentage.

La recherche de quota utilise la même clé à portée limitée que la découverte des modèles. Un échec de recherche de quota ne bloque pas l’exécution du modèle.

Consultez l’instantané en direct avec :

bashCopy code
[code]
    openclaw status --usageopenclaw models status
[/code]

Le même instantané de fournisseur est disponible pour `/status` dans le chat et dans l’interface d’utilisation d’OpenClaw. Le budget est appliqué à toute la politique, donc les requêtes effectuées par un autre client utilisant la même politique ClawRouter peuvent modifier le pourcentage restant.

## Dépannage

Symptôme | Vérification  
---|---  
Aucun modèle ClawRouter | Confirmez que le plugin est activé et autorisé par `plugins.allow`, puis vérifiez que l’identifiant est actif et accorde au moins un fournisseur prêt.  
Un modèle ClawRouter configuré est manquant | Inspectez sa capacité `/v1/catalog` et son format de route. Les contrats de transport non pris en charge sont intentionnellement filtrés.  
`Unknown model: clawrouter/...` | Ajoutez la référence exacte du catalogue à `agents.defaults.models` lorsque cette carte de configuration est utilisée comme liste d’autorisation.  
`401` ou `403` depuis le catalogue ou l’utilisation | Réémettez ou redéfinissez la portée de l’identifiant ClawRouter ; OpenClaw ne se rabat pas sur les clés des fournisseurs en amont.  
L’appel de modèle échoue après la découverte | Vérifiez la connexion du fournisseur et l’état de santé en amont dans ClawRouter, puis réessayez après le rétablissement de son état de disponibilité.  
L’utilisation affiche des totaux mais pas de pourcentage | La politique est sans compteur ; ajoutez un budget mensuel dans ClawRouter pour exposer une fenêtre de pourcentage.  
  
## Comportement de sécurité

  * La découverte du catalogue est limitée à la clé de proxy configurée et mise en cache par clé.
  * La clé de proxy est attachée uniquement lors de l’envoi de la requête ; elle n’est pas stockée dans les métadonnées du modèle.
  * Les identifiants de modèles Anthropic et Gemini natifs sont réécrits vers leurs identifiants en amont uniquement lors de l’envoi.
  * Les lignes de catalogue non prises en charge ou non accordées échouent de manière fermée et ne sont pas sélectionnables.


## Associés

[**Fournisseurs de modèles** Configuration des fournisseurs et sélection des modèles. ](</fr/concepts/model-providers>) [**Suivi de l’utilisation** Surfaces d’utilisation et d’état d’OpenClaw. ](</fr/concepts/usage-tracking>)

Was this useful?YesNo

Open issue