---
title: Claude Max API प्रॉक्सी
source_url: https://docs.openclaw.ai/hi/providers/claude-max-api-proxy
scraped_at: 2026-06-29
---

ModelsProviders

**claude-max-api-proxy** एक सामुदायिक टूल है जो आपकी Claude Max/Pro सदस्यता को OpenAI-संगत API एंडपॉइंट के रूप में उपलब्ध कराता है। इससे आप अपनी सदस्यता को OpenAI API फ़ॉर्मैट का समर्थन करने वाले किसी भी टूल के साथ उपयोग कर सकते हैं।

## इसका उपयोग क्यों करें?

दृष्टिकोण | लागत मार्ग | इनके लिए सर्वश्रेष्ठ  
---|---|---  
Anthropic API | Claude Console या क्लाउड के माध्यम से प्रति टोकन भुगतान | प्रोडक्शन ऐप्स, साझा ऑटोमेशन, अधिक मात्रा  
Claude सदस्यता प्रॉक्सी | Claude Code / `claude -p` योजना और क्रेडिट नियम | संगत टूल्स के साथ व्यक्तिगत प्रयोग  
  
यदि आपके पास Claude Max या Pro सदस्यता है और आप इसे OpenAI-संगत टूल्स के साथ उपयोग करना चाहते हैं, तो यह प्रॉक्सी कुछ व्यक्तिगत वर्कफ़्लो के लिए उपयुक्त हो सकता है। यह असीमित फ्लैट-रेट पथ नहीं है। प्रोडक्शन उपयोग के लिए API कुंजियाँ अब भी नीति और बिलिंग का अधिक स्पष्ट पथ हैं।

## यह कैसे काम करता है

CodeCopy code
[code]
    Your App → claude-max-api-proxy → Claude Code CLI / claude -p → Anthropic     (OpenAI format)              (converts format)          (uses your login)
[/code]

प्रॉक्सी:

  1. `http://localhost:3456/v1/chat/completions` पर OpenAI-फ़ॉर्मैट अनुरोध स्वीकार करता है
  2. उन्हें Claude Code CLI कमांड में बदलता है
  3. OpenAI फ़ॉर्मैट में प्रतिक्रियाएँ लौटाता है (स्ट्रीमिंग समर्थित)


## शुरू करना

* ### प्रॉक्सी इंस्टॉल करें

Node.js 22+ और Claude Code CLI आवश्यक हैं।

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### सर्वर शुरू करें

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### प्रॉक्सी का परीक्षण करें

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### OpenClaw कॉन्फ़िगर करें

OpenClaw को कस्टम OpenAI-संगत एंडपॉइंट के रूप में प्रॉक्सी की ओर इंगित करें:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## अंतर्निहित कैटलॉग

मॉडल ID | इससे मैप होता है  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## उन्नत कॉन्फ़िगरेशन

प्रॉक्सी-शैली OpenAI-संगत नोट्स

यह पथ अन्य कस्टम `/v1` बैकएंड की तरह उसी प्रॉक्सी-शैली OpenAI-संगत रूट का उपयोग करता है:

  * केवल नेटिव OpenAI अनुरोध आकार देना लागू नहीं होता
  * कोई `service_tier` नहीं, कोई Responses `store` नहीं, कोई प्रॉम्प्ट-कैश संकेत नहीं, और कोई OpenAI reasoning-compat पेलोड आकार देना नहीं
  * छिपे हुए OpenClaw एट्रिब्यूशन हेडर (`originator`, `version`, `User-Agent`) प्रॉक्सी URL पर इंजेक्ट नहीं किए जाते

LaunchAgent के साथ macOS पर स्वतः शुरू करें

प्रॉक्सी को स्वचालित रूप से चलाने के लिए LaunchAgent बनाएँ:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## नोट्स

  * यह एक **सामुदायिक टूल** है, Anthropic या OpenClaw द्वारा आधिकारिक रूप से समर्थित नहीं
  * Claude Code CLI प्रमाणित होने के साथ सक्रिय Claude Max/Pro सदस्यता आवश्यक है
  * Claude Code `claude -p` बिलिंग, उपयोग-क्रेडिट, और दर-सीमा व्यवहार विरासत में लेता है
  * प्रॉक्सी स्थानीय रूप से चलता है और किसी तृतीय-पक्ष सर्वर को डेटा नहीं भेजता
  * स्ट्रीमिंग प्रतिक्रियाएँ पूरी तरह समर्थित हैं


## संबंधित

[**Anthropic प्रदाता** Claude CLI या API कुंजियों के साथ नेटिव OpenClaw इंटीग्रेशन। ](</hi/providers/anthropic>) [**OpenAI प्रदाता** OpenAI/Codex सदस्यताओं के लिए। ](</hi/providers/openai>) [**मॉडल चयन** सभी प्रदाताओं, मॉडल संदर्भों, और फ़ेलओवर व्यवहार का अवलोकन। ](</hi/concepts/model-providers>) [**कॉन्फ़िगरेशन** पूरा कॉन्फ़िग संदर्भ। ](</hi/gateway/configuration>)

Was this useful?YesNo

Open issue