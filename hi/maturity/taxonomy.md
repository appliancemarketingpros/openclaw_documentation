---
title: परिपक्वता वर्गीकरण
source_url: https://docs.openclaw.ai/hi/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# परिपक्वता वर्गीकरण

स्कोरकार्ड के पीछे का मॉडल

सतहें > श्रेणियां > क्षमताएं > प्रमाण।

50 सतहें 4 परिवारों में समूहित हैं, और हर श्रेणी कैनोनिकल दस्तावेज़ों और QA कवरेज IDs से जुड़ी है।

उत्पाद क्षेत्रों को ब्राउज़ करें / विस्तृत वर्गीकरण खोलें / [स्कोर देखें](</hi/maturity/scorecard>)

## इस पृष्ठ को कैसे पढ़ें

सतह Gateway रनटाइम, Discord, या macOS ऐप जैसा कोई उत्पाद क्षेत्र है। प्रत्येक सतह में श्रेणियां होती हैं, और प्रत्येक श्रेणी में क्षमता-स्तर की वे जांचें होती हैं जिन्हें QA परिदृश्य कवर करते हैं। रिलीज़-स्तर के निर्णय के लिए स्कोरकार्ड का उपयोग करें; इसके नीचे के मॉडल का निरीक्षण करने के लिए इस पृष्ठ का उपयोग करें।

## परिपक्वता स्तर

M0नियोजितदिशा ज्ञात है, लेकिन कोई समर्थित उपयोगकर्ता पथ मौजूद नहीं है।प्रमोशन: डिज़ाइन इश्यू, स्वामी, और लक्षित सतह मौजूद हैं।

M1प्रयोगात्मकसावधानियों, फ्लैग, स्रोत बिल्ड, या केवल मेंटेनर प्रवाहों के पीछे लागू किया गया।प्रमोशन: मेंटेनर वर्तमान main से परिदृश्य चला सकता है।

M2अल्फ़ावास्तविक उपयोगकर्ता इसे आज़मा सकते हैं, लेकिन ब्रेकिंग बदलाव और अधूरा UX अपेक्षित हैं।प्रमोशन: प्रलेखित सेटअप, बुनियादी परीक्षण, ज्ञात सावधानियां, और कम से कम एक वास्तविक-परिवेश प्रमाण।

M3बीटासार्वजनिक पथ मौजूद है और मुख्य वर्कफ़्लो सीमित सावधानियों के साथ उपयोग करने योग्य है।प्रमोशन: इंस्टॉल/अपडेट दस्तावेज़, रिग्रेशन परीक्षण, सपोर्ट रनबुक, और अपेक्षित परिवेश में सफल परिदृश्य प्रमाण।

M4स्थिरसामान्य उपयोगकर्ताओं के लिए अनुशंसित पथ। विफलताओं को रिग्रेशन माना जाता है।प्रमोशन: रिलीज़ गेट, डॉक्टर/समस्या-निवारण पथ, विस्तृत दस्तावेज़, और दोहराया गया वास्तविक-विश्व प्रमाण।

M5क्लॉसमपरिष्कृत, आनंददायक, अच्छी तरह इंस्ट्रूमेंटेड, और सर्वोत्तम तुलनीय वर्कफ़्लो के साथ प्रतिस्पर्धी।प्रमोशन: स्थिर के साथ प्रतिनिधि उपयोगकर्ताओं में उपयोगकर्ता स्कोरकार्ड पास।

## उत्पाद क्षेत्र

### मुख्य

CLI M4स्थिर7 क्षेत्र - 90% पूर्ण Gateway रनटाइम M4स्थिर13 क्षेत्र - 89% पूर्ण एजेंट रनटाइम M3बीटा9 क्षेत्र - 79% पूर्ण सेशन, मेमोरी, और संदर्भ इंजन M3बीटा9 क्षेत्र - 79% पूर्ण चैनल फ्रेमवर्क M3बीटा8 क्षेत्र - 79% पूर्ण अवलोकनीयता M3बीटा5 क्षेत्र - 79% पूर्ण Gateway वेब ऐप M3बीटा6 क्षेत्र - 79% पूर्ण Plugins M3Beta9 क्षेत्र - 79% पूर्ण सुरक्षा, प्रमाणीकरण, पेयरिंग, और सीक्रेट्स M3Beta6 क्षेत्र - 79% पूर्ण ऑटोमेशन: Cron, हुक्स, टास्क, पोलिंग M3Beta6 क्षेत्र - 79% पूर्ण मीडिया समझ और मीडिया जनरेशन M2Alpha6 क्षेत्र - 68% पूर्ण वॉइस और रियलटाइम बातचीत M2Alpha6 क्षेत्र - 68% पूर्ण TUI M2Alpha5 क्षेत्र - 66% पूर्ण ClawHub M2Alpha4 क्षेत्र - 62% पूर्ण OpenClaw ऐप SDK M2Alpha6 क्षेत्र - 53% पूर्ण

### प्लेटफ़ॉर्म

Linux Gateway होस्ट M4स्थिर5 क्षेत्र - 89% पूर्ण macOS Gateway होस्ट M4स्थिर7 क्षेत्र - 88% पूर्ण Docker और Podman होस्टिंग M3Beta4 क्षेत्र - 79% पूर्ण WSL2 के माध्यम से Windows M3Beta6 क्षेत्र - 79% पूर्ण Raspberry Pi और छोटे Linux डिवाइस M3Beta4 क्षेत्र - 79% पूर्ण macOS कंपैनियन ऐप M3Beta8 क्षेत्र - 78% पूर्ण Android ऐप M2Alpha7 क्षेत्र - 66% पूर्ण Native Windows M2Alpha4 क्षेत्र - 66% पूर्ण Kubernetes होस्टिंग M2Alpha4 क्षेत्र - 61% पूर्ण iOS ऐप M1Experimental8 क्षेत्र - 44% पूर्ण Nix इंस्टॉल पथ M1Experimental5 क्षेत्र - 44% पूर्ण watchOS companion सतहें M1Experimental5 क्षेत्र - 44% पूर्ण Linux companion ऐप M0Planned5 क्षेत्र - 21% पूर्ण Native Windows companion ऐप M0Planned5 क्षेत्र - 21% पूर्ण

### चैनल

Discord M4Stable6 क्षेत्र - 87% पूर्ण Telegram M3Beta5 क्षेत्र - 78% पूर्ण Slack M3Beta5 क्षेत्र - 78% पूर्ण iMessage और BlueBubbles M3Beta5 क्षेत्र - 78% पूर्ण WhatsApp M3Beta5 क्षेत्र - 78% पूर्ण Matrix M2Alpha6 क्षेत्र - 67% पूर्ण Google Chat M2Alpha5 क्षेत्र - 66% पूर्ण Microsoft Teams M2Alpha5 क्षेत्र - 66% पूर्ण Signal M2Alpha5 क्षेत्र - 66% पूर्ण Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, क्षेत्रीय चैनल M2Alpha4 क्षेत्र - 58% पूर्ण Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 क्षेत्र - 54% पूर्ण वॉइस कॉल चैनल M1Experimental5 क्षेत्र - 44% पूर्ण

### प्रदाता और टूल

ब्राउज़र ऑटोमेशन, exec, और sandbox टूल M3Beta3 क्षेत्र - 79% पूर्ण OpenAI और Codex प्रदाता पथ M3Beta5 क्षेत्र - 79% पूर्ण वेब खोज टूल M3Beta4 क्षेत्र - 79% पूर्ण Anthropic प्रदाता पथ M3Beta5 क्षेत्र - 78% पूर्ण Google प्रदाता पथ M3Beta5 क्षेत्र - 78% पूर्ण OpenRouter प्रदाता पथ M3Beta4 क्षेत्र - 78% पूर्ण छवि, वीडियो, और संगीत जनरेशन टूल M2Alpha5 क्षेत्र - 68% पूर्ण स्थानीय मॉडल प्रदाता: Ollama, vLLM, SGLang, LM Studio M2Alpha5 क्षेत्र - 68% पूर्ण लॉन्ग-टेल होस्टेड प्रदाता M2Alpha3 क्षेत्र - 68% पूर्ण

## विवरण

### कोर

CLI - M4 Stable - 7 क्षेत्र

सामान्य सेटअप और मरम्मत पथ इंस्टॉल, CLI, और Gateway दस्तावेज़ों में दस्तावेजीकृत हैं। प्लेटफ़ॉर्म-विशिष्ट Windows पथ Windows via WSL2 और Native Windows पंक्तियों में ट्रैक किए जाते हैं।

कवरेज Experimental - 4%गुणवत्ता Stable - 83%पूर्णता Stable - 90%आंशिक - 6

CLI सेटअप 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक17%

स्थिर89%

स्थिर90%

[अनुक्रमणिका](</hi/install>), [इंस्टॉलर](</hi/install/installer>), [Node](</hi/install/node>), [अपडेट करना](</hi/install/updating>)

ऑनबोर्डिंग और प्रमाणीकरण सेटअप 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[ऑनबोर्ड](</hi/cli/onboard>), [कॉन्फ़िगर करें](</hi/cli/configure>), [ऑनबोर्डिंग अवलोकन](</hi/start/onboarding-overview>)

Plugin और चैनल सेटअप 5 क्षमताएँ

प्रायोगिक0%

बीटा75%

स्थिर89%

[ऑनबोर्ड](</hi/cli/onboard>), [Plugins](</hi/cli/plugins>), [चैनल](</hi/cli/channels>)

Gateway सेवा प्रबंधन 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक14%

स्थिर87%

स्थिर90%

[Gateway](</hi/cli/gateway>), [अपडेट करना](</hi/install/updating>), [समस्या निवारण](</hi/gateway/troubleshooting>)

CLI अवलोकनीयता 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

स्थिर89%

स्थिर90%

[स्थिति](</hi/cli/status>), [स्वास्थ्य](</hi/cli/health>), [लॉग](</hi/cli/logs>), [निदान](</hi/gateway/diagnostics>)

डॉक्टर 10 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

स्थिर89%

स्थिर90%

[डॉक्टर](</hi/cli/doctor>), [डॉक्टर](</hi/gateway/doctor>), [सीक्रेट्स](</hi/gateway/secrets>), [समस्या निवारण](</hi/gateway/troubleshooting>)

अपडेट और अपग्रेड 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[अपडेट करना](</hi/install/updating>), [अपडेट](</hi/cli/update>), [समस्या निवारण](</hi/gateway/troubleshooting>)

Gateway runtime - M4 Stable - 13 areas

कोर आर्किटेक्चर, प्रमाणीकरण, पेयरिंग, प्रोटोकॉल दस्तावेज़, डेमन दस्तावेज़ और CLI रनबुक व्यापक और अद्यतन हैं।

कवरेज प्रायोगिक - 6%गुणवत्ता स्थिर - 81%पूर्णता स्थिर - 89%आंशिक - 12

अनुमोदन और दूरस्थ निष्पादन 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[प्रोटोकॉल](</hi/gateway/protocol>), [अनुक्रमणिका](</hi/gateway/security>)

HTTP API 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक25%

स्थिर90%

स्थिर90%

[अनुक्रमणिका](</hi/gateway>), [Openai HTTP API](</hi/gateway/openai-http-api>), [Openresponses HTTP API](</hi/gateway/openresponses-http-api>), [Tools Invoke HTTP API](</hi/gateway/tools-invoke-http-api>), [हुक](</hi/automation/hooks>), [अनुक्रमणिका](</hi/web>)

होस्टेड वेब सतह 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

स्थिर89%

स्थिर90%

[अनुक्रमणिका](</hi/gateway>), [आर्किटेक्चर](</hi/concepts/architecture>), [Control UI](</hi/web/control-ui>), [Webchat](</hi/web/webchat>), [कैनवास](</hi/refactor/canvas>)

Gateway RPC API और इवेंट 20 क्षमताएँ / LTS-समर्थित

प्रायोगिक9%

स्थिर90%

स्थिर90%

[प्रोटोकॉल](</hi/gateway/protocol>), [अनुक्रमणिका](</hi/gateway>), [आर्किटेक्चर](</hi/concepts/architecture>)

डिवाइस प्रमाणीकरण और पेयरिंग 10 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[प्रोटोकॉल](</hi/gateway/protocol>), [पेयरिंग](</hi/gateway/pairing>), [अनुक्रमणिका](</hi/gateway/security>)

नेटवर्क एक्सेस और डिस्कवरी 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[अनुक्रमणिका](</hi/gateway>), [डिस्कवरी](</hi/gateway/discovery>), [प्रोटोकॉल](</hi/gateway/protocol>)

Node और दूरस्थ क्षमताएँ 8 क्षमताएँ

प्रायोगिक0%

बीटा75%

स्थिर89%

[प्रोटोकॉल](</hi/gateway/protocol>), [आर्किटेक्चर](</hi/concepts/architecture>), [अनुक्रमणिका](</hi/nodes>)

स्वास्थ्य, डायग्नॉस्टिक्स, और मरम्मत 7 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[अनुक्रमणिका](</hi/gateway>), [निदान](</hi/gateway/diagnostics>), [Doctor](</hi/gateway/doctor>)

प्रोटोकॉल संगतता 7 क्षमताएँ / LTS-समर्थित

प्रयोगात्मक0%

बीटा75%

स्थिर89%

[प्रोटोकॉल](</hi/gateway/protocol>), [वास्तुकला](</hi/concepts/architecture>), [Typebox](</hi/concepts/typebox>), [ब्रिज प्रोटोकॉल](</hi/gateway/bridge-protocol>)

भूमिकाएँ और अनुमतियाँ 5 क्षमताएँ / LTS-समर्थित

प्रयोगात्मक0%

बीटा75%

स्थिर89%

[प्रोटोकॉल](</hi/gateway/protocol>), [अनुक्रमणिका](</hi/gateway/security>)

Gateway जीवनचक्र 7 क्षमताएँ / LTS-समर्थित

प्रयोगात्मक33%

