---
title: आतिशबाज़ी
source_url: https://docs.openclaw.ai/hi/providers/fireworks
scraped_at: 2026-06-29
---

ModelsProviders

[Fireworks](<https://fireworks.ai>) OpenAI-संगत API के माध्यम से open-weight और routed मॉडल उपलब्ध कराता है। दो पूर्व-कैटलॉग किए गए Kimi मॉडल और runtime पर किसी भी Fireworks मॉडल या router id का उपयोग करने के लिए आधिकारिक Fireworks provider plugin इंस्टॉल करें।

गुण | मान  
---|---  
Provider id | `fireworks` (उपनाम: `fireworks-ai`)  
Package | `@openclaw/fireworks-provider`  
Auth env var | `FIREWORKS_API_KEY`  
Onboarding flag | `--auth-choice fireworks-api-key`  
Direct CLI flag | `--fireworks-api-key <key>`  
API | OpenAI-संगत (`openai-completions`)  
Base URL | `https://api.fireworks.ai/inference/v1`  
डिफ़ॉल्ट मॉडल | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
डिफ़ॉल्ट उपनाम | `Kimi K2.5 Turbo`  
  
## शुरुआत करना

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/fireworks-provider
[/code]

* ### Set the Fireworks API key

ऑनबोर्डिंगCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

सीधा फ़्लैगCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

केवल EnvCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Onboarding आपके auth profiles में `fireworks` provider के लिए key संग्रहीत करता है और **Fire Pass** Kimi K2.5 Turbo router को डिफ़ॉल्ट मॉडल के रूप में सेट करता है।

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

सूची में `Kimi K2.6` और `Kimi K2.5 Turbo (Fire Pass)` शामिल होने चाहिए। यदि `FIREWORKS_API_KEY` हल नहीं होता, तो `openclaw models status --json` अनुपलब्ध credential को `auth.unusableProfiles` के अंतर्गत रिपोर्ट करता है।

## Non-interactive सेटअप

स्क्रिप्टेड या CI इंस्टॉल के लिए, सब कुछ command line पर पास करें:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## अंतर्निहित catalog

Model ref | नाम | इनपुट | Context | अधिकतम आउटपुट | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | पाठ + छवि | 262,144 | 262,144 | जबरन बंद  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | पाठ + छवि | 256,000 | 256,000 | जबरन बंद (डिफ़ॉल्ट)  
  
## Custom Fireworks model ids

OpenClaw runtime पर किसी भी Fireworks मॉडल या router id को स्वीकार करता है। Fireworks द्वारा दिखाया गया सटीक id उपयोग करें और उसके आगे `fireworks/` prefix लगाएं। Dynamic resolution Fire Pass template (पाठ + छवि इनपुट, OpenAI-संगत API, डिफ़ॉल्ट cost zero) को clone करता है और जब id Kimi pattern से मेल खाता है, तो thinking को अपने-आप बंद कर देता है। GLM dynamic ids को text-only के रूप में चिह्नित किया जाता है, जब तक आप image input के साथ custom model entry configure नहीं करते।

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

How model id prefixing works

OpenClaw में हर Fireworks model ref `fireworks/` से शुरू होता है, जिसके बाद Fireworks platform से सटीक id या router path आता है। उदाहरण के लिए:

  * Router model: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Direct model: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw API request बनाते समय `fireworks/` prefix हटा देता है और शेष path को OpenAI-संगत `model` field के रूप में Fireworks endpoint पर भेजता है।

Why thinking is forced off for Kimi

यदि request में `reasoning_*` parameters होते हैं, तो Fireworks K2.6 400 लौटाता है, भले ही Kimi Moonshot की अपनी API के माध्यम से thinking का समर्थन करता हो। provider policy (`extensions/fireworks/thinking-policy.ts`) Kimi model ids के लिए केवल `off` thinking level घोषित करती है, इसलिए manual `/think` switches और provider-policy surfaces runtime contract के साथ संरेखित रहते हैं।

Kimi reasoning को end-to-end उपयोग करने के लिए, [Moonshot provider](</hi/providers/moonshot>) configure करें और उसी मॉडल को उसके माध्यम से route करें।

Environment availability for the daemon

यदि Gateway किसी managed service (launchd, systemd, Docker) के रूप में चलता है, तो Fireworks key उस process को दिखाई देनी चाहिए — केवल आपके interactive shell को नहीं।

macOS पर, `openclaw gateway install` पहले से ही `~/.openclaw/.env` को LaunchAgent environment file में wire करता है। key rotate करने के बाद install फिर से चलाएं (या `openclaw doctor --fix`)।

## संबंधित

[**Model providers** providers, model refs, और failover behavior चुनना। ](</hi/concepts/model-providers>) [**Thinking modes** `/think` levels, provider policies, और reasoning-सक्षम मॉडलों की routing। ](</hi/tools/thinking>) [**Moonshot** Moonshot की अपनी API के माध्यम से native thinking output के साथ Kimi चलाएं। ](</hi/providers/moonshot>) [**Troubleshooting** सामान्य troubleshooting और FAQ। ](</hi/help/troubleshooting>)

Was this useful?YesNo

Open issue