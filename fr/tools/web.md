---
title: Recherche web
source_url: https://docs.openclaw.ai/fr/tools/web
scraped_at: 2026-05-25
---

L’outil `web_search` recherche sur le Web avec votre fournisseur configuré et renvoie des résultats. Les résultats sont mis en cache par requête pendant 15 minutes (configurable).

OpenClaw inclut également `x_search` pour les publications X (anciennement Twitter) et `web_fetch` pour la récupération légère d’URL. Dans cette phase, `web_fetch` reste local tandis que `web_search` et `x_search` peuvent utiliser xAI Responses en arrière-plan.

## Démarrage rapide

* ### Choisir un fournisseur

Choisissez un fournisseur et effectuez toute configuration requise. Certains fournisseurs sont sans clé, tandis que d’autres utilisent des clés d’API. Consultez les pages des fournisseurs ci-dessous pour plus de détails.

* ### Configurer

bashCopy code
[code]
    openclaw configure --section web
[/code]

Cela stocke le fournisseur et tout identifiant nécessaire. Vous pouvez aussi définir une variable d’environnement (par exemple `BRAVE_API_KEY`) et ignorer cette étape pour les fournisseurs adossés à une API.

* ### L’utiliser

L’agent peut maintenant appeler `web_search` :

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Pour les publications X, utilisez :

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Choisir un fournisseur

[**Brave Search** Résultats structurés avec extraits. Prend en charge le mode `llm-context` et les filtres de pays/langue. Offre gratuite disponible. ](</fr/tools/brave-search>) [**DuckDuckGo** Solution de repli sans clé. Aucune clé d’API requise. Intégration non officielle basée sur HTML. ](</fr/tools/duckduckgo-search>) [**Exa** Recherche neuronale + par mots-clés avec extraction de contenu (points forts, texte, résumés). ](</fr/tools/exa-search>) [**Firecrawl** Résultats structurés. Fonctionne au mieux avec `firecrawl_search` et `firecrawl_scrape` pour l’extraction approfondie. ](</fr/tools/firecrawl>) [**Gemini** Réponses synthétisées par IA avec citations via l’ancrage Google Search. ](</fr/tools/gemini-search>) [**Grok** Réponses synthétisées par IA avec citations via l’ancrage Web xAI. ](</fr/tools/grok-search>) [**Kimi** Réponses synthétisées par IA avec citations via la recherche Web Moonshot ; les replis de chat non ancrés échouent explicitement. ](</fr/tools/kimi-search>) [**MiniMax Search** Résultats structurés via l’API de recherche MiniMax Token Plan. ](</fr/tools/minimax-search>) [**Ollama Web Search** Recherche via un hôte Ollama local connecté ou l’API Ollama hébergée. ](</fr/tools/ollama-search>) [**Perplexity** Résultats structurés avec contrôles d’extraction de contenu et filtrage de domaines. ](</fr/tools/perplexity-search>) [**SearXNG** Métarecherche auto-hébergée. Aucune clé d’API requise. Agrège Google, Bing, DuckDuckGo, et plus encore. ](</fr/tools/searxng-search>) [**Tavily** Résultats structurés avec profondeur de recherche, filtrage par sujet et `tavily_extract` pour l’extraction d’URL. ](</fr/tools/tavily>)

### Comparaison des fournisseurs