स्थिर90%

स्थिर90%

[अनुक्रमणिका](</hi/gateway>), [वास्तुकला](</hi/concepts/architecture>)

सुरक्षा नियंत्रण 6 क्षमताएँ / LTS-समर्थित

प्रयोगात्मक0%

बीटा75%

स्थिर89%

[अनुक्रमणिका](</hi/gateway/security>), [प्रोटोकॉल](</hi/gateway/protocol>), [डिस्कवरी](</hi/gateway/discovery>)

WebSocket कनेक्शन 8 क्षमताएँ / LTS-समर्थित

प्रयोगात्मक13%

स्थिर90%

स्थिर90%

[प्रोटोकॉल](</hi/gateway/protocol>), [वास्तुकला](</hi/concepts/architecture>)

एजेंट रनटाइम - M3 बीटा - 9 क्षेत्र

मुख्य लूप, मॉडल, प्रदाता रूटिंग और टूल स्ट्रीमिंग प्रथम-श्रेणी की सुविधाएँ हैं, लेकिन प्रदाता व्यवहार हर सप्ताह बदलता है और प्रत्येक रिलीज़ के लिए परिदृश्य-आधारित प्रमाण की आवश्यकता होती है।

कवरेज प्रायोगिक - 33%गुणवत्ता बीटा - 78%पूर्णता बीटा - 79%आंशिक - 6

Agent टर्न निष्पादन 3 क्षमताएँ / LTS-समर्थित

प्रायोगिक29%

बीटा79%

बीटा79%

[Agent लूप](</hi/concepts/agent-loop>), [Agent](</hi/cli/agent>), [Agent रनटाइम](</hi/concepts/agent-runtimes>)

बाहरी रनटाइम और सबएजेंट 4 क्षमताएँ

प्रायोगिक30%

बीटा79%

बीटा79%

[Agent रनटाइम](</hi/concepts/agent-runtimes>), [Anthropic](</hi/providers/anthropic>), [Google](</hi/providers/google>), [सबएजेंट](</hi/tools/subagents>)

होस्टेड प्रदाता निष्पादन 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक20%

बीटा79%

बीटा79%

[Openai](</hi/providers/openai>), [Anthropic](</hi/providers/anthropic>), [Google](</hi/providers/google>), [मॉडल](</hi/concepts/models>)

स्थानीय और स्वयं-होस्टेड प्रदाता 5 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[Ollama](</hi/providers/ollama>), [मॉडल](</hi/concepts/models>), [Agent](</hi/cli/agent>)

मॉडल और रनटाइम चयन 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक25%

बीटा79%

बीटा79%

[मॉडल](</hi/concepts/models>), [मॉडल](</hi/cli/models>), [Openai](</hi/providers/openai>), [Agent रनटाइम](</hi/concepts/agent-runtimes>)

प्रदाता प्रमाणीकरण 10 क्षमताएँ / LTS-समर्थित

प्रायोगिक24%

बीटा79%

बीटा79%

[मॉडल](</hi/concepts/models>), [Agent](</hi/cli/agent>), [मॉडल](</hi/cli/models>), [Openai](</hi/providers/openai>), [Anthropic](</hi/providers/anthropic>), [Google](</hi/providers/google>), [सबएजेंट](</hi/tools/subagents>)

स्ट्रीमिंग और प्रगति 2 क्षमताएँ

अल्फा56%

बीटा79%

बीटा79%

[स्ट्रीमिंग](</hi/concepts/streaming>), [Agent लूप](</hi/concepts/agent-loop>)

टूल कॉल और प्रतिक्रिया प्रबंधन 3 क्षमताएँ / LTS-समर्थित

अल्फा65%

बीटा79%

बीटा79%

[Agent लूप](</hi/concepts/agent-loop>), [Ollama](</hi/providers/ollama>)

टूल निष्पादन नियंत्रण 6 क्षमताएँ / LTS-समर्थित

Alpha50%

Beta79%

Beta79%

[सैंडबॉक्स बनाम टूल नीति बनाम उन्नत](</hi/gateway/sandbox-vs-tool-policy-vs-elevated>), [एजेंट लूप](</hi/concepts/agent-loop>), [सबएजेंट](</hi/tools/subagents>)

सेशन, मेमोरी, और संदर्भ इंजन - M3 बीटा - 9 क्षेत्र

मजबूत दस्तावेज़ और सक्रिय कार्यान्वयन। परिपक्वता ट्रांसक्रिप्ट की टिकाऊपन, Compaction की गुणवत्ता, और क्रॉस-क्लाइंट समानता पर निर्भर करती है।

कवरेज प्रायोगिक - 30%गुणवत्ता बीटा - 77%पूर्णता बीटा - 79%आंशिक - 6

CLI सत्र और ट्रांसक्रिप्ट प्रबंधन 2 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[सत्र](</hi/concepts/session>), [सत्र प्रबंधन Compaction](</hi/reference/session-management-compaction>), [सत्र](</hi/cli/sessions>)

टोकन प्रबंधन 3 क्षमताएँ / LTS-समर्थित

प्रायोगिक20%

बीटा79%

बीटा79%

[Compaction](</hi/concepts/compaction>), [संदर्भ](</hi/concepts/context>), [सत्र प्रबंधन Compaction](</hi/reference/session-management-compaction>)

संदर्भ इंजन 2 क्षमताएँ / LTS-समर्थित

अल्फ़ा57%

बीटा79%

बीटा79%

[संदर्भ](</hi/concepts/context>), [संदर्भ इंजन](</hi/concepts/context-engine>), [Codex संदर्भ इंजन हार्नेस](</hi/plan/codex-context-engine-harness>)

क्रॉस-क्लाइंट इतिहास और सत्र समानता 2 क्षमताएँ

प्रायोगिक40%

बीटा79%

बीटा79%

[वेबचैट](</hi/web/webchat>), [Android](</hi/platforms/android>), [चैनल रूटिंग](</hi/channels/channel-routing>)

निदान, रखरखाव और पुनर्प्राप्ति 3 क्षमताएँ

प्रायोगिक40%

बीटा79%

बीटा79%

[निदान](</hi/gateway/diagnostics>), [सत्र प्रबंधन Compaction](</hi/reference/session-management-compaction>), [फ़्लैग](</hi/diagnostics/flags>)

मुख्य प्रॉम्प्ट और संदर्भ 2 क्षमताएँ / LTS-समर्थित

प्रायोगिक38%

बीटा79%

बीटा79%

[संदर्भ](</hi/concepts/context>), [ट्रांसक्रिप्ट स्वच्छता](</hi/reference/transcript-hygiene>), [Discord](</hi/channels/discord>)

स्मृति 5 क्षमताएँ

प्रायोगिक46%

बीटा79%

बीटा79%

[स्मृति कॉन्फ़िगरेशन](</hi/reference/memory-config>), [स्मृति Qmd](</hi/concepts/memory-qmd>), [स्मृति](</hi/concepts/memory>), [Discord](</hi/channels/discord>)

सत्र रूटिंग 2 क्षमताएँ / LTS-समर्थित

प्रायोगिक25%

बीटा79%

बीटा79%

[सत्र](</hi/concepts/session>), [चैनल रूटिंग](</hi/channels/channel-routing>), [Discord](</hi/channels/discord>)

ट्रांसक्रिप्ट स्थायित्व 2 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[सेशन प्रबंधन Compaction](</hi/reference/session-management-compaction>), [ट्रांसक्रिप्ट हाइजीन](</hi/reference/transcript-hygiene>)

चैनल फ्रेमवर्क - M3 बीटा - 8 क्षेत्र

कई चैनल Gateway डिलीवरी और रूटिंग अनुबंध साझा करते हैं, लेकिन चैनल का व्यवहार अपस्ट्रीम API और खाता-नीति प्रतिबंधों के अनुसार अलग-अलग होता है।

कवरेज प्रायोगिक - 13%गुणवत्ता बीटा - 76%पूर्णता बीटा - 79%आंशिक - 5

चैनल क्रिया कमांड और स्वीकृतियाँ 5 क्षमताएँ

प्रायोगिक0%

बीटा79%

बीटा79%

[समूह](</hi/channels/groups>), [Discord](</hi/channels/discord>), [Google Chat](</hi/channels/googlechat>), [Signal](</hi/channels/signal>), [Matrix](</hi/channels/matrix>)

चैनल सेटअप 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक14%

बीटा79%

बीटा79%

[अनुक्रमणिका](</hi/channels>), [पेयरिंग](</hi/channels/pairing>), [समस्या निवारण](</hi/channels/troubleshooting>), [SDK चैनल Plugins](</hi/plugins/sdk-channel-plugins>)

समूह थ्रेड और परिवेशी कक्ष व्यवहार 5 क्षमताएँ

प्रायोगिक36%

बीटा79%

बीटा79%

[समूह](</hi/channels/groups>), [समूह संदेश](</hi/channels/group-messages>), [परिवेशी कक्ष इवेंट](</hi/channels/ambient-room-events>), [ब्रॉडकास्ट समूह](</hi/channels/broadcast-groups>), [Discord](</hi/channels/discord>)

इनबाउंड पहुँच और पहचान गेट 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

अल्फा68%

बीटा79%

[पहुँच समूह](</hi/channels/access-groups>), [समूह](</hi/channels/groups>), [Discord](</hi/channels/discord>), [LINE](</hi/channels/line>)

मीडिया अटैचमेंट और समृद्ध चैनल डेटा 4 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[LINE](</hi/channels/line>), [Signal](</hi/channels/signal>), [Google Chat](</hi/channels/googlechat>), [Matrix](</hi/channels/matrix>), [Discord](</hi/channels/discord>)

आउटबाउंड डिलीवरी और उत्तर पाइपलाइन 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक38%

बीटा79%

बीटा79%

[समूह](</hi/channels/groups>), [परिवेशी कक्ष इवेंट](</hi/channels/ambient-room-events>), [Discord](</hi/channels/discord>), [Matrix](</hi/channels/matrix>), [कॉन्फिग चैनल](</hi/gateway/config-channels>)

वार्तालाप रूटिंग और डिलीवरी 10 क्षमताएँ / LTS-समर्थित

प्रायोगिक19%

बीटा79%

बीटा79%

[चैनल रूटिंग](</hi/channels/channel-routing>), [समूह](</hi/channels/groups>), [Discord](</hi/channels/discord>), [Matrix](</hi/channels/matrix>), [समस्या निवारण](</hi/channels/troubleshooting>), [कॉन्फिगरेशन संदर्भ](</hi/gateway/configuration-reference>)

स्थिति स्वास्थ्य और ऑपरेटर नियंत्रण 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा79%

बीटा79%

[स्वास्थ्य](</hi/gateway/health>), [कॉन्फ़िगरेशन संदर्भ](</hi/gateway/configuration-reference>), [समस्या निवारण](</hi/channels/troubleshooting>), [Discord](</hi/channels/discord>)

Observability - M3 बीटा - 5 क्षेत्र

OTel, Prometheus, लॉगिंग, और निदान दस्तावेज़ मौजूद हैं। एक सार्वजनिक "ऑपरेटरों को पहले क्या देखना चाहिए" परिपक्वता समीक्षा की आवश्यकता है।

कवरेज प्रायोगिक - 18%गुणवत्ता बीटा - 75%पूर्णता बीटा - 79%आंशिक - 3

स्वास्थ्य और मरम्मत 12 क्षमताएँ / LTS-समर्थित

प्रायोगिक28%

बीटा79%

बीटा79%

[स्वास्थ्य](</hi/gateway/health>), [Telegram](</hi/channels/telegram>), [डॉक्टर](</hi/cli/doctor>), [डॉक्टर](</hi/gateway/doctor>), [SDK उपपथ](</hi/plugins/sdk-subpaths>), [स्वास्थ्य](</hi/cli/health>), [प्रोटोकॉल](</hi/gateway/protocol>)

लॉगिंग 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

अल्फा68%

बीटा79%

[लॉगिंग](</hi/logging>), [लॉगिंग](</hi/gateway/logging>), [लॉग](</hi/cli/logs>)

डायग्नॉस्टिक संग्रह 8 क्षमताएँ

प्रायोगिक30%

बीटा79%

बीटा79%

[डायग्नॉस्टिक्स](</hi/gateway/diagnostics>), [स्वास्थ्य](</hi/gateway/health>), [Codex हार्नेस](</hi/plugins/codex-harness>), [प्रोटोकॉल](</hi/gateway/protocol>)

टेलीमेट्री निर्यात 13 क्षमताएँ

प्रायोगिक33%

बीटा79%

बीटा79%

[हुक](</hi/plugins/hooks>), [Opentelemetry](</hi/gateway/opentelemetry>), [लॉगिंग](</hi/logging>), [SDK उपपथ](</hi/plugins/sdk-subpaths>), [डायग्नॉस्टिक्स Otel](</hi/plugins/reference/diagnostics-otel>), [Prometheus](</hi/gateway/prometheus>), [डायग्नॉस्टिक्स Prometheus](</hi/plugins/reference/diagnostics-prometheus>)

सत्र डायग्नॉस्टिक्स 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

अल्फा68%

बीटा79%

[Opentelemetry](</hi/gateway/opentelemetry>), [Prometheus](</hi/gateway/prometheus>), [डायग्नॉस्टिक्स](</hi/gateway/diagnostics>), [प्रोटोकॉल](</hi/gateway/protocol>)

Gateway वेब ऐप - M3 बीटा - 6 क्षेत्र

वेब UI को पेयरिंग, चैट, PWA, Talk, पुश, और रिमोट Gateway फ्लो के साथ दस्तावेज़ित किया गया है। क्रॉस-ब्राउज़र और मोबाइल-PWA स्कोरकार्ड के बाद प्रमोट करें।

कवरेज प्रायोगिक - 4%गुणवत्ता बीटा - 74%पूर्णता बीटा - 79%कोई नहीं

