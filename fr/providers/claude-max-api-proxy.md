---
title: Proxy API Claude Max
source_url: https://docs.openclaw.ai/fr/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** est un outil communautaire qui expose votre abonnement Claude Max/Pro comme un point de terminaison API compatible OpenAI. Cela vous permet d’utiliser votre abonnement avec n’importe quel outil prenant en charge le format API OpenAI.

## Pourquoi l’utiliser ?

Approche | Coût | Meilleur usage  
---|---|---  
API Anthropic | Paiement au token (~15 $/M en entrée, 75 $/M en sortie pour Opus) | Applications de production, gros volume  
Abonnement Claude Max | 200 $/mois forfaitaire | Usage personnel, développement, usage illimité  
  
Si vous avez un abonnement Claude Max et souhaitez l’utiliser avec des outils compatibles OpenAI, ce proxy peut réduire les coûts pour certains workflows. Les clés API restent le chemin de politique le plus clair pour un usage de production.

## Fonctionnement

CodeCopy code
[code]
    Votre app → claude-max-api-proxy → Claude Code CLI → Anthropic (via abonnement)   (format OpenAI)              (convertit le format)         (utilise votre connexion)
[/code]

Le proxy :

  1. Accepte des requêtes au format OpenAI sur `http://localhost:3456/v1/chat/completions`
  2. Les convertit en commandes Claude Code CLI
  3. Renvoie des réponses au format OpenAI (streaming pris en charge)


## Démarrage

* ### Installer le proxy

Nécessite Node.js 20+ et Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### Démarrer le serveur

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### Tester le proxy

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Configurer OpenClaw

Faites pointer OpenClaw vers le proxy comme point de terminaison personnalisé compatible OpenAI :

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Catalogue intégré

ID de modèle | Correspond à  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Configuration avancée

Remarques sur le style proxy compatible OpenAI

Ce chemin utilise la même route compatible OpenAI de style proxy que d’autres backends `/v1` personnalisés :

  * La mise en forme des requêtes réservée à OpenAI natif ne s’applique pas
  * Pas de `service_tier`, pas de `store` pour Responses, pas d’indices de cache de prompt, ni de mise en forme de charge utile de compatibilité de raisonnement OpenAI
  * Les en-têtes d’attribution cachés d’OpenClaw (`originator`, `version`, `User-Agent`) ne sont pas injectés sur l’URL du proxy

Démarrage automatique sur macOS avec LaunchAgent

Créez un LaunchAgent pour exécuter automatiquement le proxy :

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Liens

  * **npm :** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub :** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues :** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Remarques

  * Il s’agit d’un **outil communautaire** , non officiellement pris en charge par Anthropic ni par OpenClaw
  * Nécessite un abonnement Claude Max/Pro actif avec Claude Code CLI authentifié
  * Le proxy s’exécute localement et n’envoie aucune donnée à des serveurs tiers
  * Les réponses en streaming sont entièrement prises en charge


## Lié

[**Provider Anthropic** Intégration OpenClaw native avec Claude CLI ou des clés API. ](</fr/providers/anthropic>) [**Provider OpenAI** Pour les abonnements OpenAI/Codex. ](</fr/providers/openai>) [**Sélection de modèle** Vue d’ensemble de tous les providers, références de modèle et comportement de repli. ](</fr/concepts/model-providers>) [**Configuration** Référence complète de la configuration. ](</fr/gateway/configuration>)

Was this useful?YesNo