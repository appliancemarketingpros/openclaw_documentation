---
title: Proxy de API Claude Max
source_url: https://docs.openclaw.ai/pt-BR/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** é uma ferramenta da comunidade que expõe sua assinatura Claude Max/Pro como um endpoint de API compatível com OpenAI. Isso permite usar sua assinatura com qualquer ferramenta que suporte o formato da API OpenAI.

## Por que usar isso?

Abordagem | Custo | Melhor para  
---|---|---  
API Anthropic | Pagamento por token (~$15/M entrada, $75/M saída para Opus) | Apps de produção, alto volume  
Assinatura Claude Max | $200/mês fixos | Uso pessoal, desenvolvimento, uso ilimitado  
  
Se você tem uma assinatura Claude Max e quer usá-la com ferramentas compatíveis com OpenAI, esse proxy pode reduzir o custo em alguns fluxos de trabalho. Chaves de API continuam sendo o caminho de política mais claro para uso em produção.

## Como funciona

CodeCopy code
[code]
    Seu app → claude-max-api-proxy → Claude Code CLI → Anthropic (via assinatura)   (formato OpenAI)             (converte o formato)    (usa seu login)
[/code]

O proxy:

  1. Aceita solicitações em formato OpenAI em `http://localhost:3456/v1/chat/completions`
  2. Converte essas solicitações em comandos da CLI do Claude Code
  3. Retorna respostas em formato OpenAI (com suporte a streaming)


## Primeiros passos

* ### Install the proxy

Requer Node.js 20+ e Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### Start the server

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### Test the proxy

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Configure OpenClaw

Aponte o OpenClaw para o proxy como um endpoint personalizado compatível com OpenAI:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Catálogo integrado

ID do modelo | Mapeia para  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Configuração avançada

Observações sobre proxies compatíveis com OpenAI

Este caminho usa a mesma rota compatível com OpenAI em estilo proxy que outros backends personalizados `/v1`:

  * O formato nativo de solicitação exclusivo da OpenAI não se aplica
  * Sem `service_tier`, sem `store` do Responses, sem dicas de cache de prompt e sem modelagem de payload de compatibilidade de raciocínio da OpenAI
  * Cabeçalhos ocultos de atribuição do OpenClaw (`originator`, `version`, `User-Agent`) não são injetados na URL do proxy

Inicialização automática no macOS com LaunchAgent

Crie um LaunchAgent para executar o proxy automaticamente:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Links

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Observações

  * Esta é uma **ferramenta da comunidade** , sem suporte oficial da Anthropic nem do OpenClaw
  * Requer uma assinatura ativa Claude Max/Pro com Claude Code CLI autenticado
  * O proxy é executado localmente e não envia dados para servidores de terceiros
  * Respostas em streaming têm suporte completo


## Relacionado

[**Anthropic provider** Integração nativa do OpenClaw com Claude CLI ou chaves de API. ](</pt-BR/providers/anthropic>) [**OpenAI provider** Para assinaturas OpenAI/Codex. ](</pt-BR/providers/openai>) [**Model selection** Visão geral de todos os provedores, refs de modelo e comportamento de fallback. ](</pt-BR/concepts/model-providers>) [**Configuration** Referência completa de configuração. ](</pt-BR/gateway/configuration>)

Was this useful?YesNo