ब्राउज़र रीयलटाइम बातचीत 5 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[कंट्रोल UI](</hi/web/control-ui>), [प्रोटोकॉल](</hi/gateway/protocol>), [बातचीत](</hi/nodes/talk>)

ब्राउज़र एक्सेस और भरोसा 5 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[कंट्रोल UI](</hi/web/control-ui>), [डैशबोर्ड](</hi/web/dashboard>), [Tailscale](</hi/gateway/tailscale>), [रिमोट](</hi/gateway/remote>)

कॉन्फ़िगरेशन 5 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[कंट्रोल UI](</hi/web/control-ui>), [कॉन्फ़िगरेशन](</hi/gateway/configuration>)

ब्राउज़र UI 10 क्षमताएँ

प्रायोगिक8%

बीटा79%

बीटा79%

[कंट्रोल UI](</hi/web/control-ui>), [इंडेक्स](</hi/web>), [डैशबोर्ड](</hi/web/dashboard>), [प्रोटोकॉल](</hi/gateway/protocol>)

WebChat बातचीत 15 क्षमताएँ

प्रायोगिक10%

बीटा79%

बीटा79%

[कंट्रोल UI](</hi/web/control-ui>), [Webchat](</hi/web/webchat>), [शुरुआत करना](</hi/start/getting-started>), [चैनल रूटिंग](</hi/channels/channel-routing>), [सुरक्षित फ़ाइल संचालन](</hi/gateway/security/secure-file-operations>)

ऑपरेटर कंसोल 10 क्षमताएँ

प्रायोगिक8%

बीटा79%

बीटा79%

[कंट्रोल UI](</hi/web/control-ui>), [स्वास्थ्य](</hi/gateway/health>), [प्रोटोकॉल](</hi/gateway/protocol>), [डैशबोर्ड](</hi/web/dashboard>)

Plugins - M3 बीटा - 9 क्षेत्र

मैनिफ़ेस्ट, डिस्कवरी, लोडिंग, प्रोवाइडर/टूल आर्किटेक्चर, और अनुमोदन सीमाओं में व्यापक दस्तावेज़ और मजबूत आंतरिक रनटाइम प्रमाण मौजूद हैं। सार्वजनिक SDK API/subpaths और बाहरी वितरण प्रमाण अधिक मजबूत होने तक पंक्ति को बीटा पर रखें।

कवरेज प्रायोगिक - 12%गुणवत्ता बीटा - 72%पूर्णता बीटा - 79%आंशिक - 7

Plugin लिखना और पैकेज करना 8 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[Plugin बनाना](</hi/plugins/building-plugins>), [SDK अवलोकन](</hi/plugins/sdk-overview>), [SDK एंट्रीपॉइंट](</hi/plugins/sdk-entrypoints>), [SDK उपपथ](</hi/plugins/sdk-subpaths>), [मैनिफेस्ट](</hi/plugins/manifest>), [संदर्भ](</hi/plugins/reference>)

बंडल किए गए Plugin 5 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[Plugin इन्वेंटरी](</hi/plugins/plugin-inventory>), [Plugin](</hi/cli/plugins>), [आर्किटेक्चर आंतरिक विवरण](</hi/plugins/architecture-internals>)

कैनवास Plugin 6 क्षमताएं

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[कैनवास](</hi/plugins/reference/canvas>), [कैनवास](</hi/refactor/canvas>), [कॉन्फ़िगरेशन संदर्भ](</hi/gateway/configuration-reference>)

Plugin इंस्टॉल करना और चलाना 6 क्षमताएं / LTS-समर्थित

प्रायोगिक35%

बीटा79%

बीटा79%

[आर्किटेक्चर](</hi/plugins/architecture>), [आर्किटेक्चर आंतरिक विवरण](</hi/plugins/architecture-internals>), [Plugin](</hi/cli/plugins>)

चैनल Plugin 5 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[SDK चैनल Plugin](</hi/plugins/sdk-channel-plugins>), [SDK चैनल इनबाउंड](</hi/plugins/sdk-channel-inbound>), [SDK चैनल आउटबाउंड](</hi/plugins/sdk-channel-outbound>)

प्रदाता और उपकरण Plugin 6 क्षमताएं / LTS-समर्थित

प्रायोगिक43%

बीटा79%

बीटा79%

[SDK प्रदाता Plugin](</hi/plugins/sdk-provider-plugins>), [उपकरण Plugin](</hi/plugins/tool-plugins>), [क्षमताएं जोड़ना](</hi/plugins/adding-capabilities>)

Plugin अनुमोदन 6 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[Plugin अनुमति अनुरोध](</hi/plugins/plugin-permission-requests>), [Exec अनुमोदन](</hi/tools/exec-approvals>), [SDK चैनल Plugin](</hi/plugins/sdk-channel-plugins>)

Plugin प्रकाशित करना 6 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा68%

बीटा79%

[Plugin](</hi/cli/plugins>), [संगतता](</hi/plugins/compatibility>), [प्रकाशन](</hi/clawhub/publishing>)

Plugin का परीक्षण 6 क्षमताएँ

प्रयोगात्मक27%

बीटा79%

बीटा79%

[Sdk परीक्षण](</hi/plugins/sdk-testing>), [Sdk सेटअप](</hi/plugins/sdk-setup>), [Codex हार्नेस](</hi/plugins/codex-harness>)

सुरक्षा, auth, pairing, और secrets - M3 बीटा - 6 क्षेत्र

अच्छे दस्तावेज़ और hardening surfaces मौजूद हैं। नियमित upgrade/security scenario runs से setup regressions न होने का प्रमाण मिलने के बाद promote करें।

Coverage प्रायोगिक - 16%Quality बीटा - 72%Completeness बीटा - 79%आंशिक - 5

Approval Policy और Tool Safeguards 2 क्षमताएं / LTS-समर्थित

अल्फा50%

बीटा79%

बीटा79%

[Exec Approvals](</hi/tools/exec-approvals>), [Approvals](</hi/cli/approvals>), [Plugin Permission Requests](</hi/plugins/plugin-permission-requests>), [Audit Checks](</hi/gateway/security/audit-checks>)

Gateway Auth और Remote Access 9 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फा68%

बीटा79%

[Index](</hi/gateway/security>), [Exposure Runbook](</hi/gateway/security/exposure-runbook>), [Trusted Proxy Auth](</hi/gateway/trusted-proxy-auth>), [Tailscale](</hi/gateway/tailscale>), [Remote](</hi/gateway/remote>), [Configuration Reference](</hi/gateway/configuration-reference>), [Gateway](</hi/cli/gateway>), [Doctor](</hi/cli/doctor>), [Control UI](</hi/web/control-ui>), [Browser Control](</hi/tools/browser-control>), [Audit Checks](</hi/gateway/security/audit-checks>)

Channel Access Control 3 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फा68%

बीटा79%

[Pairing](</hi/channels/pairing>), [Telegram](</hi/channels/telegram>), [Access Groups](</hi/channels/access-groups>), [Audit Checks](</hi/gateway/security/audit-checks>)

Device और Node Pairing 11 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फा68%

बीटा79%

[Protocol](</hi/gateway/protocol>), [Devices](</hi/cli/devices>), [Pairing](</hi/channels/pairing>), [Pairing](</hi/gateway/pairing>), [Operator Scopes](</hi/gateway/operator-scopes>), [Control UI](</hi/web/control-ui>), [Webchat](</hi/web/webchat>), [Approvals](</hi/cli/approvals>)

Plugin Trust 2 क्षमताएं

प्रायोगिक0%

अल्फा68%

बीटा79%

[Manifest](</hi/plugins/manifest>), [Plugin Permission Requests](</hi/plugins/plugin-permission-requests>), [Manage Plugins](</hi/plugins/manage-plugins>), [Audit Checks](</hi/gateway/security/audit-checks>)

Credential और Secret Hygiene 5 क्षमताएं / LTS-समर्थित

प्रायोगिक46%

बीटा79%

बीटा79%

[Authentication](</hi/gateway/authentication>), [Models](</hi/cli/models>), [Openai](</hi/providers/openai>), [Oauth](</hi/concepts/oauth>), [Secrets](</hi/gateway/secrets>), [Secrets](</hi/cli/secrets>), [Secretref Credential Surface](</hi/reference/secretref-credential-surface>), [Audit Checks](</hi/gateway/security/audit-checks>)

ऑटोमेशन: cron, hooks, tasks, polling - M3 बीटा - 6 क्षेत्र

दस्तावेजीकृत और उपयोग योग्य है, लेकिन scenario proof में unattended delivery, retries, और failure visibility शामिल होने चाहिए।

Coverage प्रायोगिक - 2%Quality बीटा - 72%Completeness बीटा - 79%कोई नहीं

Cron जॉब्स 15 क्षमताएँ

प्रायोगिक0%

बीटा79%

बीटा79%

[Cron जॉब्स](</hi/automation/cron-jobs>), [Cron](</hi/cli/cron>), [प्रोटोकॉल](</hi/gateway/protocol>), [कार्य](</hi/automation/tasks>), [Discord](</hi/channels/discord>)

