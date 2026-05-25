---
title: Claude Max API proxy'si
source_url: https://docs.openclaw.ai/tr/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** , Claude Max/Pro aboneliğinizi OpenAI uyumlu bir API uç noktası olarak açığa çıkaran topluluk yapımı bir araçtır. Bu, OpenAI API biçimini destekleyen herhangi bir araçla aboneliğinizi kullanmanıza olanak tanır.

## Bunu neden kullanmalı?

Yaklaşım | Maliyet | En uygun olduğu kullanım  
---|---|---  
Anthropic API | Belirteç başına ödeme (~Opus için girişte $15/M, çıkışta $75/M) | Üretim uygulamaları, yüksek hacim  
Claude Max aboneliği | Aylık sabit $200 | Kişisel kullanım, geliştirme, sınırsız kullanım  
  
Claude Max aboneliğiniz varsa ve bunu OpenAI uyumlu araçlarla kullanmak istiyorsanız, bu proxy bazı iş akışlarında maliyeti azaltabilir. Üretimde kullanım için API anahtarları daha net ilke yoludur.

## Nasıl çalışır

CodeCopy code
[code]
    Uygulamanız → claude-max-api-proxy → Claude Code CLI → Anthropic (abonelik üzerinden)   (OpenAI biçimi)                  (biçimi dönüştürür)      (oturumunuzu kullanır)
[/code]

Bu proxy:

  1. `http://localhost:3456/v1/chat/completions` adresinde OpenAI biçimindeki istekleri kabul eder
  2. Bunları Claude Code CLI komutlarına dönüştürür
  3. Yanıtları OpenAI biçiminde döndürür (akış desteklenir)


## Başlangıç

* ### Proxy'yi kurun

Node.js 20+ ve Claude Code CLI gerektirir.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Claude CLI'nin kimlik doğrulamasının yapıldığını doğrulayınclaude --version
[/code]

* ### Sunucuyu başlatın

bashCopy code
[code]
    claude-max-api# Sunucu http://localhost:3456 adresinde çalışır
[/code]

* ### Proxy'yi test edin

bashCopy code
[code]
    # Sağlık denetimicurl http://localhost:3456/health # Modelleri listelecurl http://localhost:3456/v1/models # Sohbet tamamlamacurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### OpenClaw'ı yapılandırın

OpenClaw'ı özel OpenAI uyumlu bir uç nokta olarak proxy'ye yönlendirin:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Yerleşik katalog

Model Kimliği | Eşlendiği şey  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Gelişmiş yapılandırma

Proxy tarzı OpenAI uyumlu notlar

Bu yol, diğer özel `/v1` arka uçlarıyla aynı proxy tarzı OpenAI uyumlu rotayı kullanır:

  * Yerel yalnızca OpenAI istek şekillendirmesi uygulanmaz
  * `service_tier` yok, Responses `store` yok, istem önbelleği ipuçları yok ve OpenAI muhakeme uyumluluğu payload şekillendirmesi yok
  * Gizli OpenClaw atıf başlıkları (`originator`, `version`, `User-Agent`) proxy URL'sine enjekte edilmez

macOS'ta LaunchAgent ile otomatik başlatma

Proxy'yi otomatik çalıştırmak için bir LaunchAgent oluşturun:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Bağlantılar

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Sorunlar:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Notlar

  * Bu bir **topluluk aracı** dır; Anthropic veya OpenClaw tarafından resmi olarak desteklenmez
  * Claude Code CLI kimlik doğrulaması yapılmış etkin bir Claude Max/Pro aboneliği gerektirir
  * Proxy yerelde çalışır ve verileri herhangi bir üçüncü taraf sunucuya göndermez
  * Akışlı yanıtlar tam olarak desteklenir


## İlgili

[**Anthropic sağlayıcısı** Claude CLI veya API anahtarlarıyla yerel OpenClaw entegrasyonu. ](</tr/providers/anthropic>) [**OpenAI sağlayıcısı** OpenAI/Codex abonelikleri için. ](</tr/providers/openai>) [**Model seçimi** Tüm sağlayıcılar, model başvuruları ve yük devretme davranışına genel bakış. ](</tr/concepts/model-providers>) [**Yapılandırma** Tam yapılandırma başvurusu. ](</tr/gateway/configuration>)

Was this useful?YesNo