Fournisseur | Style de résultat | Filtres | Clé d’API  
---|---|---|---  
[Brave](</fr/tools/brave-search>) | Extraits structurés | Pays, langue, période, mode `llm-context` | `BRAVE_API_KEY`  
[DuckDuckGo](</fr/tools/duckduckgo-search>) | Extraits structurés | \-- | Aucune (sans clé)  
[Exa](</fr/tools/exa-search>) | Structuré + extrait | Mode neuronal/par mots-clés, date, extraction de contenu | `EXA_API_KEY`  
[Firecrawl](</fr/tools/firecrawl>) | Extraits structurés | Via l’outil `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</fr/tools/gemini-search>) | Synthétisé par IA + citations | \-- | `GEMINI_API_KEY`  
[Grok](</fr/tools/grok-search>) | Synthétisé par IA + citations | \-- | `XAI_API_KEY`  
[Kimi](</fr/tools/kimi-search>) | Synthétisé par IA + citations ; échoue sur les replis de chat non ancrés | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</fr/tools/minimax-search>) | Extraits structurés | Région (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</fr/tools/ollama-search>) | Extraits structurés | \-- | Aucune pour les hôtes locaux connectés ; `OLLAMA_API_KEY` pour la recherche directe `https://ollama.com`  
[Perplexity](</fr/tools/perplexity-search>) | Extraits structurés | Pays, langue, période, domaines, limites de contenu | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</fr/tools/searxng-search>) | Extraits structurés | Catégories, langue | Aucune (auto-hébergé)  
[Tavily](</fr/tools/tavily>) | Extraits structurés | Via l’outil `tavily_search` | `TAVILY_API_KEY`  
  
## Détection automatique

## Recherche Web OpenAI native

Les modèles OpenAI Responses directs utilisent automatiquement l’outil `web_search` hébergé par OpenAI lorsque la recherche Web OpenClaw est activée et qu’aucun fournisseur géré n’est épinglé. Ce comportement appartient au fournisseur dans le plugin OpenAI groupé et ne s’applique qu’au trafic API OpenAI natif, pas aux URL de base de proxy compatibles OpenAI ni aux routes Azure. Définissez `tools.web.search.provider` sur un autre fournisseur tel que `brave` pour conserver l’outil `web_search` géré pour les modèles OpenAI, ou définissez `tools.web.search.enabled: false` pour désactiver à la fois la recherche gérée et la recherche OpenAI native.

## Recherche Web Codex native

Les modèles compatibles Codex peuvent éventuellement utiliser l’outil `web_search` Responses natif du fournisseur au lieu de la fonction `web_search` gérée par OpenClaw.

  * Configurez-la sous `tools.web.search.openaiCodex`
  * Elle ne s’active que pour les modèles compatibles Codex (`openai-codex/*` ou les fournisseurs utilisant `api: "openai-codex-responses"`)
  * Le `web_search` géré continue de s’appliquer aux modèles non Codex
  * `mode: "cached"` est le paramètre par défaut et recommandé
  * `tools.web.search.enabled: false` désactive à la fois la recherche gérée et la recherche native

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Si la recherche Codex native est activée mais que le modèle actuel n’est pas compatible Codex, OpenClaw conserve le comportement `web_search` géré normal.

## Sécurité réseau

Les appels au fournisseur `web_search` géré utilisent le chemin de récupération protégé d’OpenClaw. Pour les hôtes d’API de fournisseurs de confiance, OpenClaw autorise les réponses DNS fake-IP Surge, Clash et sing-box dans `198.18.0.0/15` et `fc00::/7` uniquement pour ce nom d’hôte de fournisseur. Les autres destinations privées, loopback, link-local et de métadonnées restent bloquées.

Cette autorisation automatique ne s’applique pas aux URL `web_fetch` arbitraires. Pour `web_fetch`, activez explicitement `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` et `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` uniquement lorsque votre proxy de confiance possède ces plages synthétiques.

## Configuration de la recherche Web

Les listes de fournisseurs dans la documentation et les flux de configuration sont alphabétiques. La détection automatique conserve un ordre de priorité distinct.

Si aucun `provider` n’est défini, OpenClaw vérifie les fournisseurs dans cet ordre et utilise le premier qui est prêt :