इवेंट इनग्रेस 15 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[Telegram](</hi/channels/telegram>), [Zalo](</hi/channels/zalo>), [समस्या निवारण](</hi/channels/troubleshooting>), [BlueBubbles से iMessage](</hi/channels/imessage-from-bluebubbles>), [Gmail Pubsub इंटीग्रेशन](</hi/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</hi/automation/cron-jobs>), [Webhooks](</hi/cli/webhooks>), [Webhooks](</hi/automation/cron-jobs#webhooks>), [Webhook](</hi/automation/cron-jobs>)

ऑटोमेशन हुक्स 11 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[हुक्स](</hi/automation/hooks>), [हुक्स](</hi/cli/hooks>), [हुक्स](</hi/plugins/hooks>), [Plugin अनुमति अनुरोध](</hi/plugins/plugin-permission-requests>), [SDK सबपाथ](</hi/plugins/sdk-subpaths>)

बैकग्राउंड कार्य और फ़्लो 10 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[कार्य](</hi/automation/tasks>), [इंडेक्स](</hi/automation>), [कार्य](</hi/cli/tasks>), [TaskFlow](</hi/automation/taskflow>), [SDK रनटाइम](</hi/plugins/sdk-runtime>)

Heartbeat 5 क्षमताएँ

प्रायोगिक14%

बीटा79%

बीटा79%

[इंडेक्स](</hi/automation>), [Heartbeat](</hi/gateway/heartbeat>), [प्रतिबद्धताएँ](</hi/concepts/commitments>)

पोलिंग नियंत्रण 10 क्षमताएँ

प्रायोगिक0%

अल्फा68%

बीटा79%

[पोल](</hi/cli/message>), [संदेश](</hi/cli/message>), [Telegram](</hi/channels/telegram>), [Msteams](</hi/channels/msteams>), [बैकग्राउंड प्रोसेस](</hi/gateway/background-process>)

मीडिया समझ और मीडिया जनरेशन - M2 अल्फा - 6 क्षेत्र

व्यापक क्षमता सतह मौजूद है, लेकिन प्रदाता विविधता, फ़ाइल सीमाएँ, और Node/app समानता इसे अभी स्थिर नहीं बनातीं।

कवरेज प्रायोगिक - 2%गुणवत्ता अल्फा - 64%पूर्णता अल्फा - 68%कोई नहीं

मीडिया इनटेक और एक्सेस 8 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[मीडिया अवलोकन](</hi/tools/media-overview>), [मीडिया समझ](</hi/nodes/media-understanding>), [सुरक्षित फ़ाइल संचालन](</hi/gateway/security/secure-file-operations>), [PDF](</hi/tools/pdf>), [छवि जनरेशन](</hi/tools/image-generation>), [QR](</hi/cli/qr>), [LINE](</hi/channels/line>), [WhatsApp](</hi/channels/whatsapp>)

चैनल मीडिया हैंडलिंग 5 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[छवियाँ](</hi/nodes/images>), [मीडिया अवलोकन](</hi/tools/media-overview>), [Discord](</hi/channels/discord>)

मीडिया कॉन्फ़िगरेशन 1 क्षमता

प्रायोगिक0%

अल्फा61%

अल्फा68%

[मीडिया अवलोकन](</hi/tools/media-overview>), [छवि जनरेशन](</hi/tools/image-generation>), [मैनिफ़ेस्ट](</hi/plugins/manifest>), [Codex हार्नेस](</hi/plugins/codex-harness>)

टेक्स्ट-टू-स्पीच डिलीवरी 2 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[TTS](</hi/tools/tts>), [मीडिया अवलोकन](</hi/tools/media-overview>), [Discord](</hi/channels/discord>)

मीडिया समझ 12 क्षमताएँ

प्रायोगिक7%

अल्फा69%

अल्फा69%

[ऑडियो](</hi/nodes/audio>), [मीडिया समझ](</hi/nodes/media-understanding>), [मीडिया अवलोकन](</hi/tools/media-overview>), [WhatsApp](</hi/channels/whatsapp>), [छवियाँ](</hi/nodes/images>), [Infer](</hi/cli/infer>), [PDF](</hi/tools/pdf>)

मीडिया जनरेशन 17 क्षमताएँ

प्रायोगिक5%

अल्फा69%

अल्फा69%

[छवि जनरेशन](</hi/tools/image-generation>), [मीडिया अवलोकन](</hi/tools/media-overview>), [Skills](</hi/tools/skills>), [संगीत जनरेशन](</hi/tools/music-generation>), [वीडियो जनरेशन](</hi/tools/video-generation>)

आवाज़ और रीयलटाइम बातचीत - M2 अल्फा - 6 क्षेत्र

Control UI, ऐप्स, और प्रदाताओं में कई कार्यान्वयन मौजूद हैं। बीटा से पहले विलंबता, विफलता-मोड, और सेटअप स्कोरकार्ड की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 61%पूर्णता अल्फा - 68%कोई नहीं

Talk प्रदाता 7 क्षमताएँ

प्रयोगात्मक0%

Alpha61%

Alpha68%

[Openai](</hi/providers/openai>), [Google](</hi/providers/google>), [Sdk प्रदाता Plugin](</hi/plugins/sdk-provider-plugins>), [Talk](</hi/nodes/talk>), [Control Ui](</hi/web/control-ui>)

रीयलटाइम Talk सत्र 11 क्षमताएँ

प्रयोगात्मक0%

Alpha61%

Alpha68%

[Talk](</hi/nodes/talk>), [Control Ui](</hi/web/control-ui>)

स्पीच और ट्रांसक्रिप्शन 5 क्षमताएँ

प्रयोगात्मक0%

Alpha61%

Alpha68%

[Talk](</hi/nodes/talk>), [Openai](</hi/providers/openai>), [Google](</hi/providers/google>)

नेटिव ऐप Talk 4 क्षमताएँ

प्रयोगात्मक0%

Alpha61%

Alpha68%

[Talk](</hi/nodes/talk>), [Voicewake](</hi/platforms/mac/voicewake>)

वॉइस वेक और रूटिंग 4 क्षमताएँ

प्रयोगात्मक0%

Alpha61%

Alpha68%

[Voicewake](</hi/nodes/voicewake>), [Voicewake](</hi/platforms/mac/voicewake>), [वॉइस ओवरले](</hi/platforms/mac/voice-overlay>)

Talk ऑब्ज़र्वेबिलिटी 5 क्षमताएँ

प्रयोगात्मक0%

Alpha61%

Alpha68%

[Control Ui](</hi/web/control-ui>), [वॉइस ओवरले](</hi/platforms/mac/voice-overlay>), [Talk](</hi/nodes/talk>)

TUI - M2 Alpha - 5 क्षेत्र

दस्तावेज़ों और स्रोत में मौजूद है, लेकिन प्राथमिक उपयोगकर्ता वर्कफ़्लो के रूप में कम दिखाई देता है। स्पष्ट परिदृश्य परिभाषा की आवश्यकता है।

कवरेज प्रयोगात्मक - 0%गुणवत्ता Alpha - 59%पूर्णता Alpha - 66%कोई नहीं

रनटाइम मोड 14 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[TUI](</hi/cli/tui>), [TUI](</hi/web/tui>), [सूची](</hi/cli>)

इनपुट और कमांड 8 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[TUI](</hi/web/tui>)

सत्र प्रबंधन 3 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[TUI](</hi/web/tui>), [सत्र](</hi/cli/sessions>)

स्थानीय Shell निष्पादन 4 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[TUI](</hi/web/tui>), [TUI](</hi/cli/tui>)

रेंडरिंग और आउटपुट सुरक्षा 4 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[TUI](</hi/web/tui>), [QR](</hi/cli/qr>), [लॉग](</hi/cli/logs>), [पूर्णता](</hi/cli/completion>)

ClawHub - M2 Alpha - 4 areas

सार्वजनिक दस्तावेज़ और इकोसिस्टम अवधारणा मौजूद हैं। इंस्टॉल, भरोसा, अपडेट, रोलबैक और संगतता स्कोरकार्ड की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 58%पूर्णता अल्फा - 62%कोई नहीं

प्रकाशन 7 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा54%

अल्फ़ा55%

[प्रकाशन](</hi/clawhub/publishing>), [Skills बनाना](</hi/tools/creating-skills>), [समुदाय](</hi/plugins/community>)

कैटलॉग खोज 5 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा61%

अल्फ़ा68%

[Plugin](</hi/tools/plugin>), [Plugins](</hi/cli/plugins>), [Skills](</hi/cli/skills>), [Skills](</hi/tools/skills>), [समुदाय](</hi/plugins/community>)

संगतता और भरोसा 12 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा55%

अल्फ़ा56%

[Plugin](</hi/tools/plugin>), [Plugins](</hi/cli/plugins>), [संगतता](</hi/plugins/compatibility>), [Plugin इन्वेंटरी](</hi/plugins/plugin-inventory>), [प्रकाशन](</hi/clawhub/publishing>), [Skills](</hi/tools/skills>), [Skills कॉन्फ़िग](</hi/tools/skills-config>)

Plugin जीवनचक्र और स्वास्थ्य 26 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा61%

अल्फ़ा68%

[Plugin](</hi/tools/plugin>), [Plugins](</hi/cli/plugins>), [Skills](</hi/cli/skills>), [Skills](</hi/tools/skills>), [प्रोटोकॉल](</hi/gateway/protocol>), [बंडल](</hi/plugins/bundles>), [निर्भरता समाधान](</hi/plugins/dependency-resolution>)

OpenClaw App SDK - M2 अल्फ़ा - 6 क्षेत्र

OpenClaw App SDK, Gateway रनटाइम और Plugin SDK से अलग एक विशिष्ट बाहरी ऐप अनुबंध है। मौजूदा स्कोरिंग सार्वजनिक पैकेजिंग, ऑटो-डिस्कवरी, स्वीकृतियों, हेल्परों और संगतता से जुड़े अंतरालों के साथ एक वास्तविक `@openclaw/sdk` पथ दिखाती है।

कवरेज प्रयोगात्मक - 3%गुणवत्ता अल्फ़ा - 54%पूर्णता अल्फ़ा - 53%कोई नहीं

Client API 4 क्षमताएँ

प्रायोगिक0%

Alpha51%

Alpha50%

[Openclaw Sdk](</hi/gateway/external-apps>), [Openclaw Sdk Api Design](</hi/gateway/external-apps>)

Gateway एक्सेस 5 क्षमताएँ

प्रायोगिक0%

Alpha53%

Alpha54%

[Openclaw Sdk](</hi/gateway/external-apps>), [Openclaw Sdk Api Design](</hi/gateway/external-apps>), [Protocol](</hi/gateway/protocol>), [इंडेक्स](</hi/gateway/security>)

एजेंट वार्तालाप 6 क्षमताएँ

प्रायोगिक0%

Alpha52%

Alpha52%

[Openclaw Sdk](</hi/gateway/external-apps>), [Openclaw Sdk Api Design](</hi/gateway/external-apps>), [Protocol](</hi/gateway/protocol>)

इवेंट और अनुमोदन 5 क्षमताएँ

प्रायोगिक0%

Alpha52%

Alpha52%

[Openclaw Sdk](</hi/gateway/external-apps>), [Openclaw Sdk Api Design](</hi/gateway/external-apps>), [Protocol](</hi/gateway/protocol>)

संसाधन हेल्पर 5 क्षमताएँ

प्रायोगिक17%

Alpha62%

Alpha53%

[Openclaw Sdk](</hi/gateway/external-apps>), [Openclaw Sdk Api Design](</hi/gateway/external-apps>)

संगतता 5 क्षमताएँ

प्रायोगिक0%

Alpha54%

Alpha55%

[Openclaw Sdk Api Design](</hi/gateway/external-apps>), [Typebox](</hi/concepts/typebox>), [Protocol](</hi/gateway/protocol>)

### प्लेटफ़ॉर्म

Linux Gateway होस्ट - M4 स्थिर - 5 क्षेत्र

Node रनटाइम अनुशंसित है, systemd उपयोगकर्ता सेवा दस्तावेज़ित है, और VPS/कंटेनर मार्गदर्शन व्यापक है।

कवरेज प्रायोगिक - 0%गुणवत्ता Beta - 75%पूर्णता स्थिर - 89%आंशिक - 4

होस्ट सेटअप और अपडेट 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[अनुक्रमणिका](</hi/install>), [अपडेट करना](</hi/install/updating>), [Linux](</hi/platforms/linux>), [अनुक्रमणिका](</hi/platforms>)

Gateway रनटाइम और सेवा नियंत्रण 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[अनुक्रमणिका](</hi/gateway>), [Gateway](</hi/cli/gateway>), [Linux](</hi/platforms/linux>), [VPS](</hi/vps>)

दूरस्थ पहुंच और सुरक्षा 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[दूरस्थ](</hi/gateway/remote>), [Tailscale](</hi/gateway/tailscale>), [एक्सपोज़र रनबुक](</hi/gateway/security/exposure-runbook>), [प्रमाणीकरण](</hi/gateway/authentication>), [सीक्रेट्स](</hi/gateway/secrets>)

डायग्नोस्टिक्स और मरम्मत 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

बीटा75%

स्थिर89%

[स्थिति](</hi/cli/status>), [लॉग](</hi/cli/logs>), [Doctor](</hi/cli/doctor>), [डायग्नोस्टिक्स](</hi/gateway/diagnostics>), [अनुक्रमणिका](</hi/gateway>)

डिप्लॉयमेंट लक्ष्य 3 क्षमताएँ

प्रायोगिक0%

बीटा75%

स्थिर89%

[VPS](</hi/vps>), [Docker](</hi/install/docker>), [Hetzner](</hi/install/hetzner>), [Digitalocean](</hi/install/digitalocean>), [Kubernetes](</hi/install/kubernetes>), [Podman](</hi/install/podman>)

macOS Gateway होस्ट - M4 स्थिर - 7 क्षेत्र

LaunchAgent सेवा पथ, स्थानीय/दूरस्थ Gateway मोड, CLI इंस्टॉल, और ऐप एकीकरण दस्तावेज़ित हैं।

कवरेज प्रायोगिक - 0%गुणवत्ता बीटा - 74%पूर्णता स्थिर - 88%कोई नहीं

CLI सेटअप 4 क्षमताएँ

प्रयोगात्मक0%

बीटा74%

स्थिर88%

[Macos](</hi/platforms/macos>), [बंडल किया गया Gateway](</hi/platforms/mac/bundled-gateway>), [इंस्टॉलर](</hi/install/installer>), [Node](</hi/install/node>)

स्थानीय Gateway इंटीग्रेशन 9 क्षमताएँ

प्रयोगात्मक0%

बीटा74%

स्थिर88%

[Macos](</hi/platforms/macos>), [बंडल किया गया Gateway](</hi/platforms/mac/bundled-gateway>), [रिमोट](</hi/platforms/mac/remote>), [इंडेक्स](</hi/gateway>), [Gateway](</hi/cli/gateway>), [Bonjour](</hi/gateway/bonjour>)

रिमोट Gateway मोड 5 क्षमताएँ

प्रयोगात्मक0%

बीटा74%

स्थिर88%

[रिमोट](</hi/platforms/mac/remote>), [रिमोट](</hi/gateway/remote>), [Tailscale](</hi/gateway/tailscale>)

Gateway सेवा जीवनचक्र 10 क्षमताएँ

प्रयोगात्मक0%

बीटा74%

स्थिर88%

[Macos](</hi/platforms/macos>), [बंडल किया गया Gateway](</hi/platforms/mac/bundled-gateway>), [Gateway](</hi/cli/gateway>), [इंडेक्स](</hi/gateway>), [अपडेट](</hi/cli/update>), [अपडेट करना](</hi/install/updating>), [अनइंस्टॉल](</hi/install/uninstall>), [समस्या निवारण](</hi/gateway/troubleshooting>)

डायग्नोस्टिक्स और ऑब्ज़र्वेबिलिटी 4 क्षमताएँ

प्रयोगात्मक0%

बीटा74%

स्थिर88%

[बंडल किया गया Gateway](</hi/platforms/mac/bundled-gateway>), [Macos](</hi/platforms/macos>), [Gateway](</hi/cli/gateway>), [Doctor](</hi/gateway/doctor>), [समस्या निवारण](</hi/gateway/troubleshooting>)

अनुमतियाँ और नेटिव क्षमताएँ 4 क्षमताएँ

प्रयोगात्मक0%

बीटा74%

स्थिर88%

[Macos](</hi/platforms/macos>), [रिमोट](</hi/platforms/mac/remote>)

प्रोफ़ाइलें और आइसोलेशन 5 क्षमताएँ

प्रयोगात्मक0%

बीटा74%

स्थिर88%

[एकाधिक Gateways](</hi/gateway/multiple-gateways>), [इंडेक्स](</hi/gateway>), [Gateway](</hi/cli/gateway>)

Docker और Podman होस्टिंग - M3 बीटा - 4 क्षेत्र

इंस्टॉल दस्तावेज़ मौजूद हैं और सामान्य डिप्लॉयमेंट पथ हैं। आवर्ती रिलीज़ स्मोक द्वारा अपग्रेड और वॉल्यूम व्यवहार कैप्चर करने के बाद प्रमोट करें।

कवरेज प्रयोगात्मक - 7%गुणवत्ता बीटा - 71%पूर्णता बीटा - 79%कोई नहीं

कंटेनर सेटअप 6 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा68%

बीटा79%

[Docker](</hi/install/docker>), [Podman](</hi/install/podman>)

कंटेनर संचालन 11 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा68%

बीटा79%

[Podman](</hi/install/podman>), [Docker Vm Runtime](</hi/install/docker-vm-runtime>), [Docker](</hi/install/docker>), [Hetzner](</hi/install/hetzner>), [Hostinger](</hi/install/hostinger>)

इमेज रिलीज़ और सत्यापन 5 क्षमताएँ

प्रयोगात्मक29%

बीटा79%

बीटा79%

[Docker](</hi/install/docker>), [Docker Vm Runtime](</hi/install/docker-vm-runtime>), [पूर्ण रिलीज़ सत्यापन](</hi/reference/full-release-validation>)

एजेंट सैंडबॉक्स और टूलिंग 3 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा68%

बीटा79%

[Docker](</hi/install/docker>), [Docker Vm Runtime](</hi/install/docker-vm-runtime>)

WSL2 के माध्यम से Windows - M3 बीटा - 6 क्षेत्र

systemd/यूज़र-सर्विस मार्गदर्शन और बूट-चेन दस्तावेज़ों के साथ अनुशंसित Windows पथ। बार-बार install/update स्कोरकार्ड के बाद प्रमोट करें।

कवरेज प्रयोगात्मक - 6%गुणवत्ता अल्फ़ा - 69%पूर्णता बीटा - 79%आंशिक - 5

WSL सेटअप 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

Alpha67%

Beta79%

[Windows](</hi/platforms/windows>), [शुरुआत करना](</hi/start/getting-started>)

CLI 8 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

Alpha67%

Beta79%

[Windows](</hi/platforms/windows>), [शुरुआत करना](</hi/start/getting-started>), [अपडेट करना](</hi/install/updating>), [Onboard](</hi/cli/onboard>), [Doctor](</hi/cli/doctor>), [स्थिति](</hi/cli/status>), [लॉग](</hi/cli/logs>)

Gateway सेवा जीवनचक्र 10 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

Alpha67%

Beta79%

[Windows](</hi/platforms/windows>), [अनुक्रमणिका](</hi/gateway>), [Doctor](</hi/gateway/doctor>)

Gateway पहुँच और एक्सपोज़र 11 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

Alpha67%

Beta79%

[प्रमाणीकरण](</hi/gateway/authentication>), [रहस्य](</hi/gateway/secrets>), [रिमोट](</hi/gateway/remote>), [एक्सपोज़र रनबुक](</hi/gateway/security/exposure-runbook>), [Windows](</hi/platforms/windows>)

निदान और मरम्मत 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक38%

Beta79%

Beta79%

[Windows](</hi/platforms/windows>), [स्थिति](</hi/cli/status>), [लॉग](</hi/cli/logs>), [Doctor](</hi/cli/doctor>), [Doctor](</hi/gateway/doctor>)

ब्राउज़र और नियंत्रण UI 6 क्षमताएँ

प्रायोगिक0%

Alpha67%

Beta79%

[ब्राउज़र Wsl2 Windows रिमोट Cdp समस्या निवारण](</hi/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [ब्राउज़र](</hi/tools/browser>), [नियंत्रण UI](</hi/web/control-ui>)

Raspberry Pi और छोटे Linux डिवाइस - M3 Beta - 4 क्षेत्र

प्लेटफ़ॉर्म दस्तावेज़ मौजूद हैं और Gateway पथ Linux-आधारित है। उच्च स्तर पर जाने के लिए हार्डवेयर-विशिष्ट रिलीज़ स्मोक प्रमाण की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता Alpha - 67%पूर्णता Beta - 79%कोई नहीं

सेटअप और संगतता 12 क्षमताएँ

प्रायोगिक0%

अल्फा67%

बीटा79%

[Raspberry Pi](</hi/install/raspberry-pi>), [अनुक्रमणिका](</hi/install>), [पहले रन के अक्सर पूछे जाने वाले प्रश्न](</hi/help/faq-first-run>), [अक्सर पूछे जाने वाले प्रश्न](</hi/help/faq>), [Linux](</hi/platforms/linux>), [इंस्टॉलर](</hi/install/installer>)

दूरस्थ पहुँच और प्रमाणीकरण 9 क्षमताएँ

प्रायोगिक0%

अल्फा67%

बीटा79%

[Raspberry Pi](</hi/install/raspberry-pi>), [प्रमाणीकरण](</hi/gateway/authentication>), [सीक्रेट्स](</hi/gateway/secrets>), [पेयरिंग](</hi/gateway/pairing>), [डिवाइस](</hi/cli/devices>), [दूरस्थ](</hi/gateway/remote>), [Tailscale](</hi/gateway/tailscale>)

Gateway रनटाइम 10 क्षमताएँ

प्रायोगिक0%

अल्फा67%

बीटा79%

[अनुक्रमणिका](</hi/gateway>), [Gateway](</hi/cli/gateway>), [Raspberry Pi](</hi/install/raspberry-pi>), [Linux](</hi/platforms/linux>), [VPS](</hi/vps>)

प्रदर्शन और निदान 5 क्षमताएँ

प्रायोगिक0%

अल्फा67%

बीटा79%

[Raspberry Pi](</hi/install/raspberry-pi>), [Linux](</hi/platforms/linux>), [स्वास्थ्य](</hi/gateway/health>), [निदान](</hi/gateway/diagnostics>)

macOS साथी ऐप - M3 बीटा - 8 क्षेत्र

समृद्ध मेनू बार ऐप, अनुमतियाँ, Node मोड, कैनवास, वॉइस वेक, वेबचैट, और दूरस्थ मोड मौजूद हैं। फिर भी यह इतना तेज़ी से बदल रहा है कि इसे Stable से बचाया गया है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 66%पूर्णता बीटा - 78%कोई नहीं

कैनवास 4 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[कैनवास](</hi/platforms/mac/canvas>), [Macos](</hi/platforms/macos>), [वेबचैट](</hi/web/webchat>)

लोकल सेटअप 7 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[बंडल किया गया Gateway](</hi/platforms/mac/bundled-gateway>), [Macos](</hi/platforms/macos>), [चाइल्ड प्रोसेस](</hi/platforms/mac/child-process>), [डेवलपर सेटअप](</hi/platforms/mac/dev-setup>)

स्थिति और सेटिंग्स 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[मेनू बार](</hi/platforms/mac/menu-bar>), [आइकन](</hi/platforms/mac/icon>), [Macos](</hi/platforms/macos>), [स्वास्थ्य](</hi/platforms/mac/health>), [लॉगिंग](</hi/platforms/mac/logging>), [रिमोट](</hi/platforms/mac/remote>)

नेटिव क्षमताएँ 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Macos](</hi/platforms/macos>), [Xpc](</hi/platforms/mac/xpc>), [अनुमतियाँ](</hi/platforms/mac/permissions>), [साइनिंग](</hi/platforms/mac/signing>), [Peekaboo](</hi/platforms/mac/peekaboo>)

रिमोट कनेक्शन 3 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[रिमोट](</hi/platforms/mac/remote>), [Macos](</hi/platforms/macos>), [रिमोट](</hi/gateway/remote>)

वॉइस और बातचीत 3 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Voicewake](</hi/platforms/mac/voicewake>), [वॉइस ओवरले](</hi/platforms/mac/voice-overlay>), [बातचीत](</hi/nodes/talk>), [Macos](</hi/platforms/macos>)

