---
title: وكيل Claude Max API
source_url: https://docs.openclaw.ai/ar/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** هي أداة مجتمعية تكشف اشتراك Claude Max/Pro الخاص بك كنقطة نهاية API متوافقة مع OpenAI. يتيح لك ذلك استخدام اشتراكك مع أي أداة تدعم تنسيق OpenAI API.

## لماذا تستخدم هذا؟

النهج | التكلفة | الأفضل لـ  
---|---|---  
Anthropic API | الدفع لكل رمز (~$15/M للإدخال، $75/M للإخراج لـ Opus) | تطبيقات الإنتاج، الأحجام الكبيرة  
اشتراك Claude Max | $200/شهر ثابتة | الاستخدام الشخصي، التطوير، الاستخدام غير المحدود  
  
إذا كان لديك اشتراك Claude Max وتريد استخدامه مع أدوات متوافقة مع OpenAI، فقد يقلل هذا الوكيل التكلفة لبعض سير العمل. وتظل مفاتيح API هي المسار الأوضح من ناحية السياسة للاستخدام الإنتاجي.

## كيف يعمل

CodeCopy code
[code]
    Your App → claude-max-api-proxy → Claude Code CLI → Anthropic (via subscription)     (OpenAI format)              (converts format)      (uses your login)
[/code]

يقوم الوكيل بما يلي:

  1. يقبل الطلبات بتنسيق OpenAI عند `http://localhost:3456/v1/chat/completions`
  2. يحولها إلى أوامر Claude Code CLI
  3. يعيد الاستجابات بتنسيق OpenAI ‏(مع دعم البث)


## البدء

* ### تثبيت الوكيل

يتطلب Node.js 20+ وClaude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### بدء الخادم

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### اختبار الوكيل

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### إعداد OpenClaw

وجّه OpenClaw إلى الوكيل كنقطة نهاية مخصصة متوافقة مع OpenAI:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## الكتالوج المضمّن

معرّف النموذج | يربط إلى  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## إعداد متقدم

ملاحظات التوافق مع OpenAI على نمط الوكيل

يستخدم هذا المسار الطريق نفسه على نمط الوكيل المتوافق مع OpenAI كما في الواجهات الخلفية المخصصة الأخرى عند `/v1`:

  * لا ينطبق تشكيل الطلبات الأصلي الخاص بـ OpenAI فقط
  * لا يوجد `service_tier`، ولا `store` في Responses، ولا تلميحات prompt-cache، ولا تشكيل حمولة التوافق الخاصة بالتفكير في OpenAI
  * لا يتم حقن رؤوس الإسناد المخفية الخاصة بـ OpenClaw ‏(`originator`, `version`, `User-Agent`) على عنوان URL الخاص بالوكيل

البدء التلقائي على macOS باستخدام LaunchAgent

أنشئ LaunchAgent لتشغيل الوكيل تلقائيًا:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## الروابط

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **المشكلات:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## ملاحظات

  * هذه **أداة مجتمعية** ، وليست مدعومة رسميًا من Anthropic أو OpenClaw
  * تتطلب اشتراك Claude Max/Pro نشطًا مع Claude Code CLI موثَّقة
  * يعمل الوكيل محليًا ولا يرسل البيانات إلى أي خوادم طرف ثالث
  * الاستجابات المتدفقة مدعومة بالكامل


## ذو صلة

[**موفر Anthropic** تكامل OpenClaw أصلي مع Claude CLI أو مفاتيح API. ](</ar/providers/anthropic>) [**موفر OpenAI** لاشتراكات OpenAI/Codex. ](</ar/providers/openai>) [**اختيار النموذج** نظرة عامة على جميع الموفّرين ومراجع النماذج وسلوك failover. ](</ar/concepts/model-providers>) [**الإعداد** مرجع الإعدادات الكامل. ](</ar/gateway/configuration>)

Was this useful?YesNo