Fournisseurs adossés à une API d’abord :

  1. **Brave** \-- `BRAVE_API_KEY` ou `plugins.entries.brave.config.webSearch.apiKey` (ordre 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` ou `plugins.entries.minimax.config.webSearch.apiKey` (ordre 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY`, ou `models.providers.google.apiKey` (ordre 20)
  4. **Grok** \-- `XAI_API_KEY` ou `plugins.entries.xai.config.webSearch.apiKey` (ordre 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` ou `plugins.entries.moonshot.config.webSearch.apiKey` (ordre 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` ou `plugins.entries.perplexity.config.webSearch.apiKey` (ordre 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` ou `plugins.entries.firecrawl.config.webSearch.apiKey` (ordre 60)
  8. **Exa** \-- `EXA_API_KEY` ou `plugins.entries.exa.config.webSearch.apiKey` ; le `plugins.entries.exa.config.webSearch.baseUrl` facultatif remplace le point de terminaison Exa (ordre 65)
  9. **Tavily** \-- `TAVILY_API_KEY` ou `plugins.entries.tavily.config.webSearch.apiKey` (ordre 70)


Solutions de repli sans clé ensuite :

  10. **DuckDuckGo** \-- repli HTML sans clé, sans compte ni clé d’API (ordre 100)
  11. **Ollama Web Search** \-- repli sans clé via votre hôte Ollama local configuré lorsqu’il est joignable et connecté avec `ollama signin` ; peut réutiliser l’authentification bearer du fournisseur Ollama lorsque l’hôte en a besoin, et peut appeler la recherche directe `https://ollama.com` lorsqu’il est configuré avec `OLLAMA_API_KEY` (ordre 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` ou `plugins.entries.searxng.config.webSearch.baseUrl` (ordre 200)


Si aucun fournisseur n’est détecté, il se rabat sur Brave (vous obtiendrez une erreur de clé manquante vous invitant à en configurer une).

## Configuration

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

La configuration propre au fournisseur (clés API, URL de base, modes) se trouve sous `plugins.entries.<plugin>.config.webSearch.*`. Gemini peut aussi réutiliser `models.providers.google.apiKey` et `models.providers.google.baseUrl` comme solutions de repli de moindre priorité après sa configuration dédiée à la recherche web et `GEMINI_API_KEY`. Consultez les pages des fournisseurs pour des exemples.

`tools.web.search.provider` est validé par rapport aux identifiants de fournisseurs de recherche web déclarés par les manifestes des Plugins intégrés et installés. Une faute de frappe comme `"brvae"` fait échouer la validation de la configuration au lieu de revenir silencieusement à l’auto-détection. Si un fournisseur configuré ne dispose que d’indices de Plugin périmés, comme un bloc `plugins.entries.<plugin>` restant après la désinstallation d’un Plugin tiers, OpenClaw garde le démarrage résilient et signale un avertissement afin que vous puissiez réinstaller le Plugin ou exécuter `openclaw doctor --fix` pour nettoyer la configuration obsolète.

La sélection du fournisseur de repli `web_fetch` est distincte :

  * choisissez-le avec `tools.web.fetch.provider`
  * ou omettez ce champ et laissez OpenClaw détecter automatiquement le premier fournisseur web-fetch prêt à partir des identifiants disponibles
  * `web_fetch` hors bac à sable peut utiliser des fournisseurs de Plugins installés qui déclarent `contracts.webFetchProviders` ; les récupérations en bac à sable restent limitées aux fournisseurs intégrés
  * aujourd’hui, le fournisseur web-fetch intégré est Firecrawl, configuré sous `plugins.entries.firecrawl.config.webFetch.*`


Lorsque vous choisissez **Kimi** pendant `openclaw onboard` ou `openclaw configure --section web`, OpenClaw peut aussi demander :

  * la région de l’API Moonshot (`https://api.moonshot.ai/v1` ou `https://api.moonshot.cn/v1`)
  * le modèle de recherche web Kimi par défaut (par défaut `kimi-k2.6`)


Pour `x_search`, configurez `plugins.entries.xai.config.xSearch.*`. Il utilise le même profil d’authentification xAI que le chat, ou l’identifiant `XAI_API_KEY` / de recherche web du Plugin utilisé par la recherche web Grok. L’ancienne configuration `tools.web.x_search.*` est migrée automatiquement par `openclaw doctor --fix`. Lorsque vous choisissez Grok pendant `openclaw onboard` ou `openclaw configure --section web`, OpenClaw peut aussi proposer une configuration facultative de `x_search` avec la même clé. Il s’agit d’une étape de suivi distincte dans le parcours Grok, et non d’un choix séparé de fournisseur de recherche web de premier niveau. Si vous choisissez un autre fournisseur, OpenClaw n’affiche pas l’invite `x_search`.

### Stockage des clés API

### Fichier de configuration

Exécutez `openclaw configure --section web` ou définissez directement la clé :

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Variable d’environnement

Définissez la variable d’environnement du fournisseur dans l’environnement du processus Gateway :

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Pour une installation de Gateway, placez-la dans `~/.openclaw/.env`. Consultez [Variables d’environnement](</fr/help/faq#env-vars-and-env-loading>).

## Paramètres de l’outil

Paramètre | Description  
---|---  
`query` | Requête de recherche (obligatoire)  
`count` | Résultats à renvoyer (1-10, par défaut : 5)  
`country` | Code pays ISO à 2 lettres (p. ex. "US", "DE")  
`language` | Code de langue ISO 639-1 (p. ex. "en", "de")  
`search_lang` | Code de langue de recherche (Brave uniquement)  
`freshness` | Filtre temporel : `day`, `week`, `month` ou `year`  
`date_after` | Résultats après cette date (YYYY-MM-DD)  
`date_before` | Résultats avant cette date (YYYY-MM-DD)  
`ui_lang` | Code de langue de l’interface utilisateur (Brave uniquement)  
`domain_filter` | Tableau de liste d’autorisation/interdiction de domaines (Perplexity uniquement)  
`max_tokens` | Budget total de contenu, 25000 par défaut (Perplexity uniquement)  
`max_tokens_per_page` | Limite de jetons par page, 2048 par défaut (Perplexity uniquement)  
  
## x_search

`x_search` interroge les publications X (anciennement Twitter) avec xAI et renvoie des réponses synthétisées par l’IA avec citations. Il accepte les requêtes en langage naturel et des filtres structurés facultatifs. OpenClaw n’active l’outil `x_search` xAI intégré que sur la requête qui sert cet appel d’outil.

### Configuration de x_search

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` publie vers `<baseUrl>/responses` lorsque `plugins.entries.xai.config.xSearch.baseUrl` est défini. Si ce champ est omis, il se rabat sur `plugins.entries.xai.config.webSearch.baseUrl`, puis sur l’ancien `tools.web.search.grok.baseUrl`, et enfin sur le point de terminaison xAI public.

### Paramètres de x_search

Paramètre | Description  
---|---  
`query` | Requête de recherche (obligatoire)  
`allowed_x_handles` | Limiter les résultats à des handles X spécifiques  
`excluded_x_handles` | Exclure des handles X spécifiques  
`from_date` | Inclure uniquement les publications à cette date ou après (YYYY-MM-DD)  
`to_date` | Inclure uniquement les publications à cette date ou avant (YYYY-MM-DD)  
`enable_image_understanding` | Permettre à xAI d’inspecter les images jointes aux publications correspondantes  
`enable_video_understanding` | Permettre à xAI d’inspecter les vidéos jointes aux publications correspondantes  
  
### Exemple x_search

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Exemples

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Profils d’outils

Si vous utilisez des profils d’outils ou des listes d’autorisation, ajoutez `web_search`, `x_search` ou `group:web` :

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Associé

  * [Web Fetch](</fr/tools/web-fetch>) \-- récupérer une URL et extraire le contenu lisible
  * [Web Browser](</fr/tools/browser>) \-- automatisation complète du navigateur pour les sites fortement dépendants de JS
  * [Grok Search](</fr/tools/grok-search>) \-- Grok comme fournisseur `web_search`
  * [Ollama Web Search](</fr/tools/ollama-search>) \-- recherche web sans clé via votre hôte Ollama


Was this useful?YesNo