वेबचैट 3 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[वेबचैट](</hi/platforms/mac/webchat>), [Macos](</hi/platforms/macos>), [वेबचैट](</hi/web/webchat>)

रिमोट वेबचैट 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[वेबचैट](</hi/platforms/mac/webchat>), [रिमोट](</hi/gateway/remote>), [रिमोट](</hi/platforms/mac/remote>)

Android ऐप - M2 अल्फा - 7 क्षेत्र

सार्वजनिक Google Play पथ मौजूद है, लेकिन ऐप दस्तावेज़ अब भी रीबिल्ड को बेहद अल्फा बताते हैं और रिलीज़ हार्डनिंग कार्य का उल्लेख करते हैं।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 59%पूर्णता अल्फा - 66%कोई नहीं

मीडिया कैप्चर 1 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Android](</hi/platforms/android>), [कैमरा](</hi/nodes/camera>)

मोबाइल चैट 1 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Android](</hi/platforms/android>)

कनेक्शन सेटअप 1 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Android](</hi/platforms/android>), [Bonjour](</hi/gateway/bonjour>), [पेयरिंग](</hi/gateway/pairing>)

वितरण 3 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Android](</hi/platforms/android>)

सेटिंग्स 1 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Android](</hi/platforms/android>)

आवाज़ 1 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Android](</hi/platforms/android>), [बात करें](</hi/nodes/talk>)

डिवाइस रनटाइम 2 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Android](</hi/platforms/android>), [समस्या निवारण](</hi/nodes/troubleshooting>), [प्रोटोकॉल](</hi/gateway/protocol>)

नेटिव Windows - M2 अल्फा - 4 क्षेत्र

मुख्य CLI/Gateway फ्लो काम करते हैं, लेकिन डॉक्स अभी भी पूरे अनुभव के लिए WSL2 की अनुशंसा करते हैं और नेटिव सावधानियाँ सूचीबद्ध करते हैं।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 58%पूर्णता अल्फा - 66%आंशिक - 1

CLI 9 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

Alpha54%

Alpha64%

[अनुक्रमणिका](</hi/install>), [इंस्टॉलर](</hi/install/installer>), [Windows](</hi/platforms/windows>), [आरंभ करना](</hi/start/getting-started>), [Onboard](</hi/cli/onboard>)

Gateway प्रबंधन 11 क्षमताएँ

प्रायोगिक0%

Alpha59%

Alpha66%

[Windows](</hi/platforms/windows>), [अनुक्रमणिका](</hi/gateway>), [Gateway](</hi/cli/gateway>), [Doctor](</hi/cli/doctor>)

नेटवर्किंग 4 क्षमताएँ

प्रायोगिक0%

Alpha59%

Alpha66%

[Windows](</hi/platforms/windows>), [अनुक्रमणिका](</hi/gateway>), [Gateway](</hi/cli/gateway>)

अपडेट 4 क्षमताएँ

प्रायोगिक0%

Alpha59%

Alpha66%

[अपडेट करना](</hi/install/updating>), [CI](</hi/ci>)

Kubernetes होस्टिंग - M2 Alpha - 4 क्षेत्र

Kubernetes होस्टिंग एक अलग Kustomize-आधारित क्लस्टर डिप्लॉयमेंट पथ है। वर्तमान स्कोरिंग Kubernetes-विशिष्ट CI, ingress/TLS/NetworkPolicy पैकेजिंग, बैकअप/रीस्टोर, और उत्पादन एक्सपोज़र हार्डनिंग से जुड़े अंतरालों के साथ एक वास्तविक न्यूनतम डिप्लॉयमेंट पथ दिखाती है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फ़ा - 55%पूर्णता अल्फ़ा - 61%कोई नहीं

परिनियोजन सेटअप 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा55%

अल्फ़ा61%

[Kubernetes](</hi/install/kubernetes>), [अनुक्रमणिका](</hi/install>)

कॉन्फ़िगरेशन और सीक्रेट्स 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा55%

अल्फ़ा61%

[Kubernetes](</hi/install/kubernetes>), [सीक्रेट्स](</hi/gateway/secrets>), [परिवेश](</hi/help/environment>)

पहुँच और एक्सपोज़र 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा55%

अल्फ़ा61%

[Kubernetes](</hi/install/kubernetes>), [प्रमाणीकरण](</hi/gateway/authentication>), [रिमोट](</hi/gateway/remote>), [एक्सपोज़र रनबुक](</hi/gateway/security/exposure-runbook>)

क्लस्टर जीवनचक्र 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा55%

अल्फ़ा61%

[Kubernetes](</hi/install/kubernetes>), [अनुक्रमणिका](</hi/gateway>)

iOS app - M1 Experimental - 8 areas

आंतरिक पूर्वावलोकन / सुपर-अल्फ़ा। TestFlight और रिले-समर्थित पुश फ़्लो मौजूद हैं, लेकिन अभी तक कोई सार्वजनिक वितरण नहीं है।

कवरेज प्रयोगात्मक - 0%गुणवत्ता प्रयोगात्मक - 41%पूर्णता प्रयोगात्मक - 44%कोई नहीं

मीडिया और साझाकरण 1 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>), [कैमरा](</hi/nodes/camera>)

कैनवास और स्क्रीन 1 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>), [कैनवास](</hi/plugins/reference/canvas>)

चैट और सेशन 1 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>), [वेबचैट](</hi/web/webchat>), [प्रोटोकॉल](</hi/gateway/protocol>)

Gateway सेटअप और डायग्नोस्टिक्स 7 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>), [पेयरिंग](</hi/channels/pairing>)

वितरण 1 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>)

डिवाइस कमांड 2 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>), [प्रोटोकॉल](</hi/gateway/protocol>)

सूचनाएँ और बैकग्राउंड 1 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>), [कॉन्फ़िगरेशन](</hi/gateway/configuration>)

आवाज़ 1 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक41%

प्रयोगात्मक44%

[Ios](</hi/platforms/ios>), [बात करें](</hi/nodes/talk>)

Nix इंस्टॉल पथ - M1 प्रायोगिक - 5 क्षेत्र

वैकल्पिक इंस्टॉल प्रवाह। alpha/beta प्रमोशन से पहले अधिक स्पष्ट समर्थन आश्वासन चाहिए।

कवरेज प्रायोगिक - 0%गुणवत्ता प्रायोगिक - 41%पूर्णता प्रायोगिक - 44%कोई नहीं

इंस्टॉल हैंडऑफ़ 4 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[Nix](</hi/install/nix>), [इंडेक्स](</hi/install>), [दस्तावेज़ निर्देशिका](</hi/start/docs-directory>)

Plugin जीवनचक्र 4 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[Plugins प्रबंधित करें](</hi/plugins/manage-plugins>), [Plugin](</hi/tools/plugin>), [Nix](</hi/install/nix>)

सक्रियण और ऐप UX 7 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[Nix](</hi/install/nix>)

कॉन्फ़िग और स्थिति 7 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[Nix](</hi/install/nix>), [सेटअप](</hi/cli/setup>), [पर्यावरण](</hi/help/environment>)

सेवा रनटाइम और गार्ड 8 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[Nix](</hi/install/nix>), [सेटअप](</hi/cli/setup>), [Doctor](</hi/cli/doctor>), [अपडेट](</hi/cli/update>)

watchOS सहायक सतहें - M1 प्रायोगिक - 5 क्षेत्र

स्रोत में Watch ऐप/एक्सटेंशन सतहें हैं; सार्वजनिक दस्तावेज़ अभी इसे उपयोगकर्ता सुविधा के रूप में प्रस्तुत नहीं करते।

कवरेज प्रायोगिक - 0%गुणवत्ता प्रायोगिक - 41%पूर्णता प्रायोगिक - 44%कोई नहीं

डिलीवरी और रिकवरी 7 क्षमताएँ

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[iOS](</hi/platforms/ios>)

Exec अनुमोदन 3 क्षमताएँ

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[Exec अनुमोदन](</hi/tools/exec-approvals>), [iOS](</hi/platforms/ios>)

वितरण और सहायता 6 क्षमताएँ

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[iOS](</hi/platforms/ios>)

सूचनाएँ और जवाब 7 क्षमताएँ

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[iOS](</hi/platforms/ios>)

Watch ऐप UI 3 क्षमताएँ

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[iOS](</hi/platforms/ios>)

Linux companion app - M0 नियोजित - 5 क्षेत्र

दस्तावेज़ कहते हैं कि नेटिव Linux companion apps नियोजित हैं; Gateway आज समर्थित Linux पथ है।

कवरेज प्रायोगिक - 0%गुणवत्ता प्रायोगिक - 19%पूर्णता प्रायोगिक - 21%कोई नहीं

ऐप वितरण 3 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक19%

प्रयोगात्मक21%

[Linux](</hi/platforms/linux>), [अनुक्रमणिका](</hi/platforms>), [अनुक्रमणिका](</hi/install>)

Gateway कनेक्टिविटी 4 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक19%

प्रयोगात्मक21%

[Linux](</hi/platforms/linux>), [अनुक्रमणिका](</hi/gateway>), [पेयरिंग](</hi/gateway/pairing>), [रिमोट](</hi/gateway/remote>)

चैट और सत्र 3 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक19%

प्रयोगात्मक21%

[Linux](</hi/platforms/linux>), [प्रोटोकॉल](</hi/gateway/protocol>), [वेबचैट](</hi/web/webchat>)

डेस्कटॉप क्षमताएँ 9 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक19%

प्रयोगात्मक21%

[Linux](</hi/platforms/linux>), [Exec अनुमोदन](</hi/tools/exec-approvals>), [सीक्रेट्स](</hi/gateway/secrets>), [अनुक्रमणिका](</hi/nodes>), [Exec](</hi/tools/exec>), [बात करें](</hi/nodes/talk>), [कैमरा](</hi/nodes/camera>)

स्थिति और डायग्नोस्टिक्स 7 क्षमताएँ

प्रयोगात्मक0%

प्रयोगात्मक19%

प्रयोगात्मक21%

[Linux](</hi/platforms/linux>), [Openclaw](</hi/start/openclaw>), [Doctor](</hi/gateway/doctor>)

मूल Windows कंपैनियन ऐप - M0 नियोजित - 5 क्षेत्र

केवल नियोजित।

कवरेज प्रयोगात्मक - 0%गुणवत्ता प्रयोगात्मक - 19%पूर्णता प्रयोगात्मक - 21%कोई नहीं

इंस्टॉलेशन और अपडेट 4 क्षमताएँ

प्रायोगिक0%

प्रायोगिक19%

प्रायोगिक21%

[Windows](</hi/platforms/windows>), [इंडेक्स](</hi/install>)

Gateway कनेक्शन 3 क्षमताएँ

प्रायोगिक0%

प्रायोगिक19%

प्रायोगिक21%

[Windows](</hi/platforms/windows>), [इंडेक्स](</hi/gateway>), [पेयरिंग](</hi/gateway/pairing>), [रिमोट](</hi/gateway/remote>)

चैट सत्र 2 क्षमताएँ

प्रायोगिक0%

प्रायोगिक19%

प्रायोगिक21%

[Windows](</hi/platforms/windows>), [प्रोटोकॉल](</hi/gateway/protocol>)

स्थिति और मरम्मत 5 क्षमताएँ

प्रायोगिक0%

प्रायोगिक19%

प्रायोगिक21%

[Windows](</hi/platforms/windows>), [Doctor](</hi/gateway/doctor>), [इंडेक्स](</hi/gateway>)

डेस्कटॉप टूल और अनुमतियाँ 10 क्षमताएँ

प्रायोगिक0%

प्रायोगिक19%

प्रायोगिक21%

[Windows](</hi/platforms/windows>), [इंडेक्स](</hi/nodes>), [Exec](</hi/tools/exec>), [Exec अनुमोदन](</hi/tools/exec-approvals>), [इंडेक्स](</hi/gateway/security>)

### चैनल

Discord - M4 स्थिर - 6 क्षेत्र

गहन दस्तावेज़ और व्यापक फीचर कवरेज। वॉइस/डेलिगेशन पथों को अलग से beta/alpha के रूप में स्कोर किया जाना चाहिए।

कवरेज प्रायोगिक - 0%गुणवत्ता Beta - 73%पूर्णता स्थिर - 87%आंशिक - 4

Channel सेटअप और संचालन 10 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

Beta73%

स्थिर87%

[Discord](</hi/channels/discord>), [Discord](</hi/plugins/reference/discord>), [Fly](</hi/install/fly>), [स्लैश कमांड](</hi/tools/slash-commands>), [स्वास्थ्य](</hi/gateway/health>), [Channels](</hi/cli/channels>), [कॉन्फ़िग Channels](</hi/gateway/config-channels>)

एक्सेस और पहचान 6 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

Beta73%

स्थिर87%

[Discord](</hi/channels/discord>), [पेयरिंग](</hi/channels/pairing>), [एक्सेस समूह](</hi/channels/access-groups>), [समूह](</hi/channels/groups>)

बातचीत रूटिंग और डिलीवरी 12 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

Beta73%

स्थिर87%

[Discord](</hi/channels/discord>), [Channel रूटिंग](</hi/channels/channel-routing>), [समूह](</hi/channels/groups>), [एक्सेस समूह](</hi/channels/access-groups>), [ACP एजेंट](</hi/tools/acp-agents>), [सबएजेंट](</hi/tools/subagents>)

मीडिया और रिच सामग्री 1 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

Beta73%

स्थिर87%

[Discord](</hi/channels/discord>)

नेटिव नियंत्रण और अनुमोदन 5 क्षमताएं

प्रायोगिक0%

Beta73%

स्थिर87%

[Discord](</hi/channels/discord>), [स्लैश कमांड](</hi/tools/slash-commands>)

रीयलटाइम आवाज़ और कॉल 5 क्षमताएं

प्रायोगिक0%

Beta73%

स्थिर87%

[Discord](</hi/channels/discord>), [OpenAI](</hi/providers/openai>), [ElevenLabs](</hi/providers/elevenlabs>), [QA E2E ऑटोमेशन](</hi/concepts/qa-e2e-automation>), [कॉन्फ़िग Channels](</hi/gateway/config-channels>)

Telegram - M3 Beta - 5 क्षेत्र

मुख्य Channel नियमित उपयोग के लिए पर्याप्त परिपक्व है, लेकिन अधिक-भिन्नता वाले UX और मीडिया एज केस के लिए आवर्ती परिदृश्य प्रमाण की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता Alpha - 68%पूर्णता Beta - 78%पूर्ण - 5

चैनल सेटअप और संचालन 10 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Telegram](</hi/channels/telegram>), [कॉन्फ़िग चैनल](</hi/gateway/config-channels>), [चैनल](</hi/cli/channels>)

पहुंच और पहचान 10 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Telegram](</hi/channels/telegram>), [पेयरिंग](</hi/channels/pairing>), [एक्सेस समूह](</hi/channels/access-groups>), [समूह](</hi/channels/groups>), [मल्टी एजेंट](</hi/concepts/multi-agent>)

बातचीत रूटिंग और डिलीवरी 1 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Telegram](</hi/channels/telegram>), [समूह](</hi/channels/groups>), [मल्टी एजेंट](</hi/concepts/multi-agent>)

मीडिया और समृद्ध सामग्री 1 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Telegram](</hi/channels/telegram>), [स्थान](</hi/channels/location>)

नेटिव नियंत्रण और अनुमोदन 9 क्षमताएं / LTS-समर्थित

प्रायोगिक0%

बीटा77%

बीटा79%

[Telegram](</hi/channels/telegram>), [Exec अनुमोदन](</hi/tools/exec-approvals>), [प्रतिक्रियाएं](</hi/tools/reactions>)

Slack - M3 Beta - 5 areas

प्रथम-श्रेणी चैनल दस्तावेज़ और रूटिंग सतह। वर्कस्पेस इंस्टॉल/admin परिदृश्य स्कोरकार्ड की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फ़ा - 66%पूर्णता बीटा - 78%पूर्ण - 5

चैनल सेटअप और संचालन 10 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Slack](</hi/channels/slack>), [Slack](</hi/plugins/reference/slack>), [सीक्रेट्स](</hi/gateway/secrets>), [QA E2E स्वचालन](</hi/concepts/qa-e2e-automation>), [समस्या निवारण](</hi/channels/troubleshooting>)

पहुँच और पहचान 1 क्षमता / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Slack](</hi/channels/slack>), [पेयरिंग](</hi/channels/pairing>)

बातचीत रूटिंग और डिलीवरी 5 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Slack](</hi/channels/slack>), [बॉट लूप सुरक्षा](</hi/channels/bot-loop-protection>), [पेयरिंग](</hi/channels/pairing>)

मीडिया और समृद्ध सामग्री 1 क्षमता / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Slack](</hi/channels/slack>), [QA E2E स्वचालन](</hi/concepts/qa-e2e-automation>)

नेटिव नियंत्रण और अनुमोदन 8 क्षमताएँ / LTS-समर्थित

प्रायोगिक0%

अल्फ़ा66%

बीटा78%

[Slack](</hi/channels/slack>), [Slash कमांड](</hi/tools/slash-commands>), [निष्पादन अनुमोदन](</hi/tools/exec-approvals>)

iMessage और BlueBubbles - M3 बीटा - 5 क्षेत्र

समर्थित iMessage, साइन-इन किए हुए macOS Messages होस्ट पर imsg के माध्यम से चलता है; पुराने BlueBubbles कॉन्फ़िगरेशन के लिए माइग्रेशन आवश्यक है। macOS अनुमतियाँ, SSH रैपर, SIP/निजी API, और माइग्रेशन संबंधी सावधानियाँ स्पष्ट रखें।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फ़ा - 66%पूर्णता बीटा - 78%कोई नहीं

चैनल सेटअप और संचालन 11 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा66%

बीटा78%

[Bluebubbles Imessage](</hi/announcements/bluebubbles-imessage>), [Imessage From Bluebubbles](</hi/channels/imessage-from-bluebubbles>), [चैनल कॉन्फ़िगर करें](</hi/gateway/config-channels>), [Imessage](</hi/channels/imessage>)

पहुँच और पहचान 6 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा66%

बीटा78%

[Imessage](</hi/channels/imessage>), [Imessage From Bluebubbles](</hi/channels/imessage-from-bluebubbles>), [चैनल कॉन्फ़िगर करें](</hi/gateway/config-channels>)

वार्तालाप रूटिंग और डिलीवरी 4 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा66%

बीटा78%

[Imessage](</hi/channels/imessage>)

मीडिया और रिच कंटेंट 7 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा66%

बीटा78%

[Imessage](</hi/channels/imessage>), [Imessage From Bluebubbles](</hi/channels/imessage-from-bluebubbles>), [चैनल कॉन्फ़िगर करें](</hi/gateway/config-channels>)

नेटिव नियंत्रण और अनुमोदन 3 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा66%

बीटा78%

[Imessage](</hi/channels/imessage>)

WhatsApp - M3 बीटा - 5 क्षेत्र

कोर पथ महत्वपूर्ण और दस्तावेज़ीकृत है; अपस्ट्रीम Baileys/सेशन की अस्थिरता इसे Stable से नीचे रखती है।

कवरेज प्रयोगात्मक - 0%गुणवत्ता अल्फ़ा - 66%पूर्णता बीटा - 78%कोई नहीं

चैनल सेटअप और संचालन 5 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[WhatsApp](</hi/channels/whatsapp>), [कॉन्फ़िग चैनल](</hi/gateway/config-channels>), [WhatsApp](</hi/plugins/reference/whatsapp>), [QA E2E ऑटोमेशन](</hi/concepts/qa-e2e-automation>), [Doctor](</hi/gateway/doctor>)

एक्सेस और पहचान 7 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[WhatsApp](</hi/channels/whatsapp>), [कॉन्फ़िग चैनल](</hi/gateway/config-channels>), [QA E2E ऑटोमेशन](</hi/concepts/qa-e2e-automation>), [पेयरिंग](</hi/channels/pairing>)

वार्तालाप रूटिंग और डिलीवरी 4 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[WhatsApp](</hi/channels/whatsapp>), [समूह संदेश](</hi/channels/group-messages>)

मीडिया और समृद्ध सामग्री 2 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[WhatsApp](</hi/channels/whatsapp>)

नेटिव नियंत्रण और स्वीकृतियां 2 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[WhatsApp](</hi/channels/whatsapp>)

Matrix - M2 अल्फा - 6 क्षेत्र

बंडल किए गए plugin के माध्यम से समर्थित। ब्रिज, प्रमाणीकरण, और रूम लाइफसाइकल स्कोरकार्ड की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 60%पूर्णता अल्फा - 67%कोई नहीं

चैनल सेटअप और संचालन 5 क्षमताएँ

प्रायोगिक0%

अल्फ़ा60%

अल्फ़ा67%

[Matrix](</hi/channels/matrix>), [Matrix माइग्रेशन](</hi/channels/matrix-migration>)

पहुँच और पहचान 7 क्षमताएँ

प्रायोगिक0%

अल्फ़ा60%

अल्फ़ा67%

[Matrix](</hi/channels/matrix>), [समूह](</hi/channels/groups>), [बॉट लूप सुरक्षा](</hi/channels/bot-loop-protection>)

वार्तालाप रूटिंग और डिलीवरी 1 क्षमता

प्रायोगिक0%

अल्फ़ा60%

अल्फ़ा67%

[Matrix](</hi/channels/matrix>)

मीडिया और समृद्ध सामग्री 1 क्षमता

प्रायोगिक0%

अल्फ़ा60%

अल्फ़ा67%

[Matrix](</hi/channels/matrix>)

नेटिव नियंत्रण और अनुमोदन 6 क्षमताएँ

प्रायोगिक0%

अल्फ़ा60%

अल्फ़ा67%

[Matrix](</hi/channels/matrix>)

एन्क्रिप्शन और सत्यापन 3 क्षमताएँ

प्रायोगिक0%

अल्फ़ा60%

अल्फ़ा67%

[Matrix](</hi/channels/matrix>), [Matrix माइग्रेशन](</hi/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 areas

दस्तावेजीकृत चैनल, लेकिन एंटरप्राइज़/एडमिन सेटअप परिपक्वता जोखिम बढ़ाता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फ़ा - 59%पूर्णता अल्फ़ा - 66%कोई नहीं

चैनल सेटअप और संचालन 16 क्षमताएं

प्रायोगिक0%

अल्फ़ा59%

अल्फ़ा66%

[Googlechat](</hi/channels/googlechat>), [Googlechat](</hi/plugins/reference/googlechat>), [कॉन्फ़िग चैनल](</hi/gateway/config-channels>), [विज़ार्ड CLI संदर्भ](</hi/start/wizard-cli-reference>), [सीक्रेट्स](</hi/gateway/secrets>), [Secretref क्रेडेंशियल सरफेस](</hi/reference/secretref-credential-surface>), [हेल्थ](</hi/gateway/health>), [Plugin इन्वेंटरी](</hi/plugins/plugin-inventory>), [इंडेक्स](</hi/channels>)

पहुंच और पहचान 11 क्षमताएं

प्रायोगिक0%

अल्फ़ा59%

अल्फ़ा66%

[Googlechat](</hi/channels/googlechat>), [पेयरिंग](</hi/channels/pairing>), [एक्सेस समूह](</hi/channels/access-groups>), [कॉन्फ़िग चैनल](</hi/gateway/config-channels>), [बॉट लूप सुरक्षा](</hi/channels/bot-loop-protection>), [चैनल रूटिंग](</hi/channels/channel-routing>)

वार्तालाप रूटिंग और डिलीवरी 1 क्षमता

प्रायोगिक0%

अल्फ़ा59%

अल्फ़ा66%

[Googlechat](</hi/channels/googlechat>), [बॉट लूप सुरक्षा](</hi/channels/bot-loop-protection>), [एक्सेस समूह](</hi/channels/access-groups>), [चैनल रूटिंग](</hi/channels/channel-routing>)

मीडिया और समृद्ध सामग्री 1 क्षमता

प्रायोगिक0%

अल्फ़ा59%

अल्फ़ा66%

[Googlechat](</hi/channels/googlechat>), [संदेश](</hi/cli/message>), [मीडिया समझ](</hi/nodes/media-understanding>), [Secretref क्रेडेंशियल सरफेस](</hi/reference/secretref-credential-surface>)

नेटिव नियंत्रण और अनुमोदन 16 क्षमताएं

प्रायोगिक0%

अल्फ़ा59%

अल्फ़ा66%

[Googlechat](</hi/channels/googlechat>), [संदेश](</hi/cli/message>), [मीडिया समझ](</hi/nodes/media-understanding>), [Secretref क्रेडेंशियल सरफेस](</hi/reference/secretref-credential-surface>), [प्रतिक्रियाएं](</hi/tools/reactions>), [स्लैश कमांड](</hi/tools/slash-commands>), [कॉन्फ़िग एजेंट](</hi/gateway/config-agents>), [संदेश जीवनचक्र रीफ़ैक्टर](</hi/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 अल्फ़ा - 5 क्षेत्र

एंटरप्राइज़ प्रमाणीकरण/एडमिन प्रवाहों के लिए स्पष्ट परिदृश्य प्रमाण चाहिए।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फ़ा - 59%पूर्णता अल्फ़ा - 66%कोई नहीं

चैनल सेटअप और संचालन 9 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Msteams](</hi/channels/msteams>), [Msteams](</hi/plugins/reference/msteams>), [कॉन्फ़िग चैनल](</hi/gateway/config-channels>), [स्वास्थ्य](</hi/gateway/health>)

पहुँच और पहचान 9 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Msteams](</hi/channels/msteams>), [पेयरिंग](</hi/channels/pairing>), [पहुँच समूह](</hi/channels/access-groups>)

वार्तालाप रूटिंग और डिलीवरी 5 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Msteams](</hi/channels/msteams>), [समूह](</hi/channels/groups>), [चैनल रूटिंग](</hi/channels/channel-routing>)

मीडिया और समृद्ध सामग्री 5 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Msteams](</hi/channels/msteams>)

नेटिव नियंत्रण और अनुमोदन 5 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Msteams](</hi/channels/msteams>), [उन्नत Exec अनुमोदन](</hi/tools/exec-approvals-advanced>)

Signal - M2 अल्फा - 5 क्षेत्र

समर्थित चैनल दस्तावेज़ मौजूद हैं; अधिक मजबूत इंस्टॉल और पुनःकनेक्ट प्रमाण की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 59%पूर्णता अल्फा - 66%कोई नहीं

चैनल सेटअप और संचालन 7 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Signal](</hi/channels/signal>), [Signal](</hi/plugins/reference/signal>)

पहुँच और पहचान 6 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Signal](</hi/channels/signal>)

वार्तालाप रूटिंग और डिलीवरी 1 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Signal](</hi/channels/signal>)

मीडिया और रिच कंटेंट 7 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Signal](</hi/channels/signal>)

नेटिव नियंत्रण और अनुमोदन 3 क्षमताएँ

प्रायोगिक0%

अल्फा59%

अल्फा66%

[Signal](</hi/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regional channels - M2 Alpha - 4 areas

महत्वपूर्ण क्षेत्रीय कवरेज, लेकिन सार्वजनिक समर्थन स्तर को खाता प्रकार, अपस्ट्रीम अनुमोदन, और मेंटेनर प्रमाण के अनुसार कैलिब्रेट किया जाना चाहिए।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 55%पूर्णता अल्फा - 58%कोई नहीं

चैनल सेटअप और संचालन 6 क्षमताएँ

प्रायोगिक0%

अल्फ़ा61%

अल्फ़ा68%

[अनुक्रमणिका](</hi/channels>), [पेयरिंग](</hi/channels/pairing>), [Feishu](</hi/plugins/reference/feishu>), [आर्किटेक्चर आंतरिक विवरण](</hi/plugins/architecture-internals>)

पहुँच और पहचान 1 क्षमता

प्रायोगिक0%

अल्फ़ा53%

अल्फ़ा54%

कोई लिंक किए गए दस्तावेज़ नहीं

वार्तालाप रूटिंग और डिलीवरी 1 क्षमता

प्रायोगिक0%

अल्फ़ा53%

अल्फ़ा54%

कोई लिंक किए गए दस्तावेज़ नहीं

मीडिया और समृद्ध सामग्री 1 क्षमता

प्रायोगिक0%

अल्फ़ा53%

अल्फ़ा54%

कोई लिंक किए गए दस्तावेज़ नहीं

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 अल्फ़ा - 4 क्षेत्र

समर्थित सतहें मौजूद हैं, लेकिन परिपक्वता संभवतः अपस्ट्रीम और मेंटेनर कवरेज के अनुसार बदलती है। बाद में अलग-अलग स्कोर करें।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फ़ा - 53%पूर्णता अल्फ़ा - 54%कोई नहीं

चैनल सेटअप और संचालन 1 क्षमताएँ

प्रायोगिक0%

अल्फ़ा53%

अल्फ़ा54%

कोई लिंक किए गए दस्तावेज़ नहीं

पहुँच और पहचान 1 क्षमताएँ

प्रायोगिक0%

अल्फ़ा53%

अल्फ़ा54%

कोई लिंक किए गए दस्तावेज़ नहीं

बातचीत रूटिंग और डिलीवरी 1 क्षमताएँ

प्रायोगिक0%

अल्फ़ा53%

अल्फ़ा54%

कोई लिंक किए गए दस्तावेज़ नहीं

मीडिया और रिच सामग्री 1 क्षमताएँ

प्रायोगिक0%

अल्फ़ा53%

अल्फ़ा54%

कोई लिंक किए गए दस्तावेज़ नहीं

वॉइस कॉल चैनल - M1 प्रायोगिक - 5 क्षेत्र

जटिल रीयलटाइम व्यवहार वाला वैकल्पिक/Plugin पथ। सार्वजनिक बीटा से पहले परिदृश्य स्कोरकार्ड की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता प्रायोगिक - 41%पूर्णता प्रायोगिक - 44%कोई नहीं

चैनल सेटअप और संचालन 2 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[Voicecall](</hi/cli/voicecall>), [वॉयस कॉल](</hi/plugins/voice-call>), [प्रोटोकॉल](</hi/gateway/protocol>)

पहुंच और पहचान 1 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[वॉयस कॉल](</hi/plugins/voice-call>), [Voicecall](</hi/cli/voicecall>)

वार्तालाप रूटिंग और डिलीवरी 1 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[वॉयस कॉल](</hi/plugins/voice-call>)

मीडिया और समृद्ध सामग्री 2 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[वॉयस कॉल](</hi/plugins/voice-call>), [Plugin इन्वेंटरी](</hi/plugins/plugin-inventory>)

रीयलटाइम वॉइस और कॉल 2 क्षमताएं

प्रायोगिक0%

प्रायोगिक41%

प्रायोगिक44%

[वॉयस कॉल](</hi/plugins/voice-call>)

### प्रदाता और टूल

ब्राउज़र ऑटोमेशन, exec, और सैंडबॉक्स टूल - M3 बीटा - 3 क्षेत्र

मुख्य टूल दस्तावेजीकृत हैं, लेकिन होस्ट सुरक्षा और अनुमति UX सक्रिय स्कोरकार्ड समीक्षा के अंतर्गत बने रहने चाहिए।

कवरेज प्रायोगिक - 21%गुणवत्ता बीटा - 75%पूर्णता बीटा - 79%आंशिक - 2

ब्राउज़र स्वचालन 8 क्षमताएँ

प्रयोगात्मक13%

बीटा79%

बीटा79%

[ब्राउज़र नियंत्रण](</hi/tools/browser-control>), [परीक्षण](</hi/help/testing>), [ब्राउज़र](</hi/tools/browser>), [अनुक्रमणिका](</hi/gateway/security>), [ऑडिट जाँचें](</hi/gateway/security/audit-checks>)

टूल आह्वान और निष्पादन 6 क्षमताएँ / LTS-समर्थित

अल्फा50%

बीटा79%

बीटा79%

[Exec](</hi/tools/exec>), [पृष्ठभूमि प्रक्रिया](</hi/gateway/background-process>), [टूल्स Invoke Http API](</hi/gateway/tools-invoke-http-api>), [ऑपरेटर स्कोप](</hi/gateway/operator-scopes>), [प्रोटोकॉल](</hi/gateway/protocol>), [Exec अनुमोदन](</hi/tools/exec-approvals>), [उन्नत Exec अनुमोदन](</hi/tools/exec-approvals-advanced>), [उन्नताधिकार प्राप्त](</hi/tools/elevated>)

सैंडबॉक्स और टूल नीति 6 क्षमताएँ / LTS-समर्थित

प्रयोगात्मक0%

अल्फा68%

बीटा79%

[सैंडबॉक्सिंग](</hi/gateway/sandboxing>), [सैंडबॉक्स बनाम टूल नीति बनाम उन्नताधिकार प्राप्त](</hi/gateway/sandbox-vs-tool-policy-vs-elevated>), [मल्टी एजेंट सैंडबॉक्स टूल्स](</hi/tools/multi-agent-sandbox-tools>), [Codex हार्नेस संदर्भ](</hi/plugins/codex-harness-reference>), [कॉन्फ़िग टूल्स](</hi/gateway/config-tools>)

OpenAI और Codex प्रदाता पथ - M3 बीटा - 5 क्षेत्र

गहन दस्तावेज़, OAuth/सदस्यता पथ, रीयलटाइम आवाज़, इमेज, और संगतता व्यवहार। रिलीज़-स्कोरकार्ड प्रमाण के बिना प्रदाता में बार-बार बदलाव इसे स्थिर होने से रोकता है।

कवरेज प्रयोगात्मक - 26%गुणवत्ता बीटा - 74%पूर्णता बीटा - 79%आंशिक - 3

मॉडल और प्रमाणीकरण 6 क्षमताएँ / LTS-समर्थित

प्रायोगिक44%

Beta79%

Beta79%

[Openai](</hi/providers/openai>), [Codex Harness](</hi/plugins/codex-harness>), [मॉडल](</hi/concepts/models>), [Oauth](</hi/concepts/oauth>), [Codex Harness संदर्भ](</hi/plugins/codex-harness-reference>), [प्रमाणीकरण निगरानी](</hi/gateway/authentication>)

Responses और टूल संगतता 4 क्षमताएँ / LTS-समर्थित

प्रायोगिक40%

Beta79%

Beta79%

[Openai](</hi/providers/openai>), [Openresponses Http Api](</hi/gateway/openresponses-http-api>), [Openai Http Api](</hi/gateway/openai-http-api>), [Codex Native Plugins](</hi/plugins/codex-native-plugins>)

मूल Codex Harness 2 क्षमताएँ / LTS-समर्थित

प्रायोगिक44%

Beta79%

Beta79%

[Codex Harness](</hi/plugins/codex-harness>), [Codex Harness रनटाइम](</hi/plugins/codex-harness-runtime>), [Codex Harness संदर्भ](</hi/plugins/codex-harness-reference>), [Codex Native Plugins](</hi/plugins/codex-native-plugins>)

छवि और मल्टीमोडल इनपुट 2 क्षमताएँ

प्रायोगिक0%

Alpha67%

Beta79%

[Openai](</hi/providers/openai>), [छवि निर्माण](</hi/tools/image-generation>), [छवियाँ](</hi/nodes/images>)

वॉइस और रीयलटाइम ऑडियो 2 क्षमताएँ

प्रायोगिक0%

Alpha67%

Beta79%

[Openai](</hi/providers/openai>), [Discord](</hi/channels/discord>), [वॉइस कॉल](</hi/plugins/voice-call>)

वेब खोज टूल - M3 Beta - 4 क्षेत्र

कई प्रदाता और दस्तावेज़ मौजूद हैं। प्रत्येक प्रदाता परिवार के लिए कोटा/त्रुटि/SSRF प्रमाण की आवश्यकता है।

कवरेज प्रायोगिक - 9%गुणवत्ता Beta - 74%पूर्णता Beta - 79%कोई नहीं

खोज प्रदाता 19 क्षमताएं

प्रायोगिक11%

बीटा79%

बीटा79%

[Web](</hi/tools/web>), [Brave Search](</hi/tools/brave-search>), [Tavily](</hi/tools/tavily>), [Exa Search](</hi/tools/exa-search>), [Firecrawl](</hi/tools/firecrawl>), [Perplexity Search](</hi/tools/perplexity-search>), [Duckduckgo Search](</hi/tools/duckduckgo-search>), [Searxng Search](</hi/tools/searxng-search>), [Gemini Search](</hi/tools/gemini-search>), [Grok Search](</hi/tools/grok-search>), [Kimi Search](</hi/tools/kimi-search>), [Minimax Search](</hi/tools/minimax-search>), [Ollama Search](</hi/tools/ollama-search>), [Sdk Subpaths](</hi/plugins/sdk-subpaths>), [Sdk Overview](</hi/plugins/sdk-overview>), [Manifest](</hi/plugins/manifest>)

सेटअप और डायग्नोस्टिक्स 9 क्षमताएं

प्रायोगिक0%

अल्फा68%

बीटा79%

[Web](</hi/tools/web>), [Web Fetch](</hi/tools/web-fetch>), [Faq](</hi/help/faq>), [Api Usage Costs](</hi/reference/api-usage-costs>), [Brave Search](</hi/tools/brave-search>), [Perplexity Search](</hi/tools/perplexity-search>), [Tavily](</hi/tools/tavily>), [Firecrawl](</hi/tools/firecrawl>)

नेटवर्क सुरक्षा 4 क्षमताएं

प्रायोगिक0%

अल्फा68%

बीटा79%

[Web](</hi/tools/web>), [Web Fetch](</hi/tools/web-fetch>), [Firecrawl](</hi/tools/firecrawl>), [Searxng Search](</hi/tools/searxng-search>)

टूल उपलब्धता और Fetch 11 क्षमताएं

प्रायोगिक25%

बीटा79%

बीटा79%

[Config Tools](</hi/gateway/config-tools>), [Web Fetch](</hi/tools/web-fetch>), [Web](</hi/tools/web>), [Faq](</hi/help/faq>)

Anthropic प्रदाता पथ - M3 बीटा - 5 क्षेत्र

प्रथम-श्रेणी मॉडल प्रदाता। आवर्ती प्रमाणीकरण/कैटलॉग/टूल-कॉल परिदृश्य प्रमाण की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता बीटा - 71%पूर्णता बीटा - 78%कोई नहीं

प्रदाता प्रमाणीकरण और पुनर्प्राप्ति 9 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[Anthropic](</hi/providers/anthropic>), [Doctor](</hi/gateway/doctor>), [कॉन्फ़िगरेशन उदाहरण](</hi/gateway/configuration-examples>), [समस्या निवारण](</hi/gateway/troubleshooting>), [प्रॉम्प्ट कैशिंग](</hi/reference/prompt-caching>)

मॉडल और रनटाइम चयन 10 क्षमताएं

प्रायोगिक0%

बीटा78%

बीटा79%

[Anthropic](</hi/providers/anthropic>), [कॉन्फ़िग एजेंट](</hi/gateway/config-agents>), [मॉडल](</hi/concepts/models>), [CLI बैकएंड](</hi/gateway/cli-backends>)

अनुरोध ट्रांसपोर्ट और टर्न सिमैंटिक्स 10 क्षमताएं

प्रायोगिक0%

बीटा77%

बीटा79%

[Anthropic](</hi/providers/anthropic>), [प्रॉम्प्ट कैशिंग](</hi/reference/prompt-caching>), [समस्या निवारण](</hi/gateway/troubleshooting>), [CLI बैकएंड](</hi/gateway/cli-backends>), [मॉडल प्रदाता](</hi/concepts/model-providers>)

प्रॉम्प्ट कैश और संदर्भ 5 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[Anthropic](</hi/providers/anthropic>), [प्रॉम्प्ट कैशिंग](</hi/reference/prompt-caching>), [समस्या निवारण](</hi/gateway/troubleshooting>), [Heartbeat](</hi/gateway/heartbeat>)

मीडिया इनपुट 4 क्षमताएं

प्रायोगिक0%

अल्फा66%

बीटा78%

[Anthropic](</hi/providers/anthropic>), [कॉन्फ़िग एजेंट](</hi/gateway/config-agents>)

Google प्रदाता पथ - M3 बीटा - 5 क्षेत्र

मॉडल और रीयलटाइम सतहों वाला प्रथम-श्रेणी प्रदाता। अलग Live/Talk स्कोरिंग की आवश्यकता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 66%पूर्णता बीटा - 78%कोई नहीं

प्रदाता सेटअप और क्रेडेंशियल्स 10 क्षमताएँ

प्रायोगिक0%

अल्फा66%

बीटा78%

[Google](</hi/providers/google>), [मॉडल प्रदाता](</hi/concepts/model-providers>)

मॉडल रूटिंग और एंडपॉइंट्स 10 क्षमताएँ

प्रायोगिक0%

अल्फा66%

बीटा78%

[Google](</hi/providers/google>), [मॉडल प्रदाता](</hi/concepts/model-providers>), [Google](</hi/plugins/reference/google>), [Gemini Search](</hi/tools/gemini-search>)

प्रत्यक्ष Gemini रनटाइम 9 क्षमताएँ

प्रायोगिक0%

अल्फा66%

बीटा78%

[Google](</hi/providers/google>), [मॉडल प्रदाता](</hi/concepts/model-providers>), [FAQ मॉडल](</hi/help/faq-models>), [लाइव परीक्षण](</hi/help/testing-live>)

मीडिया, खोज, और रीयलटाइम 10 क्षमताएँ

प्रायोगिक0%

अल्फा66%

बीटा78%

[Google](</hi/plugins/reference/google>), [Google](</hi/providers/google>)

प्रॉम्प्ट कैशिंग 5 क्षमताएँ

प्रायोगिक0%

अल्फा66%

बीटा78%

[प्रॉम्प्ट कैशिंग](</hi/reference/prompt-caching>), [Google](</hi/providers/google>), [मॉडल प्रदाता](</hi/concepts/model-providers>), [टोकन उपयोग](</hi/reference/token-use>)

OpenRouter प्रदाता पथ - M3 बीटा - 4 क्षेत्र

एकीकृत प्रदाता पथ दस्तावेजीकृत और उपयोगी है, लेकिन मॉडल-विशिष्ट व्यवहार अलग-अलग होता है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 66%पूर्णता बीटा - 78%कोई नहीं

प्रदाता सेटअप और प्रमाणीकरण 14 क्षमताएँ

प्रयोगात्मक0%

अल्फा66%

बीटा78%

[Openrouter](</hi/providers/openrouter>), [मॉडल प्रदाता](</hi/concepts/model-providers>), [कॉन्फ़िगर करें](</hi/cli/configure>), [प्रमाणीकरण](</hi/gateway/authentication>), [पर्यावरण](</hi/help/environment>), [मॉडल](</hi/cli/models>), [मॉडल](</hi/concepts/models>)

चैट रनटाइम और सामान्यीकरण 15 क्षमताएँ

प्रयोगात्मक0%

अल्फा66%

बीटा78%

[Openrouter](</hi/providers/openrouter>), [मॉडल प्रदाता](</hi/concepts/model-providers>), [प्रॉम्प्ट कैशिंग](</hi/reference/prompt-caching>)

प्रदाता पुनर्प्राप्ति और निदान 5 क्षमताएँ

प्रयोगात्मक0%

अल्फा66%

बीटा78%

[मॉडल फेलओवर](</hi/concepts/model-failover>), [Openrouter](</hi/providers/openrouter>), [मॉडल](</hi/cli/models>)

मीडिया जनरेशन और वाणी 7 क्षमताएँ

प्रयोगात्मक0%

अल्फा66%

बीटा78%

[Openrouter](</hi/providers/openrouter>), [छवि जनरेशन](</hi/tools/image-generation>), [संगीत जनरेशन](</hi/tools/music-generation>), [मीडिया अवलोकन](</hi/tools/media-overview>), [वीडियो जनरेशन](</hi/tools/video-generation>), [Tts](</hi/tools/tts>)

छवि, वीडियो, और संगीत जनरेशन टूल - M2 अल्फा - 5 क्षेत्र

प्रदाताओं में क्षमता मौजूद है, लेकिन प्रति-प्रदाता प्रमाण के बिना बीटा के लिए गुणवत्ता, विलंबता, और पैरामीटर संगतता में बहुत अधिक भिन्नता है।

कवरेज प्रयोगात्मक - 0%गुणवत्ता अल्फा - 61%पूर्णता अल्फा - 68%कोई नहीं

मीडिया रूटिंग और खोज 4 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[कॉन्फ़िग एजेंट](</hi/gateway/config-agents>), [इमेज जनरेशन](</hi/tools/image-generation>), [वीडियो जनरेशन](</hi/tools/video-generation>), [संगीत जनरेशन](</hi/tools/music-generation>)

कार्य जीवनचक्र और डिलीवरी 12 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[मीडिया अवलोकन](</hi/tools/media-overview>), [इमेज जनरेशन](</hi/tools/image-generation>), [वीडियो जनरेशन](</hi/tools/video-generation>), [संगीत जनरेशन](</hi/tools/music-generation>)

इमेज जनरेशन 9 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[इमेज जनरेशन](</hi/tools/image-generation>), [अनुमान](</hi/cli/infer>), [मीडिया अवलोकन](</hi/tools/media-overview>)

वीडियो जनरेशन 11 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[वीडियो जनरेशन](</hi/tools/video-generation>), [Runway](</hi/providers/runway>), [Pixverse](</hi/providers/pixverse>), [Fal](</hi/providers/fal>), [Openrouter](</hi/providers/openrouter>)

संगीत जनरेशन 6 क्षमताएँ

प्रायोगिक0%

अल्फा61%

अल्फा68%

[संगीत जनरेशन](</hi/tools/music-generation>)

स्थानीय मॉडल प्रदाता: Ollama, vLLM, SGLang, LM Studio - M2 अल्फा - 5 क्षेत्र

उपयोगी और दस्तावेजीकृत, लेकिन परिवेश में भिन्नता अधिक है।

कवरेज प्रायोगिक - 0%गुणवत्ता अल्फा - 61%पूर्णता अल्फा - 68%कोई नहीं

Provider सेटअप, Lifecycle, और Diagnostics 12 क्षमताएं

प्रायोगिक0%

Alpha61%

Alpha68%

[स्थानीय Models](</hi/gateway/local-models>), [Lmstudio](</hi/providers/lmstudio>), [Ollama](</hi/providers/ollama>), [Vllm](</hi/providers/vllm>), [स्थानीय Model सेवाएं](</hi/gateway/local-model-services>), [Config Agents](</hi/gateway/config-agents>), [समस्या निवारण](</hi/gateway/troubleshooting>), [Doctor](</hi/gateway/doctor>)

Native Provider Plugins 10 क्षमताएं

प्रायोगिक0%

Alpha61%

Alpha68%

[Ollama](</hi/providers/ollama>), [Lmstudio](</hi/providers/lmstudio>)

OpenAI-संगत Runtime संगतता 8 क्षमताएं

प्रायोगिक0%

Alpha61%

Alpha68%

[Vllm](</hi/providers/vllm>), [Sglang](</hi/providers/sglang>), [स्थानीय Models](</hi/gateway/local-models>), [Lmstudio](</hi/providers/lmstudio>)

स्थानीय Memory और Embeddings 5 क्षमताएं

प्रायोगिक0%

Alpha61%

Alpha68%

[Memory](</hi/concepts/memory>), [Doctor](</hi/gateway/doctor>)

नेटवर्क सुरक्षा और Prompt नियंत्रण 2 क्षमताएं

प्रायोगिक0%

Alpha61%

Alpha68%

[इंडेक्स](</hi/gateway/security>), [Config Tools](</hi/gateway/config-tools>), [स्थानीय Models](</hi/gateway/local-models>)

लॉन्ग-टेल hosted providers - M2 Alpha - 3 क्षेत्र

कई docs/reference पेज मौजूद हैं; स्कोर provider metadata और live smoke coverage से जनरेट किया जाना चाहिए।

कवरेज प्रयोगात्मक - 0%गुणवत्ता अल्फ़ा - 61%पूर्णता अल्फ़ा - 68%कोई नहीं

होस्ट किए गए LLM प्रदाता 12 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा61%

अल्फ़ा68%

[सूची](</hi/providers>), [मॉडल प्रदाता](</hi/concepts/model-providers>), [लाइव परीक्षण](</hi/help/testing-live>), [ऑनबोर्ड](</hi/cli/onboard>)

होस्ट किए गए मीडिया प्रदाता 8 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा61%

अल्फ़ा68%

[मैनिफेस्ट](</hi/plugins/manifest>), [लाइव परीक्षण](</hi/help/testing-live>), [सूची](</hi/providers>)

प्रदाता संचालन 12 क्षमताएँ

प्रयोगात्मक0%

अल्फ़ा61%

अल्फ़ा68%

[सूची](</hi/providers>), [मॉडल प्रदाता](</hi/concepts/model-providers>), [मैनिफेस्ट](</hi/plugins/manifest>), [लाइव परीक्षण](</hi/help/testing-live>), [मॉडल](</hi/cli/models>)

Was this useful?YesNo

Open issue